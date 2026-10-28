# common/accolade_types 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：6（其中 Jomini 解析 5 个）
- 顶层块条目总数：31，跨文件唯一条目 31
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_accolade_categories.txt` | 1143 | 0 | 0 | jomini |
| `04_ep2_common_attributes.txt` | 39526 | 9 | 0 | jomini |
| `04_ep2_eminent_attributes.txt` | 15336 | 4 | 7 | jomini |
| `04_ep2_maa_attributes.txt` | 55171 | 12 | 150 | jomini |
| `04_ep2_skilled_attributes.txt` | 19466 | 6 | 26 | jomini |
| `_accolade_type.info` | 3542 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_accolade_categories.txt（0 条目）

（无顶层块）

### 04_ep2_common_attributes.txt（9 条目）

- marauder_attribute
- idealist_attribute
- charmer_attribute
- thug_attribute
- disciplinarian_attribute
- fanatic_attribute
- valiant_attribute
- stalwart_attribute
- scoundrel_attribute

### 04_ep2_eminent_attributes.txt（4 条目）

- huntsmaster_attribute
- blademaster_attribute
- master_of_revels_attribute
- house_knight_attribute

### 04_ep2_maa_attributes.txt（12 条目）

- archer_attribute
- skirmisher_attribute
- pike_attribute
- outrider_attribute
- vanguard_attribute
- lancer_attribute
- crossbowmen_attribute
- besieger_attribute
- camelry_attribute
- elephantry_attribute
- horse_archer_attribute
- gunpowder_attribute

### 04_ep2_skilled_attributes.txt（6 条目）

- politicker_attribute
- tactician_attribute
- reeve_attribute
- manipulator_attribute
- mentor_attribute
- contender_attribute

### 未解析文件

- `_accolade_type.info` — 纯文档（非 Jomini）
