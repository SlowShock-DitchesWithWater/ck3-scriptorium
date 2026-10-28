# -*- coding: utf-8 -*-
"""游戏权威层并入（工单07）：`game logs/` 的 script_docs dump → `game_docs/script_docs/`。

职责与边界（docs/spec.md、.scratch 工单07、docs/pipeline.md 契约）：
- 输入：仓库 `game logs/` 下用户以 debug 模式跑 `script_docs` 导出的
  7 个清单 .log + `data_types/` 5 个 .txt。来源白名单硬编码（见 DUMP_SPECS），
  只按白名单读文件——运行时会话日志（debug/error/game/setup/...）零混入。
- 输出：`game_docs/script_docs/` 每来源一个 Markdown；每条目一个
  `### 名称` 小节，条目正文（描述、Supported Scopes、Entries 列表等）逐字
  保留。这是权威层：只重排、不改写；与 wiki 层冲突时以本层为准。
- manifest：经 lib/manifest.py 持锁原子写，登记于顶层 `game_docs` 区：
  游戏版本（优先从 code_revisions.log 提取，提取不到用默认基准并注明）、
  来源文件、源字节数/mtime、条目数、产物 sha256、并入时间。
- 幂等：产物字节 = f(源字节, 源 mtime, 游戏版本)，不含运行时时间戳；
  内容未变时不重写文件、manifest 的并入时间不刷新。替换 dump 后重跑 =
  产物整体重生成（原子替换），不会堆积旧条目。

与 wiki 管线（crawl/clean/catalog/...）解耦，仅复用 lib.manifest（原子写）
与 lib.config（仓库根）。零网络请求。

用法：
  python scripts/game_layer.py            # 正常并入（写 game_docs + manifest）
  python scripts/game_layer.py --check    # 只校验产物与源一致，不落盘
  python scripts/game_layer.py --source <dir> --out <dir> --no-manifest
                                          # 测试：在临时副本上模拟 dump 更新
"""
from __future__ import annotations

import argparse
import codecs
import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import config  # noqa: E402  只读复用：仓库根路径
from lib import manifest as manifest_lib  # noqa: E402  manifest 原子写助手

# ---- 常量 ---------------------------------------------------------------

REPO_ROOT = config.REPO_ROOT
DEFAULT_SOURCE_DIR = REPO_ROOT / "game logs"
DEFAULT_OUT_DIR = REPO_ROOT / "game_docs" / "script_docs"

# 游戏版本基准事实（docs/spec.md 环境事实附录：本机 CK3 = 1.20.0）。
# code_revisions.log 若非空则尝试从其中提取版本号覆盖该默认值。
DEFAULT_GAME_VERSION = "1.20.0"

# 白名单：仅这些文件会被读取。任何不在其中的 game logs 文件（运行时会话
# 日志：debug/error/game/setup/system/memory/... 与空占位 log）一律不碰。
# kind 说明见 _parse_* 函数族。
DUMP_SPECS: list[dict] = [
    dict(source="effects.log", output="effects.md",
         kind="dash", header="Effect Documentation:", title="Effects"),
    dict(source="triggers.log", output="triggers.md",
         kind="dash", header="Trigger Documentation:", title="Triggers"),
    dict(source="event_targets.log", output="event_targets.md",
         kind="dash", header="Event Target Documentation:", title="Event Targets",
         sections=["Event Targets Saved from Code:"]),
    dict(source="event_scopes.log", output="event_scopes.md",
         kind="scopes", header="Scope Types:", title="Event Scopes"),
    dict(source="modifiers.log", output="modifiers.md",
         kind="modifiers", header="Printing Modifier Definitions:",
         title="Modifiers"),
    dict(source="on_actions.log", output="on_actions.md",
         kind="dash_colon", header="On Action Documentation:",
         title="On Actions"),
    dict(source="custom_localization.log", output="custom_localization.md",
         kind="dash_colon", header="Custom Localization Documentation:",
         title="Custom Localization"),
    dict(source="data_types/data_types_common.txt", output="data_types_common.md",
         kind="dash_verbatim", header=None, title="Data Types: common"),
    dict(source="data_types/data_types_gui.txt", output="data_types_gui.md",
         kind="dash_verbatim", header=None, title="Data Types: gui"),
    dict(source="data_types/data_types_internalclausewitzgui.txt",
         output="data_types_internalclausewitzgui.md",
         kind="dash_verbatim", header=None,
         title="Data Types: internalclausewitzgui"),
    dict(source="data_types/data_types_script.txt", output="data_types_script.md",
         kind="dash_verbatim", header=None, title="Data Types: script"),
    dict(source="data_types/data_types_uncategorized.txt",
         output="data_types_uncategorized.md",
         kind="dash_verbatim", header=None, title="Data Types: uncategorized"),
]

