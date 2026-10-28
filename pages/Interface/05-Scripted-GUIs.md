<!-- 来源: https://ck3.paradoxwikis.com/Interface oldid=35928 抓取于 2026-10-22T21:43:25+08:00 -->

# Interface — Scripted GUIs


Scripted guis are, essentially, hidden events triggered from the UI.

They are stored as .txt files in game/common/scripted_guis.

The simplest scripted gui looks like this:

```
my_sgui = {
  effect = {
    add_gold = 100
  }
}
```

It can be used in the UI, scoping to the player, like this:

```
onclick = "[GetScriptedGui('my_sgui').Execute( GuiScope.SetRoot( GetPlayer.MakeScope ).End )]"
```

If an sgui uses global effects, like `every_player = { add_gold = 100 }`, it can be used without scoping:

```
onclick = "[GetScriptedGui('my_sgui').Execute( GuiScope.End )]"
```

Other optional parameters are:

```
gui_name = {
	scope = character 		# the root scope, i.e. the target of the effects
	saved_scopes = {} 		# any additional targets

	confirm_title = "your_title"	# adding this will prompt the player to confirm the action
	confirm_text = "your_text"	# additional text in the confirmation popup

	effect = {			# what it does
		custom_tooltip = ""	# adds a tooltip
	}

	is_shown = {} 			# is it visible in the UI?

	is_valid = {} 			# can the player use it? always checked, even if you don't use enabled property on the button

	ai_is_valid = {} 		# is the AI allowed to use it? Disabled by default.
}
```

Not all blocks are necessary. A scripted gui may only contain is_shown or is_valid.

Instead of always linking to the sgui, we can declare it once with datacontext and then all other functions used in that object or its children will use that sgui:

```
datacontext = "[GetScriptedGui('gui_name')]"

onclick = "[ScriptedGui.Execute( GuiScope.SetRoot( GetPlayer.MakeScope ).End)]"

visible = "[ScriptedGui.IsShown( GuiScope.SetRoot( GetPlayer.MakeScope ).End)]"

enabled = "[ScriptedGui.IsValid( GuiScope.SetRoot( GetPlayer.MakeScope ).End)]"

tooltip = "[ScriptedGui.BuildTooltip( GuiScope.SetRoot( GetPlayer.MakeScope ).End)]"
```

Instead of `GetPlayer.MakeScope` we can scope to another game object, for example, the character in the character window:`CharacterWindow.GetCharacter.MakeScope`, or if the root of our sgui is a province, `HoldingView.GetProvince.MakeScope`.

`ScriptedGui.Execute` executes everything listed in the `effect` block. It's used with `onclick` for buttons and `on_start` or `on_finish` with animation states.

`IsShown` and `IsValid` check for conditions in is_shown and is_valid blocks. Both blocks simply return true or false and could be used with other functions, like `AddTextIf`, Select_CString, etc.

`BuildTooltip` can also be used with a textbox to display the tooltip as text.

To add another scope to our scripted gui, we use AddScope like this:

```
"[ScriptedGui.Execute( GuiScope.SetRoot( GetPlayer.MakeScope ).AddScope( 'target', CharacterWindow.GetCharacter.MakeScope ).End )]"
```

It's then used as `scope:target` in the sgui. You may use any name.

Multiple scopes can be saved this way: `AddScope().AddScope().AddScope().End`

You don't have to declare any added scopes in saved_scopes. If you do, the game will always check for them and if they are not added in the gui file, the sgui won't work.

We can also pass values, text and booleans from UI to sguis, using `MakeScopeValue`, `MakeScopeFlag` and `MakeScopeBool`

For example:

```
onclick = "[GetScriptedGui('give_gold').Execute( GuiScope.SetRoot( GetPlayer.MakeScope ).AddScope( 'balance', MakeScopeValue(GetPlayerBalance) ).End )]"
```

The number is then referenced as any other saved scope: `add_gold = scope:balance`

MakeScopeValue expects fixed point values, so you may need to convert the value first with IntToFixedPoint.

It can also accept a number directly: `MakeScopeValue('(CFixedPoint)25')`

It is important to not put any spaces before the dots or opening parentheses! `Execute(` is correct, `Execute (` is not. Other spaces can be omitted, but they help with readability.

### Displaying a variable or script value

Variables and script values can be shown in the UI like this:

A variable:

`text = "[GetPlayer.MakeScope.Var('var_name').GetValue|1]"`

A script value (defined in common/script_values):

`text = "[GetPlayer.MakeScope.ScriptValue('sval_name')|0]"`

Alternative method that allows to add another scope with AddScope:

`text = "[GuiScope.SetRoot( GetPlayer.MakeScope ).AddScope( 'target', CharacterWindow.GetCharacter.MakeScope ).ScriptValue('sval_name')|0]"`

In these examples the player character has the variable and serves as the root of the svalue. Other promotes can be used too, as long as they can use MakeScope. Search through data types logs to see if it's supported (e.g. Character.MakeScope)

|1 at the end is optional and will round down to 1 number after the decimal point, so instead of 1.573 you will see 1.5. You can set this at any number, add % to convert to a percentage, add = or + to color the value if it's positive or negative.

|O can be used with integers to display the number as an ordinal: `['(int32)2'|O]"` will be shown as `2nd`. Note, this is a capital letter O, not number zero.

To convert a script value to an integer use FixedPointToInt.

Note that script values displayed in UI are calculated on every frame, so if you have a big list of items, a big svalue calculation may impact performance, so it may be better to use variables.

When using localization to display values in events, we use this:

`event_var: "[ROOT.GetCharacter.MakeScope.Var('test_var').GetValue|0]"`

`event_value: "[SCOPE.ScriptValue('test_value')|0]"`

If you have a saved scope (named "target" here), it changes to this:

`event_var: "[target.MakeScope.Var('test_var').GetValue|0]"`

`event_value: "[GuiScope.SetRoot( target.MakeScope ).ScriptValue('test_value')|0]"`

### Displaying data lists

We can create custom lists of characters, for example, to make societies.

To do this, first, we need to add them to a variable list. This can be done though an event or a scripted gui, like this:

```
effect = {
	every_living_character = {
		limit = {
			has_trait = paranoid
		}

		root = {
			add_to_variable_list = {
				name = secret_society
				target = prev
			}
		}
	}
}
```

If we fire this effect for the player, they will be the `root`, so the list will be stored in them.

Then we use any list box (vbox, dynamicgridbox, fixedgridbox) with the datamodel set to our list

```
dynamicgridbox = {
	datamodel = "[GetPlayer.MakeScope.GetList('secret_society')]"

	item = {
		flowcontainer = {
			datacontext = "[Scope.GetCharacter]"

			portrait_head_small = {}

			text_single = {
				text = "[Character.GetNameNoTooltip]"
			}
		}
	}
}
```

To access the item, we need to use `Scope` and the matching function of our object, like `GetCharacter` or `Title`. Check Data Types to see what `Scope` functions are available. We can declare it once with a datacontext and then continue to use `Character`.

Note, your datacontext should not be inside `item = {}` itself, but inside the widget used there (be it a button, a text or a flowcontainer like here)

