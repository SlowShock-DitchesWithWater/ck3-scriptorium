<!-- 来源: https://ck3.paradoxwikis.com/Event_modding oldid=37279 抓取于 2026-10-22T21:40:25+08:00 -->

# Event modding — Strategy


### Triggering the event

|  | Please help improve this article or section by **expanding it**. |
| --- | --- |

Events do not fire automatically, they have to be fired by something in the script, for example:

- on_actions
- story cycles
- decisions
- character interactions

etc.

### Techniques and design patterns

|  | Please help improve this article or section by **expanding it**. |
| --- | --- |

If you just input the information in your will be overriding vanilla on_actions. The example below is just one of the way to add in your own events.

```
five_year_playable_pulse = { 
	on_actions = { my_five_year_playable_pulse }
}
my_five_year_playable_pulse = {
		random_events = {
# Your event change name is here.
	}
}
```

Pinging events, message events.

Other fancy ideas.
