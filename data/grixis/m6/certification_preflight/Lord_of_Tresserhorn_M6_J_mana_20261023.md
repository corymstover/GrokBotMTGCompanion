# Lord_of_Tresserhorn (Lord of Tresserhorn) — M7 review-candidate mana analysis (2026-10-23)

Counts are by quantity, from the candidate Oracle snapshot (`data/grixis/m6/oracle_snapshots/Lord_of_Tresserhorn_M7_Scryfall_20261023.json`). Land counts, the swaps and the measured values are asserted in `tests/test_m6_lord_of_tresserhorn_m7_mechanics.py`.

## Lands
35 → 35, with no land changes. Basics: 3 Swamp, 1 Island, 1 Mountain.

Coloured land sources (U/B/R) are 20/23/20 → 20/23/20. How lands are counted:
- Fetches count for every colour they can find. So do the any-colour lands: Command Tower, Mana Confluence, Exotic Orchard, Cavern of Souls and Xander's Lounge.
- Only "Add …" clauses and land subtypes are parsed.

Lands with fewer than three colours:
- **Colourless:** High Market and Rogue's Passage.
- **One colour:**
  - black: Bojuka Bog, Phyrexian Tower, Shizo, Swamp, Takenuma;
  - blue: Island, Otawara;
  - red: Arena of Glory, Mountain.
- **Two colours:**
  - B/R: Badlands, Blood Crypt, Luxury Suite, Sulfurous Springs;
  - U/B: Morphic Pool, Underground River, Underground Sea, Watery Grave;
  - U/R: Shivan Reef, Steam Vents, Training Center, Volcanic Island.

## Mana rocks and fast mana
- **Out:** Fellwar Stone, a rock that taps immediately but makes only colours an opponent's land could produce.
- **In:** Ornithopter of Paradise, which makes any colour but has summoning sickness. It is also a creature for Lord's two-creature sacrifice.
- **Unchanged:** Sol Ring, Arcane Signet, Dimir Signet, Rakdos Signet, Talisman of Creativity, Talisman of Dominance, Talisman of Indulgence, Nightscape Familiar (blue and red spells cost {1} less, including Lord), Phyrexian Altar and Ashnod's Altar.
- **New source:** Black Market Connections' Treasure mode.

## Curve and colour
- **Curve** (library nonland MV 0/1/2/3/4/5/6/7+): 0/12/32/11/5/1/1/2 → 0/13/29/13/5/1/1/2.
- **Average nonland MV:** 2.44 → 2.45 (library only).
- **Library coloured pips (U/B/R):** 12/32/11 → 13/30/11.
- **Lord's cost:** {1}{U}{B}{R} needs all three colours.
- **Turn-4 deployment** improves 0.2717 → 0.3068. Ornithopter alone gives 0.2879. That is because the creature count, not the colour count, was the binding constraint on paying the trigger.

## Hypergeometric opening 7
35 lands in a 99-card library: P(2–4 lands) 0.7306, P(1–3 lands) 0.7603, P(1–4 lands) 0.9069. These are unchanged.

## Judgment
HIGH confidence that the land base needs no change. Distortion Strike over Rogue's Passage (the Pass C 34-land case) measured 0.6490 against 0.6613 for the candidate, so it is kept as an alternative, not selected.

## Model caveats
- Seeded goldfish with one land drop per turn. Tapped lands are played on turns 1–2 and untapped lands afterwards. Fetches find an on-colour typed dual.
- No opponents, no interaction and no tutors.
- Treasure from Black Market Connections is not spent.
