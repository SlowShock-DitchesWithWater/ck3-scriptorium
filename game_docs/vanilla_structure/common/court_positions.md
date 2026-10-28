# common/court_positions 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：47（其中 Jomini 解析 45 个）
- 顶层块条目总数：166，跨文件唯一条目 166
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `tasks/00_antiquarian_tasks.txt` | 8633 | 3 | 0 | jomini |
| `tasks/00_bookmaker_tasks.txt` | 2886 | 2 | 0 | jomini |
| `tasks/00_boyan_tasks.txt` | 2322 | 2 | 0 | jomini |
| `tasks/00_caravan_master_tasks.txt` | 4870 | 3 | 0 | jomini |
| `tasks/00_charioteer_tasks.txt` | 2624 | 1 | 0 | jomini |
| `tasks/00_cherbi_tasks.txt` | 1493 | 1 | 0 | jomini |
| `tasks/00_chief_qadi_tasks.txt` | 1818 | 1 | 0 | jomini |
| `tasks/00_chronicler_tasks.txt` | 7193 | 3 | 0 | jomini |
| `tasks/00_court_artificer_tasks.txt` | 6689 | 3 | 0 | jomini |
| `tasks/00_court_brahmin_tasks.txt` | 801 | 1 | 0 | jomini |
| `tasks/00_court_brewmaster_tasks.txt` | 3271 | 3 | 0 | jomini |
| `tasks/00_court_guru_tasks.txt` | 3157 | 3 | 0 | jomini |
| `tasks/00_court_jester_tasks.txt` | 6539 | 3 | 0 | jomini |
| `tasks/00_court_musician_tasks.txt` | 1719 | 1 | 0 | jomini |
| `tasks/00_court_physician_tasks.txt` | 5464 | 3 | 0 | jomini |
| `tasks/00_court_poet_tasks.txt` | 8414 | 1 | 0 | jomini |
| `tasks/00_court_tutor_tasks.txt` | 12338 | 2 | 0 | jomini |
| `tasks/00_cupbearer_tasks.txt` | 2795 | 2 | 0 | jomini |
| `tasks/00_executioner_tasks.txt` | 1192 | 1 | 0 | jomini |
| `tasks/00_fire_dragon_engineer_tasks.txt` | 3098 | 2 | 0 | jomini |
| `tasks/00_food_taster_tasks.txt` | 2736 | 2 | 0 | jomini |
| `tasks/00_foreign_emissary_tasks.txt` | 2927 | 1 | 0 | jomini |
| `tasks/00_grand_guardian_tasks.txt` | 5778 | 3 | 0 | jomini |
| `tasks/00_grand_mentor_tasks.txt` | 10648 | 3 | 0 | jomini |
| `tasks/00_grand_preceptor_tasks.txt` | 4170 | 3 | 0 | jomini |
| `tasks/00_harem_manager_tasks.txt` | 6179 | 3 | 0 | jomini |
| `tasks/00_high_almoner_tasks.txt` | 3065 | 2 | 0 | jomini |
| `tasks/00_khlon_glan_tasks.txt` | 2616 | 1 | 0 | jomini |
| `tasks/00_master_of_the_horse_tasks.txt` | 2739 | 2 | 0 | jomini |
| `tasks/00_master_of_the_hunt_tasks.txt` | 12629 | 3 | 0 | jomini |
| `tasks/00_personal_champion_tasks.txt` | 5592 | 3 | 0 | jomini |
| `tasks/00_royal_architect_tasks.txt` | 3364 | 2 | 0 | jomini |
| `tasks/00_seneschal_tasks.txt` | 4188 | 3 | 0 | jomini |
| `tasks/00_siege_engineer_tasks.txt` | 2388 | 1 | 0 | jomini |
| `tasks/00_stargazer_tasks.txt` | 4125 | 2 | 0 | jomini |
| `tasks/00_wet_nurse_tasks.txt` | 5539 | 3 | 0 | jomini |
| `tasks/00_yeke_jarquchi_tasks.txt` | 1820 | 1 | 0 | jomini |
| `tasks/00_yurtchi_tasks.txt` | 1426 | 2 | 0 | jomini |
| `tasks/01_eparch_tasks.txt` | 11406 | 4 | 0 | jomini |
| `tasks/_court_position_tasks.info` | 4365 | - | - | 纯文档（非 Jomini） |
| `types/00_admin_court_position.txt` | 8543 | 1 | 0 | jomini |
| `types/00_camp_officers.txt` | 118165 | 28 | 3 | jomini |
| `types/00_celestial_court_positions.txt` | 43778 | 7 | 0 | jomini |
| `types/00_court_positions.txt` | 257836 | 34 | 0 | jomini |
| `types/00_mandala_court_positions.txt` | 16952 | 3 | 0 | jomini |
| `types/00_mpo_court_positions.txt` | 48042 | 8 | 0 | jomini |
| `types/_court_positions.info` | 19861 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### tasks/00_antiquarian_tasks.txt（3 条目）

