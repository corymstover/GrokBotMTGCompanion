# Be'lakor, the Dark Master — M7 candidate mana analysis (2026-10-23)

Counted by quantity from the candidate Oracle snapshot. Land and rock counts are asserted in
`tests/test_m6_belakor_the_dark_master_m7_mechanics.py`.

- **Lands:** 36 physical in both lists: 27 nonbasic + 3 Island + 2 Mountain + 4 Swamp. Unchanged. Unholy Annex // Ritual Chamber
  is an enchantment Room, not a land.
- **Rocks:** baseline 7 (Sol Ring, Arcane Signet, Fellwar Stone, Rakdos Signet, and the Talismans of Creativity, Dominance and Indulgence).
  The candidate has 6 (Fellwar Stone cut). Static land+rock sources 43 → 42.
- **Other mana (not counted below):**
  - Dark Ritual.
  - Demon cost reducers Herald of Slaanesh ({2}), Urza's Incubator ({2}), Heartless Summoning ({2}, every creature), Ancient Cellarspawn ({1}),
    and the new Herald's Horn ({1}, plus a Demon reveal each upkeep).
  - Cavern of Souls (any color for Demons).
- **Colored land sources (U/B/R):** 21/24/19 by hand count. Fetches count as all three, because each can find a typed dual.
  Exotic Orchard, Command Tower, Path of Ancestry, Crumbling Necropolis and Xander's Lounge also count as all three. Unchanged.
- **Nonland pips (U/B/R):** 15/58/20 → 15/65/17. The black load rises (Reaper BBB, Belzenlok BB, Desecration BB, Dominance BB), and black has the most sources (24 + Cavern).
- **Curve (nonland printed MV 1/2/3/4/5/6/7+):** 4/13/10/12/9/9/7 → 4/11/11/13/9/9/7. Average nonland MV goes from 4.109 to 4.125.
- **Hypergeometric (99-card library):** P(2–5 lands in the opening 7) = 0.790 (unchanged). Be'lakor costs six:
  - P(≥6 lands-or-rocks in the top 12, turn 6 on the draw): 0.425 → 0.396.
  - P(≥5 in the top 12): 0.667 → 0.639.
  These figures exclude the reducers. Be'lakor is a Demon creature spell even when cast from the command zone, so Herald's Horn
  (naming Demon) reduces him by {1}, just as Herald of Slaanesh and Urza's Incubator do.
- **Judgment (MODERATE confidence):** cutting Fellwar Stone costs about 3 points on raw on-curve odds. That is recovered for Be'lakor and every
  Demon by Horn's {1} reduction, at the price of one noncreature-mana source. Rejected: Rhystic Study over a rock (it is a Game Changer, and
  the deck needs mana for 6–7 MV Demons).
