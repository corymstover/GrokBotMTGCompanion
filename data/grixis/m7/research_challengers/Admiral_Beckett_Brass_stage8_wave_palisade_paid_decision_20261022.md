# Admiral Beckett Brass — stage 8 decision-grade Wave/Palisade paid-state comparison (2026-10-22)

**Status: RESEARCH_ONLY / PROVISIONAL STRATEGIC CHOICE, owner approval withheld.** Canonical approved Admiral remains locked at raw SHA-256 `4ba5c483eb67b5f2647d375450adf9c2b7e79a036d0ba1866e58de8441bf3414`. The formerly presented five-change D packet remains withdrawn from owner-ready status; its M6 I/J bound evidence does **not** automatically certify the stage-7 variants. The authoritative source snapshots here are the existing 121-name canonical/challenger Scryfall set and stage-3 eleven-name fresh paid-role set.

## A genuinely decision-changing question

Does Admiral gain more **same-player three-Pirate theft conversion per paid turn without sacrificing durable draw or instant defense** by adding `Cosmotronic Wave` in place of `Raise the Palisade` than by cutting `Fiery Cannonade`? And is switching `Kari Zev, Skyship Raider` to `Storm Fleet Aerialist` a consistent enough actual connection improvement to justify losing Kari's second combat body?

Both new Wave-for-Palisade packages are full physical 100-card sources:
- `Admiral_Beckett_Brass_six_Wave_Palisade_draw_resilient_20261022.txt`: original D five plus Wave IN / Palisade OUT. Six changes from canonical; **Bident, The Indomitable, Kindred Discovery, March, Path, Open and instant Cannonade remain**.
- `Admiral_Beckett_Brass_seven_Aerialist_Wave_Palisade_draw_resilient_20261022.txt`: above plus Aerialist IN / Kari Zev OUT. Seven changes. Same draw/recursion/instant-defense preservation, but Kari's menace/first strike/Monkey token lost.

Competing complete 100s include previous `six_Cosmotronic_Wave` (Wave in, **Cannonade** out), `six_Aerialist_draw_resilient` (Aerialist in, Kari out; Palisade and Cannonade preserved), `seven_Aerialist_Wave_draw_resilient` (Wave/Cannonade and Aerialist/Kari), the exact D baseline, seven Regalia/Wave and eight/nine Regalia combinations. No extra changes are justified merely to increase the total.

## Four source-bound marginal effects, including actual payable mana

| Real state | Wave instead of Palisade, retain Cannonade | Palisade instead of Cannonade, retain Palisade | Decision |
|---|---|---|---|
| 3 ready Pirates, three opposing **non-Pirate 4/4** blockers, active-player precombat, four total mana incl. R | Wave `{3}{R}` resolves, opposing creatures cannot block *this turn*: three Pirate hits; 1 damage does not kill 4/4 blockers | Palisade `{4}{U}` cannot be paid with four mana; Cannonade `{2}{R}` 2 damage also cannot remove 4/4 blockers | **Wave has a one-turn earlier theft-enabling window** |
| Same setup, five mana including U and R | Wave yields three hits; defenders survive into following turns | Palisade chooses Pirate, returns non-Pirate creatures to hands, three hits, and defenders stay away until recast | **Palisade wins persistent board reset/resource-tempo dimension**, not necessarily immediate threshold |
| 3 ready Pirates, defending opponent controls **three Pirate blockers**, adequate mana | Wave prohibits blocking regardless of blockers' creature type; three hits if no removal/fog | Palisade choosing Pirate keeps opposing Pirate blockers, denying three connections; choosing another type also bounces our Pirates | **Wave strictly more reliable in Pirate/mirror-style blocker setup** |
| 3 ready Pirates, four blockers (two big non-Pirates and two Pirates) | Wave stops every blocker for this turn: three Pirates may hit | Palisade choosing Pirate bounces two non-Pirate blockers, leaves two Pirate blockers: only one guaranteed unblocked | **Wave superior for the exact same-player threshold here** |
| Opponent turn, three 2-toughness non-Pirate attacking creatures, our Pirates in play | The preserved Cannonade can be cast as a three-mana instant during combat and kill small non-Pirates without damaging Pirate attackers | If Cannonade was the cut, Wave and Palisade are sorceries and cannot fill this exact instant defensive role | **Keep Cannonade**, unless strong opposing evidence justifies the loss |
| Following turn without opponents replaying a previously bounced 5-toughness blocker | Wave's effect ended: blocker remains for subsequent combats | Palisade's bounce leaves no blocker on battlefield if it has not been recast | **Palisade has the longer-term advantage**; not guaranteed against cheap re-deployment |
| Exactly three qualifying attacking Pirate damage sources but one removed or combat prevented in response; or Admiral absent by end step | In every package, theft prerequisite/triggers may fail | Same | **No mass-evasion spell guarantees theft or protects Admiral on its own** |

