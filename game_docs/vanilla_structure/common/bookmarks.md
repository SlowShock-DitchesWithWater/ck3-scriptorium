# common/bookmarks 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：6（其中 Jomini 解析 3 个）
- 顶层块条目总数：75，跨文件唯一条目 75
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `bookmarks/00_bookmarks.txt` | 96199 | 20 | 0 | jomini |
| `bookmarks/_bookmarks.info` | 4957 | - | - | 纯文档（非 Jomini） |
| `challenge_characters/00_challenge_characters.txt` | 32180 | 52 | 0 | jomini |
| `challenge_characters/_challenge_characters.info` | 350 | - | - | 纯文档（非 Jomini） |
| `groups/00_bookmark_groups.txt` | 167 | 3 | 0 | jomini |
| `groups/_bookmark_groups.info` | 353 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### bookmarks/00_bookmarks.txt（20 条目）

- bm_867_persia
- bm_867_iberia
- bm_867_northmen
- bm_867_adventurers
- bm_867_carolingians
- bm_867_christianity
- bm_867_mandalas
- bm_1066_hastings
- bm_1066_rags_to_riches
- bm_1066_iberia
- bm_1066_laamps
- bm_1178_call_of_the_empire
- bm_1178_swords_of_faith
- bm_1066_nomads
- bm_1178_nomads
- bm_867_china
- bm_1066_china
- bm_1178_china
- bm_1066_japan
- bm_1178_genpei

### challenge_characters/00_challenge_characters.txt（52 条目）

- challenge_character_renaud_kerak
- challenge_character_dawit_dembiya
- challenge_character_rhodri_gwynedd
- challenge_character_krutoj_nordmark
- challenge_character_badr_acre
- challenge_character_prithviraja_rajputana
- challenge_character_lambert_spoleto
- challenge_character_sargis_greater_armenia
- challenge_character_dyre_kiev
- challenge_character_eadgar_warwickshire
- challenge_character_ahmad_egypt
- challenge_character_alusian_vidin
- challenge_character_werner_aargau
- challenge_character_vicayalaya_chola_nadu
- challenge_character_piarres_albarracin
- challenge_character_john_ulster
- challenge_character_ishaq_baalbek
- challenge_character_heinrich_angria
- challenge_character_dumnarth_cornwall
- challenge_character_khusraw_malik_punjab
- challenge_character_herbert_vermandois
- challenge_character_aba_socotra
- challenge_character_werner_worms
- challenge_character_alfonsu_asturias
- challenge_character_amoghavarsha_karnata
- challenge_character_haraldr_vestfold
- challenge_character_muhammad_africa
- challenge_character_gregorios_napoli
- challenge_character_ashot_armenia
- challenge_character_gudrod_western_isles
- challenge_character_ali_taizz
- challenge_character_siemowit_wielkopolska
- challenge_character_pierre_piedmonte
- challenge_character_rogier_albi
- challenge_character_algimantas_lithuanians
- challenge_character_henri_champagne
- challenge_character_rostislav_tmutarakan
- challenge_character_raoul_valois
- challenge_character_ali_siracusa
- challenge_character_mohammed_azerbaijan
- challenge_character_richard_capua
- challenge_character_berenguer_barcelona
- challenge_character_anawrahta_pagan
- challenge_character_shisnand_coimbra
- challenge_character_erik_svealand
- challenge_character_nur_al_din_muhammed_nizari
- challenge_character_aella_northumberland
- challenge_character_richard_poitiers
- challenge_character_kulin_bosna
- challenge_character_gunda_orangallu
- challenge_character_maghan_sibi
- challenge_character_fariburz_shirvan

### groups/00_bookmark_groups.txt（3 条目）

- bm_group_867
- bm_group_1066
- bm_group_1178

### 未解析文件

- `bookmarks/_bookmarks.info` — 纯文档（非 Jomini）
- `challenge_characters/_challenge_characters.info` — 纯文档（非 Jomini）
- `groups/_bookmark_groups.info` — 纯文档（非 Jomini）
