<!-- 来源: https://ck3.paradoxwikis.com/Event_modding oldid=37279 抓取于 2026-10-22T21:40:25+08:00 -->

# Event modding — Portraits


In Crusader Kings III, portraits are now in 3D, and can now be animated as well! What follows is a list of the different portrait positions, as well as a list of animations for them.

### Portrait Positions

Portrait Positions

| Portrait Position | Description |
| --- | --- |
| left_portrait | Shown on the left side of the event scene. |
| right_portrait | Shown on the right side of the event scene. |
| lower_left_portrait | Shown on the lower left part of the event scene. |
| lower_center_portrait | Shown on the lower center part of the event scene. |
| lower_right_portrait | Shown on the lower right part of the event scene. |

Here is an example of all of the portrait positions in use at the same time, along with a screenshot:

```
example_event.1001 = {
	left_portrait = {
		character = ROOT # Whoever this is scoped to will show up in this event window position, exhibiting the chosen animation. 
		animation = fear # Take note that characters with SOME genetic traits (for example, gigantism, dwarfism) that change their character models have different animations, and if you assign one of THOSE animations to a character that does not have that model, crashes may occur.
	}
	right_portrait = {
		character = ROOT
		animation = scheme
	}
	lower_left_portrait = {
		character = ROOT
	}
	lower_center_portrait = {
		character = ROOT
	}
	lower_right_portrait = {
		character = ROOT
	}
}
```

Portraits can take the following parameters:

