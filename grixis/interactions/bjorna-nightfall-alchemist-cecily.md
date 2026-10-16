---
title: "Bjorna, Nightfall Alchemist + Cecily, Haunted Mage — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Bjorna, Nightfall Alchemist + Cecily, Haunted Mage — Interaction Review

> Bot cycle 46 · batch A · reviewed 2026-10-16. Deck: [Bjorna, Nightfall Alchemist + Cecily, Haunted Mage](../decks/bjorna-nightfall-alchemist-cecily.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-15), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/source-baseline/bjorna-nightfall-alchemist-cecily.txt`](../../exports/grixis-archidekt/source-baseline/bjorna-nightfall-alchemist-cecily.txt) · SHA-256 `745885c96c41ba3b00c4e7bab3fe677c333cfb225927ea914ecc3212a9a0d871` |
| Rulings | **15** (12 verified · 0 uncertain · 3 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-15 · rulings 2026-10-15 |
| Source attestations | [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) (deck #8: RULES PASS / PROJECT_EXCEPTION) |

## Contents
- [Summary](#summary)
- [Flags and open questions](#flags-and-open-questions)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Key card-pair interactions](#key-card-pair-interactions)
- [Timing and priority](#timing-and-priority)
- [Replacement and prevention effects](#replacement-and-prevention-effects)
- [Trigger ordering](#trigger-ordering)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [Legality and project exceptions](#legality-and-project-exceptions)
- [Rules cited](#rules-cited)

## Summary

Bjorna, Nightfall Alchemist and Cecily, Haunted Mage (Friends forever) run a big-hand spells deck: wheels and draw to eleven cards for free Cecily casts. This review re-verifies the retrospective attestation. Bot cycle 49 re-reviewed it against the M0 canonical project list, which restores the three authorized project exceptions (🚩 NOT Commander-legal): Lutri as companion, Trade Secrets and Yawgmoth's Bargain.

Rules surprises:
- Peer into the Abyss + Teferi's Ageless Insight loses on an odd library.
- Notion Thief starves the Breach + Wheel + Jeska's Will mana.
- The source blueprint misdescribes both commanders.
- Notion Thief turns Trade Secrets into a one-sided draw-6.
- Yawgmoth's Bargain + Ageless Insight gives two cards per life.

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [bjorna-05](#bjorna-05-peer-into-the-abyss--teferis-ageless-insight-an-odd-library-loses) | 🚩 list flag (dependency-risk) | Peer into the Abyss + Teferi's Ageless Insight: an odd library loses | With an odd number of cards in library, Peer + Teferi's Ageless Insight makes you draw from an empty library and lose before any drain or damage trigger resolves. Count the library first (a cantrip or one fetch changes parity), or win through Psychosis Crawler/Niv-Mizzet only when the parity is safe. |
| [bjorna-07](#bjorna-07-underworld-breach--wheel-of-fortune--jeskas-will) | 🚩 list flag (anti-synergy) | Underworld Breach + Wheel of Fortune + Jeska's Will | Notion Thief and the Breach + Wheel + Jeska's Will loop conflict: Thief steals the opponents' wheel draws, leaving Jeska's Will's mana mode at zero. Use one plan or the other in a given turn. |
| [bjorna-12](#bjorna-12-source-blueprint-misdescribes-both-commanders) | 🚩 list flag (documentation) | Source blueprint misdescribes both commanders | The source blueprint's commander summaries don't match current Oracle text (Bjorna has no noncreature-spell trigger; Cecily triggers on attack, not combat damage). It's documentation only; the approved list and the retrospective rules attestation use the correct text. |

## Commander rules text and edge cases

### bjorna-01: Bjorna: sacrifice an artifact, ping and goad a creature

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Bjorna, Nightfall Alchemist, Academy Manufactor, Lightning Greaves

**Ruling.** Bjorna's ability costs {T} and sacrificing an artifact, so it can't be responded to. It targets a **creature** (never a player), deals 1 damage and goads it. Goad lasts until your next turn: the creature must attack each combat, and must attack someone other than you if able.

The {T} cost needs haste the turn Bjorna arrives; Lightning Greaves' shroud doesn't stop her targeting other creatures. Treasures from Big Score, Brass's Bounty and Deadly Dispute, and Academy Manufactor's Clue + Food + Treasure, are fodder.

**Citations**

- Oracle, *Bjorna, Nightfall Alchemist*: “{T}, Sacrifice an artifact: Bjorna, Nightfall Alchemist deals 1 damage to target creature. Goad that creature.”
- [CR 701.15a](#cr-70115a), [CR 701.15b](#cr-70115b), [CR 602.2](#cr-6022)
- Source (re-verified): [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) → “Bjorna's artifact sacrifice is paid before the ability can be responded to. Bjorna cannot target a player with that ability.”

### bjorna-02: Cecily: draw, lose 1, *then* check eleven cards

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Cecily, Haunted Mage

**Ruling.** When Cecily attacks you draw a card and lose 1 life, then check whether you have eleven or more cards in hand. The card just drawn counts. If you do, you may cast an instant or sorcery from your hand without paying its mana cost, during the trigger's resolution, so a sorcery is fine mid-combat. It's still cast from hand. X is 0. Additional costs (Big Score's discard, Deadly Dispute's sacrifice) must still be paid. Cecily's maximum hand size of eleven lets the hand stay big between turns.

**Citations**

- Oracle, *Cecily, Haunted Mage*: “Whenever Cecily, Haunted Mage attacks, you draw a card and you lose 1 life. Then if you have eleven or more cards in your hand, you may cast an instant or sorcery spell from your hand without paying its mana cost.”
- [CR 608.2g](#cr-6082g), [CR 601.2b](#cr-6012b), [CR 402.2](#cr-4022)
- Source (re-verified): [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) → “Cecily performs the draw / life-loss instruction before checking the eleven-card threshold”

### bjorna-12: Source blueprint misdescribes both commanders

**Status:** 🚩 list flag · **Evidence:** fact · **Cards:** Bjorna, Nightfall Alchemist, Cecily, Haunted Mage

**Ruling.** The source blueprint says Bjorna 'rewards casting noncreature spells by granting haste and goading a creature', and Cecily 'rewards combat damage to a player'. Current Oracle text, quoted in bjorna-01 and bjorna-02, says otherwise: Bjorna is an artifact-sacrifice ping-and-goad, and Cecily triggers on *attacking*. The retrospective attestation already uses the correct text.

**List flag (documentation).** The source blueprint's commander summaries don't match current Oracle text (Bjorna has no noncreature-spell trigger; Cecily triggers on attack, not combat damage). It's documentation only; the approved list and the retrospective rules attestation use the correct text.

**Citations**

- Oracle, *Cecily, Haunted Mage*: “Whenever Cecily, Haunted Mage attacks, you draw a card and you lose 1 life.”
- [CR 108.1](#cr-1081)
- Source (re-verified): [`Cecily__Bjorna__Lutri_v1.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Cecily__Bjorna__Lutri_v1.md) → “Bjorna rewards casting noncreature spells by granting haste and goading a creature, while Cecily rewards combat damage to a player”

