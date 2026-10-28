# -*- coding: utf-8 -*-
"""质量门：对管线产物做外部行为断言（不测内部函数，只检查磁盘产物）。

断言组（对应 spec 测试决策"自动化质量门"）：
A. 四件套一致性：manifest 每页都有 raw JSON、pages md、catalog 条目
B. 清洗产物：非空、有 H1、无站点噪声特征串
C. 版本横幅：manifest 记录了标注版本的页，横幅信息应出现在清洗产物中
D. raw JSON 可解析且含 parse.text（重放清洗的前提）
E. 拆分一致性（工单04）：拆分页的索引/章节文件/manifest 登记一一对应

任何一条 FAIL → 退出码 1（可接 CI）。
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib import config, manifest  # noqa: E402

# 站点噪声特征串：清洗产物中一律不得出现
# （前四个来自工单验收项，其余为导航菜单/页脚类特征的补充）
NOISE_MARKERS = [
    "Active Wikis",        # 站点侧栏"活跃 wiki"栏
    "编辑源代码",           # [编辑|编辑源代码] 按钮（中文界面形态）
    "[edit",               # [edit] 按钮（英文界面形态）
    "[编辑",               # [编辑] 按钮
    "Navigation menu",     # 导航菜单
    "导航菜单",             # 导航菜单（中文）
    "Print/export",        # 侧栏打印/导出栏
    "Personal tools",      # 侧栏个人工具栏
    "mw-editsection",      # 编辑按钮的 class 残留
]


class Result:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def check(self, ok: bool, label: str, detail: str = "") -> None:
        mark = "PASS" if ok else "FAIL"
        line = f"[gate] {mark}  {label}"
        if detail and not ok:
            line += f"  —— {detail}"
        print(line, flush=True)
        if ok:
            self.passed += 1
        else:
            self.failed += 1


def run_gate(page: str | None = None) -> int:
    res = Result()
    data = manifest.read_manifest()
    pages = [page] if page else list(data["pages"])
    if not pages:
        print("[gate] FAIL  manifest 中没有任何页面记录")
        return 1

    catalog_text = (config.CATALOG_PATH.read_text(encoding="utf-8")
                    if config.CATALOG_PATH.is_file() else "")

    # 克隆模式：raw/ 原始存档不随仓库发布（合规与体积决策），克隆用户没有它。
    # raw 完整性检查属维护者侧验证，此时整体跳过并明示，而非报 141 项 FAIL。
    # 注意用"文件存在"而非"目录存在"判断——catalog.py 的 ensure_dirs 会创建空 raw/。
    clone_mode = not any(config.RAW_DIR.glob("*.json"))
    if clone_mode:
        print("[gate] 克隆模式：raw/ 不存在（原始存档不发布），跳过 raw 完整性检查")

    for title in pages:
        entry = data["pages"].get(title)
        res.check(entry is not None, f"{title}: manifest 有记录")

        # A/D. raw JSON 存在、可解析、含正文（克隆模式跳过）
        raw_path = (config.REPO_ROOT / entry["raw_file"]
                    if entry and entry.get("raw_file") else None)
        ok = (raw_path is not None and raw_path.is_file()
              and raw_path.stat().st_size > 0)
        if clone_mode:
            pass  # 见顶部说明
        else:
            res.check(ok, f"{title}: raw JSON 存在且非空")
            if ok:
                try:
                    raw = json.loads(raw_path.read_text(encoding="utf-8"))
                    ok = "parse" in raw and "text" in raw["parse"]
                    res.check(ok, f"{title}: raw 含 parse.text（可重放清洗）")
                except json.JSONDecodeError as exc:
                    res.check(False, f"{title}: raw 是合法 JSON", str(exc))

        # A. 清洗产物存在且非空
        cleaned_path = (config.REPO_ROOT / entry["cleaned_file"]
                        if entry and entry.get("cleaned_file") else None)
        ok = (cleaned_path is not None and cleaned_path.is_file()
              and cleaned_path.stat().st_size > 0)
        res.check(ok, f"{title}: 清洗 md 存在且非空")
        if not ok:
            continue  # 后续检查都依赖 md，跳过

        md = cleaned_path.read_text(encoding="utf-8")
        # 拆分页（工单04）：cleaned_file 是章节索引，正文在 pages/<页名>/ 章节文件。
        # 版本横幅/噪声检查需要覆盖全文——索引 + 全部章节文件拼接。
        org = (entry or {}).get("organize") or {}
        if org.get("split"):
            chapter_dir = config.REPO_ROOT / org["chapter_dir"]
            extra = "".join(p.read_text(encoding="utf-8")
                            for p in sorted(chapter_dir.glob("*.md")))
            full_text_for_scan = md + "\n" + extra
        else:
            full_text_for_scan = md
        md_lines = md.splitlines()

        # B. H1 存在（ATX 形态，代码围栏内不算）
        in_code = False
        h1 = False
        for ln in md_lines:
            if ln.strip().startswith("```"):
                in_code = not in_code
                continue
            if not in_code and re.match(r"^# ", ln):
                h1 = True
                break
        res.check(h1, f"{title}: 有 H1")

        # B. 噪声特征串缺失（拆分页对全文扫描：索引 + 章节文件）
        hits = [m for m in NOISE_MARKERS if m in full_text_for_scan]
        res.check(not hits, f"{title}: 无站点噪声特征串", f"命中：{hits}")

        # C. 版本横幅信息保留（manifest 记录了标注版本时；拆分页横幅可能在
        # 任一章节文件里，如 CK3AGOT 的版本号在 Patches 章节正文，故查全文）
        gv = entry.get("game_version") if entry else None
        if gv:
            res.check(gv in full_text_for_scan,
                      f"{title}: 版本标注「{gv}」保留在清洗产物中")

        # A. catalog 条目覆盖
        marker = f"ck3wiki-mod-kb:entry BEGIN {title}"
        res.check(marker in catalog_text, f"{title}: catalog 有条目")

        # E. 拆分一致性（organize 产物，工单04）：索引/章节文件/manifest 一一对应
        org = (entry or {}).get("organize") or {}
        if org.get("split"):
            cdir = config.REPO_ROOT / org["chapter_dir"]
            on_disk = sorted(p.name for p in cdir.glob("*.md")) if cdir.is_dir() else []
            in_manifest = sorted(Path(c["file"]).name for c in org["chapters"]
                                 ) + sorted(Path(s["file"]).name
                                            for c in org["chapters"] for s in c["subs"]
                                            if s.get("file"))
            res.check(on_disk == in_manifest, f"{title}: 章节文件与登记一一对应（无孤儿）",
                      f"盘上多={set(on_disk) - set(in_manifest)} 登记多={set(in_manifest) - set(on_disk)}")
            res.check(bool(on_disk) and len(on_disk) > 0, f"{title}: 章节目录非空")
            idx_text = md  # 此处 md 已是索引文件内容（cleaned_file 指向索引）
            missing = [n for n in in_manifest if n not in idx_text]
            res.check(not missing, f"{title}: 索引列出全部章节文件", f"缺：{missing}")
            res.check(bool(org.get("reassembled_ok")),
                      f"{title}: 拆分重组校验标记通过")

    print(f"[gate] 汇总：PASS {res.passed} / FAIL {res.failed}")
    return 0 if res.failed == 0 else 1


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):       # Windows 控制台中文安全输出
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="质量门：产物断言")
    ap.add_argument("--page", help="只检查指定页（默认 manifest 全部页）")
    args = ap.parse_args(argv)
    return run_gate(args.page)


if __name__ == "__main__":
    raise SystemExit(main())
