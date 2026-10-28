# common/pool_character_selectors 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：7（其中 Jomini 解析 6 个）
- 顶层块条目总数：12，跨文件唯一条目 12
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_auto_characters.txt` | 2187 | 2 | 0 | jomini |
| `00_city.txt` | 1114 | 1 | 0 | jomini |
| `00_clergy.txt` | 2169 | 2 | 0 | jomini |
| `00_herders.txt` | 964 | 1 | 0 | jomini |
| `00_holy_order.txt` | 5980 | 5 | 0 | jomini |
| `00_mercenary.txt` | 841 | 1 | 0 | jomini |
| `_pool_character_selectors.info` | 2374 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_auto_characters.txt（2 条目）

- auto_generated_title_holder
- auto_generated_local_title_holder

### 00_city.txt（1 条目）

- pool_city_succession

### 00_clergy.txt（2 条目）

- pool_court_chaplain
- pool_theocratic_succession

### 00_herders.txt（1 条目）

- pool_herder_succession

### 00_holy_order.txt（5 条目）

- pool_holy_order_succession
- pool_cultural_holy_order_succession
- pool_monastic_holy_order_succession
- pool_female_monastic_holy_order_succession
- pool_male_monastic_holy_order_succession

### 00_mercenary.txt（1 条目）

- pool_mercenary_succession

### 未解析文件

- `_pool_character_selectors.info` — 纯文档（非 Jomini）
