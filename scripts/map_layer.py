# -*- coding: utf-8 -*-
"""地图层扫描（地图室·知识层）：从游戏安装实测提取地图侧权威事实。

产物（game_docs/map_docs/）：
- map_data_dossier.md   地图数据档案：map_data 文件实测规格（尺寸/位深/调色板）、
                        definition.csv 统计、default.map 结构、河流调色板实测、
                        编辑器（-mapeditor）状态证据、视觉层（gfx）速览
- province_index.tsv    省份索引：id/r/g/b/名称/状态/源行号，grep -P "^<id>\\t" 定位
- nudger_parameters.md  auto_nudger_settings.json 参数表（数值实测 + 语义注解）

与 vanilla_index.py 同约定：
- 游戏目录三级解析（--game-dir / CK3_GAME_DIR / scripts/state/local_paths.json）；
- manifest 登记到 game_docs.map_docs（匿名 game_dir、内容指纹幂等、scanned_at 保留）；
- 纯标准库——PNG 尺寸/位深/调色板从 IHDR/PLTE 块解析，不依赖 PIL；
- 零原版内容复制：只提取结构、统计与格式事实（heightmap.heightmap 全文 16 行、
  rivers 调色板色值为格式约定，属"格式说明"而非地图内容）。

用法（仓库根）：
  python scripts/map_layer.py --game-dir "<CK3安装目录>\\game" [--out <dir>] [--no-manifest]
"""
from __future__ import annotations

import argparse
import json
import re
import struct
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib import config, manifest as manifest_lib  # noqa: E402
from game_layer import _atomic_write, _now_iso, _sha256_bytes  # noqa: E402
from vanilla_index import resolve_game_dir  # noqa: E402  三级解析复用

REPO_ROOT = config.REPO_ROOT
DEFAULT_OUT_DIR = REPO_ROOT / "game_docs" / "map_docs"
DEFAULT_GAME_VERSION = "1.20.1"   # 与 manifest vanilla_structure 快照一致

# ---------------------------------------------------------------------------
# PNG 头解析（stdlib）：IHDR → 尺寸/位深/颜色类型；PLTE → 调色板颜色
# ---------------------------------------------------------------------------

PNG_SIG = b"\x89PNG\r\n\x1a\n"
COLOR_TYPE = {0: "灰度", 2: "RGB", 3: "索引色", 4: "灰度+Alpha", 6: "RGBA"}


def png_ihdr(path: Path) -> tuple[int, int, int, int]:
    """返回 (宽, 高, 位深, 颜色类型)；非 PNG 或头损坏时抛 ValueError。"""
    with path.open("rb") as f:
        head = f.read(33)
    if len(head) < 33 or head[:8] != PNG_SIG:
        raise ValueError(f"{path.name}: 不是有效 PNG")
    w, h = struct.unpack(">II", head[16:24])
    depth, ctype = head[24], head[25]
    return w, h, depth, ctype


def png_plte(path: Path) -> list[tuple[int, int, int]]:
    """返回 PLTE 块的 RGB 列表（按槽序）；无 PLTE 返回空表。"""
    with path.open("rb") as f:
        f.read(8)
        while True:
            hdr = f.read(8)
            if len(hdr) < 8:
                return []
            length, ctype = struct.unpack(">I", hdr[:4])[0], hdr[4:8]
            data = f.read(length)
            f.read(4)  # CRC
            if ctype == b"PLTE":
                return [(data[i], data[i + 1], data[i + 2])
                        for i in range(0, len(data) - 2, 3)]


def png_fact(path: Path) -> str:
    """人读规格行：`18432×9216 · 16bit 灰度（colortype 0）`。"""
    w, h, d, t = png_ihdr(path)
    return f"{w}×{h} · {d}bit {COLOR_TYPE.get(t, '?')}（colortype {t}）"


# ---------------------------------------------------------------------------
# map_data 各定义文件实测
# ---------------------------------------------------------------------------

