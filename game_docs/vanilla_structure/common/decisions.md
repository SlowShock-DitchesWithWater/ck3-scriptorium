# common/decisions 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：77（其中 Jomini 解析 76 个）
- 顶层块条目总数：501，跨文件唯一条目 501
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_artifact_decisions.txt` | 17440 | 1 | 0 | jomini |
| `00_cultural_tradition_decisions.txt` | 17148 | 3 | 0 | jomini |
| `00_diarchy_decisions.txt` | 8351 | 1 | 0 | jomini |
| `00_dynasty_decisions.txt` | 8178 | 1 | 0 | jomini |
| `00_fp3_decisions.txt` | 13957 | 1 | 0 | jomini |
| `00_guest_decisions.txt` | 7348 | 4 | 0 | jomini |
| `00_holy_order_decisions.txt` | 27955 | 5 | 0 | jomini |
| `00_lifestyle_decisions.txt` | 14409 | 8 | 8 | jomini |
| `00_major_decisions_east_europe.txt` | 32251 | 11 | 0 | jomini |
| `00_major_decisions_iberia_north_africa.txt` | 31460 | 8 | 0 | jomini |
| `00_trait_decisions.txt` | 6475 | 3 | 4 | jomini |
| `00_unity_decisions.txt` | 34099 | 14 | 0 | jomini |
| `04_ep2_decisions.txt` | 2041 | 1 | 0 | jomini |
| `06_ce1_decisions.txt` | 27435 | 5 | 0 | jomini |
| `10_ach_oath_decisions.txt` | 38881 | 17 | 0 | jomini |
| `10_culture_conversion_decisions.txt` | 13274 | 2 | 0 | jomini |
| `10_nomad_culture_and_faith_decisions.txt` | 13377 | 6 | 0 | jomini |
| `10_nomad_other_decisions.txt` | 9584 | 3 | 0 | jomini |
| `10_religious_decisions.txt` | 79231 | 30 | 0 | jomini |
| `30_activity_decisions.txt` | 30464 | 2 | 0 | jomini |
| `30_court_decisions.txt` | 10141 | 1 | 0 | jomini |
| `30_mongol_invasion_decisions.txt` | 6415 | 1 | 0 | jomini |
| `40_japan_decisions.txt` | 16270 | 2 | 0 | jomini |
| `50_holy_site_decisions.txt` | 19864 | 6 | 0 | jomini |
| `80_major_decisions.txt` | 79302 | 23 | 0 | jomini |
| `80_major_decisions_british_isles.txt` | 25254 | 8 | 0 | jomini |
| `80_major_decisions_central_asia.txt` | 11745 | 4 | 0 | jomini |
| `80_major_decisions_east_asia.txt` | 15160 | 6 | 0 | jomini |
| `80_major_decisions_middle_east.txt` | 23184 | 10 | 0 | jomini |
| `80_major_decisions_middle_europe.txt` | 31104 | 10 | 0 | jomini |
| `80_major_decisions_roman.txt` | 36990 | 16 | 0 | jomini |
| `80_major_decisions_south_asia.txt` | 15238 | 5 | 0 | jomini |
| `90_minor_decisions.txt` | 60576 | 24 | 0 | jomini |
| `_decisions.info` | 15416 | - | - | 纯文档（非 Jomini） |
| `clerical_chastity_decisions.txt` | 1127 | 1 | 0 | jomini |
| `dlc_decisions/03_fp2_decisions.txt` | 42875 | 11 | 0 | jomini |
| `dlc_decisions/bp3/00_bp3_other_decisions.txt` | 23819 | 6 | 0 | jomini |
| `dlc_decisions/bp_2/00_bp2_other_decisions.txt` | 3305 | 1 | 0 | jomini |
| `dlc_decisions/ce_1/ce1_legendary_decisions.txt` | 10382 | 8 | 0 | jomini |
| `dlc_decisions/ep3_decisions.txt` | 81362 | 25 | 0 | jomini |
| `dlc_decisions/ep_1/00_ep1_court_grandeur_and_amenity_decisions.txt` | 7434 | 2 | 0 | jomini |
| `dlc_decisions/ep_1/00_ep1_other_decisions.txt` | 13028 | 4 | 0 | jomini |
| `dlc_decisions/ep_2/00_ep2_other_decisions.txt` | 3592 | 1 | 0 | jomini |
| `dlc_decisions/ep_3/06_ep3_admin_decisions.txt` | 44656 | 10 | 0 | jomini |
| `dlc_decisions/ep_3/06_ep3_hasan_story_cycle_decisions.txt` | 11159 | 5 | 0 | jomini |
| `dlc_decisions/ep_3/06_ep3_laamp_decisions.txt` | 83293 | 20 | 6 | jomini |
| `dlc_decisions/ep_3/06_ep3_separatist_uprising_decision.txt` | 2777 | 1 | 0 | jomini |
| `dlc_decisions/fp3_decisions.txt` | 38089 | 6 | 0 | jomini |
| `dlc_decisions/fp_1/00_fp1_major_decisions.txt` | 16428 | 4 | 0 | jomini |
| `dlc_decisions/fp_1/00_fp1_other_decisions.txt` | 3045 | 1 | 0 | jomini |
| `dlc_decisions/fp_3/fp3_dynasty_decisions.txt` | 15776 | 1 | 0 | jomini |
| `dlc_decisions/fp_3/fp3_islamic_decisions.txt` | 12994 | 3 | 0 | jomini |
| `dlc_decisions/fp_3/fp3_minor_decisions.txt` | 1129 | 1 | 0 | jomini |
| `dlc_decisions/fp_3/fp3_scholarship_decisions.txt` | 6831 | 2 | 0 | jomini |
| `dlc_decisions/fp_3/fp3_zoroastrian_decisions.txt` | 9645 | 4 | 0 | jomini |
| `dlc_decisions/mpo/09_mpo_decisions_2.txt` | 4020 | 3 | 0 | jomini |
| `dlc_decisions/mpo/mpo_court_astrologer_decision.txt` | 1425 | 1 | 0 | jomini |
| `dlc_decisions/mpo/mpo_decisions.txt` | 159206 | 15 | 0 | jomini |
| `dlc_decisions/mpo/mpo_flavor_decision.txt` | 17246 | 5 | 0 | jomini |
| `dlc_decisions/mpo/mpo_pax_mongolica_decision.txt` | 2696 | 1 | 0 | jomini |
| `dlc_decisions/pam/bulls_decisions.txt` | 23585 | 5 | 0 | jomini |
| `dlc_decisions/pam/pam_adorcism_decisions.txt` | 5815 | 2 | 0 | jomini |
| `dlc_decisions/pam/pam_antipope_decisions.txt` | 13445 | 2 | 0 | jomini |
| `dlc_decisions/pam/pam_decisions.txt` | 162556 | 39 | 0 | jomini |
| `dlc_decisions/pam/pam_saint_decisions.txt` | 19643 | 3 | 0 | jomini |
| `dlc_decisions/tgp/tgp_china_decisions.txt` | 39788 | 12 | 0 | jomini |
| `dlc_decisions/tgp/tgp_culture_decisions.txt` | 3685 | 1 | 0 | jomini |
| `dlc_decisions/tgp/tgp_dynastic_cycle_decisions.txt` | 94204 | 11 | 0 | jomini |
| `dlc_decisions/tgp/tgp_east_asia_decisions.txt` | 20611 | 7 | 0 | jomini |
| `dlc_decisions/tgp/tgp_japan_decisions.txt` | 45987 | 14 | 0 | jomini |
| `dlc_decisions/tgp/tgp_korea_decisions.txt` | 2893 | 1 | 0 | jomini |
| `dlc_decisions/tgp/tgp_silk_road_decisions.txt` | 12984 | 1 | 0 | jomini |
| `dlc_decisions/tgp/tgp_steppe_decisions.txt` | 14269 | 3 | 0 | jomini |
| `dlc_decisions/tgp/tgp_tenet_decisions.txt` | 3224 | 1 | 0 | jomini |
| `dlc_decisions/tgp/tgp_tribute_mission_decisions.txt` | 22928 | 6 | 0 | jomini |
| `test_decision.txt` | 8336 | 8 | 0 | jomini |
| `tutorial_decisions.txt` | 34981 | 1 | 0 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_artifact_decisions.txt（1 条目）

- commission_artifact_decision

### 00_cultural_tradition_decisions.txt（3 条目）

- recruit_terrain_specialist_decision
- embrace_hebrew_language_decision
- sacrifice_bear_decision

### 00_diarchy_decisions.txt（1 条目）

- diarch_attempt_to_overthrow_liege

### 00_dynasty_decisions.txt（1 条目）

- create_cadet_branch_decision

### 00_fp3_decisions.txt（1 条目）

- adopt_a_new_faith_for_persia_decision

### 00_guest_decisions.txt（4 条目）

- invite_knights_decision
- invite_claimants_decision
- scrape_the_barrel_decision
- invite_poets_decision

### 00_holy_order_decisions.txt（5 条目）

- create_holy_order_decision
- borrow_from_holy_order_decision
- cancel_holy_order_lease_decision
- create_holy_order_monastic_decision
- pam_monastic_order_new_movement_decision

### 00_lifestyle_decisions.txt（8 条目）

- embrace_celibacy_decision
- abandon_celibacy_decision
- sale_of_titles_decision
- extort_subjects_decision
- commission_epic_decision
- hold_mystical_communion_decision
- local_arbitration_decision
- draw_up_new_charts_decision

### 00_major_decisions_east_europe.txt（11 条目）

- unite_the_western_slavs_decision
- unite_the_southern_slavs_decision
- unite_the_slavs_decision
- defenders_of_highgod_decision
- promote_hungarian_settlement_decision
- revive_magyar_paganism_decision
- found_kingdom_of_bosnia_decision
- found_kingdom_of_albania_decision
- accuse_krstjani_of_heresy_decision
- launch_hungarian_migration_decision
- found_kingdom_of_livonia_decision

### 00_major_decisions_iberia_north_africa.txt（8 条目）

- form_portugal_decision
- unite_the_spanish_thrones_decision
- unite_africa_decision
- avenge_the_battle_of_tours_decision
- declare_canarias_decision
- form_the_kingdom_of_aragon_decision
- favour_the_countryside_basques_decision
- restore_old_vasconia_decision

### 00_trait_decisions.txt（3 条目）

- deceitful_progress_hostile_schemes_decision
- diligent_development_focus_decision
- impatient_rushing_all_schemes_decision

### 00_unity_decisions.txt（14 条目）

- unity_reinforce_army_decision
- unity_establish_network_decision
- unity_improve_taxation_decision
- unity_send_bailiffs_decision
- unity_placate_vassals_decision
- unity_organize_house_for_war_decision
- unity_encourage_house_economy_decision
- unity_steer_house_direction_decision
- unity_search_for_administrators_decision
- unity_improve_logistics_decision
- unity_promote_development_decision
- unity_consult_house_decision
- unity_establish_futuwaa_lodges_decision
- unity_educate_youth_in_madrasas_decision

### 04_ep2_decisions.txt（1 条目）

- decision_solve_the_journals

### 06_ce1_decisions.txt（5 条目）

- commission_legend_artifact_decision
- clear_ground_for_legendary_building
- pick_legendary_barony_decision
- isolate_capital_decision
- isolate_family_decision

### 10_ach_oath_decisions.txt（17 条目）

- diplomacy_oath_1_decision
- diplomacy_oath_2_decision
- martial_oath_1_decision
- martial_oath_2_decision
- stewardship_oath_1_decision
- stewardship_oath_2_decision
- learning_oath_1_decision
- purge_pretenders_oath_decision
- end_the_struggle_oath_decision
- greatest_hunter_oath_decision
- heir_preparation_oath_decision
- install_claimants_oath_decision
- mend_the_fracture_oath_decision
- provide_for_the_warriors_oath_decision
- provide_for_the_faithful_oath_decision
- provide_for_the_poor_oath_decision
- repent_oath_decision

### 10_culture_conversion_decisions.txt（2 条目）

- convert_to_local_culture_decision
- assimilate_local_traditions_decision

### 10_nomad_culture_and_faith_decisions.txt（6 条目）

- embrace_tengriism_decision
- proselytize_to_your_people_decision
- adopt_domicile_faith_decision
- adopt_domicile_culture_decision
- blend_traditions_decision
- enforce_traditions_decision

### 10_nomad_other_decisions.txt（3 条目）

- recruit_from_nomadic_capital_decision
- summon_fair_courtiers_decision
- create_cossack_kingdom_decision

### 10_religious_decisions.txt（30 条目）

- take_vow_of_poverty_decision
- renounce_vow_of_poverty_decision
- renounce_clerical_vows_decision
- initiate_consolamentum_decision
- seek_aid_of_the_spirits_decision
- preserve_wilderness_decision
- select_personal_deity_hinduism_decision
- select_personal_deity_germanic_decision
- meditate_in_seclusion_decision
- promote_naturism_decision
- renounce_court_naturism_decision
- give_sky_burial_decision
- raise_runestone_decision
- divine_the_stars_decision
- revoke_false_conversion_decision
- encourage_confession_of_false_conversions_decision
- abandon_crypto_faith_decision
- return_rome_decision
- invite_religious_exiles_decision
- convert_to_confucianism
- convert_to_taoism
- petition_head_of_faith_decision
- petition_antipope_decision
- seek_spiritual_mysteries_decision
- pure_land_shed_sin_decision
- seek_ancestral_guidance_decision
- inherit_ancestral_trait_decision
- pursue_conquerors_mantle_decision
- redistribute_realm_wealth_decision
- launch_undirected_great_holy_war_decision

### 30_activity_decisions.txt（2 条目）

- hold_court_decision
- petition_liege_decision

### 30_court_decisions.txt（1 条目）

- pay_homage_decision

### 30_mongol_invasion_decisions.txt（1 条目）

- submit_to_the_great_khan_decision

### 40_japan_decisions.txt（2 条目）

- pledge_loyalty_to_liege_decision
- petition_ceremonial_liege_decision

### 50_holy_site_decisions.txt（6 条目）

- elevate_holy_site_decision
- demote_holy_site_decision
- abandon_holy_site_decision
- adopt_holy_site_decision
- ai_enshrine_artifact_decision
- ai_remove_enshrined_artifact_decision

### 80_major_decisions.txt（23 条目）

- convert_to_feudalism_liege_converted_decision
- convert_clan_to_feudalism_through_liege_decision
- convert_feudalism_to_clan_through_liege_decision
- convert_whole_realm_to_feudalism_decision
- convert_to_tribalism_decision
- convert_whole_realm_to_feudalism_west_african_pagan_decision
- declare_bloodline_holy_decision
- strengthen_bloodline_decision
- dynasty_of_many_crowns_decision
- found_kingdom_decision
- found_empire_decision
- adopt_special_succession_decision
- tribal_challenge_ruler_decision
- accept_cannibalism_decision
- found_university_decision
- lunatic_building_decision
- found_witch_coven_decision
- repay_loan_decision
- escape_from_prison_decision
- found_duchy_decision
- expand_duchy_decision
- set_de_jure_capital_decision
- restore_carthage_decision

### 80_major_decisions_british_isles.txt（8 条目）

- reclaim_britannia_decision
- embrace_english_culture_decision
- england_request_laudabiliter_decision
- negotiate_the_danelaw_decision
- negotiate_the_danelaw_integrate_duchies_decision
- formalise_the_daneland_decision
- restore_dumnonia_decision
- form_cumbria_decision

### 80_major_decisions_central_asia.txt（4 条目）

- become_greatest_of_khans_decision
- establish_bactrian_supremacy_decision
- establish_yamagate_in_samarkand_decision
- break_with_the_old_ways_decision

### 80_major_decisions_east_asia.txt（6 条目）

- form_dai_viet_empire_decision
- form_majapahit_empire_decision
- form_ryukyu_empire_decision
- form_siam_kingdom_decision
- form_brunei_kingdom_decision
- form_brunei_empire_decision

### 80_major_decisions_middle_east.txt（10 条目）

- create_outremer_empire_decision
- restore_sunni_caliphate_decision
- embrace_outremer_culture_decision
- create_israel_kingdom_decision
- jewish_restore_high_priesthood_decision
- zoroastrian_restore_high_priesthood_decision
- become_saoshyant_decision
- create_armenian_empire_decision
- found_empire_of_beth_nahrain_decision
- create_dar_al_islam_decision

### 80_major_decisions_middle_europe.txt（10 条目）

- form_switzerland_kingdom_decision
- form_austria_kingdom_decision
- reform_carolingian_empire_decision
- unify_burgundy_kingdom_decision
- empower_sicilian_parliament_decision
- promote_gothic_innovations_decision
- restore_holy_roman_empire_decision
- establish_norman_culture_decision
- establish_the_electorate_of_saxony_decision
- decision_restore_carantania

### 80_major_decisions_roman.txt（16 条目）

- restore_roman_empire_decision
- restore_roman_empire_holy_decision
- restore_roman_empire_italian_decision
- form_rum_sultanate_decision
- mend_the_great_schism_decision
- set_capital_constantinople_decision
- set_capital_rome_decision
- establish_iconoclast_patriarchate_decision
- restore_ecumenical_patriarchate_decision
- restore_papacy_decision
- restore_pope_in_rome_decision
- dismantle_papacy_decision
- unify_italian_empire_decision
- dismantle_holy_pretender_decision
- dismantle_byz_pretender_decision
- rebuke_roman_revanchism_sicily

### 80_major_decisions_south_asia.txt（5 条目）

- become_chakravarti_decision
- take_stewardship_of_the_sacred_river_decision
- form_bene_israel_decision
- spread_theravada_faith_decision
- found_the_empire_of_hindustan_decision

### 90_minor_decisions.txt（24 条目）

- recruit_court_position_decision
- gain_weight_decision
- stop_gain_weight_decision
- lose_weight_decision
- stop_lose_weight_decision
- commit_suicide_decision
- secede_from_empire_decision
- pet_dog_decision
- pet_cat_decision
- stress_loss_drunkard_decision
- stress_loss_hashishiyah_decision
- stress_loss_rakish_decision
- stress_loss_reclusive_decision
- stress_loss_irritable_decision
- stress_loss_flagellant_decision
- stress_loss_profligate_decision
- stress_loss_improvident_decision
- stress_loss_contrite_decision
- stress_loss_comfort_eater_decision
- stress_loss_inappetetic_decision
- stress_loss_journaller_decision
- stress_loss_confider_decision
- stress_loss_athletic_decision
- write_muwashshah_poem_decision

### clerical_chastity_decisions.txt（1 条目）

- renounce_clerical_chastity_vow_decision

### dlc_decisions/03_fp2_decisions.txt（11 条目）

- struggle_iberia_ending_hostility_decision
- struggle_iberia_ending_compromise_decision
- struggle_iberia_ending_conciliation_decision
- secure_mediterranean_decision
- eat_cheese_decision
- golden_age_jewish_science_in_iberia_decision
- council_of_toledo_decision
- secure_iberian_foothold_decision
- build_holy_pilgrim_roads_decision
- found_kingdom_toledo_decision
- improve_city_province_decision

### dlc_decisions/bp3/00_bp3_other_decisions.txt（6 条目）

- end_investments_minor_decision
- choose_designated_terrain_decision
- choose_master_terrain_decision
- form_bosporan_kingdom_decision
- merge_aquitaine_decision
- enact_legacy_of_adventurer_decision

### dlc_decisions/bp_2/00_bp2_other_decisions.txt（1 条目）

- rites_of_passage_decision

### dlc_decisions/ce_1/ce1_legendary_decisions.txt（8 条目）

- legend_demand_fealty
- launch_a_legendary_adventure
- legendary_integration_e
- legendary_integration_k
- legendary_integration_d
- legendary_holy_war
- legendary_pacifism_spread
- legendary_conversion

### dlc_decisions/ep3_decisions.txt（25 条目）

- hold_triumph_decision
- restore_backwater_counties_decision
- prepare_greek_fire_dromons_decision
- retake_eastern_provinces_decision
- refound_pandidakterion_decision
- ask_western_help_decision
- evangelize_the_slavs_decision
- recreate_byzantine_empire_decision
- found_varangian_guard_decision
- reinstitute_grain_dole_decision
- reconfirm_grain_dole_decision
- change_state_faith
- adopt_state_faith
- found_salon_decision
- split_roman_empire_decision
- commission_icon_decision
- embrace_heresy_decision
- push_heresy_as_state_faith
- establish_silk_production_decision
- commission_silk_regalia_decision
- foster_integration_decision
- gather_faction_support_decision
- legitimize_latin_dominion_decision
- expunge_latin_dominion_decision
- go_fishing_decision

### dlc_decisions/ep_1/00_ep1_court_grandeur_and_amenity_decisions.txt（2 条目）

- order_mass_eviction_decision
- exoticise_a_grand_hall_decision

### dlc_decisions/ep_1/00_ep1_other_decisions.txt（4 条目）

- jester_entertainment_decision
- adopt_puppy_decision
- introduce_a_new_fashion_at_court_decision
- promote_other_culture_development_decision

### dlc_decisions/ep_2/00_ep2_other_decisions.txt（1 条目）

- train_for_tournament_decision

### dlc_decisions/ep_3/06_ep3_admin_decisions.txt（10 条目）

- estate_hire_agents_decisions
- estate_bolster_security_decision
- estate_governor_patrols_decision
- estate_granary_decision
- admin_confirmation_decision
- consolidate_rule_decision
- convert_to_administrative_decision
- convert_to_feudalism_from_administrative_decision
- renounce_governorship_decision
- change_imperial_aspirations_decision

### dlc_decisions/ep_3/06_ep3_hasan_story_cycle_decisions.txt（5 条目）

- hasan_evangelize_the_faith
- hasan_agitate_the_populace
- hasan_ignite_the_flames
- hasan_found_the_assassins
- hasan_expand_the_assassins

### dlc_decisions/ep_3/06_ep3_laamp_decisions.txt（20 条目）

- become_landless_adventurer_decision
- wipe_slate_decision
- adopt_a_kennel_dog
- treasure_hunting_contract_decision
- visit_local_settlement_decision
- treasure_map_contract_decision
- reject_inheritance_decision
- renounce_vows_decision
- embrace_responsibilities_decision
- change_election_candidacy_status_decision
- bandit_king_decision
- gather_provisions_decision
- seasoned_visitor_decision
- zealous_missionary_prep_decision
- zealous_missionary_start_decision
- become_conqueror_decision
- start_city_construction_decision
- knight_errant_decision
- butcher_animals_decision
- humiliate_the_stooge_decision

### dlc_decisions/ep_3/06_ep3_separatist_uprising_decision.txt（1 条目）

- separatist_uprising_decision

### dlc_decisions/fp3_decisions.txt（6 条目）

- struggle_persia_ending_assertion_decision
- struggle_persia_ending_foundation_decision
- struggle_persia_ending_rekindle_iran_decision
- favour_skilled_outsiders_decision
- fp3_sunder_the_caliphate_decision
- fp3_become_clan_government_decision

### dlc_decisions/fp_1/00_fp1_major_decisions.txt（4 条目）

- secure_high_kingdom_north_sea_decision
- found_capital_of_the_rus_decision
- elevate_mann_and_the_isles_decision
- forge_the_jomsvikings_decision

### dlc_decisions/fp_1/00_fp1_other_decisions.txt（1 条目）

- raise_stele_decision

### dlc_decisions/fp_3/fp3_dynasty_decisions.txt（1 条目）

- fp3_embellish_capital_decision

### dlc_decisions/fp_3/fp3_islamic_decisions.txt（3 条目）

- avenge_the_battle_of_nahrawan_decision
- fp3_promote_persian_scripture_decision
- fp3_name_read_in_friday_prayer_decision

### dlc_decisions/fp_3/fp3_minor_decisions.txt（1 条目）

- fp3_play_with_buzina_decision

### dlc_decisions/fp_3/fp3_scholarship_decisions.txt（2 条目）

- fp3_sponsor_persian_scholars_decision
- fp3_sponsor_research_project_decision

### dlc_decisions/fp_3/fp3_zoroastrian_decisions.txt（4 条目）

- restore_badd_fortress_decision
- destroy_the_magi_decision
- kindle_royal_fire_decision
- fp3_embrace_zoroastrianism_decision

### dlc_decisions/mpo/09_mpo_decisions_2.txt（3 条目）

- pray_to_protective_amulet_decision
- mpo_desperate_stance_decision
- adopt_nomadic_ways_decision

### dlc_decisions/mpo/mpo_court_astrologer_decision.txt（1 条目）

- mpo_divination_decision

### dlc_decisions/mpo/mpo_decisions.txt（15 条目）

- call_for_confederation_decision
- leave_confederation_decision
- study_commander_trait_decision
- mpo_decision_fertility_dance
- mpo_decision_introduce_heir
- expand_the_steppe_decision
- develop_fertility_decision
- nomad_higher_tier_title_decision
- mpo_become_greatest_of_khans_decision
- mpo_gok_world_conquest_decision
- settle_people_decision
- step_away_from_the_steppe_decision
- confederation_kingdom_decision
- settle_the_steppe_decision
- become_nomadic_decision

### dlc_decisions/mpo/mpo_flavor_decision.txt（5 条目）

- mpo_pleasure_dome_decision
- mpo_establish_paiza_system_decision
- mpo_call_for_merchants_decision
- mpo_call_for_merchants_small_decision
- mpo_abuse_authority_paiza_decision

### dlc_decisions/mpo/mpo_pax_mongolica_decision.txt（1 条目）

- mpo_pax_mongolica_decision

### dlc_decisions/pam/bulls_decisions.txt（5 条目）

- enact_a_bull_decision
- pick_crusade_target_decision
- pam_declare_rite_heresy_bull_decision
- pam_permit_tenet_bull_decision
- pam_prohibit_tenet_bull_decision

### dlc_decisions/pam/pam_adorcism_decisions.txt（2 条目）

- pam_curse_enemy_decision
- pam_seek_war_aid_decision

### dlc_decisions/pam/pam_antipope_decisions.txt（2 条目）

- declare_antipope_decision
- declare_yourself_antipope_decision

### dlc_decisions/pam/pam_decisions.txt（39 条目）

- pam_decision_confession
- pam_decision_act_of_devotion
- pam_mentor_sp_decision
- pam_establish_theocratic_dynasty_decision
- pam_convert_to_theocracy_decision
- pam_convert_theocracy_to_feudal_decision
- pam_kowtow_to_pope_decision
- pam_determine_patron_saint_decision
- pam_decision_last_rites
- create_hof_decision
- pam_levy_the_tithes_decision
- pam_send_legatine_mission_decision
- pam_reform_monastic_endowment_decision
- pam_shape_the_christian_church_decision
- pam_kingdom_of_heaven_decision
- pam_proclaim_living_word_decision
- pam_prevent_great_schism_decision
- pam_cause_great_schism_decision
- pam_mend_great_schism_decision
- pam_unite_miaphysite_churches_decision
- pam_promulgate_word_of_pious_deeds_decision
- pam_cardinal_endow_masses_decision
- pam_renounce_papal_candidacy_decision
- pam_declare_rite_heresy_decision
- pam_permit_tenet_decision
- pam_prohibit_tenet_decision
- pam_raise_khachkar_decision
- pam_proclaim_crusade_age_tenet_decision
- pam_secure_pilgrim_routes_decision
- pam_evangelize_personal_tenet_decision
- pam_persecute_tenet_decision
- consecrate_kingdom_decision
- pam_prepare_holy_myron_decision
- pam_anoint_artifact_decision
- pam_invite_syncretic_exiles_decision
- pam_study_scripture_decision
- pam_personal_sacrifice_of_wealth_decision
- pam_develop_clerical_court_decision
- pam_seize_capital_clerical_region_decision

### dlc_decisions/pam/pam_saint_decisions.txt（3 条目）

- pam_canonize_saint_decision
- pam_choose_consecration_site_decision
- pam_extract_relic_decision

### dlc_decisions/tgp/tgp_china_decisions.txt（12 条目）

- tgp_china_attend_child_exam_decision
- tgp_command_family_to_take_exams_decision
- tgp_choose_career_path_decision
- tgp_refuse_appointments_decision
- tgp_resume_appointments_decision
- tgp_minister_request_bestowal_of_honors_decision
- tgp_minister_recruit_courtiers_decision
- tgp_china_study_confucian_classics_decision
- tgp_claim_the_mantle_of_maitreya_decision
- tgp_tea_ceremony_decision
- tgp_suggest_budget_change_decision
- extract_gold_from_treasury

### dlc_decisions/tgp/tgp_culture_decisions.txt（1 条目）

- author_book_decision

### dlc_decisions/tgp/tgp_dynastic_cycle_decisions.txt（11 条目）

- situation_dynastic_cycle_claim_mandate_decision
- situation_dynastic_cycle_favor_own_culture_for_appointments
- situation_dynastic_cycle_choose_movement_decision
- movement_petition_decision
- movement_petition_change_laws_decision
- ai_movement_petition_change_laws_decision
- renounce_noble_family_title_decision
- favor_dynastic_cycle_era_decision
- favor_movement_decision
- favored_movement_consults_heaven_decision
- house_head_consults_heaven_decision

### dlc_decisions/tgp/tgp_east_asia_decisions.txt（7 条目）

- restore_mandala_capital_decision
- convert_to_mandala_government_decision
- assimilate_to_mandala_decision
- mandala_adopt_clan_government_decision
- visit_local_shrine_decision
- seize_mandala_capital_decision
- create_bunga_mas_decision

### dlc_decisions/tgp/tgp_japan_decisions.txt（14 条目）

- tgp_japan_establish_house_fief_decision
- tgp_japan_establish_soryo_manor_decision
- tgp_japan_establish_soryo_administration_decision
- tgp_japan_become_shogun_decision
- tgp_japan_emperor_restoration_decision
- tgp_japan_imperial_branch_decision
- tgp_japan_become_a_poet_decision
- tgp_japan_train_with_troops_decision
- tgp_japan_become_a_monk_decision
- tgp_japan_restore_japanese_monarchy_decision
- tgp_japan_restore_japanese_government_decision
- tgp_japan_assert_regional_dominion_government_decision
- move_shogunate_court_decision
- tgp_japan_emperor_war_decision

### dlc_decisions/tgp/tgp_korea_decisions.txt（1 条目）

- tgp_korea_unify_goryeo_decision

### dlc_decisions/tgp/tgp_silk_road_decisions.txt（1 条目）

- visit_silk_road_market_decision

### dlc_decisions/tgp/tgp_steppe_decisions.txt（3 条目）

- adopt_steppe_administration
- return_to_the_steppe_decision
- convert_to_meritocratic_decision

### dlc_decisions/tgp/tgp_tenet_decisions.txt（1 条目）

- tgp_divine_reincarnation_decision

### dlc_decisions/tgp/tgp_tribute_mission_decisions.txt（6 条目）

- tribute_mission_decision_mandala
- tribute_mission_decision_china
- tribute_mission_decision_roman_empire
- tribute_mission_decision_eastern_roman_empire
- tribute_mission_decision_dar_al_islam
- tribute_mission_decision_india

### test_decision.txt（8 条目）

- wild_goose_chase_decision
- become_leading_house_of_the_confederation_decision
- clear_our_confederations_leading_house_decision
- adjust_confederation_cohesion_decision
- change_all_house_relations_decision
- chinese_concubines_decision
- add_to_steppe_decision
- remove_from_steppe_decision

### tutorial_decisions.txt（1 条目）

- unify_region_decision

### 未解析文件

- `_decisions.info` — 纯文档（非 Jomini）
