---
title: "Saruman, the White Hand — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Saruman, the White Hand — Interaction Review

> Bot cycle 54 · batch E · reviewed 2026-10-16. Deck: [Saruman, the White Hand](../decks/saruman-the-white-hand.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/saruman-the-white-hand.txt`](../../exports/grixis-archidekt/saruman-the-white-hand.txt) · SHA-256 `d08e2578f1193c283ea882e9d8565f4c5d00bedb3bc2b625bf3760403a9cfa30` |
| Rulings | **7** (6 verified · 0 uncertain · 1 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`Saruman_the_White_Hand_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/saruman_2026-10-15/gate_output/Saruman_the_White_Hand_Rules_Attestation.json) (Rules attestation (14 items, all PASS) re-verified; Black Gate wording flagged) · [`Saruman_the_White_Hand_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Saruman_the_White_Hand_Approval_Ready_Verification_2026-10-15.md) (Approval-ready verification) |

## Contents
- [Summary](#summary)
- [Flags and open questions](#flags-and-open-questions)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Timing and priority](#timing-and-priority)
- [Replacement and prevention effects](#replacement-and-prevention-effects)
- [Trigger ordering](#trigger-ordering)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [Legality and project exceptions](#legality-and-project-exceptions)
- [Rules cited](#rules-cited)

## Summary

Saruman amasses Orcs equal to the mana value of each noncreature spell. The list favors high-mana-value spells cast cheaply (Volcanic Salvo, Treasure Cruise, Force of Will, Blasphemous Act), X spells, trigger doublers (Prodigy, Staff, Veyran), counter payoffs (Mauhúr, The Great Goblin, All Will Be One), and excess damage (Fall of Cair Andros + Act / Widespread Brutality). All 14 attestation items and the one Spellbook line are re-verified against the canonical list.

Rules surprises: an X spell cast free off Summons has X=0; Blasphemous Act kills your Army, but Fall builds a fresh one; Chandra's Ignition kills your own Saruman; Veyran doubles Saruman only for instants and sorceries. One documentation flag: the source wording on what The Black Gate targets.

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [saruman-07](#saruman-07-the-black-gate-chooses-a-player-only-the-creature-is-targeted-source-wording-off) | 🚩 list flag (documentation) | The Black Gate chooses a player; only the creature is targeted (source wording off) | The source rules attestation (The Black Gate item) says the ability 'targets a creature and a player'. Per Oracle, the player is chosen and only the creature is targeted. Text fix only; the deck isn't affected. |

## Commander rules text and edge cases

### saruman-01: Saruman counts mana value, not mana paid

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Saruman, the White Hand, Volcanic Salvo, Treasure Cruise, Force of Will, Blasphemous Act, Dig Through Time, Blood for the Blood God!

**Ruling.** Saruman's amass uses the spell's mana value. Cost reductions, delve and alternative costs don't change it. Volcanic Salvo cast for {R}{R} still amasses 12, Treasure Cruise and Dig Through Time with delve 8, a pitched Force of Will 5, Blasphemous Act 9 and Blood for the Blood God! 8. Saruman's trigger goes on the stack above the spell, so the Army grows first.

**Citations**

- Oracle, *Saruman, the White Hand*: “Whenever you cast a noncreature spell, amass Orcs X, where X is that spell's mana value. (Put X +1/+1 counters on an Army you control. It's also an Orc. If you don't control an Army, create a 0/0 black Orc Army creature token first.)”
- Scryfall ruling, *Volcanic Salvo*: “To determine the total cost of a spell, start with the mana cost or alternative cost you're paying, add any cost increases, then apply any cost reductions (such as that of Volcanic Salvo). The mana value of the spell remains unchanged, no matter what the total cost to cast it was.”
- Scryfall ruling, *Treasure Cruise*: “Delve doesn't change a spell's mana cost or mana value. For example, Treasure Cruise's mana value is 8 even if you exiled three cards to cast it.”
- Scryfall ruling, *Force of Will*: “To determine the total cost of a spell, start with the mana cost or alternative cost you're paying (such as the alternative cost of Force of Will), add any cost increases, then apply any cost reductions. Force of Will's mana value is always 5, no matter what you paid to cast it.”
- [CR 202.3](#cr-2023), [CR 601.2f](#cr-6012f)
- Source (re-verified): [`Saruman_the_White_Hand_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/saruman_2026-10-15/gate_output/Saruman_the_White_Hand_Rules_Attestation.json) → “Saruman mana-value engine”
- Source (re-verified): [`Saruman_the_White_Hand_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/saruman_2026-10-15/gate_output/Saruman_the_White_Hand_Rules_Attestation.json) → “High-MV discounted spells”

## Combos and engine lines

### saruman-05: Fall of Cair Andros + Blasphemous Act (+ Widespread Brutality, Chandra's Ignition, Soul's Fire)

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Saruman, the White Hand, Fall of Cair Andros, Blasphemous Act, Widespread Brutality, Chandra's Ignition, Soul's Fire

**Ruling.** Each opposing creature that takes excess noncombat damage triggers Fall of Cair Andros separately, amassing that excess.
- **Blasphemous Act:** 13 damage to every creature, including your Army, which is 9/9 after Saruman's trigger and dies. Fall's amass then makes a fresh 0/0 Army once the old one is gone and loads it with all the excess.
- **Widespread Brutality:** the Army deals its power to each non-Army creature, so the Army itself is spared.
- **Chandra's Ignition:** spares the Army but kills your own Saruman (2/5) once the Army has 5+ power.
- **Soul's Fire:** a safer single shot that doesn't sacrifice the Army.

**Citations**

- Oracle, *Fall of Cair Andros*: “Whenever a creature an opponent controls is dealt excess noncombat damage, amass Orcs X, where X is that excess damage. (Put X +1/+1 counters on an Army you control. It's also an Orc. If you don't control an Army, create a 0/0 black Orc Army creature token first.)”
- Oracle, *Widespread Brutality*: “Amass Zombies 2, then the Army you amassed deals damage equal to its power to each non-Army creature. (To amass Zombies 2, put two +1/+1 counters on an Army you control. It's also a Zombie. If you don't control an Army, create a 0/0 black Zombie Army creature token first.)”
- Scryfall ruling, *Fall of Cair Andros*: “Excess damage has been dealt to a creature if the damage dealt to it is greater than lethal damage. Usually, this means damage greater than its toughness, although damage already marked on the creature is taken into account.”
- [CR 120.10](#cr-12010), [CR 701.47a](#cr-70147a)
- Commander Spellbook [1823-2484](https://commanderspellbook.com/combo/1823-2484/) (community-maintained, retrieved 2026-10-16): “For each creature opponents control that is dealt excess damage, Fall of Cair Andros triggers, creating a 0/0 Army if you dont control one, and putting a number of +1/+1 counters on an Army you control equal to the excess damage.”
- Source (re-verified): [`Saruman_the_White_Hand_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/saruman_2026-10-15/gate_output/Saruman_the_White_Hand_Rules_Attestation.json) → “Fall of Cair Andros”
- Source (re-verified): [`Saruman_the_White_Hand_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/saruman_2026-10-15/gate_output/Saruman_the_White_Hand_Rules_Attestation.json) → “Widespread Brutality”
- Source (re-verified): [`Saruman_the_White_Hand_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/saruman_2026-10-15/gate_output/Saruman_the_White_Hand_Rules_Attestation.json) → “Soul's Fire / Chandra's Ignition”

