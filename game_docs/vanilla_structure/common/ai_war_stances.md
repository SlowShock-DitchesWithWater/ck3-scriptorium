# common/ai_war_stances 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：4（其中 Jomini 解析 3 个）
- 顶层块条目总数：7，跨文件唯一条目 7
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_ai_attacker_stances.txt` | 3567 | 0 | 0 | jomini |
| `00_ai_defender_stances.txt` | 4001 | 0 | 0 | jomini |
| `00_ai_war_stances.txt` | 3303 | 7 | 0 | jomini |
| `_ai_war_stances.info` | 5680 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_ai_attacker_stances.txt（0 条目）

（无顶层块）

### 00_ai_defender_stances.txt（0 条目）

（无顶层块）

### 00_ai_war_stances.txt（7 条目）

- attacker_offensive
- attacker_defensive
- defender_offensive
- defender_defensive
- defender_desperate
- great_holy_war_attacker
- great_holy_war_defender

### 未解析文件

- `_ai_war_stances.info` — 纯文档（非 Jomini）
