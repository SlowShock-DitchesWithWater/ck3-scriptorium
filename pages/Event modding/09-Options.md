<!-- 来源: https://ck3.paradoxwikis.com/Event_modding oldid=37279 抓取于 2026-10-22T21:40:25+08:00 -->

# Event modding — Options


Options within events are able to be pressed by the user. Each event may have any number of options, including none at all (a common example includes hidden events). Each option in defined in the main event block, like so:

```
example.1 = {

	# [...]

	option = {
		# option info
	}

	# [...]

}
```

A more complex example:

```
option = { # Option title
	name = stewardship_domain_special.1424.a
	trigger_event = { # Makes another event happen
		id = yearly.1012 # The event ID is the thing at the top (so stewardship_domain.6017 is valid, as is any other event, so long as it exists).
		days = { 7 14 } # Get random number between two values (unknown wether it is inclusive or exclusive), anything that takes = {X Y} can also just work as = X
	}

	hidden_effect = { # Hides stuff from showing up on the tooltip of the option
		scope:county = { # Gets the location stored in the scope "county"
			add_county_modifier = { # To add modifiers (bonuses or penalites)
				modifier = governance_land_cleared_for_settlement_modifier # https://ck3.paradoxwikis.com/Modifier_list be sure to use one that belongs to the right type (in this case, country).
				days = 3650 # How long it lasts, you can use days = {X Y} too
			}
		}
	}

	ai_chance = {
		base = 50 # What are the chances of selecting this option over others? (Does not need to be 0 to 100, it can be anything)
		modifier = {  # You can change the value based on a variety of things, in this case it is the traits of the AI character
			add = 15
			has_trait = sadistic # List of traits can be found at ..\game\common\traits\00_traits.txt
		}
		modifier = {
			add = -40 # To remove something you just add a negative number (5 + -10 = -5)
			has_trait = compassionate
		}
	}
}
```

The table below describes available keys within the `option` block:

| Key | Required | Description | Example |
| --- | --- | --- | --- |
| name | Yes | Points to a localization key for the event option button text. | name=example.1.a |
| (effects) | No | Any effects that the option may have can be written directly in the `option` block. | play_music_cue = mx_cue_banquet |
| trigger | No | Defines a trigger that has to be fulfilled for the option to be valid and thus available to the user. Not to be confused with the main event trigger. | trigger = { has_trait = shy } |
| show_as_unavailable | No | If the option is invalid, but this trigger is, the option will be shown, but disabled. This behavior is also influenced by the EVENT_OPTIONS_SHOWN_HIDE_UNAVAILABLE define. | show_as_unavailable = { short_term_gold < medium_gold_value } |
| trait | No | If the player has the given trait, show it on the left side of the option. Hovering over it will say the option is available because of the trait. This is only providing flavor, and does not actually affect the functionality of the option. | trait = honest |
| skill | No | Show the chosen skill on the left side of the option. Hovering over it will say the option is available because of your high skill. This is only providing flavor, and does not actually affect the functionality of the option. | skill = prowess |
| add_internal_flag | No | Can take the values "special" or "dangerous". The key "special" highlights the option as yellow, "dangerous" highlights the option as red. This is only providing flavor, and does not actually affect the functionality of the option. | add_internal_flag = special |
| highlight_portrait | No | Highlights the event portrait of this character while this option is hovered. This is in addition to the automatic highlighting when hovering an event option that has an effect that affects portrait characters. | highlight_portrait = scope:custom |
| fallback | No | If this is yes: if no other options meet their triggers, then this option will be shown even if its trigger is not met either. You can use this together with `trigger = { always = no }` to create an option that is only ever shown as a last resort. | fallback = yes |
| exclusive | No | If an option is marked exclusive = yes and it meets its triggers, it will be the only option shown. If multiple options are marked exclusive = yes and each meets their triggers, each will be shown. | exclusive = yes |
| flavor | No | Flavor text that is shown in the tooltip of the option. The flavor can either be a loc key or a dynamic desc with first_valid etc. | flavor = my_events.1001.a.flavor |

