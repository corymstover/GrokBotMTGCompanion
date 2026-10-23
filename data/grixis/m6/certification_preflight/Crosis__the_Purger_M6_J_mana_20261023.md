# Crosis, the Purger — M7 candidate mana analysis (2026-10-23)

Counted by quantity from the candidate Oracle snapshot. Land and rock counts are asserted in `tests/test_m6_crosis_the_purger_m7_mechanics.py`.

- **Lands:** 36 physical in both lists (28 land rows: Island x4, Mountain x3, Swamp x4 and 25 nonbasic). There are no land swaps.
  - Xander's Lounge is still the only always-tapped land (a tri-typed Island Swamp Mountain that all six fetches can find).
- **Mana rocks:** 13 → 11. Kept: Sol Ring, Mana Vault, Chrome Mox, Mox Diamond, Lotus Petal, Arcane Signet, Dimir Signet, Rakdos Signet and three Talismans. Cut: Jet Medallion and Izzet Signet.
  - Counting Dark Ritual and Black Market Connections, nonland accelerants go 15 → 13.
  - With 36 lands plus Ancient Tomb's {C}{C}, a turn-4/5 Crosis remains realistic. Losing two 2-mana rocks mainly slows a turn-4 Crosis off Signet + Signet starts.
- **Colored land sources (heuristic: fetches counted by the basic types they name; any-color lands count all three):** B/R/U 22/18/20 in both lists.
- **Curve (nonland printed MV 0/1/2/3/4/5):** 3/10/27/14/7/2 → 3/9/25/15/9/2. Average nonland MV 2.286 → 2.381.
- **Hypergeometric (99-card library, Crosis in the command zone):** P(2–5 lands in the opening 7) = 0.790 in both lists (36 lands each).
- **Commander activation:** each purge costs {2}{B} on top of Crosis's six. Deadly Rollick (free while Crosis is out) and Rankle (four mana) do not compete with holding {2}{B}. Aggravated Assault's {3}{R}{R} is meant to be paid from lands untapped by Sword of Feast and Famine.
- **Judgment (MODERATE confidence):** a slightly slower early game (two fewer 2-mana rocks, a heavier 3–4 MV band) for a much stronger payoff per Crosis hit. Pass C's own evidence plan treated Jet Medallion and the Specters as the flexible slots.
