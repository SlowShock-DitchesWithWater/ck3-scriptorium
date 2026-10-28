# common/scripted_character_templates 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：45（其中 Jomini 解析 44 个）
- 顶层块条目总数：410，跨文件唯一条目 410
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_court_character_templates.txt` | 8221 | 11 | 0 | jomini |
| `00_court_position_templates.txt` | 19615 | 35 | 0 | jomini |
| `00_foundling_templates.txt` | 213 | 1 | 0 | jomini |
| `00_fund_inspiration_character_templates.txt` | 710 | 3 | 0 | jomini |
| `00_hold_court_character_templates.txt` | 11165 | 17 | 0 | jomini |
| `00_holy_order_character_templates.txt` | 8777 | 3 | 0 | jomini |
| `00_invader_templates.txt` | 2531 | 4 | 0 | jomini |
| `00_knight_templates.txt` | 2856 | 3 | 0 | jomini |
| `00_lifestyle_friend_templates.txt` | 5491 | 15 | 0 | jomini |
| `00_mongol_templates.txt` | 9271 | 13 | 0 | jomini |
| `00_mystic_templates.txt` | 10086 | 7 | 0 | jomini |
| `00_officials_templates.txt` | 4528 | 4 | 0 | jomini |
| `00_peasant_faction_leader_template.txt` | 6203 | 3 | 0 | jomini |
| `00_peasant_leader_templates.txt` | 1180 | 2 | 0 | jomini |
| `00_peasants_template.txt` | 30785 | 34 | 0 | jomini |
| `00_physician_character_template.txt` | 1867 | 3 | 0 | jomini |
| `00_pool_repopulation_character_templates.txt` | 38504 | 8 | 0 | jomini |
| `00_priest_character_template.txt` | 24786 | 7 | 0 | jomini |
| `00_saharan_nomad_template.txt` | 1314 | 1 | 0 | jomini |
| `00_scholar_template.txt` | 2422 | 4 | 0 | jomini |
| `00_scripted_character_templates.txt` | 388 | 1 | 0 | jomini |
| `00_soldier_character_templates.txt` | 12210 | 12 | 0 | jomini |
| `00_terrain_specialist_templates.txt` | 6607 | 8 | 0 | jomini |
| `01_bp1_character_templates.txt` | 2329 | 2 | 0 | jomini |
| `01_bp1_filippa_character_templates.txt` | 5881 | 6 | 0 | jomini |
| `01_bp2_character_templates.txt` | 514 | 1 | 0 | jomini |
| `01_ep1_character_templates.txt` | 25872 | 19 | 0 | jomini |
| `01_fp1_character_templates.txt` | 29959 | 21 | 0 | jomini |
| `01_tgp_japan_character_templates.txt` | 3059 | 2 | 0 | jomini |
| `03_fp2_character_templates.txt` | 12768 | 12 | 0 | jomini |
| `04_ep2_accolade_character_templates.txt` | 112983 | 30 | 0 | jomini |
| `04_ep2_character_templates.txt` | 13700 | 28 | 0 | jomini |
| `04_ep2_character_templates_james.txt` | 966 | 1 | 0 | jomini |
| `04_ep2_james_character_templates.txt` | 438 | 1 | 0 | jomini |
| `04_fp3_character_templates.txt` | 19388 | 16 | 0 | jomini |
| `05_bp2_character_templates.txt` | 11118 | 9 | 0 | jomini |
| `05_ce1_character_templates.txt` | 1388 | 1 | 0 | jomini |
| `06_ce1_character_templates.txt` | 703 | 1 | 0 | jomini |
| `07_ep3_character_templates.txt` | 19711 | 16 | 0 | jomini |
| `09_mpo_character_templates.txt` | 22391 | 12 | 0 | jomini |
| `10_ach_character_templates.txt` | 5663 | 4 | 0 | jomini |
| `_scripted_character_templates.info` | 8890 | - | - | 纯文档（非 Jomini） |
| `pam_character_templates.txt` | 6893 | 4 | 0 | jomini |
| `pam_secular_faith_character_templates.txt` | 988 | 1 | 0 | jomini |
| `tgp_character_templates.txt` | 24559 | 24 | 0 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_court_character_templates.txt（11 条目）

- bleeding_diplomat_character
- preaching_tour_priest_character
- bernard_of_clairvaux_character
- head_chasing_monk_character
- fake_artifact_peddler_character
- adoring_fan_character
- trepanner_character
- random_learned_eunuch_character
- random_barrel_character
- beautiful_maiden_character
- beautiful_man_character

### 00_court_position_templates.txt（35 条目）

- scribe_travel_option_character
- court_jester_court_position_template
- stooge_camp_officer_template
- court_physician_court_position_template
- chief_qadi_court_position_template
- antiquarian_court_position_template
- great_antiquarian_court_position_template
- travel_leader_court_position_template
- wet_nurse_court_position_template
- master_of_spoils_camp_officer_template
- court_tutor_court_position_template
- court_guru_court_position_template
- food_taster_court_position_template
- camp_cook_camp_officer_template
- master_of_horse_court_position_template
- head_groom_camp_officer_template
- master_of_hunt_court_position_template
- huntperson_camp_officer_template
- royal_architect_court_position_template
- head_porter_camp_officer_template
- high_almoner_court_position_template
- chief_forager_camp_officer_template
- seneschal_court_position_template
- quartermaster_camp_officer_template
- cupbearer_court_position_template
- witness_camp_officer_template
- court_poet_court_position_template
- court_musician_court_position_template
- master_bard_camp_officer_template
- bodyguard_court_position_template
- champion_court_position_template
- master_of_arms_camp_officer_template
- executioner_court_position_template
- chronicler_court_position_template
- second_camp_officer_template

### 00_foundling_templates.txt（1 条目）

- peasant_villager_foundling_character

### 00_fund_inspiration_character_templates.txt（3 条目）

- adventurer_pregnant_lover_character
- adventurer_female_lover_character
- adventurer_male_lover_character

### 00_hold_court_character_templates.txt（17 条目）

- demanding_poet_character
- demanding_poet_lover_character
- demanding_poet_diplomacy_character
- demanding_poet_stewardship_character
- demanding_poet_martial_character
- demanding_poet_intrigue_character
- demanding_poet_learning_character
- suspicious_genealogist_character
- alluring_suitor_character
- ambassador_template
- mime_template
- good_merchant_template
- diplomacy_court_position_holder_template
- stewardship_court_position_holder_template
- intrigue_court_position_holder_template
- learning_court_position_holder_template
- prowess_court_position_holder_template

### 00_holy_order_character_templates.txt（3 条目）

- holy_order_leader_character
- religious_leader_character
- monastic_order_leader_character

### 00_invader_templates.txt（4 条目）

- ibn_tumart_character_template
- abd_al_mumin_character_template
- post_migration_local_warlord_template
- post_migration_minor_warlord_template

### 00_knight_templates.txt（3 条目）

- knight_errant_character
- knight
- wandering_knight_character

### 00_lifestyle_friend_templates.txt（15 条目）

- diplomacy_foreign_affairs_focus_friend_template
- diplomacy_majesty_focus_friend_template
- diplomacy_family_focus_friend_template
- martial_strategy_focus_friend_template
- martial_authority_focus_friend_template
- martial_chivalry_focus_friend_template
- stewardship_wealth_focus_friend_template
- stewardship_domain_focus_friend_template
- stewardship_duty_focus_friend_template
- intrigue_skulduggery_focus_friend_template
- intrigue_temptation_focus_friend_template
- intrigue_intimidation_focus_friend_template
- learning_medicine_focus_friend_template
- learning_scholarship_focus_friend_template
- learning_theology_focus_friend_template

### 00_mongol_templates.txt（13 条目）

- genghis_khan_character_template
- borte_character_template
- jochi_character_template
- tolui_character_template
- chagatai_character_template
- ogodei_character_template
- altun_begi_character_template
- subutai_character_template
- hoelun_character_template
- yesu_gei_character_template
- dynamic_genghis_character_template
- dynamic_genghis_spouse_template
- dynamic_genghis_child_template

### 00_mystic_templates.txt（7 条目）

- default_mystic_character
- local_saint_template
- mendicant_mystic_character
- wise_woman_character
- stylite_saint_character
- ancient_forest_traveler_character
- scammer_template

### 00_officials_templates.txt（4 条目）

- tax_collector_character
- administrator_character
- estate_owner_character
- herald_character

### 00_peasant_faction_leader_template.txt（3 条目）

- peasant_faction_leader_template
- populist_faction_leader_template
- nomadic_faction_leader_template

### 00_peasant_leader_templates.txt（2 条目）

- peasant_leader_stewardship_character
- peasant_leader_martial_character

### 00_peasants_template.txt（34 条目）

- beautiful_peasant_character
- servant_character
- witchy_template
- merchant_template
- hunter_template
- falconer_template
- detective_template
- generic_peasant_character
- generic_female_peasant_character
- challenger_peasant_character
- peasant_character
- drunken_peasant_character
- diseased_peasant_character
- peasant_child_character
- peasant_young_child_character
- peasant_toddler_character
- bandit_character_generic
- bandit_character
- criminal_brains_character
- criminal_brawn_character
- criminal_fingers_character
- guide_character
- tournament_locale_character
- child_peasant_character
- servant_father_character
- jester_template
- weird_sailor_template
- criminal_thief_bandit_character
- generic_peasant_character_no_rags
- settlement_elder_character
- opposite_gender_peasant_template
- local_noble_character
- mediocre_spouse
- master_mason_character

### 00_physician_character_template.txt（3 条目）

- physician_low_character_template
- physician_high_character_template
- physician_excellent_character_template

### 00_pool_repopulation_character_templates.txt（8 条目）

- pool_repopulate_prowess
- pool_repopulate_diplomacy
- pool_repopulate_martial
- pool_repopulate_stewardship
- pool_repopulate_intrigue
- pool_repopulate_learning
- pool_repopulate_spouse
- pool_repopulate_local_flavor

### 00_priest_character_template.txt（7 条目）

- priest_character_template
- simple_priest_character_template
- virtuous_priest_character_template
- monk_character_template
- location_pilgrim_template
- tournament_priest_character_template
- monk_brewer_template

### 00_saharan_nomad_template.txt（1 条目）

- saharan_clan_leader_character

### 00_scholar_template.txt（4 条目）

- scholar_character
- writer_character
- capital_scholar_character
- capital_writer_character

### 00_scripted_character_templates.txt（1 条目）

- frankish_knight_character

### 00_soldier_character_templates.txt（12 条目）

- soldier_friend_character
- new_commander_character
- new_warrior_character
- new_siege_engineer
- new_berserker_character
- mercenary
- great_mercenary
- retired_mercenary
- new_raider_character
- honorable_soldier_character
- old_knight_teacher
- wrestler_character

### 00_terrain_specialist_templates.txt（8 条目）

- winter_commander_character
- forest_commander_character
- mountain_commander_character
- desert_commander_character
- hill_commander_character
- jungle_commander_character
- open_commander_character
- wetlands_commander_character

### 01_bp1_character_templates.txt（2 条目）

- bp1_doppelganger_template
- bp1_bisexual_partner_template

### 01_bp1_filippa_character_templates.txt（6 条目）

- bp1_yearly_2021_martial_person_template
- bp1_yearly_2021_learning_witch_template
- bp1_yearly_2021_learning_person_template
- bp1_yearly_2021_stewardship_person_template
- bp1_yearly_2021_diplomacy_person_template
- bp1_yearly_2021_intrigue_person_template

### 01_bp2_character_templates.txt（1 条目）

- bp2_imaginary_friend_template

### 01_ep1_character_templates.txt（19 条目）

- frontier_hero_template
- errant_soldier_character
- cinderella_character
- inspired_template
- local_artisan_template
- foreign_merchant_template
- demarch_template
- millenarian_template
- miracle_baby_template
- prince_ali_template
- court_linguist_good_template
- court_linguist_medium_template
- court_linguist_cheap_template
- hidden_scion_template
- local_dispute_template
- symposium_template
- poet_template
- gardener_template
- preacher_template

### 01_fp1_character_templates.txt（21 条目）

- fp1_ms_godi_character
- fp1_ms_reformed_missionary_character
- fp1_ms_nithing_character
- fp1_ms_warrior_character
- fp1_ms_vagrant_character
- fp1_western_warrior_character
- fp1_eastern_warrior_character
- fp1_jomsviking_bigwig
- fp1_jomsviking_retainer_martial
- fp1_jomsviking_retainer_prowess
- fp1_deceitful_warrior_character
- fp1_deceitful_explorer_character
- fp1_truthful_explorer_character
- fp1_islamic_explorer_character
- fp1_capital_county_nithing_character
- fp1_capital_county_orphan_character
- fp1_trade_partner_merchant
- fp1_trade_partner_priest
- fp1_trade_partner_spy
- fp1_trade_partner_warrior
- old_country_local_warlord_template

### 01_tgp_japan_character_templates.txt（2 条目）

- tgp_japan_yearly_events_pearl_diver_template
- tgp_japan_yearly_events_tengu_warrior_template

### 03_fp2_character_templates.txt（12 条目）

- celebration_scholar_character
- celebration_martial_character
- celebration_diplomat_character
- celebration_spy_character
- celebration_steward_character
- celebration_hunter_character
- celebration_priest_character
- celebration_artisan_character
- celebration_chessmaster_character
- spanish_jewish_merchant_character
- spanish_conversos_character
- toledan_night_character

### 04_ep2_accolade_character_templates.txt（30 条目）

- accolade_marauder_character
- accolade_idealist_character
- accolade_charmer_character
- accolade_thug_character
- accolade_disciplinarian_character
- accolade_fanatic_character
- accolade_valiant_character
- accolade_stalwart_character
- accolade_scoundrel_character
- accolade_politicker_character
- accolade_tactician_character
- accolade_reeve_character
- accolade_manipulator_character
- accolade_mentor_character
- accolade_contender_character
- accolade_archer_character
- accolade_skirmisher_character
- accolade_pike_character
- accolade_outrider_character
- accolade_vanguard_character
- accolade_lancer_character
- accolade_besieger_character
- accolade_crossbowmen_character
- accolade_camelry_character
- accolade_elephantry_character
- accolade_horse_archer_character
- accolade_huntsmaster_character
- accolade_blademaster_character
- accolade_master_of_revels_character
- accolade_house_knight_character

### 04_ep2_character_templates.txt（28 条目）

- tournament_foot_character
- tournament_horse_character
- tournament_archery_character
- tournament_recital_character
- tournament_pugilism_character
- tournament_board_game_character
- loyal_fan_character
- local_beauty_character
- feral_child_template
- castaway_character
- sexy_assassin_character
- garden_hermit_character
- brainless_character_template
- heartless_knight
- cowardly_knight
- child_thief_character
- wealthy_gambler_template
- tournament_mulan_character
- quasimodo_template
- tournament_unusual_stranger
- travel_messenger
- sea_captain
- jungle_guide
- mountaineer_guide
- forder_guide
- desert_warrior_guide
- rough_terrain_guide
- cultural_ambassador

### 04_ep2_character_templates_james.txt（1 条目）

- swords_for_hire_character

### 04_ep2_james_character_templates.txt（1 条目）

- pilgrim_character

### 04_fp3_character_templates.txt（16 条目）

- fp3_raging_ghazi_character
- fp3_chinese_grand_old_lady
- fp3_chinese_eunuch_envoy
- fp3_gnostic_paragon
- fp3_sufi_mystic
- fp3_zoroastrian_armed_pilgrim
- fp3_young_rascal
- fp3_adorable_orphan
- fp3_turkic_traveler
- fp3_tomb_raider
- fp3_turko-mongol_leader
- fp3_avicenna_template
- fp3_rhazes_template
- fp3_al_akhwayni_template
- fp3_ferdowsi_template
- fp3_skilled_outsider_template

### 05_bp2_character_templates.txt（9 条目）

- bp2_wet_nurse_template
- adult_education_teacher
- adult_education_student
- foreign_architect_template
- culture_defender_knight_template
- foreign_cleric_template
- foreign_scholar_template
- foreign_official_template
- foreign_mercenary_template

### 05_ce1_character_templates.txt（1 条目）

- ce1_hooded_figure_template

### 06_ce1_character_templates.txt（1 条目）

- bard_template

### 07_ep3_character_templates.txt（16 条目）

- charioteer_template
- generic_bookmaker_character
- anatolian_guide_character
- varangian_template
- ep3_prostitute_character
- ep3_common_fan_character
- ep3_magistrate_character
- ep3_frankokratia_crusader_template
- laamp_inheritor_template
- traveler_character
- ep3_evangelizer_template
- ep3_poet_template
- ep3_wallada_heir_template
- ep3_poet_toned_down_template
- ep3_murderer_template
- ep3_sea_raider_template

### 09_mpo_character_templates.txt（12 条目）

- herder_character
- astrologer_character_template
- seasoned_pastor_character
- nomadic_chieftain_character
- nomadic_martial_character
- nomadic_commander_template
- nomadic_hunter_template
- nomadic_knight_template
- nomadic_bride_template
- nomadic_husband_template
- wounded_messenger_character_template
- throat_singer_character_template

### 10_ach_character_templates.txt（4 条目）

- funny_courtesan_character
- cunning_courtesan_character
- fearsome_courtesan_character
- experienced_courtesan_character

### pam_character_templates.txt（4 条目）

- pam_monk_courtier_template
- pam_cleric_courtier_template
- pam_nun_courtier_template
- pam_crusader_template

### pam_secular_faith_character_templates.txt（1 条目）

- pam_sf_christlike_stranger_character

### tgp_character_templates.txt（24 条目）

- tgp_orphan_character
- tgp_examiner_learning_template
- tgp_examiner_martial_template
- tgp_examiner_stewardship_template
- tgp_learning_exam_entrant_template
- tgp_stewardship_exam_entrant_template
- tgp_martial_exam_entrant_template
- tgp_concubine_template
- tgp_japan_imperial_scion_template
- tgp_decent_heir_template
- tgp_minister_administrator_template
- tgp_minister_diplomat_template
- tgp_minister_commander_template
- tgp_minister_warrior_template
- tgp_minister_scholar_template
- tgp_minister_confucian_scholar_template
- tgp_minister_eunuch_template
- very_good_eunuch_character
- tgp_warrior_monk_template
- tgp_court_brahmin_template
- tgp_khlon_glan_template
- tgp_steppe_admin_family_head_template
- tgp_poet_lover_template
- tgp_aspect_acolyte_template

### 未解析文件

- `_scripted_character_templates.info` — 纯文档（非 Jomini）
