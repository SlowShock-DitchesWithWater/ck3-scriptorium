<!-- 来源: https://ck3.paradoxwikis.com/Effects oldid=20200 抓取于 2026-10-22T21:36:40+08:00 -->

# Effects — Effect syntax


### Code effects

Code effects have a predetermined syntax. They usually require a specific scope type context to work.

The console command script_docs dumps the effects.log, which contains the list of all existing code triggers, in Documents\Paradox Interactive\Crusader Kings III\logs.

Code effects can take several forms:

#### Boolean form

Boolean effects are followed by `= yes`. The effect usually depends on the scope it is executed from, but otherwise it does not require any argument.

Ex: this effect releases the current character scope from prison.

```
release_from_prison = yes
```

#### Simple form

Simple effects require a single argument, provided on the right hand side of the `=` sign.

The argument can be:

- a scope

Ex: this effect makes the target scope the spouse of the current character scope

```
marry = scope:bride
```

- a database key

Ex: this effect changes the prison type of the current character scope

```
change_prison_type = house_arrest
```

- a numerical value

Ex: this effect adds the specified amount of gold to the current character scope

```
add_gold = 1000
```

#### Complex form

Complex effects use several parameters in a script block. Those parameters can be a boolean, a scope, a database key, a numerical value or a flag value.

Ex: this effects makes the target character, provided as a saved scope, a prisoner of the current character scope, and places them in house arrest.

```
imprison= {
  target = scope:imprisoned_character
  type = house_arrest
}
```

Some code effects have both a simple form and a complex form.

