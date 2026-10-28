<!-- 来源: https://ck3.paradoxwikis.com/Interface oldid=35928 抓取于 2026-10-22T21:43:25+08:00 -->

# Interface — UI code


CK3’s UI is composed of containers and objects inside them.

Most windows, for example, are created using a `window` container, while map icons use a widget or an hbox.

The order in the file determines the order on the screen: what's lower in the code will appear on a higher layer.

Most elements can also contain others, for example, there can be a textbox inside an icon inside a button. Nested elements, aka children, will be moved with their parent.

Position is set relative to the top left corner (either of the screen or the parent). This can be changed with `parentanchor` property. The available options are: left, right, top, bottom, hcenter (horizontal center) and vcenter (vertical center). They can be combined with a | like this: `parentanchor = right|vcenter`.

Every element is opened and closed with curly brackets, like this: `container = { }`.

The common code style is to open and close the block on the same level, while indenting the contents with one tab:

```
widget = {
  size = { 50 50 }
  alpha = 0.5
}
```

This helps you see the structure of the code better, notice any missing or extra brackets, and is needed for some editors to correctly fold the blocks of code.

### Promotes and Functions

Each window has a predefined set of commands - promotes and functions - available for it. These can be found in the data_types*.log files in `Documents/Paradox Interactive/Crusader Kings III/logs/data_types` after you use the `dump_data_types` console command.

They are used to display all data from the game, like your name, gold, children, and to set button actions.

A promote returns a scope, i.e a game object, like Character or Province, while a function returns a number, a string or a boolean (true/false), etc.

Global commands can be used anywhere, like GetPlayer (returns the player character) or GetCurrentDate.

Other commands can only be used in their window/object, for example, GetParents can only be used in the character window and must be started with `CharacterWindow.GetParents`.

Commands can be chained like this:

`CharacterWindow.GetCharacter.GetPrimaryTitle.GetHeir.GetPrimarySpouse.GetFather`

Objects can inherit the scope from their parent, meaning we wouldn't need to retype the line above to show information about this character. Instead we can set `datacontext` of a widget to this line and then every textbox in it will use `"[Character.GetNameNoTooltip]"`, `"[Character.GetGold]"`, etc.

The same applies to items in gridboxes.

##### Type casting

Unlike in script, values in UI have different types: integers, fixed-points, floats, etc.

Most of them can be converted to another type with functions like FixedPointToFloat or IntToFixedPoint. This is called type casting.

This is necessary because some functions and elements require a specific type, for example, alpha parameter requires a float.

##### Casting numbers to strings

