# Foundation batch: Gatewatch origin chronology and graph identity integrity (2026-10-31)

**Status:** independently source-checked engineering and bounded history research; **NOT foundation-certified, NOT owner-approved**. Phase 6 stays parked. No approved deck, hash, owner decision or Scryfall snapshot was edited.

## Gatewatch / Battle for Zendikar history

The new `Z` chronology strand supplies **13 events and 12 quoted strict BEFORE edges**, from the ancient Eldrazi imprisonment through the founding four's oaths and the aftermath of Ulamog and Kozilek's destruction. The evidence comes from four already-registered primary sources:

- [Wizards, *Battle for Zendikar Story Summary*](https://magic.wizards.com/en/news/magic-story/battle-zendikar-story-summary-2015-12-23): ancient prison, Nahiri's later repair, Bolas's Eye arrangement, Nissa actually releasing the titans, Gideon recruiting Jace, Sea Gate, Ob Nixilis and Kozilek.
- [Wizards, *Oath of the Gatewatch*](https://magic.wizards.com/en/news/magic-story/oath-gatewatch-2016-02-03): the original four swear the oath during the two-titan crisis.
- [Wizards, *Zendikar's Last Stand*](https://magic.wizards.com/en/news/magic-story/zendikars-last-stand-2016-02-17): the oath already exists when Chandra fights the climactic battle.
- [Wizards, *Zendikar Resurgent*](https://magic.wizards.com/en/news/magic-story/zendikar-resurgent-2016-02-24): explicit confirmation that both titans were destroyed, followed by recovery and the four Planeswalkers' next choices.

The difference between the **Eye's brood release** and **Nissa's later release of the titans** is material. So is the distinction between the ancient three-titan prison and **Ulamog's temporary Battle for Zendikar hedron trap**, later sabotaged by Ob Nixilis. The source-local sequence does not manufacture a date, assign later Gatewatch membership to the founding era, merge the story with Mending/War of the Spark/Alara chronology, or settle Ugin's warning about the consequences of the titans' deaths.

Every quote was verified against live official HTML with `python3 scripts/source_event_sequences.py --live`: **122/122 excerpts across 17/17 Wizards pages**, including all new relationships and eight unchanged source-corroborated legacy bridges. The normal generation/check path validates identifiers, source registration, grade boundaries, quote hashes, DAG cycles and strict-vs-overlap relations without requiring live network access.

| Recount | Before | After | Scope |
| --- | ---: | ---: | --- |
| Source-local strands | 13 | **14** | No inter-strand order added |
| Source-local events | 121 | **134** | +13 Gatewatch/Zendikar |
| Strict edges | 97 | **109** | +12 source-quoted BEFORE |
| Non-ordering overlap edges | 5 | **5** | Unchanged |
| Supported pairs | 381 | **459** | +78 within the new 13-event chain |
| All possible source-local pairs | 7,260 | **8,911** | Independent exhaustive pair test includes every pair |
| Source-corroborated legacy bridges | 8 | **8** | Unchanged |

Four new representative Q&A questions exercise supported early history, founding-before-defeat, aftermath and a deliberately **UNKNOWN** Gatewatch-to-War of the Spark question. The foundation review packet now contains **76** sampled Q&A cases, independently checked alongside the **8,911-pair** history oracle. This does not meet the entire Phase 4 L244 or broad Phase 7 completeness criteria.

## Phase 3 legacy navigation and story-art integrity

The graph compiler now bridges ten legacy index entries where **the same pack-local entity ID explicitly declares a different full name**, and only where that full name uniquely identifies a type-compatible graph entity. Examples are Ajani / Ajani Goldmane and the Wanderer / The Wanderer. A type collision or a merely shared first word remains unresolved. These are `contextual_pointer` navigation edges, **not new claims, aliases asserted from resemblance, node merges or canon dates**.

The official story caption atlas records an `Anointed Procession` art credit whose frozen snapshot candidate has no Oracle UUID and carries a doubled face name. That caption is **preserved in the original artifact**, but the compiler now reports it as `NO_SNAPSHOT_ORACLE_ID` in the graph input ledger and does not construct an unverifiable Card node from it. It does not guess its UUID from name similarity or another snapshot.

| Integrity check | Before | After |
| --- | ---: | ---: |
| Graph nodes / edges | 5,297 / 8,480 | **5,306 / 8,489** |
| Legacy entries bridged | 125 | **135** |
| Curated navigation edges | 126 | **136** |
| Graph Cards missing Oracle UUID | 1 | **0** |
| Dangling edges / duplicate IDs / graph builder problems | 0 / 0 / 0 | **0 / 0 / 0** |
| Registered cited claims | 1,259 | **1,259** |
| Graph orphans | 14 | **14** |

There are still **15 first-word-only legacy candidates**, **34 legacy-only index entries**, six character alias review candidates and 14 orphan nodes. None were auto-linked. The full audit is reproducible in `scripts/audit_entity_structures.py --check` and `tests/test_entity_structure_audit.py`; story-art safeguards are in `tests/test_story_art_captions.py`.

## Release and ownership boundaries

**89/137** Master Workflow tasks remain checked (**48 open**). This batch strengthens already-checked foundational engineering requirements and meaningfully reduces evidence gaps inside still-open broad history/lookup requirements; it does **not** close those requirements prematurely. The seven release gates still need their existing source/engineering/owner or continuing verification work. The status remains **NOT_RELEASE_READY**, and the three unapproved lore pilots remain deferred.
