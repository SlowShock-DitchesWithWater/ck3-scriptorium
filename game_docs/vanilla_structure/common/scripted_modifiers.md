# common/scripted_modifiers 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：46（其中 Jomini 解析 45 个）
- 顶层块条目总数：423，跨文件唯一条目 423
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_activity_scripted_modifiers.txt` | 69452 | 58 | 0 | jomini |
| `00_ai_value_modifiers.txt` | 6570 | 12 | 0 | jomini |
| `00_building_modifiers.txt` | 26338 | 49 | 0 | jomini |
| `00_character_interaction_modifiers.txt` | 33285 | 6 | 0 | jomini |
| `00_character_selection_scripted_modifiers.txt` | 502 | 2 | 0 | jomini |
| `00_councillor_scripted_modifiers.txt` | 2026 | 2 | 0 | jomini |
| `00_decisions_scripted_modifiers.txt` | 247 | 1 | 0 | jomini |
| `00_diarchy_scripted_modifiers.txt` | 9879 | 27 | 0 | jomini |
| `00_elective_successions_scripted_modifiers.txt` | 118554 | 15 | 0 | jomini |
| `00_ep1_amenities_modifiers.txt` | 3 | 0 | 0 | jomini |
| `00_ep1_artifact_modifiers.txt` | 1076 | 6 | 0 | jomini |
| `00_ep1_inspiration_modifiers.txt` | 3948 | 4 | 0 | jomini |
| `00_faction_modifiers.txt` | 121692 | 27 | 0 | jomini |
| `00_hold_court_modifiers.txt` | 2470 | 5 | 0 | jomini |
| `00_lifestyle_scripted_modifiers.txt` | 873 | 2 | 0 | jomini |
| `00_marriage_scripted_modifiers.txt` | 82833 | 9 | 0 | jomini |
| `00_military_scripted_modifiers.txt` | 434 | 1 | 0 | jomini |
| `00_perk_modifiers.txt` | 346 | 1 | 0 | jomini |
| `00_portrait_modifiers.txt` | 3630 | 20 | 0 | jomini |
| `00_religion_scripted_modifiers.txt` | 121091 | 21 | 0 | jomini |
| `00_romance_and_seduction_scripted_modifiers.txt` | 3284 | 2 | 0 | jomini |
| `00_scheme_scripted_modifiers.txt` | 110966 | 38 | 0 | jomini |
| `00_scripted_relations_scripted_modifiers.txt` | 3443 | 2 | 0 | jomini |
| `00_single_combat_scripted_modifiers.txt` | 1198 | 9 | 0 | jomini |
| `00_spouse_scripted_modifiers.txt` | 45 | 0 | 0 | jomini |
| `00_statecraft_lifestyle_scripted_modifiers.txt` | 323 | 1 | 0 | jomini |
| `00_trait_specific_scripted_modifiers.txt` | 371 | 1 | 0 | jomini |
| `00_voter_strength_scripted_modifiers.txt` | 10261 | 1 | 0 | jomini |
| `00_weather_modifiers.txt` | 1174 | 2 | 0 | jomini |
| `00_yearly_events_scripted_modifiers.txt` | 720 | 2 | 0 | jomini |
| `01_bp1_scripted_modifiers.txt` | 1635 | 4 | 0 | jomini |
| `01_fp1_scripted_modifiers.txt` | 606 | 1 | 0 | jomini |
| `02_ep1_scripted_modifiers.txt` | 3247 | 8 | 0 | jomini |
| `03_fp2_scripted_modifiers.txt` | 19438 | 12 | 0 | jomini |
| `04_ep2_scripted_modifiers.txt` | 13641 | 11 | 0 | jomini |
| `05_bp2_scripted_modifiers.txt` | 25366 | 15 | 0 | jomini |
| `05_fp3_scripted_modifiers.txt` | 9478 | 8 | 0 | jomini |
| `07_ep3_scripted_modifiers.txt` | 10045 | 8 | 6 | jomini |
| `09_mpo_scripted_modifiers.txt` | 16673 | 1 | 0 | jomini |
| `10_ach_scripted_modifiers.txt` | 2339 | 3 | 0 | jomini |
| `10_tgp_faction_modifiers.txt` | 848 | 2 | 0 | jomini |
| `10_tgp_japan_modifiers.txt` | 19381 | 6 | 0 | jomini |
| `10_tgp_scripted_modifiers.txt` | 3296 | 4 | 0 | jomini |
| `_scripted_modifiers.info` | 664 | - | - | 纯文档（非 Jomini） |
| `pam_scripted_modifiers.txt` | 741 | 1 | 0 | jomini |
| `tgp_mandala_scripted_modifiers.txt` | 11578 | 13 | 0 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_activity_scripted_modifiers.txt（58 条目）

- base_activity_modifier
- activity_guest_shared_ai_accept_modifier
- activity_guest_clergy_shared_ai_accept_modifier
- activity_guest_clergy_frivolous_ai_accept_modifier
- activity_guest_feast_ai_accept_modifier
- feast_events_ewan_0001_weight_down_for_bodyguards_modifier
- feast_events_ewan_0001_weight_up_for_bodyguards_modifier
- feast_events_ewan_0001_weight_down_for_tier_difference_modifier
- feast_events_ewan_0001_weight_up_for_tier_difference_modifier
- activity_guest_hunt_ai_accept_modifier
- activity_guest_pilgrimage_ai_accept_modifier
- activity_guest_tournament_ai_accept_modifier
- activity_tournament_violent_modifier
- activity_tournament_wager_ai_option_modifier
- activity_contest_team_size_modifier
- activity_contest_team_preference_modifier
- activity_tournament_contest_team_score_modifier
- activity_tournament_contest_entrant_preference_modifier
- activity_tournament_pas_darmes_modifier
- activity_guest_wedding_ai_accept_modifier
- activity_guest_health_ai_accept_modifier
- interesting_feast_participant_modifier
- playdate_close_age_scripted_modifier
- petition_liege_councillor_compare_modifier
- petition_liege_cost_negative_modifier
- activity_court_position_aptitude_positive_modifier
- activity_court_position_aptitude_negative_modifier
- hunt_activity_lifestyle_modifier
- hunt_activity_sighting_county_modifier
- hunt_activity_sighting_terrain_modifier
- hunt_activity_sighting_building_modifier
- hunt_activity_game_building_modifier
- hunt_activity_organization_modifier
- hunt_activity_building_development_modifier
- hunt_activity_hunter_lifestyle_modifier
- hunt_murderer_modifier
- hunt_boulder_jump_success_modifiers
- hunt_boulder_jump_failure_modifiers
- hunt_kill_melee_modifiers
- hunt_kill_bow_modifiers
- hunt_kill_hunter_modifiers
- hunt_likely_injured_modifiers
- hunt_relevant_participant_modifiers
- hunt_activity_realm_size_modifier
- activity_guest_chariot_race_ai_accept_modifier
- chariot_race_4050_agents_positive_modifiers
- chariot_race_4050_agents_negative_modifiers
- chariot_race_4050_self_positive_modifiers
- chariot_race_4050_self_negative_modifiers
- inspection_activity_options_positive_modifier
- inspection_activity_options_negative_modifier
- imperial_examination_activity_dynasty_modifier
- imperial_examination_activity_failee_modifier
- imperial_examination_activity_confucian_education_modifier
- local_examination_activity_is_hegemon_modifier
- imperial_examination_activity_forced_back_modifier
- debate_activity_is_hegemon_modifier
- imperial_examination_activity_rites_modifier

### 00_ai_value_modifiers.txt（12 条目）

- ai_target_modifier
- ai_boldness_target_modifier
- ai_compassion_target_modifier
- ai_greed_target_modifier
- ai_energy_target_modifier
- ai_honor_target_modifier
- ai_rationality_target_modifier
- ai_sociability_target_modifier
- ai_vengefulness_target_modifier
- ai_zeal_target_modifier
- ai_military_threat_modifier_with_cbs
- ai_military_threat_modifier

### 00_building_modifiers.txt（49 条目）

- ai_general_building_modifier
- ai_tier_1_building_modifier
- ai_tier_1_economical_building_preference_modifier
- ai_tier_1_pious_building_preference_modifier
- ai_economical_building_preference_modifier
- ai_pious_building_preference_modifier
- ai_skirmisher_modifier
- ai_archer_modifier
- ai_heavy_infantry_modifier
- ai_pikemen_modifier
- ai_light_cavalry_modifier
- ai_heavy_cavalry_modifier
- ai_compensate_heavy_cavalry_modifier
- ai_compensate_light_cavalry_modifier
- ai_archer_cavalry_modifier
- ai_camels_modifier
- ai_elephants_modifier
- ai_stacking_bonus_military_camps_modifier
- ai_stacking_bonus_smiths_modifier
- ai_stacking_bonus_stables_modifier
- ai_stacking_bonus_horse_pastures_modifier
- ai_stacking_bonus_hillside_grazing_modifier
- ai_stacking_bonus_warrior_lodges_modifier
- ai_stacking_bonus_wind_furnaces_modifier
- ai_stacking_bonus_outposts_modifier
- ai_stacking_bonus_camel_farms_modifier
- ai_stacking_bonus_elephant_pens_modifier
- ai_anti_synergy_cavalry_modifier
- ai_anti_synergy_armored_infantry_modifier
- ai_anti_synergy_light_infantry_modifier
- culture_likely_to_fortify_modifier
- ai_tradeport_improvement_from_culture_modifier
- ai_pasture_improvement_from_culture_modifier
- ai_hunting_grounds_improvement_from_culture_modifier
- ai_orchard_improvement_from_culture_modifier
- ai_farm_estate_improvement_from_culture_modifier
- ai_paddy_fields_improvement_from_culture_modifier
- ai_cereal_fields_improvement_from_culture_modifier
- ai_outposts_improvement_from_culture_modifier
- ai_barracks_improvement_from_culture_modifier
- ai_logging_camp_improvement_from_culture_modifier
- ai_peat_quarries_improvement_from_culture_modifier
- ai_hill_farms_improvement_from_culture_modifier
- ai_elephant_pens_improvement_from_culture_modifier
- ai_plantations_improvement_from_culture_modifier
- ai_quarries_improvement_from_culture_modifier
- directive_to_fortify_modifier
- directive_to_build_military_modifier
- directive_to_build_economy_modifier

### 00_character_interaction_modifiers.txt（6 条目）

- offer_vassalization_interaction_ai_acceptance_general
- offer_vassalization_interaction_ai_acceptance_religion_and_culture
- offer_vassalization_interaction_ai_acceptance_bonus
- offer_vassalization_interaction_ai_acceptance_relation
- offer_vassalization_interaction_ai_acceptance_diplomacy
- negotiate_alliance_interaction_ai_acceptance

### 00_character_selection_scripted_modifiers.txt（2 条目）

- is_of_minor_interest_to_weight_up_modifier
- is_of_major_interest_to_weight_up_modifier

### 00_councillor_scripted_modifiers.txt（2 条目）

- councillor_spouse_any_skill_rating_modifier
- councillor_spouse_limited_skill_rating_modifier

### 00_decisions_scripted_modifiers.txt（1 条目）

- minor_decisions_1001_modifier

### 00_diarchy_scripted_modifiers.txt（27 条目）

- intermediary_liege_will_accept_standard_modifiers
- diarch_evaluate_worth_of_war_modifier
- character_hates_scope_due_to_strife_modifier
- character_hates_scope_due_to_strife_plus_desc_modifier
- character_hates_scope_spouse_due_to_strife_plus_desc_modifier
- ai_wants_junior_or_co_emperor_modifier
- diarchy_mandate_events_committed_diarch_serves_weight_up_ai_modifier
- diarchy_mandate_events_committed_diarch_serves_weight_down_ai_modifier
- diarchy_mandate_events_high_diligency_weight_down_modifier
- diarchy_mandate_events_low_diligency_weight_down_modifier
- diarchy_1201_swing_resolve_ai_value_modifier
- diarchy_1211_swing_resolve_ai_value_modifier
- diarchy_1221_swing_resolve_ai_value_modifier
- diarchy_1231_swing_resolve_ai_value_modifier
- diarchy_1241_swing_resolve_ai_value_modifier
- diarchy_1701_swing_resolve_ai_value_modifier
- diarchy_1711_swing_resolve_ai_value_modifier
- diarchy_1721_swing_resolve_ai_value_modifier
- diarchy_1731_swing_resolve_ai_value_modifier
- diarchy_1741_swing_resolve_ai_value_modifier
- diarchy_2201_swing_resolve_ai_value_modifier
- diarchy_2211_swing_resolve_ai_value_modifier
- diarchy_2221_swing_resolve_ai_value_modifier
- diarchy_2231_swing_resolve_ai_value_modifier
- diarchy_2241_swing_resolve_ai_value_modifier
- bp2_yearly_0601_ai_weight_option_skill_modifier
- bp2_yearly_0601_ai_weight_option_perk_modifier

### 00_elective_successions_scripted_modifiers.txt（15 条目）

- elector_self_voting_pattern_feudal_elective_modifier
- holder_voting_pattern_feudal_elective_modifier
- elector_voting_pattern_circumstances_feudal_elective_modifier
- elector_voting_pattern_prestige_piety_feudal_elective_modifier
- elector_voting_pattern_traits_feudal_elective_modifier
- elector_voting_pattern_opinion_feudal_elective_modifier
- elector_voting_pattern_circumstances_gaelic_elective_modifier
- elector_voting_pattern_circumstances_saxon_elective_modifier
- elector_voting_pattern_circumstances_scandinavian_elective_modifier
- elector_voting_pattern_circumstances_tribal_elective_modifier
- elector_voting_pattern_circumstances_misc_elective_modifier
- hook_for_vote_interaction_ai_modifier
- elector_voting_pattern_confederation_modifier
- elector_voting_pattern_theocratic_elective_modifier
- elector_self_voting_pattern_theocratic_elective_modifier

### 00_ep1_amenities_modifiers.txt（0 条目）

（无顶层块）

### 00_ep1_artifact_modifiers.txt（6 条目）

- artifact_armor_type_mail_modifier
- artifact_armor_type_plate_modifier
- artifact_armor_type_scale_modifier
- artifact_armor_type_lamellar_modifier
- artifact_armor_type_laminar_modifier
- artifact_armor_type_brigandine_modifier

### 00_ep1_inspiration_modifiers.txt（4 条目）

- inspiration_royal_court_grandeur_attraction_modifier
- inspiration_royal_court_oversaturation_penalty_modifier
- inspiration_region_court_grandeur_attraction_modifier
- inspiration_region_oversaturation_penalty_modifier

### 00_faction_modifiers.txt（27 条目）

- intimidated_from_faction_modifier
- legalism_virtue_and_sin_modifier
- tenet_purgatory_sin_faction_modifier
- tenet_divine_marriage_incestuous_liege_faction_modifier
- pluralism_fundamentalism_modifier
- pluralism_fundamentalism_dual_modifier
- liege_debt_modifier
- debt_modifier
- dynamic_power_threshold_scripted_modifier
- common_discontent_progress_modifier
- common_create_faction_blockers
- common_join_faction_blockers
- common_faction_modifiers
- independence_faction_create_blockers
- independence_faction_modifiers
- nation_fracturing_faction_modifiers
- nation_fracturing_faction_blockers
- liberty_faction_modifiers
- claimant_faction_blockers
- claimant_faction_modifiers
- struggle_faction_modifiers
- join_faction_stacking_modifiers
- admin_faction_modifiers
- admin_claimant_faction_modifiers
- ceremonial_claimant_faction_modifiers
- ceremonial_claimant_faction_blockers
- imperial_policy_faction_modifiers

### 00_hold_court_modifiers.txt（5 条目）

- court_position_generator_shared_modifier
- camp_officer_generator_shared_modifier
- hold_court_8290_vassal_modifiers
- hold_court_8290_county_modifiers
- hold_court_8290_province_modifiers

### 00_lifestyle_scripted_modifiers.txt（2 条目）

- upweight_for_focus_modifier
- downweight_for_focus_modifier

### 00_marriage_scripted_modifiers.txt（9 条目）

- marriage_ai_accept_perk_modifier
- marriage_ai_accept_politic_modifier
- marriage_ai_accept_opinion_relationship_modifier
- marriage_ai_accept_succession_modifier
- marriage_ai_accept_faith_hostility_modifier
- marriage_ai_accept_fertility_modifier
- marriage_ai_accept_modifier
- elopment_ai_accept_modifier
- divorce_character_ai_accept_modifier

### 00_military_scripted_modifiers.txt（1 条目）

- factor_down_for_current_military_strength_modifier

### 00_perk_modifiers.txt（1 条目）

- mortal_adoration_murder_save_modifier

### 00_portrait_modifiers.txt（20 条目）

- portrait_western_clothing_modifier
- portrait_mena_clothing_modifier
- portrait_byzantine_clothing_modifier
- portrait_indian_clothing_modifier
- portrait_steppe_clothing_modifier
- portrait_northern_clothing_modifier
- portrait_african_clothing_modifier
- portrait_fp1_norse_clothing_modifier
- portrait_fp2_iberian_christian_clothing_modifier
- portrait_fp2_iberian_muslim_clothing_modifier
- portrait_fp3_iranian_clothing_modifier
- portrait_fp3_turkic_clothing_modifier
- portrait_clean_shaven_clothing_modifier
- portrait_western_beards_clothes_modifier
- portrait_mena_beards_clothes_modifier
- portrait_scottish_unique_haircut
- portrait_frankish_unique_haircut
- court_fashion_level_4_modifier
- court_fashion_level_4_headgear_modifier
- court_fashion_level_5_modifier

### 00_religion_scripted_modifiers.txt（21 条目）

- religion_scaled_virtuous_traits_modifier
- religion_scaled_sinful_traits_modifier
- religion_demand_conversion_default_modifier
- religion_demand_conversion_christian_situation_modifier
- religion_sway_to_rite_default_modifier
- religion_adopt_secret_faith_modifier
- sun_trial_death_modifier
- sun_trial_survival_modifier
- general_secular_to_ecclesiastic_acceptance_modifier
- general_secular_to_ecclesiastic_acceptance_secondary_recipient_modifier
- title_acquisition_clerical_acceptance_modifier
- title_acquisition_clerical_acceptance_secondary_recipient_modifier
- celestial_hierarchy_acceptance_modifier
- legalism_lawful_authority_acceptance_modifier
- celestial_hierarchy_external_ruler_puppet_acceptance_modifier
- secular_to_ecclesiastical_pam_factors_acceptance_modifier
- seek_indulgences_acceptance_modifier
- ask_for_gold_acceptance_modifier
- clerical_petition_to_authority_acceptance_modifier
- clerical_petition_displace_incumbent_acceptance_modifier
- theocratic_related_puppet_acceptance_factors_modifier

### 00_romance_and_seduction_scripted_modifiers.txt（2 条目）

- incest_acceptance_modifier
- simple_attraction_modifier

### 00_scheme_scripted_modifiers.txt（38 条目）

- laamp_contract_scheme_basic_success_chance_modifier
- scheme_type_skill_success_chance_modifier
- apply_calculated_scheme_success_chance_adjustments_modifier
- apply_opportunistic_scheme_success_chance_adjustments_modifier
- apply_indirect_scheme_success_chance_adjustments_modifier
- apply_indirect_scheme_title_success_chance_adjustments_modifier
- apply_political_scheme_success_chance_adjustments_modifier
- apply_political_scheme_title_success_chance_adjustments_modifier
- ai_agent_join_chance_basic_suite_modifier
- ai_agent_join_chance_hostile_general_suite_modifier
- ai_agent_join_chance_personal_general_suite_modifier
- ai_agent_join_chance_hostile_taboo_modifier
- ai_agent_join_chance_hostile_grievous_modifier
- ai_agent_join_chance_personal_inoffensive_modifier
- ai_agent_join_chance_laamp_contract_modifier
- ai_agent_join_chance_political_suite_modifier
- scheme_prep_ai_should_execute_scheme_modifier
- diarch_scheming_within_realm_bonus_modifier
- diarch_scheming_title_within_realm_bonus_modifier
- owner_aspect_skill_modifier
- target_share_aspect_skill_modifier
- not_share_aspect_modifier
- target_suzerain_share_aspect_skill_modifier
- political_scheme_base_chance_modifier
- political_scheme_title_base_chance_modifier
- political_scheme_admin_base_chance_modifier
- political_scheme_title_admin_base_chance_modifier
- mandala_scheme_base_chance_modifier
- dangerous_hostile_scheme_base_chance_modifier
- dangerous_hostile_scheme_title_base_chance_modifier
- diplomacy_scheme_base_chance_modifier
- hostile_scheme_base_chance_modifier
- hostile_scheme_title_base_chance_modifier
- ai_agent_join_chance_hostile_title_modifier
- house_feud_hostile_scheme_title_success_modifier
- hostile_scheme_agent_success_chance_modifier
- start_hostile_scheme_ai_base_modifiers
- personal_scheme_base_success_chance_modifiers

### 00_scripted_relations_scripted_modifiers.txt（2 条目）

- best_friend_event_weight_modifier
- nemesis_event_weight_modifier

### 00_single_combat_scripted_modifiers.txt（9 条目）

- sce_timid_personality_scripted_modifier
- sce_preferred_timid_personality_scripted_modifier
- sce_rational_personality_scripted_modifier
- sce_preferred_rational_personality_scripted_modifier
- sce_aggressive_personality_scripted_modifier
- sce_preferred_aggressive_personality_scripted_modifier
- sce_enjoys_arrogant_speeches_scripted_modifier
- sce_shrewd_fighter_scripted_modifier
- sce_preferred_shrewd_fighter_scripted_modifier

### 00_spouse_scripted_modifiers.txt（0 条目）

（无顶层块）

### 00_statecraft_lifestyle_scripted_modifiers.txt（1 条目）

- governance_ongoing_4082_vassal_weight_modifier

### 00_trait_specific_scripted_modifiers.txt（1 条目）

- trait_specific_poet_good_relations_modifier

### 00_voter_strength_scripted_modifiers.txt（1 条目）

- elector_voting_strength_byzantine_elective_modifier

### 00_weather_modifiers.txt（2 条目）

- county_has_snow_suitable_for_activities
- character_capital_has_snow_suitable_for_activities

### 00_yearly_events_scripted_modifiers.txt（2 条目）

- yearly_event_0001_skill_differential_modifier
- yearly_0001_success_modifier

### 01_bp1_scripted_modifiers.txt（4 条目）

- house_feud_hostile_scheme_agent_modifier
- house_feud_hostile_scheme_success_modifier
- house_feud_title_hostile_scheme_success_modifier
- house_feud_sway_scheme_success_modifier

### 01_fp1_scripted_modifiers.txt（1 条目）

- fp1_jomsvikings_approve_of_extra_piety_and_prestige_modifier

### 02_ep1_scripted_modifiers.txt（8 条目）

- ep1_weight_up_for_court_type_modifier
- ep1_pay_homage_nickname_taken_modifier
- ep1_2020_maa_regiment_modifier
- ep1_make_mendicants_likely_modifier
- ep1_chance_stealing_damaging_artifacts_modifier
- employer_boon_child_ai_chance_modifier
- employer_boon_treatment_ai_chance_modifier
- employer_boon_artifact_ai_chance_modifier

### 03_fp2_scripted_modifiers.txt（12 条目）

- fp2_ritual_best_friendship_interactions_ai_accept_modifier
- fp2_ritual_best_friendship_interactions_ai_chance_modifier
- bg_play_move_type_effect_extraneous_advantages_self_modifier
- bg_play_move_type_effect_extraneous_advantages_opponent_modifier
- bg_ai_weight_choices_by_skill_modifier
- fp2_struggle_set_ai_agenda_common_modifiers
- fp2_struggle_set_ai_agenda_compromise_modifiers
- fp2_struggle_set_ai_agenda_conciliation_modifiers
- fp2_struggle_set_ai_agenda_hostility_modifiers
- fp2_struggle_set_ai_agenda_opportunity_modifiers
- fp2_council_toledo_attendee_modifier
- fp2_contracting_ally_modifier

### 04_ep2_scripted_modifiers.txt（11 条目）

- activity_recurring_character_weight_modifier
- tournament_pas_darmes_culture_tradition_modifier
- tournament_duelists_modifier
- tournament_horse_contest_trait_pivotal_modifier
- tournament_foot_contest_trait_pivotal_modifier
- tournament_wit_contest_trait_pivotal_modifier
- tournament_bow_contest_trait_pivotal_modifier
- tournament_contest_winner_determiner_modifier
- wedding_similiar_family_member_modifier
- wedding_family_member_compatibility_modifier
- tournament_team_captain_modifier

### 05_bp2_scripted_modifiers.txt（15 条目）

- bp2_hostage_relative_strength_modifier
- bp2_hostage_claims_casus_bellis_modifier
- bp2_hostage_vassals_lieges_modifier
- bp2_hostage_recall_vassals_lieges_modifier
- bp2_hostage_tier_neighbor_modifier
- bp2_hostage_recall_tier_neighbor_modifier
- bp2_hostage_culture_faith_modifier
- bp2_hostage_relation_modifier
- bp2_hostage_dread_modifier
- bp2_hostage_importance_exchange_modifier
- bp2_hostage_offer_personality_modifier
- bp2_hostage_demand_personality_modifier
- bp2_hostage_exchange_personality_modifier
- bp2_hostage_return_personality_modifier
- bp2_hostage_recipient_cultural_traditions_modifier

### 05_fp3_scripted_modifiers.txt（8 条目）

- evaluate_action_decreasing_house_unity
- evaluate_action_increasing_house_unity
- fp3_challenge_house_head_negotiation_bargain_modifier
- fp3_challenge_house_head_negotiation_reject_modifier
- fp3_challenge_house_head_negotiation_strength_modifier
- fp3_struggle_0001_change_sides_weight_modifier
- fp3_struggle_resist_allied_wars_modifier
- fp3_misc_decisions_0031_preferred_cultrads_modifier

### 07_ep3_scripted_modifiers.txt（8 条目）

- laamp_improved_learning_contract_success_modifier
- laamp_improved_tracker_contract_success_modifier
- laamp_weight_up_minor_chars_modifier
- liege_offer_co_emperorship_to_faction_leader_modifier
- court_position_boon_aptitude_modifier
- court_position_boon_aptitude_multi_modifier
- demand_admin_acceptance_modifier
- ep3_adventurer_ai_contract_find_next_kingdom_modifier

### 09_mpo_scripted_modifiers.txt（1 条目）

- mpo_blood_brother_interactions_ai_accept_modifier

### 10_ach_scripted_modifiers.txt（3 条目）

- ach_likely_plotter_modifier
- ach_unlikely_plotter_modifier
- ach_squabbler_modifier

### 10_tgp_faction_modifiers.txt（2 条目）

- replace_ceremonial_regent_faction_modifiers
- restore_ceremonial_liege_faction_modifiers

### 10_tgp_japan_modifiers.txt（6 条目）

- japanese_new_house_name_modifiers
- japan_demand_admin_acceptance_modifier
- house_relation_ai_accept_modifiers
- house_relation_ai_accept_confederation_member_modifiers
- house_bloc_desire_to_join_modifiers
- house_bloc_tyranny_war_modifiers

### 10_tgp_scripted_modifiers.txt（4 条目）

- mentor_positive_evaluation_modifiers
- mentor_negative_evaluation_modifiers
- mentor_balanced_evaluation_modifiers
- tribute_mission_decision_ai_will_do_modifiers

### pam_scripted_modifiers.txt（1 条目）

- ecclesiastical_domicile_cathedral_awe_modifier

### tgp_mandala_scripted_modifiers.txt（13 条目）

- mandala_devaraja_piety_level_remove_weight_modifier
- mandala_devaraja_piety_level_add_weight_modifier
- subject_realm_size_add_weight_modifier
- subject_realm_size_lose_weight_modifier
- mandala_devaraja_capital_remove_weight_modifier
- mandala_devaraja_capital_min_third_remove_weight_modifier
- mandala_devaraja_capital_add_weight_modifier
- mandala_devaraja_capital_min_third_add_weight_modifier
- mandala_devaraja_actor_amount_of_subjects_add_weight_modifier
- mandala_devaraja_actor_amount_of_subjects_remove_weight_modifier
- mandala_devaraja_recipient_amount_of_subjects_add_weight_modifier
- mandala_devaraja_recipient_amount_of_subjects_remove_weight_modifier
- turn_subject_into_mandala_acceptance_modifier

### 未解析文件

- `_scripted_modifiers.info` — 纯文档（非 Jomini）
