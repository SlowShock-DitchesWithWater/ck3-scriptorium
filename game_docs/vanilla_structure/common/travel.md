# common/travel 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：6（其中 Jomini 解析 4 个）
- 顶层块条目总数：49，跨文件唯一条目 49
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `point_of_interest_types/_travel_point_of_interest_types.info` | 996 | - | - | 纯文档（非 Jomini） |
| `point_of_interest_types/pam_saint_point_of_interest_types.txt` | 4344 | 1 | 0 | jomini |
| `point_of_interest_types/travel_point_of_interest_types.txt` | 48937 | 19 | 0 | jomini |
| `travel_options/_travel_options.info` | 2726 | - | - | 纯文档（非 Jomini） |
| `travel_options/travel_options.txt` | 40882 | 29 | 0 | jomini |
| `travel_options/travel_options_modifiers.txt` | 88 | 0 | 0 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### point_of_interest_types/pam_saint_point_of_interest_types.txt（1 条目）

- poi_buried_saint

### point_of_interest_types/travel_point_of_interest_types.txt（19 条目）

- poi_capitals
- poi_special_buildings_martial
- poi_special_buildings_learning
- poi_special_buildings_religious
- poi_standalone_holy_site
- poi_special_buildings_diplomatic
- poi_grand_city
- poi_special_buildings_wonder
- poi_special_buildings_economic
- poi_mausoleum_at_halicarnassus
- poi_lighthouse_of_alexandria
- poi_natural_feature
- poi_legend_capitals
- poi_battles
- poi_battles_historical
- poi_special_buildings_stress_relief
- poi_silk_road_node
- poi_mandala_capital
- poi_grand_cathedral

### travel_options/travel_options.txt（29 条目）

- adventurers_scout_for_talent_option
- adventurers_make_local_deals_option
- adventurers_search_for_secrets_option
- adventurers_encourage_relationships_option
- adventurers_gather_inspiration_option
- adventurers_proselytize_zealously_option
- adventurers_forward_scouts_option
- purchase_rough_terrain_gear_option
- purchase_desert_gear_option
- purchase_forest_gear_option
- experienced_captains_option
- hire_experienced_mercenaries_option
- hire_jungle_expert_option
- hire_mountaineer_option
- hire_forder_option
- hire_desert_warrior_option
- hire_rough_terrain_expert_option
- court_physician_option
- cultural_ambassador_option
- hire_allied_mercenaries_option
- appeasement_option
- leisurely_option
- tutor_child_option
- fancy_mounts_option
- military_recruits_option
- superior_armaments_option
- anxious_option
- circumspect_option
- estate_mounts_option

### travel_options/travel_options_modifiers.txt（0 条目）

（无顶层块）

### 未解析文件

- `point_of_interest_types/_travel_point_of_interest_types.info` — 纯文档（非 Jomini）
- `travel_options/_travel_options.info` — 纯文档（非 Jomini）
