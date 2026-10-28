# common/activities 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：75（其中 Jomini 解析 69 个）
- 顶层块条目总数：476，跨文件唯一条目 476
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `activity_group_types/00_activity_group_types.txt` | 834 | 6 | 0 | jomini |
| `activity_group_types/_activity_group_types.info` | 427 | - | - | 纯文档（非 Jomini） |
| `activity_locales/_activity_locales.info` | 3027 | - | - | 纯文档（非 Jomini） |
| `activity_locales/tournament_locales.txt` | 9220 | 6 | 0 | jomini |
| `activity_types/_activity_type.info` | 42782 | - | - | 纯文档（非 Jomini） |
| `activity_types/camp_party.txt` | 19991 | 1 | 0 | jomini |
| `activity_types/chariot_race.txt` | 52065 | 1 | 0 | jomini |
| `activity_types/coronation.txt` | 132014 | 1 | 0 | jomini |
| `activity_types/debate.txt` | 29276 | 1 | 0 | jomini |
| `activity_types/ecumenical_council.txt` | 61937 | 1 | 0 | jomini |
| `activity_types/feast.txt` | 136915 | 1 | 7 | jomini |
| `activity_types/festival.txt` | 30074 | 1 | 0 | jomini |
| `activity_types/funeral.txt` | 43891 | 1 | 7 | jomini |
| `activity_types/gruesome_festival.txt` | 42843 | 1 | 0 | jomini |
| `activity_types/hike.txt` | 25905 | 1 | 0 | jomini |
| `activity_types/hunt.txt` | 144117 | 1 | 0 | jomini |
| `activity_types/imperial_examination.txt` | 57968 | 1 | 0 | jomini |
| `activity_types/inspection.txt` | 32904 | 1 | 0 | jomini |
| `activity_types/local_examination.txt` | 47125 | 1 | 0 | jomini |
| `activity_types/monument_expedition.txt` | 46274 | 1 | 0 | jomini |
| `activity_types/pam_investiture_council.txt` | 22294 | 1 | 0 | jomini |
| `activity_types/pilgrimage.txt` | 111931 | 1 | 0 | jomini |
| `activity_types/playdate.txt` | 23430 | 1 | 0 | jomini |
| `activity_types/tour.txt` | 101071 | 1 | 0 | jomini |
| `activity_types/tournament.txt` | 161567 | 1 | 0 | jomini |
| `activity_types/university_visit.txt` | 60133 | 1 | 0 | jomini |
| `activity_types/wedding.txt` | 110810 | 1 | 0 | jomini |
| `activity_types/witch_ritual.txt` | 20133 | 1 | 0 | jomini |
| `guest_invite_rules/_invite_rules.info` | 750 | - | - | 纯文档（非 Jomini） |
| `guest_invite_rules/activity_invite_rules.txt` | 30507 | 61 | 0 | jomini |
| `intents/_intents.info` | 3080 | - | - | 纯文档（非 Jomini） |
| `intents/camp_party_intents.txt` | 382 | 1 | 0 | jomini |
| `intents/chariot_race_intents.txt` | 6757 | 3 | 0 | jomini |
| `intents/coronation_intents.txt` | 4964 | 10 | 0 | jomini |
| `intents/debate_intents.txt` | 2134 | 3 | 0 | jomini |
| `intents/ecumenical_council_intents.txt` | 4259 | 5 | 0 | jomini |
| `intents/education_intents.txt` | 1435 | 2 | 0 | jomini |
| `intents/festival_intents.txt` | 2550 | 3 | 0 | jomini |
| `intents/funeral_intents.txt` | 330 | 1 | 0 | jomini |
| `intents/hunt_intents.txt` | 2394 | 3 | 0 | jomini |
| `intents/imperial_examination_intents.txt` | 6453 | 7 | 0 | jomini |
| `intents/journey_intents.txt` | 1085 | 2 | 0 | jomini |
| `intents/pilgrimage_intents.txt` | 1505 | 2 | 0 | jomini |
| `intents/roaming_intents.txt` | 669 | 3 | 0 | jomini |
| `intents/shared_intents.txt` | 8212 | 7 | 0 | jomini |
| `intents/spread_tenet_intents.txt` | 1970 | 2 | 0 | jomini |
| `intents/survey_intents.txt` | 483 | 3 | 0 | jomini |
| `intents/tour_intents.txt` | 2536 | 3 | 0 | jomini |
| `intents/tournament_intents.txt` | 1431 | 2 | 0 | jomini |
| `intents/wedding_intents.txt` | 2077 | 3 | 0 | jomini |
| `intents/witch_ritual_intents.txt` | 269 | 1 | 0 | jomini |
| `pulse_actions/_pulse_actions.info` | 698 | - | - | 纯文档（非 Jomini） |
| `pulse_actions/camp_party_actions.txt` | 38443 | 24 | 0 | jomini |
| `pulse_actions/chariot_race_actions.txt` | 7305 | 6 | 0 | jomini |
| `pulse_actions/coronation_pulse_actions.txt` | 12721 | 15 | 0 | jomini |
| `pulse_actions/debate_pulse_actions.txt` | 8880 | 5 | 0 | jomini |
| `pulse_actions/education_actions.txt` | 17778 | 14 | 0 | jomini |
| `pulse_actions/feast_pulse_actions.txt` | 19720 | 12 | 0 | jomini |
| `pulse_actions/feast_pulse_actions_oltner.txt` | 37717 | 21 | 0 | jomini |
| `pulse_actions/festival_actions.txt` | 15214 | 14 | 0 | jomini |
| `pulse_actions/general_actions.txt` | 1812 | 2 | 0 | jomini |
| `pulse_actions/hunt_pulse_actions.txt` | 51918 | 26 | 0 | jomini |
| `pulse_actions/imperial_examination_actions.txt` | 20639 | 13 | 0 | jomini |
| `pulse_actions/journey_actions.txt` | 9779 | 12 | 0 | jomini |
| `pulse_actions/pam_mendicant_preachers_apa.txt` | 1088 | 1 | 0 | jomini |
| `pulse_actions/passive_rite_learning_apa.txt` | 4623 | 4 | 0 | jomini |
| `pulse_actions/pilgrimage_actions.txt` | 25288 | 22 | 0 | jomini |
| `pulse_actions/playdate_actions.txt` | 17171 | 15 | 0 | jomini |
| `pulse_actions/roaming_actions.txt` | 23846 | 29 | 0 | jomini |
| `pulse_actions/spread_tenet_apa.txt` | 3740 | 2 | 0 | jomini |
| `pulse_actions/survey_actions.txt` | 10442 | 15 | 0 | jomini |
| `pulse_actions/tour_actions.txt` | 29262 | 18 | 0 | jomini |
| `pulse_actions/tournament_actions.txt` | 18827 | 20 | 0 | jomini |
| `pulse_actions/wedding_pulse_actions.txt` | 42533 | 17 | 0 | jomini |
| `pulse_actions/witch_ritual_actions.txt` | 5030 | 7 | 0 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### activity_group_types/00_activity_group_types.txt（6 条目）

