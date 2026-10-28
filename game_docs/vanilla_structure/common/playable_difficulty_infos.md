# common/playable_difficulty_infos 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：2（其中 Jomini 解析 1 个）
- 顶层块条目总数：14，跨文件唯一条目 14
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_playable_difficulty_infos.txt` | 1785 | 14 | 0 | jomini |
| `_playable_difficulty_infos.info` | 281 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_playable_difficulty_infos.txt（14 条目）

- pdi_at_war
- pdi_no_player_heir
- pdi_primary_heir_of_wrong_dynasty
- pdi_herder_to_nomad
- pdi_cannot_have_children
- pdi_female_under_male_dominated_doctrine
- pdi_male_under_female_dominated_doctrine
- pdi_liege_of_hostile_faith
- pdi_patrilinial_marriage_as_woman
- pdi_matrilinial_marriage_as_man
- pdi_is_in_debt
- pdi_has_poor_health
- pdi_in_regency
- pdi_admin_without_noble_title

### 未解析文件

- `_playable_difficulty_infos.info` — 纯文档（非 Jomini）
