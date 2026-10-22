# Abaddon — M6.6/M6.7 mechanical coverage disposition and next finite gate

**Date:** 2026-10-22. **Author:** GPT-6, same-model analysis, not independent Pass C.  
**Deck:** `Abaddon_the_Despoiler`. **Canonical approved raw SHA-256:** `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`. **Canonical state:** APPROVED/LOCKED, untouched.  
**Engineering parent:** `eab2bf4b88f48cdb0701839096743c189fe3470f` (PR #535 integrated). **Owner standard:** `grixis/Commander-First Decisive Optimization and Test Economy Standard.md`.

## Executed evidence, not new claims

| Mechanical obligation | Existing source-backed case/receipt | Disposition |
| --- | --- | --- |
| Abaddon life-loss threshold and eligible hand spell cascade | `data/grixis/m6/deep_reviews/Abaddon_the_Despoiler.md`; `data/grixis/m6/phase_b_bounded/abaddon_ruinous_cascade_20261021.md` (PR #511) | Bounded deterministic tests executed; not full Oracle-current list certification |
| Neheb postcombat mana, Loyal lieutenant drain, Assault payment and opponent disruption | `data/grixis/m6/phase_b_bounded/abaddon_neheb_assault_20261021.md`; `tests/test_m6_abaddon_neheb_assault.py`; PR #536 Actions run `39727801845` | Twelve reported passing fixtures including Loyal/Neheb removal; conditional loop, not win rate |
| Rakdos life-loss creature cost reduction and forfeited incumbent role | `grixis/m6/abaddon_rakdos_opportunity_cost_20261021.md`; `tests/test_m6_abaddon_rakdos_role.py` (PR #506) | Eleven documented deterministic cost/inventory cases; not a measured whole-deck outcome |
| Ignus/Birgi recast timing, mana ability windows, removal/hate | `data/grixis/m6/phase_b_bounded/abaddon_ignus_stack_windows_20261022.md` (PR #528) | Finite sourced priority fixtures; no full opponent-policy game |
| Physical 100-card mana/hand/cascade source conservation | `data/grixis/m6/phase_b_bounded/abaddon_factorial_ramp_cascades_20261022.md` (PR #532) | Existing 20,000 restricted trajectories, 46 rule and predecessor tests; no reason to repeat |
| Chaos Warp vs resolved hate, Otawara opportunity cost | `data/grixis/m6/phase_b_bounded/abaddon_chaos_warp_stax_20261021.md` (PR #516) | Bounded threat/availability fixtures; not a sampled opponent-hate prevalence |
| The Ruinous Powers upkeep/exile-owner-loss and cascade application | `data/grixis/m6/phase_b_bounded/abaddon_ruinous_cascade_20261021.md`; `data/grixis/m6/judgment_reviews/abaddon_candidate_disposition_synthesis_20261022.json` | Rules-supported retention on on-identity engine; not global optimality |

This ledger is a **reconciliation of cited prior evidence**, not another test run. It does not assert that each earlier workflow was freshly replayed at this new branch head or that current Oracle/legality is fully refreshed.

## Material gaps and finite requirements

1. **M6.6 effect-aware coverage — PARTIAL.** Exact 99-library effects, source-backed current Oracle/legality refresh, candidate-versus-incumbent decision-relevant payable interaction states and concrete red-team response paths have not been certified. Complete a finite case inventory keyed to actual required Abaddon mechanics; existing tests may be reused where identical. Do not expand to full-Magic simulation.
2. **M6.7 judgments — PARTIAL.** The four-candidate synthesis is a truthful M6 *tested-stage* analysis, not final M7 reasoning. For Grinning Ignus, Aggravated Assault, Chaos Warp and The Ruinous Powers, evaluate at least one on-identity lower-opportunity-cost alternative cut and at least two interacting whole-deck packages, with source Oracle/rules references, actual incumbents' contribution, three-color payoff and adverse hate. Finish each with a substantive M7 `SELECT_ADD`, `REJECT`, `RETAIN_ALTERNATIVE` or `EXCLUDE_INVALID`, not `HOLD`.
3. **M6.8 tested-pool I — BLOCKED.** Exact tested-pool boundaries and unresolved judgments preclude local zero-improvement certification. No claim of global optimum.
4. **M6.9 replayable J — BLOCKED.** No final bundle with checked byte hashes, original/target canonical candidate, current rules/Oracle snapshot, test head/commands, execution artifacts, limitation statements and owner-waived Pass C provenance.
5. **M6.10 acceptance — BLOCKED.** No current-cycle certification and no owner milestone acceptance. M7 owner candidate approval is independent and has not occurred.

## No-more-simulations decision

The extant factorial, first-hit, shared-effect, acceleration and source-paid trajectories answer limited mechanical questions. Their reported small sparse Ignus cascade counts do **not** demonstrate no upgrade. The appropriate next tool is the **complete deck opportunity comparison** against credible weak-slot cuts, followed by a small rules-payability/adversarial fixture *only if a concrete contested interaction could reverse a named candidate decision*. Default **zero new randomized trajectories** unless such a decision brief is committed with a finite stopping threshold. The 61-deck PR #535 plans do not apply to Abaddon.

## Next executable engineering action

Reconcile the current exact approved 100-card source and live legal/Oracle references; produce the whole-deck M7 candidate/cut opportunity table (not an approval-ready packet), specifically comparing low-cost alternative cuts for Assault, Ignus and Warp and preserving core Ruinous functions. Identify applicable unverified P0 Abaddon assertions and implement only missing source-backed deterministic cases. Execute targeted tests against **exact PR head**; then create a valid M7 packet and I/J receipts when their hard gates truly pass. Do not mark unrun tests PASS, emit local optimum or modify any canonical authority.

**State:** M6.5 COMPLETE by previously authorized non-independent owner waiver. M6.6/M6.7 PARTIAL. M6.8–M6.10 BLOCKED. M6 certified 0/62, new M7 approved 0/62. Canonical approved decks unchanged.
