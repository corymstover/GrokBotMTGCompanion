# Jeleva, Nephalia's Scourge — M7 research-candidate mana analysis (2026-10-23)

Counted by quantity from the candidate Oracle snapshot. Land counts and measured values are asserted in `tests/test_m6_jeleva_nephalias_scourge_m7_mechanics.py`.

**Lands.** 27 → 27, with no MDFCs and no land changes (1 Island, 1 Swamp, 25 nonbasic).
- Coloured land sources, U/B/R: 21/20/19 → 21/20/19. Fetches and rainbow lands are counted for each colour. Only "Add …" clauses are parsed. That is why the challenger Hanweir Battlements, which adds only {C}, would drop R to 18.
- Colourless lands: Ancient Tomb and City of Traitors. Gemstone Caverns is any colour only with a luck counter; Exotic Orchard is opponent-dependent.

**Mana rocks and fast mana** are unchanged: Sol Ring, Mana Vault, Grim Monolith, Arcane Signet, Fellwar Stone, Talisman of Creativity, Talisman of Dominance, Chrome Mox, Mox Diamond, Mox Opal, Lotus Petal and Lion's Eye Diamond, plus Dark Ritual, Cabal Ritual, Rite of Flame and Simian Spirit Guide.

**Curve and colour.**
- Curve (nonland printed MV 0/1/2/3/4/5/6/7): 6/27/19/15/1/2/1/1 → unchanged.
- Average nonland MV 1.9 → 1.9.
- Coloured pips (nonland mana costs, front face, Phyrexian {U/P} excluded), U/B/R: 29/25/15 → unchanged.

**Hypergeometric opening 7** (27 lands in a 99-card library): P(2–4 lands) 0.6023, P(1–3 lands) 0.8154 and P(1–4 lands) 0.8857. These are unchanged; the deck is built to keep 1–2 land hands with fast mana.

**Jeleva access** (exact, bounded T1/T3): P(at least one stager) is 0.5736–0.7103, and P(at least one haste/flash enabler) is 0.2577–0.3514, over 7–10 cards seen.

**Judgment (HIGH confidence):** the mana is unchanged. Exotic Orchard, Arena of Glory, Gemstone Caverns, Fellwar Stone and Mox Opal were challenged and kept. These were rejected:
- Forbidden Orchard: no colour gain, and it gives opponents tokens.
- Hanweir Battlements and Hall of the Bandit Lord: each loses a red source.
- Starting Town: marginal.
- Mox Amber: only two legendary creatures.

Model caveats:
- Each fetch counts as one source of either needed colour.
- Exotic Orchard counts as any colour (optimistic).
- Rocks and rituals are ignored (conservative, equally for all variants).
