<!-- 来源: https://ck3.paradoxwikis.com/Event_modding oldid=37279 抓取于 2026-10-22T21:40:25+08:00 -->

# Event modding — Immediate


This is a block of effect script: it will be ran *immediately* as your event is triggered, before the title, description, portraits, are even evaluated let alone rendered. This block is useful for setting variables and saving scopes to use in your text or for portraits; or for functional effects that you want to happen without the player having any control over it.

"has happened" tooltip.

```
immediate = { # Stuff that happens when the event appears on screen, works regardless of what option you select.
	add_gold = 50 # adds 50 gold to the player 
}
```

