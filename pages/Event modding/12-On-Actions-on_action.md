<!-- 来源: https://ck3.paradoxwikis.com/Event_modding oldid=37279 抓取于 2026-10-22T21:40:25+08:00 -->

# Event modding — On Actions (on_action)


On Actions are scripts that execute every time a specific action is called by the game code (such as a child being born, a character inheriting land or using a hook).
This allows modders to intercept and run their own scripts whenever said On Actions are called.

They are defined in **common/on_action**

**Important:** double-check your path. This is a singular **on_action**, not on_actions. This is a common mistake.

Example (trigger a custom event when a child is born):

```
on_birth_child = {
  events = {
    my_event.1
  }
}
```

See the .info file in that folder for more details. See on_actions.log for a full list of on_actions.

Some on_actions are called by game code directly, while others are called by script: other on_actions, events, decisions, etc.

For example, `on_birthday` is fired by code every birthday and tries to fire `on_birthday_adulthood`, but since it has a trigger `is_adult = yes` it will only fire when a character is an adult.

Such custom on_actions are useful to group events or effects. We can create new custom on_actions, we cannot create new code on_actions.

### Common examples

- `on_birth_child` - when a child is born
- `on_16th_birthday` - when a child becomes an adult
- `random_yearly_playable_pulse` - once a year, at a random date, for every count+ character who is allowed to be played. Useful for rare events.
- `quarterly_playable_pulse` - a more frequent pulse, every three months, for the same kind of characters
- `on_game_start` - when the game starts, but before the player selects a character, so `every_player` doesn't work here
- `on_game_start_after_lobby` - after the player has selected a character and confirmed. This is where you can affect player characters
- `on_death` - right before a character dies. Useful to transfer any variables to the primary_heir

Note, there is no monthly on_action. This was done to ensure better performance.

If you *really* need a monthly pulse, you could use quarterly_playable_pulse and trigger your on_action three times with increasing delay:

```
on_actions = {
  my_on_action
  delay = { months = 1 }
  my_on_action
  delay = { months = 2 }
  my_on_action
}
```

Alternatively, have the on_action call itself with a monthly delay.

### Appending

Most of the time, we want to add something to on_actions without overwriting them. We call this appending.

**Important:** effects and triggers cannot be appended directly. Only events and other on_actions are appended.

To ensure compatibility and not overwrite vanilla effects, do the following:

1. Make a new txt file.
2. Create your own on_action and add it to an existing on_action:

```
on_birth_child = { 
	on_actions = {
		my_on_action # custom on_action appended to on_birth_child
	} 
} 
my_on_action = {
	trigger = { ... } # trigger used only for this on_action
	effect = { ... } # all effects are appended safely
}
```

The example below will ovewrite vanilla effect and trigger (and any added by other mods)

```
on_birth_child = {
	trigger = { ... } 
	effect = {... } # effect and trigger are overwritten, not appended
}
```

On_actions can also be called by events and other effects like this:

`trigger_event = { on_action = my_on_action }`

### Scopes

Make sure to check what scopes are available in each on_action.

There are comments above each on_action in their files that explain their scopes.

For example, `on_game_start` doesn't have a root scope. It fires once, globally. This means we need to use global effects, like `every_ruler`.

On the other hand, `yearly_playable_pulse` fires for all playable characters, and has the character as the root scope. So we can use character effects directly, like add_gold.

**Important**: Do not use `every_living_character` in `yearly_playable_pulse` and similar on_actions.

That on_action already fires for every character. If you then try to iterate through all characters, that would result in about 200002 operations, causing massive lag and repetition of your effects.

### Properties

This table uses contents from */common/on_action/on_actions.info* file.

****

