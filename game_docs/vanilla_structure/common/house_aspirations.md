# common/house_aspirations 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：5（其中 Jomini 解析 4 个）
- 顶层块条目总数：29，跨文件唯一条目 29
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_admin_house_powers.txt` | 31720 | 13 | 4 | jomini |
| `10_tgp_celestial_house_powers.txt` | 15436 | 4 | 6 | jomini |
| `10_tgp_japan_house_aspirations.txt` | 16586 | 7 | 0 | jomini |
| `_house_aspiration.info` | 2634 | - | - | 纯文档（非 Jomini） |
| `tgp_mandala_devaraja_aspects.txt` | 24630 | 5 | 0 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_admin_house_powers.txt（13 条目）

- diplomatic_envoys
- staunch_stewards
- learned_philosophers
- tax_assessors
- army_commanders
- army_quartermasters
- tactical_besiegers
- political_meddlers
- confident_schemers
- charismatic_socialites
- respected_despots
- lofty_architects
- faithful_nobles

### 10_tgp_celestial_house_powers.txt（4 条目）

- celestial_traditional
- celestial_family
- celestial_governor
- celestial_warlord

### 10_tgp_japan_house_aspirations.txt（7 条目）

- no_aspiration
- ceremony
- determination
- humility
- prosperity
- service
- strength

### tgp_mandala_devaraja_aspects.txt（5 条目）

- no_aspect
- aspect_of_creation
- aspect_of_serenity
- aspect_of_destruction
- aspect_of_trickery

### 未解析文件

- `_house_aspiration.info` — 纯文档（非 Jomini）
