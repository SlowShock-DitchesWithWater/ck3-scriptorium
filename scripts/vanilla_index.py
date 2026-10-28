# -*- coding: utf-8 -*-
r"""原版结构索引层（工单08）：游戏目录 → `game_docs/vanilla_structure/`。

职责与边界（docs/spec.md、.scratch 工单08、docs/pipeline.md 契约）：
- 输入：本机游戏目录 `game\`（spec 环境事实附录；路径可用 --game-dir 覆盖），
  只读扫描，绝不修改游戏文件；
- 输出（全部为结构信息，零原版内容复制——产品中连 "{" 都不允许出现，
  详见 run() 的结构断言）：
  - `INDEX.md`：总索引（common 子目录摘要表、根散文件、查询用法）；
  - `common/<子目录>.md`：common 全部 128 个顶层子目录逐个的结构摘要
    （文件清单 + 每文件顶层块名/条目索引）——common 全覆盖是硬验收项；
  - `entry_map.tsv`：`条目名 \t 定义文件路径 \t 行号` 全局映射，
    查某 trait/opinion/... 定义在哪个文件可直接 grep 命中；
  - `other_dirs.md`：game\ 下其他内容目录（events/history/gui/gfx/...）
    的目录级概览（best-effort，不逐文件解析）；
- 解析：轻量自写 Jomini 顶层块扫描（标准库、字符状态机，处理注释/#、
  引号串/嵌套大括号/内联 [] 列表），只提取顶层块名与行号，不进入块体；
- manifest：登记快照日期、游戏版本、common 统计与全部产物内容指纹
  （指纹不变则快照日期不刷新，重扫描幂等）；
- 幂等：产物字节 = f(游戏目录内容, 游戏版本)，不含本次运行时间戳，
  排序确定化；连续两次扫描 diff 为空。

与 wiki 管线解耦；复用 lib.manifest（原子写）、lib.config（仓库根）、
game_layer（解码/原子写/哈希小助手）。零网络请求。

用法：
  python scripts/vanilla_index.py            # 扫描默认游戏目录并落盘
  python scripts/vanilla_index.py --check    # 只校验现有产物与盘上一致
  python scripts/vanilla_index.py --game-dir <dir> --out <dir> --no-manifest
"""
from __future__ import annotations

import argparse
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import config  # noqa: E402  只读复用：仓库根路径
from lib import manifest as manifest_lib  # noqa: E402  manifest 原子写助手
from game_layer import (  # noqa: E402  共享小助手（无副作用导入）
    _atomic_write, _now_iso, _sha256_bytes, decode_dump_text,
)

# ---- 常量 ---------------------------------------------------------------

REPO_ROOT = config.REPO_ROOT
# 游戏目录解析顺序（工单10：代码与 manifest 不得硬编码/登记本机绝对路径）：
# ① --game-dir 参数；② 环境变量 CK3_GAME_DIR；③ scripts/state/local_paths.json
# （本地配置，gitignored）的 game_dir 键。都没有则报错并给出上述三种配置方式。
DEFAULT_OUT_DIR = REPO_ROOT / "game_docs" / "vanilla_structure"
DEFAULT_GAME_VERSION = "1.20.0"   # spec 环境事实附录基准（私有文档）


def resolve_game_dir(cli_value: str | None) -> Path:
    """解析游戏 game/ 目录路径；找不到可用配置时报错退出（不猜测默认路径）。"""
    candidates: list[tuple[str, str]] = []
    if cli_value:
        candidates.append(("--game-dir 参数", cli_value))
    import json
    import os
    env = os.environ.get("CK3_GAME_DIR")
    if env:
        candidates.append(("环境变量 CK3_GAME_DIR", env))
    local_cfg = REPO_ROOT / "scripts" / "state" / "local_paths.json"
    if local_cfg.is_file():
        cfg = json.loads(local_cfg.read_text(encoding="utf-8"))
        if cfg.get("game_dir"):
            candidates.append((f"{local_cfg.name}（本地配置，不入库）", cfg["game_dir"]))
    for src, val in candidates:
        p = Path(val)
        if p.is_dir():
            return p
        print(f"[vanilla_index] 警告：{src} 指向的目录不存在：{val}")
    print("[vanilla_index] 错误：未找到可用的游戏目录。请用以下任一方式配置：\n"
          "  1) python scripts/vanilla_index.py --game-dir \"<CK3安装目录>\\game\"\n"
          "  2) set CK3_GAME_DIR=<CK3安装目录>\\game\n"
          "  3) 在 scripts/state/local_paths.json 写 {\"game_dir\": \"<路径>\"}"
          "（该文件已 gitignore，适合本机长期使用）")
    raise SystemExit(2)

