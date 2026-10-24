# Ashnod M7 Rev2 — source-counted M6 J mana review

Quantity-counted current Oracle snapshot. Commander costs {2}{U}{B}{R} and is not counted in the 99-library probability.

| Measure | Approved baseline | Grok first pass | ChatGPT Rev2 |
|---|---:|---:|---:|
| Physical lands | 33 | 33 | 33 |
| Rocks including one-shot Lotus Petal | 9 | 7 | 8 |
| Land + rock/Petal cards | 42 | 40 | 41 |
| Nonland average mana value (excluding commander) | 2.212 | 2.258 | 2.136 |
| Nonland printed U/B/R pips | 18/13/14 | 18/14/15 | 17/15/11 |
| Noncommander artifact cards | 43 | 41 | 44 |
| Noncommander creatures | 25 | 27 | 24 |
| P(>=5 land/rock/Petal cards among first 11 of 99) | 53.74% | 47.89% | 50.83% |

Last row is an exact hypergeometric **card-access proxy**, not commander cast probability, not a simulation of color availability, and not a win rate. Lotus Petal is one-shot, Basalt Monolith does not untap normally, Mox Opal is conditional, other artifacts/generators produce mana in certain board states. The math treats them all as one accessible source card and thus has known limitations.

City of Brass and Mana Confluence produce UBR unconditionally (one damage or one life when used for colored mana); the eliminated Lounge was ETB tapped and Orchard depended on opponent lands. One original Talisman is lost without full replacement, while Basalt enhances generic acceleration and has two independent combo routes with existing permanents. Eight total rock/Petal cards is a slight reliability loss vs baseline but a measurable improvement vs Grok first pass.

Red-team: 33 lands is lean for a 5-MV commander and two of the newly chosen mana pieces demand colorless conversion. Consider an extra rainbow land only when its named existing-land tradeoff is quality positive; Mana Vault was studied but no sound non-engine cut remained.
