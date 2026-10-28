# -*- coding: utf-8 -*-
"""阶段2：raw/ 的 api.php JSON → pages/ 下结构化 Markdown（重放式，不联网）。

用法：
    python scripts/clean.py --page Scripting
    python scripts/clean.py --all            # 清洗 manifest 里全部已抓页
    python scripts/clean.py --replay-golden  # 金样本回放（零网络，diff 可审）
    python scripts/clean.py --update-golden  # 规则改动有据后刷新金样本

幂等性：清洗是纯函数（raw JSON → Markdown），重复运行产出逐字节相同的文件，
直接覆盖写（无临时副产物）。清洗规则改进后重跑本阶段即可从 raw 重放，无需重爬。

金样本回放（spec 测试决策）：tests/fixtures/ 固定 1 小页（Scripting）+ 1 巨页
（Effects）的 raw JSON 副本与期望产物 golden/；改清洗规则后跑 --replay-golden
比对 unified diff，全程不触网、不依赖 manifest 状态（夹具元数据固定在
tests/fixtures/fixtures.json，保证 golden 逐字节稳定）。
"""
import argparse
import difflib
import hashlib
import json
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib import config, manifest  # noqa: E402
from lib.cleaner import clean_html  # noqa: E402

# 金样本夹具目录（raw JSON 副本 + fixtures.json 元数据 + golden/ 期望产物）
FIXTURES_DIR = config.REPO_ROOT / "tests" / "fixtures"
GOLDEN_DIR = FIXTURES_DIR / "golden"


def replay_golden(update: bool) -> int:
    """金样本回放：固定夹具离线清洗并与 golden 比对（零网络请求）。

    本函数只读 fixtures 与 lib.cleaner，不导入 session/requests/selenium
    （测试 test_cleaner_rules.py 有对应的 sys.modules 断言）。
    update=True（--update-golden）以当前规则刷新 golden 期望产物；
    默认模式遇到不一致打印 unified diff 并返回 1，golden 缺失视为失败。
    provenance 与 clean_page 同格式、取自 fixtures.json 固定值——golden 与
    未受规则影响的 pages/<页>.md 逐字节一致。
    """
    meta = json.loads((FIXTURES_DIR / "fixtures.json").read_text(encoding="utf-8"))
    rc = 0
    for fx in meta["fixtures"]:
        title = fx["title"]
        raw = json.loads((FIXTURES_DIR / f"{title}.json").read_text(encoding="utf-8"))
        provenance = (f"来源: {config.SITE_ORIGIN}/{title.replace(' ', '_')} "
                      f"oldid={fx['oldid']} 抓取于 {fx['fetched_at']}")
        md, _stats = clean_html(title, raw["parse"]["text"], provenance=provenance)
        golden_path = GOLDEN_DIR / f"{title}.md"
        if update:
            GOLDEN_DIR.mkdir(parents=True, exist_ok=True)
            golden_path.write_text(md, encoding="utf-8", newline="\n")
            print(f"[golden] 已更新 {golden_path.relative_to(config.REPO_ROOT)} "
                  f"({len(md.encode('utf-8'))}B)")
            continue
        if not golden_path.is_file():
            print(f"[golden] FAIL  {title}: golden 缺失，先跑 --update-golden 生成")
            rc = 1
            continue
        expect = golden_path.read_text(encoding="utf-8")
        if md == expect:
            print(f"[golden] PASS  {title} 与 golden 逐字节一致")
        else:
            rc = 1
            diff = difflib.unified_diff(
                expect.splitlines(keepends=True), md.splitlines(keepends=True),
                fromfile=f"golden/{title}.md", tofile=f"replay/{title}.md")
            print(f"[golden] FAIL  {title} 与 golden 不一致，diff 如下：")
            print("".join(diff), end="")
    print(f"[golden] 汇总：{'PASS' if rc == 0 else 'FAIL'}"
          f"（{len(meta['fixtures'])} 个夹具）")
    return rc


def clean_page(title: str) -> Path:
    """清洗单页：读 raw JSON → 清洗 → 写 pages/<页名>.md → manifest 补记。"""
    entry = manifest.read_manifest()["pages"].get(title)
    if not entry or not entry.get("raw_file"):
        raise SystemExit(f"[clean] manifest 中没有 {title} 的抓取记录，请先运行 crawl")
    raw_path = config.REPO_ROOT / entry["raw_file"]
    if not raw_path.is_file():
        raise SystemExit(f"[clean] raw 文件缺失：{raw_path}")

    raw = json.loads(raw_path.read_text(encoding="utf-8"))
    html = raw["parse"]["text"]
    provenance = (f"来源: {config.SITE_ORIGIN}/{title.replace(' ', '_')} "
                  f"oldid={entry.get('oldid')} 抓取于 {entry.get('fetched_at')}")
    md, stats = clean_html(title, html, provenance=provenance)

    out_path = config.PAGES_DIR / (config.safe_filename(title) + ".md")
    out_path.write_text(md, encoding="utf-8", newline="\n")
    print(f"[clean] {title}: html {stats.html_bytes}B -> md {stats.md_bytes}B "
          f"(H1={stats.h1} H2={stats.h2} H3={stats.h3} 表格={stats.tables} "
          f"代码块={stats.code_blocks} 剥[编辑]按钮={stats.pruned_editsections} "
          f"剥导航框={stats.pruned_navboxes}) -> {out_path}")

    # manifest 补记清洗产物信息（原子更新）。
    # 幂等设计：按产物内容哈希判断——内容未变时保留旧 cleaned_at 与统计，
    # 重复运行 manifest 逐字节稳定；内容变了（规则改进后重放）才刷新时间戳。
    content_sha = hashlib.sha256(md.encode("utf-8")).hexdigest()

    def _update(e: dict) -> dict:
        if e.get("cleaned_sha256") == content_sha and e.get("cleaned_file"):
            return e  # 产物未变，登记信息原样保留（幂等）
        e.update({
            "cleaned_file": f"pages/{out_path.name}",
            "cleaned_at": datetime.now().astimezone().isoformat(timespec="seconds"),
            "cleaned_bytes": stats.md_bytes,
            "cleaned_sha256": content_sha,
            "clean_stats": stats.as_dict(),
        })
        return e

    manifest.update_page(title, _update)
    return out_path


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):       # Windows 控制台中文安全输出
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="阶段2：raw JSON 清洗为 pages/ Markdown")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--page", help="页面标题（manifest 中的 title）")
    g.add_argument("--all", action="store_true", help="清洗全部已抓页")
    g.add_argument("--replay-golden", action="store_true",
                   help="金样本回放：固定夹具离线清洗并与 golden 比对（零网络）")
    g.add_argument("--update-golden", action="store_true",
                   help="以当前清洗规则刷新金样本期望产物")
    args = ap.parse_args(argv)

    if args.replay_golden:
        return replay_golden(update=False)
    if args.update_golden:
        return replay_golden(update=True)

    config.ensure_dirs()
    pages = list(manifest.read_manifest()["pages"])
    if args.all:
        targets = pages
    elif args.page:
        targets = [args.page]
    else:
        ap.error("需要 --page <标题> 或 --all")
    for t in targets:
        clean_page(t)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