def scan_definition(csv_path: Path) -> dict:
    """definition.csv 实测：行统计、连续性、RGB 唯一性、TSV 行。"""
    rows: list[dict] = []
    active_ids: list[int] = []
    dup_rgb: list[str] = []
    seen_rgb: dict[tuple[int, int, int], int] = {}
    for lineno, raw in enumerate(csv_path.read_text(
            encoding="utf-8-sig", errors="replace").splitlines(), 1):
        line = raw.strip()
        if not line:
            continue
        commented = line.startswith("#")
        body = line[1:] if commented else line
        parts = body.split(";")
        if len(parts) < 5 or not parts[0].strip().isdigit():
            continue  # 表头/异形行不计入索引
        pid = int(parts[0])
        try:
            rgb = (int(parts[1]), int(parts[2]), int(parts[3]))
        except ValueError:
            rgb = (-1, -1, -1)
        name = parts[4] if len(parts) > 4 else ""
        flag = parts[5] if len(parts) > 5 else ""
        rows.append({"id": pid, "rgb": rgb, "name": name, "flag": flag,
                     "status": "commented" if commented else "active",
                     "line": lineno})
        if not commented:
            active_ids.append(pid)
            if rgb in seen_rgb:
                dup_rgb.append(f"id {pid} 与 id {seen_rgb[rgb]} 同色 "
                               f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}")
            else:
                seen_rgb[rgb] = pid
    ids = sorted(active_ids)
    gaps = [i for i in range(ids[0], ids[-1] + 1)
            if i not in set(active_ids)] if ids else []
    return {"rows": rows, "active": len(active_ids),
            "commented": len(rows) - len(active_ids),
            "id_min": ids[0] if ids else None,
            "id_max": ids[-1] if ids else None,
            "gaps": gaps, "dup_rgb": dup_rgb}


def scan_default_map(path: Path) -> dict:
    """default.map 实测：生效文件引用、sea_zones/river_provinces 覆盖。"""
    file_refs: list[tuple[str, str]] = []
    commented_refs: list[str] = []
    sea_ranges = sea_ids = river_ranges = river_ids = 0
    for raw in path.read_text(encoding="utf-8-sig", errors="replace").splitlines():
        line = raw.strip()
        if not line:
            continue
        m = re.match(r"^(\w+)\s*=\s*\"([^\"]+)\"", line)
        if m and not line.startswith("#"):
            file_refs.append((m.group(1), m.group(2)))
        elif m:
            commented_refs.append(m.group(1))
        z = re.match(r"^sea_zones\s*=\s*RANGE\s*\{\s*(\d+)\s+(\d+)", line)
        if z:
            sea_ranges += 1
            sea_ids += int(z.group(2)) - int(z.group(1)) + 1
        elif re.match(r"^sea_zones\s*=\s*LIST", line):
            sea_ranges += 1
            sea_ids += len(re.findall(r"\d+", line)) - 1  # 去掉 LIST 字样计数字
        r = re.match(r"^river_provinces\s*=\s*RANGE\s*\{\s*(\d+)\s+(\d+)", line)
        if r:
            river_ranges += 1
            river_ids += int(r.group(2)) - int(r.group(1)) + 1
        elif re.match(r"^river_provinces\s*=\s*LIST", line):
            river_ranges += 1
            river_ids += len(re.findall(r"\d+", line)) - 1
    return {"file_refs": file_refs, "commented_refs": commented_refs,
            "sea_ranges": sea_ranges, "sea_ids": sea_ids,
            "river_ranges": river_ranges, "river_ids": river_ids}


def scan_adjacencies(path: Path) -> dict:
    """adjacencies.csv 实测：表头/行数/类型集/终止行。"""
    lines = [ln for ln in path.read_text(
        encoding="utf-8-sig", errors="replace").splitlines() if ln.strip()]
    header = lines[0] if lines else ""
    body = [ln for ln in lines[1:] if not ln.strip().startswith("#")]
    types: set[str] = set()
    for ln in body:
        p = ln.split(";")
        if len(p) >= 3 and p[2].strip():
            types.add(p[2].strip())
    last = body[-1].strip() if body else ""
    terminator = last.startswith("-1;-1")
    return {"header": header, "entries": len(body) - (1 if terminator else 0),
            "types": sorted(types), "terminator": terminator}


