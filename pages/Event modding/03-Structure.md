<!-- 来源: https://ck3.paradoxwikis.com/Event_modding oldid=37279 抓取于 2026-10-22T21:40:25+08:00 -->

# Event modding — Structure


The overall structure is similar to that of a CK2 event, with some tweaks to the syntax and a whole lot of extra features, many of them optional. The barest possible event is laid out here, and each element is described individually in a later section.

```
namespace = example
example.1 = {
	desc = example.1.desc
	
	option = {
		name = example.1.a
	}
}
```

There you go! Add this to your mod, trigger it from the in-game console using "event example.1", and you have got yourself a working event! Everything else is optional, but necessary to really flesh out the events. This is as bare-bones as it gets. Here is an example of a more fleshed out event, containing only the basics:

```
## This a basic event, use it as a base for other events. Though you probably will want to remove the annotation spam first.
superexample.1337 = { # Use comments (like this one!) to put the event name here, this way other scripters can find the event you are working on without knowing the ID.
	type = character_event
	title = "A Modding Example Worthy of Kings" # Protip: you can use strings and later replace it with loc refs later
	desc = birth.1003.b # For Sublime users: there is a "find in files" feature that is excellent for digging through loc

	theme = mental_break
	left_portrait = root

	option = { # Use comments to state what the option says or does (eg "No, I denounce you heretic!" or "Engage in duel against child"), much like with event titles, it's good practice.
		name = stewardship_domain_special.1424.a
	}
}
```

### ID and namespace

Namespaces can be any alphanumeric string (without the '.' character), and are used as prefix in the form `<namespace>.<id>`. The ID uniquely identifies your event.

If an event file uses a namespace, it has to be declared at the beginning of the file with `namespace = <namespace>`. This has to be done for every file the namespace is used in.

Notice that if the ID exceeds 9999, the event calling system will become buggy, so please consider the max allowed ID for a given namespace as 9999.

### Flags

These are top-level variables that determine your event's kind and appearance. They have a limited set of values.

| Flag | Meaning | Possible values |
| --- | --- | --- |
| type | The kind of event. It determines what sort of scope the root is. | character_event letter_event duel_event none (when an event doesn't use the root scope at all) empty (necessary for characterless events to trigger. NOTE: this means typing type = empty ) |
| hidden | Set this to true, and the event will not be shown at all; it will happen in the background. Useful for doing maintenance events that are not immediately relevant to the player. | true, false |

