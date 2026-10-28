# common/event_themes 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：3（其中 Jomini 解析 2 个）
- 顶层块条目总数：195，跨文件唯一条目 195
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_event_themes.txt` | 71074 | 155 | 1 | jomini |
| `_event_themes.info` | 3423 | - | - | 纯文档（非 Jomini） |
| `ep2_tournament_themes.txt` | 14050 | 40 | 0 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_event_themes.txt（155 条目）

- diplomacy
- martial
- stewardship
- intrigue
- learning
- family
- dynasty
- love
- marriage
- friendly
- unfriendly
- seduction
- party
- hostage
- vassal
- realm
- crown
- dread
- corruption
- war
- new_royal_court
- physical_health
- mental_health
- skull
- medicine
- plague
- faith
- christian
- dungeon
- hunting
- travel
- widgetless_travel
- travel_sea
- travel_diplomacy
- travel_intrigue
- travel_learning
- travel_martial
- travel_stewardship
- travel_danger
- widgetless_travel_danger
- memory_diplomacy
- memory_intrigue
- memory_learning
- memory_martial
- memory_negative
- memory_positive
- memory_stewardship
- memory_stress
- memory_formative
- generic_intrigue_scheme
- murder_scheme
- abduct_scheme
- fabricate_hook_scheme
- claim_throne_scheme
- seduce_scheme
- romance_scheme
- befriend_scheme
- sway_scheme
- diplomacy_foreign_affairs_focus
- diplomacy_majesty_focus
- diplomacy_family_focus
- martial_strategy_focus
- martial_authority_focus
- martial_chivalry_focus
- stewardship_wealth_focus
- stewardship_domain_focus
- stewardship_duty_focus
- intrigue_skulduggery_focus
- intrigue_temptation_focus
- intrigue_intimidation_focus
- learning_medicine_focus
- learning_scholarship_focus
- learning_theology_focus
- wanderer_journey_focus
- wanderer_destination_focus
- wanderer_internal_affairs_focus
- study_faith
- feast_activity
- murder_feast_activity
- hunt_activity
- hunt_activity_camp
- playdate_activity
- university_activity
- funeral_activity
- roaming_activity
- journey_activity
- survey_activity
- festival_activity
- coronation_activity
- rival_relation
- friend_relation
- lover_relation
- prison
- mental_break
- witchcraft
- culture_change
- education
- bastardy
- pregnancy
- alliance
- pet
- secret
- healthcare
- recovery
- death
- battle
- legend
- legend_terrain
- court
- inspiration_complete
- travel_tour
- tour_arrival
- tour_arrival_turned_away
- tour_grounds
- host_dinner
- tour_stop
- cultural_festival
- travel_pilgrimage
- pilgrimage_return
- pilgrimage_destination
- wedding_ceremony_activity
- wedding_banquet_activity
- wedding_night_activity
- bloody_wedding_ceremony
- bloody_wedding_banquet
- bloody_wedding_night
- emperor
- administrative
- byzantine
- landless_adventurer
- university
- chariot_race
- chariot_race_charioteer
- laamp
- violet_poet
- harrying
- nomads
- migration
- raid
- coronation
- dynastic_cycle
- imperial_examination
- debate
- merit
- disaster
- silk_road
- mandala
- tributary
- ruler_objectives
- default
- lisp
- ep2_video_test
- ecumenical_council
- pam_investiture_council
- lighting_test

### ep2_tournament_themes.txt（40 条目）

- tournament_locale_tavern
- tournament_locale_camp
- tournament_locale_forge
- tournament_locale_artisans
- tournament_locale_temple
- tournament_locale_village
- tournament_outskirts
- tournament_grounds
- tournament_contest
- tournament_contest_martial
- tournament_contest_boardgame
- tournament_contest_recital
- tournament_archery_pivotal
- tournament_horse_race_pivotal
- tournament_boardgame_pivotal
- tournament_joust_pivotal
- tournament_melee_pivotal
- tournament_recital_pivotal
- tournament_wrestling_pivotal
- tournament_archery_win
- tournament_archery_neutral
- tournament_archery_lose
- tournament_boardgame_win
- tournament_boardgame_neutral
- tournament_boardgame_lose
- tournament_horse_race_win
- tournament_horse_race_neutral
- tournament_horse_race_lose
- tournament_joust_win
- tournament_joust_neutral
- tournament_joust_lose
- tournament_melee_win
- tournament_melee_neutral
- tournament_melee_lose
- tournament_recital_win
- tournament_recital_neutral
- tournament_recital_lose
- tournament_wrestling_win
- tournament_wrestling_neutral
- tournament_wrestling_lose

### 未解析文件

- `_event_themes.info` — 纯文档（非 Jomini）
