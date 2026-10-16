---
title: "Davros, Dalek Creator — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Davros, Dalek Creator — Interaction Review

> Bot cycle 46 · batch A · reviewed 2026-10-16. Deck: [Davros, Dalek Creator](../decks/davros-dalek-creator.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/davros-dalek-creator.txt`](../../exports/grixis-archidekt/davros-dalek-creator.txt) · SHA-256 `c4d7cc547b742cc562c33e9ab3debca5d2c51fdeaad0b81a9f01e0a2c4f5bf30` |
| Rulings | **9** (9 verified · 0 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`Davros_Dalek_Creator_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/davros_dalek_creator_2026-10-14/Davros_Dalek_Creator_Rules_Attestation.json) (15 interactions, all PASS) |

## Contents
- [Summary](#summary)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Engines and payoffs](#engines-and-payoffs)
- [Key card-pair interactions](#key-card-pair-interactions)
- [Replacement and prevention effects](#replacement-and-prevention-effects)
- [Trigger ordering](#trigger-ordering)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [Rules cited](#rules-cited)

## Summary

Davros, Dalek Creator is a drain-and-discard deck that rewards opponents losing 3+ life each turn. This review re-verifies all fifteen items of the deck's rules attestation.

Key rule: Davros's condition is checked on resolution, not an intervening if, so end-step drains ordered above it count. Entropic Battlecruiser turns discard choices into life loss. No list errors.

## Commander rules text and edge cases

### davros-01: The 3-life check is on resolution, not an intervening if

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Davros, Dalek Creator

**Ruling.** Davros's 'if an opponent lost 3 or more life this turn' comes after the effect, not right after the trigger condition, so it isn't an intervening-if clause. Davros always triggers at your end step and checks the turn's life-loss history on resolution. So end-step drains (Perforating Artist, Wound Reflection, Missy) ordered above Davros still count.

**Citations**

- Oracle, *Davros, Dalek Creator*: “At the beginning of your end step, create a 3/3 black Dalek artifact creature token with menace if an opponent lost 3 or more life this turn.”
- [CR 603.4](#cr-6034), [CR 608.2h](#cr-6082h)
- Source (re-verified): [`Davros_Dalek_Creator_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/davros_dalek_creator_2026-10-14/Davros_Dalek_Creator_Rules_Attestation.json) → “Davros end-step trigger and 3-life qualification timing”

### davros-02: Villainous choices resolve player by player

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Davros, Dalek Creator

**Ruling.** Each qualifying opponent faces 'you draw a card, or that player discards a card'. With several opponents, the first in turn order chooses and that option is carried out before the next player chooses. A player may pick either option even if it's impossible (discarding from an empty hand).

**Citations**

- Scryfall ruling, *Davros, Dalek Creator*: “If a spell or ability requires multiple players to face a villainous choice, the result is a little different from other effects in Magic. In that case, the first player in turn order makes their choice and the action for that choice is performed before the next player makes their choice.”
- Scryfall ruling, *Davros, Dalek Creator*: “A player facing a villainous choice can always choose either option, even if one or both of the options are impossible.”
- [CR 701.55a](#cr-70155a)

## Engines and payoffs

### davros-06: Entropic Battlecruiser at station 1+ punishes discards

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Davros, Dalek Creator, Entropic Battlecruiser, Court of Ambition, Geier Reach Sanitarium

**Ruling.** With at least one charge counter, Battlecruiser makes each opponent who discards lose 3 life. It doesn't need to be a creature for that; it becomes an artifact creature at 8+. Station is sorcery speed: tap another creature, add counters equal to its power.

This turns 'or discard' options into 3 life:
- Court of Ambition's upkeep 'unless they discard'.
- Davros's own discard option.
- Geier Reach Sanitarium's draw-then-discard on your turn, which also qualifies opponents for Davros.

**Citations**

- Oracle, *Entropic Battlecruiser*: “1+ | Whenever an opponent discards a card, they lose 3 life.”
- [CR 702.184a](#cr-702184a), [CR 603.2](#cr-6032)
- Source (re-verified): [`Davros_Dalek_Creator_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/davros_dalek_creator_2026-10-14/Davros_Dalek_Creator_Rules_Attestation.json) → “Entropic Battlecruiser station thresholds”
- Source (re-verified): [`Davros_Dalek_Creator_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/davros_dalek_creator_2026-10-14/Davros_Dalek_Creator_Rules_Attestation.json) → “Court of Ambition + Entropic Battlecruiser at station 1+”
- Source (re-verified): [`Davros_Dalek_Creator_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/davros_dalek_creator_2026-10-14/Davros_Dalek_Creator_Rules_Attestation.json) → “Geier Reach Sanitarium + Entropic Battlecruiser at station 1+”

## Key card-pair interactions

### davros-07: Fixed 3-life enablers

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Davros, Dalek Creator, Maestros Charm, Loyal Subordinate

**Ruling.** Maestros Charm's drain mode (each opponent loses 3, you gain 3) and Loyal Subordinate (beginning of combat, if you control your commander: each opponent loses 3) each qualify every opponent for Davros that turn.

**Citations**

- Oracle, *Loyal Subordinate*: “Lieutenant — At the beginning of combat on your turn, if you control your commander, each opponent loses 3 life.”
- Oracle, *Maestros Charm*: “Each opponent loses 3 life and you gain 3 life.”
- [CR 119.3](#cr-1193)
- Source (re-verified): [`Davros_Dalek_Creator_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/davros_dalek_creator_2026-10-14/Davros_Dalek_Creator_Rules_Attestation.json) → “Maestros Charm threshold mode”
- Source (re-verified): [`Davros_Dalek_Creator_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/davros_dalek_creator_2026-10-14/Davros_Dalek_Creator_Rules_Attestation.json) → “Loyal Subordinate threshold line”

### davros-08: Labyrinth Raptor and menace Daleks

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Davros, Dalek Creator, Labyrinth Raptor

**Ruling.** Davros and the Dalek tokens have menace. When one becomes blocked, Labyrinth Raptor makes the defending player sacrifice a creature of their choice that's blocking it. {B}{R} gives all your menace creatures +1/+0.

**Citations**

- Oracle, *Labyrinth Raptor*: “Whenever a creature you control with menace becomes blocked, defending player sacrifices a creature of their choice that's blocking it.”
- [CR 702.111b](#cr-702111b), [CR 509.1h](#cr-5091h)
- Source (re-verified): [`Davros_Dalek_Creator_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/davros_dalek_creator_2026-10-14/Davros_Dalek_Creator_Rules_Attestation.json) → “Labyrinth Raptor + Davros/Dalek menace creatures”

## Replacement and prevention effects

### davros-05: The Valeyard doubles every villainous choice

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Davros, Dalek Creator, The Valeyard, Missy, The Dalek Emperor, Genesis of the Daleks

**Ruling.** Whenever an opponent would face a villainous choice, The Valeyard makes them face it an additional time; they can choose differently. This doubles Davros's, Missy's, The Dalek Emperor's and Genesis of the Daleks chapter IV choices.

**Citations**

- Oracle, *The Valeyard*: “If an opponent would face a villainous choice, they face that choice an additional time.”
- [CR 701.55a](#cr-70155a), [CR 614.1a](#cr-6141a)
- Source (re-verified): [`Davros_Dalek_Creator_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/davros_dalek_creator_2026-10-14/Davros_Dalek_Creator_Rules_Attestation.json) → “Davros + The Valeyard”

## Trigger ordering

### davros-03: Order end-step drains above Davros

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Davros, Dalek Creator, Perforating Artist, Wound Reflection, Missy

**Ruling.** Perforating Artist (raid), Wound Reflection and Missy also trigger at the beginning of your end step. Put Davros on the stack first and the others on top so they resolve first:
- **Wound Reflection:** doubles each opponent's life lost so far, so someone who lost 2 has now lost 4.
- **Perforating Artist:** each opponent loses 3 unless they sacrifice a nonland permanent or discard (and a discard triggers Battlecruiser).
- **Missy:** each artifact creature deals 1 damage, or you draw and chaos ensues.

Then Davros resolves with more opponents qualifying.

**Citations**

- Scryfall ruling, *Wound Reflection*: “When Wound Reflection's ability resolves, it checks how much life each opponent lost over the course of the turn, then it causes that opponent to lose that much life.”
- [CR 603.3b](#cr-6033b)
- Source (re-verified): [`Davros_Dalek_Creator_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/davros_dalek_creator_2026-10-14/Davros_Dalek_Creator_Rules_Attestation.json) → “Perforating Artist ordering with Davros”
- Source (re-verified): [`Davros_Dalek_Creator_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/davros_dalek_creator_2026-10-14/Davros_Dalek_Creator_Rules_Attestation.json) → “Wound Reflection ordering with Davros”
- Source (re-verified): [`Davros_Dalek_Creator_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/davros_dalek_creator_2026-10-14/Davros_Dalek_Creator_Rules_Attestation.json) → “Missy ordering with Davros”

### davros-04: Copying and doubling Davros

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Davros, Dalek Creator, Scientist Supreme of A.I.M., Strionic Resonator, Roaming Throne, Auton Soldier

**Ruling.** Several cards repeat Davros's trigger; each instance resolves separately and checks life loss when it resolves:
- **Scientist Supreme (once per turn, your turn) and Strionic Resonator:** copy it, because Davros is an artifact.
- **Roaming Throne:** naming Alien or Scientist adds a separate trigger.
- **Auton Soldier:** as a nonlegendary artifact copy of Davros, it has its own trigger.

**Citations**

- Oracle, *Strionic Resonator*: “{2}, {T}: Copy target triggered ability you control.”
- [CR 707.10](#cr-70710), [CR 603.2](#cr-6032), [CR 707.9b](#cr-7079b)
- Source (re-verified): [`Davros_Dalek_Creator_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/davros_dalek_creator_2026-10-14/Davros_Dalek_Creator_Rules_Attestation.json) → “Davros + Scientist Supreme of A.I.M.”
- Source (re-verified): [`Davros_Dalek_Creator_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/davros_dalek_creator_2026-10-14/Davros_Dalek_Creator_Rules_Attestation.json) → “Davros + Roaming Throne”
- Source (re-verified): [`Davros_Dalek_Creator_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/davros_dalek_creator_2026-10-14/Davros_Dalek_Creator_Rules_Attestation.json) → “Davros + Strionic Resonator”
- Source (re-verified): [`Davros_Dalek_Creator_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/davros_dalek_creator_2026-10-14/Davros_Dalek_Creator_Rules_Attestation.json) → “Auton Soldier entering as Davros”

## Zones, commander tax and the command zone

### davros-09: Commander tax; Loyal Subordinate needs Davros out

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Davros, Dalek Creator, Loyal Subordinate

**Ruling.** Davros costs {1}{U}{B}{R}, then 6, then 8. Loyal Subordinate checks that you control your commander at beginning of combat, so it's off while Davros is in the command zone. Davros is an artifact creature, so artifact copy effects (Scientist Supreme, Auton Soldier) apply.

**Citations**

- Oracle, *Davros, Dalek Creator*: “Menace”
- [CR 903.8](#cr-9038), [CR 603.4](#cr-6034)

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 119.3

If an effect causes a player to gain life or lose life, that player’s life total is adjusted accordingly.

#### CR 509.1h

An attacking creature with one or more creatures declared as blockers for it becomes a blocked creature; one with no creatures declared as blockers for it becomes an unblocked creature. This remains unchanged until the creature is removed from combat, an effect says that it becomes blocked or unblocked, or the combat phase ends, whichever comes first. A creature remains blocked even if all the creatures blocking it are removed from combat.

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 603.3b

If multiple abilities have triggered since the last time a player received priority, the abilities are placed on the stack in a two-part process. First, each player, in APNAP order, puts each triggered ability they control with a trigger condition that isn’t another ability triggering on the stack in any order they choose. (See rule 101.4.) Second, each player, in APNAP order, puts all remaining triggered abilities they control on the stack in any order they choose. Then the game once again checks for and performs state-based actions until none are performed, then abilities that triggered …

#### CR 603.4

A triggered ability may read “When/Whenever/At [trigger event], if [condition], [effect].” When the trigger event occurs, the ability checks whether the stated condition is true. The ability triggers only if it is; otherwise it does nothing. If the ability triggers, it checks the stated condition again as it resolves. If the condition isn’t true at that time, the ability is removed from the stack and does nothing. Note that this mirrors the check for legal targets. This rule is referred to as the “intervening ‘if’ clause” rule. (The word “if” has only its normal English meaning anywhere else …

#### CR 608.2h

If an effect requires information from the game (such as the number of creatures on the battlefield), the answer is determined only once, when the effect is applied. If the effect requires information from a specific object, including the source of the ability itself, the effect uses the current information of that object if it’s in the public zone it was expected to be in; if it’s no longer in that zone, or if the effect has moved it from a public zone to a hidden zone, the effect uses the object’s last known information. See rule 113.7a. If an ability states that an object does something, …

#### CR 614.1a

Effects that use the word “instead” are replacement effects. Most replacement effects use the word “instead” to indicate what events will be replaced with other events.

#### CR 701.55a

“[A player] faces a villainous choice — [option A], or [option B]” means “[A player] chooses [option A] or [option B]. Then all actions in the chosen option are performed.”

#### CR 702.111b

A creature with menace can’t be blocked except by two or more creatures. (See rule 509, “Declare Blockers Step.”)

#### CR 702.184a

Station is an activated ability. “Station” means “Tap another untapped creature you control: Put a number of charge counters on this permanent equal to the tapped creature’s power. Activate only as a sorcery.”

#### CR 707.9b

Some copy effects modify a characteristic as part of the copying process. The final set of values for that characteristic becomes part of the copiable values of the copy.

#### CR 707.10

To copy a spell, activated ability, or triggered ability means to put a copy of it onto the stack; a copy of a spell isn’t cast and a copy of an activated ability isn’t activated. A copy of a spell or ability copies both the characteristics of the spell or ability and all decisions made for it, including modes, targets, the value of X, and additional or alternative costs. (See rule 601, “Casting Spells.”) Choices that are normally made on resolution are not copied. If an effect of the copy refers to objects used to pay its costs, it uses the objects used to pay the costs of the original spell …

#### CR 903.8

A player may cast a commander they own from the command zone. A commander cast from the command zone costs an additional {2} for each previous time the player casting it has cast it from the command zone that game. This additional cost is informally known as the “commander tax.”

