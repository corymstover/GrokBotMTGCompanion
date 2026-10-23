# Garza Zol, Plague Queen — M7 research-candidate mana analysis (2026-10-23)

Counted by quantity from the candidate Oracle snapshot. Land counts and measured values are asserted in `tests/test_m6_garza_zol_plague_queen_m7_mechanics.py`.

- **Lands:** 38 physical lands → 36, plus two MDFC lands (Sink into Stupor // Soporific Springs: U; Fell the Profane // Fell Mire: B). Exotic Orchard and Takenuma, Abandoned Mire are cut.
  - Coloured land sources (fetches and rainbow lands counted for each colour they can produce), U/B/R: 25/27/24 → 25/26/23, counting the MDFC back faces.
  - Fetches 9 → 9.
- **Mana rocks:**
  - Kept: Sol Ring, Mana Vault, Grim Monolith, Arcane Signet, Dimir Signet, Izzet Signet, Rakdos Signet, Talisman of Creativity, Talisman of Dominance, Talisman of Indulgence.
  - Cut: Fellwar Stone.
- **Curve (nonland printed MV 1/2/3/4/5):** 14/27/15/3/2 → 13/28/16/4/2. Average nonland MV 2.213 → 2.270.
- **Coloured pips (nonland mana costs, front face):** U/B/R 13/9/15 → 14/11/17.
- **Hypergeometric (99-card library), opening 7:**

  | Lands | P(2–4 lands) | P(1–4 lands) | Note |
  |---|---|---|---|
  | 38 | 0.7551 | 0.8968 | baseline |
  | 36 | 0.7403 | 0.9046 | MDFCs not counted |
  | 38 | unchanged | unchanged | MDFCs counted as lands |

- **Exact Garza castability (7 mana).** Counted: lands (Ancient Tomb as 2), Sol Ring, Mana Vault, Grim Monolith, Signets, Talismans, Arcane Signet and Fellwar Stone. Colours are assumed met. By turn 4/5/6 on the play:

  | List | Turn 4 | Turn 5 | Turn 6 |
  |---|---|---|---|
  | Baseline | 0.1876 | 0.3093 | 0.4724 |
  | Candidate, MDFCs played as lands | 0.1769 | 0.2882 | 0.4451 |
  | Candidate, MDFCs never played as lands | 0.1649 | 0.2669 | 0.4073 |

  Commander tax adds 2 per previous cast.
- **New coloured costs:**
  - Lizard Blades {1}{R}, reconfigure {2};
  - Giantfall {1}{R};
  - Sink into Stupor {1}{U}{U}, or 3 life as an untapped land;
  - Fell the Profane {2}{B}{B}, or 3 life as an untapped land.
- **Judgment (MODERATE confidence):** the mana base swaps two weak lands for two MDFCs that are also interaction. The real cost is the Fellwar Stone cut: turn-6 Garza drops by 2.7 points. The keep-Fellwar / cut-Inquisitor's Flail alternative is staged for that reason.

Model caveat: each fetch counts as a source of any one Grixis colour. Exotic Orchard (which depends on opponents) counts as rainbow in the land-source counts, and Fellwar Stone as any colour in the castability model, which flatters the baseline slightly.
