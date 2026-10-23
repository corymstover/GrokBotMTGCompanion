# Doctor Doom, King of Latveria — M7 red-team memo (2026-10-23)

1. **Graveyard hate:** Dakmor Salvage's dredge loop, Crucible of Worlds and Oscorp Industries' mayhem need the graveyard.
   - The bounded trace ends the Dakmor loop at the iteration where the graveyard is exiled (hate at iteration 5: 5 iterations, 10 drain).
   - Ten graveyard-independent land-discard outlets remain (Seismic Assault, Tectonic Reformation, Lightning Axe, Mox Diamond, Coastal Peak, Canyon Slough, Fetid Pools, Xander's Lounge, Cool but Rude, Glint-Horn Buccaneer).
   - Disclosed, not repaired.
2. **Commander removed or taxed:** Doom (MV 4) is the engine; his drain is once per discard event (603.2c).
   - Swiftfoot Boots gives hexproof and still lets Doom target himself with his combat trigger. Lightning Greaves (shroud, 702.18a) was rejected because it would stop that.
   - Without Doom, Glint-Horn Buccaneer, Cool but Rude level 2, Monument to Endurance and Seismic Assault still deal damage from discards.
3. **Red mana dependence:** Seismic Assault needs RRR and Tectonic Reformation's granted cycling costs {R}. Villainous Hideout cannot pay either.
   - Exact lands-only P(three red lands among the top 11 cards) is 0.3895 → 0.4248. Red land sources are 20 → 21.
   - Green Goblin, Nemesis makes a tapped Treasure, so it cannot pay the next {R} that turn (3 red: 3 iterations, 6 drain).
4. **Library size:** the Dakmor loop is finite. With Doom alone it needs a 38-card library to drain 40; with Buccaneer, 26. Dredge needs at least two cards in the library (702.52b). Do not start it into a short library.
5. **Optional exile choices:** Containment Construct, Moonstone and Currency Converter each say "you may exile" the discarded card. Taking that option on Dakmor ends the loop after one iteration. Decline it during the loop.
6. **Monument to Endurance:** each mode once per turn, so it adds at most three modes (one draw, one Treasure, 3 life) to a loop turn.
7. **Glint-Horn Buccaneer removed:** a 2/4 haste body. The deck falls back to Doom's 2 per event; Buccaneer was chosen over Magmakin Artillerist because it is ≥ Artillerist in every bounded grid cell, not because it is safer.
8. **Change of Fortune cut:** the deck loses a one-sided 4-mana refill. Green Goblin, Revenant (needs to attack; no haste), Demand Answers and Jeska's Will remain. The exact Pass C pairing (cutting Revenant instead) is staged and rejected for this reason.
9. **Combo / bracket disclosure:**
   - Commander Spellbook find-my-combos: baseline and candidate each have **1 included combo**, 779-2546-4467 (Surly Badgersaur + Tectonic Reformation + Dakmor Salvage). Spellbook labels it "Infinite self-mill" and "Near-infinite self-discard triggers"; with a finite library it is library-bounded, and no infinite is claimed.
   - Almost-included lines: 16 → 22; they need cards that are not in the list.
   - Game Changers 6 → 7 (Ancient Tomb, Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Jeska's Will, Vampiric Tutor + Mox Diamond). **Bracket 4**, unchanged.
10. **Exceptions:** none. Doctor Doom, King of Latveria is officially Commander-legal (Marvel Super Heroes Commander, 2026-06-26); the 2026-12-18 promo printing is not a legality date. All 100 are Commander-legal and inside U/B/R per the live Scryfall batch.
11. **Losses:** Feed the Swarm, Change of Fortune, Loki, the Deceiver, Shipwreck Marsh, Fellwar Stone, Talisman of Creativity.
12. **Prior owner history:** the owner's 2026-10-14 approval removed opponent-discard punishers (Liliana's Caress, Geth's Grimoire, Waste Not) and Dark Deal. Kefka, Court Mage and Syphon Mind were evaluated as that class and rejected; Tinybones, Trinket Thief and Dark Deal are not re-added. Glint-Horn Buccaneer punishes **our own** discards and is a different class, but it needs owner review.
13. **Distinctness vs the Loki deck:** the baseline and the candidate each share 53 nonbasic names with `exports/grixis-archidekt/loki-the-deceiver.txt`. Cutting Loki and Talisman of Creativity removes two shared cards, but Red Ghost and Swiftfoot Boots are also in that deck, so overlap does not drop. Disclosed, not repaired.