- joinable
- invitations
- grand
- activities
- unavailable
- debug

### activity_locales/tournament_locales.txt（6 条目）

- tournament_locale_tournament_grounds
- tournament_locale_settlement
- tournament_locale_visitor_camp
- tournament_locale_religious_building
- tournament_locale_tavern
- tournament_locale_artisans

### activity_types/camp_party.txt（1 条目）

- activity_camp_party

### activity_types/chariot_race.txt（1 条目）

- activity_chariot_race

### activity_types/coronation.txt（1 条目）

- activity_coronation

### activity_types/debate.txt（1 条目）

- activity_debate

### activity_types/ecumenical_council.txt（1 条目）

- activity_ecumenical_council

### activity_types/feast.txt（1 条目）

- activity_feast

### activity_types/festival.txt（1 条目）

- activity_festival

### activity_types/funeral.txt（1 条目）

- activity_funeral

### activity_types/gruesome_festival.txt（1 条目）

- activity_gruesome_festival

### activity_types/hike.txt（1 条目）

- activity_roaming

### activity_types/hunt.txt（1 条目）

- activity_hunt

### activity_types/imperial_examination.txt（1 条目）

- activity_imperial_examination

### activity_types/inspection.txt（1 条目）

- activity_survey

### activity_types/local_examination.txt（1 条目）

- activity_local_examination

### activity_types/monument_expedition.txt（1 条目）

- activity_journey

### activity_types/pam_investiture_council.txt（1 条目）

- activity_investiture_council

### activity_types/pilgrimage.txt（1 条目）

- activity_pilgrimage

### activity_types/playdate.txt（1 条目）

- activity_playdate

