# common/situation 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：21（其中 Jomini 解析 18 个）
- 顶层块条目总数：287，跨文件唯一条目 287
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `catalysts/10_tgp_dynastic_cycle_catalysts.txt` | 4609 | 92 | 0 | jomini |
| `catalysts/10_tgp_natural_disaster_catalysts.txt` | 191 | 3 | 0 | jomini |
| `catalysts/10_tgp_silk_road_catalysts.txt` | 2976 | 20 | 0 | jomini |
| `catalysts/_catalysts.info` | 293 | - | - | 纯文档（非 Jomini） |
| `catalysts/catalysts.txt` | 120 | 2 | 0 | jomini |
| `catalysts/mpo_the_great_steppe_catalysts.txt` | 237 | 4 | 0 | jomini |
| `catalysts/pam_the_christian_church_catalysts.txt` | 8285 | 148 | 0 | jomini |
| `situation_group_types/00_situation_group_types.txt` | 671 | 6 | 0 | jomini |
| `situation_group_types/_situation_group_types.info` | 342 | - | - | 纯文档（非 Jomini） |
| `situations/_situations.info` | 16236 | - | - | 纯文档（非 Jomini） |
| `situations/debug_situation.txt` | 9177 | 1 | 0 | jomini |
| `situations/game_extra_nomads_arabs.txt` | 9754 | 1 | 0 | jomini |
| `situations/game_extra_nomads_horn.txt` | 9761 | 1 | 0 | jomini |
| `situations/game_extra_nomads_sahel.txt` | 9905 | 1 | 0 | jomini |
| `situations/game_extra_nomads_sami.txt` | 16736 | 1 | 0 | jomini |
| `situations/game_extra_nomads_tibet.txt` | 16874 | 1 | 0 | jomini |
| `situations/pam_christian_situation.txt` | 87595 | 1 | 6 | jomini |
| `situations/tgp_dynastic_cycle.txt` | 69916 | 1 | 5 | jomini |
| `situations/tgp_natural_disaster.txt` | 10185 | 2 | 0 | jomini |
| `situations/tgp_silk_road.txt` | 17618 | 1 | 0 | jomini |
| `situations/the_great_steppe.txt` | 30271 | 1 | 0 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### catalysts/10_tgp_dynastic_cycle_catalysts.txt（92 条目）

