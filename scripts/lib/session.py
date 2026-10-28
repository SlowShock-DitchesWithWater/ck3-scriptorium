# -*- coding: utf-8 -*-
"""站点会话管理：过反爬盾、cookie 导出/加载、限速的 api.php 访问。

背景（已核查事实 + 2026-10-22 实测补充）：
- ck3.paradoxwikis.com 有 JS 反爬盾（Fastly Client Challenge，资源前缀 /_fs-ch-*）。
- 实测结论：盾放行不依赖 cookie——过盾浏览器与 requests 的差别在
  TLS/HTTP2 指纹。用 CDP Network.getAllCookies 导出浏览器全部 cookie
  （含 httpOnly、父域）后，requests 仍只拿到验证页；浏览器内访问 api.php
  则始终正常。因此本模块采用双通道策略：
    1) 首选 requests + 已导出 cookie（工单要求的架构；盾按 IP 信誉
       放行的时间窗内可用）；
    2) 请求被盾拦截时，回退到"过盾浏览器内 fetch api.php"通道，
       浏览器持有完整会话上下文，取回原始响应体文本。
  两条通道对站点发出的每个请求都遵守 Crawl-delay >= 15 秒。
- robots.txt 无 Disallow，仅 Crawl-delay: 15。

对外主接口：
- api_get_text(params) -> str   原始响应体文本（raw/ 存档必须用它）
- api_get(params) -> dict       解析后的 JSON
- pass_shield()                 手动过盾并导出 cookie（正常流程无需单独调用）
"""
import atexit
import json
import os
import time
import urllib.parse
from typing import Any

import requests

from . import config

# 反爬盾验证页的特征串（出现任意一条即判定为"被盾拦截"）。
# 全部小写，与被检测文本的小写形式比较。
CHALLENGE_MARKERS = (
    "client challenge",        # Fastly 盾验证页 <title>（本站实测）
    "_fs-ch",                  # Fastly 盾静态资源路径前缀（本站实测）
    "just a moment",           # Cloudflare 五秒盾
    "cf-chl",                  # Cloudflare 挑战脚本/表单字段前缀
    "challenge-platform",      # 同上
    "checking your browser",   # 常见 JS 盾提示
    "attention required",      # 通用拦截页
    "enable javascript and cookies",  # 通用盾提示
)

# 过盾等待参数：真实浏览器打开首页后盾通常数秒内自动放行
SHIELD_PASS_TIMEOUT_SECONDS = 120.0
SHIELD_PASS_POLL_SECONDS = 2.0

# cookie 文件有效期：超过则主动重新过盾（盾会话 cookie 一般寿命更长，这里保守取 12 小时）
COOKIE_MAX_AGE_SECONDS = 12 * 3600.0

# 浏览器 fetch 通道的脚本超时（大页面响应体较大，留足余量）
BROWSER_FETCH_TIMEOUT_SECONDS = 120.0

# 模块级持有的过盾浏览器（懒创建；进程退出时统一关闭）
_browser_driver = None
# 本进程内 requests 通道是否已被盾拦过（拦过一次即后续直接走浏览器通道，
# 避免每个 API 调用白付一次 15 秒 crawl-delay + 一次被拦请求）
_requests_transport_dead = False


def _log(msg: str) -> None:
    """统一带前缀的日志输出（方便在管线日志里区分来源）。"""
    print(f"[session] {msg}", flush=True)


def looks_like_challenge(text: str) -> bool:
    """判断响应/页面文本是否是反爬盾验证页而非正常内容。"""
    lowered = text[:20000].lower()  # 只看开头即可，避免大页面全文扫描
    return any(marker in lowered for marker in CHALLENGE_MARKERS)


