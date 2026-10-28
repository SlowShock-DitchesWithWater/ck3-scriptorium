# common/tax_slots 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：4（其中 Jomini 解析 2 个）
- 顶层块条目总数：9，跨文件唯一条目 9
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `obligations/_tax_obligation.info` | 2056 | - | - | 纯文档（非 Jomini） |
| `obligations/clan_tax_collector.txt` | 5986 | 8 | 0 | jomini |
| `types/00_tax_slot_types.txt` | 1867 | 1 | 0 | jomini |
| `types/_tax_slot_type.info` | 3201 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### obligations/clan_tax_collector.txt（8 条目）

- default_tax_collector
- strict_taxation_tax_collector
- jizya_special_rights_tax_collector
- iqta_special_rights_tax_collector
- ghazi_special_rights_tax_collector
- deqhan_special_rights_tax_collector
- maguh_special_rights_tax_collector
- muqata_special_rights_tax_collector

### types/00_tax_slot_types.txt（1 条目）

- clan_tax_slot

### 未解析文件

- `obligations/_tax_obligation.info` — 纯文档（非 Jomini）
- `types/_tax_slot_type.info` — 纯文档（非 Jomini）