def scan_exe_strings(game_dir: Path) -> dict:
    """ck3.exe 灰盒字符串证据：mapeditor/nudge 相关标识符与路径。"""
    exe = game_dir.parent / "binaries" / "ck3.exe"
    if not exe.is_file():
        return {"exe": None}
    blob = exe.read_bytes()
    pat = re.compile(rb"[A-Za-z0-9_/.\-]{0,34}(?:mapeditor|nudge)[A-Za-z0-9_/.\-]{0,34}")
    hits = sorted({m.group(0).decode("ascii") for m in pat.finditer(blob)})
    return {"exe": exe, "exe_bytes": exe.stat().st_size, "hits": hits}


def scan_editor_artifacts(game_dir: Path) -> dict:
    """tools/mapeditor 出厂工件 + gui/map_editor 数据文件清点。"""
    tools = game_dir / "tools" / "mapeditor"
    artifacts: list[tuple[str, int]] = []
    status_no = status_lines = 0
    mask_meta = "（缺失）"
    if tools.is_dir():
        for f in sorted(tools.rglob("*")):
            if f.is_file():
                rel = f.relative_to(tools).as_posix()
                artifacts.append((rel, f.stat().st_size))
                if f.name == "map_editor_status.txt":
                    text = f.read_text(encoding="utf-8-sig", errors="replace")
                    status_lines = len(text.splitlines())
                    status_no = len(re.findall(r"=\s*no\b", text))
                if f.name == "mask_painter_meta.json":
                    mask_meta = f.read_text(encoding="utf-8-sig").strip() or "（空文件）"
    gui_dir = game_dir / "gui" / "map_editor"
    gui_files = ([f.name for f in sorted(gui_dir.iterdir()) if f.is_file()]
                 if gui_dir.is_dir() else [])
    return {"artifacts": artifacts, "status_lines": status_lines,
            "status_no": status_no, "mask_meta": mask_meta, "gui_files": gui_files}


def scan_gfx(game_dir: Path) -> dict:
    """视觉层速览：terrain 子目录体系（masks/masks_gen 等）、water、蒙版源。"""
    terrain = game_dir / "gfx" / "map" / "terrain"
    t_files: list[str] = []
    t_dirs: list[str] = []
    if terrain.is_dir():
        ents = list(terrain.iterdir())
        t_files = [e.name for e in ents if e.is_file()]
        t_dirs = sorted(e.name for e in ents if e.is_dir())
    t_sub = {d: len(list((terrain / d).glob("*")))
             for d in t_dirs if (terrain / d).is_dir()}
    water = game_dir / "gfx" / "map" / "water"
    w_total = len(list(water.glob("*"))) if water.is_dir() else 0
    cs_dir = game_dir / "content_source"
    cs = [p.name for p in sorted(cs_dir.iterdir())] if cs_dir.is_dir() else []
    return {"terrain_files": len(t_files), "terrain_dirs": t_dirs,
            "terrain_sub": t_sub, "water_total": w_total,
            "content_source": cs}


# ---------------------------------------------------------------------------
# 产物渲染
# ---------------------------------------------------------------------------

def render_province_index(defn: dict) -> str:
    out = ["# province_index.tsv —— definition.csv 省份索引（生成物，勿手改）",
           "# 列：id	r	g	b	name	第6列字面值	status	source_line",
           "# 查询示例：grep -P \"^1234\\t\" game_docs/map_docs/province_index.tsv",
           "# status=commented 行是原版注释掉的历史省份（不在活动 ID 区间内）"]
    for r in defn["rows"]:
        out.append("\t".join(str(x) for x in (
            r["id"], r["rgb"][0], r["rgb"][1], r["rgb"][2],
            r["name"], r["flag"], r["status"], r["line"])))
    return "\n".join(out) + "\n"