| Name | Description | Expected type | Example |
| --- | --- | --- | --- |
| trigger | On_actions can have triggers. If an on_action fires and its trigger returns false, nothing happens | boolean | trigger = { trigger_conditions = yes } |
| weight_multiplier | Used to manipulate the weight of this on_action if it is a candidate in a random_on_actions list (see below) | integer | weight_multiplier = { base = 1 modifier = { add = 1 trigger_conditions = yes } } |
| events | Events listed in "events" brackets will always fire as long as their trigger evaluates to true |  | events = { event_id_1 delay = { days = 365 } # A delay will mean that all events listed after it will only be fired after the delay has passed. NOTE: For performance reasons, an event will only successfully fire if it is valid both when the on_action is executed AND once the delay is complete. All firing entries support delays, whether for events or on_actions. event_id_2 delay = { months = { 6 12 } } # Setting a new delay overrides a previous delay. Delays support random ranges event_id_3 } |
| random_events | A single event will be picked to fire |  | random_events = { # A single event will be picked to fire chance_to_happen = 25 # A percentage chance determining whether the events involved will be evaluated at all chance_of_no_event = { # An entry that can be formatted as a script value (and therefore have conditional entries). Separated from "chance_to_happen" for performance reasons. Will only be evaluated if chance_to_happen is true. value = 0 if = { limit = { trigger_conditions = yes } add = 10 } } 100 = event_id_1 # The number is the weight for picking a specific event. The weight is factored by the event's weight_multiplier entry. (If no weight_multiplier is defined for the event, it is 1) 200 = event_id_2 100 = 0 # Having a "0" entry means that there is a chance no event fires, even if there are other valid events. Good for making sure that rare events don't always fire just because every other possible event is invalid. } |
| first_valid | Pick the first event for which the trigger returns true | List<event> | first_valid = { # Pick the first event for which the trigger returns true event_id_1 event_id_2 fallback_event_without_trigger } |
| on_actions | An on_action can fire other on_actions, following the same rules as with events | List<on_action> | on_actions = { # An on_action can fire other on_actions, following the same rules as with events on_action_1 on_action_2 on_action_3 } |
| random_on_actions | Same as with events. On_actions are also factored by their weight_multipliers, which defaults to 1 |  | random_on_actions = { 100 = on_action_1 200 = on_action_2 100 = 0 } |
| first_valid_on_action |  | List<on_action> | first_valid_on_action = { on_action_1 on_action_2 } |
| effect | An on_action can run effects. It can access the same default or saved scopes as the script chain/code functionality it was fired from. Note that it happens concurrently to events triggered by the on_action, NOT before. Effects run here create a separate chain than events the on_action fires, so you can for example not manipulate values in the effect, and then reliably access those in an event that was fired at the same time. Scopes or local variables set in the effect here will not carry over to any event fired by the on_action. |  | effect = { effects = yes } |
| fallback | on_actions can define a fallback on_action. If no events/on_actions are run by the on_action, the fallback gets called instead. Avoid creating infinite fallback loops, or the game may be prevented from advancing time! | on_action | fallback = another_on_action |

### On_actions from code

| Name | Description | From code | Expected scope | Other |
| --- | --- | --- | --- | --- |
| on_prestige_level_loss |  | Yes | None |  |
| on_rank_down |  | Yes | None |  |
| on_weight_changed |  | Yes | Character |  |
| on_faith_monthly |  | Yes | Faith |  |
| on_knight_combat_pulse |  | Yes | Character |  |
| on_war_invalidated |  | Yes | None |  |
| on_war_transferred |  | Yes | Character |  |
| on_divorce |  | Yes | None |  |
| on_leave_court |  | Yes | Character |  |
| on_guest_ready_to_move_to_pool |  | Yes | Character |  |
| on_guest_arrived_from_pool |  | Yes | Character |  |
| on_siege_completion |  | Yes | Character |  |
| on_war_won_attacker |  | Yes | Casus belli |  |
| on_alliance_added |  | Yes | None |  |
| on_pregnancy_mother |  | Yes | Character |  |
| on_raid_action_start |  | Yes | None |  |
| on_county_faith_change |  | Yes | Landed Title |  |
| on_title_gain_usurpation |  | Yes | None |  |
| on_release_from_prison |  | Yes | Character |  |
| random_yearly_playable_pulse |  | Yes | Character |  |
| on_raid_action_completion |  | Yes | Army |  |
| on_death |  | Yes | Character |  |
| on_birth_father |  | Yes | None |  |
| on_betrothal_broken |  | Yes | None |  |
| on_war_white_peace |  | Yes | None |  |
| three_year_playable_pulse |  | Yes | Character |  |
| on_defeat_raid_army |  | Yes | Army |  |
| on_army_enter_province |  | Yes | Character |  |
| on_join_court |  | Yes | Character |  |
| on_fired_from_council |  | Yes | Character |  |
| on_raid_loot_delivered |  | Yes | Army |  |
| on_pregnancy_ended_mother |  | Yes | None |  |
| on_title_lost |  | Yes | None |  |
| on_title_gain |  | Yes | Character |  |
| on_character_culture_change |  | Yes | Character |  |
| on_birth_child |  | Yes | Character |  |
| on_holy_order_hired |  | Yes | None |  |
| on_great_holy_war_invalidation |  | Yes | Great Holy War |  |
| on_combat_end_loser |  | Yes | Combat Side |  |
| on_concubinage |  | Yes | None |  |
| on_commander_combat_pulse |  | Yes | Character |  |
| random_yearly_everyone_pulse |  | Yes | Character |  |
| five_year_everyone_pulse |  | Yes | Character |  |
| on_perks_refunded |  | Yes | None |  |
| quarterly_playable_pulse |  | Yes | None |  |
| on_prestige_level_gain |  | Yes | None |  |
| on_faith_created |  | Yes | Character |  |
| on_holy_order_new_lease |  | Yes | None |  |
| on_title_gain_inheritance |  | Yes | None |  |
| on_game_start |  | Yes | None |  |
| on_character_faith_change |  | Yes | Character |  |
| on_combat_end_winner |  | Yes | Combat Side |  |
| on_courtier_decided_to_move_to_pool |  | Yes | Character |  |
| on_culture_era_changed |  | Yes | None |  |
| on_birthday |  | Yes | Character |  |
| on_faith_conversion |  | Yes | Character |  |
| on_raid_action_weekly |  | Yes | None |  |
| on_explicit_claim_gain |  | Yes | Character |  |
| on_courtier_ready_to_move_to_pool |  | Yes | Character |  |
| on_potential_great_holy_war_invalidation |  | Yes | Great Holy War |  |
| on_holy_order_destroyed |  | Yes | None |  |
| on_war_won_defender |  | Yes | Casus belli |  |
| yearly_global_pulse |  | Yes | None |  |
| on_great_holy_war_countdown_end |  | Yes | GreaT Holy War |  |
| yearly_playable_pulse |  | Yes | Character |  |
| three_year_pool_pulse |  | Yes | Character |  |
| on_pregnancy_father |  | Yes | None |  |
| on_piety_level_loss |  | Yes | None |  |
| on_piety_level_gain |  | Yes | None |  |
| on_siege_looting |  | Yes | None |  |
| on_title_destroyed |  | Yes | None |  |
| on_army_monthly |  | Yes | None |  |
| on_game_start_after_lobby |  | Yes | None |  |
| on_imprison |  | Yes | Character |  |
| on_birth_mother |  | Yes | Character |  |
| on_dynasty_created |  | Yes | None |  |
| on_alliance_removed |  | Yes | None |  |
| on_county_occupied |  | Yes | None |  |
| on_rank_up |  | Yes | None |  |
| on_vassal_become_powerful |  | Yes | None |  |
| on_join_war_as_secondary |  | Yes | Character |  |
| on_explicit_claim_lost |  | Yes | Character |  |
| on_alliance_broken |  | Yes | None |  |
| on_natural_death_second_chance |  | Yes | None |  |
| on_leave_council |  | Yes | Character |  |
| on_county_culture_change |  | Yes | None |  |
| on_war_started |  | Yes | None | On-action scopes: scope:defender/scope:attacker/scope:war |
| on_marriage |  | Yes | Character |  |
| on_great_holy_war_participant_replaced |  | Yes | Character |  |
| five_year_playable_pulse |  | Yes | Character |  |
| on_birth_real_father |  | Yes | None |  |
| on_game_start_with_tutorial |  | Yes | None |  |

