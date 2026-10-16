---
title: "Admiral Beckett Brass — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Admiral Beckett Brass — Interaction Review

> Bot cycle 46 · batch A · reviewed 2026-10-16. Deck: [Admiral Beckett Brass](../decks/admiral-beckett-brass.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-15), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Current list | [`exports/grixis-archidekt/admiral-beckett-brass.txt`](../../exports/grixis-archidekt/admiral-beckett-brass.txt) · SHA-256 `dbc2ce511a88eb94d70357edbf0088cf26110c3052bd2230eeb6a583b4437808` |
| Rulings | **17** (16 verified · 0 uncertain · 1 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-15 · rulings 2026-10-15 |
| Source attestations | [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) (deck #2: RULES PASS) |

## Contents
- [Summary](#summary)
- [Flags and open questions](#flags-and-open-questions)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [Key card-pair interactions](#key-card-pair-interactions)
- [Layers and continuous effects](#layers-and-continuous-effects)
- [Trigger ordering](#trigger-ordering)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [What the list depends on](#what-the-list-depends-on)
- [Rules cited](#rules-cited)

## Summary

Beckett is a Pirate lord that steals one nonland permanent per end step from a player hit by three different Pirates. This review re-verifies the retrospective attestation (Roaming Throne doubling, Open into Wonder, turn-history condition). It adds the type-changing steal package (Don Andres, Coercive Recruiter, Zara, Hostage Taker), the changelings, the one-sided sweepers and Double Down's legend-rule interaction. Flag: Kari Zev's Ragavan token is a Monkey, not a Pirate, so it never counts toward the three. No combos: the deck is a value and control engine.

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [beckett-03](#beckett-03-kari-zevs-ragavan-token-is-a-monkey-not-a-pirate) | 🚩 list flag (documentation) | Kari Zev's Ragavan token is a Monkey, not a Pirate | Easy miscount: the Ragavan token never counts as one of Beckett's three Pirates. Count Kari Zev herself, not her token. |

## Commander rules text and edge cases

### beckett-01: Three different Pirates, same player, combat damage, this turn

**Status:** ✅ verified · **Cards:** Admiral Beckett Brass

**Ruling.** The end-step trigger targets a nonland permanent controlled by a player who was dealt combat damage by three or more *different* Pirates this turn. A double striker counts once. Damage over several combat phases (Port Razer) adds up. The condition is turn history: the Pirates needn't still be on the battlefield or still be Pirates, and Beckett needn't have been out when they connected. If no player qualifies, there is no legal target and the trigger does nothing. The theft lasts indefinitely, even after Beckett leaves.

**Citations**

- Oracle, *Admiral Beckett Brass*: “At the beginning of your end step, gain control of target nonland permanent controlled by a player who was dealt combat damage by three or more Pirates this turn.”
- Scryfall ruling, *Admiral Beckett Brass*: “If one Pirate deals combat damage multiple times, most likely because it has double strike, it counts as only one of the three Pirates for Admiral Beckett Brass's triggered ability.”
- Scryfall ruling, *Admiral Beckett Brass*: “It doesn't care whether Admiral Beckett Brass was on the battlefield when those Pirates dealt combat damage, whether those creatures are still on the battlefield, or whether they're still Pirates.”
- Scryfall ruling, *Admiral Beckett Brass*: “The control-change effect of Admiral Beckett Brass's triggered ability lasts indefinitely.”
- [CR 603.3d](#cr-6033d), [CR 115.1](#cr-1151), [CR 613.1b](#cr-6131b)
- Source (re-verified): [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) → “the permanents need not still be on the battlefield at the end step for the turn-history condition to have happened.”

### beckett-02: One target, even if several players qualify

**Status:** ✅ verified · **Cards:** Admiral Beckett Brass, Roaming Throne

**Ruling.** If two players were each hit by three Pirates, Beckett still takes one permanent from either of them. With Roaming Throne naming Pirate, Beckett is 'another creature of the chosen type', so his trigger triggers an additional time. Each instance picks its own target, so you can take two permanents, from one player or from two.

**Citations**

- Oracle, *Roaming Throne*: “If a triggered ability of another creature you control of the chosen type triggers, it triggers an additional time.”
- Scryfall ruling, *Admiral Beckett Brass*: “If more than one player was dealt combat damage by three Pirates, you target only one permanent.”
- Scryfall ruling, *Roaming Throne*: “Any choices made as you put the ability onto the stack, such as modes and targets, are made separately for each instance of the ability.”
- [CR 603.2](#cr-6032)
- Source (re-verified): [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) → “`Roaming Throne` choosing Pirate causes a triggered ability of another Pirate creature you control to trigger an additional time”

## Combos and engine lines

### beckett-09: Roaming Throne naming Pirate doubles the deck's Pirate triggers

**Status:** ✅ verified · **Cards:** Admiral Beckett Brass, Roaming Throne, Admiral Brass, Unsinkable, Breeches, Eager Pillager, Coercive Recruiter, Merchant Raiders, Forerunner of the Coalition

**Ruling.** Roaming Throne (choose Pirate, so it's a Pirate too) makes triggered abilities of your *other* Pirate creatures trigger an additional time. That doubles Beckett's end step, Admiral Brass's combat reanimation and Coercive Recruiter's steal. Merchant Raiders taps a second target, and Forerunner's life loss doubles. Breeches, Eager Pillager triggers twice per attacking Pirate, but there are only three modes per turn, so the extra trigger may have no mode left to choose. Only abilities of creatures are doubled, so Double Down and Kindred Discovery aren't.

**Citations**

- Oracle, *Roaming Throne*: “This creature is the chosen type in addition to its other types.”
- Scryfall ruling, *Roaming Throne*: “Roaming Throne's last ability doesn't copy the triggered ability; it just causes the ability to trigger an additional time.”
- [CR 603.2](#cr-6032)

## Engines and payoffs

### beckett-10: Port Razer extra combats and Beckett's tally

**Status:** ✅ verified · **Cards:** Admiral Beckett Brass, Port Razer

**Ruling.** Port Razer connecting untaps all your creatures and adds a combat phase after the current one. Pirates that dealt damage in the first combat still count for Beckett. A second combat lets different Pirates hit the same player and complete the three. Port Razer itself can't attack a player it already attacked this turn, and it never has to attack.

**Citations**

- Oracle, *Port Razer*: “After this phase, there is an additional combat phase.”
- Scryfall ruling, *Port Razer*: “Port Razer doesn't have to attack in any additional combat it creates (or any other time for that matter).”
- [CR 500.8](#cr-5008), [CR 506.1](#cr-5061)

## Key card-pair interactions

### beckett-03: Kari Zev's Ragavan token is a Monkey, not a Pirate

**Status:** 🚩 list flag · **Cards:** Admiral Beckett Brass, Kari Zev, Skyship Raider, Ragavan, Nimble Pilferer

**Ruling.** Kari Zev's token is 'Ragavan, a legendary 2/1 red Monkey'. It isn't a Pirate, so it doesn't count toward Beckett's three and doesn't get his +1/+1. It enters attacking but was never declared as an attacker, so attack triggers don't see it. The card Ragavan, Nimble Pilferer (Monkey Pirate) has a different name, so the two can coexist under the legend rule.

**List flag (documentation).** Easy miscount: the Ragavan token never counts as one of Beckett's three Pirates. Count Kari Zev herself, not her token.

**Citations**

- Oracle, *Kari Zev, Skyship Raider*: “create Ragavan, a legendary 2/1 red Monkey creature token”
- Scryfall ruling, *Kari Zev, Skyship Raider*: “Although Ragavan is attacking, it was never declared as an attacking creature”
- [CR 704.5j](#cr-7045j), [CR 508.4](#cr-5084), [CR 111.4](#cr-1114)

### beckett-04: Don Andres and Coercive Recruiter turn stolen creatures into Pirates

**Status:** ✅ verified · **Cards:** Admiral Beckett Brass, Don Andres, the Renegade, Coercive Recruiter, Zara, Renegade Recruiter, Hostage Taker

**Ruling.** Don Andres makes each creature you control but don't own a Pirate, with +2/+2, menace and deathtouch. That covers Hostage Taker casts, Zara's hand-stolen attacker and Coercive Recruiter steals. Coercive Recruiter also makes its own target a Pirate with haste until end of turn. These creatures count toward Beckett's three when they deal combat damage. Tokens you create are owned by you, so Don Andres doesn't affect them.

**Citations**

- Oracle, *Don Andres, the Renegade*: “Each creature you control but don't own gets +2/+2, has menace and deathtouch, and is a Pirate in addition to its other types.”
- Oracle, *Coercive Recruiter*: “Until end of turn, it gains haste and becomes a Pirate in addition to its other types.”
- Scryfall ruling, *Don Andres, the Renegade*: “The player who creates a token is its owner.”
- [CR 613.1b](#cr-6131b), [CR 613.1d](#cr-6131d), [CR 108.3](#cr-1083), [CR 111.2](#cr-1112)

### beckett-05: Zara's stolen attacker counts but skips attack triggers

**Status:** ✅ verified · **Cards:** Admiral Beckett Brass, Zara, Renegade Recruiter, Don Andres, the Renegade

**Ruling.** Zara puts a creature from the defending player's hand onto the battlefield tapped and attacking. It wasn't declared as an attacker, so Breeches, Dire Fleet Captain and Fathom Fleet Captain don't trigger for it. With Don Andres out it's a Pirate and counts for Beckett if it connects. It returns to its owner's hand at the next end step, but Beckett's history check doesn't care.

**Citations**

- Oracle, *Zara, Renegade Recruiter*: “You may put a creature card from it onto the battlefield under your control tapped and attacking that player or a planeswalker they control.”
- Scryfall ruling, *Zara, Renegade Recruiter*: “Although the creature is attacking, it was never declared as an attacking creature.”
- [CR 508.4](#cr-5084)

### beckett-06: Changelings count as Pirates

**Status:** ✅ verified · **Cards:** Admiral Beckett Brass, Changeling Outcast, Black Market Connections

**Ruling.** Changeling makes an object every creature type in every zone. Changeling Outcast (can't block, can't be blocked) and the Shapeshifter token from Black Market Connections' 'Hire a Mercenary' mode are Pirates. They get Beckett's +1/+1 and count toward his three. They survive Fiery Cannonade and Raise the Palisade (choosing Pirate).

**Citations**

- Oracle, *Changeling Outcast*: “This creature can't block and can't be blocked.”
- Oracle, *Black Market Connections*: “Create a 3/2 colorless Shapeshifter creature token with changeling.”
- [CR 702.73a](#cr-70273a), [CR 604.3](#cr-6043)

### beckett-07: One-sided sweepers: Fiery Cannonade and Raise the Palisade

**Status:** ✅ verified · **Cards:** Admiral Beckett Brass, Fiery Cannonade, Raise the Palisade, Roaming Throne, Kari Zev, Skyship Raider

**Ruling.** Fiery Cannonade deals 2 to each non-Pirate creature. Raise the Palisade naming Pirate bounces every non-Pirate. Your survivors are your Pirates, changelings, a Roaming Throne that named Pirate, and stolen creatures made Pirates by Don Andres or Coercive Recruiter. Kari Zev's Monkey token is hit by both. Beckett's +1/+1 doesn't protect a 1-toughness non-Pirate.

**Citations**

- Oracle, *Fiery Cannonade*: “Fiery Cannonade deals 2 damage to each non-Pirate creature.”
- Oracle, *Raise the Palisade*: “Return all creatures that aren't of the chosen type to their owners' hands.”
- [CR 205.3m](#cr-2053m)

### beckett-08: Double Down copies Pirate spells; legendary copies hit the legend rule

**Status:** ✅ verified · **Cards:** Admiral Beckett Brass, Double Down, Ramirez DePietro, Pillager, Hostage Taker, Coercive Recruiter

**Ruling.** Double Down copies each outlaw spell you cast, and Pirates are outlaws. The copy resolves first and becomes a token. For nonlegendary Pirates that's a second body with its own enter-the-battlefield trigger: a second Hostage Taker exile, or a Coercive Recruiter steal. For legendary Pirates (Ramirez, Breeches, Kari Zev, Malcolm, Zara, Edward Kenway, Admiral Brass, Beckett himself), the original then resolves and the legend rule makes you keep one. Both enter-the-battlefield triggers still happen; Ramirez makes 4 Treasures and you lose 4 life. A copy isn't cast, so it doesn't count for cast triggers. Double Down doesn't trigger on Pirates put onto the battlefield without being cast.

**Citations**

- Oracle, *Double Down*: “Whenever you cast an outlaw spell, copy that spell.”
- Scryfall ruling, *Double Down*: “Double Down's ability and the copy it creates will resolve before the spell that caused it to trigger.”
- Scryfall ruling, *Double Down*: “Double Down's ability doesn't trigger if an outlaw permanent is put onto the battlefield without being cast.”
- [CR 707.10](#cr-70710), [CR 608.3f](#cr-6083f), [CR 704.5j](#cr-7045j)

### beckett-11: Open into Wonder and evasion only enable; damage must happen

**Status:** ✅ verified · **Cards:** Admiral Beckett Brass, Open into Wonder, Cover of Darkness, Storm Fleet Sprinter

**Ruling.** Open into Wonder (X creatures can't be blocked) and Cover of Darkness (choose Pirate: fear) get Pirates through, but Beckett still needs actual combat damage. Prevention or a creature removed before damage means it doesn't count.

**Citations**

- Oracle, *Open into Wonder*: “X target creatures can't be blocked this turn.”
- [CR 510.2](#cr-5102), [CR 120.3a](#cr-1203a)
- Source (re-verified): [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) → “the resulting Beckett condition still depends on actual combat damage.”

### beckett-12: The Indomitable is cast from the graveyard with tapped Pirates

**Status:** ✅ verified · **Cards:** Admiral Beckett Brass, The Indomitable

**Ruling.** The Indomitable can be cast from your graveyard while you control three or more tapped Pirates and/or Vehicles. That is checked only as you begin casting, so post-combat after a three-Pirate attack is the natural window. You still pay its cost. It needs crew 3 to attack. Its combat-damage draw triggers for any creature you control, not only Vehicles.

**Citations**

- Oracle, *The Indomitable*: “You may cast this card from your graveyard as long as you control three or more tapped Pirates and/or Vehicles.”
- Scryfall ruling, *The Indomitable*: “The Indomitable checks if you control three or more tapped Pirates and/or Vehicles only as you begin to cast it.”
- [CR 601.2](#cr-6012)

## Layers and continuous effects

### beckett-14: Beckett's anthem, Admiral Brass's base 4/4 and the lords

**Status:** ✅ verified · **Cards:** Admiral Beckett Brass, Admiral Brass, Unsinkable, Corsair Captain

**Ruling.** Admiral Brass sets a reanimated Pirate's base power and toughness to 4/4 (layer 7b). Beckett's and Corsair Captain's +1/+1 apply afterwards (layer 7c), so the creature is 6/6 with both lords. Counters also apply on top. The finality counter exiles it if it would die.

**Citations**

- Oracle, *Admiral Beckett Brass*: “Other Pirates you control get +1/+1.”
- Oracle, *Admiral Brass, Unsinkable*: “It has base power and toughness 4/4.”
- Scryfall ruling, *Admiral Brass, Unsinkable*: “Effects that otherwise modify the returned creature's power and toughness will still apply no matter when they took effect.”
- [CR 613.4b](#cr-6134b), [CR 613.4c](#cr-6134c)

## Trigger ordering

### beckett-17: Breeches, Eager Pillager's extra triggers run out of modes

**Status:** ✅ verified · **Cards:** Admiral Beckett Brass, Breeches, Eager Pillager, Roaming Throne

**Ruling.** Each Breeches trigger must choose a mode not yet chosen that turn. Once all three are used, a further trigger (from Roaming Throne or a fourth attacking Pirate) has no legal mode and is removed from the stack with no effect. The modes are chosen as the trigger goes on the stack.

**Citations**

- Oracle, *Breeches, Eager Pillager*: “Whenever a Pirate you control attacks, choose one that hasn't been chosen this turn —”
- Scryfall ruling, *Breeches, Eager Pillager*: “If you can't legally choose a mode because all three have been chosen that turn, that instance of the ability is removed from the stack with no effect.”
- [CR 603.3c](#cr-6033c), [CR 700.2](#cr-7002)

### beckett-13: End-step pile-up: Beckett, Edward Kenway, Daring Piracy, Zara, dash

**Status:** ✅ verified · **Cards:** Admiral Beckett Brass, Edward Kenway, Daring Piracy, Zara, Renegade Recruiter, Ragavan, Nimble Pilferer

**Ruling.** At the beginning of your end step all of these trigger, and you choose the order:
- Beckett's steal;
- Edward Kenway's Treasures for tapped Pirates;
- Daring Piracy's token exile;
- Zara's creature returning to hand;
- Ragavan's dash return.

Beckett's condition is history, so exiling the token or returning Zara's creature first doesn't matter. Put Edward Kenway's trigger to resolve while the attackers are still tapped and on the battlefield: anything that leaves first is no longer counted.

**Citations**

- Oracle, *Edward Kenway*: “At the beginning of your end step, create a Treasure token for each tapped Assassin, Pirate, and/or Vehicle you control.”
- Scryfall ruling, *Edward Kenway*: “If a tapped permanent you control has more than one of the subtypes listed in Edward’s first ability, count it only once when determining how many Treasure tokens to create.”
- [CR 603.3b](#cr-6033b)

## Zones, commander tax and the command zone

### beckett-15: Commander tax and the 4-mana commander

**Status:** ✅ verified · **Cards:** Admiral Beckett Brass, Deflecting Swat, Fierce Guardianship, Jeska's Will

**Ruling.** Beckett costs {1}{U}{B}{R}, then 6, then 8. Fierce Guardianship and Deflecting Swat are free and Jeska's Will gets both modes only while you control a commander, so they get worse while Beckett is off the battlefield. Beckett has no protection of his own: Lightning Greaves (shroud) and Siren Stormtamer cover him.

**Citations**

- Oracle, *Fierce Guardianship*: “If you control a commander, you may cast this spell without paying its mana cost.”
- Oracle, *Lightning Greaves*: “Equipped creature has haste and shroud.”
- Scryfall ruling, *Fierce Guardianship*: “It doesn't matter whose commander you control. Any one will do.”
- [CR 903.8](#cr-9038)

## What the list depends on

### beckett-16: What the list depends on

**Status:** ✅ verified · **Cards:** Admiral Beckett Brass

**Ruling.** The plan needs three Pirates connecting with the same player in one turn. Evasion density is high: flyers, menace, unblockable, fear via Cover of Darkness, Open into Wonder. Interaction is light on fogs and blockers. Mass blockers or fogs stop the steal for a turn but don't disable the board. Stealing a permanent is the main value; the deck has no deterministic two-card combo (Spellbook lists none).

**Citations**

- Oracle, *Admiral Beckett Brass*: “At the beginning of your end step, gain control of target nonland permanent controlled by a player who was dealt combat damage by three or more Pirates this turn.”
- [CR 510.2](#cr-5102)

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 108.3

The owner of a card in the game is the player who started the game with it in their deck. If a card is brought into the game from outside the game rather than starting in a player’s deck, its owner is the player who brought it into the game. If a card starts the game in the command zone, its owner is the player who put it into the command zone to start the game. Legal ownership of a card in the game is irrelevant to the game rules except for the rules for ante. (See rule 407.)

#### CR 111.2

The player who creates a token is its owner. The token enters the battlefield under that player’s control.

#### CR 111.4

A spell or ability that creates a token sets both its name and its subtype(s). If the spell or ability doesn’t specify the name of the token, its name is the same as its subtype(s) plus the word “Token.” Once a token is on the battlefield, changing its name doesn’t change its subtype(s), and vice versa.

#### CR 115.1

Some spells and abilities require their controller to choose one or more targets for them. The targets are object(s) and/or player(s) the spell or ability will affect. These targets are declared as part of the process of putting the spell or ability on the stack. The targets can’t be changed except by another spell or ability that explicitly says it can do so.

#### CR 120.3a

Damage dealt to a player by a source without infect causes that player to lose that much life.

#### CR 205.3m

Creatures and kindreds share their lists of subtypes; these subtypes are called creature types. One creature type is two words long: Time Lord. All other creature types are one word long: Advisor, Aetherborn, Alien, Ally, Angel, Antelope, Ape, Archer, Archon, Armadillo, Army, Artificer, Assassin, Assembly-Worker, Astartes, Atog, Aurochs, Avatar, Azra, Badger, Balloon, Barbarian, Bard, Basilisk, Bat, Bear, Beast, Beaver, Beeble, Beholder, Berserker, Bird, Bison, Blinkmoth, Boar, Bringer, Brushwagg, Camarid, Camel, Capybara, Caribou, Carrier, Cat, Centaur, Child, Chimera, Citizen, Cleric, …

#### CR 500.8

Some effects can add phases to a turn. They do this by adding the phases directly after the specified phase. If multiple extra phases are created after the same phase, the most recently created phase will occur first.

#### CR 506.1

The combat phase has five steps, which proceed in order: beginning of combat, declare attackers, declare blockers, combat damage, and end of combat. The declare blockers and combat damage steps are skipped if no creatures are declared as attackers or put onto the battlefield attacking (see rule 508.8). There are two combat damage steps if any attacking or blocking creature has first strike (see rule 702.7) or double strike (see rule 702.4).

#### CR 508.4

If a creature is put onto the battlefield attacking, its controller chooses which defending player, planeswalker a defending player controls, or battle a defending player protects it’s attacking as it enters the battlefield (unless the effect that put it onto the battlefield specifies what it’s attacking). Similarly, if an effect states that a creature is attacking, its controller chooses which defending player, planeswalker a defending player controls, or battle a defending player protects it’s attacking (unless the effect has already specified). Such creatures are “attacking” but, for the …

#### CR 510.2

Second, all combat damage that’s been assigned is dealt simultaneously. This turn-based action doesn’t use the stack. No player has the chance to cast spells or activate abilities between the time combat damage is assigned and the time it’s dealt.

#### CR 601.2

To cast a spell is to take it from where it is (usually the hand), put it on the stack, and pay its costs, so that it will eventually resolve and have its effect. Casting a spell includes proposal of the spell (rules 601.2a–d) and determination and payment of costs (rules 601.2f–h). To cast a spell, a player follows the steps listed below, in order. A player must be legally allowed to cast the spell to begin this process (see rule 601.3). If a player is unable to comply with the requirements of a step listed below while performing that step, the casting of the spell is illegal; the game …

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 603.3b

If multiple abilities have triggered since the last time a player received priority, the abilities are placed on the stack in a two-part process. First, each player, in APNAP order, puts each triggered ability they control with a trigger condition that isn’t another ability triggering on the stack in any order they choose. (See rule 101.4.) Second, each player, in APNAP order, puts all remaining triggered abilities they control on the stack in any order they choose. Then the game once again checks for and performs state-based actions until none are performed, then abilities that triggered …

#### CR 603.3c

If a triggered ability is modal, its controller announces the mode choice when putting the ability on the stack. If one of the modes would be illegal (due to an inability to choose legal targets, for example), that mode can’t be chosen. If no mode is chosen, the ability is removed from the stack. (See rule 700.2.)

#### CR 603.3d

The remainder of the process for putting a triggered ability on the stack is identical to the process for casting a spell listed in rules 601.2c–d. If a choice is required when the triggered ability goes on the stack but no legal choices can be made for it, or if a rule or a continuous effect otherwise makes the ability illegal, the ability is simply removed from the stack.

#### CR 604.3

Some static abilities are characteristic-defining abilities. A characteristic-defining ability conveys information about an object’s characteristics that would normally be found elsewhere on that object (such as in its mana cost, type line, or power/toughness box). Characteristic-defining abilities can add to or override information found elsewhere on that object. Characteristic-defining abilities function in all zones. They also function outside the game and before the game begins.

#### CR 608.3f

If the object that’s resolving is a copy of a permanent spell, it will become a token permanent as it is put onto the battlefield in any of the steps above. A token put onto the battlefield this way is no longer a copy of a spell and is not “created” for the purposes of any rules or effects that refer to creating a token.

#### CR 613.1b

Layer 2: Control-changing effects are applied.

#### CR 613.1d

Layer 4: Type-changing effects are applied. These include effects that change an object’s card type, subtype, and/or supertype.

#### CR 613.4b

Layer 7b: Effects that set power and/or toughness to a specific number or value are applied. Effects that refer to the base power and/or toughness of a creature apply in this layer.

#### CR 613.4c

Layer 7c: Effects and counters that modify power and/or toughness (but don’t set power and/or toughness to a specific number or value) are applied.

#### CR 700.2

A spell or ability is modal if it has two or more options in a bulleted list preceded by instructions for a player to choose a number of those options, such as “Choose one —.” Each of those options is a mode. Modal cards printed prior to the Khans of Tarkir™ set didn’t use bulleted lists for the modes; these cards have received errata in the Oracle card reference so the modes do appear in a bulleted list.

#### CR 702.73a

Changeling is a characteristic-defining ability. “Changeling” means “This object is every creature type.” This ability works everywhere, even outside the game. See rule 604.3.

#### CR 704.5j

If two or more legendary permanents with the same name are controlled by the same player, that player chooses one of them, and the rest are put into their owners’ graveyards. This is called the “legend rule.”

#### CR 707.10

To copy a spell, activated ability, or triggered ability means to put a copy of it onto the stack; a copy of a spell isn’t cast and a copy of an activated ability isn’t activated. A copy of a spell or ability copies both the characteristics of the spell or ability and all decisions made for it, including modes, targets, the value of X, and additional or alternative costs. (See rule 601, “Casting Spells.”) Choices that are normally made on resolution are not copied. If an effect of the copy refers to objects used to pay its costs, it uses the objects used to pay the costs of the original spell …

#### CR 903.8

A player may cast a commander they own from the command zone. A commander cast from the command zone costs an additional {2} for each previous time the player casting it has cast it from the command zone that game. This additional cost is informally known as the “commander tax.”

