# common/focuses 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：4（其中 Jomini 解析 3 个）
- 顶层块条目总数：28，跨文件唯一条目 28
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_education_focuses.txt` | 12235 | 5 | 0 | jomini |
| `00_lifestyle_focuses.txt` | 15544 | 23 | 0 | jomini |
| `00_test_focuses.txt` | 1289 | 0 | 0 | jomini |
| `_focuses.info` | 3824 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_education_focuses.txt（5 条目）

- education_diplomacy
- education_martial
- education_stewardship
- education_learning
- education_intrigue

### 00_lifestyle_focuses.txt（23 条目）

- diplomacy_foreign_affairs_focus
- diplomacy_majesty_focus
- diplomacy_family_focus
- diplomacy_adventurer_focus
- martial_strategy_focus
- martial_authority_focus
- martial_chivalry_focus
- martial_adventurer_focus
- intrigue_skulduggery_focus
- intrigue_temptation_focus
- intrigue_intimidation_focus
- intrigue_adventurer_focus
- stewardship_wealth_focus
- stewardship_domain_focus
- stewardship_duty_focus
- stewardship_adventurer_focus
- learning_medicine_focus
- learning_scholarship_focus
- learning_theology_focus
- learning_adventurer_focus
- wanderer_internal_affairs_focus
- wanderer_journey_focus
- wanderer_destination_focus

### 00_test_focuses.txt（0 条目）

（无顶层块）

### 未解析文件

- `_focuses.info` — 纯文档（非 Jomini）
