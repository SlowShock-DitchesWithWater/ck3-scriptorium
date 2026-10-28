<!-- 来源: https://ck3.paradoxwikis.com/Event_modding oldid=37279 抓取于 2026-10-22T21:40:25+08:00 -->

# Event modding — Description


Text that is going to show up in the event window can include the event's title, description, option names, and option flavor text. To write a description for an event, you can either write out literal text in the event file, or you can refer the description to a localization key which is stored in the `your_mod\localization\english\` folder (where english can be replaced by the language of the localization key for your mod). In the vanilla files, localization keys are stored in a subfolder of `localization\english` called `event_localization`, but the game can read any localization key stored in the language folder.

```
my_event.0001 = {
    title = "The Event's Title" # Literal text which will show up in game exactly as displayed here
    desc = my_event.0001.desc # A localization key to be defined in your_mod\localization\english
    # ...
}
```

It can be useful to write literal text when in the early stages of writing an event, but it is generally not advised to use literal text in your mod as it produces an error in the error.log, and it prevents you from using the powerful data context tools that allow you to reactively write out a character's name, pronouns, etc. based on which characters are getting the event. See Localization for more information on how to use these data types. To make your descriptions even more reactive, you can also write out branching and complicated `desc` entries to account for different factors when the event fires. For example, you could write out different `desc` blocks to be displayed depending on the traits of the character who is getting the event. You can do this by using `first_valid` and `random_valid` inside of your `desc` entry.

```
desc = {
    first_valid = { # Display the localization of the first valid desc block which returns true
        triggered_desc = {
            trigger = {
                has_trait = drunkard
            }
            desc = my_event.0001.desc.drunkard # An loc key to display if the trigger is true
        }
        desc = my_event.0001.desc.fallback # Another loc key to display if nothing before it is valid to display
    }
    random_valid = { # Will display a random localization key, picking from any loc keys for which the triggers return true
        desc = my_event.0001.random_1
        desc = my_event.0001.random_2
        desc = my_event.0001.random_3
        triggered_desc = {
            trigger = {
                is_female = yes
            }
            desc = my_event.0001.random_4
        }
    }
}
```

`first_valid` will pick the first `desc` block inside of it which is valid (i.e., its triggers are true). If you want to set specific triggers, you can do so by using a `triggered_desc` block, which requires a trigger and a `desc` that it should display if this description is chosen. If you write in a `desc` block instead of a `triggered_desc` block, then its triggers will always be considered true, and it will always be a valid choice to display. This means that if you use a `first_valid` block and put a `desc` before a `triggered_desc` block, the `desc` will always display.

`random_valid` is similar to `first_valid`, but instead of picking the first `desc` which returns true, it will pick a random description that has true triggers. In this case, you can put the `triggered_desc` and `desc` keys in any order, as the choice will be randomized. Like with `first_valid`, a key that is simply `desc` will always be considered a valid choice for the random selection.

You can also combine `first_valid` and `random_valid` to make a more curated randomization for your description.

```
desc = {
    first_valid = { # Pick the first desc block that returns true
        triggered_desc = { # If the character has brave...
            trigger = {
                has_trait = brave 
            }
            desc = { # Then randomly pick one of these
                random_valid = {
                    desc = my_event.0001.brave.random_1
                    desc = my_event.0001.brave.random_2
                    desc = my_event.0001.brave.random_3
                }
            }
        }
        desc = { # Otherwise, if not brave, randomly pick one of these
            random_valid = {
               desc = my_event.0001.fallback.random_1
               desc = my_event.0001.fallback.random_2
               desc = my_event.0001.fallback.random_3
            }
        }
    }
}
```

You can make these descriptions quite varied and complicated by combining these together, but be aware that writing a lot of alternatives for events can be quite time consuming. You can also combine `desc` entries by adding multiple `desc` keys outside of a `first_valid` or `random_valid` entry.

```
desc = {
    desc = { # Only display the opening if the character has the blind trait
        first_valid = {
            triggered_desc = {
                trigger = {
                    has_trait = eccentric
                }
                desc = "Many people have said, because of my eccentricity,"
            }
        }
    desc = "I am an endless font of inspiration," # Always display the middle
    desc = { # Display a different ending depending on if the character has the pregnant trait
        first_valid = {
            triggered_desc = {
                trigger = {
                    has_trait = pregnant
                }
                desc = "and I hope that I am able to pass that on to my child."
            }
            desc = "and it feels good to be appreciated like that."
        }
    }
}
```

The above description will output as many as three separate localization keys as a single event description. If the character receiving the event is eccentric and pregnant, then the event description will read: "Many people have said, because of my eccentricity, I am an endless font of inspriation, and I hope that I am able to pass that on to my child." If the character is eccentric, but not pregnant, then it will read: "Many people have said, because of my eccentricity, I am an endless font of inspiration, and it feels good to be appreciated like that." If the character is not eccentric but is pregnant, then it will read: "I am an endless font of inspiration, and I hope that i am able to pass that on to my child." And, finally, if the character is neither eccentric nor pregnant, it will read: "I am an endless font of inspiration, and it feels good to be appreciated like that."

You can make very complex event descriptions like this, but it can take a lot of work to make sure that all of the possible variations are able to work together, so if you're going to do complciated things, you're going to want to aggressively test the various permutations of your event's description to make sure that all of them make sense.

Also note that when you combine localization strings like this, they are concatenated with a space between strings. If you write two localization keys that say "I have seen this before", and ", haven't you?", then when combined, the description will read: "I have seen this before , haven't you?" So be careful when splitting localization keys to avoid misplaced spaces. On a similar note, the developers also seem to use the en-dash instead of the em-dash for punctuating description text, as the generally accepted use of an en-dash involves a leading and trailing space, whereas an em-dash is usually abutting both characters it is between (e.g., "Hello – how are you?" vs. "Hello—how are you?"), which makes it easier to disguse where the cuts are between localization keys.

`desc` blocks can be used in various places, as well, such as in the names for options:

```
option = {
    name = {
        text = {
            first_valid = {
                triggered_desc = {
                    trigger = {
                        is_female = yes
                    }
                    desc = my_event.0001.a.female
                }
                desc = my_event.0001.a.fallback
            }
        }
    }
}
```

When it comes to options, however, you have to use a `text` block between `name` and `first_valid`, or else the description won't display properly. Alternatively, for `option` blocks, you can also do it like:

```
name = {
    trigger = { has_trait = brave }
    text = my_event.0001.a.brave
}
```

You can also use these more complex descriptions in `flavor` blocks, and for those you do not need to use the `text` block, but can just do it the same as a description block:

```
flavor = {
    first_valid = {
	triggered_desc = {
	    trigger = {
                is_female = yes
             }
	     desc = my_event.0001.a.flavor.female
	}
    desc = my_event.0001.a.flavor.fallback
    }
}
```

