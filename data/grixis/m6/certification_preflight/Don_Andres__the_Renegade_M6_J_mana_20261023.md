# Don Andres, the Renegade — M7 candidate mana analysis (2026-10-23)

Counted by quantity from the candidate Oracle snapshot. Land counts and colour access are asserted in `tests/test_m6_don_andres_the_renegade_m7_mechanics.py`.

- **Lands:** 35 physical in both lists (Island ×2, Mountain and Swamp one each, plus 31 nonbasic). Two land swaps: Gloomlake Verge (U; UB with an Island or Swamp) for Shipwreck Marsh (UB), and Blazemire Verge (B; BR with a Swamp or Mountain) for Smoldering Marsh (BR).
  - Early conditional-or-tapped lands 5 → 3 (Path of Ancestry, Sulfur Falls, Xander's Lounge remain). Luxury Suite, Morphic Pool and Training Center are untapped with two or more opponents.
  - Cavern of Souls' coloured mana only casts a creature of the chosen type, so it counts for Don but not for noncreature spells. Exotic Orchard is counted as colourless.
  - The Verges are counted at their unconditional colour only (conservative); 9 names in the candidate switch on each Verge's second colour.
- **Mana rocks:** 9 in both lists (Sol Ring, Arcane Signet, Fellwar Stone, Dimir/Izzet/Rakdos Signet, Talismans of Creativity, Dominance and Indulgence). The Pass C 35-land figure includes these nine cheap rocks as a separate count.
- **Red land sources:** 22 → 21 (22 with Blazemire Verge's conditional {R}). Blue and black are unchanged or improved by the Verges' unconditional colours.
- **Curve (nonland printed MV 0/1/2/3/4/5/6/7+):** 0/4/21/15/12/6/2/4 → 0/4/21/13/13/8/2/3. Average nonland MV 3.312 → 3.297.
- **Hypergeometric (99-card library, Don in the command zone):** P(2–5 lands in the opening 7) = 0.775 in both lists (35 lands each).
- **Exact lands-only colour access** (multivariate hypergeometric with Hall's condition; rocks and Treasures ignored):
  - Don's {1}{U}{B}{R} (four lands covering U, B and R) by 10 cards: 0.4898 → 0.4864 (Verges at one colour); 0.4898 when the Verge condition is met.
  - Three lands paying U, B and R by 9 cards for a noncreature spell: 0.5844 → 0.5740; 0.5844 with the Verge condition met.
  - Red availability for Pass C's 6/7/8-mana question, by 13 cards: ≥2 red lands 0.8396 → 0.8169; ≥3 red lands 0.5901 → 0.5529; both identical to baseline with the Verge condition met.
- **Coloured pips (single-colour symbols, nonland):** U/B/R 16/36/29 → 20/38/26.
- **New coloured costs:** Gríma {2}{U}{B}, Fallen Shinobi {3}{U}{B} (ninjutsu {2}{U}{B}), Treachery {3}{U}{U} (untaps up to five lands on entry).
- **Judgment (MODERATE confidence):** the land count is unchanged. The gain is tempo (two lands that are untapped on entry rather than usually tapped), which the colour-only model does not credit; the cost is up to about 1 percentage point of three-colour access and up to 3.7 points of RRR access when a Verge's second colour is off. Insurrection's {5}{R}{R}{R} remains the deck's most red-hungry card.
