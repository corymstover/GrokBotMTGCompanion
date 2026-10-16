---
title: "Abaddon the Despoiler — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Abaddon the Despoiler — Interaction Review

> Bot cycle 46 · batch A · reviewed 2026-10-16. Deck: [Abaddon the Despoiler](../decks/abaddon-the-despoiler.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/source-baseline/abaddon-the-despoiler.txt`](../../exports/grixis-archidekt/source-baseline/abaddon-the-despoiler.txt) · SHA-256 `5448d76193923a3f9e3d4c41a327eaeaa9c6326d484d8e5a9abaf3852db2efff` |
| Rulings | **29** (26 verified · 0 uncertain · 3 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/rules/Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md) (Interaction Review v1, 63 KB, re-verified) · [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) (deck #1: RULES PASS) |

## Contents
- [Summary](#summary)
- [Flags and open questions](#flags-and-open-questions)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [Key card-pair interactions](#key-card-pair-interactions)
- [Timing and priority](#timing-and-priority)
- [Replacement and prevention effects](#replacement-and-prevention-effects)
- [Trigger ordering](#trigger-ordering)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [What the list depends on](#what-the-list-depends-on)
- [Rules cited](#rules-cited)

## Summary

Abaddon gives hand-cast spells cascade on your turn, up to the life opponents have lost that turn. This review re-verifies the source's 63 KB interaction review and the retrospective attestation against current Oracle text, rulings and CR 2026-09-25. Bot cycle 49 re-reviewed it against the M0 canonical project list (the source baseline, with Mystic Remora; GrokBot's unapproved Stormfist Crusader swap is not canonical).

New findings:
- Abaddon's cascade is mandatory once a spell qualifies. It can send a card tutored to the top to the bottom, and any 0-MV spell cast on your turn randomizes your whole library. Both are sequencing hazards.
- The source's mana value for Call Forth the Tempest is wrong (8, not 11).

The Breach package is rules-coherent but finite and fuel-dependent.

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [abaddon-06](#abaddon-06-a-stacked-top-card-is-exposed-to-every-later-cascade-on-your-turn) | 🚩 list flag (anti-synergy) | A stacked top card is exposed to every later cascade on your turn | Sequencing hazard, not a list error. Top-of-library tutors and Abaddon's mandatory cascade compete on your own turn. Pilot note: draw the tutored card first, or tutor on an opponent's end step. |
| [abaddon-07](#abaddon-07-mana-value-0-spells-always-qualify-and-their-cascade-randomizes-your-library) | 🚩 list flag (anti-synergy) | Mana value 0 spells always qualify, and their cascade randomizes your library | Pilot note: casting a 0-drop artifact or Pact from hand on your turn with Abaddon out effectively shuffles your library. Cast them before stacking the top, or on another turn. No list change: the cards are core fast mana. |
| [abaddon-08](#abaddon-08-granted-cascade-stacks-with-printed-cascade) | 🚩 list flag (documentation) | Granted cascade stacks with printed cascade | The source review's Call Forth the Tempest mana value (11) is wrong; current Oracle is MV 8, so the third instance needs X ≥ 8, not 11. No list change. |

## Commander rules text and edge cases

### abaddon-01: Abaddon's threshold counts life opponents actually lost this turn

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Abaddon the Despoiler

**Ruling.** X is the total life all opponents have lost so far this turn, summed across opponents. It resets each turn. Damage to a player counts because damage causes life loss. Direct life loss counts too. Your own life payments (fetchlands, shocklands, Ancient Tomb, Mana Confluence, Force of Will's alternative cost, Flame Rift's damage to you) never count. Gaining life back later doesn't lower X: the text counts life lost, not the net change.

**Citations**

- Oracle, *Abaddon the Despoiler*: “During your turn, spells you cast from your hand with mana value X or less have cascade, where X is the total amount of life your opponents have lost this turn.”
- [CR 120.3a](#cr-1203a), [CR 119.3](#cr-1193)
- Source (re-verified): [`Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/rules/Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md) → “The life-loss threshold is reset by the turn boundary; prior-turn life loss does not count.”
- Source (re-verified): [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) → “The threshold uses life actually lost, not attempted/prevented damage.”

### abaddon-02: Only spells cast from your hand, during your turn, get cascade

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Abaddon the Despoiler, Underworld Breach, Jeska's Will, The Ruinous Powers

