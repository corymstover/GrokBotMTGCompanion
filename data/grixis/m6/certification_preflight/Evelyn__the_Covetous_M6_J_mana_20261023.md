# Evelyn, the Covetous — M7 candidate mana analysis (2026-10-23)

Counted by quantity from the candidate Oracle snapshot. Land counts and the measured values are asserted in `tests/test_m6_evelyn_the_covetous_m7_mechanics.py`.

- **Lands:** 26 physical in both lists (one basic Island, one basic Swamp, 24 nonbasic). Thundering Falls and Blazemire Verge out; Marsh Flats and Verdant Catacombs in.
  - Coloured land sources (fetches and rainbow lands counted for each colour they can produce): U/B/R 19/19/19 → 20/20/19. Colourless-only lands: Ancient Tomb, City of Traitors. Always-tapped lands 1 → 0; Mistrise Village stays conditional (untapped with a Mountain).
  - Fetches 7 → 9 for 8 Swamp/Island/Mountain-typed targets (4 original duals, 3 shocks, the basic Swamp and Island).
- **Mana rocks and fast mana (unchanged):** Sol Ring, Mana Vault, Arcane Signet, Fellwar Stone, Talisman of Dominance, Talisman of Indulgence, Lotus Petal, Chrome Mox, Mox Diamond, Mox Opal, Lion's Eye Diamond; rituals Dark Ritual, Cabal Ritual, Culling the Weak, Rite of Flame, Simian Spirit Guide. Burnt Offering is a new sacrifice ritual.
- **Curve (nonland printed MV 0/1/2/3/4/5/6/7+):** 6/26/25/10/3/2/1/0 → 6/28/23/10/3/2/1/0. Average nonland MV 1.836 → 1.808.
- **Coloured pips (nonland, hybrid counted for each colour):** U/B/R 28/29/16 → 27/30/16.
- **Hypergeometric (99-card library, 26 lands):** P(2–4 lands in the opening 7) = 0.5805 and P(1–4) = 0.8778, unchanged.
- **Exact castability (lands plus rocks one each; moxen, rituals and LED excluded, so these are floors):**
  - Evelyn by turn 4 on the play 0.1491 → 0.1491; on the draw 0.2086 → 0.2087. By turn 5 on the play 0.2767 → 0.2768.
  - A U source for Brainstorm on turn 1: 0.8385/0.8771 → 0.8531/0.8899 (play/draw).
  - A fetch in the first 7 cards: 0.4115 → 0.4981.
- **New coloured costs:** Insolent Neonate {R}, Brainstorm {U}, Burnt Offering {B}; the two fetches cost 1 life each.
- **Judgment (MODERATE confidence):** the land base loses one tapped land and one conditional dual for two untapped fetches; Evelyn castability is unchanged and early selection improves. Cost: 2 more life-paying lands (fetches plus a shock is up to 3 life) and more exposure to Stifle-style effects and opposing fetch punishers; Blazemire Verge was the Stifle-proof B/R source.

Model caveat: each fetch is counted as a source of any one Grixis colour (true: each reaches a dual for every needed colour, but only one per fetch), and Gemstone Caverns and Exotic Orchard are counted as rainbow (Caverns needs the opening-hand luck counter, Orchard depends on opponents' lands). Absolute figures are slightly optimistic for every tested list alike.
