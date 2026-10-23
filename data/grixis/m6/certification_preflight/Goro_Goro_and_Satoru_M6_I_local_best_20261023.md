# Goro-Goro and Satoru — M6 I local-best memo for the M7 research candidate (2026-10-23)

This memo is evidence only. The candidate is NOT owner approved, NOT M6 certified and NOT owner-presentable. It is RESEARCH_ONLY: one genuine swap, below the five-swap floor. The canonical list is unchanged.

Scope: the nine complete configurations in `data/grixis/m6/ij/tested_pools/Goro_Goro_and_Satoru_M7_tested_configurations_20261023.json`, plus named single-card contenders. Each configuration is 100 cards (1 commander + 99 library). This is not a global or statistical optimum.

Baseline:
- Source: canonical encyclopedia main 9b26aa28fc7e16f6652aaec292b4edf84e20db71, file `refinement/decklists/Goro_Goro_and_Satoru_Approved_2026-10-14.txt`.
- Blob 9d9e1b7b, introduced by 4aefbf3bfb665c212871ff4f2fbb0ca4db711e77 on 2026-10-14. Registry source_commit 1836b97 has the same bytes.
- Raw SHA-256 2fd39e3b… equals the registry's recorded_sha256, so no provenance exception is used.

## Result
The research one-swap (raw 38e02f97…, lh1:55ad7a1a…) is the local best of the tested pool:
- Add: +Bitterblossom.
- Cut: −Mist-Syndicate Naga.

**Only one genuine improvement was found, so the deck is RESEARCH_ONLY.** Five is a floor, not a target. Every other candidate failed for one of these reasons:
- **It cut an owner keep without clearly better evidence:**
  - Bident of Thassa and Grazilaxx, Illithid Scholar: Pass C's own named cuts.
  - Crumbling Necropolis: the owner said no land is weak enough to change.
- **It was in a class the owner rejected:** more one-drop or evasive bodies, such as Gurmag Swiftwing and Reckless Imp.
- **It had an anti-synergy:**
  - Goblin Rabblemaster forces the Goblin commander to attack.
  - Kari Zev's Ragavan token clashes with Ragavan, Nimble Pilferer under the legend rule.
  - Splinter's anthem breaks Tetsuko's evasion.
- **It was marginal:**
  - Redoubled Stormsinger made 0 Dragons in the lean rows.
  - Rapid Hybridization over Vandalblast is a role trade.

None of these was counted. After the swap, twelve incumbents were challenged; all except Naga were kept:
- Bident of Thassa
- Grazilaxx, Illithid Scholar
- Frostcliff Siege
- Vandalblast
- Crumbling Necropolis
- Fellwar Stone
- Triton Shorestalker
- Gingerbrute
- Arcane Denial
- Lightning Greaves
- Aggravated Assault

## Why (commander-first)
Goro-Goro and Satoru ({U}{B}{R} 3/4 Legendary Creature — Goblin Human): "Whenever one or more creatures you control that entered this turn deal combat damage to a player, create a 5/5 red Dragon Spirit creature token with flying. / {1}{R}: Creatures you control gain haste until end of turn."

- **Bitterblossom over Mist-Syndicate Naga.** Bitterblossom makes a new 1/1 flying Faerie Rogue every upkeep, which is exactly the "entered this turn" attacker the trigger needs.
  - Dragon Tempest gives it haste for free. Tetsuko makes it unblockable. It is a Rogue for Silver-Fur Master and Prosperous Thief.
  - Determined Iteration can populate it. It also feeds Breath of Fury and ninjutsu.
  - As an enchantment it keeps working after sweepers and commander removal.
  - Naga's copy is created after combat damage, so it never feeds that combat's trigger.
  - Naga is a plain retained card, not one of the owner's named Ninja keeps.
- **Cost:** 1 life a turn, one fewer ninjutsu body, and the lone Faerie loses to a flying blocker.

## Owner direction
- **Cut:** Mist-Syndicate Naga is not in the owner's named Ninja list in the 2026-10-14 decisions. **No owner keep or owner addition is cut.**
- **Owner keeps stand:**
  - the named Ninja package
  - Bident of Thassa and Enduring Curiosity
  - Daring Piracy, Loyal Apprentice, Urabrask's Forge and Determined Iteration
  - Dragon Tempest and Terror of the Peaks
  - Rogue's Passage
  - the six owner additions: Phoenix Chick, Samut, Hazoret's Champion, Withering Torment, Waterbender Ascension, Raphael, the Nightwatcher and Fire Navy Trebuchet