- antiquarian_court_position_task_improve_artifacts
- antiquarian_court_position_task_exibit_artifacts
- antiquarian_court_position_task_scout_for_artifacts

### tasks/00_bookmaker_tasks.txt（2 条目）

- bookmaker_cook_the_books
- bookmaker_distribute_bribes

### tasks/00_boyan_tasks.txt（2 条目）

- boyan_impress_vassals
- boyan_prepare_raids

### tasks/00_caravan_master_tasks.txt（3 条目）

- caravan_master_prepare_travels
- caravan_master_prepare_armies
- caravan_master_improve_self

### tasks/00_charioteer_tasks.txt（1 条目）

- charioteer_training

### tasks/00_cherbi_tasks.txt（1 条目）

- cherbi_double_the_guard

### tasks/00_chief_qadi_tasks.txt（1 条目）

- chief_qadi_court_position_task_public_alms

### tasks/00_chronicler_tasks.txt（3 条目）

- chronicler_generate_seeds
- chronicler_promote_legend_realm
- chronicler_espouse_legend

### tasks/00_court_artificer_tasks.txt（3 条目）

- court_artificer_court_position_task_martial
- court_artificer_court_position_task_learning
- court_artificer_court_position_task_stewardship

### tasks/00_court_brahmin_tasks.txt（1 条目）

- court_brahmin_court_position_task_increase_tribute

### tasks/00_court_brewmaster_tasks.txt（3 条目）

- court_brewmaster_popular_opinion
- court_brewmaster_court_opinion
- court_brewmaster_experimental_brew

### tasks/00_court_guru_tasks.txt（3 条目）

- guru_teach_learning
- guru_teach_diplomacy
- guru_teach_intrigue

### tasks/00_court_jester_tasks.txt（3 条目）

- court_jester_court_position_task_entertain_court
- court_jester_court_position_task_fuel_the_rumour_mill
- court_jester_court_position_task_abuse_the_jester

### tasks/00_court_musician_tasks.txt（1 条目）

- court_musician_court_position_task_bolster_legitimacy

### tasks/00_court_physician_tasks.txt（3 条目）

- physician_treat_epidemic
- physician_guard_family
- physician_improve_self

### tasks/00_court_poet_tasks.txt（1 条目）

- court_poet_court_position_task_create_poetry

### tasks/00_court_tutor_tasks.txt（2 条目）

- court_tutor_improve_others
- court_tutor_teach_kids

### tasks/00_cupbearer_tasks.txt（2 条目）

- cupbearer_court_position_task_flatter_dignitaries
- cupbearer_court_position_task_collect_tallage

### tasks/00_executioner_tasks.txt（1 条目）

- executioner_terrify_court

### tasks/00_fire_dragon_engineer_tasks.txt（2 条目）

- fire_dragon_engineer_court_position_forge_fire_dragons
- fire_dragon_engineer_court_position_command_artillery

### tasks/00_food_taster_tasks.txt（2 条目）

- food_taster_court_position_task_brew_poisons
- food_taster_court_position_task_ear_to_the_ground

### tasks/00_foreign_emissary_tasks.txt（1 条目）

- foreign_emissary_culture_acceptance

### tasks/00_grand_guardian_tasks.txt（3 条目）

- grand_guardian_court_position_task_guard_the_capital
- grand_guardian_court_position_task_shield_the_realm
- grand_guardian_court_position_task_instill_martial_discipline

### tasks/00_grand_mentor_tasks.txt（3 条目）

- grand_mentor_court_position_task_teach_liege
- grand_mentor_court_position_task_edify_heirs
- grand_mentor_court_position_task_train_officials

### tasks/00_grand_preceptor_tasks.txt（3 条目）

- grand_preceptor_court_position_task_instill_righteousness
- grand_preceptor_court_position_task_propagate_civic_virtue
- grand_preceptor_court_position_task_exalt_imperial_deeds

### tasks/00_harem_manager_tasks.txt（3 条目）

- keeper_of_the_harem_court_position_task_maintain_decorum
- keeper_of_the_harem_court_position_task_attend_to_wellness
- keeper_of_the_harem_court_position_task_select_palace_beauties

### tasks/00_high_almoner_tasks.txt（2 条目）

- high_almoner_attend_poor
- high_almoner_court_position_task_appease_zealots

### tasks/00_khlon_glan_tasks.txt（1 条目）