PARSE_EXTS = {".txt"}             # 做 Jomini 顶层块解析的扩展名
# 文件清单逐文件列出的阈值：超过则只给目录级统计（结构信息体积控制）
LIST_FILES_THRESHOLD = 1000
# 永不逐文件列出的目录（二进制等，无导航价值）
NO_LIST_DIRS = {"binaries"}


# ---- Jomini 顶层块扫描（轻量状态机，标准库实现）--------------------------

def parse_jomini_toplevel(text: str) -> tuple[list[tuple[str, int]], int]:
    """提取顶层块名：返回 ([(块名, 起始行号 1 基), ...], 顶层标量键数)。

    只在深度 0 识别 `标识符 = {` 形态；块体（深度 > 0）仅计数花括号不读
    内容。处理：`#` 行注释、双引号字符串（含 \\ 转义与串内 {}/#）、
    内联 `[ ... ]` 列表、`=` 与 `{` 跨行。识别符字符集：除空白与
    结构符 `={}#[]"` 外均可（覆盖 e_france、NDefines、$VAR$ 等）。
    """
    entries: list[tuple[str, int]] = []
    scalars = 0
    i, n = 0, len(text)
    line = 1
    depth = 0        # {} 深度
    bracket = 0      # [] 深度
    in_str = in_comment = False
    while i < n:
        c = text[i]
        if c == "\n":
            line += 1
            in_comment = False
            i += 1
            continue
        if in_comment:
            i += 1
            continue
        if in_str:
            if c == "\\":
                # 转义：跳过下一字符（\" 等）；被转义的换行也计行
                if i + 1 < n and text[i + 1] == "\n":
                    line += 1
                i += 2
                continue
            if c == '"':
                in_str = False
            i += 1
            continue
        if c == "#":
            in_comment = True
            i += 1
            continue
        if c == '"':
            in_str = True
            i += 1
            continue
        if bracket > 0:                # 内联列表内：只管 [] 配对
            if c == "[":
                bracket += 1
            elif c == "]":
                bracket -= 1
            i += 1
            continue
        if depth > 0:                  # 块体内：只管 {} 配对（零内容读取）
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
            elif c == "[":
                bracket += 1
            i += 1
            continue
        # ---- 深度 0：识别 `标识符 = {` ----
        if c in " \t\r":
            i += 1
            continue
        if c == "[":
            bracket += 1
            i += 1
            continue
        if c in "=}":                  # 游离符号（畸形/续行残留），跳过
            i += 1
            continue
        if c == "{":                   # 匿名块
            depth += 1
            i += 1
            continue
        # 读标识符
        j = i
        while j < n and text[j] not in ' \t\r\n={}#[]"':
            j += 1
        ident = text[i:j]
        ident_line = line
        i = j
        # 前看：跳过空白/注释/换行后是否 '='，再之后是否 '{'
        k = i
        nl = 0
        while k < n and (text[k] in " \t\r" or text[k] == "\n"
                         or text[k] == "#"):
            if text[k] == "\n":
                nl += 1
                k += 1
            elif text[k] == "#":
                while k < n and text[k] != "\n":
                    k += 1
            else:
                k += 1
        if k < n and text[k] == "=":
            k += 1
            k2 = k
            while k2 < n and (text[k2] in " \t\r" or text[k2] == "\n"
                              or text[k2] == "#"):
                if text[k2] == "\n":
                    nl += 1
                    k2 += 1
                elif text[k2] == "#":
                    while k2 < n and text[k2] != "\n":
                        k2 += 1
                else:
                    k2 += 1
            if k2 < n and text[k2] == "{":
                entries.append((ident, ident_line))   # 命中顶层块
                depth += 1
                line += nl
                i = k2 + 1
                continue
            scalars += 1                             # 顶层标量赋值
            if k2 < n and text[k2] == "[":
                bracket += 1
            line += nl
            i = k2
            continue
        # 无 '=' 跟随：裸词（文档行/游离名），忽略
        line += nl
        i = max(i, k)
    return entries, scalars


