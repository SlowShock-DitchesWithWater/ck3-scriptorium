# common/scripted_relations 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：2（其中 Jomini 解析 1 个）
- 顶层块条目总数：38，跨文件唯一条目 38
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_scripted_relations.txt` | 4626 | 38 | 0 | jomini |
| `_scripted_relations.info` | 3877 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_scripted_relations.txt（38 条目）

- friend
- best_friend
- grudge
- rival
- nemesis
- mentor
- student
- lover
- soulmate
- guardian
- ward
- bully
- victim
- crush
- oaf
- soldier_friend
- intrigue_mentor
- intrigue_student
- potential_friend
- potential_rival
- potential_lover
- court_physician
- antiquarian
- wedding_very_bad_fertility
- wedding_bad_fertility
- wedding_good_fertility
- wedding_very_good_fertility
- potential_hook
- activity_recurrer
- event_recurrer
- wet_nurse
- nursed_child
- favorite_child
- old_flame
- blood_brother
- disciple
- fellow_disciple
- elder

### 未解析文件

- `_scripted_relations.info` — 纯文档（非 Jomini）
