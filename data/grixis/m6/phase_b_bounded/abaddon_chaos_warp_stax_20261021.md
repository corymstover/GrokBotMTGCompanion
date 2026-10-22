# Abaddon — Chaos Warp versus current resolved-stax defense

**M6.6/7 evidence, not certification.** Approved Abaddon main remains 100/100, SHA-256 `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`, APPROVED/LOCKED. No card swap applied. **Preregistration committed first:** `data/grixis/m6/phase_b_plans/abaddon_chaos_warp_stax_20261021.json` at `ad438f2c01067f5523fa48620ac8228ec6084dac`.

## Material source-audit correction

The original Abaddon authored whole-deck assessment and later bounded mana-access interpretation loosely referred to **The Lost and the Damned** and **The Ruinous Powers** as expensive/five-mana setup cards. Their actual printed costs are **{1}{U}{R}, mana value 3** and **{2}{B}{R}, mana value 4**, respectively. These are **not five-mana incumbents**. Lost is an especially accessible 3-MV card that produces a 3/3 red Spawn whenever you cast a nonhand spell; cascade is integral to Abaddon, so its role matters directly. Ruinous is a 4-MV repeatable upkeep stolen-spell cast engine; the **opposing owner** loses mana-value-scaled life when that card is cast, building Abaddon's same-turn threshold. Neither should be mislabeled or reflexively removed as a high-curve payoff. This erratum **does not alter their printed legal cards or the canonical list**.

Sources: https://mtg.wtf/card/40k/129/The-Lost-and-the-Damned ; https://magic.wizards.com/en/news/feature/warhammer-40000-commander-release-notes-2022-09-19 .

## Actual defense roles

The approved 99 has **Otawara, Soaring City** (Channel `{3}{U}`, discount `{1}` for each legendary creature you control) as an ability-based **temporary bounce** for an already-resolved artifact/creature/enchantment/planeswalker; it requires Otawara **in hand, not already deployed as a land**, and unlike a spell it can be activated after a player has reached the Rule-of-Law spell quota. This is a real existing answer, but its bounce lets opponents recast the problem permanent. The fixed-source draw test conservatively assumes **zero legendary creatures** when costing the channel and no alternative action for deployed Otawara.

**Chaos Warp** ({2}{R}; Commander-legal) is an additional, flexible instant-speed answer that can target **any permanent**, including nonblue enchantments and colorless artifacts on board. Its owner shuffles that permanent into their library then reveals the top card; if a permanent card, it enters. The replacement may itself be dangerous or even the same stax piece—never say Warp guarantees a lasting answer.

**Before resolution:** Swan Song can counter a cast enchantment; Force of Negation and Fierce Guardianship (conditional requirements/payment) can counter noncreature spells; Force of Will can counter any spell at its own cost. Counterspell cover is meaningful but does nothing if the relevant permanent has **already resolved**. Pyroblast's blue condition is ineffective against a white Rule of Law or colorless Null Rod. Against a **creature** like Drannith Magistrate, existing Deadly Rollick and creature-oriented removal can answer an already-resolved threat; noncreature stax is the distinctive coverage gap.

**Rule of Law / Arcane Laboratory window:** Casting Chaos Warp on an opposing **end step** while it is the pilot's first spell of that *turn* can clear the restriction in time for the next pilot turn (conditional on the revealed replacement and opponent responses). If the pilot already cast one spell that turn and the restriction remains, they **cannot** cast Warp as a second spell; Otawara's channel remains an ability option. If Abaddon grants Chaos Warp cascade (the turn's opponent-loss threshold reached 3, Abaddon controlled), the cascade trigger resolves **before Chaos Warp** removes Rule of Law, so the exiled spell cannot be cast while the restriction remains. This does **not** disprove later spells after Warp resolves. If Warp returns Rule of Law as the revealed top permanent, it has not produced a lasting out. Against Rest in Peace, removing the enchantment never returns the cards previously exiled from graveyards.

Card/rule sources:
- https://mtg.wtf/card/40k/205/Chaos-Warp
- https://mtg.wtf/card/neo/271/Otawara-Soaring-City
- https://mtg.wtf/card/m20/35/Rule-of-Law
- https://mtg.wtf/card/plst/7ED-60/Arcane-Laboratory
- https://mtg.wtf/card/40k/129/The-Lost-and-the-Damned
- https://magic.wizards.com/en/news/feature/warhammer-40000-commander-release-notes-2022-09-19

## Frozen physical comparison

`scripts/grixis_m6_abaddon_chaos_warp_stax.py` builds the exact approved **1 commander + 99 physical main** and three unapplied one-slot candidates: `+Chaos Warp / -Rakdos`; `-The Lost and the Damned`; `-The Ruinous Powers`. The fixture proves physical count, 34 land slots, singleton and source hashes. Each follows **2,000 paired seed** trajectories for opening seven plus one per own turn, no mulligans or draw effects, one supported land play each turn, real deterministic fetch reshuffles; turns 4,6,8,10 record **Warp held**, **Warp separately payable from modeled untapped land sources for {2}{R} as first spell**, **Otawara channel held** and its separately payable ability cost **{3}{U}** (with zero commander discount), and either available. Otawara played as a land is not counted as a channel answer. Replacement incidence and opponent metagame prevalence are wholly unmodeled.

**These are source-payability and rule-window diagnostics only.** They do **not** model a real Rule of Law being drawn, cast, answered or reestablished; no ramp rocks, rituals, tutors, actual cascade, player survival, conditional blue mana, opponents' responses, random replacement distribution or multiplayer match win rates. They do not assign zero value to cut incumbent effects. No measured or certified deck superiority follows.

## Commander-first judgment and stopping condition

**Current disposition: HOLD Chaos Warp until a defensible cut and real table relevance justify it; no swap applied.** Warp is an authentic answer-gap upgrade candidate, but the exact strong candidates under discussion sacrifice a substantial existing engine:

| Unapplied cut | What would be lost |
| --- | --- |
| Rakdos, Lord of Riots | Potential same-turn opponent-loss creature generic discounts for 17 other creature identities (including Abaddon recasts); BBRR casting obstacle, real 6/6 evasive threat. Note Assault competes for this same slot. |
| The Lost and the Damned | **{1}{U}{R}, MV3** nonhand spell cast to 3/3 Spawn triggers, central cascade/exile identity. |
| The Ruinous Powers | **{2}{B}{R}, MV4** repeatable stolen casts, owner-life-loss threshold generation and exile payoff support. |

No source-grounded match rate of problematic enchantments/artifacts or reliable valuation of lost Rakdos discount, spawned board, and Ruinous engine has yet proved a positive net change. *Conditional availability* of Warp and its ability to address one stax effect are not a 100-card win-rate improvement. If the identified local playgroup actually has high sustained resolved-stax density, revisit the weakest genuine engine slot in that specific environment; avoid replacing fast threshold pingers, crucial commander protection or the low-cost Lost enchantment on generalized staples logic. Phase B still PARTIAL; M6/J/I certification and M7 exact-card owner approvals all pending.
