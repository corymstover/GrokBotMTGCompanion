---
title: "Cormela, Glamour Thief — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Cormela, Glamour Thief — Interaction Review

> Bot cycle 46 · batch A · reviewed 2026-10-16. Deck: [Cormela, Glamour Thief](../decks/cormela-glamour-thief.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/cormela-glamour-thief.txt`](../../exports/grixis-archidekt/cormela-glamour-thief.txt) · SHA-256 `29dad7ed42b4c5b81bb507f96d3638c6dbe8f509f6d8e8f935f25df484930578` |
| Rulings | **10** (10 verified · 0 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`Cormela_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Rules_Attestation.json) (8 interactions, all PASS) |

## Contents
- [Summary](#summary)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Key card-pair interactions](#key-card-pair-interactions)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [Rules cited](#rules-cited)

## Summary

Cormela, Glamour Thief is a cEDH-style instant/sorcery combo deck. This review re-verifies all eight items of the deck's rules attestation (Saw in Half, Goryo's, Shallow Grave, Birgi + Molten Duplication, Dualcaster, Thassa's Oracle lines, restricted mana) against current Oracle text and the CR.

Rules point: when Cormela dies, decline the command-zone move to keep the reanimation loops going. No list errors.

## Commander rules text and edge cases

### cormela-01: Restricted mana and the death trigger

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Cormela, Glamour Thief

**Ruling.** Cormela has haste, so her {1}, {T}: add {U}{B}{R} works the turn she arrives, including on token copies. That mana can only be spent to cast instants and sorceries: not creatures (Dualcaster Mage, Thassa's Oracle), not activated abilities, not artifacts. When Cormela dies, she returns up to one instant or sorcery card from your graveyard to hand. The spell that killed her is already in the graveyard by the time the trigger targets, so she can return it.

**Citations**

- Oracle, *Cormela, Glamour Thief*: “{1}, {T}: Add {U}{B}{R}. Spend this mana only to cast instant and/or sorcery spells.”
- Oracle, *Cormela, Glamour Thief*: “When Cormela dies, return up to one target instant or sorcery card from your graveyard to your hand.”
- [CR 106.6](#cr-1066), [CR 608.2n](#cr-6082n), [CR 603.10a](#cr-60310a)
- Source (re-verified): [`Cormela_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Rules_Attestation.json) → “Cormela restricted mana”

## Combos and engine lines

### cormela-03: Cormela + Saw in Half (+ ritual or Jeska's Will)

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Cormela, Glamour Thief, Saw in Half, Dark Ritual, Cabal Ritual, Seething Song, Jeska's Will

**Ruling.** Saw in Half destroys Cormela and makes two token Cormelas. The legend rule puts one into the graveyard: it 'dies' and triggers its own copy of the death ability. The original's trigger returns Saw in Half; the token's returns the ritual. The surviving token has haste and taps for {U}{B}{R}.

For example, with Dark Ritual a loop costs 5 (Saw {2}{B}, Ritual {B}, Cormela's {1}) and gives 6, net +1 each time. Tokens of tokens copy the original token's characteristics.

**Citations**

- Oracle, *Saw in Half*: “Destroy target creature. If that creature dies this way, its controller creates two tokens that are copies of that creature”
- Scryfall ruling, *Saw in Half*: “If the copied creature was a token, the new tokens copy the original characteristics of that token as stated by the effect that created the token, with the listed exceptions.”
- [CR 704.5j](#cr-7045j), [CR 608.2n](#cr-6082n), [CR 707.2](#cr-7072)
- Source (re-verified): [`Cormela_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Rules_Attestation.json) → “Cormela + Saw in Half recursion engine”

### cormela-04: Cormela + Goryo's Vengeance or Shallow Grave + altar

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Cormela, Glamour Thief, Goryo's Vengeance, Shallow Grave, Ashnod's Altar, Phyrexian Altar

**Ruling.** Reanimate Cormela (Goryo's: a legendary creature card; Shallow Grave: the top creature card). Tap her for {U}{B}{R}, then sacrifice her to an altar. Her death trigger returns the reanimation spell, which you recast with the restricted mana. The end-step exile doesn't matter because she has already left; Goryo's ruling confirms she stays in the graveyard.

**Citations**

- Oracle, *Goryo's Vengeance*: “Return target legendary creature card from your graveyard to the battlefield. That creature gains haste.”
- Scryfall ruling, *Goryo's Vengeance*: “If the returned creature leaves the battlefield before the end step, it will remain in its current zone. It won't be exiled.”
- [CR 605.1a](#cr-6051a), [CR 903.9a](#cr-9039a)
- Source (re-verified): [`Cormela_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Rules_Attestation.json) → “Cormela + Goryo's Vengeance + Ashnod's Altar / Phyrexian Altar”
- Source (re-verified): [`Cormela_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Rules_Attestation.json) → “Cormela + Shallow Grave + Ashnod's Altar / Phyrexian Altar”

### cormela-05: Demonic Gifts loops (Cormela or Dualcaster + altar)

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Cormela, Glamour Thief, Demonic Gifts, Dualcaster Mage, Ashnod's Altar, Phyrexian Altar

**Ruling.** - **With Cormela:** Demonic Gifts gives her 'when this dies, return it'. Sacrifice her to an altar: she returns as a new object (Gifts works only once), and her death trigger returns Gifts to recast.
- **With Dualcaster:** cast Gifts, respond with Dualcaster copying it onto itself, then sacrifice. The returned Dualcaster copies the original Gifts, still on the stack, again.

**Citations**

- Oracle, *Demonic Gifts*: “Until end of turn, target creature gets +2/+0 and gains "When this creature dies, return it to the battlefield under its owner's control."”
- Scryfall ruling, *Demonic Gifts*: “The reanimating effect of Demonic Gifts works only once. Once the creature dies and returns to the battlefield, it’s a new object with no relation to the creature it was.”
- [CR 400.7](#cr-4007), [CR 707.10c](#cr-70710c)

### cormela-06: Birgi + Molten Duplication; Dualcaster + Molten Duplication or Saw in Half

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Cormela, Glamour Thief, Birgi, God of Storytelling // Harnfel, Horn of Bounty, Molten Duplication, Dualcaster Mage, Saw in Half

**Ruling.** - **Birgi:** Molten Duplication on Cormela makes a hasty token Cormela. The legend rule sends one to the graveyard, its death trigger returns Duplication, and Birgi adds {R} on each cast.
- **Dualcaster:** responding to Molten Duplication (or Saw in Half) on your creature, Dualcaster copies it targeting the newest Dualcaster. This gives arbitrarily many hasty Dualcaster tokens.

**Citations**

- Oracle, *Birgi, God of Storytelling // Harnfel, Horn of Bounty*: “Whenever you cast a spell, add {R}.”
- [CR 704.5j](#cr-7045j), [CR 707.10c](#cr-70710c)
- Source (re-verified): [`Cormela_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Rules_Attestation.json) → “Cormela + Birgi + Molten Duplication”
- Source (re-verified): [`Cormela_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Rules_Attestation.json) → “Dualcaster Mage + Molten Duplication”

### cormela-07: Thassa's Oracle + Demonic Consultation or Tainted Pact

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Cormela, Glamour Thief, Thassa's Oracle, Demonic Consultation, Tainted Pact

**Ruling.** With Thassa's Oracle's trigger on the stack (or before casting Oracle), Demonic Consultation naming a card not in your library, or Tainted Pact, exiles the library. Oracle then wins with X ≥ 0 cards. Tainted Pact stops on two cards with the same name; the list has no basic lands or duplicates, so it exiles everything. Exiling your library doesn't lose by itself; drawing from it later does.

**Citations**

- Oracle, *Thassa's Oracle*: “If X is greater than or equal to the number of cards in your library, you win the game.”
- Scryfall ruling, *Demonic Consultation*: “If you don't reveal the named card (perhaps because it was in the top six cards of your library), you'll end up exiling your entire library. You don't lose the game at that point, but will lose the next time you're instructed to draw a card.”
- [CR 704.5b](#cr-7045b), [CR 603.4](#cr-6034)
- Source (re-verified): [`Cormela_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Rules_Attestation.json) → “Thassa's Oracle + Demonic Consultation”
- Source (re-verified): [`Cormela_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Rules_Attestation.json) → “Thassa's Oracle + Tainted Pact”

### cormela-08: Underworld Breach + Lion's Eye Diamond / Lotus Petal + Brain Freeze or Wheel

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Cormela, Glamour Thief, Underworld Breach, Lion's Eye Diamond, Lotus Petal, Brain Freeze, Wheel of Fortune, Jeska's Will

**Ruling.** Breach gives escape (mana cost plus exile three other cards). Lion's Eye Diamond has a mana cost of {0}, so it can escape for {0} plus three cards. Its ability is a mana ability usable only at instant speed. Each escape is a cast, so Brain Freeze's storm count grows, and storm counts spells cast from any zone. Breach + Wheel + Jeska's Will refills opponents' hands for Jeska's mana. Breach is sacrificed at end step.

**Citations**

- Oracle, *Lion's Eye Diamond*: “Discard your hand, Sacrifice this artifact: Add three mana of any one color. Activate only as an instant.”
- Scryfall ruling, *Underworld Breach*: “If a card has no mana cost, its escape cost is an unpayable cost, so you can't cast it for that cost.”
- Scryfall ruling, *Brain Freeze*: “Spells cast from zones other than a player's hand and spells that were countered are counted by the storm ability.”
- [CR 702.138a](#cr-702138a), [CR 702.40a](#cr-70240a), [CR 605.1a](#cr-6051a)

## Key card-pair interactions

### cormela-09: Orcish Bowmasters punishes your own wheels

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Cormela, Glamour Thief, Orcish Bowmasters, Wheel of Fortune, Windfall

**Ruling.** Orcish Bowmasters triggers whenever an opponent draws a card other than the first in their draw step. Wheel of Fortune or Windfall makes each opponent draw seven: up to 21 pings and 21 amass in a four-player game. A card put into hand without the word 'draw' doesn't count.

**Citations**

- Oracle, *Orcish Bowmasters*: “whenever an opponent draws a card except the first one they draw in each of their draw steps, this creature deals 1 damage to any target.”
- Scryfall ruling, *Orcish Bowmasters*: “If a spell or ability causes an opponent to put cards into their hand without specifically using the word "draw," it's not a card drawn.”
- [CR 121.1](#cr-1211), [CR 603.2](#cr-6032)

## Zones, commander tax and the command zone

### cormela-02: Leave Cormela in the graveyard for reanimation loops

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Cormela, Glamour Thief, Goryo's Vengeance, Shallow Grave

**Ruling.** When your commander dies it goes to the graveyard, so 'dies' triggers fire. Afterward you *may* move it to the command zone as a state-based action. For Goryo's Vengeance and Shallow Grave loops you must decline, leaving Cormela in the graveyard. Shallow Grave also needs her to be the *top* creature card there.

**Citations**

- Oracle, *Shallow Grave*: “Return the top creature card of your graveyard to the battlefield.”
- [CR 903.9a](#cr-9039a), [CR 704.6d](#cr-7046d)

### cormela-10: Commander tax

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Cormela, Glamour Thief

**Ruling.** Cormela costs {1}{U}{B}{R}, then 6, then 8. Combo lines that sacrifice her repeatedly don't add tax, because she stays in the graveyard. Only casts from the command zone add tax.

**Citations**

- Oracle, *Cormela, Glamour Thief*: “Haste”
- [CR 903.8](#cr-9038)

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 106.6

Some spells or abilities that produce mana restrict how that mana can be spent, have an additional effect that affects the spell or ability that mana is spent on, or create a delayed triggered ability (see rule 603.7a) that triggers when that mana is spent. This doesn’t affect the mana’s type.

#### CR 121.1

A player draws a card by putting the top card of their library into their hand. This is done as a turn-based action during each player’s draw step. It may also be done as part of a cost or effect of a spell or ability.

#### CR 400.7

An object that moves from one zone to another becomes a new object with no memory of, or relation to, its previous existence. This rule has the following exceptions.

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 603.4

A triggered ability may read “When/Whenever/At [trigger event], if [condition], [effect].” When the trigger event occurs, the ability checks whether the stated condition is true. The ability triggers only if it is; otherwise it does nothing. If the ability triggers, it checks the stated condition again as it resolves. If the condition isn’t true at that time, the ability is removed from the stack and does nothing. Note that this mirrors the check for legal targets. This rule is referred to as the “intervening ‘if’ clause” rule. (The word “if” has only its normal English meaning anywhere else …

#### CR 603.10a

Some zone-change triggers look back in time. These are leaves-the-battlefield abilities, abilities that trigger when a player sacrifices a permanent, abilities that trigger when a card leaves a graveyard, and abilities that trigger when an object that all players can see is put into a hand or library.

#### CR 605.1a

An activated ability is a mana ability if it meets all of the following criteria: it doesn’t require a target (see rule 115.6), it could add mana to a player’s mana pool when it resolves, it’s not a loyalty ability (see rule 606, “Loyalty Abilities”), and its cost and effect don’t move any card to or from a library. Do not take into account replacement effects that may apply, other than self-replacement effects, when evaluating these criteria.

#### CR 608.2n

As the final part of an instant or sorcery spell’s resolution, the spell is put into its owner’s graveyard. As the final part of an ability’s resolution, the ability is removed from the stack and ceases to exist.

#### CR 702.40a

Storm is a triggered ability that functions on the stack. “Storm” means “When you cast this spell, copy it for each other spell that was cast before it this turn. If the spell has any targets, you may choose new targets for any of the copies.”

#### CR 702.138a

Escape represents a static ability that functions while the card with escape is in a player’s graveyard. “Escape [cost]” means “You may cast this card from your graveyard by paying [cost] rather than paying its mana cost.” Casting a spell using its escape ability follows the rules for paying alternative costs in rules 601.2b and 601.2f–h.

#### CR 704.5b

If a player attempted to draw a card from a library with no cards in it since the last time state-based actions were checked, that player loses the game.

#### CR 704.5j

If two or more legendary permanents with the same name are controlled by the same player, that player chooses one of them, and the rest are put into their owners’ graveyards. This is called the “legend rule.”

#### CR 704.6d

In a Commander game, if a commander is in a graveyard or in exile and that object was put into that zone since the last time state-based actions were checked, its owner may put it into the command zone. See rule 903, “Commander.”

#### CR 707.2

When copying an object, the copy acquires the copiable values of the original object’s characteristics and, for an object on the stack, choices made when casting or activating it (mode, targets, the value of X, whether it was kicked, how it will affect multiple targets, and so on). The copiable values are the values derived from the text printed on the object (that text being name, mana cost, color indicator, card type, subtype, supertype, rules text, power, toughness, and/or loyalty), as modified by other copy effects, by its face-down status, and by “as . . . enters” and “as . . . is turned …

#### CR 707.10c

Some effects copy a spell or ability and state that its controller may choose new targets for the copy. The player may leave any number of the targets unchanged, even if those targets would be illegal. If the player chooses to change some or all of the targets, the new targets must be legal. Once the player has decided what the copy’s targets will be, the copy is put onto the stack with those targets.

#### CR 903.8

A player may cast a commander they own from the command zone. A commander cast from the command zone costs an additional {2} for each previous time the player casting it has cast it from the command zone that game. This additional cost is informally known as the “commander tax.”

#### CR 903.9a

If a commander is in a graveyard or in exile and that object was put into that zone since the last time state-based actions were checked, its owner may put it into the command zone. This is a state-based action. See rule 704.