# ---- 扫描数据结构 ---------------------------------------------------------

@dataclass
class FileInfo:
    rel: str                      # 相对所在顶层子目录的 posix 路径
    size: int
    entries: list[tuple[str, int]] = field(default_factory=list)
    scalars: int = 0
    parsed: bool = False          # 是否做了 Jomini 解析
    note: str = ""                # 未解析原因（扩展名说明）


@dataclass
class SubdirInfo:
    name: str                     # 顶层子目录名
    files: list[FileInfo] = field(default_factory=list)

    @property
    def file_count(self) -> int:
        return len(self.files)

    @property
    def entry_count(self) -> int:
        return sum(len(f.entries) for f in self.files)

    @property
    def unique_entries(self) -> int:
        return len({e[0] for f in self.files for e in f.entries})


def scan_common(common_dir: Path) -> tuple[list[SubdirInfo], list[FileInfo]]:
    """扫描 common\\：返回 (顶层子目录列表[按名排序], 根散文件列表)。

    每个子目录递归收集文件；.txt 做 Jomini 顶层块解析，其余仅登记。
    """
    subdirs: list[SubdirInfo] = []
    loose: list[FileInfo] = []
    if not common_dir.is_dir():
        raise FileNotFoundError(f"游戏目录不存在：{common_dir}")
    for child in sorted(common_dir.iterdir(), key=lambda p: p.name.lower()):
        if child.is_dir():
            info = SubdirInfo(name=child.name)
            for f in sorted(child.rglob("*"), key=lambda p: p.as_posix().lower()):
                if f.is_file():
                    info.files.append(_scan_file(child, f))
            subdirs.append(info)
        else:
            loose.append(_scan_file(common_dir, child))
    return subdirs, loose


def _scan_file(base: Path, path: Path) -> FileInfo:
    rel = path.relative_to(base).as_posix()
    size = path.stat().st_size
    ext = path.suffix.lower()
    if ext not in PARSE_EXTS:
        notes = {".info": "纯文档（非 Jomini）", ".lookup": "索引表（逐行名，非块定义）",
                 ".json": "JSON 元数据"}
        return FileInfo(rel=rel, size=size, note=notes.get(ext, f"未解析（{ext or '无扩展名'}）"))
    try:
        text = decode_dump_text(path.read_bytes())
    except OSError as exc:
        return FileInfo(rel=rel, size=size, note=f"读取失败：{exc}")
    entries, scalars = parse_jomini_toplevel(text)
    return FileInfo(rel=rel, size=size, entries=entries,
                    scalars=scalars, parsed=True)


# ---- 渲染 ----------------------------------------------------------------

def _fmt_bytes(n: int) -> str:
    return f"{n:,}".replace(",", " ")   # 千位空格，避免与 TSV/逗号混淆


