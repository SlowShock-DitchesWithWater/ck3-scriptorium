# common/character_memory_types 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：23（其中 Jomini 解析 22 个）
- 顶层块条目总数：398，跨文件唯一条目 398
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `_character_memories.info` | 3029 | - | - | 纯文档（非 Jomini） |
| `ach_memories.txt` | 14087 | 25 | 0 | jomini |
| `bp2_hostage_memories.txt` | 5356 | 9 | 0 | jomini |
| `bp2_memories.txt` | 25570 | 32 | 0 | jomini |
| `bp3_memories.txt` | 1007 | 2 | 0 | jomini |
| `ce1_memories.txt` | 4753 | 9 | 0 | jomini |
| `character_memories_1.txt` | 104504 | 97 | 0 | jomini |
| `character_memories_events.txt` | 26885 | 46 | 0 | jomini |
| `character_memories_events_jason_ep2.txt` | 1521 | 3 | 0 | jomini |
| `character_memories_filippa_events.txt` | 26952 | 33 | 0 | jomini |
| `character_memories_travel_events.txt` | 12784 | 23 | 0 | jomini |
| `ep2_feast_memories.txt` | 2179 | 4 | 0 | jomini |
| `ep2_hunt_memories.txt` | 1893 | 2 | 0 | jomini |
| `ep2_memories_james.txt` | 3563 | 7 | 0 | jomini |
| `ep2_tournament_memories.txt` | 2540 | 2 | 0 | jomini |
| `ep2_wedding_memories.txt` | 6873 | 12 | 0 | jomini |
| `ep3_memories.txt` | 22686 | 33 | 0 | jomini |
| `jason_first_event_ep2_memories.txt` | 1009 | 2 | 0 | jomini |
| `mpo_memories.txt` | 9733 | 18 | 0 | jomini |
| `pam_memories.txt` | 6905 | 11 | 0 | jomini |
| `pam_secular_faith_memories.txt` | 1579 | 3 | 0 | jomini |
| `pilgrimage_memories.txt` | 10641 | 12 | 0 | jomini |
| `tgp_memories.txt` | 7579 | 13 | 0 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### ach_memories.txt（25 条目）

- injured_in_crowd_crush_at_coronation_memory
- promised_to_defend_confederation_memory
- offered_realm_to_confederation_memory
- defeated_detractor_in_drinking_contest_memory
- was_caught_cheating_in_drinking_contest_memory
- got_the_city_drunk_memory
- calmed_the_coronation_crowd_memory
- held_a_coronation_memory
- crowned_by_hof_memory
- coronation_coup_memory
- reconquest_oath_memory
- conquest_oath_memory
- coronation_highlighted_memory
- witnessed_a_coronation_memory
- coronation_cultural_acceptance_memory
- coronation_legitimacy_memory
- coronation_friend_memory
- coronation_alliance_memory
- coronation_hook_memory
- coronation_vassal_levies_memory
- coronation_vassal_taxes_memory
- coronation_claim_memory
- coronation_faction_discontent_memory
- coronation_faction_members_memory
- coronation_magnificence_loss_memory

### bp2_hostage_memories.txt（9 条目）

- hostage_created_hostage
- hostage_created_warden
- hostage_created_home_court
- hostage_returned_hostage
- hostage_returned_warden
- hostage_returned_home_court
- hostage_executed
- hostage_spared
- hostage_died

### bp2_memories.txt（32 条目）

- board_games_on_horseback
- pledged_marriage
- imprisoned_adult_education
- completed_adult_education
- became_promising_emissary
- became_promising_mystic
- became_promising_poet
- became_homesick_poet
- cared_for_by_host
- host_stole_aid
- hostage_taught_discretion
- famed_parent_became_very_famous
- pious_parent_became_very_pious
- favourite_toy_horse
- favourite_toy_puppet
- favourite_toy_board_game
- favourite_toy_spinning_top
- favourite_toy_marbles
- childhood_education_no_guardian
- childhood_education_guardian
- ward_education_completed
- imaginary_friend_gained_memory
- hostage_oath_of_friendship
- reaffirmed_cultural_identity
- reformed_culture_and_realm
- completed_rites_of_passage
- honored_imaginary_friend_memory
- wet_nurse_died
- incestous_marriage_wet_nurse
- incestous_divorce_wet_nurse
- ancestor_trait_memory
- ancestor_opposite_trait_memory

