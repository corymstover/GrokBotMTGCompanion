# Cycle 103 — source-backed nonbasic land access, preliminary technical critique

**Review class:** author-side engineering review, **NOT** independent Pass C, I/J, formal rules-engine certification, deck approval, or completion of M6. Canonical 62 decks stay approved and locked.

## Frozen, matched evidence

- Preregistered Cycle 103 land model and seed before implementation: `data/grixis/m6/phase_b_plans/nonbasic_land_access_62_01.json`.
- Bounded full receipts: `data/grixis/m6/phase_b_bounded/nonbasic_land_access_62_01.json`; compact source-derived summary: `data/grixis/m6/phase_b_bounded/nonbasic_land_access_62_summary_01.json`.
- All **19 named lands** passed source-specific Oracle checks for printed mana, land type and applicable entry/life restrictions against the SHA-locked October 2026 Scryfall snapshot.
- The exact same **62 × 12 = 744** seeded Cycle 102 physical-card shuffled 7-card openings and four further draws were independently replayed and compared **sample by sample**. No new hand/draw sequence was chosen to improve results.
- Under the explicit first-supported-land-in-hand, one-land-per-turn and Arcane-Signet-only policies: Signet appeared in **96/744** traces, as in Cycle 102; source-backed Signet casting increased from **12/744** (basic-only interpreter) to **51/744** (19 added nonbasic mana lands). The new interpreter recorded **1,383** modeled land plays, including **956** named nonbasics and **97** tapped entries.
- These are implementation/coverage counts under highly restricted policies, **not game probabilities, mana-base superiority, real casting reliability, or win rates**.

## Land coverage and targeted correctness

Supported: Command Tower, Crumbling Necropolis, Xander's Lounge; Underground Sea, Volcanic Island, Badlands; Watery Grave, Steam Vents, Blood Crypt; Drowned Catacomb, Sulfur Falls, Dragonskull Summit; Spirebluff Canal, Darkslick Shores, Blackcleave Cliffs; Morphic Pool, Training Center, Luxury Suite; Mana Confluence.

The implementation records permanent physical IDs and actual entering-tapped conditions. Shocklands deterministically pay 2 life to enter untapped when controller life exceeds 2; the alternative enters tapped. Checklands inspect *land subtypes*, including typed nonbasics, not just basic-name cards. Fastlands inspect number of **other** lands at entry; multiplayer bond lands use the declared three opponents. Mana Confluence pays 1 controller life as an activation cost and that life payment never counts toward Abaddon's opponent-life-loss cascade condition. Multiple possible land mana colors are assigned to satisfy printed pips through a deterministic real-source search. Invalid action tests check full rollback.

## Open model limitations and audit risks

1. Many impactful lands remain unsupported. In the 744 scripted trials, unsupported seen-by-hand incidence was logged for Bloodstained Mire (102 samples), Polluted Delta (93), Ancient Tomb (74), Scalding Tarn (69), City of Brass (60), Marsh Flats (57), Otawara, Soaring City (54), and many other fetch/utility lands. These are **occurrence counts of an unsupported land seen**, not independent game draws or comparative value.
2. This still assumes four simplified own turns, no mulligan policy, no opponent turn actions, no comprehensive priority framework and no modeled spells other than Arcane Signet in the access samples. Mana from rocks already on the battlefield, rituals, treasures, fetches, utility mana, life triggered abilities, tutors and combat are not autonomously modeled.
3. The deterministic land choice takes the first supported physical land in hand; the shock decision is fixed, not a strategy optimized to commander identity or opponents. The additional modeled sources must not be treated as a recommendation to edit any of the approved 62 decks.
4. Some modeled cards have **additional abilities** not represented, such as Xander's Lounge's cycling. Only their listed ETB and activated mana states are supported; other actions fail closed.
5. CI's sample-matched increase in modeled Signet casts is **not evidence of a stronger deck** and cannot establish any candidate-swap improvement, official Commander card legality, full Phase B, formal independent Pass C/I/J, tested-pool zero-improvement result, or M6 acceptance.

## Next bounded engineering gate

Prioritize source-verified **fetchland shuffling/search plus land zone movement**, **City of Brass damage-trigger stack behavior**, and **Ancient Tomb colorless mana plus source damage**. Each has distinct activation costs/timing; do not homogenize them into generic untapped mana. Confirm full physical-card and library/stack conservation under scripted opponent responses. Then improve actual 62-commander policy coverage rather than chasing another simplistic percentage.
