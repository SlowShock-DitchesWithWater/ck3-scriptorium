# common/ethnicities 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：25（其中 Jomini 解析 25 个）
- 顶层块条目总数：51，跨文件唯一条目 51
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_ethnicities_debug.txt` | 1435 | 2 | 0 | jomini |
| `00_ethnicities_templates.txt` | 70903 | 2 | 24 | jomini |
| `00_ethnicities_vanity_characters.txt` | 14789 | 1 | 0 | jomini |
| `01_ethnicities_african.txt` | 34932 | 1 | 24 | jomini |
| `01_ethnicities_arab.txt` | 9161 | 1 | 24 | jomini |
| `01_ethnicities_asian.txt` | 47877 | 1 | 24 | jomini |
| `01_ethnicities_asian_ainu.txt` | 18731 | 1 | 24 | jomini |
| `01_ethnicities_asian_austronesian.txt` | 22066 | 1 | 24 | jomini |
| `01_ethnicities_asian_han_chinese.txt` | 14386 | 1 | 24 | jomini |
| `01_ethnicities_asian_japanese.txt` | 18773 | 1 | 24 | jomini |
| `01_ethnicities_asian_malay.txt` | 18526 | 1 | 24 | jomini |
| `01_ethnicities_asian_manchu_korean.txt` | 12528 | 1 | 24 | jomini |
| `01_ethnicities_asian_mongol.txt` | 9202 | 1 | 24 | jomini |
| `01_ethnicities_asian_tibetan.txt` | 4171 | 1 | 24 | jomini |
| `01_ethnicities_byzantine.txt` | 2327 | 1 | 24 | jomini |
| `01_ethnicities_caucasian.txt` | 19690 | 11 | 24 | jomini |
| `01_ethnicities_circumpolar.txt` | 24140 | 4 | 24 | jomini |
| `01_ethnicities_default_morphs.txt` | 12069 | 1 | 0 | jomini |
| `01_ethnicities_east_african.txt` | 31895 | 1 | 24 | jomini |
| `01_ethnicities_indian.txt` | 21453 | 2 | 24 | jomini |
| `01_ethnicities_mediterranean.txt` | 3478 | 3 | 24 | jomini |
| `01_ethnicities_papuan.txt` | 23775 | 1 | 24 | jomini |
| `01_ethnicities_slavic.txt` | 25444 | 9 | 24 | jomini |
| `01_ethnicities_turkic.txt` | 18613 | 1 | 24 | jomini |
| `01_ethnicities_west_turkic.txt` | 21425 | 1 | 24 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_ethnicities_debug.txt（2 条目）

- debug_clothes
- debug_hair

### 00_ethnicities_templates.txt（2 条目）

- ethnicity_template
- default_constraints_template

### 00_ethnicities_vanity_characters.txt（1 条目）

- vanity_character_base

### 01_ethnicities_african.txt（1 条目）

- african

### 01_ethnicities_arab.txt（1 条目）

- arab

### 01_ethnicities_asian.txt（1 条目）

- asian

### 01_ethnicities_asian_ainu.txt（1 条目）

- asian_emishi_ainu

### 01_ethnicities_asian_austronesian.txt（1 条目）

- asian_austronesian

### 01_ethnicities_asian_han_chinese.txt（1 条目）

- asian_han_chinese

### 01_ethnicities_asian_japanese.txt（1 条目）

- asian_japanese

### 01_ethnicities_asian_malay.txt（1 条目）

- asian_malay

### 01_ethnicities_asian_manchu_korean.txt（1 条目）

- asian_manchu_korean

### 01_ethnicities_asian_mongol.txt（1 条目）

- asian_mongol

### 01_ethnicities_asian_tibetan.txt（1 条目）

- asian_tibetan

### 01_ethnicities_byzantine.txt（1 条目）

- byzantine

### 01_ethnicities_caucasian.txt（11 条目）

- caucasian_base
- caucasian
- northern_ruler_designer
- caucasian_blond
- caucasian_northern_blond
- caucasian_ginger
- caucasian_northern_ginger
- caucasian_brown_hair
- caucasian_northern_brown_hair
- caucasian_dark_hair
- caucasian_northern_dark_hair

### 01_ethnicities_circumpolar.txt（4 条目）

- circumpolar
- circumpolar_brown_hair
- circumpolar_dark_hair
- circumpolar_blonde_hair

### 01_ethnicities_default_morphs.txt（1 条目）

- default_morphs

### 01_ethnicities_east_african.txt（1 条目）

- east_african

### 01_ethnicities_indian.txt（2 条目）

- indian
- south_indian

### 01_ethnicities_mediterranean.txt（3 条目）

- mediterranean
- mediterranean_ruler_designer
- mediterranean_byzantine

### 01_ethnicities_papuan.txt（1 条目）

- papuan

### 01_ethnicities_slavic.txt（9 条目）

- slavic
- slavic_blond
- slavic_northern_blond
- slavic_ginger
- slavic_northern_ginger
- slavic_brown_hair
- slavic_northern_brown_hair
- slavic_dark_hair
- slavic_northern_dark_hair

### 01_ethnicities_turkic.txt（1 条目）

- turkic

### 01_ethnicities_west_turkic.txt（1 条目）

- turkic_west
