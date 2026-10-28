# common/combat_phase_events 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：3（其中 Jomini 解析 2 个）
- 顶层块条目总数：13，跨文件唯一条目 13
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_commander_phase_events.txt` | 10101 | 4 | 0 | jomini |
| `00_knight_phase_events.txt` | 41733 | 9 | 0 | jomini |
| `_combat_phase_events.info` | 978 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_commander_phase_events.txt（4 条目）

- commander_none
- commander_wounded
- commander_maimed
- commander_killed

### 00_knight_phase_events.txt（9 条目）

- knight_none
- knight_berserker_attack
- knight_become_berserker
- knight_shieldmaiden_attack
- knight_becomes_incapable
- knight_wounded
- knight_maimed
- knight_killed
- knight_qualify_for_accolade

### 未解析文件

- `_combat_phase_events.info` — 纯文档（非 Jomini）
