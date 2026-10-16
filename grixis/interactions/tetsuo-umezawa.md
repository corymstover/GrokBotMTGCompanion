---
title: "Tetsuo Umezawa — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Tetsuo Umezawa — Interaction Review

> Bot cycle 56 · batch F · reviewed 2026-10-16. Deck: [Tetsuo Umezawa](../decks/tetsuo-umezawa.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/tetsuo-umezawa.txt`](../../exports/grixis-archidekt/tetsuo-umezawa.txt) · SHA-256 `73a45c0240c9b5a86dfdc417d805eadbb171bec3b37e05316e3944bc58656a8f` |
| Rulings | **5** (5 verified · 0 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`Tetsuo_Umezawa_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_umezawa_2026-10-15/gate_output/Tetsuo_Umezawa_Rules_Attestation.json) (Rules attestation (13 items, all PASS) re-verified) · [`Tetsuo_Umezawa_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tetsuo_Umezawa_Approval_Ready_Verification_2026-10-15.md) (Approval-ready verification) |

## Contents
- [Summary](#summary)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [Timing and priority](#timing-and-priority)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [Rules cited](#rules-cited)

## Summary

Tetsuo Umezawa is a removal engine. {U}{B}{B}{R}, {T} destroys a tapped or blocking creature. The deck makes targets (Flood, Puppeteer, Blustersquall, Frozen Aether, goad), untaps Tetsuo (Sting, Patriar's Seal, Minamo, Retreat to Coralhelm) and copies activations (Rings, Bracers). Illusionist's Bracers + Aphetto Alchemist gives unlimited untaps and mana. All 13 attestation items and the one Spellbook line are re-verified against the canonical list.

Rules surprises: tapped OR blocking is enough; only Aura spells can't target Tetsuo; Sting untaps him in every player's combat; overloaded Blustersquall ignores hexproof. No list errors.

## Commander rules text and edge cases

### tetsuou-01: Tetsuo's target: tapped OR blocking, checked again on resolution; only Aura spells can't target him

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Tetsuo Umezawa, Bloodthirsty Blade, Frozen Aether, Propaganda

**Ruling.** Tetsuo can target a creature that's either tapped or blocking; it doesn't need to be both. The target must still qualify when the ability resolves, so an opponent can untap a tapped target to save it.

Ways to get targets:
- Attackers without vigilance tap when declared, and untapped blockers qualify once blocks are declared.
- Frozen Aether makes opponents' creatures enter tapped.
- Bloodthirsty Blade's goad forces attacks, which taps attackers.
- Propaganda doesn't force anyone to pay, so it creates no targets by itself.

"Can't be the target of Aura spells" applies only while casting Auras. Auras can still be moved onto Tetsuo, abilities of Auras can target him, and Equipment and other abilities are unaffected.

**Citations**

- Oracle, *Tetsuo Umezawa*: “{U}{B}{B}{R}, {T}: Destroy target tapped or blocking creature.”
- Oracle, *Frozen Aether*: “Artifacts, creatures, and lands your opponents control enter tapped.”
- Scryfall ruling, *Tetsuo Umezawa*: “This card can be enchanted by moving Auras onto it. The “can’t be the target” text is different from “can’t be enchanted” in that it only applies to Aura spells when they are being cast.”
- Scryfall ruling, *Tetsuo Umezawa*: “Tetsuo Umezawa can be targeted by abilities from Auras.”
- [CR 115.1](#cr-1151), [CR 608.2b](#cr-6082b), [CR 303.4a](#cr-3034a)
- Source (re-verified): [`Tetsuo_Umezawa_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_umezawa_2026-10-15/gate_output/Tetsuo_Umezawa_Rules_Attestation.json) → “Tetsuo target condition”
- Source (re-verified): [`Tetsuo_Umezawa_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_umezawa_2026-10-15/gate_output/Tetsuo_Umezawa_Rules_Attestation.json) → “Combat windows”
- Source (re-verified): [`Tetsuo_Umezawa_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_umezawa_2026-10-15/gate_output/Tetsuo_Umezawa_Rules_Attestation.json) → “Aura restriction”
- Source (re-verified): [`Tetsuo_Umezawa_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_umezawa_2026-10-15/gate_output/Tetsuo_Umezawa_Rules_Attestation.json) → “Frozen Aether and forced combat”

## Combos and engine lines

### tetsuou-03: Illusionist's Bracers + Aphetto Alchemist: infinite untaps, so Tetsuo kills every creature you can tap

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Tetsuo Umezawa, Illusionist's Bracers, Aphetto Alchemist, Arcane Signet, Flood, Puppeteer

**Ruling.** Put Bracers on an Aphetto Alchemist that can tap, then tap Alchemist targeting itself. Bracers copies the ability, and the copy untaps a second target. That gives unlimited untaps of Alchemist and one other artifact or creature each loop (Spellbook 283-4091). Untapping Arcane Signet over and over gives unlimited mana of any color. Untapping Tetsuo lets him activate again and again. Flood ({U}{U}) taps every creature without flying, so with the mana and untaps Tetsuo destroys every non-flying creature. Puppeteer taps flyers too, but only once per untap of itself.

**Citations**

- Oracle, *Aphetto Alchemist*: “{T}: Untap target artifact or creature.”
- Oracle, *Flood*: “{U}{U}: Tap target creature without flying.”
- [CR 707.10](#cr-70710), [CR 605.1a](#cr-6051a)
- Commander Spellbook [283-4091](https://commanderspellbook.com/combo/283-4091/) (community-maintained, retrieved 2026-10-16): “Illusionist's Bracers triggers, copying Aphetto Alchemist's ability targeting any other artifact or creature.”
- Commander Spellbook [283-4091](https://commanderspellbook.com/combo/283-4091/) (community-maintained, retrieved 2026-10-16): “Resolve both Aphetto Alchemist abilities, untapping it and the second target.”
- Source (re-verified): [`Tetsuo_Umezawa_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_umezawa_2026-10-15/gate_output/Tetsuo_Umezawa_Rules_Attestation.json) → “Puppeteer and Flood”