def render_subdir_md(sub: SubdirInfo, game_version: str, game_dir: Path) -> str:
    """common/<子目录>.md：文件清单 + 每文件条目名索引。"""
    out: list[str] = []
    out.append(f"# common/{sub.name} 结构摘要")
    out.append("")
    out.append(f"- 游戏目录：`{game_dir}`（CK3 {game_version}；快照日期与指纹见 manifest.json）")
    out.append(f"- 文件数：{sub.file_count}"
               f"（其中 Jomini 解析 {sum(1 for f in sub.files if f.parsed)} 个）")
    out.append(f"- 顶层块条目总数：{sub.entry_count}，跨文件唯一条目 {sub.unique_entries}")
    out.append("- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。")
    out.append("")
    out.append("## 文件清单")
    out.append("")
    out.append("| 文件 | 字节 | 顶层块 | 标量键 | 解析 |")
    out.append("|---|---|---|---|---|")
    for f in sub.files:
        out.append(f"| `{f.rel}` | {f.size} | "
                    f"{len(f.entries) if f.parsed else '-'} | "
                    f"{f.scalars if f.parsed else '-'} | "
                    f"{'jomini' if f.parsed else f.note} |")
    out.append("")
    out.append("## 条目名 → 定义文件")
    out.append("")
    out.append(f"（查单条定义文件可直接 grep 全局映射："
               f"`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）")
    out.append("")
    for f in sub.files:
        if not f.parsed:
            continue
        out.append(f"### {f.rel}（{len(f.entries)} 条目）")
        out.append("")
        if f.entries:
            for name, _line in f.entries:
                out.append(f"- {name}")
        else:
            out.append("（无顶层块）")
        out.append("")
    unparsed = [f for f in sub.files if not f.parsed]
    if unparsed:
        out.append("### 未解析文件")
        out.append("")
        for f in unparsed:
            out.append(f"- `{f.rel}` — {f.note}")
        out.append("")
    return "\n".join(out).rstrip("\n") + "\n"


def render_entry_map(subdirs: list[SubdirInfo], loose: list[FileInfo]) -> str:
    """全局条目映射 TSV：条目名 \\t 定义文件（game 根相对 posix 路径）\\t 行号。

    排序 (条目名, 路径, 行号)，确定化；重名条目（多文件定义）保留多行。
    grep 例：grep -P "^education_intrigue_1\\t" entry_map.tsv
    """
    rows: list[tuple[str, str, int]] = []
    for sub in subdirs:
        for f in sub.files:
            for name, line in f.entries:
                rows.append((name, f"common/{sub.name}/{f.rel}", line))
    for f in loose:
        for name, line in f.entries:
            rows.append((name, f"common/{f.rel}", line))
    rows.sort(key=lambda r: (r[0], r[1], r[2]))
    lines = ["# entry\tfile\tline  — CK3 原版 common 顶层块名 → 定义文件映射（结构索引，零内容复制）"]
    lines += [f"{name}\t{path}\t{line}" for name, path, line in rows]
    return "\n".join(lines) + "\n"


def render_index_md(subdirs: list[SubdirInfo], loose: list[FileInfo],
                    other_summary: list[dict], game_dir: Path,
                    game_version: str, map_rows: int) -> str:
    out: list[str] = []
    out.append("# 原版结构索引（vanilla_structure）总索引")
    out.append("")
    out.append(f"- 游戏目录：`{game_dir}`（CK3 {game_version}；快照日期与内容指纹见 manifest.json 的 game_docs.vanilla_structure）")
    out.append("- 权威顺序：script_docs dump（game_docs/script_docs/）> wiki 层（pages/）> 本结构索引（仅导航）。")
    out.append("- 生成方式：`scripts/vanilla_index.py` 递归扫描，只提取结构信息"
               "（路径/文件名/顶层块名/计数/大小），零原版文件内容复制"
               "（mod 制作时按索引直接读游戏目录）。")
    out.append("")
    out.append("## 查询方式")
    out.append("")
    out.append("1. **查某条目（trait/opinion/modifier/... 名）定义在哪个文件**：")
    out.append("   `grep -P \"^<条目名>\\t\" game_docs\\vanilla_structure\\entry_map.tsv`")
    out.append(f"   （entry_map.tsv 共 {map_rows} 行映射；输出列为 条目名/定义文件/行号，"
               "文件路径相对 game\\ 根）")
    out.append("2. **浏览某类内容的全部文件与条目**：读 `common/<子目录>.md`（下表）。")
    out.append("3. **events/history/gui/gfx 等其他目录**：读 `other_dirs.md`。")
    out.append("")
    out.append(f"## common\\ 子目录摘要（{len(subdirs)} 个，全覆盖）")
    out.append("")
    out.append("| 子目录 | 文件数 | 顶层块条目 | 唯一条目 | 摘要文件 |")
    out.append("|---|---|---|---|---|")
    for sub in subdirs:
        out.append(f"| {sub.name} | {sub.file_count} | {sub.entry_count} | "
                   f"{sub.unique_entries} | `common/{sub.name}.md` |")
    out.append("")
    if loose:
        out.append("## common\\ 根散文件")
        out.append("")
        out.append("| 文件 | 字节 | 顶层块 |")
        out.append("|---|---|---|")
        for f in loose:
            out.append(f"| `{f.rel}` | {f.size} | "
                       f"{len(f.entries) if f.parsed else '-'} |")
        out.append("")
    out.append("## 其他内容目录概览")
    out.append("")
    out.append(f"见 `other_dirs.md`（{len(other_summary)} 个 game\\ 顶层目录，目录级统计；"
               "common 以外的脚本细节按需直接读游戏目录）。")
    out.append("")
    return "\n".join(out)


