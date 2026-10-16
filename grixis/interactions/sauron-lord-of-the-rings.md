---
title: "Sauron, Lord of the Rings — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Sauron, Lord of the Rings — Interaction Review

> Bot cycle 54 · batch E · reviewed 2026-10-16. Deck: [Sauron, Lord of the Rings](../decks/sauron-lord-of-the-rings.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/sauron-lord-of-the-rings.txt`](../../exports/grixis-archidekt/sauron-lord-of-the-rings.txt) · SHA-256 `0db8b7c1b7a77f9964a14812dffb9d58f37e40a91c6152fc20e33b3917077c90` |
| Rulings | **5** (5 verified · 0 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`Sauron_Lord_of_the_Rings_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sauron_lotr_2026-10-15/gate_output/Sauron_Lord_of_the_Rings_Rules_Attestation.json) (Rules attestation (14 items, all PASS) re-verified) · [`Sauron_Lord_of_the_Rings_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Sauron_Lord_of_the_Rings_Approval_Ready_Verification_2026-10-15.md) (Approval-ready verification) |

## Contents
- [Summary](#summary)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Engines and payoffs](#engines-and-payoffs)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [Legality and project exceptions](#legality-and-project-exceptions)
- [Rules cited](#rules-cited)

## Summary

Sauron, Lord of the Rings is an eight-drop whose cast trigger amasses, mills five and reanimates even if he's countered. The list is a reanimator deck (Entomb, Buried Alive, Animate Dead, Reanimate, Metamorphosis Fanatic, Living Death), with Anger and Wonder working from the graveyard, Sneak Attack, and a four-Nazgûl Ring side engine. Fast mana (Mana Vault, Grim Monolith) is there only to cast him sooner. There are no Spellbook lines. All 14 attestation items are re-verified against the canonical list.

Rules surprises: countering Sauron doesn't stop the reanimation; the return can pick any creature card in your graveyard and is mandatory; Living Death doesn't bring back your Army token or Sauron; four Nazgûl are legal in Commander. No list errors.

## Commander rules text and edge cases

### sauronlotr-01: Cast trigger: amass 5, mill 5, then reanimate (resolves even if Sauron is countered)

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Sauron, Lord of the Rings, Command Beacon

**Ruling.** Sauron's first ability triggers when he's cast, from the command zone or from hand. It resolves before Sauron himself and works on its own, so countering the Sauron spell doesn't stop it. In order, it amasses Orcs 5, mills five, then returns a creature card from your graveyard to the battlefield. That can be a card already there or one just milled. The return is mandatory if you have a creature card. Command Beacon puts him in hand. Casting him from there has no commander tax, still triggers, and doesn't add to the tax.

**Citations**

- Oracle, *Sauron, Lord of the Rings*: “When you cast this spell, amass Orcs 5, mill five cards, then return a creature card from your graveyard to the battlefield.”
- Scryfall ruling, *Sauron, Lord of the Rings*: “The creature card you choose doesn't need to be a card you milled. You may choose a creature card that was already in your graveyard before you milled.”
- Scryfall ruling, *Command Beacon*: “If you cast a commander from your hand, the additional cost based on the number of times you've cast it from your command zone (sometimes referred to as the "commander tax") doesn't apply. Additionally, that casting won't add to the tax if you later cast the commander from the command zone.”
- [CR 603.2](#cr-6032), [CR 113.7a](#cr-1137a), [CR 903.8](#cr-9038)
- Source (re-verified): [`Sauron_Lord_of_the_Rings_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sauron_lotr_2026-10-15/gate_output/Sauron_Lord_of_the_Rings_Rules_Attestation.json) → “Sauron cast-trigger independence”
- Source (re-verified): [`Sauron_Lord_of_the_Rings_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sauron_lotr_2026-10-15/gate_output/Sauron_Lord_of_the_Rings_Rules_Attestation.json) → “Sauron trigger sequencing”
- Source (re-verified): [`Sauron_Lord_of_the_Rings_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sauron_lotr_2026-10-15/gate_output/Sauron_Lord_of_the_Rings_Rules_Attestation.json) → “Command Beacon and commander tax”

## Engines and payoffs

### sauronlotr-02: Reanimation chains: Metamorphosis Fanatic, Dance of the Dead, Animate Dead, Necromancy, Reanimate

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Sauron, Lord of the Rings, Metamorphosis Fanatic, Dance of the Dead, Animate Dead, Necromancy, Reanimate, Entomb, Buried Alive

**Ruling.** If Sauron's trigger returns Metamorphosis Fanatic, its ETB returns up to one more creature card with a lifelink counter, so you get two bodies from one cast. Entomb and Buried Alive set up the graveyard. Dance of the Dead returns its creature tapped with +1/+1. That creature doesn't untap normally, but you can pay {1}{B} in your upkeep to untap it. If Dance leaves the battlefield, the creature is sacrificed.

**Citations**

