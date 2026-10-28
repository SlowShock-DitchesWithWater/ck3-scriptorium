<!-- 来源: https://ck3.paradoxwikis.com/Interface oldid=35928 抓取于 2026-10-22T21:43:25+08:00 -->

# Interface — New windows and toggles


A new window can be added inside another or created in a separate file and spawned as a scripted widget.

Window visibility can be controlled with variables and Scripted Guis or entirely in UI with the UI Variable System.

However, it is difficult to make mods with new windows compatible with each other, since they need to add a button somewhere in an existing file to open the window.

Instead, the window could be opened with a decision, event or character interaction, but it would be less convenient for the player than a button on the hud.

### Create a window as a scripted widget

Make a new gui file with any name, for example `gui/new_window.gui`.

Create a window inside it like this, with any custom name:

```
window = {
	name = "my_window"
	layer = top
	using = Window_Size_MainTab
	using = Window_Background_Sidebar
}
```

Make a new folder called "scripted_widgets" in your gui/ folder.

Make a new txt file in it with any name, e.g. `gui\scripted_widgets\scripted_windows.txt`.

In it, add your gui file and the name of the window:

`gui/new_window.gui = my_window`

When the game loads to the map view, your window will be automatically created.

Multiple windows (or other widgets, buttons) can be created, each aded on the new line. E.g.:

```
gui/new_window.gui = my_second_window
gui/my_shortcuts.gui = my_button
etc...
```

### Toggle window visibility

The window can be toggled with UI variable system, variables or scripted guis.

**UI system**

Hide the window with:

`visible = "[GetVariableSystem.Exists('show_my_window')]"`

Have a button with:

`onclick = "[GetVariableSystem.Toggle('show_my_window')]"`

UI system is the quickest to set up, but all toggles will reset when closing the game, unlike with variables.

**Variables and SGUIs**

Hide the window with:

`visible = "[GetPlayer.MakeScope.Var('show_my_window').IsSet]"`

Make a button with:

`onclick = "[GetScriptedGui('toggle_my_window').Execute( GuiScope.SetRoot( GetPlayer.MakeScope ).End )]"`

And a scripted gui in `common/scripted_guis` with:

```
toggle_my_window = {
    effect = {
        if = {
            limit = {
                has_variable = show_my_window
            }
            remove_variable = show_my_window
        }
        else = {
            set_variable = show_my_window
        }
    }
}
```

Alternatively, it can be split into two sguis, one to set and one to remove the variable.

The variable can also be set in an event or a decision.

**SGUI**

A scripted gui can also be used for a more complex trigger.

In this case, hide the window with:

`visible = "[GetScriptedGui('show_my_window').IsShown( GuiScope.SetRoot( GetPlayer.MakeScope ).End )]"`

And have a scripted gui with:

```
show_my_window = {
    is_shown = {
        # various triggers
        is_adult = yes
        is_female = yes
        is_landed = yes
    }
}
```

Note that here the variable and the scripted gui scope to the player. Another object can be used instead or global variables/sguis, like this:

- `visible = "[GetGlobalVariable('show_my_window').IsSet]"`
- `visible = "[GetScriptedGui('show_my_window').IsShown(GuiScope.End)]"`

Remember that this window is created before the player selects the character. So when scopeing to the player, we might need to add a check that the player exists first.

For example, you can set up an invisible widget with100% size, `visible = "[GetPlayer.IsValid]"` and `alwaystransparent = yes` so it can be clicked through.

Then inside it would be your actual window with the variable or SGUI check.

There are a few other methods to create and toggle windows, but they are more cumbersome.

- PdxGuiWidget - straightfoward, but gets complicated with multiple toggles
- Animations - longer, but easier to trigger multiple things
- Console command `GUI.CreateWidget` - console commands don't work in multiplayer and disable achievements.

Below are older examples.

### Toggles with PdxGuiWidget

PdxGuiWidget is a simple function used to hide or reveal named elements.

In this example we have a container with a hidden submenu, one button that shows it and another that hides it.

1. when clicked, the first button goes back to its parent, searches in it for the submenu and the other button, reveals them and hides itself
2. the second button searches for the element and the button, reveals them and hides itself

