# Abaddon — source-paid Lost/Keeper cast and fetch payoff receipts

**Date:** 2026-10-22. **Stage:** M6.6 bounded deterministic effect-awareness; **NOT** a measured upgrade, Oracle-all-100 certification or M6/M7 milestone approval.  
**Canonical approved 100 SHA-256:** `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf` — remains APPROVED/LOCKED and unmodified.  
**Pre-implementation plan commit:** `39801f15f7a0b2b86d35a56428ebb26f29830200`, `data/grixis/m6/phase_b_plans/abaddon_lost_keeper_effect_20261022.json`.  
**Implementation:** `tests/test_m6_abaddon_lost_keeper_effect.py`; exact tests in M7 CI on this PR; run result must be checked separately. No new Monte Carlo trials.

## Decision target

Merged M7 V2 proposed `+Grinning Ignus,+Chaos Warp/-Rakdos,-Keeper` provisionally, with an alternate `-Inevitable Betrayal` cut that preserves Keeper. The meaningful choice is **not** solely six-MV Keeper versus three-MV Lost. Both actual 100-card V2 challengers *retain* `The Lost and the Damned` ({1}{U}{R}; MV3). The second deck retains `Keeper of Secrets` ({5}{R}; MV6). This study isolates precisely what retaining Keeper adds to a cascade hit; it cannot decide Betrayal's MV0 cascade value or Rakdos's loss-scaling discounts.

The source-backed rules are:

- `The Lost and the Damned`: *each* spell actually cast outside hand or land entering under your control from outside hand creates one 3/3 red Spawn (unless an opposing effect suppresses the trigger or token creation). An Ignus cast **from hand** does not do this, and an uncast cascade hit cannot. A source-paid fetchland retrieving typed land **from library** does.
- `Keeper of Secrets`: each spell **cast** outside hand triggers damage equal to that spell's MV to **target opponent**, not each opponent. An actual `Sol Ring` MV1 cascade cast grants one targeted damage if Keeper is present; an MV0 suspend spell grants a damage trigger resolving for zero if target is legal. The damage contributes to Abaddon's current-turn aggregate threshold only after the trigger resolves; it cannot retroactively affect the casting spell's cascade eligibility.
- Both cast-triggered abilities trigger even if the hit is later countered; ordinary *countering the spell* does not undo them. Removing Keeper or Lost before the cast prevents those new triggers; removal after they have triggered does not erase them.
- `Grinning Ignus` has a sorcery-timing mana ability that does **not** use the stack: Wizards' [Time Spiral Remastered notes](https://magic.wizards.com/en/news/feature/time-spiral-remastered-release-notes-2021-03-23). The available prior `ignus_stack_windows` fixture is reused with no revised rules assumption.

Public Oracle text and legality sources checked October 22: [The Lost and the Damned](https://mtg.wtf/card/40k/129%25E2%2598%2585/The-Lost-and-the-Damned); [Keeper of Secrets](https://mtg.wtf/card/40k/78/Keeper-of-Secrets); [Call Forth the Tempest](https://spellrack.com/cards/0623c51a-e829-413f-a3a0-817c0902821e). The original accepted 94-name October-12 Scryfall audit is separate; this is a **targeted rules check**, not 100 fresh Oracle requests.

## Exact physical opponents and cases

Libraries: `data/grixis/m7/research_challengers/Abaddon_the_Despoiler_v2_engine_answer_keeper.txt` and `..._v2_engine_answer_betrayal.txt`. Each: 100 main cards including one Abaddon, 99 physical library cards, only the basic Island/Mountain/Swamp duplicates, 34 lands. The prearranged conditional battlefield includes Birgi, Abaddon, Loyal Subordinate and Lost, plus Keeper **only if it is physically present in that variant**. Sol Ring is moved physically to the top of the real candidate deck as first Ignus cascade hit. The source-paid spell uses three actual prearranged colored mana sources and X=9 established by a legitimate previous Loyal beginning-of-combat trigger, not fabricated life loss. `assert_conserved` checks all 99 named physical cards after each legal zone move.

| Precommitted case | Source event | Lost Spawn when controlled | Keeper targeted damage (when controlled) |
| --- | --- | ---: | ---: |
| legal_cast_supported_hit | Actual source-paid Ignus from hand → legal MV1 Sol Ring cast from exile | 1 | 1 |
| drannith_bars_exile_cast | Drannith prevents casting the exiled hit | 0 | 0 |
| rule_of_law_bars_exile_cast | First Ignus already counts as spell; second exile cast prohibited | 0 | 0 |
| countered_nonhand_spell_still_triggers | Actual paid Ignus plus physical Sol Ring exiled and **cast**, opponent counters Sol Ring into grave; no Sol Ring effect/ETB | 1 | 1 |
| hand_cast_ignus_only | Hand spell event alone, no nonhand hit cast | 0 | 0 |
| nonhand_fetchland_entry | Physically source-correct Polluted Delta from hand sacrificed, typed Island/Swamp fetched from library enters | 1 | 0 |
| hand_land_entry_no_spawn | Polluted Delta itself entered from hand | 0 | 0 |

Zero-MV spell-cast control: MV0 exile spell still causes Spawn but deals **zero** Keeper damage. Any statement that a zero-MV hit contributes opponent damage from Keeper would be false. State snapshots have **conditional availability**: no claims about opening-hand occurrence, opponent mana, spell-protection density or winning probability.

## Interpretation and fail-closed next action

This is a bounded effect audit of **one** source-paid first cascade hit and one real fetch target. It makes the Keeper cut's opportunity cost **explicit**: choosing `-Keeper` sacrifices repeatable, single-opponent life-loss amplification from nonhand spell casts that can compound Abaddon's own threshold and damage finish. This is not erased by keeping Lost; Spawn bodies cannot stand in for immediate targeted damage. Conversely, cutting `Inevitable Betrayal` loses a potent MV0 cascade target and may alter the physical hit distribution. The current lead **must remain provisional** until those independent costs are evaluated and current Oracle/legality is refreshed for the final 100.

Certification ledger: M6.5 completed by the owner's non-independent Pass C waiver; M6.6/7 still PARTIAL, M6.8/9/10 BLOCKED; new M7 owner approvals 0/62. No canonical mutations or exceptions.
