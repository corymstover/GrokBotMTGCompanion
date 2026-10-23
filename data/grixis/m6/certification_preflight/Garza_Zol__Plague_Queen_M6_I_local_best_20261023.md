# Garza Zol, Plague Queen — M6 I local-best memo for the M7 research candidate (2026-10-23)

This memo is evidence only. The candidate is NOT owner approved, NOT M6 certified and NOT owner-presentable (RESEARCH_ONLY: four genuine swaps, below the five-swap floor). The canonical list is unchanged.

Scope: the ten complete configurations in
`data/grixis/m6/ij/tested_pools/Garza_Zol__Plague_Queen_M7_tested_configurations_20261023.json`, plus named single-card contenders. Each configuration is 100 = 1 commander + 99 library. This is not a global or statistical optimum.

Baseline: canonical encyclopedia main 9b26aa28fc7e16f6652aaec292b4edf84e20db71 (blob e3e43c53, introduced by 3e2c89d998d17f709d54f40a4d52acfd6840ee11 on 2026-10-14; registry source_commit 1836b97, same bytes), `refinement/decklists/Garza_Zol_Plague_Queen_Approved_2026-10-14.txt`. Raw SHA-256 32c0e804… equals the registry's recorded digest (no provenance exception). Logical hash lh1:f5190339… equals the registry's baseline hash.

## Result
The research four (raw 48b6a7db…, lh1:cd767801…) is the local best of the tested pool:
- Adds: +Lizard Blades, +Giantfall, +Sink into Stupor // Soporific Springs, +Fell the Profane // Fell Mire.
- Cuts: −Fellwar Stone, −Rapid Hybridization, −Exotic Orchard, −Takenuma, Abandoned Mire.

**Only four genuine improvements were found, so the deck is RESEARCH_ONLY.** Five is a floor, not a target. Every fifth candidate failed for one of these reasons:
- it was against the owner's stated direction (Nibelheim Aflame over the owner-added Nova Flame; Fire Whip, which is in the owner-removed pinger class);
- it was against the castability data (Hammer of Nazahn over Talisman of Indulgence, turn-6 Garza 0.4451 → 0.4179);
- it was no better than the incumbent (Nibelheim Aflame over Toxic Deluge).

None was counted. After the four, ten more incumbents were challenged and kept:
- Inquisitor's Flail by Fireshrieker
- Nova Flame and Toxic Deluge by Nibelheim Aflame
- Pongify by Fire Whip
- Talisman of Indulgence by Hammer of Nazahn
- Feed the Swarm by Withering Torment
- Terminate by Bedevil
- Psychotic Fury by Temur Battle Rage
- Fall of the Hammer by Pain for All
- Slip Out the Back by Shore Up

## Why (commander-first)
Garza Zol, Plague Queen ({4}{U}{B}{R} 5/5 Legendary Creature — Vampire Noble): "Flying, haste / Whenever a creature dealt damage by Garza Zol this turn dies, put a +1/+1 counter on Garza Zol. / Whenever Garza Zol deals combat damage to a player, you may draw a card."

- **Lizard Blades over Fellwar Stone.** Every Garza payoff triggers per hit: her draw, Curiosity, Kediss, Quietus Spike, Robe of the Archmagi and both Swords. Double strike doubles them, and its first-strike step lets Garza kill a blocker before it deals damage.
  - Pass C asked for this test; see below.
  - Cost: one 2-mana rock. Garza castable by turn 6 on the play falls 0.4724 → 0.4451 for the whole four-swap with MDFCs played as lands.
- **Giantfall over Rapid Hybridization.** Garza-sourced removal grows her and is lethal with Basilisk Collar or Quietus Spike. This is the owner's stated direction ("commander-sourced interaction that grows Garza", which is why Go for the Throat and Soul Shatter were trimmed). It adds an artifact mode and gives no 3/3 away. It needs a creature.
- **Sink into Stupor // Soporific Springs over Exotic Orchard** (EDHREC synergy −0.15): a land that is also a bounce for a blocker, a hate permanent or an uncounterable spell.
- **Fell the Profane // Fell Mire over Takenuma, Abandoned Mire (FLAGGED: generic removal).** It takes a land slot, not a spell slot, so the owner's trim of generic removal spells is not undone. Takenuma's channel has few targets because Garza returns to the command zone. LOW confidence.