# ---- 其他目录概览 ---------------------------------------------------------

def _dir_stats(root: Path) -> dict:
    """目录级统计：文件数、字节数、扩展名分布、子目录树（深度上限 3）。"""
    files = [f for f in root.rglob("*") if f.is_file()]
    total_bytes = sum(f.stat().st_size for f in files)
    exts = Counter(f.suffix.lower() or "(无扩展名)" for f in files)
    tree = _dir_tree(root, depth_limit=3)
    return dict(name=root.name, file_count=len(files), total_bytes=total_bytes,
                exts=exts, tree=tree)


def _dir_tree(root: Path, depth_limit: int) -> list[str]:
    lines: list[str] = []

    def walk(d: Path, depth: int) -> tuple[int, int]:
        """返回 (该子树文件数, 字节数)，同时输出树行。"""
        file_cnt = byte_cnt = 0
        children = sorted(d.iterdir(), key=lambda p: p.name.lower())
        subdirs = [c for c in children if c.is_dir()]
        for f in sorted((c for c in children if c.is_file()),
                        key=lambda p: p.name.lower()):
            file_cnt += 1
            byte_cnt += f.stat().st_size
        for c in subdirs:
            if depth >= depth_limit:
                # 超深度：只计数不展开
                sub_f = [x for x in c.rglob("*") if x.is_file()]
                sub_b = sum(x.stat().st_size for x in sub_f)
                file_cnt += len(sub_f)
                byte_cnt += sub_b
                lines.append(f"{'  ' * depth}- {c.name}/ — {len(sub_f)} 文件"
                             f"（{_fmt_bytes(sub_b)} 字节，未展开）")
            else:
                lines.append(f"{'  ' * depth}- {c.name}/")
                fc, bc = walk(c, depth + 1)
                file_cnt += fc
                byte_cnt += bc
        return file_cnt, byte_cnt

    walk(root, 0)
    return lines


def render_other_dirs_md(game_dir: Path, game_version: str) -> tuple[str, list[dict]]:
    """game\\ 下除 common 外的全部顶层目录 + 根散文件概览。

    返回 (md 文本, 每目录统计摘要列表)。文件数 ≤ LIST_FILES_THRESHOLD 且
    目录不在 NO_LIST_DIRS 的，附逐文件清单（路径+字节，仍是纯结构信息）。
    """
    summaries: list[dict] = []
    sections: list[str] = []
    top = sorted((c for c in game_dir.iterdir() if c.is_dir()),
                 key=lambda p: p.name.lower())
    root_files = sorted((c for c in game_dir.iterdir() if c.is_file()),
                        key=lambda p: p.name.lower())
    head = ["# game\\ 其他内容目录概览", "",
            f"- 游戏目录：`{game_dir}`（CK3 {game_version}）",
            "- 目录级 best-effort 概览（common\\ 的全覆盖摘要见 "
            "`common/<子目录>.md` 与 `INDEX.md`）；本文件只含结构信息。",
            ""]
    if root_files:
        head += ["## 根散文件", "", "| 文件 | 字节 |", "|---|---|"]
        head += [f"| `{f.name}` | {f.stat().st_size} |" for f in root_files]
        head += [""]
    for d in top:
        if d.name == "common":
            continue
        stats = _dir_stats(d)
        summaries.append(dict(name=d.name, file_count=stats["file_count"],
                              total_bytes=stats["total_bytes"]))
        sec = [f"## {d.name}/", "",
               f"- 文件数：{stats['file_count']}，总大小：{_fmt_bytes(stats['total_bytes'])} 字节",
               "- 扩展名分布：" + ", ".join(
                   f"{ext}×{cnt}" for ext, cnt in
                   sorted(stats["exts"].items(), key=lambda kv: -kv[1])[:8])]
        if stats["tree"]:
            sec += ["", "### 子目录树（深度 ≤3）", ""] + stats["tree"]
        can_list = (d.name not in NO_LIST_DIRS
                    and stats["file_count"] <= LIST_FILES_THRESHOLD)
        if can_list:
            sec += ["", "### 文件清单", "", "| 相对路径 | 字节 |", "|---|---|"]
            for f in sorted(d.rglob("*"), key=lambda p: p.as_posix().lower()):
                if f.is_file():
                    sec.append(f"| `{f.relative_to(d).as_posix()}` | "
                               f"{f.stat().st_size} |")
        sections.append("\n".join(sec))
    return "\n".join(head) + "\n\n" + "\n\n".join(
        s + "\n" for s in sections), summaries


