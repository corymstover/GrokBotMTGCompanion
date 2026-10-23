# Gwendlyn Di Corci — M7 research-candidate mana analysis (2026-10-23)

Counted by quantity from the candidate Oracle snapshot. Land counts and measured values are asserted in `tests/test_m6_gwendlyn_di_corci_m7_mechanics.py`.

**Lands.** 35 → 35, with no MDFCs and no land changes (2 Island, 2 Mountain, 5 Swamp, 26 nonbasic).
- Coloured land sources, U/B/R: 21/24/17 → 21/24/17. Fetches and rainbow lands are counted for each colour.
- Ancient Tomb is the one colourless land.

**Mana rocks** are unchanged: Sol Ring, Arcane Signet, Talisman of Dominance, Talisman of Indulgence, Patriar's Seal, Chrome Mox, Lotus Petal and Lion's Eye Diamond (plus Dark Ritual).

**Curve and colour.**
- Curve (nonland printed MV 0/1/2/3/4/5): 3/12/20/22/4/3 → 3/12/20/22/4/3 (Hymn and Dauthi are both 2 MV).
- Average nonland MV 2.328 → 2.328.
- Coloured pips (nonland mana costs, front face), U/B/R: 22/36/9 → 22/36/9 (both cards are {B}{B}).

**Hypergeometric opening 7** (35 lands in a 99-card library): P(2–4 lands) 0.7306 and P(1–4 lands) 0.9069, unchanged.

**Exact source-paid {U}{B}{B}{R} Gwendlyn**

| List | Play T3 | Play T4 | Draw T4 | Play T5 |
|---|---|---|---|---|
| Baseline | 0.1439 | 0.511 | 0.6035 | 0.6035 |
| Candidate | 0.1439 | 0.511 | 0.6035 | 0.6035 |
| Sulfurous Springs over Crumbling Necropolis | 0.1435 | 0.5094 | 0.6017 | 0.6017 |

Colour-agnostic upper bound (any four sources): play T3 0.1518, play T4 0.555, draw T4 0.6487. Colours cost about 4.4 points; the binding constraint is source count, not fixing. These figures check colour coverage of the four pips only.

**New coloured cost.** Hymn to Tourach costs {B}{B}, exactly Dauthi Voidwalker's cost.

**Judgment (HIGH confidence):** the mana is unchanged. Crumbling Necropolis and Exotic Orchard were challenged and kept.

Model caveats:
- Each fetch counts as any one colour.
- Exotic Orchard counts as any colour (optimistic).
- Tapped lands are assumed to be played on an earlier turn.
- Chrome Mox, Lotus Petal, Lion's Eye Diamond, Dark Ritual and Patriar's Seal are ignored (conservative).
