# common/council_positions 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：3（其中 Jomini 解析 2 个）
- 顶层块条目总数：15，跨文件唯一条目 15
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_council_positions.txt` | 88776 | 11 | 0 | jomini |
| `01_ministry_positions.txt` | 6106 | 4 | 0 | jomini |
| `_council_positions.info` | 5499 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_council_positions.txt（11 条目）

- councillor_chancellor
- councillor_steward
- councillor_marshal
- councillor_spymaster
- councillor_court_chaplain
- councillor_spouse
- councillor_vizier
- councillor_kurultai_1
- councillor_kurultai_2
- councillor_kurultai_3
- councillor_kurultai_4

### 01_ministry_positions.txt（4 条目）

- minister_personnel
- minister_justice
- minister_works
- minister_grand_marshal

### 未解析文件

- `_council_positions.info` — 纯文档（非 Jomini）