### bp3_memories.txt（2 条目）

- visited_monument
- found_exotic_animal

### ce1_memories.txt（9 条目）

- ce1_flung_corpse
- ce1_corpse_flung_at_me
- ce1_meat_shower
- ce1_travelled_far_away
- ce1_completed_my_holy_legend
- ce1_completed_my_heroic_legend
- ce1_completed_my_legitimizing_legend
- ce1_contracted_epidemic
- ce1_contracted_black_death

### character_memories_1.txt（97 条目）

- relative_died
- spouse_died
- lost_duel
- won_duel
- cat_died
- dog_died
- imprisoned
- imprisoned_other
- child_born
- twins_born
- child_stillborn
- child_premature
- first_born
- released_from_prison_memory
- escaped_from_prison_memory
- offensive_war
- defensive_war
- joined_allys_war
- seduced_family
- successful_murder
- war_won
- war_lost
- war_white_peace_attacker
- war_white_peace_defender
- match_made
- debug_memory_positive
- met_friend_first_time
- friend_died
- childhood_started_bullying_positive
- tormented_me_during_childhood
- saw_other_child_die_from_sow
- saw_other_child_die_from_horse
- saw_other_child_die_from_camel
- saw_other_child_die_from_elephant
- saw_other_child_die_from_roof_tile
- spouse_committed_adultery
- became_friends
- became_lovers
- developed_crush
- debug_memory_negative
- broke_up_lovers
- stopped_being_friends
- stopped_being_rivals
- stopped_being_grudge
- became_soulmates
- witnessed_death_battle_good
- witnessed_death_battle_good_killer
- witnessed_death_battle_bad
- witnessed_death_battle_bad_killer
- parent_was_killed_by_rivals_child
- child_killed_rival
- child_killed_by_rival
- stole_lover
- child_defeated_rival
- child_defeated_by_rival
- attacked_by_rivals_child_won
- attacked_by_rivals_child_lost
- became_rivals
- became_nemesis
- became_grudge
- helped_friend_to_die
- failed_assassination
- let_go_of_rivalry
- nemesis_died
- nemesis_killed
- nemesis_killed_by_me
- failed_assassination_by
- battle_lost_memory
- battle_won_memory
- had_sex
- friend_granted_my_claim
- hurt_someone_close_to_me
- freed_from_bad_marriage
- married
- divorced_actor
- divorced_recipient
- killed_everyone
- freed_relative_from_bad_marriage
- rival_died
- lover_died
- soulmate_died
- feud_vengeance_title
- feud_vengeance_killer
- feud_vengeance_torture
- feud_vengeance_cuckold
- house_feud_started_memory
- house_feud_ended_memory
- ascended_throne_memory
- lost_title_memory
- adopted_a_child
- was_adopted
- became_acclaimed
- accolade_created
- stripped_of_accolade
- accolade_ranked_up
- tortured_memory
- torturer_memory

### character_memories_events.txt（46 条目）

