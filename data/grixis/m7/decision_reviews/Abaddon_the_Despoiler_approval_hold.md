# Abaddon — Exact-100 M7 candidate ready for structural review, M6 certification still on hold

**Date:** 2026-10-22. **Source authority:** `corymstover/grixis-commander-encyclopediaGPT/main` retains the approved/locked list SHA-256 `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`.

This file explicitly distinguishes two levels of **ready** that must never be confused:

1. **M7 packet structural readiness:** `data/grixis/m7/decision_reviews/Abaddon_the_Despoiler.json` (machine contract), with candidate `data/grixis/m7/candidate_lists/Abaddon_the_Despoiler.txt`, SHA-256 `1fabe1251a7868838365144bf0cb1ee903d394ed90ac146b2dd9cdd45683b7dd`. Source-bound 100-card and two-swap audit, candidate decisions, 34-land invariance, Oracle/legality evidence and three tags must pass exact-head GitHub CI. The packet's contract-required `READY_FOR_EXACT_OWNER_APPROVAL_NOT_YET_APPROVED` describes **structural packet readiness only**; it does not override prerequisite M6 milestone gates or grant user approval.
2. **Project final verification/owner handoff:** still **HELD** pending formal M6.6 effect sufficiency, M6.7 certification reconciliation, M6 I tested-pool local-optimum certification for the **chosen final candidate**, and M6 J complete reproducibility bundle. The 95 case tests, 97 live Scryfall identities across five complete lists, owner-waived nonindependent Pass C (62/62) and authored qualitative selection are real evidence, **but not full fulfillment of these four gates**.

**Chosen package:** +Grinning Ignus +Chaos Warp / -Rakdos, Lord of Riots -Inevitable Betrayal. Opponent-creature-rich alternative cuts Keeper instead, losing a 40K repeated exile-cast damage payoff. No card change is made in this PR. Bracket 4 — Optimized, candidate tags `Cascade`, `Exile Cast`, `40K Chaos`.

**Priority finalization path:** (a) use exact-head CI to freeze the M7 candidate/packet under immutable hash; (b) evaluate M6.6 sufficiency and the P1/gameplay limitations **for the specific chosen candidate**, not automatic 74-card new P0 runs; (c) if defensible, complete honest selected-pool local-optimum I and full source-hashed J bundle, otherwise keep them BLOCKED and document exact cause; (d) only after all required gates, present the exact 100 and standard owner question `This deck is complete. Do you approve it?`. Upon explicit approval, write approved/locked canonical record and **only then** proceed to commander #2.

**Anti-homogenization:** retain 40K threshold hand-cast cascade, Lost/ Keeper/ Ruinous Powers, Abaddon-specific early damage, printed double cascade, and Breach backup. Do not fill missing certification with generic turbo-Grixis proxies.

**Formal statuses:** M6.5 owner waiver COMPLETE; M6.6 PARTIAL; M6.7 PARTIAL; M6.8/I BLOCKED; M6.9/J BLOCKED; M6.10 BLOCKED; revised M7 approvals 0/62; M8 not complete. Neither the structural schema validator nor current replay supersedes these statuses.
