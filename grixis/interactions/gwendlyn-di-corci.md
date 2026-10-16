---
title: "Gwendlyn Di Corci — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Gwendlyn Di Corci — Interaction Review

> Bot cycle 49 · batch C · reviewed 2026-10-16. Deck: [Gwendlyn Di Corci](../decks/gwendlyn-di-corci.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-15), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Current list | [`exports/grixis-archidekt/gwendlyn-di-corci.txt`](../../exports/grixis-archidekt/gwendlyn-di-corci.txt) · SHA-256 `4120c13480a4daa65cfd672e720c9e8a7bc83b7964730aaf342bf1da44589ca4` |
| Rulings | **10** (8 verified · 0 uncertain · 2 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-15 · rulings 2026-10-15 |
| Source attestations | [`Gwendlyn_Di_Corci_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/gwendlyn_di_corci_2026-10-14/Gwendlyn_Di_Corci_Rules_Attestation.json) (15 interactions, all PASS) |

## Contents
- [Summary](#summary)
- [Flags and open questions](#flags-and-open-questions)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [Key card-pair interactions](#key-card-pair-interactions)
- [Replacement and prevention effects](#replacement-and-prevention-effects)
- [Trigger ordering](#trigger-ordering)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [What the list depends on](#what-the-list-depends-on)
- [Rules cited](#rules-cited)

## Summary

Gwendlyn Di Corci taps on your turn to make a player discard at random. The deck stacks untappers, Illusionist's Bracers and discard payoffs. This review re-verifies the fifteen items of the deck's rules attestation and confirms its one Spellbook combo.

Rules surprises (pilot notes, no list change):
- Lightning Greaves' shroud blocks the deck's own targeted untappers and Bracers' equip.
- Chains of Mephistopheles turns your own wheels into self-mill.

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [gwendlyn-04](#gwendlyn-04-shroud-on-gwendlyn-turns-off-the-targeted-untappers-but-not-pemmins-own-untap) | 🚩 list flag (anti-synergy) | Shroud on Gwendlyn turns off the targeted untappers, but not Pemmin's own untap | Pilot note, not a list error: Lightning Greaves (the haste piece) shrouds Gwendlyn against the deck's own targeted untappers and Bracers. Equip Bracers first, or move Greaves away ({0}, sorcery speed) before untapping her with Minamo, Magewright's Stone or Patriar's Seal. The source notes this for Pemmin's shroud only. |
| [gwendlyn-06](#gwendlyn-06-chains-of-mephistopheles-hits-wheels-yours-included) | 🚩 list flag (anti-synergy) | Chains of Mephistopheles hits wheels, yours included | Pilot note, not a list error: Chains of Mephistopheles is symmetric. Don't run the Breach + LED + Wheel draw engine with Chains on the battlefield unless milling is the goal. |

## Commander rules text and edge cases

### gwendlyn-01: Tap ability: your turn only, and summoning sickness applies

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Gwendlyn Di Corci, Lightning Greaves, Thousand-Year Elixir

**Ruling.** Gwendlyn's ability has {T} in its cost, so she needs haste or to have been under your control since your turn began. Lightning Greaves gives haste. Thousand-Year Elixir lets creature abilities be activated as though they had haste, but doesn't actually grant haste, so she still can't attack. The ability targets a player, so Gwendlyn having shroud doesn't stop it.

**Citations**

- Oracle, *Gwendlyn Di Corci*: “{T}: Target player discards a card at random. Activate only during your turn.”
- Oracle, *Thousand-Year Elixir*: “You may activate abilities of creatures you control as though those creatures had haste.”
- Scryfall ruling, *Thousand-Year Elixir*: “Thousand-Year Elixir doesn’t actually grant haste to creatures you control, nor does it let you attack with them as though they had haste.”
- [CR 302.6](#cr-3026), [CR 602.5](#cr-6025), [CR 115.1](#cr-1151)
- Source (re-verified): [`Gwendlyn_Di_Corci_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/gwendlyn_di_corci_2026-10-14/Gwendlyn_Di_Corci_Rules_Attestation.json) → “Gwendlyn activation timing and summoning sickness”

## Combos and engine lines

### gwendlyn-10: Underworld Breach + LED + Wheel of Fortune

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Gwendlyn Di Corci, Underworld Breach, Lion's Eye Diamond, Wheel of Fortune

**Ruling.** LED discards your hand for {R}{R}{R}. Escape Wheel ({2}{R} plus three cards) to refill hands, escape LED for three more cards, and repeat. It needs six other cards in hand and/or graveyard. It's a draw and storm engine, not a kill. Each player discarding their hand to Wheel also triggers Liliana's Caress per card and Tinybones per player.

**Citations**

- [CR 702.138a](#cr-702138a)
- Commander Spellbook [1368-2706-3518](https://commanderspellbook.com/combo/1368-2706-3518/) (community-maintained, retrieved 2026-10-16): “You have at least six other cards in hand and/or graveyard.”
- Commander Spellbook [1368-2706-3518](https://commanderspellbook.com/combo/1368-2706-3518/) (community-maintained, retrieved 2026-10-16): “Activate Lion's Eye Diamond by discarding your hand and sacrificing it, adding {R}{R}{R}.”

## Engines and payoffs

### gwendlyn-03: Untappers: Pemmin's Aura, Minamo, Magewright's Stone, Patriar's Seal

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Gwendlyn Di Corci, Pemmin's Aura, Minamo, School at Water's Edge, Magewright's Stone, Patriar's Seal

**Ruling.** Each untap gives another activation that turn. Pemmin's Aura: {U}, doesn't target. Minamo: {U} and tap, targets a legendary permanent; it can't also tap for the {U}, so that needs another blue source. Magewright's Stone: {1}, targets a creature with a {T} ability. Patriar's Seal: {1}, targets a legendary creature you control; it can't tap for mana and untap in the same activation. None of them is a loop by itself: each untap costs mana.

**Citations**

- Oracle, *Pemmin's Aura*: “{U}: Untap enchanted creature.”
- Oracle, *Minamo, School at Water's Edge*: “{U}, {T}: Untap target legendary permanent.”
- Oracle, *Magewright's Stone*: “{1}, {T}: Untap target creature that has an activated ability with {T} in its cost.”
- Oracle, *Patriar's Seal*: “{1}, {T}: Untap target legendary creature you control.”
- [CR 602.2](#cr-6022), [CR 115.1](#cr-1151)
- Source (re-verified): [`Gwendlyn_Di_Corci_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/gwendlyn_di_corci_2026-10-14/Gwendlyn_Di_Corci_Rules_Attestation.json) → “Pemmin's Aura repeatable untap”
- Source (re-verified): [`Gwendlyn_Di_Corci_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/gwendlyn_di_corci_2026-10-14/Gwendlyn_Di_Corci_Rules_Attestation.json) → “Minamo commander untap”
- Source (re-verified): [`Gwendlyn_Di_Corci_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/gwendlyn_di_corci_2026-10-14/Gwendlyn_Di_Corci_Rules_Attestation.json) → “Magewright's Stone and Patriar's Seal”

### gwendlyn-05: Discard payoffs: per card vs per event

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Gwendlyn Di Corci, Tinybones, Pocket Nuisance, Liliana's Caress, Geth's Grimoire, Mind Twist

**Ruling.** Liliana's Caress (2 life) and Geth's Grimoire (may draw) trigger for each card an opponent discards. Tinybones uses 'one or more cards' and triggers once per player per discard event: it deals 1 to each opponent, and any player's discard counts, yours included. Mind Twist for X is one event of X cards: X Caress triggers, one Tinybones trigger. Each Gwendlyn activation is its own event.

**Citations**

- Oracle, *Tinybones, Pocket Nuisance*: “Whenever a player discards one or more cards, Tinybones deals 1 damage to each opponent.”
- Oracle, *Liliana's Caress*: “Whenever an opponent discards a card, that player loses 2 life.”
- [CR 603.2c](#cr-6032c), [CR 701.9a](#cr-7019a)
- Source (re-verified): [`Gwendlyn_Di_Corci_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/gwendlyn_di_corci_2026-10-14/Gwendlyn_Di_Corci_Rules_Attestation.json) → “Tinybones, Pocket Nuisance discard trigger”
- Source (re-verified): [`Gwendlyn_Di_Corci_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/gwendlyn_di_corci_2026-10-14/Gwendlyn_Di_Corci_Rules_Attestation.json) → “Discard payoff granularity”
- Source (re-verified): [`Gwendlyn_Di_Corci_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/gwendlyn_di_corci_2026-10-14/Gwendlyn_Di_Corci_Rules_Attestation.json) → “Mind Twist random discard”

## Key card-pair interactions

### gwendlyn-04: Shroud on Gwendlyn turns off the targeted untappers, but not Pemmin's own untap

**Status:** 🚩 list flag · **Evidence:** fact · **Cards:** Gwendlyn Di Corci, Pemmin's Aura, Lightning Greaves, Minamo, School at Water's Edge, Illusionist's Bracers

**Ruling.** Shroud means nothing can target her, your own effects included. With Pemmin's shroud mode or Lightning Greaves, Minamo, Magewright's Stone and Patriar's Seal can't untap her, and you can't equip Illusionist's Bracers (equip targets). Pemmin's Aura stays attached (it only targeted as a spell), and its {U} untap doesn't target, so it still works through shroud. Greaves can be moved off for {0}, at sorcery speed.

**List flag (anti-synergy).** Pilot note, not a list error: Lightning Greaves (the haste piece) shrouds Gwendlyn against the deck's own targeted untappers and Bracers. Equip Bracers first, or move Greaves away ({0}, sorcery speed) before untapping her with Minamo, Magewright's Stone or Patriar's Seal. The source notes this for Pemmin's shroud only.

**Citations**

- Oracle, *Lightning Greaves*: “Equipped creature has haste and shroud. (It can't be the target of spells or abilities.)”
- [CR 702.18a](#cr-70218a), [CR 702.6a](#cr-7026a), [CR 303.4a](#cr-3034a)
- Source (re-verified): [`Gwendlyn_Di_Corci_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/gwendlyn_di_corci_2026-10-14/Gwendlyn_Di_Corci_Rules_Attestation.json) → “Pemmin shroud and friendly targeting”

## Replacement and prevention effects

### gwendlyn-06: Chains of Mephistopheles hits wheels, yours included

**Status:** 🚩 list flag · **Evidence:** fact · **Cards:** Gwendlyn Di Corci, Chains of Mephistopheles, Wheel of Fortune, Windfall, Underworld Breach, Lion's Eye Diamond

**Ruling.** Chains replaces every draw except the first in a draw step: discard a card, then draw; with an empty hand, mill instead. After a wheel empties hands, every one of the seven draws becomes a mill. That's the plan against opponents, but it applies to you too. With Chains out, the Breach + LED + Wheel line mills you seven per Wheel instead of drawing, so Spellbook's 'infinite draw' result doesn't happen. Mill still feeds Breach escapes. Geth's Grimoire draws are also replaced by Chains.

**List flag (anti-synergy).** Pilot note, not a list error: Chains of Mephistopheles is symmetric. Don't run the Breach + LED + Wheel draw engine with Chains on the battlefield unless milling is the goal.

**Citations**

- Oracle, *Chains of Mephistopheles*: “If a player would draw a card except the first one they draw in each of their draw steps, that player discards a card instead. If the player discards a card this way, they draw a card. If the player doesn't discard a card this way, they mill a card.”
- Scryfall ruling, *Chains of Mephistopheles*: “If a spell or ability would cause a player to draw multiple cards, this is treated as a number of individual “draw one card” actions. Apply the effect of Chains of Mephistopheles to each one.”
- [CR 614.11](#cr-61411), [CR 121.2](#cr-1212), [CR 616.1](#cr-6161)
- Commander Spellbook [1368-2706-3518](https://commanderspellbook.com/combo/1368-2706-3518/) (community-maintained, retrieved 2026-10-16): “Resolve Wheel of Fortune, causing each player to discard their hand and draw seven cards.”
- Source (re-verified): [`Gwendlyn_Di_Corci_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/gwendlyn_di_corci_2026-10-14/Gwendlyn_Di_Corci_Rules_Attestation.json) → “Chains of Mephistopheles and wheels”

### gwendlyn-07: Chains vs Notion Thief: the drawing player chooses

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Gwendlyn Di Corci, Chains of Mephistopheles, Notion Thief

**Ruling.** Notion Thief replaces an opponent's extra draws with draws for you. If Chains also applies, the affected player (the opponent who'd draw) picks which replacement to apply first, then checks again. If they pick Notion Thief, you draw instead, and Chains may then replace your draw. There's no fixed order to rely on. Notion Thief doesn't cancel the rest of an instruction, so a 'draw then discard' still discards.

**Citations**

- Oracle, *Notion Thief*: “If an opponent would draw a card except the first one they draw in each of their draw steps, instead that player skips that draw and you draw a card.”
- Scryfall ruling, *Notion Thief*: “If an opponent is instructed to draw a card then discard a card, and Notion Thief causes you to draw a card instead, that opponent still discards a card.”
- [CR 616.1](#cr-6161), [CR 616.1e](#cr-6161e)
- Source (re-verified): [`Gwendlyn_Di_Corci_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/gwendlyn_di_corci_2026-10-14/Gwendlyn_Di_Corci_Rules_Attestation.json) → “Notion Thief and wheels”
- Source (re-verified): [`Gwendlyn_Di_Corci_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/gwendlyn_di_corci_2026-10-14/Gwendlyn_Di_Corci_Rules_Attestation.json) → “Chains and Notion Thief replacement-effect ordering”

## Trigger ordering

### gwendlyn-02: Illusionist's Bracers copies each activation

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Gwendlyn Di Corci, Illusionist's Bracers

**Ruling.** Gwendlyn's ability isn't a mana ability, so Bracers copies it: two random discards per tap, and the copy may target a different player. The copy isn't activated, so the 'only during your turn' restriction doesn't apply to it. If the cost required sacrificing Gwendlyn or the Bracers, nothing would be copied (not relevant here).

**Citations**

- Oracle, *Illusionist's Bracers*: “Whenever an ability of equipped creature is activated, if it isn't a mana ability, copy that ability. You may choose new targets for the copy.”
- Scryfall ruling, *Illusionist's Bracers*: “The copy will have the same targets as the ability it's copying unless you choose new ones.”
- [CR 707.10](#cr-70710), [CR 605.1a](#cr-6051a)
- Source (re-verified): [`Gwendlyn_Di_Corci_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/gwendlyn_di_corci_2026-10-14/Gwendlyn_Di_Corci_Rules_Attestation.json) → “Illusionist's Bracers copies Gwendlyn”

## Zones, commander tax and the command zone

### gwendlyn-08: Tergrid takes discarded permanent cards

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Gwendlyn Di Corci, Tergrid, God of Fright // Tergrid's Lantern

**Ruling.** Tergrid triggers when an opponent discards a permanent card (artifact, creature, enchantment, land, planeswalker) or sacrifices a nontoken permanent. You may put that card onto the battlefield under your control, if it's still in the graveyard when the trigger resolves. Instants and sorceries discarded to Gwendlyn don't qualify. Discards made to pay a cost trigger it above the spell.

**Citations**

- Oracle, *Tergrid, God of Fright // Tergrid's Lantern*: “Whenever an opponent sacrifices a nontoken permanent or discards a permanent card, you may put that card from a graveyard onto the battlefield under your control.”
- Scryfall ruling, *Tergrid, God of Fright // Tergrid's Lantern*: “If the card leaves the graveyard before Tergrid's ability resolves, you can't put it onto the battlefield, even if it returns to the graveyard before the ability resolves.”
- [CR 603.2](#cr-6032), [CR 400.7](#cr-4007)
- Source (re-verified): [`Gwendlyn_Di_Corci_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/gwendlyn_di_corci_2026-10-14/Gwendlyn_Di_Corci_Rules_Attestation.json) → “Tergrid discard recovery”

## What the list depends on

### gwendlyn-09: Bloodchief Ascension has no Mindcrank loop here

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Gwendlyn Di Corci, Bloodchief Ascension

**Ruling.** Ascension needs three quest counters (end steps where an opponent lost 2+ life). Then each card put into an opponent's graveyard drains 2. Mindcrank, the famous loop partner, isn't in the list, so it's an attrition payoff only: each discard to Gwendlyn drains 2 more.

**Citations**

- Oracle, *Bloodchief Ascension*: “Whenever a card is put into an opponent's graveyard from anywhere, if this enchantment has three or more quest counters on it, you may have that player lose 2 life. If you do, you gain 2 life.”
- [CR 603.4](#cr-6034)
- Source (re-verified): [`Gwendlyn_Di_Corci_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/gwendlyn_di_corci_2026-10-14/Gwendlyn_Di_Corci_Rules_Attestation.json) → “Bloodchief Ascension remains noncombo here”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 115.1

Some spells and abilities require their controller to choose one or more targets for them. The targets are object(s) and/or player(s) the spell or ability will affect. These targets are declared as part of the process of putting the spell or ability on the stack. The targets can’t be changed except by another spell or ability that explicitly says it can do so.

#### CR 121.2

Cards may only be drawn one at a time. If a player is instructed to draw multiple cards, that player performs that many individual card draws.

#### CR 302.6

A creature’s activated ability with the tap symbol or the untap symbol in its activation cost can’t be activated unless the creature has been under its controller’s control continuously since their most recent turn began. A creature can’t attack unless it has been under its controller’s control continuously since their most recent turn began. This rule is informally called the “summoning sickness” rule.

#### CR 303.4a

An Aura spell requires a target, which is defined by its enchant ability.

#### CR 400.7

An object that moves from one zone to another becomes a new object with no memory of, or relation to, its previous existence. This rule has the following exceptions.

#### CR 602.2

To activate an ability is to put it onto the stack and pay its costs, so that it will eventually resolve and have its effect. Only an object’s controller (or its owner, if it doesn’t have a controller) can activate its activated ability unless the object specifically says otherwise. Activating an ability follows the steps listed below, in order. If, at any point during the activation of an ability, a player is unable to comply with any of those steps, the activation is illegal; the game returns to the moment before that ability started to be activated (see rule 733, “Handling Illegal …

#### CR 602.5

A player can’t begin to activate an ability that’s prohibited from being activated.

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 603.2c

An ability triggers only once each time its trigger event occurs. However, it can trigger repeatedly if one event contains multiple occurrences.

#### CR 603.4

A triggered ability may read “When/Whenever/At [trigger event], if [condition], [effect].” When the trigger event occurs, the ability checks whether the stated condition is true. The ability triggers only if it is; otherwise it does nothing. If the ability triggers, it checks the stated condition again as it resolves. If the condition isn’t true at that time, the ability is removed from the stack and does nothing. Note that this mirrors the check for legal targets. This rule is referred to as the “intervening ‘if’ clause” rule. (The word “if” has only its normal English meaning anywhere else …

#### CR 605.1a

An activated ability is a mana ability if it meets all of the following criteria: it doesn’t require a target (see rule 115.6), it could add mana to a player’s mana pool when it resolves, it’s not a loyalty ability (see rule 606, “Loyalty Abilities”), and its cost and effect don’t move any card to or from a library. Do not take into account replacement effects that may apply, other than self-replacement effects, when evaluating these criteria.

#### CR 614.11

Some effects replace card draws. These effects are applied even if no cards could be drawn because there are no cards in the affected player’s library.

#### CR 616.1

If two or more replacement and/or prevention effects are attempting to modify the way an event affects an object or player, the affected object’s controller (or its owner if it has no controller) or the affected player chooses one to apply, following the steps listed below. If two or more players have to make these choices at the same time, choices are made in APNAP order (see rule 101.4).

#### CR 616.1e

Any of the applicable replacement and/or prevention effects may be chosen.

#### CR 701.9a

To discard a card, move it from its owner’s hand to that player’s graveyard.

#### CR 702.6a

Equip is an activated ability of Equipment cards. “Equip [cost]” means “[Cost]: Attach this permanent to target creature you control. Activate only as a sorcery.”

#### CR 702.18a

Shroud is a static ability. “Shroud” means “This permanent or player can’t be the target of spells or abilities.”

#### CR 702.138a

Escape represents a static ability that functions while the card with escape is in a player’s graveyard. “Escape [cost]” means “You may cast this card from your graveyard by paying [cost] rather than paying its mana cost.” Casting a spell using its escape ability follows the rules for paying alternative costs in rules 601.2b and 601.2f–h.

#### CR 707.10

To copy a spell, activated ability, or triggered ability means to put a copy of it onto the stack; a copy of a spell isn’t cast and a copy of an activated ability isn’t activated. A copy of a spell or ability copies both the characteristics of the spell or ability and all decisions made for it, including modes, targets, the value of X, and additional or alternative costs. (See rule 601, “Casting Spells.”) Choices that are normally made on resolution are not copied. If an effect of the copy refers to objects used to pay its costs, it uses the objects used to pay the costs of the original spell …

