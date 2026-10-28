# 仓库许可总览（双层许可）

本仓库内容分两层声明许可，按目录边界适用：

| 范围 | 内容 | 许可 |
|---|---|---|
| `scripts/`、`tests/`、`skills/`（ck3-mod-standards）、`catalog.md`、`manifest.json`、`docs/`（pipeline.md、reports/）、根文档（README.md、README.zh-CN.md、AGENTS.md、本文件） | 原创代码与文档 | **MIT**（见 [LICENSE](LICENSE)，2026-10-23 用户选定） |
| `pages/`（含章节子目录） | CK3 Wiki 抓取清洗文本 | **CC BY-SA 3.0**，署名 CK3 Wiki —— 详见 [`pages/CONTENT-LICENSE.md`](pages/CONTENT-LICENSE.md) |
| `tests/fixtures/`（金样本 raw JSON 与 golden 期望产物） | CK3 Wiki api.php 响应的逐字副本及其清洗产物 | 同 pages/ 层：CC BY-SA 3.0，来源标注见 `tests/fixtures/fixtures.json` |

## 代码许可：MIT

`scripts/` 等原创部分采用 MIT 许可（[LICENSE](LICENSE)）。

## 明确不在发布范围（.gitignore 已排除）

- `game_docs/`、`game logs/`：游戏 script_docs dump 与原版结构索引——游戏
  衍生数据，现实的下架（DMCA）风险面，仅本地使用；clone 者按 README 手册 A
  自行从本地游戏生成等价物。
- `raw/`、`scripts/state/`：抓取原始存档与运行状态（含会话 cookie）。
- `_reference/`：第三方合集解包（无 LICENSE，保留所有权利），仅内部参考，
  未采用其任何文本内容（页面标题清单这一事实信息除外，见 docs/spec.md 决策）。
- `docs/spec.md`：项目规划文档，含本机环境附录，不入公开仓库。
