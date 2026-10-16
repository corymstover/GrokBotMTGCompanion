---
title: "Obeka, Splitter of Seconds — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Obeka, Splitter of Seconds — Interaction Review

> Bot cycle 54 · batch E · reviewed 2026-10-16. Deck: [Obeka, Splitter of Seconds](../decks/obeka-splitter-of-seconds.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/obeka-splitter-of-seconds.txt`](../../exports/grixis-archidekt/obeka-splitter-of-seconds.txt) · SHA-256 `671cdee3418a74c1d67c164c1c5fcc58359d705724024fd12638d2403cac9a4d` |
| Rulings | **5** (5 verified · 0 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`Obeka_Splitter_of_Seconds_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Obeka_Splitter_of_Seconds_Approval_Ready_Verification_2026-10-15.md) (Approval-ready verification section 6 (rules / interaction gate)) |

## Contents
- [Summary](#summary)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Key card-pair interactions](#key-card-pair-interactions)
- [Trigger ordering](#trigger-ordering)
- [Rules cited](#rules-cited)

## Summary

Obeka, Splitter of Seconds turns combat damage into extra beginning phases (upkeep only). The list scales the damage (Mjölnir, Dragonfire Blade, Hatred, Embercleave), adds triggers (Roaming Throne, Wizard's Staff), and cashes in the upkeeps with Time Sieve fed by Thopters, Treasures, Court copies or Replicated Rings, or with Mechanized Production and Darksteel Reactor. All 5 Spellbook lines are in the canonical list.

Rules surprises: Throne + Staff give three triggers, not four; Time Sieve can sacrifice itself; eight Thopters satisfy Mechanized Production whatever it enchants; Hatred's life is spent even if countered. No list errors.

## Commander rules text and edge cases

### obekass-01: Extra upkeeps come as extra beginning phases after combat; untap and draw are skipped

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Obeka, Splitter of Seconds

**Ruling.** When Obeka deals combat damage, you get that many extra upkeep steps after the current combat phase. Each one is its own extra beginning phase, with its untap and draw steps skipped. "At the beginning of your upkeep" abilities trigger in each one. Extra combats made later in the same combat happen first, and then the game goes to the postcombat main phase. That main phase is where you use what the upkeeps produced, such as Time Sieve.

**Citations**

- Oracle, *Obeka, Splitter of Seconds*: “Whenever Obeka deals combat damage to a player, you get that many additional upkeep steps after this phase.”
- Scryfall ruling, *Obeka, Splitter of Seconds*: “Since the upkeep step can only occur during the beginning phase, getting one or more additional upkeep steps outside of the beginning phase actually means you get an additional beginning phase for each of those upkeeps after this phase. In those beginning phases, the untap and draw steps will be skipped.”
- Scryfall ruling, *Obeka, Splitter of Seconds*: “Abilities that trigger "at the beginning of [your] upkeep" will trigger at the beginning of each additional upkeep step as well.”
- Scryfall ruling, *Obeka, Splitter of Seconds*: “If multiple phases are added to the same point in your turn, the most recently created phase happens first. For example, say Obeka deals combat damage and its ability resolves during your combat damage step, giving you two additional beginning phases each containing an upkeep step after this combat phase. During end of combat, another effect gives you an additional combat phase after this combat phase. The additional combat will happen first, followed by the additional beginning phases containing the two upkeep steps.”
- [CR 500.8](#cr-5008), [CR 501.1](#cr-5011)
- Source (re-verified): [`Obeka_Splitter_of_Seconds_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Obeka_Splitter_of_Seconds_Approval_Ready_Verification_2026-10-15.md) → “Obeka-created upkeeps occur in additional beginning phases after combat; untap/draw are skipped and upkeep-triggered abilities still trigger.”

## Combos and engine lines

### obekass-04: Time Sieve fed by upkeep artifacts: Thopter Spy Network, Smaug, Court of Vantress, Replicating Ring

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Obeka, Splitter of Seconds, Time Sieve, Thopter Spy Network, Smaug the Magnificent, Court of Vantress, Replicating Ring, Tamiyo's Journal

**Ruling.** Time Sieve needs five artifacts sacrificed, and it can count itself. Each upkeep producer makes artifacts:
- **Thopter Spy Network:** a Thopter per upkeep, if you control an artifact (Sieve counts) both when the trigger would happen and when it resolves.
- **Smaug:** a Treasure per upkeep.
- **Court of Vantress:** a Sieve token per upkeep while you're monarch.
- **Replicating Ring:** eight Replicated Rings after eight counters.

Four or more damage turns the normal upkeep plus four extras into five artifacts, then an extra turn in the postcombat main. It repeats while the board survives and Obeka keeps connecting. Tamiyo's Journal Clues also count, but you can't spend one Clue on both Journal and Sieve.

**Citations**

- Oracle, *Time Sieve*: “{T}, Sacrifice five artifacts: Take an extra turn after this one.”
- Scryfall ruling, *Time Sieve*: “You may sacrifice Time Sieve as one of the artifacts to pay the cost of its own ability.”
- Scryfall ruling, *Thopter Spy Network*: “Thopter Spy Network's first ability has an “intervening ‘if' clause.” That means (1) the ability won't trigger at all unless you control an artifact as your upkeep begins, and (2) the ability will do nothing if you don't control an artifact as it resolves.”
- [CR 603.4](#cr-6034), [CR 500.7](#cr-5007)
- Commander Spellbook [1558-5085-5471](https://commanderspellbook.com/combo/1558-5085-5471/) (community-maintained, retrieved 2026-10-16): “Activate Time Sieve by tapping it and sacrificing five Thopters, causing you to take an extra turn after this one.”
- Commander Spellbook [1558-5471-7651](https://commanderspellbook.com/combo/1558-5471-7651/) (community-maintained, retrieved 2026-10-16): “Activate Time Sieve by tapping it and sacrificing five Treasures, causing you to take an extra turn after this one.”
- Commander Spellbook [1469-1558-5471](https://commanderspellbook.com/combo/1469-1558-5471/) (community-maintained, retrieved 2026-10-16): “At the beginning of your upkeep, Court of Vantress triggers, creating a token copy of Time Sieve.”
- Commander Spellbook [1558-5471-7348](https://commanderspellbook.com/combo/1558-5471-7348/) (community-maintained, retrieved 2026-10-16): “Activate Time Sieve by tapping it and sacrificing five Replicating Ring tokens, causing you to take an extra turn after this one.”
- Source (re-verified): [`Obeka_Splitter_of_Seconds_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Obeka_Splitter_of_Seconds_Approval_Ready_Verification_2026-10-15.md) → “This is a board-dependent repeatable-turn engine, not an unconditional loop from an empty board.”

### obekass-05: Upkeep win cons: Mechanized Production, Darksteel Reactor; Super Intelligence draws

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Obeka, Splitter of Seconds, Mechanized Production, Darksteel Reactor, Super Intelligence

**Ruling.** Each extra upkeep feeds these:
- **Mechanized Production:** makes another token copy. You win while its trigger resolves if you control eight artifacts sharing one name, any name. Eight Thopters work even if Production is on something else.
- **Darksteel Reactor:** gets a charge counter and wins at 20.
- **Super Intelligence on Obeka:** draws a card each time.

**Citations**

- Oracle, *Mechanized Production*: “At the beginning of your upkeep, create a token that's a copy of enchanted artifact. Then if you control eight or more artifacts with the same name as one another, you win the game.”
- Scryfall ruling, *Mechanized Production*: “The eight artifacts with the same name don't have to have the same name as the enchanted artifact. For example, you win the game if you control eight Thopter artifact creature tokens as Mechanized Production's ability resolves, even if Mechanized Production isn't attached to a Thopter.”
- Scryfall ruling, *Mechanized Production*: “If you control eight or more artifacts that share a name while you control Mechanized Production, you won't win the game yet. You'll win the game while resolving its triggered ability during your upkeep.”
- [CR 603.8](#cr-6038), [CR 104.2b](#cr-1042b)
- Commander Spellbook [2047-5471](https://commanderspellbook.com/combo/2047-5471/) (community-maintained, retrieved 2026-10-16): “Repeat step 2 as necessary for the remaining upkeep steps until you win the game.”
- Source (re-verified): [`Obeka_Splitter_of_Seconds_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Obeka_Splitter_of_Seconds_Approval_Ready_Verification_2026-10-15.md) → “Every Obeka-created upkeep supplies another independent Reactor trigger.”

## Key card-pair interactions

### obekass-02: Scaling the count: Mjölnir doubles, power pumps add, Embercleave hits twice

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Obeka, Splitter of Seconds, Mjölnir, Hammer of Thor, Dragonfire Blade, Hatred, Combat Research, Embercleave

**Ruling.** The upkeep count is the combat damage Obeka actually deals:
- **Mjölnir:** doubles that damage. Obeka is a legendary, red, non-Villain Ogre Warlock, so its equip worthy {1} applies to her.
- **Dragonfire Blade:** +2/+2, and equip costs {1} on three-color Obeka.
- **Combat Research:** +1/+1 because she's legendary.
- **Hatred:** +X/+0 for X life paid as an additional cost. The life is gone even if Hatred is countered.
- **Embercleave:** double strike, so two separate damage events and two Obeka triggers.

Base Obeka (2/5) with Mjölnir and Blade deals 8, so 8 upkeeps per trigger.

**Citations**

- Oracle, *Mjölnir, Hammer of Thor*: “Double all damage equipped creature would deal.”
- Oracle, *Dragonfire Blade*: “Equip {4}. This ability costs {1} less to activate for each color of the creature it targets.”
- Scryfall ruling, *Hatred*: “The life payment is part of the cost to cast Hatred, so it is lost if this spell is countered.”
- [CR 510.4](#cr-5104), [CR 702.4b](#cr-7024b), [CR 614.1a](#cr-6141a)
- Source (re-verified): [`Obeka_Splitter_of_Seconds_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Obeka_Splitter_of_Seconds_Approval_Ready_Verification_2026-10-15.md) → “Obeka is legendary, red, and not a Villain, so she is worthy and may use equip worthy `{1}`.”

## Trigger ordering

### obekass-03: Roaming Throne (Ogre/Warlock) + Wizard's Staff: three Obeka triggers, not four

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Obeka, Splitter of Seconds, Roaming Throne, Wizard's Staff, Combat Research

**Ruling.** Roaming Throne naming Ogre or Warlock, and Wizard's Staff equipped to Obeka, each make her trigger one extra time. Together that's 1 + 1 + 1 = 3 triggers per damage event. Effects that add triggers stack by addition, not multiplication. The Staff uses equip {3}, because Obeka is a Warlock, not a Wizard. Combat Research's draw trigger belongs to Obeka, so it gets the extra triggers too.

**Citations**

- Oracle, *Roaming Throne*: “If a triggered ability of another creature you control of the chosen type triggers, it triggers an additional time.”
- Oracle, *Wizard's Staff*: “If a triggered ability of equipped creature triggers, that ability triggers an additional time.”
- Scryfall ruling, *Roaming Throne*: “Roaming Throne's last ability doesn't copy the triggered ability; it just causes the ability to trigger an additional time. Any choices made as you put the ability onto the stack, such as modes and targets, are made separately for each instance of the ability. Any choices made on resolution, such as whether to put counters on a permanent, are also made individually.”
- [CR 603.2d](#cr-6032d)
- Source (re-verified): [`Obeka_Splitter_of_Seconds_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Obeka_Splitter_of_Seconds_Approval_Ready_Verification_2026-10-15.md) → “With both applying, one combat-damage event generates **three total Obeka trigger instances**: original + Throne + Staff, not four.”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 104.2b

An effect may state that a player wins the game.

#### CR 500.7

Some effects can give a player extra turns. They do this by adding the turns directly after the specified turn. If a player is given multiple extra turns, the extra turns are added one at a time. If multiple players are given extra turns, the extra turns are added one at a time, in APNAP order (see rule 101.4). The most recently created turn will be taken first.

#### CR 500.8

Some effects can add phases to a turn. They do this by adding the phases directly after the specified phase. If multiple extra phases are created after the same phase, the most recently created phase will occur first.

#### CR 501.1

The beginning phase consists of three steps, in this order: untap, upkeep, and draw.

#### CR 510.4

If at least one attacking or blocking creature has first strike (see rule 702.7) or double strike (see rule 702.4) as the combat damage step begins, the only creatures that assign combat damage in that step are those with first strike or double strike. After that step, instead of proceeding to the end of combat step, the phase gets a second combat damage step. The only creatures that assign combat damage in that step are the remaining attackers and blockers that had neither first strike nor double strike as the first combat damage step began, as well as the remaining attackers and blockers …

#### CR 603.2d

An ability may state that a triggered ability triggers additional times. In this case, rather than simply determining that such an ability has triggered, determine how many times it should trigger, then that ability triggers that many times. An effect that states that an ability triggers additional times doesn’t invoke itself repeatedly and doesn’t apply to other effects that affect how many times an ability triggers. An effect that states a triggered ability of an object triggers additional times refers only to triggered abilities that object has, not to any delayed or reflexive triggered …

#### CR 603.4

A triggered ability may read “When/Whenever/At [trigger event], if [condition], [effect].” When the trigger event occurs, the ability checks whether the stated condition is true. The ability triggers only if it is; otherwise it does nothing. If the ability triggers, it checks the stated condition again as it resolves. If the condition isn’t true at that time, the ability is removed from the stack and does nothing. Note that this mirrors the check for legal targets. This rule is referred to as the “intervening ‘if’ clause” rule. (The word “if” has only its normal English meaning anywhere else …

#### CR 603.8

Some triggered abilities trigger when a game state (such as a player controlling no permanents of a particular card type) is true, rather than triggering when an event occurs. These abilities trigger as soon as the game state matches the condition. They’ll go onto the stack at the next available opportunity. These are called state triggers. (Note that state triggers aren’t the same as state-based actions.) A state-triggered ability doesn’t trigger again until the ability has resolved, has been countered, or has otherwise left the stack. Then, if the object with the ability is still in the …

#### CR 614.1a

Effects that use the word “instead” are replacement effects. Most replacement effects use the word “instead” to indicate what events will be replaced with other events.

#### CR 702.4b

If at least one attacking or blocking creature has first strike (see rule 702.7) or double strike as the combat damage step begins, the only creatures that assign combat damage in that step are those with first strike or double strike. After that step, instead of proceeding to the end of combat step, the phase gets a second combat damage step. The only creatures that assign combat damage in that step are the remaining attackers and blockers that had neither first strike nor double strike as the first combat damage step began, as well as the remaining attackers and blockers that currently have …

