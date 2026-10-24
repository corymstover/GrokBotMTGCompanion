# Anhelo, the Painter — M7 candidate mana analysis (2026-10-23)

Quantity-counted from the candidate Oracle snapshot (land/rock counts asserted in
`tests/test_m6_anhelo_the_painter_m7_mechanics.py`).

- **Lands:** baseline 34 physical (25 nonbasic + 3 Island + 3 Mountain + 3 Swamp). The canonical closeout's "31 lands" is a
  row-count error. Candidate 33 (Exotic Orchard cut).
- **Rocks:** baseline 9 (Sol Ring, Arcane Signet, Fellwar Stone, Dimir/Izzet/Rakdos Signets, three Talismans) → candidate 6
  (Fellwar, Talisman of Indulgence, Talisman of Dominance cut). Static mana sources 43 → 39.
- **Other mana (not counted below):** Dark Ritual, Cormela, Big Score, Black Market Connections, Storm-Kiln Artist,
  Mana Geyser, Jeska's Will; reducers Goblin Electromancer, Thunderclap Drake, Primal Amulet.
- **Colored land sources (U/B/R):** 23/19/21 → 22/18/20.
- **Nonland pips (U/B/R):** 35/22/27 → 36/26/28 (black rises with Shade, Underdog, Detective, Bedevil BB).
- **Curve (nonland MV 0/1/2/3/4/5/6+):** 0/6/27/16/10/4/2 → 0/6/27/17/10/4/2; average 2.831 → 2.833.
- **Hypergeometric (99-card library):** P(2–5 lands in opening 7) 0.758 → 0.741; P(≥4 lands in top 10) 0.470 → 0.441;
  P(≥3 lands-or-rocks in top 9, Anhelo on curve on the draw) 0.839 → 0.768; top 8 (on the play) 0.762 → 0.680;
  P(≥4 lands-or-rocks in top 10) 0.711 → 0.610.
- **Judgment (MODERATE confidence):** the cut costs about 7–10 points on turn-3 commander/turn-4 mana thresholds, before
  counting rituals and Treasure. It buys four bodies the commander needs every turn. The same-count alternative that keeps
  Talisman of Dominance (cuts Primal Amulet instead, 40 sources) is staged as a full 100 so ChatGPT/owner can prefer it.
