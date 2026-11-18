# common/title_types 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.21.0；快照日期与指纹见 manifest.json）
- 文件数：2（其中 Jomini 解析 1 个）
- 顶层块条目总数：11，跨文件唯一条目 11
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_title_types.txt` | 2599 | 11 | 0 | jomini |
| `_title_types.info` | 3804 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_title_types.txt（11 条目）

- title_type_default_static
- title_type_default_dynamic
- title_type_mercenary_company
- title_type_holy_order
- title_type_landless_adventurer
- title_type_nomad
- title_type_noble_family
- title_type_cardinal
- title_type_ecclesiastical
- title_type_merchant_family
- title_type_republic

### 未解析文件

- `_title_types.info` — 纯文档（非 Jomini）
