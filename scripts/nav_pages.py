# -*- coding: utf-8 -*-
"""工单02：从已抓页面的 raw 存档推导 Modding 导航模板页面清单（确定性、可离线重放）。

来源（spec 已核查事实）：
- raw/Scripting.json 是 api.php?action=parse 的原始 HTML，页面底部含
  Modding 导航框（七类：Documentation/Scripting/Interface/Map/Graphics/
  Audio/Other）。清洗阶段会剥离导航框，但 raw 存档里有——从这里提取。
- 红链（不存在的页面）识别特征（三选一即红链，本站实测为 class="new" +
  href 含 redlink=1 / action=edit）：剔除不入清单。

交叉核对（只取"页面标题"这一事实信息，不采用参考合集任何文本内容）：
- 参考合集 _reference/skillset/Skills-for-.../ck3reference/Reference/ck3modwiki/
  下的 ck3.paradoxwikis.com_<标题>.md 文件名集合。差异只报告不解决
  （参考合集独有的页面属 spec 的"种子补充"批次，不在本工单抓取范围）。

产物：scripts/state/nav_pages.json（原子写）：
- crawl_order：抓取顺序（Effects 置顶——工单03需要它的 raw 做金样本；
  其余按导航框出现顺序）；
- pages：逐页 {title(规范标题，空格分隔), display, category, href}；
- redlinks：剔除的红链及原因；
- cross_check：与参考合集差集（两个方向）。

用法：
    python scripts/nav_pages.py                 # 推导并落盘 + 打印报告
    python scripts/nav_pages.py --source-page Scripting   # 换源页（默认 Scripting）
"""
import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from bs4 import BeautifulSoup  # noqa: E402

from lib import config  # noqa: E402

# 工单03 金样本页：抓取时排最前，即使批次中断也保证它先落地
PRIORITY_PAGES = ["Effects"]

# 参考合集页面文件目录（只读取文件名；目录缺失则交叉核对标记 skipped）
REFERENCE_WIKI_DIR = (REPO_REF := config.REPO_ROOT / "_reference" / "skillset"
                      / "Skills-for-CrusaderKing3-Modding-main" / "ck3reference"
                      / "Reference" / "ck3modwiki")
REFERENCE_FILE_RE = re.compile(r"^ck3\.paradoxwikis\.com_(.+)\.md$")

# 导航清单落盘位置（scripts/state/，运行时状态，不属于发布产物）
NAV_PAGES_PATH = config.STATE_DIR / "nav_pages.json"


def _find_navbox(html: str):
    """在 parse HTML 中定位底部 Modding 导航框。

    识别特征与 lib/cleaner.py 剥离逻辑一致：div[style*="border-collapse"]
    且首个链接指向 /Modding。
    """
    soup = BeautifulSoup(html, "html.parser")
    navbox = None
    for div in soup.find_all("div"):
        if div.decomposed:
            continue
        style = div.get("style") or ""
        if "border-collapse" not in style:
            continue
        first_a = div.find("a")
        if first_a is not None and (first_a.get("href") == "/Modding"
                                    or first_a.get("title") == "Modding"):
            navbox = div  # 保留最后一个匹配（页底导航框）
    return navbox


def _is_redlink(a) -> bool:
    """红链判定：class 含 new / href 含 redlink=1 / action=edit（三选一）。"""
    classes = a.get("class") or []
    href = a.get("href") or ""
    return ("new" in classes or "redlink=1" in href or "action=edit" in href)


def extract_nav_pages(html: str) -> tuple[list[dict], list[dict], list[str]]:
    """解析导航框 → (页面清单, 红链清单, 栏目名列表)。

    页面 title 取 <a title="...">（MediaWiki 规范标题，空格分隔）；
    selflink（当前页自身，无 href）取链接文字兜底。
    """
    navbox = _find_navbox(html)
    if navbox is None:
        raise RuntimeError("未在 HTML 中找到 Modding 导航框"
                           "（div[style*=border-collapse] 且首链指向 /Modding）")
    pages: list[dict] = []
    redlinks: list[dict] = []
    categories: list[str] = []
    seen_titles: set[str] = set()
    for table in navbox.find_all("table"):
        tds = table.find_all("td")
        if len(tds) < 2:
            continue
        category = tds[0].get_text(strip=True)
        if category not in categories:
            categories.append(category)
        for a in tds[1].find_all("a"):
            href = a.get("href") or ""
            display = a.get_text(strip=True)
            # 规范标题：优先 title 属性；selflink（无 href 无 title）用文字
            title = a.get("title") or display
            if not title:
                continue
            if _is_redlink(a):
                # 红链 <a title> 带站点后缀，剥离后保留纯标题便于阅读
                red_title = re.sub(r"\s*\(page does not exist\)\s*$", "", title)
                redlinks.append({"title": red_title, "display": display,
                                 "category": category, "href": href})
                continue
            # 只收站内链接（防御：外部链接不进抓取清单）
            if href and not href.startswith("/"):
                continue
            if title in seen_titles:    # 同页多栏目重复链接去重（保首个）
                continue
            seen_titles.add(title)
            pages.append({"title": title, "display": display,
                          "category": category, "href": href})
    return pages, redlinks, categories


