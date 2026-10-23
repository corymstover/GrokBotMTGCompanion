# Doctor Doom, King of Latveria — M6 I local-best memo for the M7 candidate (2026-10-23)

This memo is evidence only. The candidate is NOT owner approved and NOT M6 certified, and the canonical list is unchanged.

Scope: the ten complete configurations in
`data/grixis/m6/ij/tested_pools/Doctor_Doom__King_of_Latveria_M7_tested_configurations_20261023.json`, plus named single-card contenders. Each configuration is 100 = 1 commander + 99 library. This is not a global or statistical optimum.

## Result
The preferred six (raw 21d5ebd6…) is the local best of the tested pool:
- Adds: +Lightning Axe, +Glint-Horn Buccaneer, +Red Ghost, Intangible Genius, +Coastal Peak, +Swiftfoot Boots, +Mox Diamond.
- Cuts: −Feed the Swarm, −Change of Fortune, −Loki, the Deceiver, −Shipwreck Marsh, −Fellwar Stone, −Talisman of Creativity.

## Why (commander-first)
Doctor Doom, King of Latveria ({1}{U}{B}{R} Human Noble Villain): "Whenever you discard one or more land cards, each opponent loses 2 life." (once per discard event, 603.2c) and "At the beginning of combat on your turn, target Villain you control gains menace until end of turn. It connives." (701.50a; a discarded land drains 2 but gives no counter).