WHITELIST = {s["source"] for s in DUMP_SPECS}

# 条目分隔线：>=5 个连字符组成的整行（实测七清单为 20 连字符、data_types
# 为 23 连字符；按 >=5 宽容匹配以兼容未来微调）。
SEP_RE = re.compile(r"(?m)^-{5,}[ \t]*$")


# ---- 编码助手 -------------------------------------------------------------

def _cp1252_fallback(exc: UnicodeDecodeError):
    """UTF-8 解码失败的字节按 cp1252 兜底还原（实测 effects.log 内嵌一个
    cp1252 编码的 em-dash 0x97，其余全文件为 UTF-8）。逐字保留优先。"""
    return exc.object[exc.start:exc.end].decode("cp1252"), exc.end


codecs.register_error("ck3_cp1252_fallback", _cp1252_fallback)


def decode_dump_text(raw: bytes) -> str:
    """dump 文件解码：UTF-8（去 BOM）为主，坏字节 cp1252 兜底。"""
    return raw.decode("utf-8-sig", errors="ck3_cp1252_fallback")


# ---- 解析 ----------------------------------------------------------------

@dataclass
class Entry:
    name: str                 # 条目名（标题源）
    body_lines: list[str]     # 正文逐字行（已去首尾空行，内部空行保留）
    line_no: int = 0          # 在源文件中的起始行号（1 基，诊断用）


@dataclass
class ParsedDump:
    entries: list[Entry] = field(default_factory=list)
    sections: dict[str, list[str]] = field(default_factory=dict)  # 段名 -> 逐字行
    warnings: list[str] = field(default_factory=list)


def _split_lines(text: str) -> list[str]:
    """按 LF 切行；保留行内一切字符（逐字）。"""
    return text.split("\n")


def _strip_blank(lines: list[str]) -> list[str]:
    """去掉列表首尾的空行（全空白行），内部空行保留。"""
    start, end = 0, len(lines)
    while start < end and not lines[start].strip():
        start += 1
    while end > start and not lines[end - 1].strip():
        end -= 1
    return lines[start:end]


def _split_dash_parts(text: str) -> list[list[str]]:
    """按分隔线切块，返回行列表；空块（连续分隔线之间无内容）丢弃。"""
    parts = SEP_RE.split(text)
    blocks = []
    for part in parts:
        lines = _split_lines(part.replace("\r\n", "\n"))
        lines = _strip_blank(lines)
        if lines:
            blocks.append(lines)
    return blocks


def _parse_dash(text: str, spec: dict, colon_title: bool, verbatim_title: bool
                ) -> ParsedDump:
    """分隔线格式通用解析（effects/triggers/event_targets/on_actions/
    custom_localization/data_types 五族共用骨架）。

    - 首块必须等于文件头（如 "Effect Documentation:"）；
    - 其余每块一条目；首行为标题行；
    - title 规则：colon_title -> 去尾部冒号；verbatim_title -> 整行即名；
      否则按 "名 - 描述" 取首个 " - " 之前为名；
    - spec["sections"] 内的段头行开头的块按"命名段"处理（如
      "Event Targets Saved from Code:"），逐字保留其全部行。
    格式漂移（首行不合规则且不是已知段头）直接抛错——权威层宁可失败
    也不静默丢条目。
    """
    result = ParsedDump()
    blocks = _split_dash_parts(text)
    if not blocks:
        raise ValueError(f"{spec['source']}: 空文件")
    header = spec.get("header")
    first = blocks[0]
    if header is not None:
        if first != [header]:
            raise ValueError(
                f"{spec['source']}: 文件头不符，期望 {header!r}，"
                f"实际 {first[:2]!r}（dump 格式可能已变化，请人工核查）")
        blocks = blocks[1:]
    section_heads = set(spec.get("sections", []))
    for idx, lines in enumerate(blocks):
        first_line = lines[0]
        if first_line in section_heads:
            result.sections[first_line] = lines[1:]
            continue
        if colon_title:
            if not first_line.endswith(":"):
                raise ValueError(
                    f"{spec['source']} 第 {idx + 1} 块首行无冒号结尾："
                    f"{first_line[:80]!r}（格式漂移，请人工核查）")
            name = first_line[:-1]
        elif verbatim_title:
            name = first_line
        else:
            if " - " not in first_line:
                raise ValueError(
                    f"{spec['source']} 第 {idx + 1} 块首行缺 ' - ' 分隔："
                    f"{first_line[:80]!r}（格式漂移，请人工核查）")
            name = first_line.split(" - ", 1)[0]
        body_first = "" if (colon_title or verbatim_title) else \
            first_line.split(" - ", 1)[1]
        body = ([body_first] if body_first else []) + lines[1:]
        result.entries.append(Entry(name=name, body_lines=body))
    return result


