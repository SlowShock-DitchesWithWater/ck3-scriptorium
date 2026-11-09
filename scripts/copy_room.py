# -*- coding: utf-8 -*-
"""抄写室（copy_room）—— 为其他 mod 建立同构知识库（2026-11-09 新增）。

子命令：
  --list              枚举可建的 mod：Steam 工坊（多库发现）+ Documents 本地 mod
  --build --id N      为工坊 mod N 建 KB（签名层+结构层+差异报告）
  --build --path P    为本地/任意 mod 文件夹 P 建 KB（--name 覆盖命名）
  --sync              把已建 KB 清单再生进 catalog.md 抄写室标记区块
  --check             校验 mods_docs 与 catalog 区块同步（空也通过）

双通道复用现有管线（进程级调用，零代码耦合）：
  签名层 = game_layer.py --source <dump目录> --out mods_docs/<mod>/script_docs
           （前置：用户以目标 mod 加载态跑过 script_docs + dump_data_types）
  结构层 = vanilla_index.py --game-dir <mod文件夹> --out mods_docs/<mod>/structure
差异报告 = mods_docs/<mod>/script_docs 与 game_docs/script_docs 的 ### 条目集对比

发布边界：mods_docs/ 不入仓库（.gitignore）；本脚本与 copy_room/ 文档发布。
"""
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import config  # noqa: E402

PY = sys.executable
SCRIPTS = config.REPO_ROOT / "scripts"
MODS_DOCS = config.REPO_ROOT / "mods_docs"
CK3_APPID = "1158310"
PARADOX_MODS = (Path.home() / "Documents" / "Paradox Interactive"
                / "Crusader Kings III" / "mod")
MARK_BEGIN = "<!-- ck3wiki-mod-kb:copy-room BEGIN -->"
MARK_END = "<!-- ck3wiki-mod-kb:copy-room END -->"


# ------------------------------------------------ mod 发现

def steam_libraries() -> list[Path]:
    """解析 libraryfolders.vdf 发现全部 Steam 库（容错：失败返回常见路径）。"""
    libs: list[Path] = []
    for steam in (Path("C:/Program Files (x86)/Steam"),
                  Path("C:/Program Files/Steam")):
        vdf = steam / "steamapps" / "libraryfolders.vdf"
        if vdf.is_file():
            libs += [Path(m.group(1).replace("\\\\", "/"))
                     for m in re.finditer(r'"path"\s+"([^"]+)"', vdf.read_text(encoding="utf-8", errors="replace"))]
            break
    if not libs:
        libs = [Path("C:/Program Files (x86)/Steam")]
    return libs


def parse_descriptor(p: Path) -> dict:
    """解析 .mod / descriptor.mod（key="value" 行；容错读取）。"""
    d: dict[str, str] = {}
    try:
        for line in p.read_text(encoding="utf-8-sig", errors="replace").splitlines():
            m = re.match(r'^\s*(\w+)\s*=\s*"(.*)"\s*$', line)
            if m:
                d[m.group(1)] = m.group(2)
    except OSError:
        pass
    return d


def discover_mods() -> list[dict]:
    """枚举工坊 + 本地 mod。返回 [{id?, name, path, origin}]。"""
    out: list[dict] = []
    for lib in steam_libraries():
        ws = lib / "steamapps" / "workshop" / "content" / CK3_APPID
        if not ws.is_dir():
            continue
        for d in sorted(ws.iterdir()):
            desc = d / "descriptor.mod"
            if d.is_dir() and desc.is_file():
                meta = parse_descriptor(desc)
                out.append({"id": d.name, "name": meta.get("name", d.name),
                            "path": str(d), "origin": f"workshop[{lib}]",
                            "version": meta.get("version", "")})
    if PARADOX_MODS.is_dir():
        for f in sorted(PARADOX_MODS.glob("*.mod")):
            meta = parse_descriptor(f)
            name = meta.get("name", f.stem)
            if f.stem.startswith("ugc_"):
                # ugc_*.mod 是工坊订阅的描述符：path 指向工坊内容，补 id
                mid = f.stem[4:]
                out.append({"id": mid, "name": name, "origin": "local-ugc",
                            "path": meta.get("path", ""),
                            "version": meta.get("version", "")})
                continue
            p = meta.get("path", "")
            folder = (PARADOX_MODS / p) if p and "://" not in p else (PARADOX_MODS / f.stem)
            if folder.is_dir():
                out.append({"id": "", "name": name, "origin": "local",
                            "path": str(folder),
                            "version": meta.get("version", "")})
    return out


