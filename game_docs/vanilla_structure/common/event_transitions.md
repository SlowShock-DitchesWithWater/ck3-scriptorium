# common/event_transitions 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：4（其中 Jomini 解析 3 个）
- 顶层块条目总数：33，跨文件唯一条目 33
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `_event_transitions.info` | 1021 | - | - | 纯文档（非 Jomini） |
| `debug_test_transitions.txt` | 628 | 4 | 0 | jomini |
| `ep2_tournament_transitions.txt` | 3554 | 21 | 0 | jomini |
| `ep3_chariot_race_transitions.txt` | 1401 | 8 | 0 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### debug_test_transitions.txt（4 条目）

- debug_test_transition_0
- debug_test_transition_1
- debug_test_transition_2
- debug_test_transition_3

### ep2_tournament_transitions.txt（21 条目）

- pivotal_archery_fail
- pivotal_archery_neutral
- pivotal_archery_success
- pivotal_boardgame_fail
- pivotal_boardgame_neutral
- pivotal_boardgame_success
- pivotal_fistfighting_fail
- pivotal_fistfighting_neutral
- pivotal_fistfighting_success
- pivotal_horse_racing_fail
- pivotal_horse_racing_neutral
- pivotal_horse_racing_success
- pivotal_jousting_fail
- pivotal_jousting_neutral
- pivotal_jousting_success
- pivotal_melee_fail
- pivotal_melee_neutral
- pivotal_melee_success
- pivotal_recital_fail
- pivotal_recital_neutral
- pivotal_recital_success

### ep3_chariot_race_transitions.txt（8 条目）

- pivotal_chariots_fail_blue
- pivotal_chariots_fail_green
- pivotal_chariots_fail_red
- pivotal_chariots_fail_white
- pivotal_chariots_win_blue
- pivotal_chariots_win_green
- pivotal_chariots_win_red
- pivotal_chariots_win_white

### 未解析文件

- `_event_transitions.info` — 纯文档（非 Jomini）
