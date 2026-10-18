# Cycle 97 — Abaddon real-library cascade coverage review (preliminary)

**Date:** 2026-10-17  
**Reviewer:** ChatGPT, authoring-cycle self-critique; **NOT an independent named Pass C judgment**.  
**Scope:** M6 experimental evidence only. No swap, phase completion, approval, certification or decklist mutation.

## Traceable inputs

- Approved Abaddon baseline logical list: `lh1:5a1e5e5bb86ba35d7dbf712fbc3a7d29c3e05a17569c05e8a11976321699b793`
- Frozen source TXT SHA-256: `5448d76193923a3f9e3d4c41a327eaeaa9c6326d484d8e5a9abaf3852db2efff`
- Plan: [abaddon_real_library_replay_01.json](../phase_b_plans/abaddon_real_library_replay_01.json)
- Evidence: [abaddon_real_library_replay_01.json](../phase_b_bounded/abaddon_real_library_replay_01.json)
- Deterministic 240 per hypothesis per response profile, seed 97017; source/M3 v1.1 freeze, matched 99-index permutations and identical fixed 96-card residual-library orders after forced holding of Boltwave, Flame Rift and the swapped card.
- Comparison is against Bituminous Blast for both Heartless Hidetsugu and Tree of Perdition. Every accepted canonical deck remains unchanged.

## Observed support coverage (not card strength)

| Fixed no-removal scenario | Offered cascade hits | Supported hit casts | Unmodeled hits declined |
|---|---:|---:|---:|
| Approved Bituminous Blast | 480 | 44 (9.17%) | 436 (90.83%) |
| Heartless Hidetsugu | 480 | 17 (3.54%) | 463 (96.46%) |
| Tree of Perdition | 480 | 10 (2.08%) | 470 (97.92%) |

In the *hypothetical source-removal-before-next-activation* scenario, the approved baseline is unchanged (44/480 supported), while Heartless has 17/240 supported (7.08%) and Tree has 10/240 supported (4.17%). **Do not rank the configurations on these percentages**: the baseline uses printed plus Abaddon-granted cascade for the five-mana spell; challengers use one cascade on casting the creature, and another only after a surviving next-turn activation enables the follow-up two-mana Flame Rift. Cascade mana-value ceilings differ. These are conditional traces, not sampled draws or independent games.

## Valid conclusions

1. Every scenario uses real frozen Scryfall mana-value/land metadata for the entire 99-card list, with a matching 96-card residual library after three explicit forced-hand cards are excluded. CI recomputes the whole result, verifies matching original-deck traces across the two swaps and passes M6-only authority checks.
2. The structured supported subset can resolve some real cascade hits and tracks triggered cascade separately from printed cascade. A scripted spell can generate different numbers of cascade triggers depending on turn-local life loss, prior deployment and survival.
3. The complete remaining original deck is **not** behaviorally modeled. The experiment conservatively declines most hits; therefore it **cannot** support a Heartless/Tree improvement ranking, zero-improvement certificate, real deck win-rate, deckwide effect-aware paired Phase-B determination or formal independent Pass C judgment.
4. This is engineering verification only. M6 remains unaccepted; M7/M8 remain pending; the 62 canonical decks stay approved and locked.

## Important red-team limitations

- Abaddon in play, both other spells in hand, unlimited prior setup and explicitly injected turn-six/turn-seven mana are *forced*. The 240 repetitions sample cascade-library order only; they do not estimate how often the board state or mana appears.
- Nearly all cascade offers are **unsupported**. Declining those casts is a conservative policy for the interpreter, **not** a plausible optimized Magic play policy.
- Multiple source casts and hand spell origins are tracked; sampled opponents do not exercise priority, counterspells, removals, artifact/graveyard hate or combat.
- Split, modal, alternate-cost, suspend, damage prevention, mana-ability and battlefield-trigger mechanics beyond the exact Cycle-96 subset still need explicit Oracle-derived correctness checks before modeled use.
- 'Supported hit cast' does not imply that a sequence is strategically useful or wins. Hit distributions differ with cascade MV and are not interchangeable outcome measures.

## Next gate

Expand source-verified, explicitly implemented card-effect coverage for the highest-impact eligible cascade-hit categories **without pretending that generic cards can be represented by a proxy**. Repeat identical paired traces and report how much unsupported mass remains. After that, implement actual hand/mana/casting policy and stochastic response assumptions, verify them independently, then perform real Phase-B, named Pass C, I/J receipts and human decisions for Abaddon **and all 61 other commanders**. Do not use this note as an independent critic signoff.
