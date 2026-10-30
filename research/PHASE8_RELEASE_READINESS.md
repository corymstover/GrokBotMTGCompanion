# Phase 8: release-readiness check (read-only)

`scripts/release_readiness.py` checks each criterion in the master workflow's **Definition of the first major Companion release** against committed artifacts. Report: `data/release/readiness_2026-10-30.json`.

The statuses are MET, PARTIAL, NOT_MET and EXTERNAL (needs CI or a human). The tool never approves, locks or certifies anything. The best verdict it can give is `READY_FOR_OWNER_REVIEW`.

## Result at main b5ff3a2f (2026-10-30): **NOT_RELEASE_READY**. MET 1 · PARTIAL 3 · NOT_MET 1 · EXTERNAL 2

| Criterion | Status | Why |
|---|---|---|
| Priority enrichment backlog | PARTIAL | 3,409/5,362 done; 1,953 remain, blocked on the missing story-text, EDHREC and Spellbook caches. |
| Cited connections across Packs A, B and C | PARTIAL | All three packs are in the graph (305 nodes / 488 edges, 0 non-Wizards sources, graph current), but every pack is PRELIMINARY_RESEARCH. |
| Lookup and rules checks backed by current Scryfall | PARTIAL | Card lookups reconcile with snapshot 2026-10-29 (0 changes across 33,894 cards); rules-interaction checks are not built yet. |
| Phase 1B set catalog | MET | `QUALIFIED_OFFLINE_FUNCTIONAL_RELEASE_READY` (2026-10-29), with its 8 stated limitations. |
| Reviewed lore-first deck built from the new graph | NOT_MET | Owner-approval files exist only for earlier lore decks. The one graph-linked draft (Pilot 1, Ugin/Bolas) awaits Cory's review. |
| No Grixis regression | EXTERNAL | Guarded by focused-validation CI. Read-only SHA-256 digests of the protected paths are recorded for comparison. |
| Passing focused CI and coverage report | EXTERNAL | Check the CI runs on the release commit. |

## Fastest path to READY_FOR_OWNER_REVIEW
1. Cory reviews the Pilot 1 draft. Approval files are written only by the owner.
2. Owner review of Packs A, B and C.
3. Restore the enrichment caches, or have the owner accept the 1,953 as documented exceptions.
4. Add rules-interaction checks to the companion.