- nice_picnic
- destroyed_my_toy
- avenged_my_toy
- nice_fishing_trip
- found_my_clone
- doppelganger_claimed_my_throne
- doppelganger_claimed_my_throne_failed
- humiliated_by_rustlers
- slew_rustlers
- rival_caught_me_in_bed_with_their_child
- supported_illiterate
- reading_aid
- humiliated_illiterate
- birthday_party
- cut_down_tree
- had_a_threesome_memory
- picked_up_throne
- lost_my_addiction_memory
- stole_from_my_rival
- abused_my_peasants
- deviant_defiled_my_object
- haunted_by_a_friend_memory
- haunted_by_a_rival_memory
- haunted_by_parent_memory
- chased_by_bog_witch_memory
- met_a_nice_witch_memory
- assaulted_by_a_witch_memory
- found_a_bog_corpse_memory
- was_shown_execution_memory
- endured_storm
- friend_despite_rivalry
- detestable_family
- storm_seduction
- best_friend_died
- ganged_up_on_three_memory
- ganged_up_on_four_memory
- childless_soulmate_memory
- wedding_night_trinket
- seduced_at_feast_memory
- befriended_at_feast_memory
- became_incapable_due_to_age
- became_incapable_due_to_battle_concussion
- became_incapable_generic
- gave_cultural_gift_memory
- family_castration_memory
- family_castration_fled_memory

### character_memories_events_jason_ep2.txt（3 条目）

- fled_riot_at_races_memory
- failed_riot_at_races_memory
- calmed_the_crowd_memory

### character_memories_filippa_events.txt（33 条目）

- sacrificed_my_cat_memory
- sacrificed_my_dog_memory
- abandoned_crypto_faith_memory
- treasure_map_memory
- foggy_hill_memory
- wall_hole_memory
- completed_first_mandala_capital_memory
- upgraded_mandala_capital_memory
- flawless_mandala_trials_memory
- successful_mandala_trials_memory
- adequate_mandala_trials_memory
- failed_mandala_trials_memory
- imprisoned_mandala_trials_memory
- invalid_mandala_trials_memory
- ascended_as_mandala_devaraja_memory
- ascended_as_divined_mandala_devaraja_memory
- past_max_piety_level_memory
- became_disbelieved_memory
- became_disbelieved_known_memory
- picked_creation_aspect_memory
- picked_serenity_aspect_memory
- picked_destruction_aspect_memory
- picked_trickery_aspect_memory
- upgraded_creation_aspect_memory
- upgraded_serenity_aspect_memory
- upgraded_destruction_aspect_memory
- upgraded_trickery_aspect_memory
- rebuilt_mandala_temple_memory
- started_planning_mandala_capital_memory
- completed_creation_aspect_memory
- completed_serenity_aspect_memory
- completed_destruction_aspect_memory
- completed_trickery_aspect_memory

### character_memories_travel_events.txt（23 条目）

- encountered_delicious_ducklings_memory
- encountered_fluffy_ducklings_memory
- attacked_by_wild_beast_memory
- fooled_by_duck_memory
- almost_crushed_by_elephant_rival_memory
- almost_crushed_by_elephant_nemesis_memory
- was_hero_in_the_fire_memory
- was_disfigured_in_the_fire_memory
- was_wounded_in_the_fire_memory
- saved_someone_from_a_bull_memory
- haunted_manor_survived_assassination_attempt_memory
- friend_ignored_assassination_memory
- rival_ignored_assassination_memory
- nemesis_ignored_assassination_memory
- stood_idly_by_assassination_memory
- saved_from_assassination_memory
- ignored_assault_memory
- knight_sacrificed_memory
- saved_from_assault_memory
- forgave_and_released_prisoner_memory
- became_ill_while_traveling_memory
- memory_big_city_visited
- rescued_fallen_victim_memory

### ep2_feast_memories.txt（4 条目）

- murder_feast_massacre
- murder_feast_solo_kill
- murder_feast_goh_survivor
- murder_feast_entourage_survivor

### ep2_hunt_memories.txt（2 条目）

- hunt_animal_slayer_memory
- hunt_success_memory

### ep2_memories_james.txt（7 条目）

- feral_child_found_memory
- feral_child_socialised_memory
- feral_child_socialised_failed_memory
- attacked_by_feral_child_memory
- legendary_tour
- good_tour
- underwhelming_tour

### ep2_tournament_memories.txt（2 条目）

- tournament_improved_blade_memory
- tournament_won_contest_memory

### ep2_wedding_memories.txt（12 条目）

