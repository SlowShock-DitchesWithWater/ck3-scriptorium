# common/trade 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.21.0；快照日期与指纹见 manifest.json）
- 文件数：9（其中 Jomini 解析 5 个）
- 顶层块条目总数：126，跨文件唯一条目 91
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `county_potential_trade_goods/county_potential_trade_goods.info` | 501 | - | - | 纯文档（非 Jomini） |
| `county_potential_trade_goods/county_potential_trade_goods.txt` | 150041 | 35 | 0 | jomini |
| `trade_good_categories/00_trade_good_categories.txt` | 9016 | 21 | 0 | jomini |
| `trade_good_categories/01_need_type_trade_good_categories.txt` | 31043 | 20 | 0 | jomini |
| `trade_good_categories/_trade_good_categories.info` | 2801 | - | - | 纯文档（非 Jomini） |
| `trade_good_types/_trade_good_type.info` | 1938 | - | - | 纯文档（非 Jomini） |
| `trade_good_types/basic_trade_goods.txt` | 3672 | 44 | 0 | jomini |
| `trade_market_toll_levels/00_toll_levels.txt` | 969 | 6 | 0 | jomini |
| `trade_market_toll_levels/_toll_levels.info` | 1368 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### county_potential_trade_goods/county_potential_trade_goods.txt（35 条目）

- trade_good_alum
- trade_good_medicaments
- trade_good_horses
- trade_good_amber
- trade_good_honey
- trade_good_cattle
- trade_good_copper
- trade_good_cotton
- trade_good_dyes
- trade_good_fish
- trade_good_flax
- trade_good_fruit
- trade_good_furs
- trade_good_gems
- trade_good_gold
- trade_good_grain
- trade_good_hemp
- trade_good_incense
- trade_good_iron
- trade_good_ivory
- trade_good_jade
- trade_good_millet
- trade_good_oil
- trade_good_rice
- trade_good_salt
- trade_good_silk
- trade_good_silver
- trade_good_spices
- trade_good_stone
- trade_good_sugar
- trade_good_wine
- trade_good_wood
- trade_good_wool
- trade_good_tea
- trade_good_ceramics

### trade_good_categories/00_trade_good_categories.txt（21 条目）

- trade_category_mandala_arms
- trade_category_all
- trade_category_non_construction
- trade_category_non_food
- trade_category_non_medicinal
- trade_category_non_luxury
- trade_category_food
- trade_category_minerals
- trade_category_crops
- trade_category_luxury
- trade_category_agricultural_goods
- trade_category_forest_goods
- trade_category_rural_goods
- trade_category_fruit_hemp
- trade_category_guild_goods
- trade_category_cheap_common
- trade_category_fine_goods
- trade_category_staple_goods
- trade_category_farmed_goods
- trade_category_cultivated_luxuries
- trade_category_artisanal_goods

### trade_good_categories/01_need_type_trade_good_categories.txt（20 条目）

- trade_category_alcohol
- trade_category_comforts
- trade_category_cereals
- trade_category_meat
- trade_category_beasts_of_burden
- trade_category_salt
- trade_category_clothes
- trade_category_fabrics
- trade_category_dyes
- trade_category_alum
- trade_category_stone
- trade_category_carpentry_supplies
- trade_category_base_metals
- trade_category_luxury_items
- trade_category_jewelry_materials
- trade_category_precious_metals
- trade_category_medicaments
- trade_category_incense
- trade_category_luxury_consumption
- trade_category_books

### trade_good_types/basic_trade_goods.txt（44 条目）

- trade_good_grain
- trade_good_millet
- trade_good_rice
- trade_good_meat
- trade_good_fish
- trade_good_cheese
- trade_good_fruit
- trade_good_oil
- trade_good_honey
- trade_good_tea
- trade_good_horses
- trade_good_cattle
- trade_good_silver
- trade_good_gold
- trade_good_iron
- trade_good_copper
- trade_good_beer
- trade_good_wine
- trade_good_gems
- trade_good_amber
- trade_good_ivory
- trade_good_jade
- trade_good_wood
- trade_good_hemp
- trade_good_wool
- trade_good_cotton
- trade_good_flax
- trade_good_textiles
- trade_good_furs
- trade_good_leather
- trade_good_sugar
- trade_good_spices
- trade_good_ceramics
- trade_good_glass
- trade_good_jewelry
- trade_good_lacquerware
- trade_good_silk
- trade_good_incense
- trade_good_medicaments
- trade_good_stone
- trade_good_salt
- trade_good_alum
- trade_good_dyes
- trade_good_books_paper

### trade_market_toll_levels/00_toll_levels.txt（6 条目）

- toll_level_no_tolls
- toll_level_minimal_tolls
- toll_level_low_tolls
- toll_level_medium_tolls
- toll_level_high_tolls
- toll_level_very_high_tolls

### 未解析文件

- `county_potential_trade_goods/county_potential_trade_goods.info` — 纯文档（非 Jomini）
- `trade_good_categories/_trade_good_categories.info` — 纯文档（非 Jomini）
- `trade_good_types/_trade_good_type.info` — 纯文档（非 Jomini）
- `trade_market_toll_levels/_toll_levels.info` — 纯文档（非 Jomini）