Each add either turns a card into a land-discard event, protects the single engine, or improves the red mana the land-cycling package needs:
- **Lightning Axe** ({R} instant, discard a card or pay {5}: 5 damage to a creature). Discarding a land makes it removal plus a 2-point drain for one mana. **Feed the Swarm** is sorcery-speed, costs life, and does nothing for the discard plan.
- **Glint-Horn Buccaneer** (haste; whenever you discard one or more cards, 1 damage to each opponent per card; {1}{R}, attacking: discard then draw). It stacks on every Doom drain and loots a land on the attack. **Change of Fortune** is a 4-mana sorcery refill whose hand discard is a single event (one Doom drain).
- **Red Ghost, Intangible Genius** makes a hasty 3/3 Ape Villain whenever we draw our second card each turn. Doom's combat connive guarantees that second draw on our turn, and the Apes are Villains for Prowler, Baron Strucker and Doom Reigns Supreme. **Loki, the Deceiver** is a 4-mana Villain whose copy and card draw need Villains connecting in combat.
- **Coastal Peak** (UR cycling land: discarding it to cycling is a land discard). It replaces the UB **Shipwreck Marsh** and raises red land sources 20 → 21.
- **Swiftfoot Boots** gives hexproof (Doom can still target himself; Lightning Greaves' shroud, 702.18a, would stop his own combat trigger). **Fellwar Stone** is the most redundant of seven rocks and depends on opponents' lands.
- **Mox Diamond** (Game Changer): a 0-mana rock whose additional cost is discarding a land, i.e. a free Doom trigger. **Talisman of Creativity** is the third Talisman.

## Pass C requested tests (bounded finite versions; not win rates)
Run in `tests/test_m6_doctor_doom_king_of_latveria_m7_mechanics.py` (class `PassCBoundedMeasuredTests`). Pass C #13's final disposition was **NEEDS TESTING**.
1. **Dakmor sequence** (Pass C item 1: trigger ordering, library size, zones, graveyard interruption, Containment Construct/Moonstone/Converter choices, Monument once-per-turn limit, red cost). A deterministic trace of: cycle Dakmor Salvage for {R} (Tectonic Reformation) → discard triggers resolve first (603.3b) → the cycling draw is replaced by dredge 2 only if the library holds ≥ 2 cards (702.52b).
   - Doom alone, 40 life, 40-card library: 20 iterations, 40 drain each, lethal, 2 cards left. A 38-card library still gives 20 iterations; 37 gives 19 iterations, 38 drain, **not** lethal.
   - With Glint-Horn Buccaneer: 14 iterations, 42 drain; a 26-card library is lethal and 25 is not. With Buccaneer plus Cool but Rude level 2: 8 iterations.
   - Monument to Endurance adds at most three modes (once each per turn): 19 iterations, 41 drain.
   - Red cost: with no external {R} there are 0 iterations. Green Goblin, Nemesis makes a *tapped* Treasure, so with 3 red it is 3 iterations, 6 drain. Villainous Hideout cannot pay the granted cycling {R}.
   - Interruptions: graveyard hate at iteration 5 ends it at 5 iterations, 10 drain. Taking a Construct/Moonstone/Converter "you may exile" on Dakmor ends it after 1 iteration (the model declines that option).
   - The Commander Spellbook combo 779-2546-4467 (Badgersaur + Tectonic Reformation + Dakmor) is therefore **finite and library-bounded**; no infinite is claimed.
2. **Glint-Horn Buccaneer vs Green Goblin, Revenant** (Pass C item 2), with Magmakin Artillerist and the documented Putrid Imp / Ledger Shredder slots. A 20-cell grid: five fixed turn patterns (cycling, wheel, Seismic, quiet, cast this turn) × attack possible or not × removal before attacks or not.
   - Totals (damage to each opponent / cards): Buccaneer 79/5, Revenant 8/19, Artillerist 64/0.
   - Buccaneer beats Revenant on damage in 20/20 cells; Revenant beats Buccaneer on cards in 4/20 and does nothing (0,0) in 16/20 because it needs an attack and has no haste. Revenant's ceiling is the wheel cell (2 damage, 8 cards).
   - Buccaneer ≥ Artillerist in every cell, which is why the candidate moved from Artillerist to Buccaneer.
   - Pass C's exact pairing (+Buccaneer −Revenant) is staged as complete 100s (in the preferred six and alone on the baseline) and rejected: Revenant stays as the deck's remaining one-sided refill once Change of Fortune is cut. Ledger Shredder over Iron Monger and Putrid Imp over Demand Answers are staged seven-swaps, both rejected.
3. **Resource dependence** (Pass C item 3). Exact lands-only hypergeometric (rocks, Mox Diamond, Treasures ignored; conservative):
   - Doom's {1}{U}{B}{R} by 10 / 11 cards: 0.5550 / 0.6477 → 0.5570 / 0.6498.
   - Seismic Assault's RRR (three red lands) by 11 / 12 cards: 0.3895 / 0.4529 → 0.4248 / 0.4904. Three lands with two red among 9 cards: 0.5318 → 0.5573. Red land sources 20 → 21.
   - Recovery under graveyard hate: 10 graveyard-independent land-discard outlets in the candidate (Seismic Assault, Tectonic Reformation, Lightning Axe, Mox Diamond, Coastal Peak, Canyon Slough, Fetid Pools, Xander's Lounge, Cool but Rude, Glint-Horn Buccaneer) vs 3 graveyard-dependent ones (Dakmor Salvage, Crucible of Worlds, Oscorp Industries).

Not done, stated plainly: Pass C asked for identical turn 4–8 openings with matched red mana, Villain payoffs, attack opportunities and opposing removal and responses. There was no matched-opening playtest sample, no opponent model and no removal-response rate. No simulator in this repository models Doom's connive choices, opponents' blocks or multiplayer life totals, so no win rates are reported. The tests above are finite enumerations of the exact cases Pass C named.

## Self-challenge
- **Five-swap keeping Talisman of Creativity:** staged, RETAIN_ALTERNATIVE (MODERATE). It keeps a third Talisman instead of Mox Diamond and stays at 6 Game Changers.
- **Withering Torment instead of Lightning Axe:** staged six-swap, rejected. More flexible removal at three mana, but no discard event.
- **Magmakin Artillerist instead of Glint-Horn Buccaneer:** staged six-swap (the earlier provisional candidate), rejected by the bounded grid.
- **Pass C exact pairing, Glint-Horn Buccaneer over Green Goblin, Revenant:** staged in the six-swap and alone on the baseline, both rejected (see item 2).
- **Ledger Shredder over Iron Monger:** seven-swap, staged, rejected. Shredder connives whenever a player casts their second spell each turn but is not a Villain (Doom can't target it, and Strucker, Prowler and Doom Reigns Supreme ignore it); Iron Monger puts counters on each Villain from every connive our Villains already make.
- **Putrid Imp over Demand Answers:** seven-swap, staged, rejected. A free discard outlet but no card advantage; Demand Answers draws two.
- **Rejected singles:** Bazaar of Baghdad (vs Training Center), Faith of the Devoted (vs Black Market Connections), Lonely Sandbar (vs Desolate Lighthouse), Living Laser (vs Kang), Madame Hydra (vs Tombstone), Terminate (vs Lethal Scheme), Bedevil (vs Toxic Deluge), Lightning Greaves (shroud stops Doom's own trigger), Ash Barrens (vs Geier Reach Sanitarium).
- **owner-removed class (flagged, not re-added):** the owner's 10-14 approval removed opponent-discard punishers (Liliana's Caress, Geth's Grimoire, Waste Not) and Dark Deal. Kefka, Court Mage and Syphon Mind were evaluated and rejected as that class; Tinybones, Trinket Thief and Dark Deal are not re-added.

## Limits
Only finite rules cases and bounded enumerations are tested. Main losses:
- Feed the Swarm's enchantment answer.
- Change of Fortune's refill (Revenant, Demand Answers and Jeska's Will remain).
- Loki's Villain body.
- Fellwar Stone and Talisman of Creativity (Mox Diamond replaces one; six rocks instead of seven).
- Shipwreck Marsh's black (black land sources drop by one; blue is unchanged because Coastal Peak makes U).

Other changes:
- Game Changers 6 → 7 (Mox Diamond).
- Creatures 22 → 23; instants/sorceries 22 → 21.
- Average nonland MV 2.852 → 2.787.
