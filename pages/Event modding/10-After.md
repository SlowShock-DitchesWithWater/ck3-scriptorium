<!-- 来源: https://ck3.paradoxwikis.com/Event_modding oldid=37279 抓取于 2026-10-22T21:40:25+08:00 -->

# Event modding — After


This is a block of effect script that runs after the event has ran its course and an option has been chosen. Works the exact same as the immediate block. Won't do anything if the event has no options (for hidden events, for example).
 It is most commonly used for clean-up duty, removing variables, characters, and other kinds of data that are likely to persist when not intended to.

As an example, in the event `fp2_struggle.2009`, "Catching Thieves of Myth", the `after` block is used to check if we have a saved scope (used as a boolean) to decide if we should delete the event-generated character once the event is over.

```
after = {
	if = {
		limit = { NOT = { exists = scope:fp2_2009_thief_permanence_scope } } # Acts as a boolean, if this exists, then it is true
		scope:fp2_2009_garduna_young_thief = { silent_disappearance_effect = yes } # We kill (delete) the young thief, as it is no longer of use for future events
	}
}
```

