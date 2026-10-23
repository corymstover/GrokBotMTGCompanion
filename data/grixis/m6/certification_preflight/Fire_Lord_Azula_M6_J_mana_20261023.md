# Fire Lord Azula — M7 candidate mana analysis (2026-10-23)

Counted by quantity from the candidate Oracle snapshot. Land counts and the measured values are asserted in `tests/test_m6_fire_lord_azula_m7_mechanics.py`.

- **Lands:** 26 physical nonbasic lands → 25, plus the Sink into Stupor // Soporific Springs MDFC. Exotic Orchard and Gemstone Caverns out; Mistrise Village in.
  - Coloured land sources (fetches and rainbow lands counted for each colour they can produce): R/U/B 21/21/20 → 19/20/18 (U 21 counting the MDFC).
  - Colourless or conditional-colour lands: Ancient Tomb, Emergence Zone, Cavern of Souls. Conditional or tapped lands: Arena of Glory and Starting Town → plus Mistrise Village (untapped once we control a Mountain-typed land: 4 Mountain-typed duals, and all 9 fetches can find one).
  - Fetches 9 → 9.
- **Mana rocks and fast mana (unchanged):** Sol Ring, Mana Vault, Grim Monolith, Arcane Signet, Fellwar Stone, three Talismans, Lotus Petal, Chrome Mox, Mox Diamond, Mox Opal, Lion's Eye Diamond, Wishclaw Talisman; rituals Dark Ritual, Cabal Ritual, Rite of Flame, Simian Spirit Guide; Big Score.
  - Unexpected Windfall adds Treasures (4 when copied).
  - Vivi Ornitier (a mana creature) is cut.
- **Curve (nonland printed MV 0/1/2/3/4/5/6/7+):** 6/25/24/12/4/2/0/0 → 6/25/23/12/6/2/0/0. Average nonland MV 1.849 → 1.905.
- **Coloured pips (nonland mana costs, front face):** U/B/R 35/17/18 → 36/17/20.
- **Hypergeometric (99-card library):**
  - 26 lands: P(2–4 lands in the opening 7) = 0.5805, P(1–4) = 0.8778.
  - 25 lands, MDFC not counted: 0.5575 and 0.8686.
  - With the MDFC counted as a land: 26, unchanged from the baseline.
- **Exact Azula castability (lands plus Sol Ring, Mana Vault, Grim Monolith, Fellwar Stone (as colourless), Signet, Petal and Talismans; moxen, rituals, LED and Treasures excluded, so these are floors):**
  - By turn 4 on the play 0.4920 → 0.4905 (MDFC played as a land) or 0.4632 (never).
  - By turn 4 on the draw 0.5855 → 0.5839.
  - By turn 5 on the play 0.5861 → 0.5845.
- **New coloured costs:** Turnabout {2}{U}{U}, Sink {1}{U}{U} (or 3 life as a land), Unexpected Windfall {2}{R}{R}, Flashback {R}, Mistrise Village {U} for its ability.
- **Judgment (MODERATE confidence):** the mana base swaps two conditional rainbow lands for a conditional U land and an MDFC that is also an answer. Azula castability is within 0.0015 of the baseline when the MDFC is used as a land, and 0.029 lower if it is always held as a spell.
  - Cost: fewer black and red sources (B 20 → 18, R 21 → 19).
  - Gemstone's turn-0 rainbow mana on the draw is lost.
  - The MDFC costs 3 life to enter untapped.

Model caveat: each fetch is counted as a source of any one Grixis colour, and Exotic Orchard (depends on opponents) is counted as rainbow, which flatters the baseline slightly. Gemstone Caverns is counted as colourless in the castability model; the source counts above use the pool convention, which counts it as rainbow (an upper bound).
