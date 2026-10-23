# Doctor Doom, King of Latveria — M7 candidate mana analysis (2026-10-23)

Counted by quantity from the candidate Oracle snapshot. Land counts and colour access are asserted in `tests/test_m6_doctor_doom_king_of_latveria_m7_mechanics.py`.

- **Lands:** 38 physical in both lists (Island, Mountain and Swamp one each, plus 35 nonbasic). One land swap: Coastal Peak (UR, cycling) for Shipwreck Marsh (UB).
  - Land-discard lands: Dakmor Salvage, Oscorp Industries (mayhem), Canyon Slough, Fetid Pools, Xander's Lounge and Coastal Peak (cycling).
  - Utility lands: Ancient Tomb, Desolate Lighthouse, Geier Reach Sanitarium, Takenuma, Otawara, Training Center, Villainous Hideout.
  - Villainous Hideout's coloured mana only pays for Villain spells and Villain-source abilities, so it counts for Doom but not for Seismic Assault or the granted cycling {R}. Exotic Orchard is counted as colourless.
- **Mana rocks:** 7 in the baseline (Sol Ring, Arcane Signet, Fellwar Stone, Talismans of Creativity, Dominance and Indulgence, The Soul Stone) → 6 in the candidate (Fellwar and Creativity out, Mox Diamond in).
- **Red land sources:** 20 → 21 (per the land table in the mechanics test).
- **Curve (nonland printed MV 0/1/2/3/4/5/6/7+):** 0/7/19/17/13/4/1/0 → 1/8/17/18/12/4/1/0. Average nonland MV 2.852 → 2.787.
- **Hypergeometric (99-card library, Doom in the command zone):** P(2–5 lands in the opening 7) = 0.817 in both lists (38 lands each).
- **Exact lands-only colour access** (multivariate hypergeometric with Hall's condition; rocks and Treasures ignored):
  - {1}{U}{B}{R} (four lands covering U, B and R) by 10 / 11 cards: 0.5550 / 0.6477 → 0.5570 / 0.6498.
  - RRR (three red lands) by 11 / 12 cards: 0.3895 / 0.4529 → 0.4248 / 0.4904.
  - Three lands, two of them red, by 9 cards: 0.5318 → 0.5573.
- **Coloured pips (single-colour symbols, nonland):** U/B/R 17/29/20 → 17/27/22.
- **New coloured costs:** Lightning Axe {R}, Glint-Horn Buccaneer {1}{R}{R}, Red Ghost {2}{U}{R}, Swiftfoot Boots {2}, Mox Diamond {0} (discard a land). RR is supported by 21 red land sources and two red Talismans.
- **Judgment (MODERATE confidence):** the land count is unchanged and red access improves slightly. Black loses one land source (Shipwreck Marsh; blue is unchanged), and black pips fall by two. Mox Diamond is card disadvantage except as a Doom trigger; the five-swap keeping Talisman of Creativity is the retained alternative for players who dislike that.
