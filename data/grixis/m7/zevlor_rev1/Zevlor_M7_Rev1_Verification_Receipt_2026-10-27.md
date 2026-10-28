# Deck #62 Zevlor, Elturel Exile — M7 Rev1 exact-source engineering receipt

**Authority scope:** Cory approved *only* the exact six-swap 100-card Zevlor Rev1 raw SHA `071e9a8b9eaa0f2cfad65f4e7ef05cc5cf0a8b5f74f2221c75d68e6c4dd1bb8f` in the current conversation. The original approved/locked October 15 Zevlor source remains immutable, raw SHA `d2ea6ed8e42ec512b6a6ae7162da8c17b26494b45a9ff6d0c38882c202a42dc9`. Engineering staging and test execution are **not** a canonical lock; that needs an exact-head green canonical pull request and merge.

## Physical source binding and finite checks

- Exact candidate: `data/grixis/m7/candidate_lists/Zevlor__Elturel_Exile_M7_Rev1.txt` — 100 physical cards, 97 distinct names, Island/Mountain/Swamp ×2, 34 dedicated lands, six genuine one-for-one changes.
- Exact alternative 8 swaps: `..._Rev1_alt8.txt` SHA `23518e9c7bf894e7643f946a8801c58a031e99d98750c867305adc4fdb7e8878`; additional Intuition for Worst Fears, Magewright's Stone for Rhystic Study; rejected for losing independently strong uniqueness and draw.
- Exact alternative 9 swaps: `..._Rev1_alt9.txt` SHA `9ffc69741f36ce7a07ce48f5ff9df692d4b326770ed83781c457856196c482da`; further Inside Information for Blasphemous Act; rejected for losing the only unconditional mass creature reset.
- `Zevlor_Oct15_Authority_Baseline.txt` is byte-identical to locked old source. The `Zevlor_M7_Rev1_99slot_ledger.csv` covers all 99 incumbent physical noncommander slots. `Zevlor_M7_Rev1_Scryfall_snapshot.json` captures 108 candidate, original and counterfactual Oracle records from live Scryfall on 2026-10-27, including original Oracle IDs, target wording, color identity, mana cost and Commander legality. All 100 final cards and the two alternative 100s pass those recorded checks. The freeze is not an assertion that future bans cannot occur.
- Exact command: `python3 data/grixis/m7/zevlor_rev1/verify.py` — **23 tests PASS locally**: one full-inventory/SHA/legality, the 16 original case IDs in distinct methods, and six specific addition tests.
- Decision gate: `python3 scripts/grixis_m7_decision_gate.py --check --file data/grixis/m7/decision_reviews/Zevlor__Elturel_Exile_rev1.json` — **PASS locally**, six replacements, eleven material candidates, nine challenged physical weak slots, source-bound eight- and nine-swap full alternatives and count-independent stop.

## Original M6 blueprint → newly run M7 finite fixtures

The historical Zevlor M6 I/J `data/grixis/m6/ij/input_receipts/zevlor-elturel-exile.json` remains `inputs_attested_downstream_incomplete`, `phase_b_replayed:false`. The original `data/grixis/m6/test_blueprints/Zevlor__Elturel_Exile.json` defined **5 P0 and 11 P1** cases but did not certify their execution. These 16 case IDs instead map to new actual M7 tested methods; no historical J is silently backfilled.

| Case | Tier | Source-bound test method suffix in `verify.py` | Actual adverse/negative condition |
|---|---|---|---|
| C1 | P0 | `test_C1_haste_zone_activate_tap_and_source_paid_two` | Not on battlefield, tapped, without haste, or one generic mana fails activation |
| K1 | P0 | `test_K1_only_one_real_opponent_or_opponent_controlled_permanent` | Own-player target or multi-target set does not consume Zevlor watch |
| K2 | P0 | `test_K2_copies_are_not_cast_but_each_magecraft_triggers` | Two copies are never additional spell casts; cast-only effects receive one event |
| K3 | P0 | `test_K3_countered_original_does_not_erase_delayed_copies` | Countered original has its own graveyard zone; no Zevlor watch means no copies |
| F1 | P0 | `test_F1_no_claim_of_automatic_compact_win` | Triple no-gift hand exiles do not reduce opponent life or assert deterministic kill |
| K4 | P1 | `test_K4_copy_retains_x_mode_and_paid_gift_choice` | Insufficient X mana fails; unpaid Gift cannot be added to copied spell |
| K5 | P1 | `test_K5_bracers_separate_watches_one_cast_no_free_repeat` | One paid/tapped activation creates two watches with Bracers, not a phantom second tap |
| K6 | P1 | `test_K6_twinning_staff_one_additional_per_copy_event` | Staff adds one to each Zevlor copy event and no recursive cast/copy multiplication |
| K7 | P1 | `test_K7_swiftfoot_hexproof_allows_own_untap_greaves_shroud_does_not` | Shrouded target cannot receive Minamo/Seal own-target activation |
| E1 | P1 | `test_E1_payment_cast_valid_copy_sequence_and_negated_precondition` | Must pay two for commander activation *and* 1B for targeted End of the Hunt |
| E2 | P1 | `test_E2_support_training_omen_pemmin_seal_minamo_bracers_staff` | Omen's CU is ability-only; cannot be counted as free mana for Rousing spell casts |
| W1 | P1 | `test_W1_multiplied_payloads_captures_three_distinct_opponents` | No legal permanent to target gives no fantasy copy; three actual opponents are distinct |
| W2 | P1 | `test_W2_magecraft_witch_and_artist_real_copy_counts` | Only one cast, though Witch/Artist each see three cast-or-copy events |
| W3 | P1 | `test_W3_omen_hawker_pemmin_colorless_loop_not_colored_freecasting` | Hawker enchanted by Pemmin nets bounded colorless ability-only mana, not colored spell mana |
| F2 | P1 | `test_F2_sorcery_priority_cast_window_and_turn_boundaries` | Heist sorcery cannot cast outside sorcery window; unused watches expire end of turn |
| F3 | P1 | `test_F3_only_actual_target_not_multiple_or_untargeted_copy` | Own target and two-target sets are ineligible; no target also fails |

The six addition checks `test_s01` to `test_s06` cover greatest-mana-value edict vs artifact answer; opponent's choice and graveyard; three separate Gifts own-library partitions; source-paid red ritual and vanishing copy suspension; X=0 card filtering and real UR payment; and no-gift hand exiles without stolen-card cast permission.

**Limits:** This is an explicitly scoped finite state/stack/cost/zone test battery, not a comprehensive Magic rules engine, metagame simulation or proof of an optimal win-rate. The owner approval is already on record, but the exact engineering GitHub Actions run and later canonical certification transfer are separate required gates.