- catalyst_expansion_movement_yearly
- catalyst_advancement_movement_yearly
- catalyst_conservative_movement_yearly
- catalyst_pro_hegemon_movement_advancement_yearly
- catalyst_pro_hegemon_movement_expansion_yearly
- catalyst_pro_hegemon_movement_yearly
- catalyst_movement_gained_power_advancement
- catalyst_movement_gained_power_expansion
- catalyst_movement_gained_power_conservative
- catalyst_movement_gained_power_pro_hegemon
- catalyst_movement_consulted_heaven_advancement_positive
- catalyst_movement_consulted_heaven_advancement_negative
- catalyst_movement_consulted_heaven_expansion_positive
- catalyst_movement_consulted_heaven_expansion_negative
- catalyst_movement_consulted_heaven_instability_positive
- catalyst_movement_consulted_heaven_instability_negative
- catalyst_movement_consulted_heaven_chaos_positive
- catalyst_movement_consulted_heaven_chaos_negative
- catalyst_house_head_consulted_heaven_advancement_positive
- catalyst_house_head_consulted_heaven_advancement_negative
- catalyst_house_head_consulted_heaven_expansion_positive
- catalyst_house_head_consulted_heaven_expansion_negative
- catalyst_house_head_consulted_heaven_instability_positive
- catalyst_house_head_consulted_heaven_instability_negative
- catalyst_house_head_consulted_heaven_chaos_positive
- catalyst_house_head_consulted_heaven_chaos_negative
- catalyst_hegemon_above_maa_limit_yearly
- catalyst_hegemon_below_maa_limit_yearly
- catalyst_hegemon_outdated_maa_yearly
- catalyst_hegemon_hired_mercenary
- catalyst_hegemon_lost_defensive_territorial_war
- catalyst_hegemon_lost_capital_in_war
- catalyst_hegemon_lost_war
- catalyst_hegemon_won_war
- catalyst_hegemon_in_defensive_war_yearly
- catalyst_hegemon_appointing_low_merit_councillor
- catalyst_hegemon_appointing_low_merit_governor
- catalyst_imperial_examinations_gap_long_yearly
- catalyst_imperial_examinations_gap_short_yearly
- catalyst_hegemon_too_few_tributaries_yearly
- catalyst_hegemon_murdered
- catalyst_imperial_family_member_murdered
- catalyst_minister_imprison
- catalyst_hegemon_lost_mandate_of_heaven
- catalyst_hegemon_gains_mandate_of_heaven
- catalyst_hegemon_mandate_of_heaven_at_0
- catalyst_hegemon_below_legitimacy_yearly
- catalyst_hegemon_above_legitimacy_yearly
- catalyst_new_dynasty_inherits
- catalyst_hegemon_natural_disaster
- catalyst_hegemon_natural_disaster_recovered
- catalyst_hegemon_handled_calamity
- catalyst_hegemon_in_civil_war
- catalyst_hegemon_epidemic
- catalyst_hegemon_apocalyptic_epidemic
- catalyst_requested_incursion
- catalyst_imperial_treasury_depleted
- catalyst_imperial_treasury_raided
- catalyst_imperial_treasury_debt
- catalyst_cleared_treasury_debt
- catalyst_hegemony_too_few_lands
- catalyst_hegemony_far_too_few_lands
- catalyst_diarch_mandate
- catalyst_governor_embezzlement
- catalyst_dipped_into_treasury
- catalyst_hegemon_influenced_by_interaction
- catalyst_hegemon_targeted_by_political_scheme
- catalyst_governor_raided_estate
- catalyst_governor_slander
- catalyst_governor_challenged_status
- catalyst_great_wall
- catalyst_grand_campaign
- catalyst_grand_campaign_lost
- catalyst_minister_project_culture
- catalyst_great_project_great_wall_contribution
- catalyst_great_project_establish_control_contribution
- catalyst_minister_compel_religious_uniformity
- catalyst_minister_train_troops
- catalyst_minister_conduct_census
- catalyst_event_advancement_medium_progress
- catalyst_event_mongol_empire_appears
- catalyst_event_mongol_empire_attacks_major
- catalyst_event_mongol_empire_attacks_minor
- catalyst_tyrannical_extinguish_noble_family
- catalyst_ministers_abused_privilege_of_office
- catalyst_find_secrets_bad_outcome
- catalyst_find_secrets_good_outcome
- catalyst_minister_blackmailed
- catalyst_minister_exposed_secret
- catalyst_minister_pardoned_known_criminal
- catalyst_minister_pardoned_dangerous_criminal
- catalyst_minister_caught_exam_cheater

### catalysts/10_tgp_natural_disaster_catalysts.txt（3 条目）

- catalyst_situation_passing_of_time_monthly
- catalyst_natural_disaster_great_project_investment
- catalyst_natural_disaster_great_project_completion

### catalysts/10_tgp_silk_road_catalysts.txt（20 条目）

- catalyst_silk_road_region_war
- catalyst_silk_road_adjacent_upstream_region_war
- catalyst_silk_road_distant_upstream_region_war
- catalyst_silk_road_region_peace
- catalyst_silk_road_adjacent_upstream_region_peace
- catalyst_silk_road_distant_upstream_region_peace
- catalyst_silk_road_iranian_intermezzo_in_unrest
- catalyst_silk_road_iranian_intermezzo_ending_reached
- catalyst_silk_road_china_stability
- catalyst_silk_road_china_consolidation
- catalyst_silk_road_china_grand_canal_expanded
- catalyst_silk_road_china_grand_canal_expanded_secondary
- catalyst_silk_road_china_grand_canal_expanded_tertiary
- catalyst_silk_road_mpo_region_resettled
- catalyst_silk_road_byzantium_blew_up
- catalyst_silk_road_mpo_region_to_steppe
- catalyst_silk_road_raided
- catalyst_silk_road_mongol_devastation
- catalyst_silk_road_low_control_at_peace
- catalyst_silk_road_famous_market_built

### catalysts/catalysts.txt（2 条目）

- catalyst_win_any_war_within_the_region
- catalyst_gift_independent_ruler

### catalysts/mpo_the_great_steppe_catalysts.txt（4 条目）

- catalyst_situation_passing_of_time_blessing
- catalyst_situation_passing_of_time_lucky_chance_blessing
- catalyst_situation_passing_of_time_havsarsan
- catalyst_situation_passing_of_time_lucky_chance_havsarsan

### catalysts/pam_the_christian_church_catalysts.txt（148 条目）

