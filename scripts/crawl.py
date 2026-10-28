# -*- coding: utf-8 -*-
"""阶段1：抓取页面 → raw/ 存 api.php 原始 JSON → manifest 登记。

用法：
    python scripts/crawl.py --page Scripting            # 单页（幂等跳过已抓页）
    python scripts/crawl.py --page Scripting --force    # 忽略已抓记录强制重抓
    python scripts/crawl.py --nav                       # 批量：导航模板全部页面
                                                          （清单来自 scripts/state/nav_pages.json，
                                                           由 scripts/nav_pages.py 推导）
    python scripts/crawl.py --nav --limit 5             # 批量但本轮最多抓 5 页
                                                          （断点续跑验证/分批抓取用）
    python scripts/crawl.py --nav --refresh             # 增量刷新（游戏新版本发布后重跑）：
                                                          action=query 批量查各页当前 revid，
                                                          oldid 未变且 raw 完好 → 跳过（零 parse 请求）；
                                                          oldid 变化 / raw 缺失或损坏 → 重抓覆盖修复

批量模式的请求语义（工单02验收）：
- 普通模式（续跑）：先做纯离线确认（manifest 记录 + raw 完好 + 已知重定向映射），
  已完成的页零网络请求；只有离线无法确认的页才发起 1 次批量 query（<=50 标题/请求）
  解析重定向/核对存在性。全部完成时整轮零网络请求。
  重定向映射持久化在 scripts/state/nav_redirects.json（如 Checksum -> Patches），
  使含重定向链接的清单在下一轮也能离线确认。
- --refresh 模式：不做离线确认，始终批量核对全部页的当前 revid（版本刷新语义）。

流程（每步都有注释对应工单验收项）：
1. 幂等检查：manifest 已有该页且 raw 文件在盘 → 直接跳过（不发任何网络请求）
2. action=query&prop=revisions 取 last revid（oldid）与页面大小
   （批量模式用 action=query 多标题批量查，一次请求最多 50 标题，最省请求）
3. action=parse&oldid=... 取模板展开后的渲染 HTML（不能用 action=raw：
   部分页面正文在引用模板内，raw 会丢内容）
4. 原始响应体逐字存 raw/<页名>.json；manifest 原子登记
   标题/oldid/抓取时间/页面标注的游戏版本/大小
相邻 API 请求间隔 >= 15 秒（robots.txt Crawl-delay，硬下限不可配置）。
"""
import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import nav_pages  # noqa: E402

from lib import config, manifest, session  # noqa: E402

# 页面标注的游戏版本提取：
# 1) 优先识别 "timeless" 横幅（本站 eu4box 模板的写法，意为与版本无关，
#    如 Scripting 页："This article is timeless and should be accurate
#    for any version of the game."）→ 记为 "timeless"；
# 2) 否则找第一个 "version x.y[.z]" 形态（如 "Version 1.16"）；
# 3) 都没有记 null（未标注）。
_VERSION_RE = re.compile(
    r"version\s+([0-9]+(?:\.[0-9]+)+(?:\.[0-9xX]+)?)", re.IGNORECASE)


def extract_game_version(html: str) -> str | None:
    """从 parse 渲染 HTML 提取页面横幅标注的游戏版本标注。

    返回：数字版本号（如 "1.16"）、"timeless"（版本无关标注）或 None。
    实现：剥掉标签取可见文本再匹配（横幅在页首，命中即返回）。
    """
    text = re.sub(r"<[^>]+>", " ", html)
    if re.search(r"article\s+is\s+timeless", text, re.IGNORECASE):
        return "timeless"
    m = _VERSION_RE.search(text)
    return m.group(1) if m else None


