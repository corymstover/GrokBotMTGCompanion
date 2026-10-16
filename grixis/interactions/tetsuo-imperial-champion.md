---
title: "Tetsuo, Imperial Champion — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Tetsuo, Imperial Champion — Interaction Review

> Bot cycle 56 · batch F · reviewed 2026-10-16. Deck: [Tetsuo, Imperial Champion](../decks/tetsuo-imperial-champion.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-15), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/tetsuo-imperial-champion.txt`](../../exports/grixis-archidekt/tetsuo-imperial-champion.txt) · SHA-256 `1e551bc95c4918b340539539ed8ba1275f791d4f19330eb6141f84a48927a0d4` |
| Rulings | **6** (6 verified · 0 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-15 · rulings 2026-10-15 |
| Source attestations | [`Tetsuo_Imperial_Champion_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_imperial_champion_2026-10-15/gate_output/Tetsuo_Imperial_Champion_Rules_Attestation.json) (Rules attestation (19 items, all PASS) re-verified) · [`Tetsuo_Imperial_Champion_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tetsuo_Imperial_Champion_Approval_Ready_Verification_2026-10-15.md) (Approval-ready verification) |

## Contents
- [Summary](#summary)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [Timing and priority](#timing-and-priority)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [Rules cited](#rules-cited)

## Summary

Tetsuo, Imperial Champion is Voltron with free spells. If he's equipped when he attacks, he either deals damage equal to his biggest Equipment's MV or free-casts an instant or sorcery up to that MV. Extra combats (Savage Beating, World at War, Genji Glove, Hexplate Wallbreaker, Godo, Aggravated Assault + Sword of Feast and Famine or Reaver Cleaver) retrigger him. All 2 Spellbook lines and all 19 attestation items are re-verified against the canonical list. The cut Relentless Assault and Seize the Day are absent.

Rules surprises: Excalibur's mana value stays 12 even when it's nearly free; no-mana-cost suspend cards (MV 0) always fit his cap; Savage Beating's extra combat comes with no main phase between; casting World at War in combat still works and still rebounds. No list errors.

## Commander rules text and edge cases

### tetsuoic-01: Intervening-if attack trigger; ceiling = greatest Equipment MV on resolution

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Tetsuo, Imperial Champion, Excalibur, Sword of Eden, Kaldra Compleat, Argentum Armor, Embercleave, Leyline Axe, Basilisk Collar

**Ruling.** Tetsuo triggers only if he's equipped when he attacks, and does nothing if he's unequipped when the trigger resolves. The mode and any target are chosen as it goes on the stack. The number used is the greatest mana value among Equipment attached when it resolves. Cost reductions don't lower mana value, so Excalibur counts as 12 however little you paid. Kaldra Compleat counts 7, Argentum Armor and Embercleave 6, and Leyline Axe 4. In the damage mode Tetsuo is the source. With Basilisk Collar that damage has deathtouch and lifelink, even though it isn't combat damage.

**Citations**

- Oracle, *Tetsuo, Imperial Champion*: “Whenever Tetsuo attacks, if it's equipped, choose one —”
- Scryfall ruling, *Tetsuo, Imperial Champion*: “If Tetsuo isn't equipped when it's declared as an attacking creature, the ability won't trigger. If Tetsuo isn't equipped when the ability resolves, the ability won't do anything.”
- [CR 603.4](#cr-6034), [CR 202.3](#cr-2023), [CR 702.2b](#cr-7022b)
- Source (re-verified): [`Tetsuo_Imperial_Champion_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_imperial_champion_2026-10-15/gate_output/Tetsuo_Imperial_Champion_Rules_Attestation.json) → “Tetsuo attack trigger and equipped condition”
- Source (re-verified): [`Tetsuo_Imperial_Champion_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_imperial_champion_2026-10-15/gate_output/Tetsuo_Imperial_Champion_Rules_Attestation.json) → “Greatest Equipment mana value”
- Source (re-verified): [`Tetsuo_Imperial_Champion_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_imperial_champion_2026-10-15/gate_output/Tetsuo_Imperial_Champion_Rules_Attestation.json) → “Leyline Axe”
- Source (re-verified): [`Tetsuo_Imperial_Champion_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_imperial_champion_2026-10-15/gate_output/Tetsuo_Imperial_Champion_Rules_Attestation.json) → “Basilisk Collar and Tetsuo damage mode”

## Combos and engine lines

### tetsuoic-04: Aggravated Assault + Sword of Feast and Famine or The Reaver Cleaver: infinite combats

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Tetsuo, Imperial Champion, Aggravated Assault, Sword of Feast and Famine, The Reaver Cleaver, Buster Sword

**Ruling.** Connect with Sword of Feast and Famine to untap your lands, or with The Reaver Cleaver on a creature with 5+ power for at least six Treasures. Then, in the postcombat main phase, pay {3}{R}{R} for Aggravated Assault: another combat and main phase, with your creatures untapped. That's Spellbook 900-3750 and 3750-5039. Each new combat retriggers Tetsuo. Assault is sorcery speed, so it only works in a main phase. Buster Sword adds a draw and a free cast up to the damage dealt; the cast must happen as its trigger resolves.

**Citations**

- Oracle, *Aggravated Assault*: “{3}{R}{R}: Untap all creatures you control. After this main phase, there is an additional combat phase followed by an additional main phase. Activate only as a sorcery.”
- Scryfall ruling, *Buster Sword*: “You choose whether to cast a spell from among the cards in your hand as Buster Sword's middle ability resolves. You can't wait to cast one later in the turn. Timing restrictions based on the card's types are ignored.”
- [CR 602.5d](#cr-6025d), [CR 500.8](#cr-5008)
- Commander Spellbook [900-3750](https://commanderspellbook.com/combo/900-3750/) (community-maintained, retrieved 2026-10-16): “Sword of Feast and Famine triggers, causing that opponent to discard a card, and you to untap all lands you control.”
- Commander Spellbook [3750-5039](https://commanderspellbook.com/combo/3750-5039/) (community-maintained, retrieved 2026-10-16): “The creature triggers, creating at least six Treasure tokens.”
- Source (re-verified): [`Tetsuo_Imperial_Champion_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_imperial_champion_2026-10-15/gate_output/Tetsuo_Imperial_Champion_Rules_Attestation.json) → “Aggravated Assault plus Sword of Feast and Famine”
- Source (re-verified): [`Tetsuo_Imperial_Champion_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_imperial_champion_2026-10-15/gate_output/Tetsuo_Imperial_Champion_Rules_Attestation.json) → “Buster Sword”

## Engines and payoffs

### tetsuoic-06: Attaching and protecting: Hammer of Nazahn, Brass Squire, Blacksmith's Talent, Swiftfoot Boots, Chandra's Ignition

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Tetsuo, Imperial Champion, Hammer of Nazahn, Brass Squire, Blacksmith's Talent, Swiftfoot Boots, Chandra's Ignition

**Ruling.** Getting equipped and finishing:
- Hammer of Nazahn attaches Equipment as it enters, and Brass Squire attaches at instant speed.
- Blacksmith's Talent level 2 attaches at the beginning of combat, so Tetsuo is equipped before he attacks.
- Swiftfoot Boots gives hexproof without shroud, so your own effects can still target him.
- Chandra's Ignition makes a large equipped Tetsuo the damage source, hitting each other creature and each opponent for his power. That's why Sword of Wealth and Power, with protection from sorceries, was cut. Ignition does nothing if its target is illegal.

**Citations**

- Oracle, *Chandra's Ignition*: “Target creature you control deals damage equal to its power to each other creature and each opponent.”
- Scryfall ruling, *Chandra's Ignition*: “The creature is the source of the damage, not Chandra's Ignition. For example, Chandra's Ignition can have a white creature deal damage to a creature with protection from red.”
- [CR 702.11b](#cr-70211b), [CR 702.6a](#cr-7026a)
- Source (re-verified): [`Tetsuo_Imperial_Champion_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_imperial_champion_2026-10-15/gate_output/Tetsuo_Imperial_Champion_Rules_Attestation.json) → “Attachment engines”
- Source (re-verified): [`Tetsuo_Imperial_Champion_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_imperial_champion_2026-10-15/gate_output/Tetsuo_Imperial_Champion_Rules_Attestation.json) → “Swiftfoot Boots”
- Source (re-verified): [`Tetsuo_Imperial_Champion_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_imperial_champion_2026-10-15/gate_output/Tetsuo_Imperial_Champion_Rules_Attestation.json) → “Chandras Ignition”
- Source (re-verified): [`Tetsuo_Imperial_Champion_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_imperial_champion_2026-10-15/gate_output/Tetsuo_Imperial_Champion_Rules_Attestation.json) → “Mana-base revision”

## Timing and priority

### tetsuoic-02: Free cast during resolution: sorceries in combat, no-mana-cost suspend cards, entwine

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Tetsuo, Imperial Champion, Ancestral Vision, Profane Tutor, Wheel of Fate, Inevitable Betrayal, Savage Beating

**Ruling.** Tetsuo lets you cast a spell while his trigger resolves, so sorcery timing doesn't matter, but other restrictions still apply. Casting without paying the mana cost rules out alternative costs, but you may pay additional costs. Savage Beating's entwine {1}{R} can be paid on top of the free cast.

Ancestral Vision, Profane Tutor, Wheel of Fate and Inevitable Betrayal have no mana cost, so their MV is 0. They can't be cast normally, but casting them free is exactly what's needed. Any equipped Tetsuo can cast them.

**Citations**

- Oracle, *Savage Beating*: “Cast this spell only during combat on your turn.”
- Scryfall ruling, *Profane Tutor*: “A card with no mana cost can't be cast normally; you'll need a way to cast it for an alternative cost or without paying its mana cost, such as by suspending it.”
- Scryfall ruling, *Ancestral Vision*: “If you cast a card "without paying its mana cost," such as with suspend, you can't choose to cast it for any alternative costs. You can, however, pay additional costs. If the card has any mandatory additional costs, you must pay those if you want to cast the card.”
- [CR 601.2f](#cr-6012f), [CR 702.42a](#cr-70242a), [CR 202.3](#cr-2023)
- Source (re-verified): [`Tetsuo_Imperial_Champion_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_imperial_champion_2026-10-15/gate_output/Tetsuo_Imperial_Champion_Rules_Attestation.json) → “Casting during trigger resolution”
- Source (re-verified): [`Tetsuo_Imperial_Champion_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_imperial_champion_2026-10-15/gate_output/Tetsuo_Imperial_Champion_Rules_Attestation.json) → “No-mana-cost suspend spells”
- Source (re-verified): [`Tetsuo_Imperial_Champion_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_imperial_champion_2026-10-15/gate_output/Tetsuo_Imperial_Champion_Rules_Attestation.json) → “Savage Beating”