- catalyst_clergy_appointed_from_same_family
- catalyst_clergy_hor_short_reign
- catalyst_catholic_hof_weak_papal_state_control
- catalyst_clergy_marries
- catalyst_clergy_has_child
- catalyst_clergy_simony
- catalyst_clergy_sold_claim
- catalyst_clergy_hosted_feast
- catalyst_clergy_attended_feast
- catalyst_clergy_embezzled_treasury
- catalyst_clergy_withdrew_funds_from_treasury
- catalyst_the_christian_church_temple_holding_created
- catalyst_the_christian_church_ruler_completed_pilgrimage
- catalyst_clergy_court_chaplain_murdered
- catalyst_clergy_archbishop_murdered
- catalyst_clergy_cardinal_murdered
- catalyst_clergy_head_of_rite_murdered
- catalyst_clergy_exposed_forbidden_personal_tenet
- catalyst_clergy_exposed_criminal_trait
- catalyst_the_christian_church_head_of_faith_murdered
- catalyst_the_christian_church_head_of_faith_marries
- catalyst_the_christian_church_head_of_faith_has_child
- catalyst_the_christian_church_ruler_imprisons_head_of_faith
- catalyst_the_christian_church_papal_dynasty_capture
- catalyst_clergy_unreformed_pagan_county_converted_to_faith
- catalyst_clergy_elevated_to_archbishopric
- catalyst_clergy_gained_landed_title
- catalyst_the_christian_church_clerical_region_created
- catalyst_the_christian_church_clerical_region_expanded
- catalyst_the_christian_church_clerical_region_split
- catalyst_great_project_cathedral_contribution
- catalyst_great_project_cathedral_completed
- catalyst_great_project_mass_rite_conversion_contribution
- catalyst_the_christian_church_appointed_cardinal
- catalyst_the_christian_church_appointed_monastic_cardinal
- catalyst_the_christian_church_appointed_nepotistic_cardinal
- catalyst_clergy_self_proclaimed_cardinal
- catalyst_clergy_influenced_own_candidacy
- catalyst_the_christian_church_stripped_cardinalate
- catalyst_holy_war_incited
- catalyst_major_holy_war_incited
- catalyst_minor_holy_war_incited
- catalyst_clergy_hired_holy_order
- catalyst_clergy_hired_mercenaries
- catalyst_consecrated_kingdom_for_ruler
- catalyst_consecrated_kingdom_for_theocrat
- catalyst_prelate_empowered_self_with_kingdom
- catalyst_hof_bestowed_title_major
- catalyst_hof_bestowed_title
- catalyst_hof_bestowed_title_clergy_major
- catalyst_hof_bestowed_title_clergy
- catalyst_hof_bestowed_title_clergy_minor
- catalyst_conditional_appointment_used
- catalyst_secular_influenced_clerical_candidacy
- catalyst_investiture_council_settled_spiritual
- catalyst_investiture_council_settled_temporal
- catalyst_secular_interference_in_papal_election
- catalyst_restore_hre_with_pope_blessing
- catalyst_the_christian_church_restored_hre_without_blessing
- catalyst_the_christian_church_strenghtened_claim
- catalyst_the_christian_church_requested_legitimacy
- catalyst_the_christian_church_white_peace_enforced
- catalyst_the_christian_church_victory_enforced
- catalyst_the_christian_church_requested_realm_priest_replacement
- catalyst_the_christian_church_ruler_hired_non_christian_councillor
- catalyst_the_christian_church_ruler_married_non_christian
- catalyst_the_christian_church_swayed_to_rite
- catalyst_the_christian_church_study_faith_scheme_completed
- catalyst_the_christian_church_ecclesiastical_grant_claim
- catalyst_the_christian_church_threatened_ecclesiastical_grant_claim
- catalyst_ecclesiastical_transfer_land_interaction
- catalyst_ecclesiastical_transfer_land_interaction_major
- catalyst_ask_for_gold
- catalyst_ask_for_gold_minor
- catalyst_ask_for_influence
- catalyst_lift_excommunication
- catalyst_lift_excommunication_minor
- catalyst_declaration_of_repentance
- catalyst_declaration_of_repentance_minor
- catalyst_request_excommunication
- catalyst_request_excommunication_minor
- catalyst_excommunicate
- catalyst_excommunicate_minor
- catalyst_seek_indulgences
- catalyst_seek_indulgences_minor
- catalyst_the_christian_church_jerusalem_reclaimed
- catalyst_the_christian_church_christian_holy_site_reclaimed
- catalyst_lose_jerusalem
- catalyst_lose_holy_site
- catalyst_exposed_forbidden_personal_tenet
- catalyst_hosted_ecumenical_council
- catalyst_secular_hosted_ecumenical_council
- catalyst_the_christian_church_new_rite
- catalyst_the_christian_church_new_divergent_rite
- catalyst_the_christian_church_main_power_faith_changed
- catalyst_the_christian_church_ruler_converted_from_christianity
- catalyst_the_christian_church_ruler_converted_to_christianity
- catalyst_the_christian_church_great_schism
- catalyst_shaped_the_christian_church_fragile_unity
- catalyst_shaped_the_christian_church_saeculum_obscurum
- catalyst_shaped_the_christian_church_conversion_phase
- catalyst_shaped_the_christian_church_reform_phase
- catalyst_shaped_the_christian_church_investiture_crisis
- catalyst_shaped_the_christian_church_crusade_phase
- catalyst_shaped_the_christian_church_concord
- catalyst_shaped_the_christian_church_fragile_unity_dynasty
- catalyst_shaped_the_christian_church_saeculum_obscurum_dynasty
- catalyst_shaped_the_christian_church_conversion_phase_dynasty
- catalyst_shaped_the_christian_church_reform_phase_dynasty
- catalyst_shaped_the_christian_church_investiture_crisis_dynasty
- catalyst_shaped_the_christian_church_crusade_phase_dynasty
- catalyst_shaped_the_christian_church_concord_dynasty
- catalyst_shaped_the_christian_church_fragile_unity_hof
- catalyst_shaped_the_christian_church_saeculum_obscurum_hof
- catalyst_shaped_the_christian_church_conversion_phase_hof
- catalyst_shaped_the_christian_church_reform_phase_hof
- catalyst_shaped_the_christian_church_investiture_crisis_hof
- catalyst_shaped_the_christian_church_crusade_phase_hof
- catalyst_shaped_the_christian_church_concord_hof
- catalyst_pope_declared_popular_core_tenet
- catalyst_pope_declared_unpopular_core_tenet
- catalyst_the_christian_church_papal_bull_enacted
- catalyst_the_christian_church_established_theocratic_dynasty
- catalyst_the_christian_church_founded_military_order
- catalyst_the_christian_church_founded_monastic_order
- catalyst_the_christian_church_consecrated_bloodline
- catalyst_the_christian_church_staged_act_of_devotion
- catalyst_the_christian_church_revoked_order_lease
- catalyst_neighboring_unreformed_pagan_raid_you
- catalyst_county_converted_to_faith
- catalyst_county_converted_from_faith
- catalyst_the_christian_church_excommunication_war_declared
- catalyst_the_christian_church_humiliation_war_declared
- catalyst_the_christian_church_same_faith_ruler_war_declared
- catalyst_the_christian_church_civil_war_in_christian_kingdom
- catalyst_non_christian_kingdom_in_europe
- catalyst_byzantine_emperor_non_christian
- catalyst_the_christian_church_great_holy_war_won
- catalyst_the_christian_church_great_holy_war_lost
- catalyst_the_christian_church_great_holy_war_declared_on_christian
- catalyst_the_christian_church_non_christian_peasant_revolt_raised
- catalyst_the_christian_church_ruler_died_in_battle_against_non_christian
- catalyst_the_christian_church_antipope_declared
- catalyst_the_christian_church_antipope_sponsored
- catalyst_the_christian_church_antipope_removed
- catalyst_heresy_light_outbreak
- catalyst_heresy_dangerous_rite
- catalyst_heresy_historical_outbreak

