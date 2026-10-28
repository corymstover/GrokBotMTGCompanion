# Canonical M7 certification-transfer repair inventory — 2026-10-27

**EVIDENCE AUDIT ONLY — NOT CERTIFICATION, NOT A NEW APPROVAL OR A WAIVER.**

This inventory was reconciled read-only against canonical
`corymstover/grixis-commander-encyclopediaGPT/main` at
`89ef6f71eddf6e18b49b76d0bfb6f82e7f721bc5`, using its immutable
`frozen_approval_snapshot_2026-10-24.json`, required 61-plan manifest,
`state/current_deck_overrides.json`, and the real
`scripts/verify_m7_certification_transfer.py --check` gate. The frozen
snapshots and all 62 approved hashes were **not changed**.

## Real canonical gate result before Deck 56 lock

`M7 CERTIFICATION TRANSFER BLOCKED: Missing evidence file:
refinement/verification/m7_certification_transfer/Nekusar__the_Mindrazer_043d2521cec1e82d.json`

The gate stops on its first failure; independent inventory found **28**
post-snapshot changed approvals, of which **14** lack the mandatory
case-by-case JSON transfer records. Passing the later Deck 56 focused
workflow does not cure the pre-existing failures or certify original
M6 P0/P1 gameplay.

| Current canonical ID | Approved raw SHA prefix | Planned P0 | Planned P1 | Transfer status |
|---|---|---:|---:|---|
| Nekusar__the_Mindrazer | `043d2521cec1e82d` | 5 | 10 | Missing |
| Nicol_Bolas | `a6079935a50b9469` | 5 | 10 | Missing |
| Nicol_Bolas__the_Ravager | `acfa7922e262805a` | 5 | 10 | Missing |
| Goben__Gene_Splice_Savant | `c002a49243bd5478` | **No matching plan** | **No matching plan** | Missing; Norman identity conflict |
| Parnesse__the_Subtle_Brush | `63b605a2c36ec81a` | 5 | 11 | Missing; no dedicated M7 case test located in branch inventory |
| RogSi | `97f3c0ca70303b44` | 6 | 11 | Missing |
| Saruman__the_White_Hand | `dbf71bc86caec1be` | 5 | 13 | Missing |
| Sauron__Lord_of_the_Rings | `c427805f78f7aca7` | 5 | 10 | Missing |
| Sauron__the_Dark_Lord | `266660c6a3241c07` | 5 | 10 | Missing |
| Sedris__the_Traitor_King | `b0aa141fe5d27b1e` | 5 | 10 | Missing |
| Sol_kanar_the_Swamp_King | `2bd99c569df4a868` | 5 | 9 | Missing |
| Sol_kanar_the_Tainted | `c244b7c3e31b108a` | 5 | 10 | Missing |
| Tetsuo_Umezawa | `e00196135931bde6` | 5 | 9 | Missing |
| Tetsuo__Imperial_Champion | `36890584524fb32d` | 5 | 9 | Missing |

At least **66 non-Norman P0 designs** need proof-by-case transfer or fresh
execution; the existing Deck 43 Norman/Goben roster mismatch prevents a
legitimate 61-plan mapping for that entry. The historical M7 candidate
tests for many decks exist, but their exact scoped evidence must be checked
before recording a P0 `PASSED`. Unexecuted designs and P1 deferrals may not
be silently represented as passes.

## Deck 56 The Madcap Jester — owner-approved, canonical pending

- Owner approved exact M7 Rev1 100-card raw SHA-256
  `643eb1cc4827c1dd95485e9922506b514746e6bbc5b4b8a4cfff0f44b1007e43`
  in ChatGPT on 2026-10-27 after its complete Archidekt list was shown.
- Engineering PR [#737](https://github.com/corymstover/GrokBotMTGCompanion/pull/737)
  head `efe4a4ec7cc611815789f64318c5782acb43538f` was merged as
  `e2a36d71a9fce014805193b7a1b6de2099cf772c`.
- Dedicated exact-head run
  [#40592714973](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40592714973)
  and repository M7 gate
  [#40592714914](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40592714914)
  passed. They certify physical/Oracle and **24 bounded** conditions; they
  do **not** turn all original M6 designed cases into formally paid passes.
- The original M6 commander plan
  `data/grixis/m6/test_blueprints/The_Madcap_Jester.json` has five P0 IDs
  (`C1`, `K1`, `K2`, `K3`, `F1`) and ten P1 IDs
  (`K4`, `K5`, `K6`, `E1`, `E2`, `W1`, `W2`, `W3`, `F2`, `F3`).
- `K2`: Dauthi Voidwalker replacement sends would-be-milled cards to
  exile with void counters. The candidate's bounded test explicitly **does
  not certify** whether the exiling is attributed to the Brain Freeze
  controller for The Madcap Jester's permission trigger. Do not change this
  to `PASSED` solely because the changed zone is correct; that would certify
  a different statement.
- `K3`: The original blueprint's assertion that Uba Mask's replacement
  "doesn't trigger" Jester was not proven by a test that merely asserts
  Uba Mask is absent from the final list. This requires causal/rules review,
  even if the candidate ultimately excludes Uba Mask.
- Original M6 I/J inputs were attested but downstream Phase B is
  incomplete. The owner explicitly approved the **decklist**, not an
  invented I/J acceptance or rewrite of the evidence-transfer policy.
- Canonical approved Oct15 artifact remains byte-for-byte unchanged
  (`caeffc07503581cd3ecba798ebc4e09d48f07310f1f117ce3b90a04b5ca6bfa7`).

## Repair sequencing and fail-closed rule

1. Match every missing record against its actual owner receipt, approved
   source bytes, engineering exact-head CI and the canonical pinned plan;
   never synthesize missing test execution from a passing structural gate.
2. Transfer genuinely source-matched executed P0/P1 cases with test method,
   costs, zones, source Oracle and adversarial branch. Freshly execute gaps;
   defer P1 only with explicit deck-specific consequences.
3. Resolve the **Norman Osborn vs Goben** roster/plan conflict with Cory's
   specific authorization. Do not silently rename the immutable 62-deck
   snapshot, alter the required case manifest, or invent a Goben plan.
4. Re-run the real fail-closed canonical validator and focused tests on
   an exact-head certification repair PR. Only when green, create or merge
   the separately approved Deck 56 canonical lock, then verify live main
   and unchanged other deck hashes.

This file is a continuity and forensic ledger; it is not permission to
lower the gate or claim the unresolved work already completed.