# ---- 主流程 ---------------------------------------------------------------

def run(game_dir: Path, out_dir: Path, game_version: str,
        write_manifest: bool, check_only: bool) -> int:
    common_dir = game_dir / "common"
    print(f"[vanilla_index] 游戏目录：{game_dir}（版本标注 {game_version}）")
    subdirs, loose = scan_common(common_dir)
    total_files = sum(s.file_count for s in subdirs) + len(loose)
    parsed_files = sum(1 for s in subdirs for f in s.files if f.parsed) + \
        sum(1 for f in loose if f.parsed)
    total_entries = sum(s.entry_count for s in subdirs) + \
        sum(len(f.entries) for f in loose)
    print(f"[vanilla_index] common\\：{len(subdirs)} 个顶层子目录 + "
          f"{len(loose)} 个根散文件，共 {total_files} 文件"
          f"（Jomini 解析 {parsed_files} 个），顶层块条目 {total_entries} 个")

    # 生成全部产物文本（内存中，check/写盘两用）
    products: dict[str, str] = {}   # 相对 out_dir 的 posix 路径 -> 内容
    for sub in subdirs:
        products[f"common/{sub.name}.md"] = render_subdir_md(
            sub, game_version, game_dir)
    map_text = render_entry_map(subdirs, loose)
    products["entry_map.tsv"] = map_text
    map_rows = map_text.count("\n") - 1   # 减注释头行

    other_text, other_summary = render_other_dirs_md(game_dir, game_version)
    products["other_dirs.md"] = other_text
    products["INDEX.md"] = render_index_md(
        subdirs, loose, other_summary, game_dir, game_version, map_rows)

    # ---- 结构断言：零内容复制 ----
    # 产物的每一行都由 路径/文件名/大小/计数/顶层块名/行号 组成；
    # 顶层块名（标识符）按解析器定义不可能包含 '{'，路径与数字亦然——
    # 因此任何产物中出现 '{' 即说明有块体内容混入，硬失败。
    for rel, content in products.items():
        if "{" in content:
            raise AssertionError(
                f"零内容复制断言失败：{rel} 中出现 '{{'（疑似块体内容混入）")
    # entry_map 行数守恒
    expected_rows = sum(s.entry_count for s in subdirs) + \
        sum(len(f.entries) for f in loose)
    if map_rows != expected_rows:
        raise AssertionError(
            f"entry_map 行数 {map_rows} != 条目总数 {expected_rows}")

    if check_only:
        ok = True
        for rel, content in sorted(products.items()):
            p = out_dir / rel
            same = p.is_file() and p.read_text(encoding="utf-8") == content
            print(f"[vanilla_index][check] {rel}: "
                  f"{'一致' if same else '缺失或内容有差异'}")
            ok = ok and same
        print(f"[vanilla_index][check] {'PASS' if ok else 'FAIL'}")
        return 0 if ok else 1

    out_dir.mkdir(parents=True, exist_ok=True)
    changed = []
    for rel, content in sorted(products.items()):
        if _atomic_write(out_dir / rel, content):
            changed.append(rel)
    print(f"[vanilla_index] 落盘 {len(products)} 个产物，"
          f"{len(changed)} 个内容有变（其余字节相同未重写）")

    if write_manifest:
        _update_manifest(game_dir, game_version, products, subdirs, loose,
                         total_files, parsed_files, total_entries, map_rows,
                         other_summary, bool(changed))
    return 0


