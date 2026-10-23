# Inalla, Archmage Ritualist — M6 I local-best memo for the M7 research candidate (2026-10-23)

This memo is evidence only. The candidate is NOT owner approved, NOT M6 certified and NOT owner-presentable. It is RESEARCH_ONLY: zero genuine swaps, below the five-swap floor. The canonical list is unchanged.

Scope: the nine complete configurations in `data/grixis/m6/ij/tested_pools/Inalla__Archmage_Ritualist_M7_tested_configurations_20261023.json`, plus named single-card contenders. Each configuration is 100 cards (1 commander + 99 library). This is not a global or statistical optimum.

Baseline:
- Source: canonical encyclopedia main 9b26aa28fc7e16f6652aaec292b4edf84e20db71, file `refinement/decklists/Inalla_Archmage_Ritualist_Approved_2026-10-14.txt`.
- Blob 204b8096, introduced by afb35c06. Registry source_commit 1836b97 has the same bytes.
- Raw SHA-256 81333ac7… equals the registry's recorded_sha256, so no provenance exception is used.

## Result
The research candidate (raw 916e056b…, lh1:c3f63347…) is the canonical 100 re-serialized, with the same logical hash. It is the local best of the tested pool among configurations that respect owner direction.

**Zero genuine improvements were found, so the deck is RESEARCH_ONLY.** Five is a floor, not a target. Nineteen candidates were judged and twelve incumbents were challenged. Every candidate failed for one of these reasons:
- **Owner-removed or owner-rejected:** Dualcaster Mage and Snapcaster Mage (removed 2026-10-14), Micromancer, Spectral Arcanist and Samut, Tyrant of Naktamun (rejected).
- **Marginal or redundant:** Defense Grid, Gifts Ungiven, Tishana's Tidebinder, Crystal Vein, Tarnished Citadel, Jeweled Amulet, The One Ring, Mindbreak Trap, Phantasmal Image, Buried Alive and Grim Tutor.
- **No commander value:** Twinflame makes tokens, and tokens do not trigger Eminence (the "nontoken" clause).
- **Invalid:** Dockside Extortionist is banned; Culling Ritual is off-identity (B/G).

None of these was counted. All twelve challenged incumbents were kept: Kefka, Court Mage // Kefka, Ruler of Ruin, Thundertrap Trainer, Apprentice Necromancer, Blood Pet, Wheel of Fortune, Lim-Dûl's Vault, Hoarding Broodlord, Exotic Orchard, Fellwar Stone, Red Elemental Blast, Final Fortune and Otawara, Soaring City.

## Why (commander-first)
Inalla, Archmage Ritualist ({2}{U}{B}{R} 4/5 Legendary Creature — Human Wizard):
- Eminence: "Whenever another nontoken Wizard you control enters, if Inalla is in the command zone or on the battlefield, you may pay {1}. If you do, create a token that's a copy of that Wizard. The token gains haste. Exile it at the beginning of the next end step."
- "Tap five untapped Wizards you control: Target player loses 7 life."

**Strongest change: +Dualcaster Mage −Kefka.**
- Dualcaster Mage is a Human Wizard with flash for {1}{R}{R}. With Saw in Half (Spellbook 147-500) or Essence Flux (147-4598), both already in the 99, it makes two new complete combos (16 → 18).
- Lands-only castability at 10 cards seen: Dualcaster's RR is 0.4605; Kefka's five lands is 0.0958.
- But the owner explicitly removed Dualcaster Mage on 2026-10-14, and the brief forbids re-adding removed cards. It is RETAIN_ALTERNATIVE as an OWNER DECISION and not counted.

**Kefka is kept** as an owner addition:
- It is a Wizard, so Eminence copies its ETB.
- The copy is legendary; the ETB still resolves before the legend rule removes one (Pass C ruling note).

## Owner direction
- Every incumbent is owner-directed: 50 explicit retained cards plus 49 owner additions. No cut was clearly better on evidence, so **no owner keep or addition is overridden**.
- **Owner-removed cards are not re-added:** Dualcaster Mage, Snapcaster Mage, Archaeomancer, Brainstorm, Fierce Guardianship, Deflecting Swat, Force of Negation, Naban, Dean of Iteration, Kess, Dissident Mage, Patron Wizard and the Panharmonicon / Molten Echoes Wizard-value class.
- **Owner-rejected cards are not re-added:** Micromancer, Spectral Arcanist, Samut, Orcish Bowmasters, Valley Floodcaller, Pyroblast, Daze, Into the Flood Maw, Dispel, Corpse Dance, Dance of the Dead, Necromancy, Starting Town, Training Center, Forbidden Orchard and Phyrexian Tower.
- The staged alternatives are complete 100s on the baseline, so the owner can pick one directly.

