# common/messages 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：43（其中 Jomini 解析 42 个）
- 顶层块条目总数：728，跨文件唯一条目 728
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_messages.txt` | 5631 | 26 | 5 | jomini |
| `01_activity_messages.txt` | 2261 | 11 | 0 | jomini |
| `01_alliance_messages.txt` | 3120 | 19 | 0 | jomini |
| `01_artifact_messages.txt` | 1936 | 10 | 0 | jomini |
| `01_character_messages.txt` | 4256 | 27 | 0 | jomini |
| `01_childhood_messages.txt` | 1751 | 9 | 0 | jomini |
| `01_council_messages.txt` | 6410 | 33 | 0 | jomini |
| `01_court_messages.txt` | 5415 | 31 | 0 | jomini |
| `01_court_position_messages.txt` | 1651 | 9 | 0 | jomini |
| `01_culture_messages.txt` | 1498 | 10 | 0 | jomini |
| `01_currency_messages.txt` | 702 | 3 | 0 | jomini |
| `01_death_messages.txt` | 2012 | 10 | 0 | jomini |
| `01_diarch_messages.txt` | 3318 | 16 | 1 | jomini |
| `01_domain_messages.txt` | 1854 | 8 | 1 | jomini |
| `01_dynasty_messages.txt` | 7067 | 41 | 0 | jomini |
| `01_faction_messages.txt` | 2829 | 17 | 0 | jomini |
| `01_family_messages.txt` | 1396 | 7 | 0 | jomini |
| `01_hook_messages.txt` | 1131 | 8 | 0 | jomini |
| `01_interaction_messages.txt` | 356 | 2 | 0 | jomini |
| `01_law_messages.txt` | 1107 | 8 | 0 | jomini |
| `01_marriage_messages.txt` | 1652 | 12 | 0 | jomini |
| `01_multiplayer_messages.txt` | 686 | 3 | 0 | jomini |
| `01_relationship_messages.txt` | 2154 | 10 | 0 | jomini |
| `01_religious_messages.txt` | 8639 | 49 | 0 | jomini |
| `01_scheme_messages.txt` | 5602 | 32 | 0 | jomini |
| `01_secret_messages.txt` | 1168 | 5 | 0 | jomini |
| `01_skill_messages.txt` | 5892 | 33 | 0 | jomini |
| `01_struggle_messages.txt` | 1939 | 10 | 0 | jomini |
| `01_title_messages.txt` | 1792 | 12 | 0 | jomini |
| `01_travel_messages.txt` | 927 | 4 | 0 | jomini |
| `01_vassal_messages.txt` | 2336 | 12 | 0 | jomini |
| `01_war_messages.txt` | 11792 | 73 | 0 | jomini |
| `02_ep1_messages.txt` | 609 | 2 | 0 | jomini |
| `04_ep2_messages.txt` | 2245 | 11 | 0 | jomini |
| `04_fp3_messages.txt` | 785 | 3 | 0 | jomini |
| `05_bp2_messages.txt` | 882 | 4 | 0 | jomini |
| `06_ce1_messages.txt` | 2070 | 12 | 0 | jomini |
| `07_ep3_messages.txt` | 12507 | 63 | 1 | jomini |
| `09_mpo_messages.txt` | 2737 | 12 | 0 | jomini |
| `10_pam_messages.txt` | 4146 | 17 | 0 | jomini |
| `_messages.info` | 3485 | - | - | 纯文档（非 Jomini） |
| `passive_rite_learning_messages.txt` | 884 | 4 | 0 | jomini |
| `tgp_messages.txt` | 8156 | 40 | 1 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_messages.txt（26 条目）

- msg_custom_player_message
- event_generic_bad
- event_generic_bad_text
- event_generic_good
- event_generic_good_text
- event_generic_neutral
- event_generic_neutral_text
- event_generic_bad_with_text
- event_generic_neutral_with_text
- event_generic_good_with_text
- send_interface_message
- send_interface_message_good
- send_interface_message_bad
- send_interface_message_as_toast
- send_interface_message_as_popup
- event_toast_effect_good
- event_toast_effect_neutral
- event_toast_effect_bad
- event_toast_text_good
- event_toast_text_and_effect_good
- event_toast_text_neutral
- event_toast_text_and_effect_neutral
- event_toast_text_bad
- event_toast_text_and_effect_bad
- msg_event_timeout
- msg_letter_event_timeout

### 01_activity_messages.txt（11 条目）

- msg_tournament_knight_arrives
- toast_tournament_arrival_prestige
- toast_tournament_contest_reward
- toast_tournament_marriage_prize
- toast_tournament_qualifying
- toast_tournament_not_qualifying
- toast_tournament_qualification_champion
- toast_tournament_qualification_knight
- event_activity_good_with_text
- event_activity_bad_with_text
- event_chariot_race_sow_discord

### 01_alliance_messages.txt（19 条目）

- msg_alliance
- msg_broken_alliance
- msg_expired_alliance
- msg_expired_alliance_ally_death
- msg_alliance_became_landed
- msg_alliance_became_unlanded
- msg_broken_confederation
- msg_joined_confederation
- msg_joined_house_bloc
- msg_house_joined_house_bloc
- msg_left_house_bloc
- msg_house_left_house_bloc
- msg_house_bloc_created
- msg_house_bloc_disbanded
- msg_house_bloc_destroyed
- msg_house_bloc_leader
- msg_house_bloc_cohesion_change_good
- msg_house_bloc_cohesion_change_neutral
- msg_house_bloc_cohesion_change_bad

### 01_artifact_messages.txt（10 条目）

- msg_artifact_claim_gained
- msg_artifact_claim_lost
- msg_artifact_gained
- msg_artifact_lost
- event_artifact_good_with_text
- event_artifact_good_text
- event_artifact_good
- event_artifact_bad_with_text
- event_artifact_bad_text
- event_artifact_bad

### 01_character_messages.txt（27 条目）

- msg_perk_point_added
- msg_focus_invalidated
- msg_gain_nickname
- msg_lost_nickname
- msg_character_level_increase
- msg_character_level_decrease
- msg_gained_stress_level
- msg_lost_stress_level
- msg_gain_trait
- msg_lose_trait
- msg_becomes_obese
- msg_becomes_malnourished
- msg_stops_being_obese
- msg_stops_being_malnourished
- msg_health_change
- msg_new_heir
- msg_new_heir_newborn
- msg_new_heir_old_heir_dead
- msg_no_new_heir
- msg_no_new_heir_old_heir_dead
- event_trait_good
- event_trait_neutral
- event_trait_bad
- secondary_character_stress_good
- event_stress_good
- event_stress_neutral
- event_stress_bad

### 01_childhood_messages.txt（9 条目）

- event_childhood_good
- event_childhood_good_text
- event_childhood_good_with_text
- event_childhood_bad
- event_childhood_bad_text
- event_childhood_bad_with_text
- event_childhood_neutral
- event_childhood_neutral_text
- event_childhood_neutral_with_text

### 01_council_messages.txt（33 条目）

- msg_council_task_finished
- msg_council_task_finished_location
- msg_invalidation_of_council_task
- msg_chancellor_task_bad
- msg_chancellor_task_good
- msg_marshal_task_bad
- msg_marshal_task_good
- msg_steward_task_bad
- msg_steward_task_good
- msg_spymaster_task_bad
- msg_spymaster_task_good
- msg_court_chaplain_task_bad
- msg_court_chaplain_task_good
- msg_kurultai_task_bad
- msg_kurultai_task_good
- msg_spouse_task_bad
- msg_spouse_task_good
- msg_spouse_patronage
- msg_fired_from_council
- msg_council_swap_position
- msg_left_council_position
- event_chancellor_bad
- event_chancellor_good
- event_marshal_bad
- event_marshal_good
- event_steward_bad
- event_steward_good
- event_spymaster_bad
- event_spymaster_good
- event_court_chaplain_bad
- event_court_chaplain_good
- event_spouse_bad
- event_spouse_good

### 01_court_messages.txt（31 条目）

- character_preparing_to_leave
- character_has_left
- character_arrived
- msg_notable_guest
- msg_courtier_child_of_age
- msg_court_inspiration
- msg_court_inspiration_neutral
- msg_court_language
- msg_court_grandeur_good
- msg_court_grandeur_bad
- event_royal_court_good_with_text
- event_royal_court_good_text
- event_royal_court_good
- event_royal_court_neutral_with_text
- event_royal_court_neutral_text
- event_royal_court_neutral
- event_royal_court_bad_with_text
- event_royal_court_bad_text
- event_royal_court_bad
- event_language_good
- event_language_neutral
- event_language_bad
- event_prison_good
- event_prison_neutral
- event_prison_bad
- event_knight_good
- event_knight_neutral
- event_knight_bad
- event_guest_good
- event_guest_neutral
- event_guest_bad

### 01_court_position_messages.txt（9 条目）

- msg_court_position_gained
- msg_court_position_removed
- msg_court_position_invalidated_employee
- msg_court_position_invalidated_employer
- msg_court_position_invalidated_and_replaced_employer
- event_court_physician_bad
- event_court_physician_good
- event_champion_neutral
- event_bodyguard_neutral

### 01_culture_messages.txt（10 条目）

- msg_culture_conversion
- msg_new_fascination_selected
- msg_innovation_discovered
- msg_fascination_discovered
- msg_era_discovered
- msg_first_era_discovered
- msg_no_longer_culture_head
- msg_become_culture_head
- msg_culture_hybridized
- msg_culture_tradition_change

### 01_currency_messages.txt（3 条目）

- event_gold_bad
- event_gold_neutral
- event_gold_good

### 01_death_messages.txt（10 条目）

- family_has_died
- councillor_has_died
- prisoner_has_died
- friend_has_died
- elder_has_died
- lover_has_died
- notable_has_died
- event_death_bad
- event_death_neutral
- event_death_good

### 01_diarch_messages.txt（16 条目）

- msg_diarch_acting_effect
- msg_diarch_acting_text_and_effect
- msg_mandate_results_good_effect
- msg_mandate_results_good_text_and_effect
- msg_mandate_results_bad_effect
- msg_mandate_results_bad_text
- msg_mandate_results_bad_text_and_effect
- msg_mandate_results_neutral_effect
- msg_mandate_results_neutral_text
- msg_mandate_results_neutral_text_and_effect
- msg_start_diarchy
- msg_inherit_diarchy
- msg_end_diarchy
- msg_change_diarchy_type
- msg_diarchy_more_power
- msg_diarchy_less_power

### 01_domain_messages.txt（8 条目）

- msg_county_corruption_bad
- msg_county_corruption_good
- msg_county_corruption_good_increase_control
- msg_building_done
- event_domain_good
- event_domain_good_with_text
- event_domain_bad
- event_domain_bad_with_text

### 01_dynasty_messages.txt（41 条目）

- msg_cadet_branch_created
- msg_created_new_house
- msg_i_became_dynast
- msg_i_not_dynast_anymore
- msg_became_dynast
- msg_dynasty_child_of_age
- msg_child_of_age
- msg_dynasty_perk_added
- msg_dynasty_perk_removed
- msg_dynasty_prestige_level_increase
- msg_dynasty_prestige_level_dencrease
- msg_i_became_head_of_house
- msg_i_not_head_of_house_anymore
- msg_became_head_of_house
- msg_new_powerful_family
- msg_new_noble_family
- house_feud_begins_message
- house_feud_reciprocated_message
- house_feud_ends_message
- house_feud_continues_message
- house_feud_kill_bad_message
- house_feud_kill_good_message
- house_feud_torture_bad_message
- house_feud_torture_good_message
- house_feud_cuckolded_bad_message
- house_feud_cuckolded_good_message
- house_feud_avenged_bad_message
- house_feud_avenged_good_message
- house_feud_war_good_message
- house_feud_war_bad_message
- house_feud_white_peace_message
- house_feud_stole_artifact_bad_message
- house_feud_stole_artifact_good_message
- msg_house_unity_change_stage
- msg_house_unity_change_value
- event_dynasty_good
- event_dynasty_good_with_text
- event_dynasty_neutral
- event_dynasty_neutral_with_text
- event_dynasty_bad
- event_dynasty_bad_with_text

### 01_faction_messages.txt（17 条目）

- msg_disbanded_faction_target_died
- msg_removed_from_faction_not_valid
- msg_removed_from_faction_not_valid_leader
- msg_removed_from_faction_not_liege
- msg_faction_against_liege_created
- msg_faction_against_me_created
- msg_faction_grows
- msg_county_faction_against_liege_created
- msg_county_faction_against_me_created
- msg_faction_against_me_disbanded
- msg_faction_local_not_leader_anymore
- msg_faction_local_becomes_leader
- msg_faction_forced_to_join
- msg_my_faction_disbanded
- event_faction_good_text
- event_faction_neutral
- event_faction_neutral_text

### 01_family_messages.txt（7 条目）

- msg_family_became_concubine
- msg_child_born_toast
- msg_grandchild_born_toast
- msg_royal_child_born_toast
- msg_child_language
- msg_child_faith
- msg_known_pregnancy

### 01_hook_messages.txt（8 条目）

- msg_my_hook_replaced
- msg_my_hook_added
- msg_hook_on_me_replaced
- msg_hook_on_me_added
- msg_hook_on_me_expired
- msg_my_hook_expired
- event_hook_bad
- event_hook_good

### 01_interaction_messages.txt（2 条目）

- interaction_prison_single_side
- interaction_prison_ransom

### 01_law_messages.txt（8 条目）

- msg_liege_passed_law
- msg_liege_changed_budget_law
- msg_liege_passed_title_law
- msg_liege_removed_title_law
- msg_law_invalidated
- msg_law_invalidated_no_new_law
- msg_realm_law_changed
- msg_government_changed

### 01_marriage_messages.txt（12 条目）

- msg_marriage
- msg_betrothal_invalidated
- msg_break_betrothal
- msg_betrothal_invalidated_player_heir
- msg_break_betrothal_player_heir
- msg_betrothal_fulfilled
- msg_divorce
- msg_divorce_player_heir
- msg_spouse_invalidated
- msg_spouse_invalidated_player_heir
- msg_marriage_forced
- msg_consort_invalidated

### 01_multiplayer_messages.txt（3 条目）

- msg_player_character_changed
- msg_player_new_character
- msg_player_new_observer

### 01_relationship_messages.txt（10 条目）

- msg_set_relation_friend
- msg_set_relation_best_friend
- msg_set_relation_rival
- msg_set_relation_nemesis
- msg_set_relation_grudge
- msg_set_relation_lover
- msg_set_relation_soulmate
- msg_set_relation_blood_brother
- msg_set_relation_disciple
- msg_set_relation_elder

### 01_religious_messages.txt（49 条目）

- excommunicated_other_message
- event_heresy_outbreak_neutral
- event_heresy_outbreak_bad
- event_heresy_outbreak_good
- event_hof_established
- msg_i_became_head_of_faith
- msg_i_became_head_of_multiple_faiths
- msg_i_not_head_of_faith_anymore
- msg_i_not_head_of_multiple_faiths_anymore
- msg_holy_site_created
- msg_holy_site_created_by_character
- msg_holy_site_adopted
- msg_holy_site_adopted_by_character
- msg_holy_site_elevated
- msg_holy_site_elevated_by_character
- msg_holy_site_demoted
- msg_holy_site_demoted_by_character
- msg_holy_site_abandoned
- msg_holy_site_abandoned_by_character
- holy_order_founded_message
- monastic_holy_order_founded_message
- enemy_holy_order_founded_message
- holy_order_expanded_message
- monastic_holy_order_expanded_message
- holy_order_hired_message
- holy_order_hired_by_enemy_message
- holy_order_lease_revoked_message
- msg_holy_order_dismissed
- msg_holy_order_patronage_lost
- msg_holy_order_patronage_gained
- msg_holy_order_destroyed
- msg_new_theocracy_lesee_approve
- msg_new_theocracy_lesee_disapprove
- event_great_holy_war_good_message
- great_holy_war_bad_message
- msg_council_conversion_bad
- msg_council_conversion_neutral
- msg_council_conversion_good
- msg_rite_updated
- event_bishop_good
- event_bishop_bad
- event_religious_good
- event_religious_good_text
- event_religious_good_with_text
- event_religious_bad
- event_religious_bad_with_text
- event_religious_bad_text
- event_religious_neutral_text
- event_religious_neutral

### 01_scheme_messages.txt（32 条目）

- sway_good_message
- sway_bad_message
- fabricate_hook_bad_message
- fabricate_hook_invalidated_message
- abduct_invalidated_i_imprisoned_message
- murder_invalidated_message
- murder_agent_join_or_leave_message
- msg_scheme_froze
- msg_scheme_froze_until
- diplo_contract_scheme_invalidated_message
- martial_contract_scheme_invalidated_message
- stewardship_contract_scheme_invalidated_message
- intrigue_contract_scheme_invalidated_message
- learning_contract_scheme_invalidated_message
- msg_promoted_scheme
- msg_legitimacy_fostered_scheme
- msg_legitimacy_damaged_scheme
- msg_scheme_abandoned
- msg_agent_joined_my_scheme
- msg_agent_removed_my_scheme
- msg_2_agents_removed_my_scheme
- msg_multiple_agents_removed_my_scheme
- msg_scheme_opportunity_threshold
- msg_countermeasure_change
- mentoring_scheme_good_message
- mentoring_scheme_bad_message
- study_scheme_good_message
- study_scheme_bad_message
- siphon_scheme_good_message
- siphon_scheme_bad_message
- event_sway_neutral
- event_scheme_bad

### 01_secret_messages.txt（5 条目）

- secret_exposed_message
- secret_discovered_message
- event_witchcraft_good
- event_witchcraft_neutral
- event_witchcraft_bad

### 01_skill_messages.txt（33 条目）

- event_diplomacy_bad
- event_diplomacy_good
- event_diplomacy_neutral
- event_diplomacy_bad_with_text
- event_diplomacy_good_with_text
- event_diplomacy_neutral_with_text
- event_martial_bad
- event_martial_good
- event_martial_bad_with_text
- event_martial_good_with_text
- event_martial_text_good
- event_stewardship_bad
- event_stewardship_bad_with_text
- event_stewardship_neutral
- event_stewardship_neutral_with_text
- event_stewardship_good
- event_stewardship_good_with_text
- event_intrigue_bad
- event_intrigue_good
- event_intrigue_bad_with_text
- event_intrigue_good_with_text
- event_intrigue_neutral
- event_learning_bad
- event_learning_good
- event_learning_bad_with_text
- event_learning_good_with_text
- event_prowess_bad
- event_prowess_good
- event_prowess_bad_with_text
- event_prowess_good_with_text
- event_prowess_good_desc
- event_prowess_bad_desc
- event_prowess_neutral

### 01_struggle_messages.txt（10 条目）

- msg_struggle_phase_end
- msg_struggle_phase_transitioned
- msg_catalyst_triggered
- msg_catalyst_triggered_no_character
- event_struggle_good
- event_struggle_good_with_text
- event_struggle_bad
- event_struggle_bad_with_text
- event_struggle_neutral
- event_struggle_neutral_with_text

### 01_title_messages.txt（12 条目）

- msg_title_rank_up
- msg_title_rank_down
- msg_change_primary
- msg_inherited_single_title
- msg_inherited_titles
- msg_lost_single_title
- msg_lost_titles
- msg_accomplice_gained_title
- msg_accomplice_denied_title
- event_title_good
- event_title_bad
- msg_cleric_support_title_gain

### 01_travel_messages.txt（4 条目）

- event_travel_good
- event_travel_good_with_text
- event_travel_bad
- event_travel_bad_with_text

### 01_vassal_messages.txt（12 条目）

- msg_vassal_contract_level_invalidated
- msg_vassal_contract_2_levels_invalidated
- msg_vassal_contract_multiple_levels_invalidated
- msg_vassal_contract_change
- msg_gained_independence
- msg_liege_changed
- msg_liege_ceded_title
- msg_liege_gained_title
- msg_pledged_loyalty_to_liege
- msg_refused_pledge_loyalty_to_liege
- msg_vassal_decision_good
- msg_tributary_invalidated

### 01_war_messages.txt（73 条目）

- msg_war_ally_joined
- msg_war_ally_joined_multiple
- msg_war_ally_removed
- msg_war_ally_removed_multiple
- msg_war_ally_replaced
- msg_war_ally_transferred
- msg_war_enemy_new_ally
- msg_war_enemy_joined
- msg_war_enemy_joined_multiple
- msg_war_enemy_removed
- msg_war_enemy_removed_multiple
- msg_war_enemy_replaced
- msg_war_enemy_transferred
- msg_war_player_joined
- msg_war_player_removed
- msg_war_player_replaced
- msg_war_player_transferred
- event_war_invalidated
- msg_war_casus_belli_changed
- msg_war_declared_on_me
- msg_war_declared_on_vassal
- msg_war_declared_on_tributary
- msg_tributary_declared_war_on_tributary
- msg_war_declared_on_suzerain
- msg_war_declared_on_liege
- msg_war_declared_by_liege
- msg_liege_war_ended_attacker_win
- msg_liege_war_ended_defender_win
- msg_liege_war_ended_white_peace
- msg_liege_war_ended_invalid
- msg_war_ended_invalid
- msg_war_ended_neighbor
- msg_tributary_contract_broken_due_to_war
- msg_troops_gained
- msg_troops_disbanding_civil_war
- msg_peace_armies_disbanded
- msg_character_captured_by_me
- msg_character_captured_by_other_side
- event_captured_combatants_good
- event_captured_combatants_neutral
- event_captured_combatants_bad
- event_slain_combatants_good
- event_slain_combatants_neutral
- event_slain_combatants_bad
- msg_mercenary_company_dismissed
- msg_raid_completed
- msg_raid_lost
- msg_raid_intent_invalidated
- msg_barter_completed
- msg_barter_loot_delivered
- msg_barter_loot_lost
- msg_barter_loot_won
- msg_barter_aborted
- msg_siege_won
- msg_siege_loot
- msg_siege_started
- msg_siege_lost_with_text
- msg_siege_piety
- msg_siege_effect
- event_war_bad
- event_war_bad_with_text
- event_war_good
- event_war_good_with_text
- event_truce_bad
- event_truce_bad_with_text
- event_truce_good
- event_truce_good_with_text
- event_truce_neutral
- event_truce_neutral_with_text
- event_raid_good
- event_raid_good_text
- event_raid_bad
- event_raid_bad_text

### 02_ep1_messages.txt（2 条目）

- msg_court_amenity_setting_invalidated
- msg_courtiers_gain_court_traits

### 04_ep2_messages.txt（11 条目）

- msg_accolade_gained_rank
- msg_accolade_lost_rank
- msg_accolade_active
- msg_accolade_succession_toast
- msg_accolade_succession
- event_accolade_good_with_text
- event_accolade_bad_text
- msg_accolade_eligibility
- msg_accolade_squires
- msg_accolade_knight_training
- msg_accolade_merc

### 04_fp3_messages.txt（3 条目）

- event_tax_collector_bad_with_text
- event_tax_collector_good_with_text
- event_tax_collector_good

### 05_bp2_messages.txt（4 条目）

- event_hostage_good
- event_hostage_good_with_text
- event_hostage_bad
- event_hostage_bad_with_text

### 06_ce1_messages.txt（12 条目）

- msg_disease_contraction
- msg_disease_recovery
- msg_epidemic_outbreak
- msg_epidemic_infection
- msg_legitimacy_gain
- msg_legitimacy_loss
- msg_legend_promoter_join
- msg_legend_promoter_leave
- msg_promoted_legend_unowned
- msg_promoted_legend_completed
- msg_legend_library_added
- msg_legend_seed_created

### 07_ep3_messages.txt（63 条目）

- msg_domicile_moved
- msg_domicile_building_started
- msg_domicile_building_cancelled
- msg_domicile_building_completed
- msg_domicile_building_unlocked
- msg_domicile_damaged
- msg_landless_adventurer_battle_gold
- msg_landless_adventurer_nearby
- msg_landless_adventurer_expulsion_consequences
- msg_landless_adventurer_expulsion_consequences_adventurer
- msg_titles_renounced_to_me
- msg_titles_renounced_by_me
- event_landless_adventurer_good
- event_landless_adventurer_good_with_text
- event_landless_adventurer_neutral
- event_landless_adventurer_neutral_with_text
- event_landless_adventurer_bad
- event_landless_adventurer_bad_with_text
- event_camp_follower_with_text
- msg_task_contract_created
- danger_landless_adventurer_bad_with_text
- msg_provincial_army_reassigned
- msg_governance_contracts
- msg_governor_duties
- msg_candidacy_harmed
- msg_candidacy_improved
- msg_governor_candidate_promoted_leading
- msg_governor_candidate_demoted_leading
- msg_governor_challenges_weakness
- msg_unflattering_imperial_trait_gossip
- msg_governor_compliments_legitimacy
- msg_governor_challenging_illegitimacy
- msg_governor_supports_rule
- msg_governor_upset_about_skill
- msg_governor_upset_about_governance
- msg_governor_upset_about_insolvency
- msg_governor_upset_about_bad_govs
- msg_admin_border_change_good_with_text
- msg_admin_border_change_neutral_with_text
- msg_admin_border_change_bad_with_text
- msg_admin_title_gained
- msg_admin_title_gained_foe
- msg_admin_title_lost
- msg_admin_title_lost_foe
- msg_admin_provincial_army_request_accepted
- msg_admin_provincial_army_request_denied
- msg_admin_eparch_with_text_good
- msg_scheme_breached
- msg_frankokratia_crusader_joining
- msg_frankokratia_byz_slaughter
- msg_akolouthos_steels_varangians
- msg_greek_fire_ready
- msg_poem_kept
- msg_contract_completion_reward
- msg_byz_latin_de_jure_switch
- msg_frankokratia_anarchy_end
- msg_frankokratia_former_emp_courtier
- msg_pacification_rise
- msg_resistance_rise
- msg_pacification_falls
- msg_resistance_falls
- msg_peasant_supported
- msg_peasant_controlled

### 09_mpo_messages.txt（12 条目）

- event_raiding_good_with_text
- event_gok_submission_with_text
- msg_gok_slaughter
- msg_gok_destruction
- event_gok_temujin_with_text
- steppe_expansion_happened
- msg_migration_into_realm
- msg_migration_into_neighbour
- msg_tributaries_breaking_free_good
- msg_tributaries_breaking_free_bad
- msg_yurt_yearly_good
- msg_mpo_de_jure_shifting

### 10_pam_messages.txt（17 条目）

- msg_monastic_leader_beatified
- msg_pam_new_saint_canonized
- msg_spiritual_fulfillment_changed
- msg_spiritual_fulfillment_changed_tenet_added
- msg_spiritual_fulfillment_changed_tenet_removed
- msg_pam_rite_growth_spread
- msg_pam_heresy_spread
- msg_clerical_region_liege_change
- msg_clerical_region_independence
- msg_pam_new_archbishop
- msg_pam_new_pope_elected
- msg_clerical_region_conversion_started
- msg_clerical_region_conversion_ended
- msg_ecumenical_council_ruling
- msg_pam_great_schism_progress
- msg_order_espousing_beliefs
- msg_order_took_over_monastery

### passive_rite_learning_messages.txt（4 条目）

- msg_passive_learned_rite
- msg_passive_learned_tenet
- msg_passive_learned_tenet_special
- msg_passive_learned_doctrine

### tgp_messages.txt（40 条目）

- msg_house_relation_level_changed_good
- msg_house_relation_level_changed_neutral
- msg_house_relation_level_changed_bad
- msg_house_relation_ended
- event_tribute_good_text
- event_tribute_good_with_text
- event_tribute_neutral_text
- event_tribute_bad_with_text
- msg_mandala_good_with_text
- msg_mandala_neutral_with_text
- msg_mandala_bad_with_text
- msg_mandala_neutral_text
- msg_mandala_bad
- msg_mandala_creator_birth_good
- event_conversion_good
- event_conversion_bad_text
- msg_natural_disaster_started
- msg_natural_disaster_army_damaged_good
- msg_natural_disaster_army_damaged_bad
- msg_natural_disaster_army_events
- msg_tributary_capital_province_development_growth
- event_msg_merit_effect_good
- event_msg_merit_effect_bad
- msg_mandala_temple_completed_01
- msg_mandala_temple_completed_02up
- msg_mandala_contracts_text_neutral
- msg_great_project_planned
- msg_great_project_started
- msg_great_project_aborted
- msg_great_project_completed
- msg_great_project_contributed
- msg_great_project_reward
- msg_appointed_to_title
- msg_silk_road_prosperity_peace_good
- msg_silk_road_prosperity_war_bad
- msg_silk_road_good
- msg_silk_road_neutral
- msg_silk_road_bad
- msg_silk_road_innovation_movement
- msg_silk_road_innovation_spread

### 未解析文件

- `_messages.info` — 纯文档（非 Jomini）