## Owner direction
- **Cuts:** all four are plain RETAIN lines in the owner's 2026-10-14 decisions. **No owner keep or owner addition is cut.**
- **Owner keeps stand:** Blade of the Bloodchief, Brotherhood Regalia, Chandra's Ignition, Curiosity, Grafted Exoskeleton, Mask of Memory, Quietus Spike, Shadowspear, Swiftfoot Boots, Sword of Feast and Famine, Sword of Fire and Ice, Trailblazer's Boots, Rogue's Passage, and the premium interaction and tutor shell. The owner addition Nova Flame also stays.
- **Owner-removed cards are not re-added:** Lightning Greaves, Embercleave, Bident of Thassa, Ophidian Eye, Frantic Search, Waltz of Rage, Go for the Throat, Soul Shatter, the Vampire tribal cards, Sword of Truth and Justice, the pinger class (Viridian Longbow, Gorgon's Head), Unscythe, Vorpal Sword, extra fast mana and compact combo. Fire Whip appears only in a rejected staged list.

## Pass C requested tests (bounded finite versions; not win rates)
These are in `data/grixis/m7/research_challengers/Garza_Zol__Plague_Queen_bounded_measured_tests_20261023.json` and recomputed in `tests/test_m6_garza_zol_plague_queen_m7_mechanics.py`. Pass C's final disposition was **NEEDS TESTING**, with primary challenger +Fireshrieker / −Inquisitor's Flail. The Pass C receipt is a NON-INDEPENDENT owner-equivalent (actual technical independence FALSE).

1. **Double strike vs Inquisitor's Flail, and both together.** The ledger covers 5 equipment states × 8 blocker states × 3 configurations: bare, with Basilisk Collar, and with trample from Shadowspear.
   - Unblocked commander damage: no equipment 5; Flail 10; double strike 10, with 2 Garza draws; both 20.
   - Blocks: double-strike Garza kills and survives a 5/5 vanilla, a 3/3 deathtouch and a 4/4 double striker. Bare or Flail Garza dies to all three.
   - Bad blocks: double strike trades with a 5/5 first striker and dies to an 8/8 or a 5/5 indestructible blocker. Flail + Lizard Blades survives the 8/8.
2. **Removal between strike steps.** Double strike deals 5 instead of 10, and Flail still deals 10. This is Flail's only winning row.
3. **Infect, Kediss, Curiosity and Spike.**
   - Grafted Exoskeleton at 7 power: 14 poison, lethal, with Flail or double strike.
   - Curiosity + Kediss at a 3-opponent table: 6 Curiosity draws with double strike vs 3 with Flail.
   - Quietus Spike against an opponent at 40: they go to 6 with double strike vs 15 with Flail.
   - Power 6 with Flail + Lizard Blades: 24 commander damage in one hit (lethal).
4. **7-mana access.** Exact hypergeometric Garza castability by turn 4/5/6 on the play:
   - baseline 0.1876 / 0.3093 / 0.4724;
   - candidate 0.1769 / 0.2882 / 0.4451 with MDFCs played as lands, or 0.1649 / 0.2669 / 0.4073 if they are never played as lands;
   - keep-Fellwar / cut-Flail four: the same as the baseline (0.4724 at turn 6 with MDFCs as lands);
   - Hammer five: 0.1668 / 0.2682 / 0.4179.

   Commander tax adds 2 per previous cast.

Not done, stated plainly: there were no matched-hand games and no win rates. The repo has no validated Garza game or opponent model.

## Self-challenge
- **Fireshrieker instead of Lizard Blades (four):** staged, RETAIN_ALTERNATIVE. It has the same combat rows but needs one more setup mana.
- **Lizard Blades cutting Inquisitor's Flail and keeping Fellwar Stone (four):** staged, RETAIN_ALTERNATIVE. It keeps baseline castability but loses the 4× one-hit kill.
- **Pass C's exact list (+Fireshrieker / −Inquisitor's Flail on the baseline):** staged, RETAIN_ALTERNATIVE.
- **Five-swaps:** Nibelheim Aflame over Nova Flame, Nibelheim Aflame over Toxic Deluge, Fire Whip over Pongify and Hammer of Nazahn over Talisman of Indulgence. All were staged and rejected, and none was counted.
- **Rejected singles:** Cranial Plating, Sword of War and Peace, Sword of Sinew and Steel, Withering Torment, Bedevil, Temur Battle Rage, Mask of Riddles, Psionic Gift, Rabid Gnaw, The Last Agni Kai, Pain for All, Mox Amber, Thran Dynamo, Relic of Sauron and Shore Up. Jeweled Lotus is banned.

## Limits
Only finite rules cases and exact enumerations are tested.

Main losses:
- Fellwar Stone's mana (castability −2.7 points by turn 6);
- Rapid Hybridization's one-mana creature-free removal;
- Exotic Orchard's rainbow mana;
- Takenuma's channel recursion.

Game Changers 9 → 9 (Bracket 4). Average nonland MV 2.213 → 2.270.