### activity_types/tour.txt（1 条目）

- activity_tour

### activity_types/tournament.txt（1 条目）

- activity_tournament

### activity_types/university_visit.txt（1 条目）

- activity_adult_education

### activity_types/wedding.txt（1 条目）

- activity_wedding

### activity_types/witch_ritual.txt（1 条目）

- activity_witch_ritual

### guest_invite_rules/activity_invite_rules.txt（61 条目）

- activity_invite_rule_friends
- activity_invite_rule_potential_friends
- activity_invite_rule_rivals
- activity_invite_rule_rivals_if_appropriate
- activity_invite_rule_lovers
- activity_invite_rule_potential_lovers
- activity_invite_rule_close_family
- activity_invite_rule_extended_family
- activity_invite_rule_liege
- activity_invite_rule_suzerain
- activity_invite_rule_confederates
- activity_invite_rule_vassals
- activity_invite_rule_tributaries
- activity_invite_rule_fellow_vassals
- activity_invite_neighbouring_rulers
- activity_invite_rule_knights
- activity_invite_rule_courtiers
- activity_invite_rule_guests
- activity_invite_rule_house_witches
- activity_invite_rule_other_witches
- activity_invite_rule_all_lieges
- activity_invite_rule_hof
- activity_invite_rule_player_heir
- activity_invite_rule_hunters
- activity_invite_rule_glory_hounds
- activity_invite_spouses_close_family
- activity_invite_spouses_extended_family
- activity_invite_rule_siblings
- activity_invite_rule_crushes
- activity_invite_rule_personal_scheme_targets
- activity_invite_rule_powerful_vassals_children
- activity_invite_rule_fellow_vassals_children
- activity_invite_rule_vassals_children
- activity_invite_spouses
- activity_invite_mp
- activity_invite_rule_vassals_and_below
- activity_invite_rule_charioteers
- activity_invite_rule_landless_adventurers
- activity_invite_rule_landless_adventurers_restricted_range
- activity_invite_rule_landless_adventurers_restricted_range_opinion
- activity_invite_rule_followers
- activity_invite_rule_local_lord
- activity_invite_rule_councillors
- activity_invite_rule_imperial_exam_close_family
- activity_invite_rule_imperial_exam_entrants
- activity_invite_rule_local_exam_entrants
- activity_invite_rule_landless_family_heads_entrants
- activity_invite_rule_local_exam_close_family
- activity_invite_rule_imperial_exam_guests
- activity_invite_rule_local_exam_guests
- activity_invite_rule_bloc_house_heads
- activity_invite_rule_bloc_members
- activity_invite_rule_debate_movement_members
- activity_invite_rule_debate_movement_other_members
- activity_invite_rule_player_family_opt_in_local_exam
- activity_invite_rule_player_family_opt_in_imperial_exam
- activity_invite_hof_and_hor
- activity_invite_cardinals
- activity_invite_archbishops
- activity_invite_clergy
- activity_invite_rule_clergy

### intents/camp_party_intents.txt（1 条目）

- fireside_chat_intent

### intents/chariot_race_intents.txt（3 条目）

- increase_influence_intent
- sow_discord_intent
- appease_populace_intent

### intents/coronation_intents.txt（10 条目）

- coronation_impress_attendees
- coronation_weaken_detractors
- coronation_embrace_supporters
- coronation_exalt_crown
- coronation_bear_witness
- coronation_seize_advantages
- coronation_offer_support
- coronation_advocate_domain
- coronation_profess_rights
- coronation_disrupt_loyalists

### intents/debate_intents.txt（3 条目）

- debate_increase_movement_power_intent
- debate_gain_disciples_intent
- debate_gain_elder_intent

### intents/ecumenical_council_intents.txt（5 条目）

- spiritual_intent_host
- spiritual_intent
- fervor_intent
- clerical_appointment_intent
- alliance_intent

### intents/education_intents.txt（2 条目）

- study_hard_intent
- university_revelry_intent

### intents/festival_intents.txt（3 条目）

- raise_cohesion_intent
- add_to_bloc_intent
- remove_from_bloc_intent

### intents/funeral_intents.txt（1 条目）

- mourn_intent

### intents/hunt_intents.txt（3 条目）

- slay_beast_intent
- successful_nerge_intent
- dreadful_nerge_intent

### intents/imperial_examination_intents.txt（7 条目）

