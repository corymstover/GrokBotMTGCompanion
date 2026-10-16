---
title: "Don Andres, the Renegade — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Don Andres, the Renegade — Interaction Review

> Bot cycle 48 · batch B · reviewed 2026-10-16. Deck: [Don Andres, the Renegade](../decks/don-andres-the-renegade.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-15), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Current list | [`exports/grixis-archidekt/don-andres-the-renegade.txt`](../../exports/grixis-archidekt/don-andres-the-renegade.txt) · SHA-256 `3c5a31e6cf23e2b81d7d4e85d28426231de10d714aae769da886aeff384c7e03` |
| Rulings | **12** (11 verified · 0 uncertain · 1 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-15 · rulings 2026-10-15 |
| Source attestations | [`Don_Andres_the_Renegade_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/don_andres_the_renegade_2026-10-14/Don_Andres_the_Renegade_Rules_Attestation.json) (13 interactions, all PASS) |

## Contents
- [Summary](#summary)
- [Flags and open questions](#flags-and-open-questions)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Engines and payoffs](#engines-and-payoffs)
- [Key card-pair interactions](#key-card-pair-interactions)
- [Layers and continuous effects](#layers-and-continuous-effects)
- [Replacement and prevention effects](#replacement-and-prevention-effects)
- [Trigger ordering](#trigger-ordering)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [Rules cited](#rules-cited)

## Summary

Don Andres, the Renegade pays off stealing: opponent-owned creatures you control become +2/+2 menace deathtouch Pirates, and casting an opponent-owned noncreature spell makes two tapped Treasures. This review re-verifies the thirteen items of the deck's rules attestation against current CR, Oracle and official rulings.

Rules surprise: Dauthi Voidwalker stops opponent-owned creatures from dying, so Thieving Amalgam's drain doesn't trigger while it's out (anti-synergy note, no list change). No list errors.

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [donandres-06](#donandres-06-dauthi-voidwalker-turns-off-thieving-amalgams-drain) | 🚩 list flag (anti-synergy) | Dauthi Voidwalker turns off Thieving Amalgam's drain | Pilot note, not a list error: the two cards pull in different directions for opponent-owned nontoken creatures. Voidwalker gives free replays; Amalgam gives the 2-life drain. Choose which one you want before chump-attacking or sacrificing stolen creatures. |

## Commander rules text and edge cases

### donandres-01: Ownership, not control, decides both of Don's abilities

**Status:** ✅ verified · **Cards:** Don Andres, the Renegade

**Ruling.** Don's static bonus applies to every creature you control whose card (or token) belongs to someone else. That covers creatures you steal, opponents' creature cards you cast, creatures you reanimate from opponents' graveyards, and opponent-owned cards put directly onto the battlefield under your control. Ownership never changes: the owner is whoever started the game with the card, and the owner of a token is the player who created it. So a stolen opponent token (for example from Coercive Recruiter or Insurrection) gets the bonus too.

**Citations**

- Oracle, *Don Andres, the Renegade*: “Each creature you control but don't own gets +2/+2, has menace and deathtouch, and is a Pirate in addition to its other types.”
- Scryfall ruling, *Don Andres, the Renegade*: “The player who creates a token is its owner.”
- [CR 108.3](#cr-1083), [CR 111.2](#cr-1112), [CR 613.1b](#cr-6131b)
- Source (re-verified): [`Don_Andres_the_Renegade_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/don_andres_the_renegade_2026-10-14/Don_Andres_the_Renegade_Rules_Attestation.json) → “Don Andres controlled-but-not-owned creature static effect”

### donandres-02: The Treasure trigger needs a noncreature spell that someone else owns

**Status:** ✅ verified · **Cards:** Don Andres, the Renegade, Court of Locthwain, Praetor's Grasp, Outrageous Robbery

**Ruling.** Don triggers when you cast a noncreature spell whose card belongs to another player: an opponent's instant, sorcery, artifact, enchantment or planeswalker cast from exile (Court of Locthwain, Praetor's Grasp, Outrageous Robbery) or from their graveyard. The spell that steals (Praetor's Grasp, Outrageous Robbery) is your own card and doesn't trigger Don. Opponent-owned creature spells don't trigger him either; they get the static bonus once they're on the battlefield.

**Citations**

- Oracle, *Don Andres, the Renegade*: “Whenever you cast a noncreature spell you don't own, create two tapped Treasure tokens.”
- [CR 108.3](#cr-1083), [CR 601.2](#cr-6012)
- Source (re-verified): [`Don_Andres_the_Renegade_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/don_andres_the_renegade_2026-10-14/Don_Andres_the_Renegade_Rules_Attestation.json) → “Don Andres noncreature stolen-spell trigger”
- Source (re-verified): [`Don_Andres_the_Renegade_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/don_andres_the_renegade_2026-10-14/Don_Andres_the_Renegade_Rules_Attestation.json) → “Court of Locthwain stolen-card casting”

## Engines and payoffs

### donandres-11: Cast-a-spell-you-don't-own payoffs stack with Don

**Status:** ✅ verified · **Cards:** Don Andres, the Renegade, Gonti, Night Minister, Tasha, the Witch Queen, Thieving Varmint

**Ruling.** Gonti gives a Treasure to any player who casts a spell they don't own, Tasha makes a 3/3 Demon whenever you cast a spell you don't own, and Thieving Varmint's mana can only be spent on such spells. Unlike Don's trigger, Gonti and Tasha also count opponent-owned creature spells. A stolen noncreature spell with all three out makes three Treasures and a Demon.

**Citations**

- Oracle, *Gonti, Night Minister*: “Whenever a player casts a spell they don't own, that player creates a Treasure token.”
- Oracle, *Tasha, the Witch Queen*: “Whenever you cast a spell you don't own, create a 3/3 black Demon creature token.”
- Oracle, *Thieving Varmint*: “Spend this mana only to cast spells you don't own.”
- Scryfall ruling, *Thieving Varmint*: “You may spend the two mana added by the last ability on the same spell you don’t own or on two different spells you don’t own.”
- [CR 603.2](#cr-6032)

## Key card-pair interactions

### donandres-08: Each Wand of Wonder spell is a separate trigger

**Status:** ✅ verified · **Cards:** Don Andres, the Renegade, Wand of Wonder

**Ruling.** Wand of Wonder lets you cast up to X instants and sorceries exiled from opponents' libraries, X from 1 to 3 by the d20 roll. Each is a separate noncreature spell you don't own, so each triggers Don separately.

**Citations**

- Oracle, *Wand of Wonder*: “You may cast up to X instant and/or sorcery spells from among cards exiled this way without paying their mana costs.”
- [CR 601.2](#cr-6012)
- Source (re-verified): [`Don_Andres_the_Renegade_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/don_andres_the_renegade_2026-10-14/Don_Andres_the_Renegade_Rules_Attestation.json) → “Wand of Wonder multi-cast interaction”

### donandres-09: Exiled-face-down theft keeps the owner

**Status:** ✅ verified · **Cards:** Don Andres, the Renegade, Decadent Dragon // Expensive Taste, Black Cat, Cunning Thief, Siphon Insight

**Ruling.** Expensive Taste, Black Cat and Siphon Insight exile opponents' cards face down for you to play. Exile doesn't change ownership. Noncreature spells cast from them trigger Don, and creature spells cast from them get his bonus. Black Cat's permission lasts as long as the cards stay exiled, and mana of any type can be spent. Normal timing rules still apply.

**Citations**

- Oracle, *Decadent Dragon // Expensive Taste*: “Exile the top two cards of target opponent's library face down. You may look at and play those cards for as long as they remain exiled.”
- Oracle, *Black Cat, Cunning Thief*: “You may play the exiled cards for as long as they remain exiled.”
- Scryfall ruling, *Black Cat, Cunning Thief*: “You must follow all normal timing rules when playing a land or casting a spell this way.”
- Scryfall ruling, *Decadent Dragon // Expensive Taste*: “You must still follow all normal timing rules to play cards exiled with Expensive Taste.”
- [CR 108.3](#cr-1083), [CR 406.3](#cr-4063)
- Source (re-verified): [`Don_Andres_the_Renegade_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/don_andres_the_renegade_2026-10-14/Don_Andres_the_Renegade_Rules_Attestation.json) → “Decadent Dragon // Expensive Taste”
- Source (re-verified): [`Don_Andres_the_Renegade_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/don_andres_the_renegade_2026-10-14/Don_Andres_the_Renegade_Rules_Attestation.json) → “Black Cat, Cunning Thief”

### donandres-10: Don makes stolen creatures Pirates for Pirate payoffs

**Status:** ✅ verified · **Cards:** Don Andres, the Renegade, Admiral Beckett Brass, Kindred Discovery, Coercive Recruiter

**Ruling.** Opponent-owned creatures you control are Pirates while Don is out. They count for Beckett's three-Pirate damage check and for Kindred Discovery naming Pirate, and their arrival triggers Coercive Recruiter. Beckett's check looks back at which Pirates dealt combat damage, so it doesn't matter if Don leaves later in the turn.

**Citations**

- Oracle, *Don Andres, the Renegade*: “Each creature you control but don't own gets +2/+2, has menace and deathtouch, and is a Pirate in addition to its other types.”
- Oracle, *Coercive Recruiter*: “Whenever this creature or another Pirate you control enters, gain control of target creature until end of turn.”
- Scryfall ruling, *Admiral Beckett Brass*: “It doesn't care whether Admiral Beckett Brass was on the battlefield when those Pirates dealt combat damage, whether those creatures are still on the battlefield, or whether they're still Pirates.”
- [CR 613.1d](#cr-6131d), [CR 205.3m](#cr-2053m)
- Source (re-verified): [`Don_Andres_the_Renegade_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/don_andres_the_renegade_2026-10-14/Don_Andres_the_Renegade_Rules_Attestation.json) → “Admiral Beckett Brass and Don's Pirate type”
- Source (re-verified): [`Don_Andres_the_Renegade_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/don_andres_the_renegade_2026-10-14/Don_Andres_the_Renegade_Rules_Attestation.json) → “Kindred Discovery / Coercive Recruiter Pirate checks”

## Layers and continuous effects

### donandres-05: Manifested opponent cards are 2/2s that get the bonus

**Status:** ✅ verified · **Cards:** Don Andres, the Renegade, Thieving Amalgam

**Ruling.** Thieving Amalgam manifests the top card of each opponent's library at their upkeep. The face-down 2/2 is a creature you control and that opponent owns, so with Don out it's a 4/4 menace, deathtouch Pirate. The opponent can't look at the face-down card. It can only be turned face up for its mana cost if it's a creature card.

**Citations**

- Oracle, *Thieving Amalgam*: “At the beginning of each opponent's upkeep, you manifest the top card of that player's library.”
- Scryfall ruling, *Thieving Amalgam*: “Your opponents can't look at the card they own that you manifested.”
- [CR 701.40a](#cr-70140a), [CR 708.2](#cr-7082), [CR 613.1](#cr-6131)
- Source (re-verified): [`Don_Andres_the_Renegade_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/don_andres_the_renegade_2026-10-14/Don_Andres_the_Renegade_Rules_Attestation.json) → “Thieving Amalgam manifest interaction”

## Replacement and prevention effects

### donandres-06: Dauthi Voidwalker turns off Thieving Amalgam's drain

**Status:** 🚩 list flag · **Evidence:** fact · **Cards:** Don Andres, the Renegade, Dauthi Voidwalker, Thieving Amalgam

**Ruling.** Dauthi Voidwalker exiles any card that would go to an opponent's graveyard from anywhere. A stolen or manifested creature you control is owned by an opponent, so when it would die it goes to exile with a void counter instead. It never dies, so Thieving Amalgam's 'creature you control but don't own dies' drain doesn't trigger. Tokens still die normally. The upside: the exiled card gets a void counter, so Voidwalker can later play it for free.

**List flag (anti-synergy).** Pilot note, not a list error: the two cards pull in different directions for opponent-owned nontoken creatures. Voidwalker gives free replays; Amalgam gives the 2-life drain. Choose which one you want before chump-attacking or sacrificing stolen creatures.

**Citations**

- Oracle, *Dauthi Voidwalker*: “If a card would be put into an opponent's graveyard from anywhere, instead exile it with a void counter on it.”
- Oracle, *Thieving Amalgam*: “Whenever a creature you control but don't own dies, its owner loses 2 life and you gain 2 life.”
- Scryfall ruling, *Dauthi Voidwalker*: “Abilities that would trigger when those creatures die won't trigger.”
- Scryfall ruling, *Dauthi Voidwalker*: “Tokens still die while Dauthi Voidwalker is on the battlefield.”
- [CR 700.4](#cr-7004), [CR 614.6](#cr-6146), [CR 400.3](#cr-4003)

## Trigger ordering

### donandres-07: Roaming Throne on Pirate doubles the Treasure trigger, not the static

**Status:** ✅ verified · **Cards:** Don Andres, the Renegade, Roaming Throne

**Ruling.** Don is a Pirate. With Roaming Throne naming Pirate, his Treasure ability triggers an additional time, so each qualifying spell makes four tapped Treasures. Throne only affects triggered abilities; the +2/+2, menace and deathtouch are static and aren't doubled. Throne doesn't copy the ability, it triggers again.

**Citations**

- Oracle, *Roaming Throne*: “If a triggered ability of another creature you control of the chosen type triggers, it triggers an additional time.”
- Scryfall ruling, *Roaming Throne*: “Roaming Throne's last ability doesn't copy the triggered ability; it just causes the ability to trigger an additional time.”
- [CR 603.2](#cr-6032), [CR 604.1](#cr-6041)
- Source (re-verified): [`Don_Andres_the_Renegade_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/don_andres_the_renegade_2026-10-14/Don_Andres_the_Renegade_Rules_Attestation.json) → “Roaming Throne naming Pirate”

## Zones, commander tax and the command zone

### donandres-03: Copies you make are spells you own

**Status:** ✅ verified · **Cards:** Don Andres, the Renegade, Arcane Heist

**Ruling.** The owner of a copy of a spell is the player who put it on the stack. A cipher copy of Arcane Heist is therefore yours, and casting it doesn't trigger Don. The opponent's instant or sorcery that Arcane Heist lets you cast from their graveyard is theirs, so that cast does trigger Don. If that spell would go to their graveyard afterwards, Arcane Heist exiles it instead.

**Citations**

- Oracle, *Arcane Heist*: “You may cast target instant or sorcery card from an opponent's graveyard without paying its mana cost. If that spell would be put into their graveyard, exile it instead.”
- Scryfall ruling, *Don Andres, the Renegade*: “The owner of a copy of a spell is the player under whose control it was put onto the stack.”
- Scryfall ruling, *Arcane Heist*: “The copy of the card with cipher is created in and cast from exile.”
- [CR 707.10](#cr-70710), [CR 707.12](#cr-70712), [CR 702.99a](#cr-70299a)
- Source (re-verified): [`Don_Andres_the_Renegade_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/don_andres_the_renegade_2026-10-14/Don_Andres_the_Renegade_Rules_Attestation.json) → “Arcane Heist cipher copies”

### donandres-04: Putting a card onto the battlefield isn't casting it

**Status:** ✅ verified · **Cards:** Don Andres, the Renegade, Jhoira, Weatherlight Corsair, Animate Dead, Reanimate

**Ruling.** Jhoira puts an opponent's historic permanent card onto the battlefield under your control, and Animate Dead and Reanimate can return an opponent's creature card. None of those is a cast, so a noncreature historic permanent from Jhoira doesn't trigger Don's Treasures. Any creature that arrives this way is still opponent-owned, so it gets +2/+2, menace, deathtouch and the Pirate type.

**Citations**

- Oracle, *Jhoira, Weatherlight Corsair*: “You put that card onto the battlefield under your control and lose life equal to that permanent's mana value.”
- Oracle, *Reanimate*: “Put target creature card from a graveyard onto the battlefield under your control.”
- [CR 601.2](#cr-6012), [CR 108.3](#cr-1083)
- Source (re-verified): [`Don_Andres_the_Renegade_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/don_andres_the_renegade_2026-10-14/Don_Andres_the_Renegade_Rules_Attestation.json) → “Jhoira, Weatherlight Corsair”
- Source (re-verified): [`Don_Andres_the_Renegade_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/don_andres_the_renegade_2026-10-14/Don_Andres_the_Renegade_Rules_Attestation.json) → “Animate Dead and Reanimate opposing graveyards”

### donandres-12: Stolen permanents leave with their owner

**Status:** ✅ verified · **Cards:** Don Andres, the Renegade, Hostage Taker, Admiral Beckett Brass

**Ruling.** If an opponent leaves the game, every object they own leaves too, including creatures you stole (Beckett, Gilded Drake, Hostage Taker casts). If you leave, cards you control from Hostage Taker are exiled. Hostage Taker's exiled card returns at once if Taker leaves before you cast it; once you begin casting it, it's a new object you keep.

**Citations**

- Scryfall ruling, *Hostage Taker*: “Once you begin to cast the exiled card, it's considered a new object. You'll control that spell and the permanent that spell becomes even if Hostage Taker leaves the battlefield.”
- Scryfall ruling, *Admiral Beckett Brass*: “In a multiplayer game, if a player leaves the game, all cards that player owns leave as well, and any effects that give the player control of permanents immediately end.”
- [CR 800.4a](#cr-8004a)

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 108.3

The owner of a card in the game is the player who started the game with it in their deck. If a card is brought into the game from outside the game rather than starting in a player’s deck, its owner is the player who brought it into the game. If a card starts the game in the command zone, its owner is the player who put it into the command zone to start the game. Legal ownership of a card in the game is irrelevant to the game rules except for the rules for ante. (See rule 407.)

#### CR 111.2

The player who creates a token is its owner. The token enters the battlefield under that player’s control.

#### CR 205.3m

Creatures and kindreds share their lists of subtypes; these subtypes are called creature types. One creature type is two words long: Time Lord. All other creature types are one word long: Advisor, Aetherborn, Alien, Ally, Angel, Antelope, Ape, Archer, Archon, Armadillo, Army, Artificer, Assassin, Assembly-Worker, Astartes, Atog, Aurochs, Avatar, Azra, Badger, Balloon, Barbarian, Bard, Basilisk, Bat, Bear, Beast, Beaver, Beeble, Beholder, Berserker, Bird, Bison, Blinkmoth, Boar, Bringer, Brushwagg, Camarid, Camel, Capybara, Caribou, Carrier, Cat, Centaur, Child, Chimera, Citizen, Cleric, …

#### CR 400.3

If an object would go to any library, graveyard, or hand other than its owner’s, it goes to its owner’s corresponding zone.

#### CR 406.3

Exiled cards are, by default, kept face up and may be examined by any player at any time. Cards “exiled face down” can’t be examined by any player except when instructions allow it. However, if a player is instructed to look at a card and then exile it face down, or once a player is allowed to look at a card exiled face down, that player may continue to look at that card until it leaves the exile zone or is part of a pile of cards that are shuffled, even if the instruction allowing the player to do so no longer applies.

#### CR 601.2

To cast a spell is to take it from where it is (usually the hand), put it on the stack, and pay its costs, so that it will eventually resolve and have its effect. Casting a spell includes proposal of the spell (rules 601.2a–d) and determination and payment of costs (rules 601.2f–h). To cast a spell, a player follows the steps listed below, in order. A player must be legally allowed to cast the spell to begin this process (see rule 601.3). If a player is unable to comply with the requirements of a step listed below while performing that step, the casting of the spell is illegal; the game …

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 604.1

Static abilities do something all the time rather than being activated or triggered. They are written as statements, and they’re simply true.

#### CR 613.1

The values of an object’s characteristics are determined by starting with the actual object. For a card, that means the values of the characteristics printed on that card. For a token or a copy of a spell or card, that means the values of the characteristics defined by the effect that created it. Then all applicable continuous effects are applied in a series of layers in the following order:

#### CR 613.1b

Layer 2: Control-changing effects are applied.

#### CR 613.1d

Layer 4: Type-changing effects are applied. These include effects that change an object’s card type, subtype, and/or supertype.

#### CR 614.6

If an event is replaced, it never happens. A modified event occurs instead, which may in turn trigger abilities. Note that the modified event may contain instructions that can’t be carried out, in which case the impossible instruction is simply ignored.

#### CR 700.4

The term dies means “is put into a graveyard from the battlefield.”

#### CR 701.40a

To manifest a card, turn it face down. It becomes a 2/2 face-down creature card with no text, no name, no subtypes, and no mana cost. Put that card onto the battlefield face down. That permanent is a manifested permanent for as long as it remains face down. The effect defining its characteristics works while the card is face down and ends when it’s turned face up.

#### CR 702.99a

Cipher appears on some instants and sorceries. It represents two abilities. The first is a spell ability that functions while the spell with cipher is on the stack. The second is a static ability that functions while the card with cipher is in the exile zone. “Cipher” means “If this spell is represented by a card, you may exile this card encoded on a creature you control” and “For as long as this card is encoded on that creature, that creature has ‘Whenever this creature deals combat damage to a player, you may copy the encoded card and you may cast the copy without paying its mana cost.’”

#### CR 707.10

To copy a spell, activated ability, or triggered ability means to put a copy of it onto the stack; a copy of a spell isn’t cast and a copy of an activated ability isn’t activated. A copy of a spell or ability copies both the characteristics of the spell or ability and all decisions made for it, including modes, targets, the value of X, and additional or alternative costs. (See rule 601, “Casting Spells.”) Choices that are normally made on resolution are not copied. If an effect of the copy refers to objects used to pay its costs, it uses the objects used to pay the costs of the original spell …

#### CR 707.12

An effect that instructs a player to cast a copy of an object (and not just copy a spell) follows the rules for casting spells, except that the copy is created in the same zone the object is in and then cast while another spell or ability is resolving. Casting a copy of an object follows steps 601.2a–h of rule 601, “Casting Spells,” and then the copy becomes cast. Once cast, the copy is a spell on the stack, and just like any other spell it can resolve or be countered.

#### CR 708.2

Face-down spells and face-down permanents have no characteristics other than those listed by the ability or rules that allowed the spell or permanent to be face down. Any listed characteristics are the copiable values of that object’s characteristics. (See rule 613, “Interaction of Continuous Effects,” and rule 707, “Copying Objects.”)

#### CR 800.4a

When a player leaves the game, all objects (see rule 109) owned by that player leave the game and any effects which give that player control of any objects or players end. Then, if that player controlled any objects on the stack not represented by cards, those objects cease to exist. Then, if there are any objects still controlled by that player, those objects are exiled. This is not a state-based action. It happens as soon as the player leaves the game. If the player who left the game had priority at the time they left, priority passes to the next player in turn order who’s still in the game.

