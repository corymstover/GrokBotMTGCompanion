# Cormela, Glamour Thief — M7 candidate mana analysis (2026-10-23)

Counted by quantity from the candidate Oracle snapshot. Land counts, Mountain-typed lands and fetch reach are asserted in `tests/test_m6_cormela_glamour_thief_m7_mechanics.py`.

- **Lands:** 30 physical in both lists (27 nonbasic + Island + Mountain + Swamp).
  - Always-tapped lands: 1 → 0. Undercity Sewers is out.
  - Mistrise Village is the only conditional land. It enters untapped with any of Badlands, Blood Crypt, Mountain, Steam Vents or Volcanic Island, and each of the 7 fetches can find one of those.
  - Luxury Suite, Morphic Pool and Training Center enter untapped in multiplayer, as before.
- **Mana artifacts:** 13 in both lists: Sol Ring, Mana Vault, Chrome Mox, Mox Diamond, Mox Opal, Lotus Petal, LED, Arcane Signet, three Talismans, Ashnod's Altar and Phyrexian Altar.
- **Rituals and converters (instants/sorceries that make unrestricted mana):** Dark Ritual, Cabal Ritual, Culling the Weak, Rite of Flame, Seething Song and Jeska's Will, plus Frantic Search, which untaps three lands for a net +2 when paid with Cormela's mana. Simian Spirit Guide is unchanged.
- **Colored land sources (heuristic: fetches counted by the basic types they name; any-color lands count all three):**
  - U/B/R 19/18/17 → 19/17/16.
  - The drop is Exotic Orchard (counted as any color) and Sewers (U/B) leaving, with Underground River (U/B) and Mistrise (U) coming in.
  - The heuristic undercounts fetches: every fetch can reach a U/B/R typed dual (Underground Sea, Badlands, Volcanic Island, Watery Grave, Blood Crypt, Steam Vents). So real fetchable color access for each of U, B and R is higher than shown.
- **Curve (nonland printed MV 0/1/2/3/4/5):** 6/25/18/16/2/2 → 6/22/20/17/2/2. Average nonland MV 1.841 → 1.899 (Frantic Search 3 for Looting 1; Twinflame 2 and Squelcher 2 for two 1-drops).
- **Hypergeometric (99-card library, Cormela in the command zone):** P(2–5 lands in the opening 7) = 0.683 in both lists (30 lands each).
  - What changes is land quality: no always-tapped land, and a guaranteed U/B source replaces a conditional one.
- **Judgment (MODERATE confidence):** turn-2/3 Cormela ({1}{U}{B}{R}) is slightly more reliable on the untapped-land axis and slightly less on the raw black/red count. Frantic Search adds mana conversion on the combo turn.
