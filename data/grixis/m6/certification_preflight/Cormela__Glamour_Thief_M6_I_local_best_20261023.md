# Cormela, Glamour Thief — M6 I local-best memo for the M7 candidate (2026-10-23)

This memo is evidence only. The candidate is NOT owner approved and NOT M6 certified, and the canonical list is unchanged.

Scope: the seven complete configurations in
`data/grixis/m6/ij/tested_pools/Cormela__Glamour_Thief_M7_tested_configurations_20261023.json`, plus named single-card contenders. Each configuration is 100 = 1 commander + 99 library. This is not a global or statistical optimum.

## Result
The preferred five (raw 1cb098f4…) is the local best of the tested pool:
- Adds: +Mistrise Village, +Underground River, +Frantic Search, +Twinflame, +Hexing Squelcher.
- Cuts: −Undercity Sewers, −Exotic Orchard, −Faithless Looting, −Gitaxian Probe, −Red Elemental Blast.

## Why
Cormela's mana ({1},{T}: {U}{B}{R}) can only cast instants and sorceries. Her death trigger returns one instant or sorcery. The approved list wins by:
- looping her death (Saw in Half, Molten Duplication, Demonic Gifts, Shallow Grave, Goryo's Vengeance, the altars) into Tendrils of Agony or Brain Freeze, or
- Thassa's Oracle with Consultation or Pact, or Breach + LED + Brain Freeze.

The five adds each serve that engine better than the slot they take:
- **Frantic Search** is paid entirely by her restricted {U}{B}{R}. It untaps three lands, a net +2 unrestricted mana plus a loot. Faithless Looting is card disadvantage.
- **Twinflame** is a second Molten Duplication on Cormela. The legend-rule death returns it. It is infinite with Birgi (Spellbook 392-1235-4867), and with Dualcaster Mage it is a 2-card infinite (147-1235). Gitaxian Probe has no Cormela synergy.
- **Hexing Squelcher** makes every spell on the combo turn uncounterable, gives Cormela ward (pay 2 life) and is sacrifice fodder. Red Elemental Blast duplicates Pyroblast.
- **Mistrise Village** enters untapped with any of 5 Mountain-typed lands, all fetchable by the 7 fetches. It also protects one spell. Undercity Sewers always enters tapped.
- **Underground River** gives guaranteed U/B. Exotic Orchard depends on opponents.

## Self-challenge
- **Four without Hexing Squelcher (REB kept):** staged and rejected. REB is redundant with Pyroblast, while Squelcher protects the entire combo turn.
- **Pass C's challenger, Muddle the Mixture over Seething Song:** staged as a six-swap and rejected. Seething Song kept: it is a converter and Spellbook 500-4036-4867.
- **Abrade over Preordain:** six-swap, staged, RETAIN_ALTERNATIVE, not selected. Chain of Vapor and Otawara already answer Cursed Totem, Null Rod and hatebears, and Preordain keeps cantrip density.
- **Burnt Offering over Windfall (plus Abrade):** seven-swap, staged, RETAIN_ALTERNATIVE, not selected. Windfall's refuel and Bowmasters damage are unique, and the deck already has four sacrifice outlets.
- **Rejected:** Verdant Catacombs and Arid Mesa (fetch-target saturation), Lim-Dûl's Vault, Grim Monolith (colorless, Game Changer), Spellseeker, Mana Drain (UU), Mox Amber, Defense Grid (symmetric), Galvanic Iteration, Ragavan and The One Ring (generic), Culling Ritual (off-identity).

## Limits
Only finite rules cases are tested (tests/test_m6_cormela_glamour_thief_m7_mechanics.py). There is no simulation or win-rate data.

Main losses:
- Undercity Sewers' surveil and Orchard's potential third color.
- Faithless Looting's flashback.
- Probe's free storm count and peek.
- The second one-mana blue hoser.
- Instants and sorceries 46 → 45; average nonland MV 1.841 → 1.899.
