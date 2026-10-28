# -*- coding: utf-8 -*-
r"""生成 docs/reports/clean_stats.md：每页清洗统计对照报告（spec 用户故事16）。

对照基线：scripts/state/clean_stats_baseline_03.json（工单03 规则改进前的
manifest clean_stats 快照）。基线缺失时只输出当轮统计，Δ 列留空。

运行（仓库根）：
    python scripts\clean_report.py
只读 manifest 与基线文件，写 docs/reports/clean_stats.md（可重复运行）。
"""
import json
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib import config, manifest  # noqa: E402

BASELINE = config.STATE_DIR / "clean_stats_baseline_03.json"
OUT = config.REPO_ROOT / "docs" / "reports" / "clean_stats.md"


def _delta(new, old):
    """带符号差值；基线缺失返回 ''。"""
    if old is None:
        return ""
    d = new - old
    return "0" if d == 0 else f"{d:+d}"


def main() -> None:
    data = manifest.read_manifest()
    baseline = (json.loads(BASELINE.read_text(encoding="utf-8"))
                if BASELINE.is_file() else {})
    rows = []
    n_changed = 0
    for title, e in data["pages"].items():
        st = e.get("clean_stats") or {}
        bs = (baseline.get(title) or {}).get("clean_stats") or {}
        changed = (baseline.get(title) or {}).get("cleaned_sha256") != e.get("cleaned_sha256")
        n_changed += bool(changed and baseline)
        rows.append({
            "title": title, "changed": changed,
            "html": st.get("html_bytes", 0),
            "md_old": bs.get("md_bytes"), "md_new": st.get("md_bytes", 0),
            "h2": (st.get("h2", 0), bs.get("h2")),
            "h3": (st.get("h3", 0), bs.get("h3")),
            "tables": (st.get("tables", 0), bs.get("tables")),
            "code": st.get("code_blocks", 0),
            "pe": st.get("pruned_editsections", 0),
            "pn": st.get("pruned_navboxes", 0),
        })

    now = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M")
    lines = [
        "# 清洗统计对照报告（clean_stats）",
        "",
        f"- 生成时间：{now}；页数：{len(rows)}（manifest pages 区全部条目）",
        f"- 对照基线：`scripts/state/clean_stats_baseline_03.json`"
        f"（工单03 表格规则精化前快照；基线存在的页中产物 sha 变化 {n_changed} 页）",
        "- 本轮规则变化（工单03）：表格行改为直属结构遍历（嵌套表不再并进父表）、"
        "rowspan 跨行值逐行重复展开、colspan 保持空列补齐、单元格内嵌套表压缩为"
        "内联文本（两列「键: 值」、多列「 / 」连接）、新增剥离脚注列表"
        "（div.reflist / ol.references，全库仅 Bookmarks/Characters 两页有）",
        "- Δ 列为 相对新规则 − 基线；`H2/H3/表` 列为 新(旧)",
        "",
        "| 页面 | html B | md B (旧) | md ΔB | H2 | H3 | 表 | 代码块 | 剥[编辑] | 剥导航框 | 规则后变化 |",
        "| --- | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- |",
    ]
    for r in sorted(rows, key=lambda x: x["title"].lower()):
        md_old = f"{r['md_old']}" if r["md_old"] is not None else "—"
        lines.append(
            f"| {r['title']} | {r['html']} | {r['md_new']} ({md_old}) "
            f"| {_delta(r['md_new'], r['md_old'])} "
            f"| {r['h2'][0]}({r['h2'][1] if r['h2'][1] is not None else '—'}) "
            f"| {r['h3'][0]}({r['h3'][1] if r['h3'][1] is not None else '—'}) "
            f"| {r['tables'][0]}({r['tables'][1] if r['tables'][1] is not None else '—'}) "
            f"| {r['code']} | {r['pe']} | {r['pn']} | {'是' if r['changed'] else '否'} |")
    lines += [
        "",
        "阅读提示：Δmd 为负且 H2/H3 不变的页多为脚注列表剥离（预期）；表格数"
        "变化的页是嵌套表不再重复计入父表或反之；`剥导航框` 每页 1 = 底部整只"
        "Modding 导航框（内含 7 张栏目表）。",
        "",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"[report] {len(rows)} 页 -> {OUT.relative_to(config.REPO_ROOT)}")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