- **Fit with the owner's plan:** Bitterblossom matches the owner's stated support plan ("repeatable beginning-of-combat or attack-token engines"). It is an engine, not one of the "low-impact bodies" the owner rejected.
- **Owner-removed cards are not re-added:** Reinforced Ronin, Rising of the Day, Feed the Swarm, Combat Research, Impact Tremors and Kaito, Dancing Shadow. The rejected challengers (Invisible Stalker, the extra one-drops, the haste-redundancy cards, Kaito, Cunning Infiltrator, Higure and the other Ninjas, and the generic turbo combo) are not added either.

## Pass C requested tests (bounded finite versions; not win rates)
These are in `data/grixis/m7/research_challengers/Goro_Goro_and_Satoru_bounded_measured_tests_20261023.json` and recomputed in `tests/test_m6_goro_goro_and_satoru_m7_mechanics.py`.

Pass C's final disposition was **NEEDS TESTING**. It compared the exact baseline against +Bitterblossom −Bident of Thassa and +Bitterblossom −Grazilaxx, Illithid Scholar. The Pass C receipt is a NON-INDEPENDENT owner-equivalent review (same model family, with a technical-independence waiver).

1. **Per-card ledger.** The grid is 2 profiles (lean; engine with Daring Piracy) × 5 opponent cases (open, flyer wall, Goro removed turn 5, sweeper turn 6, one extra combat turn 6) × 5 cards, over turns 1–7 with a paid turn-3 Goro.
   - Dragons made, Bitterblossom vs Naga:

     | Profile | Open | Flyer wall | Removal | Sweeper | Extra combat |
     |---|---|---|---|---|---|
     | Lean | 4 vs 2 | 0 vs 2 | 2 vs 1 | 3 vs 2 | 6 vs 3 |
     | Engine | 8 vs 6 | 4 vs 2 | 5 vs 4 | 6 vs 5 | 11 vs 9 |

   - Bident of Thassa drew 2–23 cards and Grazilaxx 2–11. Each added Dragons only in engine rows.
   - Redoubled Stormsinger made 0 Dragons in every lean row and 3–10 in engine rows.
   - Life at the end: 35 with Bitterblossom, 40 otherwise.
2. **Castability.** Exact chance of a paid {U}{B}{R} on turn 3: 0.6668 on the play and 0.7456 on the draw, the same for baseline and candidate.
   - Challenge with a non-mana placeholder replacing Fellwar Stone: 0.6452 / 0.7254, so Fellwar Stone stays.
   - Dragonskull Summit over Crumbling Necropolis: 0.6654.

Not done, stated plainly: there were no matched-hand games and no win rates. The repo has no validated Goro game or opponent model.

## Self-challenge
- **Pass C alt A (+Bitterblossom −Bident of Thassa):** staged and rejected. It cuts an owner keep and the deck's largest draw engine.
- **Pass C alt B (+Bitterblossom −Grazilaxx, Illithid Scholar):** staged and rejected. Grazilaxx gives per-player draw, rescues blocked attackers and has the highest synergy.
- **Deep-review example (+Bitterblossom −Frostcliff Siege):** staged and rejected. Its Temur mode gives continuous haste.
- **Two-swaps:**
  - Redoubled Stormsinger over Frostcliff Siege: rejected.
  - Rapid Hybridization over Vandalblast: RETAIN_ALTERNATIVE.
  - Dragonskull Summit over Crumbling Necropolis: rejected.
  - None was counted.
- **Rejected singles:** Reckless Imp, Captain's Claws, Legion Warboss, Goblin Rabblemaster, Kari Zev, Skyship Raider, Elektra, Daughter of the Hand, Oroku Saki, Shredder Rising, Splinter, Hamato Yoshi, Reconnaissance Mission, Baleful Strix, Gurmag Swiftwing, Ninja Teen, Sneak Attack and Swiftfoot Boots. Jeweled Lotus is banned.

## Limits
Only finite scripted rules cases and exact enumerations are tested. Main loss: Mist-Syndicate Naga's ninjutsu body and late copy growth.

Game Changers 6 → 6 (Bracket 4). Average nonland MV 2.53 → 2.52.
