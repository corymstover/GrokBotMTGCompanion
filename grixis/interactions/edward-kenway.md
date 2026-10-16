---
title: "Edward Kenway — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Edward Kenway — Interaction Review

> Bot cycle 48 · batch B · reviewed 2026-10-16. Deck: [Edward Kenway](../decks/edward-kenway.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-15), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/edward-kenway.txt`](../../exports/grixis-archidekt/edward-kenway.txt) · SHA-256 `1e8b8ea5e52e2ea499f07f0d72cbc4305b81cfbf370a163d1378dacc01690b9b` |
| Rulings | **11** (10 verified · 0 uncertain · 1 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-15 · rulings 2026-10-15 |
| Source attestations | [`Edward_Kenway_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edward_kenway_2026-10-14/Edward_Kenway_Rules_Attestation.json) (11 interactions, all PASS) |

## Contents
- [Summary](#summary)
- [Flags and open questions](#flags-and-open-questions)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Key card-pair interactions](#key-card-pair-interactions)
- [Replacement and prevention effects](#replacement-and-prevention-effects)
- [Trigger ordering](#trigger-ordering)
- [What the list depends on](#what-the-list-depends-on)
- [Rules cited](#rules-cited)

## Summary

Edward Kenway makes a Treasure at your end step for each tapped Assassin, Pirate or Vehicle, and Vehicles that connect exile cards for you to play. This review re-verifies the eleven items of the deck's rules attestation, and confirms its five Time Sieve and Malcolm combo lines against cached Commander Spellbook steps.

Rules surprise: with Academy Manufactor out, Fateful Discovery's mandatory draws can deck you during a Time Sieve extra-turn lock (dependency-risk flag, no list change).

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [edward-08](#edward-08-fateful-discoverys-mandatory-draws-can-deck-you-during-an-extra-turn-lock) | 🚩 list flag (dependency-risk) | Fateful Discovery's mandatory draws can deck you during an extra-turn lock | Pilot note, not a list error: with Academy Manufactor and Fateful Discovery both out, the Time Sieve lock needs a kill within a few turns, or Fateful Discovery should be removed from the plan. Spellbook labels the Time Sieve lines 'Lock', not a win. |

## Commander rules text and edge cases

### edward-01: Each tapped permanent counts once

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Edward Kenway

**Ruling.** Edward's end-step trigger counts tapped permanents you control that are Assassins, Pirates and/or Vehicles. A permanent with several of those types (Edward himself is an Assassin Pirate) still makes one Treasure. The count is taken when the trigger resolves, so whatever is still tapped then counts. Attackers without vigilance stay tapped until your next untap step.

**Citations**

- Oracle, *Edward Kenway*: “At the beginning of your end step, create a Treasure token for each tapped Assassin, Pirate, and/or Vehicle you control.”
- Scryfall ruling, *Edward Kenway*: “If a tapped permanent you control has more than one of the subtypes listed in Edward’s first ability, count it only once when determining how many Treasure tokens to create.”
- [CR 608.2h](#cr-6082h), [CR 205.3m](#cr-2053m)
- Source (re-verified): [`Edward_Kenway_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edward_kenway_2026-10-14/Edward_Kenway_Rules_Attestation.json) → “Edward subtype count-once rule”

### edward-02: Vehicle damage exiles a card you may play, lands included

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Edward Kenway, Ramirez DePietro, Pillager

**Ruling.** Each Vehicle that deals combat damage to a player triggers Edward separately. The exiled card can be played, so a land can be your land drop for the turn, at normal timing. Ramirez DePietro only lets you cast the card, so lands exiled with Ramirez can't be played. Cards exiled by Edward stay exiled face down if you leave the game.

**Citations**

- Oracle, *Edward Kenway*: “Whenever a Vehicle you control deals combat damage to a player, look at the top card of that player's library, then exile it face down. You may play that card for as long as it remains exiled.”
- Oracle, *Ramirez DePietro, Pillager*: “You may cast that card for as long as it remains exiled.”
- Scryfall ruling, *Ramirez DePietro, Pillager*: “You may not play lands exiled with the last ability.”
- Scryfall ruling, *Edward Kenway*: “If you leave the game, the cards remain exiled face down indefinitely. No player may look at them.”
- [CR 305.2](#cr-3052), [CR 305.3](#cr-3053), [CR 406.3](#cr-4063)
- Source (re-verified): [`Edward_Kenway_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edward_kenway_2026-10-14/Edward_Kenway_Rules_Attestation.json) → “Edward Vehicle damage play permission”
- Source (re-verified): [`Edward_Kenway_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edward_kenway_2026-10-14/Edward_Kenway_Rules_Attestation.json) → “Ramirez versus Edward exile permissions”

## Combos and engine lines

### edward-03: Edward + Time Sieve: five tapped permanents = an extra turn

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Edward Kenway, Time Sieve

**Ruling.** Tap at least five Assassins, Pirates and/or Vehicles (attacking is the usual way). Edward's end-step trigger makes at least five Treasures. Sacrifice them to Time Sieve during that end step for an extra turn, and repeat each turn. Time Sieve can be one of the five artifacts it sacrifices, but then it's gone.

**Citations**

- Oracle, *Edward Kenway*: “At the beginning of your end step, create a Treasure token for each tapped Assassin, Pirate, and/or Vehicle you control.”
- Oracle, *Time Sieve*: “{T}, Sacrifice five artifacts: Take an extra turn after this one.”
- Scryfall ruling, *Time Sieve*: “You may sacrifice Time Sieve as one of the artifacts to pay the cost of its own ability.”
- [CR 500.7](#cr-5007), [CR 602.2](#cr-6022)
- Commander Spellbook [1558-5736](https://commanderspellbook.com/combo/1558-5736/) (community-maintained, retrieved 2026-10-16): “At the beginning of your end step, Edward Kenway's first ability triggers, creating at least five Treasure tokens.”
- Commander Spellbook [1558-5736](https://commanderspellbook.com/combo/1558-5736/) (community-maintained, retrieved 2026-10-16): “Activate Time Sieve by tapping it and sacrificing five Treasures, causing you to take an extra turn after this one.”
- Source (re-verified): [`Edward_Kenway_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edward_kenway_2026-10-14/Edward_Kenway_Rules_Attestation.json) → “Luxurious Locomotive plus Time Sieve”

### edward-04: Luxurious Locomotive: over-crew with five creatures

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Edward Kenway, Luxurious Locomotive, Time Sieve

**Ruling.** Crew lets you tap more creatures than needed. Crew Luxurious Locomotive (crew 1, once per turn) with five creatures. When it attacks, it makes a Treasure for each creature that crewed it, including ones no longer on the battlefield. Five Treasures pay Time Sieve. The crewing Pirates and Assassins and the attacking Locomotive are tapped, so Edward also counts them at end step.

**Citations**

- Oracle, *Luxurious Locomotive*: “Whenever this Vehicle attacks, create a Treasure token for each creature that crewed it this turn.”
- Scryfall ruling, *Luxurious Locomotive*: “You may tap more creatures than necessary to activate a crew ability.”
- Scryfall ruling, *Luxurious Locomotive*: “Luxurious Locomotive's triggered ability counts each creature that crewed it this turn, including creatures that are no longer on the battlefield as the ability resolves.”
- [CR 702.122a](#cr-702122a), [CR 702.122c](#cr-702122c)
- Commander Spellbook [1558-6307](https://commanderspellbook.com/combo/1558-6307/) (community-maintained, retrieved 2026-10-16): “Activate Luxurious Locomotive's crew ability by tapping five creatures you control with total power 1 or greater, causing Luxurious Locomotive to become an artifact creature until end of turn.”
- Source (re-verified): [`Edward_Kenway_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edward_kenway_2026-10-14/Edward_Kenway_Rules_Attestation.json) → “Luxurious Locomotive over-crewing with Edward”
- Source (re-verified): [`Edward_Kenway_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edward_kenway_2026-10-14/Edward_Kenway_Rules_Attestation.json) → “Luxurious Locomotive plus Time Sieve”

### edward-05: The Reaver Cleaver and Hoard Hauler extra-turn lines

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Edward Kenway, The Reaver Cleaver, Hoard Hauler, Time Sieve

**Ruling.** The Reaver Cleaver on a creature with power 4+ (Cleaver adds +1/+1 and trample) makes that many Treasures when it deals combat damage to a player: five or more pays Time Sieve. Hoard Hauler (crew 3) makes a Treasure for each artifact the damaged player controls, so it only works against an opponent with five or more artifacts. Hoard Hauler is a Vehicle, so its damage also triggers Edward's exile.

**Citations**

- Oracle, *The Reaver Cleaver*: “Whenever this creature deals combat damage to a player or planeswalker, create that many Treasure tokens.”
- Oracle, *Hoard Hauler*: “Whenever this Vehicle deals combat damage to a player, create a Treasure token for each artifact they control.”
- [CR 510.2](#cr-5102), [CR 702.19b](#cr-70219b)
- Commander Spellbook [1558-5039](https://commanderspellbook.com/combo/1558-5039/) (community-maintained, retrieved 2026-10-16): “The creature triggers, creating at least five Treasure tokens.”
- Commander Spellbook [451-1558](https://commanderspellbook.com/combo/451-1558/) (community-maintained, retrieved 2026-10-16): “Deal combat damage to an opponent who controls five or more artifacts using Hoard Hauler.”
- Source (re-verified): [`Edward_Kenway_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edward_kenway_2026-10-14/Edward_Kenway_Rules_Attestation.json) → “Reaver Cleaver plus Time Sieve retained line”

### edward-06: Malcolm + Glint-Horn Buccaneer

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Edward Kenway, Malcolm, Keen-Eyed Navigator, Glint-Horn Buccaneer

**Ruling.** Glint-Horn is a Pirate. While it's attacking, pay {1}{R} and discard: its discard trigger deals 1 to each opponent. Malcolm counts any damage from Pirates, not just combat damage, so it makes one Treasure per opponent dealt damage. Two Treasures pay the next activation, and Glint-Horn draws you a replacement card. With two or more opponents it repeats until they die or you run out of cards.

**Citations**

- Oracle, *Glint-Horn Buccaneer*: “{1}{R}, Discard a card: Draw a card. Activate only if this creature is attacking.”
- Scryfall ruling, *Malcolm, Keen-Eyed Navigator*: “Malcolm's triggered ability considers all damage dealt by Pirates you control to opponents, not just combat damage.”
- [CR 120.3](#cr-1203), [CR 603.2](#cr-6032)
- Commander Spellbook [4508-4869](https://commanderspellbook.com/combo/4508-4869/) (community-maintained, retrieved 2026-10-16): “Malcolm triggers, creating a Treasure token for each opponent dealt damage this way.”
- Commander Spellbook [4508-4869](https://commanderspellbook.com/combo/4508-4869/) (community-maintained, retrieved 2026-10-16): “Activate two Treasures by tapping and sacrificing them, adding {1}{R}.”
- Source (re-verified): [`Edward_Kenway_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edward_kenway_2026-10-14/Edward_Kenway_Rules_Attestation.json) → “Malcolm plus Glint-Horn Buccaneer”

## Key card-pair interactions

### edward-11: Ramirez and Don Andres

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Edward Kenway, Ramirez DePietro, Pillager, Don Andres, the Renegade

**Ruling.** A noncreature spell cast from Ramirez's exile is a spell you don't own, so Don Andres makes two tapped Treasures. Stolen creature spells don't trigger Don, but once on the battlefield they're +2/+2 menace deathtouch Pirates under him. That also makes them count for Edward's end-step Treasures when tapped.

**Citations**

- Oracle, *Don Andres, the Renegade*: “Whenever you cast a noncreature spell you don't own, create two tapped Treasure tokens.”
- [CR 108.3](#cr-1083)
- Source (re-verified): [`Edward_Kenway_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edward_kenway_2026-10-14/Edward_Kenway_Rules_Attestation.json) → “Ramirez and Don Andres”

## Replacement and prevention effects

### edward-07: Academy Manufactor triples Treasure output

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Edward Kenway, Academy Manufactor, Malcolm, Keen-Eyed Navigator, Time Sieve

**Ruling.** With one Manufactor, every Treasure you would create becomes a Clue, a Food and a Treasure. All are artifacts, so Time Sieve can sacrifice any of them. Two Manufactors make three of each. Spellbook's line: two Pirates connecting with two opponents make two of each token through Malcolm, more than the five artifacts Time Sieve needs.

**Citations**

- Oracle, *Academy Manufactor*: “If you would create a Clue, Food, or Treasure token, instead create one of each.”
- Scryfall ruling, *Academy Manufactor*: “If you control one Academy Manufactor and would create some number of Clue, Food, or Treasure tokens, you will instead create that many Clue tokens, that many Food tokens, and that many Treasure tokens.”
- [CR 614.1a](#cr-6141a), [CR 111.10](#cr-11110)
- Commander Spellbook [1558-4231-4508](https://commanderspellbook.com/combo/1558-4231-4508/) (community-maintained, retrieved 2026-10-16): “Malcolm triggers, creating at least two Treasure, Food and Clue tokens.”
- Source (re-verified): [`Edward_Kenway_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edward_kenway_2026-10-14/Edward_Kenway_Rules_Attestation.json) → “Academy Manufactor and Fateful Discovery”

## Trigger ordering

### edward-09: RMS Titanic: the Edward trigger survives Titanic's sacrifice

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Edward Kenway, RMS Titanic

**Ruling.** When Titanic deals combat damage to a player, its own trigger (sacrifice it, make that many Treasures) and Edward's exile trigger both fire. Edward's trigger resolves independently of Titanic. Titanic is gone by the end step, so Edward doesn't count it.

**Citations**

- Oracle, *RMS Titanic*: “When RMS Titanic deals combat damage to a player, sacrifice it and create that many Treasure tokens.”
- Oracle, *Edward Kenway*: “Whenever a Vehicle you control deals combat damage to a player, look at the top card of that player's library, then exile it face down. You may play that card for as long as it remains exiled.”
- [CR 113.7a](#cr-1137a), [CR 603.3b](#cr-6033b)
- Source (re-verified): [`Edward_Kenway_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edward_kenway_2026-10-14/Edward_Kenway_Rules_Attestation.json) → “RMS Titanic timing with Edward”

### edward-10: Roaming Throne on Assassin or Pirate

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Edward Kenway, Roaming Throne

**Ruling.** Edward is an Assassin and a Pirate, so Roaming Throne naming either type doubles both of his triggers. Each end-step instance counts the tapped permanents again: twice the Treasures. Roaming Throne itself is the chosen type; if it's tapped at end step, Edward counts it too.

**Citations**

- Oracle, *Roaming Throne*: “This creature is the chosen type in addition to its other types.”
- Scryfall ruling, *Roaming Throne*: “Roaming Throne's last ability doesn't copy the triggered ability; it just causes the ability to trigger an additional time.”
- [CR 603.2](#cr-6032)
- Source (re-verified): [`Edward_Kenway_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edward_kenway_2026-10-14/Edward_Kenway_Rules_Attestation.json) → “Roaming Throne with Edward”

## What the list depends on

### edward-08: Fateful Discovery's mandatory draws can deck you during an extra-turn lock

**Status:** 🚩 list flag · **Evidence:** fact · **Cards:** Edward Kenway, Fateful Discovery, Academy Manufactor, Time Sieve

**Ruling.** Fateful Discovery draws a card whenever an artifact you control enters, and the draw isn't optional. With Academy Manufactor, an end step with five tapped permanents makes 15 artifacts and draws 15 cards. Over a few Time Sieve extra turns you'll draw your library out. Drawing from an empty library loses at the next state-based check. The source attestation treats this as pure upside.

**List flag (dependency-risk).** Pilot note, not a list error: with Academy Manufactor and Fateful Discovery both out, the Time Sieve lock needs a kill within a few turns, or Fateful Discovery should be removed from the plan. Spellbook labels the Time Sieve lines 'Lock', not a win.

**Citations**

- Oracle, *Fateful Discovery*: “Whenever an artifact you control enters, draw a card.”
- [CR 704.5b](#cr-7045b), [CR 121.4](#cr-1214)
- Source (re-verified): [`Edward_Kenway_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edward_kenway_2026-10-14/Edward_Kenway_Rules_Attestation.json) → “Academy Manufactor and Fateful Discovery”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 108.3

The owner of a card in the game is the player who started the game with it in their deck. If a card is brought into the game from outside the game rather than starting in a player’s deck, its owner is the player who brought it into the game. If a card starts the game in the command zone, its owner is the player who put it into the command zone to start the game. Legal ownership of a card in the game is irrelevant to the game rules except for the rules for ante. (See rule 407.)

#### CR 111.10

Some effects instruct a player to create a predefined token. These effects use the definition below to determine the characteristics the token is created with. The effect that creates a predefined token may also modify or add to the predefined characteristics.

#### CR 113.7a

Once activated or triggered, an ability exists on the stack independently of its source. Destruction or removal of the source after that time won’t affect the ability. Note that some abilities cause a source to do something (for example, “This creature deals 1 damage to any target”) rather than the ability doing anything directly. In these cases, any activated or triggered ability that references information about the source for use while announcing an activated ability or putting a triggered ability on the stack checks that information when the ability is put onto the stack. Otherwise, it …

#### CR 120.3

Damage may have one or more of the following results, depending on whether the recipient of the damage is a player or permanent, the characteristics of the damage’s source, and the characteristics of the damage’s recipient (if it’s a permanent).

#### CR 121.4

A player who attempts to draw a card from a library with no cards in it loses the game the next time a player would receive priority. (This is a state-based action. See rule 704.)

#### CR 205.3m

Creatures and kindreds share their lists of subtypes; these subtypes are called creature types. One creature type is two words long: Time Lord. All other creature types are one word long: Advisor, Aetherborn, Alien, Ally, Angel, Antelope, Ape, Archer, Archon, Armadillo, Army, Artificer, Assassin, Assembly-Worker, Astartes, Atog, Aurochs, Avatar, Azra, Badger, Balloon, Barbarian, Bard, Basilisk, Bat, Bear, Beast, Beaver, Beeble, Beholder, Berserker, Bird, Bison, Blinkmoth, Boar, Bringer, Brushwagg, Camarid, Camel, Capybara, Caribou, Carrier, Cat, Centaur, Child, Chimera, Citizen, Cleric, …

#### CR 305.2

A player can normally play one land during their turn; however, continuous effects may increase this number.

#### CR 305.3

A player can’t play a land, for any reason, if it isn’t their turn. Ignore any part of an effect that instructs a player to do so.

#### CR 406.3

Exiled cards are, by default, kept face up and may be examined by any player at any time. Cards “exiled face down” can’t be examined by any player except when instructions allow it. However, if a player is instructed to look at a card and then exile it face down, or once a player is allowed to look at a card exiled face down, that player may continue to look at that card until it leaves the exile zone or is part of a pile of cards that are shuffled, even if the instruction allowing the player to do so no longer applies.

#### CR 500.7

Some effects can give a player extra turns. They do this by adding the turns directly after the specified turn. If a player is given multiple extra turns, the extra turns are added one at a time. If multiple players are given extra turns, the extra turns are added one at a time, in APNAP order (see rule 101.4). The most recently created turn will be taken first.

#### CR 510.2

Second, all combat damage that’s been assigned is dealt simultaneously. This turn-based action doesn’t use the stack. No player has the chance to cast spells or activate abilities between the time combat damage is assigned and the time it’s dealt.

#### CR 602.2

To activate an ability is to put it onto the stack and pay its costs, so that it will eventually resolve and have its effect. Only an object’s controller (or its owner, if it doesn’t have a controller) can activate its activated ability unless the object specifically says otherwise. Activating an ability follows the steps listed below, in order. If, at any point during the activation of an ability, a player is unable to comply with any of those steps, the activation is illegal; the game returns to the moment before that ability started to be activated (see rule 733, “Handling Illegal …

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 603.3b

If multiple abilities have triggered since the last time a player received priority, the abilities are placed on the stack in a two-part process. First, each player, in APNAP order, puts each triggered ability they control with a trigger condition that isn’t another ability triggering on the stack in any order they choose. (See rule 101.4.) Second, each player, in APNAP order, puts all remaining triggered abilities they control on the stack in any order they choose. Then the game once again checks for and performs state-based actions until none are performed, then abilities that triggered …

#### CR 608.2h

If an effect requires information from the game (such as the number of creatures on the battlefield), the answer is determined only once, when the effect is applied. If the effect requires information from a specific object, including the source of the ability itself, the effect uses the current information of that object if it’s in the public zone it was expected to be in; if it’s no longer in that zone, or if the effect has moved it from a public zone to a hidden zone, the effect uses the object’s last known information. See rule 113.7a. If an ability states that an object does something, …

#### CR 614.1a

Effects that use the word “instead” are replacement effects. Most replacement effects use the word “instead” to indicate what events will be replaced with other events.

#### CR 702.19b

The controller of an attacking creature with trample first assigns damage to the creature(s) blocking it. Once all those blocking creatures are assigned lethal damage, any excess damage is assigned as its controller chooses among those blocking creatures and the player, planeswalker, or battle the creature is attacking. When checking for assigned lethal damage, take into account damage already marked on the creature and damage from other creatures that’s being assigned during the same combat damage step, but not any abilities or effects that might change the amount of damage that’s actually …

#### CR 702.122a

Crew is an activated ability of Vehicle cards. “Crew N” means “Tap any number of other untapped creatures you control with total power N or greater: This permanent becomes an artifact creature until end of turn.”

#### CR 702.122c

A Vehicle is “crewed by” a creature if that creature was tapped to pay the cost to activate that Vehicle’s crew ability.

#### CR 704.5b

If a player attempted to draw a card from a library with no cards in it since the last time state-based actions were checked, that player loses the game.

