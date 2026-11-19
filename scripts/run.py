# -*- coding: utf-8 -*-
"""管线统一入口：一条命令跑通四阶段 + 质量门；一条命令刷新原版游戏层。

用法：
    python scripts/run.py --page Scripting            # 全流程（抓取→清洗→组织→建目录→质量门）
    python scripts/run.py --page Scripting --force    # 忽略已抓记录强制重抓
    python scripts/run.py --stage clean --page Scripting   # 只跑某一阶段
                                                      # 可选：crawl/clean/organize/catalog/gate/all
    python scripts/run.py --stage game                # 原版游戏层三通道一条命令刷新：
                                                      # game_layer → vanilla_index → map_layer
                                                      # → catalog（游戏层区块）→ 质量门
    python scripts/run.py --stage game --auto         # 同上，且先无头驱动游戏导出两条
                                                      # dump 命令（scripts/headless_dump.py，
                                                      # Steam 版实测；免手动进游戏开控制台）
                                                      # （mod 侧同构入口：copy_room.py --build --auto）

各阶段可独立重复运行且幂等（详见 docs/pipeline.md）。
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import catalog  # noqa: E402
import clean  # noqa: E402
import crawl  # noqa: E402
import game_layer  # noqa: E402
import map_layer  # noqa: E402
import organize  # noqa: E402
import quality_gate  # noqa: E402
import vanilla_index  # noqa: E402
from lib import config  # noqa: E402

# 阶段执行顺序（pipeline 契约：后一阶段只依赖前一阶段的磁盘产物）
STAGES = ("crawl", "clean", "organize", "catalog", "gate")

# dump 哨兵文件：script_docs 白名单首个产物（game_layer 同款判据的简化版）
DUMP_SENTINEL = "effects.log"
DOC_LOGS = (Path.home() / "Documents" / "Paradox Interactive"
            / "Crusader Kings III" / "logs")


def resolve_dump_source() -> Path | None:
    """定位最新的 script_docs dump：仓库 game logs\\ 与 Documents logs\\ 二选一。

    两处都有哨兵文件时取 mtime 较新者（游戏更新后新 dump 总在 Documents；
    game logs\\ 是仓库归档副本），并打印决策依据；都没有则返回 None。
    """
    repo_logs = config.REPO_ROOT / "game logs"
    cands = [(d / DUMP_SENTINEL) for d in (repo_logs, DOC_LOGS)]
    cands = [s for s in cands if s.is_file()]
    if not cands:
        return None
    if len(cands) == 2 and cands[0].stat().st_mtime < cands[1].stat().st_mtime:
        cands.reverse()   # Documents 的 dump 更新——优先
    chosen = cands[0]
    note = "（两处均有，取 effects.log 较新者）" if len(cands) == 2 else ""
    print(f"[run] dump 源：{chosen.parent}{note}")
    return chosen.parent


def refresh_game_layers() -> int:
    """--stage game：原版三通道 + catalog 游戏层区块 + 质量门，一条命令。"""
    source = resolve_dump_source()
    if source is None:
        print(f"[run] 未找到 script_docs dump（哨兵 {DUMP_SENTINEL}）。"
              "请以 -debug_mode 启动游戏，在控制台跑 script_docs 与 "
              "dump_data_types 两条命令后重试。查找位置：\n"
              f"  {config.REPO_ROOT / 'game logs'}\n  {DOC_LOGS}")
        return 2
    # 版本一次解析、三通道同标：game_layer 自带提取（code_revisions.log→
    # debug.log→基准默认），vanilla_index/map_layer 无提取能力，显式传参
    version, version_source = game_layer.extract_game_version(source)
    print(f"[run] 游戏版本：{version}（{version_source}）——三通道统一标注")
    steps = [
        ("签名层 game_layer", lambda: game_layer.main(["--source", str(source)])),
        # game-dir 三级解析（--game-dir 缺省 → CK3_GAME_DIR →
        # scripts/state/local_paths.json），由 vanilla_index 统一处理
        ("结构层 vanilla_index",
         lambda: vanilla_index.main(["--game-version", version])),
        ("地图层 map_layer",
         lambda: map_layer.main(["--game-version", version])),
        ("catalog 游戏层区块", lambda: catalog.main([])),
        ("质量门", lambda: quality_gate.main([])),
    ]
    for name, fn in steps:
        print(f"===== {name} =====", flush=True)
        rc = fn()
        if rc != 0:
            print(f"===== {name} 失败（退出码 {rc}），中止 =====")
            return rc
    print("===== 游戏层刷新完成 =====")
    return 0


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):       # Windows 控制台中文安全输出
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="CK3 wiki 知识库管线入口")
    ap.add_argument("--page", default="Scripting",
                    help="页面标题（默认 Scripting 样本页）")
    ap.add_argument("--stage", default="all",
                    choices=STAGES + ("all", "game"),
                    help="执行到哪个阶段/只跑哪个阶段；game=原版游戏层三通道")
    ap.add_argument("--force", action="store_true",
                    help="传给 crawl：忽略已抓记录强制重抓")
    ap.add_argument("--auto", action="store_true",
                    help="--stage game 专用：先无头驱动游戏 exe 导出两条 dump 命令"
                         "（需 Steam 版游戏安装与 Steam 客户端在运行；"
                         "见 scripts/headless_dump.py）")
    args = ap.parse_args(argv)

    if args.stage == "game":
        if args.auto:
            from headless_dump import run_dump as headless_run  # 延迟导入
            print("===== 无头导出 dump（--auto）=====", flush=True)
            rc = headless_run(None)
            if rc != 0:
                print(f"===== 无头导出失败（退出码 {rc}），中止 =====")
                return rc
        return refresh_game_layers()
    if args.auto:
        print("[run] --auto 仅与 --stage game 组合使用")
        return 2
    plan = STAGES if args.stage == "all" else (args.stage,)
    rc = 0
    for stage in plan:
        print(f"===== 阶段：{stage} =====", flush=True)
        if stage == "crawl":
            rc = crawl.main(["--page", args.page] +
                            (["--force"] if args.force else []))
        elif stage == "clean":
            rc = clean.main(["--page", args.page])
        elif stage == "organize":
            rc = organize.main([])
        elif stage == "catalog":
            rc = catalog.main(["--page", args.page])
        elif stage == "gate":
            rc = quality_gate.main(["--page", args.page])
        if rc != 0:
            print(f"===== 阶段 {stage} 失败（退出码 {rc}），中止 =====")
            return rc
    print("===== 全部阶段完成 =====")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
