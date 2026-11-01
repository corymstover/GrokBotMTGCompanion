# ChatGPT foundation handoff — v2.90 (2026-11-01)

## Verified starting point

- GitHub `main` before this batch: merge commit `1ee95f93bcc2b1deaca4f266736bfc200e3032a8` from [PR #959](https://github.com/corymstover/GrokBotMTGCompanion/pull/959), exact-head **23/23**, post-merge **10/10**.
- The original Master Workflow v2.89 reported **89/137 checked, 48 open**. It distinguished broad incompleteness from three narrow technical deliverables that already had substantial implementation.
- Do not resume Phase 6 or pilot approvals before foundation certification. Preserve all 62 approved Grixis decks and dated historical source snapshots.

## v2.90 work and evidence

- Added independent snapshot recensus of all 16 card-history identity buckets, checking G6's 37,853 dated English-paper identities / 33,766 single-set debuts / 4,087 ties, edge-layout disclosure and zero per-set mismatches.
- Exhaustively test-navigated **all twelve** official source-title Set Atlas → story-series bridges, checked direct Wizards page citations and the strict real-world date/in-universe chronology separation.
- Enforced a multi-domain 86-case representative difficult-Q&A matrix, including published interaction, disputed histories, unsupported joins and known negative evidence.
- Independent recensus passes using the committed history index. Full `audit_phase1b_snapshot_gates.py --check` is **blocked locally** by the absent pinned October 29 compressed Scryfall file; raw-source fresh replay remains a release-time gate, not a claimed success.
- Marked only **K053, K104, K122** complete because these *specific engineering deliverables* are demonstrably fulfilled within their already disclosed scope; the stronger research/release criteria remain unchecked. Full checklist triage now **92/137 checked, 45 open; 28 under review and 17 blocked**.
- Evidence: `research/FOUNDATION_ENGINEERING_CLOSURE_V290_2026-11-01.md`, generated `data/release/full_checklist_triage_2026-11-01.json`, tests `tests/test_foundation_v290_checklist_closure.py`.

## Gate and next work

- Run independent local artifact rebuilding, comprehensive relevant tests, exact-head GitHub CI, merge and post-merge checks before claiming this batch integrated. **Technical checklist completion is not owner acceptance or foundation certification**.
- Next true blockers: historical set source exceptions, cross-plane source-graded chronology, broader plane/character/faction histories, live Scryfall/CR currentness and owner-reviewed foundation release gate. Source/owner gaps must not be relabeled complete; 10 Phase 6 tasks remain intentionally parked.