def wait_crawl_delay() -> float:
    """阻塞等待直至距上次已记录请求 >= MIN_CRAWL_DELAY_SECONDS。

    时间戳持久化在 STATE_DIR/last_request.txt，跨进程/跨阶段生效，
    requests 通道与浏览器 fetch 通道共用同一记账。
    返回实际睡眠的秒数（用于日志与测试）。
    """
    config.ensure_dirs()
    last = None
    try:
        raw = config.LAST_REQUEST_PATH.read_text(encoding="utf-8").strip()
        last = float(raw)
    except (OSError, ValueError):
        last = None

    sleep_for = 0.0
    if last is not None:
        # 上限保护：单次睡眠封顶 5 分钟，避免时钟异常导致死等
        sleep_for = min(config.MIN_CRAWL_DELAY_SECONDS - (time.time() - last),
                        300.0)
        if sleep_for > 0:
            _log(f"crawl-delay：还需等待 {sleep_for:.1f} 秒（下限 "
                 f"{config.MIN_CRAWL_DELAY_SECONDS:.0f}s，robots.txt 要求，不可配置更小）")
            time.sleep(sleep_for)
    _mark_request()
    return sleep_for


def _mark_request() -> None:
    """记录"刚刚发出一次请求"的时间戳（原子写，避免并行进程写坏）。"""
    tmp = config.LAST_REQUEST_PATH.with_suffix(".tmp")
    tmp.write_text(str(time.time()), encoding="utf-8")
    os.replace(tmp, config.LAST_REQUEST_PATH)


def _cookies_fresh() -> bool:
    """已导出的 cookie 文件是否存在且未过自设有效期。"""
    if not config.COOKIE_PATH.is_file():
        return False
    age = time.time() - config.COOKIE_PATH.stat().st_mtime
    return age < COOKIE_MAX_AGE_SECONDS


# ---------------------------------------------------------------- 浏览器通道

def _get_browser():
    """懒创建过盾浏览器：打开站点首页 → 等盾放行 → 常驻进程内复用。"""
    global _browser_driver
    if _browser_driver is not None:
        return _browser_driver
    # Selenium 在函数内导入：让不需要过盾的阶段（clean 等）无需装浏览器
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    _log("启动 Chrome 真实浏览器过盾（有头模式，盾会检测 headless）…")
    opts = Options()
    opts.add_argument("--start-maximized")
    _browser_driver = webdriver.Chrome(options=opts)
    atexit.register(close_browser)
    _wait_shield_pass(_browser_driver)
    _export_cookies(_browser_driver)
    return _browser_driver


def _wait_shield_pass(driver) -> None:
    """在当前浏览器里等待盾放行：页面不含盾特征且出现 MediaWiki 标志。"""
    driver.get(config.SITE_ORIGIN + "/")
    deadline = time.time() + SHIELD_PASS_TIMEOUT_SECONDS
    while time.time() < deadline:
        src = driver.page_source or ""
        if not looks_like_challenge(src) and (
                'id="mw-navigation"' in src or "mw-body" in src):
            return
        time.sleep(SHIELD_PASS_POLL_SECONDS)
    raise RuntimeError(
        f"过盾超时：浏览器页面在 {SHIELD_PASS_TIMEOUT_SECONDS:.0f}s 内未出现正常 wiki 内容")


def _export_cookies(driver) -> None:
    """导出会话 cookie 为本地 JSON（原子写：临时文件 + os.replace）。

    说明：本站盾的放行标记实测不在 cookie 里（见模块头注释），导出 cookie
    主要是满足会话复用契约与 Analytical/Consent cookie 的携带；requests
    通道能否过盾取决于站点侧 IP/指纹信誉。
    """
    cookies = driver.get_cookies()
    if not cookies:
        raise RuntimeError("过盾后未取到任何 cookie")
    tmp = config.COOKIE_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(cookies, ensure_ascii=False, indent=2),
                   encoding="utf-8")
    os.replace(tmp, config.COOKIE_PATH)
    _log(f"过盾成功，已导出 {len(cookies)} 个 cookie 到 {config.COOKIE_PATH}")


def pass_shield() -> None:
    """用 Selenium 真实浏览器访问站点首页过盾，导出会话 cookie 为 JSON。"""
    driver = _get_browser()  # 已有常驻浏览器时只是复用并重新校验放行
    _wait_shield_pass(driver)
    _export_cookies(driver)


def close_browser() -> None:
    """关闭常驻过盾浏览器（幂等；由 atexit 兜底调用）。"""
    global _browser_driver
    if _browser_driver is not None:
        try:
            _browser_driver.quit()
        finally:
            _browser_driver = None


