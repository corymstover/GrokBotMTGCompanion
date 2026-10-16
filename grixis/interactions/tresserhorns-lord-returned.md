---
title: "Tresserhorn's Lord, Returned — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Tresserhorn's Lord, Returned — Interaction Review

> Bot cycle 56 · batch F · reviewed 2026-10-16. Deck: [Tresserhorn's Lord, Returned](../decks/tresserhorns-lord-returned.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/tresserhorns-lord-returned.txt`](../../exports/grixis-archidekt/tresserhorns-lord-returned.txt) · SHA-256 `d30533e2a9574c55552115353ba2c16fc36aacf11be3c4b700d52bc9cddbcd3e` |
| Rulings | **7** (5 verified · 0 uncertain · 2 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md) (Approval-ready verification (no rules attestation JSON in source)) |

## Contents
- [Summary](#summary)
- [Flags and open questions](#flags-and-open-questions)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [What the list depends on](#what-the-list-depends-on)
- [Legality and project exceptions](#legality-and-project-exceptions)
- [Rules cited](#rules-cited)

## Summary

Tresserhorn's Lord, Returned is a 10/4 trample, indestructible Zombie. When he enters you must sacrifice three creatures (three draws) or sacrifice him (one draw), and he draws on every creature sacrifice after that. The deck loops The Locust God with a free outlet, loops Gravecrawler, and spikes draws with Plumb the Forbidden, Allure of Power and Infantry Shield. All 21 Spellbook lines have every piece in the list. The source has no rules attestation JSON, so this review uses the approval-ready verification, and the canonical list matches its 19-card delta. The commander's one official ruling (Gatherer, 7/29/2026) is quoted verbatim. The deck stays PENDING_RELEASE until 2026-11-13.

Rules surprises: declining the enter cost still draws 1; three sacrifices = three draws; Blasphemous Edict takes Tresserhorn unless you have 13+ other creatures; Nightscape Familiar saves only {1}. Flags: anti-synergy (Edict) and documentation (the source's premature legality claim). No list errors.

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [tressret-05](#tressret-05-blasphemous-edict-sacrifices-tresserhorn-unless-you-have-13-other-creatures) | 🚩 list flag (anti-synergy) | Blasphemous Edict sacrifices Tresserhorn unless you have 13+ other creatures | Blasphemous Edict sacrifices Tresserhorn too unless you control 13+ other creatures (the cards still draw). |
| [tressret-07](#tressret-07-pending-release-the-source-says-its-legal-now-but-official-sources-say-2026-11-13) | 🚩 list flag (documentation) | Pending release: the source says it's legal now, but official sources say 2026-11-13 | Source claims current Commander legality; Gatherer/Wizards/Scryfall: not legal until 2026-11-13. Pending state kept. |

## Commander rules text and edge cases

### tressret-01: The enter trigger: pay all of it (three sacrifices = three draws) or he's sacrificed (one draw)

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Tresserhorn's Lord, Returned

**Ruling.** When Tresserhorn's Lord enters, you either do all of it or none: sacrifice three creatures, pay 3 life and have an opponent draw three. You can't pay part of it.
- **If you pay,** he's on the battlefield when the three sacrifices happen, so his draw ability triggers three times, once per creature.
- **If you don't or can't,** he's sacrificed. His own sacrifice triggers his draw ability once, by looking back in time, and he can then go to the command zone.

His indestructibility doesn't stop either sacrifice.

Official Gatherer ruling (7/29/2026, Mystery Booster Commander Edition release notes; https://gatherer.wizards.com/MBC/en-us/52/tresserhorns-lord-returned): "If you sacrifice Tresserhorn's Lord for any reason (including as part of the effect of his first triggered ability), his last triggered ability will trigger. If you sacrifice him at the same time as one or more other creatures, his last ability will trigger for each of those creatures, including himself." That ruling isn't in the 2026-10-15 rulings bulk yet; it was quoted from Gatherer on 2026-10-16.

**Citations**

- Oracle, *Tresserhorn's Lord, Returned*: “When Tresserhorn's Lord enters, sacrifice him unless you sacrifice three creatures, pay 3 life, and have target opponent draw three cards.”
- Oracle, *Tresserhorn's Lord, Returned*: “Whenever you sacrifice a creature, draw a card.”
- [CR 118.12](#cr-11812), [CR 603.10a](#cr-60310a), [CR 603.2c](#cr-6032c), [CR 701.21a](#cr-70121a)
- Source (re-verified): [`Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md) → “The same release notes state that if Tresserhorn is sacrificed, including to its own ETB trigger, its sacrifice-draw ability triggers”

## Combos and engine lines

### tressret-02: The Locust God + any free sacrifice outlet: endless draw-and-Insect loop

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Tresserhorn's Lord, Returned, The Locust God, Ashnod's Altar, Phyrexian Altar, Viscera Seer, Carrion Feeder, Goblin Bombardment, Woe Strider, Skullclamp, Yawgmoth, Thran Physician

**Ruling.** Sacrifice a creature to a free outlet. Tresserhorn draws a card, which makes a hasty Insect from The Locust God, and you sacrifice that Insect next. That's Spellbook 1339-2034-7920, 1339-2292-7920, 1339-2438-7920, 1339-5147-7920 and 997-1339-7920. Skullclamp and Yawgmoth versions work even without Tresserhorn. Tresserhorn's draw is mandatory, but each sacrifice is your choice, so stop before you deck yourself. Goblin Bombardment or a drain payoff ends the game.

**Citations**

- Oracle, *The Locust God*: “Whenever you draw a card, create a 1/1 blue and red Insect creature token with flying and haste.”
- Scryfall ruling, *The Locust God*: “If a spell or ability causes you to put cards into your hand without specifically using the word “draw,” The Locust God's first triggered ability won't trigger.”
- [CR 603.2](#cr-6032), [CR 104.3c](#cr-1043c)
- Commander Spellbook [1339-2034-7920](https://commanderspellbook.com/combo/1339-2034-7920/) (community-maintained, retrieved 2026-10-16): “When the creature dies, Tresserhorn's Lord triggers, causing you to draw a card.”
- Commander Spellbook [1339-2034-7920](https://commanderspellbook.com/combo/1339-2034-7920/) (community-maintained, retrieved 2026-10-16): “The Locust God triggers, creating a 1/1 Insect creature token with flying and haste.”
- Source (re-verified): [`Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md) → “The Locust God + Tresserhorn + a free sacrifice outlet loops once a creature sacrifice/draw seeds the process”

### tressret-03: Gravecrawler loops: the Zombie commander enables them and draws on each

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Tresserhorn's Lord, Returned, Gravecrawler, Phyrexian Altar, Pitiless Plunderer, Warren Soultrader, Blood Artist, Zulaport Cutthroat, Bastion of Remembrance, Marionette Apprentice

**Ruling.** Tresserhorn is a Zombie, so Gravecrawler can be cast from your graveyard while he's out. Phyrexian Altar or a Pitiless Plunderer Treasure pays its {B}, and each loop draws a card. Warren Soultrader costs 1 life per loop, so it needs a payoff that gains life: Blood Artist, Zulaport Cutthroat or Bastion of Remembrance. Marionette Apprentice drains opponents but doesn't give you life back.

**Citations**

- Oracle, *Gravecrawler*: “You may cast this card from your graveyard as long as you control a Zombie.”
- [CR 601.2](#cr-6012)
- Commander Spellbook [2577-4050](https://commanderspellbook.com/combo/2577-4050/) (community-maintained, retrieved 2026-10-16): “Cast Gravecrawler from your graveyard by paying {B}.”
- Commander Spellbook [2577-3025-5670](https://commanderspellbook.com/combo/2577-3025-5670/) (community-maintained, retrieved 2026-10-16): “When Gravecrawler dies, Bastion of Remembrance triggers, causing you to gain 1 life and target opponent to lose 1 life.”
- Source (re-verified): [`Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md) → “Gravecrawler + Phyrexian Altar: Tresserhorn is a Zombie”

## Engines and payoffs

### tressret-04: Sacrifice-as-cost draw spikes: Plumb the Forbidden, Allure of Power, Infantry Shield

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Tresserhorn's Lord, Returned, Plumb the Forbidden, My Precious // Allure of Power, Infantry Shield, Wand of Orcus

**Ruling.** Big draw turns:
- **Plumb the Forbidden** sacrificing N creatures gives N Tresserhorn draws plus N+1 Plumb draws, so 2N+1 cards for N+1 life.
- **Allure of Power's** sacrifice is an additional cost, so it's a Tresserhorn draw on top of its two. Later, My Precious gives hexproof and unblockable.
- **Infantry Shield** on the 10-power Tresserhorn makes 10 attacking Warriors. They're sacrificed at the next end step, which is 10 draws.
- **Wand of Orcus** gives Tresserhorn deathtouch, so with trample he only needs to assign 1 damage to each blocker. Each damage he deals to a player is a Zombie.

**Citations**

- Oracle, *Plumb the Forbidden*: “As an additional cost to cast this spell, you may sacrifice one or more creatures. When you do, copy this spell for each creature sacrificed this way.”
- Scryfall ruling, *Infantry Shield*: “Although the Warrior tokens enter as attacking creatures, they were never declared as attacking creatures. Abilities that trigger whenever a creature attacks won’t trigger when the tokens enter attacking.”
- [CR 702.181a](#cr-702181a), [CR 702.2c](#cr-7022c), [CR 702.19b](#cr-70219b)
- Source (re-verified): [`Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md) → “Plumb the Forbidden with N creatures sacrificed generates N Tresserhorn triggers plus N+1 spell/copy draws: 2N+1 cards total”

### tressret-06: Cost and protection: Nightscape Familiar ({1} off), Not of This World ({0} for a 10-power target), Cavern

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Tresserhorn's Lord, Returned, Nightscape Familiar, Not of This World, Cavern of Souls

**Ruling.** Support pieces:
- **Nightscape Familiar:** Tresserhorn is blue and red, but it still reduces his cost by only {1}, to {1}{U}{B}{R}.
- **Not of This World:** costs {0} against a spell or ability targeting the 10-power Tresserhorn. It doesn't help against untargeted sweepers or edicts.
- **Cavern of Souls** naming Zombie makes Tresserhorn, Gravecrawler and other Zombies uncounterable.

**Citations**

- Scryfall ruling, *Nightscape Familiar*: “A spell you cast that’s blue and red costs {1} less, not {2} less.”
- Scryfall ruling, *Not of This World*: “Not of This World's second ability checks the current state of the targets of the spell or ability it's targeting to determine whether one of them is a creature you control with power 7 or greater. This check is made as you cast Not of This World, before you activate mana abilities.”
- [CR 601.2f](#cr-6012f)
- Source (re-verified): [`Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md) → “Nightscape Familiar reduces only generic mana”

## What the list depends on

### tressret-05: Blasphemous Edict sacrifices Tresserhorn unless you have 13+ other creatures

**Status:** 🚩 list flag · **Evidence:** fact · **Cards:** Tresserhorn's Lord, Returned, Blasphemous Edict

**Ruling.** Blasphemous Edict makes each player sacrifice thirteen creatures. That gets around indestructible. All sacrifices happen at once, so Tresserhorn draws for each creature you lose, himself included. If you control fewer than thirteen creatures, you must sacrifice all of them, Tresserhorn too. To keep him, you need at least 13 other creatures. Otherwise plan to recast him, with tax.

**List flag (anti-synergy).** Blasphemous Edict sacrifices Tresserhorn too unless you control 13+ other creatures (the cards still draw).

**Citations**

- Scryfall ruling, *Blasphemous Edict*: “If a player controls fewer than thirteen creatures when Blasphemous Edict resolves, they will sacrifice all of their creatures.”
- Scryfall ruling, *Blasphemous Edict*: “Starting with the player whose turn it is, each player in turn order chooses which creatures they will sacrifice, then all the creatures chosen by all players are sacrificed at the same time. Players get to know the choices made by players who chose before them.”
- [CR 701.21a](#cr-70121a)
- Source (re-verified): [`Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md) → “Blasphemous Edict's chosen creatures are sacrificed simultaneously.”

## Legality and project exceptions

### tressret-07: Pending release: the source says it's legal now, but official sources say 2026-11-13

**Status:** 🚩 list flag · **Evidence:** fact · **Cards:** Tresserhorn's Lord, Returned

**Ruling.** The approval-ready note says the Mystery Booster Commander release notes make Tresserhorn's Lord, Returned (MBC #52) Commander-legal now, and that the project exception is stale. Official sources disagree for now. Gatherer lists Commander under "Not Legal Formats", and Wizards' "What's Inside Mystery Booster Commander Edition?" (editor's note) says: "New-to-Magic MBC cards will be legal in Commander on November 13, 2026." Scryfall 2026-10-15 bulk agrees. The deck stays PENDING_RELEASE with its registered exception. This review checks interactions only, and the legality claim is the source's documentation error.

**List flag (documentation).** Source claims current Commander legality; Gatherer/Wizards/Scryfall: not legal until 2026-11-13. Pending state kept.

**Citations**

- Oracle, *Tresserhorn's Lord, Returned*: “Trample, indestructible”
- Source (re-verified): [`Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md) → “Current official release-note legality supersedes the stale project future-release exception for Tresserhorn's Lord, Returned.”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 104.3c

If a player is required to draw more cards than are left in their library, they draw the remaining cards and then lose the game the next time a player would receive priority. (This is a state-based action. See rule 704.)

#### CR 118.12

Some spells, activated abilities, and triggered abilities read, “[Do something]. If [a player] [does, doesn’t, or can’t], [effect].” Or “[A player] may [do something]. If [that player] [does, doesn’t, or can’t], [effect].” The action [do something] is a cost, paid when the spell or ability resolves. The “If [a player] [does, doesn’t, or can’t]” clause checks whether the player chose to pay an optional cost or started to pay a mandatory cost, regardless of what events actually occurred.

#### CR 601.2

To cast a spell is to take it from where it is (usually the hand), put it on the stack, and pay its costs, so that it will eventually resolve and have its effect. Casting a spell includes proposal of the spell (rules 601.2a–d) and determination and payment of costs (rules 601.2f–h). To cast a spell, a player follows the steps listed below, in order. A player must be legally allowed to cast the spell to begin this process (see rule 601.3). If a player is unable to comply with the requirements of a step listed below while performing that step, the casting of the spell is illegal; the game …

#### CR 601.2f

The player determines the total cost of the spell. Usually this is just the mana cost. Some spells have additional or alternative costs. Some effects may increase or reduce the cost to pay, or may provide other alternative costs. Costs may include paying mana, tapping permanents, sacrificing permanents, discarding cards, and so on. The total cost is the mana cost or alternative cost (as determined in rule 601.2b), plus all additional costs and cost increases, and minus all cost reductions. If multiple cost reductions apply, the player may apply them in any order. If the mana component of the …

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 603.2c

An ability triggers only once each time its trigger event occurs. However, it can trigger repeatedly if one event contains multiple occurrences.

#### CR 603.10a

Some zone-change triggers look back in time. These are leaves-the-battlefield abilities, abilities that trigger when a player sacrifices a permanent, abilities that trigger when a card leaves a graveyard, and abilities that trigger when an object that all players can see is put into a hand or library.

#### CR 701.21a

To sacrifice a permanent, its controller moves it from the battlefield directly to its owner’s graveyard. A player can’t sacrifice something that isn’t a permanent, or something that’s a permanent they don’t control. Sacrificing a permanent doesn’t destroy it, so regeneration or other effects that replace destruction can’t affect this action.

#### CR 702.2c

Any nonzero amount of combat damage assigned to a creature by a source with deathtouch is considered to be lethal damage for the purposes of determining if excess damage is being dealt.

#### CR 702.19b

The controller of an attacking creature with trample first assigns damage to the creature(s) blocking it. Once all those blocking creatures are assigned lethal damage, any excess damage is assigned as its controller chooses among those blocking creatures and the player, planeswalker, or battle the creature is attacking. When checking for assigned lethal damage, take into account damage already marked on the creature and damage from other creatures that’s being assigned during the same combat damage step, but not any abilities or effects that might change the amount of damage that’s actually …

#### CR 702.181a

Mobilize is a triggered ability. “Mobilize N” means “Whenever this creature attacks, create N 1/1 red Warrior creature tokens. Those tokens enter tapped and attacking. Sacrifice them at the beginning of the next end step.”

