# M6 / M7 Secondary Completion Sub-Tracker

**Companion to the overall M0–M8 project tracker** — live milestone accounting amended by Cory's formal 2026-10-21 Pass C independence waiver. The original Cycle131 history below remains historical context.

> This is a status report, not an approval, a new optimization result, or authorization to change a deck. The live source of milestone acceptance is `data/grixis/registry.json`. The current canonical 62/62 approved/locked lists are in the separate encyclopedia repository.
>
> **Formal waiver receipts:** `data/grixis/m6/governance/pass_c_owner_waiver_20261021.json` and [M6 Pass C Owner Waiver](M6%20Pass%20C%20Owner%20Waiver%202026-10-21.md). M6 Phase B remains PARTIAL and no deck is M6-certified.

## Progress at a glance

| Milestone | Completed sub-gates | Partially executed gates | Complete deck certifications / review decisions | Official status |
| --- | ---: | ---: | ---: | --- |
| **M6 — refinement with formally owner-waived Pass C** | **5/10 (50%)** | 1 | **0/62 certified** | **In progress** |
| **M7 — Cory review and second refinement** | **0/6 (0%)** | 0 | **0/62 new M7 decisions** | **Not started** |

**50% means five of ten amended M6 *governance sub-gates*, not 50% of gameplay testing or deck certification.** M6.5's owner-waived completion counts a review-governance substitution, **not** 62 technically independent third-model reviews (actual independent count: **0/62**). All other M6 obligations remain; no Phase B, M7 or M8 acceptance is implied.

### M6 sub-gates

| Gate | State | Scope and remaining requirement |
| --- | --- | --- |
| **M6.1** Accepted M5 inputs/provenance | ✅ Complete, 62/62 | M5 authority and input SHA receipts available |
| **M6.2** Objective-specific A/B technical projections | ✅ Complete, 62/62 | Sealed objective-specific projections; their technical separation does **not** establish independent operators or full blind review |
| **M6.3** Reconciliation/deep-review queue creation | ✅ Complete, 62/62 | Reconciliation inventory exists; the **8,848** deep-review items **are not adjudicated** |
| **M6.4** Commander-first case-specific judgment preparation | ✅ Complete, 62/62 | Cycle131 added the 29 missing source-anchored authored exact-candidate reviews, verified against approved 100s, blueprints and frozen Oracle. This is **not** formal independent Pass C or a conclusion about all 8,848 candidates |
| **M6.5** Pass C with formal owner waiver | ✅ Complete under owner-waived substitute, 62/62 | Cory explicitly authorized the 62 GPT-6 owner-equivalent Josh-Lee-Kwai reviews to **replace** the third-model requirement on 2026-10-21; independent third-model work was **not performed (0/62)**. See [formal waiver](M6%20Pass%20C%20Owner%20Waiver%202026-10-21.md). The 47 NEEDS TESTING dispositions remain Phase B obligations |
| **M6.6** Effect-aware Phase B, paired tests, stress & red team | ◐ Partial foundation, **0/62 certified** | Cycles 118–126 supply bounded source, mana and hypothetical opponent fixtures for 3 decks. Cycle125 fixed the original invalid Jewel-to-Rings payment; Cycle126 tested Bolas Mox vs Amplifier across 1,024 paired physical shuffles (300/296/267 payable commander casts, just 3 transforms per policy and 1 Amp doubling). Complete Phase B remains 0/62 |
| **M6.7** Decision-grade `judgment_review` obligations | ☐ Blocked, 0/62 | Resolve strategic conflicts and human-judgment requirements |
| **M6.8** I: tested-pool local zero-improvement certification | ☐ Blocked, 0/62 | Requires resolved judgments and all relevant tests; certifies tested pool only, never global optimality |
| **M6.9** J: final complete reproducibility bundles | ☐ Blocked, 0/62 | 62 *input* receipts exist, but no final complete per-deck evidence bundles |
| **M6.10** Complete schema-ready packets and M6 acceptance | ☐ Blocked, 0/62 | User-controlled milestone acceptance; 0 formally complete M6 certificates |

### M7 sub-gates

