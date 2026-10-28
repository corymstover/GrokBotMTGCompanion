# Wick, the Whorled Mind — Deck #61 M7 Rev1 source-bound verification receipt

**Status:** M7 approval candidate, **not** an owner approval, M6 historical Phase B replay, or canonical replacement. All 61 other locked decks and the Oct15 Wick source are unchanged.

## Authority and finite inventory

- Canonical `corymstover/grixis-commander-encyclopediaGPT/main` approved/locked Oct15 Wick source `refinement/decklists/Wick_the_Whorled_Mind_Approved_2026-10-15.txt`, raw SHA-256 `f4556840dc8f7a8e1d532b73652d0035592b52b86adbbad6ed8fbe4270341e98` (refreshed from live repo 2026-10-27 CT).
- `Wick_Oct15_Authority_Baseline.txt`: vendored exact bytes, immutable input of local fixtures. Baseline approved status belongs only to that preexisting source.
- Proposed exact owner-candidate `data/grixis/m7/candidate_lists/Wick__the_Whorled_Mind_M7_Rev1.txt`, 100 cards, 9 additions/9 removals, raw SHA `1aea08a53b983ee9ce083c1e9c95b366a3abc478a43b75517714d6280b484c48`.
- Full 100-card alternatives `..._alt11.txt` SHA `bb79980af439382f8ff0810efcfdb42ecd80aa5cf6efb8c8f41607c1146e13f1` and `..._alt12.txt` SHA `38b3c4480d5a57a9caf82f6164c0399a1067eebae3b3f3c4c992e6afc83ac58f`.
- `Wick_M7_Rev1_99slot_ledger.csv`: all 99 noncommander physical copies, each with incumbent reason, proposed-cut marker and baseline SHA. Island x2 is the only repeated name in each list.
- `Wick_M7_Rev1_Scryfall_snapshot.json`: source-bound current (2026-10-27 CT) Scryfall `POST /cards/collection` Oracle response for all 111 unique card names present in approved baseline and three proposals. Each record carries original Oracle ID, Oracle text/card faces, Commander legality and color identity; all 111 resolved as Commander legal and U/B/R-compatible. **The snapshot proves its capture, not an automatic verification of any future Oracle/ban-list change.**

## M6 historical I/J to M7 Rev1 exact-source correspondence

Historical Wick M6 I/J intake remains `inputs_attested_downstream_incomplete`, with `phase_b_replayed:false`. The fourteen *original* M6 P0/P1 case definitions were design-only. Accordingly no prior I/J or M6 acceptance is carried forward or described as complete. The new, independently executable **M7-only** `verify.py` reads exact SHA-pinned Oct15, Rev1, alt11 and alt12 cards plus current Oracle snapshot and executes the corresponding bounded rules/counterfactuals against the **proposed Rev1 source**:

