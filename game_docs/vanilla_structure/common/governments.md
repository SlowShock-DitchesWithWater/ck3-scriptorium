# common/governments 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：4（其中 Jomini 解析 3 个）
- 顶层块条目总数：20，跨文件唯一条目 20
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_government_types.txt` | 34740 | 16 | 0 | jomini |
| `01_japan_government_types.txt` | 4964 | 2 | 0 | jomini |
| `02_theocratic_government_types.txt` | 4396 | 2 | 0 | jomini |
| `_governments.info` | 30614 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_government_types.txt（16 条目）

- feudal_government
- republic_government
- clan_government
- tribal_government
- wanua_government
- mercenary_government
- holy_order_government
- monastic_holy_order_government
- administrative_government
- landless_adventurer_government
- nomad_government
- herder_government
- celestial_government
- mandala_government
- steppe_admin_government
- meritocratic_government

### 01_japan_government_types.txt（2 条目）

- japan_administrative_government
- japan_feudal_government

### 02_theocratic_government_types.txt（2 条目）

- theocracy_government
- ecclesiastical_government

### 未解析文件

- `_governments.info` — 纯文档（非 Jomini）
