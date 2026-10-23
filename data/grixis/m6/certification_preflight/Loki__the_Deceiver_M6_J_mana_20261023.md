# Loki__the_Deceiver (Loki, the Deceiver) — M7 research-candidate mana analysis (2026-10-23)

Counted by quantity from the candidate Oracle snapshot (`data/grixis/m6/oracle_snapshots/Loki__the_Deceiver_M7_Scryfall_20261023.json`). Land counts, the swaps and the measured values are asserted in `tests/test_m6_loki_the_deceiver_m7_mechanics.py`.

**Lands.** 34 → 34, with no land changes. Basics: 3 Island, 3 Swamp, 2 Mountain.
- Coloured land sources, U/B/R: 21/20/20 → 21/20/20. Fetches and any-colour lands (Command Tower, Mana Confluence, Exotic Orchard, Path of Ancestry, Oscorp Industries, Xander's Lounge) count for each colour they can produce or find. Cavern of Souls and Villainous Hideout count as any colour; they are restricted, but restricted to Villain creature spells, which is most of the deck's coloured spells. Only "Add …" clauses and land subtypes are parsed.
- Lands with fewer than three colours: colourless Hall of Echoes; Urborg, Tomb of Yawgmoth (it makes {B} through its static ability); B/R Badlands, Blood Crypt, Dragonskull Summit, Luxury Suite; U/B Drowned Catacomb, Morphic Pool, Underground Sea, Watery Grave; U/R Steam Vents, Sulfur Falls, Training Center, Volcanic Island; U Island, Otawara, Soaring City; B Swamp; R Mountain.

**Mana rocks and fast mana.** Unchanged: Sol Ring, Arcane Signet, Talisman of Creativity, Talisman of Dominance, Talisman of Indulgence, Patchwork Banner, Loki's Scepter, The Soul Stone; plus Dark Ritual, Jeska's Will and the Black Market Connections Treasure mode. The Villain cost reducers Baron Strucker, HYDRA Overlord and Tombstone, Career Criminal, and Urza's Incubator (naming Villain) are unchanged.

**Curve and colour.**
- Curve (library nonland printed MV 0/1/2/3/4/5/6/7+): 0/5/15/18/16/4/4/3 → 0/5/15/16/17/4/5/3. (The decision review's MV4 17 → 18 counts Loki; MV7 2 and MV9 1 are the 7+ bucket.)
- Average nonland MV 3.38 → 3.45 (library only; 3.394 → 3.455 including Loki).
- Coloured pips, U/B/R. Library front faces: 27/34/15 → 27/37/14. All mana costs, including Loki and both faces of Norman Osborn // Green Goblin: 29/36/17 → 29/39/16.
- Both adds are double-black ({4}{B}{B} and {2}{B}{B}). That is supported by 20 black land sources, the B-producing rocks and Dark Ritual.

**Hypergeometric opening 7** (34 lands in a 99-card library): P(2–4 lands) 0.7195, P(1–3 lands) 0.7721 and P(1–4 lands) 0.9081. These are unchanged.

**Bounded deployment** (seed 28, 20,000 games, on the play, no mulligans):
- P(Loki on battlefield by turn 4): 0.6242 → 0.6195.
- P(Loki attacks with a valid Villain target): turn 4 0.1803 → 0.1682; turn 5 0.5849 → 0.5696.
- P(Villain with MV ≤3 deployed by turn 3): 0.3005 → 0.2567.

The cost of the two swaps is the curve: the deck loses two three-drops.

**Judgment (HIGH that the land base needs no change):**
- Secluded Courtyard over Path of Ancestry measured about one point better on attack timing (turn 4 0.1682 → 0.1767; turn 5 0.5696 → 0.5803; noise about ±0.5 points). It is rejected as marginal. Its coloured mana works only for Villain creature spells and abilities, so it gives {C} to Mana Drain, Rhystic Study, Demonic Tutor, Toxic Deluge, Dark Ritual, Jeska's Will and Chaos Warp, which a deployment goldfish undercounts.
- Ancient Tomb was rejected: colourless burst in a deck with 37 black front-face pips, and it would be a sixth Game Changer.

Model caveats:
- Seeded goldfish with one land drop per turn; tapped lands are played on turns 1–2 and untapped lands afterwards; check-lands follow their typed condition; fetches find an on-colour typed dual.
- No opponents, no interaction and no tutors.
- Dark Ritual, Jeska's Will, Treasure and Urza's Incubator are not used (conservative).
