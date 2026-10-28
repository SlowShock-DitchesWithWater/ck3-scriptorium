# -*- coding: utf-8 -*-
"""工单05：一跳候选清单生成 + 种子必抓 + 勾选补抓（断点可续跑）。

职责边界（与既有脚本的关系）：
- 链接枚举只用 raw/*.json 的 parse HTML（清洗产物已丢链接目标）；
  剔除底部 Modding 导航框 subtree（识别特征与 lib/cleaner.py 一致）、
  红链、外部链接、纯锚点、非主命名空间链接。
- 页面存在性/大小/重定向用 action=query&prop=info 批量查（50 标题/请求，
  redirects=1 跟随重定向拿规范标题），结果缓存于 state/onehop_info_cache.json，
  重跑清单只增量查新出现的标题（已缓存/已抓页零请求）。
- 补抓直接复用 crawl.crawl_page（单页逻辑 + session 15s 限速 + 双通道 +
  manifest.update_page 原子登记），本脚本不做任何直接请求循环/manifest 写入。

产物（scripts/state/，运行时状态）：
- onehop_candidates.json  机器可读候选清单（含种子核查结果与统计证据）
- onehop_candidates.md    人可勾选版（checkbox + 频次降序）
- onehop_selection.json   用户勾选状态（重跑生成不覆盖；默认勾选只在
                          文件缺失时写入一次 = 10 个种子中可抓者）
- onehop_info_cache.json  prop=info 批量查询缓存（标题 -> 规范标题/大小/revid）

用法：
    python scripts/onehop.py --list            # 枚举+查大小并落盘（默认动作）
    python scripts/onehop.py --list --offline  # 纯离线枚举（不查 API，大小留缓存值）
    python scripts/onehop.py --list --refresh-info   # 忽略缓存重查全部信息
    python scripts/onehop.py --list --max-info-requests N  # 本轮最多 N 次批量查询
    python scripts/onehop.py --select "标题A" "标题B"     # 勾选
    python scripts/onehop.py --unselect "标题A"          # 取消勾选
    python scripts/onehop.py --crawl          # 抓取勾选且未抓的页（增量，已抓跳过）
    python scripts/onehop.py --crawl --limit 3  # 本轮最多抓 3 页（断点续跑/分批）
    python scripts/onehop.py --status          # 汇总当前状态

退出码：--crawl 全部完成 0；--limit 截断仍有剩余 2（与 crawl.py --nav 语义一致）。
"""
import argparse
import json
import os
import re
import sys
import urllib.parse
from collections import Counter
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from bs4 import BeautifulSoup  # noqa: E402

import crawl  # noqa: E402  复用单页抓取逻辑与 raw 完好性检查
from lib import config, manifest, session  # noqa: E402

# ---- 落盘位置（scripts/state/，运行时状态不属于发布产物）----
CANDIDATES_JSON = config.STATE_DIR / "onehop_candidates.json"
CANDIDATES_MD = config.STATE_DIR / "onehop_candidates.md"
SELECTION_PATH = config.STATE_DIR / "onehop_selection.json"
INFO_CACHE_PATH = config.STATE_DIR / "onehop_info_cache.json"

# ---- 种子页（spec 抓取范围"种子补充"批次；下划线形式是 URL 形态，
#      API 查询传空格形式即可）----
SEED_PAGES = [
    "Effects list",
    "Triggers list",
    "Scopes list",
    "Scripted effects",
    "Weight modifier",
    "Defines",
    "Lists",
    "Artifact modding",
    "Interactions modding",
    "Customizable localization",
]

# 非主命名空间链接前缀（小写比较；href 已解码并把下划线还原为空格）。
# 一跳候选只考虑主条目命名空间的 wiki 页。注意本站项目命名空间写作
# "CK3 Wiki:"（带空格），版本横幅模板会在每页链接 CK3 Wiki:Versioning，
# 属模板噪声而非正文链接，必须一并挡掉。
DENIED_NS_PREFIXES = (
    "special:", "file:", "category:", "template:", "user:", "user talk:",
    "help:", "mediawiki:", "talk:", "project:", "ck3 wiki:", "ck3wiki:",
    "modding talk:", "paradox wiki:",
    "file talk:", "template talk:", "category talk:", "help talk:",
    "thread:", "topic:", "translation:", "gadget:", "property:", "concept:",
)


