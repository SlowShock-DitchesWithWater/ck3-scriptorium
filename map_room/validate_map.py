#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CK3 地图校验器（地图室·工具层）——对 mod 的 map_data 做机器可查的硬约束检查。

规则来源（权威顺序同知识库）：
1. game_docs/map_docs/map_data_dossier.md（游戏 1.20.1 实测档案，最高权威）；
2. pages/Map modding.md（wiki oldid 34676，1.1 时代，冲突时以上者为准）。
严重度按原版实测校准：原版自身就违反的规则（如 definition.csv 存在 1 组
重复色）记 WARN 而非 ERROR。

用法（任意目录）：
  python map_room/validate_map.py <mod根目录> [--game-root <CK3的game目录>] [--deep]

<mod根目录> = 含 map_data\\ 的目录（mod 文件夹，或直接传游戏 game\\ 校验原版）。
mod 里缺省的 map_data 文件视为继承原版：给了 --game-root 就对继承文件同样
检查；不给则记 SKIP。退出码 = ERROR 数（0 = 全绿或仅有 WARN/SKIP）。

依赖：Pillow（像素解码与调色板）；--deep 的河流拓扑检查另需 numpy，缺则跳过。
"""
from __future__ import annotations

import argparse
import re
import struct
import sys
from pathlib import Path

try:
    from PIL import Image
    Image.MAX_IMAGE_PIXELS = None   # 原版 169M 像素，关闭 Pillow 安全限制
except ImportError:                  # pragma: no cover
    print("错误：缺少 Pillow（pip install pillow）", file=sys.stderr)
    raise SystemExit(2)

# ---- 内置权威常量（CK3 1.20.1 实测；--game-root 可覆盖部分）----
TERRAIN_TYPES_1_20_1 = {            # common/terrain_types 顶层块名，17 个
    "coastal_sea", "desert", "desert_mountains", "drylands", "farmlands",
    "floodplains", "forest", "hills", "jungle", "mountains", "oasis",
    "plains", "sea", "steppe", "taiga", "terraced_hills", "wetlands",
}
RIVERS_PALETTE_1_20_1 = {           # 原版 rivers.png 实际用色（19）
    (0x00, 0xFF, 0x00), (0xFF, 0x00, 0x00), (0xFF, 0xFC, 0x00),
    (0xFF, 0x00, 0x80), (0xFF, 0xFF, 0xFF),                    # wiki 记载 5 特殊色
    (0x00, 0x00, 0x64), (0x00, 0x00, 0x96), (0x00, 0x00, 0xC8),
    (0x00, 0x00, 0xE1), (0x00, 0x00, 0xFF), (0x00, 0x64, 0xFF),
    (0x00, 0x96, 0xFF), (0x00, 0xC8, 0xFF), (0x00, 0xE1, 0xFF),  # 蓝色梯度
}
RIVERS_TOLERATED = {                # wiki 未记载但原版在用 → WARN 而非 ERROR
    (0x00, 0x55, 0x00), (0x00, 0x7D, 0x00), (0x00, 0x9E, 0x00),
    (0x18, 0xCE, 0x00), (0x02, 0x00, 0x01),
}
ADJ_TYPES = {"sea", "river_large"}  # 原版 adjacencies.csv Type 列实测
KNOWN_GHOST_REFS = {"continent"}    # default.map 引用但原版亦无此文件 → WARN

PNG_SIG = b"\x89PNG\r\n\x1a\n"
COLOR_TYPE_NAME = {0: "灰度", 2: "RGB", 3: "索引色", 4: "灰度+Alpha", 6: "RGBA"}


class Report:
    def __init__(self) -> None:
        self.errors = 0
        self.lines: list[str] = []

    def add(self, sev: str, code: str, msg: str) -> None:
        self.lines.append(f"[{sev} {code}] {msg}")
        if sev == "ERROR":
            self.errors += 1

    def ok(self, code: str, msg: str) -> None:
        self.add("PASS", code, msg)

    def skip(self, code: str, msg: str) -> None:
        self.add("SKIP", code, msg)


def png_header(path: Path) -> tuple[int, int, int, int]:
    """stdlib 解析 IHDR → (宽, 高, 位深, 颜色类型)。"""
    with path.open("rb") as f:
        head = f.read(33)
    if len(head) < 33 or head[:8] != PNG_SIG:
        raise ValueError(f"{path.name}: 不是有效 PNG")
    w, h = struct.unpack(">II", head[16:24])
    return w, h, head[24], head[25]


def spec(w: int, h: int, d: int, t: int) -> str:
    return f"{w}×{h} · {d}bit {COLOR_TYPE_NAME.get(t, '?')}"


def parse_definition(path: Path) -> dict:
    """definition.csv → 活动/注释行、色→id、id→名。"""
    out = {"active": {}, "colors": {}, "commented": 0, "bad_rows": []}
    for lineno, raw in enumerate(
            path.read_text(encoding="utf-8-sig", errors="replace").splitlines(), 1):
        line = raw.strip()
        if not line:
            continue
        commented = line.startswith("#")
        body = line[1:] if commented else line
        parts = body.split(";")
        if len(parts) < 5 or not parts[0].strip().isdigit():
            if not commented:
                out["bad_rows"].append((lineno, line[:40]))
            continue
        if commented:
            out["commented"] += 1
            continue
        pid = int(parts[0])
        try:
            rgb = (int(parts[1]), int(parts[2]), int(parts[3]))
        except ValueError:
            out["bad_rows"].append((lineno, line[:40]))
            continue
        out["active"][pid] = parts[4] if len(parts) > 4 else ""
        out["colors"].setdefault(rgb, []).append(pid)
    return out


def validate(root: Path, game_root: Path | None, deep: bool) -> Report:
    rep = Report()
    md = root / "map_data"

    def resolve(name: str) -> Path | None:
        """mod 文件优先，缺省视为继承原版（--game-root 提供则检查继承件）。"""
        p = md / name
        if p.is_file():
            return p
        if game_root and (game_root / "map_data" / name).is_file():
            return game_root / "map_data" / name   # 继承原版
        return None

    # ---- M01 definition.csv ----
    dpath = resolve("definition.csv")
    if not dpath:
        rep.add("ERROR", "M01", "map_data/definition.csv 缺失（mod 与原版都没有）")
        return rep
    d = parse_definition(dpath)
    where = "mod" if (md / "definition.csv").is_file() else "原版继承"
    rep.ok("M01", f"definition.csv 解析成功（{where}）："
                  f"{len(d['active'])} 活动行 / {d['commented']} 注释行")
    for lineno, frag in d["bad_rows"][:5]:
        rep.add("WARN", "M01", f"第 {lineno} 行无法解析：{frag}…")

    ids = sorted(d["active"])
    id_set = set(ids)

    # ---- M02 ID 连续性 ----
    if not ids:
        rep.add("ERROR", "M02", "definition.csv 无有效活动行")
    else:
        gaps = [i for i in range(ids[0], ids[-1] + 1) if i not in id_set]
        if gaps:
            rep.add("ERROR", "M02", f"活动 id 不连续（wiki：必须连续否则崩溃），"
                                    f"缺口 {len(gaps)} 个：{gaps[:10]}")
        else:
            rep.ok("M02", f"id {ids[0]}..{ids[-1]} 完全连续")

    # ---- M03 颜色唯一性 ----
    dups = {c: p for c, p in d["colors"].items() if len(p) > 1}
    for rgb, pids in list(dups.items())[:10]:
        h = "#%02x%02x%02x" % rgb
        rep.add("WARN", "M03", f"{h} 被 id {'/'.join(map(str, pids))} 重复使用"
                               f"（原版实测自带 1 组，故 WARN；建议消除）")
    black = d["colors"].get((0, 0, 0), [])
    if len(black) > 1:
        rep.add("WARN", "M03", "黑色 (0,0,0) 被 id "
                               f"{'/'.join(map(str, black))} 共享——wiki：黑为不可"
                               "通行地形保留色（原版 = id 0 水体 + 阿尔卑斯类不可"
                               "行省共享黑，颜色承载语义、引擎可容忍；自定义地图"
                               "慎用）")
    elif not black:
        rep.add("WARN", "M03", "缺 id 0（水体黑位）——自定义地图请保留 0;0;0;0;x;x;")
    else:
        rep.ok("M03", f"颜色唯一（重复 {len(dups)} 组，黑位 id {black[0]}）")

    # ---- M04/M05 provinces.png ----
    ppath = resolve("provinces.png")
    img_colors: set[tuple[int, int, int]] = set()
    if not ppath:
        rep.add("ERROR", "M04", "map_data/provinces.png 缺失")
    else:
        w, h, dep, ct = png_header(ppath)
        src = "mod" if (md / "provinces.png").is_file() else "原版继承"
        if ct not in (2,) or dep != 8:
            if ct == 3:
                rep.add("ERROR", "M04", "provinces.png 是索引色（P）——wiki 要求 "
                                        "8/24bit RGB 平色，索引色会 CTD")
            else:
                rep.add("WARN", "M04", f"provinces.png 颜色类型 {ct}/位深 {dep}"
                                       "（wiki 要求 8bit RGB）")
        else:
            rep.ok("M04", f"provinces.png {spec(w, h, dep, ct)}（{src}）")
        rpath = resolve("rivers.png")
        if rpath:
            rw, rh, _, _ = png_header(rpath)
            if (rw, rh) != (w, h):
                rep.add("ERROR", "M04", f"rivers.png {rw}×{rh} 与 provinces.png "
                                        f"{w}×{h} 尺寸不一致（wiki：必须一致否则崩溃）")
            else:
                rep.ok("M04", f"rivers.png 与 provinces.png 尺寸一致（{w}×{h}）")
        # 像素级色集（PIL 解码；numpy 缺失则跳过）
        im = Image.open(ppath)
        if im.mode not in ("RGB", "RGBA"):
            rep.add("ERROR", "M05", f"provinces.png 解码模式 {im.mode}，非 RGB")
        else:
            try:
                import numpy as np
            except ImportError:
                np = None
                rep.skip("M05", "缺 numpy，跳过像素级色集检查")
            if np is not None:
                arr = np.asarray(im.convert("RGB"), dtype=np.uint8)
                packed = (arr[:, :, 0].astype(np.uint32) << 16
                          | arr[:, :, 1].astype(np.uint32) << 8
                          | arr[:, :, 2].astype(np.uint32))
                uniq = np.unique(packed)
                img_colors = {(int(u) >> 16, (int(u) >> 8) & 0xFF, int(u) & 0xFF)
                              for u in uniq.tolist()}
                defined = set(d["colors"])
                extra = img_colors - defined
                missing = {c for c, p in d["colors"].items()
                           if len(p) == 1 and c not in img_colors and p != [0]}
                if extra:
                    sev = "WARN" if len(extra) <= 3 else "ERROR"
                    sample = " ".join("#%02x%02x%02x" % c for c in sorted(extra)[:8])
                    rep.add(sev, "M05", f"provinces.png 有 {len(extra)} 种颜色不在 "
                                        f"definition.csv（疑抗锯齿/杂色）：{sample}")
                else:
                    rep.ok("M05", "provinces.png 颜色全部在 definition.csv 中")
                if missing:
                    sample = " ".join(f"#{c[0]:02x}{c[1]:02x}{c[2]:02x}(id "
                                      f"{'/'.join(map(str, d['colors'][c]))})"
                                      for c in sorted(missing)[:8])
                    rep.add("WARN", "M05", f"definition.csv 有 {len(missing)} 色未出现在 "
                                           f"图上（定义了没用，不致命）：{sample}")

    # ---- M06 rivers.png 调色板 ----
    rpath = resolve("rivers.png")
    if not rpath:
        rep.add("ERROR", "M06", "map_data/rivers.png 缺失")
    else:
        im = Image.open(rpath)
        if im.mode != "P":
            rep.add("ERROR", "M06", f"rivers.png 模式为 {im.mode}，必须是索引色（P）"
                                    "——非索引色即 CTD（wiki + 原版实测）")
        else:
            pal = im.getpalette() or []
            cols_all = {(pal[i], pal[i + 1], pal[i + 2])
                        for i in range(0, len(pal), 3)}
            try:    # 只检查被像素实际引用的槽位（GIMP 等工具的 padding 槽任意）
                import numpy as np
                used = np.unique(np.asarray(im)).tolist()
            except ImportError:
                # 纯 PIL 回退：索引图槽位 ≤256，getcolors(256) 必能枚举
                used = [idx for _, idx in (im.getcolors(256) or [])]
            cols = {(pal[3 * i], pal[3 * i + 1], pal[3 * i + 2])
                    for i in used if 3 * i + 2 < len(pal)}
            unknown = cols - RIVERS_PALETTE_1_20_1 - RIVERS_TOLERATED
            if game_root and (game_root / "map_data/rivers.png").is_file():
                vp = Image.open(game_root / "map_data/rivers.png").getpalette() or []
                vanilla_cols = {(vp[i], vp[i + 1], vp[i + 2])
                                for i in range(0, len(vp), 3)}
                unknown -= vanilla_cols        # 原版调色板内色一律放行
                tolerated_from_vanilla = cols & vanilla_cols - RIVERS_PALETTE_1_20_1
                for c in sorted(tolerated_from_vanilla):
                    rep.add("WARN", "M06", f"调色板含原版同款未记载色 "
                                           f"#{c[0]:02x}{c[1]:02x}{c[2]:02x}")
            if unknown:
                sample = " ".join(f"#{c[0]:02x}{c[1]:02x}{c[2]:02x}"
                                  for c in sorted(unknown)[:8])
                rep.add("ERROR", "M06", f"rivers.png 调色板有 {len(unknown)} 种"
                                        f"非允许色（CTD 风险）：{sample}")
            else:
                rep.ok("M06", f"rivers.png 索引色调色板合法（{len(cols)} 色）")

    # ---- M07/M08 heightmap 体系 ----
    hpath = resolve("heightmap.png")
    pw = ph = None
    if ppath:
        pw, ph, _, _ = png_header(ppath)
    if not hpath:
        rep.add("ERROR", "M07", "map_data/heightmap.png 缺失")
    else:
        w, h, dep, ct = png_header(hpath)
        src = "mod" if (md / "heightmap.png").is_file() else "原版继承"
        if ct != 0 or dep != 16:
            rep.add("ERROR", "M07", f"heightmap.png {spec(w, h, dep, ct)}——"
                                    "要求 16bit 灰度（colortype 0）")
        else:
            rep.ok("M07", f"heightmap.png {spec(w, h, dep, ct)}（{src}）")
        if pw is not None:
            if (w, h) == (2 * pw, 2 * ph):
                rep.ok("M07", "尺寸关系符合 1.18+ 规则（heightmap = 省份图 2 倍边长）")
                ipath = resolve("indirection_heightmap.png")
                if ipath:
                    iw, ih, _, _ = png_header(ipath)
                    if (iw, ih) == (pw // 32, ph // 32):
                        rep.ok("M07", f"indirection {iw}×{ih} = 省份图 1/32（1.20 实测）")
                    else:
                        rep.add("WARN", "M07", f"indirection {iw}×{ih} ≠ 省份图 "
                                               f"{pw // 32}×{ph // 32}（1.18+ 寻址图；"
                                               "若为编辑器 repack 产物会自行重写）")
            elif (w, h) == (pw, ph):
                rep.add("WARN", "M07", "heightmap 与省份图同尺寸——这是 ≤1.17 的"
                                       "旧规则；对 CK3 1.18+ 会渲染异常")
            else:
                rep.add("ERROR", "M07", f"heightmap {w}×{h} 与省份图 {pw}×{ph} "
                                        "既非 2 倍（1.18+）也非同尺寸（≤1.17）")
    mpath = resolve("heightmap.heightmap")
    if not mpath:
        rep.add("WARN", "M08", "map_data/heightmap.heightmap 缺失")
    else:
        text = mpath.read_text(encoding="utf-8-sig", errors="replace")
        m = re.search(r"original_heightmap_size\s*=\s*\{\s*(\d+)\s+(\d+)", text)
        if not m:
            rep.add("ERROR", "M08", "heightmap.heightmap 缺 original_heightmap_size")
        elif hpath:
            mw, mh = int(m.group(1)), int(m.group(2))
            hw, hh, _, _ = png_header(hpath)
            if (mw, mh) != (hw, hh):
                rep.add("ERROR", "M08", f"original_heightmap_size {{{mw} {mh}}} ≠ "
                                        f"heightmap.png 实际 {hw}×{hh}")
            else:
                rep.ok("M08", f"original_heightmap_size 与 heightmap.png 一致（{hw}×{hh}）")

    # ---- M09 adjacencies.csv ----
    apath = resolve("adjacencies.csv")
    if not apath:
        rep.skip("M09", "adjacencies.csv 缺失（可选文件，跳过）")
    else:
        rows = [ln for ln in apath.read_text(
            encoding="utf-8-sig", errors="replace").splitlines() if ln.strip()]
        body = [ln for ln in rows[1:] if not ln.strip().startswith("#")]
        bad_ids: list[str] = []
        bad_types: list[str] = []
        for ln in body:
            p = ln.split(";")
            if p[0].strip() == "-1":
                continue
            for idx in (0, 1):
                v = p[idx].strip()
                if v.isdigit() and int(v) not in id_set:
                    bad_ids.append(f"{v}@{p[3] if len(p) > 3 else '?'}")
            if len(p) > 2 and p[2].strip() and p[2].strip() not in ADJ_TYPES:
                bad_types.append(p[2].strip())
        if bad_ids:
            rep.add("ERROR", "M09", f"adjacencies 引用了 definition.csv 不存在的 id："
                                    f"{' '.join(bad_ids[:8])}")
        if bad_types:
            rep.add("ERROR", "M09", f"Type 列非法取值：{' '.join(sorted(set(bad_types))[:8])}"
                                    f"（实测合法：{'/'.join(sorted(ADJ_TYPES))}）")
        if not bad_ids and not bad_types:
            rep.ok("M09", f"adjacencies.csv {len(body)} 行，id/Type 合法")
        if not body or not body[-1].strip().startswith("-1;-1"):
            rep.add("WARN", "M09", "末尾缺 -1;-1;;-1;… 终止行（wiki：缺失会无限载入）")
        else:
            rep.ok("M09", "终止行存在")

    # ---- M10 default.map ----
    dmp = resolve("default.map")
    if not dmp:
        rep.add("WARN", "M10", "map_data/default.map 缺失（继承原版时省份数必须一致）")
    else:
        bad_zone: list[str] = []
        zones = 0
        for raw in dmp.read_text(encoding="utf-8-sig",
                                 errors="replace").splitlines():
            line = raw.strip()
            m = re.match(r"^(sea_zones|river_provinces)\s*=\s*(RANGE|LIST)\s*\{(.*)\}",
                         line)
            if not m or line.startswith("#"):
                continue
            zones += 1
            nums = [int(x) for x in re.findall(r"\d+", m.group(3))]
            if m.group(2) == "RANGE" and len(nums) >= 2 and nums[0] > nums[1]:
                bad_zone.append(f"RANGE{{{nums[0]} {nums[1]}}} 倒序")
            bad_zone += [f"{n}" for n in nums if n not in id_set]
        if bad_zone:
            rep.add("ERROR", "M10", "sea_zones/river_provinces 引用了不存在的 id："
                                    f"{' '.join(bad_zone[:10])}")
        else:
            rep.ok("M10", f"sea_zones/river_provinces 共 {zones} 区段，id 全部有效")
        for raw in dmp.read_text(encoding="utf-8-sig",
                                 errors="replace").splitlines():
            line = raw.strip()
            m = re.match(r"^(\w+)\s*=\s*\"([^\"]+)\"", line)
            if not m or line.startswith("#"):
                continue
            key, ref = m.group(1), m.group(2)
            if not (md / ref).is_file():
                sev = "WARN" if key in KNOWN_GHOST_REFS else "ERROR"
                note = "（原版亦无此文件，幽灵引用）" if key in KNOWN_GHOST_REFS else ""
                rep.add(sev, "M10", f"default.map 引用的 {ref} 不存在{note}")

    # ---- M11 province_terrain ----
    terr_files = sorted((root / "common" / "province_terrain").glob("*.txt"))
    if game_root:
        terr_files += sorted((game_root / "common" / "province_terrain").glob("*.txt"))
    if not terr_files:
        rep.skip("M11", "common/province_terrain/ 无文件（跳过）")
    else:
        valid_terr = set(TERRAIN_TYPES_1_20_1)
        if game_root:
            for tf in (game_root / "common" / "terrain_types").glob("*.txt"):
                for bm in re.finditer(r"^([A-Za-z0-9_]+)\s*=\s*\{",
                                      tf.read_text(encoding="utf-8-sig",
                                                   errors="replace"), re.M):
                    valid_terr.add(bm.group(1))
        bad: list[str] = []
        covered = set()
        for tf in terr_files:
            for tm in re.finditer(r"^\s*(\d+)\s*=\s*([A-Za-z0-9_]+)",
                                  tf.read_text(encoding="utf-8-sig",
                                               errors="replace"), re.M):
                pid, terr = int(tm.group(1)), tm.group(2)
                covered.add(pid)
                if pid not in id_set:
                    bad.append(f"id {pid} 不存在")
                elif terr not in valid_terr:
                    bad.append(f"id {pid} 地形 {terr}")
        if bad:
            rep.add("ERROR", "M11", f"province_terrain 问题 {len(bad)} 处："
                                    f"{'；'.join(bad[:8])}")
        else:
            rep.ok("M11", f"province_terrain {len(covered)} 条全部有效")
        rep.add("INFO", "M11", f"地形覆盖 {len(covered & id_set)}/{len(id_set)} 个省份"
                               "（海域/无地形省份不计）")

    # ---- M12 landed_titles province 引用 ----
    title_files = sorted((root / "common" / "landed_titles").glob("*.txt"))
    if not title_files:
        rep.skip("M12", "common/landed_titles/ 无文件（跳过）")
    else:
        refs: set[int] = set()
        bad: list[int] = []
        for tf in title_files:
            for pm in re.finditer(r"\bprovince\s*=\s*(\d+)",
                                  tf.read_text(encoding="utf-8-sig",
                                               errors="replace")):
                pid = int(pm.group(1))
                refs.add(pid)
                if pid not in id_set:
                    bad.append(pid)
        if bad:
            rep.add("ERROR", "M12", f"landed_titles 引用了不存在的省份 id："
                                    f"{' '.join(map(str, sorted(bad)[:10]))}")
        else:
            rep.ok("M12", f"landed_titles 引用 {len(refs)} 个省份 id 全部有效")
        orphan = id_set - refs - {0}
        rep.add("INFO", "M12", f"{len(orphan)} 个省份无 b_ 头衔（海域正常；"
                               f"陆地缺头衔则该省不可用）")

    # ---- M13 河流拓扑（--deep）----
    if deep and rpath and Image.open(rpath).mode == "P":
        try:
            import numpy as np
        except ImportError:
            rep.skip("M13", "缺 numpy，跳过河流拓扑深检")
        else:
            arr = np.asarray(Image.open(rpath))
            # 河流像素 = 蓝梯度 + 三特殊色（绿/红/黄）；品红/白/陆地色不计
            pal = (Image.open(rpath).getpalette() or [])
            special_idx = {i for i in range(0, len(pal), 3)
                           if (pal[i], pal[i + 1], pal[i + 2]) in
                           {(0, 255, 0), (255, 0, 0), (255, 252, 0)}}
            blue_idx = {i for i in range(0, len(pal), 3)
                        if pal[i] == 0 and pal[i + 1] == 0 and pal[i + 2] > 0}
            river = np.isin(arr, sorted(blue_idx | special_idx))
            neigh = sum(np.roll(river, s, axis=ax) for ax, s in
                        ((0, 1), (0, -1), (1, 1), (1, -1)))
            blue_px = np.isin(arr, sorted(blue_idx))
            viol_blue = int(np.sum(blue_px & (neigh > 2)))
            special_px = np.isin(arr, sorted(special_idx))
            viol_special = int(np.sum(special_px & (neigh > 3)))
            if viol_blue or viol_special:
                rep.add("WARN", "M13", f"河流拓扑疑点：蓝色像素邻接>2 的 "
                                        f"{viol_blue} 个、特殊色邻接>3 的 "
                                        f"{viol_special} 个（wiki 约束，启发式检查）")
            else:
                rep.ok("M13", "河流拓扑约束（正交邻接数）通过")
    elif deep:
        rep.skip("M13", "rivers.png 非索引色或缺失，跳过深检")

    return rep


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(
        description="CK3 地图校验器（规则：game_docs/map_docs 实测档案 + wiki）")
    ap.add_argument("target", help="mod 根目录（含 map_data\\），或游戏 game\\ 目录")
    ap.add_argument("--game-root", help="CK3 的 game 目录（解析继承文件/原版口径）")
    ap.add_argument("--deep", action="store_true",
                    help="附加河流拓扑深检（需 numpy，较慢）")
    args = ap.parse_args(argv)

    root = Path(args.target)
    if not root.is_dir():
        print(f"错误：目录不存在：{root}", file=sys.stderr)
        return 2
    game_root = Path(args.game_root) if args.game_root else None
    if game_root and not game_root.is_dir():
        print(f"错误：--game-root 目录不存在：{game_root}", file=sys.stderr)
        return 2

    rep = validate(root, game_root, args.deep)
    print(f"== CK3 地图校验 · {root} ==")
    for ln in rep.lines:
        print(ln)
    n_err = rep.errors
    n_warn = sum(1 for ln in rep.lines if ln.startswith("[WARN"))
    n_skip = sum(1 for ln in rep.lines if ln.startswith("[SKIP"))
    print(f"== 结果：ERROR {n_err} · WARN {n_warn} · SKIP {n_skip} ==")
    if n_err == 0:
        print("无致命问题（WARN 项建议处理，SKIP 项为缺文件未检查）")
    return n_err


if __name__ == "__main__":
    raise SystemExit(main())
