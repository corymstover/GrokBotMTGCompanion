---
title: "Nekusar, the Mindrazer — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Nekusar, the Mindrazer — Interaction Review

> Bot cycle 51 · batch D · reviewed 2026-10-16. Deck: [Nekusar, the Mindrazer](../decks/nekusar-the-mindrazer.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-15), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/nekusar-the-mindrazer.txt`](../../exports/grixis-archidekt/nekusar-the-mindrazer.txt) · SHA-256 `485e4aa8caea97c607374dde3e15c052ee87e15502ee2161a37cc0ecfbe2cf5f` |
| Rulings | **9** (8 verified · 0 uncertain · 1 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-15 · rulings 2026-10-15 |
| Source attestations | [`Nekusar_the_Mindrazer_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nekusar_the_Mindrazer_Approval_Ready_Verification_2026-10-15.md) (Approval-ready verification; rules sections 5–15 re-checked against Oracle, rulings and CR) |

## Contents
- [Summary](#summary)
- [Flags and open questions](#flags-and-open-questions)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [Replacement and prevention effects](#replacement-and-prevention-effects)
- [Trigger ordering](#trigger-ordering)
- [What the list depends on](#what-the-list-depends-on)
- [Rules cited](#rules-cited)

## Summary

Nekusar gives everyone extra draws and pings opponents for each card. The list stacks additive trigger multipliers (Wizard's Staff, Harmonic Prodigy, Krang), more draw punishers, Ghyrson Starn's exactly-1 bonus, and both discard and shuffle wheels. All seven Spellbook lines are confirmed.

Rules surprises: Krang doesn't add to Nekusar's draw-step trigger; the multipliers add, they don't multiply; shuffle wheels don't trigger discard payoffs; Molten Psyche counts every draw that turn. One flag: Krang doubles Spiteful Visions and Phyrexian Tyranny on your own draws.

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [nekusar-03](#nekusar-03-krang-also-doubles-spiteful-visions-and-phyrexian-tyranny-on-your-own-draws) | 🚩 list flag (dependency-risk) | Krang also doubles Spiteful Visions and Phyrexian Tyranny on your own draws | Spiteful Visions and Phyrexian Tyranny punish your own draws, and Krang doubles those triggers too, so your wheels can kill you. |

## Commander rules text and edge cases

### nekusar-01: Extra draw for everyone; 1 damage per opponent draw

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Nekusar, the Mindrazer

**Ruling.** At the beginning of each player's draw step, that player draws an extra card. That trigger resolves after the normal draw. Nekusar deals 1 damage to an opponent for each card they draw, at any time and for any reason. Only real draws count. Effects that put cards into a hand without saying "draw" don't trigger it. Your own draws don't trigger it either.

**Citations**

- Oracle, *Nekusar, the Mindrazer*: “Whenever an opponent draws a card, Nekusar deals 1 damage to that player.”
- Scryfall ruling, *Nekusar, the Mindrazer*: “If a spell or ability causes you to put cards into your hand without specifically using the word "draw," it doesn't count as drawing cards and it doesn't cause Nekusar's second ability to trigger.”
- [CR 504.1](#cr-5041), [CR 120.3](#cr-1203)

## Combos and engine lines

### nekusar-05: Peer into the Abyss + any draw punisher

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Nekusar, the Mindrazer, Peer into the Abyss, Sheoldred, the Apocalypse, Underworld Dreams, Orcish Bowmasters, Razorkin Needlehead

**Ruling.** Target an opponent. They lose half their life, rounded up, and draw half their library, rounded up. Each draw triggers Nekusar, Underworld Dreams, Razorkin Needlehead, Bowmasters (after their first draw-step card) or Sheoldred (2 each). With the multipliers that's usually lethal. It works best when their library is about the size of their life total or larger.

**Citations**

- Oracle, *Peer into the Abyss*: “Target player draws cards equal to half the number of cards in their library and loses half their life. Round up each time.”
- Scryfall ruling, *Peer into the Abyss*: “The life lost is rounded up, not the remaining life total. For example, if the target player has 7 life, they lose 4 life and end up with 3. Similarly, the number of cards drawn is rounded up, not the number of cards remaining in the library.”
- [CR 120.3](#cr-1203), [CR 119.3](#cr-1193)
- Commander Spellbook [1561-1972](https://commanderspellbook.com/combo/1561-1972/) (community-maintained, retrieved 2026-10-16): “Nekusar triggers for each card drawn this way.”
- Commander Spellbook [1561-2720](https://commanderspellbook.com/combo/1561-2720/) (community-maintained, retrieved 2026-10-16): “An opponent has cards in their library greater than their life total.”
- Commander Spellbook [1561-2498](https://commanderspellbook.com/combo/1561-2498/) (community-maintained, retrieved 2026-10-16): “Sheoldred's second ability triggers for each card drawn this way.”

### nekusar-06: Curiosity on Niv-Mizzet loops; on Nekusar it's value

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Nekusar, the Mindrazer, Curiosity, Niv-Mizzet, Parun, Consecrated Sphinx

**Ruling.** On Niv-Mizzet, Curiosity loops: each draw pings an opponent, and that may draw again. It's optional and limited by your library. On Nekusar, each ping to an opponent may draw you a card. Your draws don't trigger Nekusar, so it doesn't loop, but Niv pings on each of them. Consecrated Sphinx's two draws per opponent draw also feed Niv.

**Citations**

- Oracle, *Curiosity*: “Whenever enchanted creature deals damage to an opponent, you may draw a card.”
- Oracle, *Niv-Mizzet, Parun*: “Whenever you draw a card, Niv-Mizzet deals 1 damage to any target.”
- [CR 603.2](#cr-6032), [CR 121.1](#cr-1211)
- Commander Spellbook [1089-2353](https://commanderspellbook.com/combo/1089-2353/) (community-maintained, retrieved 2026-10-16): “Curiosity attached to Niv-Mizzet.”
- Source (re-verified): [`Nekusar_the_Mindrazer_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nekusar_the_Mindrazer_Approval_Ready_Verification_2026-10-15.md) → “Because Curiosity uses **may**, the controller can stop the sequence.”

### nekusar-09: Underworld Breach + Wheel of Fortune + Jeska's Will

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Nekusar, the Mindrazer, Underworld Breach, Wheel of Fortune, Jeska's Will

**Ruling.** With Breach, escape Jeska's Will for at least six {R}, then escape Wheel of Fortune. Every player discards and draws seven, and with Nekusar each opponent takes at least 7. Repeat. It needs an opponent with six or more cards in hand and enough graveyard to exile.

**Citations**

- [CR 702.138a](#cr-702138a)
- Commander Spellbook [1368-1878-2706](https://commanderspellbook.com/combo/1368-1878-2706/) (community-maintained, retrieved 2026-10-16): “An opponent has at least six cards in hand.”
- Commander Spellbook [1368-1878-2706](https://commanderspellbook.com/combo/1368-1878-2706/) (community-maintained, retrieved 2026-10-16): “Cast Wheel of Fortune from your graveyard for its escape cost by paying {2}{R} and exiling three other cards from your graveyard, causing each player to discard their hand and draw seven cards.”

## Engines and payoffs

### nekusar-08: Wheels: discard vs shuffle — Waste Not and Liliana's Caress need discard; Molten Psyche counts all draws

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Nekusar, the Mindrazer, Wheel of Fortune, Windfall, Whispering Madness, Dark Deal, Jace's Archivist, Winds of Change, Molten Psyche, Waste Not, Liliana's Caress

**Ruling.** Two kinds of wheel:
- **Discard wheels** (Wheel of Fortune, Windfall, Whispering Madness, Dark Deal, Jace's Archivist, Wheel and Deal, Reforge the Soul, Magus of the Wheel): trigger Waste Not and Liliana's Caress (2 life per discarded card).
- **Shuffle wheels** (Winds of Change, Molten Psyche): the hand is shuffled away, not discarded, so no discard triggers. They're still cheap mass draws.

Molten Psyche's metalcraft damage counts every card each opponent drew that turn, not just its own draws, so cast it last in the chain.

**Citations**

- Oracle, *Molten Psyche*: “Metalcraft — If you control three or more artifacts, Molten Psyche deals damage to each opponent equal to the number of cards that player has drawn this turn.”
- Oracle, *Liliana's Caress*: “Whenever an opponent discards a card, that player loses 2 life.”
- Scryfall ruling, *Molten Psyche*: “The metalcraft effect counts all cards each opponent drew for any reason during that turn, not just the cards those opponents drew due to Molten Psyche’s first effect.”
- [CR 701.9a](#cr-7019a), [CR 701.24a](#cr-70124a)
- Source (re-verified): [`Nekusar_the_Mindrazer_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nekusar_the_Mindrazer_Approval_Ready_Verification_2026-10-15.md) → “It does not discard and therefore does not trigger Waste Not/Liliana's Caress from those hand changes”

## Replacement and prevention effects

### nekusar-04: Ghyrson Starn wants exactly 1 damage; doublers would break it

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Nekusar, the Mindrazer, Ghyrson Starn, Kelermorph, Fate Unraveler, Underworld Dreams, Razorkin Needlehead, Kederekt Parasite

**Ruling.** Each 1-damage ping from another source you control triggers Ghyrson for 2 more. That covers Nekusar, Fate Unraveler, Underworld Dreams, Razorkin Needlehead, Kederekt Parasite, Spiteful Visions and Niv-Mizzet, so each ping becomes 3. Several pings at once trigger Ghyrson that many times. A damage doubler would turn the 1 into 2 and stop Ghyrson. The source cut Solphim for exactly that reason, and this list has no doubler.

**Citations**

- Oracle, *Ghyrson Starn, Kelermorph*: “Three Autostubs — Whenever another source you control deals exactly 1 damage to a permanent or player, Ghyrson Starn deals 2 damage to that permanent or player.”
- Scryfall ruling, *Ghyrson Starn, Kelermorph*: “If another source deals exactly 1 damage to a permanent or player multiple times or deals exactly 1 damage to multiple permanents and/or players simultaneously, Ghryson Starn, Kellermorph's last ability triggers that many times.”
- [CR 614.1a](#cr-6141a), [CR 120.3](#cr-1203)
- Source (re-verified): [`Nekusar_the_Mindrazer_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nekusar_the_Mindrazer_Approval_Ready_Verification_2026-10-15.md) → “With Solphim present, Nekusar's would-be 1 becomes 2; Ghyrson therefore does not see an event in which Nekusar dealt exactly 1.”

## Trigger ordering

### nekusar-02: Wizard's Staff + Harmonic Prodigy + Krang: additive, and Krang skips the draw-step trigger

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Nekusar, the Mindrazer, Wizard's Staff, Harmonic Prodigy, Krang, the All-Powerful

**Ruling.** Each of these adds one more instance of a trigger. They add up; they don't multiply:
- **Wizard's Staff:** equip Wizard {1}, and Nekusar is a Wizard.
- **Harmonic Prodigy:** affects another Wizard you control.
- **Krang:** only triggers caused by a player drawing a card. Nekusar's draw-step trigger is caused by the step beginning, so Krang doesn't add to it.

With all three: 3 draw-step triggers, so an opponent draws 4 cards in their draw step, and 4 damage triggers per card drawn. Each extra instance is a separate trigger, not a copy, and you choose targets for each.

**Citations**

- Oracle, *Wizard's Staff*: “If a triggered ability of equipped creature triggers, that ability triggers an additional time.”
- Oracle, *Harmonic Prodigy*: “If a triggered ability of a Shaman or another Wizard you control triggers, that ability triggers an additional time.”
- Oracle, *Krang, the All-Powerful*: “If a player drawing a card causes a triggered ability of a permanent you control to trigger, that ability triggers an additional time.”
- Scryfall ruling, *Krang, the All-Powerful*: “Krang's first ability doesn't copy the triggered ability; it just causes the ability to trigger an additional time. Any choices made as you put the ability onto the stack, such as modes and targets, are made separately for each instance of the ability. Any choices made on resolution, such as whether to put counters on a permanent, are also made individually.”
- [CR 603.2](#cr-6032), [CR 603.3b](#cr-6033b)
- Source (re-verified): [`Nekusar_the_Mindrazer_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nekusar_the_Mindrazer_Approval_Ready_Verification_2026-10-15.md) → “Nekusar's draw-step trigger: **base + Staff + Prodigy = 3 instances**.”
- Source (re-verified): [`Nekusar_the_Mindrazer_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nekusar_the_Mindrazer_Approval_Ready_Verification_2026-10-15.md) → “Krang **does not** add an instance of Nekusar's beginning-of-draw-step ability”

### nekusar-07: Draw-step stack: normal draw, then order Nekusar's extra draws before Teferi's Puzzle Box

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Nekusar, the Mindrazer, Teferi's Puzzle Box, Kami of the Crescent Moon, Anvil of Bogardan, Spiteful Visions

**Ruling.** The turn-based draw happens first, then the beginning-of-draw-step triggers go on the stack. On any player's turn, you control Nekusar, Kami, Spiteful Visions, Anvil and Teferi's Puzzle Box, so you choose their order. Let the extra-draw triggers resolve first, then Puzzle Box. That player's bigger hand goes to the bottom and gets redrawn, and each redraw triggers the punishers. Anvil's discard after each extra draw feeds Waste Not and Liliana's Caress.

**Citations**

- Oracle, *Teferi's Puzzle Box*: “At the beginning of each player's draw step, that player puts the cards in their hand on the bottom of their library in any order, then draws that many cards.”
- Oracle, *Anvil of Bogardan*: “At the beginning of each player's draw step, that player draws an additional card, then discards a card.”
- Scryfall ruling, *Teferi's Puzzle Box*: “You do your normal draw before this ability is put on the stack.”
- [CR 504.1](#cr-5041), [CR 603.3b](#cr-6033b)

## What the list depends on

### nekusar-03: Krang also doubles Spiteful Visions and Phyrexian Tyranny on your own draws

**Status:** 🚩 list flag · **Evidence:** fact · **Cards:** Nekusar, the Mindrazer, Krang, the All-Powerful, Spiteful Visions, Phyrexian Tyranny, Wheel of Fortune, Echo of Eons

**Ruling.** Spiteful Visions damages every player who draws, you included. Phyrexian Tyranny makes every player who draws lose 2 life unless they pay {2}. You control both, so Krang doubles them on your own draws too. A Wheel of Fortune with both out and Krang costs you 14 damage and 28 life (or 14 payments of {2}), on top of the extra draw-step cards. Sheoldred's +2 per draw softens this. Plan your own wheels around your life total.

**List flag (dependency-risk).** Spiteful Visions and Phyrexian Tyranny punish your own draws, and Krang doubles those triggers too, so your wheels can kill you.

**Citations**

- Oracle, *Spiteful Visions*: “Whenever a player draws a card, this enchantment deals 1 damage to that player.”
- Oracle, *Phyrexian Tyranny*: “Whenever a player draws a card, that player loses 2 life unless they pay {2}.”
- Scryfall ruling, *Spiteful Visions*: “Spiteful Visions's second ability triggers any time any player draws a card, not just when a player draws a card as a result of its first ability.”
- Scryfall ruling, *Phyrexian Tyranny*: “If more than one card is drawn at a time, this triggers for each card drawn.”
- [CR 603.2](#cr-6032), [CR 120.3](#cr-1203)

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 119.3

If an effect causes a player to gain life or lose life, that player’s life total is adjusted accordingly.

#### CR 120.3

Damage may have one or more of the following results, depending on whether the recipient of the damage is a player or permanent, the characteristics of the damage’s source, and the characteristics of the damage’s recipient (if it’s a permanent).

#### CR 121.1

A player draws a card by putting the top card of their library into their hand. This is done as a turn-based action during each player’s draw step. It may also be done as part of a cost or effect of a spell or ability.

#### CR 504.1

First, the active player draws a card. This turn-based action doesn’t use the stack.

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 603.3b

If multiple abilities have triggered since the last time a player received priority, the abilities are placed on the stack in a two-part process. First, each player, in APNAP order, puts each triggered ability they control with a trigger condition that isn’t another ability triggering on the stack in any order they choose. (See rule 101.4.) Second, each player, in APNAP order, puts all remaining triggered abilities they control on the stack in any order they choose. Then the game once again checks for and performs state-based actions until none are performed, then abilities that triggered …

#### CR 614.1a

Effects that use the word “instead” are replacement effects. Most replacement effects use the word “instead” to indicate what events will be replaced with other events.

#### CR 701.9a

To discard a card, move it from its owner’s hand to that player’s graveyard.

#### CR 701.24a

To shuffle a library or a face-down pile of cards, randomize the cards within it so that no player knows their order.

#### CR 702.138a

Escape represents a static ability that functions while the card with escape is in a player’s graveyard. “Escape [cost]” means “You may cast this card from your graveyard by paying [cost] rather than paying its mana cost.” Casting a spell using its escape ability follows the rules for paying alternative costs in rules 601.2b and 601.2f–h.