- imperial_exam_taker_intent
- local_exam_taker_intent
- imperial_exam_support_entrants_intent
- local_exam_support_entrants_intent
- exam_assist_exam_intent
- exam_recruit_courtiers_intent
- exam_give_favor_intent

### intents/journey_intents.txt（2 条目）

- journey_knowledge_hoarding_intent
- journey_curiosity_intent

### intents/pilgrimage_intents.txt（2 条目）

- reflection_intent
- zealot_intent

### intents/roaming_intents.txt（3 条目）

- roaming_befriend_intent
- roaming_mystic_intent
- roaming_storyteller_intent

### intents/shared_intents.txt（7 条目）

- reduce_stress_intent
- murder_attendee_intent
- woo_attendee_intent
- befriend_attendee_intent
- spread_legend_intent
- legitimacy_intent
- impose_obedience_intent

### intents/spread_tenet_intents.txt（2 条目）

- spread_personal_tenet_intent
- praise_the_gods_intent

### intents/survey_intents.txt（3 条目）

- survey_overseer_intent
- survey_learning_intent
- survey_learning_intent_guest

### intents/tour_intents.txt（3 条目）

- lechery_intent
- altruism_intent
- justice_intent

### intents/tournament_intents.txt（2 条目）

- win_contest_intent
- recruit_knights_intent

### intents/wedding_intents.txt（3 条目）

- diplomatic_intent
- matchmaking_intent
- banquet_mischief_intent

### intents/witch_ritual_intents.txt（1 条目）

- worship_devil_intent

### pulse_actions/camp_party_actions.txt（24 条目）

- apa_bonded_by_fire
- apa_taught_repair
- apa_revelry_hangover_camp
- apa_local_food_camp
- apa_lauded_food_camp
- apa_guest_of_honor_impressed
- apa_camp_host_gifted
- apa_cultural_acceptance
- apa_fireside_chat_shared_stories_martial
- apa_fireside_chat_shared_stories_learning
- apa_fireside_chat_shared_stories_diplomacy
- apa_fireside_chat_shared_stories_stewardship
- apa_fireside_chat_shared_stories_intrigue
- apa_fireside_chat_shared_drinks
- apa_fireside_chat_inspiring_speech
- apa_camp_party_sad_lonesome
- apa_camp_party_shadows_in_the_dark
- apa_camp_party_fortress_of_solitude
- apa_camp_party_lecture
- apa_camp_party_tales_of_distant_lands
- apa_camp_party_tales_of_war
- apa_camp_party_tales_of_lands_lost
- apa_camp_party_blademaster_sparring
- apa_camp_party_tales_of_piety

### pulse_actions/chariot_race_actions.txt（6 条目）

- apa_cheering_on_competitors
- apa_thunderous_applause
- apa_celebrating_unexpected_overtake
- apa_exchanging_race_commentary
- apa_forging_alliances
- apa_donates_to_the_poor

### pulse_actions/coronation_pulse_actions.txt（15 条目）

- loyalty_pledge
- nobles_cheer
- received_blessing
- regalia_impresses_attendees
- supporters_bond
- detractors_bond
- befriend_loyalists
- supporter_stresses_detractor
- praised_king_together
- bonded_over_help
- beautiful_choir_song
- taking_a_break
- heir_diplomacy_boost
- heir_stewardship_boost
- heir_learning_boost

### pulse_actions/debate_pulse_actions.txt（5 条目）

- apa_movement_ridiculed
- apa_debate_brought_huangdi_gift
- apa_debate_entrant_disagreement
- apa_debate_found_disciple
- apa_debate_fruitful_debate

### pulse_actions/education_actions.txt（14 条目）

- apa_leveraging_language_skills
- apa_bonded_during_studies
- apa_procrastination
- apa_university_discussions
- apa_night_on_books
- apa_student_disagreement
- apa_rowdy_student
- apa_impromptu_poetry
- apa_impressed_teacher
- apa_revelry_hangover
- apa_studied_confucian_classics
- apa_local_food
- apa_aced_homework
- apa_pangur_ban

### pulse_actions/feast_pulse_actions.txt（12 条目）

- excellent_food
- impressed_courtly_vassal
- hook_trusting_guest
- impressed_guest_honor
- leftover_food_giveaway
- virtuous_feast
- noble_privileges
- good_kitty
- good_puppy
- antiquarian_admires_artifact
- jester_entertained_guests
- apa_executioner

