# Cycle 106 — Abaddon physical-slot comparison: preliminary critic review

**Classification:** authored engineering critique and deterministic bounded test, **NOT** a completed independent Pass C or M6 Phase B; no approved swap, zero-improvement certificate, or deck modification.

## Source and experiment

- [Preregistered scope](../phase_b_plans/abaddon_physical_slot_01.json) committed **before** implementation at `d928ddf03fa571c88c9b1186b085547b5352dae9`.
- [Detailed per-trial evidence](../phase_b_bounded/abaddon_physical_slot_01.json) and [source-generated compact summary](../phase_b_bounded/abaddon_physical_slot_summary_01.json).
- Authority locked: approved Abaddon raw SHA-256 `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`; approved source TXT SHA `5448d76193923a3f9e3d4c41a327eaeaa9c6326d484d8e5a9abaf3852db2efff`.
- 240 fixed-seed 7-card openings with eight natural controller-turn draws for each of three 100-card lists: approved Bituminous Blast slot, Heartless Hidetsugu replacing that **exact physical slot**, and Tree of Perdition replacing that same slot. Card identities and registered mana costs were checked against the pinned October Scryfall source.
- Same physical source slot and seeds means all three start with paired initial hands, except the specified replaced card. Fetchland searches can alter later draw order, but the modeled land choices in these three variants generated the same number of fetch shuffles under the fixed policy. This is *not* a full probability or performance model.
- All three states contain a real Abaddon commander, and every main library has 99 physical cards. Only registered lands produce mana; exact colored sources pay observed casts. The fixed own-turn **commander-first** policy prioritizes Abaddon over casting the slot when both could be paid.

## Actual, narrow observed result

| Measured event across 240 paired seed samples | Approved Blast | Heartless alternative | Tree alternative |
|---|---:|---:|---:|
| Slot physically seen in sampled cards | 26 | 26 | 26 |
| Slot held with payable modeled land sources | 8 | 8 | 19 |
| Supported creature cast and put onto battlefield | not modeled (Blast) | 7 | 19 |
| Eligible candidate tap activation by turn 8 (no haste) | not applicable | 4 | 16 |
| Abaddon actually cast from command under fixed land policy | 126 | 126 | 126 |
| Candidate activation with confirmed Abaddon-present, payable Boltwave/Flame Rift in hand | 0 | 0 | 0 |

Heartless's conditional nonprevented ability when legally activated deals floor(half life) to all players; an opponent's scripted removal after activating cannot undo that ability on the stack. Tree's 0/13 exchange affects a single target opponent's life and **fails** after a source-removal outcome before resolution. Both require surviving a full turn without haste. Three named opponent response branches are **externally scripted counterfactuals**, not legally executed removal spells or survival probabilities.

## Why this is NOT a fair comparative power test yet

1. **Asymmetric model coverage:** Bituminous Blast is an instant requiring a legal creature target and has **printed cascade**. No opponent creature targets or eligible cascade-hit effects are fully represented in this own-turn access policy. Thus Blast was **never cast** by the model, even when eight held-and-source-payable opportunities existed. The zero cast count for Blast is a **model refusal**, not a real inability, poor card value, or grounds for replacing it. Candidate creature casting was physically executed, so the numerical outcomes must NOT be treated as symmetrical candidate-versus-baseline effects.
2. **Artificial spell choice priority:** Commander-first and at-most-one tested nonland cast each turn were deliberately fixed for tractable comparison. This suppresses other realistic lines and produces identical commander casting (126/240) despite different slot usage. It cannot establish a beneficial deck performance change.
3. **Very incomplete mana acceleration:** Rocks, free mana artifacts, rituals, Treasures, reductions and other cards in the approved list are not modeled as available mana in the access policy. It should not be compared to prior M3 v1.1 commander turn-four access rates, which used different features and turn ranges.
4. **Conditional activation is not an Abaddon benefit:** Raising X to a large value is not equivalent to legal cascade follow-through. Real opponents may die or prevent damage, the pilot may be damaged, the creature may be removed, the commander may be absent, and no relevant next spell might be in hand. Here **zero** sampled activations led to a source-payable Boltwave or Flame Rift follow-up with Abaddon present; almost all other 99-card effects remain unmodeled, so this cannot prove such lines do not occur in real games.
5. **No true opponent or win policy:** Board presence, blockers, creature targets, interaction resources, actual opponent turns, mulligans, lifelink/replacement/protection and full legal state-based actions are absent. Do not infer win probability, expected removal survival, opponent threat or Bracket change.
6. **No confirmed best candidate:** A few Heartless/Tree source-backed cast/activation opportunities do not outweigh unquantified Blast removal and printed-cascade value; the appropriate verdict is `CANNOT_EVALUATE_RELATIVE_DECK_STRENGTH`, not improvement, tie, or zero improvement.

## Engineering next gate, focused on actual commander-first strategy

To turn this into defensible **Phase B** rather than repeating access measurements, design a finite, adversarial *balanced* value comparator: give Bituminous Blast actual legal creature targets with explicitly defined board states, resolve real printed and Abaddon-granted cascades from the current physical library, and implement enough hit effect/value categories that unknowns can be bounded rather than silently zeroed. Include realistic spell/rock/ritual mana development, opponent removal windows and actual hand-held follow-up casts in the same causal timeline. Every unsupported spell or priority interaction should be marked `cannot_evaluate` under a preregistered unknown budget. Seek a truly independent rules/strategy critic before a card proposal.

**Approval position:** RETAIN the protected approved Bituminous Blast baseline; do **not** approve Heartless, Tree, or an alternate removal of Birgi/Kessig based on this test. This is a hold for further evidence, **not** a proof that no improvement exists. Canonical 62/62 locked decks and M6 pending status remain unchanged.