| Parameter | Description | Example |
| --- | --- | --- |
| character | The character whose portrait is shown. | `character = scope:event_target` |
| animation | The animation that will play | `animation = anger` |
| triggered_animation | Plays a certain animation if the triggers are met. If not, will default to animation set with `animation =` | triggered_animation = { trigger = {} animation = fear } |
| triggered_outfit | Set an outfit for use in this event. (Additional Information on outfit_tags) | triggered_outfit = { trigger = {} outfit_tags = no_clothes (also accepts multiple tags, in the format outfit_tags = { tag1 tag2 } remove_default_outfit = yes/no } |
| hide_info | Prevents the game from showing any info on the character (tooltip, COA, clicks, etc). Only the portrait will be shown. | `hide_info = yes/no` |

### Animations

| Event-Compatible Animation IDs |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| idle | chancellor | steward | spymaster | chaplain | marshal |
| minister_works | grand_marshal | frontend_center_idle | frontend_left_idle | frontend_right_idle | personality_honorable |
| personality_dishonorable | personality_bold | personality_coward | personality_greedy | personality_content | personality_vengeful |
| personality_forgiving | personality_rational | personality_irrational | personality_compassionate | personality_callous | personality_zealous |
| personality_cynical | admiration | anger | beg | boredom | crying |
| delirium | disappointed | disapproval | disbelief | disgust | dismissal |
| eccentric | ecstasy | fear | flirtation | flirtation_left | grief |
| happiness | interested | interested_left | laugh | love | manic |
| mental_anguish | nervous | pain | paranoia | poison | rage |
| sadness | schadenfreude | scheme | shame | shock | stress |
| stunned | wailing | wedding_happy_cry | worry | pregnant | newborn |
| peekaboo | child_hobby_horse | clutching_toy | clutching_ball | clutching_doll | go_to_your_room |
| sick | cough | shiver | sick_stomach | severelywounded | loss_1 |
| holding_crutch | page_flipping | writing | reading | stressed_teacher | happy_teacher |
| throne_room_writer | thinking_all | thinking | emotion_thinking_scepter | pondering | contemplating |
| deliberation | prisonhouse | prisondungeon | war_attacker | war_defender | war_over_tie |
| war_over_win | war_over_loss | drink | drink_goblet | toast | toast_goblet |
| wedding_drunk | acknowledging | betting | bribing | chess_certain_win | chess_cocky |
| crowning | condemnation | dancing | dancing_plague | debating | eavesdrop |
| eyeroll | fanning_coyly | fanning | japanese_war_fan | hero_flex | lantern |
| physician | pointing | scepter | serving_tray | stayback | storyteller |
| survey | survey_staff | holding_staff | shepherd_with_sheep | villain | zealous_superior |
| acknowledging_crozier | divine_gesture_1 | divine_gesture_2 | divine_gesture_3 | divine_gesture_4 | divine_ecstasy |
| divine_ecstasy_kneeling | holding_crozier | prayer_muslim | prayer_crossing | prayer | prayer_standing |
| prayer_standing_eyes | preaching | preaching_no_book | thurible | situla | priest_good |
| priest_corrupt | whipping | self_flagellation | spiritual_fulfillment | hunting_horn | hunting_carcass_start |
| hunting_falcon | wedding_groom_right | wedding_bride_left | wedding_priest | reception_groom_left | reception_bride_right |
| wedding_objection_start | marshal_random_weapon | marshal_axe | marshal_dagger | marshal_mace | marshal_shield |
| sword_shield_aggressive | assassin | aggressive_axe | aggressive_mace | aggressive_sword | aggressive_dagger |
| aggressive_spear | aggressive_hammer | aggressive_unarmed | celebrate_axe | celebrate_mace | celebrate_sword |
| celebrate_dagger | celebrate_spear | celebrate_hammer | sword_coup_degrace | wrestling_victory | sword_yield_start |
| wrestling_yield_start | wooden_sword_yield_start | throne_room_wooden_sword | celebrate_wooden_sword | aggressive_wooden_sword | marshal_wooden_sword |
| wooden_sword_coup_degrace | random_weapon_coup_degrace | random_weapon_aggressive | random_weapon_celebrate | random_weapon_yield | inspect_weapon |
| menacing | menacing_wooden_sword | threatening | hunting_knife_start | crossbow | bow_idle |
| hunting_shortbow_rest_arrow_default | hunting_shortbow_rest_bluntarrow_default | hunting_shortbow_aim_arrow_default | hunting_shortbow_aim_bluntarrow_default | hunting_longbow_rest_arrow_default | hunting_longbow_rest_bluntarrow_default |
| hunting_longbow_aim_arrow_default | hunting_longbow_aim_bluntarrow_default | throne_room_one_handed_passive_1 | throne_room_one_handed_passive_2 | throne_room_one_handed_passive_3 | throne_room_two_handed_passive_1 |
| throne_room_two_handed_passive_shield | jodan_no_kamae | chudan_no_kamae | gedan_no_kamae | hasso_no_kamae | waki_gamae |
| relaxed_spear | throne_room_ruler | throne_room_ruler_3 | throne_room_ruler_hu | throne_room_ruler_jp | emperor |
| holding_hu | throne_room_chancellor | throne_room_messenger_1 | throne_room_messenger_2 | throne_room_messenger_3 | holding_scrolls |
| throne_room_conversation_1 | throne_room_conversation_2 | throne_room_conversation_3 | throne_room_conversation_4 | throne_room_cheer_1 | throne_room_cheer_2 |
| throne_room_applaud_1 | throne_room_kneel_1 | throne_room_kneel_2 | seiza | sitting | throne_room_curtsey_1 |
| throne_room_bow_1 | throne_room_bow_2 | throne_room_bow_3 | obsequious_bow | prostration | gongshou |
| gongshou_with_hu | wu_shu_bao_quan_li | jockey_lance_tilted | jockey_lance_couched_gallop | jockey_gallop | jockey_idle |
| jockey_victory | jockey_loss | jockey_walk | jockey_wave | standing_horse | horse_archer_idle |
| horse_archer_aggressive | horse_surveying | horse_exhausted | horse_conversing_right | horse_conversing_left | horse_sword_shield |
| chariot_neutral | chariot_happy | chariot_shocked | chariot_w_horses_neutral | chariot_w_horses_happy | chariot_w_horses_shocked |
| instrument_active | instrument_idle | shawm_active | shawm_idle | qanun_active | qanun_idle |
| guqin_active | guqin_idle | lute_active | lute_idle | chifonie_active | chifonie_idle |
| alto_flute_active | alto_flute_idle | incapable | dead | bind_pose |  |