### tetsuoic-03: Extra combats: Savage Beating vs World at War vs the cut Relentless Assault

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Tetsuo, Imperial Champion, Savage Beating, World at War, Genji Glove, Hexplate Wallbreaker, Godo, Bandit Warlord, Akki Battle Squad

**Ruling.** Extra-combat cards and when their combat happens:
- **Savage Beating:** the extra combat comes right after the current one, with no main phase between. Tetsuo attacks again and triggers again.
- **World at War:** works if it resolves before the first postcombat main phase ends, so casting it in the first combat is fine. The new combat comes after the second main phase and untaps everything that attacked. Cast from hand, even free, it rebounds for another free cast next upkeep.
- **Relentless Assault and Seize the Day:** both make their combat "after this main phase", so they do nothing when cast in combat. They're correctly out of the list.
- **Genji Glove, Hexplate Wallbreaker and Godo:** add a combat only on the first combat or first attack each turn. Glove and Wallbreaker are MV 5, enough for Savage Beating or World at War.
- **Akki Battle Squad:** triggers once a turn.

Tetsuo's own trigger has no turn limit.

**Citations**

- Oracle, *World at War*: “After the second main phase this turn, there's an additional combat phase followed by an additional main phase. At the beginning of that combat, untap all creatures that attacked this turn.”
- Oracle, *Genji Glove*: “Whenever equipped creature attacks, if it's the first combat phase of the turn, untap it. After this phase, there is an additional combat phase.”
- Scryfall ruling, *Savage Beating*: “The additional combat phase is directly after the combat phase in which Savage Beating is cast. There isn't a main phase between the two combat phases.”
- Scryfall ruling, *World at War*: “As long as World at War resolves before the first postcombat main phase of a turn ends, it will have its full effect. That will happen in most cases, since it’s a sorcery (meaning it’s probably cast during the first or second main phase of a turn), and it has rebound (meaning it’ll be cast during your upkeep). If, however, it’s cast later than that, it won’t create any new phases.”
- [CR 500.8](#cr-5008), [CR 702.88a](#cr-70288a)
- Source (re-verified): [`Tetsuo_Imperial_Champion_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_imperial_champion_2026-10-15/gate_output/Tetsuo_Imperial_Champion_Rules_Attestation.json) → “World at War”
- Source (re-verified): [`Tetsuo_Imperial_Champion_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_imperial_champion_2026-10-15/gate_output/Tetsuo_Imperial_Champion_Rules_Attestation.json) → “Historical Relentless Assault / Seize the Day correction”
- Source (re-verified): [`Tetsuo_Imperial_Champion_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_imperial_champion_2026-10-15/gate_output/Tetsuo_Imperial_Champion_Rules_Attestation.json) → “Repeated Tetsuo attacks”
- Source (re-verified): [`Tetsuo_Imperial_Champion_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_imperial_champion_2026-10-15/gate_output/Tetsuo_Imperial_Champion_Rules_Attestation.json) → “Genji Glove / Hexplate Wallbreaker”
- Source (re-verified): [`Tetsuo_Imperial_Champion_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_imperial_champion_2026-10-15/gate_output/Tetsuo_Imperial_Champion_Rules_Attestation.json) → “Godo and Samurai typing”

## Zones, commander tax and the command zone

### tetsuoic-05: Oathkeeper: return the Samurai card, or let the commander rule take it

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Tetsuo, Imperial Champion, Oathkeeper, Takeno's Daisho

**Ruling.** If an equipped Tetsuo dies, Oathkeeper returns him, because it checks whether the card is a Samurai, and Tetsuo is a Human Samurai. Leave him in the graveyard when state-based actions offer the command zone, or the trigger can't find him. If Oathkeeper itself goes to the graveyard while attached, it exiles Tetsuo. You can then move him to the command zone as a state-based action.

**Citations**

- Oracle, *Oathkeeper, Takeno's Daisho*: “Whenever equipped creature dies, return that card to the battlefield under your control if it's a Samurai card.”
- Oracle, *Oathkeeper, Takeno's Daisho*: “When Oathkeeper is put into a graveyard from the battlefield, exile equipped creature.”
- Scryfall ruling, *Oathkeeper, Takeno's Daisho*: “Oathkeeper's second ability checks whether the card's creature type is Samurai, not whether the creature was a Samurai when it left the battlefield.”
- [CR 903.9a](#cr-9039a), [CR 400.7](#cr-4007)
- Source (re-verified): [`Tetsuo_Imperial_Champion_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_imperial_champion_2026-10-15/gate_output/Tetsuo_Imperial_Champion_Rules_Attestation.json) → “Oathkeeper, Takenos Daisho”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 202.3

The mana value of an object is a number equal to the total amount of mana in its mana cost, regardless of color.

#### CR 400.7

An object that moves from one zone to another becomes a new object with no memory of, or relation to, its previous existence. This rule has the following exceptions.

#### CR 500.8

Some effects can add phases to a turn. They do this by adding the phases directly after the specified phase. If multiple extra phases are created after the same phase, the most recently created phase will occur first.

#### CR 601.2f

The player determines the total cost of the spell. Usually this is just the mana cost. Some spells have additional or alternative costs. Some effects may increase or reduce the cost to pay, or may provide other alternative costs. Costs may include paying mana, tapping permanents, sacrificing permanents, discarding cards, and so on. The total cost is the mana cost or alternative cost (as determined in rule 601.2b), plus all additional costs and cost increases, and minus all cost reductions. If multiple cost reductions apply, the player may apply them in any order. If the mana component of the …

#### CR 602.5d

Activated abilities that read “Activate only as a sorcery” mean the player must follow the timing rules for casting a sorcery spell, though the ability isn’t actually a sorcery. The player doesn’t actually need to have a sorcery card that they could cast.

#### CR 603.4

A triggered ability may read “When/Whenever/At [trigger event], if [condition], [effect].” When the trigger event occurs, the ability checks whether the stated condition is true. The ability triggers only if it is; otherwise it does nothing. If the ability triggers, it checks the stated condition again as it resolves. If the condition isn’t true at that time, the ability is removed from the stack and does nothing. Note that this mirrors the check for legal targets. This rule is referred to as the “intervening ‘if’ clause” rule. (The word “if” has only its normal English meaning anywhere else …

#### CR 702.2b

A creature with toughness greater than 0 that’s been dealt damage by a source with deathtouch since the last time state-based actions were checked is destroyed as a state-based action. See rule 704.

#### CR 702.6a

Equip is an activated ability of Equipment cards. “Equip [cost]” means “[Cost]: Attach this permanent to target creature you control. Activate only as a sorcery.”

#### CR 702.11b

“Hexproof” on a permanent means “This permanent can’t be the target of spells or abilities your opponents control.”

#### CR 702.42a

Entwine is a static ability of modal spells (see rule 700.2) that functions while the spell is on the stack. “Entwine [cost]” means “You may choose all modes of this spell instead of just the number specified. If you do, you pay an additional [cost].” Using the entwine ability follows the rules for choosing modes and paying additional costs in rules 601.2b and 601.2f–h.

#### CR 702.88a

Rebound appears on some instants and sorceries. It represents a static ability that functions while the spell is on the stack and may create a delayed triggered ability. “Rebound” means “If this spell was cast from your hand, instead of putting it into your graveyard as it resolves, exile it and, at the beginning of your next upkeep, you may cast this card from exile without paying its mana cost.”

#### CR 903.9a

If a commander is in a graveyard or in exile and that object was put into that zone since the last time state-based actions were checked, its owner may put it into the command zone. This is a state-based action. See rule 704.