def _now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def _atomic_write(path: Path, text: str) -> None:
    """原子落盘（临时文件 + os.replace，与 lib/manifest.py 同款策略）。"""
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8", newline="\n")
    os.replace(tmp, path)


# ---------------------------------------------------------------- 离线链接枚举

def _decompose_navboxes(soup: BeautifulSoup) -> int:
    """剔除底部 Modding 导航框 subtree，返回其内锚点数（统计证据）。

    识别特征与 lib/cleaner.py / nav_pages.py 完全一致：
    div[style*="border-collapse"] 且首个链接指向 /Modding。
    """
    anchors = 0
    for div in soup.find_all("div"):
        if div.decomposed:
            continue
        style = div.get("style") or ""
        if "border-collapse" not in style:
            continue
        first_a = div.find("a")
        if first_a is not None and (first_a.get("href") == "/Modding"
                                    or first_a.get("title") == "Modding"):
            anchors += len(div.find_all("a"))
            div.decompose()
    return anchors


def _href_to_title(href: str) -> str | None:
    """wiki 内链 href（/Page_title 或 /Page_title#fragment）-> 主命名空间标题。

    非主命名空间/纯锚点/编辑入口/特殊页返回 None。
    """
    path = href.split("#", 1)[0]
    if not path.startswith("/") or path.startswith("//"):
        return None                     # 外链/协议相对/纯锚点
    title = urllib.parse.unquote(path[1:]).replace("_", " ").strip()
    if not title or title.lower() == "main page":
        return None
    lowered = title.lower()
    if any(lowered.startswith(p) for p in DENIED_NS_PREFIXES):
        return None                     # 非主命名空间
    if "action=edit" in href or "redlink=1" in href:
        return None                     # 编辑入口（红链的兜底特征）
    return title


def enumerate_body_links() -> dict:
    """从全部已抓页 raw 存档枚举正文 wiki 内链（纯离线，零网络请求）。

    返回：
    {
      "counts": {目标标题: 锚点出现次数},
      "sources": {目标标题: [来源页…按 manifest 插入顺序去重]},
      "source_pages": 参与枚举的页数,
      "skipped_raw": [raw 缺失/损坏而跳过的页],
      "stats": {各类剔除计数，含导航框锚点数},
    }
    """
    counts: Counter[str] = Counter()
    sources: dict[str, list[str]] = {}
    skipped_raw: list[str] = []
    stats = {"navbox_anchors": 0, "external_or_anchor": 0,
             "redlinks": 0, "denied_ns": 0, "total_anchors": 0}
    mf_pages = manifest.read_manifest()["pages"]
    used = 0
    for title, entry in mf_pages.items():
        raw_file = entry.get("raw_file")
        if not raw_file or not (config.REPO_ROOT / raw_file).is_file():
            skipped_raw.append(title)
            continue
        try:
            raw = json.loads((config.REPO_ROOT / raw_file)
                             .read_text(encoding="utf-8"))
            html = raw["parse"]["text"]
        except (OSError, json.JSONDecodeError, KeyError):
            skipped_raw.append(title)
            continue
        used += 1
        soup = BeautifulSoup(html, "html.parser")
        stats["navbox_anchors"] += _decompose_navboxes(soup)
        for a in soup.find_all("a"):
            if a.decomposed:
                continue                # 已随导航框等外层分解
            stats["total_anchors"] += 1
            href = a.get("href") or ""
            classes = a.get("class") or []
            if "new" in classes:        # 红链（不存在的页面）三特征之一，本站实测
                stats["redlinks"] += 1
                continue
            # 目标一律由 href 推导：MW 生成的正文内链 href 即链接目标
            # （/Page_title 或 /Page_title#fragment）。不能优先取 title 属性——
            # 章节编辑按钮的 title 是"编辑章节：X"、缩略图放大链接是"放大"，
            # 都不是页面标题（首轮实测因此混入 448 个伪标题）。
            target = _href_to_title(href)
            if target is None:
                # 外链/纯锚点 vs 命中 deny 列表/编辑入口，归类计数
                if href.startswith("/") or href.startswith("./"):
                    stats["denied_ns"] += 1
                else:
                    stats["external_or_anchor"] += 1
                continue
            counts[target] += 1
            src = sources.setdefault(target, [])
            if title not in src:
                src.append(title)
    return {"counts": dict(counts), "sources": sources, "source_pages": used,
            "skipped_raw": skipped_raw, "stats": stats}


