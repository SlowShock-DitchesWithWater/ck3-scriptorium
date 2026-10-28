<!-- 来源: https://ck3.paradoxwikis.com/Event_modding oldid=37279 抓取于 2026-10-22T21:40:25+08:00 -->

# Event modding — Themes


A Theme is a collection of background, lighting environment for character portraits, and sound effects. They are declared in common/event_themes/.

| Theme |  |  |  |
| --- | --- | --- | --- |
| abduct_scheme | alliance | bastardy | battle |
| befriend_scheme | claim_throne_scheme | corruption | crown |
| culture_change | death | default | diplomacy |
| diplomacy_family_focus | diplomacy_foreign_affairs_focus | diplomacy_majesty_focus | dread |
| dungeon | dynasty | education | fabricate_hook_scheme |
| faith | family | feast_activity | friend_relation |
| friendly | generic_intrigue_scheme | healthcare | hunt_activity |
| hunting | intrigue | intrigue_intimidation_focus | intrigue_skulduggery_focus |
| intrigue_temptation_focus | learning | learning_medicine_focus | learning_scholarship_focus |
| learning_theology_focus | love | lover_relation | marriage |
| martial | martial_authority_focus | martial_chivalry_focus | martial_strategy_focus |
| medicine | mental_break | mental_health | murder_scheme |
| party | pet | physical_health | pilgrimage_activity |
| pregnancy | prison | realm | recovery |
| rival_relation | romance_scheme | secret | seduce_scheme |
| seduction | skull | stewardship | stewardship_domain_focus |
| stewardship_duty_focus | stewardship_wealth_focus | sway_scheme | unfriendly |
| vassal | war | witchcraft |  |

Individual elements of the theme can be overridden using `override_background`, `override_icon`, `override_sound`, and `override_environment`.

#### Backgrounds

| Background |  |  |  |
| --- | --- | --- | --- |
| alley_day | alley_night | armory | army_camp |
| battlefield | bedchamber | burning_building | corridor_day |
| corridor_night | council_chamber | courtyard | docks |
| dungeon | farmland | feast | gallows |
| garden | market | market_east | market_india |
| market_tribal | market_west | physicians_study | sitting_room |
| study | tavern | temple | temple_church |
| temple_generic | temple_mosque | temple_scope | terrain |
| terrain_activity | terrain_scope | throne_room | throne_room_east |
| throne_room_india | throne_room_mediterranean | throne_room_scope | throne_room_tribal |
| throne_room_west | wilderness | wilderness_desert | wilderness_forest |
| wilderness_forest_pine | wilderness_mountains | wilderness_scope | wilderness_steppe |

### Environments

When you've selected a background, the appropriate environment is automatically selected. Only overwrite it when necessary.

| Environment |  |  |
| --- | --- | --- |
| environment_body | environment_council | environment_cw_east_main |
| environment_cw_east_spouse | environment_cw_east_throneroom_main | environment_cw_east_throneroom_spouse |
| environment_cw_india_main | environment_cw_india_spouse | environment_cw_india_throneroom_main |
| environment_cw_india_throneroom_spouse | environment_cw_mediterranean_main | environment_cw_mediterranean_spouse |
| environment_cw_mediterranean_throneroom_main | environment_cw_mediterranean_throneroom_spouse | environment_cw_tavern |
| environment_cw_tavern_spouse | environment_cw_tribal_main | environment_cw_tribal_spouse |
| environment_cw_west | environment_cw_west_spouse | environment_event_alley |
| environment_event_alley_day | environment_event_armory | environment_event_battlefield |
| environment_event_bedchamber | environment_event_church | environment_event_corridor_day |
| environment_event_courtyard | environment_event_desert | environment_event_docks |
| environment_event_dungeon | environment_event_farms | environment_event_feast |
| environment_event_forest | environment_event_forest_pine | environment_event_gallows |
| environment_event_garden | environment_event_genericcamp | environment_event_market_east |
| environment_event_market_tribal | environment_event_market_west | environment_event_mosque |
| environment_event_mountains | environment_event_sittingroom | environment_event_standard |
| environment_event_steppe | environment_event_study | environment_event_study_physician |
| environment_event_tavern | environment_event_temple | environment_event_throne_room_west |
| environment_frontend_east_heir | environment_frontend_east_main | environment_frontend_east_secondary |
| environment_frontend_india_heir | environment_frontend_india_main | environment_frontend_india_secondary |
| environment_frontend_mediterranean_heir | environment_frontend_mediterranean_main | environment_frontend_mediterranean_secondary |
| environment_frontend_tribal_heir | environment_frontend_tribal_main | environment_frontend_tribal_secondary |
| environment_frontend_west_heir | environment_frontend_west_main | environment_frontend_west_secondary |
| environment_head | environment_hud | environment_portrait_editor |
| environment_shoulders | environment_standard | environment_torso |
| environment_war_overview |  |  |

