# Kess, Dissident Mage — M7 research-candidate mana analysis (2026-10-23)

Counted by quantity from the candidate Oracle snapshot. Land counts, colour sources and measured values are asserted in `tests/test_m6_kess_dissident_mage_m7_mechanics.py`.

**Lands.** 27 → 27, no basics, no MDFCs and no land changes.
- Coloured land sources, U/B/R: 21/18/19 → 21/18/19. Fetches and rainbow lands are counted for each colour they can produce or find. Only "Add …" clauses and land subtypes are parsed.
- Lands with fewer than three colours: colourless Ancient Tomb, City of Traitors and Gemstone Caverns (any colour only with a luck counter); B/R Badlands, Blood Crypt, Luxury Suite; U/R Fiery Islet, Steam Vents, Training Center, Volcanic Island; U Mistrise Village, Otawara, Soaring City; U/B Morphic Pool, Underground Sea, Watery Grave.

**Mana rocks and fast mana** are unchanged: Sol Ring, Mana Vault, Grim Monolith, Arcane Signet, Fellwar Stone, Talisman of Creativity, Talisman of Dominance, Talisman of Indulgence, Chrome Mox, Mox Diamond, Mox Opal, Lotus Petal and Lion's Eye Diamond, plus Dark Ritual, Cabal Ritual, Rite of Flame and Simian Spirit Guide.

**Curve and colour.**
- Curve (nonland printed MV 0/1/2/3/4/5+): 6/27/20/12/5/2 → 6/26/21/12/5/2.
- Average nonland MV 1.85 → 1.86.
- Coloured pips (nonland mana costs, front face), U/B/R: 30/22/13 → 31/22/13. Mana Drain needs {U}{U}; 21 blue land sources plus Arcane Signet, Talisman of Creativity, Talisman of Dominance, Fellwar Stone, the Moxen and Lotus Petal cover it. Bounded P({U}{U} available) turns 2–6: 0.5028/0.6688/0.7442/0.7973/0.8395 (lands plus Signet/Talismans only; conservative).
- First Kess deployment (four mana with U, B and R) turns 3–6: 0.1215/0.3577/0.4488/0.5328, identical for baseline and candidate.

**Hypergeometric opening 7** (27 lands in a 99-card library): P(2–4 lands) 0.6023, P(1–3 lands) 0.8154 and P(1–4 lands) 0.8857. These are unchanged; the deck is built to keep 1–2 land hands with fast mana.

**Judgment (HIGH confidence):** the land base is unchanged and the candidate's one extra blue pip is covered. City of Traitors, Fellwar Stone and Rite of Flame were challenged and kept. These were rejected:
- Undercity Sewers over City of Traitors: enters tapped in a turbo list; the colour gain is small.
- Urza's Saga over City of Traitors: colourless like City but slow (the chapter III tutor arrives two turns later, then the Saga sacrifices itself); no colour gain and no immediate burst toward Kess.
- Exotic Orchard over City of Traitors: opponent-dependent and low synergy with nine fetches, four duals, City of Brass, Mana Confluence and Command Tower.
- Spell Pierce + Mana Drain over Personal Tutor + Fellwar Stone: cutting a two-mana rock slows a four-mana commander.

Model caveats:
- Each fetch counts as one source of either needed colour.
- Gemstone Caverns is counted colourless (conservative).
- Moxen, Lotus Petal, Lion's Eye Diamond, Sol Ring, Mana Vault, Grim Monolith and rituals are ignored in the turn tables (conservative, equally for all variants).
