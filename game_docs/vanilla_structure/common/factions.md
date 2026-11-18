# common/factions 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.21.0；快照日期与指纹见 manifest.json）
- 文件数：9（其中 Jomini 解析 8 个）
- 顶层块条目总数：14，跨文件唯一条目 14
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_factions.txt` | 37580 | 3 | 0 | jomini |
| `00_nation_fracturing_faction.txt` | 11489 | 1 | 0 | jomini |
| `00_nomadic_faction.txt` | 13507 | 1 | 0 | jomini |
| `00_peasant_faction_new.txt` | 18919 | 1 | 1 | jomini |
| `00_populist_faction.txt` | 49520 | 2 | 0 | jomini |
| `00_republic_popular_faction.txt` | 3823 | 1 | 0 | jomini |
| `01_burgher_autonomy_faction.txt` | 14402 | 1 | 0 | jomini |
| `10_tgp_factions.txt` | 39429 | 4 | 0 | jomini |
| `_factions.info` | 11017 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_factions.txt（3 条目）

- independence_faction
- liberty_faction
- claimant_faction

### 00_nation_fracturing_faction.txt（1 条目）

- nation_fracturing_faction

### 00_nomadic_faction.txt（1 条目）

- nomadic_faction

### 00_peasant_faction_new.txt（1 条目）

- peasant_faction

### 00_populist_faction.txt（2 条目）

- populist_faction
- escalated_peasant_faction

### 00_republic_popular_faction.txt（1 条目）

- republic_popular_faction

### 01_burgher_autonomy_faction.txt（1 条目）

- burgher_autonomy_faction

### 10_tgp_factions.txt（4 条目）

- replace_ceremonial_regent_faction
- restore_ceremonial_liege_faction
- ceremonial_claimant_faction
- imperial_policy_faction

### 未解析文件

- `_factions.info` — 纯文档（非 Jomini）
