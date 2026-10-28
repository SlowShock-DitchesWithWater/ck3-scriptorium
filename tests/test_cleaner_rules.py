# -*- coding: utf-8 -*-
r"""工单03：清洗规则 → 断言映射测试（全部用真实 raw 夹具，不用人造 HTML）。

运行（仓库根）：
    python tests/test_cleaner_rules.py
退出码 0 = 全部通过（或克隆模式下全部跳过/通过）；任一 FAIL 退出 1。

克隆模式：raw/ 原始存档不随仓库发布——依赖 raw 的分区自动 SKIP 并明示；
金样本夹具（tests/fixtures/，已发布）驱动的分区照常运行。
零网络保证：不导入 session/requests/selenium。
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from bs4 import BeautifulSoup  # noqa: E402

from lib import config  # noqa: E402
from lib.cleaner import clean_html, _prune  # noqa: E402

REPO = config.REPO_ROOT
FIX = REPO / "tests" / "fixtures"
# 克隆模式 = raw/ 无实际存档（用文件而非目录判断：catalog.py 的 ensure_dirs
# 会创建空 raw/ 目录）
RAW_AVAILABLE = any(config.RAW_DIR.glob("*.json"))

_passed = 0
_failed = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global _passed, _failed
    print(f"{'PASS' if ok else 'FAIL'}  {label}" + (f"  —— {detail}" if not ok and detail else ""))
    _passed, _failed = _passed + (1 if ok else 0), _failed + (0 if ok else 1)


def skip(label: str) -> None:
    print(f"SKIP  {label}（克隆模式：raw/ 不发布）")


def load_raw(title: str) -> dict | None:
    """读 raw/<页>.json；克隆模式（raw/ 不存在）返回 None。"""
    p = config.RAW_DIR / f"{title}.json"
    if not p.is_file():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


def render(title: str, html: str) -> tuple[str, object]:
    return clean_html(title, html)


def md_lines_outside_fences(md: str) -> list[str]:
    """代码围栏外的行（围栏内逐字内容不参与标题/表格类断言）。"""
    out, in_code = [], False
    for ln in md.splitlines():
        if ln.strip().startswith("```"):
            in_code = not in_code
            continue
        if not in_code:
            out.append(ln)
    return out


def main() -> int:
    # ---------- 金样本夹具：Scripting（小页）与 Effects（巨页）——克隆模式可用 ----------
    for title in ("Scripting", "Effects"):
        raw = json.loads((FIX / f"{title}.json").read_text(encoding="utf-8"))
        html = raw["parse"]["text"]
        md, stats = render(title, html)

        # 〔剥离〕〔编辑|编辑源代码〕按钮：有得剥 + 产物零残留
        check(f"{title}〔剥离·编辑按钮〕剥计数>0 且无残留",
              stats.pruned_editsections > 0
              and "编辑源代码" not in md and "[edit" not in md,
              f"pruned={stats.pruned_editsections}")

        # 〔剥离〕Modding 导航框
        check(f"{title}〔剥离·导航框〕剥计数≥1 且无 'Active Wikis'",
              stats.pruned_navboxes >= 1 and "Active Wikis" not in md,
              f"pruned={stats.pruned_navboxes}")

        # 〔剥离〕图片：产物无 Markdown 图片语法与 img 标签
        check(f"{title}〔剥离·图片〕无 '![' 与 '<img'", "![" not in md and "<img" not in md)

        # 〔剥离〕分类标签：catlinks 若存在于 raw，其标题不成行出现
        soup = BeautifulSoup(html, "html.parser")
        cat = soup.find("div", class_="catlinks")
        cat_ok = cat is None or not any(
            ln.strip() in ("Categories", "分类") for ln in md.splitlines())
        check(f"{title}〔剥离·分类标签〕分类栏标题不成行出现", cat_ok)

        # 〔保留〕标题层级：_prune 后 soup 的非空 h2/h3/h4 数 == md 围栏外对应行数
        _prune(soup)
        for tag, prefix in (("h2", "## "), ("h3", "### "), ("h4", "#### ")):
            want = sum(1 for h in soup.find_all(tag) if h.get_text(strip=True))
            got = sum(1 for ln in md_lines_outside_fences(md) if ln.startswith(prefix))
            check(f"{title}〔保留·标题层级〕{tag} 数 {want} == md {got}", want == got)

        # 〔保留〕链接只留文字：无 Markdown 链接语法、无残留 a/href
        check(f"{title}〔保留·链接只留文字〕无 '](' / '<a ' / 'href='",
              "](http" not in md and "<a " not in md and "href=" not in md)

        # 〔幂等〕同一输入两次清洗逐字节一致
        md2, _ = render(title, html)
        check(f"{title}〔幂等〕两次清洗逐字节一致", md == md2)

    # ---------- Scripting 专项（小页细节） ----------
    s_raw = load_raw("Scripting")
    if s_raw is None:
        skip("Scripting 专项（toc/横幅/段落）")
    else:
        s_html = s_raw["parse"]["text"]
        s_md, _ = render("Scripting", s_html)

        # 〔剥离〕站内目录框：toc 编号序列不成行出现（取 toc 前 5 项）
        soup = BeautifulSoup(s_html, "html.parser")
        toc = soup.find("div", id="toc")
        if toc is not None:
            entries = [a.get_text(strip=True) for a in toc.select("li a") if a.get_text(strip=True)]
            bad = [f"{i} {t}" for i, t in enumerate(entries[:5], 1)
                   if any(ln.strip() == f"{i} {t}" for ln in s_md.splitlines())]
            check("Scripting〔剥离·目录框〕toc 编号行零残留（raw 有 toc，前提成立）", not bad,
                  f"残留：{bad}")
        else:
            check("Scripting〔剥离·目录框〕raw 无 toc，跳过", True)

        # 〔保留〕版本横幅：timeless 标注 + 引用块形态
        check("Scripting〔保留·版本横幅〕timeless 在产物中且为 > [!] 引用块",
              "timeless" in s_md and "> [!]" in s_md)

        # 〔保留〕正文段落：_prune 后首个非空 <p> 的文字片段逐字在产物中
        soup2 = BeautifulSoup(s_html, "html.parser")
        _prune(soup2)
        first_p = next((p for p in soup2.find_all("p") if p.get_text(strip=True)), None)
        frag = re.sub(r"\s+", " ", first_p.get_text()).strip()[:60] if first_p else ""
        check("Scripting〔保留·正文段落〕首段 60 字逐字命中", bool(frag) and frag in s_md,
              f"frag={frag!r}")

    # ---------- Effects 专项（巨页知识负载） ----------
    e_raw = load_raw("Effects")
    if e_raw is None:
        skip("Effects 专项（代码逐字/表格形态）")
    else:
        e_html = e_raw["parse"]["text"]
        e_md, e_stats = render("Effects", e_html)

        # 〔保留〕代码块逐字：首个 <pre> 的前 3 行作为连续行原样出现
        pre0 = next(p for p in BeautifulSoup(e_html, "html.parser").find_all("pre"))
        lines0 = [l for l in pre0.get_text().strip().splitlines()[:3]]
        joined = "\n".join(lines0)
        check("Effects〔保留·代码块逐字〕pre[0] 前 3 行连续原样出现", joined in e_md,
              f"needle={lines0[:1]}")

        # 〔保留〕表格转管道表：effects 主表表头 + 分隔行
        check("Effects〔保留·表格·表头行〕Name|Description|Usage|Supported scopes|Supported targets",
              "| Name | Description | Usage | Supported scopes | Supported targets |" in e_md)
        check("Effects〔保留·表格·分隔行〕管道表分隔行存在",
              any(re.match(r"^\|( --- \|){2,}$", ln) for ln in e_md.splitlines()))
        check("Effects〔保留·表格·计数〕stats.tables>0", e_stats.tables > 0,
              f"tables={e_stats.tables}")

    # ---------- rowspan 展开（Localization modding，全库 rowspan 最多页） ----------
    l_raw = load_raw("Localization")
    if l_raw is None:
        skip("Localization〔展开·rowspan〕")
    else:
        l_soup = BeautifulSoup(l_raw["parse"]["text"], "html.parser")
        rs_cell = None
        for c in l_soup.find_all("td"):
            try:
                if int(c.get("rowspan", 1) or 1) > 1:
                    rs_cell = c
                    break
            except ValueError:
                continue
        l_md, _ = render("Localization", l_raw["parse"]["text"])
        if rs_cell is not None:
            span = int(rs_cell["rowspan"])
            text = re.sub(r"\s+", " ", rs_cell.get_text()).strip()
            hits = sum(1 for ln in l_md.splitlines()
                       if ln.startswith("| ") and text and text in ln)
            check(f"Localization〔展开·rowspan〕跨 {span} 行的分组值「{text[:24]}」"
                  f"在表格行出现 ≥{span} 次（行自包含）", hits >= span, f"hits={hits}")
        else:
            check("Localization〔展开·rowspan〕raw 无 rowspan，跳过", True)

    # ---------- 嵌套表内联（Culture modding，嵌套 Parameter 表页） ----------
    c_raw = load_raw("Culture modding")
    if c_raw is None:
        skip("Culture modding〔内联·嵌套表〕")
    else:
        c_soup = BeautifulSoup(c_raw["parse"]["text"], "html.parser")
        nested = next((t for t in c_soup.find_all("table") if t.find_parent("table")), None)
        c_md, _ = render("Culture modding", c_raw["parse"]["text"])
        if nested is not None:
            tr1 = nested.find_all("tr")[1]
            cells = [re.sub(r"\s+", " ", x.get_text()).strip()
                     for x in tr1.find_all(["th", "td"])]
            inline_form = (" / ".join(cells) if len(cells) != 2
                           else f"{cells[0]}: {cells[1]}")
            one_line = any(inline_form in ln for ln in c_md.splitlines())
            check(f"Culture modding〔内联·嵌套表〕嵌套首行「{inline_form[:40]}…」"
                  "完整出现在单行内（内容零丢失）", one_line)
        else:
            check("Culture modding〔内联·嵌套表〕raw 无嵌套表，跳过", True)

    # ---------- 脚注列表剥离（Bookmarks modding，含 ol.references 的页） ----------
    b_raw = load_raw("Bookmarks modding")
    if b_raw is None:
        skip("Bookmarks modding〔剥离·脚注列表〕")
    else:
        b_soup = BeautifulSoup(b_raw["parse"]["text"], "html.parser")
        refs = b_soup.select("ol.references li, div.reflist li")
        b_md, _ = render("Bookmarks modding", b_raw["parse"]["text"])
        if refs:
            first_ref = re.sub(r"\s+", " ", refs[0].get_text()).strip()[:50]
            check("Bookmarks modding〔剥离·脚注列表〕首条引用文字不入产物",
                  first_ref not in b_md, f"needle={first_ref!r}")
        else:
            check("Bookmarks modding〔剥离·脚注列表〕raw 无脚注列表，跳过", True)

    # ---------- 金样本回放机制（含扰动演示：改规则→diff 可审→还原→PASS） ----------
    sys.path.insert(0, str(REPO / "scripts"))
    import clean as clean_mod  # noqa: E402

    rc0 = clean_mod.replay_golden(update=False)
    check("回放〔机制〕未扰动规则时 PASS（退出码 0）", rc0 == 0)

    orig = clean_mod.clean_html

    # 扰动模拟「改规则」：产物尾部多一行注释（签名/返回形态与生产一致）
    def _perturbed(title, html, provenance=None):
        md, stats = orig(title, html, provenance=provenance)
        return md + "\n<!-- 规则扰动 -->\n", stats

    clean_mod.clean_html = _perturbed
    rc1 = clean_mod.replay_golden(update=False)
    clean_mod.clean_html = orig  # 还原
    rc2 = clean_mod.replay_golden(update=False)
    check("回放〔机制〕注入规则扰动后 FAIL（退出码 1，diff 已打印）", rc1 == 1)
    check("回放〔机制〕还原后复 PASS", rc2 == 0)

    # ---------- 零网络断言 ----------
    net = [m for m in sys.modules if m.split(".")[0] in ("requests", "selenium")
           or m.endswith("lib.session")]
    check("〔零网络〕全程未加载 requests/selenium/lib.session", not net, f"加载了：{net}")

    print(f"\n汇总：PASS {_passed} / FAIL {_failed}（规则→断言映射见上方标签；"
          f"{'raw/ 可用，全量运行' if RAW_AVAILABLE else '克隆模式，raw 依赖项已 SKIP'}）")
    return 0 if _failed == 0 else 1


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    raise SystemExit(main())
