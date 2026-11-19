English | [简体中文](README.zh-CN.md)

# Copy Room — Scriptorium's knowledge bases for other mods

> The scriptorium's main body serves **vanilla** CK3; the Copy Room builds
> isomorphic knowledge bases for **other mods** (workshop or local), to
> support sub-mod (sub-mod / compatibility patch) development: look up the
> parent mod's added effect/trigger/on_action signatures, find which file
> defines an entry, and see the API-surface diff against vanilla.

## Name

One of the rooms of the scriptorium. A copy room is where scribes transcribe
**derivative works against a master copy** — the parent mod is the "master
copy" a sub-mod is developed against. Sibling rooms: the Map Room
(`map_room/`), the Reading Room (`reading_room/`).

## Architecture (three channels, all reusing the existing pipeline)

A mod KB lives side by side with this documentation: every `<mod-id>/`
subdirectory below this folder is one mod's KB (built locally, never
committed). The isomorphic refresh entry for the vanilla side is
`python scripts/run.py --stage game` (one command, all three channels).

| Channel | Products | Prerequisite |
|---|---|---|
| Signature layer (authority) | `copy_room/<mod-id>/script_docs/` (12 lists, converted from the mod-loaded dump) | **The user must run `script_docs` + `dump_data_types` in-game with the target mod loaded** (both commands; the export lands in Documents\...\Crusader Kings III\logs\) |
| Structure layer (navigation) | `copy_room/<mod-id>/structure/` (INDEX + entry_map.tsv + per-subdirectory summaries of common/) | No game launch needed — scans the mod folder directly |
| Map layer (map-replacing mods) | `copy_room/<mod-id>/map_docs/` (dossier + province_index.tsv + nudger parameters, same trio as the Map Room) | No game launch; built automatically when the mod ships `map_data/definition.csv` (the core knowledge for total-conversion mods like EK2), otherwise skipped |
| Diff report | `copy_room/<mod-id>/DIFF_vs_vanilla.md` | Auto-generated: signatures added/removed by this mod vs vanilla (the new API surface a sub-mod may call) |

**Measured basis (2026-11-09, Elder Kings 2)**: with a mod loaded, the dump
is a "vanilla + mod" merged view (effects +4, triggers +13, on_actions +145,
custom_localization +641, data_types +245; the code-side native lists
unchanged) — the dump channel works for mods and is required.

## How to use

```bat
:: 1) List mods available on this machine (workshop + local, with id/name/path):
python scripts\copy_room.py --list

:: 2+3) One command, three steps (STEAM version): headless export of the
::    mod-loaded dump (the game starts twice with -mod=<its .mod file> and
::    exits on its own; Steam client must be running) -> build the KB ->
::    headless re-export of the vanilla dump (restores Documents logs so a
::    later --stage game never picks up the merged view):
python scripts\copy_room.py --build --id 2887120253 --auto

::    Manual alternative for the export step: launch the game with the target
::    mod (-debug_mode), run BOTH console commands (script_docs and
::    dump_data_types), quit; then build without --auto (--path for local mod
::    folders, --name to override naming, --dump to select a dump copy
::    elsewhere).

:: 4) Verify the catalog's Copy Room section (optional):
python scripts\copy_room.py --check
```

Platform note: the headless exporter follows the **Steam-version** layout
(the game exe at `binaries\ck3.exe`, next to the `game\` folder of the
install directory). The Microsoft Store / Game Pass PC edition installs
under WindowsApps with a different layout and does not need the Steam
client — set `game_exe` (and `game_dir`) in `scripts\state\local_paths.json`
to adapt; untested here. One launch runs ONE console command (the game exits
after each), which is why every export means two game starts.

If the signature layer is missing (step 2 never ran), `--build` still
completes the structure layer and leaves a notice; re-run `--build` after
exporting the dump.

## Catalog indexing convention

The Copy Room section at the end of `catalog.md` is a **static pointer**
(to this README and `ls copy_room/`), never a listing of KBs — mod KBs are
local-only products, and a listing would tie the published catalog to one
machine's directories. Each KB carries its own `README.md` recording origin,
composition and retrieval entry; `--sync` rebuilds the section if damaged,
`--check` verifies its presence (CI runs this).

## Publishing boundary (important)

`copy_room/<mod-id>/` is **never published** (the `copy_room/*` rule in
.gitignore, this README excepted): mod content belongs to its authors, and
the volume is considerable. Anyone can rebuild an equivalent locally with
the steps above — same policy as `game logs/`. The Copy Room's **code and
documentation** (this README + scripts/copy_room.py) ship with the repo.

## Retrieval convention

When answering sub-mod development questions: query mod-specific signatures
in `copy_room/<mod-id>/script_docs/` first, and locate entries via
`copy_room/<mod-id>/structure/entry_map.tsv`; on name clashes with vanilla
the mod layer wins (a sub-mod runs inside the parent mod's environment);
for vanilla behaviour fall back to `game_docs/`.
