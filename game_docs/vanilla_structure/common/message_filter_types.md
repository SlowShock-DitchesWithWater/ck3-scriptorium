# common/message_filter_types 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：3（其中 Jomini 解析 2 个）
- 顶层块条目总数：195，跨文件唯一条目 195
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_message_filter_types.txt` | 14352 | 194 | 0 | jomini |
| `_message_filter_types.info` | 900 | - | - | 纯文档（非 Jomini） |
| `passive_rite_learning_message_filter_types.txt` | 151 | 1 | 0 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_message_filter_types.txt（194 条目）

- heir_change
- character_level_change
- character_lifestyle
- character_nickname
- character_stress
- secondary_character_stress
- character_health
- character_trait
- relationship_gained
- hook_on_me
- hook_on_other
- marriage_started
- marriage_ended
- legitimacy_change
- child_born
- grandchild_born
- child_language
- known_pregnancy
- family_became_concubine
- family_marriage_started
- marriage_ended_heir
- realm_priest_endorsement
- council_task
- councillor_ongoing
- councillor
- councillor_liege
- dynasty_prestige
- dynasty_perk
- dynasty_head_change
- dynasty_cadet_created
- dynasty_child_of_age
- child_of_age
- house_head_change
- house_feud_status
- courtier_arrived
- courtier_arrived_notable
- courtier_leaving
- courtier_child_of_age
- court_position
- court_position_held
- scheme_agent
- scheme_ended
- scheme_progress
- scheme_completion
- scheme_opportunity_threshold
- countermeasure_change
- secret_discovered
- secret_exposed
- interaction_consequence
- ransom_result
- death_family
- death_councillor
- death_prisoner
- death_relation
- death_notable
- title_gained
- title_lost
- title_primary_changed
- title_rank_changed
- clergy_title_transfer
- independence_gained
- vassal_contract_changed
- liege_changed
- government_changed
- law_changed
- law_liege
- faction
- faction_liege
- liege_ceded_title
- alliance_formed
- alliance_broken
- confederation
- war_participation
- war_participation_ally
- war_participation_enemy
- war_target
- war_ended
- war_ended_liege
- war_ended_neighbor
- war_declared_liege
- war_target_liege
- war_target_vassal
- war_target_tributary
- war_target_suzerain
- tributary_war
- war_troops_gained
- war_troops_dismissed
- war_enemy_troops
- combat_casualties
- combat_prisoners
- raid_completed
- raid_lost
- raid_intent_invalidated
- barter_completed
- barter_loot_delivered
- barter_aborted
- barter_loot_lost
- barter_loot_won
- siege_won
- siege_won_loot
- siege_started_enemy
- siege_won_enemy
- artifact_claim
- artifact_ownership
- building_started
- building_completed
- county_corruption
- culture_head
- culture_traditions
- culture_innovation
- culture_era
- culture_hybridized_nearby
- culture_conversion_notable
- faith_excommunication
- head_of_faith_changed
- holy_site_changed
- liege_converting_holding
- rite_updated
- holy_order_founded
- holy_order_destroyed
- holy_order_founded_enemy
- holy_order_patronage
- holy_order_hired
- court_amenity
- court_language
- court_grandeur
- courtier_court_trait
- court_inspiration
- struggle_catalyst
- struggle_phase
- house_unity_stage
- house_unity_change
- diarch
- accolade_activity
- accolade_rank
- accolade_succession
- accolade_eligibility
- accolade_squire_training
- accolade_knight_training
- accolade_mercenary
- tournament_arrival
- tournament_knight_arrives
- tournament_qualification
- tournament_qualification_champion
- tournament_qualification_knight
- legend_promoter
- legend_seed
- epidemic_outbreak
- epidemic_spread
- court_contracted_epidemic
- court_recover_epidemic
- appointment_candidacy
- candidate_title_gained
- candidate_title_lost
- governance_contracts
- governor_notification
- provincial_army_assignment
- admin_border_change
- admin_provincial_army_requests
- admin_new_powerful_family
- admin_new_noble_family
- laamp_contracts
- laamp_follower_event
- laamp_nearby
- domicile_moved
- migration_into_realm
- migration_into_neighbour
- tributaries_breaking_free
- yurt_yearly_benefits
- mpo_de_jure_shifting
- gok_gained_vassal
- great_steppe
- silk_road
- house_relation_changed
- mandala_aspect
- mandala_contract
- tributary
- natural_disaster_started
- natural_disaster_army_damaged
- great_project
- great_project_contribution
- appointed_to_title
- character_becomes_saint
- spiritual_fulfillment_changed
- clerical_region
- ecumenical_council_ruling
- great_schism_progress
- order_espousing_beliefs
- generic_interface_message_good
- generic_interface_message_bad
- generic_interface_message_neutral
- event_outcome
- multiplayer
- custom_message

### passive_rite_learning_message_filter_types.txt（1 条目）

- passive_religious_learning

### 未解析文件

- `_message_filter_types.info` — 纯文档（非 Jomini）
