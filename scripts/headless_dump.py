# -*- coding: utf-8 -*-
"""无头 dump 导出器（2026-11-18 实测定案）：不进游戏、不开控制台，直接驱动
游戏 exe 执行 dump 控制台命令，命令执行完毕游戏自动退出。

机制依据：游戏自带的官方文档 `game\\_commandline_options.info`——
  -run_console_action=<控制台命令>   启动即执行该命令随后退出（application 态）
  -nographics                        无图形模式（官方"自动化测试用"参数）
  -mod="<.mod 文件路径>"              加载指定 mod（抄写室的 mod 加载态 dump）

实测限制（2026-11-18，Steam 版 CK3 1.21.0）：
  - 一次启动只能挂一条 action（早期态 clausewitz 对 dump_data_types 报
    "Unknown command" 且首条失败即中止启动），故两条命令各启动一次；
  - Steam 版需要 Steam 客户端在运行（steam_api 初始化）；
  - 产物与"手动进游戏开控制台导出"逐字节等价（game_layer --check PASS 实证）。

平台说明：默认按 **Steam 版**布局解析 exe（<安装目录>\\binaries\\ck3.exe；
<安装目录>\\game\\ 即 vanilla_index.py 的 --game-dir）。Microsoft Store /
Game Pass PC 版安装在 WindowsApps 下、目录布局与权限不同且不依赖 Steam——
本脚本未在该平台实测；其他布局可在 scripts/state/local_paths.json 写
"game_exe" 键直指 exe 路径适配。

用法（仓库根）：
  python scripts/headless_dump.py                           # 原版：两条 dump 命令
  python scripts/headless_dump.py --mod "<路径\\xxx.mod>"    # mod 加载态（Documents logs
                                                             # 变为合并视图，用完恢复原版）
  python scripts/headless_dump.py --game-root "<CK3 安装目录>"

退出码：0 = 两条命令全部成功且游戏进程已退出；非 0 = 有失败或残留进程。
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import config  # noqa: E402

DOC_LOGS = (Path.home() / "Documents" / "Paradox Interactive"
            / "Crusader Kings III" / "logs")
DUMP_COMMANDS = ("script_docs", "dump_data_types")
GAME_EXE_NAME = "ck3.exe"
LOCAL_CFG = config.REPO_ROOT / "scripts" / "state" / "local_paths.json"


def resolve_game_exe(cli_root: Path | None) -> Path:
    """解析游戏 exe：--game-root > local_paths.json(game_exe / game_dir 推导)
    > CK3_GAME_DIR 推导。Steam 版布局：安装目录 = game\\ 的上一级。"""
    if cli_root:
        exe = cli_root / "binaries" / GAME_EXE_NAME
        if exe.is_file():
            return exe
        raise SystemExit(f"[headless] {exe} 不存在（--game-root 应指 CK3 安装目录，"
                         "Steam 版布局为 <安装目录>\\binaries\\ck3.exe）")
    if LOCAL_CFG.is_file():
        cfg = json.loads(LOCAL_CFG.read_text(encoding="utf-8"))
        if cfg.get("game_exe"):
            p = Path(cfg["game_exe"])
            if p.is_file():
                return p
            print(f"[headless] 警告：local_paths.json 的 game_exe 不存在：{p}")
        gd = cfg.get("game_dir")
        if gd:
            p = Path(gd).parent / "binaries" / GAME_EXE_NAME
            if p.is_file():
                return p
    env = os.environ.get("CK3_GAME_DIR")
    if env:
        p = Path(env).parent / "binaries" / GAME_EXE_NAME
        if p.is_file():
            return p
    raise SystemExit(
        "[headless] 未找到游戏 exe。三选一：--game-root <CK3 安装目录>（Steam 版）"
        " / scripts/state/local_paths.json 写 game_exe 或 game_dir / 环境变量"
        " CK3_GAME_DIR（指 game\\ 目录）")


def _tasklist_running(image: str) -> bool | None:
    """tasklist 查进程；非 Windows / tasklist 不可用时返回 None（无法判定）。

    按字节匹配（tasklist 输出为本机代码页如 GBK，text=True 在 UTF-8 模式下
    会让解码线程崩掉得到空 stdout——实测踩坑）；进程名是纯 ASCII，字节匹配
    与代码页无关。
    """
    try:
        r = subprocess.run(["tasklist", "/FI", f"IMAGENAME eq {image}"],
                           capture_output=True, timeout=15)
    except (OSError, subprocess.TimeoutExpired):
        return None
    needle = image.lower().encode("ascii", "ignore")
    return needle in (r.stdout or b"").lower()


def run_dump(mod_file: Path | None = None,
             game_root: Path | None = None) -> int:
    """驱动游戏无头执行两条 dump 命令（各启动一次，跑完自动退出）。

    mod_file 非空时以该 mod 加载态导出（合并视图）——调用方负责之后恢复
    原版 dump。返回 0=全部成功。
    """
    exe = resolve_game_exe(game_root)
    print(f"[headless] 游戏 exe：{exe}（Steam 版布局；其他平台见模块 docstring）")
    if mod_file is not None and not mod_file.is_file():
        print(f"[headless] 错误：--mod 文件不存在：{mod_file}")
        return 2
    steam = _tasklist_running("steam.exe")
    if steam is False:
        print("[headless] 警告：未检测到 Steam 客户端进程——Steam 版通常无法启动，"
              "请先启动 Steam 再重试（非 Steam 平台可忽略）")

    rc = 0
    for cmd in DUMP_COMMANDS:
        args = [str(exe), "-debug_mode", "-nographics"]
        if mod_file is not None:
            # -mod 路径必须正斜杠：实测反斜杠形式游戏会静默不加载 mod
            #（命令照常执行、导出的是原版清单，2026-11-19 踩坑）
            args.append(f"-mod={mod_file.as_posix()}")
        args.append(f"-run_console_action={cmd}")
        print(f"[headless] 启动游戏：-run_console_action={cmd}"
              f"{'（-mod 加载态）' if mod_file is not None else ''} …")
        t0 = time.monotonic()
        try:
            r = subprocess.run(args, cwd=str(exe.parent.parent))
        except OSError as e:
            print(f"[headless] 启动失败：{e}")
            return 2
        dt = time.monotonic() - t0
        ok = r.returncode == 0
        print(f"[headless] {cmd}：{'OK' if ok else '失败'}（退出码 {r.returncode}，{dt:.0f}s）")
        if not ok:
            rc = 1

    # 退出确认（用户规约）：run_console_action 语义即"执行完退出"，subprocess
    # 已等待进程结束；此处兜底复查有无残留实例——只警告不击杀，避免误伤
    # 用户自己开着的游戏。
    time.sleep(2)
    lingering = _tasklist_running(GAME_EXE_NAME)
    if lingering:
        print(f"[headless] 警告：仍有 {GAME_EXE_NAME} 进程在运行（残留实例或用户"
              "自行启动的游戏）——请手动确认关闭后再进行后续步骤")
        rc = rc or 1
    elif lingering is None:
        print("[headless] 注：无法查询进程表（非 Windows？），跳过退出确认")
    else:
        print("[headless] 游戏进程已全部退出 ✓")

    if rc == 0:
        print(f"[headless] dump 产物目录：{DOC_LOGS}")
    return rc


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="无头 dump 导出器（驱动游戏 exe "
                                             "执行控制台 dump 命令后自动退出）")
    ap.add_argument("--mod", default=None,
                    help=".mod 文件路径：以该 mod 加载态导出（合并视图）")
    ap.add_argument("--game-root", default=None,
                    help="CK3 安装目录（Steam 版布局 <目录>\\binaries\\ck3.exe）")
    args = ap.parse_args(argv)
    return run_dump(Path(args.mod) if args.mod else None,
                    Path(args.game_root) if args.game_root else None)


if __name__ == "__main__":
    raise SystemExit(main())
