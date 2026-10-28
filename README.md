English | [简体中文](README.zh-CN.md)

[![ci](https://github.com/SlowShock-DitchesWithWater/ck3-scriptorium/actions/workflows/ci.yml/badge.svg)](https://github.com/SlowShock-DitchesWithWater/ck3-scriptorium/actions/workflows/ci.yml)

# CK3 Scriptorium — CK3 Modding Knowledge Base

A local, layered, source-cited knowledge base about **Crusader Kings III (CK3)
modding**, built for two audiences: **AI agents that write mods** — they look
things up here instead of trusting their own memory — and **human modders and
maintainers**. It combines three layers (wiki explainers, signatures exported
by the game itself, and a vanilla-file index) so that every answer can carry a
real file path and a version note instead of hallucinated script syntax.

Why this exists: large language models are unreliable about CK3's script
language (Jomini). Effect, trigger, modifier and field names get freely
invented, producing code that merely *looks* like CK3 script. This repo's
approach: check the summary catalog (`catalog.md`) first, read **only the
specific file sections needed**, and require every fact to carry a source path
and version annotation — no RAG, no stuffing the whole library into context.

## Quick Start

### Path 1 — just use the knowledge base (no install, no commands)

Get the files: on GitHub click the green **Code** button → **Download ZIP**,
then unzip anywhere you like. (If you know git, `git clone` works too.)

**Human readers:** open `catalog.md` in any text editor. It is the table of
contents of the whole knowledge base ("catalog" = a directory you follow to
the right file): one entry per topic, each telling you which file to open
(the `文件位置` / file-location field) and which sections it contains. The
entries' summaries are written in Chinese, but every entry also lists English
keywords and English section names, so searching with Ctrl+F for an English
term works fine. Then open the file the entry points to — wiki explainers live
under `pages\`, game signatures under `game_docs\script_docs\`.

**AI-agent users:** put this repository somewhere the agent can read it and
tell it, for example: *"Read AGENTS.md at the repo root first, then answer my
questions from this repo, citing source file paths."* `AGENTS.md` is the
retrieval protocol written for agents — a four-step lookup flow plus
ready-made query recipes.

Three typical lookups this setup handles:

1. *"What is the exact signature of the effect `add_gold`?"* — search
   `game_docs\script_docs\effects.md` for the heading `### add_gold`; dump
   entries list the description and supported scopes.
2. *"Which vanilla file defines the trait `education_intrigue_1`?"* — look the
   name up in `game_docs\vanilla_structure\entry_map.tsv`, which maps entry
   name → defining file → line number (e.g. `common/traits/00_traits.txt`);
   then read that file inside your own CK3 installation.
3. *"How do achievements / on_actions / mod-folder rules work?"* — search
   `catalog.md` for the keyword, then read the wiki page it lists under
   `pages\`.

> **The game layer is not in the published repository.** `game_docs\` is
> derived from the game's own debug dump, so distributing it would mean
> redistributing game-derived data — a real takedown (DMCA) risk. This is a
> deliberate compliance decision. If you have CK3 installed, follow the
> game-layer steps in **Manual A** below to generate an equivalent locally.

### Path 2 — rebuild or refresh the knowledge base (needs Python)

"Crawling" simply means downloading wiki pages into a local archive; the
pipeline then cleans and indexes them. Minimal version — full detail in
**Manual A**:

```bat
:: 1) Install Python 3.10+ from https://www.python.org/downloads/ (this project
::    was developed and tested on 3.13), then check it:
python --version

:: 2) Install the three libraries (pip is Python's package installer):
pip install selenium requests beautifulsoup4

:: 3) Crawl the wiki (needs internet + the Chrome browser; resumable —
::    already-fetched pages are skipped automatically):
<python> scripts\crawl.py --nav
<python> scripts\onehop.py --list
<python> scripts\onehop.py --crawl

