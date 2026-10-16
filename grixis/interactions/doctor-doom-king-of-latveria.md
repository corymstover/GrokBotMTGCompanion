---
title: "Doctor Doom, King of Latveria — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Doctor Doom, King of Latveria — Interaction Review

> Bot cycle 48 · batch B · reviewed 2026-10-16. Deck: [Doctor Doom, King of Latveria](../decks/doctor-doom-king-of-latveria.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-15), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/doctor-doom-king-of-latveria.txt`](../../exports/grixis-archidekt/doctor-doom-king-of-latveria.txt) · SHA-256 `3505f9a465a8ed61f9689d7a38c67b47d68b487001565b9ccc08de82a62f1574` |
| Rulings | **11** (10 verified · 1 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-15 · rulings 2026-10-15 |
| Source attestations | [`Doctor_Doom_King_of_Latveria_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/doctor_doom_king_of_latveria_2026-10-14/Doctor_Doom_King_of_Latveria_Rules_Attestation.json) (13 interactions, all PASS) |

## Contents
- [Summary](#summary)
- [Flags and open questions](#flags-and-open-questions)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [Layers and continuous effects](#layers-and-continuous-effects)
- [Replacement and prevention effects](#replacement-and-prevention-effects)
- [Trigger ordering](#trigger-ordering)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [Rules cited](#rules-cited)

## Summary

Doctor Doom, King of Latveria drains 2 from each opponent whenever you discard one or more lands, and connives a Villain each combat. This review re-verifies the thirteen items of the deck's rules attestation, and checks the Dakmor Salvage loops against cached Commander Spellbook steps.

Key rules: Doom triggers once per discard event (wheels give one trigger), dredge loops are library-bounded, and Bone Miser's mana can't pay the cost that caused it. No list errors.

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [doom-09](#doom-09-trade-routes--bone-miser-or-badgersaur--dakmor) | ⚠️ uncertain | Trade Routes + Bone Miser or Badgersaur + Dakmor | Rebuilt from the source attestation; Spellbook has no cached variant with Trade Routes for this list, so the line is checked against Oracle and rulings only. |

## Commander rules text and edge cases

### doom-01: One trigger per discard event, not per land

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Doctor Doom, King of Latveria, Wheel of Fortune, Windfall, Cool but Rude

**Ruling.** Doom says 'one or more land cards', so one discard event triggers him once however many lands are in it. Wheel of Fortune or Windfall discarding three lands drains each opponent 2, not 6. Separate discards (cycling, Psychic Frog activations, Trade Routes) each trigger him. Cool but Rude level 2 says 'Whenever you discard a card', so it triggers once for each card, including in a wheel.

**Citations**

- Oracle, *Doctor Doom, King of Latveria*: “Whenever you discard one or more land cards, each opponent loses 2 life.”
- Oracle, *Cool but Rude*: “Whenever you discard a card, this Class deals 2 damage to each opponent.”
- [CR 603.2c](#cr-6032c), [CR 701.9a](#cr-7019a)
- Source (re-verified): [`Doctor_Doom_King_of_Latveria_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/doctor_doom_king_of_latveria_2026-10-14/Doctor_Doom_King_of_Latveria_Rules_Attestation.json) → “Doctor Doom land-discard trigger event granularity”
- Source (re-verified): [`Doctor_Doom_King_of_Latveria_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/doctor_doom_king_of_latveria_2026-10-14/Doctor_Doom_King_of_Latveria_Rules_Attestation.json) → “Cool but Rude versus Doctor Doom discard granularity”
- Source (re-verified): [`Doctor_Doom_King_of_Latveria_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/doctor_doom_king_of_latveria_2026-10-14/Doctor_Doom_King_of_Latveria_Rules_Attestation.json) → “Wheel of Fortune and Windfall retained role”

### doom-02: Combat connive targets a Villain and fails if it's gone

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Doctor Doom, King of Latveria

**Ruling.** At beginning of combat Doom targets a Villain you control (Doom himself qualifies). If that target is illegal on resolution, the whole ability does nothing: no menace, no draw, no discard. Connive is draw then discard; a nonland discard gives a +1/+1 counter, while a land discard instead triggers Doom's drain.

**Citations**

- Oracle, *Doctor Doom, King of Latveria*: “At the beginning of combat on your turn, target Villain you control gains menace until end of turn. It connives.”
- [CR 608.2b](#cr-6082b), [CR 701.50a](#cr-70150a)
- Source (re-verified): [`Doctor_Doom_King_of_Latveria_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/doctor_doom_king_of_latveria_2026-10-14/Doctor_Doom_King_of_Latveria_Rules_Attestation.json) → “Doctor Doom beginning-of-combat target legality”

## Combos and engine lines

### doom-08: Tectonic Reformation + Surly Badgersaur + Dakmor Salvage

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Doctor Doom, King of Latveria, Tectonic Reformation, Surly Badgersaur, Dakmor Salvage

**Ruling.** Tectonic Reformation gives Dakmor cycling {R}. Cycling discards it as a cost: Badgersaur makes a Treasure and Doom triggers, both resolving before the cycling draw. Replace the draw with dredge 2 to return Dakmor, then crack the Treasure for {R} and repeat. Each cycle drains each opponent 2. With three opponents at 40 life, 20 cycles kill, which mills 40 cards.

**Citations**

- Oracle, *Tectonic Reformation*: “Each land card in your hand has cycling {R}.”
- Oracle, *Surly Badgersaur*: “Whenever you discard a land card, create a Treasure token.”
- Scryfall ruling, *Surly Badgersaur*: “If you discard a card as a cost to cast a spell or activate an ability, Surly Badgersaur's triggered ability resolves before that spell or ability but after you've chosen targets for it.”
- [CR 702.29a](#cr-70229a), [CR 702.52a](#cr-70252a), [CR 603.3](#cr-6033)
- Commander Spellbook [779-2546-4467](https://commanderspellbook.com/combo/779-2546-4467/) (community-maintained, retrieved 2026-10-16): “Activate Dakmor Salvage's cycling ability by paying {R} and discarding it.”
- Commander Spellbook [779-2546-4467](https://commanderspellbook.com/combo/779-2546-4467/) (community-maintained, retrieved 2026-10-16): “Resolve the Dakmor Salvage ability, causing you to mill two cards and return Dakmor Salvage from your graveyard to your hand.”
- Source (re-verified): [`Doctor_Doom_King_of_Latveria_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/doctor_doom_king_of_latveria_2026-10-14/Doctor_Doom_King_of_Latveria_Rules_Attestation.json) → “Tectonic Reformation + Surly Badgersaur + Dakmor Salvage + Doctor Doom”

### doom-09: Trade Routes + Bone Miser or Badgersaur + Dakmor

**Status:** ⚠️ uncertain · **Evidence:** hypothesis · **Cards:** Doctor Doom, King of Latveria, Trade Routes, Bone Miser, Surly Badgersaur, Dakmor Salvage

**Ruling.** Trade Routes: {1}, discard a land, draw. Discarding Dakmor triggers Doom and Bone Miser ({B}{B}) or Badgersaur (a Treasure); they resolve before the draw, which dredges Dakmor back. The mana can pay the next activation, not the current one: Bone Miser's mana trigger uses the stack, so it can't pay the cost that caused it. Each loop is one Doom trigger and mills two. Bone Miser nets {B} per loop.

**Uncertain.** Rebuilt from the source attestation; Spellbook has no cached variant with Trade Routes for this list, so the line is checked against Oracle and rulings only.

**Citations**

- Oracle, *Trade Routes*: “{1}, Discard a land card: Draw a card.”
- Oracle, *Bone Miser*: “Whenever you discard a land card, add {B}{B}.”
- Scryfall ruling, *Bone Miser*: “Notably, this means that you can’t pay a cost of “{2}, Discard a card” by discarding a land card and using the {B}{B} produced to pay for the {2}.”
- [CR 602.2](#cr-6022), [CR 605.1a](#cr-6051a), [CR 702.52a](#cr-70252a)
- Source (re-verified): [`Doctor_Doom_King_of_Latveria_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/doctor_doom_king_of_latveria_2026-10-14/Doctor_Doom_King_of_Latveria_Rules_Attestation.json) → “Trade Routes + Bone Miser + Dakmor Salvage + Doctor Doom”
- Source (re-verified): [`Doctor_Doom_King_of_Latveria_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/doctor_doom_king_of_latveria_2026-10-14/Doctor_Doom_King_of_Latveria_Rules_Attestation.json) → “Trade Routes + Surly Badgersaur + Dakmor Salvage + Doctor Doom”

## Engines and payoffs

### doom-05: Glorious Purpose counts each connive

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Doctor Doom, King of Latveria, Glorious Purpose, Ultron, Unlimited, Villainous Hideout

**Ruling.** Each connive by a creature you control adds a +1/+1 counter to it and a plan counter. At six, sacrifice it, exile your top four and cast any number of them free. Spells with {X} are cast with X = 0. Connive sources in the list: Doom's combat trigger, Ultron attacking, Villainous Hideout, Baron Strucker.

**Citations**

- Oracle, *Glorious Purpose*: “Whenever a creature you control connives, put a +1/+1 counter on that creature and a plan counter on this enchantment.”
- [CR 701.50a](#cr-70150a), [CR 601.2b](#cr-6012b)
- Source (re-verified): [`Doctor_Doom_King_of_Latveria_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/doctor_doom_king_of_latveria_2026-10-14/Doctor_Doom_King_of_Latveria_Rules_Attestation.json) → “Glorious Purpose with repeated connive”

### doom-06: Psychic Frog: a free, repeatable land outlet

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Doctor Doom, King of Latveria, Psychic Frog

**Ruling.** 'Discard a card' is Frog's whole cost, so each activation is a separate discard event and each land triggers Doom. Doom's trigger goes on the stack above the Frog ability and resolves first.

**Citations**

- Oracle, *Psychic Frog*: “Discard a card: Put a +1/+1 counter on this creature.”
- [CR 602.2](#cr-6022), [CR 603.3](#cr-6033)
- Source (re-verified): [`Doctor_Doom_King_of_Latveria_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/doctor_doom_king_of_latveria_2026-10-14/Doctor_Doom_King_of_Latveria_Rules_Attestation.json) → “Psychic Frog as separable land-discard outlet”

### doom-11: Archfiend of Ifnir punishes every cycle and discard

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Doctor Doom, King of Latveria, Archfiend of Ifnir, Tectonic Reformation

**Ruling.** Archfiend of Ifnir puts a -1/-1 counter on each opponent's creature whenever you cycle or discard another card. Cycling a land with Tectonic Reformation is both a cycle and a discard, but it's one event, so Archfiend triggers once. In the Dakmor loop it wipes out small creatures alongside Doom's drain.

**Citations**

- Oracle, *Archfiend of Ifnir*: “Whenever you cycle or discard another card, put a -1/-1 counter on each creature your opponents control.”
- Scryfall ruling, *Archfiend of Ifnir*: “An ability that triggers whenever you "cycle or discard" a card triggers only once if you cycle a card.”
- [CR 603.2c](#cr-6032c), [CR 702.29a](#cr-70229a)

## Layers and continuous effects

### doom-03: Chameleon copy keeps its own name, so no legend rule

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Doctor Doom, King of Latveria, Chameleon, Master of Disguise, Spark Double

**Ruling.** Chameleon can enter as a copy of Doom except its name is Chameleon, Master of Disguise. It is a legendary Doom with a different name, so the legend rule doesn't apply. Spark Double's copy isn't legendary and enters with an extra +1/+1 counter. Both give an independent land-discard trigger and combat connive. Mayhem lets you cast Chameleon from the graveyard if you discarded it this turn, at normal timing.

**Citations**

- Oracle, *Chameleon, Master of Disguise*: “You may have Chameleon enter as a copy of a creature you control, except his name is Chameleon, Master of Disguise.”
- Scryfall ruling, *Spark Double*: “Spark Double isn’t legendary if it copies a legendary permanent, and this exception is copiable.”
- Scryfall ruling, *Chameleon, Master of Disguise*: “You must follow all normal timing rules when casting a spell with mayhem.”
- [CR 707.9b](#cr-7079b), [CR 704.5j](#cr-7045j), [CR 707.2](#cr-7072)
- Source (re-verified): [`Doctor_Doom_King_of_Latveria_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/doctor_doom_king_of_latveria_2026-10-14/Doctor_Doom_King_of_Latveria_Rules_Attestation.json) → “Chameleon, Master of Disguise entering as Doctor Doom”
- Source (re-verified): [`Doctor_Doom_King_of_Latveria_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/doctor_doom_king_of_latveria_2026-10-14/Doctor_Doom_King_of_Latveria_Rules_Attestation.json) → “Spark Double entering as Doctor Doom”

## Replacement and prevention effects

### doom-07: Dakmor Salvage is renewable, bounded by the library

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Doctor Doom, King of Latveria, Dakmor Salvage

**Ruling.** Dredge 2 replaces any draw, not just the draw step. You can't use it with fewer than two cards in your library. Every Dakmor loop below therefore mills two per iteration and stops when the library runs out. It's lethal with enough cards, not infinite. Effects that put cards into hand without 'draw' can't be replaced.

**Citations**

- Scryfall ruling, *Dakmor Salvage*: “Dredge can replace any card draw, not only the one during your draw step.”
- Scryfall ruling, *Dakmor Salvage*: “You can't attempt to use a dredge ability if you don't have enough cards in your library.”
- [CR 702.52a](#cr-70252a), [CR 702.52b](#cr-70252b)
- Source (re-verified): [`Doctor_Doom_King_of_Latveria_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/doctor_doom_king_of_latveria_2026-10-14/Doctor_Doom_King_of_Latveria_Rules_Attestation.json) → “Dakmor Salvage dredge replacement”

## Trigger ordering

### doom-04: Roaming Throne on Villain doubles both Doom triggers

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Doctor Doom, King of Latveria, Roaming Throne

**Ruling.** With Villain named, Doom's land-discard drain and combat connive each trigger an additional time. Each combat instance picks its own target. That is two connives, which also means two Glorious Purpose counters.

**Citations**

- Oracle, *Roaming Throne*: “If a triggered ability of another creature you control of the chosen type triggers, it triggers an additional time.”
- Scryfall ruling, *Roaming Throne*: “Any choices made as you put the ability onto the stack, such as modes and targets, are made separately for each instance of the ability.”
- [CR 603.2](#cr-6032)
- Source (re-verified): [`Doctor_Doom_King_of_Latveria_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/doctor_doom_king_of_latveria_2026-10-14/Doctor_Doom_King_of_Latveria_Rules_Attestation.json) → “Roaming Throne choosing Villain”

## Zones, commander tax and the command zone

### doom-10: Crucible of Worlds doesn't let you cycle lands from the graveyard

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Doctor Doom, King of Latveria, Crucible of Worlds, Dakmor Salvage

**Ruling.** Crucible lets you play lands from your graveyard, still one land drop per turn at sorcery timing. It doesn't let you activate cycling or other abilities of lands there. Its role is replaying discarded lands, not extra Doom triggers.

**Citations**

- Scryfall ruling, *Crucible of Worlds*: “Crucible of Worlds doesn't allow you to activate abilities (such as cycling) of land cards in your graveyard.”
- [CR 305.2](#cr-3052), [CR 702.29a](#cr-70229a)

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 305.2

A player can normally play one land during their turn; however, continuous effects may increase this number.

#### CR 601.2b

If the spell is modal, the player announces the mode choice (see rule 700.2). If the player wishes to splice any cards onto the spell (see rule 702.47), they reveal those cards in their hand. If the spell has alternative or additional costs that will be paid as it’s being cast such as buyback or kicker costs (see rules 118.8 and 118.9), the player announces their intentions to pay any or all of those costs (see rule 601.2f). A player can’t apply two alternative methods of casting or two alternative costs to a single spell. If the spell has a variable cost that will be paid as it’s being cast …

#### CR 602.2

To activate an ability is to put it onto the stack and pay its costs, so that it will eventually resolve and have its effect. Only an object’s controller (or its owner, if it doesn’t have a controller) can activate its activated ability unless the object specifically says otherwise. Activating an ability follows the steps listed below, in order. If, at any point during the activation of an ability, a player is unable to comply with any of those steps, the activation is illegal; the game returns to the moment before that ability started to be activated (see rule 733, “Handling Illegal …

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 603.2c

An ability triggers only once each time its trigger event occurs. However, it can trigger repeatedly if one event contains multiple occurrences.

#### CR 603.3

Once an ability has triggered, its controller puts it on the stack as an object that’s not a card the next time a player would receive priority. See rule 117, “Timing and Priority.” The ability becomes the topmost object on the stack. It has the text of the ability that created it, and no other characteristics. It remains on the stack until it’s countered, it resolves, a rule causes it to be removed from the stack, or an effect moves it elsewhere.

#### CR 605.1a

An activated ability is a mana ability if it meets all of the following criteria: it doesn’t require a target (see rule 115.6), it could add mana to a player’s mana pool when it resolves, it’s not a loyalty ability (see rule 606, “Loyalty Abilities”), and its cost and effect don’t move any card to or from a library. Do not take into account replacement effects that may apply, other than self-replacement effects, when evaluating these criteria.

#### CR 608.2b

If the spell or ability specifies targets, it checks whether the targets are still legal. A target that’s no longer in the zone it was in when it was targeted is illegal. Other changes to the game state may cause a target to no longer be legal; for example, its characteristics may have changed or an effect may have changed the text of the spell. If the source of an ability has left the zone it was in, its last known information is used during this process. If all its targets, for every instance of the word “target,” are now illegal, the spell or ability doesn’t resolve. It’s removed from the …

#### CR 701.9a

To discard a card, move it from its owner’s hand to that player’s graveyard.

#### CR 701.50a

Certain spells and abilities instruct a permanent to connive. To do so, that permanent’s controller draws a card, then discards a card. If a nonland card is discarded this way, that player puts a +1/+1 counter on the conniving permanent.

#### CR 702.29a

Cycling is an activated ability that functions only while the card with cycling is in a player’s hand. “Cycling [cost]” means “[Cost], Discard this card: Draw a card.”

#### CR 702.52a

Dredge is a static ability that functions only while the card with dredge is in a player’s graveyard. “Dredge N” means “As long as you have at least N cards in your library, if you would draw a card, you may instead mill N cards and return this card from your graveyard to your hand.”

#### CR 702.52b

A player with fewer cards in their library than the number required by a dredge ability can’t mill any of them this way.

#### CR 704.5j

If two or more legendary permanents with the same name are controlled by the same player, that player chooses one of them, and the rest are put into their owners’ graveyards. This is called the “legend rule.”

#### CR 707.2

When copying an object, the copy acquires the copiable values of the original object’s characteristics and, for an object on the stack, choices made when casting or activating it (mode, targets, the value of X, whether it was kicked, how it will affect multiple targets, and so on). The copiable values are the values derived from the text printed on the object (that text being name, mana cost, color indicator, card type, subtype, supertype, rules text, power, toughness, and/or loyalty), as modified by other copy effects, by its face-down status, and by “as . . . enters” and “as . . . is turned …

#### CR 707.9b

Some copy effects modify a characteristic as part of the copying process. The final set of values for that characteristic becomes part of the copiable values of the copy.