def reference_titles() -> tuple[list[str], bool]:
    """读参考合集文件名集合 → (标题列表(空格分隔), 目录是否存在)。"""
    if not REFERENCE_WIKI_DIR.is_dir():
        return [], False
    titles = []
    for f in sorted(REFERENCE_WIKI_DIR.glob("*.md")):
        m = REFERENCE_FILE_RE.match(f.name)
        if m:
            titles.append(m.group(1).replace("_", " "))
    return titles, True


def build_nav_manifest(source_page: str = "Scripting") -> dict:
    """推导完整导航清单（含交叉核对），返回待落盘的 dict。"""
    # 源页 raw 存档：按 safe_filename 定位（命名约定见 docs/pipeline.md §2；
    # 源页 Scripting 的标题无重定向，文件名与标题一致）
    raw_path = config.RAW_DIR / (config.safe_filename(source_page) + ".json")
    if not raw_path.is_file():
        raise SystemExit(
            f"[nav_pages] 源页 raw 存档不存在：{raw_path}，请先抓取 {source_page}")
    raw = json.loads(raw_path.read_text(encoding="utf-8"))
    html = raw["parse"]["text"]

    pages, redlinks, categories = extract_nav_pages(html)

    # 抓取顺序：优先页置顶，其余保持导航框顺序
    order = list(PRIORITY_PAGES) + [p["title"] for p in pages
                                    if p["title"] not in PRIORITY_PAGES]

    # ---- 交叉核对（只取页面标题事实信息；差异只报告不解决）----
    ref_titles, ref_exists = reference_titles()
    if ref_exists:
        nav_set = {p["title"] for p in pages}
        in_nav_not_in_ref = sorted(nav_set - set(ref_titles))
        in_ref_not_in_nav = sorted(set(ref_titles) - nav_set)
    else:
        in_nav_not_in_ref = in_ref_not_in_nav = None

    return {
        "schema_version": 1,
        "derived_from": f"raw/{raw_path.name}",
        "derived_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "categories": categories,
        "pages": pages,
        "redlinks": redlinks,
        "crawl_order": order,
        "cross_check": {
            "reference_dir": str(REFERENCE_WIKI_DIR.relative_to(config.REPO_ROOT)),
            "reference_found": ref_exists,
            "reference_page_count": len(ref_titles) if ref_exists else 0,
            "in_nav_not_in_reference": in_nav_not_in_ref,
            "in_reference_not_in_nav": in_ref_not_in_nav,
        },
    }


def write_nav_manifest(data: dict) -> Path:
    """原子落盘（临时文件 + os.replace，与 lib/manifest.py 同款策略）。"""
    config.ensure_dirs()
    tmp = NAV_PAGES_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n",
                   encoding="utf-8", newline="\n")
    os.replace(tmp, NAV_PAGES_PATH)
    return NAV_PAGES_PATH


def load_nav_pages(derive_if_missing: bool = True,
                   source_page: str = "Scripting") -> dict:
    """读取导航清单；缺失时（可选）现场推导。crawl.py 批量模式复用本入口。"""
    if NAV_PAGES_PATH.is_file():
        return json.loads(NAV_PAGES_PATH.read_text(encoding="utf-8"))
    if not derive_if_missing:
        raise SystemExit(f"[nav_pages] 导航清单不存在：{NAV_PAGES_PATH}"
                         "（先运行 python scripts/nav_pages.py）")
    print("[nav_pages] 导航清单缺失，现场推导…")
    data = build_nav_manifest(source_page)
    write_nav_manifest(data)
    return data


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):       # Windows 控制台中文安全输出
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(
        description="推导 Modding 导航模板页面清单（离线，从 raw 存档）")
    ap.add_argument("--source-page", default="Scripting",
                    help="导航框来源页（默认 Scripting，须已抓取）")
    args = ap.parse_args(argv)

    data = build_nav_manifest(args.source_page)
    path = write_nav_manifest(data)

    # ---- 报告 ----
    per_cat: dict[str, int] = {}
    for p in data["pages"]:
        per_cat[p["category"]] = per_cat.get(p["category"], 0) + 1
    print(f"[nav_pages] 栏目（{len(data['categories'])} 类）：{data['categories']}")
    print(f"[nav_pages] 有效页面 {len(data['pages'])} 页，分布：")
    for cat, n in per_cat.items():
        print(f"[nav_pages]   {cat}: {n}")
    print(f"[nav_pages] 剔除红链 {len(data['redlinks'])} 个：")
    for r in data["redlinks"]:
        print(f"[nav_pages]   {r['title']}（栏目 {r['category']}，href={r['href']}）")
    cc = data["cross_check"]
    if cc["reference_found"]:
        print(f"[nav_pages] 交叉核对参考合集（{cc['reference_page_count']} 页标题）：")
        print(f"[nav_pages]   导航有/参考无（{len(cc['in_nav_not_in_reference'])}）："
              f"{cc['in_nav_not_in_reference']}")
        print(f"[nav_pages]   参考有/导航无（{len(cc['in_reference_not_in_nav'])}）："
              f"{cc['in_reference_not_in_nav']}")
    else:
        print(f"[nav_pages] 参考合集目录缺失，交叉核对跳过：{cc['reference_dir']}")
    print(f"[nav_pages] 抓取顺序（前 5）：{data['crawl_order'][:5]} …")
    print(f"[nav_pages] 清单已落盘：{path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
