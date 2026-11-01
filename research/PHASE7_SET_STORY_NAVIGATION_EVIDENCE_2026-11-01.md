# Phase 7 v2.89 — source-graded set → story-series navigation

**Status:** bounded Phase 1B/Phase 7 integration; **not** an in-universe chronology, comprehensive story index, plot summary, image attribution, or foundation certification.

The normal `scripts/mv_ask.py ask` entry point now supports:

- `What official Magic stories are linked to The Brothers' War set?`
- `Show the release date and official story series for Bloomburrow`
- `Is War of the Spark linked to an official story series?`

## Evidence contract

1. Resolve a unique Scryfall Set API code/metadata name from the committed `data/set_atlas/catalog_2026-10-29.json`. The resolver handles initial `The` in named releases without guessing a substring match.
2. Require exact snapshot and set-code concordance with `data/set_atlas/phase1b_release_scope_story_bridge_2026-10-29.json`. The bridge contains **12** explicit Wizards publication-title links among **1,062** catalogued set codes. It is not an exhaustive fiction association map.
3. For a matched bridge, return the official series title, total recovered story pages and at most three sample pages, with their **Wizards URL**, exact title and **publication date**. Each sample URL appears in the top-level evidence citations.
4. Report the set's `released_at` date as **Scryfall metadata**, distinct from the official page publication dates. Neither date indicates when a fictional event occurred. Official title association is navigation only; no inference about depicted art, plot, lore event order, or Commander legality.
5. For a known set missing from the 12-link index, return `NO_OFFICIAL_TITLE_STORY_LINK_IN_BOUNDED_INDEX`, not a false claim that Wizards published no story. Unknown sets fail closed as `NOT_FOUND` without primary-story citations. Scope flags do not incorrectly label this full-code lookup as an English-paper-only printing count.

## Representative adversarial cases

| Question | Verified answer | Deliberate limit |
| --- | --- | --- |
| *The Brothers' War* | Set code `bro`, Scryfall recorded date **2022-11-18**, official story title *The Brothers' War*, **10** stories in recovered series; three sampled Wizards pages begin **2022-10-20**. | Publication before release is not time travel or a War-era chronology proof. |
| *Bloomburrow* | Set code `blb`, official *Bloomburrow* series, **5** recovered story pages; independently scoped set date. | No implied character, region or art depiction link. |
| *War of the Spark* | Known `war` set, no title bridge in this **bounded** 12-series index. | Does **not** assert that no War of the Spark fiction exists. |
| *Zorblax Time Rift* | `NOT_FOUND`, no named official story. | No guessed set name or source URLs. |

## Verification and hold

- `tests/test_mv_ask_set_atlas.py` includes five new adversarial tests for exact-name resolution, citations, real-vs-fictional chronology, unsupported links, unknown names and routing regression.
- `scripts/build_foundation_acceptance_packet.py` adds three deterministic Q&A acceptance cases with anti-overclaim assertions: **86 representative cases, NOT CERTIFIED**.
- `.github/workflows/phase7-companion-ask.yml` exercises the cited Brothers' War route and discovers the extended tests.

The wider checklist remains **89/137 checked, 48 open**. Phase 1B classification/source exceptions, comprehensive plane/faction histories, cross-ledger in-universe chronology and broader difficult-Q&A capability remain open. No Phase 6 deckbuilding, pilot approvals or protected-deck mutations.
