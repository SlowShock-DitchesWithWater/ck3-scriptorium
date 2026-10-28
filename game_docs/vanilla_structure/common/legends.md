# common/legends 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：6（其中 Jomini 解析 3 个）
- 顶层块条目总数：74，跨文件唯一条目 73
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `chronicles/00_chronicles.txt` | 34411 | 33 | 0 | jomini |
| `chronicles/_chronicles.info` | 1951 | - | - | 纯文档（非 Jomini） |
| `legend_seeds/00_legend_seeds.txt` | 22980 | 38 | 0 | jomini |
| `legend_seeds/_legend_seeds.info` | 1453 | - | - | 纯文档（非 Jomini） |
| `legend_types/00_legends.txt` | 35668 | 3 | 0 | jomini |
| `legend_types/_legends.info` | 4572 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### chronicles/00_chronicles.txt（33 条目）

- debug_legend
- beast_slayer
- ancestral_glory
- ancestral_glory_not_in_history
- ancient_people
- saintly_deed
- holy_warrior
- saintly_location
- saintly_building
- saintly_life
- saintly_descent
- mythical_descent
- godly_descent
- war_won_chronicle
- new_title
- great_deed_dynasty
- great_deed_region
- great_deed_title
- great_deed_faith
- valiant_defense
- raised_by_animals
- sacred_birth
- divine_intervention
- fought_devil
- exotic_backstory
- tournament_won
- accolade_chronicle
- priesthood_restoration
- struggle_conclusion
- legendary_battle
- new_faith_legend
- swan_knight
- conqueror_chronicle

### legend_seeds/00_legend_seeds.txt（38 条目）

- king_arthur
- carolingian
- sons_of_david
- magi_descendant
- the_wheelwright
- vercingetorix
- saman_khudah
- bahram_gur
- cadell
- descendants_of_brahman
- gothic_kings
- sons_of_rurik
- holy_warrior
- holy_site
- el_cid
- alfred_of_wessex
- peasant_emperor
- william_gellones
- edward_the_martyr
- yazdagird_iii
- afrasiyab
- sceafa
- new_troy_london
- corineus
- scota
- pyusawhti
- menelik_i
- kings_of_semien
- roman_heritage
- hunnic_heritage
- premysl
- borjigin
- naga_descent
- hieros_gamos_skirnismal
- shibi_chakravarti
- the_red_hand
- ragnarr
- ce1_heroic_legacy_1

### legend_types/00_legends.txt（3 条目）

- heroic
- legitimizing
- holy

### 未解析文件

- `chronicles/_chronicles.info` — 纯文档（非 Jomini）
- `legend_seeds/_legend_seeds.info` — 纯文档（非 Jomini）
- `legend_types/_legends.info` — 纯文档（非 Jomini）
