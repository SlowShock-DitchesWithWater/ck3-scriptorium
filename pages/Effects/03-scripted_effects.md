<!-- 来源: https://ck3.paradoxwikis.com/Effects oldid=20200 抓取于 2026-10-22T21:36:40+08:00 -->

# Effects — scripted_effects


Scripted_effects are macros that enable replacing an assortment of effects with a single statement, to make script more legible and avoid repetition.

They are defined in common/scripted_effects, and can be used anywhere effects are allowed.

A scripted_effect can use other scripted_effects, but recursion is not allowed.

### Simple form

Simple scripted_effects execute a predetermined set of effects.

Ex: if the following set of effects are repeatedly used to give a character gold, prestige and piety:

```
add_gold = 1000
add_prestige = 1000
add_piety = 1000
```

instead of repeating the same set of triggers in different places, they can be defined as a scripted_effect:

```
give_gold_prestige_piety = {
   add_gold = 1000
   add_prestige = 1000
   add_piety = 1000
}
```

and anywhere that set of effects needs to be executed, it can be replaced by the following statement:

```
give_gold_prestige_piety = yes
```

Because scripted_effects can be used in a variety of different contexts, it is advised not to use in their definition ambiguous event targets such as `root` or `prev`.

### Complex form

Scripted_effects can also have a complex form that handles literal text replacement, allowing to pass arguments.

Ex: if the following set of effects are repeatedly used to give a character gold, prestige and piety:

```
add_gold = 1000
add_prestige = 1000
add_piety = 1000
```

that set of triggers can be defined as a scripted_effect, but instead of using a specific value for those effects, the scripted_effect uses an argument defined in uppercase letters wrapped in two $ signs:

```
give_gold_prestige_piety = {
   add_gold = $VALUE$
   add_prestige = $VALUE$
   add_piety = $VALUE$
}
```

When used, the complex form of the scripted_effect specifies what the expected argument is, by using the same name but without the $ signs:

```
give_gold_prestige_piety = { VALUE = 1000 }
```

With that form, every occurrence of $VALUE$ in the scripted_effect will be *literally* replaced with the argument provided: the text replacement happens *before* the scripted_trigger is evaluated. For this reason, caution is advised when using scripted_effect arguments to pass event targets or script_values, because their interpretation is contextual.

Ex: consider the following scripted_effect that makes a character give gold to another character:

```
give_gold = {
   $GIVER$ = {
      remove_short_term_gold = $VALUE$
      $TAKER$ = {
         add_gold = $VALUE$
      }
   }
}
```

If used like so from a character scope to make the father give money to the mother:

```
give_gold = {
   GIVER = father
   TAKER = mother
   VALUE = 1000
}
```

Text replacement being literal means that the scripted_effect will be interpreted as such:

```
give_gold = {
   father = {
      remove_short_term_gold = 1000
      mother = {
         add_gold = 1000
      }
   }
}
```

So the character receiving the money is not the intended character.

To avoid such issues, arguments in scripted_effects can be saved as scopes within the scripted_effect itself, before doing any context switch.

```
give_gold = {
   $GIVER$ = { save_scope_as = giver }
   $TAKER$ = { save_scope_as = taker }
   save_scope_value_as = {
      name = gold_amount
      value = $VALUE$
   }
   scope:giver = {
      remove_short_term_gold = scope:gold_amount
      scope:taker = {
         add_gold = scope:gold_amount
      }
   }
   clear_saved_scope = giver
   clear_saved_scope = taker
}
```