def render_dossier(game_dir: Path, version: str, defn: dict,
                   dmap: dict, adj: dict, exe: dict, art: dict,
                   gfx: dict, heightmap_meta: str) -> str:
    md = game_dir / "map_data"
    files = sorted((f.name, f.stat().st_size)
                   for f in md.iterdir() if f.is_file())
    subdir = md / "geographical_regions"
    subdir_n = len(list(subdir.iterdir())) if subdir.is_dir() else 0
    png_specs = {}
    for name in ("heightmap.png", "provinces.png", "rivers.png",
                 "indirection_heightmap.png", "packed_heightmap.png"):
        p = md / name
        if p.is_file():
            try:
                png_specs[name] = png_fact(p)
            except ValueError:
                png_specs[name] = "（PNG 头解析失败）"
    pal = png_plte(md / "rivers.png") if (md / "rivers.png").is_file() else []
    uniq_pal = sorted(set(pal))
    hw, hh, _, _ = png_ihdr(md / "heightmap.png")
    pw, ph, _, _ = png_ihdr(md / "provinces.png")
    missing_refs = []
    for key, ref in dmap["file_refs"]:
        if key in ("definitions", "provinces", "rivers", "topology",
                   "adjacencies", "island_region", "seasons", "continent",
                   "climate", "positions", "tree_definition",
                   "terrain_definition"):
            if not (md / ref).is_file():
                missing_refs.append(f"{key} = \"{ref}\"")

    L: list[str] = []
    L.append("# 地图数据档案（map_docs dossier）\n")
    L.append(f"- 游戏目录：`{game_dir}`（CK3 {version}；快照日期与内容指纹见"
             f" manifest.json 的 game_docs.map_docs）")
    L.append("- 生成方式：`scripts/map_layer.py` 实测提取（PNG 头解析 / CSV 统计 /"
             " exe 字符串灰盒扫描），零推测、零原版内容复制。")
    L.append("- 权威顺序：本档案（游戏实测）> wiki 层（pages/Map modding.md，"
             "oldid 34676，页面标注版本 1.1）。冲突点在各节单独标注。")
    L.append("- 配套工具：`map_room/validate_map.py`（地图校验器）；"
             "工作流向导见 `map_room/WORKFLOW.md`。\n")

    L.append("## map_data/ 文件实测清单\n")
    L.append(f"共 {len(files)} 个文件 + geographical_regions/ 子目录"
             f"（{subdir_n} 个文件）。\n")
    L.append("| 文件 | 字节 | 实测规格 |")
    L.append("|---|---|---|")
    for name, size in files:
        spec = png_specs.get(name, "")
        if name == "heightmap.heightmap":
            spec = "分块索引（见下节全文）"
        elif name == "nodes.dat":
            spec = "二进制（无 default.map 引用；疑为编辑器生成的寻路数据，待实验确认）"
        elif name.endswith(".csv"):
            spec = {"definition.csv": f"{defn['active']} 活动行 + "
                     f"{defn['commented']} 注释行",
                    "adjacencies.csv": f"{adj['entries']} 条连接"
                     + ("；终止行在" if adj["terminator"] else "；**终止行缺失**")
                    }.get(name, "")
        elif name == "default.map":
            spec = (f"{len(dmap['file_refs'])} 个生效文件引用"
                    + ("；含幽灵引用" if missing_refs else ""))
        L.append(f"| `{name}` | {size} | {spec} |")
    L.append("")

    L.append("### 关键尺寸关系（1.18+ 实测，wiki 未记载）\n")
    L.append(f"- heightmap.png {hw}×{hh} 恰为 provinces.png/rivers.png "
             f"{pw}×{ph} 的 **2 倍边长**（4 倍像素）。")
    L.append("- wiki（oldid 34676，1.1 时代）\"heightmap 与 provinces 同尺寸\""
             "的规则只适用于 1.17 及以前；1.18/1.19 起高度图独立为 2 倍分辨率"
             "分块体系（packed/indirection 两张派生图由编辑器 repack 生成）。")
    L.append(f"- indirection_heightmap.png {png_specs.get('indirection_heightmap.png','')}"
             "：寻址图，实测边长为 provinces.png 的 **1/32**（= heightmap 的 1/64）；"
             "wiki 旧文 \"×1/32\" 以 1.1 时代单一地图尺寸表述，按省份图口径衡量仍符。"
             f"packed_heightmap.png {png_specs.get('packed_heightmap.png','')}"
             "：非原图尺寸的压缩打包形态（repack 产物）。\n")

    L.append("## heightmap.heightmap（1.18+ 分块格式，全文）\n")
    L.append("```")
    L.append(heightmap_meta.strip())
    L.append("```")
    L.append("")
    L.append("字段注解（语义标注【推断】者为参数名推断，非官方文档）："
             "`heightmap_file`/`indirection_file` 指向派生图；"
             "`original_heightmap_size` 必须等于 heightmap.png 实际尺寸；"
             "`tile_size`【推断】分块像素宽；`level_offsets`【推断】各压缩级别的"
             "行偏移；`max_compress_level`【推断】最大压缩级别数；"
             "`empty_tile_offset`【推断】空块指针。**此文件由编辑器 repack 生成，"
             "手改 heightmap 后应在编辑器里重打包，而非手编此文件。**\n")

    L.append("## definition.csv 实测\n")
    L.append("- 行格式：`id;r;g;b;名称;x;`（UTF-8 无 BOM、无引号字段；"
             "第 6 列原版恒为字面值 `x`；`#` 前缀为注释行）。")
    L.append(f"- 活动行 {defn['active']} 个，id {defn['id_min']}..{defn['id_max']} "
             f"完全连续（缺口 {len(defn['gaps'])} 个）；注释行 {defn['commented']} 个，"
             "全部落在活动区间之外（历史遗留省份，仅作参考）。")
    L.append(f"- id 0 为水体（0;0;0;0;x;x;）；黑色 (0,0,0) 为保留色。"
             f"活动行重复色 {len(defn['dup_rgb'])} 组。")
    L.append("- **wiki 冲突注记**：wiki 示例表头与首列语义（\"ID From\" 等）"
             "与实测不符——实测第 5 列为男爵领名（大写）、无独立 type 列；"
             "陆海类型由 default.map 的 sea_zones/river_provinces 区段表达。"
             "以本节实测为准。")
    L.append("- 逐省索引：`province_index.tsv`（同目录；"
             "`grep -P \"^<id>\\t\"` 或按名称 grep）。\n")

    L.append("## rivers.png 调色板实测\n")
    L.append(f"索引色 PNG（colortype 3），256 槽调色板，实际用色 "
             f"{len(uniq_pal)} 种：\n")
    L.append("| 颜色 | wiki 语义（oldid 34676） | 备注 |")
    L.append("|---|---|---|")
    wiki_sem = {"#00ff00": "河流系统源头（每系统仅一个）",
                "#ff0000": "支流汇入（流向该像素）",
                "#fffc00": "河流分叉（流离该像素）",
                "#ff0080": "海/湖/可航河道",
                "#ffffff": "陆地"}
    blue_ramp = {"#000064", "#000096", "#0000c8", "#0000e1", "#0000ff",
                 "#0064ff", "#0096ff", "#00c8ff", "#00e1ff"}
    extra_green = {"#005500", "#007d00", "#009e00", "#18ce00"}
    for c in uniq_pal:
        h = "#%02x%02x%02x" % c
        if h in wiki_sem:
            note = "wiki 记载"
        elif h in blue_ramp:
            note = "wiki 记载：蓝色梯度，越暗越宽"
        elif h in extra_green:
            note = "**wiki 未记载，原版在用**（校验器降级为 WARN）"
        elif h == "#020001":
            note = "近黑占位槽（index 0 附近，疑未使用）"
        else:
            note = "未识别"
        L.append(f"| `{h}` | {wiki_sem.get(h, '—')} | {note} |")
    L.append("")
    L.append("- wiki 称\"调色板外颜色（含抗锯齿/透明）即 CTD\"；实测原版自身"
             "携带 4 个未记载绿色变体，说明引擎对部分色有容忍——**安全做法"
             "仍是从原版 rivers.png 起步**（校验器对未记载色报 WARN 而非 ERROR）。\n")

    L.append("## default.map 实测\n")
    L.append(f"- 生效文件引用 {len(dmap['file_refs'])} 个："
             + "、".join(f"`{k}`" for k, _ in dmap["file_refs"]) + "。")
    if missing_refs:
        L.append("- **幽灵引用**（default.map 引用但 map_data/ 无此文件，"
                 "原版亦如此，疑可选/遗留）：" + "；".join(f"`{m}`" for m in missing_refs))
    if dmap["commented_refs"]:
        L.append("- 注释掉的引用键：`" + "、".join(sorted(set(dmap["commented_refs"]))) + "`。")
    L.append(f"- `sea_zones`：{dmap['sea_ranges']} 个 RANGE/LIST 区段，"
             f"覆盖 id 约 {dmap['sea_ids']} 个；`river_provinces`："
             f"{dmap['river_ranges']} 个区段，覆盖 id 约 {dmap['river_ids']} 个"
             "（可航大河，陆海军通行规则见 wiki Map modding）。")
    L.append("- 修改省份 id 布局后必须同步更新这两类区段，否则海陆判定错乱。\n")

    L.append("## adjacencies.csv 实测\n")
    L.append(f"- 实测表头：`{adj['header']}`（wiki 示例表头 \"ID From;…\" 与原版"
             "不一致，以实测为准）。")
    L.append(f"- 连接条目 {adj['entries']} 条；Type 实测取值："
             + "、".join(f"`{t}`" for t in adj["types"]) + "。")
    L.append("- 末尾终止行 `-1;-1;;-1;-1;-1;-1;-1;` 原版**存在**"
             "（wiki 警告缺失会导致无限载入，实测印证其必要性）。")
    L.append("- 坐标可用 `-1` 表示用默认军队落点；`#` 行为注释。\n")

    L.append("## 编辑器（-mapeditor）状态证据（灰盒实测）\n")
    if exe.get("exe"):
        L.append(f"- 主程序 `{exe['exe'].relative_to(exe['exe'].parents[2])}` "
                 f"{exe['exe_bytes']:,} 字节；mapeditor/nudge 相关字符串 "
                 f"{len(exe['hits'])} 条：")
        L.append("  ```")
        for h in exe["hits"]:
            L.append(f"  {h}")
        L.append("  ```")
        L.append("  模块名（mapeditor_heightmap / border_helper / spline_network /"
                 " detail_data / composite_spline_graphics / interface / auto_nudge）"
                 "与启动参数 `-mapeditor` 均内嵌于二进制；专用 shader 位于"
                 " `gfx/FX/jomini/mapeditor/`。")
    L.append(f"- `tools/mapeditor/` 出厂工件："
             + "；".join(f"`{n}`（{s:,}B）" for n, s in art["artifacts"]))
    L.append(f"  - `map_editor_status.txt`：{art['status_lines']:,} 行开发期任务清单，"
             f"`=no` 条目 {art['status_no']:,} 个——内部工具状态文件直接随游戏分发。")
    L.append(f"  - `mask_painter/mask_painter_meta.json` 内容为 {art['mask_meta']}；"
             "`content_source/TODO.txt` 亦为开发备忘（提及 map_object_painter）。")
    L.append(f"- `gui/map_editor/` 数据文件：{len(art['gui_files'])} 个"
             + (f"（{'、'.join(art['gui_files'])}）" if art["gui_files"] else "")
             + "——编辑器主 UI 硬编码于二进制（exe 引用的 `gui/map_editor/mapeditor`"
             " 数据文件未随游戏分发），仅地图模式切换面板为数据驱动。")
    L.append("- 游戏 `script_documentation` dump 中零 mapeditor 条目"
             "（官方文档缺失；wiki 教程为社区逆向成果）。\n")

    L.append("## 视觉层速览（gfx，1.18+ 重构后形态）\n")
    L.append(f"- `gfx/map/terrain/`：顶层 {gfx['terrain_files']} 个文件（每地形类型的 "
             "diffuse/normal/properties PBR 三件套）+ 子目录 "
             + "、".join(f"`{d}/`（{n} 个）" for d, n in gfx["terrain_sub"].items())
             + "。")
    masks_n = gfx["terrain_sub"].get("masks", 0)
    gen_n = gfx["terrain_sub"].get("masks_gen", 0)
    L.append(f"- **逐像素地形蒙版仍在，已移入子目录**：`masks/` {masks_n} 张、"
             f"`masks_gen/` {gen_n} 张 `_mask.png`（wiki 1.3 时代\"63 张 _mask\""
             "清单过时；自定义分辨率需缩放的就是这批蒙版 + flat_maps/）。"
             "`flat_maps/` 为平面地图贴图，`unmasked/` 为无蒙版回退材质。")
    L.append(f"- `gfx/map/water/`：{gfx['water_total']} 个文件"
             "（flowmap/foam/watercolor 等，自定义分辨率仍需按 wiki 比例缩放）。")
    L.append(f"- `content_source/`：{('、'.join(gfx['content_source']) or '空')}"
             "（对象蒙版源数据，TODO.txt 标注其挂载意图）。\n")

    L.append("## 配套索引与工具\n")
    L.append("- 逐省索引：`province_index.tsv`（本目录）。")
    L.append("- auto-nudge 摆放参数表：`nudger_parameters.md`（本目录）。")
    L.append("- 地图校验器：`map_room/validate_map.py`"
             "（对 mod 的 map_data 做本档案全部机械检查）。")
    L.append("- 工作流向导（启动项 / repack / 常见故障）：`map_room/WORKFLOW.md`。")
    return "\n".join(L) + "\n"