:: 4) Build all offline products from the crawl archive (no network needed):
<python> scripts\clean.py --all
<python> scripts\organize.py
<python> scripts\catalog.py
<python> scripts\quality_gate.py
```

`<python>` stands for the Python executable of your environment — plain
`python` if it is on your PATH (on Windows, if console output turns into
mojibake, run it as `python -X utf8 ...`).

Steps 1–4 give you the wiki layer and its catalog. The game authority layer
and the vanilla structure index additionally require a local CK3
installation — that is the full rebuild described in **Manual A**.

## What's Inside

`catalog.md` is the single lookup entry point: a two-level summary directory
(topic → sections, with "when to look here" hints, keywords, and source and
version notes). Don't read it end to end — search a keyword, then read only
the entries and files it points to. (For agents this rule is formalized in
`AGENTS.md`.)

| Layer | Location | What it is | Authority |
|---|---|---|---|
| Wiki explainer layer | `pages\` | Cleaned text of the ck3.paradoxwikis.com Modding pages (CC BY-SA 3.0). Mechanic explainers, tutorials, usage examples. | Lower |
| Game authority layer | `game_docs\script_docs\` | The game's own debug dump (the `script_docs` console command): one exhaustive, machine-generated list each for effects, triggers, modifiers, on_actions, event_targets, event_scopes, custom_localization, plus the data-type lists. Every entry's real signature. Not in the published repo — generated locally (see Manual A). | **High** |
| Vanilla structure index | `game_docs\vanilla_structure\` | `entry_map.tsv` maps entry name → defining vanilla file → line number, plus a summary for every `common` subdirectory. Pure navigation, zero game content. | Navigation |

**Authority order: game dump (`game_docs`) over wiki (`pages`).** When the two
layers disagree, the dump wins and the answer should point out the conflict.
Layer sizes, sources and version annotations live in the snapshot block at the
top of `catalog.md` and in each entry's source line.

## Repository Layout

| Path | What it is | Published? |
|---|---|---|
| `catalog.md` | The single lookup entry point (original work) | Yes |
| `pages\` | Cleaned wiki text (derived from CK3 Wiki, CC BY-SA 3.0; see `pages\CONTENT-LICENSE.md`) | Yes |
| `scripts\` | Pipeline: crawl / clean / organize / catalog / quality_gate / game_layer / vanilla_index | Yes |
| `tests\` | Cleaning-rule assertions, catalog-protection tests, golden fixtures | Yes |
| `skills\` | Original procedural skill for AI agents: `ck3-mod-standards` — CK3 mod scripting standards (scope discipline, on_action bridging, load-order compatibility, localization rules; anti-hallucination via this knowledge base). Install: copy to your agent's skills dir, e.g. `~/.agents/skills/` | Yes |
| `docs\` | `docs\pipeline.md` (pipeline contract), `docs\reports\` (cleaning statistics); `docs\spec.md` is internal planning and stays local | Partially |
| `AGENTS.md`, `AGENTS.zh-CN.md`, `README.md`, `README.zh-CN.md`, `LICENSES.md`, `LICENSE` | Agent retrieval protocol (EN/CN); this manual in two languages; licensing | Yes |
| `manifest.json` | Per-page oldid / timestamp / version registry (the version anchors) | Yes |
| `raw\` | Raw JSON archives of the wiki API (for offline replay when cleaning rules improve) | No (local) |
| `game_docs\` | Game-derived content: dump conversion products + vanilla structure index | No (local, generated) |
| `game logs\` | Raw logs produced by the game's script_docs dump (input of game_layer) | No (local) |
| `scripts\state\` | Runtime state (navigation lists, cookies, run logs, self-check scripts) | No |
| `_reference\`, `.scratch\` | Internal workspaces | No |

## Manuals

### Requirements (common to all three manuals)

- Python 3.10 or newer (this project was developed and tested on 3.13).
  Exactly three third-party libraries are needed — `selenium`, `requests`,
  `beautifulsoup4` — and one pip command installs all three. Any virtual
  environment or install method works; `<python>` below means "the Python
  executable of that environment".
- The Chrome browser: the target wiki sits behind an anti-bot shield. The
  pipeline passes the shield with a real browser session and then accesses the
  API (dual-channel logic in `scripts\lib\session.py`).
- Rebuilding the game authority layer requires CK3 installed locally (its
  debug mode can run the `script_docs` console command).
- The pipeline rate-limits itself: at least 15 seconds between requests to the
  wiki (the site's robots.txt Crawl-delay — a hard floor, not configurable);
  a full crawl takes longer as the page count grows.
- All commands were tested in Windows cmd; for other shells, substitute
  equivalents.

### Manual A: full rebuild from scratch

```bat
:: —— 1. Wiki layer (needs internet + Chrome; already-fetched pages are skipped, so the run is resumable) ——
<python> scripts\crawl.py --nav
::    This fetches every page of the Modding navigation template. Then add the one-hop
::    seed pages (Effects list / Triggers list etc.; the selection is written on first run):
<python> scripts\onehop.py --list
<python> scripts\onehop.py --crawl

