# -*- coding: utf-8 -*-
"""管线统一入口：一条命令跑通四阶段 + 质量门。

用法：
    python scripts/run.py --page Scripting            # 全流程（抓取→清洗→组织→建目录→质量门）
    python scripts/run.py --page Scripting --force    # 忽略已抓记录强制重抓
    python scripts/run.py --stage clean --page Scripting   # 只跑某一阶段
                                                      # 可选：crawl/clean/organize/catalog/gate/all
各阶段可独立重复运行且幂等（详见 docs/pipeline.md）。
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import catalog  # noqa: E402
import clean  # noqa: E402
import crawl  # noqa: E402
import organize  # noqa: E402
import quality_gate  # noqa: E402

# 阶段执行顺序（pipeline 契约：后一阶段只依赖前一阶段的磁盘产物）
STAGES = ("crawl", "clean", "organize", "catalog", "gate")


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):       # Windows 控制台中文安全输出
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="CK3 wiki 知识库管线入口")
    ap.add_argument("--page", default="Scripting",
                    help="页面标题（默认 Scripting 样本页）")
    ap.add_argument("--stage", default="all",
                    choices=STAGES + ("all",), help="执行到哪个阶段/只跑哪个阶段")
    ap.add_argument("--force", action="store_true",
                    help="传给 crawl：忽略已抓记录强制重抓")
    args = ap.parse_args(argv)

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