*(This is an advanced section. Skip it if you're just learning)*

Currently, there is no vanilla function to turn a number into a string. This may be needed for string comparisons or concatenating numbers with text.

The workaround is to pass the number to localization, which will then be treated as a string in UI.

Here are the steps, using player age as the example:

1. Create custom localization in common/customizable_localization:

```
NumberToString = {
    type = all

    text = {
        localization_key = number_to_string
    }
}
```

2. In the gui file, pass the number to it:

`raw_text = "[GuiScope.AddScope( 'number', MakeScopeValue(IntToFixedPoint( GetPlayer.GetAge ))).Custom( 'NumberToString' )]"`

Note that GetAge returns int32, and MakeScopeValue only accepts fixed-points, so we need to cast it first with IntToFixedPoint. Adjust this if your value is of a different type.

3. In the localization, we grab our saved 'number' scope:

```
l_english:
 number_to_string: "[SCOPE.GetValue('number')|0]"
```

And this will be passed to UI as a string. Localization number_to_string essentially replaces our whole line in the second step. Read more about customizable localization here.

The function in the second step can be replaced by a macro to make it shorter and easier to reuse.

To do that, create a new file in a data_binding folder (outside of gui):

```
macro = {
    description = "Returns the int32 as a string."
    definition = "GetString_int32(Arg0)"
    replace_with = "GuiScope.AddScope( 'number', MakeScopeValue(IntToFixedPoint(Arg0))).Custom('NumberToString')"
}
```

This can be used as `"[GetString_int32( GetPlayer.GetAge )]"` or `"[GetString_int32( '(int32)2' )]"`

### UI Components

These are basic components that compose all windows. The game has many predefined types, based on these components, which can be found in gui/shared.

You can preview some of them in the UI Library window. To open it, toggle release mode under the console and the UI Library button will appear above it.

`window`

- A movable container. To enable movement, add `movable = yes` property.
- Can be fixed size or resized by its children.
- In the game the background is set using templates, like `using = Window_Background` and `using = Window_Decoration`.
- If a child is outside of a window, it won't be clickable and won't show a tooltip. Use `allow_outside = yes` to change this.
- Clicking a window will bring it to the front of other windows that share the same layer. Use `PdxGuiWidget.StackTop` or `PdxGuiWidget.StackBottom` to manipulate the order.

`widget`

- A static container, similar to a window. Clicking it does not bring it to the front.

`margin_widget`

- Similar to a widget, but can be resized with margins. (This allows us to make windows that resize to screens of different size, by setting height to 100% and margins to ~50 to show the hud)

`container`

- Does not have a fixed size (but you can set maximumsize).
- Resizes automatically to fit all its children, including invisible ones. Use `ignoreinvisible = yes` to ignore them.
- Often used to group multiple elements to move them together.

`flowcontainer`

- Arranges all its children in a horizontal row and resizes to fit them. Use `direction = vertical` to make it vertical.
- Doesn't ignore invisible children by default. Use `ignoreinvisible = yes` to change it.
- Can't have fixed size.
- Its children cannot have positions, as they are set automatically.
- If you need to adjust position of its child, you can put it inside a container or a widget and then change position relative to this parent.

`hbox`/`vbox`

- Arranges all its children in a horizontal row and spreads them along its width. Vbox is the same but vertical.
- Can't have fixed size, instead resizes to fit its children or to the size of the parent, depending on the layout policy.
- Can be limited by minimumsize, maximumsize, min_width, max_width and margins.
- Ignores invisible children by default. Use `ignoreinvisible = no` to change this.
- Accepts datamodels (to create lists from game data).

`dynamicgridbox`

- Is only used with datamodels.
- Arranges all the items vertically. Use `flipdirection = yes` to make it horizontal.
- Doesn't ignore invisible items by default. Use `ignoreinvisible = yes` to change it.
- Resized by the content and limited by minimumsize and maximumsize.
- Items can be of different size.
- Can become laggy with very long lists.

`fixedgridbox`

- Similar to a dynamic box but all its items are of fixed size (it is essentially a table).
- Is only used with datamodels.
- Arranges all its items vertically. Use `flipdirection = yes` to make it horizontal.
- Cannot ignore invisible items.
- Can be fixed size, resized by the content and limited by minimumsize and maximumsize.
- Much better for performance with long lists.

`overlappingitembox`

- Is only used with datamodels.
- Arranges all its items horizontally and overlaps them if the list is longer that the size of the box. Use `flipdirection = yes` to make it horizontal.
- Can be fixed size or autoresized.

`scrollarea`

- A widget with scrollbars that appear if the content is bigger than its size.
- Scrollbars can be disabled with `scrollbarpolicy_horizontal = always_off` and `scrollbarpolicy_vertical = always_off`.
- Can be fixed size, resized by the content and limited by minimumsize and maximumsize.
- Game files primarily use a `scrollbox` type, which is a scrollarea with a background, scrollbar and margins.

`button`

- A clickable object. Accepts `onclick` and `onrightclick`.
  - When adding a right click function, include `button_ignore = none`.
- Doesn't have a texture by default.
- Can be fixed size or resized by its children.
  - A button without size can be used to add invisible hotkeys.

`icon`

- Displays a texture.
- Can be used as a widget to store children.
- Can be flipped with `mirror = horizontal` or `mirror = vertical`.

`textbox`

- Shows text.
- Can be fixed size or autoresized.
- Use `elide = right` or `elide = left` to cut off text that is too long
- Can be a single line or multiple, with `multiline = yes`.
- Game files primarily use types set in gui/shared/text.gui, like `text_single`. Use them to keep visual consistency and to type less code every time.

#### hbox/vbox

Hboxes and vboxes are resizable containers that order and resize or spread out their children. hbox orders children horizontally, vbox vertically, otherwise they work the same way, so all examples here apply to both.

They automatically center themselves and their children. Do not use parentanchor, it will break the layout. Instead use `expand={}` to push things to one side. See examples below.

Almost all windows use a vbox to arrange their contents vertically. As a rule of thumb, use expanding policies on a vbox and `expand={}` after it. This solves 90% of problems with layout.

**Important:** objects with large size can stretch boxes and mess up the layout. This often happens in vanilla with long text, especially with German and Russian languages.

Set max_width on your text and test it with very long strings. Use LOREM_IPSUM_TITLE and LOREM_IPSUM_DESCRIPTION localization keys to insert large placeholder text.

**Detailed behavior:**

On the screenshots below, hboxes have black background. All of the examples are available in the UI Library mod.

| By default, an hbox works similar to a flowcontainer: it orders children horizontally and resizes to fit them. hbox = { button_round = {} button_round = {} } |  |
| --- | --- |
| With `layoutpolicy_horizontal = expanding` it expands to the width of its parent and spreads its chilren out hbox = { layoutpolicy_horizontal = expanding button_round = {} button_round = {} } |  |
| To group its children, we can use `expand={}` to push them to one side. `expand` is a template widget with layout policies set to "growing" (defined in gui/shared/windows.gui) hbox = { layoutpolicy_horizontal = expanding button_round = {} button_round = {} expand = {} } |  |
| With "expanding" policy on children, it also resizes them This is useful for creating tabs, without needing to manually set their size hbox = { layoutpolicy_horizontal = expanding button_standard = { layoutpolicy_horizontal = expanding } button_standard = { layoutpolicy_horizontal = expanding } } |  |
| With "expanding" horizontal and vertical policy, the hbox and its children will resize in both directions hbox = { layoutpolicy_horizontal = expanding layoutpolicy_vertical = expanding button_standard = { layoutpolicy_horizontal = expanding layoutpolicy_vertical = expanding } button_standard = { layoutpolicy_horizontal = expanding layoutpolicy_vertical = expanding } } |  |

If placed in fixed size parent it will by default expand both horizontally and vertically up to entire size of the parent. But if placed in other vbox/hbox they will not expand to the parent size.

#### Layout policies

Layout policies control how children are resized by hboxes/vboxes. This also applies to boxes inside other boxes.

There are two types, layoutpolicy_horizontal and layoutpolicy_vertical, controlling horizontal and vertical behavior.

There are five policies, with fixed applied by default:

1. **fixed** - keeps original size. Cannot grow or shrink past it. An hbox/vbox with "fixed" will resize to fit children, like a container.
2. **expanding** - grows to the width/height of the parent, cannot shrink below original size. Has priority over children with other policies. If multiple children are set to "expanding", they split available space equally.
3. **growing** - same as "expanding" but with lower priority. If a child with "expanding" is present, "growing" will not grow. This also means the expand = {} widget would resize to 0, so change its policies if you want to use it with "expanding".
4. **preferred** - grows or shrinks, depending on available space.
5. **shrinking** - can shrink below its original size, cannot grow past it.

Layout policies also respect minimumsize, maximumsize, min_width and max_width.

| "expanding" takes priority over "growing" but will not shrink it smaller than the original (fixed) size hbox = { max_width = 400 layoutpolicy_horizontal = expanding button_standard_small = { layoutpolicy_horizontal = expanding } button_standard_small = { layoutpolicy_horizontal = growing } } |  |
| --- | --- |
| "preferred" and "shrinking" can both shrink, when there is little space. You may need to limit your hbox with max_width or "shrinking" policy to see this effect. hbox = { layoutpolicy_horizontal = shrinking button_standard_small = { layoutpolicy_horizontal = growing } button_standard_small = { layoutpolicy_horizontal = preferred } button_standard_small = { layoutpolicy_horizontal = shrinking } } |  |

#### Animation states

Animations can be created with `state`, like this:

```
state = {
    name = _show
    alpha = 0.5
    duration = 0.5
}
```

This state will set the alpha of its object to 50% over 0.5 second when it becomes visible, and it's triggered automatically due to its name.

States can:

- change properties, like size, position, alpha
- play sounds with `start_sound = { soundeffect = "event:..." }`
- execute functions, similar to a button, with `on_start` and `on_finish` instead of `onclick`

`on_start` triggers at the start of the animation.

`on_finish` triggers at the end, if the state has duration set. If not, it's instant like `on_start`.

***Known issue:*** `on_start` is currently bugged and triggers twice. Use `on_finish` whenever possible.

**State names**

There is a number of predefined names that automatically trigger the state:

- _show - triggers when the object becomes visible. Note that this only fires for the widget itself, not any of its children.
- _hide - when the objects becomes invisible
- _mouse_hierarchy_enter - when the cursor is placed over this window or button
- _mouse_hierarchy_leave - when the cursor leaves this window or button
- _mouse_press - when this button is pressed
- _mouse_click - when this button is pressed and released
- _mouse_release - when the button is released
- daily_tick - triggers every day
- monthly_tick - triggers every month

Some windows have their own specific state names, like `phase_change` and `new_battle_event` in the combat window.

**State triggers**

States can be given any other name and triggered manually, using it.

`TriggerAnimation` triggers one named state in the scoped object.

`PdxGuiTriggerAllAnimations` triggers all states with the same name that are visible on screen.

Examples:

`onclick = "[PdxGuiWidget.TriggerAnimation('my_state')]"` - triggers the state that's set inside the button itself.

`onclick = "[PdxGuiWidget.AccessParent.FindChild('widget_with_state').TriggerAnimation('my_state')]"` - goes to the parent of the button, finds a child named "widget_with_state" and triggers its state. You may need to chain multiple `AccessParent.AccessParent` to return higher in the hierarchy. `FindChild`, however, can search through multiple levels.

`onclick = "[PdxGuiTriggerAllAnimations('my_state')]"` - triggers all states with this name, even if they are in other (visible) windows.

***Known issue:*** if the state is inside an invisible object when `TriggerAnimation` or `PdxGuiTriggerAllAnimations` are used, the state will trigger later when the object becomes visible.

**Automatic triggers**

States can also trigger automatically when a condition is met.

`trigger_on_create = yes` - triggers when the window is first created. Not triggered by changing visibility, though it will generally be triggered when the parent widget becomes visible.

`trigger_when` - triggers when the condition is met.

Note that `trigger_when` doesn't prevent the state from firing when triggered manually, it doesn't work like a trigger in an event. It's more like its own on_action.

Bezier curve of Animation_Curve_Default

**Bezier**

For states with duration, a bezier curve can be used to control the rate of change of the animation, to add easing.

For example, this is a bezier curve used by many windows in the game, a template called Animation_Curve_Default:

`bezier = { 0.25 0.1 0.25 1 }`

The numbers are two sets of coordinates for the control points. See the image.

This curve means the window appears with a tiny delay, becomes visible much faster and then eases into 100%.

The effect is not very strong, but it helps create a more natural feeling.

Use this website to try out different bezier curves: https://cubic-bezier.com/#.25,.1,.25,1

To simplify, the two extremes are:

`{ 0 1 1 0 }` appears fast

`{ 1 0 0 1 }` appears slow

### Templates

Templates and types are named blocks of code which can be used multiple times throughout the code, like buttons, window backgrounds, and text styles. This helps maintain the same style and reduces the amount of code we write.

Templates can store the contents of an entire window or just one line, like this one:

```
template Window_Size_Sidebar
{
	size = { 610 100% }
}
```

This template can be used with "using = Window_Size_Sidebar", which will, essentially, replace the "using" line with the contents of the template.

Templates are global and can be defined in any .gui file. Most of the game templates are stored in gui/shared. A local version, local_template, has to be defined within the same file.

Commonly used templates and types can be seen in the UI Library. To access it, open the console, toggle Release Mode, and a new button called "UI Library" should appear.

#### Types

While templates may be as small as one property, types are always whole elements, like a button or a widget.

text_single and text_multi are types of a textbox with many properties already defined for them, so we don't need to retype them every time and instead simply write:

```
text_single = {
	text = "my text"
}
```

Types are defined in a slightly different way, by creating a named group of types first:

```
types Standard_Types
{
	type text_single = textbox {
	...
	}
}
```

The name of the group can be anything, it has no impact.

#### Blockoverride

Templates and types can have named override blocks, which allow us to edit a part of an instance without changing the whole template. For example, a template may have a default block of text:

```
block "text"
{
	text = "default_text"
}
```

To replace it, we add a blockoverride with the same name in our instance:

```
blockoverride "text"
{
	text = "actual text"
}
```

We can also remove it from our instance like this: `blockoverride "text" {}`

#### Replacing types

We can replace individual templates or types, without overwriting whole vanilla files.

For that, create a new file that comes **first** alphabetically. For example, start it with 00_. Like this: 00_my_types.gui.

If replacing a type, remember to define a group first, with any name. Then define the type inside it.

If it's a template, just put the template definition in, don't need to add anything else.

Example. Let's say we want to redefine button_standard_small to have a different default size. We'll create a new file, 00_small_button.gui and write in it:

```
types SmallButton {
  type button_standard_small = button_standard
    {
        size = { 40 25 }
    }
}
```

#### Adding mod compatibility

It is common that two mods overwrite the same GUI file and thus come into conflict if loaded together: only customizations made by the mod later in the load order will be present in the game.

Modders can collaborate to provide compatibility by using GUI types or templates and creating a "hook" for another mod inside their own.

To do this, one or both collaborating modders include usages of types/templates from the other mod inside the modded `.gui` file.

For example, a modder adds `some_other_mods_type = {}` or `using = some_other_mods_template` to `window_character.gui` or another modified vanilla file.

If this mod is then loaded together with the one which defines such a type or template, it will appear in the window. Otherwise, this line will have no visual effect - and a single error will be recorded to `error.log` once, on initial loading.

It is therefore good practice to extract custom additions made to vanilla `.gui` files into types/templates in separate custom `.gui` files, even if you're only using each addition once across your mod's own codebase. Doing so will allow other modders to achieve compatibility with your mod by inserting usages of your types/templates into their own code, potentially even without needing to coordinate with you.

#### Datamodels

Datamodels are used to display lists, eg:

`datamodel = "[CharacterWindow.GetChildren]"`

Datamodels can be displayed with: vbox, hbox, flowcontainer, dynamicgridbox, fixedgridbox, overlappingitembox.

A widget can also display a single item from a list like this:

```
datacontext_from_model = {
	datamodel = "[EventWindowData.GetOptions]"
	index = "1"
}
```

Many vanilla lists are hardcoded, meaning we can't add other items to them, remove them or change sorting.

However, some items in a list can be hidden with `visible = "[]"` parameter. Be aware of two issues:

- A fixedgridbox would leave empty gaps, because it doesn't dynamically resize its cells.
- A dynamicgridbox with multiple rows or columns would also have empty gaps.

In order to create custom sorting, we would need to make the same list in script, as a variable list, and then use ordered_in_list to sort it.

See Advanced Character Search mod for reference.

To display a variable list, use `[GetPlayer.MakeScope.GetList('list_name')]` or `[GetGlobalList]` for a global variable list.

If it's not saved on the player, then scope to the correct object, like `CharacterWindow.GetCharacter.MakeScope...`

See more below.

Do not confuse datamodel with datacontext!

Datacontext usually references a single promote, i.e. a game object, like `[CharacterWindow.GetCharacter]`.

One of very rare exceptions is the list of traits in the character window:

`datacontext = "[CharacterWindow.GetTraitArrays]" datamodel = "[TraitArrays.GetPersonalityTraits]"`