### situation_group_types/00_situation_group_types.txt（6 条目）

- major
- struggles
- minor
- natural_disasters
- story_cycles
- debug

### situations/debug_situation.txt（1 条目）

- debug_situation

### situations/game_extra_nomads_arabs.txt（1 条目）

- game_rule_extra_nomads_arabs

### situations/game_extra_nomads_horn.txt（1 条目）

- game_rule_extra_nomads_horn

### situations/game_extra_nomads_sahel.txt（1 条目）

- game_rule_extra_nomads_sahel

### situations/game_extra_nomads_sami.txt（1 条目）

- game_rule_extra_nomads_sami

### situations/game_extra_nomads_tibet.txt（1 条目）

- game_rule_extra_nomads_tibet

### situations/pam_christian_situation.txt（1 条目）

- the_christian_church

### situations/tgp_dynastic_cycle.txt（1 条目）

- dynastic_cycle

### situations/tgp_natural_disaster.txt（2 条目）

- natural_disaster_earthquake
- natural_disaster_flood

### situations/tgp_silk_road.txt（1 条目）

- silk_road_situation

### situations/the_great_steppe.txt（1 条目）

- the_great_steppe

### 未解析文件

- `catalysts/_catalysts.info` — 纯文档（非 Jomini）
- `situation_group_types/_situation_group_types.info` — 纯文档（非 Jomini）
- `situations/_situations.info` — 纯文档（非 Jomini）
