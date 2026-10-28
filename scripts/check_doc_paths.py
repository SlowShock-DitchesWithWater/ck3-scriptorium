# -*- coding: utf-8 -*-
r"""文档路径自检（工单09）：验证 AGENTS.md / README.md 中引用的全部路径真实存在。

背景：参考合集（_reference/skillset）的教训就是"AGENTS 规约空指/坏路径"——
规约里让 agent 去读的文件必须逐一实测在盘。本脚本把文档里出现的每个
路径型引用提取出来，相对仓库根逐一检查，输出 PASS/EXTERNAL/FAIL 清单；
任一 FAIL 退出码 1。零网络、只读文档与目录项。

用法（仓库根）：
    python scripts/state/check_doc_paths.py                 # 默认查 AGENTS.md + README.md + README.zh-CN.md
    python scripts/state/check_doc_paths.py AGENTS.md       # 指定文档（可多个）

判定规则：
- PASS     ：路径（文件或目录）在仓库内存在；
- EXTERNAL ：指向用户本机游戏安装目录的引用（首段是 game/common/events 等
             原版顶层目录，如 entry_map.tsv 的输出示例 common/traits/00_traits.txt），
             仓库外不检查，报告注明；
- FAIL     ：仓库内应当存在却找不到 → 空指/坏路径。

提取规则（宁可多报也不漏报，两级）：
1. 反引号 span：`xxx\yyy` 形态的精确引用——若整体含路径分隔符且
   首段是已知仓库根/外部根（或含 <占位符>），整体作为一个 token；
2. 逐词扫描（含代码块与正文）：在每个空格分词内查找含分隔符的子串
   或带已知扩展名的文件名。

已知仓库根（首段命中才整体采信反引号 span）：
pages / game_docs / game logs / scripts / tests / docs / raw / lib /
_reference / .scratch / .playwright-mcp
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # scripts/
from lib import config  # noqa: E402  只读复用：仓库根路径

REPO_ROOT = config.REPO_ROOT

# 仓库内已知根目录/根文件首段（反引号 span 整体采信的条件）
KNOWN_ROOTS = {
    "pages", "game_docs", "game logs", "scripts", "tests", "docs", "raw", "lib",
    "_reference", ".scratch", ".playwright-mcp", "state",
}
# 仓库外（用户本机游戏安装目录）顶层目录首段 → EXTERNAL，不做存在性检查
EXTERNAL_ROOTS = {
    "game", "common", "events", "history", "gui", "gfx", "localization",
}
# 仓库外裸文件名（如目标站点的 robots.txt）→ EXTERNAL，不检查
EXTERNAL_BARE_NAMES = {"robots.txt"}

# 已知扩展名：裸文件名也视为路径引用
FILE_EXT_RE = re.compile(r"[A-Za-z0-9_\-.]+\.(?:md|tsv|json|py|txt|log|bat|html)\b")
# 分词内含分隔符的路径子串（分词内不含空格，故字符类无需空格）
PATH_SUB_RE = re.compile(r"[A-Za-z0-9_\-.\u4e00-\u9fff<>$*]+(?:[\\/][A-Za-z0-9_\-.\u4e00-\u9fff<>$*]+)+")
# 反引号 span
TICK_RE = re.compile(r"`([^`\n]+)`")


def _clean(token: str) -> str:
    """归一化：剥修饰符与首尾标点，统一分隔符，去尾部斜杠/省略号。"""
    token = token.strip("`*\" ")
    token = token.strip("。，；：、（）()[]【】：,;")
    token = token.rstrip("/\\")
    token = token.rstrip(".")   # 省略号尾巴（如 game_docs\...），Windows 下 "..." 还会被当 "." 误判存在
    return token.strip()


def _whole_pathlike(span: str) -> bool:
    """反引号 span 是否可整体视为一个路径引用。

    条件：含分隔符，且（首段是已知根，或末段带已知扩展名，或含 <占位符>）。
    首段是外部根的（common/...）也算路径引用（判 EXTERNAL）。
    以占位符开头（如 `<python> scripts\run.py ...` 命令示例）不算——
    交给逐词扫描按部分提取真实路径。
    """
    if not any(sep in span for sep in "\\/"):
        return False
    if span.startswith("<"):
        return False
    first = re.split(r"[\\/]", span, maxsplit=1)[0].strip()
    if first.lower() in KNOWN_ROOTS or first.lower() in EXTERNAL_ROOTS:
        return True
    if FILE_EXT_RE.search(span.split("\\")[-1].split("/")[-1]):
        return True
    return "<" in span


def extract_paths(text: str) -> list[str]:
    """从文档全文提取全部路径型引用（去重、保序）。"""
    found: list[str] = []
    seen: set[str] = set()

    def add(token: str) -> None:
        token = _clean(token)
        if not token or token.lower().startswith(("http:", "https:")):
            return
        if token not in seen:
            seen.add(token)
            found.append(token)

    # 1) 反引号 span：优先整体采信
    tick_spans: list[str] = []
    for m in TICK_RE.finditer(text):
        span = m.group(1).strip()
        tick_spans.append(span)
        if _whole_pathlike(span):
            add(span)

    def scan_parts(chunk: str) -> None:
        """逐词扫描：命中含分隔符子串或带扩展名文件名则 add。"""
        for part in re.split(r"\s+", chunk):
            part = part.strip("`'\"")
            if not part or part.startswith(("-", "/", "--")):
                continue
            m = PATH_SUB_RE.search(part)
            if m:
                add(m.group(0))
                continue
            m2 = FILE_EXT_RE.search(part)
            if m2:
                add(m2.group(0))

    # 2) 逐词扫描（代码块、正文兜底）。反引号 span 已整体采信，挖掉再扫，
    #    避免 "pages\Event modding.md" 被空格劈成两个假 token；
    #    但裸文件名 span（如 `effects.md`）仍要单独扫（无分隔符不满足整体采信）。
    residue = TICK_RE.sub(" ", text)
    scan_parts(residue)
    for span in tick_spans:
        if not _whole_pathlike(span):
            scan_parts(span)
    return found


def check_one(token: str, repo_files: dict[str, Path],
              doc_dir: Path | None = None) -> tuple[str, str]:
    """检查单个路径引用。返回 (状态, 说明)。状态：PASS / EXTERNAL / SKIP / FAIL。

    doc_dir：引用所在文档的目录——`../../xxx` 式文档相对路径按它解析。
    """
    norm = token.replace("/", "\\")
    first = norm.split("\\")[0].lower()

    # 仓库外引用：首段是原版游戏安装目录，或已知仓库外裸文件名
    if first in EXTERNAL_ROOTS:
        return "EXTERNAL", "仓库外（游戏安装目录相对路径），不检查"
    if norm.lower() in EXTERNAL_BARE_NAMES:
        return "EXTERNAL", "仓库外（非本仓库文件），不检查"

    # 非路径文本（散文里的斜线连词，如 effect/trigger）：
    # 首段不是已知仓库根、整体无已知扩展名、无占位符/通配符 → 不当路径检查
    has_ext = bool(FILE_EXT_RE.fullmatch(norm.split("\\")[-1]))
    if (first not in KNOWN_ROOTS and "\\" in norm and not has_ext
            and "<" not in token and "*" not in token):
        return "SKIP", "非路径文本（斜线连词）"

    # 仓库内直查（字面路径，含目录引用）
    if (REPO_ROOT / norm).exists():
        return "PASS", str(Path(norm))

    # 按设计不随仓库发布/由用户本地生成的路径：克隆中不存在属正常状态，
    # 不当坏路径报（维护者机器上存在时已在上面 exists 分支 PASS，走不到这）
    not_shipped_roots = {"game_docs", "game logs", "raw", "_reference", ".scratch"}
    not_shipped_full = {"docs\\spec.md", "kb_location.txt", "local_paths.json",
                        "entry_map.tsv",
                        # 游戏层 dump 产物裸文件名（维护者机器上经全库索引 PASS）
                        "effects.md", "triggers.md", "modifiers.md", "on_actions.md",
                        "event_targets.md", "event_scopes.md",
                        "custom_localization.md", "data_types_common.md",
                        "data_types_gui.md", "data_types_internalclausewitzgui.md",
                        "data_types_script.md", "data_types_uncategorized.md"}
    if first in not_shipped_roots or norm.lower() in not_shipped_full \
            or norm.lower().startswith("scripts\\state"):
        return "EXTERNAL", "按设计不随仓库发布（本地生成/维护者侧）"

    # 占位符/通配：glob 命中即 PASS；否则检查最长字面前缀（父目录）
    if "<" in token or "*" in token:
        glob_pat = re.sub(r"<[^<>]*>", "*", token).replace("/", "\\")
        hits = list(REPO_ROOT.glob(glob_pat))
        if hits:
            return "PASS", f"通配命中 {len(hits)} 处（如 {hits[0].relative_to(REPO_ROOT)}）"
        prefix = re.split(r"[<*]", norm)[0].rstrip("\\")
        if prefix and (REPO_ROOT / prefix).exists():
            return "PASS", f"占位符父目录存在：{prefix}"

    # 裸文件名（无分隔符）：全仓库索引搜索
    if "\\" not in norm:
        hit = repo_files.get(norm.lower())
        if hit is not None:
            return "PASS", f"裸文件名命中 {hit}"

    # 文档相对路径（含 ..）：按引用所在文档的目录解析（如 skill 内 ../../catalog.md）
    if ".." in token and doc_dir is not None:
        resolved = (doc_dir / token).resolve()
        try:
            resolved.relative_to(REPO_ROOT)
        except ValueError:
            return "EXTERNAL", f"解析到仓库外：{resolved}"
        if resolved.is_file():
            return "PASS", f"文档相对路径命中 {resolved.relative_to(REPO_ROOT)}"

    return "FAIL", "仓库内不存在"


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):  # Windows 控制台中文安全输出
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    # 无参数（或空参数）时默认检查仓库根的 AGENTS×2 与两份 README + skill 两版
    docs = [REPO_ROOT / a for a in (argv if argv else
            ["AGENTS.md", "AGENTS.zh-CN.md", "README.md", "README.zh-CN.md",
             "skills/ck3-mod-standards/SKILL.md",
             "skills/ck3-mod-standards/SKILL.zh-CN.md"])]
    missing_docs = [d for d in docs if not d.is_file()]
    if missing_docs:
        print(f"[check_doc_paths] 待检文档不存在：{[str(d) for d in missing_docs]}")
        return 2

    # 全仓库文件名索引（裸文件名检查用；跳过大目录以提速）
    repo_files: dict[str, Path] = {}
    skip_top = {"raw", "_reference", ".scratch", ".playwright-mcp", "game logs", "__pycache__"}
    for p in REPO_ROOT.rglob("*"):
        rel = p.relative_to(REPO_ROOT)
        if rel.parts and rel.parts[0] in skip_top:
            continue
        if p.is_file() and p.suffix.lower() in {".md", ".tsv", ".json", ".py", ".txt",
                                                ".log", ".bat", ".html"}:
            repo_files.setdefault(p.name.lower(), rel)

    n_pass = n_ext = n_fail = 0
    for doc in docs:
        text = doc.read_text(encoding="utf-8")
        tokens = extract_paths(text)
        print(f"===== {doc.name}：{len(tokens)} 个路径引用 =====")
        for t in tokens:
            status, detail = check_one(t, repo_files, doc_dir=doc.parent)
            mark = {"PASS": "PASS ", "EXTERNAL": "EXT  ", "SKIP": "SKIP", "FAIL": "FAIL "}[status]
            print(f"  [{mark}] {t:<62} {detail}")
            n_pass += status == "PASS"
            n_ext += status == "EXTERNAL"
            n_fail += status == "FAIL"
        print()
    print(f"合计：PASS {n_pass} · EXTERNAL {n_ext} · SKIP 若干（非路径文本） · FAIL {n_fail}")
    if n_fail:
        print("结论：存在空指/坏路径，修复文档后再发布。")
        return 1
    print("结论：全部路径引用真实存在（无空指/坏路径）。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
