# -*- coding: utf-8 -*-
"""共享路径与常量配置。

所有阶段脚本（crawl/clean/organize/catalog/quality_gate）从这里取路径，
保证四阶段产物落盘位置一致。路径一律由本文件位置推导，与运行时 cwd 无关。
"""
from pathlib import Path

# 仓库根目录 = scripts/ 的上一级
REPO_ROOT = Path(__file__).resolve().parent.parent.parent

# ---- 四阶段产物目录（与 docs/pipeline.md 契约一致）----
RAW_DIR = REPO_ROOT / "raw"        # 阶段1：api.php 原始 JSON 存档（重放清洗用，不发布）
PAGES_DIR = REPO_ROOT / "pages"    # 阶段2：清洗后的结构化 Markdown
MANIFEST_PATH = REPO_ROOT / "manifest.json"  # 每页 oldid/抓取时间/标注版本/大小
CATALOG_PATH = REPO_ROOT / "catalog.md"      # 阶段4：两级中文摘要目录（唯一检索入口）

# ---- 运行时状态（会话 cookie、上次请求时间戳），不属于发布产物 ----
STATE_DIR = Path(__file__).resolve().parent.parent / "state"
COOKIE_PATH = STATE_DIR / "cookies.json"
LAST_REQUEST_PATH = STATE_DIR / "last_request.txt"
# 批量抓取学到的重定向映射（导航标题 -> 规范标题，如 Checksum -> Patches）。
# 普通批量模式用它做"零网络请求续跑"的离线确认（见 crawl.crawl_nav）。
NAV_REDIRECTS_PATH = STATE_DIR / "nav_redirects.json"

# ---- 站点 ----
SITE_ORIGIN = "https://ck3.paradoxwikis.com"
API_URL = SITE_ORIGIN + "/api.php"

# ---- 限速 ----
# robots.txt 规定 Crawl-delay: 15。这是硬下限，任何调用方不得配置为更小值；
# wait_crawl_delay() 以此常量为唯一依据，未提供任何可覆盖入口。
MIN_CRAWL_DELAY_SECONDS = 15.0


def ensure_dirs() -> None:
    """确保产物与状态目录存在（幂等）。"""
    for d in (RAW_DIR, PAGES_DIR, STATE_DIR):
        d.mkdir(parents=True, exist_ok=True)


def safe_filename(page_title: str) -> str:
    """页面标题 → 安全文件名（raw/pages 通用命名约定）。

    规则：保留英文字母/数字/点/连字符/下划线/空格与括号，
    路径分隔符（子页面标题中的 "/"）替换为 "__"，其余非法字符替换为 "_"。
    例：Modding/Scripting -> Modding__Scripting
    """
    name = page_title.strip().replace("/", "__").replace("\\", "__")
    # Windows 文件名非法字符 : * ? " < > |
    for ch in ':*?"<>|':
        name = name.replace(ch, "_")
    return name