def _parse_scopes(text: str, spec: dict) -> ParsedDump:
    """event_scopes.log：无分隔线；空行分隔的块，块首行 `name:`，
    其后为属性行（Evaluate Triggers: ... 等），全部逐字保留。"""
    result = ParsedDump()
    blocks = [b for b in text.split("\n\n")]
    warned_header = False
    for block in blocks:
        lines = _strip_blank(_split_lines(block))
        if not lines:
            continue
        first = lines[0]
        if first == spec["header"]:
            continue  # "Scope Types:" 文件头
        if not (first.endswith(":") and " " not in first):
            if not warned_header:
                result.warnings.append(
                    f"{spec['source']}: 块首行非 'name:' 形态：{first[:60]!r}")
                warned_header = True
            continue
        result.entries.append(Entry(name=first[:-1], body_lines=lines[1:]))
    return result


def _parse_modifiers(text: str, spec: dict) -> ParsedDump:
    """modifiers.log：无分隔线；条目以 `Tag: <名>` 行起始，其后属性行
    （Use areas: / Extra info: ...）逐字保留，空行结束条目。"""
    result = ParsedDump()
    current: Entry | None = None
    for line in _split_lines(text):
        if line.startswith("Tag: "):
            if current is not None:
                result.entries.append(current)
            current = Entry(name=line[5:].strip(), body_lines=[])
        elif current is not None:
            if not line.strip():          # 空行结束当前条目
                result.entries.append(current)
                current = None
            else:
                current.body_lines.append(line)
        elif line.strip() and line != spec["header"]:
            result.warnings.append(
                f"{spec['source']}: Tag 块外的游离行：{line[:60]!r}")
    if current is not None:
        result.entries.append(current)
    return result


def parse_source(source_rel: str, text: str) -> ParsedDump:
    """按 DUMP_SPECS 中该来源的 kind 分派解析。"""
    spec = next(s for s in DUMP_SPECS if s["source"] == source_rel)
    kind = spec["kind"]
    if kind == "dash":
        return _parse_dash(text, spec, colon_title=False, verbatim_title=False)
    if kind == "dash_colon":
        return _parse_dash(text, spec, colon_title=True, verbatim_title=False)
    if kind == "dash_verbatim":
        return _parse_dash(text, spec, colon_title=False, verbatim_title=True)
    if kind == "scopes":
        return _parse_scopes(text, spec)
    if kind == "modifiers":
        return _parse_modifiers(text, spec)
    raise ValueError(f"未知 kind: {kind}")


# ---- 渲染（Markdown，grep 友好）------------------------------------------

def render_product(spec: dict, parsed: ParsedDump, game_version: str,
                   source_mtime: str, source_bytes: int) -> str:
    """来源 → Markdown。确定性输出：同一输入字节恒得同一产物字节。"""
    out: list[str] = []
    out.append(f"# {spec['title']}（script_docs 权威清单）")
    out.append("")
    out.append(f"- 来源：`game logs/{spec['source']}`（CK3 {game_version} "
               f"`script_docs` 控制台导出）")
    out.append(f"- 源文件时间：{source_mtime}（文件 mtime，视为 dump 生成时间）")
    out.append(f"- 源文件大小：{source_bytes} 字节")
    out.append(f"- 条目数：{len(parsed.entries)}")
    if parsed.sections:
        for sec in parsed.sections:
            out.append(f"- 附加段：{sec}（{len(parsed.sections[sec])} 行）")
    out.append("- 正文逐字来自 dump，仅重排为每条目一节；与 wiki 层冲突时以本层为准。")
    out.append("")
    for entry in parsed.entries:
        out.append(f"### {entry.name}")
        out.append("")
        if entry.body_lines:
            out.extend(entry.body_lines)
            out.append("")
    for sec_name, lines in parsed.sections.items():
        out.append(f"## {sec_name}")
        out.append("")
        out.append("> 以下各行逐字来自 dump（每行一个名字）。")
        out.append("")
        out.extend(lines)
        out.append("")
    return "\n".join(out).rstrip("\n") + "\n"


