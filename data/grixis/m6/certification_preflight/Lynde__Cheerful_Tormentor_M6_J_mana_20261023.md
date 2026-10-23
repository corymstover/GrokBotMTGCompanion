# Lynde__Cheerful_Tormentor (Lynde, Cheerful Tormentor) — M7 research-candidate mana analysis (2026-10-23)

Counts are by quantity, from the candidate Oracle snapshot (`data/grixis/m6/oracle_snapshots/Lynde__Cheerful_Tormentor_M7_Scryfall_20261023.json`). Land counts, the swaps and the measured values are asserted in `tests/test_m6_lynde_cheerful_tormentor_m7_mechanics.py`.

## Lands
Unchanged at 35 in both lists. Basics: 4 Island, 3 Mountain, 3 Swamp. Neither swap touches a land.

Coloured land sources (U/B/R) stay 20/20/21. Colourless or utility lands, unchanged: Ancient Tomb, Bojuka Bog, Training Center (and the five-colour Command Tower, Exotic Orchard, City of Brass, Mana Confluence).

## Curve and colour
- **Curve** (library nonland, front faces, MV 0/1/2/3/4/5/6/7+): 1/7/14/21/7/9/2/3 → 1/7/14/21/8/8/3/2.
- **Average nonland MV:** 3.22 → 3.19.
- **Library coloured pips (U/B/R):** 22/33/14 → 26/29/14. Court of Vantress ({2}{U}{U}) and Extravagant Replication ({4}{U}{U}) move four pips from black to blue; there are 20 blue land sources.
- **Lynde's cost:** {1}{U}{B}{R}, all three colours at four mana.

## Deployment (seeded goldfish, seed 31, N=20000)
- P(Lynde cast) by turn 4: 0.629 → 0.629. By turn 7: 0.8681 → 0.8681.
- P(Lynde with a repeatable own-Curse outlet) by turn 7: 0.2716 → 0.2716.
- P(Lynde with an extra-upkeep source) by turn 7: 0.2622 → 0.2622.
- P(Lynde with Court or Replication) by turn 7: 0 → 0.1381; with Cruel Reality or Death's Hold: 0.1051 → 0.

## Hypergeometric opening 7
35 lands in a 99-card library: P(2–4 lands) 0.7306.

## Probes
- Staff of Compleation over Nightscape Familiar: turn-4 cast 0.6179, outlet 0.3379 (staged, not selected).
- Strionic Resonator over Nightscape Familiar: turn-4 cast 0.6179 (owner rejected; compare-only).

## Judgment
HIGH confidence that the land base needs no change. The swaps add two non-land 4- and 6-drops in place of a 7- and a 5-drop, so the curve gets slightly lower.
