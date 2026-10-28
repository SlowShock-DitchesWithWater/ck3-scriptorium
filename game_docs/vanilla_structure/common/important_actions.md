# common/important_actions 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：36（其中 Jomini 解析 35 个）
- 顶层块条目总数：301，跨文件唯一条目 301
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_action_take_decision_or_interaction.txt` | 4112 | 5 | 0 | jomini |
| `00_activity_actions.txt` | 9535 | 20 | 0 | jomini |
| `00_artifact_actions.txt` | 551 | 1 | 0 | jomini |
| `00_diarchy_actions.txt` | 16116 | 14 | 0 | jomini |
| `00_dynasty_actions.txt` | 424 | 1 | 0 | jomini |
| `00_education_actions.txt` | 3338 | 4 | 0 | jomini |
| `00_inheritance_actions.txt` | 12466 | 10 | 0 | jomini |
| `00_lifestyle.txt` | 3394 | 8 | 0 | jomini |
| `00_marriage_actions.txt` | 9784 | 8 | 0 | jomini |
| `00_mercenaries_actions.txt` | 469 | 1 | 0 | jomini |
| `00_personal_actions.txt` | 14546 | 12 | 0 | jomini |
| `00_raid.txt` | 1080 | 1 | 0 | jomini |
| `00_reactive_advice.txt` | 42124 | 56 | 0 | jomini |
| `00_reactive_advice_japan.txt` | 3056 | 4 | 0 | jomini |
| `00_reactive_advice_playtest.txt` | 595 | 1 | 0 | jomini |
| `00_realm_actions.txt` | 23109 | 28 | 0 | jomini |
| `00_temp_actions.txt` | 1880 | 0 | 0 | jomini |
| `00_title_actions.txt` | 2592 | 2 | 0 | jomini |
| `00_war_actions.txt` | 5892 | 5 | 0 | jomini |
| `01_bp1_actions.txt` | 744 | 1 | 0 | jomini |
| `01_ep1_actions.txt` | 4398 | 4 | 0 | jomini |
| `01_ep1_reactive_advice.txt` | 1981 | 2 | 0 | jomini |
| `01_fp1_actions.txt` | 2827 | 2 | 0 | jomini |
| `03_fp2_actions.txt` | 2905 | 2 | 0 | jomini |
| `03_fp2_reactive_advice.txt` | 785 | 1 | 0 | jomini |
| `04_ep2_actions.txt` | 2716 | 3 | 0 | jomini |
| `05_bp2_actions.txt` | 9358 | 4 | 0 | jomini |
| `05_fp3_actions.txt` | 1043 | 2 | 0 | jomini |
| `06_ce1_actions.txt` | 2651 | 4 | 0 | jomini |
| `07_ep3_actions.txt` | 7994 | 8 | 0 | jomini |
| `09_mpo_actions.txt` | 13839 | 15 | 0 | jomini |
| `10_empire_faith_gate_actions.txt` | 2210 | 1 | 0 | jomini |
| `_important_actions.info` | 3348 | - | - | 纯文档（非 Jomini） |
| `contract_actions.txt` | 16909 | 13 | 0 | jomini |
| `pam_actions.txt` | 40810 | 26 | 0 | jomini |
| `tgp_actions.txt` | 39422 | 32 | 0 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_action_take_decision_or_interaction.txt（5 条目）

- action_take_decision
- action_ask_for_pardon
- action_convert_at_war_interaction
- action_plan_great_project
- action_contribute_to_great_project

### 00_activity_actions.txt（20 条目）

- action_can_host_activity
- action_can_join_open_activity
- action_invited_to_activity
- action_awaiting_coronation
- action_active_diplomacy_oath_1
- action_active_martial_oath_1
- action_active_martial_oath_2
- action_active_stewardship_oath_1
- action_active_stewardship_oath_2
- action_active_learning_oath_1
- action_active_purge_pretenders_oath
- action_active_end_the_struggle_oath
- action_active_greatest_hunter_oath
- action_active_heir_preparation_oath
- action_active_install_claimants_oath
- action_active_mend_the_fracture_oath
- action_active_provide_for_the_warriors_oath
- action_active_provide_for_the_faithful_oath
- action_active_provide_for_the_poor_oath
- action_active_repent_oath

### 00_artifact_actions.txt（1 条目）

- action_can_reforge_artifact

### 00_diarchy_actions.txt（14 条目）

- action_end_regency
- action_swing_scales_regent
- action_swing_scales_liege_entrenched_dangerous
- action_regent_revoke
- action_regent_retract
- action_regent_imprison
- action_legal_meddling
- action_syphon_treasury
- action_shift_privileges
- action_subsidise_liege_authority
- action_designate_regent_for_hook
- action_appoint_co_emperor_junior
- action_appoint_co_emperor_adult_child
- action_appoint_co_monarch

### 00_dynasty_actions.txt（1 条目）

- action_can_choose_dynasty_perk

### 00_education_actions.txt（4 条目）

- action_send_child_to_university
- action_send_guardian_to_university
- action_send_child_to_your_university
- action_send_yourself_to_university

### 00_inheritance_actions.txt（10 条目）

- action_no_heir
- action_no_player_heir_but_replacement_exists_gameover_risk
- action_primary_heir_wrong_dynasty_no_replacement_exists
- action_primary_heir_wrong_dynasty_but_replacement_exists
- action_title_lost_from_realm_on_succession
- action_title_lost_from_realm_on_foreign_ruler_succession
- action_nominate_successor
- action_title_election
- action_in_line_of_succession_for_title
- action_heir_in_line_of_succession_for_title

### 00_lifestyle.txt（8 条目）

- action_can_choose_lifestyle
- action_can_spend_perk_point
- action_lifestyle_diplo
- action_lifestyle_intrigue
- action_lifestyle_learning
- action_lifestyle_martial
- action_lifestyle_stewarship
- action_lifestyle_wanderer

### 00_marriage_actions.txt（8 条目）

- action_adult_player_heir_not_married
- action_adult_ruler_not_married
- action_non_adult_ruler_not_betrothed
- action_betrothed_can_marry
- action_close_family_can_marry
- action_can_take_concubine
- action_too_few_spouses
- action_grand_wedding_can_marry

### 00_mercenaries_actions.txt（1 条目）

- mercenary_contract_expiring

### 00_personal_actions.txt（12 条目）

- action_dying
- action_can_assign_guardian
- action_can_ransom
- action_should_pay_ransom
- action_vassal_ransom_gives_hook
- action_can_vassalize
- action_can_propose_alliance_to_family_member
- action_can_potentially_propose_alliance_to_family_member
- action_can_demand_payment
- action_can_ask_hof_for_money
- action_can_ask_hof_for_claim
- action_hook_expiring

### 00_raid.txt（1 条目）

- action_being_raided

### 00_reactive_advice.txt（56 条目）

- action_reactive_advice_mercenaries
- action_reactive_advice_succession
- action_reactive_advice_bastards
- action_reactive_advice_protecting_against_hostile_schemes
- action_reactive_advice_protect_against_factions
- action_reactive_advice_imprisoned
- action_reactive_advice_county_control
- action_reactive_advice_bankruptcy
- action_reactive_advice_rightful_liege
- action_reactive_advice_bishop_endorsement
- action_reactive_advice_encyclopedia
- action_reactive_advice_religion_rites
- action_reactive_advice_dynamic_culture
- action_reactive_advice_fabricate_claim
- action_reactive_advice_education
- action_reactive_advice_tooltip_modes
- action_perk_bonus_cap_modes
- action_reactive_advice_varangian_adventure
- action_reactive_advice_court_positions
- action_reactive_advice_artifact_inventory
- action_reactive_advice_tours_picking_vassals
- action_reactive_advice_regency_for_liege
- action_reactive_advice_regency_for_regent
- action_reactive_advice_set_future_regent
- action_reactive_advice_travel_planning
- action_reactive_advice_house_unity
- action_reactive_advice_tax_collector
- action_reactive_advice_legitimacy
- action_reactive_advice_epidemics
- action_reactive_advice_plague_resistance
- action_reactive_advice_tutorial_schemes
- action_reactive_advice_tutorial_war
- action_reactive_advice_favorite_child
- action_reactive_advice_army_automation
- action_reactive_advice_landless_adventurer
- action_reactive_advice_admin_gov
- action_reactive_advice_admin_gov_troops
- action_reactive_advice_agent_scheme_rework
- action_reactive_advice_laamp_contract_move
- action_reactive_advice_migration
- action_reactive_advice_great_steppe
- action_reactive_advice_kurultai
- action_reactive_advice_tributaries
- action_reactive_advice_treasury
- action_reactive_advice_meritocratic_governor
- action_reactive_advice_dynastic_cycle
- action_reactive_advice_merit_candidacy
- action_reactive_advice_china_council
- action_reactive_advice_great_projects
- action_reactive_advice_natural_disasters
- action_reactive_advice_women_in_china
- action_reactive_advice_christian_situation
- action_reactive_advice_puppets
- action_reactive_advice_clerical_regions
- action_reactive_advice_personal_beliefs
- action_reactive_advice_ecclesiastical_ruler

### 00_reactive_advice_japan.txt（4 条目）

- action_reactive_advice_welcome_to_japan
- action_reactive_advice_soryo_intro
- action_reactive_advice_lead_your_soryo_bloc
- action_reactive_advice_soryo_regent_become_shogun

### 00_reactive_advice_playtest.txt（1 条目）

- action_lesson_tgp_playtest_intro_mandala

### 00_realm_actions.txt（28 条目）

- action_can_lawfully_imprison
- action_can_pardon
- action_above_domain_limit
- action_above_vassal_limit
- action_too_many_held_duchies
- action_empty_council_position
- action_powerful_vassal_not_on_council
- action_wrong_holding_type
- action_upgrade_tribal_holding_type
- action_disabled_building
- action_dangerous_faction_targeting_me
- action_county_in_dangerous_populist_faction
- action_mega_duke_penalty
- action_in_debt
- action_in_treasury_debt
- action_missing_ghw_beneficiary
- action_ghw_participation_alert
- action_not_endorsed_by_realm_priest
- action_not_endorsed_by_realm_priest_no_holding
- action_low_control_in_county
- action_can_use_hook_to_change_contract
- action_grant_vassal_to_rightful_liege
- action_can_create_head_of_faith_title
- action_can_create_head_of_faith_title_spiritual
- action_can_claim_liege_title
- action_station_men_at_arms
- action_title_lost_from_realm_by_vassal_war
- action_can_raze_holding

### 00_temp_actions.txt（0 条目）

（无顶层块）

### 00_title_actions.txt（2 条目）

- action_can_create_title
- action_can_usurp_title

### 00_war_actions.txt（5 条目）

- action_has_any_display_cb_on
- action_can_call_ally
- action_can_call_house_member
- action_can_call_dynasty_member
- action_not_enough_knights

### 01_bp1_actions.txt（1 条目）

- action_ongoing_house_feud

### 01_ep1_actions.txt（4 条目）

- action_has_unopened_court_event
- action_has_open_court_event
- action_has_courtier_or_guest_with_inspiration
- action_can_hire_court_physician

### 01_ep1_reactive_advice.txt（2 条目）

- action_reactive_advice_should_form_hybrid_culture
- action_reactive_advice_royal_court

### 01_fp1_actions.txt（2 条目）

- action_can_challenge_to_single_combat
- action_can_make_shieldmaiden

### 03_fp2_actions.txt（2 条目）

- action_can_offer_assistance
- action_can_bargain_fealty

### 03_fp2_reactive_advice.txt（1 条目）

- action_reactive_advice_struggle

### 04_ep2_actions.txt（3 条目）

- action_recent_hunt_sighting
- action_empty_accolade_slot
- action_accolade_can_spend_attribute

### 05_bp2_actions.txt（4 条目）

- action_can_offer_hostage
- action_can_demand_hostage
- action_can_exchange_hostage
- action_can_recall_hostage

### 05_fp3_actions.txt（2 条目）

- action_appoint_tax_collector
- action_assign_tax_payers

### 06_ce1_actions.txt（4 条目）

- action_inherit_legend
- action_promote_legend
- action_promote_foreign_legend
- action_upgrade_legend

### 07_ep3_actions.txt（8 条目）

- action_laamp_support_expiring_legend
- action_laamp_apprehension_threat
- action_laamp_camp_purpose
- action_ep3_can_ask_hof_for_influence
- action_ep3_laamp_contract_travel
- action_in_debt_landless
- action_primary_heir_not_inheriting_held_admin_title
- action_invested_candidate_not_inheriting_admin_title

### 09_mpo_actions.txt（15 条目）

- action_can_interrogate
- action_join_tributary_war
- action_can_hire_court_astrologer
- action_low_fertility
- action_demand_tributary
- action_pacify_tributary
- action_can_demand_herd
- action_upgrade_nomadic_holding_type
- action_upgrade_herder_holding_type
- action_chaotic_succession
- action_losing_tributaries
- action_switch_to_tributary
- action_upgrade_dominance
- action_offer_submission_or_ruin
- action_offer_confederation

### 10_empire_faith_gate_actions.txt（1 条目）

- action_efg_request_excommunication

### contract_actions.txt（13 条目）

- action_can_complete_task_contract
- action_can_complete_steal_artifact_contract
- action_can_start_laamp_raid_contract
- action_can_start_join_war_contract
- action_can_train_knights_contract
- action_can_generate_claim_contract
- action_can_make_request_interaction
- action_can_press_faction_demands_contract
- action_new_task_contract
- action_new_tier_3_task_contract
- action_new_criminal_task_contract
- action_new_governance_issue
- action_new_tier_3_governance_issue

### pam_actions.txt（26 条目）

- action_excommunicated_recovery
- action_excommunication_at_risk
- action_losing_realm_to_clerical_region
- action_in_line_for_local_clerical_region
- action_can_request_new_clerical_region
- action_can_request_clerical_region_expansion
- action_can_request_enforce_succession
- action_can_demand_church_succession
- action_pam_decision_confession
- action_can_select_personal_tenet
- action_can_request_preach_legitimacy
- action_targeted_by_mass_rite_conversion
- action_sanctify_artifact
- action_can_appoint_cardinals
- action_can_make_clerical_puppet
- action_can_make_external_clerical_puppet
- action_can_make_external_ruler_puppet
- action_opportunity_to_study_scripture
- action_can_upgrade_great_cathedral
- action_can_plan_mass_conversion
- action_can_sway_ruler_to_rite
- action_can_ask_subordinates_for_gold
- action_sway_ruler_to_rite_unlikely
- action_can_sway_prelate_to_rite
- action_sway_prelate_to_rite_unlikely
- action_can_found_holy_site_in_capital

### tgp_actions.txt（32 条目）

- action_too_many_celestial_province_types
- action_too_many_celestial_province_types_2
- action_mandala_tributary_at_risk_of_breakaway
- action_hegemonic_tributary_has_low_subject_standing_tributary
- action_hegemonic_tributary_has_low_subject_standing_suzerain
- action_no_mandala_aspect
- action_can_upgrade_mandala_aspect
- action_can_go_on_tribute_mission
- action_no_mandala_decree
- action_new_mandala_ritual
- action_could_exact_tribute_from
- action_can_call_tributary
- action_targeted_by_grand_campaign
- action_can_upgrade_house_aspiration
- action_no_house_aspiration
- action_aspiration_does_not_match_house_bloc
- action_missing_elder
- action_can_make_elder_request
- action_would_accept_mandala_embrace
- action_can_request_treasury
- action_can_request_examination_support
- action_start_great_project
- action_can_send_to_childrens_examination
- action_opportunity_to_study_classics
- action_unaligned_join_movement
- action_landless_admin_escape_to_realm
- action_minister_can_imprison
- action_minister_can_pardon
- action_can_be_pardoned_by_minister
- action_pay_governors_treasury_debt
- action_minister_can_pay_treasury_debt
- action_can_find_secrets

### 未解析文件

- `_important_actions.info` — 纯文档（非 Jomini）
