# common/game_rules 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：3（其中 Jomini 解析 2 个）
- 顶层块条目总数：86，跨文件唯一条目 86
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_game_rules.txt` | 26474 | 85 | 0 | jomini |
| `01_empire_faith_gate_rules.txt` | 200 | 1 | 0 | jomini |
| `_game_rules.info` | 1545 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_game_rules.txt（85 条目）

- difficulty
- gender_equality
- end_date
- historical_characters
- random_harm
- random_harm_target
- conquerors_frequency
- conquerors_bonuses
- conquerors_inheritance
- black_death_occurrence
- black_death_frequency
- other_epidemic_frequency
- minor_disease_frequency
- elderly_health
- same_sex_relations
- same_sex_marriage
- sexuality_distribution
- adoption
- matrilineal_marriages
- exclave_independence
- multiplayer_murder_schemes
- legend_spread_chance
- legend_cost
- historical_legends
- name_of_byzantium
- realm_stability
- hybrid_culture_ai_frequency
- hybrid_culture_ai_restrictions
- divergent_culture_ai_frequency
- hybrid_and_divergence_cooldowns
- branched_rite_frequency
- branched_rite_amount
- heresy_outbreak_frequency
- regional_heresy
- mongol_invasion
- random_nickname_frequency
- casus_belli_costs
- culture_conversion_speed
- faith_conversion_speed
- diplomatic_range
- de_jure_requirement
- empire_obscurity_requirement
- custom_duchies
- custom_kingdoms
- generate_families
- faith_acceptance
- randomized_faiths
- random_ruler_placement
- ai_embarkation_cost
- domain_limit_tweaks
- hungarian_migration
- dlc_fp1_scandinavian_adventurers
- dissolution_umayyad
- dlc_fp3_seljuk_invasion
- situation_the_great_steppe
- struggle_iberia
- struggle_persia
- historicity_ruler_of_munster
- historicity_norman_conquest
- northeast_asia_nomad_region
- tibet_nomad_region
- sami_nomad_region
- arabia_nomad_region
- sahel_nomad_region
- horn_of_africa_nomad_region
- historicity_extra_admin_egypt
- historicity_extra_admin_arabia
- historicity_extra_admin_ghana
- historicity_extra_admin_kabulistan
- historicity_extra_admin_persia
- historicity_extra_admin_maghreb
- historicity_extra_admin_tamilakam
- historicity_extra_admin_carolingians
- historicity_extra_admin_player_wherever
- title_creation_imperial_power_projection
- title_creation_imperial_power_projection_targeting
- historicity_frankokratia
- ai_laamp_numbers
- advantage_damage_effect
- easteregg_characters
- coronation_laws
- silk_road_starting_innovations
- natural_disaster_earthquakes
- natural_disaster_floods
- unrestricted_dynasty_legacies

### 01_empire_faith_gate_rules.txt（1 条目）

- empire_faith_gate

### 未解析文件

- `_game_rules.info` — 纯文档（非 Jomini）
