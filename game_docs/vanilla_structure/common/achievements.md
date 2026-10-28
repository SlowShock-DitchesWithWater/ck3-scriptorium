# common/achievements 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：13（其中 Jomini 解析 11 个）
- 顶层块条目总数：198，跨文件唯一条目 198
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `_achievements.info` | 3498 | - | - | 纯文档（非 Jomini） |
| `ce1_achievements.txt` | 2834 | 11 | 0 | jomini |
| `ce3_achievements.txt` | 3536 | 10 | 0 | jomini |
| `ep1_achievements.txt` | 7683 | 20 | 0 | jomini |
| `ep2_achievements.txt` | 8562 | 20 | 0 | jomini |
| `ep3_achievements.txt` | 6936 | 20 | 0 | jomini |
| `ep4_achievements.txt` | 6490 | 20 | 0 | jomini |
| `fp1_achievements.txt` | 4155 | 10 | 0 | jomini |
| `fp2_achievements.txt` | 3285 | 11 | 0 | jomini |
| `fp3_achievements.txt` | 3616 | 10 | 0 | jomini |
| `mpo_achievements.txt` | 2722 | 10 | 0 | jomini |
| `msgrdk_achievements.json` | 20390 | - | - | JSON 元数据 |
| `standard_achievements.txt` | 21208 | 56 | 0 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### ce1_achievements.txt（11 条目）

- ce1_not_today_achievement
- ce1_divine_right_achievement
- ce1_youll_never_take_me_alive_achievement
- ce1_the_pharaoh_islands_achievement
- ce1_canonized_achievement
- ce1_upward_mobility_achievement
- ce1_cant_touch_this_achievement
- ce1_legendary_achievement
- ce1_f_achievement
- ce1_local_legend_achievement
- ce1_neverending_story_achievement

### ce3_achievements.txt（10 条目）

- ce3_04_the_two_swords_achievement
- ce3_02_guidos_guiding_light_achievement
- ce3_11_servus_servorum_dei_achievement
- ce3_12_papal_bull_achievement
- ce3_07_the_father_the_son_and_the_holy_grandson_achievement
- ce3_13_where_theres_a_will_achievement
- ce3_14_home_see_advantage_achievement
- ce3_15_cardinal_sin_achievement
- ce3_06_fathers_best_side_achievement
- ce3_16_holier_than_thou_achievement

### ep1_achievements.txt（20 条目）

- ep1_01_achievement
- ep1_02_achievement
- ep1_03_achievement
- ep1_04_achievement
- ep1_05_achievement
- ep1_06_achievement
- ep1_07_achievement
- ep1_08_achievement
- ep1_09_achievement
- ep1_10_achievement
- ep1_11_achievement
- ep1_12_achievement
- ep1_13_achievement
- ep1_14_achievement
- ep1_15_achievement
- ep1_16_achievement
- ep1_17_achievement
- ep1_18_achievement
- ep1_19_achievement
- ep1_20_achievement

### ep2_achievements.txt（20 条目）

- ep2_01_the_grandest_tour_achievement
- ep2_02_your_eternal_reward_achievement
- ep2_03_imperial_march_achievement
- ep2_04_black_dinner_achievement
- ep2_05_there_and_back_again_achievement
- ep2_06_the_very_best_achievement
- ep2_07_like_no_one_ever_was_achievement
- ep2_08_a_thousand_and_one_nights_achievement
- ep2_09_a_knights_tale_achievement
- ep2_10_hunting_accident_achievement
- ep2_11_lions_and_tigers_and_bears_oh_my_achievement
- ep2_12_fly_my_pretty_achievement
- ep2_13_pathway_to_heaven_achievement
- ep2_14_sir_lance_a_lot_achievement
- ep2_15_im_in_my_elements_achievement
- ep2_16_ahab_achievement
- ep2_17_little_william_marshal_achievement
- ep2_18_a_true_and_perfect_knight_achievement
- ep2_19_a_e_i_o_u_and_me_achievement
- ep2_20_the_iron_and_golden_king_achievement

### ep3_achievements.txt（20 条目）

- ep3_01_the_old_man_of_the_mountain_achievement
- ep3_02_band_of_brothers_achievement
- ep3_03_mio_cid_achievement
- ep3_04_birthright_achievement
- ep3_05_historically_inaccurate_achievement
- ep3_06_quantum_leap_achievement
- ep3_07_kingdom_of_heaven_achievement
- ep3_08_new_management_achievement
- ep3_09_rags_to_riches_to_rags_to_riches_achievement
- ep3_10_tamar_mepe_achievement
- ep3_11_despoiler_of_byzantium_achievement
- ep3_12_chaos_is_a_ladder_achievement
- ep3_13_epic_paperwork_achievement
- ep3_14_against_the_odds_achievement
- ep3_15_in_good_estate_achievement
- ep3_16_i_got_a_permit_achievement
- ep3_17_despotic_achievement
- ep3_18_byzywork_achievement
- ep3_19_not_content_to_serve_achievement
- ep3_20_started_from_the_bottom_now_were_ere_achievement