**Ruling.** The grant needs all three: it is your turn, the spell is cast from your hand, and its mana value is ≤ X when cast. Spells cast from exile (cascade hits, Jeska's Will, Harnfel, The Ruinous Powers, Prosper, suspend, foretell), from the graveyard (Underworld Breach escape) or from the command zone (Abaddon himself) never get Abaddon's cascade. Their own printed cascade still works.

**Citations**

- Oracle, *Abaddon the Despoiler*: “During your turn, spells you cast from your hand with mana value X or less have cascade, where X is the total amount of life your opponents have lost this turn.”
- [CR 702.85a](#cr-70285a), [CR 113.10](#cr-11310), [CR 601.2](#cr-6012)
- Source (re-verified): [`Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/rules/Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md) → “Only spells cast from the controller's hand receive cascade from Abaddon.”
- Source (re-verified): [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) → “A spell cast from exile by cascade is not cast from hand and does not receive Abaddon's grant”

### abaddon-04: Mana value, not the cost you paid, is what is compared

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Abaddon the Despoiler, Fierce Guardianship, Deadly Rollick, Force of Will, Nightscape Familiar, Blasphemous Act

**Ruling.** Abaddon and cascade both compare mana value, which comes only from the printed mana cost. Alternative costs (Fierce Guardianship, Deadly Rollick and Deflecting Swat for free, Force of Will's pitch) and cost reductions (Nightscape Familiar, Blasphemous Act's own discount) change what you pay, not mana value. A free Fierce Guardianship cast from your hand on your turn at X ≥ 3 has cascade and can hit a nonland card with MV 0–2. A free Deadly Rollick at X ≥ 4 can hit MV 0–3. Force of Negation's free mode works only on an opponent's turn, so its free cast never gets Abaddon's cascade.

**Citations**

- Oracle, *Abaddon the Despoiler*: “During your turn, spells you cast from your hand with mana value X or less have cascade, where X is the total amount of life your opponents have lost this turn.”
- Oracle, *Force of Negation*: “If it's not your turn, you may exile a blue card from your hand rather than pay this spell's mana cost.”
- Scryfall ruling, *Blasphemous Act*: “The mana value of the spell is determined only by its mana cost, no matter what the total cost to cast the spell was.”
- [CR 118.9c](#cr-1189c), [CR 202.3](#cr-2023), [CR 601.2f](#cr-6012f)
- Source (re-verified): [`Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/rules/Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md) → “The general rule is that **alternate cost changes what is paid, not mana value or the hand-cast zone condition**.”

### abaddon-07: Mana value 0 spells always qualify, and their cascade randomizes your library

**Status:** 🚩 list flag · **Evidence:** fact · **Cards:** Abaddon the Despoiler, Lion's Eye Diamond, Lotus Petal, Chrome Mox, Pact of Negation

**Ruling.** X can't be negative, so Lion's Eye Diamond, Lotus Petal, Chrome Mox and Pact of Negation cast from your hand on your turn always have cascade. Cascade looks for a nonland card with mana value less than 0, which doesn't exist. You therefore exile your whole library, then put it all on the bottom in a random order. Nothing is cast, and any card you set up on top is randomized. The source review only noted that Pact 'gains no useful cascade hit'. The library randomization is an addition from this review.

**List flag (anti-synergy).** Pilot note: casting a 0-drop artifact or Pact from hand on your turn with Abaddon out effectively shuffles your library. Cast them before stacking the top, or on another turn. No list change: the cards are core fast mana.

**Citations**

- Oracle, *Abaddon the Despoiler*: “During your turn, spells you cast from your hand with mana value X or less have cascade, where X is the total amount of life your opponents have lost this turn.”
- [CR 702.85a](#cr-70285a), [CR 202.3a](#cr-2023a)
- Source (re-verified): [`Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/rules/Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md) → “Pact of Negation remains different: its mana value is 0, so no card can have lower mana value than it; its cascade instance cannot find a legal card to cast.”

### abaddon-08: Granted cascade stacks with printed cascade

**Status:** 🚩 list flag · **Evidence:** fact · **Cards:** Abaddon the Despoiler, Bituminous Blast, Call Forth the Tempest, Noise Marine

**Ruling.** Each cascade instance triggers separately. Bituminous Blast (MV 5) cast from hand on your turn at X ≥ 5 cascades twice, and each trigger looks for MV < 5. Call Forth the Tempest has **mana value 8** ({5}{R}{R}{R}), so at X ≥ 8 it gets a third instance. The archived review said 'mana value 11 ({8}{R}{R}{R})', which is wrong for current Oracle. Noise Marine (MV 5) gets two triggers at X ≥ 5. Each hit resolves above the original spell, so Blast's 4 damage resolves last.

**List flag (documentation).** The source review's Call Forth the Tempest mana value (11) is wrong; current Oracle is MV 8, so the third instance needs X ≥ 8, not 11. No list change.

**Citations**

- Oracle, *Call Forth the Tempest*: “Cascade, cascade”
- Scryfall ruling, *Call Forth the Tempest*: “the second cascade ability will look for a card with mana value less than Call Forth the Tempest's mana value of 8.”
- [CR 702.85c](#cr-70285c)
- Source (re-verified): [`Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/rules/Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md) → “**Call Forth the Tempest** has two printed instances of cascade and mana value 11 ({8}{R}{R}{R}).”

### abaddon-09: Cards without a mana cost: cascade hits, never Abaddon casts

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Abaddon the Despoiler, Ancestral Vision, Inevitable Betrayal, Profane Tutor

**Ruling.** Ancestral Vision, Inevitable Betrayal and Profane Tutor have MV 0 and no mana cost, so they can't be cast from hand normally. Suspending them is a special action, not a cast. When suspend's last time counter comes off you may cast them from exile, which gets no Abaddon cascade. Any cascade with MV ≥ 1 can hit them and cast them for free. That is a cast from exile, so it triggers Keeper of Secrets, The Lost and the Damned, Prosper, Passionate Archaeologist, Wild-Magic Sorcerer and Nalfeshnee. Underworld Breach can't escape them: their escape cost includes an unpayable mana cost.

**Citations**

- Scryfall ruling, *Ancestral Vision*: “A card with no mana cost can't be cast normally; you'll need a way to cast it for an alternative cost or without paying its mana cost, such as by suspending it.”
- Scryfall ruling, *Ancestral Vision*: “Exiling a card with suspend isn't casting that card.”
- Scryfall ruling, *Underworld Breach*: “If a card has no mana cost, its escape cost is an unpayable cost, so you can't cast it for that cost.”
- [CR 702.62a](#cr-70262a), [CR 202.3a](#cr-2023a), [CR 702.85a](#cr-70285a)
- Source (re-verified): [`Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/rules/Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md) → “When cast from exile this way they are normal spell casts, not suspend casts.”

## Combos and engine lines

### abaddon-20: Underworld Breach + Lion's Eye Diamond + Brain Freeze

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Abaddon the Despoiler, Underworld Breach, Lion's Eye Diamond, Brain Freeze

**Ruling.** With Breach and LED on the battlefield and Brain Freeze in the graveyard:
1. Sacrifice LED for three mana of one color. LED's mana ability is instant-speed, and discarding your hand is part of its cost.
2. Escape LED for {0} plus three other graveyard cards.
3. Escape Brain Freeze for {1}{U} plus three cards.
Every escape is a cast, so storm grows. Storm copies aren't cast and don't add to storm. Mill yourself for fuel and finish by milling opponents.

Notes:
- Escape casts come from the graveyard, so none of them gets Abaddon's cascade.
- Milling an empty library doesn't make a player lose. They lose only when they try to draw from it (e.g. Wheel of Fortune or Windfall). Keep enough library to survive your own wheel.
- Breach is sacrificed at the end step.
- It is a resource-dependent finite loop with a fuel requirement, not a free infinite. The archived worked line needs at least six other cards across hand and graveyard.

**Citations**

- Oracle, *Underworld Breach*: “The escape cost is equal to the card's mana cost plus exile three other cards from your graveyard.”
- Oracle, *Lion's Eye Diamond*: “Discard your hand, Sacrifice this artifact: Add three mana of any one color. Activate only as an instant.”
- Scryfall ruling, *Lion's Eye Diamond*: “The ability is a mana ability, so it is activated and resolves as a mana ability, but it can only be activated at times when you can cast an instant.”
- Scryfall ruling, *Brain Freeze*: “The copies are put directly onto the stack. They aren't cast and won't be counted by other spells with storm cast later in the turn.”
- Scryfall ruling, *Brain Freeze*: “Spells cast from zones other than a player's hand and spells that were countered are counted by the storm ability.”
- [CR 702.138a](#cr-702138a), [CR 702.40a](#cr-70240a), [CR 707.10](#cr-70710), [CR 605.3a](#cr-6053a), [CR 121.4](#cr-1214), [CR 701.17a](#cr-70117a)
- Source (re-verified): [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) → “it is not represented as an unconditional infinite or as interaction-proof”
- Source (re-verified): [`Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/rules/Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md) → “This is a resource-dependent finite-game combo sequence, not a resource-free mathematical infinite.”

### abaddon-21: Breach + Lotus Petal + Brain Freeze

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Abaddon the Despoiler, Underworld Breach, Lotus Petal, Brain Freeze

**Ruling.** Lotus Petal's escape cost is {0} plus three cards. Each escape is a cast and nets one mana, so two Petal escapes pay for each Brain Freeze escape ({1}{U}) and add storm. The mill must keep returning at least nine cards per cycle (6 for the two Petals, 3 for Brain Freeze) to sustain the loop. The Spellbook record lists this as infinite self-mill and near-infinite mill. The same notes apply as for the LED line: no Abaddon cascade, and a mill finish needs a draw.

**Citations**

- Oracle, *Lotus Petal*: “{T}, Sacrifice this artifact: Add one mana of any color.”
- Scryfall ruling, *Underworld Breach*: “If it is a permanent spell, it enters the battlefield and will return to its owner's graveyard if it dies later.”
- [CR 702.138a](#cr-702138a), [CR 702.40a](#cr-70240a)

### abaddon-22: Breach + Wheel of Fortune (+ LED or Jeska's Will)

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Abaddon the Despoiler, Underworld Breach, Wheel of Fortune, Lion's Eye Diamond, Jeska's Will

**Ruling.** Each escaped Wheel discards everyone's hand and draws seven. That refills your graveyard, and opponents run out of library first if you've milled them. With LED, cracking LED in response pays for the next escaped Wheel ({2}{R} + 3 cards). With Jeska's Will, its mana mode (red for each card in a target opponent's hand, seven after a Wheel) plus its exile mode pay for and fuel the loop. Both modes need you to control a commander as you cast it. Drawing from an empty library is a loss at the next priority check. That is the kill, and also your own risk.

**Citations**

- Oracle, *Jeska's Will*: “If you control a commander as you cast this spell, you may choose both instead.”
- Oracle, *Wheel of Fortune*: “Each player discards their hand, then draws seven cards.”
- Scryfall ruling, *Jeska's Will*: “Use the number of cards in the target opponent's hand as Jeska's Will resolves to determine how much {R} to add.”
- [CR 702.138a](#cr-702138a), [CR 121.4](#cr-1214), [CR 104.3c](#cr-1043c)

## Engines and payoffs

### abaddon-11: Combat life loss opens the threshold early

**Status:** ✅ verified · **Evidence:** derived_metric · **Cards:** Abaddon the Despoiler, Loyal Subordinate, Bloodletter of Aclazotz

**Ruling.** Loyal Subordinate makes each opponent lose 3 at beginning of combat if you control your commander as it resolves. That's X = 9 at a four-player table, or 18 with Bloodletter, which opens Abaddon cascades for post-combat main-phase spells. It's life loss, not damage, so Solphim doesn't double it. (The cycle 46 version of this ruling also covered Stormfist Crusader, a GrokBot challenger swap that isn't in the canonical list.)

**Citations**

- Oracle, *Loyal Subordinate*: “At the beginning of combat on your turn, if you control your commander, each opponent loses 3 life.”
- Scryfall ruling, *Loyal Subordinate*: “If you don’t control your commander as the lieutenant ability resolves, you won’t get its effect.”
- [CR 603.4](#cr-6034), [CR 119.3](#cr-1193)
- Source (re-verified): [`Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/rules/Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md) → “**Loyal Subordinate + Bloodletter**”

### abaddon-29: Mystic Remora: triggers aren't casts; its own cascade can only hit a 0-drop

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Abaddon the Despoiler, Mystic Remora

**Ruling.** Mystic Remora's cumulative upkeep and draw triggers aren't spells cast, so they don't raise X or cascade. Cast from hand on your turn with X ≥ 1, Remora (mana value 1) cascades into a mana-value-0 nonland card only. That randomizes your library like any 0-drop cascade (abaddon-07). It's in the canonical list in the slot GrokBot's challenger gave to Stormfist Crusader.

**Citations**

- Oracle, *Mystic Remora*: “Whenever an opponent casts a noncreature spell, you may draw a card unless that player pays {4}.”
- Scryfall ruling, *Mystic Remora*: “Paying cumulative upkeep is always optional. If it's not paid, the permanent with cumulative upkeep is sacrificed. Partial payments of the total cumulative upkeep cost can't be made.”
- [CR 702.24a](#cr-70224a), [CR 702.85a](#cr-70285a)
- Source (re-verified): [`Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/rules/Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md) → “Its upkeep and draw triggers are not casts and do not increase Abaddon's threshold.”

### abaddon-12: Neheb converts the turn's life loss into post-combat mana

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Abaddon the Despoiler, Neheb, the Eternal

**Ruling.** Neheb adds {R} for each 1 life opponents lost this turn, at the beginning of your postcombat main phase. It counts total life lost, not the net change in life totals. The trigger uses the stack (it is not a mana ability), and Neheb must be on the battlefield when that phase begins. Neheb's afflict is life loss, so it also raises X.

**Citations**

- Oracle, *Neheb, the Eternal*: “At the beginning of each of your postcombat main phases, add {R} for each 1 life your opponents have lost this turn.”
- Scryfall ruling, *Neheb, the Eternal*: “Neheb's ability checks only how much life opponents lost during the turn, not by how much their life total decreased compared to the start of the turn.”
- Scryfall ruling, *Neheb, the Eternal*: “Because it triggers at the beginning of a phase, Neheb's last ability isn't a mana ability.”
- [CR 106.4](#cr-1064), [CR 603.2](#cr-6032)

### abaddon-13: Rakdos: castable only after life loss; reduces generic mana only

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Abaddon the Despoiler, Rakdos, Lord of Riots

**Ruling.** Rakdos can't be cast unless an opponent lost life this turn, and his discount doesn't apply to himself. Once he's out, creature spells cost {1} less per life opponents lost. The discount can't reduce colored pips and applies after cost increases like commander tax, so it can make Abaddon's recast cheaper. Reduced cost doesn't change mana value, so Abaddon's cascade comparison is unaffected.

**Citations**

- Oracle, *Rakdos, Lord of Riots*: “You can't cast Rakdos unless an opponent lost life this turn.”
- Scryfall ruling, *Rakdos, Lord of Riots*: “Rakdos's last ability won't reduce the cost to cast Rakdos itself.”
- Scryfall ruling, *Rakdos, Lord of Riots*: “If there are additional costs to cast a creature spell, such as a kicker cost or the commander tax, apply those increases before applying cost reductions.”
- Scryfall ruling, *Rakdos, Lord of Riots*: “Rakdos's last ability can't reduce the colored mana requirement of a creature spell you cast.”
- [CR 601.2f](#cr-6012f), [CR 118.7d](#cr-1187d)

### abaddon-14: Cast-from-exile payoffs see cascade hits but not copies

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Abaddon the Despoiler, Keeper of Secrets, Passionate Archaeologist, The Lost and the Damned, Prosper, Tome-Bound, Nalfeshnee

**Ruling.** Each spell cast off a cascade, Jeska's Will, Harnfel, The Ruinous Powers, Prosper or Mind's Desire is a cast from exile. It triggers Keeper of Secrets (damage equal to its MV), Abaddon's Passionate Archaeologist ability (same), a Spawn from The Lost and the Damned, and a Treasure from Prosper. Nalfeshnee also copies it. Copies (Nalfeshnee, storm) are not cast and trigger none of these. Keeper and The Lost and the Damned also trigger on escape casts from the graveyard and on casting Abaddon from the command zone. Keeper's and Archaeologist's damage to opponents is damage, so it raises X and Solphim doubles it.

**Citations**

- Oracle, *Keeper of Secrets*: “Whenever you cast a spell from anywhere other than your hand, this creature deals damage equal to that spell's mana value to target opponent.”
- Oracle, *Passionate Archaeologist*: “Commander creatures you own have "Whenever you cast a spell from exile, this creature deals damage equal to that spell's mana value to target opponent."”
- Oracle, *The Lost and the Damned*: “you cast a spell from anywhere other than your hand, create a 3/3 red Spawn creature token.”
- Oracle, *Prosper, Tome-Bound*: “Whenever you play a card from exile, create a Treasure token.”
- Scryfall ruling, *Prosper, Tome-Bound*: “The Pact Boon ability triggers whenever you play any cards from exile, not just those exiled with the Mystic Arcanum ability.”
- [CR 707.10](#cr-70710), [CR 120.3a](#cr-1203a)
- Source (re-verified): [`Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/rules/Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md) → “Copies of a spell are not cast, so they do not trigger Keeper of Secrets.”

## Key card-pair interactions

### abaddon-15: Passionate Archaeologist works from the 99

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Abaddon the Despoiler, Passionate Archaeologist

**Ruling.** Passionate Archaeologist is a Background, but the deck runs it as an ordinary enchantment in the 99, not as a second commander (Abaddon has no 'Choose a Background'). Its static ability gives the trigger to commander creatures you own, so Abaddon has it only while Abaddon is on the battlefield. A cast from exile while Abaddon is in the command zone or graveyard deals nothing.

**Citations**

- Oracle, *Passionate Archaeologist*: “Commander creatures you own have”
- Scryfall ruling, *Passionate Archaeologist*: “If you control a Background that grants an ability to commander creatures you own, and you own more than one commander creature, each of them will have that ability.”
- [CR 702.124k](#cr-702124k), [CR 113.6](#cr-1136)
- Source (re-verified): [`Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/rules/Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md) → “Abaddon is a commander creature you own, so the Background gives Abaddon an ability that triggers when you cast a spell from exile.”

### abaddon-16: Wild-Magic Sorcerer: only the first exile cast each turn cascades

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Abaddon the Despoiler, Wild-Magic Sorcerer

**Ruling.** The first spell you cast from exile each turn gets cascade, so the first cascade hit or Jeska's Will card can chain. Later exile casts that turn don't. If Sorcerer arrives after your first exile cast that turn, it gives nothing more that turn. Two Sorcerers would give that one spell two instances, but the deck has one.

**Citations**

- Oracle, *Wild-Magic Sorcerer*: “The first spell you cast from exile each turn has cascade.”
- Scryfall ruling, *Wild-Magic Sorcerer*: “The first spell you cast from exile each turn will have cascade, even if it's not the first spell you've cast that turn.”
- [CR 702.85c](#cr-70285c)
- Source (re-verified): [`Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/rules/Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md) → “The extra cascade is limited to the first spell cast from exile each turn”

### abaddon-17: Nalfeshnee copies exile casts; permanent copies are hasty, temporary tokens

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Abaddon the Despoiler, Nalfeshnee, Storm-Kiln Artist

**Ruling.** Nalfeshnee copies each spell you cast from exile. A copied permanent spell becomes a token with haste that's sacrificed at end step. The copy isn't cast, so it gets no cascade and doesn't trigger Keeper, Archaeologist, Prosper, The Lost and the Damned or storm count. Storm-Kiln Artist does trigger on a copied instant or sorcery.

**Citations**

- Oracle, *Nalfeshnee*: “Whenever you cast a spell from exile, copy it.”
- Oracle, *Storm-Kiln Artist*: “Whenever you cast or copy an instant or sorcery spell, create a Treasure token.”
- [CR 707.10](#cr-70710)
- Source (re-verified): [`Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/rules/Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md) → “Nalfeshnee's copy is not cast.”

### abaddon-18: Delayed Blast Fireball is the 5-damage version whenever it's cast from exile

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Abaddon the Despoiler, Delayed Blast Fireball

**Ruling.** Cast from exile for any reason (cascade hit, foretell, Jeska's Will, Harnfel, Prosper), it deals 5 to each opponent and their creatures. That is 15 life lost at a three-opponent table, 30 with Solphim, 60 with Solphim and Bloodletter. Cast from hand it deals 2, but it can get Abaddon's cascade at X ≥ 3. Foretelling is a special action that costs {2} on your turn.

**Citations**

- Oracle, *Delayed Blast Fireball*: “If this spell was cast from exile, it deals 5 damage to each opponent and each creature they control instead.”
- Scryfall ruling, *Delayed Blast Fireball*: “Delayed Blast Fireball deals 5 damage if it was cast from exile for any reason; it doesn't have to be from its foretell ability.”
- [CR 702.143a](#cr-702143a), [CR 116.2h](#cr-1162h)

### abaddon-19: The Ruinous Powers: opponents' cards, life loss only after the cast

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Abaddon the Despoiler, The Ruinous Powers, Bloodletter of Aclazotz

**Ruling.** At your upkeep you exile a random opponent's top card. Until end of turn you may play it, with mana of any color. When you cast it, its owner (that opponent) loses life equal to its MV, which raises X, and Bloodletter doubles it. It's cast from exile, so it never gets Abaddon's cascade, and the life loss comes after the cast. Normal timing rules apply. A land played this way causes no life loss.

**Citations**

- Oracle, *The Ruinous Powers*: “When you cast a spell this way, its owner loses life equal to its mana value.”
- Scryfall ruling, *The Ruinous Powers*: “You must follow all normal timing rules when casting a spell or playing a land using the permission granted by Ruinous Powers.”
- [CR 603.2](#cr-6032)
- Source (re-verified): [`Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/rules/Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md) → “The spell cast from The Ruinous Powers is from exile, not your hand, so Abaddon does not grant cascade to that spell.”

### abaddon-23: Jeska's Will: needs a commander to choose both modes; exiled cards can't cascade off Abaddon

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Abaddon the Despoiler, Jeska's Will

**Ruling.** The 'both modes' check is made as you cast. Any commander you control counts, and losing it afterwards changes nothing. Cards played from the exile mode follow normal timing; a land needs an unused land drop. As casts from exile they trigger the exile payoffs but not Abaddon's cascade. Jeska's Will itself, cast from hand at X ≥ 3, can have cascade.

**Citations**

- Oracle, *Jeska's Will*: “Exile the top three cards of your library. You may play them this turn.”
- Scryfall ruling, *Jeska's Will*: “Once you've chosen both modes for the spell, it doesn't matter whether you continue to control a commander.”
- Scryfall ruling, *Jeska's Will*: “You pay all costs and follow all timing rules for cards played with the permission from the last mode of Jeska's Will.”
- [CR 601.2b](#cr-6012b)

### abaddon-24: Storm counts cascade hits and escapes; copies count for magecraft only

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Abaddon the Despoiler, Mind's Desire, Brain Freeze, Flusterstorm, Storm-Kiln Artist, Birgi, God of Storytelling // Harnfel, Horn of Bounty

**Ruling.** Storm counts every spell cast before it this turn, including cascade hits, exile casts and escapes. Storm copies aren't cast. Storm-Kiln Artist's magecraft triggers on cast *or copy*, so each Brain Freeze or Flusterstorm copy makes a Treasure. Birgi, Kessig Flamebreather, Vivi Ornitier and Exalted Flamer trigger only on casts. Mind's Desire cast from hand at X ≥ 6 cascades as well as storming. Its exiled cards are played from exile, which feeds the exile payoffs.

**Citations**

- Oracle, *Storm-Kiln Artist*: “Whenever you cast or copy an instant or sorcery spell, create a Treasure token.”
- Oracle, *Birgi, God of Storytelling // Harnfel, Horn of Bounty*: “Whenever you cast a spell, add {R}.”
- Scryfall ruling, *Mind's Desire*: “The copies are put directly onto the stack. They aren't cast and won't be counted by other spells with storm cast later in the turn.”
- [CR 702.40a](#cr-70240a), [CR 707.10](#cr-70710)
- Source (re-verified): [`Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/rules/Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md) → “Storm-Kiln Artist** triggers when you cast or copy an instant or sorcery.”

### abaddon-25: Blasphemous Act under Abaddon

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Abaddon the Despoiler, Blasphemous Act

**Ruling.** Blasphemous Act has mana value 9 however little you pay, so it gets Abaddon's cascade only at X ≥ 9. A creature cast off that cascade resolves before the wipe and then dies to it. Its 13 damage hits your own engines too (Abaddon, Keeper, Storm-Kiln Artist, Thermo-Alchemist). Damage to creatures isn't life loss, so it doesn't raise X.

**Citations**

- Oracle, *Blasphemous Act*: “This spell costs {1} less to cast for each creature on the battlefield.”
- Scryfall ruling, *Blasphemous Act*: “The total cost to cast Blasphemous Act is locked in before you pay that cost.”
- [CR 202.3](#cr-2023), [CR 702.85a](#cr-70285a)
- Source (re-verified): [`Abaddon_Step_5_Blasphemous_Act_Interaction_Check_2026-10-13.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/tests/Abaddon_Step_5_Blasphemous_Act_Interaction_Check_2026-10-13.md) → “Blasphemous Act”

## Timing and priority

### abaddon-03: Eligibility is checked as the spell is cast; later life loss can't add cascade

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Abaddon the Despoiler, Thermo-Alchemist, Boltwave

**Ruling.** Cascade is a cast trigger, so whether the spell has cascade is fixed when casting finishes. If a spell's own damage or life loss pushes X up after it resolves, that same spell does not gain cascade. Raise X first: ping with Thermo-Alchemist, let Loyal Subordinate's trigger resolve, or resolve a Boltwave. Only then cast the spell that needs the higher threshold.

**Citations**

- Oracle, *Abaddon the Despoiler*: “During your turn, spells you cast from your hand with mana value X or less have cascade, where X is the total amount of life your opponents have lost this turn.”
- Oracle, *Thermo-Alchemist*: “{T}: This creature deals 1 damage to each opponent.”
- Scryfall ruling, *Call Forth the Tempest*: “Cascade triggers when you cast the spell, meaning that it resolves before that spell.”
- [CR 702.85a](#cr-70285a), [CR 603.2](#cr-6032)
- Source (re-verified): [`Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/rules/Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md) → “Abaddon checks the threshold as each spell is cast. Life loss caused by that spell after it has been cast cannot retroactively give that spell cascade.”

### abaddon-27: Thermo-Alchemist, Vivi and Birgi: summoning sickness and mana windows

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Abaddon the Despoiler, Thermo-Alchemist, Vivi Ornitier, Birgi, God of Storytelling // Harnfel, Horn of Bounty

**Ruling.** Thermo-Alchemist's {T} ability needs it to have been under your control since your turn began. Each instant or sorcery cast untaps it, so it can ping again before the next spell. Vivi's {0} mana ability works only during your turn and once per turn, for X equal to its power. Its +1/+1 counter trigger resolves before the spell that caused it. Birgi's {R} stays in your pool until end of turn.

**Citations**

- Oracle, *Vivi Ornitier*: “Activate only during your turn and only once each turn.”
- Oracle, *Birgi, God of Storytelling // Harnfel, Horn of Bounty*: “Until end of turn, you don't lose this mana as steps and phases end.”
- Scryfall ruling, *Vivi Ornitier*: “Vivi Ornitier's last ability resolves before the spell that caused it to trigger.”
- [CR 302.6](#cr-3026), [CR 605.1a](#cr-6051a), [CR 106.4](#cr-1064)

## Replacement and prevention effects

### abaddon-10: Bloodletter and Solphim modify different events

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Abaddon the Despoiler, Bloodletter of Aclazotz, Solphim, Mayhem Dominus, Boltwave, Flame Rift

**Ruling.** Solphim doubles noncombat **damage** from your sources to opponents. Bloodletter doubles the **life loss** an opponent takes on your turn. They are replacement effects on different events, so both apply. Boltwave's 3 becomes 6 damage, which causes 12 life lost per opponent, so X = 36 at a three-opponent table. Flame Rift's 4 becomes 8 damage and 16 lost per opponent; the 4 it deals to you is not doubled. Bloodletter doesn't change damage, so lifelink gains only the damage dealt. Solphim does nothing for pure life loss (Loyal Subordinate, The Ruinous Powers).

**Citations**

- Oracle, *Bloodletter of Aclazotz*: “If an opponent would lose life during your turn, they lose twice that much life instead.”
- Oracle, *Solphim, Mayhem Dominus*: “If a source you control would deal noncombat damage to an opponent or a permanent an opponent controls, it deals double that damage to that player or permanent instead.”
- Scryfall ruling, *Bloodletter of Aclazotz*: “Bloodletter of Aclazotz's last ability doesn't change the amount of damage dealt to opponents.”
- [CR 614.1a](#cr-6141a), [CR 120.3a](#cr-1203a), [CR 616.1](#cr-6161)
- Source (re-verified): [`Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/rules/Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md) → “These are replacement effects acting on different parts of damage/life loss.”

## Trigger ordering

### abaddon-05: Cascade resolves before the spell that has it

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Abaddon the Despoiler, Vampiric Tutor, Imperial Seal, Mystical Tutor, Brainstorm, Ponder

**Ruling.** Cascade triggers on cast and goes on the stack above its spell, so it resolves first. A cascaded Vampiric Tutor, Imperial Seal, Mystical Tutor, Brainstorm or Ponder can't set up the top card for its own cascade. The tutor's top-deck effect only applies after its cascade has already exiled cards.

**Citations**

- Scryfall ruling, *Call Forth the Tempest*: “Cascade triggers when you cast the spell, meaning that it resolves before that spell.”
- [CR 702.85a](#cr-70285a), [CR 405.2](#cr-4052), [CR 603.3b](#cr-6033b)
- Source (re-verified): [`Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/rules/Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md) → “Cascade resolves before its source spell, so the cantrip/tutor cannot set up the top card for its own already-triggered cascade”

### abaddon-06: A stacked top card is exposed to every later cascade on your turn

**Status:** 🚩 list flag · **Evidence:** fact · **Cards:** Abaddon the Despoiler, Vampiric Tutor, Imperial Seal, Mystical Tutor, Brainstorm

**Ruling.** Under Abaddon, cascade is not optional. Once a hand-cast spell qualifies, the cascade must exile cards; you only choose whether to cast the hit. A card you put on top (Vampiric Tutor, Imperial Seal, Mystical Tutor, Brainstorm) is the first card the next cascade on your turn exiles. If it is a nonland card with lower mana value than the cascading spell, you may cast it for free, which is a strong line. Otherwise (a land, or MV equal or higher) it goes to the bottom in a random order and is lost for the turn. Sequence: draw it first, or cascade only from a spell with higher MV than the tutored card.

**List flag (anti-synergy).** Sequencing hazard, not a list error. Top-of-library tutors and Abaddon's mandatory cascade compete on your own turn. Pilot note: draw the tutored card first, or tutor on an opponent's end step.

**Citations**

- Oracle, *Abaddon the Despoiler*: “During your turn, spells you cast from your hand with mana value X or less have cascade, where X is the total amount of life your opponents have lost this turn.”
- Scryfall ruling, *Call Forth the Tempest*: “When the cascade ability resolves, you must exile cards. The only optional part of the ability is whether or not you cast the last card exiled.”
- [CR 702.85a](#cr-70285a)
- Source (re-verified): [`Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/rules/Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md) → “A tutor that puts a card on top can therefore set up a later, higher-mana-value cascade spell.”

## Zones, commander tax and the command zone

### abaddon-26: Commander tax and recasting Abaddon

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Abaddon the Despoiler, Keeper of Secrets, The Lost and the Damned, Rakdos, Lord of Riots

**Ruling.** Each cast from the command zone costs {2} more per previous cast: {2}{U}{B}{R}, then 7, then 9. Casting Abaddon from the command zone isn't a cast from hand, so it gets no cascade (his ability works only on the battlefield anyway). It does count as 'anywhere other than your hand', so it triggers Keeper of Secrets and The Lost and the Damned. Rakdos reduces the generic part after the tax.

**Citations**

- Oracle, *The Lost and the Damned*: “you cast a spell from anywhere other than your hand”
- Scryfall ruling, *Rakdos, Lord of Riots*: “If there are additional costs to cast a creature spell, such as a kicker cost or the commander tax, apply those increases before applying cost reductions.”
- [CR 903.8](#cr-9038), [CR 903.9a](#cr-9039a)

## What the list depends on

### abaddon-28: What the list depends on

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Abaddon the Despoiler, Underworld Breach, Lion's Eye Diamond, Brain Freeze, Wheel of Fortune, Bloodletter of Aclazotz

**Ruling.** The deck wins in two ways:
- **Abaddon cascade turns:** these need X built before the big spells, with Boltwave, Thermo-Alchemist, Loyal Subordinate, the exile-damage creatures and Bloodletter doubling.
- **The Breach package:** it is commander-independent. Abaddon adds nothing to escape casts.

Both lines fold to graveyard hate and counters on key pieces. The interaction suite (Force of Will, Fierce Guardianship, Pact of Negation, Swan Song, Flusterstorm, Pyroblast, Deflecting Swat) protects them. Pact of Negation needs {3}{U}{U} at your next upkeep or you lose the game. If Pact is countered, the delayed trigger never happens.

**Citations**

- Oracle, *Pact of Negation*: “At the beginning of your next upkeep, pay {3}{U}{U}. If you don't, you lose the game.”
- Scryfall ruling, *Pact of Negation*: “If Pact of Negation is countered or otherwise doesn't resolve (perhaps because its target became illegal), the delayed triggered ability that threatens you with a game loss won't trigger at the beginning of your next upkeep.”
- [CR 603.7a](#cr-6037a)

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 104.3c

If a player is required to draw more cards than are left in their library, they draw the remaining cards and then lose the game the next time a player would receive priority. (This is a state-based action. See rule 704.)

#### CR 106.4

When an effect instructs a player to add mana, that mana goes into a player’s mana pool. From there, it can be used to pay costs immediately, or it can stay in the player’s mana pool as unspent mana. Each player’s mana pool empties at the end of each step and phase, and the player is said to lose this mana. Cards with abilities that produce mana or refer to unspent mana have received errata in the Oracle™ card reference to no longer explicitly refer to the mana pool.

#### CR 113.6

Abilities of an instant or sorcery spell usually function only while that object is on the stack. Abilities of all other objects usually function only while that object is on the battlefield. The exceptions are as follows:

#### CR 113.10

Effects can add or remove abilities of objects. An effect that adds an ability will state that the object “gains” or “has” that ability, or similar. An effect that removes an ability will state that the object “loses” that ability.

#### CR 116.2h

A player who has a card with foretell in their hand may pay {2} and exile that card face down. This is a special action. A player may take this action any time they have priority during their turn. See rule 702.143, “Foretell.”

#### CR 118.7d

If a cost is reduced by an amount of colorless mana that exceeds its colorless mana component, the cost’s colorless mana component is reduced to nothing and the cost’s generic mana component is reduced by the difference.

#### CR 118.9c

An alternative cost doesn’t change a spell’s mana cost, only what its controller has to pay to cast it. Spells and abilities that ask for that spell’s mana cost still see the original value.

#### CR 119.3

If an effect causes a player to gain life or lose life, that player’s life total is adjusted accordingly.

#### CR 120.3a

Damage dealt to a player by a source without infect causes that player to lose that much life.

#### CR 121.4

A player who attempts to draw a card from a library with no cards in it loses the game the next time a player would receive priority. (This is a state-based action. See rule 704.)

#### CR 202.3

The mana value of an object is a number equal to the total amount of mana in its mana cost, regardless of color.

#### CR 202.3a

The mana value of an object with no mana cost is 0, unless that object is the back face of a nonmodal double-faced permanent or spell, or it is a melded permanent.

#### CR 302.6

A creature’s activated ability with the tap symbol or the untap symbol in its activation cost can’t be activated unless the creature has been under its controller’s control continuously since their most recent turn began. A creature can’t attack unless it has been under its controller’s control continuously since their most recent turn began. This rule is informally called the “summoning sickness” rule.

#### CR 405.2

The stack keeps track of the order that spells and/or abilities were added to it. Each time an object is put on the stack, it’s put on top of all objects already there.

#### CR 601.2

To cast a spell is to take it from where it is (usually the hand), put it on the stack, and pay its costs, so that it will eventually resolve and have its effect. Casting a spell includes proposal of the spell (rules 601.2a–d) and determination and payment of costs (rules 601.2f–h). To cast a spell, a player follows the steps listed below, in order. A player must be legally allowed to cast the spell to begin this process (see rule 601.3). If a player is unable to comply with the requirements of a step listed below while performing that step, the casting of the spell is illegal; the game …

#### CR 601.2b

If the spell is modal, the player announces the mode choice (see rule 700.2). If the player wishes to splice any cards onto the spell (see rule 702.47), they reveal those cards in their hand. If the spell has alternative or additional costs that will be paid as it’s being cast such as buyback or kicker costs (see rules 118.8 and 118.9), the player announces their intentions to pay any or all of those costs (see rule 601.2f). A player can’t apply two alternative methods of casting or two alternative costs to a single spell. If the spell has a variable cost that will be paid as it’s being cast …

#### CR 601.2f

The player determines the total cost of the spell. Usually this is just the mana cost. Some spells have additional or alternative costs. Some effects may increase or reduce the cost to pay, or may provide other alternative costs. Costs may include paying mana, tapping permanents, sacrificing permanents, discarding cards, and so on. The total cost is the mana cost or alternative cost (as determined in rule 601.2b), plus all additional costs and cost increases, and minus all cost reductions. If multiple cost reductions apply, the player may apply them in any order. If the mana component of the …

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 603.3b

If multiple abilities have triggered since the last time a player received priority, the abilities are placed on the stack in a two-part process. First, each player, in APNAP order, puts each triggered ability they control with a trigger condition that isn’t another ability triggering on the stack in any order they choose. (See rule 101.4.) Second, each player, in APNAP order, puts all remaining triggered abilities they control on the stack in any order they choose. Then the game once again checks for and performs state-based actions until none are performed, then abilities that triggered …

#### CR 603.4

A triggered ability may read “When/Whenever/At [trigger event], if [condition], [effect].” When the trigger event occurs, the ability checks whether the stated condition is true. The ability triggers only if it is; otherwise it does nothing. If the ability triggers, it checks the stated condition again as it resolves. If the condition isn’t true at that time, the ability is removed from the stack and does nothing. Note that this mirrors the check for legal targets. This rule is referred to as the “intervening ‘if’ clause” rule. (The word “if” has only its normal English meaning anywhere else …

#### CR 603.7a

Delayed triggered abilities are created during the resolution of spells or abilities, as the result of a replacement effect being applied, or as a result of a static ability that allows a player to take an action. A delayed triggered ability won’t trigger until it has actually been created, even if its trigger event occurred just beforehand. Other events that happen earlier may make the trigger event impossible.

#### CR 605.1a

An activated ability is a mana ability if it meets all of the following criteria: it doesn’t require a target (see rule 115.6), it could add mana to a player’s mana pool when it resolves, it’s not a loyalty ability (see rule 606, “Loyalty Abilities”), and its cost and effect don’t move any card to or from a library. Do not take into account replacement effects that may apply, other than self-replacement effects, when evaluating these criteria.

#### CR 605.3a

A player may activate an activated mana ability whenever they have priority, whenever they are casting a spell or activating an ability that requires a mana payment, or whenever a rule or effect asks for a mana payment, even if it’s in the middle of casting or resolving a spell or activating or resolving an ability.

#### CR 614.1a

Effects that use the word “instead” are replacement effects. Most replacement effects use the word “instead” to indicate what events will be replaced with other events.

#### CR 616.1

If two or more replacement and/or prevention effects are attempting to modify the way an event affects an object or player, the affected object’s controller (or its owner if it has no controller) or the affected player chooses one to apply, following the steps listed below. If two or more players have to make these choices at the same time, choices are made in APNAP order (see rule 101.4).

#### CR 701.17a

For a player to mill a number of cards, that player puts that many cards from the top of their library into their graveyard.

#### CR 702.24a

Cumulative upkeep is a triggered ability that imposes an increasing cost on a permanent. “Cumulative upkeep [cost]” means “At the beginning of your upkeep, if this permanent is on the battlefield, put an age counter on this permanent. Then you may pay [cost] for each age counter on it. If you don’t, sacrifice it.” If [cost] has choices associated with it, each choice is made separately for each age counter, then either the entire set of costs is paid, or none of them is paid. Partial payments aren’t allowed.

#### CR 702.40a

Storm is a triggered ability that functions on the stack. “Storm” means “When you cast this spell, copy it for each other spell that was cast before it this turn. If the spell has any targets, you may choose new targets for any of the copies.”

#### CR 702.62a

Suspend is a keyword that represents three abilities. The first is a static ability that functions while the card with suspend is in a player’s hand. The second and third are triggered abilities that function in the exile zone. “Suspend N—[cost]” means “If you could begin to cast this card by putting it onto the stack from your hand, you may pay [cost] and exile it with N time counters on it. This action doesn’t use the stack,” and “At the beginning of your upkeep, if this card is suspended, remove a time counter from it,” and “When the last time counter is removed from this card, if it’s …

#### CR 702.85a

Cascade is a triggered ability that functions only while the spell with cascade is on the stack. “Cascade” means “When you cast this spell, exile cards from the top of your library until you exile a nonland card whose mana value is less than this spell’s mana value. You may cast that card without paying its mana cost if the resulting spell’s mana value is less than this spell’s mana value. Then put all cards exiled this way that weren’t cast on the bottom of your library in a random order.”

#### CR 702.85c

If a spell has multiple instances of cascade, each triggers separately.

#### CR 702.124k

“Choose a Background” means “You may designate two cards as your commander rather than one if one of them is this card and the other is a legendary Background enchantment card.” You can’t designate two cards as your commander if one has a “choose a Background” ability and the other is not a legendary Background enchantment card, and legendary Background enchantment cards can’t be your commander unless you have also designated a commander with “choose a Background.”

#### CR 702.138a

Escape represents a static ability that functions while the card with escape is in a player’s graveyard. “Escape [cost]” means “You may cast this card from your graveyard by paying [cost] rather than paying its mana cost.” Casting a spell using its escape ability follows the rules for paying alternative costs in rules 601.2b and 601.2f–h.

#### CR 702.143a

Foretell is a keyword that functions while the card with foretell is in a player’s hand. Any time a player has priority during their turn, that player may pay {2} and exile a card with foretell from their hand face down. That player may look at that card as long as it remains in exile. They may cast that card after the current turn has ended by paying any foretell cost it has rather than paying that spell’s mana cost. Casting a spell this way follows the rules for paying alternative costs in rules 601.2b and 601.2f–h.

#### CR 707.10

To copy a spell, activated ability, or triggered ability means to put a copy of it onto the stack; a copy of a spell isn’t cast and a copy of an activated ability isn’t activated. A copy of a spell or ability copies both the characteristics of the spell or ability and all decisions made for it, including modes, targets, the value of X, and additional or alternative costs. (See rule 601, “Casting Spells.”) Choices that are normally made on resolution are not copied. If an effect of the copy refers to objects used to pay its costs, it uses the objects used to pay the costs of the original spell …

#### CR 903.8

A player may cast a commander they own from the command zone. A commander cast from the command zone costs an additional {2} for each previous time the player casting it has cast it from the command zone that game. This additional cost is informally known as the “commander tax.”

#### CR 903.9a

If a commander is in a graveyard or in exile and that object was put into that zone since the last time state-based actions were checked, its owner may put it into the command zone. This is a state-based action. See rule 704.