- khlon_glan_assist_provisioning

### tasks/00_master_of_the_horse_tasks.txt（2 条目）

- master_of_horse_oversee_breeding
- master_of_horse_mightiest_warhorse

### tasks/00_master_of_the_hunt_tasks.txt（3 条目）

- master_of_hunt_court_position_task_regular_game
- master_of_hunt_court_position_task_dangerous_game
- master_of_hunt_court_position_task_legendary_game

### tasks/00_personal_champion_tasks.txt（3 条目）

- champion_compete_task
- champion_exercise_ruler
- champion_improve_self

### tasks/00_royal_architect_tasks.txt（2 条目）

- royal_architect_fortify_lands
- royal_architect_public_works

### tasks/00_seneschal_tasks.txt（3 条目）

- seneschal_handling_estate
- seneschal_improve_court
- seneschal_improve_domain

### tasks/00_siege_engineer_tasks.txt（1 条目）

- siege_engineer_build_equipment

### tasks/00_stargazer_tasks.txt（2 条目）

- court_astrologer_guide_shepherds
- court_astrologer_handling_weather

### tasks/00_wet_nurse_tasks.txt（3 条目）

- wet_nurse_instill_virtue
- wet_nurse_promote_relationships
- wet_nurse_promote_competition

### tasks/00_yeke_jarquchi_tasks.txt（1 条目）

- yeke_jarquchi_culture_acceptance

### tasks/00_yurtchi_tasks.txt（2 条目）

- yurtchi_lean_times
- yurtchi_prosperous_times

### tasks/01_eparch_tasks.txt（4 条目）

- eparch_appease_populace
- eparch_support_troops
- eparch_enforce_public_order
- eparch_development

### types/00_admin_court_position.txt（1 条目）

- eparch_court_position

### types/00_camp_officers.txt（28 条目）

- second_camp_officer
- quartermaster_camp_officer
- armorer_camp_officer
- chief_forager_camp_officer
- master_thief_camp_officer
- head_porter_camp_officer
- head_groom_camp_officer
- huntperson_camp_officer
- kennelperson_camp_officer
- chief_engineer_camp_officer
- witness_camp_officer
- person_haggler_camp_officer
- camp_cook_camp_officer
- master_bard_camp_officer
- stooge_camp_officer
- master_of_arms_camp_officer
- light_cavalry_captain_camp_officer
- camelry_captain_camp_officer
- elephantry_captain_camp_officer
- heavy_cavalry_captain_camp_officer
- horse_archer_captain_camp_officer
- archer_captain_camp_officer
- heavy_infantry_captain_camp_officer
- light_infantry_captain_camp_officer
- pike_captain_camp_officer
- master_of_spoils_camp_officer
- laureate_camp_officer
- camp_priest_camp_officer

### types/00_celestial_court_positions.txt（7 条目）

- grand_preceptor_court_position
- grand_mentor_court_position
- grand_guardian_court_position
- fire_dragon_engineer_court_position
- keeper_of_the_harem_court_position
- favored_minister_court_position
- minister_bureaucrat_court_position

### types/00_court_positions.txt（34 条目）

- court_physician_court_position
- travel_leader_court_position
- antiquarian_court_position
- seneschal_court_position
- court_tutor_court_position
- wet_nurse_court_position
- charioteer_court_position
- bookmaker_court_position
- akolouthos_court_position
- chief_eunuch_court_position
- master_of_horse_court_position
- master_of_hunt_court_position
- master_assassin_court_position
- cultural_emissary_court_position
- cave_hermit_court_position
- chief_qadi_court_position
- court_gardener_court_position
- court_scholar_court_position
- chronicler_court_position
- champion_court_position
- court_brewmaster_court_position
- lady_in_waiting_court_position
- royal_architect_court_position
- high_almoner_court_position
- court_poet_court_position
- court_musician_court_position
- cupbearer_court_position
- food_taster_court_position
- keeper_of_swans_court_position
- court_jester_court_position
- executioner_court_position
- bodyguard_court_position
- court_artificer_court_position
- garuda_court_position

### types/00_mandala_court_positions.txt（3 条目）

- court_guru_court_position
- court_brahmin_court_position
- khlon_glan_court_position

### types/00_mpo_court_positions.txt（8 条目）

- court_astrologer_court_position
- boyan_court_position
- siege_engineer_court_position
- yurtchi_court_position
- cherbi_court_position
- yeke_jarquchi_court_position
- foreign_emissary_court_position
- keeper_of_the_horses_court_position

### 未解析文件

- `tasks/_court_position_tasks.info` — 纯文档（非 Jomini）
- `types/_court_positions.info` — 纯文档（非 Jomini）
