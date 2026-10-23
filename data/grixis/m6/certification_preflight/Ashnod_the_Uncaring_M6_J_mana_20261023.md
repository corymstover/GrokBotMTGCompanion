# Ashnod the Uncaring — M7 candidate mana analysis (2026-10-23)

Counted by quantity from the candidate Oracle snapshot. Land and rock counts are asserted in
`tests/test_m6_ashnod_the_uncaring_m7_mechanics.py`.

- **Lands:** 33 physical in both lists (25 nonbasic + 3 Island + 2 Mountain + 3 Swamp). Unchanged.
- **Rocks:** baseline 9 (Sol Ring, Arcane Signet, Fellwar Stone, Mind Stone, Talismans of Creativity/Dominance/
  Indulgence, Mox Opal, Lotus Petal). Candidate 7 (Fellwar Stone and Talisman of Indulgence cut). Static sources 42 → 40.
- **Other mana (not counted below):** Krark-Clan Ironworks, Ashnod's Altar, Crime Novelist, Treasure Vault, Urza, Priest of
  Forgotten Gods (BB, BBBB when copied); cost reducers Etherium Sculptor and Enthusiastic Mechanaut (Foundry Inspector cut).
- **Colored land sources (U/B/R):** 17/15/14, counting fetches and Exotic Orchard. Unchanged.
- **Nonland pips (U/B/R):** 18/13/14 → 18/14/15 (Priest +B, Reshapers +R).
- **Curve (nonland printed MV 0/1/2/3/4/5/6+):** 4/13/24/18/5/1/1 → 3/14/24/17/5/2/1; average 2.212 → 2.258.
- **Hypergeometric (99-card library):** P(2–5 lands in the opening 7) 0.741 → 0.741. Ashnod costs five:
  P(≥5 lands-or-rocks in the top 11, turn 5 on the draw) 0.537 → 0.479; top 10 (on the play) 0.426 → 0.372.
  P(≥4 in the top 10) 0.687 → 0.636.
- **Judgment (MODERATE confidence):** about a 5–6-point cost on on-curve commander odds, before counting KCI/Altar/
  Novelist/Treasure Vault mana and the cost reducers. That buys four Ashnod-copyable sacrifice abilities and three
  Spellbook-listed Ashnod loops. Rejected: cutting a third rock (Mind Stone) for Sage of Lat-Nam.
