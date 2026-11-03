# 仓库许可总览（双层许可）

本仓库内容分两层声明许可，按目录边界适用：

| 范围 | 内容 | 许可 |
|---|---|---|
| `scripts/`、`map_room/`、`tests/`、`skills/`（ck3-mod-standards）、`catalog.md`、`manifest.json`、`docs/`（pipeline.md、reports/）、根文档（README.md、README.zh-CN.md、AGENTS.md、AGENTS.zh-CN.md、本文件） | 原创代码与文档 | **MIT**（见 [LICENSE](LICENSE)，2026-10-23 用户选定） |
| `pages/`（含章节子目录） | CK3 Wiki 抓取清洗文本 | **CC BY-SA 3.0**，署名 CK3 Wiki —— 详见 [`pages/CONTENT-LICENSE.md`](pages/CONTENT-LICENSE.md) |
| `game_docs/`（script_docs 12 清单 + vanilla_structure 结构索引 + map_docs 地图实测档案） | 游戏自生 debug dump 的转换产物 + 原版文件结构元数据 + 地图侧实测事实 | 见下方「游戏衍生数据」节 |
| `tests/fixtures/`（金样本 raw JSON 与 golden 期望产物） | CK3 Wiki api.php 响应的逐字副本及其清洗产物 | 同 pages/ 层：CC BY-SA 3.0，来源标注见 `tests/fixtures/fixtures.json` |
| `reading_room/`（阅览室自选文章） | 用户自写的外部文章笔记 + 出处链接（**不含原文全文**——许可红线见其 README） | 笔记正文随仓库 **MIT**（自写内容）；引用的短片段版权归原出处，条目内已标注 |

## 游戏衍生数据（game_docs/）

`game_docs/` 的内容派生自 Crusader Kings III 自身：script_docs 各清单为游戏
debug 输出（`script_docs` / `dump_data_types` 控制台命令）的忠实转换（仅版式，
无再创作）；vanilla_structure 为纯结构元数据（路径/条目名/计数，零游戏文件
正文）；map_docs 为地图安装文件的实测事实（尺寸/格式/统计/调色板色值，
由 `scripts/map_layer.py` 就地测量，除 heightmap.heightmap 全文 16 行这一
格式说明外零游戏内容复制）。**本仓库不对其主张任何权利，全部相关权利归
Paradox Interactive。** 2026-10-28 项目所有者权衡后决定随仓库发布以降低
使用门槛（此前为不发布 + 本地生成）。若权利方提出异议将立即下架。

## 代码许可：MIT

`scripts/` 等原创部分采用 MIT 许可（[LICENSE](LICENSE)）。

## 明确不在发布范围（.gitignore 已排除）

- `game logs/`：游戏的原始 dump 日志（含运行时会话日志）——体积与必要性
  考虑仅本地保留；按 README 手册 A 第 3-4 步可随时再生成 game_docs/。
- `raw/`、`scripts/state/`：抓取原始存档与运行状态（含会话 cookie）。
- `_reference/`：第三方合集解包（无 LICENSE，保留所有权利），仅内部参考，
  未采用其任何文本内容（页面标题清单这一事实信息除外，见 docs/spec.md 决策）。
- `docs/spec.md`：项目规划文档，含本机环境附录，不入公开仓库。