```
container = {
	button = {
		name = "show submenu"

		onclick = "[PdxGuiWidget.AccessParent.FindChild('submenu').Show]"
		onclick = "[PdxGuiWidget.AccessParent.FindChild('hide submenu').Show]"
		onclick = "[PdxGuiWidget.Hide]"
	}

	button = {
		name = "hide submenu"
		visible = no

		onclick = "[PdxGuiWidget.AccessParent.FindChild('submenu').Hide]"
		onclick = "[PdxGuiWidget.AccessParent.FindChild('show submenu').Show]"
		onclick = "[PdxGuiWidget.Hide]"
	}

	widget = {
		name = "submenu"
		visible = no
	}
}
```

If the elements are separated by more parents/children, we can repeat AccessParent like this:

```
onclick = "[PdxGuiWidget.AccessParent.AccessParent.AccessParent.AccessParent.FindChild('submnenu').Show]"
```

Each button can hide or reveal multiple elements of any type. You only need to provide the name.

Pros:

- easy to set up for a simple toggle

Cons:

- the toggles will reset any time the game is restarted
- If you want to hide multiple things or toggles, the code will get very bloated and hard to manage
- trying to hide entries in a data list (like a dynamicgridbox) will only hide the first instance

### Toggles with animation

We can set up animations that are triggered by buttons (or conditions) to hide/show elements or to even move them. This way we don't need to count how many parents separate the button and the window and we can trigger many things at once with just one onclick.

The previous example would look like this and work the same way. The first button triggers "show_submenu", which hides the button and shows the rest, while the second button triggers "hide_submenu", which hides this button and the widget and shows the first button.

```
container = {
	button = {

		state = { # this is an animation
			name = show_submenu
			on_start = "[PdxGuiWidget.Hide]"
		}
		state = {
			name = hide_submenu
			on_start = "[PdxGuiWidget.Show]"
		}

		onclick = "[PdxGuiTriggerAllAnimations('show_submenu')]"
	}

	button = {
		visible = no

		state = {
			name = show_submenu
			on_start = "[PdxGuiWidget.Show]"
		}
		state = {
			name = hide_submenu
			on_start = "[PdxGuiWidget.Hide]"
		}

		onclick = "[PdxGuiTriggerAllAnimations('hide_submenu')]"
	}

	widget = {
		visible = no

		state = {
			name = show_submenu
			on_start = "[PdxGuiWidget.Show]"
		}
		state = {
			name = hide_submenu
			on_start = "[PdxGuiWidget.Hide]"
		}
	}
}
```

it is longer, but animations can be saved as templates and reused with one line, like `using = hide_animation`. Fullscreen Barbershop uses animations extensively, if you want a better example.

Pros:

- easier to link many things together, and even open a different window and trigger an animation in it

Cons:

- animation blocks can be quite lengthy
- all toggles will reset when the game is restarted

### System Variables

System variables are used internally by the game, they are not save persistent and cannot be directly accessed through scripts.

No setup is needed for them as they can be directly created in the .gui file.

The syntax for using system variables is:

`onclick = "[GetVariableSystem.Toggle( 'var_name' )]"`

or:

```
datacontext = "[GetVariableSystem]"
onclick = "[VariableSystem.Toggle( 'var_name' )]"
```

The available functions are:

- Clear - `Clear( 'var_name' )` clears the variable
- ClearIf - `ClearIf( 'var_name', Condition )` clears the variable if Condition is true
- Exists - `Exists( 'var_name' )` Boolean, returns true if the variable exists
- Get - `Get( 'var_name' )` CString, returns the string stored in the variable
- HasValue - `HasValue( 'var_name', 'string' )` Boolean, returns true if the variable has the provided string
- Set - `Set( 'var_name', 'string' )` sets the variable to the provided string
- Toggle - `Toggle( 'var_name' )` clears the variable if it exists, creates it if it does not
- SetOrToggle - `SetOrToggle( 'var_name', 'string' )` clears the variable if it exists and has the same string. If it doesn't, sets it to the provided string

#### Toggles with System Variables

A basic toggle using system variables in this file would looks like this:

```
container = {
	button = {
		onclick = "[GetVariableSystem.Toggle( 'gui_toggle' )]"
	}

	widget = {
		visible = "[GetVariableSystem.Exists( 'gui_toggle' )]"
	}
}
```