### pulse_actions/feast_pulse_actions_oltner.txt（21 条目）

- spouse_skill_diplomacy_improves
- spouse_gives_host_prestige
- spouse_manages_feast_splendidly
- spouse_impresses_clergy
- spouse_gives_hook
- relation_gains_friend
- lauded_food
- guest_of_honor_impressed
- guest_of_honor_praised
- children_bonding
- guest_impressed_by_court_artifact
- guest_chokes_on_bone
- guest_brawl
- friend_lauds_efforts
- courtly_vassals_appeased
- spouse_insults_host
- host_gains_diplo_xp
- host_gains_steward_xp
- host_gains_intrigue_xp
- ridiculed_food
- guest_tells_fantastic_joke

### pulse_actions/festival_actions.txt（14 条目）

- festival_friendship
- festival_romance
- festival_rivalry
- beautiful_festival
- festival_learning
- liege_festival_presence
- festival_cohesion
- festival_join_bloc
- festival_remove_from_bloc
- festival_influence
- liege_festival_prosperity
- festival_prayer
- festival_flowers
- festival_house_relation_increase

### pulse_actions/general_actions.txt（2 条目）

- guest_friendship
- guest_insulted

### pulse_actions/hunt_pulse_actions.txt（26 条目）

- hunt_tracks_character
- hunt_tracks_option
- hunt_tracks_dog
- hunt_tracks_building
- hunt_hunters_bond
- hunt_dog_bond
- hunt_knowledge_sharing
- hunt_small_game
- hunt_moh_positive
- hunt_moh_negative
- hunt_poetic_inspiration
- hunt_fervor_gain
- hunt_distinguished_ability
- hunt_annoyed_owner
- hunt_impressive_grounds
- hunt_eggs_found
- hunt_successful_kill
- hunt_very_successful_kill
- hunt_worked_together
- hunt_failed_kill
- hunt_failed_several_kills
- hunt_successful_maneuver
- hunt_learned_maneuver
- hunt_prowess_mastery
- hunt_martial_mastery
- hunt_make_example

### pulse_actions/imperial_examination_actions.txt（13 条目）

- apa_boasting_calligraphy
- apa_impressive_shot
- apa_overcome_with_stress
- apa_brought_huangdi_gift
- apa_friendly_discussions
- apa_high_tempers
- apa_impressed_examiner
- apa_entrant_disagreement
- apa_burning_midnight_oil
- apa_found_disciple
- apa_fruitful_debate
- apa_confucian_fervor
- apa_floating_poetry

### pulse_actions/journey_actions.txt（12 条目）

- apa_child_learns_something
- apa_scribe_makes_notes
- apa_spotted_by_locals
- apa_vista_of_monument
- apa_spouse_learns_something
- apa_monument_insight
- apa_ate_local_food
- apa_entourage_stops_pickpocket
- apa_cultural_mingling
- apa_strange_markings
- apa_regional_story
- apa_legend_spreads

### pulse_actions/pam_mendicant_preachers_apa.txt（1 条目）

- apa_pam_mendicant_preachers_conversion

### pulse_actions/passive_rite_learning_apa.txt（4 条目）

- apa_passive_religious_learning_host
- apa_passive_religious_learning_guest
- apa_passive_religious_learning_pilgrimage_pool
- apa_passive_religious_learning_pilgrimage_rite

### pulse_actions/pilgrimage_actions.txt（22 条目）

- apa_prayer
- apa_lead_procession
- apa_communal_prayer
- apa_silent_contemplation
- apa_spiritual_journey
- apa_overcome_with_emotion
- apa_preaching_wrath_of_god
- apa_preaching_to_unbelievers
- apa_charity_for_the_poor
- apa_donated_to_holy_site_temple
- apa_tended_to_travellers
- apa_sight_seeing_group
- apa_cultured_discussion
- apa_audience
- apa_picked_up_local_language
- apa_studying_scripture
- apa_visited_markets
- apa_foreign_custom
- apa_pilgrim_protection
- apa_pilgrim_hospitals
- apa_comet_sighted
- apa_good_omen

### pulse_actions/playdate_actions.txt（15 条目）

- apa_won_at_dice
- apa_good_manners
- apa_visited_friends_chapel
- apa_mentor_taught_me
- apa_read_a_book
- apa_joked_together
- apa_rescued_kid
- apa_shared_food
- apa_broke_toy
- apa_found_gold_stash
- apa_sang_nice_song
- apa_learned_from_kid
- apa_practiced_with_swords
- apa_studied_ledger
- apa_had_charming_convo

