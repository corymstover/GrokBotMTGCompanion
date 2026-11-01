# Foundation certification candidate v2.99 — handoff (2026-11-01)

**Authority:** `MTG_MULTIVERSE_MASTER_WORKFLOW.md` v2.99. **Candidate:** `READY_FOR_OWNER_REVIEW` is a machine verdict, **not certification**. **Checklist:** 105/137 checked, 32 open (including 10 deferred Phase 6 tasks). **Release definition:** 5 of 7 evidence gates accepted for finite bounded scope; two require exact-head external CI and protected Grixis proof.

## New acceptance evidence

- `scripts/audit_foundation_graph_scope.py` / `data/release/foundation_graph_scope_review_2026-11-01.json`: 78 cited, correctly graded Packs A/B/C graph claims; all primary Wizards sources, checked source/graph hashes; conservative seven-choice genealogy owner disposition file. No source claim grades changed and no fabricated cross-pack event order.
- `data/release/knowledge_foundation_acceptance.json`: explicitly accepted 119-case chronology/history/Q&A packet, with 626 inventoried source pages and 17 source-local event strands. The old packet remains an evidence snapshot marked NOT_CERTIFIED and Phase 6 deferred, as appropriate.
- `scripts/audit_lookup_rules_scope.py` / `data/release/lookup_rules_scope_review_2026-11-01.json`: SHA-pinned November 1 **22:00 UTC** Scryfall Oracle/ruling/parity audit (7 Oracle tracked changes, 49 printing changes, 0 ruling changes, none representing indexed Oracle-text drift), six tested supported routes, exact older CR citation and explicit newer official update bulletin. Critical rule changes return UNKNOWN rather than a false current ruling.
- Rebuilt `data/release/readiness_2026-11-01.json`, certification dry-run, full 137-checklist triage, Progress Tracker, and 119-question acceptance-packet hashes after route/source changes.

## Mandatory next steps before calling the foundation certified

1. Compare the candidate tree with `main`; confirm *zero* protected Grixis file changes and 62 unchanged archived approved decks.
2. Run every PR/push workflow on the exact candidate, then merge; verify all post-merge main workflows and source freshness. Do not assume a remembered CI result applies to a new SHA.
3. Only after those checks pass, record a final, SHA-pinned **knowledge-foundation-only certificate**, check K136 and K137, and preserve the open source/maintenance/Phase 6 checklist tasks.
4. Preserve all three unapproved lore pilots; they are post-foundation. Continue primary-source genealogy/history and full revised Wizards CR discovery as maintenance/research, never silently promote unsupported content.

See `research/FOUNDATION_SCOPE_REVIEW_V299_2026-11-01.md` for accepted scope, all source limitations and exact evidence references.
