# Cycle 125 — External GrokBot review intake and Cycle119 restricted-mana erratum

## Source custody and independent-review status
- Received GrokBot original non-author M6 Pass C review on 2026-10-19 as uploaded files:
  - `GrokBot_PassC_Review_Cycle124_2026-10-19.md`: SHA-256 `aed0c43159731a4aba6dfa7a13662a7bb0d8ca7d1fa1365210be15d3f07d80c0`
  - `GrokBot_PassC_Review_Cycle124_2026-10-19.json`: SHA-256 `31a26b65f1fba3e1e678196036b92d6175b0b6e8712d83cedb0c6a91af9abb85`
- Original reviewer disclosed previous GrokBot project/blueprint exposure, but no access to original author judgments for these three swaps before recording its verdicts. **Not strictly blinded; not fully independent of initial blueprint framing.** Do not promote to formal 62/62 Pass C.
- Reviewer source-locked verdicts: Gwendlyn `KEEP Opposition Agent` (moderate); Nicol Bolas the Ravager `REPLACE Mox Diamond with Aetheric Amplifier` (low/moderate **conditional on additional tests**); Mai and Zuko `KEEP An Offer You Can't Refuse` (moderate).
- All judgments are advisory. No approved, locked deck was unlocked or edited. Zero formal M6 certifications.

## Rules correction — original Cycle119 result was invalid
Original `scripts/grixis_m6_cycle119_bounded_effects.py::rings_copy()` paid the {2} on Rings of Brighthearth's **triggered ability** using The Enigma Jewel's restricted {C}{C}. Jewel says that mana may be spent only to **activate abilities**, so the attempted direct Rings payment was not legal. Historic successful CI [#39189755415](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/39189755415) and its related artifact must **not** be cited as proof that this original payment line was rules-correct. Preserve its original artifact in place, marked **SUPERSEDED_FOR_MAI_RINGS_PAYMENT**.

The corrected finite conditional line, presuming all three artifacts are present and untapped at the relevant priority window, is:
1. Tap Basalt Monolith for three *ordinary* {C}.
2. Tap Jewel for two *activated-ability-only* {C}; this presumes it entered on an earlier turn and has untapped since.
3. Activate Basalt's {3} untap ability, spending two restricted Jewel mana plus one ordinary mana. Two ordinary {C} remain.
4. Rings triggers; pay its {2} using the remaining **ordinary** mana, not restricted Jewel mana. Create a copy of Basalt's untap ability.
5. Resolve copy, untap Basalt; tap it for three ordinary {C} before original untap resolves.
6. Resolve original untap; Basalt ends untapped, with three ordinary {C} floating in the same phase.

This correct conditional trace is **not** a source-backed deck-game simulation, infinite-mana finding, actual opponent-response event, win rate, or proof of a swap advantage. The old test's result field has been corrected to `spent_restricted_C_on_rings_trigger: 0` and the paid Basalt activation/ordinary Rings payment recorded separately. Atomic negative tests reject using Jewel-restricted-only mana for Rings.

## Remaining independent discrepancies
- Bolas review's theme-first `REPLACE` recommendation is provisional; actual Mox timing, artifacts, activation windows, full planeswalker deployment costs and interaction remain untested.
- Jewel's current front cost is {U}, not generic. Front supertype Legendary and Nicol Bolas, the Arisen's initial seven loyalty are missing from some abbreviated packet representations and should be carried into complete Oracle verification.
- Grok correctly rules Jewel cannot fund Rings' trigger **directly**, but this does not establish that Jewel can never support the Monolith/Rings engine indirectly.
- No new formal Pass C completion, local zero-improvement certificate, independent blind reviewer, complete Phase B gameplay proof, M6/M7 acceptance or canonical approval is claimed.

## Gate status
- M0–M5: accepted; M6: in progress, secondary gate checklist **3/10 completed** plus two partial.
- M7: not started, secondary gate checklist **0/6**.
- Canonical approved/locked 62/62; formal M6-certified 0/62; M8-certified 0/62.
- Next task is independent source/review provenance qualification and effect-aware stress/decision evidence, not applying these three candidate swaps.