def get_oldid(page_title: str) -> dict:
    """action=query&prop=revisions：取页面 last revid 与 wikitext 大小。"""
    data = session.api_get({
        "action": "query",
        "format": "json",
        "formatversion": 2,
        "titles": page_title,
        "redirects": 1,                  # 跟随重定向，保证拿到规范页
        "prop": "revisions",
        "rvprop": "ids|timestamp|size",
        "rvlimit": 1,
    })
    pages = data.get("query", {}).get("pages", [])
    if not pages:
        raise RuntimeError(f"query 未返回页面：{page_title}（响应：{data}）")
    page = pages[0]
    if "missing" in page:
        raise RuntimeError(f"页面不存在：{page_title}")
    rev = page["revisions"][0]
    return {
        "oldid": rev["revid"],
        "pageid": page["pageid"],
        "title": page["title"],          # 重定向解析后的规范标题
        "size_bytes": rev.get("size", 0),
        "fetched_at": datetime.now().astimezone().isoformat(timespec="seconds"),
    }


def get_oldids_batch(titles: list[str]) -> dict[str, dict | None]:
    """action=query 多标题批量查 last revid（一次请求最多 50 标题）。

    刷新模式检查 oldid、批量抓取前置解析重定向都用它，比逐页单查省
    掉 N-1 次限速请求。redirects=1 跟随重定向，返回值按键为**请求时的
    标题**（导航框原始标题），值为该页信息（含重定向解析后的规范标题）
    或 None（页面不存在）。每请求前照常走 wait_crawl_delay（>=15s）。
    """
    result: dict[str, dict | None] = {}
    for i in range(0, len(titles), 50):
        chunk = titles[i:i + 50]
        data = session.api_get({
            "action": "query",
            "format": "json",
            "formatversion": 2,
            "titles": "|".join(chunk),
            "redirects": 1,
            "prop": "revisions",
            "rvprop": "ids|size",
            # 注意：多标题模式下禁止传 rvlimit（API 会报
            # "rvlimit may only be used with a single page"）；
            # 多页模式默认每页只返回最新一条修订，正合本意
        })
        if "error" in data:
            raise RuntimeError(f"批量 query 返回错误：{data['error']}")
        q = data.get("query", {})
        # 重定向表：from -> to（罕见链式重定向迭代解析，防环）
        redirect_map = {r["from"]: r["to"] for r in q.get("redirects", [])}
        pages_by_title = {p["title"]: p for p in q.get("pages", [])}

        def _resolve(t: str) -> str:
            seen = set()
            while t in redirect_map and t not in seen:
                seen.add(t)
                t = redirect_map[t]
            return t

        for t in chunk:
            page = pages_by_title.get(_resolve(t))
            if page is None or "missing" in page or not page.get("revisions"):
                result[t] = None
                continue
            rev = page["revisions"][0]
            result[t] = {
                "oldid": rev["revid"],
                "pageid": page["pageid"],
                "title": page["title"],      # 重定向解析后的规范标题
                "size_bytes": rev.get("size", 0),
            }
    return result


def raw_intact(raw_path: Path) -> bool:
    """raw 存档完好性检查：存在、非空、是合法 JSON 且含 parse.text。

    刷新模式用它发现"oldid 没变但产物被改坏"的页（如手工截断的 json），
    这类页即使版本未变也要重抓修复——oldid 比对发现不了它们。
    """
    try:
        if not raw_path.is_file() or raw_path.stat().st_size == 0:
            return False
        raw = json.loads(raw_path.read_text(encoding="utf-8"))
        return "parse" in raw and "text" in raw["parse"]
    except (OSError, json.JSONDecodeError):
        return False


