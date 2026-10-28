# common/men_at_arms_types 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：11（其中 Jomini 解析 10 个）
- 顶层块条目总数：111，跨文件唯一条目 111
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_cultural_maa_types.txt` | 30511 | 37 | 16 | jomini |
| `00_fp3_maa_types.txt` | 5389 | 4 | 16 | jomini |
| `00_holy_order_maa_types.txt` | 3109 | 2 | 13 | jomini |
| `00_maa_types.txt` | 14441 | 14 | 15 | jomini |
| `00_regional_maa_types.txt` | 2900 | 2 | 15 | jomini |
| `01_accolade_maa_types.txt` | 12660 | 11 | 16 | jomini |
| `01_fp1_maa_types.txt` | 4301 | 4 | 16 | jomini |
| `07_ep3_maa_types.txt` | 10168 | 11 | 16 | jomini |
| `09_mpo_maa_types.txt` | 9670 | 9 | 16 | jomini |
| `10_tgp_maa_types.txt` | 16396 | 17 | 16 | jomini |
| `_men_at_arms_types.info` | 4897 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_cultural_maa_types.txt（37 条目）

- huscarl
- landsknecht
- longbowmen
- goedendag
- gendarme
- chasseur
- picchieri
- praetorian
- caballero
- monaspa
- cataphract
- hobelar
- schiltron
- metsanvartija
- horse_archers
- ayyar
- mubarizun
- mulaththamun
- archers_of_the_nile
- paiks
- druzhina
- hussar
- horn_warrior
- bush_hunter
- shomer
- garudas
- khandayat
- mountaineer
- sahel_horsemen
- guinea_warrior
- sarawit
- abudrar
- zbrojnosh
- palace_guards
- shenbigong
- guanch_vaulter
- teulu

### 00_fp3_maa_types.txt（4 条目）

- asawira
- tarkhan
- zupin_warrior
- tawashi

### 00_holy_order_maa_types.txt（2 条目）

- order_serjeants
- order_knights

### 00_maa_types.txt（14 条目）

- light_footmen
- bowmen
- light_horsemen
- pikemen_unit
- armored_footmen
- onager
- armored_horsemen
- mangonel
- crossbowmen
- trebuchet
- bombard
- handgunners
- house_guard
- pikemen_militia

### 00_regional_maa_types.txt（2 条目）

- camel_rider
- war_elephant

### 01_accolade_maa_types.txt（11 条目）

- accolade_maa_archers
- accolade_maa_skirmishers
- accolade_maa_pikes
- accolade_maa_outriders
- accolade_maa_vanguards
- accolade_maa_lancers
- accolade_maa_crossbowers
- accolade_maa_cameliers
- accolade_maa_elephantiers
- accolade_maa_horse_archers
- accolade_maa_handgunners

### 01_fp1_maa_types.txt（4 条目）

- vigmen
- bondi
- varangian_veterans
- jomsviking_pirates

### 07_ep3_maa_types.txt（11 条目）

- ayrudzi
- conrois
- akritai
- ballistrai
- skoutatoi
- varangian_guards
- handpicked_faithful
- maa_bandits
- maa_poachers
- maa_marauders
- maa_thieves

### 09_mpo_maa_types.txt（9 条目）

- nomadic_riders
- torch_bearers
- kheshig
- steppe_raiders
- heavy_horse_archers
- nomad_lancers
- mangudai
- cataphract_archers
- maturkan_warriors

### 10_tgp_maa_types.txt（17 条目）

- emishi_horse_archers
- japanese_horse_archers
- warrior_monks
- fire_lancers
- gakgung_archers
- ballista_elephant
- pesilat_warriors
- samurai
- zhanmadao_infantry
- black_armor_cavalry
- tiefutu
- burenjia
- rocket_carts
- ballista
- cloud_ladder
- siege_tower
- cannon

### 未解析文件

- `_men_at_arms_types.info` — 纯文档（非 Jomini）
