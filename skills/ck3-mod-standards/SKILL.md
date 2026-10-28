---
name: ck3-mod-standards
description: CK3 (Crusader Kings III) mod scripting standards: constrains scope discipline, on_action bridging, load-order compatibility, naming & localization rules, and performance habits whenever writing, editing, reviewing, or generating CK3 mod script — and forces signature checks against the local knowledge base to prevent hallucination. Use when the user mentions CK3 mod, CK3 模组, crusader kings mod, Jomini script, writing/editing events, decisions, traits, mechanics, on_action, effect/trigger, localization, mod file layout, or asks to review/fix/debug mod code — even for a single small effect block or one localization line. 中文版规约见同目录 SKILL.zh-CN.md。
metadata:
  version: "1.3"
---

# CK3 Mod Scripting Standards (ck3-mod-standards)

For AI agents: follow these standards whenever you produce CK3 (Jomini) mod code.
Rules come in two layers — **procedural discipline** (stable over time; the body of
this file) and **signature facts** (drift with game versions; always looked up in
the knowledge base, never written from memory).

(中文版：[SKILL.zh-CN.md](SKILL.zh-CN.md))

This skill only covers *how to write the code*. The retrieval protocol for the
knowledge base itself (how to look things up) is the `AGENTS.md` at the knowledge
base root; runtime error diagnosis (Tiger, the game's error log) is out of scope.

## 0. Signature anti-hallucination (top priority)

Any effect / trigger / modifier / on_action / field name: **either it comes from
the knowledge base, or you explicitly say "not verified"**. There is no third option.

Knowledge base location — resolve in this order, first hit wins:

1. **Co-location:** if `../../catalog.md` and `../../AGENTS.md` exist relative to
   this SKILL.md (the skill sits inside a cloned ck3-scriptorium repo under
   `skills/`), that repo root **is** the knowledge base — no config needed.
2. **`kb_location.txt`** in this skill's directory: a one-line absolute path to
   the knowledge base root (per-machine config, gitignored — create it to pin a
   separately-cloned or non-co-located copy).
3. **Environment variable** `CK3_KB_PATH`, holding the knowledge base root path.
4. **Ask the user** for the path (typically their ck3-scriptorium clone), then
   offer to save it into `kb_location.txt` so future sessions skip this step.

Retrieval rules are in the knowledge base's root `AGENTS.md`
(grep `catalog.md` first → read the hit's `pages/` or `game_docs/` file). Fast paths:

- Effect/trigger signatures and Supported Scopes → `game_docs/script_docs/effects.md` / `triggers.md` (`### name` sections, authority layer)
- Which vanilla file defines an entry (trait/title/culture/…) → `game_docs/vanilla_structure/entry_map.tsv`
- Mechanics explainers → grep `catalog.md` for the keyword → read the hit page

After generating code, verify every script word you used actually exists; look up
any word you are not sure about before using it.

## 1. Scope discipline

Every piece of CK3 script is interpreted inside a scope (character / title /
province / faith / none…). Wrong scope produces code that *looks* right but
behaves wrong.

- **Confirm the current scope before writing any effect/trigger.** In events the
  default `root` is the trigger's chain; on_actions each have their own expected
  scope (e.g. `on_game_start` has no root — it fires once, globally, so only
  global effects like `every_ruler` work; `yearly_playable_pulse` has the
  character as root) — per `pages/Event modding/12-On-Actions-on_action.md`
  (on_action tables and Scopes section) and `game_docs/script_docs/event_scopes.md`.
- **Self-verify after every scope switch:** chained switches (e.g. `father = { … }`)
  can land on an empty scope; when the target may not exist, guard with an
  existence check (trigger side) or use `limit`.
- `root` / `this` / `prev` only work in blocks that **have a default context** —
  some blocks (e.g. character interactions) have no `root` (per `pages/Scopes.md`).
  When unsure, look it up; don't assume.
- Wide iterations (`every_*`) must narrow with `limit` or weights — see §5.

## 2. on_action bridging (never overwrite vanilla)

When hooking into an existing on_action (e.g. `on_birth_child`), **never write its
`trigger`/`effect` directly — that is an override and eats the logic of vanilla and
every other mod.** The correct pattern (per `pages/Event modding/12-On-Actions-on_action.md` §Appending):

```
# New txt file of your own (common/on_action/ — note the directory name is
# singular on_action, NOT on_actions)
on_birth_child = {
  on_actions = { my_mod_my_on_action }   # append your custom on_action
}
my_mod_my_on_action = {
  trigger = { ... }    # belongs to this block only
  effect = { ... }     # effects appended safely, overriding no one
}
```

Key points:

- `events` and `on_actions` lists are **append** semantics; `trigger`/`effect` are
  **override** semantics — only the former two may be added directly.
- Custom on_actions exist to group and reuse (events/effects); you may create new
  custom on_actions but **cannot create new code-side on_actions**.
- Every on_action has its own expected scope — check the table first (the
  "On_actions from code" table in the same chapter).
- There is no monthly pulse (for performance); approximate monthly with
  `quarterly_playable_pulse` + `delay = { months = … }` staged firing.

## 3. Load-order compatibility (minimal footprint)

Same-path files are **replaced whole**; same-entity names resolve by **alphabetical
filename order, last one wins** (entity-level override; events are not
overridable entities — route through a scripted effect) — per
`pages/Mod compatibility.md`:

- **Minimize your footprint:** only override vanilla files/entities you truly
  change; prefer "appending" (on_action lists, new files with new entities) over
  overriding. The smaller the footprint, the better other mods coexist.
- **Prefix everything with your mod prefix:** scripted_effects/triggers,
  on_actions, event IDs, variable names (e.g. a `mymod_` prefix). Bare names
  (`my_effect`) collide easily.
- **Cross-mod cooperation points use agreed entities:**
  - Shared variable: mod A sets `set_variable = { name = amod_did_x … }`, mod B
    probes with `has_variable = amod_did_x` — no dependency on the other being loaded.
  - Shared scripted effect: A ships the default implementation in an early-alphabet
    file (`aaa_…`); B wanting to replace it defines the same entity in a
    late-alphabet file (`zzz_…`) which overrides.
  - Detecting another mod: the detectee defines `xxx_is_loaded = { always = yes }`
    (scripted trigger, late-alphabet file); the detector defines the same name as
    `always = no` (early-alphabet file) and checks `xxx_is_loaded = yes`.
- Total-conversion (TC) compatibility — removing vanilla content — is a much
  higher bar (no references to specific faiths/cultures or other database
  entities); don't aim for it unless the user explicitly asks.

## 4. File layout & localization

- Mod structure: a mod folder plus a same-named `.mod` descriptor under
  `~\Paradox Interactive\Crusader Kings III\mod`; the folder path must not contain
  non-English characters (per `pages/Mod structure.md`).
- Script files go into the matching `common\*` subdirectory (decisions →
  `common/decisions`, on_action → `common/on_action`, …); file names carry the
  mod prefix.
- **All player-visible text goes through localization keys** — never hardcoded
  into event bodies:
  - Under `localization\<language>\` create files like `xxx_l_english.yml`:
    the file name contains `l_<language>`, the first line is `l_english:`, and the
    encoding is **UTF-8 with BOM** (per `pages/Localization.md`).
  - Event/decision titles, descriptions and options all use keys; produce the loc
    file together with the script — leave no `TITLE_MISSING` behind.

## 5. Performance habits

- **Never nest a full character iteration inside a per-character pulse:** e.g.
  `yearly_playable_pulse` already fires for every playable character; adding
  `every_living_character` inside creates roughly 200002 operations of disaster
  (per the §Scopes warning in `pages/Event modding/12-On-Actions-on_action.md`).
- Wide iterations always carry a `limit`; use `random_*` with weights instead of
  `every_*` plus home-made randomness.
- Control event frequency with `mean_time_to_happen` / weights — prefer low
  frequency; heavy logic goes into low-frequency pulses.

## 6. Pre-delivery checklist

Go through every item after producing code:

1. Every script word (effect/trigger/field) checked against the knowledge base?
   Source paths traceable?
2. Scope explicit for every block? Every `root` usage confirmed to have a root?
3. on_action only appended (`on_actions = { … }` / `events = { … }`), no vanilla
   `trigger`/`effect` overridden?
4. Entities/files/variables/event IDs all carry the mod prefix? No unnecessary
   vanilla file overridden?
5. All player-visible text has localization keys? Loc file format correct (BOM /
   `l_english:` / file name)?
6. All loops have limits? No full-scope iteration nested in per-character pulses?

## Sources & timeliness

The procedural discipline in this file is distilled from the local knowledge base:
`pages/Mod compatibility.md`, `pages/Event modding/12-On-Actions-on_action.md`,
`pages/Localization.md`, `pages/Scopes.md`, `pages/Mod structure.md`, and
`game_docs/script_docs/` (the signature authority layer). The knowledge base's
snapshot date and game version live in the snapshot block atop its `catalog.md`
(this file deliberately records no such numbers — they rot as the base refreshes).
Signature and numeric facts drift with game versions: always check the base, and
never treat this file's example code as signature facts (examples demonstrate
structure and discipline only).