### ep4_achievements.txt（20 条目）

- ep4_01_fishing_in_china_achievement
- ep4_02_the_heavenly_kingdom_achievement
- ep4_03_sword_of_japan_achievement
- ep4_04_a_living_god_on_earth_achievement
- ep4_05_grand_governor_achievement
- ep4_06_mandate_of_heaven_achievement
- ep4_07_cut_off_the_head_and_the_body_will_follow_achievement
- ep4_08_shogun_achievement
- ep4_09_devaraja_achievement
- ep4_10_confucian_scholar_achievement
- ep4_11_bloc_politics_achievement
- ep4_12_upper_upper_achievement
- ep4_13_how_its_done_done_done_achievement
- ep4_14_daits_how_you_do_it_achievement
- ep4_15_humble_beginnings_achievement
- ep4_16_flying_colors_achievement
- ep4_17_highway_of_ideas_achievement
- ep4_18_yes_i_need_my_samurai_achievement
- ep4_19_stamp_of_approval_achievement
- ep4_20_promised_land_achievement

### fp1_achievements.txt（10 条目）

- fp1_01_achievement
- fp1_02_achievement
- fp1_03_achievement
- fp1_04_achievement
- fp1_05_achievement
- fp1_06_achievement
- fp1_07_achievement
- fp1_08_achievement
- fp1_09_achievement
- fp1_10_achievement

### fp2_achievements.txt（11 条目）

- fp2_historys_best_friends
- fp2_basque_in_my_glory
- fp2_friendship_is_magic
- fp2_high_stakes_chess
- fp2_iberia_or_iberia
- fp2_andalusian_inquisition
- fp2_iberian_hostilities
- fp2_iberian_conciliation
- fp2_iberian_compromise
- fp2_holiday_in_iberia
- fp2_el_cid_achievement

### fp3_achievements.txt（10 条目）

- fp3_rich_in_diversity_achievement
- fp3_darius_revenge_achievement
- fp3_mulct_them_dry_achievement
- fp3_the_umma_strikes_back_achievement
- fp3_royal_flush_achievement
- fp3_fiscal_res_achievement
- fp3_abassid_strong_achievement
- fp3_challenger_caliphate_achievement
- fp3_vassalize_the_caliph_achievement
- fp3_rekindle_iran_achievement

### mpo_achievements.txt（10 条目）

- mpo_the_stallion_that_mounts_the_world_achievement
- mpo_nobodys_business_achievement
- mpo_tribute_band_achievement
- mpo_this_chinggis_everything_achievement
- mpo_steppe_by_steppe_achievement
- mpo_in_xanadu_achievement
- mpo_settling_in_achievement
- mpo_blood_of_my_blood_achievement
- mpo_confedup_achievement
- mpo_shut_up_nerge_achievement

### standard_achievements.txt（56 条目）

- until_death_do_us_part_achievement
- way_of_life_achievement
- a_legacy_to_last_the_ages_achievement
- a_house_of_my_own_achievement
- dreadful_ruler_achievement
- stressful_situation_achievement
- not_so_feudal_system_achievement
- the_succession_is_safe_achievement
- almost_there_achievement
- last_count_first_king_achievement
- prolific_achievement
- a_name_known_throughout_the_world_achievement
- end_of_an_era_achievement
- turning_to_diamonds_achievement
- reconquista_achievement
- seven_holy_cities_achievement
- frankokratia_achievement
- celebrity_achievement
- saint_achievement
- keeping_it_in_the_family_achievement
- non_nobis_domine_achievement
- trapped_in_the_web_achievement
- followed_by_shadows_achievement
- what_nepotism_achievement
- rise_from_the_ashes_achievement
- the_emerald_isle_achievement
- from_rags_to_riches_achievement
- give_a_dog_a_bone_achievement
- al_andalus_achievement
- wily_as_the_fox_achievement
- sibling_rivalry_achievement
- blood_eagle_achievement
- kings_to_the_seventh_generation_achievement
- norman_yoke_achievement
- royal_dignity_achievement
- going_places_achievement
- land_of_the_rus_achievement
- above_god_achievement
- paragon_of_virtue_achievement
- the_things_love_does_for_us_achievement
- fine_print_achievement
- know_your_place_achievement
- monumental_achievement
- its_not_a_cult_achievement
- the_things_we_do_for_love_achievement
- an_unfortunate_accident_achievement
- death_did_us_part_achievement
- for_the_faith_achievement
- bad_blood_achievement
- seductive_achievement
- the_emperors_new_clothes_achievement
- a_perfect_circle_achievement
- carolingian_consolidation_achievement
- moving_up_in_the_world_achievement
- beacon_of_progress_achievement
- mother_of_us_all_achievement

### 未解析文件

- `_achievements.info` — 纯文档（非 Jomini）
- `msgrdk_achievements.json` — JSON 元数据
