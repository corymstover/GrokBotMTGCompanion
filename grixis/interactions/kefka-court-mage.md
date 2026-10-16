---
title: "Kefka, Court Mage // Kefka, Ruler of Ruin — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Kefka, Court Mage // Kefka, Ruler of Ruin — Interaction Review

> Bot cycle 49 · batch C · reviewed 2026-10-16. Deck: [Kefka, Court Mage // Kefka, Ruler of Ruin](../decks/kefka-court-mage.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-15), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Current list | [`exports/grixis-archidekt/kefka-court-mage.txt`](../../exports/grixis-archidekt/kefka-court-mage.txt) · SHA-256 `9388bb55da7655d18604837675e4fcb72ced74414fd184841f2074b7e31d1de0` |
| Rulings | **11** (11 verified · 0 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-15 · rulings 2026-10-15 |
| Source attestations | [`Kefka_Court_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kefka_court_mage_2026-10-14/Kefka_Court_Mage_Rules_Attestation.json) (17 interactions, all PASS (Valley Floodcaller, Cursed Totem and Samut items refer to cards not in the list)) |

## Contents
- [Summary](#summary)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Layers and continuous effects](#layers-and-continuous-effects)
- [Timing and priority](#timing-and-priority)
- [Replacement and prevention effects](#replacement-and-prevention-effects)
- [Trigger ordering](#trigger-ordering)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [Rules cited](#rules-cited)

## Summary

Kefka, Court Mage makes everyone discard on enter and attack, and draws for each card type discarded. For {8} he transforms into Ruler of Ruin, which draws you a card for each point of life opponents lose on your turn. This review re-verifies the attestation. Six Spellbook lines (Oracle, Breach) are confirmed.

Rules surprises: single-faced clones can't transform (CR 701.27c), but Molten Duplication's token can; Saw in Half on your commander still makes tokens; discarding Anger to Kefka's own trigger gives same-turn haste. The attestation's Valley Floodcaller item is about a card that isn't in the current list. No list errors.

## Commander rules text and edge cases

### kefka-01: Discard trigger counts card types, per trigger

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Kefka, Court Mage

**Ruling.** Each enter or attack trigger makes every player discard one card. Then you draw one card for each card type among the cards discarded by that trigger. Separate triggers count separately. Legendary, basic and snow are supertypes and don't count. Kindred and battle are card types.

**Citations**

- Oracle, *Kefka, Court Mage*: “Whenever Kefka enters or attacks, each player discards a card. Then you draw a card for each card type among cards discarded this way.”
- Scryfall ruling, *Kefka, Court Mage*: “The card types in Magic include artifact, battle, creature, enchantment, instant, kindred, land, planeswalker, and sorcery. Legendary, basic, and snow are supertypes, not card types; Hero and Saga are subtypes, not card types.”
- [CR 205.2a](#cr-2052a), [CR 603.2](#cr-6032)
- Source (re-verified): [`Kefka_Court_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kefka_court_mage_2026-10-14/Kefka_Court_Mage_Rules_Attestation.json) → “Kefka front-face enters/attacks trigger”

### kefka-02: {8}: opponents' sacrifice is simultaneous, then Kefka transforms

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Kefka, Court Mage

**Ruling.** Sorcery speed only. In turn order, each opponent chooses a permanent, then all of them are sacrificed at once and Kefka transforms. Ruler of Ruin draws you as many cards as an opponent loses life during your turn. That turns combat damage and Orcish Bowmasters pings into card draw.

**Citations**

- Oracle, *Kefka, Ruler of Ruin*: “Whenever an opponent loses life during your turn, you draw that many cards.”
- Scryfall ruling, *Kefka, Court Mage*: “While resolving Kefka, Court Mage's last ability, the next opponent in turn order chooses a permanent they control, then each other opponent in turn order does the same. Then each of the chosen permanents are sacrificed simultaneously.”
- [CR 701.27a](#cr-70127a), [CR 101.4](#cr-1014)
- Source (re-verified): [`Kefka_Court_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kefka_court_mage_2026-10-14/Kefka_Court_Mage_Rules_Attestation.json) → “Ruler of Ruin transformation and life-loss engine”

## Combos and engine lines

### kefka-11: Oracle and Breach finishes; protection notes

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Kefka, Court Mage, Thassa's Oracle, Demonic Consultation, Tainted Pact, Underworld Breach, Lion's Eye Diamond, Brain Freeze, Hexing Squelcher, Beseech the Mirror

**Ruling.** Standard Oracle lines (100 distinct names) and Breach + LED + Brain Freeze. Hexing Squelcher makes your spells uncounterable but doesn't stop removal. Bargained Beseech casts during its own resolution. That's why Samut, whose split second would block it, isn't in the list.

**Citations**

- [CR 121.4](#cr-1214), [CR 702.138a](#cr-702138a), [CR 608.2g](#cr-6082g)
- Commander Spellbook [742-1295](https://commanderspellbook.com/combo/742-1295/) (community-maintained, retrieved 2026-10-16): “Cast Demonic Consultation by paying {B}, naming Thassa's Oracle and thus exiling your library due to you not having a card named Thassa's Oracle in your library.”
- Commander Spellbook [1368-3518-4856](https://commanderspellbook.com/combo/1368-3518-4856/) (community-maintained, retrieved 2026-10-16): “You have at least six other cards in hand and/or graveyard.”
- Source (re-verified): [`Kefka_Court_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kefka_court_mage_2026-10-14/Kefka_Court_Mage_Rules_Attestation.json) → “Thassa's Oracle plus Demonic Consultation/Tainted Pact”
- Source (re-verified): [`Kefka_Court_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kefka_court_mage_2026-10-14/Kefka_Court_Mage_Rules_Attestation.json) → “Underworld Breach plus Lion's Eye Diamond plus Brain Freeze”
- Source (re-verified): [`Kefka_Court_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kefka_court_mage_2026-10-14/Kefka_Court_Mage_Rules_Attestation.json) → “Hexing Squelcher protection”
- Source (re-verified): [`Kefka_Court_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kefka_court_mage_2026-10-14/Kefka_Court_Mage_Rules_Attestation.json) → “Beseech the Mirror and rejected Samut split-second anti-synergy”

## Layers and continuous effects

### kefka-05: Gogo copies Kefka without the legend rule

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Kefka, Court Mage, Gogo, Mysterious Mime

**Ruling.** Gogo becomes a copy of Kefka but keeps its own name, so the legend rule doesn't apply. Both get +2/+0 and haste and must attack, so you get two attack triggers. Becoming a copy isn't entering, so no enter trigger. Gogo is single-faced, so it can't transform (see kefka-06).

**Citations**

- Scryfall ruling, *Gogo, Mysterious Mime*: “If Gogo copies a legendary creature, Gogo will also be legendary, but because its name remains Gogo, Mysterious Mime, the "legend rule" won't cause either of them to be put into the graveyard.”
- [CR 707.9b](#cr-7079b), [CR 704.5j](#cr-7045j)
- Source (re-verified): [`Kefka_Court_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kefka_court_mage_2026-10-14/Kefka_Court_Mage_Rules_Attestation.json) → “Gogo copying Kefka at beginning of combat”

### kefka-06: Clones of Kefka: Image and Metamorph vs. Molten Duplication

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Kefka, Court Mage, Phantasmal Image, Phyrexian Metamorph, Molten Duplication

**Ruling.** Copying a double-faced permanent copies the face that's up. Phantasmal Image or Phyrexian Metamorph as Kefka gets an enter trigger, then the legend rule leaves one Kefka; the trigger still resolves. A single-faced clone told to transform does nothing. So a clone kept as Kefka can pay {8} for the opponents' sacrifice but stays front-face, and could repeat that on a later turn. A Molten Duplication token of Kefka is a double-faced token, so it could transform. It has haste, so you can keep it over the original, attack with it, and lose it at end step.

**Citations**

- Scryfall ruling, *Kefka, Court Mage*: “A token that is created as a copy of a double-faced permanent or a double-faced card in another zone is a double-faced token. It will have both the front face and back face of whatever object it's copying. If it's copying a double-faced permanent whose back face is up, the token will enter with its back face up. It can transform if instructed to do so.”
- [CR 707.8](#cr-7078), [CR 707.8a](#cr-7078a), [CR 701.27c](#cr-70127c), [CR 704.5j](#cr-7045j)
- Source (re-verified): [`Kefka_Court_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kefka_court_mage_2026-10-14/Kefka_Court_Mage_Rules_Attestation.json) → “Phantasmal Image and Phyrexian Metamorph copying Kefka”
- Source (re-verified): [`Kefka_Court_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kefka_court_mage_2026-10-14/Kefka_Court_Mage_Rules_Attestation.json) → “Molten Duplication on Kefka”

## Timing and priority

### kefka-04: Haste: discard Anger to Kefka's own trigger, or use Arena of Glory

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Kefka, Court Mage, Anger, Arena of Glory

**Ruling.** If you discard Anger to Kefka's enter trigger and control a Mountain-typed land (Badlands, Blood Crypt, Steam Vents, Volcanic Island), Kefka has haste right away and can attack for a second trigger. Exerted Arena of Glory mana spent on Kefka also gives haste.

**Citations**

- Oracle, *Anger*: “As long as this card is in your graveyard and you control a Mountain, creatures you control have haste.”
- Scryfall ruling, *Anger*: “The timestamp for the "in your graveyard" ability is set at the time that this card goes to your graveyard, regardless of whether you control a Mountain at that time.”
- [CR 702.10a](#cr-70210a), [CR 205.3i](#cr-2053i)
- Source (re-verified): [`Kefka_Court_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kefka_court_mage_2026-10-14/Kefka_Court_Mage_Rules_Attestation.json) → “Anger discarded to Kefka grants same-turn haste”
- Source (re-verified): [`Kefka_Court_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kefka_court_mage_2026-10-14/Kefka_Court_Mage_Rules_Attestation.json) → “Arena of Glory grants Kefka haste”

## Replacement and prevention effects

### kefka-10: Demonic Counsel needs delirium to be a full tutor

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Kefka, Court Mage, Demonic Counsel

**Ruling.** Without delirium it only finds a Demon. With four or more card types in your graveyard, it finds any card, with no reveal. Kefka's discards help reach delirium.

**Citations**

- Oracle, *Demonic Counsel*: “Delirium — If there are four or more card types among cards in your graveyard, instead search your library for any card, put it into your hand, then shuffle.”
- Scryfall ruling, *Demonic Counsel*: “In the case where Demonic Counsel's delirium ability allows you to search your library for any card, you won't have to reveal that card. (You could, but as your demonic counsel, I wouldn't advise it.)”
- [CR 207.2c](#cr-2072c), [CR 614.1a](#cr-6141a)
- Source (re-verified): [`Kefka_Court_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kefka_court_mage_2026-10-14/Kefka_Court_Mage_Rules_Attestation.json) → “Demonic Counsel delirium restriction”

## Trigger ordering

### kefka-03: Harmonic Prodigy doubles both faces

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Kefka, Court Mage, Harmonic Prodigy

**Ruling.** Both faces are Wizards, so Harmonic Prodigy doubles the front face's enter/attack trigger and Ruler of Ruin's draw trigger.

**Citations**

- Oracle, *Harmonic Prodigy*: “If a triggered ability of a Shaman or another Wizard you control triggers, that ability triggers an additional time.”
- [CR 603.2](#cr-6032)
- Source (re-verified): [`Kefka_Court_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kefka_court_mage_2026-10-14/Kefka_Court_Mage_Rules_Attestation.json) → “Harmonic Prodigy doubles both Kefka faces”

### kefka-09: Tinybones and Waste Not off Kefka's discards

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Kefka, Court Mage, Tinybones, Bauble Burglar, Waste Not

**Ruling.** Opponents' discards trigger Tinybones (exile with stash) and Waste Not. Those triggers go on the stack after Kefka's trigger finishes. Kefka has already counted the card types, so Tinybones exiling the cards changes nothing.

**Citations**

- Oracle, *Waste Not*: “Whenever an opponent discards a noncreature, nonland card, draw a card.”
- Oracle, *Tinybones, Bauble Burglar*: “Whenever an opponent discards a card, exile it from their graveyard with a stash counter on it.”
- [CR 603.3](#cr-6033), [CR 608.2](#cr-6082)
- Source (re-verified): [`Kefka_Court_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kefka_court_mage_2026-10-14/Kefka_Court_Mage_Rules_Attestation.json) → “Tinybones and Waste Not with Kefka discard”

## Zones, commander tax and the command zone

### kefka-07: Saw in Half on your commander Kefka

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Kefka, Court Mage, Saw in Half

**Ruling.** Kefka really dies; the move to the command zone is a state-based action after Saw in Half resolves. So the dies-this-way condition holds and you get two token Kefkas. Both enter triggers fire, then the legend rule leaves one token. If you use a replacement that sends Kefka elsewhere instead of the graveyard, there are no tokens.

**Citations**

- Scryfall ruling, *Saw in Half*: “If the creature isn't destroyed (perhaps because it has indestructible), its controller doesn't create any tokens. The same is true if the creature is destroyed but instead of going to its owner's graveyard, a replacement effect moves it elsewhere, such as”
- [CR 903.9a](#cr-9039a), [CR 704.5j](#cr-7045j), [CR 603.3](#cr-6033)
- Source (re-verified): [`Kefka_Court_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kefka_court_mage_2026-10-14/Kefka_Court_Mage_Rules_Attestation.json) → “Saw in Half on commander Kefka”

### kefka-08: Blink re-triggers: Essence Flux and Displacer Kitten

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Kefka, Court Mage, Essence Flux, Displacer Kitten

**Ruling.** Exile-and-return makes a new front-face Kefka with a new enter trigger. Kitten does this on every noncreature spell. A transformed Kefka comes back front-face up.

**Citations**

- Scryfall ruling, *Displacer Kitten*: “When the card returns to the battlefield, it will be a new object with no connection to the card that was exiled.”
- [CR 400.7](#cr-4007), [CR 712.14](#cr-71214)
- Source (re-verified): [`Kefka_Court_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kefka_court_mage_2026-10-14/Kefka_Court_Mage_Rules_Attestation.json) → “Essence Flux and Displacer Kitten blink Kefka”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 101.4

If multiple players would make choices and/or take actions at the same time, the active player (the player whose turn it is) makes any choices required, then the next player in turn order (usually the player seated to the active player’s left) makes any choices required, followed by the remaining nonactive players in turn order. Then the actions happen simultaneously. This rule is often referred to as the “Active Player, Nonactive Player (APNAP) order” rule.

#### CR 121.4

A player who attempts to draw a card from a library with no cards in it loses the game the next time a player would receive priority. (This is a state-based action. See rule 704.)

#### CR 205.2a

The card types are artifact, battle, conspiracy, creature, dungeon, enchantment, instant, kindred, land, phenomenon, plane, planeswalker, scheme, sorcery, and vanguard. See section 3, “Card Types.”

#### CR 205.3i

Lands have their own unique set of subtypes; these subtypes are called land types. The land types are Cave, Desert, Forest, Gate, Island, Lair, Locus, Mine, Mountain, Plains, Planet, Power-Plant, Sphere, Swamp, Tower, Town, and Urza’s. Of that list, Forest, Island, Mountain, Plains, and Swamp are the basic land types. See rule 305.6.

#### CR 207.2c

An ability word appears in italics at the beginning of some abilities. Ability words are similar to keywords in that they tie together cards that have similar functionality, but they have no special rules meaning and no individual entries in the Comprehensive Rules. The ability words are adamant, addendum, alliance, battalion, bloodrush, celebration, channel, chroma, cohort, constellation, converge, council’s dilemma, coven, delirium, descend 4, descend 8, disappear, domain, eerie, eminence, enrage, fateful hour, fathomless descent, ferocious, flurry, formidable, grandeur, hellbent, heroic, …

#### CR 400.7

An object that moves from one zone to another becomes a new object with no memory of, or relation to, its previous existence. This rule has the following exceptions.

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 603.3

Once an ability has triggered, its controller puts it on the stack as an object that’s not a card the next time a player would receive priority. See rule 117, “Timing and Priority.” The ability becomes the topmost object on the stack. It has the text of the ability that created it, and no other characteristics. It remains on the stack until it’s countered, it resolves, a rule causes it to be removed from the stack, or an effect moves it elsewhere.

#### CR 608.2

If the object that’s resolving is an instant spell, a sorcery spell, or an ability, its resolution may involve several steps. The steps described in rules 608.2a and 608.2b are followed first. The steps described in rules 608.2c–m are then followed as appropriate, in no specific order. The steps described in rule 608.2n and 608.2p are followed last.

#### CR 608.2g

If an effect gives a player the option to pay mana, they may activate mana abilities before taking that action. If an effect specifically instructs or allows a player to cast a spell during resolution, they do so by following the steps in rules 601.2a–i, except no player receives priority after it’s cast. That spell becomes the topmost object on the stack, and the currently resolving spell or ability continues to resolve, which may include casting other spells this way. No other spells can normally be cast and no other abilities can normally be activated during resolution.

#### CR 614.1a

Effects that use the word “instead” are replacement effects. Most replacement effects use the word “instead” to indicate what events will be replaced with other events.

#### CR 701.27a

To transform a permanent, turn it over so that its other face is up. Only permanents represented by double-faced tokens and double-faced cards can transform. (See rule 712, “Double-Faced Cards.”)

#### CR 701.27c

If a spell or ability instructs a player to transform a permanent that isn’t represented by a double-faced token or a double-faced card, nothing happens.

#### CR 702.10a

Haste is a static ability.

#### CR 702.138a

Escape represents a static ability that functions while the card with escape is in a player’s graveyard. “Escape [cost]” means “You may cast this card from your graveyard by paying [cost] rather than paying its mana cost.” Casting a spell using its escape ability follows the rules for paying alternative costs in rules 601.2b and 601.2f–h.

#### CR 704.5j

If two or more legendary permanents with the same name are controlled by the same player, that player chooses one of them, and the rest are put into their owners’ graveyards. This is called the “legend rule.”

#### CR 707.8

When copying a melded permanent or other double-faced permanent, use the copiable values of the face that’s currently up to determine the characteristics of the copy. See rule 712, “Double-Faced Cards.”

#### CR 707.8a

If an effect creates a token that is a copy of a double-faced permanent or a double-faced card not on the battlefield, the resulting token is a double-faced token that has both a front face and a back face. The characteristics of each face are determined by the copiable values of the same face of the permanent or card it is a copy of, as modified by any other copy effects that apply to that object. If the token is a copy of a double-faced permanent with its back face up, the token enters the battlefield with its back face up. This rule does not apply to tokens that are created with their own …

#### CR 707.9b

Some copy effects modify a characteristic as part of the copying process. The final set of values for that characteristic becomes part of the copiable values of the copy.

#### CR 712.14

A double-faced card put onto the battlefield from a zone other than the stack enters the battlefield with its front face up by default.

#### CR 903.9a

If a commander is in a graveyard or in exile and that object was put into that zone since the last time state-based actions were checked, its owner may put it into the command zone. This is a state-based action. See rule 704.

