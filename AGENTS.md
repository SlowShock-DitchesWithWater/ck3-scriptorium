# AGENTS.md — CK3 Modding Knowledge Base · AI Retrieval Rules

> This file is for any AI agent answering CK3 modding questions from this repository.
> Your job: obtain **source-cited, hallucination-free** knowledge with minimal context.
> Every command and path in these rules has been tested against this repo.
> (中文版：[AGENTS.zh-CN.md](AGENTS.zh-CN.md))

## 0. What this repo is (30-second version)

A three-layer knowledge base plus one summary catalog. Current snapshot page count and
game version live in the snapshot block at the top of `catalog.md` (do not record those
numbers anywhere else — they rot).

| Layer | Location | Contents | Authority |
|---|---|---|---|
| Wiki explainer layer | `pages/` | Cleaned text from ck3.paradoxwikis.com Modding section | Low |
| Game authority layer | `game_docs/script_docs/` | Debug dump from the game itself: effects / triggers / modifiers / on_actions / event_targets / event_scopes / custom_localization lists + 5 data_types files | **High** |
| Vanilla structure index | `game_docs/vanilla_structure/` | entry-name → defining-file map + summaries of all 128 `common` subdirectories | Navigation |

**Authority order: game_docs (dump) > pages (wiki).** When the two layers conflict,
the dump wins — and say so in your answer, pointing at the conflict.

**`game_docs/` ships with the repository** (built from the game's own debug
dump; see the snapshot block for the current game version). It is game-derived
data — this repo claims no rights over it (`LICENSES.md`). After a CK3 version
update the layer can be refreshed locally via the game-layer steps in
`README.md` (Manual A).

`catalog.md` is the two-level summary catalog of every entry — **the single retrieval
entry point, but never read it whole: grep it first, then follow the hit** (see below).

## 1. Standard retrieval flow (four steps)

1. **Classify the question**, then pick a recipe from section 2 (A signatures / B explainers / C entry location / D version-sensitive).
2. **Query the catalog**: grep `catalog.md` for a keyword; when an entry hits, read only
   the file named in its `文件位置` (file-location) field — not the whole catalog, and
   not the whole target page either.
3. **No catalog hit → pages fallback**: grep the whole `pages/` tree for the keyword
   (commands in recipe B), still reading only the matching file. The catalog cannot
   index every fact; the fallback is a normal path, not a detour.
4. **Every answer must cite its source**: a concrete file (`pages/<name>.md` or
   `game_docs/<layer>/<product>.md`) plus the section/entry name. If you did not read
   it, do not answer: writing effect/trigger/modifier/field names from model memory is
   forbidden.

### How to grep (`catalog.md` and `pages/*.md` are UTF-8)

```bash
# ASCII keywords (effect/trigger names, page names — the vast majority of queries):
grep -n -i "trait" catalog.md
# Windows cmd equivalent (GBK codepage — only reliable for ASCII keywords):
findstr /n /i /c:"trait" catalog.md

# Non-ASCII keywords (catalog summaries are written in Chinese):
python -X utf8 -c "import sys;sys.stdout.reconfigure(encoding='utf-8');[print(f'{i}: {l.rstrip()}') for i,l in enumerate(open('catalog.md',encoding='utf-8'),1) if 'trait' in l]"
```

Catalog entry fields at a glance (entry counts are in the snapshot block):
`文件位置` file location (go read it) · `来源` source (URL + oldid + fetch date + page-stated game version) · `何时查` when-to-consult and `中文摘要` Chinese summary (use these to judge relevance) · `英文关键词` English keywords · `章节` section list (H2; read only what you need).

## 2. Query recipes (all commands tested)

### Recipe A: effect / trigger / modifier / on_action / custom_localization / data-type signatures

**Go straight to the authority layer — do not start at the wiki.** Each list file has
one section per entry with a `### Name` heading, containing the description and
`Supported Scopes:`. Files (all under `game_docs/script_docs/`):

`effects.md` · `triggers.md` · `modifiers.md` · `on_actions.md` ·
`event_targets.md` · `event_scopes.md` · `custom_localization.md` ·
`data_types_common.md` · `data_types_gui.md` ·
`data_types_internalclausewitzgui.md` · `data_types_script.md` ·
`data_types_uncategorized.md` (if a type is missing from the first four data_types
files, fall back to this one).

```bash
# Known name — hit the heading line exactly (prints line numbers; then read only that ### section):
grep -n "### add_gold" game_docs/script_docs/effects.md

# Only semantics known (e.g. "give a character gold") — search by meaning first, then filter to headings:
grep -n -i "gold" game_docs/script_docs/effects.md | grep "### "
```

**Dump entries usually carry only the description + Supported Scopes, no usage
examples.** When you need an example, search the wiki layer full-text for the
effect/trigger name (cold-start acceptance testing proved this the fastest path):

```bash
grep -rn "add_gold" pages/
```

The wiki mega-list pages (`pages/Effects list.md`, `pages/Triggers list.md`,
`pages/Commands.md`) are explainer references only; entry-level answers defer to the
dump layer.

### Recipe B: mechanics / how-to / explainers (wiki layer)

