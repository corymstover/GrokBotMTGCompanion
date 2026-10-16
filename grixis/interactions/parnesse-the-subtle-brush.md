---
title: "Parnesse, the Subtle Brush — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Parnesse, the Subtle Brush — Interaction Review

> Bot cycle 54 · batch E · reviewed 2026-10-16. Deck: [Parnesse, the Subtle Brush](../decks/parnesse-the-subtle-brush.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/parnesse-the-subtle-brush.txt`](../../exports/grixis-archidekt/parnesse-the-subtle-brush.txt) · SHA-256 `8c32a449aa6ee96ff110e1813f40a6797b0dea722a57acdd91e0ac93e78fd93b` |
| Rulings | **10** (8 verified · 1 uncertain · 1 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`Parnesse_the_Subtle_Brush_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/parnesse_2026-10-15/gate_output/Parnesse_the_Subtle_Brush_Rules_Attestation.json) (Rules attestation (12 items, all PASS) re-verified) · [`Parnesse_the_Subtle_Brush_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Parnesse_the_Subtle_Brush_Approval_Ready_Verification_2026-10-15.md) (Approval-ready verification) |

## Contents
- [Summary](#summary)
- [Flags and open questions](#flags-and-open-questions)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Replacement and prevention effects](#replacement-and-prevention-effects)
- [Trigger ordering](#trigger-ordering)
- [What the list depends on](#what-the-list-depends-on)
- [Rules cited](#rules-cited)

## Summary

Parnesse taxes anything an opponent aims at you 4 life, and lets an opponent share your spell copies, which is always optional. The list is a copy-spell storm deck: Reiterate, Reverberate, Increasing Vengeance and Return the Favor loop with Prismari, Goggles, Alania, Thousand-Year Storm or Narset's Reversal, and Ral or Professor Onyx turns the unlimited magecraft into a win. Mana comes from Reiterate + Mana Geyser or Jeska's Will, and Storm-Kiln Artist with Bonus Round. All 25 Spellbook lines and all 12 attestation items are checked against the canonical list.

Rules surprises: Mizzix's Mastery's 'cast a copy of the card' isn't 'copying a spell'; Harmonic Prodigy also doubles Storm-Kiln (a Shaman); Bonus Round copies opponents' responses too.

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [parnesse-07](#parnesse-07-bonus-round-is-symmetric-opponents-responses-get-copied-too) | 🚩 list flag (anti-synergy) | Bonus Round is symmetric: opponents' responses get copied too | Bonus Round copies opponents' instant or sorcery responses during your combo turn (a doubled counterspell or removal). It's a sequencing risk, not a list error. |
| [parnesse-10](#parnesse-10-do-opponents-retargeted-parnesse-copies-hit-her-own-4-life-tax) | ⚠️ uncertain | Do opponents' retargeted Parnesse copies hit her own 4-life tax? | No Parnesse ruling addresses copies created with new targets; derived from 707.10c only. |

## Commander rules text and edge cases

### parnesse-01: What counts as 'you copy a spell': stack copies yes, cast-a-copy-of-a-card no

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Parnesse, the Subtle Brush, Mizzix's Mastery, Reiterate, Narset's Reversal, Prismari, the Inspiration, Thunderclap Drake

**Ruling.** Parnesse triggers when you put a copy of a spell onto the stack. Reiterate, Narset's Reversal, Increasing Vengeance, Reverberate, Return the Favor, storm (Prismari), Pyromancer's Goggles, Alania, Bonus Round, Thunderclap Drake, Twinning Staff and Ral's −2 all do that. Mizzix's Mastery doesn't. It copies a card in exile and lets you cast that copy, which is casting, not copying a spell. That's why the source cut Arcane Bombardment. Cast copies still set off magecraft.

**Citations**

- Oracle, *Parnesse, the Subtle Brush*: “Whenever you copy a spell, up to one target opponent may also copy that spell. They may choose new targets for that copy.”
- Scryfall ruling, *Veyran, Voice of Duality*: “Some effects instruct you to copy an instant or sorcery card in a zone other than the stack. These copies do not cause magecraft abilities to trigger. However, most effects that do this also allow you to cast the copy, and casting the copy will cause magecraft abilities to trigger.”
- [CR 707.10](#cr-70710), [CR 707.12](#cr-70712), [CR 702.40a](#cr-70240a)
- Source (re-verified): [`Parnesse_the_Subtle_Brush_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/parnesse_2026-10-15/gate_output/Parnesse_the_Subtle_Brush_Rules_Attestation.json) → “Parnesse spell-copy boundary”
- Source (re-verified): [`Parnesse_the_Subtle_Brush_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/parnesse_2026-10-15/gate_output/Parnesse_the_Subtle_Brush_Rules_Attestation.json) → “Arcane Bombardment exclusion”
- Source (re-verified): [`Parnesse_the_Subtle_Brush_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/parnesse_2026-10-15/gate_output/Parnesse_the_Subtle_Brush_Rules_Attestation.json) → “Mizzix's Mastery classification”

