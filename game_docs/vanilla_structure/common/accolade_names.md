# common/accolade_names 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：2（其中 Jomini 解析 1 个）
- 顶层块条目总数：16，跨文件唯一条目 16
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_accolade_names.txt` | 116523 | 16 | 0 | jomini |
| `_accolade_name.info` | 1501 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_accolade_names.txt（16 条目）

- accolade_the_knight_of_the_animal
- accolade_the_animal_of_capital
- accolade_the_knight_of_the_flower
- accolade_leader_of_the_culture_maa
- accolade_leader_of_the_lieges_maa
- accolade_leader_of_the_culture_unit
- accolade_leader_of_the_lieges_unit
- accolade_knight_of_god
- accolade_bearer_of_the_lieges_item
- accolade_first_of_the_field
- accolade_the_warrior_in_the_terrain
- accolade_the_defender_of_lieges_title
- accolade_the_foe_of_enemy_faith
- accolade_the_knight_of_aspect
- accolade_goodest_of_knights
- accolade_the_material_knight

### 未解析文件

- `_accolade_name.info` — 纯文档（非 Jomini）
