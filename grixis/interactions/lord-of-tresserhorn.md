---
title: "Lord of Tresserhorn — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Lord of Tresserhorn — Interaction Review

> Bot cycle 49 · batch C · reviewed 2026-10-16. Deck: [Lord of Tresserhorn](../decks/lord-of-tresserhorn.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/lord-of-tresserhorn.txt`](../../exports/grixis-archidekt/lord-of-tresserhorn.txt) · SHA-256 `ce42932da71b7ae64899536b586fe031cd51f6a639074fd94590d1d66a79379b` |
| Rulings | **13** (12 verified · 0 uncertain · 1 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`Lord_of_Tresserhorn_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_of_tresserhorn_2026-10-14/Lord_of_Tresserhorn_Rules_Attestation.json) (21 interactions, all PASS) |

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
- [What the list depends on](#what-the-list-depends-on)
- [Rules cited](#rules-cited)

## Summary

Lord of Tresserhorn is a 10/4 for four with a harsh enter trigger. The deck suppresses or counters that trigger, then kills with infect (Phyresis, Tainted Strike, Kediss spreading poison to the table), 22 double-strike commander damage, or Gravecrawler and Skeleton loops. This review re-verifies all 21 attestation items. Nineteen Spellbook lines are confirmed.

One flag: Lightning Greaves' shroud blocks the deck's own Lord-targeting kill spells. Rules surprises: Lord himself is the Zombie that enables Gravecrawler; Kediss works from the 99; Pain for All triggers even on lethal damage.

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [tresserhorn-08](#tresserhorn-08-lightning-greaves-shroud-blocks-your-own-lord-spells-brotherhood-regalia-doesnt) | 🚩 list flag (anti-synergy) | Lightning Greaves' shroud blocks your own Lord spells; Brotherhood Regalia doesn't | Pilot note, not a list error: Lightning Greaves' shroud blocks the deck's own Lord-targeting kill spells (Tainted Strike, Uncaged Fury, Chandra's Ignition, Pain for All, Slip Out the Back). Re-equip Greaves to another creature before the kill turn; Boots and Regalia don't conflict. |

## Commander rules text and edge cases

### tresserhorn-01: The enter trigger: life loss, two sacrifices (possibly Lord), opponent draws

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Lord of Tresserhorn

**Ruling.** On resolution you lose 2 life (it's loss, not a payment, so it can take you below 0), sacrifice two creatures, and the target opponent draws two. With zero or one other creature, Lord himself is one of the two. Regeneration can't save him from a sacrifice. The rest still happens.

**Citations**

- Oracle, *Lord of Tresserhorn*: “When Lord of Tresserhorn enters, you lose 2 life, you sacrifice two creatures, and target opponent draws two cards.”
- Scryfall ruling, *Lord of Tresserhorn*: “When Lord of Tresserhorn enters, if you have zero or one other creature on the battlefield, Lord of Tresserhorn itself will be sacrificed as part of its ability's effect. Regeneration won't save it. The rest of the effect still happens.”
- Scryfall ruling, *Lord of Tresserhorn*: “Since this is a loss of life and not a payment, your life total can be reduced below zero by this.”
- [CR 701.21a](#cr-70121a), [CR 701.19a](#cr-70119a), [CR 119.3](#cr-1193)
- Source (re-verified): [`Lord_of_Tresserhorn_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_of_tresserhorn_2026-10-14/Lord_of_Tresserhorn_Rules_Attestation.json) → “Lord of Tresserhorn enters trigger and sacrifice requirement”

## Combos and engine lines

### tresserhorn-05: Infect Lord: Tainted Strike or Phyresis, then Kediss

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Lord of Tresserhorn, Tainted Strike, Phyresis, Kediss, Emberclaw Familiar

**Ruling.** Lord is 10/4. Phyresis gives infect: ten poison from one hit. Tainted Strike makes him 11 power with infect. Kediss (in the 99, not a partner commander here) triggers when any commander you control deals combat damage to an opponent. Lord then deals that much to each other opponent, and with infect still on, that's poison too: a table kill. Kediss's damage isn't combat damage, so it doesn't count toward commander damage or retrigger Kediss.

**Citations**

- Oracle, *Kediss, Emberclaw Familiar*: “Whenever a commander you control deals combat damage to an opponent, it deals that much damage to each other opponent.”
- Scryfall ruling, *Kediss, Emberclaw Familiar*: “The damage the commander deals as a result of Kediss's triggered ability isn't combat damage. It isn't tracked with combat damage dealt by commanders and won't cause Kediss's ability to trigger again.”
- Scryfall ruling, *Kediss, Emberclaw Familiar*: “Kediss's triggered ability will trigger if any commander you control deals combat damage to an opponent, not just your commander.”
- [CR 702.90b](#cr-70290b), [CR 704.5c](#cr-7045c)
- Commander Spellbook [264-1218](https://commanderspellbook.com/combo/264-1218/) (community-maintained, retrieved 2026-10-16): “Deal combat damage with Lord of Tresserhorn, causing target opponent to get eleven poison counters.”
- Commander Spellbook [2822-4651](https://commanderspellbook.com/combo/2822-4651/) (community-maintained, retrieved 2026-10-16): “Kediss triggers, causing your commander to give each other opponent at least ten poison counters due to its infect.”
- Source (re-verified): [`Lord_of_Tresserhorn_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_of_tresserhorn_2026-10-14/Lord_of_Tresserhorn_Rules_Attestation.json) → “Tainted Strike and Phyresis infect conversion”
- Source (re-verified): [`Lord_of_Tresserhorn_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_of_tresserhorn_2026-10-14/Lord_of_Tresserhorn_Rules_Attestation.json) → “Kediss infect spread”

### tresserhorn-06: Noncombat infect: Chandra's Ignition and Pain for All

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Lord of Tresserhorn, Chandra's Ignition, Pain for All, Phyresis, Tainted Strike, Blasphemous Act

**Ruling.** Chandra's Ignition on an infect Lord deals 10 (11 with Tainted Strike) infect damage to each opponent, so poison everywhere with no combat. Pain for All's enter trigger hits one target for his power. Its second trigger fires even on lethal damage. With a regeneration shield, Blasphemous Act's 13 to Lord becomes 13 to each opponent, as poison if he has infect.

**Citations**

- Oracle, *Chandra's Ignition*: “Target creature you control deals damage equal to its power to each other creature and each opponent.”
- Oracle, *Pain for All*: “Whenever enchanted creature is dealt damage, it deals that much damage to each opponent.”
- Scryfall ruling, *Pain for All*: “If lethal damage is dealt to the enchanted creature, Pain for All’s last ability still triggers.”
- [CR 702.90b](#cr-70290b), [CR 120.3](#cr-1203)
- Source (re-verified): [`Lord_of_Tresserhorn_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_of_tresserhorn_2026-10-14/Lord_of_Tresserhorn_Rules_Attestation.json) → “Chandra's Ignition with infect”
- Source (re-verified): [`Lord_of_Tresserhorn_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_of_tresserhorn_2026-10-14/Lord_of_Tresserhorn_Rules_Attestation.json) → “Pain for All immediate and reflected damage”

### tresserhorn-07: Uncaged Fury: 22 commander damage

**Status:** ✅ verified · **Evidence:** derived_metric · **Cards:** Lord of Tresserhorn, Uncaged Fury

**Ruling.** Uncaged Fury makes Lord 11/5 with double strike. If both damage steps hit the same opponent, that's 22 combat damage from a commander, past the 21 threshold.

**Citations**

- Oracle, *Uncaged Fury*: “Target creature gets +1/+1 and gains double strike until end of turn.”
- [CR 702.4b](#cr-7024b), [CR 903.10a](#cr-90310a)
- Source (re-verified): [`Lord_of_Tresserhorn_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_of_tresserhorn_2026-10-14/Lord_of_Tresserhorn_Rules_Attestation.json) → “Uncaged Fury commander-damage kill”

### tresserhorn-11: Gravecrawler loops (Lord himself is the other Zombie)

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Lord of Tresserhorn, Gravecrawler, Rooftop Storm, Phyrexian Altar, Ashnod's Altar, Pitiless Plunderer, Viscera Seer, Carrion Feeder, Goblin Bombardment, Warren Soultrader, Blood Artist, Zulaport Cutthroat

**Ruling.** Gravecrawler can be cast from the graveyard while you control a Zombie, and Lord of Tresserhorn is one. Loops:
- Rooftop Storm makes it free with any sacrifice outlet (Bombardment kills directly).
- Pitiless Plunderer's Treasure pays the {B} when sacrificing to Phyrexian Altar, Ashnod's Altar, Viscera Seer or Carrion Feeder.
- Warren Soultrader (1 life) plus Blood Artist or Zulaport (gain 1) is life-neutral and drains.
Plunderer triggers on any other creature you control dying, tokens included.

**Citations**

- Oracle, *Gravecrawler*: “You may cast this card from your graveyard as long as you control a Zombie.”
- Oracle, *Pitiless Plunderer*: “Whenever another creature you control dies, create a Treasure token.”
- Scryfall ruling, *Gravecrawler*: “Once you've cast Gravecrawler and it's on the stack, it doesn't matter if you lose control of the other Zombie.”
- [CR 601.3](#cr-6013), [CR 118.9](#cr-1189)
- Commander Spellbook [2452-2577-5147](https://commanderspellbook.com/combo/2452-2577-5147/) (community-maintained, retrieved 2026-10-16): “Cast Gravecrawler from your graveyard by paying {0}.”
- Commander Spellbook [2577-4871-5147](https://commanderspellbook.com/combo/2577-4871-5147/) (community-maintained, retrieved 2026-10-16): “When Gravecrawler dies, Pitiless Plunderer triggers, creating a Treasure token.”
- Commander Spellbook [2577-2842-5670](https://commanderspellbook.com/combo/2577-2842-5670/) (community-maintained, retrieved 2026-10-16): “Activate Warren Soultrader by paying 1 life and sacrificing Gravecrawler.”
- Commander Spellbook [2577-4050](https://commanderspellbook.com/combo/2577-4050/) (community-maintained, retrieved 2026-10-16): “You control an additional Zombie.”
- Source (re-verified): [`Lord_of_Tresserhorn_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_of_tresserhorn_2026-10-14/Lord_of_Tresserhorn_Rules_Attestation.json) → “Rooftop Storm plus Gravecrawler”
- Source (re-verified): [`Lord_of_Tresserhorn_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_of_tresserhorn_2026-10-14/Lord_of_Tresserhorn_Rules_Attestation.json) → “Phyrexian Altar plus Pitiless Plunderer plus Gravecrawler”
- Source (re-verified): [`Lord_of_Tresserhorn_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_of_tresserhorn_2026-10-14/Lord_of_Tresserhorn_Rules_Attestation.json) → “Warren Soultrader plus Gravecrawler drain loop”

### tresserhorn-12: Reassembling Skeleton loops without a Zombie

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Lord of Tresserhorn, Reassembling Skeleton, Pitiless Plunderer, Ashnod's Altar, Phyrexian Altar, Warren Soultrader, Zulaport Cutthroat, Blood Artist

**Ruling.** Reassembling Skeleton returns for {1}{B}. Ashnod's Altar ({C}{C}) or Phyrexian Altar ({1}) plus Plunderer's Treasure pays for it, for unbounded death triggers and mana. With Soultrader, two Treasures per loop (Soultrader + Plunderer) do the same, and Zulaport or Blood Artist drains.

**Citations**

- [CR 603.10a](#cr-60310a)
- Commander Spellbook [1580-2034-4871](https://commanderspellbook.com/combo/1580-2034-4871/) (community-maintained, retrieved 2026-10-16): “Activate Reassembling Skeleton by paying {1}{B}, returning it from your graveyard to the battlefield tapped.”
- Commander Spellbook [1385-1580-4871-5670](https://commanderspellbook.com/combo/1385-1580-4871-5670/) (community-maintained, retrieved 2026-10-16): “Activate Warren Soultrader by paying 1 life and sacrificing Reassembling Skeleton.”

## Key card-pair interactions

### tresserhorn-08: Lightning Greaves' shroud blocks your own Lord spells; Brotherhood Regalia doesn't

**Status:** 🚩 list flag · **Evidence:** fact · **Cards:** Lord of Tresserhorn, Lightning Greaves, Swiftfoot Boots, Brotherhood Regalia, Tainted Strike, Chandra's Ignition, Pain for All, Slip Out the Back, Uncaged Fury

**Ruling.** Brotherhood Regalia gives ward {2} (opponents only) and unblockable, and equips a legendary creature for {1}, so you can still target Lord. Lightning Greaves gives shroud, which stops your own Tainted Strike, Uncaged Fury, Chandra's Ignition, Pain for All and Slip Out the Back. Move Greaves first. Swiftfoot Boots' hexproof doesn't have this problem.

**List flag (anti-synergy).** Pilot note, not a list error: Lightning Greaves' shroud blocks the deck's own Lord-targeting kill spells (Tainted Strike, Uncaged Fury, Chandra's Ignition, Pain for All, Slip Out the Back). Re-equip Greaves to another creature before the kill turn; Boots and Regalia don't conflict.

**Citations**

- Oracle, *Brotherhood Regalia*: “Equipped creature has ward {2}, is an Assassin in addition to its other types, and can't be blocked.”
- [CR 702.18a](#cr-70218a), [CR 702.11b](#cr-70211b), [CR 702.21a](#cr-70221a)
- Source (re-verified): [`Lord_of_Tresserhorn_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_of_tresserhorn_2026-10-14/Lord_of_Tresserhorn_Rules_Attestation.json) → “Brotherhood Regalia versus Whispersilk Cloak”

## Timing and priority

### tresserhorn-04: Haste: sacrifice Anger to Lord's own trigger, or use Arena of Glory

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Lord of Tresserhorn, Anger, Arena of Glory

**Ruling.** Sacrifice Anger as one of the two creatures. With a Mountain-typed land, Anger in the graveyard gives Lord haste right away. Exerted Arena of Glory mana spent on Lord also gives haste.

**Citations**

- Oracle, *Anger*: “As long as this card is in your graveyard and you control a Mountain, creatures you control have haste.”
- [CR 702.10a](#cr-70210a), [CR 205.3i](#cr-2053i)
- Source (re-verified): [`Lord_of_Tresserhorn_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_of_tresserhorn_2026-10-14/Lord_of_Tresserhorn_Rules_Attestation.json) → “Anger plus Lord's own sacrifice trigger”
- Source (re-verified): [`Lord_of_Tresserhorn_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_of_tresserhorn_2026-10-14/Lord_of_Tresserhorn_Rules_Attestation.json) → “Arena of Glory haste”

### tresserhorn-09: Not of This World and Slip Out the Back protect Lord

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Lord of Tresserhorn, Not of This World, Slip Out the Back

**Ruling.** Not of This World costs {7} less when it counters a spell or ability that targets Lord with power 7 or more. That's normally free, and it can target abilities, not just spells. Slip Out the Back puts a +1/+1 counter on Lord and phases him out with his Auras and Equipment. Phasing isn't leaving the battlefield, so there are no leave or enter triggers and he keeps the counter. He's removed from combat if attacking.

**Citations**

- Oracle, *Not of This World*: “This spell costs {7} less to cast if it targets a spell or ability that targets a creature you control with power 7 or greater.”
- Scryfall ruling, *Slip Out the Back*: “As a creature is phased out, Auras and Equipment attached to it also phase out at the same time. Those Auras and Equipment will phase in at the same time that creature does, and they'll phase in still attached to that creature.”
- Scryfall ruling, *Slip Out the Back*: “An attacking or blocking creature that phases out is removed from combat.”
- [CR 702.26b](#cr-70226b), [CR 702.26d](#cr-70226d), [CR 601.2f](#cr-6012f)
- Source (re-verified): [`Lord_of_Tresserhorn_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_of_tresserhorn_2026-10-14/Lord_of_Tresserhorn_Rules_Attestation.json) → “Not of This World cost reduction”
- Source (re-verified): [`Lord_of_Tresserhorn_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_of_tresserhorn_2026-10-14/Lord_of_Tresserhorn_Rules_Attestation.json) → “Slip Out the Back protection and counter retention”

## Replacement and prevention effects

### tresserhorn-03: Regeneration only replaces destruction

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Lord of Tresserhorn, Toxic Deluge, Blasphemous Act

**Ruling.** {B} gives a regeneration shield that replaces Lord's next destruction this turn: lethal damage (Blasphemous Act) or 'destroy'. It doesn't help against sacrifice, toughness 0 or less, or -X/-X like Toxic Deluge.

**Citations**

- Oracle, *Lord of Tresserhorn*: “{B}: Regenerate Lord of Tresserhorn.”
- [CR 701.19a](#cr-70119a), [CR 704.5f](#cr-7045f), [CR 704.5g](#cr-7045g)
- Source (re-verified): [`Lord_of_Tresserhorn_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_of_tresserhorn_2026-10-14/Lord_of_Tresserhorn_Rules_Attestation.json) → “Regeneration limitations”

## Trigger ordering

### tresserhorn-02: Turning off the drawback: Torpor Orb, Karn, Dress Down, Stifle, Tale's End

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Lord of Tresserhorn, Torpor Orb, Karn, Argent Defender, Dress Down, Stifle, Tale's End

**Ruling.** Torpor Orb or Karn, Argent Defender already in play means Lord's entry never triggers. If Karn enters at the same time as Lord, Lord's trigger is still suppressed. Dress Down only works if it's out before Lord enters; it can't remove a trigger already on the stack. While it's out, Lord also loses regeneration and any abilities granted before Dress Down entered. Abilities granted after it (Tainted Strike's infect, Uncaged Fury's double strike) stay, so plan the kill turn around it. Dress Down is sacrificed at end step. Stifle or Tale's End counters the trigger itself.

**Citations**

- Oracle, *Karn, Argent Defender*: “Artifacts and creatures entering the battlefield don't cause abilities to trigger.”
- Oracle, *Dress Down*: “Creatures lose all abilities.”
- Scryfall ruling, *Karn, Argent Defender*: “If Karn, Argent Defender and another artifact or creature enter the battlefield at the same time, neither one will cause triggered abilities to trigger when they enter the battlefield.”
- Scryfall ruling, *Dress Down*: “If an effect grants a creature an ability after Dress Down has entered the battlefield, it won't lose that ability.”
- [CR 603.2](#cr-6032), [CR 613.1f](#cr-6131f), [CR 701.6a](#cr-7016a)
- Source (re-verified): [`Lord_of_Tresserhorn_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_of_tresserhorn_2026-10-14/Lord_of_Tresserhorn_Rules_Attestation.json) → “Torpor Orb and Karn, Argent Defender suppress Lord”
- Source (re-verified): [`Lord_of_Tresserhorn_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_of_tresserhorn_2026-10-14/Lord_of_Tresserhorn_Rules_Attestation.json) → “Dress Down suppresses Lord only when sequenced before entry”
- Source (re-verified): [`Lord_of_Tresserhorn_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_of_tresserhorn_2026-10-14/Lord_of_Tresserhorn_Rules_Attestation.json) → “Stifle and Tale's End counter Lord's triggered ability”

## Zones, commander tax and the command zone

### tresserhorn-10: Rooftop Storm makes Lord cost {0} plus tax

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Lord of Tresserhorn, Rooftop Storm

**Ruling.** Lord is a Zombie, so Rooftop Storm's {0} alternative cost applies. Commander tax is an additional cost and is still paid on top. Mana value doesn't change.

**Citations**

- Scryfall ruling, *Rooftop Storm*: “The mana cost and mana value of the spell are unchanged. Rooftop Storm only changes what you pay.”
- [CR 118.9d](#cr-1189d), [CR 903.8](#cr-9038)
- Source (re-verified): [`Lord_of_Tresserhorn_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_of_tresserhorn_2026-10-14/Lord_of_Tresserhorn_Rules_Attestation.json) → “Rooftop Storm and commander tax”

## What the list depends on

### tresserhorn-13: Torpor Orb and Karn: what the list gave up

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Lord of Tresserhorn, Torpor Orb, Karn, Argent Defender, Muddle the Mixture

**Ruling.** Torpor Orb and Karn shut off creature enter triggers for everyone, including yours. The source cut its own enter-trigger creatures for that reason (Fleshbag Marauder, Plaguecrafter and others). The remaining engines run on death, token, upkeep and graveyard triggers. Treasures and other artifacts entering under Karn don't trigger anything either. Muddle the Mixture (mana value 2) transmutes for Torpor Orb, Phyresis, Brotherhood Regalia and the other two-drops.

**Citations**

- Scryfall ruling, *Karn, Argent Defender*: “Replacement effects, such as a permanent entering the battlefield tapped or with counters on it, are unaffected. Abilities that apply "as [this permanent] enters" are replacement effects.”
- [CR 603.6a](#cr-6036a), [CR 702.53a](#cr-70253a)
- Source (re-verified): [`Lord_of_Tresserhorn_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_of_tresserhorn_2026-10-14/Lord_of_Tresserhorn_Rules_Attestation.json) → “Torpor/Karn internal nonbo challenge”
- Source (re-verified): [`Lord_of_Tresserhorn_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_of_tresserhorn_2026-10-14/Lord_of_Tresserhorn_Rules_Attestation.json) → “Muddle the Mixture transmute”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 118.9

Some spells have alternative costs. An alternative cost is a cost listed in a spell’s text, or applied to it from another effect, that its controller may pay rather than paying the spell’s mana cost. Alternative costs are usually phrased, “You may [action] rather than pay [this object’s] mana cost,” or “You may cast [this object] without paying its mana cost.” Note that some alternative costs are listed in keywords; see rule 702.

#### CR 118.9d

If an alternative cost is being paid to cast a spell, any additional costs, cost increases, and cost reductions that affect that spell are applied to that alternative cost. (See rule 601.2f.)

#### CR 119.3

If an effect causes a player to gain life or lose life, that player’s life total is adjusted accordingly.

#### CR 120.3

Damage may have one or more of the following results, depending on whether the recipient of the damage is a player or permanent, the characteristics of the damage’s source, and the characteristics of the damage’s recipient (if it’s a permanent).

#### CR 205.3i

Lands have their own unique set of subtypes; these subtypes are called land types. The land types are Cave, Desert, Forest, Gate, Island, Lair, Locus, Mine, Mountain, Plains, Planet, Power-Plant, Sphere, Swamp, Tower, Town, and Urza’s. Of that list, Forest, Island, Mountain, Plains, and Swamp are the basic land types. See rule 305.6.

#### CR 601.2f

The player determines the total cost of the spell. Usually this is just the mana cost. Some spells have additional or alternative costs. Some effects may increase or reduce the cost to pay, or may provide other alternative costs. Costs may include paying mana, tapping permanents, sacrificing permanents, discarding cards, and so on. The total cost is the mana cost or alternative cost (as determined in rule 601.2b), plus all additional costs and cost increases, and minus all cost reductions. If multiple cost reductions apply, the player may apply them in any order. If the mana component of the …

#### CR 601.3

A player can begin to cast a spell only if a rule or effect allows that player to cast it and no rule or effect prohibits that player from casting it.

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 603.6a

Enters-the-battlefield abilities trigger when a permanent enters the battlefield. These are written, “When [this object] enters, . . . “ or “Whenever a [type] enters, . . .” Each time an event puts one or more permanents onto the battlefield, all permanents on the battlefield (including the newcomers) are checked for any enters-the-battlefield triggers that match the event.

#### CR 603.10a

Some zone-change triggers look back in time. These are leaves-the-battlefield abilities, abilities that trigger when a player sacrifices a permanent, abilities that trigger when a card leaves a graveyard, and abilities that trigger when an object that all players can see is put into a hand or library.

#### CR 613.1f

Layer 6: Ability-adding effects, keyword counters, ability-removing effects, and effects that say an object can’t have an ability are applied.

#### CR 701.6a

To counter a spell or ability means to cancel it, removing it from the stack. It doesn’t resolve and none of its effects occur. A countered spell is put into its owner’s graveyard.

#### CR 701.19a

If the effect of a resolving spell or ability regenerates a permanent, it creates a replacement effect that protects the permanent the next time it would be destroyed this turn. In this case, “Regenerate [permanent]” means “The next time [permanent] would be destroyed this turn, instead remove all damage marked on it and its controller taps it. If it’s an attacking or blocking creature, remove it from combat.”

#### CR 701.21a

To sacrifice a permanent, its controller moves it from the battlefield directly to its owner’s graveyard. A player can’t sacrifice something that isn’t a permanent, or something that’s a permanent they don’t control. Sacrificing a permanent doesn’t destroy it, so regeneration or other effects that replace destruction can’t affect this action.

#### CR 702.4b

If at least one attacking or blocking creature has first strike (see rule 702.7) or double strike as the combat damage step begins, the only creatures that assign combat damage in that step are those with first strike or double strike. After that step, instead of proceeding to the end of combat step, the phase gets a second combat damage step. The only creatures that assign combat damage in that step are the remaining attackers and blockers that had neither first strike nor double strike as the first combat damage step began, as well as the remaining attackers and blockers that currently have …

#### CR 702.10a

Haste is a static ability.

#### CR 702.11b

“Hexproof” on a permanent means “This permanent can’t be the target of spells or abilities your opponents control.”

#### CR 702.18a

Shroud is a static ability. “Shroud” means “This permanent or player can’t be the target of spells or abilities.”

#### CR 702.21a

Ward is a triggered ability. Ward [cost] means “Whenever this permanent becomes the target of a spell or ability an opponent controls, counter that spell or ability unless that player pays [cost].”

#### CR 702.26b

If a permanent phases out, its status changes to “phased out.” Except for rules and effects that specifically mention phased-out permanents, a phased-out permanent is treated as though it does not exist. It can’t affect or be affected by anything else in the game. A permanent that phases out is removed from combat. (See rule 506.4.)

#### CR 702.26d

The phasing event doesn’t actually cause a permanent to change zones or control, even though it’s treated as though it’s not on the battlefield and not under its controller’s control while it’s phased out. Zone-change triggers don’t trigger when a permanent phases in or out. Tokens continue to exist on the battlefield while phased out. Counters and stickers remain on a permanent while it’s phased out. Effects that check a phased-in permanent’s history won’t treat the phasing event as having caused the permanent to leave or enter the battlefield or its controller’s control.

#### CR 702.53a

Transmute is an activated ability that functions only while the card with transmute is in a player’s hand. “Transmute [cost]” means “[Cost], Discard this card: Search your library for a card with the same mana value as the discarded card, reveal that card, and put it into your hand. Then shuffle your library. Activate only as a sorcery.”

#### CR 702.90b

Damage dealt to a player by a source with infect doesn’t cause that player to lose life. Rather, it causes that source’s controller to give the player that many poison counters. See rule 120.3.

#### CR 704.5c

If a player has ten or more poison counters, that player loses the game. Ignore this rule in Two-Headed Giant games; see rule 704.6b instead.

#### CR 704.5f

If a creature has toughness 0 or less, it’s put into its owner’s graveyard. Regeneration can’t replace this event.

#### CR 704.5g

If a creature has toughness greater than 0, it has damage marked on it, and the total damage marked on it is greater than or equal to its toughness, that creature has been dealt lethal damage and is destroyed. Regeneration can replace this event.

#### CR 903.8

A player may cast a commander they own from the command zone. A commander cast from the command zone costs an additional {2} for each previous time the player casting it has cast it from the command zone that game. This additional cost is informally known as the “commander tax.”

#### CR 903.10a

A player who’s been dealt 21 or more combat damage by the same commander over the course of the game loses the game. (This is a state-based action. See rule 704.)

