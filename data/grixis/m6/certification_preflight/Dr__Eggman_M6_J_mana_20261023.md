# Dr. Eggman — M7 candidate mana analysis (2026-10-23)

Counted by quantity from the candidate Oracle snapshot. Land counts and colour access are asserted in `tests/test_m6_dr_eggman_m7_mechanics.py`.

- **Lands:** 31 physical in both lists (Island, Mountain and Swamp ×2 each, plus 25 nonbasic). The preferred five changes no land.
  - Colourless-only lands: Ancient Tomb, Academy Ruins, Urza's Saga and Inventors' Fair. Exotic Orchard is counted as U/B/R in the main DP; the conservative run counts it as colourless, and access never rises.
  - Land sources by colour: U 17, B 17, R 17.
- **Mana rocks:** Sol Ring, Arcane Signet, Fellwar Stone and three Talismans are counted in the DP. Mox Opal is in both lists but is not counted, because it needs metalcraft. Fellwar Stone is counted as colourless.
- **Curve (nonland printed MV 0/1/2/3/4/5/6/7+):** 1/1/15/12/14/7/8/10 → 1/1/15/11/13/9/9/9. Average nonland MV 4.206 → 4.221. Eggman's put branch is the main way to deploy the top end. Su-Chi (8) and Behemoth (6) are put targets, not hardcasts.
- **Hypergeometric (99-card library, Eggman in the command zone):** P(2–5 lands in the opening 7) = 0.703 (31 lands); 0.723 at 32.
- **Exact lands-plus-rocks access** (multivariate hypergeometric; each source counted once):
  - P(≥5 lands by card 11/12): 0.2289/0.3032 (31), 0.2539/0.3328 (32), 0.2798/0.3631 (33).
  - P(Eggman castable: ≥3 lands, five sources and U, B and R covered, by card 11/12): 0.3751/0.4696 (31), 0.404/0.5009 (32), 0.4333/0.532 (33).
- **Coloured pips (single-colour symbols, nonland):** U/B/R 26/23/13 → 28/24/13.
- **New coloured costs:** Possession Engine {3}{U}{U}, Interceptor Mechan {2}{B}{R}; Skysovereign {5}, Su-Chi {8} and Behemoth {6} are generic.
- **Judgment (MODERATE confidence):** the 31-land count is the owner's deliberate choice (2026-10-14), and the candidate keeps it. A 32nd land buys about 3 percentage points of commander access by cards 11–12. It is staged as the Pass C six-swap (+Silverbluff Bridge −Thoughtcast) for the owner to decide, not selected.
