# ChatGPT foundation handoff — v2.93 (2026-11-01)

## Starting repository authority

- Verified remote `main` at `03551e6fe6bdb8e16db9311551b9bcb45a5be0a3`, merge of PR #962.
- Master Workflow v2.92: **94/137 checked, 43 open** (26 under review, 17 blocked); foundation **NOT_RELEASE_READY**. Phase 6 and three draft pilots parked; all 62 approved Grixis lists protected.

## Proposed batch (not an acceptance or merger claim)

- New quote-backed five-event Azorius guildmaster succession from three Wizards 2019 story episodes. Counts: **16 strands, 144 events, 116 strict edges, five overlaps, 472/10,296 ordered pairs**, eight unchanged legacy bridges. No assumed present leader or inter-strand order.
- Fixed card lookup to use the verified October 30 Scryfall Oracle drift report with exact snapshot-manifest, indexed-row and field-count safeguards; old and changed-card shards fail closed.
- Three more hard chronology questions in the foundation acceptance packet: **92 representative cases, NOT CERTIFIED**.
- Local source replay **129/129 quotes across 21 live Wizards pages**; 138 Phase 7 Q&A tests passed. See `research/PHASE4_AZORIUS_SUCCESSION_AND_PHASE7_FRESHNESS_2026-11-01.md`.
- **No checkbox closed:** still 94/137 checked, 43 open. This increases evidence breadth and fixes dated lookup trust, but K099, K119, K121, K133 and release gates remain open.

## Before integration / next work

Rebuild and check the acceptance packet, graph/chronology and triage; run targeted CI on the exact feature head, merge only with green required checks and verify `main`. If a newer Scryfall bulk exists at release time, independently replay it. Prioritize the unresolved first-party set codes and the larger War of the Spark / Phyrexia histories without inventing cross-plane orders. Do not treat a successful bounded packet as an exhaustive lore or rules certification. Protect the decks, pilots and frozen source records.
