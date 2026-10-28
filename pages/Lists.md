<!-- 来源: https://ck3.paradoxwikis.com/Lists oldid=20403 抓取于 2026-10-22T22:28:03+08:00 -->

# Lists

Lists can be accessed using list-builders: `any_X`, `every_X`, `random_X`, `ordered_X`.

This article will use the `every_X` effect list-builder in its examples.

## Code lists

When a scope has the same relation to multiple others, those can be provided in a list built in code. For example, in a character scope, code provides the `child` list, which contains all children that character ever had.

### List Parameters

Some code lists have specific parameters that can be used in the list-builders. As those are parameters of the list, and not triggers, they don't go in the limit block.

- even_if_dead

Code lists of character scopes often only access living characters by default, even if the list technically includes dead character, in which case the `even_if_dead` parameter allows accessing dead characters.

```
every_child = {
   even_if_dead = yes
   limit = { < triggers > }
   < effects >
}
```

- scripted_relations

From a character scope, the `relations` list provides all scripted_relations of that character. The `type` parameter specifies which scripted_relations should be in the list.

```
every_relation = {
   type = friend
   type = lover
   limit = { < triggers > }
   < effects >
}
```

## scripted_lists

[top]

scripted_lists are defined in `common/scripted_lists` and are used to customize code lists often used with the same limit conditions.

Ex: list builder for adult unlanded children

```
adult_unlanded_child = {
   base = child # any vanilla list builder can be used as base
   conditions = {
      is_adult = yes
      is_landed_ruler = no
   }
}
```

Once defined as such, this scripted_list can be used with all list-builders, and further trimmed down using a limit block.

```
every_adult_unlanded_child = {
   limit = { < triggers > }
   < effects >
}
```

Note: as of 1.4.4, scripted_lists cannot be used in script_values, which is likely a bug.

## Custom lists

[top]

The `in_list` list-builder can be used to access arbitrarily named lists of scopes created in script.

### Normal lists

The `add_to_list` effect adds the scope it is executed from to the list with that name.

```
add_to_list = < list name >
```

Once the list is built, it can be accessed using list-builders through `in_list`, with the list name provided as a parameter:

```
every_in_list = {
   list = < list name >
   limit = { < triggers > }
   < effects >
}
```

Like a saved scope, a normal list is available throughout the unbroken effect chain it is built in.

### Variable lists

The `add_to_variable_list` effect adds the target scope to a list stored on the scope it is executed in.

```
add_to_variable_list = {
   name = < list name >
   target = < scope >
}
```

The target can be provided with a database reference, an event target, or a saved scope.

Once the list is built, it can be accessed using list-builders through the `in_list`, with the list name provided as a parameter:

```
every_in_list = {
   variable = < variable list name >
   limit = { < triggers >
   < effects >
}
```

.

Like a variable, a variable list is stored on a specific scope, and can only be accessed from that specific scope.
