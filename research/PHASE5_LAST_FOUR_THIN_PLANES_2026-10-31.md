# Phase 5 — Four remaining thin-plane dossiers (v2.68)

**Status: PRELIMINARY_RESEARCH_NOT_OWNER_APPROVED.** A finite citation-coverage milestone, not an assertion of complete histories, total chronology, foundation certification, or permission to resume Phase 6 deckbuilding.

Thirteen direct plane relations in [`pack_p5_last_four_thin_planes_2026-10-31.json`](../data/lore_research/pack_p5_last_four_thin_planes_2026-10-31.json) have individual short excerpts, official Wizards citations, date/story perspective, known limitations and graph provenance. Every new excerpt, plus the independent Un-set continuity boundary, passed the **live eight-page HTML audit**.

| Registered plane | Before → after | Source-bounded history | Essential boundary |
| --- | ---: | --- | --- |
| Bablovia | 1 → 5 | [World Class](https://magic.wizards.com/en/news/magic-story/world-class-2017-11-29): student accounts of the five-part government, early Widgeteers, S.N.E.A.K. job board and Goblin Explosioneers | [Wizards' Unstable design feature](https://magic.wizards.com/en/news/making-magic/get-it-unstable-edition-2022-03-21) distinguishes the silver-border Un- setting from ordinary black-border Magic. All four new claims use `ALTERNATE_CONTINUITY`. The older `SSX020` grade is an explicitly open historical source-cache audit issue; do **not** treat it as a mainline bridge. The student's 54-year date is relative, not AR. |
| Meditation Realm | 3 → 5 | [Chronicle of Bolas: The Unwritten Now](https://magic.wizards.com/en/news/magic-story/chronicle-bolas-unwritten-now-2018-08-15) recounts early Ugin contemplation; [Planes of Planechase](https://magic.wizards.com/en/news/feature/planes-planechase-2009-12-30) records Bolas's Madaran-adviser meeting use | Neither ancient use proves an intact current realm after the separately researched Dragonstorm destruction or a current address for Bolas or Ugin. |
| Muraganda | 1 → 5 | [Aetherdrift Planeswalker's Guide, Part 2](https://magic.wizards.com/en/news/feature/planeswalkers-guide-to-aetherdrift-part-2): ancient magic-using civilization's collapse, shattered moons and later impacts, rebuilding survivor societies, and Grand Prix-era Saurid Autocracy | The cause and precise date of moon shattering are unstated. The Saurid Autocracy was a dominant state, not demonstrated ruler of the whole world; folklore on ooze origin is explicitly disputed. |
| Skalla | 2 → 5 | [Vivien's official profile](https://magic.wizards.com/en/story/vivien-reid-planeswalker) on the natural/technological conflict; [Unbowed, Part 1](https://magic.wizards.com/en/news/magic-story/unbowed-part-1-2018-08-29) on remembered wildlife; [What Core Can I Say?](https://magic.wizards.com/en/news/making-magic/what-core-can-i-say-part-2-2019-07-08) on Arkbow spirit-copy preservation | Remembered ecosystems and summoned spirit copies are not living present-day survivors or evidence of a complete pre-destruction political chronology. |

## Deterministic, bounded outcome

- **0/33 registered plane dossiers** remain below five direct cited relations. The threshold is triage, not thorough history research or plane registration completeness. Every dossier remains `complete_history: false` through its Q&A interface.
- Graph: **1,259 graded claims**, **5,290 nodes**, **8,473 edges**; **640/640 registered** Character/Faction nodes have some direct cited incident claim. This is not a census of every character or faction in Magic.
- Same inventoried official story source scope: **576 cited + 50 reviewed without a claim = 626** accounted pages; the eight live official pages were checked independently and do not enlarge the old frozen inventory.
- Claim-to-card anchor index: **1,259 accounted claims** and **4,118 anchors** after append-only non-set-pack regeneration. The absent pinned Scryfall bulk still prevents full historical printing/art-source replay.
- Foundation review packet: **38 unique representative real Q&A calls**, including one per final plane and Bablovia's `ALTERNATE_CONTINUITY_PRESENT` confidence flag. No Q&A example establishes a total chronology.
- **83/137 engineering checklist unchanged**; Phase 8 remains `NOT_RELEASE_READY`, foundation owner signoff ungranted, three lore-deck pilots `UNAPPROVED`, Phase 6 parked. All 62 approved Grixis decks and owner records are outside this change.

## Reproduce and inspect

```sh
python3 scripts/audit_p5_last_four_thin_planes.py --check
python3 scripts/audit_p5_last_four_thin_planes.py --live  # optional, live network required
python3 -m unittest discover -s tests -p 'test_p5_last_four_thin_planes.py' -q
python3 scripts/build_multiverse_graph.py --check
python3 scripts/build_plane_history_dossiers.py --check
python3 scripts/build_plane_history_priorities.py --check
python3 scripts/build_story_coverage_inventory.py --check
python3 scripts/build_claim_card_anchors.py --check
python3 scripts/build_foundation_acceptance_packet.py --check
python3 scripts/certification_dry_run.py --check
python3 scripts/update_multiverse_progress_tracker.py --check
```

The v2.68 proof **does not** close wider chronology, narrator/revision disputes, unregistered or under-researched planes, comprehensive biographies, the pinned Scryfall source-bulk restoration or owner foundation acceptance. Evidence density and legal/card provenance are separate questions. Do not start deckbuilding simply because the registered thin-plane counter is zero.