def _update_manifest(game_dir: Path, game_version: str, products: dict,
                     subdirs: list[SubdirInfo], loose: list[FileInfo],
                     total_files: int, parsed_files: int, total_entries: int,
                     map_rows: int, other_summary: list[dict],
                     any_changed: bool) -> None:
    """manifest 顶层 game_docs.vanilla_structure 区登记（持锁原子写）。

    幂等：全部产物 sha256 的合成指纹不变时，快照日期 scanned_at 保留旧值。
    """
    fingerprint_src = "\n".join(
        f"{rel}\t{_sha256_bytes(c.encode('utf-8'))}"
        for rel, c in sorted(products.items()))
    fingerprint = _sha256_bytes(fingerprint_src.encode("utf-8"))
    now = _now_iso()
    with manifest_lib.manifest_locked():
        data = manifest_lib.read_manifest()
        gd = data.setdefault("game_docs", {})
        vs = gd.setdefault("vanilla_structure", {})
        prev_fp = vs.get("fingerprint")
        scanned_at = vs.get("scanned_at", now) if prev_fp == fingerprint else now
        vs.update({
            # 工单10：manifest 会发布，不登记本机绝对路径——只记标签，
            # 实际路径由本地 scripts/state/local_paths.json / CK3_GAME_DIR 提供
            "game_dir": "(local game install)/game",
            "game_version": game_version,
            "game_version_source": "spec 环境事实附录基准（可用 --game-version 覆盖）",
            "scanned_at": scanned_at,
            "fingerprint": fingerprint,
            "common": {
                "top_subdir_count": len(subdirs),
                "loose_file_count": len(loose),
                "file_total": total_files,
                "parsed_file_total": parsed_files,
                "entry_total": total_entries,
                "unique_entry_total": sum(s.unique_entries for s in subdirs),
                "entry_map_rows": map_rows,
            },
            "other_dirs": {d["name"]: d["file_count"] for d in other_summary},
            "products_dir": "game_docs/vanilla_structure",
            "products_count": len(products),
            "products_bytes": sum(len(c.encode("utf-8"))
                                  for c in products.values()),
            "key_products": {
                "index": "game_docs/vanilla_structure/INDEX.md",
                "entry_map": "game_docs/vanilla_structure/entry_map.tsv",
                "other_dirs": "game_docs/vanilla_structure/other_dirs.md",
            },
        })
        manifest_lib.write_manifest(data)
    print(f"[vanilla_index] manifest 已登记 game_docs.vanilla_structure"
          f"（指纹 {fingerprint[:12]}…，产物 {len(products)} 个，"
          f"快照日期 {'保留（内容未变）' if prev_fp == fingerprint else '刷新'}）")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--game-dir", default=None,
                    help="CK3 安装目录下的 game\\ 子目录（缺省依次取环境变量"
                         " CK3_GAME_DIR 与 scripts/state/local_paths.json）")
    ap.add_argument("--out", default=str(DEFAULT_OUT_DIR),
                    help="产物目录（默认 game_docs/vanilla_structure）")
    ap.add_argument("--game-version", default=DEFAULT_GAME_VERSION,
                    help="快照标注的游戏版本（默认 1.20.0 基准事实）")
    ap.add_argument("--no-manifest", action="store_true",
                    help="不写 manifest（测试用）")
    ap.add_argument("--check", action="store_true",
                    help="只校验现有产物与盘上一致，不落盘")
    args = ap.parse_args(argv)
    game_dir = resolve_game_dir(args.game_dir)
    return run(game_dir, Path(args.out), args.game_version,
               not args.no_manifest, args.check)


if __name__ == "__main__":
    sys.exit(main())
