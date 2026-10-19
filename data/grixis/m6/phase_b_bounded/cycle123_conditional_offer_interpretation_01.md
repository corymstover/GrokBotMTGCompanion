# Cycle 123 — Conditional An Offer counterspell window

This is a narrow, source-paid rules witness for Mai and Zuko, not a multiplayer gameplay test or a card-swap recommendation.

## Registered experiment

The preregistered plan is `data/grixis/m6/phase_b_plans/cycle123_conditional_offer_stack_prereg_01.json`. It inherits Cycle 122's 19 Oracle-checked named nonbasic lands, conditional entries, original 99-card approved list, exact one-slot baseline/challenger swap, 1,024 paired shuffles, seed 120026, seven opening cards and one draw per own turn through turn eight.

The approved baseline has An Offer You Can't Refuse and the challenger has The Enigma Jewel // Locus of Enlightenment. Oracle-cost {U} is verified for both cards. No canonical card or approval changes were made.

## Executed evidence (not opponent statistics)

- The named slot was drawn 144 times in each arm.
- In 112 of 1,024 source-deck samples, the approved baseline had both a physical An Offer in hand and an available modeled nonbasic land source that could pay {U}.
- For those 112 states, **the test injected one hypothetical, counterable opponent noncreature instant into a virtual opponent stack** at the first payable window. The pilot's actual physical An Offer went from hand to stack to graveyard, tapped a physical source, spent its mana and applied a four-pass *scripted* priority resolution. All 112 fixtures conditionally countered that *assumed* target; 224 virtual opponent Treasure tokens were counted, two per resolved Offer.
- In 112 parallel uncounterable-target fixtures, the spells were not countered, but the opponents still received 224 virtual Treasures. In 112 illegal-after-cast-target fixtures, the Offer did not resolve and granted no Treasure.
- The creature-target, absent-spell and missing-priority negative branches were rejected without spending mana or changing source-card zones: 336 rejected invalid fixture attempts.
- The candidate Jewel received 112 own-main-phase supported, uncontested paid placements. It does not provide the approved counterspell's response; its own activated-ability synergy and Mai/Zuko flash windows remain unmodeled.

**None** of the opponent spells were obtained from an actual opponent deck, drawn in a simulated multiplayer game, or assigned a real-world occurrence rate. Four priority passes were assumed explicitly, not predicted. The conditional count cannot be interpreted as wins prevented, real opponent responsiveness, an upgrade/downgrade rate or complete Phase B.

## Verification and authority boundary

[Cycle 123 CI run](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/39196534496) passed 15 regression tests, frozen Oracle archive checksum, source logical hash, physical-zone conservation, 19 named-land prerequisite, all counterspell variants and a reproducible 1,024-pair receipt. Artifact: `cycle123-virtual-opponent-conditional-offer-receipt` (ID 12161539997).

Official milestone M6 remains in progress, M7 has not started, and the secondary sub-tracker remains M6 **3/10 gates complete** with two partial; M7 **0/6**. Formal M6 certification is 0/62, independent Pass C is pending, and no candidate was approved or swapped. All 62 canonical decks remain locked.

The next substantive gate is effect-aware, source-backed opportunity analysis that includes actual modeled opponent turns and legal choices, followed by truly independent review—not another authored hypothetical passing off as gameplay proof.
