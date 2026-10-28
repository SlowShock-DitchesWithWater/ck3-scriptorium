# common/effect_localization 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：37（其中 Jomini 解析 36 个）
- 顶层块条目总数：1017，跨文件唯一条目 1017
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_activity_effects.txt` | 2034 | 8 | 0 | jomini |
| `00_additional_effects.txt` | 7070 | 53 | 0 | jomini |
| `00_ce1_effects.txt` | 763 | 4 | 0 | jomini |
| `00_character_effects.txt` | 64782 | 266 | 0 | jomini |
| `00_council_effects.txt` | 1300 | 12 | 0 | jomini |
| `00_county_effects.txt` | 653 | 4 | 0 | jomini |
| `00_culture_effect.txt` | 3220 | 16 | 0 | jomini |
| `00_custom_effects.txt` | 3395 | 29 | 0 | jomini |
| `00_dynasty_effects.txt` | 1232 | 5 | 0 | jomini |
| `00_faction_effects.txt` | 2201 | 12 | 0 | jomini |
| `00_fp3_effects.txt` | 2404 | 12 | 0 | jomini |
| `00_landed_title_effects.txt` | 1201 | 6 | 0 | jomini |
| `00_legend_effects.txt` | 2900 | 12 | 0 | jomini |
| `00_maa_effects.txt` | 780 | 2 | 0 | jomini |
| `00_perk_effects.txt` | 33577 | 193 | 0 | jomini |
| `00_province_effects.txt` | 1815 | 9 | 0 | jomini |
| `00_religion_effects.txt` | 8339 | 42 | 0 | jomini |
| `00_scheme_effects.txt` | 4989 | 28 | 0 | jomini |
| `00_secret_effects.txt` | 1279 | 8 | 0 | jomini |
| `00_title_effects.txt` | 6495 | 22 | 0 | jomini |
| `00_travel_effects.txt` | 3324 | 16 | 0 | jomini |
| `00_vassal_effects.txt` | 1742 | 4 | 0 | jomini |
| `00_war_effects.txt` | 7093 | 32 | 0 | jomini |
| `01_ep1_effects.txt` | 6704 | 30 | 0 | jomini |
| `01_fp1_effects.txt` | 2012 | 10 | 0 | jomini |
| `02_ep1_effects.txt` | 1244 | 5 | 0 | jomini |
| `03_fp2_effects.txt` | 3271 | 21 | 0 | jomini |
| `04_ep2_diarchy_effects.txt` | 2610 | 10 | 0 | jomini |
| `04_ep2_effects.txt` | 5628 | 17 | 0 | jomini |
| `05_bp2_hostage_effects.txt` | 3257 | 16 | 0 | jomini |
| `07_ep3_effects.txt` | 7528 | 31 | 0 | jomini |
| `08_tgp_effects.txt` | 4122 | 17 | 0 | jomini |
| `09_situation_effects.txt` | 1450 | 5 | 0 | jomini |
| `10_ach_effects.txt` | 271 | 2 | 0 | jomini |
| `10_tgp_effects.txt` | 7802 | 48 | 0 | jomini |
| `_effect_localization.info` | 1221 | - | - | 纯文档（非 Jomini） |
| `pam_effects.txt` | 2027 | 10 | 0 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_activity_effects.txt（8 条目）

- accept_activity_invite
- decline_activity_invite
- invite_to_activity
- spiteful_guests_liked_defacing
- remove_from_activity
- add_to_activity
- skip_activity_phase
- petition_liege_block_firing_councillor_effect_tt

### 00_additional_effects.txt（53 条目）

- set_num_pregnancy_children
- copy_inheritable_appearance_from
- start_tutorial_lesson
- clear_title_laws_effects
- add_title_law_effects
- add_knows_of_killer
- set_generated_bisexuality_chance
- change_target_weight
- remove_special_title
- pledge_defender
- remove_perk
- try_create_suggestion
- join_faction_skip_check
- create_alliance
- title_create_faction
- set_special_title
- set_pregnancy_assumed_father
- battle_event
- remove_province_modifier
- remove_realm_law
- remove_all_character_modifier_instances
- set_special_character
- set_killer_public
- set_generated_homosexuality_chance
- consume_divorce_reasons
- copy_title_history
- remove_all_dynasty_modifier_instances
- assign_commander
- refund_perks
- remove_special_character
- allow_in_scheme
- add_perk
- set_generated_asexuality_chance
- clear_forced_vote
- remove_title_law_effects
- change_first_name
- remove_all_house_modifier_instances
- add_hook_no_toast
- set_real_father
- set_real_mother
- adopt
- set_immortal_age
- add_dynasty_perk
- remove_dynasty_perk
- change_current_weight
- remove_all_province_modifier_instances
- create_dynamic_title
- remove_commander
- remove_title_law
- remove_all_county_modifier_instances
- faction_remove_war
- get_all_innovations_from
- add_loot

### 00_ce1_effects.txt（4 条目）

- ce1_legitimacy_legacy_2_effect
- ce1_legitimacy_legacy_3_effect
- ce1_legitimacy_legacy_4_effect
- ce1_legitimacy_legacy_5_effect

### 00_character_effects.txt（266 条目）

- add_gold
- remove_gold
- pay_gold
- add_opinion
- add_opinion_for_duration
- add_opinion_decaying
- add_opinion_growing
- add_opinion_imprison_reason
- add_opinion_imprison_reason_unusable
- remove_opinion
- add_dread
- change_provisions
- add_legitimacy
- create_betrothal
- create_betrothal_matrilineal
- break_betrothal
- make_concubine
- remove_concubine
- add_stress
- add_stress_critical
- set_to_lowborn
- set_dynasty
- set_known_bastard_on_pregnancy
- make_pregnant
- set_father
- add_prestige
- add_prestige_experience
- add_prestige_no_experience
- set_child_of_concubine_on_pregnancy
- spawn_activity
- complete_activity
- add_trait
- add_trait_force_tooltip
- make_trait_active
- make_trait_active_force_tooltip
- add_trait_xp
- add_trait_xp_single
- remove_trait
- remove_trait_force_tooltip
- make_trait_inactive
- make_trait_inactive_force_tooltip
- add_courtier
- set_knight_status
- start_scheme_against_character
- start_scheme_against_title
- start_scheme_against_culture
- start_scheme_against_faith
- start_scheme_against_nothing
- add_scheme_modifier_duration
- set_focus
- set_focus_no
- set_trait_rank
- stress_impact
- stress_impact_critical
- add_guest_courtier
- return_to_court
- remove_courtier_or_guest
- add_focus_progress
- multiply_focus_progress
- set_focus_progress
- set_relation_guardian
- remove_relation_guardian
- set_relation_ward
- remove_relation_ward
- educate_child_option_convert_culture_effect
- educate_child_option_convert_culture_likely_effect
- educate_child_option_convert_culture_unlikely_effect
- educate_child_option_convert_faith_effect
- educate_child_option_convert_faith_likely_effect
- educate_child_option_convert_faith_unlikely_effect
- educate_child_option_zeal_effect
- educate_child_option_zeal_likely_effect
- educate_child_option_zeal_unlikely_effect_low
- set_relation_mentor
- set_relation_student
- remove_relation_mentor
- remove_relation_student
- set_relation_intrigue_mentor
- set_relation_intrigue_student
- remove_relation_intrigue_mentor
- remove_relation_intrigue_student
- set_relation_potential_lover
- remove_relation_potential_lover
- set_relation_potential_friend
- remove_relation_potential_friend
- set_relation_potential_rival
- set_relation_wedding_good_fertility
- set_relation_wedding_very_good_fertility
- set_relation_wedding_bad_fertility
- set_relation_wedding_very_bad_fertility
- remove_relation_potential_rival
- add_visiting_courtier
- visit_court_of
- set_relation_oaf
- remove_relation_oaf
- set_relation_bully
- remove_relation_bully
- set_relation_crush
- remove_relation_crush
- set_relation_victim
- remove_relation_victim
- set_relation_friend
- remove_relation_friend
- set_relation_soldier_friend
- remove_relation_soldier_friend
- set_relation_rival
- remove_relation_rival
- set_relation_grudge
- remove_relation_grudge
- set_relation_lover
- set_relation_court_physician
- remove_relation_court_physician
- remove_relation_lover
- set_relation_soulmate
- remove_relation_soulmate
- set_relation_best_friend
- remove_relation_best_friend
- set_relation_nemesis
- remove_relation_nemesis
- set_relation_disciple
- remove_relation_disciple
- set_relation_elder
- remove_relation_elder
- set_relation_external_clerical_puppet
- remove_relation_external_clerical_puppet
- set_relation_external_ruler_puppet
- remove_relation_external_ruler_puppet
- add_character_modifier
- add_character_modifier_duration
- remove_character_modifier
- duel
- duel_against
- add_prestige_level
- add_piety
- add_piety_no_experience
- add_piety_experience
- add_piety_level
- create_hybrid_culture
- set_culture
- set_culture_same_as
- add_prowess_skill
- add_diplomacy_skill
- add_stewardship_skill
- add_martial_skill
- add_intrigue_skill
- add_learning_skill
- imprison
- release_from_prison
- change_prison_type
- add_tyranny
- create_character
- create_named_character
- add_hook
- add_hook_strong
- add_hook_perpetual
- remove_hook
- use_hook
- use_hook_strong
- banish
- depose
- add_truce_one_way
- add_truce_both_ways
- cancel_truce_one_way
- cancel_truce_both_ways
- change_liege
- keep_liege
- death
- death_killer
- end_pregnancy
- set_domicile_culture
- set_domicile_faith
- set_character_faith
- set_character_rite
- set_character_rite_fulfillment_change
- set_character_faith_with_conversion
- set_character_secret_faith
- set_house
- break_alliance
- allow_alliance
- set_employer
- give_nickname
- remove_nickname
- spawn_army
- add_realm_law
- add_realm_law_skip_effects
- set_designated_heir
- clear_designated_heir
- divorce
- add_opinion_theocracy_approve
- add_hook_theocracy_approve
- marry
- marry_matrilineal
- marry_same_sex
- change_government
- add_house_modifier
- add_house_modifier_duration
- add_house_unity_modifier
- add_house_unity_modifier_duration
- remove_house_modifier
- add_dynasty_modifier
- add_dynasty_modifier_duration
- remove_dynasty_modifier
- create_holy_order
- refill_garrison
- refill_levy
- set_player_character
- move_to_pool
- move_to_pool_at
- recruit_courtier
- vassal_contract_increase_obligation_level
- vassal_contract_decrease_obligation_level
- start_tributary
- end_tributary
- set_primary_spouse
- add_diplomacy_lifestyle_xp
- add_martial_lifestyle_xp
- add_stewardship_lifestyle_xp
- add_intrigue_lifestyle_xp
- add_learning_lifestyle_xp
- add_wanderer_lifestyle_xp
- add_diplomacy_lifestyle_perk_points
- add_martial_lifestyle_perk_points
- add_stewardship_lifestyle_perk_points
- add_intrigue_lifestyle_perk_points
- add_learning_lifestyle_perk_points
- add_wanderer_lifestyle_perk_points
- loyalty_and_respect_perk_stats_effect
- set_sexuality
- hajj_distance_info_text
- remove_decision_cooldown
- remove_interaction_cooldown
- remove_interaction_cooldown_against
- remove_scheme_cooldown_against
- destroy_character_memory
- consume_imprisonment_reasons
- consume_banish_reasons
- consume_revoke_title_reason
- consume_execute_reasons
- end_story
- force_vote_as_no_duration
- force_vote_as
- party_baron_negative_attitude_counter_stress_tt
- party_baron_positive_attitude_counter_stress_tt
- set_subject_contract_modification_blocked
- copy_localized_text
- remove_localized_text
- set_mother
- change_trait_rank
- set_relation_potential_hook
- remove_relation_potential_hook
- add_glory
- add_subject_standing
- upon_holding_completion
- reminds_of_childhood_decision
- fire_tax_collector
- set_relation_favorite_child
- remove_relation_favorite_child
- vassals_can_become_administrative
- headless_heir_rises_to_challenge_tt
- headless_heir_ignores_challenge_tt
- pay_herd
- add_geographical_region
- set_relation_blood_brother
- change_realm_law_level
- change_title_law_level
- enact_treasury_budgets

### 00_council_effects.txt（12 条目）

- finish_council_task
- start_default_task
- assign_council_task
- assign_councillor
- assign_councillor_type
- fire_councillor
- fire_councillor_skip_effects
- set_council_task
- set_court_council_task
- set_county_council_task
- change_de_jure_drift_progress
- marshal_task_0304_a_tt

### 00_county_effects.txt（4 条目）

- add_county_modifier
- add_county_modifier_duration
- remove_county_modifier
- add_terrain_modifier

### 00_culture_effect.txt（16 条目）

- add_innovation
- add_innovation_progress
- remove_innovation
- get_random_innovation_from
- add_random_innovation
- decide_on_local_culture_conversion
- change_cultural_acceptance
- learn_language_of_culture
- unlearn_language_of_culture
- learn_language
- unlearn_language
- set_ethos_from
- set_language_from
- reset_culture_creation_date
- remove_culture_tradition
- add_culture_tradition

### 00_custom_effects.txt（29 条目）

- custom_seize_title_and_below_de_jure
- custom_seize_title
- feast_main_befriend.2002.because_of_hospitality_tenet
- raise_runestone_decision_warning
- pam_raise_khachkar_decision_warning
- weapon_inspiration_cost_tt
- armor_inspiration_cost_tt
- book_inspiration_cost_tt
- weaver_inspiration_cost_tt
- adventure_inspiration_cost_tt
- artisan_inspiration_cost_tt
- smith_inspiration_cost_tt
- alchemy_inspiration_cost_tt
- bow_inspiration_cost_tt
- religious_artifact_inspiration_cost_tt
- fp2_struggle_hostility_list_tt
- fp2_struggle_secure_iberian_foothold_list_tt
- fp2_struggle_house_tt
- murder_outcome_murdered_rival_tt
- active_unity_level_description_tt
- ep2_tournament_maysir_tt
- admin_confirmation_decision_tt_if_accepted
- mpo_gok_war_of_submission_victory_tt
- mpo_gok_war_of_submission_will_happen_tt
- mpo_gok_war_of_submission_defeat_tt
- gok_gov_switch_options_tt
- gok_gov_if_super_nomadic_tt
- scheme_potential_suzerain_might_join_war_tt
- if_host_accepts_oath_tt

### 00_dynasty_effects.txt（5 条目）

- create_cadet_branch
- add_dynasty_prestige_level
- add_dynasty_prestige
- add_unity_value
- set_house_head

### 00_faction_effects.txt（12 条目）

- add_faction_discontent
- add_joined_faction_discontent
- add_targeting_factions_discontent
- join_faction
- join_faction_forced
- leave_faction
- destroy_faction
- create_faction
- faction_start_war
- title_join_faction
- title_leave_faction
- faction_cooldown_effect

### 00_fp3_effects.txt（12 条目）

- fp3_khvarenah_legacy_court_positions_effect
- fp3_khvarenah_legacy_2_effect
- fp3_khvarenah_legacy_2_hostile_effect
- fp3_khvarenah_legacy_3_marriage_effect
- fp3_khvarenah_legacy_3_spouse_task_effect
- fp3_khvarenah_legacy_4_effect
- fp3_khvarenah_legacy_tax_collector_effect
- fp3_khvarenah_legacy_4_secondary_effect
- fp3_khvarenah_legacy_4_secondary_effect_addition
- kindle_royal_fire_decision_warning
- claim_the_imamate_decision_warning
- fp3_khvarenah_legacy_5_decision_effect

### 00_landed_title_effects.txt（6 条目）

- set_county_culture
- set_county_faith
- set_title_name
- set_title_prefix
- reset_title_name
- reset_title_prefix

### 00_legend_effects.txt（12 条目）

- add_legend_owner_modifier
- add_legend_province_modifier
- add_legend_county_modifier
- add_legend_owner_modifier_duration
- add_legend_province_modifier_duration
- add_legend_county_modifier_duration
- remove_legend_owner_modifier
- remove_legend_province_modifier
- remove_legend_county_modifier
- remove_all_legend_owner_modifier_instances
- remove_all_legend_province_modifier_instances
- remove_all_legend_county_modifier_instances

### 00_maa_effects.txt（2 条目）

- create_maa_regiment
- change_maa_regiment_size

### 00_perk_effects.txt（193 条目）

- unshackled_lust_perk_effect
- subtle_desire_perk_effect
- mortal_adoration_perk_effect
- murder_feast_perk_effect
- home_advantage_perk_effect
- graceful_recovery_perk_effect
- smooth_operator_perk_effect
- truth_is_relative_perk_effect
- truth_is_relative_scheme_effect
- digging_for_dirt_perk_effect
- kidnapper_perk_effect
- kidnapper_perk_nomadic_effect
- court_of_shadows_perk_effect
- court_of_shadows_perk_papal_vote_effect
- court_of_shadows_perk_papabile_effect
- court_of_shadows_perk_admin_effect
- court_of_shadows_perk_effect.increased_grace
- prepared_for_anything_perk_bonus_effect
- dark_insights_perk_effect
- divine_retribution_perk_effect
- prison_feudal_complex_perk_effect
- strict_organization_perk_effect
- courtship_perk_effect
- promising_prospects_perk_effect
- peacemaker_perk_effect
- thoughtful_perk_effect
- thoughtful_perk_nomadic_effect
- ducal_conquest_perk_effect
- forced_vassalage_perk_effect
- bloc_join_perk_effect
- adaptive_traditions_perk_effect
- bellum_justum_effect
- flexible_truces_perk_effect
- defensive_negotiations_perk_effect
- embassies_perk_effect
- accomplished_forger_perk_effect
- red_wedding_perk_effect
- befriend_perk_effect
- unlocks_board_games_interaction_effect
- confidants_perk_effect
- groomed_to_rule_perk_effect
- groomed_to_rule_perk_2_effect
- thicker_than_water_perk_effect
- kin_legacy_2_legacy_effect
- kin_legacy_3_legacy_effect
- kin_legacy_4_legacy_effect
- kin_accolade_effect
- kin_legacy_5_legacy_effect
- friendly_counsel_perk_effect
- friendly_counsel_perk_nomadic_effect
- honored_to_serve_nomadic_perk
- sound_foundations_perk_effect
- true_ruler_perk_effect
- true_ruler_nomadic_perk_effect
- true_ruler_confederation_perk_effect
- refund_all_perks
- stalwart_leader_perk_effect
- chivalric_dominance_perk_incite_war_effect
- it_is_my_domain_perk_effect
- at_any_cost_perk_effect
- tax_man_perk_effect
- pedagogy_perk_effect
- open_minded_perk_effect
- anatomical_studies_perk_effect
- mental_resilience_perk_effect
- restraint_perk_effect
- carefree_perk_effect
- know_thyself_perk_effect
- religious_icon_perk_effect
- religious_icon_nomadic_perk_effect
- religious_icon_perk_canonization_effect
- prophet_perk_living_word_effect
- wash_your_hands_perk_effect
- praetorian_guard_perk_effect
- praetorian_guard_nomadic_perk_effect
- writing_history_perk_effect
- golden_obligations_perk_effect
- meritocracy_perk_effect
- loyalty_and_respect_perk_obedience_effect
- chains_of_loyalty_perk_effect
- toe_the_line_perk_effect
- clerical_justifications_perk_effect
- clerical_justifications_perk_passive_learning_effect
- hard_rule_perk_effect
- learn_on_the_job_perk_effect
- zealous_proselytizer_perk_effect
- nomadic_zealous_proselytizer_inspire_conversion_effect
- nomadic_zealous_proselytizer_stargazer_effect
- zealous_proselytizer_perk_effect_spread_tenet
- sanctioned_loopholes_perk_effect
- sanctioned_loopholes_perk_effect_beseech_claim
- sanctioned_loopholes_perk_effect_sell_claim
- planned_cultivation_perk_effect
- enduring_hardships_perk_effect
- blood_legacy_4_effect
- warfare_legacy_2_effect
- warfare_legacy_3_effect
- warfare_legacy_5_unlock_effect
- warfare_legacy_5_effect
- guile_legacy_2_effect
- law_legacy_1_effect
- glory_legacy_1_perk_effect
- glory_legacy_4_perk_effect
- erudition_legacy_4_effect
- erudition_legacy_1_effect
- erudition_legacy_5_effect
- guile_legacy_5_effect
- legacy_additional_language_effect
- legacy_cultural_acceptance_from_language_schemes_effect
- legacy_more_acceptance_from_council_job_effect
- legacy_cultural_emissary_court_position_effect
- legacy_promote_culture_decision_effect
- legacy_hooks_on_different_culture_vassals_effect
- set_absolute_country_control
- commission_epic_potential_cost_effect
- commission_epic_once_complete_effect
- extort_subjects_effect
- unlock_dueling_rivals_effect
- unlock_dueling_for_everyone_effect
- unlocks_stalwart_leader_non_admin_duels_effect
- ep2_activities_legacy_2_grand_weddings_cheaper_effect
- ep2_activities_legacy_2_grand_weddings_acceptance_boost_effect
- ep2_activities_legacy_2_grand_weddings_increased_strong_hook_on_liege_event_effect
- ep2_activities_legacy_1_pilgrimages_cheaper_effect
- ep2_activities_legacy_1_pilgrimages_add_learning_per_holy_site_effect
- ep2_activities_legacy_3_tours_majesty_modifier_effect
- ep2_activities_legacy_3_tours_intimidation_modifier_effect
- ep2_activities_legacy_3_tours_taxation_modifier_effect
- ep2_activities_legacy_3_tours_reset_modifier_timers_effect
- ep2_activities_legacy_4_hunts_up_legendary_hunt_sightings_effect
- ep2_activities_legacy_5_tournaments_invite_knights_boosts_effect
- ep2_activities_legacy_5_house_heads_get_one_freebie_grand_activity_effect
- ce1_heroic_legacy_2_effect
- ce1_heroic_legacy_3_effect
- ce1_heroic_legacy_4_effect
- ce1_heroic_legacy_5_effect
- well_prepared_perk_effect
- far_and_wide_perk_effect
- just_one_more_hill_perk_effect
- roaming_perk_effect
- of_the_people_perk_effect
- of_the_people_perk_nomadic_effect
- of_the_people_perk_2_effect
- travel_companion_perk_effect
- the_home_away_from_home_perk_effect
- local_arbitration_perk_effect
- local_arbitration_perk_2_effect
- local_arbitration_wanderers_purpose
- local_arbitration_mercenaries_purpose
- local_arbitration_scholar_purpose
- local_arbitration_explorers_purpose
- local_arbitration_brigands_purpose
- local_arbitration_legitimists_purpose
- power_at_home_perk_effect
- journey_planner_perk_effect
- finally_there_perk_effect
- finally_there_perk_2_effect
- mercenary_contacts_perk_effect
- been_there_done_that_perk_effect
- souvenirs_aplenty_perk_effect
- souvenirs_aplenty_nomadic_perk_effect
- souvenirs_aplenty_perk_2_effect
- souvenirs_aplenty_perk_3_effect
- gracious_host_impeccable_guest_perk_effect
- gracious_host_impeccable_guest_perk_2_effect
- gracious_host_impeccable_guest_perk_3_effect
- gracious_host_impeccable_guest_perk_4_effect
- journey_perk_effect
- journey_perk_2_effect
- local_inspection_perk_effect
- local_inspection_perk_2_effect
- local_inspection_perk_3_effect
- local_hero_perk_effect
- travel_logs_perk_effect
- travel_logs_perk_2_effect
- know_your_land_know_your_people_perk_effect
- know_your_land_know_your_people_perk_2_effect
- know_your_land_know_your_people_perk_3_effect
- mustering_the_troops_perk_effect
- mustering_the_troops_perk_2_effect
- surveyor_no_stone_unturned_perk_effect
- surveyor_no_stone_unturned_nomadic_perk_effect
- no_stone_unturned_perk_2_effect
- no_stone_unturned_perk_cooldown_message
- personal_touch_effect
- personal_touch_2_effect
- personal_touch_3_effect
- personal_touch_4_effect
- local_adjudicate_location_tt
- realm_charts_perk_effect
- realm_charts_perk_2_effect
- draw_up_new_charts_complete_effect
- befriend_perk_prestige_cost_effect

### 00_province_effects.txt（9 条目）

- add_province_modifier
- add_province_modifier_duration
- generate_building
- add_building
- remove_building
- set_holding_type
- add_special_building_slot
- add_special_building
- begin_create_holding

### 00_religion_effects.txt（42 条目）

- change_fervor
- warchest_divide_gold
- warchest_divide_piety
- warchest_divide_prestige
- warchest_divide_gold_player
- warchest_divide_piety_player
- warchest_divide_prestige_player
- unpledge_attacker
- unpledge_defender
- set_great_holy_war_target
- set_beneficiary
- reset_designated_winner
- divide_war_chest
- reset_beneficiary
- change_war_chest_gold
- change_war_chest_piety
- change_war_chest_prestige
- do_ghw_title_handout
- set_designated_winner
- add_doctrine
- remove_doctrine
- pledge_attacker
- set_religious_head_title
- remove_religious_head_title
- pilgrimage_because_i_have_armed_pilgrimages
- pilgrimage_because_i_have_tenet_mendicant_preachers
- pilgrimage_because_i_have_tenet_pentarchy
- pilgrimage_because_i_have_tenet_esotericism
- pilgrimage_because_i_have_tenet_struggle_submission
- pilgrimage_because_i_have_tenet_ancestor_worship
- pilgrimage_piousness_because_i_have_tenet_armed_pilgrimages
- pilgrimage_piousness_because_i_have_tenet_struggle_submission
- pilgrimage_piousness_because_i_have_tenet_warmonger
- pilgrimage_entourage_gains_pilgrim_trait
- pilgrimage_entourage_gains_hajjaj_trait
- create_temporal_head_of_faith
- new_religious_head_title
- can_never_reform_kuzarism_tt
- add_known_faith
- add_known_tenet
- add_known_doctrine
- add_known_rite

### 00_scheme_effects.txt（28 条目）

- add_agent_slot
- force_add_to_agent_slot
- add_to_agent_slot
- change_opportunities
- forbid_from_scheme
- expose_scheme
- expose_scheme_agent
- add_scheme_cooldown
- claim_throne_success_discovery_warning_effect
- scheme_target_died
- scheme_target_imprisoned_by_other
- scheme_target_no_longer_courtier
- scheme_target_no_longer_courtier_no_var
- scheme_target_is_your_courtier
- scheme_target_no_longer_lover
- scheme_target_not_in_diplomatic_range
- i_could_not_take_their_place
- add_scheme_modifier
- remove_scheme_modifier
- add_scheme_progress
- end_scheme
- in_addition_effect_tooltip
- learn_language_will_cancel_ongoing_schemes_tt
- petition_liege_second_if_tt
- begin_scheme_with_starter_package_tooltip_effect_tt
- add_contact
- add_scheme_breach
- reset_scheme_progress

### 00_secret_effects.txt（8 条目）

- add_secret
- add_secret_participant
- remove_secret
- expose_secret
- reveal_to
- set_secret_owner
- spend_by
- disable_exposure_by

### 00_title_effects.txt（22 条目）

- change_title_holder
- change_title_holder_include_vassals
- get_title
- destroy_title
- set_add_claim_on_loss
- change_development_level
- change_development_progress
- change_development_progress_with_overflow
- change_county_control
- add_pressed_claim
- add_unpressed_claim
- remove_claim
- make_claim_strong
- make_claim_weak
- lease_out_to_holy_order
- revoke_lease_from_holy_order
- revoke_lease
- set_primary_title_to
- set_de_jure_liege_title
- set_realm_capital
- clear_title_laws
- add_title_law

### 00_travel_effects.txt（16 条目）

- add_companion
- start_travel_plan
- complete_travel_plan
- pause_travel_plan
- resume_travel_plan
- abort_travel_plan
- cancel_travel_plan
- return_home
- add_travel_option
- add_travel_plan_modifier
- add_travel_plan_modifier_duration
- set_travel_leader
- delay_travel_plan
- add_destination_progress
- add_travel_waypoint
- remove_character

### 00_vassal_effects.txt（4 条目）

- vassal_contract_set_obligation_level
- tributary_contract_set_obligation_level
- apply_ai_vassal_obligation_vassal_most_desired
- apply_ai_vassal_obligation_liege_most_desired

### 00_war_effects.txt（32 条目）

- start_war
- de_jure_attacker_prestige
- de_jure_defender_prestige
- becomes_independent
- add_attacker
- add_defender
- remove_participant
- end_war_attacker_victory
- end_war_white_peace
- end_war_defender_victory
- end_war_invalidated
- add_prestige_from_contribution
- add_gold_from_contribution
- add_piety_from_contribution
- add_influence_from_contribution
- add_merit_from_contribution
- add_herd_from_contribution
- add_renown_from_contribution
- add_treasury_from_contribution
- add_provisions_from_contribution
- add_opinion_from_contribution
- set_casus_belli
- set_called_to
- start_great_holy_war
- start_ghw_war
- attack_ally_text
- attack_suzerain_text
- attack_breaking_truce_text
- attack_breaking_betrothal_text
- attack_same_faith_peace_of_god_text
- if_you_win_effect
- if_you_lose_effect

### 01_ep1_effects.txt（30 条目）

- sponsor_inspiration
- end_inspiration_sponsorship
- destroy_inspiration
- change_inspiration_progress
- invest_gold
- public_execution_tooltip
- public_execution_too_soon_tooltip
- destroy_artifact
- destroy_owned_artifact
- add_durability
- set_max_durability
- set_owner
- add_personal_artifact_claim
- add_house_artifact_claim
- remove_personal_artifact_claim
- remove_house_artifact_claim
- add_artifact_modifier
- remove_artifact_modifier
- copy_artifact_modifiers
- every_court_position_employer
- random_court_position_employer
- every_court_position_holder
- random_court_position_holder
- appoint_court_position
- revoke_court_position
- replace_court_position
- create_artifact
- set_artifact_rarity
- equip_artifact_to_owner
- unequip_artifact_from_owner

### 01_fp1_effects.txt（10 条目）

- fp1_adventure_legacy_1_effect
- fp1_adventure_legacy_2_effect
- fp1_adventure_legacy_3_effect
- fp1_adventure_legacy_5_effect
- send_to_varangian_guard_interaction_effect
- fp1_pillage_legacy_1_effect
- fp1_pillage_legacy_3_effect
- fp1_pillage_legacy_4_effect
- fp1_pillage_legacy_5_effect
- fp1_adventure_legacy_2_secondary_effect

### 02_ep1_effects.txt（5 条目）

- set_amenity_level
- change_current_court_grandeur
- commission_artifact_decision_warning_effect
- pay_homage_gift_warning_effect
- petition_liege_warning_effect

### 03_fp2_effects.txt（21 条目）

- fp2_urbanism_legacy_1_effect
- fp2_urbanism_legacy_3_effect
- fp2_urbanism_legacy_4_effect
- fp2_urbanism_legacy_2_effect
- fp2_urbanism_legacy_5_effect
- fp2_coterie_legacy_1_effect
- fp2_coterie_legacy_2_effect
- fp2_coterie_legacy_3_effect
- fp2_coterie_legacy_4_effect
- fp2_coterie_legacy_5_effect
- start_struggle
- end_struggle
- activate_struggle_catalyst
- change_struggle_phase
- set_culture_as_involved
- set_culture_as_uninvolved
- set_faith_as_involved
- set_faith_as_uninvolved
- many_secrets_exchanged
- several_secrets_exchanged
- few_secrets_exchanged

### 04_ep2_diarchy_effects.txt（10 条目）

- designate_diarch
- try_start_diarchy
- end_diarchy
- set_diarchy_type
- set_diarch
- set_diarchy_swing
- change_diarchy_swing
- depose_diarch
- change_strife_opinion
- set_diarchy_mandate

### 04_ep2_effects.txt（17 条目）

- complete_activity_intent
- tournament_disqualify_tt
- tournament_contest_disqualify_tt
- tournament_contest_disqualify_round_tt
- tournament_contest_disqualify_win_tt
- tournament_contest_resign_tt
- tournament_contest_resign_round_tt
- tournament_contest_resign_win_tt
- tournament_contest_replaced_tt
- tournament_contest_round_tt
- tournament_contest_round_win_tt
- tournament_contest_withdraw_tt
- tournament_contest_knocked_tt
- winning_knight_rewards_tt
- losing_knight_rewards_tt
- qualifying_knight_rewards_tt
- tournament_contest_round_next_tt

### 05_bp2_hostage_effects.txt（16 条目）

- take_hostage
- return_hostage
- attack_breaking_truce_hostage
- hostage_leaves_home_tt
- hostage_pacts_on_arrival_tt
- hostage_heads_home_tt
- ward_effects_on_arrival_tt
- ward_nearing_adulthood_tt
- hostage_attack_warning_tt
- hostage_execution_warning_tt
- hostage_prestige_income_tt
- hostage_prestige_renown_income_tt
- warden_lower_title_tier_tt
- warden_lower_dynasty_renown_tt
- hostage_prestige_piety_renown_income_tt
- hostage_faith_hostility_tt

### 07_ep3_effects.txt（31 条目）

- move_domicile
- change_influence
- change_influence_level
- change_influence_no_experience
- create_task_contract
- accept_task_contract
- invalidate_contract
- ep3_otherwise_tt
- ep3_story_cycle_admin_eunuch_upgrade_modifier_tt
- ep3_story_cycle_admin_eunuch_downgrade_modifier_tt
- create_noble_family_tt
- change_maa_troops_count
- reinforce_soldiers_effect_tt
- deplete_army_by_percentage
- add_supply
- subtract_supply
- clear_supply
- refill_supply
- execute_prisoner_interaction_tt_co_emperor_usurpation
- change_appointment_investment
- change_appointment_investment_with_investor
- IS_ALLOWED_TO_REVOKE_ADMIN_GOVERNMENT
- estate_unlock_granary_decision_factors_tt
- contact_list_request_interaction_possible_outcomes
- evict_adventurer_consequences_tt
- transfer_owned_maa_control
- on_declared_war_in_admin
- if_actor_accepts_desc
- if_byz_dissolves_tt
- contract_assistance_interaction_condition_tt
- ep3_hire_laamp_mercs_payment_tt

### 08_tgp_effects.txt（17 条目）

- pledge_loyalty_to_liege_gift_warning_effect
- influence_family_effect
- demand_retake_exam_effect
- create_house_bloc_effect
- join_house_bloc_effect
- leave_house_bloc_effect
- leave_house_bloc_cooldown_effect
- change_house_bloc_leader_effect
- disband_house_bloc_effect
- challenge_house_head_japanese_admin
- transfer_treasury_because_you_are_greedy
- transfer_treasury_because_you_are_generous
- tgp_bloc_war_defeat_member_description
- tgp_bloc_war_defeat_member_house_description
- tgp_create_meritocratic_ruling_regent_title_effect
- add_barter_goods
- remove_barter_goods

### 09_situation_effects.txt（5 条目）

- trigger_situation_catalyst
- trigger_sub_region_catalyst
- change_top_phase
- change_phase
- add_takeover_phase_points

### 10_ach_effects.txt（2 条目）

- if_host_calms_crowd_desc
- if_crush_happens_desc

### 10_tgp_effects.txt（48 条目）

- set_house_relation
- change_house_relation_level
- clear_house_relation
- house_relation_improved_minor_desc
- house_relation_improved_medium_desc
- house_relation_improved_major_desc
- house_relation_damaged_minor_desc
- house_relation_damaged_medium_desc
- house_relation_damaged_major_desc
- tutor_improved_exam_chances_tt
- tutor_needed_for_exam_chances_tt
- divine_happenstance_tt
- because_of_your_divine_happenstance_tt
- scheme_increase_movement_power_effect_tooltip
- scheme_decrease_movement_power_effect_tooltip
- because_you_are_a_schemer_tt
- tgp_merit_legacy_advantage
- tgp_dynasty_legacy_movement_power_bonus
- tgp_dynasty_legacy_extra_disciple_limit
- tgp_dynasty_legacy_invite_to_movement
- tgp_dynasty_legacy_governor_efficiency_bonus
- tgp_dynasty_legacy_unlock_east_asian_estate_archive
- tgp_dynasty_legacy_unlock_east_asian_estate_gate
- tgp_dynasty_legacy_pick_career
- tgp_dynasty_legacy_invite_to_movement_bonus
- tgp_dynasty_legacy_celestial_minister_aidee_bonus
- tgp_dynasty_legacy_celestial_minister_aidee_discount
- tgp_legacy_celestial_candidate_score_bonus
- tgp_dynasty_legacy_influence_career_bonus
- tgp_legacy_meritocratic_candidate_score_bonus
- tgp_legacy_powerfuL_family
- tgp_dynasty_legacy_same_dynasty_likelier_to_join_bloc
- tgp_dynasty_legacy_same_dynasty_increased_bloc_cohesion
- tgp_dynasty_legacy_can_hire_court_poet
- tgp_dynasty_legacy_court_poet_discount
- tgp_dynasty_legacy_court_poet_bonuses
- tgp_dynasty_legacy_unlock_poetry_collection
- tgp_dynasty_legacy_unlock_domicile_retainer_accomodations
- tgp_dynasty_legacy_unlock_improve_house_relation_inside_bloc_interaction
- tgp_dynasty_legacy_cheaper_to_host_festivals
- tgp_legitimacy_visit_capital_temples
- tgp_legitimacy_pilgrimages
- tgp_sea_legacy_tributary_acceptance
- tgp_sea_legacy_more_likely_to_contribute_to_gp
- tgp_sea_legacy_new_great_project_contributions
- tgp_sea_legacy_pass_one_succession_challenge
- tgp_sea_legacy_heir_succession_modifier
- tgp_sea_legacy_easier_to_become_mandala

### pam_effects.txt（10 条目）

- change_rite_divergence
- add_tenet
- remove_tenet
- pam_legacy_2_petition_effect
- pam_legacy_2_treasury_effect
- pam_legacy_3_evangelize_effect
- pam_legacy_4_candidacy_effect
- pam_legacy_4_cardinal_effect
- pam_legacy_5_papabile_effect
- pam_legacy_5_shape_church_effect

### 未解析文件

- `_effect_localization.info` — 纯文档（非 Jomini）