def slugify(s: str) -> str:
    t = re.sub(r"[^\w\-]+", "-", s).strip("-")
    return re.sub(r"-{2,}", "-", t)[:40].lower() or "mod"


# ------------------------------------------------ 建 KB

def build(mod: dict, dump_dir: Path | None) -> int:
    mid = mod.get("id") or slugify(mod["name"])
    target = MODS_DOCS / f"{mid}-{slugify(mod['name'])}"
    sig_out = target / "script_docs"
    struct_out = target / "structure"
    dump = dump_dir or (Path.home() / "Documents" / "Paradox Interactive"
                        / "Crusader Kings III" / "logs")

    print(f"[copy_room] 目标 mod：{mod['name']}（{mod.get('origin', '?')}）")
    print(f"[copy_room] 产物目录：{target.relative_to(config.REPO_ROOT)}")

    # 通道 1：签名层（需要 dump；缺失时跳过并提示，结构层仍可建）
    if any(dump.glob("*.log")):
        r = subprocess.run([PY, "-X", "utf8", str(SCRIPTS / "game_layer.py"),
                            "--source", str(dump), "--out", str(sig_out),
                            "--no-manifest"], capture_output=True, text=True,
                           encoding="utf-8", errors="replace")
        print(r.stdout.strip().splitlines()[-1] if r.stdout else r.stderr[-200:])
        if r.returncode != 0:
            return r.returncode
    else:
        print(f"[copy_room] 警告：{dump} 无清单日志——签名层跳过。"
              f"请以目标 mod 加载态在游戏控制台跑 script_docs + dump_data_types 后重跑。")

    # 通道 2：结构层（直接扫 mod 文件夹）
    r = subprocess.run([PY, "-X", "utf8", str(SCRIPTS / "vanilla_index.py"),
                        "--game-dir", mod["path"], "--out", str(struct_out),
                        "--no-manifest"], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if r.returncode != 0:
        print(r.stdout[-300:], r.stderr[-300:])
        return r.returncode
    print("[copy_room] 结构层完成")

    # 差异报告 + 元信息 README
    write_diff(target, mod)
    write_readme(target, mod, sig_out.is_dir())
    print(f"[copy_room] 完成：{target.name}")
    return 0


def _entries(p: Path) -> set[str]:
    return {m.group(1) for m in
            re.finditer(r"^### (.+)$", p.read_text(encoding="utf-8"), re.M)}


def write_diff(target: Path, mod: dict) -> None:
    van = config.REPO_ROOT / "game_docs" / "script_docs"
    lines = [f"# {mod['name']} · 相对原版的签名差异",
             "",
             f"- 生成：{datetime.now():%Y-%m-%d}；基线：game_docs/script_docs（原版快照）",
             "- NEW = 该 mod 环境新增（子 mod 可直接调用的 API 面）；",
             "  REMOVED = 原版有而该环境没有（被移除/改名，子 mod 慎用）", ""]
    sig = target / "script_docs"
    if not sig.is_dir():
        lines.append("（签名层未生成——跑过 script_docs/dump_data_types 后重建）")
        (target / "DIFF_vs_vanilla.md").write_text("\n".join(lines) + "\n",
                                                   encoding="utf-8", newline="\n")
        return
    for f in sorted(sig.glob("*.md")):
        v = van / f.name
        if not v.is_file():
            continue
        ve, ke = _entries(v), _entries(f)
        new, removed = sorted(ke - ve), sorted(ve - ke)
        if not new and not removed:
            continue
        lines.append(f"## {f.name}（+{len(new)} / -{len(removed)}）")
        for n in new:
            lines.append(f"- NEW `{n}`")
        for n in removed:
            lines.append(f"- REMOVED `{n}`")
        lines.append("")
    (target / "DIFF_vs_vanilla.md").write_text("\n".join(lines) + "\n",
                                               encoding="utf-8", newline="\n")


def write_readme(target: Path, mod: dict, has_sig: bool) -> None:
    entry_map = target / "structure" / "entry_map.tsv"
    n_entries = sum(1 for _ in entry_map.open(encoding="utf-8")) - 1 if entry_map.is_file() else 0
    text = (f"# Mod 知识库 · {mod['name']}\n\n"
            f"- 来源：{mod.get('origin', '?')}（工坊/本地 ID：{mod.get('id') or '—'}）\n"
            f"- mod 文件夹：`{mod['path']}`\n"
            f"- 生成：{datetime.now():%Y-%m-%d}\n"
            f"- 组成：`script_docs/`（mod 加载态签名层"
            f"{'✓' if has_sig else '✗ 未生成——需游戏内跑两条 dump 命令'}）、"
            f"`structure/`（结构索引，{n_entries} 条目映射）、"
            f"`DIFF_vs_vanilla.md`（与原版差异）\n"
            f"- 检索：签名 grep `script_docs/*.md` 的 `### 名称`；"
            f"条目定位 grep `structure/entry_map.tsv`；"
            f"子 mod 场景同名条目以本层为准，原版行为回查 `game_docs/`\n")
    (target / "README.md").write_text(text, encoding="utf-8", newline="\n")


# ------------------------------------------------ catalog 区块

def render_section() -> str:
    lines = [MARK_BEGIN,
             "## 抄写室 · 其他 Mod 知识库（mods_docs，本地生成不发布；"
             "构建方式见 `copy_room/README.md`）", ""]
    kbs = sorted(MODS_DOCS.glob("*/README.md")) if MODS_DOCS.is_dir() else []
    if not kbs:
        lines.append("（暂无 mod 知识库。`python scripts/copy_room.py --list` 枚举，"
                     "`--build --id <工坊id>` 或 `--path <mod文件夹>` 构建，"
                     "`--sync` 并入本目录。）")
    for r in kbs:
        lines += [f"### {r.parent.name}", f"- {r.read_text(encoding='utf-8').splitlines()[0].lstrip('# ').strip()}",
                  f"- **位置**：`mods_docs/{r.parent.name}/`（README / script_docs / "
                  "structure / DIFF_vs_vanilla）", ""]
    lines.append(MARK_END)
    return "\n".join(lines) + "\n"


def sync() -> int:
    section = render_section()
    cat = config.CATALOG_PATH
    text = cat.read_text(encoding="utf-8")
    if MARK_BEGIN in text and MARK_END in text:
        text = re.sub(re.escape(MARK_BEGIN) + r".*?" + re.escape(MARK_END),
                      lambda _: section.rstrip("\n"), text, flags=re.S)
    else:
        text = text.rstrip("\n") + "\n\n" + section
    cat.write_text(text, encoding="utf-8", newline="\n")
    n = len(list(MODS_DOCS.glob("*/README.md"))) if MODS_DOCS.is_dir() else 0
    print(f"[copy_room] catalog 区块已同步（{n} 个 KB）")
    return 0


def check() -> int:
    want = render_section()
    text = config.CATALOG_PATH.read_text(encoding="utf-8") if config.CATALOG_PATH.is_file() else ""
    ok = want.strip() in text
    n = len([p for p in MODS_DOCS.glob("*/README.md")]) if MODS_DOCS.is_dir() else 0
    print(f"[copy_room][check] mod KB {n} 个；catalog 区块"
          f"{'一致' if ok else '不一致（跑 --sync）'}")
    return 0 if ok else 1


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    args = argv if argv is not None else sys.argv[1:]
    if "--list" in args:
        mods = discover_mods()
        print(f"发现 {len(mods)} 个 mod：")
        for m in mods:
            print(f"  [{'id ' + m['id'] if m['id'] else 'local':>16}] {m['name']}"
                  f"  <-  {m['path']}")
        return 0
    if "--build" in args:
        mods = discover_mods()
        target = None
        if "--id" in args:
            want = args[args.index("--id") + 1]
            target = next((m for m in mods if m.get("id") == want), None)
            if target is None:
                print(f"[copy_room] 未发现 id={want} 的 mod（先 --list 核对）")
                return 2
        elif "--path" in args:
            p = Path(args[args.index("--path") + 1])
            if not p.is_dir():
                print(f"[copy_room] 路径不存在：{p}")
                return 2
            desc = p / "descriptor.mod"
            meta = parse_descriptor(desc) if desc.is_file() else {}
            target = {"id": "", "name": meta.get("name", p.name),
                      "path": str(p), "origin": "path", "version": ""}
        if target is None:
            print("用法：--build --id <工坊id> | --build --path <mod文件夹> [--dump <dump目录>]")
            return 2
        dump = Path(args[args.index("--dump") + 1]) if "--dump" in args else None
        return build(target, dump)
    if "--sync" in args:
        return sync()
    if "--check" in args:
        return check()
    print("用法：python scripts/copy_room.py --list | --build ... | --sync | --check")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