### pulse_actions/roaming_actions.txt（29 条目）

- apa_roaming_feather
- apa_roaming_ancient_runestone
- apa_roaming_ancient_megalith
- apa_roaming_natural_arch
- apa_roaming_coast_seashells
- apa_roaming_forest_gnarled_oak
- apa_roaming_rabbit_family
- apa_roaming_desert_lilies
- apa_roaming_desert_lilies_oasis
- apa_roaming_desert_fox
- apa_roaming_mountain_river
- apa_roaming_lonely_yurt
- apa_roaming_standing_stone
- apa_roaming_wildflowers
- apa_roaming_lost_sheep
- apa_roaming_friendly_dog
- apa_roaming_grazing_cattle
- apa_roaming_rock_outcrop_plains
- apa_roaming_rock_outcrop_hills
- apa_roaming_waterfall
- apa_roaming_heron
- apa_roaming_dragonfly
- apa_roaming_ducklings
- apa_roaming_dates
- apa_roaming_oasis_shelter
- apa_roaming_oasis_traders
- apa_roaming_traders
- apa_roaming_luminescent_mushrooms
- apa_roaming_wild_berries

### pulse_actions/spread_tenet_apa.txt（2 条目）

- apa_pam_spread_tenet_host
- apa_pam_spread_tenet_guest

### pulse_actions/survey_actions.txt（15 条目）

- apa_survey_bad_harvest
- apa_survey_good_harvest
- apa_survey_bad_merchant_guild
- apa_survey_good_merchant_guild
- apa_survey_bad_noble
- apa_survey_good_noble
- apa_survey_tax_problems
- apa_survey_extra_taxes
- apa_survey_old_bridge
- apa_survey_bad_mercenaries
- apa_survey_good_mercenaries
- apa_survey_small_festival
- apa_survey_fishing_rights
- apa_survey_city_walls
- apa_survey_local_gift

### pulse_actions/tour_actions.txt（18 条目）

- courtier_friendship
- courtiers_became_lovers
- courtiers_became_rivals
- courtiers_got_into_fight
- courtier_improved_skill
- courtier_theological_debate
- courtier_got_sick
- courtier_learned_language
- liege_local_tax
- liege_local_benevolence
- liege_intimidated_courtier
- liege_visited_benevolence
- levied_tax
- local_mayor_tax
- tax_rich_local
- church_tax
- increased_control
- local_baron_tax

### pulse_actions/tournament_actions.txt（20 条目）

- tournament_guest_ptv_small
- tournament_acclaimed_participant
- tournament_entry_fee
- tournament_win_memory
- tournament_studied_techniques
- tournament_knight_skill
- tournament_learned_from_knight
- tournament_game_of_rhetoric
- tournament_equipment_improved
- tournament_relaxed_in_tavern
- tournament_explored_village
- tournament_prayed_temple
- tournament_host_feted
- tournament_host_gifted
- tournament_tilting_demonstration
- tournament_archery_arrow_split
- tournament_recital_successful_verse
- tournament_joust_lance_broken
- tournament_joust_unhorsed
- tournament_horse_stumbles

### pulse_actions/wedding_pulse_actions.txt（17 条目）

- dynasty_blessing
- cultural_acceptance
- marriage_reflection
- royal_gift
- gossip_with_guests
- contact_network
- wedding_gift
- bonding_spouse_family
- received_flowers
- admired_venue
- knight_praised
- mischievous_joke
- seductive_exchange
- poetry_performance
- music_performance
- floral_exhibit
- spouse_impressed

### pulse_actions/witch_ritual_actions.txt（7 条目）

- sacrifed_small_animal
- demonic_chant
- recited_witchcraft_treatise
- admire_moon
- mournful_music
- praised_horned_god_together
- apa_imbued_artifact

### 未解析文件

- `activity_group_types/_activity_group_types.info` — 纯文档（非 Jomini）
- `activity_locales/_activity_locales.info` — 纯文档（非 Jomini）
- `activity_types/_activity_type.info` — 纯文档（非 Jomini）
- `guest_invite_rules/_invite_rules.info` — 纯文档（非 Jomini）
- `intents/_intents.info` — 纯文档（非 Jomini）
- `pulse_actions/_pulse_actions.info` — 纯文档（非 Jomini）
