---
title: "Nicol Bolas, the Ravager // Nicol Bolas, the Arisen — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Nicol Bolas, the Ravager // Nicol Bolas, the Arisen — Interaction Review

> Bot cycle 51 · batch D · reviewed 2026-10-16. Deck: [Nicol Bolas, the Ravager // Nicol Bolas, the Arisen](../decks/nicol-bolas-the-ravager.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/nicol-bolas-the-ravager.txt`](../../exports/grixis-archidekt/nicol-bolas-the-ravager.txt) · SHA-256 `ff0f90a467b05c94bdf58371d37a848946877ec707115ac5e47c2260bc40c1f4` |
| Rulings | **8** (8 verified · 0 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`Nicol_Bolas_the_Ravager_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nicol_Bolas_the_Ravager_Approval_Ready_Verification_2026-10-15.md) (Approval-ready verification; rules sections 5–16 re-checked against Oracle, rulings and CR) |

## Contents
- [Summary](#summary)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [Key card-pair interactions](#key-card-pair-interactions)
- [Layers and continuous effects](#layers-and-continuous-effects)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [Rules cited](#rules-cited)

## Summary

Nicol Bolas, the Ravager transforms by exiling and returning, so the Arisen arrives as a new planeswalker that can activate loyalty at once. Training Grounds makes this cost five mana. The list copies loyalty abilities (Rowan's Talent, Rings, Jaya's Phoenix), runs Chain Veil and Teferi engines, and supports loyalty with proliferate, Sanctum Lurker and phasing. Three Spellbook lines are confirmed; the source's Rings + Chain Veil variant is rules-checked but tagged hypothesis.

Rules surprises: Kitten on the Arisen returns Ravager and strips its Talents; copied loyalty abilities don't move loyalty; Dark Intimations doesn't boost a transformed Arisen; a non-DFC copy of Ravager is exiled for good. No list errors.

## Commander rules text and edge cases

### bolasrav-01: Transform by exile-and-return: the Arisen is a new object and can use loyalty right away

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Nicol Bolas, the Ravager // Nicol Bolas, the Arisen, Training Grounds

**Ruling.** The {4}{U}{B}{R} ability (sorcery speed) exiles Ravager and returns the card transformed as Nicol Bolas, the Arisen. As a new object, the Arisen enters with its printed loyalty and can activate a loyalty ability that same turn. If Ravager leaves the battlefield in response, the card stays wherever it went. Training Grounds reduces the cost to {2}{U}{B}{R}, because this is an activated ability of a creature. Colored symbols aren't reduced. A non-DFC copy of Ravager (Spark Double) is exiled by the ability and never returns.

**Citations**

- Oracle, *Nicol Bolas, the Ravager // Nicol Bolas, the Arisen*: “{4}{U}{B}{R}: Exile Nicol Bolas, then return him to the battlefield transformed under his owner's control. Activate only as a sorcery.”
- Scryfall ruling, *Nicol Bolas, the Ravager // Nicol Bolas, the Arisen*: “You can activate one of the planeswalker's loyalty abilities the turn it enters the battlefield.”
- Scryfall ruling, *Nicol Bolas, the Ravager // Nicol Bolas, the Arisen*: “If Nicol Bolas leaves the battlefield after his creature face's activated ability has been activated but before it resolves, the card remains in whichever zone it moves to. It won't be exiled or return transformed.”
- Scryfall ruling, *Nicol Bolas, the Ravager // Nicol Bolas, the Arisen*: “If another permanent that isn't a double-faced card (such as Mirror Image) becomes a copy of Nicol Bolas, the Ravager, activating the ability to exile it and return it transformed will only exile it. It won't return to the battlefield at all.”
- [CR 712.14a](#cr-71214a), [CR 400.7](#cr-4007), [CR 606.3](#cr-6063), [CR 306.5b](#cr-3065b)
- Source (re-verified): [`Nicol_Bolas_the_Ravager_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nicol_Bolas_the_Ravager_Approval_Ready_Verification_2026-10-15.md) → “Training Grounds reduces `{4}{U}{B}{R}` to **`{2}{U}{B}{R}`**.”

## Combos and engine lines

### bolasrav-04: Teferi, Temporal Archmage + The Chain Veil (+ Rings)

**Status:** ✅ verified · **Evidence:** hypothesis · **Cards:** Nicol Bolas, the Ravager // Nicol Bolas, the Arisen, Teferi, Temporal Archmage, The Chain Veil, Rings of Brighthearth, Mana Vault, Sol Ring

**Ruling.** The Spellbook line:
1. Pay {4} and tap The Chain Veil.
2. Use Teferi's −1 to untap Chain Veil and three mana permanents that make {4}.
3. Repeat until Teferi runs out of loyalty, then recast him and use his +1.

The source's Rings version: copy the Chain Veil activation for {2}. Each Chain Veil resolution grants another activation, so two resolutions pay for both a −1 and a +1. Teferi's loyalty then stays level as long as the untapped permanents make {6}. The Rings version isn't a Spellbook line and needs at least {6} from three permanents Teferi can untap (for example Mana Vault + Sol Ring + a Signet). Every activation must be in your main phase with an empty stack.

**Citations**

- Oracle, *The Chain Veil*: “{4}, {T}: For each planeswalker you control, you may activate one of its loyalty abilities once this turn as though none of its loyalty abilities have been activated this turn.”
- Oracle, *Teferi, Temporal Archmage*: “−1: Untap up to four target permanents.”
- Scryfall ruling, *The Chain Veil*: “Each additional time The Chain Veil’s last ability resolves will allow you to activate a loyalty ability of each planeswalker you control an additional time. For example, if you activate The Chain Veil’s last ability, untap it, then activate it again, you can activate a loyalty ability of a planeswalker you control three times that turn.”
- [CR 606.3](#cr-6063), [CR 707.10](#cr-70710)
- Commander Spellbook [787-1124](https://commanderspellbook.com/combo/787-1124/) (community-maintained, retrieved 2026-10-16): “Activate Teferi's second loyalty ability by removing a loyalty counter from it, untapping the Chain Veil and the three mana-producing permanents.”
- Source (re-verified): [`Nicol_Bolas_the_Ravager_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nicol_Bolas_the_Ravager_Approval_Ready_Verification_2026-10-15.md) → “The verification does **not** claim that any two pieces alone form an infinite combo.”

### bolasrav-05: Teferi, Master of Time + Ichormoon Gauntlet + Chain Veil / Rowan's Talent: infinite turns

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Nicol Bolas, the Ravager // Nicol Bolas, the Arisen, Teferi, Master of Time, Ichormoon Gauntlet, The Chain Veil, Rowan's Talent

**Ruling.** Ichormoon Gauntlet gives every planeswalker "[0]: Proliferate" and "[−12]: Take an extra turn". Teferi, Master of Time's −10 takes two extra turns. Teferi can activate at instant speed on any player's turn, but still only once per turn. With two other planeswalkers (the Arisen counts), you build Teferi to 10 by proliferating. With Rowan's Talent on Teferi, his −10 is copied for four extra turns. The Chain Veil adds one more activation each turn. Each extra turn rebuilds the loyalty.

**Citations**

- Oracle, *Ichormoon Gauntlet*: “Planeswalkers you control have "[0]: Proliferate" and "[−12]: Take an extra turn after this one."”
- Oracle, *Teferi, Master of Time*: “−10: Take two extra turns after this one.”
- Scryfall ruling, *Ichormoon Gauntlet*: “Only one loyalty ability of each planeswalker may be activated per turn, no matter how many it has gained.”
- [CR 606.3](#cr-6063), [CR 500.7](#cr-5007), [CR 701.34a](#cr-70134a)
- Commander Spellbook [1124-1543-2247](https://commanderspellbook.com/combo/1124-1543-2247/) (community-maintained, retrieved 2026-10-16): “You control at least two other planeswalkers.”
- Commander Spellbook [652-1543-2247](https://commanderspellbook.com/combo/652-1543-2247/) (community-maintained, retrieved 2026-10-16): “Rowan's Talent triggers, copying Teferi's ability.”

## Engines and payoffs

### bolasrav-03: Copied loyalty abilities don't cost loyalty: Rowan's Talent, Rings of Brighthearth, Jaya's Phoenix

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Nicol Bolas, the Ravager // Nicol Bolas, the Arisen, Rowan's Talent, Rings of Brighthearth, Jaya's Phoenix

**Ruling.** Rowan's Talent copies every loyalty ability of the enchanted planeswalker. Rings of Brighthearth can copy one for {2}. Jaya's Phoenix copies the next one after it deals combat damage. Only the original changes loyalty. On the Arisen: +2 draws four, −3 makes two 10-damage instances, and −4 reanimates two targets. The −12 can be copied whenever the original is legal. Loyalty abilities still need your main phase with an empty stack.

**Citations**

- Oracle, *Rowan's Talent*: “Whenever you activate a loyalty ability of enchanted planeswalker, copy that ability. You may choose new targets for the copy.”
- Scryfall ruling, *Rowan's Talent*: “Copying a loyalty ability doesn't cause any loyalty counters to be added to or removed from the enchanted planeswalker.”
- Scryfall ruling, *Rings of Brighthearth*: “An activated mana ability is one that produces mana as it resolves, not one that costs mana to activate.”
- [CR 707.10](#cr-70710), [CR 606.4](#cr-6064)
- Source (re-verified): [`Nicol_Bolas_the_Ravager_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nicol_Bolas_the_Ravager_Approval_Ready_Verification_2026-10-15.md) → “A copied loyalty ability does **not** repeat its loyalty cost.”

### bolasrav-08: Loyalty support: proliferate (Tekuthal doubles), Sanctum Lurker at 0, Ripples phase-out

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Nicol Bolas, the Ravager // Nicol Bolas, the Arisen, Sanctum Lurker, Ripples of Potential, Dreamtide Whale, Tekuthal, Inquiry Dominus, Flux Channeler, Inexorable Tide, Karn's Bastion, Vraska, Betrayal's Sting

**Ruling.** These keep loyalty up:
- **Proliferate** (Flux Channeler, Inexorable Tide, Dreamtide Whale, Karn's Bastion, Vraska's 0, the Gauntlet's 0): Tekuthal makes each one happen twice. Dreamtide Whale can proliferate its own time counters to delay vanishing.
- **Sanctum Lurker:** a walker at 0 loyalty isn't put into the graveyard, so you can use the −12 down to exactly 0 and then use Lurker's +2. Other removal still works.
- **Ripples of Potential:** proliferates, then phases out anything that got a counter. The counters stay, and phasing out doesn't trigger leaves-the-battlefield abilities.

**Citations**

- Oracle, *Sanctum Lurker*: “Planeswalkers you control aren't put into their owners' graveyards for having 0 loyalty.”
- Oracle, *Tekuthal, Inquiry Dominus*: “If you would proliferate, proliferate twice instead.”
- Scryfall ruling, *Sanctum Lurker*: “If a planeswalker you control has zero loyalty counters while you control Sanctum Lurker, it will not be put into its owner's graveyard. You may still activate abilities of that planeswalker that cost [0] or that add counters to it as a cost, such as the one granted by Sanctum Lurker.”
- Scryfall ruling, *Ripples of Potential*: “Phasing out doesn't cause any "leaves the battlefield" abilities to trigger. Similarly, phasing in won't cause any "enters the battlefield" abilities to trigger.”
- [CR 701.34a](#cr-70134a), [CR 704.5i](#cr-7045i), [CR 702.26b](#cr-70226b)
- Source (re-verified): [`Nicol_Bolas_the_Ravager_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nicol_Bolas_the_Ravager_Approval_Ready_Verification_2026-10-15.md) → “The protection is specifically from the state-based action for 0 loyalty; it does not make planeswalkers indestructible or prevent other removal.”

## Key card-pair interactions

### bolasrav-06: Bolas planeswalker checks and casts: Deliver Unto Evil yes, Dark Intimations no

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Nicol Bolas, the Ravager // Nicol Bolas, the Arisen, Deliver Unto Evil, Dark Intimations, Nicol Bolas, Dragon-God, Nicol Bolas, God-Pharaoh, Nicol Bolas, Planeswalker, Nicol Bolas, the Deceiver

**Ruling.** Deliver Unto Evil returns all four cards if you control any Bolas planeswalker: the Arisen, Dragon-God, God-Pharaoh, Planeswalker or Deceiver. Dark Intimations' graveyard bonus needs you to cast a Bolas planeswalker spell. Transforming Ravager isn't a cast, so the Arisen doesn't get the extra loyalty. Casting one of the four other Bolas walkers does.

**Citations**

- Oracle, *Deliver Unto Evil*: “Choose up to four target cards in your graveyard. If you control a Bolas planeswalker, return those cards to your hand.”
- Oracle, *Dark Intimations*: “When you cast a Bolas planeswalker spell, exile this card from your graveyard. That planeswalker enters with an additional loyalty counter on it.”
- [CR 205.3j](#cr-2053j), [CR 601.2](#cr-6012)
- Source (re-verified): [`Nicol_Bolas_the_Ravager_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nicol_Bolas_the_Ravager_Approval_Ready_Verification_2026-10-15.md) → “Transforming Ravager through his activated ability does **not** cast a planeswalker spell”

## Layers and continuous effects

### bolasrav-07: Spark Double copies the Arisen; Nicol Bolas, Dragon-God borrows every walker's loyalty abilities

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Nicol Bolas, the Ravager // Nicol Bolas, the Arisen, Spark Double, Nicol Bolas, Dragon-God

**Ruling.** Spark Double can enter as a copy of the transformed Arisen. It's nonlegendary, has one extra loyalty, and has the Arisen's abilities. It isn't a DFC, but it never needs to transform. Nicol Bolas, Dragon-God has the loyalty abilities of every other planeswalker on the battlefield, including opponents' walkers and the Gauntlet's granted ones. References to the original's name refer to Dragon-God instead. He still gets only one loyalty activation per turn, unless The Chain Veil adds one.

**Citations**

- Oracle, *Nicol Bolas, Dragon-God*: “Nicol Bolas has all loyalty abilities of all other planeswalkers on the battlefield.”
- Scryfall ruling, *Nicol Bolas, Dragon-God*: “While Nicol Bolas may end up with an astonishing number of loyalty abilities, you can still activate only one loyalty ability of Nicol Bolas, Dragon-God during each of your turns.”
- Scryfall ruling, *Nicol Bolas, Dragon-God*: “Nicol Bolas doesn't gain any static or triggered abilities of other planeswalkers or any activated abilities they may have that aren't loyalty abilities.”
- [CR 707.2](#cr-7072), [CR 707.9b](#cr-7079b), [CR 606.3](#cr-6063)
- Source (re-verified): [`Nicol_Bolas_the_Ravager_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nicol_Bolas_the_Ravager_Approval_Ready_Verification_2026-10-15.md) → “It may copy the **currently transformed Arisen** because the Arisen is a planeswalker you control.”

## Zones, commander tax and the command zone

### bolasrav-02: Displacer Kitten resets to Ravager (front face) — and strips Talents

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Nicol Bolas, the Ravager // Nicol Bolas, the Arisen, Displacer Kitten, Rowan's Talent, Liliana's Talent, Tergrid, God of Fright // Tergrid's Lantern

**Ruling.** A DFC that enters from anywhere but the stack comes in front face up unless told otherwise. So when Kitten blinks the Arisen, it returns as Ravager, a new object with no loyalty counters. Each opponent discards again, and Tergrid can take any permanent cards they discard. Any Aura on the Arisen, such as Rowan's Talent or Liliana's Talent, goes to the graveyard. Use Kitten to replay the ETB, not to protect the planeswalker.

**Citations**

- Oracle, *Tergrid, God of Fright // Tergrid's Lantern*: “Whenever an opponent sacrifices a nontoken permanent or discards a permanent card, you may put that card from a graveyard onto the battlefield under your control.”
- Scryfall ruling, *Displacer Kitten*: “When the card returns to the battlefield, it will be a new object with no connection to the card that was exiled. Auras attached to the exiled creature will be put into their owners' graveyards. Any Equipment will become unattached and remain on the battlefield. Any counters on the exiled permanent will cease to exist.”
- Scryfall ruling, *Nicol Bolas, the Ravager // Nicol Bolas, the Arisen*: “A double-faced card enters the battlefield with its front face up by default, unless a spell or ability instructs you to put it onto the battlefield transformed, in which case it enters with its back face up. The back face of a double-faced card can't be played.”
- [CR 712.14](#cr-71214), [CR 400.7](#cr-4007), [CR 704.5m](#cr-7045m)
- Source (re-verified): [`Nicol_Bolas_the_Ravager_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nicol_Bolas_the_Ravager_Approval_Ready_Verification_2026-10-15.md) → “Because Kitten does not instruct the card to enter transformed, the double-faced card returns front face up as Ravager, retriggering the ETB discard.”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 205.3j

Planeswalkers have their own unique set of subtypes; these subtypes are called planeswalker types. The planeswalker types are Ajani, Aminatou, Angrath, Arlinn, Ashiok, Bahamut, Basri, Bolas, Calix, Chandra, Comet, Dack, Dakkon, Daretti, Davriel, Dellian, Dihada, Domri, Dovin, Ellywick, Elminster, Elspeth, Estrid, Freyalise, Garruk, Gideon, Grist, Guff, Huatli, Jace, Jared, Jaya, Jeska, Kaito, Karn, Kasmina, Kaya, Kiora, Koth, Liliana, Lolth, Lukka, Minsc, Mordenkainen, Nahiri, Narset, Niko, Nissa, Nixilis, Oko, Quintorius, Ral, Rowan, Saheeli, Samut, Sarkhan, Serra, Sivitri, Sorin, Szat, …

#### CR 306.5b

A planeswalker has the intrinsic ability “This permanent enters with a number of loyalty counters on it equal to its printed loyalty number.” This ability creates a replacement effect (see rule 614.1c).

#### CR 400.7

An object that moves from one zone to another becomes a new object with no memory of, or relation to, its previous existence. This rule has the following exceptions.

#### CR 500.7

Some effects can give a player extra turns. They do this by adding the turns directly after the specified turn. If a player is given multiple extra turns, the extra turns are added one at a time. If multiple players are given extra turns, the extra turns are added one at a time, in APNAP order (see rule 101.4). The most recently created turn will be taken first.

#### CR 601.2

To cast a spell is to take it from where it is (usually the hand), put it on the stack, and pay its costs, so that it will eventually resolve and have its effect. Casting a spell includes proposal of the spell (rules 601.2a–d) and determination and payment of costs (rules 601.2f–h). To cast a spell, a player follows the steps listed below, in order. A player must be legally allowed to cast the spell to begin this process (see rule 601.3). If a player is unable to comply with the requirements of a step listed below while performing that step, the casting of the spell is illegal; the game …

#### CR 606.3

A player may activate a loyalty ability of a permanent they control any time they have priority and the stack is empty during a main phase of their turn, but only if no player has previously activated a loyalty ability of that permanent that turn.

#### CR 606.4

The cost to activate a loyalty ability of a permanent is to put on or remove from that permanent a certain number of loyalty counters, as shown by the loyalty symbol in the ability’s cost. This cost may be modified by other effects.

#### CR 701.34a

To proliferate means to choose any number of permanents and/or players that have a counter, then give each one additional counter of each kind that permanent or player already has.

#### CR 702.26b

If a permanent phases out, its status changes to “phased out.” Except for rules and effects that specifically mention phased-out permanents, a phased-out permanent is treated as though it does not exist. It can’t affect or be affected by anything else in the game. A permanent that phases out is removed from combat. (See rule 506.4.)

#### CR 704.5i

If a planeswalker has loyalty 0, it’s put into its owner’s graveyard.

#### CR 704.5m

If an Aura is attached to an illegal object or player, or is not attached to an object or player, that Aura is put into its owner’s graveyard.

#### CR 707.2

When copying an object, the copy acquires the copiable values of the original object’s characteristics and, for an object on the stack, choices made when casting or activating it (mode, targets, the value of X, whether it was kicked, how it will affect multiple targets, and so on). The copiable values are the values derived from the text printed on the object (that text being name, mana cost, color indicator, card type, subtype, supertype, rules text, power, toughness, and/or loyalty), as modified by other copy effects, by its face-down status, and by “as . . . enters” and “as . . . is turned …

#### CR 707.9b

Some copy effects modify a characteristic as part of the copying process. The final set of values for that characteristic becomes part of the copiable values of the copy.

#### CR 707.10

To copy a spell, activated ability, or triggered ability means to put a copy of it onto the stack; a copy of a spell isn’t cast and a copy of an activated ability isn’t activated. A copy of a spell or ability copies both the characteristics of the spell or ability and all decisions made for it, including modes, targets, the value of X, and additional or alternative costs. (See rule 601, “Casting Spells.”) Choices that are normally made on resolution are not copied. If an effect of the copy refers to objects used to pay its costs, it uses the objects used to pay the costs of the original spell …

#### CR 712.14

A double-faced card put onto the battlefield from a zone other than the stack enters the battlefield with its front face up by default.

#### CR 712.14a

If a spell or ability puts a double-faced card onto the battlefield “transformed” or “converted,” it enters the battlefield with its back face up. If a player is instructed to put a card that isn’t a double-faced card onto the battlefield transformed or converted, that card stays in its current zone.

