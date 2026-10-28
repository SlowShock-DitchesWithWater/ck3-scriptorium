# common/morpheme_strip_rules 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：3（其中 Jomini 解析 2 个）
- 顶层块条目总数：6，跨文件唯一条目 6
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_morpheme_strip_rules.info` | 2014 | - | - | 纯文档（非 Jomini） |
| `00_morpheme_strip_rules.txt` | 2017 | 3 | 0 | jomini |
| `99_morpheme_strip_russian.txt` | 2599 | 3 | 0 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_morpheme_strip_rules.txt（3 条目）

- english_rite_ism
- english_rite_i_suffix
- english_islamic_school_i

### 99_morpheme_strip_russian.txt（3 条目）

- russian_dyn_suffix
- russian_rite_i_suffix
- russian_rite_title_suffix

### 未解析文件

- `00_morpheme_strip_rules.info` — 纯文档（非 Jomini）
