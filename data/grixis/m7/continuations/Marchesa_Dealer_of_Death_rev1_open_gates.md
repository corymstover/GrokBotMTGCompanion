# Deck 34 M7 Rev1 exact-source continuation ledger

Owner-unapproved, research-only engineering draft PR #714, Oct 25, 2026
(America/Chicago). Scope: Marchesa, Dealer of Death **only**.

- Live canonical `corymstover/grixis-commander-encyclopediaGPT@main` still
  approved/locked Oct 15 list raw SHA
  `34a6a940c54aaebde612ae5d3a244e22931d3a977fa26e4c43f2a76aafc0f6b1`.
- Eight-swap current proposed 100 raw SHA
  `f6f68d204925ef3528166722d874cd4122e50755b30f8b9a9ac19d7eff9afd3e`.
- Baseline, proposed TXT, exact swaps, tradeoffs, 3 complete 100-card
  alternative lists and 19 focused local tests: PR #714.
- Exact case-source plan:
  `data/grixis/m6/test_blueprints/Marchesa__Dealer_of_Death.json`;
  design-only at capture. The existing `m6/ij/input_receipts/marchesa-dealer-of-death.json`
  states `phase_b_replayed=false`, `inputs_attested_downstream_incomplete`.
- Status **RESEARCH_ONLY_NOT_CERTIFIED**. No new canonical write, user approval,
  official 100-card bulk refresh, exact I/J closeout, or M6 certificate has occurred.

## Targeted finite test coverage map — no automatic formal promotion

| Case | Priority | Existing focused executable check | Remaining certification limitation |
|---|---|---|---|
| C1 | P0 | `test_C1_commander_paid_selection_and_removed_negation` | Verify source-paid timing with formal priority, target invalidation, library-one-card edge |
| K1 crime definition | P0 | `test_K1_target_definition_and_one_crime_per_ability` | Explicit cast/activate/put-trigger-on-stack cases with source-verified CR and controllers |
| K2 Hex X=0 | P0 | `test_K2_hex_parasite_x_zero_source_paid` | Current Oracle + valid opposing permanent + opponent response and life/payment fixture |
| K3 Spatial | P0 | `test_K3_spatial_binding_life_and_repeat` | Phasing condition, same turn response and repeated source cost against legal board |
| F1 graveyard hate | P0 | `test_F1_graveyard_hate_and_counterplay` | Full payable Breach line and named hate interruption both with/without Marchesa |
| K4 Lapis | P1 | `test_K4_lapis_trigger_targets_even_if_optional_three_declined` | Opponent blue-spell stack, trigger target choice, resolution timing and {3} payment in formal fixture |
| K5 Tezzeret Kitten | P1 | `test_K5_tezzeret_kitten_new_object_and_priority_window` | Confirm blink/loyalty legality under opposing counter/removal and required spell timing |
| K6 extra turns | P1 | `test_K6_removed_last_chance_is_not_current_candidate_requirement` | Final M7 has only Final Fortune; source M6 two-extra-turn package absent: document scoped deferral |
| K7 Mox/Magda | P1 | `test_K7_mox_amber_and_magda_tapped_treasure` | Full 3-pip paid Marchesa cast and freshly tapped Treasure windows |
| E1 crime engine | P1 | `test_E1_claws_devils_and_drake_paid_new_crimes` | Card-accurate opponents' sacrificial timing, GY-empty Claws, copied triggers and paid {1} |
| E2 fast mana/draw | P1 | `test_E2_mana_and_draw_limitations` | Source-paid 100-card opening 3-pip/color stress and relevant effects, not proxy success rates |
| W1 Oracle/Pact | P1 | `test_W1_oracle_consult_source_paid_and_stack_disruption` | Full Tainted Pact/Consult option, exiled library Oracle trigger devotion/responses |
| W2 Breach | P1 | `test_W2_breach_led_brain_freeze_hate_response` | Paid recursive escape costs, library/mana/conservation and finite win endpoint |
| W3 Bow/Alchemist | P1 | `test_W3_bow_alchemist_three_finite_tap_cycles_and_tomem` | Summoning-sickness, equipment priority, damage per target and Cursed Totem interruption |
| F2 Marchesa removed | P1 | `test_F2_removed_commander_gives_no_selection` | Recast source mana/tax and opponent responses |
| F3 baseline identity loss | P1 | `test_F3_historical_baseline_is_not_the_M7_source` | Historical 48-card rebuild is not a new M7 mechanic; explanatory P1 disposition required |

These local unit fixtures encode correct high-level interactions but lack
complete MTG board/stack state transitions. They are **not** the same thing as
formal M6 P0/P1 test acceptance, a reliable multiplayer win-rate model, a
fresh Oct25 100-card Oracle fetch, or a final I/J bundle.

## Next actions, in order

1. Verify PR #714 exact-head CI, resolve failures without changing 100-card
   membership except with a distinct new candidate revision/hash.
2. Perform actual full-list current Scryfall collection/Commander legality
   verification (92 retained baseline names + eight new), pin exact source
   timestamps and no named exception. Retain earlier snapshots as evidence.
3. Complete rules-faithful payable P0 fixtures C1/K1/K2/K3/F1; handle
   relevant P1 with either executable evidence or explicit approved
   defer/coverage consequence. Transfer every case ID to the exact candidate
   including removed `Last Chance` and added Mayhem/Claws/Drake/Consult.
4. Execute/close actual missing M6 I/J candidate-specific comparison and
   provenance (baseline and three whole-100 portfolios) to the governance
   contract. A mere attested input is not an I/J certification.
5. Write schema-valid prospective M7 decision JSON with exact 100 and all
   verified true gates, run `scripts/grixis_m7_decision_gate.py --check`,
   get exact-head CI. Until gates genuinely pass, do **not** label owner-ready.
6. When complete, present one full Archidekt copy-paste 100 and its exact raw
   SHA for Cory's **single** `Approve`. Only after this may a separate
   narrowly scoped canonical PR/merge/lock touch Marchesa's active state.

No ask for a second owner authorization to perform routine engineering work.
Keep previous 33 M7 locks and every other canonical deck untouched.
