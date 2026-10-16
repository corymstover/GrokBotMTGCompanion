---
title: "Thraximundar — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Thraximundar — Interaction Review

> Bot cycle 56 · batch F · reviewed 2026-10-16. Deck: [Thraximundar](../decks/thraximundar.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-15), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/thraximundar.txt`](../../exports/grixis-archidekt/thraximundar.txt) · SHA-256 `e5cf53533e1e71adce8e404d00cbad9a31c5ad68b9ac79632319ffc9b26e133e` |
| Rulings | **5** (4 verified · 0 uncertain · 1 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-15 · rulings 2026-10-15 |
| Source attestations | [`Thraximundar_Approval_Ready_Verification_v2_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Thraximundar_Approval_Ready_Verification_v2_2026-10-15.md) (Approval-ready verification v2 (no rules attestation JSON in source)) |

## Contents
- [Summary](#summary)
- [Flags and open questions](#flags-and-open-questions)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [What the list depends on](#what-the-list-depends-on)
- [Rules cited](#rules-cited)

## Summary

Thraximundar is a hasty Zombie that forces an edict when it attacks and gets a +1/+1 counter whenever any player sacrifices a creature. The deck pairs opponent edicts (Winter, Vona's Hunger, Flare of Malice, Call to the Grave) with sacrifice loops: 17 Spellbook lines with Gravecrawler, which Thraximundar enables as the other Zombie, and Reassembling Skeleton. The source has no rules attestation JSON, so this review uses the v2 approval-ready verification, and the canonical list matches its 13-card delta.

Rules surprises: the attack edict resolves before blocks; any sacrifice anywhere grows him; Rooftop Storm still pays commander tax. One dependency-risk flag: Cultist's upkeep sacrifice is mandatory and can force Thraximundar to sacrifice himself. No list errors.

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [thrax-04](#thrax-04-cultist-of-the-absolute-33-flying-deathtouch-ward-and-a-mandatory-upkeep-sacrifice) | 🚩 list flag (dependency-risk) | Cultist of the Absolute: +3/+3 flying deathtouch ward, and a mandatory upkeep sacrifice | Cultist of the Absolute's granted upkeep sacrifice is mandatory; with no other creature, Thraximundar must sacrifice himself. |

## Commander rules text and edge cases

### thrax-01: Thraximundar: attack edict before blocks; grows on ANY player's sacrifice

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Thraximundar, Winter, Tormented Loner, Vona's Hunger, Flare of Malice, Call to the Grave

**Ruling.** Thraximundar's attack trigger resolves in the declare attackers step, so the defending player sacrifices before they can block. His counter trigger fires on every creature sacrifice by any player for any reason:
- **Your own outlets:** each sacrifice is a trigger.
- **Opponents' edicts:** Winter, Vona's Hunger and Flare of Malice each give one trigger per creature sacrificed. A planeswalker sacrificed to Flare doesn't count.
- **Flare of Malice's alternative cost:** sacrificing a nontoken black creature to cast it is a sacrifice too.
- **Call to the Grave:** every player's upkeep. Thraximundar is a Zombie, so it can't be chosen.

**Citations**

- Oracle, *Thraximundar*: “Whenever a player sacrifices a creature, you may put a +1/+1 counter on Thraximundar.”
- Oracle, *Call to the Grave*: “At the beginning of each player's upkeep, that player sacrifices a non-Zombie creature of their choice.”
- Scryfall ruling, *Thraximundar*: “Thraximundar's middle ability resolves during the declare attackers step. The defending player sacrifices a creature before it would get a chance to block.”
- Scryfall ruling, *Thraximundar*: “Thraximundar's last ability triggers whenever any player (including you) sacrifices a creature for any reason. It doesn't trigger only when a creature is sacrificed due to its middle ability. Note that Thraximundar itself doesn't allow you to sacrifice any creatures.”
- [CR 508.1m](#cr-5081m), [CR 603.2](#cr-6032), [CR 701.21a](#cr-70121a)
- Source (re-verified): [`Thraximundar_Approval_Ready_Verification_v2_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Thraximundar_Approval_Ready_Verification_v2_2026-10-15.md) → “Its attack trigger makes the defending player sacrifice a creature, and its last ability triggers whenever **any player** sacrifices a creature.”
- Source (re-verified): [`Thraximundar_Approval_Ready_Verification_v2_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Thraximundar_Approval_Ready_Verification_v2_2026-10-15.md) → “**Call to the Grave** makes each player sacrifice a non-Zombie creature on that player's upkeep.”

## Combos and engine lines

### thrax-02: Gravecrawler loops: Thraximundar is the "other Zombie"

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Thraximundar, Gravecrawler, Phyrexian Altar, Ashnod's Altar, Rooftop Storm, Carrion Feeder, Pitiless Plunderer, Warren Soultrader, Goblin Bombardment, Altar of Dementia, Grimgrin, Corpse-Born, Blood Artist, Zulaport Cutthroat

**Ruling.** Gravecrawler can be cast from your graveyard while you control a Zombie, and Thraximundar is one. Sacrifice it to an outlet, then recast it with:
- **Phyrexian Altar:** its {B}.
- **Rooftop Storm:** {0}.
- **Pitiless Plunderer:** its Treasure.
- **Warren Soultrader:** its Treasure.

That's 13 Spellbook lines, all with every piece in the list. Every loop is a sacrifice, so Thraximundar grows without limit. Add Blood Artist, Zulaport or Goblin Bombardment to finish. Once Gravecrawler is on the stack, losing the other Zombie doesn't matter. Rooftop Storm doesn't change Gravecrawler's mana value.

**Citations**

- Oracle, *Gravecrawler*: “You may cast this card from your graveyard as long as you control a Zombie.”
- Oracle, *Rooftop Storm*: “You may pay {0} rather than pay the mana cost for Zombie creature spells you cast.”
- Scryfall ruling, *Gravecrawler*: “Once you've cast Gravecrawler and it's on the stack, it doesn't matter if you lose control of the other Zombie.”
- Scryfall ruling, *Rooftop Storm*: “The mana cost and mana value of the spell are unchanged. Rooftop Storm only changes what you pay.”
- [CR 601.2](#cr-6012), [CR 118.9](#cr-1189)
- Commander Spellbook [2577-4050](https://commanderspellbook.com/combo/2577-4050/) (community-maintained, retrieved 2026-10-16): “You control an additional Zombie.”
- Commander Spellbook [2577-4050](https://commanderspellbook.com/combo/2577-4050/) (community-maintained, retrieved 2026-10-16): “Cast Gravecrawler from your graveyard by paying {B}.”
- Commander Spellbook [2438-2452-2577](https://commanderspellbook.com/combo/2438-2452-2577/) (community-maintained, retrieved 2026-10-16): “Cast Gravecrawler from your graveyard by paying {0}.”
- Source (re-verified): [`Thraximundar_Approval_Ready_Verification_v2_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Thraximundar_Approval_Ready_Verification_v2_2026-10-15.md) → “**Gravecrawler + Phyrexian Altar + another Zombie:** sacrifice Gravecrawler for {B}, then recast it for {B}.”

### thrax-03: Reassembling Skeleton + Pitiless Plunderer + Ashnod's / Phyrexian Altar

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Thraximundar, Reassembling Skeleton, Pitiless Plunderer, Ashnod's Altar, Phyrexian Altar, Warren Soultrader

**Ruling.** Sacrificing Skeleton gives altar mana plus a Plunderer Treasure, and that pays {1}{B} to return it tapped. Ashnod's Altar nets {C} per loop. Spellbook lists 1580-2034-4871, 1580-4050-4871 and the Soultrader variants. These loops don't need a Zombie. Each sacrifice is another Thraximundar counter.

**Citations**

- Oracle, *Reassembling Skeleton*: “{1}{B}: Return this card from your graveyard to the battlefield tapped.”
- [CR 605.1a](#cr-6051a)
- Commander Spellbook [1580-2034-4871](https://commanderspellbook.com/combo/1580-2034-4871/) (community-maintained, retrieved 2026-10-16): “Activate Reassembling Skeleton by paying {1}{B}, returning it from your graveyard to the battlefield tapped.”
- Source (re-verified): [`Thraximundar_Approval_Ready_Verification_v2_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Thraximundar_Approval_Ready_Verification_v2_2026-10-15.md) → “**Reassembling Skeleton + Pitiless Plunderer + Ashnod's Altar:** Ashnod's Altar supplies {C}{C} and Plunderer supplies a Treasure”

## Engines and payoffs

### thrax-05: Yawgmoth proliferate, Shizo fear, Command Beacon, Rooftop Storm on the commander

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Thraximundar, Yawgmoth, Thran Physician, Shizo, Death's Storehouse, Command Beacon, Rooftop Storm

**Ruling.** Support pieces:
- **Yawgmoth:** pay 1 life and sacrifice another creature for a card and an optional -1/-1 counter. Each one is a Thraximundar counter, and his proliferate adds another +1/+1.
- **Shizo:** gives the legendary Thraximundar fear for {B}.
- **Command Beacon:** puts him in your hand. Casting him from hand has no commander tax and doesn't add to it.
- **Rooftop Storm:** casts the Zombie Thraximundar for {0} instead of {4}{U}{B}{R}, but commander tax from the command zone is still added.

**Citations**

- Oracle, *Shizo, Death's Storehouse*: “{B}, {T}: Target legendary creature gains fear until end of turn. (It can't be blocked except by artifact creatures and/or black creatures.)”
- Scryfall ruling, *Command Beacon*: “If you cast a commander from your hand, the commander tax doesn't apply. Additionally, that casting won't add to commander tax if you later cast the commander from the command zone.”
- Scryfall ruling, *Yawgmoth, Thran Physician*: “To proliferate, you can choose any permanent that has a counter, including ones controlled by opponents. You can choose any player who has a counter, including opponents. You can't choose cards in any zone other than the battlefield, even if they have counters on them.”
- [CR 701.34a](#cr-70134a), [CR 903.8](#cr-9038), [CR 702.36b](#cr-70236b)
- Source (re-verified): [`Thraximundar_Approval_Ready_Verification_v2_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Thraximundar_Approval_Ready_Verification_v2_2026-10-15.md) → “**Rooftop Storm** remains a major commander-specific accelerator”

## What the list depends on

### thrax-04: Cultist of the Absolute: +3/+3 flying deathtouch ward, and a mandatory upkeep sacrifice

**Status:** 🚩 list flag · **Evidence:** fact · **Cards:** Thraximundar, Cultist of the Absolute

**Ruling.** Cultist of the Absolute gives commander creatures you own +3/+3, flying, deathtouch, "Ward—Pay 3 life" and "At the beginning of your upkeep, sacrifice a creature." That upkeep sacrifice is mandatory and can be any creature, including Thraximundar himself. With another creature it's a free counter. If Thraximundar is your only creature, you must sacrifice him. Keep fodder such as Gravecrawler or Reassembling Skeleton, which can come back.

**List flag (dependency-risk).** Cultist of the Absolute's granted upkeep sacrifice is mandatory; with no other creature, Thraximundar must sacrifice himself.

**Citations**

- Oracle, *Cultist of the Absolute*: “Commander creatures you own get +3/+3 and have flying, deathtouch, "Ward—Pay 3 life," and "At the beginning of your upkeep, sacrifice a creature."”
- [CR 603.2](#cr-6032), [CR 701.21a](#cr-70121a)
- Source (re-verified): [`Thraximundar_Approval_Ready_Verification_v2_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Thraximundar_Approval_Ready_Verification_v2_2026-10-15.md) → “Sacrificing another creature to the granted upkeep ability grows Thraximundar.”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 118.9

Some spells have alternative costs. An alternative cost is a cost listed in a spell’s text, or applied to it from another effect, that its controller may pay rather than paying the spell’s mana cost. Alternative costs are usually phrased, “You may [action] rather than pay [this object’s] mana cost,” or “You may cast [this object] without paying its mana cost.” Note that some alternative costs are listed in keywords; see rule 702.

#### CR 508.1m

Any abilities that trigger on attackers being declared trigger.

#### CR 601.2

To cast a spell is to take it from where it is (usually the hand), put it on the stack, and pay its costs, so that it will eventually resolve and have its effect. Casting a spell includes proposal of the spell (rules 601.2a–d) and determination and payment of costs (rules 601.2f–h). To cast a spell, a player follows the steps listed below, in order. A player must be legally allowed to cast the spell to begin this process (see rule 601.3). If a player is unable to comply with the requirements of a step listed below while performing that step, the casting of the spell is illegal; the game …

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 605.1a

An activated ability is a mana ability if it meets all of the following criteria: it doesn’t require a target (see rule 115.6), it could add mana to a player’s mana pool when it resolves, it’s not a loyalty ability (see rule 606, “Loyalty Abilities”), and its cost and effect don’t move any card to or from a library. Do not take into account replacement effects that may apply, other than self-replacement effects, when evaluating these criteria.

#### CR 701.21a

To sacrifice a permanent, its controller moves it from the battlefield directly to its owner’s graveyard. A player can’t sacrifice something that isn’t a permanent, or something that’s a permanent they don’t control. Sacrificing a permanent doesn’t destroy it, so regeneration or other effects that replace destruction can’t affect this action.

#### CR 701.34a

To proliferate means to choose any number of permanents and/or players that have a counter, then give each one additional counter of each kind that permanent or player already has.

#### CR 702.36b

A creature with fear can’t be blocked except by artifact creatures and/or black creatures. (See rule 509, “Declare Blockers Step.”)

#### CR 903.8

A player may cast a commander they own from the command zone. A commander cast from the command zone costs an additional {2} for each previous time the player casting it has cast it from the command zone that game. This additional cost is informally known as the “commander tax.”

