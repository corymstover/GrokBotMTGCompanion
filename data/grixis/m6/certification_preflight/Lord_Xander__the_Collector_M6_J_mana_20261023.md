# Lord_Xander__the_Collector (Lord Xander, the Collector) — M7 research-candidate mana analysis (2026-10-23)

Counts are by quantity, from the candidate Oracle snapshot (`data/grixis/m6/oracle_snapshots/Lord_Xander__the_Collector_M7_Scryfall_20261023.json`). Land counts, the swaps and the measured values are asserted in `tests/test_m6_lord_xander_the_collector_m7_mechanics.py`.

## Lands
Land slots stay at 33:
- Baseline: 33 lands.
- Candidate: 32 lands plus the Malakir Rebirth // Malakir Mire MDFC (Bojuka Bog out).
- Basics: 2 Island, 2 Swamp, 2 Mountain.

Coloured land sources (U/B/R; dedicated lands, with Prismatic Vista counted for all three) are 18/20/18 → 18/19/18. Malakir Mire is an extra B source when it is played as a land.

Both Bojuka Bog and Malakir Mire enter tapped and tap for {B}, so tempo is unchanged when the MDFC is used as a land.

Colourless or utility lands, unchanged: Ancient Tomb, Hall of Echoes (owner add), Hall of the Bandit Lord, Urza's Saga.

## Curve and colour
- **Curve** (library nonland, front faces, MV 0/1/2/3/4/5/6): 3/14/23/15/7/3/1 → 3/15/22/16/7/3/1. Malakir is counted at MV1.
- **Average nonland MV:** 2.33 → 2.33.
- **Library coloured pips (U/B/R):** 27/18/9 → 27/19/9.
- **Xander's cost:** {4}{U}{B}{R} needs all three colours and seven mana. He is usually reanimated or copied instead.

## Deployment (seeded goldfish, seed 30, N=20000)
- P(Xander cast) by turn 7: 0.3779 → 0.3779.
- P(Xander attack trigger) by turn 6: 0.1924 → 0.1857. By turn 7: 0.2978 → 0.2897.
- The whole difference comes from Swiftfoot Boots' equip {1} (Greaves equips for {0}).

## Hypergeometric opening 7
33 land slots in a 99-card library: P(2–4) 0.7069, P(1–3) 0.7825, P(1–4) 0.9083.

## Probes
These are complete 100s:
- Chrome Mox over Talisman of Creativity: turn-7 cast 0.3808. Noise-level, and it adds a Game Changer.
- Command Beacon over Xander's Lounge: 0.3786.
- Glasspool Mimic over Training Center: 0.3749.

None is selected.

## Judgment
HIGH confidence that the land base needs no change beyond the like-for-like tapped-{B} MDFC slot.