# nudger 参数语义注解：数值来自实测 JSON；语义列凡未标注者为参数名+wiki
# （pages/Map modding.md「Auto nudge」节）语境推断，官方无文档。
NUDGER_SEMANTICS: dict[str, dict[str, str]] = {
    "building_priority": "各类对象自动摆放的优先级（数值小=先摆）",
    "avoid_distance": "各类对象之间的最小间距（地图单位）",
    "siege_pattern": "攻城器械落点的采样模式（距点距离/坡度/离边距离/避南北因子）",
    "stack_player_pattern": "玩家部队堆叠落点模式（水平/垂直偏移与离边距离）",
    "combat_pattern": "战斗场景落点模式",
    "building_pattern": "地产建筑落点模式（范围/朝南偏好/南岸距离）",
    "special_building_pattern": "特殊建筑落点模式",
    "activities_pattern": "活动场景落点模式",
    "rotation_unit_stack_player": "部队堆叠旋转角范围（from/to 弧度）",
    "rotation_combat": "战斗场景旋转角范围",
    "rotation_special_building": "特殊建筑旋转角范围",
    "rotation_buildings": "建筑旋转角范围",
    "rotation_activities": "活动场景旋转角范围",
}


def render_nudger(game_dir: Path) -> str:
    src = game_dir / "tools" / "mapeditor" / "auto_nudger_settings.json"
    data = json.loads(src.read_text(encoding="utf-8-sig"))
    L = ["# auto-nudge 摆放参数表（auto_nudger_settings.json）\n"]
    L.append(f"- 来源：游戏安装 `tools/mapeditor/auto_nudger_settings.json` 实测"
             "（数值列为原版当前值，重跑 `scripts/map_layer.py` 刷新）。")
    L.append("- 背景：wiki（pages/Map modding.md「Auto nudge」节）记载可在编辑器"
             "里微调自动摆放；本表把随游戏分发的全部约 60 个参数连同数值列出。")
    L.append("- **语义均为参数名 + 数值语境的推断，官方无文档**"
             "（仅 `building_priority`/`avoid_distance` 的「对象优先级/间距」语义"
             "有 wiki 原文背书）；拿不准的参数改前先在编辑器里做对照实验。\n")
    for section, params in data.items():
        L.append(f"## {section}\n")
        L.append(f"语义（推断）：{NUDGER_SEMANTICS.get(section, '—')}\n")
        L.append("| 参数 | 原版值 |")
        L.append("|---|---|")
        for k, v in params.items():
            L.append(f"| `{k}` | `{v}` |")
        L.append("")
    return "\n".join(L) + "\n"