### parnesse-02: Parnesse's protection is a ward-like trigger worth 4 life; her gift is optional

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Parnesse, the Subtle Brush

**Ruling.** Parnesse's first ability triggers when you or your permanents become the target of an opponent's spell or ability. It counters that spell or ability unless they pay 4 life. It's a triggered ability like ward, so it uses the stack and can be Stifled. It also covers you as a player, not just your permanents. Her second ability targets "up to one" opponent, so you can always choose no one. Every extra Parnesse trigger from Wizard's Staff, Harmonic Prodigy or Veyran is also optional to aim.

**Citations**

- Oracle, *Parnesse, the Subtle Brush*: “Whenever you or a permanent you control becomes the target of a spell or ability an opponent controls, counter that spell or ability unless that player pays 4 life.”
- [CR 702.21a](#cr-70221a), [CR 115.1](#cr-1151), [CR 603.3d](#cr-6033d)
- Source (re-verified): [`Parnesse_the_Subtle_Brush_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/parnesse_2026-10-15/gate_output/Parnesse_the_Subtle_Brush_Rules_Attestation.json) → “Reiterate + Mana Geyser”

## Combos and engine lines

### parnesse-04: Copy-the-copier loops: Reiterate / Reverberate / Increasing Vengeance / Return the Favor with storm, Goggles, Alania, Thousand-Year Storm or Narset's Reversal

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Parnesse, the Subtle Brush, Reiterate, Reverberate, Increasing Vengeance, Return the Favor, Narset's Reversal, Prismari, the Inspiration, Pyromancer's Goggles, Alania, Divergent Storm, Thousand-Year Storm, Ral, Storm Conduit, Professor Onyx

**Ruling.** The copy spell targets some spell. A second copy source (storm from Prismari, Goggles' mana, Alania's first-sorcery trigger, Thousand-Year Storm, or Narset's Reversal) then copies the copy spell, and that copy targets the original copy spell. Each resolution copies it again, giving unlimited copies and magecraft triggers. Ral's 1 damage or Onyx's drain per copy finishes the game. Parnesse triggers on every copy, but her gift is optional, so the loop is unaffected.

**Citations**

- Oracle, *Ral, Storm Conduit*: “Whenever you cast or copy an instant or sorcery spell, Ral deals 1 damage to target opponent or planeswalker.”
- Oracle, *Professor Onyx*: “Magecraft — Whenever you cast or copy an instant or sorcery spell, each opponent loses 2 life and you gain 2 life.”
- Scryfall ruling, *Narset's Reversal*: “If a copy of a spell is returned to its owner’s hand, it’s moved there, then it will cease to exist as a state-based action.”
- [CR 707.10](#cr-70710), [CR 707.10c](#cr-70710c)
- Commander Spellbook [3368-7683](https://commanderspellbook.com/combo/3368-7683/) (community-maintained, retrieved 2026-10-16): “Reiterate's storm ability triggers, creating at least one copy of Reiterate targeting the original Reiterate.”
- Commander Spellbook [3368-6790](https://commanderspellbook.com/combo/3368-6790/) (community-maintained, retrieved 2026-10-16): “Pyromancer's Goggles triggers, copying Reiterate, with the copy targeting the original Reiterate.”
- Commander Spellbook [11-3368](https://commanderspellbook.com/combo/11-3368/) (community-maintained, retrieved 2026-10-16): “Cast Narset's Reversal by paying {U}{U}, copying Reiterate targeting the spell cast in step 1 and returning the original Reiterate to your hand.”
- Commander Spellbook [3368-5959](https://commanderspellbook.com/combo/3368-5959/) (community-maintained, retrieved 2026-10-16): “Alania triggers, causing an opponent to draw a card and you to copy Reiterate, with the copy targeting the original Reiterate.”
- Source (re-verified): [`Parnesse_the_Subtle_Brush_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/parnesse_2026-10-15/gate_output/Parnesse_the_Subtle_Brush_Rules_Attestation.json) → “Prismari, the Inspiration / storm”

### parnesse-05: Reiterate with buyback + Mana Geyser or Jeska's Will: infinite red mana

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Parnesse, the Subtle Brush, Reiterate, Mana Geyser, Jeska's Will

**Ruling.** Cast Mana Geyser, or Jeska's Will on an opponent with a big hand. Holding priority, cast Reiterate with buyback for {4}{R}{R} to copy it. If the copy makes six or more {R}, you can repeat for unlimited copies and magecraft. Seven or more nets mana each loop. Jeska's Will copies keep the modes chosen for the original, both modes if you controlled a commander when you cast it, and its target opponent's hand size sets the mana.

**Citations**

- Oracle, *Mana Geyser*: “Add {R} for each tapped land your opponents control.”
- Scryfall ruling, *Reiterate*: “If the spell that's copied is modal (that is, it says "Choose one —" or the like), the copy will have the same mode. A different mode can't be chosen.”
- [CR 707.10](#cr-70710), [CR 702.27a](#cr-70227a)
- Commander Spellbook [2091-3368](https://commanderspellbook.com/combo/2091-3368/) (community-maintained, retrieved 2026-10-16): “Holding priority, cast Reiterate with buyback by paying {4}{R}{R}, creating a copy of Mana Geyser and returning Reiterate to your hand.”
- Commander Spellbook [1878-3368](https://commanderspellbook.com/combo/1878-3368/) (community-maintained, retrieved 2026-10-16): “Holding priority, cast Reiterate with buyback by paying {4}{R}{R}, creating a copy of Jeska's Will and returning Reiterate to your hand.”
- Source (re-verified): [`Parnesse_the_Subtle_Brush_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/parnesse_2026-10-15/gate_output/Parnesse_the_Subtle_Brush_Rules_Attestation.json) → “Reiterate + Mana Geyser”

### parnesse-06: Storm-Kiln Artist Treasure engines: Bonus Round or Thousand-Year Storm + Narset's Reversal

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Parnesse, the Subtle Brush, Storm-Kiln Artist, Bonus Round, Thousand-Year Storm, Narset's Reversal

**Ruling.** Storm-Kiln makes a Treasure each time you cast or copy an instant or sorcery. With Bonus Round copying each spell, Narset's Reversal copies the spell and bounces it to recast. That nets Treasures each loop, so you get unlimited Treasures and magecraft. Harmonic Prodigy doubles Storm-Kiln's Treasures.

**Citations**

- Oracle, *Bonus Round*: “Until end of turn, whenever a player casts an instant or sorcery spell, that player copies it and may choose new targets for the copy.”
- Scryfall ruling, *Storm-Kiln Artist*: “If an effect creates multiple copies of an instant or sorcery spell, magecraft abilities trigger once for each copy created by the effect.”
- [CR 707.10](#cr-70710)
- Commander Spellbook [11-2492-5195](https://commanderspellbook.com/combo/11-2492-5195/) (community-maintained, retrieved 2026-10-16): “Resolve the Bonus Round trigger, copying the instant or sorcery.”
- Commander Spellbook [11-3584-5195](https://commanderspellbook.com/combo/11-3584-5195/) (community-maintained, retrieved 2026-10-16): “Resolve the Storm-Kiln Artist trigger, creating a Treasure artifact token.”

### parnesse-09: Primal Wellspring + Frantic Search + Reiterate / Narset's Reversal

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Parnesse, the Subtle Brush, Primal Amulet // Primal Wellspring, Frantic Search, Reiterate, Narset's Reversal

**Ruling.** Wellspring mana spent on Frantic Search copies it. The copy untaps Wellspring and two other lands, which pays for Frantic Search again. Reiterate or Narset's Reversal re-buys the original to keep looting through the deck. Each copy is a Parnesse trigger and a magecraft trigger.

**Citations**

- [CR 707.10](#cr-70710)
- Commander Spellbook [1484-2196-3368](https://commanderspellbook.com/combo/1484-2196-3368/) (community-maintained, retrieved 2026-10-16): “Primal Wellspring triggers, copying Frantic Search.”
- Commander Spellbook [11-1484-2196](https://commanderspellbook.com/combo/11-1484-2196/) (community-maintained, retrieved 2026-10-16): “Resolve the copy of Frantic Search, looting twice and untapping Primal Wellspring and the two other lands.”

## Replacement and prevention effects

### parnesse-08: Twinning Staff, Tempt with Mayhem, demonstrate (Replication Technique), Sunken Palace

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Parnesse, the Subtle Brush, Twinning Staff, Tempt with Mayhem, Replication Technique, Dualcaster Mage, Sunken Palace

**Ruling.** Each of these interacts with Parnesse differently:
- **Twinning Staff:** each copy event makes one more copy, and that extra copy is another Parnesse trigger. A Mizzix's Mastery card copy gets no extra copy.
- **Tempt with Mayhem:** you make at least one copy, plus one for each opponent who copies. Only your copies trigger Parnesse.
- **Demonstrate:** your Replication Technique copy triggers Parnesse; the chosen opponent's copy doesn't. With Dualcaster Mage, Technique gives unlimited Mage tokens (Spellbook 147-1883).
- **Sunken Palace:** its mana copies the spell or ability it pays for. Parnesse triggers only when that's a spell.

**Citations**

- Oracle, *Twinning Staff*: “If you would copy a spell one or more times, instead copy it that many times plus an additional time. You may choose new targets for the additional copy.”
- Scryfall ruling, *Twinning Staff*: “If an effect copies a card rather than a spell (such as that of God-Eternal Kefnet), this doesn't cause an additional copy to be created.”
- Scryfall ruling, *Replication Technique*: “If you cast the spell and choose not to copy it, no opponent will get to copy it either.”
- [CR 614.1a](#cr-6141a), [CR 702.144a](#cr-702144a), [CR 707.10](#cr-70710)
- Commander Spellbook [147-1883](https://commanderspellbook.com/combo/147-1883/) (community-maintained, retrieved 2026-10-16): “When Dualcaster Mage enters the battlefield, it triggers, copying Replication Technique, targeting Dualcaster Mage.”
- Source (re-verified): [`Parnesse_the_Subtle_Brush_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/parnesse_2026-10-15/gate_output/Parnesse_the_Subtle_Brush_Rules_Attestation.json) → “Twinning Staff”
- Source (re-verified): [`Parnesse_the_Subtle_Brush_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/parnesse_2026-10-15/gate_output/Parnesse_the_Subtle_Brush_Rules_Attestation.json) → “Tempt with Mayhem”
- Source (re-verified): [`Parnesse_the_Subtle_Brush_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/parnesse_2026-10-15/gate_output/Parnesse_the_Subtle_Brush_Rules_Attestation.json) → “Replication Technique / demonstrate”
- Source (re-verified): [`Parnesse_the_Subtle_Brush_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/parnesse_2026-10-15/gate_output/Parnesse_the_Subtle_Brush_Rules_Attestation.json) → “Sunken Palace”

## Trigger ordering

### parnesse-03: Trigger doublers: Wizard's Staff, Harmonic Prodigy, Veyran double magecraft and Treasures

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Parnesse, the Subtle Brush, Wizard's Staff, Harmonic Prodigy, Veyran, Voice of Duality, Storm-Kiln Artist, Ral, Storm Conduit, Professor Onyx

**Ruling.** Parnesse is a Vampire Wizard, so Wizard's Staff costs {1} to equip and Harmonic Prodigy doubles her triggers. The real payoff is elsewhere:
- Prodigy also doubles Storm-Kiln Artist (a Dwarf Shaman) and the other Wizards (Veyran, Alania, Dualcaster).
- Veyran makes every cast-or-copy trigger fire again, including Ral's ping, Professor Onyx's drain and Storm-Kiln's Treasure.

These stack by adding, and each copy from a single effect triggers magecraft separately.

**Citations**

- Oracle, *Harmonic Prodigy*: “If a triggered ability of a Shaman or another Wizard you control triggers, that ability triggers an additional time.”
- Oracle, *Veyran, Voice of Duality*: “If you casting or copying an instant or sorcery spell causes a triggered ability of a permanent you control to trigger, that ability triggers an additional time.”
- Scryfall ruling, *Veyran, Voice of Duality*: “If an effect creates multiple copies of an instant or sorcery spell, magecraft abilities trigger once for each copy created by the effect.”
- [CR 603.2d](#cr-6032d)
- Source (re-verified): [`Parnesse_the_Subtle_Brush_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/parnesse_2026-10-15/gate_output/Parnesse_the_Subtle_Brush_Rules_Attestation.json) → “Wizard's Staff”
- Source (re-verified): [`Parnesse_the_Subtle_Brush_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/parnesse_2026-10-15/gate_output/Parnesse_the_Subtle_Brush_Rules_Attestation.json) → “Harmonic Prodigy”
- Source (re-verified): [`Parnesse_the_Subtle_Brush_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/parnesse_2026-10-15/gate_output/Parnesse_the_Subtle_Brush_Rules_Attestation.json) → “Veyran, Voice of Duality”

### parnesse-10: Do opponents' retargeted Parnesse copies hit her own 4-life tax?

**Status:** ⚠️ uncertain · **Evidence:** hypothesis · **Cards:** Parnesse, the Subtle Brush

**Ruling.** When you give an opponent a Parnesse copy, they may choose new targets for it. If they aim it at you or your permanents, the copy goes on the stack with those targets, and it's a spell that opponent controls. That suggests Parnesse's first ability triggers on it, the same way ward does on retargeted copies. No official ruling on Parnesse confirms this.

**Uncertain.** No Parnesse ruling addresses copies created with new targets; derived from 707.10c only.

**Citations**

- Oracle, *Parnesse, the Subtle Brush*: “Whenever you or a permanent you control becomes the target of a spell or ability an opponent controls, counter that spell or ability unless that player pays 4 life.”
- [CR 707.10c](#cr-70710c), [CR 702.21a](#cr-70221a)

## What the list depends on

### parnesse-07: Bonus Round is symmetric: opponents' responses get copied too

**Status:** 🚩 list flag · **Evidence:** fact · **Cards:** Parnesse, the Subtle Brush, Bonus Round

**Ruling.** Bonus Round works for every player until end of turn, not just you. On your combo turn, an opponent's instant cast in response gets copied as well, so a counterspell or removal spell comes in twice. Copies of their spells that target you or your permanents still run into Parnesse's 4-life tax. Cast Bonus Round when the table is tapped out, or with protection backup.

**List flag (anti-synergy).** Bonus Round copies opponents' instant or sorcery responses during your combo turn (a doubled counterspell or removal). It's a sequencing risk, not a list error.

**Citations**

- Oracle, *Bonus Round*: “Until end of turn, whenever a player casts an instant or sorcery spell, that player copies it and may choose new targets for the copy.”
- [CR 707.10](#cr-70710)

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 115.1

Some spells and abilities require their controller to choose one or more targets for them. The targets are object(s) and/or player(s) the spell or ability will affect. These targets are declared as part of the process of putting the spell or ability on the stack. The targets can’t be changed except by another spell or ability that explicitly says it can do so.

#### CR 603.2d

An ability may state that a triggered ability triggers additional times. In this case, rather than simply determining that such an ability has triggered, determine how many times it should trigger, then that ability triggers that many times. An effect that states that an ability triggers additional times doesn’t invoke itself repeatedly and doesn’t apply to other effects that affect how many times an ability triggers. An effect that states a triggered ability of an object triggers additional times refers only to triggered abilities that object has, not to any delayed or reflexive triggered …

#### CR 603.3d

The remainder of the process for putting a triggered ability on the stack is identical to the process for casting a spell listed in rules 601.2c–d. If a choice is required when the triggered ability goes on the stack but no legal choices can be made for it, or if a rule or a continuous effect otherwise makes the ability illegal, the ability is simply removed from the stack.

#### CR 614.1a

Effects that use the word “instead” are replacement effects. Most replacement effects use the word “instead” to indicate what events will be replaced with other events.

#### CR 702.21a

Ward is a triggered ability. Ward [cost] means “Whenever this permanent becomes the target of a spell or ability an opponent controls, counter that spell or ability unless that player pays [cost].”

#### CR 702.27a

Buyback appears on some instants and sorceries. It represents two static abilities that function while the spell is on the stack. “Buyback [cost]” means “You may pay an additional [cost] as you cast this spell” and “If the buyback cost was paid, put this spell into its owner’s hand instead of into that player’s graveyard as it resolves.” Paying a spell’s buyback cost follows the rules for paying additional costs in rules 601.2b and 601.2f–h.

#### CR 702.40a

Storm is a triggered ability that functions on the stack. “Storm” means “When you cast this spell, copy it for each other spell that was cast before it this turn. If the spell has any targets, you may choose new targets for any of the copies.”

#### CR 702.144a

Demonstrate is a triggered ability. “Demonstrate” means “When you cast this spell, you may copy it and you may choose new targets for the copy. If you copy the spell, choose an opponent. That player copies the spell and may choose new targets for that copy.”

#### CR 707.10

To copy a spell, activated ability, or triggered ability means to put a copy of it onto the stack; a copy of a spell isn’t cast and a copy of an activated ability isn’t activated. A copy of a spell or ability copies both the characteristics of the spell or ability and all decisions made for it, including modes, targets, the value of X, and additional or alternative costs. (See rule 601, “Casting Spells.”) Choices that are normally made on resolution are not copied. If an effect of the copy refers to objects used to pay its costs, it uses the objects used to pay the costs of the original spell …

#### CR 707.10c

Some effects copy a spell or ability and state that its controller may choose new targets for the copy. The player may leave any number of the targets unchanged, even if those targets would be illegal. If the player chooses to change some or all of the targets, the new targets must be legal. Once the player has decided what the copy’s targets will be, the copy is put onto the stack with those targets.

#### CR 707.12

An effect that instructs a player to cast a copy of an object (and not just copy a spell) follows the rules for casting spells, except that the copy is created in the same zone the object is in and then cast while another spell or ability is resolving. Casting a copy of an object follows steps 601.2a–h of rule 601, “Casting Spells,” and then the copy becomes cast. Once cast, the copy is a spell on the stack, and just like any other spell it can resolve or be countered.

