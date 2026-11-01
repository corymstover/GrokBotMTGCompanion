# Phase 1B/4/7 v2.91 — sourced real-world versus in-universe timeline comparison

**Acceptance:** K054 is closed as a **bounded, separately labeled two-axis navigation capability**, not as a complete chronology of Magic, an art-scene attribution, a universal premier-set census, or foundation-release certification.

## Sources and proof boundary

Three independent frozen research inputs are joined in one read-only question:

1. **Real-world Scryfall Set API `released_at` metadata**, named set/catalogue snapshot 2026-10-29, with its provenance recorded in Phase 1B.
2. **Real-world official Wizards story-page publication dates**, from the existing 12-title source-graded release-to-story publication bridge; these are actual Wizards URLs, not guessed card-lore associations.
3. **In-universe quoted event relations**, from `data/lore_research/relative_chronology_2026-10-30.json` and `data/lore_research/source_event_sequences_2026-10-30.json`, **only if `source_url` exactly matches one of the official story pages in (2)**. Each resulting relation retains the source quote, SHA-256, event labels, typed relation, graded ledger and direct URL. Neither a source-title match nor shared date creates a new lore ordering edge.

The Q&A route is `ask->set_atlas:dual_timeline`. For example:

`Compare The Brothers' War set release chronology with cited in-universe events`

| Real-world set release metadata | Official story publication | Fictional event evidence from that exact story page |
| --- | --- | --- |
| `bro`: **2022-11-18** per Scryfall | Episode 1 on **2022-10-20** | Episode 1's printed **69 AR** header is retained as `SAME_TIME_AS_LABEL`; the quoted story also orders the war's end **before** Penregon's five-years-later scene. |
| `bro`: same set date | Chapter 1 on **2022-10-21** | The chapter states Urza's tower engineering occurred millennia **before** the chapter's story present. |

This is **three** directly cited event relations across two exact shared official pages, not an assertion that publication occurred in 69 AR. The code always returns `fictional_event_date_corresponding_to_set_release: null` and `release_vs_fictional_event_order: NOT_COMPARABLE_DIFFERENT_CHRONOLOGY_AXES`.

## Non-inference tests

- All **12/12** existing official story title bridges are asked through the dual-timeline route and independently compared against the actual two ledger edge sets by exact source URL; there are no synthetic plot events for unlinked story pages.
- *Bloomburrow* has an official story title link, but no event-order edge on the limited **sampled** pages in the two existing ledgers. It reports `NO_CITED_IN_UNIVERSE_EVENT_ON_LINKED_SAMPLE_PAGES`, not a fabricated plot chronology or a claim the full series has none.
- *War of the Spark* is a known set without a bridge in the **12-title index**: it reports incomplete evidence, not that there was no War of the Spark fiction.
- *Zorblax Time Rift* is an unknown set: `NOT_FOUND`, no invented Wizards URLs.
- An `SAME_TIME_AS_LABEL` AR scene is never used as proof that a different scene happened earlier; strict `BEFORE` is reserved for its own quoted relation.

## Validation and remaining work

- `tests/test_mv_ask_set_atlas.py`: three new targeted regressions and the prior 14 route tests.
- `tests/test_foundation_v291_dual_timeline.py`: two new acceptance methods; full 12-title independent join matrix and K054/foundation/deckbuilding gate assertions.
- `scripts/build_foundation_acceptance_packet.py`: three new adversarial Q&A cases with strict anti-time-conflation guard checks. **89 representative cases, not certified**.
- CI: Phase 7 exercises the new CLI query; Phase 8 independently checks both the technical closeout and new timeline tests.

The Master Workflow now has **93/137 checked, 44 open** (27 under review, 17 blocked). The broad Phase 4 chronology, source grade and unresolved cross-plane eras remain unfinished; the two-axis route provides verified *navigation*, not universal event synchronization. Current Oracle/rules freshness and owner release gates remain pending. No approved decks or historical bulk snapshots were touched.