# ---- 游戏版本提取 ----------------------------------------------------------

def extract_game_version(source_dir: Path) -> tuple[str, str]:
    """尝试从 code_revisions.log 提取版本；失败则用基准事实 1.20.0。

    返回 (版本串, 来源说明)。code_revisions.log 仅作元数据来源，不转产物。
    """
    cr = source_dir / "code_revisions.log"
    if cr.is_file() and cr.stat().st_size > 0:
        text = decode_dump_text(cr.read_bytes())
        m = re.search(r"(?m)\b(\d+\.\d+(?:\.\d+)*)\b", text)
        if m:
            return m.group(1), f"code_revisions.log 提取（文件 {cr}）"
    return DEFAULT_GAME_VERSION, (
        f"基准事实默认值 {DEFAULT_GAME_VERSION}（docs/spec.md 环境事实附录；"
        f"code_revisions.log 为空/无版本信息，未能提取）")


# ---- 产物落盘（幂等）-------------------------------------------------------

def _atomic_write(path: Path, content: str) -> bool:
    """内容有变才写（临时文件 + os.replace）。返回是否写入。"""
    data = content.encode("utf-8")
    if path.is_file() and path.read_bytes() == data:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_bytes(data)
    import os
    os.replace(tmp, path)
    return True


def _now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


# ---- 白名单断言 -----------------------------------------------------------

def assert_whitelist(source_dir: Path) -> list[str]:
    """断言白名单文件全部在盘；列出被排除的运行时会话日志（仅列名，不读）。

    白名单式排除：本模块只可能读 WHITELIST 内文件（read 调用点唯一且
    已被白名单过滤），因此产物中不可能出现任何会话日志内容。
    """
    missing = [s for s in sorted(WHITELIST)
               if not (source_dir / s).is_file()]
    if missing:
        # 报错即自愈指引（solve, don't defer）：告诉用户缺什么、怎么补
        need_dtypes = any(m.startswith("data_types/") for m in missing)
        hint = ("\n发生了什么：游戏 dump 来源缺少白名单文件。\n"
                "下一步怎么做：确认 CK3 以 -debug_mode 启动后在控制台跑过两个命令：\n"
                "  script_docs        （生成 7 个清单 .log）\n"
                "  dump_data_types    （生成 data_types\\ 下 5 个 .txt）\n"
                "然后用 --source 指向 <文档目录>\\Paradox Interactive\\Crusader Kings III\\"
                "script_documentation 重跑本命令。\n"
                if need_dtypes else
                "\n发生了什么：游戏 dump 来源缺少清单 .log。\n"
                "下一步怎么做：CK3 以 -debug_mode 启动后在控制台跑 script_docs，"
                "再用 --source 指向 script_documentation 目录重跑本命令。\n")
        raise FileNotFoundError(f"白名单来源缺失: {missing}{hint}")
    present = {p.relative_to(source_dir).as_posix()
               for p in source_dir.rglob("*") if p.is_file()}
    excluded = sorted(present - WHITELIST)
    return excluded


# ---- 主流程 ---------------------------------------------------------------

