<!-- 来源: https://ck3.paradoxwikis.com/Effects oldid=20200 抓取于 2026-10-22T21:36:40+08:00 -->

# Effects — Effect blocks


Effects are executed in effect script blocks.

Those are either explicitly named so, like a decision's `effect = { }` block, or their name alludes to when the effect block is executed, like an event's `immediate = { }` block which is immediately executed when the event fires, even before the event window opens, by opposition to the event's `after = { }` block, which is executed after any event option has been picked.

Some effect blocks are executed when something else happens, like a character interaction's `on_accept` block, and must not be confused with on_actions.

In some cases, effects are used in hybrid blocks that accept effects amongst other things. Ex: event options

```
option = {
   is_shown = { is_ai = yes }
   ai_will_do = { base = 100 }
   add_gold = 100
}
```

In this block, `add_gold` is the effect executed when the option is picked, but `is_shown = { }` is a trigger block and `ai_will_do` is an aI logic block.

