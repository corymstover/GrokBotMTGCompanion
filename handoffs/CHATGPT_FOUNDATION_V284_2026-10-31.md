# Foundation continuation handoff — v2.84 (2026-10-31)

## Verified in this batch

- Real baseline: GitHub `main` after merged PR #952 (`0f488e5177a41f9b359b423889b38e63df273a40`). No deck, owner gate or archived source snapshot was touched.
- Graph: ten unique, pack-declared full-name variants now bridge curated navigation without merging nodes or making canon claims; one Oracle-less art-caption match is preserved but excluded from Card graph identity. Current graph: **5,306 nodes, 8,489 edges, 1,259 claims**, 0 bad Card Oracle IDs, 0 graph problems. Audit: **135 bridged** legacy entries; 15 first-word candidates, 34 legacy-only and 14 orphan nodes still unresolved.
- Chronology: new **13-event, 12-edge** Zendikar/Gatewatch source-local historical strand. All source-local strands: **14 / 134 events / 109 strict edges / 5 overlap edges / 459 of 8,911 ordered pairs**. Cross-strand event ordering is still UNKNOWN absent its own source proof; the 56-event Pack A–C legacy ledger and eight source-verified bridges were not changed.
- Live Wizards independent verification: `python3 scripts/source_event_sequences.py --live` reports **122 quotes / 17 source pages PASS**. The full 8,911-pair oracle independently reconstructs reachability, verifies output and catches unsupported chronology paths.
- Q&A: **76** representative acceptance questions, with four additional Gatewatch chronology/UNKNOWN cases. Master Workflow **89/137 checked, 48 open**. Status **NOT_RELEASE_READY**; conditional owner acceptance is not activated.

## Code/regression commands

```bash
python3 scripts/build_multiverse_graph.py --check
python3 scripts/audit_entity_structures.py --check
python3 scripts/source_event_sequences.py --check
python3 scripts/build_plane_history_dossiers.py --check
python3 scripts/build_foundation_acceptance_packet.py --check
python3 scripts/audit_full_checklist.py --check
python3 -m unittest tests.test_source_event_sequences tests.test_chronology_global_pair_matrix tests.test_story_art_captions tests.test_entity_structure_audit -q
```

The official-text `--live` check requires internet; offline checks keep hashes and graph/chronology provenance reproducible. Read `research/PHASE4_GATEWATCH_AND_GRAPH_IDENTITY_2026-10-31.md` for direct Wizards URLs and explicit evidence limits.

## Next highest-value unfinished work

1. Review Phase 7 **integrated card/lore/rules answers and difficult interaction explanations** against live, stable official sources; isolate unsupported current rules/legality answers and add independent adversarial tests. Do not mistake archived card-text snapshots for today's legality.
2. Continue **cross-era, independently linked historical coverage** where direct primary text supports it (Bolas/Gatewatch Amonkhet → War of the Spark; Thran/Weatherlight/Phyrexia). Require explicit source-verified same-event bridges before comparing unrelated strands. Preserve disputed histories and alternative continuities as qualified.
3. Resolve **Phase 1B product-set categories and foreign-bordered printing codes** only with specific Wizards primary documentation. The all-time premier census and set-product street dates are not certified by set metadata alone.
4. Treat exact-head GitHub Actions, owner decisions, and full release-readiness certification as hard gates. Do **not** turn the existing owner-conditional acceptance into approval on the strength of CI alone.

The user's foundation-first directive is still in force: **no new deckbuilding, no approval requests for Pilots 1–3, no changes to the 62 archived approved Grixis decks, their hashes or snapshot manifests.**