| Original case | Tier | Rev1 source-bound executed fixture | Adversarial / result boundary |
| --- | --- | --- | --- |
| C1 | P0 | `test_C1_commander_trigger_and_adversarial_opponent_rat` | Opponent Rat does not trigger Wick; four own Rat entries add four Snail counters. |
| K1 | P0 | `test_K1_snail_last_known_power_and_activation_source_independent` | Activated ability reads sacrificed Snail's last known power even when Wick dies in response. |
| K2 | P0 | `test_K2_type_changers_preserve_snail_and_conspiracy_does_not` | Add-type effects preserve Snail; Conspiracy replaces type and cannot pay Snail cost. |
| K3 | P0 | `test_K3_wick_infect_source_and_cast_window` | Wick deals damage; infect on Snail alone does not make Wick's ability poison. |
| F1 | P0 | `test_F1_actual_three_colors_and_cavern_restriction` | Requires unrestricted U, B and R; Cavern's Rat-colored cast restriction does not fund ability. |
| K4 | P1 | `test_K4_cavern_cast_only_and_K5_ozolith_combat_window` | Distinguishes creature-cast mana from activated-ability mana. |
| K5 | P1 | `test_K4_cavern_cast_only_and_K5_ozolith_combat_window` | Ozolith's delayed combat counter transfer cannot be immediate instant-speed sacrifice recovery. |
| E1 | P1 | `test_E1_growth_requires_rat_entries_and_E2_type_changer` | Rat entry triggers are necessary for Snail growth; merely changing type does not count as entering. |
| E2 | P1 | `test_E1_growth_requires_rat_entries_and_E2_type_changer` | Type changer only causes next newly entering Snail/Rat to trigger Wick if condition met. |
| W1 | P1 | `test_W1_snail_rat_free_outlet_stack_recursion_and_disruption` | Actual pending Wick trigger and free Snail outlet are required; enchantment or commander removal interrupts loop. |
| W2 | P1 | `test_W2_marrow_gnawer_alarm_actual_rat_arithmetic` | Two existing Rats allow sustainability, three allow net growth, given sacrifice-before-count sequencing. |
| W3 | P1 | `test_W3_power_draw_infect_and_deckout_adversary` | A large mandatory draw can lose the game even if the table is damaged; no guaranteed unchecked win. |
| F2 | P1 | `test_F2_snail_or_wick_removed_in_response` | Losing Snail before an entry trigger resolves creates a new 1/1; losing Wick prevents later triggers. |
| F3 | P1 | `test_F3_artifact_vs_enchantment_hate_differentiated` | Distingishes free artifact outlets from enchantment Bombardment and artifact versus enchantment hate. |

Five additional scoped Rev1 swap checks (`test_s01`–`test_s05`) read exact Oracle facts for Rank Rat/Colony, Swarmyard Massacre's tribal protection and unprotected Snail, Yawgmoth life costs, Beseech bargain and always-tapped Malakir Mire, and typed fetch reach. The 18 Python test methods consist of **twelve** source-bound methods mapping all **fourteen** original case IDs (K4/K5 and E1/E2 are grouped), **five** new swap methods, and **one** common 100-card scope/hash/legality method. Thus 18 test methods does not imply 18 independent historical M6 case certifications.

Bounded fixture execution: `python3 data/grixis/m7/wick_rev1/verify.py` — **18 methods passed**. M7 structural execution: `python3 scripts/grixis_m7_decision_gate.py --check --file data/grixis/m7/decision_reviews/Wick__the_Whorled_Mind_rev1.json` — **`M7_STRUCTURALLY_DECISION_READY_NOT_OWNER_APPROVED`**, nine swaps, twelve material candidates, eight-plus real weak slots, two fully manifested higher-count 100s. Both are required again by exact-head GitHub Actions on the integration PR.

**Execution scope limitations:** This is deterministic, card-text-pinned, finite state/cost fixture verification, not a comprehensive MTG rules engine, playtest win rate, opponent metagame probability estimate or inherited M6 I/J replay/Pass C certificate. The original historical M6 I/J downstream status is explicitly *not* changed. New conditional commander interactions are checked in their specific modeled windows; an actual pilot must still account for priority, replacement effects, targeting and available mana in a real game.

## Final M7 strategic decision

The selected nine changes support more certain Rat entry, better interaction, sacrifice/tutor access and earlier colored mana. Real downsides include Yawgmoth paying life, Malakir Mire **always entering tapped** (its front face also loses two life), triple-black Beseech, five-mana Massacre possibly shrinking the Snail, and fetches relying on library search. Two larger portfolios (eleven and twelve swaps) were explicitly constructed and checked, then rejected for losing Ozolith persistent counters, basic Island resilience and Piper's recurring Rat generation. Sword of the Squeak only counts controlled creatures with **base power or base toughness one**; it does not count every Rat without regard to base stats.

**Owner gate:** This candidate is not yet canonically APPROVED/LOCKED and should only be locked after Cory explicitly approves the exact 100 and SHA. The engineering PR remains unmerged until then; a current exact-head passing CI receipt must be linked before asking for approval.