When clicked, the system variable is toggled depending on whether it exists, this is then used to show/hide the widget.

#### Tabs with System Variables

A basic setup for three tabs would look like this:

```
container = {
	button = {
		onclick = "[GetVariableSystem.Set( 'gui_tabs', 'tab_1' )]"
	}
	button = {
		onclick = "[GetVariableSystem.Set( 'gui_tabs', 'tab_2' )]"
	}
	button = {
		onclick = "[GetVariableSystem.Set( 'gui_tabs', 'tab_3' )]"
	}

	widget = {
		visible = "[GetVariableSystem.HasValue( 'gui_toggle', 'tab_1' )]"
	}
	widget = {
		visible = "[GetVariableSystem.HasValue( 'gui_toggle', 'tab_2' )]"
	}
	widget = {
		visible = "[GetVariableSystem.HasValue( 'gui_toggle', 'tab_3' )]"
	}
}
```

Note that the variable initially has no value and none of the widgets would show.

To set a default tab the variable needs to be set by the button opening the window:

```
button = {
	onclick = "[GetVariableSystem.Toggle( 'gui_toggle' )]" # this opens the window
	onclick = "[GetVariableSystem.Set( 'gui_tabs', 'tab_1' )]" # this set the default tab
}
```

or using a state block when the window is shown:

```
state = {
	name = _show
	on_start = "[GetVariableSystem.Set( 'gui_tabs', 'tab_1' )]"
}
```

Alternatively one of the widgets can be set to appear when the variable doesn't exist, avoiding the need for an initial value:

```
container = {
	button = {
		onclick = "[GetVariableSystem.Clear( 'gui_tabs' )]"
	}
	button = {
		onclick = "[GetVariableSystem.Set( 'gui_tabs', 'tab_2' )]"
	}
	button = {
		onclick = "[GetVariableSystem.Set( 'gui_tabs', 'tab_3' )]"
	}

	widget = {
		visible = "[Not( GetVariableSystem.Exists( 'gui_toggle' ) )]"
	}
	widget = {
		visible = "[GetVariableSystem.HasValue( 'gui_toggle', 'tab_2' )]"
	}
	widget = {
		visible = "[GetVariableSystem.HasValue( 'gui_toggle', 'tab_3' )]"
	}
}
```

This is the equivalent of the first example with one of the methods to set a default value.

Pros:

- simple and easy to remember syntax
- easier to link many things, even in different windows
- can be extended with additional commands (see below) to show entirely new windows, avoiding the need to have the widget in hud.gui

The downsides:

- no direct interaction with scripts, they must be set & cleared using the gui
- can be harder to keep track of
- all toggles will reset when the game is restarted

### Creating a new Widget

It is possible to create entirely new windows by using the `ExecuteConsoleCommand( ... )` command.

First create a window in a .gui file to be displayed, for example "gui/custom_windows/my_window.gui". Ensure that you have named the main window.

```
window = {
	name = "my_custom_window"
	parentanchor = center
	layer = middle
	size = { 100 100 }
	using = Window_Background
}
```

The above creates a 100 by 100 window in the center of the screen, the important part is the name as it is used to create the window.

The button to create the window would look like:

```
button = {
	onclick = "[ExecuteConsoleCommand('gui.createwidget gui/custom_windows/my_window.gui my_custom_window')]"
}
```

To close it:

```
button = {
	onclick = "[ExecuteConsoleCommand('gui.ClearWidgets my_custom_window')]"
}
```

Make sure that there is only one space between gui.ClearWidgets and my_custom_window. If there is more than 1 space, gui.ClearWidgets will clear all widgets created with console, not just my_custom_window.

Or combined into a toggle:

```
button = {
	onclick = "[ExecuteConsoleCommand( Select_CString( GetVariableSystem.Exists('my_window_open'), 'gui.ClearWidgets my_custom_window', 'gui.createwidget gui/custom_windows/my_window.gui my_custom_window' ) )]"
	onclick = "[GetVariableSystem.Toggle('my_window_open')]"
}
```

The toggle works by setting a system variable and selecting the command to execute based on it.

`Select_CString( ... )` takes three arguments:

- A Condition
- A string for true
- A string for false

If the condition returns true, the first string is used, else the second is. In the above toggle, if the system variable exists the window is destroyed, otherwise it is created.