def _browser_fetch_text(params: dict[str, Any]) -> str:
    """浏览器内 fetch api.php，返回原始响应体文本。

    前提：浏览器当前停靠在站点同源页面（过盾后停在首页）。
    这是真实浏览器发出的请求，同样遵守 crawl-delay。
    """
    driver = _get_browser()
    # 确认还停在站点内（防止外部代码导航走了）；不在则重新过盾回首页
    if config.SITE_ORIGIN not in (driver.current_url or ""):
        _wait_shield_pass(driver)

    url = config.API_URL + "?" + urllib.parse.urlencode(params)
    wait_crawl_delay()
    driver.set_script_timeout(BROWSER_FETCH_TIMEOUT_SECONDS)
    # fetch 同源请求，credentials 默认含 cookie；结果逐字回传 Python
    script = (
        "const cb = arguments[arguments.length - 1];"
        "fetch(arguments[0], {credentials: 'include'})"
        "  .then(r => r.text())"
        "  .then(t => cb(t))"
        "  .catch(e => cb('__FETCH_ERROR__:' + e));"
    )
    text = driver.execute_async_script(script, url)
    if not isinstance(text, str):
        raise RuntimeError(f"浏览器 fetch 返回异常类型：{type(text)}")
    if text.startswith("__FETCH_ERROR__:"):
        raise RuntimeError(f"浏览器 fetch 失败：{text}")
    if looks_like_challenge(text):
        # 盾在浏览器内也拦截了（少见）：重新过盾一次后重试
        _log("浏览器通道也被盾拦截，重新过盾…")
        _wait_shield_pass(driver)
        _export_cookies(driver)
        wait_crawl_delay()
        text = driver.execute_async_script(script, url)
        if looks_like_challenge(text):
            raise RuntimeError("浏览器通道重新过盾后仍被拦，放弃")
    return text


# ---------------------------------------------------------------- requests 通道

def build_api_session() -> requests.Session:
    """构造加载了盾会话 cookie 的 requests.Session。"""
    if not _cookies_fresh():
        pass_shield()
    session = requests.Session()
    session.headers.update({
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/154.0.0.0 Safari/537.36"),
    })
    cookies = json.loads(config.COOKIE_PATH.read_text(encoding="utf-8"))
    for c in cookies:
        session.cookies.set(c["name"], c["value"],
                            domain=c.get("domain"), path=c.get("path", "/"))
    return session


def _requests_fetch_text(params: dict[str, Any]) -> str:
    """requests + cookie 调 api.php。被盾拦截时抛 _ChallengeBlocked。"""
    session = build_api_session()
    try:
        wait_crawl_delay()
        resp = session.get(config.API_URL, params=params, timeout=60)
        if resp.status_code != 200 or looks_like_challenge(resp.text):
            raise _ChallengeBlocked(resp.status_code)
        return resp.text
    finally:
        session.close()


class _ChallengeBlocked(Exception):
    """requests 通道被盾拦截的内部信号。"""

    def __init__(self, status: int):
        super().__init__(f"HTTP {status}")
        self.status = status


# ---------------------------------------------------------------- 统一入口

def api_get_text(params: dict[str, Any]) -> str:
    """调用 api.php 并返回原始响应体文本（逐字，未重排）。

    通道选择：先试 requests（本进程未被判死时）；被盾拦截则切换到
    过盾浏览器内 fetch，并在进程内记住"requests 已死"避免重复浪费限速窗口。
    raw/ 存档必须用本函数，保证存的是站点原样字节。
    """
    global _requests_transport_dead
    if not _requests_transport_dead:
        try:
            return _requests_fetch_text(params)
        except _ChallengeBlocked as exc:
            _requests_transport_dead = True
            _log(f"requests 通道被盾拦截（{exc}），本进程改用浏览器 fetch 通道")
    return _browser_fetch_text(params)


def api_get(params: dict[str, Any]) -> dict[str, Any]:
    """调用 api.php 并返回解析后的 JSON dict（内含盾检测与通道回退）。"""
    body = api_get_text(params)
    try:
        return json.loads(body)
    except json.JSONDecodeError:
        # 非 JSON 且未触发盾特征：可能是 API 报错页（如参数错误）。
        # MediaWiki 正常报错也是 JSON，这里直接抛出原文便于排查。
        raise RuntimeError(f"api.php 返回非 JSON：{body[:300]!r}")
