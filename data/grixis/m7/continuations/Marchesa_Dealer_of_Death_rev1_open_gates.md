# Deck 34 M7 Rev1 exact-source continuation ledger

Owner-unapproved exact M7 engineering PR #714, Oct 25, 2026
(America/Chicago). Scope: Marchesa, Dealer of Death **only**.

- Live canonical `corymstover/grixis-commander-encyclopediaGPT@main` still
  approved/locked Oct 15 list raw SHA
  `34a6a940c54aaebde612ae5d3a244e22931d3a977fa26e4c43f2a76aafc0f6b1`.
- Eight-swap current proposed 100 raw SHA
  `931baa2762738ab32cd274ae8e128d0e3cd1aa85e81e51c2faa4934c1c70f363`.
- Baseline, proposed TXT, exact swaps, tradeoffs, 3 complete 100-card
  alternative lists, 24 local tests, and current 100/100 Oracle snapshot: PR #714.
- Exact case-source plan:
  `data/grixis/m6/test_blueprints/Marchesa__Dealer_of_Death.json`;
  design-only at capture. The existing `m6/ij/input_receipts/marchesa-dealer-of-death.json`
  states `phase_b_replayed=false`, `inputs_attested_downstream_incomplete`.
- Status **PROSPECTIVE_APPROVAL_CANDIDATE_PENDING_EXACT_HEAD_CI**. No canonical
  write or owner approval. A scoped 16-case source-bound M7 transfer is recorded
  separately; it does not rewrite historic M6/I/J or claim a full model replay.

## Fresh source and bounded transfer receipts

- Scryfall 2026-10-26 UTC: 100/100 Oracle identities, 100/100 officially
  Commander legal, 100/100 UBR color identity, 0 exceptions. The collection
  endpoint matched 99 cards; the 100th double-faced `Sink into Stupor` was
  resolved by the named endpoint. Includes current Hawkeye's Bow Oracle.
  Snapshot: `data/grixis/m7/oracle_snapshots/Marchesa_Dealer_of_Death_Rev1_Scryfall_20261026.json`.
- A second test file `tests/test_m7_marchesa_dealer_rev1_oracle_snapshot.py`
  source-checks the exact 100 cards and P0/P1 Oracle text. Combined test count:
  24. This is bounded, not a universal game-engine reproduction.
- The scoped disposition of all 16 source blueprint IDs (including K6 removed
  Last Chance and limited E2/W2/W3) is recorded at
  `data/grixis/m7/verification/Marchesa_Dealer_of_Death_Rev1_Scoped_M6_IJ_20261026.json`.
- The structured whole-99 and post-floor source-bound M7 gate packet is
  `data/grixis/m7/decision_reviews/Marchesa__Dealer_of_Death_rev1.json`.
  The latest PR CI must pass its `grixis_m7_decision_gate.py` run.

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

These finite source-anchored unit fixtures encode correct bounded interactions
but lack complete MTG board/stack state transitions. They are **not** a new
historical formal M6 replay, a universal win-rate model, or a global optimum
certificate. The current 100/100 Oracle transaction and scoped M7 case
disposition are completed; historical receipt remains unchanged.

## Next actions, in order

1. Verify PR #714 exact-head CI on 24 bounded tests plus the M7 decision
   packet, resolving failures without changing 100-card membership except via
   a distinct new candidate revision/hash.
2. Confirm current canonical remains unchanged and exact source SHA holds.
3. Present one full Archidekt copy-paste 100 and its exact raw
   SHA for Cory's **single** `Approve`. Only after this may a separate
   narrowly scoped canonical PR/merge/lock touch Marchesa's active state.

No ask for a second owner authorization to perform routine engineering work.
Keep previous 33 M7 locks and every other canonical deck untouched.
