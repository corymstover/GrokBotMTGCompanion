# Abaddon — source-locked physical first-cascade-hit screen for MV3 Grinning Ignus

**Stage:** M6.6 exploratory Phase B. This is a reproducible **conditional physical-library cascade-hit screen**, not whole-deck play, not a combo probability and not a superior-swap claim. Preregistered plan `data/grixis/m6/phase_b_plans/abaddon_ignus_cascade_first_hit_20261021.json` committed at `bc27aaf6148bcf1ef2b5101d1b619414445ee96f` **before** tests or simulator implementation. Frozen canonical Abaddon remains APPROVED/LOCKED (raw SHA-256 `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`). Frozen physical engineering source `5448d76193923a3f9e3d4c41a327eaeaa9c6326d484d8e5a9abaf3852db2efff`.

## Physical Oracle-driven target inventory

The current frozen Abaddon 99 includes exactly **35 nonland physical cards of mana value less than 3** (7 MV0, 15 MV1, 13 MV2), not 41: the latter figure incorrectly retains six land names in the graph query. This study validates every card against the frozen `data/grixis/graph/abaddon-the-despoiler.json` Git blob `5dc2d6deeb58bf267e8c2ee3da7091b54d14d5fb`, without importing rankings as truth. Removing MV2 Nightscape Familiar or MV1 Rite of Flame decreases the available subthree payoff inventory by one, unlike removing Rakdos. No substitution is authorized.

Major low-cost role families include **nine castable ramp artifacts** (Chrome Mox, Lion's Eye Diamond, Lotus Petal, Mana Vault, Sol Ring, Arcane Signet, and the three Talismans), **three rituals** (Dark Ritual, Cabal Ritual, Rite of Flame), **six tutors** (Demonic Tutor, Gamble, Imperial Seal, Mystical Tutor, Profane Tutor, Vampiric Tutor) and conditional burn Boltwave / Flame Rift. **Ancestral Vision, Inevitable Betrayal, and Profane Tutor have no mana cost but MV0; cascade's optional cast-without-paying permission lets them be cast.** The roles overlap (Profane Tutor is also a tutor). This is why naive ‘has printed payable cost’ filters falsely exclude valuable cascade targets.

A successful cascade triggered by a **hand-cast Ignus spell of printed mana value 3** stops on the first nonland card with *strictly* lower mana value; cards equal MV3 and all lands are exiled past. The pilot may cast the hit from exile without paying its mana cost, then returns uncast cards to the library bottom in random order. No target or chosen legal cast means the hit also bottoms. The exiled cast spell **cannot receive Abaddon's hand-only cascade**. Rakdos/Nightscape cost discounts do not change the MV threshold.

## Stack-sensitive real legality

For the registered stack containing only **the original red creature spell Grinning Ignus** while its cascade resolves:

- **Swan Song** cannot target the original (only enchantment/instant/sorcery).
- **Flusterstorm** cannot target the original (instant/sorcery only). Its storm ability does not make its illegal target legal.
- **Pact of Negation** technically may target the original Ignus, but doing so would counter the engine creature and leave a next-upkeep mana liability; the fixed conservative policy **declines** this hit, bottoming it.
- **Pyroblast** legally *can* target the red Ignus spell, because it checks blue on resolution; it will not counter the nonblue spell. The fixed policy permits the cast (possible spell-cast triggers), but scores no blue-counter effect.
- With **Rule of Law already active** and Ignus already cast as the turn's single spell, the hit cannot be cast as a second spell. With a resolved **Drannith Magistrate**, it cannot be cast from exile. The cascade trigger itself still exiles and bottoms cards. These are **separate scripted adversarial cases**, not probabilities that these hate permanents occur.

Against an open state, an eligible hit is only an **offered optional cast, not a guaranteed good effect**. No additional stack targets beyond Ignus, and no unmodeled permanent, hand, land or opponent spell can be assumed. Some other target-specific cards may depend on the presence of other permanents or opponents' resources, so the ‘permissible under fixed stack’ class **does not prove strategic usefulness**.

## Matched experiment

Five exact 100-card physical libraries are compared: locked Abaddon, unapplied +Ignus / -Rakdos, +Ignus / -Nightscape Familiar, +Ignus / -Rite of Flame, and +Assault / -Rakdos (negative control for real Ignus assembly, not an Assault activation test). 2,000 matched seeds per variant: draw seven, draw once on each own turn, follow registered physical one-land/fetch search and shuffle policy through turns 4,6,8,10. At *each checkpoint*, independently copy the still-physical post-draw/deployment library, **assume for this one test only** that an MV3 Ignus cascade trigger exists, follow all exiles, first eligible hit, optional legal cast, and physically restore uncast cards to shuffled library bottom. Those checkpoint examples **do not construct a battlefield with Abaddon/Birgi/Ignus or opponent life loss**. Source-paid actual assembly was separately counted in PR #520; these distribution counts are not a multiplication-ready conditional engine performance estimate.

The actual **effect** of any eligible hit is not simulated: casting Chrome Mox would still require imprint decision, LED activation demands a hand discard, ritual mana has colors/timing, tutoring alters the library, spells may require targets, free Ancestral Vision draws cards, storm counts previous spells, and a free burn hit modifies same-turn life-loss threshold. Therefore count role exposure as ‘cascade role opportunities’, not ramp/deck strength/real game wins. Those effects, interaction, and tutor targets remain the next material testing frontier before an optimized Grinning Ignus recommendation.

**Authority:** existing 62 canonical APPROVED/LOCKED untouched. M6.6 and M6.7 PARTIAL 0/62; no M6 I/J certificate, no M7 new owner decision. Respect the Oct 21 formal narrow Pass C nonindependent owner waiver without claiming genuine independent review.

## Sources
- Canonical current card audit `refinement/tests/Abaddon_Current_Card_Audit_2026-10-13.csv` (source Oracle and present-printing legality).
- [Comprehensive Rules, cascade 702.85a, 118.6a, mana value 202.3a](https://blogs.magicjudges.org/rules/comprehensive-rules/).
- [Ancestral Vision cast off cascade despite no mana cost](https://blogs.magicjudges.org/rulestips/2013/01/you-cant-flashback-ancestral-vision-but-you-can-cascade-into-it/).
- [Pyroblast: may target nonblue spells](https://mtg.wtf/card/ema/142/Pyroblast).