:: —— 2. Wiki-side products (offline; replayed from raw\) ——
<python> scripts\clean.py --all
<python> scripts\organize.py
<python> scripts\catalog.py
<python> scripts\quality_gate.py

:: —— 3. Game authority layer (offline; needs the game installed locally) ——
::    A fresh clone contains only the wiki layer; the game authority layer
::    (dump signatures) is built on your machine in three steps:
::    a) Launch CK3 with -debug_mode (add it to Steam launch options).
::    b) Open the console (` key) and run BOTH commands — each writes a
::       different part, both are required:
::         script_docs      -> the 7 list .log files
::         dump_data_types  -> the 5 .txt files under data_types\
::       The export lands in %USERPROFILE%\Documents\Paradox Interactive\
::       Crusader Kings III\logs\   (verified against CK3 1.20)
::    c) Point --source straight at that folder — no copying needed (the
::       other files there are runtime logs, ignored automatically):
<python> scripts\game_layer.py --source "%USERPROFILE%\Documents\Paradox Interactive\Crusader Kings III\logs"
::    Success looks like: 12 .md files under game_docs\script_docs\ and a new
::    game_docs.script_docs section in manifest.json.
::    Alternative: create the repo's `game logs\` directory (gitignored,
::    absent in clones), copy the export there, then run without arguments.

:: —— 4. Vanilla structure index (offline; needs the game installation directory) ——
<python> scripts\vanilla_index.py --game-dir "<your CK3 install directory>\game"
::    game-dir configuration (pick one; option 3 is recommended for long-term local use):
::    1) pass --game-dir every time; 2) the CK3_GAME_DIR environment variable;
::    3) scripts\state\local_paths.json containing {"game_dir": "<path>"} (that directory is gitignored)

:: —— 5. Merge the game layer into the catalog + final gate ——
<python> scripts\catalog.py
<python> scripts\quality_gate.py
```

Single-page full run (debugging): `<python> scripts\run.py --page Scripting`.

### Manual B: refresh after a game update

```bat
:: 1. Re-run script_docs on the new game version and replace the dump files under game logs\
:: 2. Rebuild the game layer (products are fully regenerated from the new dump; version
::    annotations update automatically; offline)
<python> scripts\game_layer.py
<python> scripts\vanilla_index.py --game-dir "<your CK3 install directory>\game"
:: 3. Incremental wiki refresh (needs internet: batch-checks each page's revid; unchanged pages cost zero requests)
<python> scripts\crawl.py --nav --refresh
::    To also re-check the one-hop extra pages: re-run <python> scripts\onehop.py --crawl
:: 4. Replay the full pipeline (offline)
<python> scripts\clean.py --all
<python> scripts\organize.py
<python> scripts\catalog.py
<python> scripts\quality_gate.py
```

### Manual C: using the knowledge base from a new AI-agent session

1. Have the agent read `AGENTS.md` at the repo root first (the retrieval
   protocol: four-step flow + query recipes per question type).
2. Core loop: search `catalog.md` for keywords → follow each hit's
   file-location / sections fields and read only those files.
3. Every answer must cite source paths (`pages\...` or `game_docs\...`);
   effect / trigger / modifier signatures always come from the authority
   layer, never from model memory.
4. Optional self-check of the protocol itself:
   `<python> scripts\check_doc_paths.py` (verifies that path references
   in AGENTS and the READMEs are not dangling).

## Testing (all offline)

```bat
<python> scripts\quality_gate.py          :: product assertions for every page
<python> tests\test_cleaner_rules.py      :: cleaning rules → assertion mapping (real fixtures)
<python> tests\test_catalog_protection.py :: catalog human-field protection / idempotency
<python> tests\spotcheck_tables.py        :: table zero-loss spot check (raw-needle based)
<python> scripts\clean.py --replay-golden :: golden replay (Scripting + Effects fixed fixtures)
<python> scripts\check_doc_paths.py       :: AGENTS / README path-reference self-check
:: maintainer-only (need unpublished local data):
<python> scripts\game_layer.py --check    :: game-layer products match their sources (needs game logs/)
<python> scripts\vanilla_index.py --check :: structure index matches the game directory (needs the game dir)
```

The first six run anywhere, including a fresh clone: checks that need the
unpublished `raw/` archive (or game directories) detect its absence and
**skip with a clear notice instead of failing** — CI runs exactly this
clone-mode set (`.github/workflows/ci.yml`).

## Snapshot

Every number in this README that changes with the snapshot is concentrated in
the table below (nowhere else in the text); after a refresh, only this table
needs editing. The same information is regenerated automatically in the
snapshot block at the top of `catalog.md`.

| Item | Value |
|---|---|
| Wiki layer — crawl date | 2026-10-22 (nav/seed batches) + 2026-10-23 (one-hop backfill; old Patch changelog pages excluded by design) |
| Wiki layer — pages in this snapshot | 141 (live count in the snapshot block atop `catalog.md`) |
| Game layer — CK3 version of the dump | 1.20.0 |
| Game layer — merged on | 2026-10-22 |
| Game layer — entry counts | effects 2128 · triggers 1937 · modifiers 761 · on_actions 932 · event_targets 328 · event_scopes 74 · custom_localization 2782 |
| Vanilla structure index | `entry_map.tsv` with 78167 lines; summaries for 128 `common` subdirectories; scanned 2026-10-22 against CK3 1.20.0 |
| `catalog.md` size | about 131 KB |

Timeliness: anything newer than the dates above — a new game patch, wiki edits
after the crawl date — is not in this knowledge base yet. For version-sensitive
facts, check the entry's source line (oldid / fetch date / page-stated game
version) before trusting it; agents follow recipe D in `AGENTS.md`. To catch
up, use **Manual B** (game update) and the crawl steps of **Manual A**
(wiki update).

## License

Two layers, split by directory — the full statement lives in `LICENSES.md`:

- **Code and original documentation** — `scripts\`, `tests\`, `catalog.md`,
  `manifest.json`, `docs\` (pipeline.md, reports) and the root documents
  (`README.md`, `README.zh-CN.md`, `AGENTS.md`, `LICENSES.md`): **MIT
  License**, see `LICENSE`.
- **Wiki-derived content** — `pages\` (including its chapter subdirectories)
  and the golden fixtures under `tests\fixtures\`: **CC BY-SA 3.0**,
  attribution: CK3 Wiki (<https://ck3.paradoxwikis.com>). Redistribution must
  share alike under the same license; details in `pages\CONTENT-LICENSE.md`.
- **Not distributed** — `game_docs\`, `raw\`, `game logs\`, `scripts\state\`,
  `_reference\`: game-derived data, raw crawl archives, session state and
  third-party reference material never leave the local machine.
