# Cycle 98 — Abaddon ten-effect coverage audit (preliminary)

**Status:** CI validated, frozen-Oracle checks passed, deterministic paired replay verified.  
**Review category:** Authors' evidence-coverage critique only; **NOT** an independent or formal named Pass C judgment.  
**Authority:** Evidence-only. Never change canonical 62 decks, approvals, exception records or M6 acceptance based on this analysis.

## Source and evolution

- Frozen canonical Abaddon logical hash: `lh1:5a1e5e5bb86ba35d7dbf712fbc3a7d29c3e05a17569c05e8a11976321699b793`.
- Frozen TXT export SHA-256: `5448d76193923a3f9e3d4c41a327eaeaa9c6326d484d8e5a9abaf3852db2efff`.
- [Cycle 97 accepted baseline evidence](../phase_b_bounded/abaddon_real_library_replay_01.json); [Cycle 98 preregistration](../phase_b_plans/abaddon_effect_coverage_01.json); [Cycle 98 new evidence](../phase_b_bounded/abaddon_effect_coverage_01.json).
- Oracle checks were reconciled to the *actual frozen October 2026* "this artifact" wording for Lotus Petal and the Talismans after a deliberate fail-closed CI mismatch. The initial plan remains available in Git history; neither the card effects nor seed, pairings, profiles or metric policy changed.
- Brainstorm can legally put the scripted Flame Rift back into the library. A second fail-closed test caught Cycle 97's assumption that it would remain in hand. The new replay counts this as `fixed_followup_not_held` and does not invent a cast; **the accepted Cycle 97 replay is unchanged**.

## Results, no-removal profile (240 fixed-seed full-99 shuffles per comparison)

| Fixed scripted configuration | C97 supported/offered | C98 supported/offered | C98 unsupported/offered |
|---|---:|---:|---:|
| Approved Bituminous Blast baseline | 44/480 (9.2%) | 140/480 (29.2%) | 340/480 (70.8%) |
| Heartless Hidetsugu replacement | 17/480 (3.5%) | 141/475 (29.7%) | 334/475 (70.3%) |
| Tree of Perdition replacement | 10/480 (2.1%) | 142/474 (30.0%) | 332/474 (70.0%) |

Do not compare these rows as deck power. Offers differ after Brainstorm changes the forced follow-up hand and because slot mana values affect cascade ceilings. "Supported cast" means the finite interpreter resolved that hit, not that the result was strategically beneficial.

Under scripted pre-activation source removal, the baseline remains 140/480 supported; Heartless produces 65/240 supported, Tree 68/240. These scripted differences reflect available triggers and card-effect coverage, not actual removal probabilities or deck matchup performance.

## Precisely expanded scope

The interpreter now handles **ten more named effects** under rigid recorded choices: Sol Ring; Arcane Signet; Lotus Petal; Talisman of Creativity, Dominance, and Indulgence; Dark Ritual; Rite of Flame; Brainstorm; Ponder.

Checks include actual frozen Oracle text and MV; mana payment and activation; artifact tap/sacrifice; Talisman damage to pilot only (not opponents); fixed Brainstorm/Ponder choice policies; exact ritual resolution within recorded graveyard assumptions; and conservative noncasts for unmodeled offers.

The new artifacts are **not automatically tapped or chosen as ramp during replay**. This run records legitimate entry/cast effects and verifies their activated mana behavior separately. Do not describe the support increase as an increase in simulated actual mana advantage.

## Unclosed blockers

1. About **70% of the observed no-removal offers** are still unsupported and deliberately declined, including high-impact tutors, counters, cantrips/combo pieces and replacement interactions. An unsupported offer cannot be assigned zero real gameplay benefit or declared bad.
2. The replay forces Abaddon onto the battlefield, chooses a specific three-card hand, injects mana each turn and uses one predetermined policy for Brainstorm/Ponder. It is **not** an opening-hand/deck-development simulation or opponent-reactive game.
3. More supported casts do not identify the strongest candidate. Cascade randomization, real hand access, timing, full mana resources, response windows, available targets, spell value, printed double cascade and other commander hooks remain incompletely tested.
4. No formal independent Pass C, accepted Phase B, I/J reproducibility/improvement certificate, tested-pool zero-improvement certification, M6 acceptance or user swap authorization follows from Cycle 98.

## Next

Expand support only for source-verified, high-impact card abilities where actual target/stack/graveyard details can be modeled and audited. Prioritize **accuracy and stateful choice policies**, not maximizing the supported-hit percentage. Then move from the forced 3-card hand to a real hand/land/mana/commander state with perturbations and paired deckwide evidence. All 62 commanders require their own commander-first evaluation.
