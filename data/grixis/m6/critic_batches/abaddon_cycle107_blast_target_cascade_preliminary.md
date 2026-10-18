# Cycle 107 — Legal Bituminous Blast target and printed cascade: preliminary critique

**Review category:** technical engineering author critique, NOT formal independent Pass C, Phase B, tested-pool zero-improvement proof, user-approved swap, or M6 acceptance.

## Exact scope and provenance

- [Preregistered test contract](../phase_b_plans/abaddon_blast_target_cascade_01.json) was committed first at `f14a338ccb8751167809714fd6350c36724e4499`.
- [Full per-seed receipts](../phase_b_bounded/abaddon_blast_target_cascade_01.json), [reproducible compact audit](../phase_b_bounded/abaddon_blast_target_cascade_summary_01.json).
- Approved original Abaddon physical 99+1 source and raw SHA `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf` were preserved; exact archived Bituminous Blast Oracle text was checked.
- Cycle 106 fixed baseline seeds (240) and opening seven cards were matched. A *scripted external opposing 3/3 creature* was supplied expressly to make Bituminous Blast's target legal. This creature is neither a physical card inserted into Abaddon's 100-card deck nor a real modeled opposing 100-card deck.
- Two explicitly counterfactual target policies were tested, each with 240 samples: target persists; or target is externally removed **after** Blast's cast and before its resolution. The latter is an outcome script, not an actual opposing removal spell with verified targeting, mana or priority chain.
- Bituminous Blast's physical ID moves from actual hand, with source-backed printed mana payment, onto the stack and then the graveyard. Printed cascade triggers above the original spell, before the 4-damage instant resolves; target disappearance does not stop independent triggers. Exiled physical library IDs return to the library bottom in a reproducible randomized order.
- Registered adversarial microtests also verify an independent Abaddon-granted second cascade when the commander is on the battlefield and opponents had already lost at least five life before the hand cast, and no retroactive cascade grant when that condition does not hold.

## Results from 240 seeded own-turn baseline samples

| Measurement | No target removal | Target removed after cast |
|---|---:|---:|
| Held with modeled source-affordable mana | 8 | 8 |
| Blast cast from real hand | 7 | 7 |
| Printed cascade triggers resolved | 7 | 7 |
| Eligible lower-mana-value offers | 7 | 7 |
| Scripted opposing 3/3 removed by Blast | 7 | 0 |
| Blast failed to resolve due to illegal target | 0 | 7 |
| Potential value of uncast cascade hits | UNKNOWN | UNKNOWN |

The eight payable opportunities do not imply eight actual casts because the fixed commander-first own-turn spell policy may consume available mana beforehand. The seven found cards were **legally declined** from cascade under a deterministic choice policy and explicitly flagged `UNKNOWN_NOT_ZERO` to prevent false-value comparisons. No hit was modeled as zero-value.

## What remains unresolved

1. **Cascade card quality and downstream game impact:** The printed cascade offers are physically real, but none of the offered card effects was cast/resolved, so true removal/cascade strength and Abaddon follow-up remain unmeasured.
2. **Comparability to Heartless/Tree:** Cycle 106's 7 Heartless casts and 19 Tree casts were under scripted policies without opposing threat/response modeling. The new Blast fixture is intentionally favorable to an instant removal spell with an opposing 3/3 target; it is not equivalent opponent-board modeling for the alternative creatures. Do not compare raw damage, number of resolved effects, or seven legal Blast casts to any candidate as a deck superiority score.
3. **Opponent-state realism:** The external 3/3 is guaranteed by fiat. Actual opponent boards, game stage, blockers, removal windows, creature value, other threats, target immunity/hexproof, damage prevention and priority interactions remain absent.
4. **Limited source/hand policy:** 240 seeded simplified own-turn histories, eight turns with no mulligans, nonland ramp, 99-card spell sequencing, true opponent turns or combo wins. Real access and performance cannot be inferred.
5. **No balanced effect-aware Phase B:** The controlled two-cascade precondition is a passing rules test, not evidence of frequency or relative value in a full game. Unmodeled cascade hits/unknown board responses are decisive open gates under Cycle 105's conservative readiness policy.

## Decision

Keep the 62 canonical lists approved and locked; **retain Bituminous Blast in the current approved Abaddon deck** pending an independently critiqued matched opponent-board effect comparator. No automatic Heartless or Tree addition, no M6 Phase B, formal Pass C/I/J or zero-improvement proof.

**Next discriminating experiment:** classify actual physical cascade offers by card-specific feasibility and *supported* realized follow-through at the same state, using a preregistered unknown-value budget. Include an equal opponent-threat/response fixture for Heartless and Tree and track when Abaddon is on board with relevant cards actually in hand. If too many effects remain unknown, report `CANNOT_EVALUATE` rather than imputing impact.
