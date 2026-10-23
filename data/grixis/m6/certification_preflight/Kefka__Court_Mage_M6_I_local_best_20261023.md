# Kefka, Court Mage // Kefka, Ruler of Ruin — M6 I local-best memo for the M7 research candidate (2026-10-23)

This memo is evidence only. The candidate is NOT owner approved, NOT M6 certified and NOT owner-presentable. It is RESEARCH_ONLY: one genuine swap, below the five-swap floor. The canonical list is unchanged.

Scope: the twelve complete configurations in `data/grixis/m6/ij/tested_pools/Kefka__Court_Mage_M7_tested_configurations_20261023.json`, plus named single-card contenders. Each configuration is 100 cards (1 commander + 99 library). This is not a global or statistical optimum.

Baseline:
- Source: canonical encyclopedia main 9b26aa28fc7e16f6652aaec292b4edf84e20db71, file `refinement/decklists/Kefka_Court_Mage_Approved_2026-10-14.txt`.
- Blob 84dbe0b4, introduced by canonical approval commit 7bf011ac on 2026-10-14. Registry source_commit 1836b97 has the same bytes.
- Raw SHA-256 cd36192f… equals the overrides approved_list_sha256, the tracker final_list_hash and the registry recorded_sha256, so no provenance exception is used. Logical hash lh1:a858b678….

## Result
The research candidate (raw 4adf02f9…, lh1:ba340792…) is the canonical 100 with **+Dualcaster Mage −Culling the Weak**. It is the local best of the tested pool among configurations that respect owner direction.

**One genuine improvement was found, so the deck is RESEARCH_ONLY.** Five is a floor, not a target. Twenty-one candidates were judged and sixteen incumbents were challenged. Apart from Dualcaster Mage, every candidate failed for one of these reasons:
- **Measured only a small gain in the Pass C test:** Entomb (over Demonic Counsel or Borne Upon a Wind).
- **Does not clearly beat an owner keep or addition:** Dragon's Rage Channeler (Tinybones, Bauble Burglar), Mockingbird (Molten Duplication), Spark Double (Gogo, Mysterious Mime).
- **Generic or homogenizing:** Grinding Station, Defense Grid.
- **Nonbo:** Vexing Bauble (stops your own free spells: Force of Will, Fierce Guardianship, Pact of Negation, Lotus Petal-fuelled Breach turns).
- **Redundant:** Twinflame (Molten Duplication already does the job).
- **Marginal or no better:** Mistrise Village, Vivi Ornitier, Strix Serenade, Praetor's Grasp, Snapcaster Mage, Flesh Duplicate, Mox Amber, Urza's Saga, Generator Servant.
- **Invalid:** Dockside Extortionist is banned; Manamorphose is off-identity (R/G hybrid).
- **Staged alternatives, not counted:** Talisman of Indulgence over Culling the Weak (RETAIN_ALTERNATIVE fallback if Dualcaster Mage is declined); Dualcaster Mage over Diabolic Intent (RETAIN_ALTERNATIVE alternative cut).

Challenged incumbents: Culling the Weak (cut), Diabolic Intent, Demonic Counsel, Borne Upon a Wind, Tinybones, Bauble Burglar, Molten Duplication, Talisman of Creativity, Island, Gogo, Mysterious Mime, Anger, Mental Misstep, Swan Song, Fellwar Stone, Arena of Glory, Starting Town and Wishclaw Talisman. All except Culling the Weak were kept.

## Why (commander-first)
Kefka, Court Mage ({2}{U}{B}{R} 4/5 Legendary Creature — Human Wizard): "Whenever Kefka enters or attacks, each player discards a card. Then you draw a card for each card type among cards discarded this way."

The deck's edge over a generic Grixis list is repeating that enter trigger (Harmonic Prodigy, Essence Flux, Displacer Kitten, Phantasmal Image, Phyrexian Metamorph, Molten Duplication, Saw in Half) and giving Kefka haste (Anger, Arena of Glory, Gogo).

**The one swap: +Dualcaster Mage −Culling the Weak (MODERATE confidence).**
- Dualcaster Mage turns three owner-added spine cards already in the 99 into two-card lines: Molten Duplication (Commander Spellbook 147-5487, infinite hasty tokens), Saw in Half (147-500) and Essence Flux (147-4598). Spellbook 6 → 9.
- It is a flash Wizard, so Harmonic Prodigy doubles its enter trigger; the spare copy may target Kefka (CR 707.10c), giving a Kefka enter trigger on every iteration.
- Culling the Weak is not an owner explicit keep. It needs a creature (P(an MV≤2 creature seen) 0.4115 on turn 1 to 0.6075 on turn 6) and makes only black.
- **Data caveat:** adoption is neutral to slightly against the swap. EDHREC cEDH 497/2232 for Dualcaster against 861/2232 for Culling; EDHTop16 one-year conversion 0.1706 (252 entries) against 0.1867 (557). The gap is inside sampling noise (difference standard error about 0.027).
- **Owner-direction flag:** the Molten Duplication kill does not require Kefka, which is close to the owner's reason for rejecting the Valley Floodcaller bounce-combo package. Mitigation: it is one slot, uses cards already in the deck for Kefka's copy plan and loops Kefka through Prodigy. The owner must decide; the zero-swap baseline remains available.

