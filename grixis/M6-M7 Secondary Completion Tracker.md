# M6 / M7 Secondary Completion Sub-Tracker

**Companion to the overall M0–M8 project tracker** — authoritative snapshot **after Cycle 128**.

> This is a status report, not an approval, a new optimization result, or authorization to change a deck. The live source of milestone acceptance is `data/grixis/registry.json`. The current canonical 62/62 approved/locked lists are in the separate encyclopedia repository.

## Progress at a glance

| Milestone | Completed sub-gates | Partially executed gates | Complete deck certifications / review decisions | Official status |
| --- | ---: | ---: | ---: | --- |
| **M6 — refinement and independent certification** | **3/10 (30%)** | 2 | **0/62 certified** | **In progress** |
| **M7 — Cory review and second refinement** | **0/6 (0%)** | 0 | **0/62 new M7 decisions** | **Not started** |

**30% means exactly three out of ten named *sub-gate checkboxes*, not 30% of elapsed work, tested candidate quality, or deck completion.** A gate is counted complete only when its *narrowly stated* result exists; source data and partial tests do not count as independent critique, actual games, or final certificates.

### M6 sub-gates

| Gate | State | Scope and remaining requirement |
| --- | --- | --- |
| **M6.1** Accepted M5 inputs/provenance | ✅ Complete, 62/62 | M5 authority and input SHA receipts available |
| **M6.2** Objective-specific A/B technical projections | ✅ Complete, 62/62 | Sealed objective-specific projections; their technical separation does **not** establish independent operators or full blind review |
| **M6.3** Reconciliation/deep-review queue creation | ✅ Complete, 62/62 | Reconciliation inventory exists; the **8,848** deep-review items **are not adjudicated** |
| **M6.4** Commander-first case-specific judgment preparation | ◐ Partial, 21/62 | Cycles 112–116 and 128 authored source-specific analyses; 18 exact-swap HOLDs and 3 unresolved hypotheses across 21 decks (41 remain); no formal independent critic |
| **M6.5** Named independent Pass C & conflict resolution | ☐ Blocked, 0/62 | Three GrokBot non-author analytical reviews received; prior blueprint exposure disclosed and strict blinding not claimed. Qualification, full 62-deck independent Pass C and reconciliation remain incomplete |
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

**Latest completed engineering cycle:** 128; merge commit `d39c2ec8161ea71368bf957af5ff4f84b169a7a6`; [Cycle128 PR #240](https://github.com/corymstover/GrokBotMTGCompanion/pull/240), [Cycle128 CI](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/39207557465), six frozen-Oracle and real physical-source authored HOLD reviews. [Cycle127 PR #239](https://github.com/corymstover/GrokBotMTGCompanion/pull/239) prepared 62 neutral packets without claiming completed reviews. Author review 21/62, M6 3/10 complete gates (2 partial), independent Pass C 0/62, effect-aware complete Phase B 0/62, M7 0/6, M8 0/62. Prior Cycle126 Bolas comparison remains inconclusive. Three external advisory reviews received; none qualifies automatically as formal Pass C.

**Protected canonical evidence:** 62/62 locks verified at encyclopedia HEAD `b77ba89b72eacfa4d58d1db937e3a91a2000dd16`; overrides file Git blob SHA `81801b2f9d3387b171c01f1fcae255b385a5b698`.
