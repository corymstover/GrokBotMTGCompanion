# Kefka, Court Mage // Kefka, Ruler of Ruin — M7 research-candidate mana analysis (2026-10-23)

Counted by quantity from the candidate Oracle snapshot. Land counts, colour sources and measured values are asserted in `tests/test_m6_kefka_court_mage_m7_mechanics.py`.

**Lands.** 28 → 28, with no MDFCs and no land changes (1 Island, 27 nonbasic).
- Coloured land sources, U/B/R: 21/20/20 → 21/20/20. Fetches and rainbow lands are counted for each colour they can produce or find. Only "Add …" clauses and land subtypes are parsed.
- Lands with fewer than three colours: colourless Ancient Tomb, City of Traitors and Gemstone Caverns (any colour only with a luck counter); R Arena of Glory; B/R Badlands, Blood Crypt, Luxury Suite; U/B Morphic Pool, Underground Sea, Watery Grave; U Island, Otawara, Soaring City; U/R Steam Vents, Volcanic Island.
- Mountain-subtype sources for Anger and Arena of Glory: 13 (4 duals plus 9 fetches); P(at least one) 0.6391 on turn 1 to 0.8346 on turn 6.

**Mana rocks and fast mana** are unchanged: Sol Ring, Mana Vault, Grim Monolith, Arcane Signet, Fellwar Stone, Talisman of Creativity, Talisman of Dominance, Chrome Mox, Mox Diamond, Mox Opal, Lotus Petal and Lion's Eye Diamond, plus Dark Ritual, Cabal Ritual, Rite of Flame and Simian Spirit Guide. The cut removes Culling the Weak (a creature-gated black ritual).

**Curve and colour.**
- Curve (nonland printed MV 0/1/2/3/4/5): 6/22/23/12/6/2 → 6/21/23/13/6/2.
- Average nonland MV 1.94 → 1.97.
- Coloured pips (nonland mana costs, front face), U/B/R: 24/26/17 → 24/25/19. Dualcaster Mage needs {R}{R}; 20 red land sources plus Talisman of Creativity, Arcane Signet, Fellwar Stone, Chrome Mox, Mox Diamond, Lotus Petal and Rite of Flame cover it.

**Hypergeometric opening 7** (28 lands in a 99-card library): P(2–4 lands) 0.623, P(1–3 lands) 0.8138 and P(1–4 lands) 0.8924. These are unchanged; the deck is built to keep 1–2 land hands with fast mana.

**Judgment (HIGH confidence):** the land base is unchanged and the candidate's extra red pips are covered. Island, Arena of Glory, Starting Town, Fellwar Stone and Talisman of Creativity were challenged and kept. These were rejected:
- Mistrise Village over Island: Cavern of Souls and Hexing Squelcher already make Kefka uncounterable; it enters tapped and removes the only basic.
- Mox Amber over Fellwar Stone: few legendaries.
- Urza's Saga over Starting Town: loses a coloured source.
- Generator Servant over Arena of Glory: a one-shot haste creature replacing a land.
- Talisman of Indulgence is the staged fallback for the Culling slot if Dualcaster Mage is declined.

Model caveats:
- Each fetch counts as one source of either needed colour.
- Gemstone Caverns is counted colourless (conservative).
- Rocks and rituals are ignored in the source counts (conservative, equally for all variants).
