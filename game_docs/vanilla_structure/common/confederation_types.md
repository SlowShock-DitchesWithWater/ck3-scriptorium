# common/confederation_types 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.21.0；快照日期与指纹见 manifest.json）
- 文件数：4（其中 Jomini 解析 3 个）
- 顶层块条目总数：9，跨文件唯一条目 9
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_confederation_types.txt` | 5781 | 2 | 0 | jomini |
| `10_house_bloc_types.txt` | 15799 | 6 | 0 | jomini |
| `10_trade_league.txt` | 6350 | 1 | 0 | jomini |
| `_confederation_types.info` | 8597 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_confederation_types.txt（2 条目）

- nomadic_confederation
- lombard_league

### 10_house_bloc_types.txt（6 条目）

- house_bloc_ceremony
- house_bloc_determination
- house_bloc_humility
- house_bloc_prosperity
- house_bloc_service
- house_bloc_strength

### 10_trade_league.txt（1 条目）

- trade_league

### 未解析文件

- `_confederation_types.info` — 纯文档（非 Jomini）
