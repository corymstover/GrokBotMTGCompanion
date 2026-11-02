# v3.07 — First-party set-context navigation, bounded K055 acceptance

This batch independently replays **K055 only**. The task says to connect sets
to **supported** planes, story arcs, factions, characters, mechanics and
Commander-relevant releases **without inventing lore connections**. It does
not authorize pretending to have a canon record for all 1,062 Scryfall codes.

## Evidence and exact limits

`scripts/audit_set_multiverse_context.py --check` joins four frozen inputs:

1. `data/set_atlas/product_catalog_2026-10-29.json`: **1,062** set codes,
   typed Scryfall product metadata, and exact `parent_set_code`. These are
   third-party catalog fields, *not* stand-alone first-party canon claims.
2. `data/set_atlas/phase1b_release_scope_story_bridge_2026-10-29.json`:
   **12** named Wizards story-publication series and **35** official story
   page URLs, each already registered in the frozen Multiverse graph.
3. `data/multiverse_graph/multiverse_graph.json`: source→claim citations
   and claim→typed entity assertions. **117** Character, **11** Faction,
   and **8** Plane *source/claim/entity rows* retain exact source URLs,
   claim IDs, canon grades and subject/object roles. These are not 136
   independent people and planes, nor evidence that every card in the
   associated set depicts any of them.
4. `data/set_atlas/set_context_primary_sources_2026-11-01.json`: manually
   verified first-party pages explicitly discussing named set mechanics or
   related Commander deck products, with strict pinned source URLs and labels.

The four independently checked Wizards pages are:

- [The Brothers' War Mechanics](https://magic.wizards.com/en/news/feature/the-brothers-war-mechanics): Prototype and Powerstones in `bro`.
- [Bloomburrow Mechanics](https://magic.wizards.com/en/news/feature/bloomburrow-mechanics): Offspring, Forage, Valiant in `blb`.
- [Tarkir: Dragonstorm Mechanics](https://magic.wizards.com/en/news/feature/tarkir-dragonstorm-mechanics): Endure, Behold, Mobilize, Harmonize, Omens in `tdm`.
- [Tarkir: Dragonstorm Commander Decklists](https://magic.wizards.com/en/news/announcements/tarkir-dragonstorm-commander-decklists): five preconstructed Commander lists, joined only to Scryfall's separately verified `tdc`→`tdm` parent relation. This is **not** approval of this project's pilot decks.

Run `python3 scripts/audit_set_multiverse_context.py --code tdm` for the
explicitly limited results; `--code tdc` or `--code lea` shows the independent
product type and an `NO_VERIFIED_STORY_CONTEXT_IN_THIS_SNAPSHOT` status.
There is **no guess** based on similar set names, parent products, card art,
dates or fictional setting. A cited graph entity is a source/claim association,
not proof that the entity occurs on a given printing or that all its story
events occurred at the set's release time.

## Failure-closed acceptance

`tests/test_set_multiverse_context.py` (9 tests) rejects a substituted or
inflated mechanics source, broken Commander parentage, unregistered story
page, non-Wizards graph source status, stale output and nonexistent set code.
The frozen report is 100% byte-rebuilt from input hashes. The original
v3.00 foundation acceptance and certificate are unchanged.

**Disposition:** This is a bounded PASS for K055's *supported connection
capability*. It is **not** an exhaustive first-party set roster (K050),
complete lore for any plane (K074/K079/etc.), global story chronology
(K088/K103), or all-time source complete card depiction inventory.

## Repository scope

- Historical checklist: **116/137 checked**, **21** unchecked.
- Active repository-build tasks: **15**, after excluding only K105,
  K112–K114, K125 and K126; the three pilot reviews occur after development.
- Protected Grixis lists: unchanged; all three pilot decks: **UNAPPROVED**.
- Foundation: independently **7/7** certified, not upgraded by this batch.
