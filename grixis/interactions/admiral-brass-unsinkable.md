---
title: "Admiral Brass, Unsinkable — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Admiral Brass, Unsinkable — Interaction Review

> Bot cycle 46 · batch A · reviewed 2026-10-16. Deck: [Admiral Brass, Unsinkable](../decks/admiral-brass-unsinkable.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-15), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Current list | [`exports/grixis-archidekt/admiral-brass-unsinkable.txt`](../../exports/grixis-archidekt/admiral-brass-unsinkable.txt) · SHA-256 `e29dc5ed5ec6cc85863cf82408f7ecb29128e6668b5adf6ac60ea2c2b4deb2b5` |
| Rulings | **15** (13 verified · 1 uncertain · 1 list flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-15 · rulings 2026-10-15 |
| Source attestations | [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) (deck #3: RULES PASS) |

## Contents
- [Summary](#summary)
- [Flags and open questions](#flags-and-open-questions)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Engines and payoffs](#engines-and-payoffs)
- [Key card-pair interactions](#key-card-pair-interactions)
- [Layers and continuous effects](#layers-and-continuous-effects)
- [Replacement and prevention effects](#replacement-and-prevention-effects)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [What the list depends on](#what-the-list-depends-on)
- [Rules cited](#rules-cited)

## Summary

Admiral Brass, Unsinkable is a Pirate reanimator. Each combat she returns a Pirate creature card as a hasty base 4/4 with a finality counter. This review re-verifies the retrospective attestation (Power Conduit removing the counter, Roaming Throne doubling, the base 4/4 versus counters) and adds the graveyard package.

Flag: finality counters make returned creatures get exiled instead of dying. That quietly turns off Pitiless Plunderer, Victimize's sacrifice and later recursion for those creatures unless Power Conduit removes the counter first.

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [brass-02](#brass-02-finality-counters-mean-exile-not-death) | 🚩 list flag (anti-synergy) | Finality counters mean exile, not death | Pitiless Plunderer, Victimize's sacrifice and the sacrifice outlets (Broadside Bombardiers' boast) lose value on Brass-returned creatures, which are exiled instead of dying. A minor non-bo, not a list error: remove the counter with Power Conduit first, or sacrifice other fodder. |
| [brass-10](#brass-10-mass-reanimation-patriarchs-bidding-and-living-death-are-symmetric) | ⚠️ uncertain | Mass reanimation: Patriarch's Bidding and Living Death are symmetric | Whether these are favorable depends on opponents' graveyards at the time; this is a play-pattern judgment, not a rules question. |

## Commander rules text and edge cases

### brass-01: The combat reanimation: Pirate creature card, finality counter, base 4/4, haste

**Status:** ✅ verified · **Cards:** Admiral Brass, Unsinkable

**Ruling.** At the beginning of combat on your turn, Brass may return target Pirate creature card from your graveyard. It comes back with a finality counter, has base power and toughness 4/4 indefinitely, and haste until end of turn, so it can attack that combat. The trigger targets on the stack, so opponents can respond by exiling the card from your graveyard. It also needs a Pirate creature card in your graveyard when the trigger goes on the stack. Brass's own enter trigger (mill four) and Buried Alive, Entomb and the looters fill the graveyard.

**Citations**

- Oracle, *Admiral Brass, Unsinkable*: “At the beginning of combat on your turn, you may return target Pirate creature card from your graveyard to the battlefield with a finality counter on it. It has base power and toughness 4/4. It gains haste until end of turn.”
- Scryfall ruling, *Admiral Brass, Unsinkable*: “Finality counters work on any permanent, not only creatures. If a permanent with a finality counter on it would be put into a graveyard from the battlefield, exile it instead.”
- [CR 122.1h](#cr-1221h), [CR 613.4b](#cr-6134b), [CR 115.1](#cr-1151)
- Source (re-verified): [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) → “may return a Pirate creature card from your graveyard with a finality counter, base P/T 4/4, and haste until end of turn.”

## Engines and payoffs

### brass-07: Skeleton Crew triggers on every reanimation and encore

**Status:** ✅ verified · **Cards:** Admiral Brass, Unsinkable, Skeleton Crew, Amphin Mutineer, Living Death

**Ruling.** Whenever one or more creature cards leave your graveyard, Skeleton Crew makes a 2/2 Skeleton Pirate. Each separate event triggers it once: Brass's reanimation, Reanimate, Animate Dead, Victimize (two cards at once = one trigger), Living Death (one trigger), and exiling Amphin Mutineer to pay encore. Its own {5}{B} return from the graveyard doesn't trigger it.

**Citations**

- Oracle, *Skeleton Crew*: “Whenever one or more creature cards leave your graveyard, create a 2/2 black Skeleton Pirate creature token.”
- Scryfall ruling, *Skeleton Crew*: “If two or more creature cards leave your graveyard as a single event, Skeleton Crew's second ability will trigger once.”
- Scryfall ruling, *Skeleton Crew*: “Resolving Skeleton Crew's last ability won't cause its second ability to trigger.”
- [CR 603.10a](#cr-60310a)

### brass-08: Descend: milling and discarding permanent cards

**Status:** ✅ verified · **Cards:** Admiral Brass, Unsinkable, Enterprising Scallywag, Brass's Tunnel-Grinder // Tecutlan, the Searing Rift

**Ruling.** You descend when a permanent card goes to your graveyard from anywhere. Brass's mill four, Entomb, Buried Alive and discarding creatures all count; tokens don't. Enterprising Scallywag and Tunnel-Grinder check once at your end step. They needn't have been on the battlefield when you descended.

**Citations**

- Oracle, *Enterprising Scallywag*: “At the beginning of your end step, if you descended this turn, create a Treasure token.”
- Scryfall ruling, *Enterprising Scallywag*: “Tokens are not cards, and while tokens are put into the graveyard before ceasing to exist, that action doesn't count as a player having descended.”
- [CR 700.11](#cr-70011)

## Key card-pair interactions

### brass-03: Power Conduit removes the finality counter

**Status:** ✅ verified · **Cards:** Admiral Brass, Unsinkable, Power Conduit

**Ruling.** Power Conduit's cost includes removing a counter from a permanent you control, so the finality counter can go. Without it, the creature dies normally and can be reanimated again later. The 4/4 base and haste come from Brass's resolved effect, not from the counter, so they stay. Removing the counter is a cost, so it happens immediately and can't be responded to. The creature has to be on the battlefield first.

**Citations**

- Oracle, *Power Conduit*: “{T}, Remove a counter from a permanent you control: Choose one —”
- [CR 122.1h](#cr-1221h), [CR 602.2](#cr-6022)
- Source (re-verified): [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) → “removing the finality counter before the creature would be put into a graveyard means that counter no longer supplies the exile replacement for that later event.”

### brass-04: Roaming Throne (Pirate) doubles the reanimation

**Status:** ✅ verified · **Cards:** Admiral Brass, Unsinkable, Roaming Throne

**Ruling.** Brass is a Pirate creature, so Roaming Throne naming Pirate makes Brass's beginning-of-combat trigger trigger an additional time. Each instance needs its own target Pirate creature card. If Throne is already on the battlefield when Brass enters, Brass's mill-four enter trigger is doubled too.

**Citations**

- Oracle, *Roaming Throne*: “If a triggered ability of another creature you control of the chosen type triggers, it triggers an additional time.”
- [CR 603.2](#cr-6032)
- Source (re-verified): [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) → “`Roaming Throne` choosing Pirate causes Brass's beginning-of-combat triggered ability to trigger an additional time”

### brass-05: Changeling cards are Pirate creature cards in the graveyard

**Status:** ✅ verified · **Cards:** Admiral Brass, Unsinkable, Changeling Outcast

**Ruling.** Changeling works in every zone, so Changeling Outcast in your graveyard is a legal 'Pirate creature card' target for Brass. It returns as a 4/4 haste creature that can't be blocked.

**Citations**

- Oracle, *Changeling Outcast*: “Changeling (This card is every creature type.)”
- [CR 702.73a](#cr-70273a)

### brass-09: Wonder in the graveyard gives your team flying

**Status:** ✅ verified · **Cards:** Admiral Brass, Unsinkable, Wonder, Entomb, Buried Alive

**Ruling.** Wonder works from the graveyard as long as you control an Island. The list has 2 basic Islands, Volcanic Island and other Island-typed duals (Underground Sea, Steam Vents, Watery Grave, Xander's Lounge). Entomb or Buried Alive puts Wonder in the graveyard for evasive Pirate attacks that feed Beckett-style combat triggers. Wonder is an Incarnation, not a Pirate, so Brass can't return it.

**Citations**

- Oracle, *Wonder*: “As long as this card is in your graveyard and you control an Island, creatures you control have flying.”
- [CR 113.6](#cr-1136)

### brass-10: Mass reanimation: Patriarch's Bidding and Living Death are symmetric

**Status:** ⚠️ uncertain · **Cards:** Admiral Brass, Unsinkable, Patriarch's Bidding, Living Death

**Ruling.** Each player chooses a type for Patriarch's Bidding. You choose Pirate (changelings included), but opponents return their own chosen type too. Living Death returns every player's graveyard creatures after everyone sacrifices their board. Your finality-counter creatures are exiled during the sacrifice (brass-02). These are table-wide effects; the value depends on the graveyards.

**Uncertain.** Whether these are favorable depends on opponents' graveyards at the time; this is a play-pattern judgment, not a rules question.

**Citations**

- Scryfall ruling, *Patriarch's Bidding*: “Then, all creature cards that have one or more of the chosen types are returned to the battlefield at the same time.”
- Scryfall ruling, *Living Death*: “Then all players sacrifice all creatures they control at the same time.”
- [CR 101.4](#cr-1014)

### brass-11: Victimize needs two targets and a sacrifice on resolution

**Status:** ✅ verified · **Cards:** Admiral Brass, Unsinkable, Victimize

**Ruling.** Victimize must target two creature cards in your graveyard. The sacrifice happens on resolution, so the creature you sacrifice can't be one of the returned cards. If one target is gone you still sacrifice and return the other. A Brass-returned creature sacrificed to it is exiled (finality).

**Citations**

- Scryfall ruling, *Victimize*: “You must choose two targets. You can't cast Victimize targeting only one creature card.”
- Scryfall ruling, *Victimize*: “The creature you sacrifice isn't chosen until Victimize resolves.”
- [CR 608.2b](#cr-6082b)

### brass-13: Gemcutter Buccaneer turns Treasures into Pirate equipment

**Status:** ✅ verified · **Cards:** Admiral Brass, Unsinkable, Gemcutter Buccaneer

**Ruling.** With Gemcutter Buccaneer, Treasures are also Equipment with 'Equipped creature gets +2/+0', and equip Pirate {1} is cheaper than equip {3}. Sacrificing an attached Treasure for mana removes the bonus. Each Pirate that enters makes a tapped Treasure, including Brass's reanimations.

**Citations**

- Oracle, *Gemcutter Buccaneer*: “Treasures you control are Equipment in addition to their other types and have "Equipped creature gets +2/+0," equip Pirate {1}, and equip {3}.”
- [CR 301.5](#cr-3015)

## Layers and continuous effects

### brass-06: Base 4/4 overwrites earlier P/T-setting effects; lords and counters still apply

**Status:** ✅ verified · **Cards:** Admiral Brass, Unsinkable, Admiral Beckett Brass, Corsair Captain, Skeleton Crew, Animate Dead

**Ruling.** Brass's base 4/4 is a layer 7b setting effect. It overwrites earlier setting effects but not modifications. Beckett's, Corsair Captain's and Skeleton Crew's +1/+1, +1/+1 counters, and Animate Dead's −1/−0 (on a different reanimation) apply in layer 7c on top.

**Citations**

- Scryfall ruling, *Admiral Brass, Unsinkable*: “Admiral Brass, Unsinkable's effect will overwrite any previous effects that set the returned creature's power and toughness to specific numbers.”
- [CR 613.4b](#cr-6134b), [CR 613.4c](#cr-6134c)

## Replacement and prevention effects

### brass-02: Finality counters mean exile, not death

**Status:** 🚩 list flag · **Cards:** Admiral Brass, Unsinkable, Pitiless Plunderer, Victimize, Living Death

**Ruling.** A creature with a finality counter that would go to the graveyard from the battlefield is exiled instead, so it never 'dies'.
- **Pitiless Plunderer** doesn't make a Treasure for it.
- **Victimize** sacrificing it exiles it.
- **Living Death** exiles such creatures as they're sacrificed, so they won't be available later. Living Death returns only the cards exiled by its first instruction.

Bounce or other zone changes work normally. Remove the counter with Power Conduit first to keep the creature recursive.

**List flag (anti-synergy).** Pitiless Plunderer, Victimize's sacrifice and the sacrifice outlets (Broadside Bombardiers' boast) lose value on Brass-returned creatures, which are exiled instead of dying. A minor non-bo, not a list error: remove the counter with Power Conduit first, or sacrifice other fodder.

**Citations**

- Oracle, *Pitiless Plunderer*: “Whenever another creature you control dies, create a Treasure token.”
- Scryfall ruling, *Admiral Brass, Unsinkable*: “Finality counters work on any permanent, not only creatures. If a permanent with a finality counter on it would be put into a graveyard from the battlefield, exile it instead.”
- Scryfall ruling, *Living Death*: “Only cards exiled by Living Death's first instruction are put onto the battlefield.”
- [CR 122.1h](#cr-1221h), [CR 700.4](#cr-7004), [CR 614.1a](#cr-6141a)

### brass-12: Angrath's Marauders doubles all your damage

**Status:** ✅ verified · **Cards:** Admiral Brass, Unsinkable, Angrath's Marauders, Broadside Bombardiers

**Ruling.** Angrath's Marauders doubles damage from any source you control to any permanent or player: combat damage, Broadside Bombardiers' boast, and so on. For trample you assign the unmodified damage first. Divided damage is divided before doubling.

**Citations**

- Oracle, *Angrath's Marauders*: “If a source you control would deal damage to a permanent or player, it deals double that damage to that permanent or player instead.”
- Scryfall ruling, *Angrath's Marauders*: “If a creature with trample you control would deal combat damage to a blocking creature while you control Angrath's Marauders, you must assign its unmodified damage.”
- [CR 614.1a](#cr-6141a)

## Zones, commander tax and the command zone

### brass-14: Commander tax and the graveyard plan

**Status:** ✅ verified · **Cards:** Admiral Brass, Unsinkable

**Ruling.** Brass costs {2}{U}{B}{R}, then 7, then 9. Each recast mills four more. The deck relies on its graveyard, so graveyard hate (exile effects, Rest in Peace-style pieces) stops both Brass's trigger and the reanimation spells. Brass's trigger targets, so a response that exiles the target card fizzles it.

**Citations**

- Oracle, *Admiral Brass, Unsinkable*: “When Admiral Brass enters, mill four cards.”
- [CR 903.8](#cr-9038), [CR 608.2b](#cr-6082b)

## What the list depends on

### brass-15: What the list depends on

**Status:** ✅ verified · **Cards:** Admiral Brass, Unsinkable, Buried Alive, Entomb, Reanimate, Animate Dead

**Ruling.** The deck depends on Pirate creature cards in the graveyard at beginning of combat and on Brass surviving to combat. Entomb (instant) and Buried Alive set up the turn before. Reanimate costs life equal to the card's mana value. Animate Dead's creature is sacrificed if the Aura leaves. No two-card combo (Spellbook lists none); the plan is recurring value and combat.

**Citations**

- Oracle, *Reanimate*: “You lose life equal to that card's mana value.”
- Oracle, *Animate Dead*: “When this Aura leaves the battlefield, that creature's controller sacrifices it.”
- [CR 603.4](#cr-6034)

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 101.4

If multiple players would make choices and/or take actions at the same time, the active player (the player whose turn it is) makes any choices required, then the next player in turn order (usually the player seated to the active player’s left) makes any choices required, followed by the remaining nonactive players in turn order. Then the actions happen simultaneously. This rule is often referred to as the “Active Player, Nonactive Player (APNAP) order” rule.

#### CR 113.6

Abilities of an instant or sorcery spell usually function only while that object is on the stack. Abilities of all other objects usually function only while that object is on the battlefield. The exceptions are as follows:

#### CR 115.1

Some spells and abilities require their controller to choose one or more targets for them. The targets are object(s) and/or player(s) the spell or ability will affect. These targets are declared as part of the process of putting the spell or ability on the stack. The targets can’t be changed except by another spell or ability that explicitly says it can do so.

#### CR 122.1h

One or more finality counters on a permanent create a single replacement effect that stops the permanent from going to the graveyard. That effect is “If this permanent would be put into a graveyard from the battlefield, exile it instead.”

#### CR 301.5

Some artifacts have the subtype “Equipment.” An Equipment can be attached to a creature. It can’t legally be attached to anything that isn’t a creature.

#### CR 602.2

To activate an ability is to put it onto the stack and pay its costs, so that it will eventually resolve and have its effect. Only an object’s controller (or its owner, if it doesn’t have a controller) can activate its activated ability unless the object specifically says otherwise. Activating an ability follows the steps listed below, in order. If, at any point during the activation of an ability, a player is unable to comply with any of those steps, the activation is illegal; the game returns to the moment before that ability started to be activated (see rule 733, “Handling Illegal …

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 603.4

A triggered ability may read “When/Whenever/At [trigger event], if [condition], [effect].” When the trigger event occurs, the ability checks whether the stated condition is true. The ability triggers only if it is; otherwise it does nothing. If the ability triggers, it checks the stated condition again as it resolves. If the condition isn’t true at that time, the ability is removed from the stack and does nothing. Note that this mirrors the check for legal targets. This rule is referred to as the “intervening ‘if’ clause” rule. (The word “if” has only its normal English meaning anywhere else …

#### CR 603.10a

Some zone-change triggers look back in time. These are leaves-the-battlefield abilities, abilities that trigger when a player sacrifices a permanent, abilities that trigger when a card leaves a graveyard, and abilities that trigger when an object that all players can see is put into a hand or library.

#### CR 608.2b

If the spell or ability specifies targets, it checks whether the targets are still legal. A target that’s no longer in the zone it was in when it was targeted is illegal. Other changes to the game state may cause a target to no longer be legal; for example, its characteristics may have changed or an effect may have changed the text of the spell. If the source of an ability has left the zone it was in, its last known information is used during this process. If all its targets, for every instance of the word “target,” are now illegal, the spell or ability doesn’t resolve. It’s removed from the …

#### CR 613.4b

Layer 7b: Effects that set power and/or toughness to a specific number or value are applied. Effects that refer to the base power and/or toughness of a creature apply in this layer.

#### CR 613.4c

Layer 7c: Effects and counters that modify power and/or toughness (but don’t set power and/or toughness to a specific number or value) are applied.

#### CR 614.1a

Effects that use the word “instead” are replacement effects. Most replacement effects use the word “instead” to indicate what events will be replaced with other events.

#### CR 700.4

The term dies means “is put into a graveyard from the battlefield.”

#### CR 700.11

Some cards refer to whether a player has “descended this turn.” This means that a permanent card has been put into that player’s graveyard from anywhere this turn. “The number of times [a player] descended this turn” means “the number of permanent cards put into [that player’s] graveyard from anywhere this turn.” In both cases, no permanent cards put into the player’s graveyard that turn are required to still be in that graveyard.

#### CR 702.73a

Changeling is a characteristic-defining ability. “Changeling” means “This object is every creature type.” This ability works everywhere, even outside the game. See rule 604.3.

#### CR 903.8

A player may cast a commander they own from the command zone. A commander cast from the command zone costs an additional {2} for each previous time the player casting it has cast it from the command zone that game. This additional cost is informally known as the “commander tax.”

