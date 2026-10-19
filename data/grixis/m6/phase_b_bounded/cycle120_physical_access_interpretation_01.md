# Cycle 120 — Source-physical paired draw exposure (not actual card play)

**Verified evidence:** [GitHub Actions #39190852520](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/39190852520) passed on `c531a4204b6b79277920c2d7b3641d7d27124e22`. Artifact `cycle120-24576-paired-physical-source-access` (ID `12159892585`) records 8,192 seeded paired 99-card-library shuffles for each of the three commander decks. Every unchanged card maps to the same physical index and the removed approved slot aligns with its one-card candidate. The 62-deck approval registry and canonical repository are **not changed**.

## Observed physical access: 7 opening cards + one per turn, no mulligan, turns 1–8

| Commander | Registered named opportunity | T4 qualifying shuffles / 8,192 | T8 qualifying shuffles / 8,192 | T8 proportion and Wilson 95% interval |
|---|---|---:|---:|---|
| Gwendlyn Di Corci | Candidate Aphetto Alchemist physically seen | 895 | 1,268 | 15.4785% [14.7114%, 16.2779%] |
| Gwendlyn | Challenger Alchemist + Pemmin's Aura physically seen | 79 | 160 | 1.9531% [1.6752%, 2.2761%] |
| Gwendlyn | Baseline Opposition Agent physically seen | 895 | 1,268 | 15.4785% [14.7114%, 16.2779%] |
| Nicol Bolas, the Ravager | Opening 7 contains baseline Mox Diamond and another physical land | 554 | 554 | 6.7627% [6.2389%, 7.3270%] |
| Nicol Bolas | Challenger Aetheric Amplifier physically seen | 895 | 1,268 | 15.4785% [14.7114%, 16.2779%] |
| Nicol Bolas | Baseline Mox Diamond and a land among cards seen by checkpoint | 882 | 1,267 | 15.4663% [14.6995%, 16.2655%] |
| Mai and Zuko | Challenger Enigma Jewel physically seen | 895 | 1,268 | 15.4785% [14.7114%, 16.2779%] |
| Mai and Zuko | Challenger Jewel + Basalt Monolith + Rings of Brighthearth physically seen | 6 | 14 | 0.1709% [0.1018%, 0.2867%] |
| Mai and Zuko | Baseline An Offer You Can't Refuse physically seen | 895 | 1,268 | 15.4785% [14.7114%, 16.2779%] |

The conditional Mox hand counts distinguish a *spare land in the seven-card opening hand* from a land merely seen among the first 15 cards. In the latter situation that land may already have been played or spent. Neither value shows Ravager castability. The Mai triple-card count is not a combo, an activation, mana availability, or a winning game.

## Paired method and what it proves

- Exact one-slot difference, 99 physical main cards plus one commander, no duplicate nonbasic names. Same permutation for the two variants; the unmodified 98 slots appear in identical order.
- Per deck, all 8,192 paired shuffles have matching access to the original removed card and its replacement **at precisely the same sample indices and turns**. A one-card swap cannot change the probability of seeing *that slot* in this no-tutor/no-filter model.
- The exact same fixed seed and `m098` registered changed-card index are used across the three decks, so the `1,268` singleton count is identical and cross-deck counts are **correlated**, not 24,576 independent trials for pooled inference. Wilson intervals refer to each 8,192-sample deck only; no multi-deck aggregate CI is warranted.
- A single physical singleton appears in the first 15 cards with theoretical unmodified-deck probability `15/99 ≈ 15.1515%`. Its observed deviation is sampling noise, not a power ranking.
- Each receipt contains at most two auditable sample examples with physical slot IDs and first-seen positions; these do not establish legal spell casts or board presence.

## Preregistration correction disclosed

The original preregistration commit `da4e192be79d2a4f119c370e0714bd34145a336e` registered all nine opportunity names, sample sizes, seed and source IDs. A generator bug used `.add/.cut` against prior Cycle119 source records instead of `.candidate_add/.approved_cut`, serializing seven named required-card entries as `null`. CI first failed a script syntax error, then failed the physical-card presence gate. **Before any successful result**, the planned required-card names were corrected and the reason explicitly recorded under `prereg_correction`. The script now has fail-closed null/wrong-arm name checks and a negative regression test. It would be misleading to describe the original plan as fully correct or to hide this amendment.

## Unresolved gates and no approval

- Does **not** pay actual spell costs, track battlefield/tapped/priority state, automatically resolve Cycle119 rules effects, or simulate actual opponents, tutors, mulligans, bonus card draws or deck-specific tactical policy.
- **Zero** Cycle120 sampled source events were promoted to actual source-paid effect execution. Six Cycle119 conditional fixture *types* remain source-anchored but manually stipulated.
- Does not establish candidate improvement, independent strategic Pass C/I/J, multiplayer Phase B, win probability, full present-day legality or tested-pool zero-improvement.
- No applied changes to canonical 62 decks, approval SHA hashes, legality exception registry or milestone acceptance.
- **Next meaningful M6 prerequisite:** add fail-closed, source-paid actual casting and turn-resource proofs to the sampled access examples, including supported lands, summoning sickness, mana-use restrictions and stack responses. Do not claim a generic seven-plus-turn source package is automatically assembled.

**Recommended interpretation:** The analysis clarifies the frequency at which the commander-specific combos could even start to become accessible under a deliberately restricted draw model. This gives physical evidence for prioritizing further rule-and-resource modeling; it is not itself an optimization verdict.
