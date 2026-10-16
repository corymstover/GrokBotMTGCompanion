---
title: "Loki, the Deceiver — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Loki, the Deceiver — Interaction Review

> Bot cycle 49 · batch C · reviewed 2026-10-16. Deck: [Loki, the Deceiver](../decks/loki-the-deceiver.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/loki-the-deceiver.txt`](../../exports/grixis-archidekt/loki-the-deceiver.txt) · SHA-256 `a46c0474940b72ac3ae843bd8e6fdcdd9dd10988222dbe0a23a42daeb96cfd53` |
| Rulings | **7** (7 verified · 0 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`Loki_the_Deceiver_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/loki_the_deceiver_2026-10-14/Loki_the_Deceiver_Rules_Attestation.json) (10 interactions, all PASS (Vulture and Puppet Master are only named in the red-team item and aren't in the list)) |

## Contents
- [Summary](#summary)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Layers and continuous effects](#layers-and-continuous-effects)
- [Trigger ordering](#trigger-ordering)
- [Rules cited](#rules-cited)

## Summary

Loki, the Deceiver attacks and makes a hasty, non-legendary Illusion copy of another Villain, and draws whenever Villains connect. This review re-verifies all 10 attestation items. There are no Spellbook combos for this list; it's a value and combat engine.

Rules surprises: Loki's tokens enter attacking, so the copied creature's own attack triggers never fire; Sundial only saves the token if the sacrifice trigger is already on the stack; the Scepter's temporary Villain type isn't copied. No list errors.

## Commander rules text and edge cases

### loki-01: The token enters attacking, so its own attack triggers don't fire

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Loki, the Deceiver, Ultron, Unlimited, Killmonger, Ruthless Usurper

**Ruling.** Loki's token enters tapped and attacking but was never declared as an attacker. 'Whenever this attacks' abilities of the copied Villain don't trigger: Ultron's connive, Killmonger's +1/+0. Enter triggers, static abilities and combat-damage triggers all work, including Killmonger's artifact sacrifice + Treasure. The token isn't legendary, so the legend rule never applies. You choose which player it attacks.

**Citations**

- Oracle, *Loki, the Deceiver*: “Whenever Loki attacks, create a tapped and attacking token that's a copy of another target Villain you control, except it isn't legendary and it's an Illusion in addition to its other types. Sacrifice that token at the beginning of the next end step.”
- [CR 508.3a](#cr-5083a), [CR 508.4](#cr-5084), [CR 707.9b](#cr-7079b)
- Source (re-verified): [`Loki_the_Deceiver_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/loki_the_deceiver_2026-10-14/Loki_the_Deceiver_Rules_Attestation.json) → “Loki attack token and enters-attacking timing”
- Source (re-verified): [`Loki_the_Deceiver_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/loki_the_deceiver_2026-10-14/Loki_the_Deceiver_Rules_Attestation.json) → “Attack-trigger copy-target red-team”

### loki-02: Villain combat damage draws once per batch

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Loki, the Deceiver, Red Ghost, Intangible Genius

**Ruling.** 'Whenever one or more Villains you control deal combat damage to a player' triggers once per player dealt damage at once, not once per Villain. Red Ghost is an unblockable Villain, so it reliably connects. If Loki's draw is your second card of the turn, Red Ghost makes a hasty 3/3 Ape Villain, though only after combat damage.

**Citations**

- Oracle, *Loki, the Deceiver*: “Whenever one or more Villains you control deal combat damage to a player, draw a card.”
- Oracle, *Red Ghost, Intangible Genius*: “Whenever you draw your second card each turn, create a 3/3 red Ape Villain creature token with haste.”
- [CR 603.2c](#cr-6032c), [CR 510.2](#cr-5102)
- Source (re-verified): [`Loki_the_Deceiver_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/loki_the_deceiver_2026-10-14/Loki_the_Deceiver_Rules_Attestation.json) → “Loki plus Red Ghost, Intangible Genius”

## Layers and continuous effects

### loki-03: Titan of Littjara and Roaming Throne choose Villain

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Loki, the Deceiver, Titan of Littjara, Roaming Throne

**Ruling.** A Titan or Throne that chose Villain is a Villain and a legal Loki target. A Loki token of Titan makes its own as-enters choice (choose Villain again) and gets its enter draw. A Throne on Villain makes triggers of other Villains trigger again. That includes Loki (a God Sorcerer Villain): two attack triggers and two copies. A Throne token made by Loki arrives too late to double the trigger that created it.

**Citations**

- Oracle, *Roaming Throne*: “If a triggered ability of another creature you control of the chosen type triggers, it triggers an additional time.”
- Scryfall ruling, *Titan of Littjara*: “The choice of creature type is made as Titan of Littjara enters the battlefield. Players can't respond to this choice. Titan of Littjara's second ability starts applying immediately.”
- Scryfall ruling, *Roaming Throne*: “Roaming Throne's last ability doesn't copy the triggered ability; it just causes the ability to trigger an additional time. Any choices made as you put the ability onto the stack, such as modes and targets, are made separately for each instance of the ability.”
- [CR 614.12](#cr-61412), [CR 603.2](#cr-6032), [CR 707.2](#cr-7072)
- Source (re-verified): [`Loki_the_Deceiver_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/loki_the_deceiver_2026-10-14/Loki_the_Deceiver_Rules_Attestation.json) → “Loki plus Titan of Littjara”
- Source (re-verified): [`Loki_the_Deceiver_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/loki_the_deceiver_2026-10-14/Loki_the_Deceiver_Rules_Attestation.json) → “Roaming Throne choosing Villain”

### loki-04: Hall of Echoes as a second Loki

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Loki, the Deceiver, Hall of Echoes

**Ruling.** For {5}, Hall of Echoes becomes a copy of Loki and turns off the legend rule for your permanents that turn. If you've controlled Hall since your turn began, it isn't summoning sick and can attack: two Loki attack triggers. Becoming a copy isn't entering. Both effects end together at end of turn, so there's never a legend-rule moment while Hall is still Loki.

**Citations**

- Oracle, *Hall of Echoes*: “{5}: This land becomes a copy of target creature you control until end of turn. The "legend rule" doesn't apply to permanents you control this turn.”
- Scryfall ruling, *Hall of Echoes*: “Both effects of Hall of Echoes's last ability have the same duration, and they'll wear off at exactly the same time. As such, there's no moment at which Hall of Echoes is still a copy of the target creature after the "legend rule" begins to apply again.”
- Scryfall ruling, *Hall of Echoes*: “Because Hall of Echoes isn't entering the battlefield when it becomes a copy of the creature, any "When [this creature] enters" or "[This creature] enters with" abilities of the copied creature won't apply.”
- [CR 707.2](#cr-7072), [CR 704.5j](#cr-7045j), [CR 302.6](#cr-3026)
- Source (re-verified): [`Loki_the_Deceiver_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/loki_the_deceiver_2026-10-14/Loki_the_Deceiver_Rules_Attestation.json) → “Hall of Echoes copying Loki before combat”

### loki-07: Loki's Scepter: a temporary Villain copies as a non-Villain

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Loki, the Deceiver, Loki's Scepter

**Ruling.** Loki's Scepter steals a creature until end of turn and makes it a Villain with haste, so it can attack and be Loki's copy target. The token copies only the copiable values, though. The Scepter's Villain type isn't copiable, so a non-Villain creature's token is only an Illusion, not a Villain. It doesn't count for Loki's draw or Doctor Octopus's anthem.

**Citations**

- Oracle, *Loki's Scepter*: “When Loki's Scepter enters, gain control of target creature until end of turn. Untap that creature. Until end of turn, it becomes a Villain in addition to its other types and gains haste.”
- [CR 707.2](#cr-7072), [CR 613.1d](#cr-6131d)
- Source (re-verified): [`Loki_the_Deceiver_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/loki_the_deceiver_2026-10-14/Loki_the_Deceiver_Rules_Attestation.json) → “Loki's Scepter temporary Villain type and Loki copying”

## Trigger ordering

### loki-05: Keeping the token: The Master, Multiplied and Sundial

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Loki, the Deceiver, The Master, Multiplied, Sundial of the Infinite

**Ruling.** Loki's end-step sacrifice is a delayed trigger you control, so The Master, Multiplied stops it and the token stays. With Sundial, let the sacrifice trigger go on the stack, then end the turn: the trigger is exiled and won't come back. If you activate Sundial earlier, the end step is skipped and 'next end step' triggers wait for the next turn's end step, so the token isn't saved.

**Citations**

- Oracle, *The Master, Multiplied*: “Triggered abilities you control can't cause you to sacrifice or exile creature tokens you control.”
- Scryfall ruling, *Sundial of the Infinite*: “If Sundial of the Infinite's ability is activated before the end step, any "at the beginning of the end step"-triggered abilities won't get the chance to trigger that turn because the end step is skipped.”
- [CR 603.7a](#cr-6037a), [CR 724.1](#cr-7241)
- Source (re-verified): [`Loki_the_Deceiver_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/loki_the_deceiver_2026-10-14/Loki_the_Deceiver_Rules_Attestation.json) → “The Master, Multiplied and Loki's delayed sacrifice”
- Source (re-verified): [`Loki_the_Deceiver_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/loki_the_deceiver_2026-10-14/Loki_the_Deceiver_Rules_Attestation.json) → “Sundial of the Infinite and Loki's delayed sacrifice”

### loki-06: Doctor Octopus token: anthem now, draw before the sacrifice

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Loki, the Deceiver, Doctor Octopus, Master Planner

**Ruling.** A Loki copy of Doctor Octopus gives other Villains +2/+2 for the rest of combat. At your end step, its refill-to-eight trigger and Loki's delayed sacrifice trigger together. You order them so the draw resolves first. The refill checks your hand size when it resolves.

**Citations**

- Oracle, *Doctor Octopus, Master Planner*: “At the beginning of your end step, if you have fewer than eight cards in hand, draw cards equal to the difference.”
- [CR 603.3b](#cr-6033b), [CR 613.4c](#cr-6134c)
- Source (re-verified): [`Loki_the_Deceiver_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/loki_the_deceiver_2026-10-14/Loki_the_Deceiver_Rules_Attestation.json) → “Doctor Octopus copy token during combat and end step”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 302.6

A creature’s activated ability with the tap symbol or the untap symbol in its activation cost can’t be activated unless the creature has been under its controller’s control continuously since their most recent turn began. A creature can’t attack unless it has been under its controller’s control continuously since their most recent turn began. This rule is informally called the “summoning sickness” rule.

#### CR 508.3a

An ability that reads “Whenever [a creature] attacks, . . .” triggers if that creature is declared as an attacker. Similarly, “Whenever [a creature] attacks [a player, planeswalker, or battle], . . .” triggers if that creature is declared as an attacker attacking that player or permanent. Such abilities won’t trigger if a creature is put onto the battlefield attacking.

#### CR 508.4

If a creature is put onto the battlefield attacking, its controller chooses which defending player, planeswalker a defending player controls, or battle a defending player protects it’s attacking as it enters the battlefield (unless the effect that put it onto the battlefield specifies what it’s attacking). Similarly, if an effect states that a creature is attacking, its controller chooses which defending player, planeswalker a defending player controls, or battle a defending player protects it’s attacking (unless the effect has already specified). Such creatures are “attacking” but, for the …

#### CR 510.2

Second, all combat damage that’s been assigned is dealt simultaneously. This turn-based action doesn’t use the stack. No player has the chance to cast spells or activate abilities between the time combat damage is assigned and the time it’s dealt.

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 603.2c

An ability triggers only once each time its trigger event occurs. However, it can trigger repeatedly if one event contains multiple occurrences.

#### CR 603.3b

If multiple abilities have triggered since the last time a player received priority, the abilities are placed on the stack in a two-part process. First, each player, in APNAP order, puts each triggered ability they control with a trigger condition that isn’t another ability triggering on the stack in any order they choose. (See rule 101.4.) Second, each player, in APNAP order, puts all remaining triggered abilities they control on the stack in any order they choose. Then the game once again checks for and performs state-based actions until none are performed, then abilities that triggered …

#### CR 603.7a

Delayed triggered abilities are created during the resolution of spells or abilities, as the result of a replacement effect being applied, or as a result of a static ability that allows a player to take an action. A delayed triggered ability won’t trigger until it has actually been created, even if its trigger event occurred just beforehand. Other events that happen earlier may make the trigger event impossible.

#### CR 613.1d

Layer 4: Type-changing effects are applied. These include effects that change an object’s card type, subtype, and/or supertype.

#### CR 613.4c

Layer 7c: Effects and counters that modify power and/or toughness (but don’t set power and/or toughness to a specific number or value) are applied.

#### CR 614.12

Some replacement effects modify how a permanent enters the battlefield. (See rules 614.1c–d.) Such effects may come from the permanent itself if they affect only that permanent (as opposed to a general subset of permanents that includes it). They may also come from other sources. To determine which replacement effects apply and how they apply, check the characteristics of the permanent as it would exist on the battlefield, taking into account replacement effects that have already modified how it enters the battlefield (see rule 616.1), continuous effects from the permanent’s own static …

#### CR 704.5j

If two or more legendary permanents with the same name are controlled by the same player, that player chooses one of them, and the rest are put into their owners’ graveyards. This is called the “legend rule.”

#### CR 707.2

When copying an object, the copy acquires the copiable values of the original object’s characteristics and, for an object on the stack, choices made when casting or activating it (mode, targets, the value of X, whether it was kicked, how it will affect multiple targets, and so on). The copiable values are the values derived from the text printed on the object (that text being name, mana cost, color indicator, card type, subtype, supertype, rules text, power, toughness, and/or loyalty), as modified by other copy effects, by its face-down status, and by “as . . . enters” and “as . . . is turned …

#### CR 707.9b

Some copy effects modify a characteristic as part of the copying process. The final set of values for that characteristic becomes part of the copiable values of the copy.

#### CR 724.1

Some cards end the turn. When an effect ends the turn, follow these steps in order, as they differ from the normal process for resolving spells and abilities (see rule 608, “Resolving Spells and Abilities”).