def load_nav_redirects() -> dict[str, str]:
    """读批量查询学到的重定向映射（导航标题 -> 规范标题）。

    文件缺失/损坏时返回空映射（首次批量运行前的正常状态）。
    有了它，普通批量模式才能对含重定向链接的清单做零网络请求的离线确认
    （例：导航链接 Checksum 在 manifest 里的键是规范标题 Patches）。
    """
    try:
        data = json.loads(config.NAV_REDIRECTS_PATH.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


def save_nav_redirects(mapping: dict[str, str]) -> None:
    """原子落盘重定向映射（临时文件 + os.replace，与 manifest 同款策略）。"""
    config.ensure_dirs()
    tmp = config.NAV_REDIRECTS_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(mapping, ensure_ascii=False, indent=2,
                              sort_keys=True) + "\n",
                   encoding="utf-8", newline="\n")
    os.replace(tmp, config.NAV_REDIRECTS_PATH)


def fetch_parse_html(oldid: int) -> tuple[str, dict]:
    """action=parse：取模板展开后的渲染正文 HTML（prop=text）。

    返回 (原始响应体文本, 解析后的 dict)。disablelimitreport=1 只是去掉
    响应里的解析报告噪音，不改动正文内容；其余参数保持默认。raw/ 存档
    存原始响应体逐字内容（契约见 docs/pipeline.md）。
    """
    body = session.api_get_text({
        "action": "parse",
        "format": "json",
        "formatversion": 2,
        "oldid": oldid,
        "prop": "text",
        "disablelimitreport": 1,
    })
    try:
        data = json.loads(body)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"parse 响应非 JSON：{body[:300]!r}") from exc
    if "parse" not in data or "text" not in data.get("parse", {}):
        raise RuntimeError(f"parse 响应缺少正文：{data}")
    return body, data


def crawl_page(page_title: str, force: bool = False,
               preinfo: dict | None = None) -> Path:
    """抓取单页并存档+登记。返回 raw 文件路径；已抓且未强制时为 no-op。

    preinfo：批量模式由 get_oldids_batch 预查的页面信息（oldid/规范标题/
    大小），传入则跳过单页 query 请求（每页只花 1 次 parse 请求）。
    """
    config.ensure_dirs()

    # --- 幂等检查：manifest 有记录且 raw 文件存在 → 跳过 ---
    existing = manifest.read_manifest()["pages"].get(page_title)
    if not force and existing and existing.get("raw_file"):
        raw_path = config.REPO_ROOT / existing["raw_file"]
        if raw_path.is_file():
            print(f"[crawl] 跳过（已抓，幂等）：{page_title} "
                  f"oldid={existing.get('oldid')} -> {raw_path}")
            return raw_path

    print(f"[crawl] 开始抓取：{page_title}")
    info = dict(preinfo) if preinfo else get_oldid(page_title)
    info.setdefault("fetched_at",
                    datetime.now().astimezone().isoformat(timespec="seconds"))
    print(f"[crawl] 规范标题={info['title']} oldid={info['oldid']} "
          f"wikitext 大小={info['size_bytes']}B")

    body, raw_data = fetch_parse_html(info["oldid"])   # 内部保证 >=15s 间隔
    version = extract_game_version(raw_data["parse"]["text"])

    raw_path = config.RAW_DIR / (config.safe_filename(info["title"]) + ".json")
    # 原始响应体逐字存档（newline="" 防止文本模式改写换行）
    with open(raw_path, "w", encoding="utf-8", newline="") as f:
        f.write(body)
    print(f"[crawl] raw 已存：{raw_path}（{len(body.encode('utf-8'))}B），"
          f"标注游戏版本={version or '未标注'}")

    # --- manifest 原子登记（字段即工单要求五项 + 定位信息）---
    canonical_title = info["title"]

    def _update(entry: dict) -> dict:
        entry.update({
            "title": canonical_title,
            "oldid": info["oldid"],
            "fetched_at": info["fetched_at"],
            "game_version": version,             # 页面横幅标注的游戏版本，可为 null
            "size_bytes": info["size_bytes"],    # wikitext 源码大小（API 报告值）
            "raw_file": f"raw/{raw_path.name}",
            "raw_bytes": raw_path.stat().st_size,
        })
        return entry

    manifest.update_page(canonical_title, _update)
    print(f"[crawl] manifest 已登记：{canonical_title}")
    return raw_path