## Engines and payoffs

### tetsuou-02: Copying the activation: Rings of Brighthearth and Illusionist's Bracers

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Tetsuo Umezawa, Rings of Brighthearth, Illusionist's Bracers

**Ruling.** Illusionist's Bracers on Tetsuo copies every activation for free. Rings of Brighthearth copies it for {2}, once per activation. Both copies can choose new targets, so one {U}{B}{B}{R} activation can destroy up to three tapped or blocking creatures. The copies resolve before the original, and resolve even if the original is countered.

**Citations**

- Oracle, *Illusionist's Bracers*: “Whenever an ability of equipped creature is activated, if it isn't a mana ability, copy that ability. You may choose new targets for the copy.”
- Scryfall ruling, *Rings of Brighthearth*: “The triggered ability of Rings of Brighthearth and the copy it creates both resolve before the ability that caused it to trigger. They resolve even if that ability is countered.”
- Scryfall ruling, *Rings of Brighthearth*: “You can't pay {2} more than once for each time the triggered ability of Rings of Brighthearth resolves.”
- [CR 707.10](#cr-70710), [CR 602.1](#cr-6021)
- Source (re-verified): [`Tetsuo_Umezawa_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_umezawa_2026-10-15/gate_output/Tetsuo_Umezawa_Rules_Attestation.json) → “Rings plus Bracers”

## Timing and priority

### tetsuou-04: Untap engines: Sting each combat, Patriar's Seal, Minamo, Puppeteer, Retreat to Coralhelm

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Tetsuo Umezawa, Sting, the Glinting Dagger, Patriar's Seal, Minamo, School at Water's Edge, Puppeteer, Retreat to Coralhelm, Lightning Greaves, Swiftfoot Boots

**Ruling.** Untap engines:
- **Sting** untaps Tetsuo at the beginning of every combat, including opponents' combats. You get priority before attackers are declared, so in multiplayer that's a fresh activation each turn if you have {U}{B}{B}{R}.
- **Patriar's Seal** ({1}, {T}) and **Minamo** ({U}, {T}) untap legendary Tetsuo. One Seal can't both make mana and untap, since both need {T}.
- **Puppeteer** untaps Tetsuo, or taps a target.
- **Retreat to Coralhelm** triggers on each land entering, so a fetchland and the land it finds give two triggers.

Untapping Tetsuo doesn't affect an activation already on the stack. Sting, Lightning Greaves and Swiftfoot Boots give haste, so he can use his {T} ability the turn you gain control of him.

**Citations**

- Oracle, *Sting, the Glinting Dagger*: “At the beginning of each combat, untap equipped creature.”
- Oracle, *Patriar's Seal*: “{1}, {T}: Untap target legendary creature you control.”
- Oracle, *Retreat to Coralhelm*: “Landfall — Whenever a land you control enters, choose one —”
- Scryfall ruling, *Retreat to Coralhelm*: “A landfall ability triggers whenever a land you control enters for any reason. It triggers whenever you play a land, as well as whenever a spell or ability puts a land onto the battlefield under your control.”
- [CR 302.6](#cr-3026), [CR 702.10b](#cr-70210b), [CR 507.1](#cr-5071)
- Source (re-verified): [`Tetsuo_Umezawa_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_umezawa_2026-10-15/gate_output/Tetsuo_Umezawa_Rules_Attestation.json) → “Sting the Glinting Dagger”
- Source (re-verified): [`Tetsuo_Umezawa_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_umezawa_2026-10-15/gate_output/Tetsuo_Umezawa_Rules_Attestation.json) → “Untap after activation”
- Source (re-verified): [`Tetsuo_Umezawa_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_umezawa_2026-10-15/gate_output/Tetsuo_Umezawa_Rules_Attestation.json) → “Patriars Seal”
- Source (re-verified): [`Tetsuo_Umezawa_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_umezawa_2026-10-15/gate_output/Tetsuo_Umezawa_Rules_Attestation.json) → “Retreat plus fetchlands”
- Source (re-verified): [`Tetsuo_Umezawa_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_umezawa_2026-10-15/gate_output/Tetsuo_Umezawa_Rules_Attestation.json) → “Haste package”

## Zones, commander tax and the command zone

### tetsuou-05: Blustersquall overload and Sink into Stupor

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Tetsuo Umezawa, Blustersquall, Sink into Stupor // Soporific Springs

**Ruling.** Blustersquall's normal cast taps one target creature. Overloaded, it taps every creature you don't control without targeting, so hexproof and protection don't stop it. That makes the whole table legal Tetsuo targets. Cast without paying its mana cost, it can't be overloaded. Sink into Stupor bounces a spell or nonland permanent rather than countering it, and the MDFC can be played as Soporific Springs instead.

**Citations**

- Scryfall ruling, *Blustersquall*: “Because a spell with overload doesn't target when its overload cost is paid, it may affect permanents with hexproof or with protection from the appropriate color.”
- Scryfall ruling, *Blustersquall*: “If you are instructed to cast a spell with overload "without paying its mana cost," you can't choose to pay its overload cost instead.”
- [CR 702.96a](#cr-70296a), [CR 712.12](#cr-71212)
- Source (re-verified): [`Tetsuo_Umezawa_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_umezawa_2026-10-15/gate_output/Tetsuo_Umezawa_Rules_Attestation.json) → “Blustersquall”
- Source (re-verified): [`Tetsuo_Umezawa_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/tetsuo_umezawa_2026-10-15/gate_output/Tetsuo_Umezawa_Rules_Attestation.json) → “Sink into Stupor MDFC”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 115.1

Some spells and abilities require their controller to choose one or more targets for them. The targets are object(s) and/or player(s) the spell or ability will affect. These targets are declared as part of the process of putting the spell or ability on the stack. The targets can’t be changed except by another spell or ability that explicitly says it can do so.

#### CR 302.6

A creature’s activated ability with the tap symbol or the untap symbol in its activation cost can’t be activated unless the creature has been under its controller’s control continuously since their most recent turn began. A creature can’t attack unless it has been under its controller’s control continuously since their most recent turn began. This rule is informally called the “summoning sickness” rule.

#### CR 303.4a

An Aura spell requires a target, which is defined by its enchant ability.

#### CR 507.1

First, if the game being played is a multiplayer game in which the active player’s opponents don’t all automatically become defending players, the active player chooses one of their opponents. That player becomes the defending player. This turn-based action doesn’t use the stack. (See rule 506.2.)

#### CR 602.1

Activated abilities have a cost and an effect. They are written as “[Cost]: [Effect.] [Activation instructions (if any).]”

#### CR 605.1a

An activated ability is a mana ability if it meets all of the following criteria: it doesn’t require a target (see rule 115.6), it could add mana to a player’s mana pool when it resolves, it’s not a loyalty ability (see rule 606, “Loyalty Abilities”), and its cost and effect don’t move any card to or from a library. Do not take into account replacement effects that may apply, other than self-replacement effects, when evaluating these criteria.

#### CR 608.2b

If the spell or ability specifies targets, it checks whether the targets are still legal. A target that’s no longer in the zone it was in when it was targeted is illegal. Other changes to the game state may cause a target to no longer be legal; for example, its characteristics may have changed or an effect may have changed the text of the spell. If the source of an ability has left the zone it was in, its last known information is used during this process. If all its targets, for every instance of the word “target,” are now illegal, the spell or ability doesn’t resolve. It’s removed from the …

#### CR 702.10b

If a creature has haste, it can attack even if it hasn’t been controlled by its controller continuously since their most recent turn began. (See rule 302.6.)

#### CR 702.96a

Overload is a keyword that represents two static abilities that function while the spell with overload is on the stack. Overload [cost] means “You may choose to pay [cost] rather than pay this spell’s mana cost” and “If you chose to pay this spell’s overload cost, change its text by replacing all instances of the word ‘target’ with the word ‘each.’” Casting a spell using its overload ability follows the rules for paying alternative costs in rules 601.2b and 601.2f–h.

#### CR 707.10

To copy a spell, activated ability, or triggered ability means to put a copy of it onto the stack; a copy of a spell isn’t cast and a copy of an activated ability isn’t activated. A copy of a spell or ability copies both the characteristics of the spell or ability and all decisions made for it, including modes, targets, the value of X, and additional or alternative costs. (See rule 601, “Casting Spells.”) Choices that are normally made on resolution are not copied. If an effect of the copy refers to objects used to pay its costs, it uses the objects used to pay the costs of the original spell …

#### CR 712.12

A player playing a modal double-faced card or a copy of a modal double-faced card as a land chooses one of its faces that’s a land before putting it onto the battlefield. It enters the battlefield with that face up. See rule 305, “Lands.”

