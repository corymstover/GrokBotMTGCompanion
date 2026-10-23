# Edea, Possessed Sorceress — M7 candidate mana analysis (2026-10-23)

Counted by quantity from the candidate Oracle snapshot. Land counts and colour access are asserted in `tests/test_m6_edea_possessed_sorceress_m7_mechanics.py`.

- **Lands:** 35 physical in both lists (Island, Mountain and Swamp ×3 each, plus 26 nonbasic). Hall of Echoes replaces High Market, so one colourless utility land replaces another.
  - Coloured land sources: U 19, B 19, R 18, unchanged.
- **Mana rocks:** Sol Ring, Arcane Signet, Fellwar Stone and three Talismans are counted in the DP, each once.
- **Curve (nonland printed MV 0/1/2/3/4/5/6/7+):** 0/9/13/18/14/5/3/2 → 0/10/13/17/15/4/3/2. Average nonland MV 3.203 → 3.156.
- **Coloured pips (nonland):** U/B/R 15/32/23 → 15/31/24.
- **Hypergeometric (99-card library):** P(2–5 lands in the opening 7) = 0.7746 with 35 lands.
- **Exact lands-plus-rocks access on the play** (the same in both lists):
  - P(a land drop every turn up to turn T), T = 3/4/5/6/7: 0.6811/0.4984/0.3342/0.2069/0.1191.
  - P(Edea castable by turn T: five sources, three lands, U/B/R covered): 0.0456/0.2304/0.4878/0.588/0.6772.
- **New coloured costs:** Aggravated Assault {2}{R} (activation {3}{R}{R}), Combat Celebrant {2}{R}, Geyadrone Dihada {1}{U}{B}{R}, Kaya's Ghostform {B}. Cut nonland MV totals 14 (Evereth 3, Zara 5, Ayara 3, Spotlight 3); add nonland MV totals 11. Hall of Echoes' {5} copy activation and Aggravated Assault's {3}{R}{R} are mana sinks.
- **Judgment (MODERATE confidence):** the mana is unchanged. Aggravated Assault's activation competes with Edea's own mana. It is used at most min(mana//5, red//2) times per main phase.