- grand_wedding_got_married
- grand_wedding_massacre_survivor
- grand_wedding_massacre_guest
- grand_wedding_massacre_spouse_survivor
- grand_wedding_massacre
- grand_wedding_solo_kill
- grand_wedding_refused_to_marry
- grand_wedding_death_at_wedding
- grand_wedding_missed_wedding_in_prison
- grand_wedding_canceled_in_prison
- grand_wedding_completed_host
- grand_wedding_completed_guest

### ep3_memories.txt（33 条目）

- byz_held_triumph
- deposed_liege_memory
- changed_state_faith_memory
- adopted_state_faith_memory
- became_landless_adventurer_memory
- endured_greek_fire_memory
- byz_theodosian_border_memory
- refounded_pandidakterion_memory
- western_help_pope
- western_help_ally
- evangelized_memory
- was_evangelized_memory
- reformed_ere_memory
- found_varangian_memory
- grain_dole_memory
- seized_realm_memory
- realm_seized_memory
- seized_realm_failed_memory
- realm_seized_failed_memory
- frankokratia_installed_byz_claimant_memory
- sacked_byzantium_memory
- noble_family_adopted
- was_noble_family_adopted
- adventurer_family_adopted
- was_adventurer_family_adopted
- procured_estate_memory
- frankokratia_byz_independent_memory
- frankokratia_byz_kingdom_memory
- frankokratia_latin_kingdom_memory
- frankokratia_latin_admin_memory
- wedding_infidelity_spouse
- wedding_infidelity_kin
- wedding_infidelity_victim

### jason_first_event_ep2_memories.txt（2 条目）

- trampled_during_race_rescue
- successful_race_rescue

### mpo_memories.txt（18 条目）

- sent_predecessors_head_memory
- exiled_kin_memory
- exiled_by_kin_memory
- defected_from_kin_memory
- took_kins_widow_concubine_memory
- widow_taken_concubine_memory
- became_blood_brother
- nomad_showed_weakness_in_war
- suzerain_defended_me_in_war
- had_chaotic_kurultai_succession
- had_stable_kurultai_succession
- gok_called_the_clans
- gok_defeated_defiance_war
- gok_defeated_defiance_war_defenders
- gok_defeated_defiance_war_attackers
- gok_won_defiance_war
- gok_won_defiance_war_defenders
- gok_won_defiance_war_attackers

### pam_memories.txt（11 条目）

- founded_cathedral_memory
- built_cathedral_memory
- upgraded_cathedral_memory
- founded_monastic_order_memory
- sent_to_join_monastic_order_memory
- negotiated_for_land_memory
- gave_away_land_memory
- pam_holy_myron_coronation_memory
- sanctified_artifact_memory
- converted_faith_memory
- converted_rite_memory

### pam_secular_faith_memories.txt（3 条目）

- pam_sf_kings_touch_healing_memory
- pam_sf_deliverance_memory
- pam_sf_prophecy_fulfilled_memory

### pilgrimage_memories.txt（12 条目）

- completed_pilgrimage
- completed_pilgrimage_friend
- completed_hajj_memory
- pilgrimage_handled_predecessor_remains_memory
- good_predator_omen_memory
- bad_predator_omen_memory
- good_prey_omen_memory
- bad_prey_omen_memory
- bad_but_good_prey_omen_memory
- hajj_prophet_like_sacrifice_memory
- memory_apa_converted
- memory_apa_was_converted

### tgp_memories.txt（13 条目）

- passed_child_exam_memory
- failed_child_exam_memory
- passed_provincial_exam_memory
- failed_provincial_exam_memory
- passed_metropolitan_exam_memory
- failed_metropolitan_exam_memory
- passed_palace_exam_memory
- survived_disaster_memory
- establish_house_fief_memory
- seized_throne_memory
- throne_seized_memory
- seized_throne_failed_memory
- throne_seized_failed_memory

### 未解析文件

- `_character_memories.info` — 纯文档（非 Jomini）
