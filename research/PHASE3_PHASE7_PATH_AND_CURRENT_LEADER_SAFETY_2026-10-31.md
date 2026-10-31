# Phase 3/4/7 — Evidence-safe graph navigation, leadership and full chronology pair matrix

**Checkpoint:** 2026-10-31

**Status:** ENGINEERING CORRECTNESS MILESTONE; PRELIMINARY RESEARCH / NOT_RELEASE_READY.

## Independently reproduced defects

1. `MG.path('piru', 'ugin', max_depth=1)` used to return the **first hop of a two-hop path**. That prefix did not reach Ugin, although the API returned it as a path to Ugin. Paths are now searched with a real depth cap and return `None` unless the target is reached within it.
2. The graph path from the alternate-world Echoverse to Nicol Bolas previously returned the `A012` `ALTERNATE_CONTINUITY` edge as an ordinary path. Another shortest path between Bolas and Karn traversed `CANON_DISPUTED` edges. A path now defaults to cited `CANON_CONFIRMED` edges. Explicit `--include-qualified` allows inspection of those uncertain branches with their status still visible, and unsourced shortcuts are never followed. Each hop records the actual traversal direction separately from the source claim's original direction. Undirected navigation does **not** prove cause, sequence, travel, or historical continuity.
3. `Who leads the Izzet?`, `Who is the guildmaster of the Izzet?` and `Who rules the Azorius?` were marked `VERIFIED` because their cited leader relationships were confirmed, although publication dates do not establish who holds the office **today**. Present-tense leader answers now say `QUALIFIED`, set `CURRENT_LEADER_NOT_ESTABLISHED`, and include `verified_current_leader: null`. Past-tense `Who led the Izzet?` remains a verified cited relationship; unsupported leaders remain `NOT_FOUND`.

## Independent validation scope

- `tests/test_graph_path_evidence_safety.py` checks actual known paths and a fabricated minimal adversarial graph where a shorter disputed or unsourced edge competes with a two-hop cited and confirmed route. It also checks CLI max-depth, reverse traversal, alternate-continuity opt-in and invalid bounds.
- `tests/test_mv_ask_present_leader_safety.py` probes bare-present leader phrasings and every faction having an incoming cited leader edge, without assuming the current officeholder; old factual relations and unknown factions remain intact.
- `tests/test_chronology_global_pair_matrix.py` rebuilds source-local reachability **independently** of the production closure algorithm from every strict cited edge, checks its saved materialization and compares every **6,441 unordered pair** of the **114** source-local events against the retriever. It requires strict proof paths for the **371** supported orders, verifies that the three overlapping relations do not become strict, rejects cross-strand ordering without provenance and verifies `UNKNOWN` is kept when no path exists. This validates graph algebra and handling of stored source quotes, **not independently the complete accuracy of all Magic stories**.
- The knowledge-only foundation acceptance packet now executes **67 representative questions** (three more leadership cases) and preserves sourced past-tense answers and honest present-tense uncertainty. The two cross-plane graph-navigation examples still require fully cited paths; neither is treated as a story chronology.

## Replay

```sh
python3 -m unittest tests.test_graph_path_evidence_safety tests.test_mv_ask_present_leader_safety tests.test_chronology_global_pair_matrix -q
python3 -m unittest tests.test_multiverse_graph tests.test_mv_ask_temporal_confidence tests.test_mv_ask_leader_phrasings_b14 tests.test_foundation_acceptance_packet -q
python3 scripts/source_event_sequences.py --check
python3 scripts/query_lore_chronology.py --check
python3 scripts/build_foundation_acceptance_packet.py --check
python3 scripts/audit_full_checklist.py --check
python3 scripts/update_multiverse_progress_tracker.py --check
```

No new historical identity, absolute AR year, owner approval or deck-research
scope was inferred. Checklist stays **89/137 checked, 48 open**. Foundation
status is **NOT_RELEASE_READY**; the 62 approved Grixis lists, archived
snapshot evidence and three parked UNAPPROVED lore pilots remain untouched.
