# Grixistax___October_2026 (Kraum, Ludevic's Opus + Tevesh Szat, Doom of Fools) — M7 research-candidate mana analysis (2026-10-23)

Counted by quantity from the candidate Oracle snapshot. Land counts, the swaps and measured values are asserted in `tests/test_m6_grixistax_october_2026_m7_mechanics.py`.

**Lands.** 26 → 26, including one Island, one Swamp and one Mountain, with no land changes.
- Coloured land sources, U/B/R: 19/19/17 → 19/19/17. Fetches and rainbow lands are counted for each colour they can produce or find. Only "Add …" clauses and land subtypes are parsed.
- Lands with fewer than three colours: colourless Ancient Tomb and Gemstone Caverns (any colour only with a luck counter); B/R Badlands, Blood Crypt; U/R Steam Vents, Volcanic Island; U/B Morphic Pool, Underground Sea, Watery Grave; U Island, Otawara, Soaring City; B Swamp, Phyrexian Tower; R Mountain.
- Under our own Contamination every land taps for {B} only; under our own Blood Moon / Magus of the Moon nonbasic lands tap for {R}; under Back to Basics our nonbasic lands do not untap. Coloured rocks are unaffected (CR 305.7 and Contamination's land-only replacement).

**Mana rocks and fast mana.** Candidate: Sol Ring, Mana Vault, Grim Monolith, Arcane Signet (new), Talisman of Creativity, Talisman of Dominance, Chrome Mox, Mox Diamond, Mox Opal, Lotus Petal and Lion's Eye Diamond, plus Dark Ritual. Mox Amber is cut.

**Curve and colour.**
- Curve (nonland printed MV 0/1/2/3/4/5+): 8/18/18/19/8/1 → 7/18/20/18/8/1.
- Average nonland MV 2.06 → 2.07.
- Coloured pips (nonland mana costs, front face), U/B/R: 24/26/10 → 23/27/10.
- Commanders: Kraum {3}{U}{R}, Tevesh {4}{B}. Bounded P(five mana including B for Tevesh) by turn 4: 0.1526 → 0.1657.

**Hypergeometric opening 7** (26 lands in a 98-card library): P(2–4 lands) 0.5865, P(1–3 lands) 0.8157 and P(1–4 lands) 0.8801. These are unchanged; the deck keeps 1–2 land hands with fast mana.

**Lock-state colour access (bounded, turn 4).** Under Contamination P(U): baseline 0.2788, candidate 0.3299; P(UU) 0.0377 → 0.0533. Under Blood Moon the baseline has P(U) 0.7587. Full tables are in the bounded measured-tests receipt.

**Judgment (MODERATE confidence for the rock swap; HIGH that the land base needs no change):**
- Arcane Signet over Mox Amber improves mean mana and colour access in every lock state; Talisman of Indulgence, the Pass C challenger, has the same raw mana but no blue and is dominated.
- Gemstone Caverns was challenged and kept (partner cEDH 73/81). These were rejected:
  - Strip Mine and Urza's Saga over Gemstone Caverns: both lose their abilities under our own Moon effects.
  - Undercity Sewers over Gemstone Caverns: enters tapped.
  - City of Traitors over Arid Mesa: Arid Mesa is an owner addition; the colourless burst does not clearly beat fetch fixing under our colour locks.
  - Fellwar Stone over Mox Amber: dominated by Arcane Signet (its colours depend on opponents' lands, which our own Moon and Contamination also rewrite).

Model caveats:
- Seeded goldfish: one land drop per turn, rocks deployed greedily, fetches resolved to a typed dual or basic; no mulligans, no opponents, no interaction.
- Gemstone Caverns is counted colourless (conservative).
- Lion's Eye Diamond, Lotus Petal and Dark Ritual are treated as one-shot and do not count as persistent sources.
