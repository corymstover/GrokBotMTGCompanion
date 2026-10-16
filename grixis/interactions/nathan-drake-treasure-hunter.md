---
title: "Nathan Drake, Treasure Hunter — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Nathan Drake, Treasure Hunter — Interaction Review

> Bot cycle 51 · batch D · reviewed 2026-10-16. Deck: [Nathan Drake, Treasure Hunter](../decks/nathan-drake-treasure-hunter.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/nathan-drake-treasure-hunter.txt`](../../exports/grixis-archidekt/nathan-drake-treasure-hunter.txt) · SHA-256 `112b792ce420b422a35d9d9f301cd826a4ca46b50f5c25736683eb80c6160698` |
| Rulings | **8** (7 verified · 0 uncertain · 1 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`Nathan_Drake_Treasure_Hunter_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nathan_Drake_Treasure_Hunter_Approval_Ready_Verification_2026-10-15.md) (Approval-ready verification; rules sections 5–12 re-checked against Oracle, rulings and CR) |

## Contents
- [Summary](#summary)
- [Flags and open questions](#flags-and-open-questions)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Engines and payoffs](#engines-and-payoffs)
- [Timing and priority](#timing-and-priority)
- [Trigger ordering](#trigger-ordering)
- [What the list depends on](#what-the-list-depends-on)
- [Rules cited](#rules-cited)

## Summary

Each Nathan attack exiles every player's top card and lets you cast one of them during the trigger. His mana fixing covers only spells you don't own. The list adds more triggers (Roaming Throne on Rogue, Firebender Ascension, Karlach), pays with firebending (Fire Nation Palace, Azula), and rewards casting from exile or casting stolen spells (Wild-Magic Sorcerer, Nalfeshnee, Gonti, Tasha, Don Andres). No Spellbook lines.

Rules surprises: your own top card is exiled for good if you don't cast it; Passionate Archaeologist works on Nathan from the 99; Azula's copies don't trigger the stolen-spell payoffs. One flag: Dauthi Voidwalker starves Tinybones.

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [nathan-07](#nathan-07-dauthi-voidwalker-starves-tinybones) | 🚩 list flag (anti-synergy) | Dauthi Voidwalker starves Tinybones | Dauthi Voidwalker's replacement keeps opponents' graveyards empty, turning off Tinybones' combat-damage cast. |

## Commander rules text and edge cases

### nathan-01: Attack trigger: one spell from the exiled tops, cast during resolution; the rest stay exiled

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Nathan Drake, Treasure Hunter, Etali, Primal Storm

**Ruling.** When Nathan attacks, the top card of every library, yours included, is exiled. While the trigger resolves, you may cast one spell from among them. You cast it during the resolution, so card-type timing is ignored. Sorceries and creatures work in combat, and the spell goes on the stack above the rest of the trigger. You still pay its costs. Lands can't be chosen. Cards you don't cast stay exiled for good, so this also exiles your own top card. Etali, Primal Storm works the same way, but casts any number free. Its rulings cover the timing.

**Citations**

- Oracle, *Nathan Drake, Treasure Hunter*: “Whenever Nathan Drake attacks, exile the top card of each player's library. You may cast a spell from among those cards.”
- Scryfall ruling, *Etali, Primal Storm*: “If you cast any of the exiled cards, you do so as part of the resolution of the triggered ability. You can't wait to cast them later in the turn. Timing permissions based on a card's type are ignored, and the spells resolve before blockers are declared.”
- Scryfall ruling, *Etali, Primal Storm*: “Any cards not cast, including land cards, remain in exile. They can't be cast on later turns, even if Etali attacks again.”
- [CR 608.2g](#cr-6082g), [CR 601.2](#cr-6012)
- Source (re-verified): [`Nathan_Drake_Treasure_Hunter_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nathan_Drake_Treasure_Hunter_Approval_Ready_Verification_2026-10-15.md) → “A land exiled by Nathan cannot be chosen as the spell because lands are not spells.”

### nathan-02: Mana fixing covers only spells you don't own and stolen permanents' abilities

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Nathan Drake, Treasure Hunter, Thieving Varmint

**Ruling.** Nathan lets you spend mana as though it were any color, but only for spells you don't own and for abilities of permanents you control but don't own. Your own exiled card gets no fixing, so a {U}{U} card still needs blue. Thieving Varmint's mana works the same way: only for spells you don't own. Like all "as though any color" effects, this changes how you pay, not the cost.

**Citations**

- Oracle, *Nathan Drake, Treasure Hunter*: “You may spend mana as though it were mana of any color to cast spells you don't own or to activate abilities of permanents you control but don't own.”
- Oracle, *Thieving Varmint*: “{T}, Pay 1 life: Add two mana of any one color. Spend this mana only to cast spells you don't own.”
- [CR 609.4b](#cr-6094b), [CR 601.2g](#cr-6012g)
- Source (re-verified): [`Nathan_Drake_Treasure_Hunter_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nathan_Drake_Treasure_Hunter_Approval_Ready_Verification_2026-10-15.md) → “it does not turn the controller's own exiled top card into a five-color spell.”

## Engines and payoffs

### nathan-04: More Nathan triggers: Roaming Throne (Rogue), Firebender Ascension, Karlach

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Nathan Drake, Treasure Hunter, Roaming Throne, Firebender Ascension, Karlach, Fury of Avernus

**Ruling.** Three ways to get more Nathan triggers:
- **Roaming Throne:** name Rogue (Nathan is a Human Rogue) and his attack trigger triggers twice. Each instance exiles its own set of top cards and allows one cast.
- **Firebender Ascension:** gets a quest counter whenever an attacking creature's own trigger fires, such as Nathan's or the Soldier's firebending. At 4+ counters it copies the trigger. The copy goes above the original and resolves first.
- **Karlach:** if you attack in the first combat, attackers untap, gain first strike, and you get one more combat in which Nathan attacks again. There's no extra main phase in between.

**Citations**

- Oracle, *Roaming Throne*: “If a triggered ability of another creature you control of the chosen type triggers, it triggers an additional time.”
- Oracle, *Karlach, Fury of Avernus*: “Whenever you attack, if it's the first combat phase of the turn, untap all attacking creatures. They gain first strike until end of turn. After this phase, there is an additional combat phase.”
- Scryfall ruling, *Firebender Ascension*: “Firebender Ascension's ability will always go on the stack on top of the triggered ability that caused it to trigger. The copy it creates will be created on the stack on top of the original triggered ability and the copy will resolve before that ability.”
- Scryfall ruling, *Karlach, Fury of Avernus*: “Notably, the triggered ability of Karlach doesn't give you any additional main phases. This means that you will move directly from the end of combat step of one combat phase to the beginning of combat step of the next one.”
- [CR 603.2](#cr-6032), [CR 707.10](#cr-70710), [CR 500.8](#cr-5008)
- Source (re-verified): [`Nathan_Drake_Treasure_Hunter_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nathan_Drake_Treasure_Hunter_Approval_Ready_Verification_2026-10-15.md) → “Choosing **Rogue** includes Nathan Drake, whose type line is Human Rogue.”

### nathan-05: Cast-from-exile payoffs: Wild-Magic Sorcerer, Nalfeshnee, Passionate Archaeologist, Interdimensional Web Watch

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Nathan Drake, Treasure Hunter, Wild-Magic Sorcerer, Nalfeshnee, Passionate Archaeologist, Interdimensional Web Watch

**Ruling.** Nathan's casts come from exile, so these all trigger:
- **Wild-Magic Sorcerer:** the first spell you cast from exile each turn has cascade. Cascade digs your own library, and its free spell resolves first.
- **Nalfeshnee:** copies each spell cast from exile. A permanent copy gets haste and is sacrificed at end step.
- **Passionate Archaeologist:** a Background, but it works from the 99. It gives commander creatures you own (Nathan) "whenever you cast a spell from exile, deal damage equal to its mana value to target opponent".
- **Interdimensional Web Watch:** its mana can only be spent on spells from exile.

**Citations**

- Oracle, *Wild-Magic Sorcerer*: “The first spell you cast from exile each turn has cascade. (When you cast your first spell from exile, exile cards from the top of your library until you exile a nonland card that costs less. You may cast it without paying its mana cost. Put the exiled cards on the bottom in a random order.)”
- Oracle, *Passionate Archaeologist*: “Commander creatures you own have "Whenever you cast a spell from exile, this creature deals damage equal to that spell's mana value to target opponent."”
- Scryfall ruling, *Wild-Magic Sorcerer*: “The first spell you cast from exile each turn will have cascade, even if it's not the first spell you've cast that turn.”
- [CR 702.85a](#cr-70285a), [CR 707.10](#cr-70710)

### nathan-06: Spells-you-don't-own payoffs: Gonti, Tasha, Vaan, Don Andres

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Nathan Drake, Treasure Hunter, Gonti, Night Minister, Tasha, the Witch Queen, Vaan, Street Thief, Don Andres, the Renegade

**Ruling.** These trigger when you cast a stolen card:
- **Gonti, Night Minister:** a Treasure.
- **Tasha:** a 3/3 Demon.
- **Vaan:** +1/+1 counters on your Scouts, Pirates and Rogues.
- **Don Andres:** two tapped Treasures, but only for noncreature spells. He also gives stolen creatures +2/+2, menace and deathtouch.

Your own exiled top card doesn't count for any of them. Azula's copies of stolen spells don't trigger them either, because copies aren't cast.

**Citations**

- Oracle, *Gonti, Night Minister*: “Whenever a player casts a spell they don't own, that player creates a Treasure token.”
- Oracle, *Don Andres, the Renegade*: “Whenever you cast a noncreature spell you don't own, create two tapped Treasure tokens.”
- [CR 108.3](#cr-1083), [CR 707.10](#cr-70710)

## Timing and priority

### nathan-08: Haste and evasion: Arena of Glory, Shizo, Brotherhood Regalia

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Nathan Drake, Treasure Hunter, Arena of Glory, Shizo, Death's Storehouse, Brotherhood Regalia

**Ruling.** Nathan triggers on attack, so damage isn't needed, but he's only a 3/2 first striker:
- **Arena of Glory:** pay {R}, then tap and exert it for {R}{R}. If that mana is spent on Nathan, he has haste the turn he's cast. It enters untapped only if you control a Mountain.
- **Shizo:** {B},{T} gives a legendary creature fear.
- **Brotherhood Regalia:** equip legendary {1}. The creature is unblockable and has ward {2}.

**Citations**

- Oracle, *Brotherhood Regalia*: “Equipped creature has ward {2}, is an Assassin in addition to its other types, and can't be blocked.”
- Oracle, *Arena of Glory*: “{R}, {T}, Exert this land: Add {R}{R}. If any of that mana is spent on a creature spell, it gains haste until end of turn.”
- [CR 702.10b](#cr-70210b), [CR 302.6](#cr-3026)
- Source (re-verified): [`Nathan_Drake_Treasure_Hunter_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nathan_Drake_Treasure_Hunter_Approval_Ready_Verification_2026-10-15.md) → “When Arena mana is spent on Nathan, Nathan can gain haste and attack immediately”

## Trigger ordering

### nathan-03: Firebending first: Fire Nation Palace and Fire Lord Azula pay for the stolen spell

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Nathan Drake, Treasure Hunter, Fire Nation Palace, Fire Lord Azula, Firebender Ascension

**Ruling.** Firebending triggers when its creature attacks, just like Nathan's ability. Put the firebending trigger on top so its {R} resolves first and stays until end of combat. Then spend it on the spell Nathan lets you cast, as any color if you don't own the spell.
- **Fire Nation Palace:** {1}{R},{T} gives Nathan firebending 4 before combat. It enters untapped only if you control a basic land.
- **Fire Lord Azula:** if she's attacking too, she copies the stolen spell. The copy isn't cast, so cast triggers don't fire again, and a permanent spell's copy becomes a token.

**Citations**

- Oracle, *Fire Nation Palace*: “{1}{R}, {T}: Target creature you control gains firebending 4 until end of turn. (Whenever it attacks, add {R}{R}{R}{R}. This mana lasts until end of combat.)”
- Oracle, *Fire Lord Azula*: “Whenever you cast a spell while Fire Lord Azula is attacking, copy that spell. You may choose new targets for the copy. (A copy of a permanent spell becomes a token.)”
- Scryfall ruling, *Fire Lord Azula*: “The copy is created on the stack, so it's not "cast." Abilities that trigger when a player casts a spell won't trigger.”
- Scryfall ruling, *Fire Lord Azula*: “Mana from firebending abilities isn't lost until you leave combat and go to your second main phase. It can be used at any time during combat, even after combat damage has been dealt.”
- [CR 603.3b](#cr-6033b), [CR 702.189a](#cr-702189a), [CR 707.10](#cr-70710)
- Source (re-verified): [`Nathan_Drake_Treasure_Hunter_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nathan_Drake_Treasure_Hunter_Approval_Ready_Verification_2026-10-15.md) → “The controller can put the firebending trigger above Nathan's trigger, resolve it for four red mana, and then use that mana on an eligible spell cast during Nathan's resolving trigger.”

## What the list depends on

### nathan-07: Dauthi Voidwalker starves Tinybones

**Status:** 🚩 list flag · **Evidence:** fact · **Cards:** Nathan Drake, Treasure Hunter, Dauthi Voidwalker, Tinybones, the Pickpocket

**Ruling.** Dauthi Voidwalker exiles, with a void counter, any card that would go to an opponent's graveyard. Tinybones casts nonland permanent cards from an opponent's graveyard, so with Voidwalker out it has nothing to take. Voidwalker can sacrifice itself to play one void card free, which partly makes up for it. Don't plan on both at once.

**List flag (anti-synergy).** Dauthi Voidwalker's replacement keeps opponents' graveyards empty, turning off Tinybones' combat-damage cast.

**Citations**

- Oracle, *Dauthi Voidwalker*: “If a card would be put into an opponent's graveyard from anywhere, instead exile it with a void counter on it.”
- Oracle, *Tinybones, the Pickpocket*: “Whenever Tinybones deals combat damage to a player, you may cast target nonland permanent card from that player's graveyard, and mana of any type can be spent to cast that spell.”
- [CR 614.1a](#cr-6141a), [CR 614.6](#cr-6146)

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 108.3

The owner of a card in the game is the player who started the game with it in their deck. If a card is brought into the game from outside the game rather than starting in a player’s deck, its owner is the player who brought it into the game. If a card starts the game in the command zone, its owner is the player who put it into the command zone to start the game. Legal ownership of a card in the game is irrelevant to the game rules except for the rules for ante. (See rule 407.)

#### CR 302.6

A creature’s activated ability with the tap symbol or the untap symbol in its activation cost can’t be activated unless the creature has been under its controller’s control continuously since their most recent turn began. A creature can’t attack unless it has been under its controller’s control continuously since their most recent turn began. This rule is informally called the “summoning sickness” rule.

#### CR 500.8

Some effects can add phases to a turn. They do this by adding the phases directly after the specified phase. If multiple extra phases are created after the same phase, the most recently created phase will occur first.

#### CR 601.2

To cast a spell is to take it from where it is (usually the hand), put it on the stack, and pay its costs, so that it will eventually resolve and have its effect. Casting a spell includes proposal of the spell (rules 601.2a–d) and determination and payment of costs (rules 601.2f–h). To cast a spell, a player follows the steps listed below, in order. A player must be legally allowed to cast the spell to begin this process (see rule 601.3). If a player is unable to comply with the requirements of a step listed below while performing that step, the casting of the spell is illegal; the game …

#### CR 601.2g

If the total cost includes a mana payment, the player then has a chance to activate mana abilities (see rule 605, “Mana Abilities”). Mana abilities must be activated before costs are paid.

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 603.3b

If multiple abilities have triggered since the last time a player received priority, the abilities are placed on the stack in a two-part process. First, each player, in APNAP order, puts each triggered ability they control with a trigger condition that isn’t another ability triggering on the stack in any order they choose. (See rule 101.4.) Second, each player, in APNAP order, puts all remaining triggered abilities they control on the stack in any order they choose. Then the game once again checks for and performs state-based actions until none are performed, then abilities that triggered …

#### CR 608.2g

If an effect gives a player the option to pay mana, they may activate mana abilities before taking that action. If an effect specifically instructs or allows a player to cast a spell during resolution, they do so by following the steps in rules 601.2a–i, except no player receives priority after it’s cast. That spell becomes the topmost object on the stack, and the currently resolving spell or ability continues to resolve, which may include casting other spells this way. No other spells can normally be cast and no other abilities can normally be activated during resolution.

#### CR 609.4b

If an effect allows a player to spend mana “as though it were mana of any [type or color],” this affects only how the player may pay a cost. It doesn’t change that cost, and it doesn’t change what mana was actually spent to pay that cost. The same is true for effects that say “mana of any type can be spent.”

#### CR 614.1a

Effects that use the word “instead” are replacement effects. Most replacement effects use the word “instead” to indicate what events will be replaced with other events.

#### CR 614.6

If an event is replaced, it never happens. A modified event occurs instead, which may in turn trigger abilities. Note that the modified event may contain instructions that can’t be carried out, in which case the impossible instruction is simply ignored.

#### CR 702.10b

If a creature has haste, it can attack even if it hasn’t been controlled by its controller continuously since their most recent turn began. (See rule 302.6.)

#### CR 702.85a

Cascade is a triggered ability that functions only while the spell with cascade is on the stack. “Cascade” means “When you cast this spell, exile cards from the top of your library until you exile a nonland card whose mana value is less than this spell’s mana value. You may cast that card without paying its mana cost if the resulting spell’s mana value is less than this spell’s mana value. Then put all cards exiled this way that weren’t cast on the bottom of your library in a random order.”

#### CR 702.189a

Firebending is a triggered ability. “Firebending N” means “Whenever this creature attacks, add N {R}. Until end of combat, you don’t lose this mana as steps and phases end.”

#### CR 707.10

To copy a spell, activated ability, or triggered ability means to put a copy of it onto the stack; a copy of a spell isn’t cast and a copy of an activated ability isn’t activated. A copy of a spell or ability copies both the characteristics of the spell or ability and all decisions made for it, including modes, targets, the value of X, and additional or alternative costs. (See rule 601, “Casting Spells.”) Choices that are normally made on resolution are not copied. If an effect of the copy refers to objects used to pay its costs, it uses the objects used to pay the costs of the original spell …