# ---------------------------------------------------------------- info 批量查询与缓存

def load_info_cache() -> dict:
    try:
        data = json.loads(INFO_CACHE_PATH.read_text(encoding="utf-8"))
        return data.get("entries", {}) if isinstance(data, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


def save_info_cache(entries: dict) -> None:
    config.ensure_dirs()
    _atomic_write(INFO_CACHE_PATH, json.dumps(
        {"schema_version": 1, "entries": entries},
        ensure_ascii=False, indent=2, sort_keys=True) + "\n")


def query_infos(titles: list[str]) -> dict[str, dict | None]:
    """action=query&prop=info 批量查（50 标题/请求，redirects=1）。

    返回按**请求标题**键控：值为页面信息 dict（canonical/size/lastrevid）
    或 None（页面不存在）。每次请求走 session.api_get（15s 限速 + 双通道）。
    """
    result: dict[str, dict | None] = {}
    for i in range(0, len(titles), 50):
        chunk = titles[i:i + 50]
        print(f"[onehop] prop=info 批量查询 {len(chunk)} 标题"
              f"（{i // 50 + 1}/{(len(titles) + 49) // 50} 批）…", flush=True)
        data = session.api_get({
            "action": "query", "format": "json", "formatversion": 2,
            "titles": "|".join(chunk),
            "redirects": 1,
            "prop": "info",
        })
        if "error" in data:
            raise RuntimeError(f"prop=info 批量查询返回错误：{data['error']}")
        q = data.get("query", {})
        # normalized（大小写/下划线归一）与 redirects（重定向）两级映射，
        # 罕见链式情形迭代解析（防环）
        maps = [{n["from"]: n["to"] for n in q.get("normalized", [])},
                {r["from"]: r["to"] for r in q.get("redirects", [])}]

        def _resolve(t: str) -> str:
            seen = set()
            for m in maps:
                while t in m and t not in seen:
                    seen.add(t)
                    t = m[t]
            return t

        pages_by_title = {p["title"]: p for p in q.get("pages", [])}
        for t in chunk:
            page = pages_by_title.get(_resolve(t))
            if page is None or "missing" in page:
                result[t] = None
                continue
            result[t] = {
                "canonical": page["title"],       # 重定向解析后的规范标题
                "pageid": page.get("pageid"),
                "size_bytes": page.get("length", 0),   # wikitext 大小
                "lastrevid": page.get("lastrevid"),    # 即 oldid（补抓预信息用）
            }
    return result


def ensure_infos(titles: list[str], offline: bool = False,
                 refresh: bool = False,
                 max_requests: int = 0) -> tuple[dict, int, list[str]]:
    """确保 titles 的 info 都有（缓存优先，缺口联网补齐）。

    返回 (info_by_title, 本次联网请求次数, 本轮未查到信息的标题列表)。
    offline=True 时不联网，缺口标题信息为 None 且记入未查列表；
    max_requests>0 时限制批量查询次数，超出部分留给下次 --list 续查。
    """
    cache = {} if refresh else load_info_cache()
    fetched_at = _now()
    need = [t for t in titles if t not in cache]
    requests = 0
    if need and not offline:
        to_query = need if not max_requests else need[:max_requests * 50]
        infos = query_infos(to_query)
        requests = (len(to_query) + 49) // 50
        for t, info in infos.items():
            entry = dict(info) if info else {"missing": True}
            entry["fetched_at"] = fetched_at
            cache[t] = entry
        save_info_cache(cache)
        need = need[len(to_query):]     # 未查部分（max_requests 截断时）
    elif need and offline:
        pass                            # 离线模式：缺口留 None，由调用方标注
    else:
        save_info_cache(cache) if refresh else None   # refresh 时回写全量
    info_map = {t: cache.get(t) for t in titles}
    unresolved = [t for t in need]
    return info_map, requests, unresolved


# ---------------------------------------------------------------- 勾选状态

def load_selection() -> dict | None:
    try:
        return json.loads(SELECTION_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def save_selection(selected: dict[str, bool]) -> None:
    config.ensure_dirs()
    _atomic_write(SELECTION_PATH, json.dumps(
        {"schema_version": 1, "selected": selected, "updated_at": _now()},
        ensure_ascii=False, indent=2, sort_keys=True) + "\n")


# ---------------------------------------------------------------- 清单生成

def _entry_title_in_manifest(info: dict | None, link_title: str,
                             mf_pages: dict) -> tuple[str | None, str]:
    """解析一个链接标题的覆盖状态。

    返回 (canonical 规范标题或 None, status)：
    status ∈ {"crawled"(链接标题即已抓页), "covered"(经重定向解析到已抓页),
              "missing"(不存在), "candidate"(可抓)}。
    info 为 None 且未联网时返回 ("", "unknown") 由调用方处理。
    """
    if link_title in mf_pages:
        return link_title, "crawled"
    if info is None:
        return None, "missing"
    if info.get("missing"):
        return None, "missing"
    canonical = info.get("canonical") or link_title
    if canonical in mf_pages:
        return canonical, "covered"
    return canonical, "candidate"


def generate_list(offline: bool = False, refresh_info: bool = False,
                  max_info_requests: int = 0) -> dict:
    """枚举一跳链接 -> 查 info -> 落盘 JSON + MD。返回清单 dict。"""
    mf_pages = manifest.read_manifest()["pages"]
    enum = enumerate_body_links()
    counts, sources = enum["counts"], enum["sources"]

    # 全部需要 API 信息的标题：枚举目标中不在 manifest 的 + 全部种子
    direct_crawled = {t for t in counts if t in mf_pages}
    query_titles = sorted(set(counts) - direct_crawled) + \
        [s for s in SEED_PAGES if s not in counts]
    info_map, requests, unresolved = ensure_infos(
        query_titles, offline=offline, refresh=refresh_info,
        max_requests=max_info_requests)

    selection = load_selection()
    default_selection = selection is None

    # ---- 聚合候选 / 覆盖（已抓）/ 不存在 ----
    candidates: list[dict] = []
    covered: list[dict] = []
    missing: list[dict] = []
    for t in sorted(set(counts) | set(SEED_PAGES)):
        freq = counts.get(t, 0)
        src = sources.get(t, [])
        is_seed = t in SEED_PAGES
        info = info_map.get(t) if t in query_titles else None
        canonical, status = _entry_title_in_manifest(info, t, mf_pages)
        if t in unresolved and status not in ("crawled",):
            status, canonical = "unknown", ""     # 本轮未联网查到的标题
        base = {
            "title": t, "freq": freq, "source_count": len(src),
            "sources": src, "seed": is_seed,
            "size_bytes": (mf_pages[t].get("size_bytes") if t in mf_pages
                           else (info or {}).get("size_bytes")),
        }
        if status == "crawled":
            covered.append({**base, "canonical": t,
                            "status": "crawled",
                            "must_crawl": False})
        elif status == "covered":
            covered.append({**base, "canonical": canonical,
                            "status": "covered_redirect"})
        elif status == "missing":
            missing.append({**base, "canonical": None, "status": "missing"})
        else:
            candidates.append({**base, "canonical": canonical or t,
                               "status": status, "must_crawl": is_seed,
                               "pageid": (info or {}).get("pageid"),
                               "lastrevid": (info or {}).get("lastrevid")})

    # 频次降序、来源页数次之、标题字母序保证稳定输出
    candidates.sort(key=lambda c: (-c["freq"], -c["source_count"], c["title"]))
    covered.sort(key=lambda c: (-c["freq"], c["title"]))

    # ---- 种子核查表（存在性/重定向如实记录）----
    cand_by_title = {c["title"]: c for c in candidates}
    seeds_report = []
    for s in SEED_PAGES:
        if s in mf_pages:
            note = "已抓（manifest 在册）"
        elif s in cand_by_title:
            c = cand_by_title[s]
            note = ("待抓（默认勾选）" if c["status"] == "candidate"
                    else "本轮未联网核实（下次 --list 补查）")
        else:
            hit = next((m for m in missing if m["title"] == s), None)
            hit_cov = next((m for m in covered if m["title"] == s), None)
            if hit is not None:
                note = "不存在（API prop=info 返回 missing）"
            elif hit_cov is not None:
                note = f"重定向至已抓页 {hit_cov['canonical']}，无需补抓"
            else:
                note = "未出现在正文链接中，且本轮未核实"
        seeds_report.append({"title": s, "note": note})

    # ---- 勾选初始化（仅文件缺失时写一次；默认勾选 = 可抓种子）----
    if default_selection:
        init = {c["title"]: True for c in candidates if c["must_crawl"]}
        save_selection(init)
        print(f"[onehop] 勾选文件缺失，已按种子默认初始化勾选 "
              f"{len(init)} 项 -> {SELECTION_PATH.name}")
    sel = (load_selection() or {"selected": {}})["selected"]

    data = {
        "schema_version": 1,
        "generated_at": _now(),
        "source_pages": enum["source_pages"],
        "skipped_raw": enum["skipped_raw"],
        "enumeration_stats": enum["stats"],
        "info_requests_this_run": requests,
        "unresolved_titles": unresolved,
        "candidates": candidates,
        "covered": covered,
        "missing": missing,
        "seeds": seeds_report,
        "selected": sel,
    }
    config.ensure_dirs()
    _atomic_write(CANDIDATES_JSON, json.dumps(data, ensure_ascii=False,
                                              indent=2) + "\n")
    write_candidates_md(data, sel)
    print(f"[onehop] 清单已落盘：{CANDIDATES_JSON}")
    print(f"[onehop] 可勾选版：{CANDIDATES_MD}")
    print(f"[onehop] 候选 {len(candidates)} 页 / 命中已抓 {len(covered)} 页 / "
          f"不存在 {len(missing)} 页 / 本轮 info 请求 {requests} 次"
          f"（未核实 {len(unresolved)} 标题留待下次）")
    return data


def _fmt_sources(src: list[str], cap: int = 6) -> str:
    if len(src) <= cap:
        return "、".join(src)
    return "、".join(src[:cap]) + f" 等 {len(src)} 页"


def write_candidates_md(data: dict, sel: dict[str, bool]) -> None:
    """渲染人可勾选的 Markdown 清单（checkbox 反映勾选文件状态）。"""
    st = data["enumeration_stats"]
    lines = [
        "# 一跳候选清单（onehop candidates）",
        "",
        f"> 生成时间：{data['generated_at']}（scripts/onehop.py --list，可反复重跑，不丢勾选）",
        f"> 来源：{data['source_pages']} 页已抓页正文内链聚合；"
        f"剔除：Modding 导航框 {st['navbox_anchors']} 锚点、红链 {st['redlinks']}、"
        f"外链/锚点 {st['external_or_anchor']}、非主命名空间 {st['denied_ns']}。",
        "> 勾选方式：`python scripts/onehop.py --select \"标题\"` / `--unselect \"标题\"`"
        "（状态存 scripts/state/onehop_selection.json）；补抓：`--crawl`。",
        "",
        f"## 候选页（按出现频次降序，共 {len(data['candidates'])}）",
        "",
    ]
    for c in data["candidates"]:
        checked = "x" if sel.get(c["title"]) else " "
        tags = "【必抓·种子】" if c["must_crawl"] else ""
        size = f" · 大小 {c['size_bytes']}B" if c.get("size_bytes") is not None else ""
        status = " · **信息待核实**" if c["status"] == "unknown" else ""
        lines.append(
            f"- [{checked}] **{c['title']}**（频次 {c['freq']} · "
            f"来源 {c['source_count']} 页{_fmt_sources(c['sources'])}）"
            f"{size}{status}{tags}")
    lines += ["", f"### 重定向到已抓页（无需补抓，共 "
              f"{sum(1 for c in data['covered'] if c['status'] == 'covered_redirect')}）", ""]
    for c in data["covered"]:
        if c["status"] == "covered_redirect":
            lines.append(f"- {c['title']} → {c['canonical']}（已抓）")
    lines += ["", f"### 页面不存在（正文有链接但目标缺失，共 {len(data['missing'])}）", ""]
    for m in data["missing"]:
        lines.append(f"- {m['title']}（API prop=info missing）")
    lines += ["", "## 种子页核查（spec 种子补充批次，共 10）", "",
              "| 种子 | 状态 |", "|---|---|"]
    for s in data["seeds"]:
        lines.append(f"| {s['title']} | {s['note']} |")
    lines += ["", f"## 一跳命中已抓页对照（共 {len(data['covered'])}，不进候选）", ""]
    for c in data["covered"]:
        size = f" · 大小 {c['size_bytes']}B" if c.get("size_bytes") is not None else ""
        lines.append(f"- **{c['title']}**（频次 {c['freq']} · "
                     f"来源 {c['source_count']} 页）{size}")
    _atomic_write(CANDIDATES_MD, "\n".join(lines) + "\n")


# ---------------------------------------------------------------- 补抓

def _lookup(data: dict, title: str) -> dict | None:
    """在候选与已覆盖（重定向/已抓）两个集合里找勾选标题的条目。

    补抓后重跑 --list 会把已抓页从 candidates 挪进 covered，勾选文件里的
    标题仍指向旧清单条目——必须两处都查，否则已抓页会被误报"不在清单"。
    """
    for c in data["candidates"]:
        if c["title"] == title:
            return c
    for c in data["covered"]:
        if c["title"] == title:
            return {**c, "status": "covered"}   # covered=crawled/redirect 统称已覆盖
    for m in data.get("missing", []):
        if m["title"] == title:
            return m
    return None


def crawl_selected(limit: int | None = None) -> int:
    """抓取勾选且未抓的页（增量语义：manifest 在册且 raw 完好 → 跳过零请求）。"""
    if not CANDIDATES_JSON.is_file():
        print("[onehop] 候选清单不存在，先运行 --list")
        return 1
    data = json.loads(CANDIDATES_JSON.read_text(encoding="utf-8"))
    sel = (load_selection() or {"selected": {}})["selected"]
    selected_titles = [t for t, on in sel.items() if on]

    mf_pages = manifest.read_manifest()["pages"]
    pending: list[tuple[str, dict]] = []   # (勾选标题, 候选条目)
    for t in selected_titles:
        c = _lookup(data, t)
        if c is None:
            print(f"[onehop] 跳过：{t} —— 不在当前候选清单（先 --list 后重试）")
            continue
        if c["status"] in ("missing",):
            print(f"[onehop] 跳过：{t} —— 页面不存在")
            continue
        canonical = c.get("canonical") or t
        entry = mf_pages.get(canonical)
        if entry and entry.get("raw_file") and \
                crawl.raw_intact(config.REPO_ROOT / entry["raw_file"]):
            print(f"[onehop] 跳过（已抓，增量语义）：{t} -> {canonical}")
            continue
        # 未在册，或在册但 raw 损坏（修复语义，重抓覆盖）
        pending.append((t, c))

    print(f"[onehop] 勾选 {len(selected_titles)} 项，本轮待抓 {len(pending)} 页")
    batch = pending if limit is None else pending[:limit]
    if limit is not None and len(pending) > limit:
        print(f"[onehop] --limit {limit}：本轮只抓前 {limit} 页，"
              f"其余 {len(pending) - limit} 页留给下次续跑")
    for i, (t, c) in enumerate(batch, 1):
        print(f"[onehop] 进度 {i}/{len(batch)}：{t}", flush=True)
        preinfo = None
        if c.get("lastrevid"):
            preinfo = {"oldid": c["lastrevid"], "pageid": c.get("pageid"),
                       "title": c.get("canonical") or t,
                       "size_bytes": c.get("size_bytes") or 0}
            # crawl_page 内部走 1 次 parse 请求（15s 限速内建）
        crawl.crawl_page(c.get("canonical") or t, force=True, preinfo=preinfo)
    remaining = len(pending) - len(batch)
    print(f"[onehop] 本轮抓取 {len(batch)} 页，剩余待抓 {remaining} 页；"
          f"抓完后重跑 --list 刷新清单状态")
    return 0 if remaining == 0 else 2


# ---------------------------------------------------------------- 汇总

def print_status() -> None:
    mf_pages = manifest.read_manifest()["pages"]
    print(f"[onehop] manifest 在册 {len(mf_pages)} 页")
    if not CANDIDATES_JSON.is_file():
        print("[onehop] 候选清单尚未生成（--list）")
        return
    data = json.loads(CANDIDATES_JSON.read_text(encoding="utf-8"))
    sel = (load_selection() or {"selected": {}})["selected"]
    selected = [t for t, on in sel.items() if on]
    done = 0
    for t in selected:
        c = _lookup(data, t)
        canonical = (c or {}).get("canonical") or t
        entry = mf_pages.get(canonical)
        if entry and entry.get("raw_file") and \
                (config.REPO_ROOT / entry["raw_file"]).is_file():
            done += 1
    print(f"[onehop] 清单生成于 {data['generated_at']}：候选 "
          f"{len(data['candidates'])} / 命中已抓 {len(data['covered'])} / "
          f"不存在 {len(data['missing'])}")
    print(f"[onehop] 勾选 {len(selected)} 项，其中已入 manifest {done} 项，"
          f"待抓 {len(selected) - done} 项")


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):       # Windows 控制台中文安全输出
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="工单05：一跳候选清单与补抓")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--list", action="store_true", help="生成候选清单（默认动作）")
    g.add_argument("--crawl", action="store_true", help="补抓勾选页（增量）")
    g.add_argument("--status", action="store_true", help="打印汇总状态")
    g.add_argument("--select", nargs="+", metavar="TITLE",
                   help="勾选一个或多个候选标题")
    g.add_argument("--unselect", nargs="+", metavar="TITLE", help="取消勾选")
    ap.add_argument("--offline", action="store_true",
                    help="（--list）纯离线枚举，不联网核实大小/存在性")
    ap.add_argument("--refresh-info", action="store_true",
                    help="（--list）忽略缓存重查全部标题信息")
    ap.add_argument("--max-info-requests", type=int, default=0, metavar="N",
                    help="（--list）本轮最多 N 次 prop=info 批量请求"
                         "（0=不限），超出部分下次续查")
    ap.add_argument("--limit", type=int, default=None, metavar="N",
                    help="（--crawl）本轮最多抓 N 页，剩余下次续跑")
    args = ap.parse_args(argv)

    config.ensure_dirs()
    if args.select or args.unselect:
        sel = (load_selection() or {"selected": {}})["selected"]
        known = set()
        if CANDIDATES_JSON.is_file():
            known = {c["title"] for c in json.loads(
                CANDIDATES_JSON.read_text(encoding="utf-8"))["candidates"]}
        for t in args.select or []:
            sel[t] = True
            if t not in known:
                print(f"[onehop] 提示：{t} 不在当前候选清单，已记录；"
                      f"下次 --list 若出现则可抓")
        for t in args.unselect or []:
            sel.pop(t, None)
        save_selection(sel)
        print(f"[onehop] 勾选已更新（共 {sum(1 for v in sel.values() if v)} 项）"
              f"-> {SELECTION_PATH.name}")
        return 0
    if args.crawl:
        return crawl_selected(limit=args.limit)
    if args.status:
        print_status()
        return 0
    generate_list(offline=args.offline, refresh_info=args.refresh_info,
                  max_info_requests=args.max_info_requests)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
