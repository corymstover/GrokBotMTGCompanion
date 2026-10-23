# Anhelo, the Painter — M6 I local-best memo for the M7 candidate (2026-10-23)

Evidence only. NOT owner approved, NOT M6 certification, canonical unchanged. Scope: the six complete 100-card
configurations in `data/grixis/m6/ij/tested_pools/Anhelo__the_Painter_M7_tested_configurations_20261023.json` plus named
single-card contenders. Not a global or statistical optimum.

## Result
Preferred five (raw 2c696db8…, lh1:284c4e09…) is the local best of the tested pool:
+Skyclave Shade, +Sinister Concierge, +Dogged Detective, +Tenacious Underdog, +Bedevil /
−Fellwar Stone, −Talisman of Indulgence, −Exotic Orchard, −Talisman of Dominance, −Feed the Swarm.

## Why
Anhelo copies the first instant/sorcery each turn only by sacrificing a power-2+ creature. The approved list fielded
43 static mana sources (34 lands, 9 rocks) and relied partly on instant-made tokens that use up the casualty slot
themselves. The four bodies are casualty-legal and come back (graveyard cast, blitz from graveyard, return to hand,
suspend), and Bedevil can be copied on opponents' turns.

## Self-challenge
- Underdog over Primal Amulet (keeping Dominance) — better mana, loses Wellspring copy engine: alternative, not selected.
- Wizards of Thay over Thunderclap Drake — alternative, not selected (curve, Drake is cheaper fodder).
- Mystic Sanctuary over Training Center, Windfall+Gravecrawler over Geyser+Galvanic — rejected.
- Rotten Reunion / Waste Management / Talrand's Invocation — rejected: instant/sorcery-made fodder cannot pay its own turn's casualty.

## Limits
Finite rules cases only (tests/test_m6_anhelo_the_painter_m7_mechanics.py). No simulation or win-rate. The mana cost
is real (see mana memo) and is the strongest argument against the package.