- Oracle, *Metamorphosis Fanatic*: “When this creature enters, return up to one target creature card from your graveyard to the battlefield with a lifelink counter on it.”
- Scryfall ruling, *Dance of the Dead*: “This is a new wording. Dance of the Dead is now an Aura. You target a creature card in a graveyard when you cast it. It enters attached to that card. Then it returns that card to the battlefield, and attaches itself to that card again (since the card is treated as a new object on the battlefield).”
- [CR 603.6a](#cr-6036a)
- Source (re-verified): [`Sauron_Lord_of_the_Rings_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sauron_lotr_2026-10-15/gate_output/Sauron_Lord_of_the_Rings_Rules_Attestation.json) → “Metamorphosis Fanatic chain”
- Source (re-verified): [`Sauron_Lord_of_the_Rings_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sauron_lotr_2026-10-15/gate_output/Sauron_Lord_of_the_Rings_Rules_Attestation.json) → “Dance of the Dead”

## Zones, commander tax and the command zone

### sauronlotr-03: Living Death: exile, sacrifice, return. Tokens and Sauron don't come back

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Sauron, Lord of the Rings, Living Death, Phyrexian Tower, Sneak Attack

**Ruling.** Living Death resolves in three steps, each happening for all players at once:
1. Exile every creature card from every graveyard.
2. Sacrifice every creature on the battlefield.
3. Put the exiled cards onto the battlefield.

Only cards exiled in step 1 return. Your Orc Army token and Sauron himself are sacrificed in step 2 and don't return; Sauron can go to the command zone. Sacrifice creatures beforehand with Phyrexian Tower ({B}{B}, a mana ability) so they're in the graveyard for step 1. Sneak Attack's end-step sacrifice also stocks the graveyard.

**Citations**

- Oracle, *Living Death*: “Each player exiles all creature cards from their graveyard, then sacrifices all creatures they control, then puts all cards they exiled this way onto the battlefield.”
- Scryfall ruling, *Living Death*: “Only cards exiled by Living Death's first instruction are put onto the battlefield. If a replacement effect (such as that of Leyline of the Void) causes any of the sacrificed creatures to be exiled instead of put into a graveyard, those cards aren't returned to the battlefield.”
- Scryfall ruling, *Sneak Attack*: “You sacrifice the creature only if you still control it. If that creature has left the battlefield, even if it came back, you don't sacrifice it.”
- [CR 608.2c](#cr-6082c), [CR 111.7](#cr-1117), [CR 903.9a](#cr-9039a)
- Source (re-verified): [`Sauron_Lord_of_the_Rings_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sauron_lotr_2026-10-15/gate_output/Sauron_Lord_of_the_Rings_Rules_Attestation.json) → “Living Death sequencing”
- Source (re-verified): [`Sauron_Lord_of_the_Rings_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sauron_lotr_2026-10-15/gate_output/Sauron_Lord_of_the_Rings_Rules_Attestation.json) → “Phyrexian Tower”
- Source (re-verified): [`Sauron_Lord_of_the_Rings_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sauron_lotr_2026-10-15/gate_output/Sauron_Lord_of_the_Rings_Rules_Attestation.json) → “Sneak Attack graveyard setup”

### sauronlotr-05: Anger and Wonder work from the graveyard, if you control a Mountain or Island

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Sauron, Lord of the Rings, Anger, Wonder, The Mouth of Sauron

**Ruling.** Sauron's mill can bin Anger and Wonder. From your graveyard, Anger gives your creatures haste while you control a Mountain, and Wonder gives flying while you control an Island. Typed duals count, and Anger works even if you had no Mountain when it was milled. The Mouth of Sauron can target you: mill three, then amass Orcs equal to the instants and sorceries in your graveyard.

**Citations**

- Oracle, *Anger*: “As long as this card is in your graveyard and you control a Mountain, creatures you control have haste.”
- Oracle, *The Mouth of Sauron*: “When The Mouth of Sauron enters, target player mills three cards. Then amass Orcs X, where X is the number of instant and sorcery cards in that player's graveyard. (Put X +1/+1 counters on an Army you control. It's also an Orc. If you don't control an Army, create a 0/0 black Orc Army creature token first.)”
- Scryfall ruling, *Anger*: “The timestamp for the "in your graveyard" ability is set at the time that this card goes to your graveyard, regardless of whether you control a Mountain at that time.”
- [CR 113.6](#cr-1136), [CR 305.6](#cr-3056)
- Source (re-verified): [`Sauron_Lord_of_the_Rings_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sauron_lotr_2026-10-15/gate_output/Sauron_Lord_of_the_Rings_Rules_Attestation.json) → “Anger and Wonder land-type checks”
- Source (re-verified): [`Sauron_Lord_of_the_Rings_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sauron_lotr_2026-10-15/gate_output/Sauron_Lord_of_the_Rings_Rules_Attestation.json) → “The Mouth of Sauron self-mill”
- Source (re-verified): [`Sauron_Lord_of_the_Rings_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sauron_lotr_2026-10-15/gate_output/Sauron_Lord_of_the_Rings_Rules_Attestation.json) → “Fast-mana role”

## Legality and project exceptions

### sauronlotr-04: Four Nazgûl are legal; each temptation grows every Wraith once per Nazgûl

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Sauron, Lord of the Rings, Nazgûl

**Ruling.** Nazgûl's own text lets a deck run up to nine copies, overriding the singleton rule. The canonical list runs four. Each Nazgûl's ETB has the Ring tempt you, and each Nazgûl triggers on every temptation. With k Nazgûl out, one temptation puts k counters on each Wraith. Sauron's trigger when an opponent's commander dies is another temptation, and it happens even if that commander goes to the command zone. The Ring can tempt you even if you control no creatures.

**Citations**

- Oracle, *Nazgûl*: “A deck can have up to nine cards named Nazgûl.”
- Oracle, *Nazgûl*: “Whenever the Ring tempts you, put a +1/+1 counter on each Wraith you control.”
- Scryfall ruling, *Nazgûl*: “The last ability of Nazgûl also lets you ignore the "singleton" rule in formats like Commander.”
- Scryfall ruling, *Sauron, Lord of the Rings*: “Sauron, Lord of the Rings's last ability will trigger even if the owner of the commander that died chooses to return it to the command zone after it dies.”
- [CR 903.5b](#cr-9035b), [CR 701.54a](#cr-70154a)
- Source (re-verified): [`Sauron_Lord_of_the_Rings_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sauron_lotr_2026-10-15/gate_output/Sauron_Lord_of_the_Rings_Rules_Attestation.json) → “Nazgûl deck construction”
- Source (re-verified): [`Sauron_Lord_of_the_Rings_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sauron_lotr_2026-10-15/gate_output/Sauron_Lord_of_the_Rings_Rules_Attestation.json) → “Nazgûl and Ring temptation”
- Source (re-verified): [`Sauron_Lord_of_the_Rings_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sauron_lotr_2026-10-15/gate_output/Sauron_Lord_of_the_Rings_Rules_Attestation.json) → “Sauron opponent-commander death trigger”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 111.7

A token that’s in a zone other than the battlefield ceases to exist. This is a state-based action; see rule 704. (Note that if a token changes zones, applicable triggered abilities will trigger before the token ceases to exist.)

#### CR 113.6

Abilities of an instant or sorcery spell usually function only while that object is on the stack. Abilities of all other objects usually function only while that object is on the battlefield. The exceptions are as follows:

#### CR 113.7a

Once activated or triggered, an ability exists on the stack independently of its source. Destruction or removal of the source after that time won’t affect the ability. Note that some abilities cause a source to do something (for example, “This creature deals 1 damage to any target”) rather than the ability doing anything directly. In these cases, any activated or triggered ability that references information about the source for use while announcing an activated ability or putting a triggered ability on the stack checks that information when the ability is put onto the stack. Otherwise, it …

#### CR 305.6

The basic land types are Plains, Island, Swamp, Mountain, and Forest. If an object uses the words “basic land type,” it’s referring to one of these subtypes. An object with the land card type and a basic land type has the intrinsic ability “{T}: Add [mana symbol],” even if the text box doesn’t actually contain that text or the object has no text box. For Plains, [mana symbol] is {W}; for Islands, {U}; for Swamps, {B}; for Mountains, {R}; and for Forests, {G}. See rule 107.4a. See also rule 605, “Mana Abilities.”

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 603.6a

Enters-the-battlefield abilities trigger when a permanent enters the battlefield. These are written, “When [this object] enters, . . . “ or “Whenever a [type] enters, . . .” Each time an event puts one or more permanents onto the battlefield, all permanents on the battlefield (including the newcomers) are checked for any enters-the-battlefield triggers that match the event.

#### CR 608.2c

The controller of the spell or ability follows its instructions in the order written. However, replacement effects may modify these actions. In some cases, later text on the card may modify the meaning of earlier text (for example, “Destroy target creature. It can’t be regenerated” or “Counter target spell. If that spell is countered this way, put it on top of its owner’s library instead of into its owner’s graveyard.”) Don’t just apply effects step by step without thinking in these cases—read the whole text and apply the rules of English to the text.

#### CR 701.54a

Certain spells and abilities have the text “the Ring tempts you.” Each time the Ring tempts you, choose a creature you control. That creature becomes your Ring-bearer until another creature becomes your Ring-bearer or another player gains control of it.

#### CR 903.5b

Other than basic lands, each card in a Commander deck must have a different English name. For the purposes of deck construction, cards with interchangeable names have the same English name (see rule 201.3).

#### CR 903.8

A player may cast a commander they own from the command zone. A commander cast from the command zone costs an additional {2} for each previous time the player casting it has cast it from the command zone that game. This additional cost is informally known as the “commander tax.”

#### CR 903.9a

If a commander is in a graveyard or in exile and that object was put into that zone since the last time state-based actions were checked, its owner may put it into the command zone. This is a state-based action. See rule 704.

