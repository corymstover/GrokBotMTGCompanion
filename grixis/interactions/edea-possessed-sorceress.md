---
title: "Edea, Possessed Sorceress — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Edea, Possessed Sorceress — Interaction Review

> Bot cycle 48 · batch B · reviewed 2026-10-16. Deck: [Edea, Possessed Sorceress](../decks/edea-possessed-sorceress.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/edea-possessed-sorceress.txt`](../../exports/grixis-archidekt/edea-possessed-sorceress.txt) · SHA-256 `d41924a6b09c4232b438aa863c833a28f67bdd6598c9bba470ae66f23428acd6` |
| Rulings | **11** (11 verified · 0 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`Edea_Possessed_Sorceress_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edea_possessed_sorceress_2026-10-14/Edea_Possessed_Sorceress_Rules_Attestation.json) (18 interactions, all PASS) |

## Contents
- [Summary](#summary)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Key card-pair interactions](#key-card-pair-interactions)
- [Layers and continuous effects](#layers-and-continuous-effects)
- [Timing and priority](#timing-and-priority)
- [Trigger ordering](#trigger-ordering)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [What the list depends on](#what-the-list-depends-on)
- [Rules cited](#rules-cited)

## Summary

Edea, Possessed Sorceress steals an opponent's creature each combat; when a creature you control but don't own dies, it goes back to its owner and you draw. This review re-verifies the eighteen items of the deck's rules attestation.

Key rules: extra Edea death triggers only draw, Irma-Edea misses the combat she copies in, and ordering Chaos Shrine's Black Crystal first keeps the opponent's creature. Thassa makes a steal permanent. No list errors.

## Commander rules text and edge cases

### edea-01: The combat steal is targeted; Arcane Lighthouse handles hexproof

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Edea, Possessed Sorceress, Arcane Lighthouse

**Ruling.** Edea's combat trigger targets a creature an opponent controls. If the target is illegal on resolution, nothing happens. Activate Arcane Lighthouse before beginning of combat: opponents' creatures lose hexproof and shroud for the turn. It only affects creatures they control when it resolves.

**Citations**

- Oracle, *Edea, Possessed Sorceress*: “At the beginning of combat on your turn, gain control of target creature an opponent controls until end of turn. Untap that creature. It gains haste until end of turn.”
- Scryfall ruling, *Arcane Lighthouse*: “The second ability applies only to creatures controlled by your opponents when it resolves.”
- [CR 115.1](#cr-1151), [CR 608.2b](#cr-6082b), [CR 702.11a](#cr-70211a)
- Source (re-verified): [`Edea_Possessed_Sorceress_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edea_possessed_sorceress_2026-10-14/Edea_Possessed_Sorceress_Rules_Attestation.json) → “Edea temporary control and targeting”

### edea-02: A borrowed creature that dies goes back to its owner, and you draw

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Edea, Possessed Sorceress, Viscera Seer, Phyrexian Altar, Pitiless Plunderer

**Ruling.** A creature Edea took is still owned by its opponent. If it dies while you control it (sacrificed to Viscera Seer, Phyrexian Altar, Ashnod's Altar), Edea returns it under its owner's control and you draw. Your 'creature you control dies' triggers (Pitiless Plunderer, Grave Pact, Mayhem Devil on the sacrifice) see the death. Edea's return is a new permanent for its owner: its enters abilities trigger for that player, not for you.

**Citations**

- Oracle, *Edea, Possessed Sorceress*: “Whenever a creature you control but don't own dies, return it to the battlefield under its owner's control and you draw a card.”
- [CR 700.4](#cr-7004), [CR 603.3a](#cr-6033a), [CR 400.7](#cr-4007), [CR 108.3](#cr-1083)
- Source (re-verified): [`Edea_Possessed_Sorceress_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edea_possessed_sorceress_2026-10-14/Edea_Possessed_Sorceress_Rules_Attestation.json) → “Edea death trigger after a borrowed creature dies”

## Key card-pair interactions

### edea-09: Saw in Half on a borrowed creature

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Edea, Possessed Sorceress, Saw in Half

**Ruling.** Saw in Half destroys the creature, and the creature's controller makes the two half-size copies. If you destroy a creature you borrowed, you get the tokens, Edea returns the card to its owner and you draw. If a replacement effect exiles it instead of letting it die, there are no tokens.

**Citations**

- Oracle, *Saw in Half*: “If that creature dies this way, its controller creates two tokens that are copies of that creature”
- Scryfall ruling, *Saw in Half*: “The same is true if the creature is destroyed but instead of going to its owner's graveyard, a replacement effect moves it elsewhere, such as exile.”
- [CR 701.8a](#cr-7018a), [CR 700.4](#cr-7004)
- Source (re-verified): [`Edea_Possessed_Sorceress_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edea_possessed_sorceress_2026-10-14/Edea_Possessed_Sorceress_Rules_Attestation.json) → “Saw in Half on a borrowed creature”

### edea-10: More borrowing: Mass Mutiny and Captivating Crew

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Edea, Possessed Sorceress, Mass Mutiny, Captivating Crew

**Ruling.** Mass Mutiny takes up to one creature from each opponent until end of turn. It's errata'd to 'up to one', so you can cast it when an opponent has none. Captivating Crew steals at sorcery speed for {3}{R}, so do it precombat, then let Edea take a second creature at beginning of combat. Every borrowed creature is opponent-owned, so each death triggers Edea.

**Citations**

- Oracle, *Captivating Crew*: “{3}{R}: Gain control of target creature an opponent controls until end of turn. Untap that creature. It gains haste until end of turn. Activate only as a sorcery.”
- Scryfall ruling, *Mass Mutiny*: “The phrase "up to one" was inadvertently omitted from Mass Mutiny's rules text. The card has received errata to correct this.”
- [CR 108.3](#cr-1083), [CR 307.1](#cr-3071)
- Source (re-verified): [`Edea_Possessed_Sorceress_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edea_possessed_sorceress_2026-10-14/Edea_Possessed_Sorceress_Rules_Attestation.json) → “Mass Mutiny with Edea”
- Source (re-verified): [`Edea_Possessed_Sorceress_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edea_possessed_sorceress_2026-10-14/Edea_Possessed_Sorceress_Rules_Attestation.json) → “Captivating Crew sequencing”

## Layers and continuous effects

### edea-04: Edea copies: Spark Double, Sakashima, Irma

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Edea, Possessed Sorceress, Spark Double, Sakashima of a Thousand Faces, Irma, Part-Time Mutant

**Ruling.** Spark Double is a nonlegendary Edea. With Sakashima out, the legend rule doesn't apply to you, so a Sakashima-Edea is fine. Irma becomes a copy at beginning of combat but keeps her own name and the copy ability. She doesn't become Edea until after that combat's beginning-of-combat triggers, so she misses that steal. She stays Edea afterwards, so she triggers in later combats that turn, such as Full Throttle or Karlach extra combats.

**Citations**

- Oracle, *Irma, Part-Time Mutant*: “At the beginning of combat on your turn, Irma becomes a copy of up to one other target creature you control, except her name is Irma, Part-Time Mutant and she has this ability.”
- Oracle, *Sakashima of a Thousand Faces*: “The "legend rule" doesn't apply to permanents you control.”
- Scryfall ruling, *Irma, Part-Time Mutant*: “Because Irma isn't entering the battlefield when she becomes a copy of another creature, any "When [this creature] enters" or "[This creature] enters with" abilities of the copied creature won't apply.”
- [CR 707.2](#cr-7072), [CR 704.5j](#cr-7045j), [CR 603.2](#cr-6032), [CR 507.1](#cr-5071)
- Source (re-verified): [`Edea_Possessed_Sorceress_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edea_possessed_sorceress_2026-10-14/Edea_Possessed_Sorceress_Rules_Attestation.json) → “Spark Double and Sakashima as Edea copies”
- Source (re-verified): [`Edea_Possessed_Sorceress_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edea_possessed_sorceress_2026-10-14/Edea_Possessed_Sorceress_Rules_Attestation.json) → “Irma, Part-Time Mutant copying Edea”

## Timing and priority

### edea-05: Extra combats mean extra steals

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Edea, Possessed Sorceress, Full Throttle, Karlach, Fury of Avernus

**Ruling.** Every combat phase has its own beginning-of-combat step, so Edea takes another creature in each one. Full Throttle adds two combats after the main phase you cast it in. There's no main phase between them, so sorcery-speed sacrifice outlets and Captivating Crew can't be used in between. Full Throttle untaps creatures that attacked this turn at each combat. Karlach adds one combat after the first, only if you attack in the first combat phase.

**Citations**

- Oracle, *Full Throttle*: “After this main phase, there are two additional combat phases.”
- Oracle, *Karlach, Fury of Avernus*: “Whenever you attack, if it's the first combat phase of the turn, untap all attacking creatures.”
- Scryfall ruling, *Full Throttle*: “There is no main phase between the two additional combat phases.”
- Scryfall ruling, *Karlach, Fury of Avernus*: “Notably, the triggered ability of Karlach doesn't give you any additional main phases.”
- [CR 500.8](#cr-5008), [CR 507.1](#cr-5071)
- Source (re-verified): [`Edea_Possessed_Sorceress_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edea_possessed_sorceress_2026-10-14/Edea_Possessed_Sorceress_Rules_Attestation.json) → “Full Throttle and Edea”
- Source (re-verified): [`Edea_Possessed_Sorceress_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edea_possessed_sorceress_2026-10-14/Edea_Possessed_Sorceress_Rules_Attestation.json) → “Karlach additional combat and Edea”

## Trigger ordering

### edea-03: Extra death triggers only draw

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Edea, Possessed Sorceress, Roaming Throne, Strionic Resonator, Gogo, Master of Mimicry

**Ruling.** When one borrowed creature dies and Edea's death ability triggers more than once (Roaming Throne naming Warlock, a Spark Double or Sakashima copy) or is copied (Strionic Resonator, Gogo), only the first instance can return the card. The card is then a new object. Every other instance still draws a card. An extra or copied combat trigger can target a second opposing creature. Gogo copies X times for {X}{X}, X can't be 0, and the copies resolve before the original.

**Citations**

- Scryfall ruling, *Roaming Throne*: “Any choices made as you put the ability onto the stack, such as modes and targets, are made separately for each instance of the ability.”
- Scryfall ruling, *Gogo, Master of Mimicry*: “The copy will resolve before the original ability does.”
- [CR 400.7](#cr-4007), [CR 707.10](#cr-70710), [CR 603.2](#cr-6032)
- Source (re-verified): [`Edea_Possessed_Sorceress_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edea_possessed_sorceress_2026-10-14/Edea_Possessed_Sorceress_Rules_Attestation.json) → “Multiple Edea death triggers for one death”
- Source (re-verified): [`Edea_Possessed_Sorceress_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edea_possessed_sorceress_2026-10-14/Edea_Possessed_Sorceress_Rules_Attestation.json) → “Roaming Throne naming Warlock”
- Source (re-verified): [`Edea_Possessed_Sorceress_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edea_possessed_sorceress_2026-10-14/Edea_Possessed_Sorceress_Rules_Attestation.json) → “Strionic Resonator with Edea”
- Source (re-verified): [`Edea_Possessed_Sorceress_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edea_possessed_sorceress_2026-10-14/Edea_Possessed_Sorceress_Rules_Attestation.json) → “Gogo, Master of Mimicry copying Edea triggers”

### edea-07: Black Crystal vs Edea: order the triggers to keep the card

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Edea, Possessed Sorceress, Chaos Shrine's Black Crystal

**Ruling.** When a borrowed nontoken creature dies, Black Crystal (exile it) and Edea (return it, draw) both trigger, and you order them. Put Black Crystal on top: it exiles the card, Edea can't find it but still draws, and on a later upkeep you can put that opponent's card onto the battlefield under your control with a finality counter. Put Edea on top to give the creature back.

**Citations**

- Oracle, *Chaos Shrine's Black Crystal*: “At the beginning of your upkeep, you may put a creature card exiled with Chaos Shrine's Black Crystal onto the battlefield under your control with a finality counter on it.”
- Scryfall ruling, *Chaos Shrine's Black Crystal*: “Finality counters work on any permanent, not only creatures. If a permanent with a finality counter on it would be put into a graveyard from the battlefield, exile it instead.”
- [CR 603.3b](#cr-6033b), [CR 400.7](#cr-4007), [CR 122.1](#cr-1221)
- Source (re-verified): [`Edea_Possessed_Sorceress_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edea_possessed_sorceress_2026-10-14/Edea_Possessed_Sorceress_Rules_Attestation.json) → “Chaos Shrine's Black Crystal and Edea”

### edea-08: Nightmare Shepherd first gives you a 1/1 copy

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Edea, Possessed Sorceress, Nightmare Shepherd

**Ruling.** If Nightmare Shepherd's trigger resolves first, you may exile the borrowed creature and get a 1/1 Nightmare token copy that you own. Edea then can't return the card, but you still draw. The token copies the creature as it last existed on the battlefield.

**Citations**

- Oracle, *Nightmare Shepherd*: “Whenever another nontoken creature you control dies, you may exile it. If you do, create a token that's a copy of that creature, except it's 1/1 and it's a Nightmare in addition to its other types.”
- Scryfall ruling, *Nightmare Shepherd*: “The token copies the creature as it last existed on the battlefield before it died, not as it existed in the graveyard before it was exiled.”
- [CR 603.3b](#cr-6033b), [CR 111.2](#cr-1112), [CR 707.2](#cr-7072)
- Source (re-verified): [`Edea_Possessed_Sorceress_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edea_possessed_sorceress_2026-10-14/Edea_Possessed_Sorceress_Rules_Attestation.json) → “Nightmare Shepherd and Edea”

## Zones, commander tax and the command zone

### edea-06: Thassa turns a temporary steal into a permanent one

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Edea, Possessed Sorceress, Thassa, Deep-Dwelling

**Ruling.** You still control the borrowed creature during your end step, because 'until end of turn' effects end in cleanup. Thassa can blink it: it returns under your control as a new object, unaffected by Edea's expiring effect. You keep it indefinitely, until another effect changes control or its owner leaves the game.

**Citations**

- Oracle, *Thassa, Deep-Dwelling*: “At the beginning of your end step, exile up to one other target creature you control, then return that card to the battlefield under your control.”
- Scryfall ruling, *Thassa, Deep-Dwelling*: “If you gain control of a creature “until end of turn,” you’ll control it during your end step.”
- [CR 514.2](#cr-5142), [CR 400.7](#cr-4007), [CR 800.4a](#cr-8004a)
- Source (re-verified): [`Edea_Possessed_Sorceress_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edea_possessed_sorceress_2026-10-14/Edea_Possessed_Sorceress_Rules_Attestation.json) → “Thassa, Deep-Dwelling permanently retains an Edea-borrowed creature”

## What the list depends on

### edea-11: Cut cards: Garland and Marchesa

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Edea, Possessed Sorceress

**Ruling.** Two source decisions are re-checked. Garland, Royal Kidnapper (cut) stops you from sacrificing any creature you control but don't own, which shuts off Edea's sacrifice plan. Marchesa, the Black Rose (cut) is unreliable here: Edea's mandatory trigger returns the card to its owner before Marchesa's delayed return, and once the card leaves the graveyard Marchesa can't return it. Neither card is in the current list. Both cuts are correct.

**Citations**

- Oracle, *Edea, Possessed Sorceress*: “Whenever a creature you control but don't own dies, return it to the battlefield under its owner's control and you draw a card.”
- [CR 701.21a](#cr-70121a), [CR 400.7](#cr-4007)
- Source (re-verified): [`Edea_Possessed_Sorceress_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edea_possessed_sorceress_2026-10-14/Edea_Possessed_Sorceress_Rules_Attestation.json) → “Garland, Royal Kidnapper anti-synergy”
- Source (re-verified): [`Edea_Possessed_Sorceress_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/edea_possessed_sorceress_2026-10-14/Edea_Possessed_Sorceress_Rules_Attestation.json) → “Marchesa, the Black Rose does not cleanly retain Edea's borrowed dead creature”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 108.3

The owner of a card in the game is the player who started the game with it in their deck. If a card is brought into the game from outside the game rather than starting in a player’s deck, its owner is the player who brought it into the game. If a card starts the game in the command zone, its owner is the player who put it into the command zone to start the game. Legal ownership of a card in the game is irrelevant to the game rules except for the rules for ante. (See rule 407.)

#### CR 111.2

The player who creates a token is its owner. The token enters the battlefield under that player’s control.

#### CR 115.1

Some spells and abilities require their controller to choose one or more targets for them. The targets are object(s) and/or player(s) the spell or ability will affect. These targets are declared as part of the process of putting the spell or ability on the stack. The targets can’t be changed except by another spell or ability that explicitly says it can do so.

#### CR 122.1

A counter is a marker placed on an object or player that modifies its characteristics and/or interacts with a rule, ability, or effect. Counters are not objects and have no characteristics. Notably, a counter is not a token, and a token is not a counter. Counters with the same name or description are interchangeable.

#### CR 307.1

A player who has priority may cast a sorcery card from their hand during a main phase of their turn when the stack is empty. Casting a sorcery as a spell uses the stack. (See rule 601, “Casting Spells.”)

#### CR 400.7

An object that moves from one zone to another becomes a new object with no memory of, or relation to, its previous existence. This rule has the following exceptions.

#### CR 500.8

Some effects can add phases to a turn. They do this by adding the phases directly after the specified phase. If multiple extra phases are created after the same phase, the most recently created phase will occur first.

#### CR 507.1

First, if the game being played is a multiplayer game in which the active player’s opponents don’t all automatically become defending players, the active player chooses one of their opponents. That player becomes the defending player. This turn-based action doesn’t use the stack. (See rule 506.2.)

#### CR 514.2

Second, the following actions happen simultaneously: all damage marked on permanents (including phased-out permanents) is removed and all “until end of turn” and “this turn” effects end. This turn-based action doesn’t use the stack.

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 603.3a

A triggered ability is controlled by the player who controlled its source at the time it triggered, unless it’s a delayed triggered ability. To determine the controller of a delayed triggered ability, see rules 603.7d–f.

#### CR 603.3b

If multiple abilities have triggered since the last time a player received priority, the abilities are placed on the stack in a two-part process. First, each player, in APNAP order, puts each triggered ability they control with a trigger condition that isn’t another ability triggering on the stack in any order they choose. (See rule 101.4.) Second, each player, in APNAP order, puts all remaining triggered abilities they control on the stack in any order they choose. Then the game once again checks for and performs state-based actions until none are performed, then abilities that triggered …

#### CR 608.2b

If the spell or ability specifies targets, it checks whether the targets are still legal. A target that’s no longer in the zone it was in when it was targeted is illegal. Other changes to the game state may cause a target to no longer be legal; for example, its characteristics may have changed or an effect may have changed the text of the spell. If the source of an ability has left the zone it was in, its last known information is used during this process. If all its targets, for every instance of the word “target,” are now illegal, the spell or ability doesn’t resolve. It’s removed from the …

#### CR 700.4

The term dies means “is put into a graveyard from the battlefield.”

#### CR 701.8a

To destroy a permanent, move it from the battlefield to its owner’s graveyard.

#### CR 701.21a

To sacrifice a permanent, its controller moves it from the battlefield directly to its owner’s graveyard. A player can’t sacrifice something that isn’t a permanent, or something that’s a permanent they don’t control. Sacrificing a permanent doesn’t destroy it, so regeneration or other effects that replace destruction can’t affect this action.

#### CR 702.11a

Hexproof is a static ability.

#### CR 704.5j

If two or more legendary permanents with the same name are controlled by the same player, that player chooses one of them, and the rest are put into their owners’ graveyards. This is called the “legend rule.”

#### CR 707.2

When copying an object, the copy acquires the copiable values of the original object’s characteristics and, for an object on the stack, choices made when casting or activating it (mode, targets, the value of X, whether it was kicked, how it will affect multiple targets, and so on). The copiable values are the values derived from the text printed on the object (that text being name, mana cost, color indicator, card type, subtype, supertype, rules text, power, toughness, and/or loyalty), as modified by other copy effects, by its face-down status, and by “as . . . enters” and “as . . . is turned …

#### CR 707.10

To copy a spell, activated ability, or triggered ability means to put a copy of it onto the stack; a copy of a spell isn’t cast and a copy of an activated ability isn’t activated. A copy of a spell or ability copies both the characteristics of the spell or ability and all decisions made for it, including modes, targets, the value of X, and additional or alternative costs. (See rule 601, “Casting Spells.”) Choices that are normally made on resolution are not copied. If an effect of the copy refers to objects used to pay its costs, it uses the objects used to pay the costs of the original spell …

#### CR 800.4a

When a player leaves the game, all objects (see rule 109) owned by that player leave the game and any effects which give that player control of any objects or players end. Then, if that player controlled any objects on the stack not represented by cards, those objects cease to exist. Then, if there are any objects still controlled by that player, those objects are exiled. This is not a state-based action. It happens as soon as the player leaves the game. If the player who left the game had priority at the time they left, priority passes to the next player in turn order who’s still in the game.