def crawl_nav(refresh: bool = False, limit: int | None = None) -> int:
    """批量抓取导航模板全部页面（工单02核心入口）。

    流程：
    1. 读 scripts/state/nav_pages.json 的 crawl_order（Effects 置顶；
       缺失时由 nav_pages.load_nav_pages 现场离线推导）；
    2a. 普通模式（续跑）先做纯离线确认：manifest 有记录 + raw 完好 +
        已知重定向映射（state/nav_redirects.json）的页直接判完成，零请求；
        全部确认时整轮不发任何网络请求（断点续跑零请求语义）；
    2b. 仅对离线无法确认的页发批量 query（action=query 多标题，一次最多
        50 标题）解析重定向/核对存在性，并持久化新学到的重定向映射；
        --refresh 模式跳过离线确认，始终批量核对全部页的当前 revid；
    3. 逐页决策：
       - 普通模式（断点续跑）：manifest 有记录且 raw 完好 → 跳过；
       - --refresh 模式（游戏新版本后重跑）：oldid 未变且 raw 完好 → 跳过；
         oldid 变化 / raw 缺失或损坏 / 新页 → 重抓覆盖（修复语义）；
    4. 每次抓取仍走 crawl_page → session.api_get_text（15s 限速 + 双通道），
       manifest 走 manifest.update_page 原子登记。
    limit：本轮最多抓取的页数（0 表示不抓只报告），用于分批/续跑验证。
    返回：待抓页未清零时为 2（供脚本判断"还有剩余"），全部完成返回 0。
    """
    nav = nav_pages.load_nav_pages()
    titles: list[str] = nav["crawl_order"]
    print(f"[crawl] 导航清单：{len(titles)} 页（来源 {nav['derived_from']}），"
          f"模式={'增量刷新(refresh)' if refresh else '批量抓取(续跑跳过已抓页)'}")

    done = 0          # 本轮实际抓取页数
    pending = []      # 决策后需要抓取的 (导航标题, 规范标题, info)
    skipped = 0       # 各类跳过合计（离线确认 + 联网决策）
    skipped_unchanged = 0
    seen_canonical: set[str] = set()   # 重定向解析后去重（防两导航链同指一页）

    # ---- 离线确认快路径（普通模式专属；refresh 必须联网核对 revid）----
    redirects = load_nav_redirects()
    if not refresh:
        mf_pages = manifest.read_manifest()["pages"]
        offline_ok: list[str] = []      # 离线确认完成的导航标题
        query_titles: list[str] = []    # 离线无法确认、需联网解析的标题
        for t in titles:
            canonical = redirects.get(t, t)   # 无映射时假定非重定向
            entry = mf_pages.get(canonical)
            if (entry and entry.get("raw_file")
                    and raw_intact(config.REPO_ROOT / entry["raw_file"])):
                # 完成确认（重复解析到同一规范页的导航链接也计为跳过）
                if canonical not in seen_canonical:
                    seen_canonical.add(canonical)
                offline_ok.append(t)
            else:
                query_titles.append(t)
        skipped += len(offline_ok)
        if not query_titles:
            print(f"[crawl] 离线确认：{len(offline_ok)} 页全部已完成且 raw 完好，"
                  f"本轮零网络请求（未触碰 api.php，含批量 query）")
            return 0
        print(f"[crawl] 离线确认 {len(offline_ok)} 页已完成；"
              f"剩 {len(query_titles)} 页需联网核对（批量 query 只查这些标题）")
    else:
        query_titles = titles           # refresh：全量核对当前 revid

    # ---- 批量查询当前 revid：1 次请求（<=50 标题）/批，含 15s 限速 ----
    infos = get_oldids_batch(query_titles)
    # 持久化新学到的重定向（导航标题 != 规范标题），供下轮离线确认复用
    new_redirects = {t: info["title"] for t, info in infos.items()
                     if info and info["title"] != t}
    if new_redirects:
        redirects.update(new_redirects)
        save_nav_redirects(redirects)
        print(f"[crawl] 重定向映射已更新并落盘 {config.NAV_REDIRECTS_PATH.name}："
              f"{new_redirects}")

    for t in query_titles:
        info = infos.get(t)
        if info is None:
            print(f"[crawl] 页面不存在（红链或已删除），跳过：{t}")
            continue
        canonical = info["title"]
        if canonical in seen_canonical:
            print(f"[crawl] 跳过（重定向解析后重复）：{t} -> {canonical}")
            continue
        seen_canonical.add(canonical)
        entry = manifest.read_manifest()["pages"].get(canonical)
        raw_ok = False
        if entry and entry.get("raw_file"):
            raw_ok = raw_intact(config.REPO_ROOT / entry["raw_file"])
        if entry and raw_ok and entry.get("oldid") == info["oldid"]:
            # raw 完好且版本一致：普通模式=已完成，refresh 模式=未变页
            reason = "已抓" if not refresh else "oldid 未变"
            skipped += 1
            if refresh:
                skipped_unchanged += 1
            print(f"[crawl] 跳过（{reason}）：{t} -> {canonical} "
                  f"oldid={info['oldid']}")
            continue
        if entry and raw_ok and not refresh:
            # 普通模式下版本不同也跳过（增量刷新语义只属于 --refresh）
            skipped += 1
            print(f"[crawl] 跳过（已抓；oldid 有变化，如需刷新用 --nav --refresh）："
                  f"{t} -> {canonical} 盘上 oldid={entry.get('oldid')} "
                  f"当前 oldid={info['oldid']}")
            continue
        pending.append((t, canonical, info))

    extra = f"（其中 oldid 未变 {skipped_unchanged}）" if refresh else ""
    print(f"[crawl] 决策汇总：本轮待抓 {len(pending)} 页，跳过 {skipped} 页{extra}")

    total_pending = len(pending)
    if limit is not None:
        if total_pending > limit:
            print(f"[crawl] --limit {limit}：本轮只抓前 {limit} 页，"
                  f"其余 {total_pending - limit} 页留给下次续跑")
        pending = pending[:limit]

    for i, (t, canonical, info) in enumerate(pending, 1):
        print(f"[crawl] 进度：{i}/{len(pending)}（本轮待抓）", flush=True)
        crawl_page(canonical, force=True, preinfo=info)
        done += 1

    remaining = total_pending - done
    print(f"[crawl] 批量结束：本轮抓取 {done} 页，剩余待抓 {remaining} 页，"
          f"预计耗时 {remaining * 15 // 60}~{remaining * 2 * 15 // 60} 分钟")
    return 0 if remaining == 0 else 2  # 退出码 2 = 仍有待抓页（--limit 截断）


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):       # Windows 控制台中文安全输出
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="阶段1：抓取页面存 raw/ 并登记 manifest")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--page", help="单页标题（默认 Scripting）")
    g.add_argument("--nav", action="store_true",
                   help="批量抓取导航模板全部页面（清单 state/nav_pages.json）")
    ap.add_argument("--force", action="store_true",
                    help="（单页模式）忽略已抓记录强制重抓")
    ap.add_argument("--refresh", action="store_true",
                    help="（配合 --nav）增量刷新：批量查当前 revid，oldid 未变且"
                         " raw 完好的页跳过，变化/损坏/缺失的页重抓覆盖")
    ap.add_argument("--limit", type=int, default=None, metavar="N",
                    help="（配合 --nav）本轮最多抓 N 页，剩余下次续跑（分批验证用）")
    args = ap.parse_args(argv)
    if args.nav:
        return crawl_nav(refresh=args.refresh, limit=args.limit)
    crawl_page(args.page or "Scripting", force=args.force)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
