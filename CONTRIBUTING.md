# Contributing / 参与贡献

English first, 中文在后。All code and docs live in one repo — clone it and you are ready.

## What this project accepts

- **Fixes and improvements to the pipeline** (`scripts/`), the **cleaning rules**
  (`scripts/lib/cleaner.py`), tests, and documentation.
- **Corrections to catalog summaries** (`catalog.md`): the `何时查` / `中文摘要`
  fields are human-maintained — edit them directly in `catalog.md`; the generator
  never overwrites them (protected by `tests/test_catalog_protection.py`).
- **Improvements to the standards skill** (`skills/ck3-mod-standards/`) — keep the
  English primary (`SKILL.md`) and Chinese copy (`SKILL.zh-CN.md`) in sync.

## What this project cannot accept

- **Re-crawled or updated wiki content as raw dumps** — snapshot refreshes are a
  maintainer operation (rate-limited crawl, ~30-40 min); open an issue instead.
- **Hand-edits to `game_docs/`** — the game layer is published, but it is
  machine-generated from the game's dump; refreshes go through the pipeline
  (README Manual A/B) by maintainers. Raw dump logs (`game logs/`) are never
  committed.
- Content copied from third-party modding skill collections (licensing).

## Before you open a PR

1. Install Python ≥3.10 with `beautifulsoup4` (`pip install beautifulsoup4`).
2. Run the offline test suites — all must pass (raw-dependent checks auto-skip
   if you have no `raw/`):

   ```bash
   python scripts/quality_gate.py
   python scripts/clean.py --replay-golden
   python tests/test_cleaner_rules.py
   python tests/test_catalog_protection.py
   python tests/spotcheck_tables.py
   ```

3. If you changed `lib/cleaner.py`, regenerate expectations and show the diff:
   `python scripts/clean.py --replay-golden` must FAIL first (showing your
   behavioral change), then `python scripts/clean.py --update-golden` refreshes
   the golden files — include them in the PR so the change is reviewable.
4. Keep `docs/pipeline.md` in sync with any behavior change (it is the contract).
5. Commit style: one logical change per commit, imperative subject line
   (e.g. `cleaner: expand rowspan cells into every spanned row`).

## 中文说明

- 接受：管线/清洗规则/测试/文档的修复与改进；`catalog.md` 的「何时查/中文摘要」
  人工字段可直接编辑（有保护机制，不会重跑丢失）；skill 双语版本需同步维护。
- 不接受：wiki 重抓内容（快照刷新是维护者操作，请开 issue）；对 `game_docs/`
  的手改（游戏层已发布，但由管线生成，刷新走 README 手册 A/B 由维护者执行；
  原始 dump 日志 `game logs/` 永不入库）；搬运第三方合集内容。
- PR 前跑通上面五个零网络测试套件；改了 `lib/cleaner.py` 的，先让金样本回放
  FAIL（展示行为变化）、再 `--update-golden` 刷新期望产物一并提交；行为变化需
  同步 `docs/pipeline.md`。
