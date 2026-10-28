# -*- coding: utf-8 -*-
r"""工单06：catalog.py 人工字段保护 + 机械字段刷新 + 快照语义的夹具测试。

夹基（fixture）就是仓库当前的真实 catalog.md（已含 56 页人工草稿与游戏层
条目）——先备份字节，测试中允许篡改/重跑，结束时逐字节还原，仓库不留痕。

运行（仓库根）：
    python tests\test_catalog_protection.py
退出码 0 = 全部通过；任一 FAIL 打印原因并退出 1。

零网络：catalog.py 只读 manifest.json 与 pages/（import 链上无
requests/selenium/lib.session）。
"""
import contextlib
import io
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from lib import config, manifest  # noqa: E402
import catalog  # noqa: E402

CATALOG = config.CATALOG_PATH
PLACEHOLDER = catalog.PLACEHOLDER

_passed = 0
_failed = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global _passed, _failed
    print(f"{'PASS' if ok else 'FAIL'}  {label}" + (f"  —— {detail}" if not ok and detail else ""))
    if ok:
        _passed += 1
    else:
        _failed += 1


def entry_block(text: str, marker_title: str) -> str | None:
    begin = f"<!-- ck3wiki-mod-kb:entry BEGIN {marker_title} -->"
    end = f"<!-- ck3wiki-mod-kb:entry END {marker_title} -->"
    if begin not in text or end not in text:
        return None
    pat = re.compile(re.escape(begin) + r".*?" + re.escape(end), re.DOTALL)
    return pat.search(text).group(0)


def field(block: str, name: str) -> str | None:
    m = re.search(rf"^- \*\*{name}\*\*：(.*)$", block, re.MULTILINE)
    return m.group(1).strip() if m else None


def run_catalog(args: list[str] | None = None) -> None:
    with contextlib.redirect_stdout(io.StringIO()):
        rc = catalog.main(args)
    assert rc == 0, f"catalog.main({args}) 退出码 {rc}"


