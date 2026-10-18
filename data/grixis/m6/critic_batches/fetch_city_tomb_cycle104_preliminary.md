# Cycle 104 — Fetch, City, Tomb: preliminary engineering critique

**Review status:** technical author-side audit, NOT a named independent Pass C or I/J formal certificate; no deck swap or milestone acceptance is authorized.

## Inputs and preregistration

- [Cycle 104 preregistration](../phase_b_plans/fetch_city_tomb_62_01.json) committed **before** tests and model implementation (initial plan commit `2e5795194fe859587558ed55c458085774076a25`).
- [Detailed reproducible evidence](../phase_b_bounded/fetch_city_tomb_62_01.json) and [compact evidence index](../phase_b_bounded/fetch_city_tomb_62_summary_01.json).
- All **12 new lands** verified against SHA-256-locked October 2026 Scryfall Oracle: 10 fetchlands, City of Brass and Ancient Tomb.
- Frozen authority: all **62 current approved and locked canonical lists unchanged**; current registry M6 in progress. Previous versions of the simulator and recorded Cycle 103 evidence remain unchanged.

## Actual finite-model behavior

1. **Fetchlands:** ten legal printed subtype search classes. Paying one life, tapping and sacrificing the physical land happens as activation cost, *before* ability goes on the stack. Opponents may pass, and the search/physical-library shuffle resolves after four passes. The selected physical library land enters battlefield with its modeled tapped/untapped/shock choice. The land found does not use an additional land play. Fetch target choice is deterministic (modeled untapped, greatest mana flexibility, then alphabetic), not an optimal Commander strategy. Unmodeled printed-typed targets are excluded from this deliberately incomplete target pool; tests do not establish complete strategic fetch legality.
2. **Ancient Tomb:** mana ability adds **{C}{C}**, with **2 damage to the controller immediately**, not with a stack trigger. Physical mana source payment can use the two colorless units for a two-generic Arcane Signet, while preserving source ID, tapped state and the controller life total.
3. **City of Brass:** tap gives flexible mana immediately but separately creates a **one-damage-to-controller trigger**; the four-seat stack pass policy resolves this later. The damage trigger can resolve even if the land itself is removed, and is placed above a card cast using the land in the bounded policy. City damage does not raise Abaddon's opponent-life-loss threshold.
4. Atomic source and card identity invariants protect against illegal activations, incorrect mana colors, duplicate cards, missed priority windows and partially paid costs.

## Reproduced experimental coverage, not performance

The same 62 x 12 = **744** initial seeds/opening seven-card hands were used as Cycle 103. **Later draws are intentionally not forced equal:** actual fetchland search shuffles legitimately change subsequent card order. The system recorded:

| Measurement | Cycle 103 | Cycle 104 |
|---|---:|---:|
| 62-deck samples | 744 | 744 |
| Arcane Signet seen | 96 | 93 |
| Arcane Signet physically cast from modeled sources | 51 | 75 |
| Fetch abilities resolved | not modeled | 468 |
| Distinct samples with post-search draw divergence | not modeled | 323 |
| City damage trigger resolutions | not modeled | 4 |
| Ancient Tomb mana activations | not modeled | 8 |

The number of Signet casts measures capability of a limited, fixed four-turn land-and-Signet policy. It **must not** be interpreted as a deck power comparison, probability of good mana, win-rate or evidence for a deck upgrade. The 93 versus 96 Signet-visibility difference is expected under post-search shuffles, so only initial hands are strictly paired.

## Limitations and risks

- Only 10 fetchland names and the 19 Cycle 103 modeled nonbasic mana lands plus basics are included in fetch targets. Other cards with a basic land subtype and utility effects remain unmodeled, so choosing a modeled target is a conservative simulated decision, **not** proof of the full legal or strategically optimal search choices.
- City and Tomb controller damage is bounded under no prevention/replacement and no life-ending actions. Lethal cases deliberately fail closed; full death triggers and state-based actions remain absent.
- No full multiplayer priority engine, opponents' spells, mulligans, complete turn progression, extra card selection, attack decisions, commander-specific tutors, cascade execution, or actual combo strategy value.
- The simulated player automatically activates fetchlands on its own main phase if modeled legal. This is a fixed heuristic and not an opponent-responsive Magic policy.
- This does not complete M6 Phase B, formal independent Pass C/I/J, deck-specific optimization, any tested-pool zero-improvement certificate, human approval or M8 final exports.

## Next meaningful gate

Audit which unmodeled source/value mechanics are truly bottlenecking real commander-first decisions, not just Arcane Signet execution. The most valuable next work may be a **measurable Abaddon commander-specific cast/cascade decision evaluation** attached to this exact physical state, with explicit unmodeled outcome boundaries and a skeptic review, rather than another unbounded expansion of mana-source coverage. Preserve all 62 approved lists unless the user explicitly approves exact upgrades.
