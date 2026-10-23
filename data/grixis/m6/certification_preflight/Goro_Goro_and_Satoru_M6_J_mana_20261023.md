# Goro-Goro and Satoru — M7 research-candidate mana analysis (2026-10-23)

Counted by quantity from the candidate Oracle snapshot. Land counts and measured values are asserted in `tests/test_m6_goro_goro_and_satoru_m7_mechanics.py`.

**Lands.** 33 → 33, with no MDFCs and no land changes.
- Coloured land sources, U/B/R: 25/21/21 → 25/21/21. Fetches, Fabled Passage and rainbow lands are counted for each colour they can produce or fetch (the repo static `mana_base` record uses its own convention and reports 24/20/20).
- There are 2 colourless utility lands: Ancient Tomb and Rogue's Passage.

**Mana rocks** are unchanged: Sol Ring, Arcane Signet, Fellwar Stone, Talisman of Creativity, Talisman of Dominance and Talisman of Indulgence.

**Curve and colour.**
- Curve (nonland printed MV 1/2/3/4/5): 13/21/19/10/3 → 13/22/18/10/3.
- Average nonland MV 2.53 → 2.52.
- Coloured pips (nonland mana costs, front face), U/B/R: 35/18/24 → 34/19/24.

**Hypergeometric opening 7** (33 lands in a 99-card library): P(2–4 lands) 0.7069 and P(1–4 lands) 0.9083, unchanged.

**Exact paid {U}{B}{R} Goro on turn 3**

| List | Play T3 | Draw T3 (= play T4) |
|---|---|---|
| Baseline | 0.6668 | 0.7456 |
| Candidate | 0.6668 | 0.7456 |
| Non-mana placeholder for Fellwar Stone | 0.6452 | 0.7254 |
| Dragonskull Summit over Crumbling Necropolis | 0.6654 | 0.7443 |

These figures check colour coverage of the three pips only.

**New coloured cost.** Bitterblossom costs {1}{B} on turn 2 and drains 1 life each upkeep. Mist-Syndicate Naga's ninjutsu {2}{U} is removed.

**Judgment (HIGH confidence):** the mana is unchanged. Fellwar Stone and Crumbling Necropolis were challenged and kept.

Model caveats:
- Each fetch counts as the two colours of its fetchable typed duals.
- Exotic Orchard and Fellwar Stone count as any colour (optimistic).
- Tapped lands are assumed to be played on an earlier turn.
