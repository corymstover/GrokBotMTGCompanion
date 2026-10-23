# Cult of Skaro — M7 candidate mana analysis (2026-10-23)

Counted by quantity from the candidate Oracle snapshot. Land counts are asserted in `tests/test_m6_cult_of_skaro_m7_mechanics.py`.

- **Lands:** 34 physical in both lists (28 land rows: Island x3, Mountain x3, Swamp x3 and 25 nonbasic). There are no land swaps.
  - Xander's Lounge always enters tapped; Arena of Glory is conditional.
- **Mana rocks:** 9 in both lists (Sol Ring, Mana Vault, Mox Opal, Arcane Signet, Dimir Signet, Fellwar Stone and three Talismans).
  - Artifact reducers 3 → 2 (Etherium Sculptor cut; Enthusiastic Mechanaut and Shuri, Wakandan Inventor stay).
- **Colored land sources (heuristic: fetches counted by the basic types they name; any-color lands count all three):** R/B/U 18/17/17 in both lists.
- **Curve (nonland printed MV 0/1/2/3/4/5/6/7+):** 1/4/21/11/14/4/7/3 → 1/4/19/13/14/6/6/2. Average nonland MV 3.354 → 3.338.
- **Hypergeometric (99-card library, Cult in the command zone):** P(2–5 lands in the opening 7) = 0.758 in both lists (34 lands each).
- **New colored pips:** Kindred Discovery {3}{U}{U}, Hammer of Purphoros {1}{R}{R}, Shaun {3}{U}{R}, Karlach {4}{R}, Quantum Misalignment {4}{U}, Skorpekh Lord {2}{B}. Pass C warned about the UU cost with 34 lands: there are 17 blue land sources plus Arcane Signet, Dimir Signet, Fellwar Stone, two blue Talismans and Mox Opal.
- **Judgment (MODERATE confidence):** the mana base is unchanged. The candidate shifts two slots from MV 2 to MV 3 and one from MV 7 to MV 5, and loses one reducer. These are acceptable for more Cult triggers per turn.