## Pass C requested tests (bounded finite versions; not win rates)
These are in `data/grixis/m7/research_challengers/Inalla__Archmage_Ritualist_bounded_measured_tests_20261023.json` and recomputed in `tests/test_m6_inalla_archmage_ritualist_m7_mechanics.py`.

Pass C's final disposition was **NEEDS TESTING**. It asked for a targeted Phase B: the locked baseline vs −Kefka +Dualcaster Mage and −Kefka +Micromancer (optionally −Thundertrap Trainer +Snapcaster Mage), on the same 27-land UBR mana, measuring RR vs U castability, tutor reach and combo deltas. The Pass C receipt is a NON-INDEPENDENT owner-equivalent review (same model family, with a technical-independence waiver).

1. **T1 castability.** Exact hypergeometric, lands only, 10 cards seen (turn 4 on the play):

   | Card | Requirement | Probability |
   |---|---|---|
   | Dualcaster Mage | RR | 0.4605 |
   | Kefka | five lands | 0.0958 |
   | Micromancer | four lands with U | 0.2717 |
   | Snapcaster Mage / Thundertrap Trainer | two lands with U | 0.8045 |

   Rocks and rituals were ignored for all variants equally.
2. **T2 tutor reach.** Spellseeker reaches 33 instants and sorceries in the 99; Micromancer reaches 20. Micromancer misses 13, including Demonic Tutor, Tainted Pact, Finale of Promise, Brain Freeze and Pact of Negation.
3. **T3 combos.** Commander Spellbook find-my-combos:
   - Baseline: 16 included.
   - Dualcaster alternatives: 18 (147-500, 147-4598).
   - Every other staged list: no new combo.
4. **T4 Thundertrap Trainer.** 58 noncreature, nonland cards in the 99. P(at least one hit in the top 4) is 0.973098; with an Eminence copy (8 cards) it is 0.999442. Snapcaster Mage has the same castability but needs a graveyard target.
5. **T5 rules facts.** From Oracle and official rulings: the intervening-if clause (CR 603.4), last-known information, the tap-five cost without {T} (CR 302.6) and Samut's split second (CR 702.61a).

Not done, stated plainly: there were no matched-hand games, no opponent model and no win rates. The repo has no validated Inalla game engine.

## Self-challenge
- **Pass C exact (+Dualcaster Mage −Kefka):** staged; RETAIN_ALTERNATIVE as an OWNER DECISION (owner-removed).
- **Pass C competing (+Micromancer −Kefka):** staged and rejected. Micromancer is owner-rejected, its reach is 20 vs 33, and its castability is 0.2717.
- **Pass C optional (+Snapcaster Mage −Thundertrap Trainer):** staged and rejected. Snapcaster is owner-removed, and the Trainer is an owner addition with an exact 0.973 hit rate.
- **Two-swaps:**
  - +Dualcaster +Snapcaster / −Kefka −Thundertrap Trainer (the Pass C union; OWNER DECISION).
  - +Defense Grid +Gifts Ungiven / −Kefka −Blood Pet (rejected; it cuts owner additions for marginal value).
  - Neither was counted.
- **One-swap data challenge:** Tishana's Tidebinder over Thundertrap Trainer was staged and rejected (owner addition; lower hit value).
- **Mana challenges:** Crystal Vein and Tarnished Citadel over Exotic Orchard and Otawara were rejected; the 27-land UBR mana is kept.
- **Rejected singles:** Defense Grid, Gifts Ungiven, Tishana's Tidebinder, Crystal Vein, Tarnished Citadel, Jeweled Amulet, The One Ring, Mindbreak Trap, Phantasmal Image, Twinflame, Buried Alive, Grim Tutor, Spectral Arcanist, Samut, Micromancer and Snapcaster Mage. Dockside Extortionist is banned; Culling Ritual is off-identity.

## Limits
Only finite scripted rules cases and exact enumerations are tested.

- Game Changers 18 → 18 (Bracket 5).
- Average nonland MV 2.0 → 2.0.
- Commander Spellbook 16 → 16 complete combos.