## Combos and engine lines

### bjorna-05: Peer into the Abyss + Teferi's Ageless Insight: an odd library loses

**Status:** 🚩 list flag · **Evidence:** fact · **Cards:** Cecily, Haunted Mage, Peer into the Abyss, Teferi's Ageless Insight

**Ruling.** Spellbook lists Peer into the Abyss (targeting yourself) + Teferi's Ageless Insight as infinite card draw. Peer first fixes the number (half your library, rounded up), then each draw is replaced by two. With L cards in library you try to draw 2 × ⌈L/2⌉ cards.
- **Odd L:** that's L + 1 draws, so one draw from an empty library, and you lose at the next state-based check, *before* Niv-Mizzet or Psychosis Crawler triggers go on the stack.
- **Even L:** you draw your whole library exactly and survive until your next draw.

Peer also takes half your life (rounded up).

**List flag (dependency-risk).** With an odd number of cards in library, Peer + Teferi's Ageless Insight makes you draw from an empty library and lose before any drain or damage trigger resolves. Count the library first (a cantrip or one fetch changes parity), or win through Psychosis Crawler/Niv-Mizzet only when the parity is safe.

**Citations**

- Oracle, *Teferi's Ageless Insight*: “If you would draw a card except the first one you draw in each of your draw steps, draw two cards instead.”
- Oracle, *Peer into the Abyss*: “Target player draws cards equal to half the number of cards in their library and loses half their life. Round up each time.”
- Scryfall ruling, *Peer into the Abyss*: “To draw the cards, first the player determines how many cards to draw, then draws them. This event may be modified so that a different number of cards are actually drawn.”
- [CR 121.4](#cr-1214), [CR 704.5b](#cr-7045b), [CR 117.5](#cr-1175), [CR 614.1a](#cr-6141a)

### bjorna-06: Peer into the Abyss + Psychosis Crawler

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Cecily, Haunted Mage, Peer into the Abyss, Psychosis Crawler, Niv-Mizzet, Parun

**Ruling.** Peer on yourself draws half your library. Each card drawn triggers Psychosis Crawler (each opponent loses 1) and Niv-Mizzet (1 damage to any target). It's lethal when the cards drawn reach the opponents' life totals. You also lose half your life. The Crawler's P/T equals your hand size.

**Citations**

- Oracle, *Psychosis Crawler*: “Whenever you draw a card, each opponent loses 1 life.”
- Scryfall ruling, *Peer into the Abyss*: “The life lost is rounded up, not the remaining life total.”
- [CR 603.2](#cr-6032), [CR 121.2](#cr-1212)

### bjorna-07: Underworld Breach + Wheel of Fortune + Jeska's Will

**Status:** 🚩 list flag · **Evidence:** fact · **Cards:** Cecily, Haunted Mage, Underworld Breach, Wheel of Fortune, Jeska's Will, Notion Thief

**Ruling.** With Breach, Wheel of Fortune escapes for {2}{R} plus three other graveyard cards and refills every hand to seven. Jeska's Will (both modes with a commander) then adds {R} per card in an opponent's hand and exiles three to play. Repeating this is the Spellbook loop, limited by graveyard fuel.

Anti-synergy: with Notion Thief out, opponents' wheel draws (other than their first in their draw step) become your draws. Their hands stay empty and Jeska's Will's mana mode makes nothing.

**List flag (anti-synergy).** Notion Thief and the Breach + Wheel + Jeska's Will loop conflict: Thief steals the opponents' wheel draws, leaving Jeska's Will's mana mode at zero. Use one plan or the other in a given turn.

**Citations**

- Oracle, *Wheel of Fortune*: “Each player discards their hand, then draws seven cards.”
- Oracle, *Notion Thief*: “If an opponent would draw a card except the first one they draw in each of their draw steps, instead that player skips that draw and you draw a card.”
- Scryfall ruling, *Jeska's Will*: “Use the number of cards in the target opponent's hand as Jeska's Will resolves to determine how much {R} to add.”
- [CR 702.138a](#cr-702138a), [CR 614.1a](#cr-6141a)

## Key card-pair interactions

### bjorna-09: Triskaidekaphile needs exactly thirteen at upkeep

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Cecily, Haunted Mage, Triskaidekaphile

**Ruling.** Triskaidekaphile wins only with *exactly* thirteen cards as your upkeep begins (and on resolution). You can't draw in your upkeep before it checks. Its {3}{U} draw on the previous end step or an opponent's turn sets the count.

**Citations**

- Oracle, *Triskaidekaphile*: “At the beginning of your upkeep, if you have exactly thirteen cards in your hand, you win the game.”
- Scryfall ruling, *Triskaidekaphile*: “If you have fewer cards in your hand, you won't be able to draw cards during your upkeep in time to cause the ability to trigger.”
- [CR 603.4](#cr-6034)

## Timing and priority

### bjorna-04: Robe of the Archmagi draws after Cecily's trigger

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Cecily, Haunted Mage, Robe of the Archmagi

**Ruling.** Robe of the Archmagi draws on *combat damage*, after Cecily's attack trigger has resolved. So it can't raise the hand to eleven for that attack; it sets up the next one. Cecily is a Wizard, so the {1} equip cost applies.

**Citations**

- Oracle, *Robe of the Archmagi*: “Whenever equipped creature deals combat damage to a player, you draw that many cards.”
- [CR 510.2](#cr-5102), [CR 508.1m](#cr-5081m)
- Source (re-verified): [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) → “Robe cannot raise the hand to eleven for that same attack; it supports later attacks.”

## Replacement and prevention effects

### bjorna-08: Wheels with Notion Thief and Teferi's Ageless Insight

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Cecily, Haunted Mage, Notion Thief, Teferi's Ageless Insight, Windfall, Whispering Madness, Reforge the Soul, Echo of Eons, Dark Deal

**Ruling.** - **Notion Thief:** opponents skip their wheel draws and you draw instead. With three opponents, Windfall or Wheel gives you up to 7 + 21 cards. They still discard.
- **Teferi's Ageless Insight:** doubles your non-draw-step draws, so a wheel gives 14.
- **Order of replacements:** the drawing player chooses the order of replacement effects.

This reaches eleven cards for Cecily and thirteen for Triskaidekaphile.

**Citations**

- Scryfall ruling, *Notion Thief*: “If an opponent is instructed to draw a card then discard a card, and Notion Thief causes you to draw a card instead, that opponent still discards a card.”
- Scryfall ruling, *Teferi's Ageless Insight*: “If two or more replacement effects would apply to a card-drawing event, the player drawing the card chooses the order in which to apply them.”
- [CR 614.1a](#cr-6141a), [CR 616.1](#cr-6161)

### bjorna-15: Trade Secrets with Notion Thief: the opponent's two become yours

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Cecily, Haunted Mage, Trade Secrets, Notion Thief, Teferi's Ageless Insight

**Ruling.** Trade Secrets makes the target opponent draw two, then you draw up to four, and the opponent may repeat. With Notion Thief out, the opponent's draws aren't in their draw step, so they skip them and you draw instead: six cards for you, none for them, and they have no reason to repeat. Teferi's Ageless Insight can then double each of your draws, including the ones Thief hands you, since that's a new draw event. That's up to twelve, enough for Cecily's eleven.

**Citations**

- Oracle, *Trade Secrets*: “Target opponent draws two cards, then you draw up to four cards. That opponent may repeat this process as many times as they choose.”
- Oracle, *Notion Thief*: “If an opponent would draw a card except the first one they draw in each of their draw steps, instead that player skips that draw and you draw a card.”
- Scryfall ruling, *Teferi's Ageless Insight*: “If two or more replacement effects would apply to a card-drawing event, the player drawing the card chooses the order in which to apply them.”
- [CR 614.1a](#cr-6141a), [CR 616.1f](#cr-6161f), [CR 614.5](#cr-6145)

### bjorna-16: Yawgmoth's Bargain: skip the draw step, pay 1 life per card

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Cecily, Haunted Mage, Yawgmoth's Bargain, Teferi's Ageless Insight, Psychosis Crawler, Triskaidekaphile

**Ruling.** Bargain skips your draw step and draws a card for each 1 life at instant speed. That fills the hand to Cecily's eleven, or to exactly thirteen before your end step for Triskaidekaphile. With no draw step there's no 'first draw' for Teferi's Ageless Insight to exempt, so every Bargain draw becomes two cards for 1 life. Each card drawn also triggers Psychosis Crawler. Life is the limit: Cecily's attacks and Peer into the Abyss cost life too.

**Citations**

- Oracle, *Yawgmoth's Bargain*: “Pay 1 life: Draw a card.”
- Oracle, *Teferi's Ageless Insight*: “If you would draw a card except the first one you draw in each of your draw steps, draw two cards instead.”
- [CR 614.1b](#cr-6141b), [CR 614.1a](#cr-6141a), [CR 119.4](#cr-1194)

## Trigger ordering

### bjorna-03: Harmonic Prodigy doubles Wizard and Shaman triggers

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Cecily, Haunted Mage, Harmonic Prodigy, Niv-Mizzet, Parun, Archmage Emeritus, Storm-Kiln Artist, Emry, Lurker of the Loch

**Ruling.** Harmonic Prodigy makes triggered abilities of Shamans and *other* Wizards you control trigger an additional time:
- Cecily (Wizard): two attack triggers, each drawing, losing 1 and checking the hand separately, so possibly two free spells.
- Niv-Mizzet, Parun (Dragon Wizard): both its draw-ping and its cast-draw doubled.
- Archmage Emeritus (Wizard), Storm-Kiln Artist (Shaman) and Emry's enter trigger also doubled.

Bjorna is a Human, not a Wizard, so she isn't affected.

**Citations**

- Oracle, *Harmonic Prodigy*: “If a triggered ability of a Shaman or another Wizard you control triggers, that ability triggers an additional time.”
- [CR 603.2](#cr-6032), [CR 603.3b](#cr-6033b)
- Source (re-verified): [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) → “`Harmonic Prodigy` can cause Cecily's triggered ability to trigger an additional time because Cecily is a Wizard”

## Zones, commander tax and the command zone

### bjorna-13: Two commanders, separate tax

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Bjorna, Nightfall Alchemist, Cecily, Haunted Mage

**Ruling.** Bjorna and Cecily share Partner—Friends forever. Each has its own tax: Bjorna {U}{R} then 4, 6; Cecily {1}{U}{B}{R} then 6, 8. Commander damage is tracked per commander. 'Control a commander' (Jeska's Will) is satisfied by either.

**Citations**

- Oracle, *Bjorna, Nightfall Alchemist*: “Partner—Friends forever (You can have two commanders if both have this ability.)”
- [CR 702.124i](#cr-702124i), [CR 903.8](#cr-9038), [CR 903.10a](#cr-90310a)

### bjorna-14: Lutri as companion: {3} to hand, then a flash copy of your spell

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Cecily, Haunted Mage, Lutri, the Spellchaser

**Ruling.** Lutri starts outside the game. Paying {3} to put it into your hand is a special action: main phase, stack empty, can't be responded to. After that it's an ordinary card. Lutri has flash, and its copy trigger only works if you cast it. So cast it while your own instant or sorcery is on the stack, including one Cecily cast for free, since you get priority before it resolves. The copy isn't cast. Commander singleton already meets the companion condition.

**Citations**

- Oracle, *Lutri, the Spellchaser*: “When Lutri enters, if you cast it, copy target instant or sorcery spell you control. You may choose new targets for the copy.”
- Scryfall ruling, *Lutri, the Spellchaser*: “Paying {3} to put your companion into your hand is a special action. It doesn't use the stack and players can't respond to it. Once you take this action, you may cast that card if it's legal to do so before any other player can take actions.”
- Scryfall ruling, *Lutri, the Spellchaser*: “The copy is created on the stack, so it's not "cast." Abilities that trigger when a player casts a spell won't trigger. It will resolve before the original spell does.”
- [CR 116.2g](#cr-1162g), [CR 702.139c](#cr-702139c), [CR 707.10](#cr-70710)

## Legality and project exceptions

### bjorna-11: Canonical list keeps three authorized project exceptions

**Status:** ✅ verified · **Evidence:** approved_decision · **Cards:** Cecily, Haunted Mage, Bjorna, Nightfall Alchemist, Lutri, the Spellchaser, Trade Secrets, Yawgmoth's Bargain

**Ruling.** The canonical project list (M0 registry) keeps Cory's three authorized exceptions: Lutri as companion, plus Trade Secrets and Yawgmoth's Bargain in the main deck. None of them is Commander-legal.
- Trade Secrets and Yawgmoth's Bargain are banned in Commander (Wizards B&R; Scryfall 2026-10-15).
- Lutri is legal in the 99 but banned as a companion (Wizards B&R). Scryfall's legality field can't express that.

The Bot cycle 16 swaps (Trade Secrets → Wizard Class, Yawgmoth's Bargain → Flame of Anor, no companion) now exist only as the derived compliance projection, which isn't canonical. This review covers the canonical list. bjorna-10 (Flame of Anor) was retired in cycle 49 because that card is only in the projection.

**Citations**

- Oracle, *Lutri, the Spellchaser*: “Companion — Each nonland card in your starting deck has a different name.”
- Scryfall ruling, *Lutri, the Spellchaser*: “You may have one companion in the Commander variant. Your deck, including your commander, must meet its companion requirement. Your companion is not one of your one hundred cards.”
- [CR 903.3](#cr-9033), [CR 702.139a](#cr-702139a)
- Source (re-verified): [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) → “The deck is therefore **project-valid under the registered exceptions, not officially Commander-legal without qualification**.”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 108.1

Use the Oracle card reference when determining a card’s wording. A card’s Oracle text can be found using the Gatherer card database at Gatherer.Wizards.com.

#### CR 116.2g

A player who has chosen a companion may pay {3} to put that card from outside the game into their hand. This is a special action. A player can take this action any time they have priority and the stack is empty during a main phase of their turn, but only if they haven’t done so yet this game. (See rule 702.139, “Companion.”)

#### CR 117.5

Each time a player would get priority, the game first performs all applicable state-based actions as a single event (see rule 704, “State-Based Actions”), then repeats this process until no state-based actions are performed. Then triggered abilities are put on the stack (see rule 603, “Handling Triggered Abilities”). These steps repeat in order until no further state-based actions are performed and no abilities trigger. Then the player who would have received priority does so.

#### CR 119.4

If a cost or effect allows a player to pay an amount of life greater than 0, the player may do so only if their life total is greater than or equal to the amount of the payment. If a player pays life, the payment is subtracted from their life total; in other words, the player loses that much life.

#### CR 121.2

Cards may only be drawn one at a time. If a player is instructed to draw multiple cards, that player performs that many individual card draws.

#### CR 121.4

A player who attempts to draw a card from a library with no cards in it loses the game the next time a player would receive priority. (This is a state-based action. See rule 704.)

#### CR 402.2

Each player has a maximum hand size, which is normally seven cards. A player may have any number of cards in their hand, but as part of their cleanup step, the player must discard excess cards down to the maximum hand size.

#### CR 508.1m

Any abilities that trigger on attackers being declared trigger.

#### CR 510.2

Second, all combat damage that’s been assigned is dealt simultaneously. This turn-based action doesn’t use the stack. No player has the chance to cast spells or activate abilities between the time combat damage is assigned and the time it’s dealt.

#### CR 601.2b

If the spell is modal, the player announces the mode choice (see rule 700.2). If the player wishes to splice any cards onto the spell (see rule 702.47), they reveal those cards in their hand. If the spell has alternative or additional costs that will be paid as it’s being cast such as buyback or kicker costs (see rules 118.8 and 118.9), the player announces their intentions to pay any or all of those costs (see rule 601.2f). A player can’t apply two alternative methods of casting or two alternative costs to a single spell. If the spell has a variable cost that will be paid as it’s being cast …

#### CR 602.2

To activate an ability is to put it onto the stack and pay its costs, so that it will eventually resolve and have its effect. Only an object’s controller (or its owner, if it doesn’t have a controller) can activate its activated ability unless the object specifically says otherwise. Activating an ability follows the steps listed below, in order. If, at any point during the activation of an ability, a player is unable to comply with any of those steps, the activation is illegal; the game returns to the moment before that ability started to be activated (see rule 733, “Handling Illegal …

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 603.3b

If multiple abilities have triggered since the last time a player received priority, the abilities are placed on the stack in a two-part process. First, each player, in APNAP order, puts each triggered ability they control with a trigger condition that isn’t another ability triggering on the stack in any order they choose. (See rule 101.4.) Second, each player, in APNAP order, puts all remaining triggered abilities they control on the stack in any order they choose. Then the game once again checks for and performs state-based actions until none are performed, then abilities that triggered …

#### CR 603.4

A triggered ability may read “When/Whenever/At [trigger event], if [condition], [effect].” When the trigger event occurs, the ability checks whether the stated condition is true. The ability triggers only if it is; otherwise it does nothing. If the ability triggers, it checks the stated condition again as it resolves. If the condition isn’t true at that time, the ability is removed from the stack and does nothing. Note that this mirrors the check for legal targets. This rule is referred to as the “intervening ‘if’ clause” rule. (The word “if” has only its normal English meaning anywhere else …

#### CR 608.2g

If an effect gives a player the option to pay mana, they may activate mana abilities before taking that action. If an effect specifically instructs or allows a player to cast a spell during resolution, they do so by following the steps in rules 601.2a–i, except no player receives priority after it’s cast. That spell becomes the topmost object on the stack, and the currently resolving spell or ability continues to resolve, which may include casting other spells this way. No other spells can normally be cast and no other abilities can normally be activated during resolution.

#### CR 614.1a

Effects that use the word “instead” are replacement effects. Most replacement effects use the word “instead” to indicate what events will be replaced with other events.

#### CR 614.1b

Effects that use the word “skip” are replacement effects. These replacement effects use the word “skip” to indicate what events, steps, phases, or turns will be replaced with nothing.

#### CR 614.5

A replacement effect doesn’t invoke itself repeatedly; it gets only one opportunity to affect an event or any modified events that may replace that event.

#### CR 616.1

If two or more replacement and/or prevention effects are attempting to modify the way an event affects an object or player, the affected object’s controller (or its owner if it has no controller) or the affected player chooses one to apply, following the steps listed below. If two or more players have to make these choices at the same time, choices are made in APNAP order (see rule 101.4).

#### CR 616.1f

Once the chosen effect has been applied, this process is repeated (taking into account only replacement or prevention effects that would now be applicable) until there are no more left to apply.

#### CR 701.15a

Certain spells and abilities can goad a creature. Until the next turn of the controller of that spell or ability, that creature is goaded.

#### CR 701.15b

Goaded is a designation a permanent can have. A goaded creature attacks each combat if able and attacks a player other than the controller of the permanent, spell, or ability that caused it to be goaded if able. Goaded is neither an ability nor part of the permanent’s copiable values.

#### CR 702.124i

“Partner—[text]” means “You may designate two legendary cards as your commander rather than one if each of them has the same ‘partner—[text]’ ability.” The “partner—[text]” abilities are “partner—Character select,” “partner—Father & son,” “partner—Friends forever,” and “partner—Survivors.”

#### CR 702.138a

Escape represents a static ability that functions while the card with escape is in a player’s graveyard. “Escape [cost]” means “You may cast this card from your graveyard by paying [cost] rather than paying its mana cost.” Casting a spell using its escape ability follows the rules for paying alternative costs in rules 601.2b and 601.2f–h.

#### CR 702.139a

Companion is a keyword ability that functions outside the game. It’s written as “Companion—[Condition].” Before the game begins, you may reveal one card you own from outside the game with a companion ability whose condition is fulfilled by your starting deck. (See rule 103.2b.) Once during the game, any time you have priority and the stack is empty, but only during a main phase of your turn, you may pay {3} and put that card into your hand. This is a special action that doesn’t use the stack (see rule 116.2g). This is a change from previous rules.

#### CR 702.139c

Once you take the special action and put the card with companion into your hand, it remains in the game until the game ends.

#### CR 704.5b

If a player attempted to draw a card from a library with no cards in it since the last time state-based actions were checked, that player loses the game.

#### CR 707.10

To copy a spell, activated ability, or triggered ability means to put a copy of it onto the stack; a copy of a spell isn’t cast and a copy of an activated ability isn’t activated. A copy of a spell or ability copies both the characteristics of the spell or ability and all decisions made for it, including modes, targets, the value of X, and additional or alternative costs. (See rule 601, “Casting Spells.”) Choices that are normally made on resolution are not copied. If an effect of the copy refers to objects used to pay its costs, it uses the objects used to pay the costs of the original spell …

#### CR 903.3

Each deck has a legendary card designated as its commander. That card must be either (a) a creature card, (b) a Vehicle card, or (c) a Spacecraft card with one or more power/toughness boxes. This designation is not a characteristic of the object represented by the card; rather, it is an attribute of the card itself. The card retains this designation even when it changes zones.

#### CR 903.8

A player may cast a commander they own from the command zone. A commander cast from the command zone costs an additional {2} for each previous time the player casting it has cast it from the command zone that game. This additional cost is informally known as the “commander tax.”

#### CR 903.10a

A player who’s been dealt 21 or more combat damage by the same commander over the course of the game loses the game. (This is a state-based action. See rule 704.)

