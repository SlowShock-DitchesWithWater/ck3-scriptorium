# common/diarchies 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：6（其中 Jomini 解析 4 个）
- 顶层块条目总数：17，跨文件唯一条目 17
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `diarchy_mandates/00_mandates.txt` | 11469 | 9 | 0 | jomini |
| `diarchy_mandates/_mandates.info` | 429 | - | - | 纯文档（非 Jomini） |
| `diarchy_types/00_co_rulerships.txt` | 9678 | 3 | 0 | jomini |
| `diarchy_types/00_primeministerships.txt` | 16042 | 2 | 0 | jomini |
| `diarchy_types/00_regencies.txt` | 9269 | 3 | 0 | jomini |
| `diarchy_types/_diarchies.info` | 2458 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### diarchy_mandates/00_mandates.txt（9 条目）

- fill_coffers
- swell_armies
- promote_authority
- ranching
- horde_mustering
- promote_obedience
- promote_merit
- promote_might
- placate_movements

### diarchy_types/00_co_rulerships.txt（3 条目）

- junior_emperorship
- co_emperorship
- co_monarchy

### diarchy_types/00_primeministerships.txt（2 条目）

- vizierate
- grand_secretariat

### diarchy_types/00_regencies.txt（3 条目）

- temporary_regency
- regency
- nomad_regency

### 未解析文件

- `diarchy_mandates/_mandates.info` — 纯文档（非 Jomini）
- `diarchy_types/_diarchies.info` — 纯文档（非 Jomini）
