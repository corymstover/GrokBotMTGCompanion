# Inalla, Archmage Ritualist — M7 research-candidate mana analysis (2026-10-23)

Counted by quantity from the candidate Oracle snapshot. Land counts and measured values are asserted in `tests/test_m6_inalla_archmage_ritualist_m7_mechanics.py`.

**Lands.** 27 → 27, with no MDFCs and no land changes (1 Island, 1 Swamp, 25 nonbasic).
- Coloured land sources, U/B/R: 20/19/17 → 20/19/17. Fetches, rainbow lands and Cavern of Souls (naming Wizard) are counted for each colour.
- Colourless lands: Ancient Tomb and City of Traitors. Gemstone Caverns is any colour only with a luck counter.

**Mana rocks and fast mana** are unchanged: Sol Ring, Mana Vault, Grim Monolith, Arcane Signet, Fellwar Stone, Talisman of Dominance, Talisman of Indulgence, Chrome Mox, Mox Diamond, Mox Opal, Lotus Petal and Lion's Eye Diamond, plus Dark Ritual, Cabal Ritual, Simian Spirit Guide and Blood Pet.

**Curve and colour.**
- Curve (nonland printed MV 0/1/2/3/4/5/7+): 6/25/25/7/2/5/2 → unchanged.
- Average nonland MV 2.0 → 2.0.
- Coloured pips (nonland mana costs, front face), U/B/R: 25/37/13 → unchanged.

**Hypergeometric opening 7** (27 lands in a 99-card library): P(2–4 lands) 0.6023, P(1–3 lands) 0.8154 and P(1–4 lands) 0.8857. These are unchanged; the deck is built to keep 1–2 land hands with fast mana.

**Pass C Wizards** (exact, lands only, 10 cards seen):
- Dualcaster Mage RR: 0.4605.
- Kefka (five lands): 0.0958.
- Micromancer (four lands with U): 0.2717.
- Snapcaster Mage / Thundertrap Trainer: 0.8045.

**Judgment (HIGH confidence):** the mana is unchanged. Exotic Orchard, Fellwar Stone and Otawara, Soaring City were challenged and kept. Crystal Vein and Tarnished Citadel were rejected (colourless, or damage for no gain over the current rainbow lands).

Model caveats:
- Each fetch counts as one source of either needed colour (fetch reach is verified in the receipt).
- Exotic Orchard counts as any colour (optimistic).
- Rocks and rituals are ignored (conservative, equally for all variants).
