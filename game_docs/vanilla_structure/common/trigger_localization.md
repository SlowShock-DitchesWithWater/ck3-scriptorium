# common/trigger_localization 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：54（其中 Jomini 解析 53 个）
- 顶层块条目总数：1706，跨文件唯一条目 1706
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_achievement_triggers.txt` | 8048 | 77 | 0 | jomini |
| `00_adultery_triggers.txt` | 404 | 3 | 0 | jomini |
| `00_artifact_triggers.txt` | 1688 | 5 | 0 | jomini |
| `00_building_requirement_triggers.txt` | 1789 | 15 | 0 | jomini |
| `00_building_triggers.txt` | 1307 | 12 | 0 | jomini |
| `00_character_relation_triggers.txt` | 4934 | 43 | 0 | jomini |
| `00_character_script_list_triggers.txt` | 1424 | 14 | 0 | jomini |
| `00_character_triggers.txt` | 57742 | 311 | 0 | jomini |
| `00_culture_triggers.txt` | 7037 | 62 | 0 | jomini |
| `00_custom_triggers.txt` | 4707 | 29 | 0 | jomini |
| `00_debug_triggers.txt` | 5728 | 83 | 0 | jomini |
| `00_dlc_triggers.txt` | 457 | 2 | 0 | jomini |
| `00_doctrine_triggers.txt` | 9399 | 51 | 0 | jomini |
| `00_dynasty_triggers.txt` | 1489 | 14 | 0 | jomini |
| `00_faction_triggers.txt` | 1946 | 16 | 0 | jomini |
| `00_ghw_triggers.txt` | 967 | 12 | 0 | jomini |
| `00_government_triggers.txt` | 1863 | 10 | 0 | jomini |
| `00_holy_order_triggers.txt` | 407 | 6 | 0 | jomini |
| `00_landed_title_triggers.txt` | 4763 | 38 | 0 | jomini |
| `00_law_triggers.txt` | 615 | 6 | 0 | jomini |
| `00_legend_triggers.txt` | 689 | 3 | 0 | jomini |
| `00_lifestyle_triggers.txt` | 958 | 10 | 0 | jomini |
| `00_logic_triggers.txt` | 864 | 5 | 0 | jomini |
| `00_province_script_list_triggers.txt` | 733 | 6 | 0 | jomini |
| `00_province_triggers.txt` | 1821 | 24 | 0 | jomini |
| `00_religion_triggers.txt` | 5508 | 34 | 0 | jomini |
| `00_scheme_script_list_triggers.txt` | 1830 | 23 | 0 | jomini |
| `00_scope_comparison_triggers.txt` | 6611 | 45 | 0 | jomini |
| `00_script_list_triggers.txt` | 2383 | 22 | 0 | jomini |
| `00_secret_script_list_triggers.txt` | 502 | 4 | 0 | jomini |
| `00_secret_triggers.txt` | 564 | 7 | 0 | jomini |
| `00_travel_triggers.txt` | 451 | 6 | 0 | jomini |
| `00_tutorial_triggers.txt` | 3567 | 39 | 0 | jomini |
| `00_unity_triggers.txt` | 342 | 1 | 0 | jomini |
| `00_war_triggers.txt` | 3454 | 33 | 0 | jomini |
| `01_character_interaction_triggers.txt` | 36200 | 326 | 0 | jomini |
| `01_decision_triggers.txt` | 7631 | 70 | 0 | jomini |
| `01_fp1_achievement_triggers.txt` | 1062 | 10 | 0 | jomini |
| `02_ep1_achievement_triggers.txt` | 2015 | 20 | 0 | jomini |
| `02_ep1_royal_court_triggers.txt` | 4254 | 19 | 0 | jomini |
| `03_fp2_struggle_triggers.txt` | 2969 | 15 | 0 | jomini |
| `04_ep2_diarchy_triggers.txt` | 2168 | 18 | 0 | jomini |
| `04_fp3_struggle_triggers.txt` | 549 | 4 | 0 | jomini |
| `05_ep2_achievement_triggers.txt` | 6925 | 60 | 0 | jomini |
| `06_bp2_hostage_triggers.txt` | 1524 | 10 | 0 | jomini |
| `07_ce1_achievement_triggers.txt` | 1165 | 11 | 0 | jomini |
| `08_ep3_admin_triggers.txt` | 435 | 3 | 0 | jomini |
| `08_ep3_laamp_triggers.txt` | 4423 | 32 | 0 | jomini |
| `09_mpo_achievement_triggers.txt` | 1119 | 10 | 0 | jomini |
| `09_mpo_triggers.txt` | 274 | 3 | 0 | jomini |
| `10_ce3_achievement_triggers.txt` | 1231 | 10 | 0 | jomini |
| `_trigger_localization.info` | 5558 | - | - | 纯文档（非 Jomini） |
| `ce1_legend_triggers.txt` | 440 | 2 | 0 | jomini |
| `tgp_triggers.txt` | 2043 | 12 | 0 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_achievement_triggers.txt（77 条目）

- until_death_do_us_part_achievement_trigger
- way_of_life_achievement_trigger
- a_legacy_to_last_the_ages_achievement_trigger
- a_house_of_my_own_achievement_trigger
- dreadful_ruler_achievement_trigger
- stressful_situation_achievement_trigger
- not_so_feudal_system_achievement_trigger
- the_succession_is_safe_achievement_trigger
- almost_there_achievement_trigger
- last_count_first_king_achievement_trigger
- prolific_achievement_trigger
- a_name_known_throughout_the_world_achievement_trigger
- end_of_an_era_achievement_trigger
- turning_to_diamonds_achievement_trigger
- reconquista_achievement_trigger
- seven_holy_cities_achievement_trigger
- frankokratia_achievement_trigger
- celebrity_achievement_trigger
- saint_achievement_trigger
- keeping_it_in_the_family_achievement_trigger
- non_nobis_domine_achievement_trigger
- trapped_in_the_web_achievement_trigger
- followed_by_shadows_achievement_trigger
- what_nepotism_achievement_trigger
- rise_from_the_ashes_achievement_trigger
- the_emerald_isle_achievement_trigger
- from_rags_to_riches_achievement_trigger
- give_a_dog_a_bone_achievement_trigger
- al_andalus_achievement_trigger
- wily_as_the_fox_achievement_trigger
- sibling_rivalry_achievement_trigger
- blood_eagle_achievement_trigger
- kings_to_the_seventh_generation_achievement_trigger
- norman_yoke_achievement_trigger
- royal_dignity_achievement_trigger
- going_places_achievement_trigger
- land_of_the_rus_achievement_trigger
- above_god_achievement_trigger
- paragon_of_virtue_achievement_trigger
- the_things_love_does_for_us_achievement_trigger
- fine_print_achievement_trigger
- know_your_place_achievement_trigger
- monumental_achievement_trigger
- its_not_a_cult_achievement_trigger
- the_things_we_do_for_love_achievement_trigger
- an_unfortunate_accident_achievement_trigger
- death_did_us_part_achievement_trigger
- for_the_faith_achievement_trigger
- bad_blood_achievement_trigger
- seductive_achievement_trigger
- the_emperors_new_clothes_achievement_trigger
- a_perfect_circle_achievement_trigger
- carolingian_consolidation_achievement_trigger
- moving_up_in_the_world_achievement_trigger
- beacon_of_progress_achievement_trigger
- mother_of_us_all_achievement_trigger
- fp2_historys_best_friends_trigger
- fp2_basque_in_my_glory_trigger
- fp2_friendship_is_magic_trigger
- fp2_high_stakes_chess_trigger
- fp2_iberia_or_iberia_trigger
- fp2_andalusian_inquisition_trigger
- fp2_iberian_hostilities_trigger
- fp2_iberian_conciliation_trigger
- fp2_iberian_compromise_trigger
- fp2_holiday_in_iberia_trigger
- fp2_el_cid_achievement_trigger
- fp3_rich_in_diversity_achievement_trigger
- fp3_darius_revenge_achievement_trigger
- fp3_mulct_them_dry_achievement_trigger
- fp3_the_umma_strikes_back_achievement_trigger
- fp3_royal_flush_achievement_trigger
- fp3_fiscal_res_achievement_trigger
- fp3_abassid_strong_achievement_trigger
- fp3_challenger_caliphate_achievement_trigger
- fp3_vassalize_the_caliph_achievement_trigger
- fp3_rekindle_iran_achievement_trigger

### 00_adultery_triggers.txt（3 条目）

- bastard_not_of_my_house_trigger
- house_head_would_not_approve_trigger
- mother_is_married_trigger

### 00_artifact_triggers.txt（5 条目）

- rarity_trigger_greater_or_equal
- rarity_trigger_greater_than
- rarity_trigger_less_or_equal
- rarity_trigger_less_than
- rarity_trigger_not_equal

### 00_building_requirement_triggers.txt（15 条目）

- building_requirement_tribal_holding_in_county
- building_requirement_nomad_holding_in_county
- building_requirement_herder_holding_in_county
- building_requirement_castle_city_church_failed
- building_requirement_castle_city_church_tribe_failed
- building_requirement_hall_of_heroes_failed
- buddhas_of_bamian_trigger
- holy_site_building_trigger
- holy_site_muslim_or_holy_site_trigger
- holy_site_christian_or_holy_site_trigger
- holy_site_muslim_christian_or_holy_site_trigger
- holy_site_muslim_or_zoroastrian_or_holy_site_trigger
- holy_site_jewish_or_holy_site_trigger
- holy_site_shinto_or_holy_site_trigger
- vastly_over_domain_limit_trigger

### 00_building_triggers.txt（12 条目）

- has_building
- has_building_or_higher
- has_ongoing_construction
- has_free_building_slot
- has_holding_type
- building_slots
- free_building_slots
- num_buildings
- has_special_building_slot
- has_special_building
- no_special_building_slot
- has_holding

### 00_character_relation_triggers.txt（43 条目）

- sex_opposite_of
- is_at_war_with
- is_allied_to
- is_allied_in_war
- target_is_same_character_or_above
- target_is_liege_or_above
- target_is_vassal_or_below
- is_tributary_of_suzerain_or_above
- is_attracted_to_women
- is_attracted_to_men
- has_sexuality
- is_attracted_to_gender_of
- can_be_parent_of
- has_relation_crush
- has_relation_bully
- num_of_relation_bully
- has_relation_victim
- num_of_relation_victim
- has_relation_lover
- num_of_relation_lover
- has_relation_soulmate
- num_of_relation_soulmate
- num_of_relation_crush
- has_relation_friend
- has_relation_best_friend
- has_relation_blood_brother
- num_of_relation_friend
- num_of_relation_best_friend
- has_relation_rival
- num_of_relation_rival
- has_relation_nemesis
- num_of_relation_nemesis
- has_relation_guardian
- num_of_relation_guardian
- has_relation_ward
- num_of_relation_ward
- has_relation_mentor
- has_relation_elder
- has_relation_disciple
- has_any_scripted_relation
- has_mother
- has_father
- has_any_artifact

### 00_character_script_list_triggers.txt（14 条目）

- any_living_character
- any_living_character_all
- any_pool_character
- any_pool_character_all
- any_vassal
- any_vassal_all
- any_vassal_or_below
- any_vassal_percent
- any_vassal_count
- any_in_de_jure_hierarchy_percent_greater_or_equal
- any_in_de_jure_hierarchy_all
- any_relation
- any_relation_all
- any_situation_sub_region_all

### 00_character_triggers.txt（311 条目）

- has_character_flag
- is_married
- is_betrothed
- is_adult
- is_landed
- is_landless_ruler
- is_playable_character
- is_landless_adventurer
- is_governor
- is_landless_administrative
- is_landed_or_landless_administrative
- is_landed_or_landless_administrative_or_theocratic
- is_lowborn
- is_ruler
- is_theocratic_lessee
- is_claimant
- has_claim_on
- has_strong_claim_on
- already_has_strong_claim_on
- allowed_more_spouses
- character_has_commander_trait_scope_does_not
- can_have_children
- has_trait_with_flag_can_murder_own_children
- has_trait_with_flag_can_not_marry
- has_councillor_for_skill
- is_house_head
- has_hook
- has_hook_from_secret
- is_hostile
- is_in_an_activity
- is_at_home
- has_activity_intent
- target_is_de_jure_liege_or_above
- is_at_war_with_liege
- is_in_civil_war
- is_in_ongoing_great_holy_war
- has_character_modifier
- reverse_has_opinion_modifier
- has_opinion_modifier
- opinion_greater_or_equal
- opinion_less_than
- trait_is_sin
- trait_is_virtue
- trait_is_sin_rite
- trait_is_virtue_rite
- has_trait
- has_trait_group
- has_trait_xp
- has_trait_xp_greater_or_equal
- has_trait_xp_less_than
- has_trait_xp_single
- has_trait_xp_single_greater_or_equal
- has_trait_xp_single_less_than
- is_imprisoned
- is_independent_ruler
- is_head_of_faith
- is_imprisoned_by
- imprisoner
- time_in_prison_type
- is_in_prison_type
- time_in_prison
- days_in_prison
- is_parent_of
- is_child_of
- is_sibling_of
- is_uncle_or_aunt_of
- is_nibling_of
- is_grandparent_of
- is_great_grandparent_of
- is_great_grandchild_of
- is_at_war
- gold_greater_or_equal
- gold_less_than
- gold_greater_than
- gold
- gold_equal
- gold_less_or_equal
- piety_greater_or_equal
- piety_less_than
- piety_greater_than
- piety
- piety_level
- piety_equal
- piety_less_or_equal
- prestige_greater_or_equal
- prestige_less_than
- prestige_greater_than
- dynasty_prestige
- prestige
- prestige_equal
- prestige_less_or_equal
- herd_greater_or_equal
- herd_less_than
- treasury_greater_or_equal
- treasury_or_gold_greater_or_equal
- barter_goods
- is_councillor
- is_normal_councillor
- is_special_councillor
- has_council_position
- is_councillor_of
- has_free_council_slot
- is_performing_council_task
- has_realm_law
- vassal_limit_available
- vassalization_cb_target_too_many_counties
- claimant_already_pressing_their_claim
- claimant_titles_held_by_attacker_vassals
- claimant_titles_held_by_you_or_vassal
- claimant_is_blind
- claim_target_position_is_weak
- claimant_is_attacker_or_same_dynasty
- byzantine_claimant_is_disfigured
- byzantine_claimant_is_celibate
- is_not_theocratic_court_chaplain
- grant_title_stealing_acclaimed_knight
- partition_primary_heir_unfair
- days_until_ghw_launch
- has_culture
- has_same_culture_group_as
- has_same_culture_as
- has_culture_group
- has_faith
- has_religion
- prestige_level
- prestige_level_greater_or_equal
- prestige_level_less_than
- influence_level
- influence_level_greater_or_equal
- influence_level_less_than
- piety_level_greater_or_equal
- piety_level_less_than
- dread
- tyranny
- subject_standing
- legitimacy
- legitimacy_level
- age
- age_less_than
- vassal_contract_uses_obligation_levels
- vassal_contract_modification_above_baron
- subject_contract_is_blocked_from_modification
- vassal_contract_can_be_modified
- character_is_religious_head_of_faith
- diplomacy
- diplomacy_greater_or_equal
- diplomacy_less_than
- martial
- martial_greater_or_equal
- martial_less_than
- stewardship
- stewardship_greater_or_equal
- stewardship_less_than
- intrigue
- intrigue_greater_or_equal
- intrigue_less_than
- learning
- learning_greater_or_equal
- learning_less_than
- can_attack_in_hierarchy
- is_incapable
- is_immortal
- has_trait_rank
- number_of_traits
- number_of_opposing_personality_traits
- number_of_opposing_traits
- number_of_lifestyle_traits
- number_of_commander_traits
- number_of_commander_traits_in_common
- number_of_traits_in_common
- num_of_bad_genetic_traits
- num_of_bad_genetic_traits_equal
- num_virtuous_traits
- has_same_sinful_trait
- has_same_virtue_trait
- number_of_sinful_traits_in_common
- number_of_virtue_traits_in_common
- num_of_good_genetic_traits
- num_of_good_genetic_traits_equal
- domain_size
- realm_size
- realm_size_greater_or_equal
- realm_size_less_than
- sub_realm_size
- sub_realm_size_greater_or_equal
- sub_realm_size_less_than
- any_sub_realm_title
- any_sub_realm_empire
- any_sub_realm_kingdom
- any_sub_realm_duchy
- any_sub_realm_county
- found_kingdom_decision_three_duchies_held
- found_empire_decision_three_kingdoms_held
- has_strong_hook
- has_strong_usable_hook
- has_hook_of_type
- has_usable_hook
- has_weak_hook
- reverse_opinion
- opinion
- stress
- stress_level
- stress_level_greater_or_equal
- stress_level_less_than
- is_pregnant
- is_spouse_of
- is_concubine
- is_concubine_of
- is_close_family_of
- is_grandchild_of
- is_twin
- is_twin_of
- is_cousin_of
- is_extended_family_of
- is_close_or_extended_family_of
- tier_difference
- highest_held_title_tier
- holds_landed_title
- has_truce
- is_knight
- is_knight_of
- is_employer_of
- is_courtier
- is_courtier_of
- is_foreign_court_or_pool_guest
- is_pool_guest_of
- is_powerful_vassal
- is_powerful_vassal_of
- number_of_powerful_vassals
- is_vassal_or_below_of
- is_heir_of
- is_primary_heir_of
- is_male
- is_female
- patrilinear_marriage
- matrilinear_marriage
- patrilinear_betrothal
- matrilinear_betrothal
- is_vassal_of
- is_commanding_army
- is_in_army
- is_player_heir_of
- is_consort_of
- demand_vassal_conversion_interaction_cooldown
- in_diplomatic_range
- realm_to_title_distance_squared
- death_reason
- has_imprisonment_reason
- completely_controls
- completely_controls_region
- was_discovered_fabricating_hooks_already
- already_has_hook_on_ruler_target
- already_has_strong_hook_on_target
- has_any_secrets
- already_knows_secret_about_ruler_target
- already_knows_criminal_secret_about_target
- spymaster_will_not_find_secrets_at_own_court
- law_change_approval_is_cowed
- wants_more_vassals
- is_alive
- health
- is_clergy
- prowess
- prowess_greater_or_equal
- prowess_less_than
- prowess_no_portrait
- prowess_no_portrait_greater_or_equal
- prowess_no_portrait_less_than
- ransom_cost
- sex_same_as
- has_any_nickname
- is_local_player
- domain_limit
- has_had_focus_for_days
- is_council_task_valid
- is_council_task_valid_county
- is_council_task_valid_court
- chancellor_will_not_increase_their_own_opinion
- chancellor_will_not_increase_their_liege_opinion
- has_any_court_position
- has_employed_any_court_position
- has_court_position
- employs_court_position
- can_be_employed_as
- can_employ_court_position_type
- is_court_position_employer
- any_court_position_employer
- any_court_position_holder
- has_royal_court
- can_not_fabricate_hooks_on_wanderers
- is_decision_on_cooldown
- found_empire_decision_not_part_of_iberian_struggle
- no_activity_available
- has_potential_accolade_successors
- is_rightful_liege_of
- was_preferred_heir
- influence_greater_or_equal
- influence_less_than
- any_ally
- character_is_land_realm_neighbor
- number_of_tributaries_greater_or_equal
- number_of_tributaries_less_than
- merit_level
- merit_level_greater_or_equal
- merit_level_less_than
- is_liege_or_above_of
- character_this_not_equal
- character_this_equal
- is_in_guest_subset
- realm_law_group_at_minimum_level
- realm_law_group_at_maximum_level

### 00_culture_triggers.txt（62 条目）

- has_innovation
- innovation_unlocked_by_decision_trigger
- has_cultural_era_or_later
- de_jure_drifting_towards
- de_jure_drift_progress
- can_only_change_culture_once
- culture_present_in_realm_for_hybridization
- culture_is_not_parent_culture
- culture_is_not_child_culture
- culture_present_in_realm_for_divergence
- culture_has_tradition_cooldown
- culture_in_winter_geographical_region_trigger_desc
- culture_in_non_sedentary_geographical_region_trigger_desc
- culture_in_britannia_region_trigger_desc
- culture_in_india_region_trigger_desc
- culture_in_world_europe_north_region_trigger_desc
- culture_in_forest_desc
- culture_in_mountains_desc
- culture_in_dryland_desc
- culture_in_desert_desc
- culture_in_hills_desc
- culture_in_jungle_desc
- culture_in_steppe_desc
- culture_not_egalitarian
- culture_not_bellicose
- culture_not_pacifist_trigger_desc
- culture_not_warlike_trigger_desc
- culture_has_winter_warriors_desc
- culture_has_forest_fighter_desc
- culture_has_mountaineers_desc
- culture_has_warriors_of_the_dry_desc
- culture_has_highland_warriors_desc
- culture_has_jungle_warriors_desc
- culture_has_quarrelsome_desc
- culture_has_malleable_invaders_desc
- culture_has_hunters_desc
- culture_has_warrior_culture_desc
- culture_has_martial_admiration_desc
- culture_on_coast_desc
- knows_language
- knows_language_of_culture
- has_cultural_tradition
- lacks_overlapping_cultrad_tradition_fp1_coastal_warriors
- lacks_overlapping_cultrad_tradition_fp1_northern_stories
- lacks_overlapping_cultrad_tradition_fp1_trials_by_combat
- lacks_overlapping_cultrad_tradition_fp1_the_right_to_prove
- lacks_overlapping_cultrad_tradition_runestones
- lacks_overlapping_cultrad_tradition_fp1_performative_honour
- lacks_overlapping_cultrad_tradition_warrior_culture
- lacks_overlapping_cultrad_tradition_seafaring
- lacks_overlapping_cultrad_tradition_poetry
- lacks_overlapping_cultrad_tradition_storytellers
- lacks_overlapping_cultrad_tradition_city_keepers
- percentage_of_culture_on_coast_desc
- mystical_ancestors_disinherit
- merciful_blindings_disinherited
- lacks_overlapping_cultrad_tt
- has_cultural_pillar
- has_cultural_parameter
- num_discovered_innovations
- num_discovered_innovations_in_era
- has_same_culture_heritage

### 00_custom_triggers.txt（29 条目）

- can_be_combatant_based_on_gender
- clergy_can_be_combatant
- controls_enough_culture_counties
- auto_accept_interaction_ai
- has_law_allowing_succession_law_change
- is_not_wandering_child
- basic_claimant_found
- basic_capable_claimant_found
- claimant_faction_already_exists
- steal_back_artifact_can_start_scheme
- ALREADY_PLANNING_ACTIVITY
- ALREADY_IN_ACTIVITY
- GAME_OVER_CANNOT_PLAY_THEOCRACY
- GAME_OVER_CANNOT_PLAY_ADVENTURER
- GAME_OVER_CANNOT_PLAY_ADMIN
- GAME_OVER_CANNOT_PLAY_REPUBLIC
- GAME_OVER_CANNOT_PLAY_MERCENARY
- GAME_OVER_CANNOT_PLAY_HOLY_ORDER
- GAME_OVER_CANNOT_PLAY_BARON
- SUPPRESS
- malabarism_religious_head_exists_tt
- ENGAGED_IN_SINGLE_COMBAT
- realm_has_more_than_2_siegeable_holdings_trigger_custom_desc
- any_opposite_trait_all
- followers_over_diplomacy
- has_contagious_deadly_disease_trigger
- HOF_DOESNT_EXIST
- CORONATION_RELIGIOUS_AUTHORITY_DOESNT_EXIST
- CORONATION_ANOINTMENT_GUEST_AUTHORITY_DOESNT_EXIST

### 00_debug_triggers.txt（83 条目）

- ai_diplomacy_stance
- is_ai
- ai_honor
- ai_rationality
- ai_energy
- ai_greed
- ai_compassion
- ai_zeal
- ai_boldness
- ai_sociability
- ai_vengefulness
- has_province_modifier
- current_date
- current_day
- current_month
- current_year
- time_of_year
- current_computer_date
- has_icon
- is_color
- in_color_list
- base_weight
- target_weight
- current_weight
- current_weight_for_portrait
- is_tutorial_active
- years_from_game_start
- game_start_date
- diplomacy_for_portrait
- prowess_for_portrait
- martial_for_portrait
- stewardship_for_portrait
- intrigue_for_portrait
- learning_for_portrait
- has_gene
- is_visibly_fertile
- fertility
- pregnancy_days
- has_variable
- has_map_mode
- num_of_relation_intrigue_student
- has_secret_relation_intrigue_student
- has_relation_soldier_friend
- has_secret_relation_soldier_friend
- num_of_relation_mentor
- has_secret_relation_student
- has_relation_oaf
- num_of_relation_oaf
- has_secret_relation_rival
- has_secret_relation_potential_rival
- has_relation_potential_rival
- num_of_relation_potential_rival
- has_secret_relation_soulmate
- has_secret_relation_potential_lover
- has_relation_potential_lover
- num_of_relation_potential_lover
- has_secret_relation_crush
- has_secret_relation_victim
- has_secret_relation_bully
- has_secret_relation_friend
- has_secret_relation_potential_friend
- has_relation_potential_friend
- num_of_relation_potential_friend
- has_secret_relation_best_friend
- has_secret_relation_guardian
- has_secret_relation_court_physician
- has_secret_relation_intrigue_mentor
- has_secret_relation_oaf
- has_any_secret_relation
- story_type
- owns_a_story
- has_trait_with_flag
- is_frontend_character_selected
- is_widgetid_open
- can_start_tutorial_lesson
- has_inactive_trait
- witchcraft_scheme_blocked
- crypto_religion_scheme_blocked
- has_game_rule
- release_only
- has_global_variable
- ai_values_divergence
- year_of_birth

### 00_dlc_triggers.txt（2 条目）

- has_dlc
- has_dlc_feature

### 00_doctrine_triggers.txt（51 条目）

- incompatible_tenet_armed_pilgrimages_trigger
- incompatible_tenet_anachoresis_trigger
- incompatible_tenet_pacifism_trigger
- incompatible_tenet_communion_trigger
- incompatible_tenet_sacred_shadows_trigger
- incompatible_tenet_dharmic_pacifism_trigger
- incompatible_tenet_human_sacrifice_trigger
- incompatible_tenet_gruesome_festivals_trigger
- incompatible_tenet_mendicant_preachers_trigger
- incompatible_tenet_hedonistic_trigger
- incompatible_tenet_gnosticism_trigger
- incompatible_tenet_eastern_syncretism_trigger
- incompatible_tenet_other_syncretism_trigger
- incompatible_tenet_false_conversion_sanction_trigger
- incompatible_tenet_pentarchy_trigger
- incompatible_tenet_sacrificial_ceremonies_trigger
- incompatible_tenet_consolamentum_trigger
- incompatible_tenet_shared_hof_pacifists_vs_warmongers
- incompatible_tenet_shared_hof_criminal_witches_vs_adorcists
- incompatible_tenet_shared_hof_hedonists_vs_ascetics
- incompatible_tenet_shared_hof_cannibals_vs_non_cannibals
- incompatible_tenet_shared_hof_world_vs_humsac_grufes
- incompatible_tenet_shared_hof_monogamy_vs_polygamy
- incompatible_tenet_shared_hof_world_vs_unrestricted_incest
- incompatible_tenet_armed_pilgrimages_vs_forbidden_pilgrimages
- incompatible_doctrine_mummification_trigger
- incompatible_tenet_aniconism_trigger
- rome_must_be_faithfully_restored_trigger
- doctrine_pluralism_fundamentalist_trigger
- doctrine_inverted_pluralism_fundamentalist_trigger
- doctrine_pluralism_pluralistic_trigger
- doctrine_inverted_pluralism_pluralistic_trigger
- doctrine_unrestricted_consanguinity_trigger
- doctrine_requires_theocratic_head_of_faith_trigger
- doctrine_no_head_of_faith_trigger
- doctrine_requires_head_of_faith_trigger
- has_doctrine
- rite_has_doctrine
- has_doctrine_parameter
- rite_has_parameter
- incompatible_doctrine_theocracy_temporal_trigger
- incompatible_doctrine_spiritual_appointment_temporal_trigger
- incompatible_with_crimes_trigger
- ADULTERY_MUST_BE_FULLY_ACCEPTED
- must_select_carnal_exaltation
- fedayeen_required_doctrines_trigger
- decision_has_court_chaplain
- decision_sought_aid_of_spirits
- decision_consolamentum_health
- court_chaplain_cant_fire_doctrines
- court_chaplain_cant_reassign_doctrines

### 00_dynasty_triggers.txt（14 条目）

- dynasty_prestige_greater_or_equal
- dynasty_prestige_less_than
- has_dynasty_modifier
- has_house_modifier
- has_house_unity_modifier
- dynasty_prestige_level
- dynasty_prestige_level_greater_or_equal
- dynasty_prestige_level_less_than
- adult_house_member_percent_greater_or_equal
- adult_house_member_count_greater_or_equal
- has_dynasty
- dynasty_num_unlocked_perks
- has_dynasty_perk
- house_head_equal

### 00_faction_triggers.txt（16 条目）

- can_create_faction
- can_join_faction
- character_blocked_from_joining
- barons_joining_independence_factions
- character_is_immune_to_factions
- has_lowest_crown_authority
- has_lowest_imperial_bureaucracy
- has_lowest_tribal_authority
- has_lowest_celestial_bureaucracy
- has_lowest_meritocratic_bureaucracy
- has_lowest_japanese_bureaucracy
- already_has_lowest_government_authority
- faction_can_join_create_in_another_faction
- character_has_faction_disabling_modifier
- is_a_faction_member
- faction_can_press_demands

### 00_ghw_triggers.txt（12 条目）

- pledge_ghw_liege_condition
- pledge_ghw_indep_or_faith_condition
- pledge_ghw_recently_unpledged
- pledge_ghw_papal_hooked_pledge
- pledge_ghw_no_war_after_start
- ghw_give_gold_already_giving_gold
- ghw_give_gold_already_given_gold
- ghw_recipient_must_not_be_realm_priest
- ghw_attackers_strength
- is_pledged_ghw_attacker
- ghw_defenders_strength
- is_directed_ghw

### 00_government_triggers.txt（10 条目）

- government_has_flag
- government_allows
- government_disallows
- has_government
- has_same_government_trigger
- change_law_male_preference_faith_requirement
- change_law_female_preference_faith_requirement
- has_house_unity_parameter
- use_government_authority
- has_clerical_region

### 00_holy_order_triggers.txt（6 条目）

- hold_king_tier_title_or_higher
- not_inheriting_check
- not_rival_leader_check
- was_asked_to_take_vows_recently
- is_holy_order
- controls_holy_site

### 00_landed_title_triggers.txt（38 条目）

- recent_history
- is_contested
- place_in_line_of_succession
- place_in_line_of_succession_range
- has_succession_appointment_investors
- succession_appointment_score_invested
- tier_equal
- tier_less_than
- tier_less_or_equal
- tier_greater_than
- tier_greater_or_equal
- mend_schism_roma_bishop
- mend_schism_alexandria_bishop
- mend_schism_jerusalem_bishop
- mend_schism_antiocheia_bishop
- mend_schism_byzantion_bishop
- mend_schism_no_rite
- form_austria_hre_dynasty_trigger
- has_title
- restore_high_priesthood_holy_sites
- jerusalem_is_same_faith
- has_primary_title
- geographical_region
- consecrate_bloodline_holy_site
- has_revokable_lease
- has_order_of_succession
- has_title_law_flag
- is_titular
- form_germania_christian_trigger
- form_hispania_must_end_struggle_trigger
- title_held_years
- landed_title_this_equal
- appointment_candidate_score_greater_or_equal
- appointment_candidate_score_less_than
- appointment_candidate_accumulated_score_greater_or_equal
- appointment_candidate_accumulated_score_less_than
- title_law_group_at_minimum_level
- title_law_group_at_maximum_level

### 00_law_triggers.txt（6 条目）

- succession_laws_must_have_organised_government_tooltip
- succession_laws_must_not_be_forced_partition
- succession_laws_must_have_valid_tanistry_culture
- succession_laws_must_not_be_temporal
- number_of_election_votes
- border_wars_laws_triggers

### 00_legend_triggers.txt（3 条目）

- has_legend_owner_modifier
- has_legend_province_modifier
- has_legend_county_modifier

### 00_lifestyle_triggers.txt（10 条目）

- has_focus
- has_lifestyle
- has_perk
- perk_points_assigned
- already_reset_perks
- diplomacy_lifestyle_perk_points
- martial_lifestyle_perk_points
- stewardship_lifestyle_perk_points
- intrigue_lifestyle_perk_points
- learning_lifestyle_perk_points

### 00_logic_triggers.txt（5 条目）

- and
- or
- not
- nand
- calc_true_if

### 00_province_script_list_triggers.txt（6 条目）

- any_province
- any_province_all
- any_realm_province
- any_directly_owned_province
- any_directly_owned_province_count
- any_realm_province_all

### 00_province_triggers.txt（24 条目）

- development_level
- development_rate
- is_county_capital
- potential_county_control_task_trigger
- county_opinion
- monthly_county_control_change
- num_county_followers
- is_coastal
- is_lakeside
- is_lakeside_county
- has_stationed_regiment
- has_stationed_regiment_of_base_type
- is_coastal_county
- is_holy_site
- has_county_modifier
- has_realm_law_flag
- is_capital_barony
- has_construction_with_flag
- num_leased_titles
- is_raided
- has_province_owner
- is_leased_out
- is_holy_site_of
- any_county_province

### 00_religion_triggers.txt（34 条目）

- religion_tag
- rite_religion_tag
- fervor
- num_virtuous_traits_greater_or_equal
- num_virtuous_traits_less_than
- num_sinful_traits
- num_sinful_traits_greater_or_equal
- num_sinful_traits_less_than
- has_same_religion_as
- has_dominant_ruling_gender
- religion
- is_in_family
- holy_sites_controlled_greater_or_equal
- holy_sites_controlled_less_than
- number_realm_holy_sites_held_by_faithful
- direct_realm_holy_sites_held_by_faithful_confederation
- faith_allows_legitimization_of_bastards
- cannot_create_hof_title_at_or_above_liege_tier
- character_can_only_create_one_faith
- character_can_only_create_one_rite
- character_can_only_edit_one_rite
- any_faith_ruler
- claim_the_imamate_decision.need_at_least_five_same_faith_counties
- claim_the_imamate_decision.need_at_least_fifteen_same_faith_counties
- claim_the_imamate_decision.foreign_ruler
- claim_the_imamate_decision.no_more_than_x_sinful_traits
- avenge_the_battle_of_nahrawan_sunni_caliphate_irrelevant
- avenge_the_battle_of_nahrawan_shia_caliphate_irrelevant
- pledged_to_not_promote_persian_desc
- name_already_read_in_friday_prayer
- name_read_in_friday_prayer_crown_authority
- knows_about_character_being_same_crypto_religionist
- spiritual_fulfillment_greater_or_equal
- spiritual_fulfillment_less_than

### 00_scheme_script_list_triggers.txt（23 条目）

- any_scheme
- any_scheme_all
- any_scheme_agent_character
- any_scheme_agent_all
- scheme_progress
- scheme_success_chance
- has_scheme_modifier
- scheme_phase_duration
- scheme_skill
- is_valid_as_agent_in_slot
- is_valid_as_agent_in_any_slot
- can_start_scheme
- scheme_resistance
- scheme_secrecy
- is_forced_into_scheme
- is_scheme_exposed
- scheme_type
- scheme_number_of_exposed_agents
- scheme_monthly_progress
- does_not_want_to_be_soulmates
- scheme_target_same_language_as_existing_scheme
- is_scheming_against
- agent_slot_contribution

### 00_scope_comparison_triggers.txt（45 条目）

- province_county_equal
- landed_title_county_equal
- province_duchy_equal
- landed_title_duchy_equal
- province_kingdom_equal
- landed_title_kingdom_equal
- province_empire_equal
- landed_title_empire_equal
- province_hegemony_equal
- landed_title_hegemony_equal
- holder_equal
- de_jure_liege_equal
- de_facto_liege_equal
- liege_equal
- killer_equal
- imprisoner_equal
- host_equal
- betrothed_equal
- mother_equal
- father_equal
- real_father_equal
- player_heir_equal
- character_rite_equal
- character_faith_equal
- character_religion_equal
- character_culture_equal
- character_culture_group_equal
- house_equal
- dynasty_equal
- landed_title_rite_equal
- landed_title_rite_not_equal
- landed_title_faith_equal
- landed_title_faith_not_equal
- landed_title_religion_equal
- landed_title_religion_not_equal
- landed_title_culture_equal
- landed_title_culture_not_equal
- province_rite_equal
- province_faith_equal
- province_religion_equal
- province_culture_equal
- capital_province_equal
- faith_religion_equal
- culture_culture_group_equal
- accolade_type_this_equal

### 00_script_list_triggers.txt（22 条目）

- any_child
- any_child_all
- any_spouse
- any_spouse_all
- any_courtier
- any_courtier_all
- any_courtier_count
- any_warden_hostage
- any_hooked_character
- any_hooked_character_all
- any_claimant
- any_claimant_all
- any_holy_site
- any_holy_site_barony
- any_dynasty_member_count
- any_held_title
- any_held_title_count
- any_held_title_percent
- any_realm_county
- any_realm_county_count
- any_confederation_member_house
- any_confederation_member_house_percent

### 00_secret_script_list_triggers.txt（4 条目）

- any_secret
- any_secret_all
- any_known_secret
- any_known_secret_all

### 00_secret_triggers.txt（7 条目）

- is_spent_by
- can_be_exposed_by
- has_secret_relation_lover
- is_known_by
- same_secret_type_as
- secret_type
- is_shunned_or_criminal_for

### 00_travel_triggers.txt（6 条目）

- is_travelling
- is_aborted
- is_completed
- is_paused
- is_cancelled
- can_cancel

### 00_tutorial_triggers.txt（39 条目）

- lesson_basics_tooltips_in_tooltips_hover_word
- lesson_basics_tooltips_in_tooltips_hover_word_deeper
- lesson_basics_characters_click_on_character
- lesson_basics_lifestyle_open_window_tt
- lesson_basics_lifestyle_choose_focus_tt
- lesson_basics_open_character_view_tt
- lesson_basics_open_interactions_tt
- lesson_basics_send_gift_tt
- lesson_basics_realm_view_tt
- lesson_basics_succession_tab_tt
- lesson_basics_open_interactions_marriage_tt
- lesson_basics_marriage_view_tt
- lesson_basics_open_interactions_marriage_alt_tt
- lesson_basics_get_married_tt
- lesson_basics_change_map_mode_1_tt
- lesson_basics_change_map_mode_2_tt
- lesson_basics_vassals_tab_tt
- lesson_basics_council_view_tt
- lesson_basics_intrigue_view_tt
- lesson_basics_schemes_tab_tt
- tutorial_basic_schemes_start_swaying_tt
- lesson_basics_hooks_and_secrets_tab_tt
- lesson_basics_military_view_tt
- reactive_advice_mercenaries_task
- lesson_basics_culture_open_view_trigger
- lesson_basics_culture_open_innovations_tab_trigger
- lesson_basics_religion_click_religion_tt
- ra_court_pos_open_view_trigger
- ra_maa_stationing_open_card_step_tt
- ra_maa_stationing_click_station_button_tt
- ra_maa_stationing_select_station_tt
- lesson_declare_war_tt
- lesson_open_war_overview_tt
- lesson_basics_start_construction_tt
- lesson_raise_troops_tt
- ra_tours_picking_vassals_add_prompt
- lesson_basics_council_fabricate_claim_tt
- lesson_basics_quick_unpause_tt
- lesson_basics_quick_find_spouse_tt

### 00_unity_triggers.txt（1 条目）

- has_house_unity_stage

### 00_war_triggers.txt（33 条目）

- is_attacker
- is_defender
- is_participant
- is_war_leader
- has_any_cb_on
- has_any_display_cb_on
- has_raised_armies
- was_called
- has_valid_casus_belli
- has_used_lifetime_subjugation
- declared_major_religious_war_flag_tt
- great_holy_war_cooldown
- is_attacker_in_war
- is_defender_in_war
- is_war_overview_tab_open
- is_leader_in_war
- is_participant_in_war
- is_at_war_as_attacker
- has_pledged_attacker
- is_at_war_as_defender
- has_pledged_defender
- faction_is_at_war
- attacker_war_score
- defender_war_score
- is_white_peace_possible
- war_days
- using_cb
- has_cb_on
- max_military_strength
- is_army_in_siege_relevant_for
- raid_loot
- is_occupied
- army_supply

### 01_character_interaction_triggers.txt（326 条目）

- character_interactions_imprison_ally_without_reason
- character_interactions_imprison_recently_ransomed
- character_interactions_revoke_title_from_ally_without_reason
- has_law_allowing_title_revocation_tribal
- has_law_allowing_title_revocation_crown
- has_law_allowing_title_revocation_church
- has_law_allowing_title_revocation_soryo
- liege_has_law_allowing_title_revocation_tribal
- cannot_diarch_revoke_administrative_titles
- liege_has_law_allowing_title_revocation_crown
- has_admin_allowing_designate_heir
- has_crown_authority_designate_heir
- has_law_allowing_designate_heir
- vassal_contract_forbids_revocation
- liege_vassal_contract_forbids_revocation
- diarch_has_claim_on_revokable_title
- you_must_have_a_claim_on_the_title
- you_must_have_a_de_jure_vassal_to_retract
- you_must_be_be_de_jure_liege_of_this_vassal
- dynasty_member_leads_election
- religion_does_not_allow_theocratic_revocations
- has_law_allowing_vassal_retraction_tribal
- has_law_allowing_vassal_retraction_crown
- has_law_allowing_vassal_retraction_church
- has_law_allowing_vassal_retraction_admin
- liege_has_law_allowing_vassal_retraction_tribal
- liege_has_law_allowing_vassal_retraction_crown
- liege_has_law_allowing_vassal_retraction_admin
- has_tribal_law_allowing_succession_law_change
- has_crown_law_allowing_succession_law_change_feudal
- has_crown_law_allowing_succession_law_change_japanese_feudal
- has_crown_law_allowing_succession_law_change
- has_imperial_bureaucracy_law_allowing_succession_law_change
- has_law_allowing_partition_succession_law_change
- no_powerful_vassal_with_negative_opinion
- can_target_character_with_scheme
- can_start_more_schemes_of_category
- befriend_already_lover
- befriend_already_friend
- seduce_already_lover
- romance_already_soulmate
- SCHEME_SEDUCE_UNWILLING_INCEST_TOO_YOUNG
- seduce_blocked
- seduce_cooldown
- romance_cooldown
- romance_success_blocked
- seduce_general_10_year_cooldown
- no_attraction_due_to_gender
- no_attraction_due_to_gender_me
- abduct_own_children_block
- test_interaction_not_implemented
- character_is_clergy_and_cannot_marry
- can_marry_check_secondary_actor
- can_marry_check_secondary_recipient
- can_betroth_check_secondary_actor
- can_betroth_check_secondary_recipient
- actor_is_house_head
- basic_can_marry_check_recipient
- character_to_marry_exists
- recently_divorced
- spending_hook
- is_betrothed_auto_accept
- recipient_is_spouse
- must_be_war_leader
- cannot_call_same_character_multiple_times
- cannot_call_vassal_to_war
- cannot_call_liege_to_war
- cannot_call_liege_ally_against_fellow_vassal
- cannot_create_cadet_branch
- is_recipients_player_heir
- is_player_heir
- education_interaction_adult_secondary_actor
- education_interaction_adult_secondary_recipient
- education_interaction_two_wards_only
- character_to_educate_exists
- already_scheming_language
- character_to_guard_exists
- no_target_language
- faith_is_reformed
- faith_has_been_reformed
- recently_took_tribal_challenge_ruler_decision
- I_have_imprisoned_target
- i_have_been_caught_trying_to_murder_target
- you_have_been_caught_trying_to_elope_with_target
- you_have_been_caught_trying_to_steal_artifact_from_target
- you_have_recently_stolen_artifact_from_target
- basic_valid_vassal_to_tranfer
- basic_vassal_to_retract
- diarch_is_de_jure_liege_of_retractable_vassal
- cannot_grant_own_diarch_as_vassal
- basic_is_at_war_with_vassal
- basic_is_at_war_with_sub_vassal
- basic_independence_faction_at_war
- basic_ally_can_join_because_liege_or_vassals
- liege_is_at_war_with_recipient
- vassal_is_at_war_with_recipient
- declare_war_hook_on_liege
- is_not_bankrupt
- army_blocks_defender_army
- elope_scheme_character_reserved
- yearly_1010_abducted
- yearly_1010_abductor
- hof_ask_for_gold_excommunicated
- hof_ask_for_claim_no_baronies
- hof_ask_for_claim_theocratic_lessee
- hof_ask_for_claim_has_pressed_claim_already
- hof_ask_for_claim_excommunicated
- seek_indulgences_excommunicated
- declaration_of_repentance_hook
- declaration_of_repentance_hook_valid
- declaration_of_repentance_hook_invalid
- excommunication_hook
- excommunication_hook_valid
- excommunication_hook_invalid
- temporal_condemnation_learning_requirement
- temporal_condemnation_is_not_sinful
- temporal_condemnation_less_sinful_than_me
- temporal_condemnation_as_sinful_as_me
- temporal_condemnation_has_been_condemned
- host_honored_guest_is_hostile
- host_honored_guest_is_evil
- host_honored_guest_is_unwell
- host_honored_guest_is_commanding
- host_honored_guest_is_imprisoned
- host_honored_guest_is_at_war
- host_honored_guest_is_my_courtier
- is_already_war_enemy_of_primary_enemy
- is_married_matrilineally_and_spouse_is_dominant_partner
- is_married_matrilineally
- is_married_patrilineally_and_spouse_is_dominant_partner
- is_married_patrilineally
- is_escaped_prisoner
- is_paiza_merchant
- is_war_enemy_with_another_target_war_enemy
- has_usable_hook_or_council_rights_through_vassal_contract
- is_blocked_from_being_fired_from_council
- is_war_enemy_with_my_war_ally
- is_war_ally_of_primary_enemy
- is_of_wrong_faith_for_holy_war
- is_of_attacker_faith_in_holy_war
- is_war_ally_of_another_target_enemy
- offer_fealty_interaction_neighboring_condition
- FACTION_CANT_JOIN_IF_TARGET
- FACTION_CANT_JOIN_CREATE_ADULT
- FACTION_CANT_JOIN_CREATE_ALLIED
- FACTION_CANT_JOIN_CREATE_HOOK
- FACTION_CANT_JOIN_CREATE_IMPRISONED
- FACTION_CANT_JOIN_CREATE_INCAPABLE
- create_faction_imprisoned
- faction_relation_blocks_joining_friend
- faction_relation_blocks_joining_lover
- FACTION_SOFT_BLOCK_IS_NOT_COURT_CHAPLAIN
- join_faction_target
- sway_blocked
- modify_vassal_contract_select_different_obligation_level
- modify_non_feudal_vassal_contract_select_different_obligation_level
- vassal_modify_vassal_contract_cannot_increase_obligation_level
- vassal_modify_vassal_contract_obligation_change_limit
- liege_modify_vassal_contract_cannot_exceed_tyranny_cap
- vassal_modify_vassal_contract_unnecessary_hook_usage_vassal_favor
- vassal_modify_vassal_contract_unnecessary_hook_usage_equal
- tributary_modify_tributary_contract_unnecessary_hook_usage_tributary_favor
- tributary_modify_tributary_contract_unnecessary_hook_usage_equal
- is_dynast
- is_a_witch
- is_not_a_witch
- has_a_witch_secret_known_by_character
- has_a_crypto_religionist_secret_known_by_character
- not_family_or_adventurer_title
- has_51_percent_of_a_dejure_title
- has_15_percent_of_a_dejure_title
- has_21_percent_of_a_dejure_title
- has_31_percent_of_a_dejure_title
- has_41_percent_of_a_dejure_title
- cannot_blackmail_own_lover_secret
- cannot_blackmail_over_own_bastard
- cant_blackmail_another_witch
- cannot_blackmail_crypto_religionist_of_same_faith
- already_has_a_superior_hook
- promised_not_to_reveal_secret
- cannot_imprison_almohad_leader
- character_interactions_hostile_actions_disabled_delay
- character_interactions_not_rel_head_title
- character_interactions_not_clerical_region_title
- character_interactions_not_clerical_elector_title
- character_interactions_not_antipope_office_title
- character_is_real_head
- character_is_not_real_head
- character_is_rite_head
- cannot_demand_religious_head_conversion
- cannot_demand_holy_order_master_conversion
- cannot_demand_unsubordinate_landed_ruler_conversion
- cannot_demand_steadfast_character_conversion
- release_take_vows_invalid_recruit
- release_banish_invalid_take_vows
- release_executioner_invalid_recruit
- release_executioner_invalid_take_vows_condition
- release_vows_invalid_not_your_faith
- release_vows_invalid_not_your_court
- release_byz_vows_invalid
- release_byz_disfigure_invalid
- release_prisoner_disfigure_blind_castrate_condition
- release_renounce_claims
- torture_cooldown_actor
- currently_being_tortured
- has_sent_interaction_already
- has_no_option_selected
- character_unavailable_to_be_offered_as_concubine
- has_already_rejected_renegotiation
- rulers_family_is_married_to_other_ruler_trigger
- rulers_child_parent_sibling_is_married_to_other_rulers_trigger
- is_protected_via_contract
- is_protected_via_contract_self_or_liege
- already_has_an_alliance_deal
- cannot_stop_war_when_already_fighting
- cannot_stop_war_timer
- faith_creation_duchy_or_higher
- has_crown_authority_cooldown
- has_tribal_authority_cooldown
- has_nomadic_authority_cooldown
- has_church_authority_cooldown
- nomadic_authority_2_level_requirement
- nomadic_authority_3_level_requirement
- nomadic_authority_4_level_requirement
- has_imperial_bureaucracy_cooldown
- has_celestial_bureaucracy_cooldown
- has_meritocratic_bureaucracy_cooldown
- has_japanese_bureaucracy_cooldown
- nomadic_authority_5_greatest_khan
- nomadic_authority_5_gurkhan
- is_player_heir_of_trigger_text
- pressing_claim_of_character_trigger_text
- buy_claim_has_pressed_claim_already
- buy_claim_no_king_or_emperor_kingdom
- buy_claim_no_emperor_empire
- buy_claim_no_religious_titles
- buy_claim_no_landless_adventurer_title
- buy_claim_no_noble_family_titles
- kick_from_court_interaction_travelling_family_invalid
- demand_payment_too_little_gold
- join_war_interaction_recipient_warring_with_my_liege
- join_war_interaction_recipient_not_def_GHW
- join_war_interaction_target_not_contract_war
- join_war_interaction_recipient_too_distant
- join_war_interaction_recipient_not_liege
- join_war_interaction_recipient_not_ally
- join_war_interaction_recipient_not_fighting_peasant_faction
- join_war_interaction_already_warring_against_enemy
- join_war_interaction_already_in_target_war
- was_recently_granted_independence
- not_recently_offered_submission
- truce_on_recipient_tt
- is_de_jure_vassal_check
- is_at_war_with_another_vassal
- feudalize_holding_interaction_title_not_county_or_below
- has_all_tribal_innovations
- must_have_usable_hook_blocker
- blocked_from_remove_councillor
- is_not_considering_offer_of_subjugation
- take_concubine_allowed_more
- take_concubine_available_character_opp
- tranfer_vassal_available_vassal
- break_betrothal_hook_used
- break_betrothal_gwedding_ongoing
- offer_fealty_neighboring_and_de_jure_condition
- offer_fealty_neighboring_condition
- character_interaction_ready_to_consider
- no_blackmailable_secret
- already_strong_hook
- not_allowed_in_varangian_guard
- same_realm_as
- already_have_a_claim_on_this_title
- already_have_claims_on_all_titles
- literalist_debate_interaction_has_been_debated
- literalist_debate_timing
- sumptuary_debate_has_been_debated
- sumptuary_debate_timing
- is_already_in_all_wars
- is_character_interaction_valid
- is_character_interaction_potentially_accepted
- TAKE_VOWS_INTERACTION_MARTIAL_EDUCATION
- fp1_tbc_no_available_champions
- fp1_tbc_recipient_banned_from_combat
- banned_from_combat_old_and_frail
- steal_back_artifact_must_have_claim_blocker
- need_non_house_head_hook
- need_non_best_friend_hook
- not_enough_stress
- challenge_for_artifact_interaction_valid_tt_1
- challenge_for_artifact_interaction_valid_tt_2
- challenge_for_artifact_interaction_valid_tt_3
- demand_artifact_interaction_is_valid_tt_2
- demand_artifact_interaction_valid_tt_1
- county_must_have_city
- county_must_have_culture
- must_be_one_county_count
- must_not_have_landed_relatives
- must_not_be_heir_to_any_title
- too_many_republics
- foreign_prison_revocation
- recent_conversion_to_tribalism
- gift_artifact_dynasty_banner_head_tt
- any_unequipped_artifact_tt
- demand_dynasty_banner_artifact_tt
- baron_revocation
- prisoner_revocation
- synergise_friendship_interaction_cannot_share_education
- target_has_your_faith
- you_must_not_have_a_claim_on_the_title
- basic_valid_hostage_to_offer
- basic_valid_hostage_to_demand
- hostage_oath_of_friendship_trigger
- vassal_has_the_wrong_faith
- vassal_has_the_wrong_religion
- vassal_is_not_far_enough
- influence_child_personality_interaction_trait_limit
- revoke_title_not_noble_family_title
- influence_child_personality_interaction_all_same_traits
- influence_child_commander_interaction_all_same_traits
- hof_ask_for_claim_on_admin_titles
- steal_herd_blocked_target_none_tt
- liege_demands_vow_taking
- grant_government_too_many_theocratic_vassals_tt
- grant_government_cooldown_tt
- grant_government_kingdom_blocked_tt
- grant_government_nomad_settled_only_tt

### 01_decision_triggers.txt（70 条目）

- create_cadet_branch_decision_succession_line
- create_cadet_branch_decision_ancestor_in_house
- is_king_or_emperor
- has_two_castle_county
- has_holy_order_barony_selected
- has_holy_order_county_selected
- reclaim_britannia_decision_custom
- accept_cannibalism_decision_custom
- capital_province_in_ganges_region
- my_vassal_or_liege_is_ruler_of_ganges
- under_outremer_liege
- under_outremer_empire
- commission_epic_potential_cost_effect
- has_count_vassals_or_higher
- capital_in_england_region_tooltip
- reclaim_britannia_custom_decision
- greatest_of_khans_title_tier_requirement
- send_child_to_university_province_condition
- send_child_to_university_university_condition
- has_pilgrimage_cooldown
- borrow_from_holy_order_gold_condition
- found_kingdom_decision_advanced_succesion
- found_kingdom_decision_elective_succesion
- no_built_university
- is_head_of_religion
- grant_titles_interaction_can_only_give_diarch_de_jure_liege_to_diarch
- grant_titles_interaction_children_not_allowed_temple
- grant_titles_interaction_title_being_wagered
- deceitful_progress_hostile_schemes_decision_missing_scheme
- impatient_rushing_all_schemes_decision_missing_scheme
- promote_hungarian_settlement_decision_ecumenical_christian
- launch_hungarian_migration_decision_before_last_date
- unite_the_spanish_thrones_decision_primary
- divine_the_stars_trigger
- cannot_be_atoned_krstjani_leader_flag
- negotiate_the_danelaw.valid_opponent.tt
- negotiate_the_danelaw.controlled_duchies.tt
- negotiate_the_danelaw_integrate_duchies_decision.duchies_within_danelaw.tt
- negotiate_the_danelaw_integrate_duchies_decision.duchies_within_england.tt
- formalise_the_daneland_decision.must_be_after_1100.tt
- decision_refound_hre_own_three_kingdoms.tt
- secure_high_kingdom_north_sea_decision_solve_danelaw
- secede_from_empire_decision_trigger_debt
- secede_from_empire_decision_trigger_war
- raise_stele_decision_ancestor
- raise_stele_decision_victory
- raise_stele_decision_rank
- forge_the_jomsvikings_decision.tt.empty_castle_or_city
- forge_the_jomsvikings_decision.tt.is_in_correct_region
- found_capital_of_the_rus_decision_before_last_date
- unite_the_western_slavs_decision_tt_1
- unite_the_western_slavs_decision_tt_2
- restore_roman_empire_decision_tt
- exoticise_a_grand_hall_decision.tt.any_valid_hegemny
- exoticise_a_grand_hall_decision.tt.any_valid_empire
- exoticise_a_grand_hall_decision.tt.any_valid_kingdom
- court_already_has_a_fashion_tend_tt
- favour_the_countryside_basques_decision.have_sinful_piety_level
- favour_the_countryside_basques_decision.you_have_x_or_more_traits_virtuous_to_basque_paganism
- favour_the_countryside_basques_decision.completely_control_X_counties_from_old_vasconia
- favour_the_countryside_basques_decision.before_last_date
- canarias_must_be_developed_tt
- canarias_must_be_filled_tt
- at_least_10_jewish_counties_tt
- lackluster_diet_hindrance_desc
- create_cadet_branch_decision_in_another_realm
- harrying_ended_tooltip
- high_pacification_tooltip
- hasan_stroy_cycle_camp_at_foe_realm
- has_locations_to_map_tt

### 01_fp1_achievement_triggers.txt（10 条目）

- far_from_home_achievement_trigger
- miklagardariki_achievement_trigger
- canute_the_greater_achievement_trigger
- king_of_all_the_isles_achievement_trigger
- faster_than_the_fox_achievement_trigger
- volva_achievement_trigger
- saga_in_stone_achievement_trigger
- first_of_the_crusader_kings_achievement_trigger
- fans_of_ibn_fadlan_achievement_trigger
- a_dangerous_business_achievement_trigger

### 02_ep1_achievement_triggers.txt（20 条目）

- patronage_achievement_trigger
- converging_paths_achievement_trigger
- changing_course_achievement_trigger
- hoarder_achievement_trigger
- creme_de_la_creme_achievement_trigger
- polyglot_achievement_trigger
- inspirational_achievement_trigger
- one_of_a_kind_achievement_trigger
- true_tolerance_achievement_trigger
- delusions_of_grandeur_achievement_trigger
- bod_chen_po_achievement_trigger
- turkish_eagle_achievement_trigger
- rise_of_the_ghurids_achievement_trigger
- brave_and_bold_achievement_trigger
- lingua_franca_achievement_trigger
- beta_israel_achievement_trigger
- they_belong_in_a_museum_achievement_trigger
- i_made_this_achievement_trigger
- nobody_comes_to_fika_achievement_trigger
- the_true_royal_court_achievement_trigger

### 02_ep1_royal_court_triggers.txt（19 条目）

- can_sponsor_own_inspiration
- can_sponsor_inspiration_already_sponsor
- amenity_level
- amenity_level_greater_or_equal
- amenity_level_less_than
- average_amenity_level
- average_amenity_level_greater_or_equal
- average_amenity_level_less_than
- court_grandeur_current_level
- cultural_acceptance
- cultural_acceptance_greater_or_equal
- cultural_acceptance_less_than
- culture_age
- culture_age_greater_or_equal
- culture_age_less_than
- has_pending_court_events
- has_spawned_court_events
- AT_LEAST_ONE_GUEST_TRIGGER
- AT_LEAST_ONE_UNIMPORTANT_COURTIER_TRIGGER

### 03_fp2_struggle_triggers.txt（15 条目）

- is_culture_involved_in_struggle
- is_faith_involved_in_struggle
- is_struggle_phase
- is_struggle_type
- empty_spooky_trigger
- appoint_a_righteous_caliph_decision.need_at_least_ten_same_faith_counties
- appoint_a_righteous_caliph_decision.cant_be_caliphal_controller
- appoint_a_righteous_caliph_decision.no_more_than_x_sinful_traits
- appoint_a_righteous_caliph_decision.caliph_not_in_diplo_range
- appoint_a_righteous_caliph_decision.control_one_holy_site
- appoint_a_righteous_caliph_decision.control_two_holy_sites
- appoint_a_righteous_caliph_decision.caliph_has_x_or_more_traits_sinful_to_your_faith
- appoint_a_righteous_caliph_decision.has_wishes_to_schism_caliphate_flag
- fp2_bg_recipient_banned_from_board_games
- at_least_one_county_with_neutral_negative_opinion

### 04_ep2_diarchy_triggers.txt（18 条目）

- has_diarchy_active_parameter
- has_diarchy_parameter
- diarchy_swing_greater_than
- is_diarchy_successor
- has_active_diarchy
- is_diarch_of_target
- is_diarch
- strife_opinion
- years_in_diarchy
- years_as_diarch
- has_active_mandate
- mandate_type_qualification
- diarch_aptitude
- diarch_loyalty
- is_designated_diarch
- time_after_designated_diarch
- has_diarchy_type
- diarch_interactions_tt_is_able

### 04_fp3_struggle_triggers.txt（4 条目）

- fp3_install_loyalist_cb_cooldown_trigger_desc
- fp3_please_dont_give_me_negative_gold
- generic_is_not_part_of_same_struggle_desc
- fp3_is_involved_in_struggle_trigger

### 05_ep2_achievement_triggers.txt（60 条目）

- the_grandest_tour_achievement_trigger
- your_eternal_reward_achievement_trigger
- imperial_march_achievement_trigger
- black_dinner_achievement_trigger
- there_and_back_again_achievement_trigger
- the_very_best_achievement_trigger
- like_no_one_ever_was_achievement_trigger
- a_thousand_and_one_nights_achievement_trigger
- a_knights_tale_achievement_trigger
- hunting_accident_achievement_trigger
- lions_and_tigers_and_bears_oh_my_achievement_trigger
- fly_my_pretty_achievement_trigger
- pathway_to_heaven_achievement_trigger
- sir_lance_a_lot_achievement_trigger
- im_in_my_elements_achievement_trigger
- ahab_achievement_trigger
- little_william_marshal_achievement_trigger
- a_true_and_perfect_knight_achievement_trigger
- a_e_i_o_u_and_me_achievement_trigger
- the_iron_and_golden_king_achievement_trigger
- the_old_man_of_the_mountain_achievement_trigger
- band_of_brothers_trigger
- mio_cid_achievement_trigger
- birthright_achievement_trigger
- historically_inaccurate_achievement_trigger
- quantum_leap_achievement_trigger
- kingdom_of_heaven_achievement_trigger
- new_management_achievement_trigger
- rags_to_riches_to_rags_to_riches_achievement_trigger
- tamar_mepe_achievement_trigger
- despoiler_of_byzantium_achievement_trigger
- chaos_is_a_ladder_achievement_trigger
- epic_paperwork_achievement_trigger
- against_the_odds_achievement_trigger
- in_good_estate_achievement_trigger
- i_got_a_permit_achievement_trigger
- despotic_achievement_trigger
- byzywork_achievement_trigger
- not_content_to_serve_achievement_trigger
- started_from_the_bottom_now_were_ere_achievement_trigger
- ep4_01_fishing_in_china_achievement_trigger
- ep4_02_the_heavenly_kingdom_achievement_trigger
- ep4_03_sword_of_japan_achievement_trigger
- ep4_04_a_living_god_on_earth_achievement_trigger
- ep4_05_grand_governor_achievement_trigger
- ep4_06_mandate_of_heaven_achievement_trigger
- ep4_07_cut_off_the_head_and_the_body_will_follow_achievement_trigger
- ep4_08_shogun_achievement_trigger
- ep4_09_devaraja_achievement_trigger
- ep4_10_confucian_scholar_achievement_trigger
- ep4_11_bloc_politics_achievement_trigger
- ep4_12_upper_upper_achievement_trigger
- ep4_13_how_its_done_done_done_achievement_trigger
- ep4_14_daits_how_you_do_it_achievement_trigger
- ep4_15_humble_beginnings_achievement_trigger
- ep4_16_flying_colors_achievement_trigger
- ep4_17_highway_of_ideas_achievement_trigger
- ep4_18_yes_i_need_my_samurai_achievement_trigger
- ep4_19_stamp_of_approval_achievement_trigger
- ep4_20_promised_land_achievement_trigger

### 06_bp2_hostage_triggers.txt（10 条目）

- is_hostage
- is_hostage_warden
- has_away_hostages
- is_hostage_of
- is_hostage_from
- was_hostage_child
- hostage_duration
- hostage_already_travelling_tt
- rites_of_passage_trigger_not_proven
- rites_of_passage_trigger_delayed

### 07_ce1_achievement_triggers.txt（11 条目）

- ce1_not_today_achievement_trigger
- ce1_divine_right_achievement_trigger
- ce1_youll_never_take_me_alive_achievement_trigger
- ce1_the_pharaoh_islands_achievement_trigger
- ce1_canonized_achievement_trigger
- ce1_upward_mobility_achievement_trigger
- ce1_cant_touch_this_achievement_trigger
- ce1_legendary_achievement_trigger
- ce1_f_achievement_trigger
- ce1_local_legend_achievement_trigger
- ce1_neverending_story_achievement_trigger

### 08_ep3_admin_triggers.txt（3 条目）

- cabinet_of_curiosities_upgrade_trigger_2
- cabinet_of_curiosities_upgrade_trigger_3
- admin_cannot_grant_vassal_noble_family

### 08_ep3_laamp_triggers.txt（32 条目）

- purchase_land_barony_tt
- purchase_land_kingdom_tt
- purchase_land_religious_tt
- purchase_land_noble_family_tt
- purchase_land_landless_adventurer_tt
- purchase_land_minimum_county_tt
- purchase_land_complete_control_tt
- negotiate_settlement_barony_tt
- negotiate_settlement_kingdom_tt
- negotiate_settlement_religious_tt
- negotiate_settlement_noble_family_tt
- negotiate_settlement_landless_adventurer_tt
- negotiate_settlement_minimum_county_tt
- any_character_task_contract
- has_task_contract_type
- contact_list_request_interaction_create_contracts
- treasure_hunting_contract_decision_limit
- decision_already_visiting_local_settlement
- visit_local_settlement_decision_sieged
- ep3_laamp_diplo_range_trigger_tt
- not_have_master_of_arms_building
- not_have_armorer_building
- provision_cost_to_owner
- provisions_greater_or_equal
- provision_cost_to_domicile
- decision_already_excavating_treasure
- adventurer_not_famous_trigger_tt
- adventurer_not_famous_or_patron_trigger_tt
- adventurer_employer_is_duke_or_above_trigger_tt
- is_contact_of
- procure_estate_low_rank_tt
- procure_estate_at_war_tt

### 09_mpo_achievement_triggers.txt（10 条目）

- mpo_the_stallion_that_mounts_the_world_achievement_trigger
- mpo_nobodys_business_achievement_trigger
- mpo_tribute_band_achievement_trigger
- mpo_this_chinggis_everything_achievement_trigger
- mpo_steppe_by_steppe_achievement_trigger
- mpo_in_xanadu_achievement_trigger
- mpo_settling_in_achievement_trigger
- mpo_blood_of_my_blood_achievement_trigger
- mpo_confedup_achievement_trigger
- mpo_shut_up_nerge_achievement_trigger

### 09_mpo_triggers.txt（3 条目）

- blood_brother_memory_trigger
- blood_brother_former_war_allies_trigger
- blood_brother_common_enemy_trigger

### 10_ce3_achievement_triggers.txt（10 条目）

- ce3_04_the_two_swords_achievement_trigger
- ce3_02_guidos_guiding_light_achievement_trigger
- ce3_11_servus_servorum_dei_achievement_trigger
- ce3_12_papal_bull_achievement_trigger
- ce3_07_the_father_the_son_and_the_holy_grandson_achievement_trigger
- ce3_13_where_theres_a_will_achievement_trigger
- ce3_14_home_see_advantage_achievement_trigger
- ce3_15_cardinal_sin_achievement_trigger
- ce3_06_fathers_best_side_achievement_trigger
- ce3_16_holier_than_thou_achievement_trigger

### ce1_legend_triggers.txt（2 条目）

- has_personal_legend_seed
- has_triggered_legend_seed

### tgp_triggers.txt（12 条目）

- participant_group_has_character
- is_any_movement_leader_tt
- top_participant_group_equal
- tgp_is_hegemon_or_below_in_dynastic_cycle_trigger_tt
- grand_campaign_target_border_tt
- conservative_powerful_families_tt
- conservative_ministers_tt
- not_conservative_powerful_families_tt
- not_conservative_ministers_tt
- target_is_not_war_leader
- target_is_a_minister_desc
- participant_group_type

### 未解析文件

- `_trigger_localization.info` — 纯文档（非 Jomini）