```bash
# 1) Catalog first (prefer English keywords: page names, script terms):
grep -n -i "achievement" catalog.md
grep -n -i "on_action" catalog.md

# 2) Non-ASCII keywords or no catalog hit — pages-wide fallback (python one-liner):
python -X utf8 -c "import sys,pathlib;sys.stdout.reconfigure(encoding='utf-8');[print(f'{p}: {i}: {l.rstrip()}') for p in pathlib.Path('pages').rglob('*.md') for i,l in enumerate(p.read_text(encoding='utf-8').splitlines(),1) if 'achievement' in l.lower()]"
```

After a hit, read the file named in the entry. **Split pages**: the page-name file of
the pages below is only a chapter index; the body lives in same-named subdirectories
(each index lists its chapter files):

- `pages/Effects.md` (index) → `pages/Effects/01-Effect-blocks.md` and siblings
- `pages/Event modding.md` → `pages/Event modding/` (13 chapter files)
- `pages/Interface.md` → `pages/Interface/` (9 chapter files)
- `pages/Data types.md` → `pages/Data types/` (4 chapter files)
- more split pages exist; every index file carries its chapter list (also in the
  manifest's `organize` field per page)

### Recipe C: which vanilla file defines an entry (trait / decision / opinion / …)

```bash
grep -P "^education_intrigue_1\t" game_docs/vanilla_structure/entry_map.tsv
```

Outputs three tab-separated columns: entry name, defining file (relative to the game
install's `game/` directory), line number — e.g. `common/traits/00_traits.txt  11`.
The map holds structure only, zero vanilla content; after getting the path, read the
original file in **the user's local game installation** (this repo does not ship
vanilla files).

- To browse all files and entries of one content type: read
  `game_docs/vanilla_structure/INDEX.md` first, then the per-subdirectory summaries
  under `game_docs/vanilla_structure/common/` (all 128 covered).
- Non-`common` directories (events / history / gui / gfx / …):
  `game_docs/vanilla_structure/other_dirs.md`.

### Recipe D: version-sensitive facts ("since which version…" questions)

1. Find the wiki body first via recipe B — version numbers usually sit in prose
   sentences (e.g. "since 1.9 patch").
2. Cross-check both layers' version annotations and cite them in the answer:
   - wiki: the entry's `来源` (source) line (oldid / fetch date / page-stated version);
   - dump: the game-version source line in each `game_docs/script_docs/` file header.
3. A page stating `timeless` means the wiki claims version-independence; if it still
   conflicts with prose, the dump layer wins.

## 3. Context discipline (hard rules)

- **Never read whole** these large files (always grep-locate, then read the needed
  fragment): `catalog.md`, `pages/Effects list.md`, `pages/Triggers list.md`,
  everything under `game_docs/script_docs/`, and
  `game_docs/vanilla_structure/entry_map.tsv`.
- **Quote code blocks and signatures verbatim** — no rewriting, no "helpful
  normalization" of field names.
- Any effect / trigger / modifier / field name: either it comes from a file you just
  read (cite the path), or you explicitly state "not verified against the knowledge
  base". There is no third option.
- wiki vs dump conflict → dump wins, and name the conflict in your answer.
- Version-sensitive conclusions must carry version annotations (recipe D).

## 4. Paths that are NOT knowledge entries (do not read them for answers)

| Path | What it is |
|---|---|
| `raw/` | Raw api.php JSON archive (for cleaning replay, not knowledge; not shipped to clones) |
| `game logs/` | Original script_docs dump logs (already converted into `game_docs/script_docs/` — read that instead; not shipped) |
| `scripts/state/` | Pipeline runtime state and one-off probe scripts |
| `scripts/`, `tests/` | Pipeline code and tests (maintainer-facing; see `README.md`) |
| `manifest.json` | Pipeline registry (advanced version tracing; everyday version info is in catalog `来源` lines) |
| `_reference/`, `.scratch/` | Internal workspaces (not shipped) |
| `docs/pipeline.md`, `docs/spec.md` | Pipeline contract and project spec (maintainer-facing) |
| `skills/` | The bundled `ck3-mod-standards` scripting-standards skill (install into an agent when writing mod code; not knowledge) |

## 5. Timeliness self-check

Before answering, if the conclusion could drift with game versions (new effects,
numbers, achievement rules…), judge snapshot freshness with recipe D's two-layer
annotations (snapshot dates are in the `catalog.md` snapshot block). For anything
newer than the snapshot, say **"this knowledge base's snapshot does not cover it"** —
never patch the gap with model memory.

## 6. User override

The user's explicit instruction in the current conversation overrides this file.
If something here conflicts with it, state the conflict and get confirmation before
proceeding.

## 7. Stop and ask the user first

- Before **re-crawling the wiki or re-running the dump** (any network or pipeline
  run): explain what will run and how long it takes (a full re-crawl is ~30–40
  rate-limited minutes); proceed only after consent.
- If a wiki/dump conflict changes the answer: report the conflict instead of
  silently picking a side.
- If the user asks about knowledge newer than the snapshot: say so and ask whether
  to refresh the snapshot — do not improvise.