def human_fields(text: str, titles: list[str]) -> dict[str, tuple[str, str]]:
    out = {}
    for t in titles:
        b = entry_block(text, t)
        if b:
            out[t] = (field(b, "何时查") or "", field(b, "中文摘要") or "")
    return out


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    original = CATALOG.read_bytes()          # 夹具字节备份（finally 还原）
    data = manifest.read_manifest()
    wiki_titles = list(data["pages"])
    gd = data.get("game_docs") or {}
    game_ids = [f"game:{n}" for n in (gd.get("script_docs") or {})]
    game_ids += ["game:INDEX.md", "game:entry_map.tsv"]

    try:
        text = CATALOG.read_text(encoding="utf-8")

        # --- 前置：夹具完整性（草稿已填、占位符清零、游戏层条目齐全） ---
        drafted = human_fields(text, wiki_titles)
        check("夹具：56 页条目全部存在且人工字段已填（非占位符）",
              len(drafted) == len(wiki_titles)
              and all(w != PLACEHOLDER and s != PLACEHOLDER
                      for w, s in drafted.values()),
              f"{len(drafted)}/{len(wiki_titles)} 页有草稿")
        check("夹具：游戏层条目齐全（12 script_docs + INDEX + entry_map）",
              all(entry_block(text, g) for g in game_ids),
              f"缺：{[g for g in game_ids if not entry_block(text, g)]}")

        # --- 1. 保护 + 幂等：全量重生成后逐字节不变（人工+机械都不动） ---
        before_human = human_fields(text, wiki_titles + game_ids)
        run_catalog()
        text2 = CATALOG.read_text(encoding="utf-8")
        check("重跑 catalog.py：整文件逐字节不变（幂等）",
              text2 == text)
        after_human = human_fields(text2, wiki_titles + game_ids)
        check("重跑 catalog.py：全部人工字段（何时查/中文摘要）逐字不变",
              before_human == after_human)

        # --- 2. 机械字段刷新语义：篡改派生字段 → 重跑恢复为 manifest 派生值 ---
        run_catalog()  # 确保从稳态出发
        text = CATALOG.read_text(encoding="utf-8")
        # 快照行由 manifest 派生（取各页 fetched_at 最大值），日期随抓取轮次
        # 变化（2026-10-23 补抓后即变）——必须动态提取，不能硬编码日期
        snap_line = re.search(r"^> 快照：抓取 .*$", text, re.MULTILINE).group(0)
        tampered = text.replace("oldid 20200，抓取 2026-10-22", "oldid 99999，抓取 2000-01-01", 1)
        tampered = tampered.replace("2128 条", "0 条", 1)              # 游戏层条目数
        tampered = tampered.replace(snap_line, "> 快照：抓取 1999-99-99", 1)
        # 同条目人工字段注入标记物：重跑后必须原样保留
        keep_block = entry_block(tampered, "Effects")
        assert keep_block, "Effects 条目缺失"
        marker_human = "标记物-人工字段必须存活-ZZ"
        tampered = tampered.replace(
            "- **何时查**：写事件/决策的执行动作",
            f"- **何时查**：{marker_human}写事件/决策的执行动作", 1)
        CATALOG.write_text(tampered, encoding="utf-8", newline="\n")
        run_catalog()
        text3 = CATALOG.read_text(encoding="utf-8")
        check("机械字段刷新：篡改的 oldid/抓取日期恢复为 manifest 值",
              "oldid 20200，抓取 2026-10-22" in text3
              and "99999" not in entry_block(text3, "Effects"))
        check("机械字段刷新：游戏层条目数恢复（2128 条）", "2128 条" in entry_block(text3, "game:effects.md"))
        check("机械字段刷新：快照日期恢复（且整块与 manifest 派生一致）",
              catalog.SNAP_BEGIN in text3
              and "1999-99-99" not in text3
              and catalog.build_snapshot(manifest.read_manifest())
              in text3)
        eff3 = entry_block(text3, "Effects")
        check("人工字段保护：篡改机械字段时，人工字段改动逐字保留",
              marker_human in (field(eff3, "何时查") or ""))
        # 还原标记物：把人工字段改回正式草稿（下一轮重跑会保护"非占位符"值，
        # 所以直接重写为原始字节更干净）
        CATALOG.write_bytes(original)
        run_catalog()
        check("还原原始字节后重跑 == 稳态（闭环）",
              CATALOG.read_text(encoding="utf-8") == text2)

        # --- 3. 头部永不动：快照块之前的文本跨重跑逐字节一致 ---
        header_of = lambda s: s.split(catalog.SNAP_BEGIN)[0]  # noqa: E731
        check("文件头（快照块之前）重跑后逐字节不变",
              header_of(CATALOG.read_text(encoding="utf-8")) == header_of(text2))

        # --- 4. 覆盖：manifest 全部页 + 游戏层全部产物有条目标记 ---
        text4 = CATALOG.read_text(encoding="utf-8")
        missing = [t for t in wiki_titles
                   if f"ck3wiki-mod-kb:entry BEGIN {t}" not in text4]
        check("覆盖：manifest 全部 wiki 页有 catalog 条目（quality_gate A7 同口径）",
              not missing, f"缺：{missing}")
        miss_g = [g for g in game_ids if not entry_block(text4, g)]
        check("覆盖：游戏层 14 条目齐全（12 dump 产物 + INDEX + entry_map）",
              not miss_g, f"缺：{miss_g}")
        no_auth = [g for g in game_ids
                   if "与 wiki 冲突时以本条目为准" not in (entry_block(text4, g) or "")]
        check("游戏层条目全部明示权威顺序标注", not no_auth, f"缺标注：{no_auth}")

        # --- 5. 关键词：EXTRA_KEYWORDS 补充词出现在对应条目关键词行 ---
        bad_kw = []
        for title, extras in catalog.EXTRA_KEYWORDS.items():
            b = entry_block(text4, title)
            if not b:
                continue
            kws = (field(b, "英文关键词") or "")
            if any(re.search(rf"(^|；){re.escape(e)}(；|$)", kws) is None for e in extras[:2]):
                bad_kw.append(title)
        check("英文关键词行含 EXTRA_KEYWORDS 补充词（抽查前 2 个/页）",
              not bad_kw, f"异常页：{bad_kw}")

        # --- 6. 单页模式语义：不动快照与游戏层 ---
        tampered_snap = text4.replace(snap_line, "> 快照：抓取 1111-11-11", 1)
        CATALOG.write_text(tampered_snap, encoding="utf-8", newline="\n")
        run_catalog(["--page", "Scripting"])
        text5 = CATALOG.read_text(encoding="utf-8")
        check("单页模式：快照块不动（仍为篡改值，快照只由全量跑刷新）",
              "1111-11-11" in text5)
        check("单页模式：目标条目仍被重建（Scripting 条目存在）",
              entry_block(text5, "Scripting") is not None)
    finally:
        CATALOG.write_bytes(original)          # 夹具还原：仓库不留痕

    print(f"汇总：PASS {_passed} / FAIL {_failed}")
    return 0 if _failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
