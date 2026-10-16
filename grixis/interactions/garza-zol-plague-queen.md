---
title: "Garza Zol, Plague Queen — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Garza Zol, Plague Queen — Interaction Review

> Bot cycle 48 · batch B · reviewed 2026-10-16. Deck: [Garza Zol, Plague Queen](../decks/garza-zol-plague-queen.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-15), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/garza-zol-plague-queen.txt`](../../exports/grixis-archidekt/garza-zol-plague-queen.txt) · SHA-256 `b0dfe1fc5ad19d3d8b3eeb350b1abc42f0de3e32526032a558b5717df32e5fda` |
| Rulings | **11** (10 verified · 0 uncertain · 1 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-15 · rulings 2026-10-15 |
| Source attestations | [`Garza_Zol_Plague_Queen_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/garza_zol_plague_queen_2026-10-14/Garza_Zol_Plague_Queen_Rules_Attestation.json) (15 interactions, all PASS) |

## Contents
- [Summary](#summary)
- [Flags and open questions](#flags-and-open-questions)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [Replacement and prevention effects](#replacement-and-prevention-effects)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [What the list depends on](#what-the-list-depends-on)
- [Rules cited](#rules-cited)

## Summary

Garza Zol, Plague Queen is a flying, hasty Voltron commander. She grows when creatures she damaged die and draws when she connects. This review re-verifies the fifteen items of the deck's rules attestation, and confirms the Kediss + Grafted Exoskeleton and Aggravated Assault lines against cached Commander Spellbook steps.

Rules surprise: Jeska, Thrice Reborn (in the 99) enters with 0 loyalty and dies if Garza hasn't been cast from the command zone yet. Casting Garza from hand after Command Beacon doesn't count (dependency-risk flag, no list change). No list errors.

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [garza-08](#garza-08-jeska-needs-garza-cast-from-the-command-zone-first) | 🚩 list flag (dependency-risk) | Jeska needs Garza cast from the command zone first | Edge case, not a list error: Jeska is a planeswalker in the 99 here, not a partner commander, so her loyalty depends on how many times Garza was cast from the command zone. Cast Garza normally at least once before deploying Jeska. |

## Commander rules text and edge cases

### garza-01: Any damage from Garza counts, and the death can come later

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Garza Zol, Plague Queen

**Ruling.** Garza's counter ability looks for a creature that Garza dealt damage to at any point this turn and that then dies, however it dies. The damage can be combat or noncombat (her Chandra's Ignition or Nova Flame blast, a Thornbite Staff ping). Each such death is a separate trigger and a separate counter.

**Citations**

- Oracle, *Garza Zol, Plague Queen*: “Whenever a creature dealt damage by Garza Zol this turn dies, put a +1/+1 counter on Garza Zol.”
- [CR 120.1](#cr-1201), [CR 603.10a](#cr-60310a), [CR 700.4](#cr-7004)
- Source (re-verified): [`Garza_Zol_Plague_Queen_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/garza_zol_plague_queen_2026-10-14/Garza_Zol_Plague_Queen_Rules_Attestation.json) → “Garza damage-and-death trigger scope”

## Combos and engine lines

### garza-05: Kediss + Grafted Exoskeleton: one hit poisons every opponent

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Garza Zol, Plague Queen, Kediss, Emberclaw Familiar, Grafted Exoskeleton

**Ruling.** Garza is 5/5; Exoskeleton makes her 7/7 with infect, so she needs three more power for 10 (counters, Hatred). Her combat damage gives the defending player 10+ poison. Kediss then makes Garza deal that much noncombat damage to each other opponent. That damage also has infect, so each other opponent gets 10+ poison too. Kediss's extra damage isn't combat damage, so it doesn't count as commander damage.

**Citations**

- Oracle, *Kediss, Emberclaw Familiar*: “Whenever a commander you control deals combat damage to an opponent, it deals that much damage to each other opponent.”
- Scryfall ruling, *Grafted Exoskeleton*: “Infect's effect applies to any damage, not just combat damage.”
- Scryfall ruling, *Kediss, Emberclaw Familiar*: “The damage the commander deals as a result of Kediss's triggered ability isn't combat damage. It isn't tracked with combat damage dealt by commanders and won't cause Kediss's ability to trigger again.”
- [CR 702.90b](#cr-70290b), [CR 704.5c](#cr-7045c), [CR 903.10a](#cr-90310a)
- Commander Spellbook [2822-3681](https://commanderspellbook.com/combo/2822-3681/) (community-maintained, retrieved 2026-10-16): “Your commander has power 10 or greater.”
- Commander Spellbook [2822-3681](https://commanderspellbook.com/combo/2822-3681/) (community-maintained, retrieved 2026-10-16): “Kediss triggers, causing your commander to give each other opponent at least ten poison counters due to its infect.”
- Source (re-verified): [`Garza_Zol_Plague_Queen_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/garza_zol_plague_queen_2026-10-14/Garza_Zol_Plague_Queen_Rules_Attestation.json) → “Kediss secondary damage”
- Source (re-verified): [`Garza_Zol_Plague_Queen_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/garza_zol_plague_queen_2026-10-14/Garza_Zol_Plague_Queen_Rules_Attestation.json) → “Grafted Exoskeleton infect multipliers”

### garza-09: Sword of Feast and Famine or Reaver Cleaver + Aggravated Assault

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Garza Zol, Plague Queen, Sword of Feast and Famine, The Reaver Cleaver, Aggravated Assault

**Ruling.** Each connecting hit with Sword of Feast and Famine untaps your lands; in the postcombat main phase pay {3}{R}{R} for Aggravated Assault (untap creatures, another combat and main phase), and repeat. Reaver Cleaver works the same way: power 5+ means at least six Treasures per hit. Aggravated Assault is sorcery speed, so activate it in the postcombat main phase. Garza has flying and haste, which helps her connect.

**Citations**

- Oracle, *Aggravated Assault*: “{3}{R}{R}: Untap all creatures you control. After this main phase, there is an additional combat phase followed by an additional main phase. Activate only as a sorcery.”
- Scryfall ruling, *Aggravated Assault*: “You will normally activate this ability during your postcombat main phase so you can untap any creatures that attacked.”
- [CR 500.8](#cr-5008), [CR 602.5d](#cr-6025d)
- Commander Spellbook [900-3750](https://commanderspellbook.com/combo/900-3750/) (community-maintained, retrieved 2026-10-16): “Sword of Feast and Famine triggers, causing that opponent to discard a card, and you to untap all lands you control.”
- Commander Spellbook [3750-5039](https://commanderspellbook.com/combo/3750-5039/) (community-maintained, retrieved 2026-10-16): “The creature triggers, creating at least six Treasure tokens.”
- Source (re-verified): [`Garza_Zol_Plague_Queen_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/garza_zol_plague_queen_2026-10-14/Garza_Zol_Plague_Queen_Rules_Attestation.json) → “Sword of Feast and Famine plus Aggravated Assault”

## Engines and payoffs

### garza-02: Basilisk Collar + Thornbite Staff: a repeatable deathtouch ping

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Garza Zol, Plague Queen, Basilisk Collar, Thornbite Staff

**Ruling.** Thornbite Staff gives Garza '{2}, {T}: 1 damage to any target' and untaps her whenever any creature dies. With Basilisk Collar's deathtouch, 1 damage kills any creature that can be damaged. Each kill untaps Garza and gives her a counter, and Collar's lifelink gains 1. Each ping still costs {2}, so it repeats as long as you have mana and targets.

**Citations**

- Oracle, *Thornbite Staff*: “Equipped creature has "{2}, {T}: This creature deals 1 damage to any target" and "Whenever a creature dies, untap this creature."”
- [CR 702.2b](#cr-7022b), [CR 704.5h](#cr-7045h), [CR 702.15b](#cr-70215b)
- Source (re-verified): [`Garza_Zol_Plague_Queen_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/garza_zol_plague_queen_2026-10-14/Garza_Zol_Plague_Queen_Rules_Attestation.json) → “Basilisk Collar plus Thornbite Staff”

### garza-03: Chandra's Ignition and Nova Flame: Garza is the source

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Garza Zol, Plague Queen, Chandra's Ignition, Nova Flame, Basilisk Collar, Blade of the Bloodchief, Curiosity

**Ruling.** Both spells make the targeted creature deal the damage, so Garza is the source. With deathtouch she kills every other creature that can be damaged. Each death gives a Garza counter, and Blade of the Bloodchief adds two more per death because she's a Vampire. Ignition also hits each opponent, so Curiosity draws once per opponent. If Garza is an illegal target on resolution, Ignition does nothing.

**Citations**

- Oracle, *Chandra's Ignition*: “Target creature you control deals damage equal to its power to each other creature and each opponent.”
- Oracle, *Blade of the Bloodchief*: “If equipped creature is a Vampire, put two +1/+1 counters on it instead.”
- Scryfall ruling, *Chandra's Ignition*: “The creature is the source of the damage, not Chandra's Ignition. For example, Chandra's Ignition can have a white creature deal damage to a creature with protection from red.”
- [CR 120.1](#cr-1201), [CR 702.2b](#cr-7022b), [CR 608.2b](#cr-6082b)
- Source (re-verified): [`Garza_Zol_Plague_Queen_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/garza_zol_plague_queen_2026-10-14/Garza_Zol_Plague_Queen_Rules_Attestation.json) → “Deathtouch with Chandra's Ignition and Nova Flame”
- Source (re-verified): [`Garza_Zol_Plague_Queen_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/garza_zol_plague_queen_2026-10-14/Garza_Zol_Plague_Queen_Rules_Attestation.json) → “Blade of the Bloodchief counter stacking”

### garza-04: Scythe of the Wretched steals everything Garza damaged

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Garza Zol, Plague Queen, Scythe of the Wretched

**Ruling.** Scythe triggers for each creature equipped Garza damaged this turn that dies, even if something else killed it. It only has to be attached when the creature dies, not when the damage was dealt. Each trigger returns that card under your control and moves Scythe onto it. After an Ignition wipe, Scythe ends up on the last creature returned, so re-equip Garza for {4}.

**Citations**

- Oracle, *Scythe of the Wretched*: “Whenever a creature dealt damage by equipped creature this turn dies, return that card to the battlefield under your control. Attach this Equipment to that creature.”
- Scryfall ruling, *Scythe of the Wretched*: “The Scythe's ability triggers even if something other than the damage dealt by the equipped creature causes the creature to be put into a graveyard that turn.”
- Scryfall ruling, *Scythe of the Wretched*: “Scythe of the Wretched needs to equip your creature when the other creature goes to the graveyard for the ability to trigger, but it doesn't matter whether the Scythe equipped your creature when the damage was actually dealt.”
- [CR 603.2](#cr-6032), [CR 701.3a](#cr-7013a)
- Source (re-verified): [`Garza_Zol_Plague_Queen_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/garza_zol_plague_queen_2026-10-14/Garza_Zol_Plague_Queen_Rules_Attestation.json) → “Scythe of the Wretched with Garza-sourced mass damage”

### garza-10: Robe of the Archmagi and Curiosity draws

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Garza Zol, Plague Queen, Robe of the Archmagi, Curiosity, Kediss, Emberclaw Familiar

**Ruling.** Robe draws cards equal to Garza's combat damage to a player, and Garza's own trigger may draw one more (six cards from a base 5-power hit). Curiosity triggers on any damage to an opponent, so it also draws for Kediss's damage and Chandra's Ignition, once per opponent.

**Citations**

- Oracle, *Robe of the Archmagi*: “Whenever equipped creature deals combat damage to a player, you draw that many cards.”
- Oracle, *Garza Zol, Plague Queen*: “Whenever Garza Zol deals combat damage to a player, you may draw a card.”
- Oracle, *Curiosity*: “Whenever enchanted creature deals damage to an opponent, you may draw a card.”
- [CR 120.1](#cr-1201), [CR 603.2](#cr-6032)
- Source (re-verified): [`Garza_Zol_Plague_Queen_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/garza_zol_plague_queen_2026-10-14/Garza_Zol_Plague_Queen_Rules_Attestation.json) → “Robe of the Archmagi plus Garza combat trigger”
- Source (re-verified): [`Garza_Zol_Plague_Queen_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/garza_zol_plague_queen_2026-10-14/Garza_Zol_Plague_Queen_Rules_Attestation.json) → “Curiosity retained over redundant combat-only draw”

## Replacement and prevention effects

### garza-07: Damage multipliers for commander damage and poison

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Garza Zol, Plague Queen, Hatred, Jeska, Thrice Reborn, Inquisitor's Flail, Psychotic Fury

**Ruling.** Commander damage is lethal at 21 from one commander. Hatred: pay 16 life for +16/+0 on a 5-power Garza = 21. The life is paid as a cost, so it's lost if Hatred is countered. Jeska's 0 triples Garza's combat damage to an opponent: 7 power (with Exoskeleton) = 21 damage or 21 poison. Two Jeska activations multiply by nine. Inquisitor's Flail doubles it. Psychotic Fury gives the multicolored Garza double strike, two hits.

**Citations**

- Oracle, *Jeska, Thrice Reborn*: “Until your next turn, if that creature would deal combat damage to one of your opponents, it deals triple that damage to that player instead.”
- Scryfall ruling, *Hatred*: “The life payment is part of the cost to cast Hatred, so it is lost if this spell is countered.”
- Scryfall ruling, *Inquisitor's Flail*: “If a creature is equipped with a second Inquisitor’s Flail, combat damage dealt by and dealt to that creature will be multiplied by four.”
- [CR 903.10a](#cr-90310a), [CR 614.1a](#cr-6141a), [CR 702.4b](#cr-7024b)
- Source (re-verified): [`Garza_Zol_Plague_Queen_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/garza_zol_plague_queen_2026-10-14/Garza_Zol_Plague_Queen_Rules_Attestation.json) → “Hatred commander-damage threshold”
- Source (re-verified): [`Garza_Zol_Plague_Queen_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/garza_zol_plague_queen_2026-10-14/Garza_Zol_Plague_Queen_Rules_Attestation.json) → “Jeska commander-damage threshold”
- Source (re-verified): [`Garza_Zol_Plague_Queen_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/garza_zol_plague_queen_2026-10-14/Garza_Zol_Plague_Queen_Rules_Attestation.json) → “Grafted Exoskeleton infect multipliers”

## Zones, commander tax and the command zone

### garza-11: The Ozolith keeps Garza's counters

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Garza Zol, Plague Queen, The Ozolith

**Ruling.** When Garza leaves with counters, wherever she goes (the command zone included), The Ozolith gets the same counters, using her last-known information. At your beginning of combat you may move all of them (not some) to a target creature, such as the recast Garza. If that target is illegal, the counters stay.

**Citations**

- Oracle, *The Ozolith*: “Whenever a creature you control leaves the battlefield, if it had counters on it, put those counters on The Ozolith.”
- Scryfall ruling, *The Ozolith*: “You can't move only some of the counters from The Ozolith onto the target creature.”
- [CR 603.10a](#cr-60310a), [CR 903.9a](#cr-9039a)
- Source (re-verified): [`Garza_Zol_Plague_Queen_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/garza_zol_plague_queen_2026-10-14/Garza_Zol_Plague_Queen_Rules_Attestation.json) → “The Ozolith and commander zone changes”

## What the list depends on

### garza-06: Grafted Exoskeleton: unattaching it sacrifices Garza

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Garza Zol, Plague Queen, Grafted Exoskeleton, Slip Out the Back

**Ruling.** If Exoskeleton becomes unattached for any reason (moved by its own equip, removed, or Garza stops being a creature), you sacrifice Garza. Re-equipping it to another creature sacrifices Garza. Phasing out with Slip Out the Back is safe: attached Equipment phases out with her and stays attached.

**Citations**

- Oracle, *Grafted Exoskeleton*: “Whenever this Equipment becomes unattached from a permanent, sacrifice that permanent.”
- Oracle, *Slip Out the Back*: “Put a +1/+1 counter on target creature. It phases out.”
- [CR 702.26g](#cr-70226g), [CR 701.3a](#cr-7013a)
- Source (re-verified): [`Garza_Zol_Plague_Queen_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/garza_zol_plague_queen_2026-10-14/Garza_Zol_Plague_Queen_Rules_Attestation.json) → “Slip Out the Back and attached permanents”

### garza-08: Jeska needs Garza cast from the command zone first

**Status:** 🚩 list flag · **Evidence:** fact · **Cards:** Garza Zol, Plague Queen, Jeska, Thrice Reborn, Command Beacon

**Ruling.** Jeska enters with one loyalty counter for each time you've cast a commander from the command zone this game. If you've never cast Garza from the command zone, she enters with 0 loyalty and goes to the graveyard as a state-based action before you can use her 0. Casting Garza from hand after Command Beacon doesn't count. Command Beacon avoids commander tax because that cast isn't from the command zone.

**List flag (dependency-risk).** Edge case, not a list error: Jeska is a planeswalker in the 99 here, not a partner commander, so her loyalty depends on how many times Garza was cast from the command zone. Cast Garza normally at least once before deploying Jeska.

**Citations**

- Oracle, *Jeska, Thrice Reborn*: “Jeska enters with a loyalty counter on her for each time you've cast a commander from the command zone this game.”
- Oracle, *Command Beacon*: “{T}, Sacrifice this land: Put your commander into your hand from the command zone.”
- [CR 704.5i](#cr-7045i), [CR 903.8](#cr-9038)
- Source (re-verified): [`Garza_Zol_Plague_Queen_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/garza_zol_plague_queen_2026-10-14/Garza_Zol_Plague_Queen_Rules_Attestation.json) → “Command Beacon commander-tax mitigation”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 120.1

Objects can deal damage to battles, creatures, planeswalkers, and players. This is generally detrimental to the object or player that receives that damage. An object that deals damage is the source of that damage.

#### CR 500.8

Some effects can add phases to a turn. They do this by adding the phases directly after the specified phase. If multiple extra phases are created after the same phase, the most recently created phase will occur first.

#### CR 602.5d

Activated abilities that read “Activate only as a sorcery” mean the player must follow the timing rules for casting a sorcery spell, though the ability isn’t actually a sorcery. The player doesn’t actually need to have a sorcery card that they could cast.

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 603.10a

Some zone-change triggers look back in time. These are leaves-the-battlefield abilities, abilities that trigger when a player sacrifices a permanent, abilities that trigger when a card leaves a graveyard, and abilities that trigger when an object that all players can see is put into a hand or library.

#### CR 608.2b

If the spell or ability specifies targets, it checks whether the targets are still legal. A target that’s no longer in the zone it was in when it was targeted is illegal. Other changes to the game state may cause a target to no longer be legal; for example, its characteristics may have changed or an effect may have changed the text of the spell. If the source of an ability has left the zone it was in, its last known information is used during this process. If all its targets, for every instance of the word “target,” are now illegal, the spell or ability doesn’t resolve. It’s removed from the …

#### CR 614.1a

Effects that use the word “instead” are replacement effects. Most replacement effects use the word “instead” to indicate what events will be replaced with other events.

#### CR 700.4

The term dies means “is put into a graveyard from the battlefield.”

#### CR 701.3a

To attach an Aura, Equipment, or Fortification to an object or player means to take it from where it currently is and put it onto that object or player. If something is attached to a permanent on the battlefield, it’s customary to place it so that it’s physically touching the permanent. An Aura, Equipment, or Fortification can’t be attached to an object or player it couldn’t enchant, equip, or fortify, respectively.

#### CR 702.2b

A creature with toughness greater than 0 that’s been dealt damage by a source with deathtouch since the last time state-based actions were checked is destroyed as a state-based action. See rule 704.

#### CR 702.4b

If at least one attacking or blocking creature has first strike (see rule 702.7) or double strike as the combat damage step begins, the only creatures that assign combat damage in that step are those with first strike or double strike. After that step, instead of proceeding to the end of combat step, the phase gets a second combat damage step. The only creatures that assign combat damage in that step are the remaining attackers and blockers that had neither first strike nor double strike as the first combat damage step began, as well as the remaining attackers and blockers that currently have …

#### CR 702.15b

Damage dealt by a source with lifelink causes that source’s controller, or its owner if it has no controller, to gain that much life (in addition to any other results that damage causes). See rule 120.3.

#### CR 702.26g

When a permanent phases out, any Auras, Equipment, or Fortifications attached to that permanent phase out at the same time. This alternate way of phasing out is known as phasing out “indirectly.” An Aura, Equipment, or Fortification that phased out indirectly won’t phase in by itself, but instead phases in along with the permanent it’s attached to.

#### CR 702.90b

Damage dealt to a player by a source with infect doesn’t cause that player to lose life. Rather, it causes that source’s controller to give the player that many poison counters. See rule 120.3.

#### CR 704.5c

If a player has ten or more poison counters, that player loses the game. Ignore this rule in Two-Headed Giant games; see rule 704.6b instead.

#### CR 704.5h

If a creature has toughness greater than 0, and it’s been dealt damage by a source with deathtouch since the last time state-based actions were checked, that creature is destroyed. Regeneration can replace this event.

#### CR 704.5i

If a planeswalker has loyalty 0, it’s put into its owner’s graveyard.

#### CR 903.8

A player may cast a commander they own from the command zone. A commander cast from the command zone costs an additional {2} for each previous time the player casting it has cast it from the command zone that game. This additional cost is informally known as the “commander tax.”

#### CR 903.9a

If a commander is in a graveyard or in exile and that object was put into that zone since the last time state-based actions were checked, its owner may put it into the command zone. This is a state-based action. See rule 704.

#### CR 903.10a

A player who’s been dealt 21 or more combat damage by the same commander over the course of the game loses the game. (This is a state-based action. See rule 704.)