All source bindings are exact: Wave is `{3}{R}` sorcery (1 damage and *one-turn* cannot-block); Palisade `{4}{U}` sorcery (bounce creatures other than chosen type); Cannonade `{2}{R}` **instant** (2 to non-Pirate creatures); Open at X=3 costs `{3}{U}{U}` and can grant three unblockability + three on-hit draws. These are deterministic hypothetical *resolved-spell* configurations, not samples of four-player game frequency. Opponent priority/removal, legal blocking restrictions, commander timing, and per-spell payment are explicitly outside the simplified blocker-count function except where stated. `tests/test_m7_admiral_stage8_wave_palisade_paid_combat.py` encodes the bounded facts and explanatory limits.

## Author decision, independent of a numerical swap target

**Provisional leading research configuration: six_Wave_Palisade_draw_resilient (6 strategic replacements).** The specific replacement `Cosmotronic Wave` IN / `Raise the Palisade` OUT is **SELECT_ADD as the next candidate-bound research choice**, because it trades a one-mana more expensive non-Pirate bounce for a cheaper color-flexible blanket can't-block effect that works through Pirate blockers and retains Cannonade's unique instant job. This is a relative, commander-first conclusion for the present opportunity pool, **not** a statement of global optimum or final owner-ready acceptance. If the metagame's persistent mass creature bounce / recast-tax function makes Palisade demonstrably more valuable, reverse the choice; record that as a material sensitivity.

**Aerialist against Kari: RETAIN_ALTERNATIVE, not selected in the leading six-change list.** Both printed cards are Pirates. Aerialist makes flying rather than menace and can enter larger after an earlier attack, but Kari attacks with first strike/menace and creates an additional attacking non-Pirate Monkey. That Monkey does not help Admiral's three-Pirate hit requirement, but is a real attack / sacrifice / artifact-adjacent pressure piece and draws cards from Bident or The Indomitable if it hits. Against a single flying blocker and no other defenders, Kari's menace can outperform Aerialist; against two ground blockers and open skies the reverse can occur. There is insufficient evidence to discard the richer baseline payoff solely because Aerialist's EDHREC *lift* ratio is high. The full seven-change research source is preserved for future reevaluation.

**Wave-for-Cannonade: RETAIN_ALTERNATIVE, not primary.** It preserves Palisade's long-term reset and adds Wave, but sacrifices the only Cannonade effect, and the deck already has Open into Wonder/Cyclonic Rift/Toxic Deluge offering different broad evasion/interaction. The source-bound opponent-turn two-toughness pressure state is material.

**Regalia / Spotlight for Bident: RETAIN_ALTERNATIVE, not selected.** Protecting or evading one legendary attacker (Regalia) or single-use mass unblock + hexproof (Spotlight) has real utility, but the draw lost from Bident's every-creature hit triggers is substantial; three Pirate connections typically generate several card-draw triggers, meaning evasion and refill can synergize instead of compete. The Indomitable provides some redundancy but is no permission to discard a second engine automatically.

**Captain Storm / Shizo for March / Path: RETAIN_ALTERNATIVE, not selected.** Actual two-Pirate `{B}` recovery and three-color Pirate fixing/scry matter more to repeated attempts than extra size or paid one-legend fear under current available comparisons. Captain Storm + Skyship is a genuine counter combo, not a guaranteed one-source unblock.

**Dreamcaller replacing Open: REJECT for preferred all-purpose configuration.** Two taps for four mana and a later Pirate flyer is strong in a two-blocker board, but Open X3 guarantees three unblockable candidates with a draw on each hit against larger boards. Dreamcaller entering at flash speed has no haste by default and cannot immediately become the third attacking Pirate.

**EDHREC candidate discovery remains upstream research**, not a mandatory inclusion list. Top-inclusion cards already canonical are independently challenged where appropriate. High-lift Aerialist, Dreamcaller, Kitesail Corsair, Kukemssa Pirates, Deadeye Brawler and Prying Blade received reasoned dispositions in the source registry. The full Stage7 doc compares every physically completed package. No hidden five-, six-, seven-, or nine-swap stopping rule is inferred.

## Strict next gate (not covered by this Stage8 comparison)

1. Execute the nine finite source-paid fixture methods on the **exact PR head** alongside focused/broad contract jobs. Correct failures; do not report planned fixtures as passed.
2. Verify the **new exact** six_Wave_Palisade raw SHA-256 and complete 100-card source; independently verify all introduced/current Oracle/legality with fresh source evidence where required, including `Cosmotronic Wave` and `Raise the Palisade`.
3. Re-evaluate Pirate-connection and response-sensitive P0/P1 mechanics changed by dropping Palisade for Wave, using existing D fixtures only where directly unaffected.
4. Rebind M6 I/J tested-pool scope and reproducibility package to **that exact 100-card hash**, not historical D, and run owner-ready schema, whole-deck review and exact-head CI without relaxing hard gates.
5. Present a complete verified new Admiral deck to Cory **only then** for explicit M7 approval; do not mutate canonical approval/lock meanwhile. After that approval, reopen Abaddon under no-minimum-anchoring + EDHREC inclusion/lift, and do not start deck #3 before both are finalized.

This document makes a meaningful *qualitative* selection for the next verification stage, without claiming any unexecuted mechanical proof or owner approval.