## Timing and priority

### saruman-02: X spells and MDFCs: X counts on the stack, but a free cast sets X to 0

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Saruman, the White Hand, Assault on Osgiliath, Summons of Saruman, Shatterskull Smashing // Shatterskull, the Hammer Pass, Kazuul's Fury // Kazuul's Cliffs, Sea Gate Restoration // Sea Gate, Reborn, Sink into Stupor // Soporific Springs

**Ruling.** **X spells:** on the stack, X adds to mana value, so Assault on Osgiliath, Summons of Saruman (including its flashback) and Shatterskull Smashing scale Saruman's trigger. A spell cast without paying its mana cost has X = 0, so an Assault cast free off Summons gives Saruman nothing.

**Summons' free cast:** it happens during resolution, ignores timing, and is a real cast, so it triggers Saruman for that spell's mana value.

**MDFCs:** casting the spell face triggers Saruman for that face's mana value. Playing the land face is a land play, not a cast.

**Citations**

- Scryfall ruling, *Summons of Saruman*: “If the spell has {X} in its mana cost, you must choose 0 as the value of X.”
- Scryfall ruling, *Summons of Saruman*: “If you want to cast one of the milled cards, you cast it as part of the resolution of Summons of Saruman. You can't wait to cast the spell later in the turn. Timing permissions based on the card's type are ignored.”
- [CR 202.3e](#cr-2023e), [CR 107.3b](#cr-1073b), [CR 712.11b](#cr-71211b)
- Source (re-verified): [`Saruman_the_White_Hand_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/saruman_2026-10-15/gate_output/Saruman_the_White_Hand_Rules_Attestation.json) → “X spells”
- Source (re-verified): [`Saruman_the_White_Hand_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/saruman_2026-10-15/gate_output/Saruman_the_White_Hand_Rules_Attestation.json) → “Summons of Saruman”
- Source (re-verified): [`Saruman_the_White_Hand_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/saruman_2026-10-15/gate_output/Saruman_the_White_Hand_Rules_Attestation.json) → “MDFC spell/land package”

## Replacement and prevention effects

### saruman-04: Mauhúr adds +1 per counter event; The Great Goblin and All Will Be One per event

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Saruman, the White Hand, Mauhúr, Uruk-hai Captain, The Great Goblin, All Will Be One, Bothersome Noisemaker

**Ruling.** Mauhúr turns each event that puts +1/+1 counters on your Army, Goblins or Orcs into that many plus one, so each amass X becomes X+1. The Great Goblin deals 2 to an opponent for each counter event on a Goblin, Orc or Army. All Will Be One deals damage equal to the counters actually placed, after Mauhúr. Bothersome Noisemaker's amass Goblins 1 is a separate trigger and a separate counter event. An Army that is a Goblin or Orc has ward {2} from Saruman.

**Citations**

- Oracle, *Mauhúr, Uruk-hai Captain*: “If one or more +1/+1 counters would be put on an Army, Goblin, or Orc you control, that many plus one +1/+1 counters are put on it instead.”
- Oracle, *All Will Be One*: “Whenever you put one or more counters on a permanent or player, this enchantment deals that much damage to target opponent, creature an opponent controls, or planeswalker an opponent controls.”
- Scryfall ruling, *Mauhúr, Uruk-hai Captain*: “Mauhúr's last ability applies to counters placed on Army tokens when you amass Orcs (or Zombies, or anything else.)”
- Scryfall ruling, *Saruman, the White Hand*: “A creature that is both a Goblin and an Orc still only gets one instance of ward {2} from Saruman, the White Hand's last ability.”
- [CR 614.1a](#cr-6141a), [CR 701.47a](#cr-70147a)
- Source (re-verified): [`Saruman_the_White_Hand_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/saruman_2026-10-15/gate_output/Saruman_the_White_Hand_Rules_Attestation.json) → “Mauhúr replacement”
- Source (re-verified): [`Saruman_the_White_Hand_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/saruman_2026-10-15/gate_output/Saruman_the_White_Hand_Rules_Attestation.json) → “The Great Goblin / All Will Be One”
- Source (re-verified): [`Saruman_the_White_Hand_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/saruman_2026-10-15/gate_output/Saruman_the_White_Hand_Rules_Attestation.json) → “Bothersome Noisemaker”

## Trigger ordering

### saruman-03: Trigger doublers: Harmonic Prodigy, Wizard's Staff, Veyran (Saruman is an Avatar Wizard)

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Saruman, the White Hand, Harmonic Prodigy, Wizard's Staff, Veyran, Voice of Duality

**Ruling.** Each of these adds one more Saruman trigger, and they add together:
- Harmonic Prodigy (Saruman is a Wizard).
- Wizard's Staff, with equip Wizard {1}.
- Veyran, but only when the spell is an instant or sorcery, since Veyran cares about casting or copying those. Saruman's trigger on artifact or enchantment spells isn't doubled by Veyran.

With all three, an instant gives four amass triggers.

**Citations**

- Oracle, *Veyran, Voice of Duality*: “If you casting or copying an instant or sorcery spell causes a triggered ability of a permanent you control to trigger, that ability triggers an additional time.”
- [CR 603.2d](#cr-6032d)
- Source (re-verified): [`Saruman_the_White_Hand_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/saruman_2026-10-15/gate_output/Saruman_the_White_Hand_Rules_Attestation.json) → “Harmonic Prodigy / Wizard's Staff / Veyran”

## Zones, commander tax and the command zone

### saruman-06: Mizzix's Mastery casts copies, which do trigger Saruman

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Saruman, the White Hand, Mizzix's Mastery

**Ruling.** Mizzix's Mastery copies instant or sorcery cards in exile and lets you cast them. Each one you cast is a noncreature spell, so Saruman triggers for its mana value. Overloaded, it triggers for every copy you cast, plus 4 for Mastery itself (overload doesn't change its mana value).

**Citations**

- Oracle, *Mizzix's Mastery*: “Exile target card that's an instant or sorcery from your graveyard. For each card exiled this way, copy it, and you may cast the copy without paying its mana cost. Exile Mizzix's Mastery.”
- [CR 707.12](#cr-70712), [CR 202.3](#cr-2023)
- Source (re-verified): [`Saruman_the_White_Hand_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/saruman_2026-10-15/gate_output/Saruman_the_White_Hand_Rules_Attestation.json) → “Mizzix's Mastery”

## Legality and project exceptions

### saruman-07: The Black Gate chooses a player; only the creature is targeted (source wording off)

**Status:** 🚩 list flag · **Evidence:** fact · **Cards:** Saruman, the White Hand, The Black Gate

**Ruling.** The Black Gate's {1}{B}, {T} ability targets only a creature. The player with the most life, or tied for it, is chosen when the ability resolves, not targeted. So hexproof or shroud on that player doesn't stop it, and Saruman's ward isn't involved. That player's creatures can't block your Army this turn. The source attestation says the ability "targets a creature and a player". The effect is described correctly, but the targeting wording is wrong.

**List flag (documentation).** The source rules attestation (The Black Gate item) says the ability 'targets a creature and a player'. Per Oracle, the player is chosen and only the creature is targeted. Text fix only; the deck isn't affected.

**Citations**

- Oracle, *The Black Gate*: “{1}{B}, {T}: Choose a player with the most life or tied for most life. Target creature can't be blocked by creatures that player controls this turn.”
- [CR 115.1](#cr-1151), [CR 608.2c](#cr-6082c)
- Source (re-verified): [`Saruman_the_White_Hand_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/saruman_2026-10-15/gate_output/Saruman_the_White_Hand_Rules_Attestation.json) → “The Black Gate”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 107.3b

If a player is casting a spell that has an {X} in its mana cost, the value of X isn’t defined by the text of that spell, and an effect lets that player cast that spell while paying neither its mana cost nor an alternative cost that includes X, then the only legal choice for X is 0. This doesn’t apply to effects that only reduce a cost, even if they reduce it to zero. See rule 601, “Casting Spells.”

#### CR 115.1

Some spells and abilities require their controller to choose one or more targets for them. The targets are object(s) and/or player(s) the spell or ability will affect. These targets are declared as part of the process of putting the spell or ability on the stack. The targets can’t be changed except by another spell or ability that explicitly says it can do so.

#### CR 120.10

Some triggered abilities check whether a permanent has been dealt excess damage. These abilities check after the permanent has been dealt damage by one or more sources. If those sources together dealt an amount of damage to a creature greater than lethal damage, excess damage equal to the difference was dealt to that creature. If those sources together dealt an amount of damage to a planeswalker greater than that planeswalker’s loyalty before the damage was dealt, excess damage equal to the difference was dealt to that planeswalker. If those sources together dealt an amount of damage to a …

#### CR 202.3

The mana value of an object is a number equal to the total amount of mana in its mana cost, regardless of color.

#### CR 202.3e

When calculating the mana value of an object with an {X} in its mana cost, X is treated as 0 while the object is not on the stack, and X is treated as the number chosen for it while the object is on the stack.

#### CR 601.2f

The player determines the total cost of the spell. Usually this is just the mana cost. Some spells have additional or alternative costs. Some effects may increase or reduce the cost to pay, or may provide other alternative costs. Costs may include paying mana, tapping permanents, sacrificing permanents, discarding cards, and so on. The total cost is the mana cost or alternative cost (as determined in rule 601.2b), plus all additional costs and cost increases, and minus all cost reductions. If multiple cost reductions apply, the player may apply them in any order. If the mana component of the …

#### CR 603.2d

An ability may state that a triggered ability triggers additional times. In this case, rather than simply determining that such an ability has triggered, determine how many times it should trigger, then that ability triggers that many times. An effect that states that an ability triggers additional times doesn’t invoke itself repeatedly and doesn’t apply to other effects that affect how many times an ability triggers. An effect that states a triggered ability of an object triggers additional times refers only to triggered abilities that object has, not to any delayed or reflexive triggered …

#### CR 608.2c

The controller of the spell or ability follows its instructions in the order written. However, replacement effects may modify these actions. In some cases, later text on the card may modify the meaning of earlier text (for example, “Destroy target creature. It can’t be regenerated” or “Counter target spell. If that spell is countered this way, put it on top of its owner’s library instead of into its owner’s graveyard.”) Don’t just apply effects step by step without thinking in these cases—read the whole text and apply the rules of English to the text.

#### CR 614.1a

Effects that use the word “instead” are replacement effects. Most replacement effects use the word “instead” to indicate what events will be replaced with other events.

#### CR 701.47a

To amass [subtype] N means “If you don’t control an Army creature, create a 0/0 black [subtype] Army creature token. Choose an Army creature you control. Put N +1/+1 counters on that creature. If it isn’t a [subtype], it becomes a [subtype] in addition to its other types.”

#### CR 707.12

An effect that instructs a player to cast a copy of an object (and not just copy a spell) follows the rules for casting spells, except that the copy is created in the same zone the object is in and then cast while another spell or ability is resolving. Casting a copy of an object follows steps 601.2a–h of rule 601, “Casting Spells,” and then the copy becomes cast. Once cast, the copy is a spell on the stack, and just like any other spell it can resolve or be countered.

#### CR 712.11b

A player casting a modal double-faced card or a copy of a modal double-faced card as a spell chooses which face they are casting before putting it onto the stack.

