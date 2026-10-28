# -*- coding: utf-8 -*-
r"""工单03：表格知识零丢失抽查——raw 表格行 → 清洗产物逐字命中验证。

思路：以 raw JSON 的表格单元格文字（源真相）为针，在 pages/<页>.md 中找
单行完整命中（该行含该行全部单元格文字）。行内强调字符（** ` 等）与
管道转义在匹配前归一化，避免排版差异误报。

内置 4 例（工单03 验收）：Effects 主表 3 行 + Culture modding 嵌套表首行。
可扩展：python tests/spotcheck_tables.py --needle "<页名>" "<任意文字>"

运行（仓库根）：
    python tests\spotcheck_tables.py
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from bs4 import BeautifulSoup  # noqa: E402

from lib import config, manifest  # noqa: E402


def collapse(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def read_page_text(page: str) -> str:
    """读页面全文：拆分页（organize.split，工单04）= 索引 + 全部章节文件拼接。"""
    entry = manifest.read_manifest()["pages"].get(page)
    parts = [(config.PAGES_DIR / f"{page}.md").read_text(encoding="utf-8")]
    org = (entry or {}).get("organize") or {}
    if org.get("split"):
        for p in sorted((config.REPO_ROOT / org["chapter_dir"]).glob("*.md")):
            parts.append(p.read_text(encoding="utf-8"))
    return "\n".join(parts)


def normalize_md_line(ln: str) -> str:
    """md 行归一化：去行内强调符号、还原管道转义，便于与 raw 文字比对。"""
    ln = ln.replace("\\|", "|")
    ln = re.sub(r"(\*\*|\*|`)", "", ln)
    return collapse(ln)


def row_needles(table: BeautifulSoup, row_idx: int) -> list[str]:
    """取表格第 row_idx 行全部单元格文字（源真相针）。"""
    trs = [t for t in table.find_all("tr") if not t.find_parent("tr")]
    cells = trs[row_idx].find_all(["th", "td"])
    return [collapse(c.get_text()) for c in cells if collapse(c.get_text())]


def check_row(page: str, needles: list[str], desc: str) -> bool:
    md = read_page_text(page)
    lines = [normalize_md_line(l) for l in md.splitlines()]
    hit = any(all(n in ln for n in needles) for ln in lines)
    print(f"{'PASS' if hit else 'FAIL'}  {page} · {desc}"
          + ("" if hit else f"  —— 未命中行，针={needles}"))
    return hit


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="表格知识零丢失抽查")
    ap.add_argument("--needle", nargs=2, metavar=("页名", "文字"),
                    help="自定义抽查：页名 + 任意文字（可多次）", action="append")
    args = ap.parse_args(argv)

    ok = True

    # 克隆模式：默认抽查的"针"来自 raw/（不发布）。--needle 自定义针只读 pages/，
    # 克隆下仍可用。用文件而非目录判断（catalog.py 的 ensure_dirs 会创建空 raw/）。
    if not args.needle and not any(config.RAW_DIR.glob("*.json")):
        print("SKIP  内置抽查（克隆模式：raw/ 不发布，针不可构造）。"
              "自定义针仍可用：python tests/spotcheck_tables.py --needle <页名> <文字>")
        print("汇总：SKIP（克隆模式）")
        return 0

    if not args.needle:
        # 内置 4 例：Effects 主表（Name|Description|Usage|…）行 1/2 + 第二表行 1，
        # Culture modding 首张嵌套表行 1（嵌套内联形态）
        e_html = json.loads((config.RAW_DIR / "Effects.json")
                            .read_text(encoding="utf-8"))["parse"]["text"]
        e_soup = BeautifulSoup(e_html, "html.parser")
        tables = [t for t in e_soup.find_all("table") if not t.find_parent("table")]
        ok &= check_row("Effects", row_needles(tables[0], 1), "主表行1（if 效果整行）")
        ok &= check_row("Effects", row_needles(tables[0], 2), "主表行2（整行）")
        ok &= check_row("Effects", row_needles(tables[1], 1), "第二表行1（整行）")

        c_html = json.loads((config.RAW_DIR / "Culture modding.json")
                            .read_text(encoding="utf-8"))["parse"]["text"]
        c_soup = BeautifulSoup(c_html, "html.parser")
        nested = next(t for t in c_soup.find_all("table") if t.find_parent("table"))
        # 注意：嵌套表 tr 的祖先链会经过父表的 tr，不能按 find_parent("tr") 过滤，
        # 直接取该表自身的全部 tr
        tr1 = nested.find_all("tr")[1]
        cells = [collapse(c.get_text()) for c in tr1.find_all(["th", "td"])]
        # 嵌套表行内联进父单元格：三列以「 / 」连接为单行，全部列文字同现一行
        ok &= check_row("Culture modding", cells, "嵌套表首行（Parameter|Type|Description 内联）")

    for page, text in args.needle or []:
        ok &= check_row(page, [text], f"自定义针：{text[:40]}")

    print(f"汇总：{'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    raise SystemExit(main())
