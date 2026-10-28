<!-- 来源: https://ck3.paradoxwikis.com/Interface oldid=35928 抓取于 2026-10-22T21:43:25+08:00 -->

# Interface — Inspecting GUI


We can inspect UI elements in the game with gui.debug inspector or with GUI Editor.

gui.debug is faster, but the editor can also edit the interface right in the game. That said, GUI Editor is very limited and is not recommended.

Both methods let us quickly open the right gui file in the text editor and even jump to the right line. This requires a little bit of setup (you only need to do it once).

If you don't have a proper text editor, install VSCode or Sublime.

To open gui files from the game:

1. Find the .exe file of your text editor, right click it and choose Copy as path.
2. Open pdx_settings.txt in Documents\Paradox Interactive\Crusader Kings III
3. Search for "editor" and in its value paste the path to your text editor, like this: `value="E:\Program Files\Microsoft VS Code\Code.exe"`
4. In the "editor_postfix" below add `:$ -rg` for its value, like this: `value=":$ -rg"`
5. Save the file.

The postfix is what tells the editor to jump to the right line.

For Pulsar and Notepad++, the editor_postfix value must be `":$:1"`, as in `value=":$:1"`.

After this you can launch the game and quickly open .gui files. The path can also be changed in the game console, using `settings` console command, but it will require restarting the game.

### GUI Debug

gui.debug is a console command that enables the inspector.

gui.debug tweaker

It shows a tooltip with debug information, allows us to select a gui element, open its .gui file and jump to its exact line.

To use it:

1. launch the game with `-debug_mode -develop` options.
2. Open the console with a ` (below Esc)
3. type `tweak gui.debug` and press Enter
4. In the tweaker menu uncheck all options and check GUI.Debug
5. After that you can use gui.debug command directly, without opening the tweaker. There is a button under the console for it.

(We disable other debug options because they highlight all existing elements and it can be overwhelming)

gui.debug tooltip

With the inspector active, your cursor will highlight a gui element with a green border and the tooltip will show its file. The number afterwards is the line it's on.

Alt + left-click selects other elements above or below.

Alt + right-click opens the .gui file in your text editor and jumps to the line with that element.

Optional:

To avoid opening the tweaker every time, consider adding your own button to the console, with these commands:

`onclick = "[ExecuteConsoleCommands('gui.DebugRenderOutsideParent;gui.Debug.DrawUnderMouse;gui.Debug.DrawAll;gui.Debug')]"`

This will toggle all the extra options and enable gui.debug. Then use the other button to only toggle gui.debug.

You can also make your own button with a hotkey that would fire gui.debug and spawn the button in with a scripted widget. See scripted widgets below.

### GUI Editor

GUI Editor

GUI Editor is a developer tool for editing the UI in the game.

While it may seem less intimidating then editing raw files, it is also much more limited.

To use it, launch the game with `-debug_mode` and `-develop` options.

To open the editor, either:

- press Ctrl+F8
- open the console with the ` key (below Esc), click GUI Editor
- open the console, run gui_editor command

**Features**

By default the editor starts with the Edit mode enabled. You can disable it in the top window, called Outliner. Hotkey "E".

- The edit mode is similar to the Inspect mode in browsers. While it’s enabled you can’t interact with the game, but it allows you to select parts of the UI and change them in the Properties window below.
- Scroll with your mouse wheel to change what element the editor should focus on, since hud.gui tends to get on top of other windows.
- Light blue border indicated the selected element. To hide other borders, uncheck "Show Hierarchy" in the Outliner (Hotkey "L").
- Holding the right mouse button allows to move the selected element.
- Alt+right-click opens the file with that element. Be careful, you can accidentally move the element with right click!
- To undo anything, press Ctrl+Z or the undo button in the Outliner. Redo is next to it, Ctrl+Y.
- Red stars * in the Outliner indicate unsaved changes. Press Ctrl+S or the save button at the top to save them. Make sure the gui files you're editing are in your mod, otherwise it will write the changes to the game folder. (To reset them, verify integrity from Steam's properties window)
- You can move any dev windows by dragging them and resize them by dragging the edges.
- You can drag UI elements in the Outliner's hierarchy to reorder them. Right-click to show the context menu.
- You can change or add new properties (by clicking the plus symbol) in the Properties window.

By clicking "Window" in the Outliner, you can open two more windows: UI components and Registered Data Types.

- UI Components is like a palette from which you can drag new elements to the UI. gui/shared/standard.gui and gui/defaults.gui contain the most common things, like buttons, icons and text.
- Registered Data Types may be used to look up what functions are available to display data from the game.
- Clicking the top right button in the Data Types will dump this data to your log folder (Documents/Paradox Interactive/Crusader Kings III/logs/data_types). You can also use `dump_data_types` console command.

Note: it is often easy to select a template by mistake, changing which will affect *all* instances of it in the UI. Pay attention to what file you have selected in the outliner. If you see in the Properties window a blue header that starts with "type:", it is a template, so be careful not to edit this part (unless you intend to).