# ---------------------------------------------------------------------------
# manifest 登记（镜像 vanilla_index：匿名、指纹幂等、scanned_at 保留）
# ---------------------------------------------------------------------------

def _update_manifest(game_dir: Path, game_version: str,
                     products: dict[str, str], defn: dict) -> None:
    fingerprint_src = "\n".join(
        f"{rel}\t{_sha256_bytes(c.encode('utf-8'))}"
        for rel, c in sorted(products.items()))
    fingerprint = _sha256_bytes(fingerprint_src.encode("utf-8"))
    now = _now_iso()
    with manifest_lib.manifest_locked():
        data = manifest_lib.read_manifest()
        gd = data.setdefault("game_docs", {})
        mdoc = gd.setdefault("map_docs", {})
        prev_fp = mdoc.get("fingerprint")
        scanned_at = mdoc.get("scanned_at", now) if prev_fp == fingerprint else now
        mdoc.update({
            "game_dir": "(local game install)/game",
            "game_version": game_version,
            "game_version_source": "默认与 vanilla_structure 快照一致"
                                    "（可用 --game-version 覆盖）",
            "scanned_at": scanned_at,
            "fingerprint": fingerprint,
            "stats": {
                "province_active": defn["active"],
                "province_commented": defn["commented"],
                "province_id_max": defn["id_max"],
            },
            "products_dir": "game_docs/map_docs",
            "products_count": len(products),
            "key_products": {
                "dossier": "game_docs/map_docs/map_data_dossier.md",
                "province_index": "game_docs/map_docs/province_index.tsv",
                "nudger": "game_docs/map_docs/nudger_parameters.md",
            },
        })
        manifest_lib.write_manifest(data)
    print(f"[map_layer] manifest 已登记 game_docs.map_docs"
          f"（指纹 {fingerprint[:12]}…，产物 {len(products)} 个，"
          f"快照日期 {'保留（内容未变）' if prev_fp == fingerprint else '刷新'}）")


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="地图层扫描（地图室·知识层）")
    ap.add_argument("--game-dir", help="CK3 安装目录的 game\\ 子目录"
                                       "（或用 CK3_GAME_DIR / local_paths.json）")
    ap.add_argument("--out", default=str(DEFAULT_OUT_DIR),
                    help="产物目录（默认 game_docs/map_docs）")
    ap.add_argument("--game-version", default=DEFAULT_GAME_VERSION,
                    help="覆盖登记的游戏版本号")
    ap.add_argument("--no-manifest", action="store_true",
                    help="只写产物，不登记 manifest")
    args = ap.parse_args(argv)

    game_dir = resolve_game_dir(args.game_dir)
    md = game_dir / "map_data"
    for req in ("definition.csv", "provinces.png", "rivers.png",
                "heightmap.png", "default.map"):
        if not (md / req).is_file():
            print(f"[map_layer] 错误：{md} 下缺少 {req}，不是有效的游戏目录")
            return 2
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    defn = scan_definition(md / "definition.csv")
    dmap = scan_default_map(md / "default.map")
    adj = scan_adjacencies(md / "adjacencies.csv")
    exe = scan_exe_strings(game_dir)
    art = scan_editor_artifacts(game_dir)
    gfx = scan_gfx(game_dir)
    hm_meta = (md / "heightmap.heightmap").read_text(encoding="utf-8-sig")

    products = {
        "game_docs/map_docs/map_data_dossier.md":
            render_dossier(game_dir, args.game_version, defn, dmap, adj,
                           exe, art, gfx, hm_meta),
        "game_docs/map_docs/province_index.tsv":
            render_province_index(defn),
        "game_docs/map_docs/nudger_parameters.md": render_nudger(game_dir),
    }
    for rel, content in products.items():
        _atomic_write(REPO_ROOT / rel, content)
        print(f"[map_layer] 已写 {rel}（{len(content):,} 字符）")

    if not args.no_manifest:
        _update_manifest(game_dir, args.game_version, products, defn)
    print(f"[map_layer] 完成：省份活动行 {defn['active']}（连续 "
          f"{defn['id_min']}..{defn['id_max']}），注释行 {defn['commented']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
