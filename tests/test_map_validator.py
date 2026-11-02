# -*- coding: utf-8 -*-
r"""地图校验器夹具测试：合成微型 mod（8×4 省份图），先验证全绿，
再逐项注入缺陷验证各检查会开火。运行（仓库根）：
    python tests\test_map_validator.py
退出码 0 = 全部通过。零网络；依赖 Pillow（与 map_room/validate_map.py 同）。
"""
import contextlib
import io
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "map_room"))

try:
    from PIL import Image
except ImportError:                 # clone/CI 环境可能未装 Pillow：明确跳过不判 FAIL
    print("SKIP  缺少 Pillow（pip install pillow）——地图校验器测试整体跳过")
    raise SystemExit(0)

try:
    import numpy                    # M05/M06 像素级检查依赖 numpy
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False

import validate_map as vm

_passed = 0
_failed = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global _passed, _failed
    print(f"{'PASS' if ok else 'FAIL'}  {label}" + (f"  —— {detail}" if not ok and detail else ""))
    _passed += ok
    _failed += not ok


def build_fixture(base: Path) -> Path:
    """合成微型 mod：省份图 8×4（id 0 水体 + id 1/2 陆地）。"""
    md = base / "map_data"
    (md / "").mkdir(parents=True, exist_ok=True)
    (md / "definition.csv").write_text(
        "0;0;0;0;x;x;\n1;255;0;0;REDLAND;x;\n2;0;0;255;BLUELAND;x;\n",
        encoding="utf-8")
    # provinces.png：三块平色（左 1/3 红、中 1/3 蓝、右 1/3 黑水体）
    prov = Image.new("RGB", (8, 4))
    for x in range(8):
        for y in range(4):
            prov.putpixel((x, y), (255, 0, 0) if x < 3
                          else ((0, 0, 255) if x < 6 else (0, 0, 0)))
    prov.save(md / "provinces.png")
    # rivers.png：索引色，全白（陆地）——调色板只放允许色
    riv = Image.new("P", (8, 4))
    riv.putpalette([0xFF, 0xFF, 0xFF] + [0] * 765)
    riv.save(md / "rivers.png")
    # heightmap.png：16bit 灰度 16×8（省份图 2 倍，1.18+ 规则）
    hm = Image.new("I;16", (16, 8), 100)
    hm.save(md / "heightmap.png")
    (md / "heightmap.heightmap").write_text(
        'heightmap_file="map_data/packed_heightmap.png"\n'
        'indirection_file="map_data/indirection_heightmap.png"\n'
        "original_heightmap_size={ 16 8 }\n", encoding="utf-8")
    (md / "adjacencies.csv").write_text(
        "From;To;Type;Through;start_x;start_y;stop_x;stop_y;Comment\n"
        "1;2;sea;2;-1;-1;-1;-1;bridge\n"
        "-1;-1;;-1;-1;-1;-1;-1;\n", encoding="utf-8")
    (md / "default.map").write_text(
        'definitions = "definition.csv"\nprovinces = "provinces.png"\n'
        'rivers = "rivers.png"\ntopology = "heightmap.heightmap"\n'
        'adjacencies = "adjacencies.csv"\n'
        "sea_zones = LIST { 2 }\n", encoding="utf-8")
    pt = base / "common" / "province_terrain"
    pt.mkdir(parents=True, exist_ok=True)
    (pt / "00_province_terrain.txt").write_text(
        "default_land=plains\ndefault_sea=sea\n1=plains\n2=sea\n",
        encoding="utf-8")
    lt = base / "common" / "landed_titles"
    lt.mkdir(parents=True, exist_ok=True)
    (lt / "00_titles.txt").write_text(
        "c_test = {\n\tcolor = { 1 1 1 }\n\tb_barony = {\n\t\tprovince = 1\n\t}\n}\n",
        encoding="utf-8")
    return base


def run(root: Path) -> tuple[vm.Report, str]:
    with contextlib.redirect_stdout(io.StringIO()):
        rep = vm.validate(root, None, False)
    return rep, "\n".join(rep.lines)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    tmp = Path(tempfile.mkdtemp(prefix="ck3_mapval_"))
    try:
        # --- 1. 干净夹具：0 ERROR ---
        root = build_fixture(tmp / "clean")
        rep, out = run(root)
        check("干净夹具：0 ERROR", rep.errors == 0, out)

        # --- 2. 注入缺陷：每项都应开火（numpy 用例在其缺失时跳过） ---
        cases = [
            ("M02 id 缺口", lambda r: (r / "map_data/definition.csv").write_text(
                "0;0;0;0;x;x;\n2;0;0;255;BLUELAND;x;\n", encoding="utf-8"), "M02", True),
            ("M03 非 id0 用黑+重复", lambda r: (r / "map_data/definition.csv").write_text(
                "0;0;0;0;x;x;\n1;0;0;0;BLACK;x;\n1;0;0;0;DUP;x;\n",
                encoding="utf-8"), "M03", True),
            ("M05 杂色", lambda r: _repaint(r, (254, 0, 0)), "M05", HAS_NUMPY),
            ("M06 非法调色板", lambda r: _bad_palette(r), "M06", True),
            ("M07 高度图尺寸错", lambda r: Image.new(
                "I;16", (8, 4), 100).save(r / "map_data/heightmap.png"), "M07", True),
            ("M08 元数据尺寸错", lambda r: (r / "map_data/heightmap.heightmap").write_text(
                "original_heightmap_size={ 99 99 }\n", encoding="utf-8"), "M08", True),
            ("M09 引用坏 id", lambda r: (r / "map_data/adjacencies.csv").write_text(
                "From;To;Type;Through;start_x;start_y;stop_x;stop_y;Comment\n"
                "1;77;sea;2;-1;-1;-1;-1;bad\n", encoding="utf-8"), "M09", True),
            ("M10 sea_zones 坏 id", lambda r: (r / "map_data/default.map").write_text(
                "sea_zones = LIST { 42 }\n", encoding="utf-8"), "M10", True),
            ("M11 地形名非法", lambda r: (r / "common/province_terrain/00_province_terrain.txt").write_text(
                "default_land=plains\n1=mars terrain\n", encoding="utf-8"), "M11", True),
            ("M12 头衔引用坏 id", lambda r: (r / "common/landed_titles/00_titles.txt").write_text(
                "b_barony = { province = 99 }\n", encoding="utf-8"), "M12", True),
        ]
        for label, mutate, code, runnable in cases:
            if not runnable:
                check(f"缺陷检测：{label}（缺 numpy，跳过）", True)
                continue
            case_dir = tmp / ("case_" + code)
            root2 = build_fixture(case_dir)
            mutate(root2)
            rep2, out2 = run(root2)
            fired = any(f"[ERROR {code}]" in ln or f"[WARN {code}]" in ln
                        for ln in rep2.lines)
            check(f"缺陷检测：{label} 触发 {code}", fired, out2)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print(f"\n汇总：PASS {_passed} / FAIL {_failed}")
    return 1 if _failed else 0


def _repaint(root: Path, color: tuple[int, int, int]) -> None:
    p = root / "map_data/provinces.png"
    im = Image.open(p).convert("RGB")
    im.putpixel((7, 3), color)          # 定义外杂色（抗锯齿模拟）
    im.save(p)


def _bad_palette(root: Path) -> None:
    p = root / "map_data/rivers.png"
    im = Image.open(p)
    im.putpalette([0x12, 0x34, 0x56] + [0] * 765)   # 非允许色
    im.save(p)


if __name__ == "__main__":
    raise SystemExit(main())