## Owner direction
- Every incumbent is owner-directed: 80 retained baseline cards plus 19 owner additions on 2026-10-14.
- Explicit keeps (Gogo, Hexing Squelcher, Phyrexian Metamorph, Tinybones, Waste Not and the blueprint spine) are all retained. The cut, Culling the Weak, is not an explicit keep, so **no owner keep or addition is overridden**; the flag above is disclosed instead.
- **Owner-removed cards and classes are not re-added:** Animate Dead, Dauthi Voidwalker, Geth's Grimoire, Kroxa, Titan of Death's Hunger, Laughing Mad, Liliana's Caress, Megrim, Monument to Endurance, Nightscape Familiar, Sheoldred, the Apocalypse, Strionic Resonator, Windfall, Mountain, Swamp, Xander's Lounge, Exotic Orchard, Cyclonic Rift, Opposition Agent, Psychosis Crawler, Cursed Totem, Samut, Tyrant of Naktamun, the Banishing Knack / Retraction Helix package, The One Ring, Birgi, God of Storytelling // Harnfel, Horn of Bounty, Faerie Mastermind and extra discard payoffs.
- The staged alternatives are complete 100s on the baseline, so the owner can pick one directly.

## Pass C requested tests (bounded finite versions; not win rates)
These are in `data/grixis/m7/research_challengers/Kefka__Court_Mage_bounded_measured_tests_20261023.json` and recomputed in `tests/test_m6_kefka_court_mage_m7_mechanics.py`.

Pass C's final disposition was **NEEDS TESTING**. It asked to compare the locked baseline with Entomb/Counsel and Entomb/Borne alternatives (four-type delirium before Counsel, Anger plus Mountain-subtype source availability, earliest Kefka deployment/attack, tutor windows, grave hate) and optionally a Dragon's Rage Channeler/Tinybones challenge. The Pass C receipt is a NON-INDEPENDENT owner-equivalent review (alias Josh-Lee-Kwai, ChatGPT/OpenAI GPT-6, with a technical-independence waiver).

1. **Mountain-subtype sources.** 13 (Badlands, Blood Crypt, Steam Vents, Volcanic Island plus 9 fetches). Exact P(at least one) by turn 1–6: 0.6391, 0.6901, 0.7343, 0.7727, 0.8059, 0.8346.
2. **Anger haste window (exact).**

   | Turn (cards seen) | Baseline (Anger + Mountain source) | Plus Entomb (Anger or Entomb + Mountain source) |
   |---|---|---|
   | 1 (7) | 0.0413 | 0.0804 |
   | 5 (11) | 0.0863 | 0.1642 |

   The relative gain is real but the absolute gain is small, and Kefka's own enter-trigger discard already bins Anger in the native line.
3. **Demonic Counsel delirium (seeded Monte Carlo, seed 25, N=200000).** There is no Demon in the 99. Turn 4: 0.0659 lower bound (no extra discard) to 0.4229 upper bound (one free typed discard); turn 6: 0.111 / 0.5463.
4. **Dualcaster Mage partner access (exact).** P(Dualcaster and at least one of Molten Duplication, Saw in Half, Essence Flux seen) 0.0123 on turn 1 to 0.0367 on turn 6, before tutors.
5. **Culling the Weak early creature (exact).** Seven MV≤2 creatures: 0.4115 on turn 1 to 0.6075 on turn 6.
6. **Dragon's Rage Channeler vs Tinybones.** Not run as a separate measurement: Pass C made it conditional on materially changing the decision, and Tinybones is an explicit owner keep that DRC does not clearly beat (only Demonic Counsel uses delirium).

Commander Spellbook: the baseline has 6 complete combos. The candidate has 9. Every alternative is 6, except Dualcaster Mage over Diabolic Intent, which is 9.

Not done, stated plainly: there were no matched-hand games, no opponent model and no win rates. The repo has no validated Kefka game engine.

## Limits
Only finite scripted rules cases, exact enumerations and one seeded proxy are tested.

- Game Changers 20 → 20 (Bracket 5).
- Average nonland MV 1.94 → 1.97.
- Commander Spellbook 6 → 9 complete combos.
