<!-- 来源: https://ck3.paradoxwikis.com/Interface oldid=35928 抓取于 2026-10-22T21:43:25+08:00 -->

# Interface — Basics


The interface in CK3 is created through .gui files in the game/gui folder, which are somewhat similar to html files.

As such, you can edit them with any text editor, like VS Code, Sublime or Pulsar. Choose Python or Perl 6 for syntax highlighting, they fit well.

CK3 uses .dds files for textures, which are saved inside the game/gfx/ folder. Although it can also accept .png files in many places.

To edit or save .dds files use either Photoshop with Intel plugin or GIMP with this plugin.

Steam launch options for auto-reloading files

**Launch options**

To auto-reload gui files in the game and use console commands, add `-debug_mode -develop` launch options:

- right-click the game on Steam, choose Properties, in Launch Options at the bottom enter `-debug_mode -develop`

Every time a .gui file is saved it will be reloaded by the game.

**Important console commands:**

- `dump_data_types` - lists all available GUI functions in data_types*.log files in your log folder (Documents/Paradox Interactive/Crusader Kings III/logs/data_types)

You can merge all the log files to make it easier to search through them.

To do it quickly, make and run a .bat file in the data_types folder with this code: `type *.txt > ALL_DATA_TYPES.txt`

- `tweak gui.debug` - enables highlighting of UI elements. Uncheck all options, check gui.debug. The tooltip will show the exact file and line of the element.
- `release_mode` - shows the error counter on screen. Very useful to quickly spot when you made an error in UI. Can be toggled with a button under the console.
- `gui_editor` - opens the GUI editor, hotkey Control + F8

Error counter

Optional, not usually needed with hot reload:

- `reload gui` - reloads all gui files or a specific file if provided its name: `reload gui/frontend_main.gui`
- `reload texture` - reloads all texture files or a specific file: `reload texture flatmap.dds`

Other tips:

- keep the error log open to see if there is a mistake in the code (it's in the same log folder)
- keep the data types logs open, so your text editor uses it for autocompletion
- you can use test_gui.gui in gui/debug for testing. To show this window, open the console and click Test Window. To close it, run the `GUI.ClearWidgets` command.
- fold code so it's easier to see its structure. Usual hotkeys are Ctrl+K, Ctrl+1 (where 1 is the level at which to fold the code).