def run(source_dir: Path, out_dir: Path, game_version_override: str | None,
        write_manifest: bool, check_only: bool) -> int:
    excluded_logs = assert_whitelist(source_dir)
    print(f"[game_layer] 来源目录：{source_dir}")
    print(f"[game_layer] 白名单 {len(WHITELIST)} 个文件全部在盘；"
          f"排除运行时会话/占位日志 {len(excluded_logs)} 个（未读取）：")
    for name in excluded_logs:
        print(f"    - 排除: {name}")

    if game_version_override:
        version, version_source = game_version_override, "命令行 --game-version 指定"
    else:
        version, version_source = extract_game_version(source_dir)
    print(f"[game_layer] 游戏版本：{version}（{version_source}）")

    results: dict[str, dict] = {}
    for spec in DUMP_SPECS:
        src_path = source_dir / spec["source"]
        assert spec["source"] in WHITELIST  # 防御：非白名单禁止读取
        raw = src_path.read_bytes()
        text = decode_dump_text(raw)
        parsed = parse_source(spec["source"], text)
        if not parsed.entries:
            raise ValueError(f"{spec['source']}: 解析得到 0 条目，中止")
        for w in parsed.warnings:
            print(f"[game_layer] 警告 {w}")
        mtime = datetime.fromtimestamp(
            src_path.stat().st_mtime).astimezone().isoformat(timespec="seconds")
        content = render_product(spec, parsed, version, mtime, len(raw))
        out_path = out_dir / spec["output"]
        results[spec["output"]] = dict(
            spec=spec, content=content, out_path=out_path,
            entry_count=len(parsed.entries),
            section_counts={k: len(v) for k, v in parsed.sections.items()},
            source_bytes=len(raw), source_mtime=mtime,
        )
        print(f"[game_layer] {spec['source']} -> {spec['output']}: "
              f"{len(parsed.entries)} 条目"
              + (f"，附加段 {results[spec['output']]['section_counts']}"
                 if parsed.sections else ""))

    if check_only:
        ok = True
        for name, r in results.items():
            exists = r["out_path"].is_file()
            same = exists and r["out_path"].read_text(encoding="utf-8") == r["content"]
            print(f"[game_layer][check] {name}: "
                  f"{'一致' if same else ('缺失' if not exists else '内容有差异')}")
            ok = ok and same
        print(f"[game_layer][check] {'PASS' if ok else 'FAIL'}")
        return 0 if ok else 1

    out_dir.mkdir(parents=True, exist_ok=True)
    changed: list[str] = []
    for name, r in results.items():
        if _atomic_write(r["out_path"], r["content"]):
            changed.append(name)
    print(f"[game_layer] 落盘 {len(results)} 个产物，"
          f"{len(changed)} 个内容有变（其余字节相同未重写）")

    # 产物自检：### 小节数 == 条目数（含 ### 前缀的条目名不可能出现在正文中
    # 造成多计——dump 正文行不以 '### ' 开头，实测无一例外；此处再验一次）。
    for name, r in results.items():
        n_head = sum(1 for line in r["content"].split("\n")
                     if line.startswith("### "))
        expect = r["entry_count"]
        if n_head != expect:
            raise AssertionError(
                f"{name}: ### 小节数 {n_head} != 条目数 {expect}（可能存在以 "
                f"'### ' 开头的正文行，需人工核查）")

    if write_manifest:
        _update_manifest(version, version_source, results, changed)
    return 0


def _update_manifest(version: str, version_source: str,
                     results: dict[str, dict], changed: list[str]) -> None:
    """manifest 顶层 game_docs.script_docs 区登记（经 lib.manifest 持锁）。"""
    now = _now_iso()
    with manifest_lib.manifest_locked():
        data = manifest_lib.read_manifest()
        gd = data.setdefault("game_docs", {})
        sd = gd.setdefault("script_docs", {})
        gd["game_version"] = version
        gd["game_version_source"] = version_source
        # 幂等：内容全部未变时不刷新顶层并入时间（与单产物 merged_at 策略一致）
        if changed:
            gd["merged_at_latest"] = now
        for name, r in results.items():
            sha = _sha256_bytes(r["content"].encode("utf-8"))
            prev = sd.get(name, {})
            # 幂等：内容未变时保留原并入时间，manifest 整体字节不变
            merged_at = prev.get("merged_at", now) if prev.get(
                "output_sha256") == sha and not (name in changed) else now
            sd[name] = {
                "source_file": f"game logs/{r['spec']['source']}",
                "source_bytes": r["source_bytes"],
                "source_mtime": r["source_mtime"],   # dump 生成时间（mtime 近似）
                "entry_count": r["entry_count"],
                "sections": r["section_counts"] or None,
                "output_file": r["out_path"].relative_to(
                    config.REPO_ROOT).as_posix(),
                "output_bytes": len(r["content"].encode("utf-8")),
                "output_sha256": sha,
                "merged_at": merged_at,
            }
        manifest_lib.write_manifest(data)
    print(f"[game_layer] manifest 已登记 game_docs.script_docs（{len(results)} 项）")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--source", default=str(DEFAULT_SOURCE_DIR),
                    help="dump 来源目录（默认仓库 game logs；测试可指向副本）")
    ap.add_argument("--out", default=str(DEFAULT_OUT_DIR),
                    help="产物目录（默认 game_docs/script_docs）")
    ap.add_argument("--game-version", default=None,
                    help="覆盖游戏版本标注（默认自动提取/基准事实 1.20.0）")
    ap.add_argument("--no-manifest", action="store_true",
                    help="不写 manifest（测试用）")
    ap.add_argument("--check", action="store_true",
                    help="只校验现有产物与源一致，不落盘")
    args = ap.parse_args(argv)
    return run(Path(args.source), Path(args.out),
               args.game_version, not args.no_manifest, args.check)


if __name__ == "__main__":
    sys.exit(main())
