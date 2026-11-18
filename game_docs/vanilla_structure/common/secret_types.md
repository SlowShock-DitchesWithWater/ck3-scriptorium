# common/secret_types 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.21.0；快照日期与指纹见 manifest.json）
- 文件数：5（其中 Jomini 解析 4 个）
- 顶层块条目总数：22，跨文件唯一条目 22
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_bastard_secrets.txt` | 10194 | 2 | 0 | jomini |
| `00_secret_types.txt` | 18173 | 16 | 0 | jomini |
| `_secret_types.info` | 1511 | - | - | 纯文档（非 Jomini） |
| `dynastic_cycle_secrets.txt` | 5375 | 3 | 0 | jomini |
| `gdp_merchant_secrets.txt` | 1683 | 1 | 0 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_bastard_secrets.txt（2 条目）

- secret_disputed_heritage
- secret_unmarried_illegitimate_child

### 00_secret_types.txt（16 条目）

- secret_deviant
- secret_homosexual
- secret_murder_attempt
- secret_cannibal
- secret_lover
- secret_murder
- secret_non_believer
- secret_incest
- secret_witch
- secret_crypto_religionist
- secret_embezzler
- secret_coup_plotter
- secret_raid_estate
- secret_forbidden_personal_tenet
- secret_dealbreaker
- secret_spy

### dynastic_cycle_secrets.txt（3 条目）

- secret_siphoned_treasury
- secret_request_incursion
- secret_exam_cheater

### gdp_merchant_secrets.txt（1 条目）

- secret_disguised_usury

### 未解析文件

- `_secret_types.info` — 纯文档（非 Jomini）
