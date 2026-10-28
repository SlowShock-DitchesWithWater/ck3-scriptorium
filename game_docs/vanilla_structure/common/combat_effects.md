# common/combat_effects 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：2（其中 Jomini 解析 1 个）
- 顶层块条目总数：31，跨文件唯一条目 31
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_combat_effects.txt` | 2215 | 31 | 0 | jomini |
| `_combat_effects.info` | 470 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_combat_effects.txt（31 条目）

- defender_river
- defender_river_large
- defender_strait
- supply_state_supplied_advantage
- supply_state_running_low_advantage
- supply_state_starving_advantage
- recently_disembarked_advantage
- holding_defender_advantage
- combat_debt_level_0
- combat_debt_level_1
- combat_debt_level_2
- combat_debt_level_3
- combat_debt_level_4
- combat_debt_level_5
- combat_debt_level_6
- combat_debt_level_7
- combat_debt_level_8
- combat_debt_level_9
- treasury_combat_debt_level_0
- treasury_combat_debt_level_1
- treasury_combat_debt_level_2
- treasury_combat_debt_level_3
- treasury_combat_debt_level_4
- treasury_combat_debt_level_5
- treasury_combat_debt_level_6
- treasury_combat_debt_level_7
- treasury_combat_debt_level_8
- treasury_combat_debt_level_9
- combat_debt_level_no_income
- unreformed_faith_province
- gathering_army_advantage

### 未解析文件

- `_combat_effects.info` — 纯文档（非 Jomini）
