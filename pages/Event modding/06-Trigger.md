<!-- 来源: https://ck3.paradoxwikis.com/Event_modding oldid=37279 抓取于 2026-10-22T21:40:25+08:00 -->

# Event modding — Trigger


This is an additional requirement for an event to work.

```
trigger = { # This is the set of requirements necessary for this event to enable (a gigant IF statement for the event itself)
	culture = {
		has_innovation = innovation_guilds # Checks if you have unlocked guilds on your cultural research
	}
}
```

You can also lock certain requirements in a trigger behind a trigger of their own, using `trigger_if`.
The requirements inside of the `trigger_if` will only be checked if the contents of the `limit` block are true. Optionally, you can add a `trigger_else` afterwards to check alternative requirements if the `trigger_if` fails.

```
trigger = {
	any_held_county = { # We check that we have a blacksmith
		any_county_province = {
			has_building_or_higher = blacksmiths_01
		}
	}

	trigger_if = { # If our character is greedy, then we add the requirement to have 500 gold
		limit = { has_trait = greedy }
		gold > 500
	}
	trigger_else = { # Otherwise, you must have at least 50 piety and 10 gold
		piety > 50
        gold > 10
	}
}
```

The trigger is checked before the event fires, which means that you cannot use any of the scopes created in the Immediate block when checking if certain characters meet triggers. For example, if you wanted to create an event where you wanted to know if a knight had the brave trait, you could not create a scope called `scope:knight` in the immediate block and then check that same scope in the trigger. Instead, to check if a character could meet the triggers for your event, you probably want to use a list builder.

```
trigger = {
    any_knight = { # Will look at all knights of the root character to see if any match the triggers
        has_trait = brave
    }
}
```

### on_trigger_fail

Runs when the trigger fails.