| Gate | State | Scope and remaining requirement |
| --- | --- | --- |
| **M7.1** Receive M6-complete decision packets | ☐ Blocked, 0/62 | Cannot reuse preparatory M6 packets as complete |
| **M7.2** Cory's explicit second-cycle decision for each deck | ☐ Not started, 0/62 | The existing 62 canonical approvals do **not** count as M7 packet decisions |
| **M7.3** Verify M7-reviewed hashes against registry | ☐ Not started, 0/62 | Record exact newly reviewed deck hashes |
| **M7.4** Re-close decks changed in cycle 2 | ☐ Conditional | Only if the user approves changes; existing locks remain protected |
| **M7.5** Process reopen triggers and planned releases | ☐ Not started | Includes documented 2026-11-13 trigger; do not mark a future event processed |
| **M7.6** Explicit M7 milestone acceptance | ☐ Not started | Only the user can accept after requirements are met |

## How to keep this tracker trustworthy

The machine-readable status and named evidence are in [`data/grixis/milestone_m6_m7_subtracker.json`](../data/grixis/milestone_m6_m7_subtracker.json). This Markdown page and its JSON are **dated snapshots**. Before reporting any change, compare the live GitHub registry, approved deck authority, verified PRs, evidence receipts, and milestone criteria; update the snapshots and cite the new exact CI head.

The ongoing ChatGPT project progress section will always include:

1. Overall milestones M0–M8.
2. **M6 complete/total gates**, partial gates, 0–62 formal M6 deck certifications, named next blocker.
3. **M7 complete/total gates**, 0–62 second-cycle decisions, and dependency.
4. 62/62 canonical approved/locked versus 0/62 formally M8-certified (until evidence changes).
5. Current cycle, last merged PR, CI URL and blockers.
6. **Your Next Step** (last).

**Milestone authority:** `grixis/Grixis Authority Model.md`, sections M6 and M7.

**Certification details:** `grixis/Grixis M6 I-J Contract.md`; `data/grixis/m6/sealed/reconciliation_manifest.json`; `data/grixis/m6/preflight.json`.

**Historical checkpoint, superseded by the owner waiver and merged October 21 follow-ups:** Cycle 131; merge commit `88f062be961c39108e58213c1763e31fb46c396b`; [Cycle131 PR #247](https://github.com/corymstover/GrokBotMTGCompanion/pull/247), [exact-head CI #39216759804](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/39216759804). **62/62 source-specific authored commander reviews complete** (last 29 in five detailed bundles), with a [Pass C handoff](M6%20Authored%2062%20Pass%20C%20Handoff.md). **At that historical checkpoint, 4/10 M6 subordinate gates were complete, 1 partial**; following the 2026-10-21 formal waiver, it is **5/10** with the additional M6.5 gate satisfied *only on the waived owner-equivalent basis*. Independent third-model Pass C remains a factual 0/62, full certified Phase B 0/62, M6 certified 0/62, M7 0/6, M8 0/62. The 62 existing canonical approvals remain read-only. Three previous GrokBot advisory reviews do not qualify automatically as independent Pass C.

**Protected canonical evidence:** 62/62 locks verified at encyclopedia HEAD `b77ba89b72eacfa4d58d1db937e3a91a2000dd16`; overrides file Git blob SHA `81801b2f9d3387b171c01f1fcae255b385a5b698`.

## Separate comprehensive one-deck-at-a-time quality review (owner instruction 2026-10-19)

The 62/62 M6.4 authored cases are **candidate-specific source coverage**, not an exhaustive whole-deck strategic refinement. Historically, the owner required sequential comprehensive authored deep reviews prior to a final third-model handoff; **those deep reviews and the owner-equivalent Pass C are now both 62/62 complete**, with the independent requirement formally waived for M6.5. The durable authoritative quality-pass ledger is `data/grixis/m6/single_deck_depth_tracker.json`, initialized at **0/62** and ordered by the canonical CSV starting with Abaddon. The required process is `grixis/M6 Commander-First Single-Deck Review Standard.md` and root `AGENTS.md`. This quality pass does **not** undo the earlier M6.4 limited-coverage completion, approve any deck/card change, certify Pass C or alter M6's existing gate count. Recognize the canonical Goben versus engineering Norman ID discrepancy and three normalized-ID variants in the ledger before claiming per-deck review completeness.
