# Edward Kenway — M7 candidate mana analysis (2026-10-23)

Counted by quantity from the candidate Oracle snapshot. Land counts and the measured values are asserted in `tests/test_m6_edward_kenway_m7_mechanics.py`.

- **Lands:** 35 physical in both lists (Island ×2, Swamp ×2, Mountain ×1, plus 30 nonbasic). No land changes.
  - Coloured land sources (fetchlands and rainbow lands counted for each colour they can produce): U 21, B 20, R 19, unchanged. Colourless-only lands: Ancient Tomb, Urza's Saga.
- **Mana rocks:** baseline Sol Ring, Arcane Signet, Mana Vault, Fellwar Stone and three Talismans (7 durable) plus Lotus Petal and Chrome Mox, Mox Diamond, Mox Opal. Candidate: 6 durable (Fellwar cut) and no Petal.
- **Curve (nonland printed MV 0/1/2/3/4/5/6/7+):** 4/8/13/18/14/7/0/0 → 3/9/12/18/15/7/0/0. Average nonland MV 2.797 → 2.844.
- **Coloured pips (nonland, hybrid counted for each colour):** U/B/R 33/12/22 → 36/13/21.
- **Hypergeometric (99-card library):** P(2–5 lands in the opening 7) = 0.7746 with 35 lands, unchanged.
- **Exact turn-5 Edward castability** (at least five sources among lands plus durable rocks, U, B and R covered; moxen, Ancient Tomb's second mana and Treasure excluded, so these are floors):
  - Petal counted as a source: on the play 0.5538 → 0.5025; on the draw 0.6544 → 0.6038.
  - Petal excluded: on the play 0.5283 → 0.5025; on the draw 0.6295 → 0.6038.
  - P(five lands by turn 5) alone: 0.3342 play / 0.4251 draw, unchanged.
- **New coloured costs:** Mu Yanling {2}{U}{U}, Mirkwood Bats {3}{B}, Spectral Sailor {U}, Malcolm, the Eyes {U}{R}; Brotherhood Vertibird {3} is colourless. Spectral Sailor's {3}{U} draw is a Treasure sink.
- **Judgment (MODERATE confidence):** the land base is unchanged, and the cost is one durable rock and Petal. Edward's own end-step Treasures and Lannery's loss reduce turn-6+ mana slightly. This is the main cost of the package and is disclosed. The Fateful/Adrestia Pass C alternatives and the four-swap keep Fellwar Stone and match the Petal-excluded baseline.

Model caveat: Cavern of Souls and Exotic Orchard are counted as sources of every Grixis colour (approximation; Cavern's coloured mana is creature-type restricted and Orchard depends on opponents' lands). Absolute figures are slightly optimistic for every tested list alike; neither land changes between lists.
