---
title: "Wick, the Whorled Mind — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Wick, the Whorled Mind — Interaction Review

> Bot cycle 56 · batch F · reviewed 2026-10-16. Deck: [Wick, the Whorled Mind](../decks/wick-the-whorled-mind.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/wick-the-whorled-mind.txt`](../../exports/grixis-archidekt/wick-the-whorled-mind.txt) · SHA-256 `0d784f93911618a7f6698ad8f1ad0799399ed2305df5c9568dbdbfb75b31f8e5` |
| Rulings | **6** (6 verified · 0 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md) (Approval-ready verification (no rules attestation JSON in source)) |

## Contents
- [Summary](#summary)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [Key card-pair interactions](#key-card-pair-interactions)
- [What the list depends on](#what-the-list-depends-on)
- [Rules cited](#rules-cited)

## Summary

Wick, the Whorled Mind makes or grows a single Snail whenever a Rat enters, then sacrifices it for damage to each opponent and draws equal to its power. The deck makes Snails into Rats (Arcane Adaptation, Leyline of Transformation, Maskwood Nexus) for 12 free-outlet loops, runs Marrow-Gnawer + Intruder Alarm for infinite Rats, and grows Snail power with Bulk Up, Blade, Relic and Ozolith. Tainted Strike turns the hit into poison. The source has no rules attestation JSON, so this review uses the approval-ready verification, and the canonical list matches its 23-card delta. All 13 Spellbook lines have every piece in the list.

Rules surprises: Wick is the damage source, so infect on Wick means poison; "if you don't control a Snail" is checked on resolution, which is what makes the sacrifice-in-response loop work; Conspiracy would break it; Cavern's mana can't activate Wick. No list errors.

## Commander rules text and edge cases

### wick-01: Wick: create-or-grow Snail on Rat entry; the activation uses the Snail's last-known power

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Wick, the Whorled Mind, Song of Totentanz, Rat King, Verminister, Tangled Colony, Voracious Vermin

**Ruling.** Each time Wick or another Rat you control enters, you get a new 1/1 Snail if you don't control one, or a +1/+1 counter on a Snail you control. "If you don't control a Snail" is checked when the trigger resolves, not when it triggers. Several Rats entering at once (Song of Totentanz for X, token makers) give one trigger each: the first makes the Snail and the rest grow it.

Wick's activation sacrifices the Snail as a cost. Damage to each opponent and the cards drawn both use the Snail's power as it last existed on the battlefield. Wick is the source of that damage.

**Citations**

- Oracle, *Wick, the Whorled Mind*: “Whenever Wick or another Rat you control enters, create a 1/1 black Snail creature token if you don't control a Snail. Otherwise, put a +1/+1 counter on a Snail you control.”
- Oracle, *Song of Totentanz*: “Create X 1/1 black Rat creature tokens with "This token can't block." Creatures you control gain haste until end of turn.”
- Scryfall ruling, *Wick, the Whorled Mind*: “Use the power of the sacrificed Snail as it last existed on the battlefield to determine how much damage to deal and how many cards to draw. While Wick may have given the Snail up, Wick won’t let you down.”
- [CR 603.2c](#cr-6032c), [CR 608.2h](#cr-6082h), [CR 113.7a](#cr-1137a)
- Source (re-verified): [`Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md) → “**Wick sacrifice resolution:** damage and cards use the sacrificed Snail's power as it last existed on the battlefield.”

## Combos and engine lines

### wick-02: Rat-typed Snails + free outlet: each Snail is a Rat that makes the next Snail

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Wick, the Whorled Mind, Arcane Adaptation, Leyline of Transformation, Maskwood Nexus, Ashnod's Altar, Phyrexian Altar, Viscera Seer, Carrion Feeder, Goblin Bombardment, Altar of Dementia, Mirkwood Bats, Impact Tremors, Zulaport Cutthroat

**Ruling.** Arcane Adaptation or Leyline of Transformation naming Rat, or Maskwood Nexus, adds Rat to your creatures and keeps their other types, so the Snail token is also a Rat. When Wick or a Rat enters, sacrifice your Snail in response to the trigger. The trigger then makes a new Snail, which is a Rat, so it triggers Wick again. Repeat. That's 12 Spellbook lines (803-/5853- with Ashnod's or Phyrexian Altar, Viscera Seer, Carrion Feeder, Goblin Bombardment or Altar of Dementia). Each loop is a sacrifice, a death and a token entering. Goblin Bombardment, Mirkwood Bats, Impact Tremors or Zulaport finishes. Conspiracy, correctly cut, would set creatures to Rat only, so the Snail would stop being a Snail.

**Citations**

- Oracle, *Arcane Adaptation*: “Creatures you control are the chosen type in addition to their other types. The same is true for creature spells you control and creature cards you own that aren't on the battlefield.”
- [CR 205.1b](#cr-2051b), [CR 613.1d](#cr-6131d), [CR 603.3b](#cr-6033b)
- Commander Spellbook [803-2034-5853](https://commanderspellbook.com/combo/803-2034-5853/) (community-maintained, retrieved 2026-10-16): “Holding priority, if you control a Snail, activate Ashnod's Altar by sacrificing the Snail, adding {C}{C}.”
- Commander Spellbook [803-2034-5853](https://commanderspellbook.com/combo/803-2034-5853/) (community-maintained, retrieved 2026-10-16): “Arcane Adaptation on the battlefield with "Rat" chosen.”
- Source (re-verified): [`Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md) → “**Conspiracy rejected:** choosing Rat makes affected creatures the chosen type rather than preserving all existing creature types, so the Snail ceases to be a Snail.”

### wick-03: Marrow-Gnawer + Intruder Alarm: infinite Rats (and infinite Snail growth)

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Wick, the Whorled Mind, Marrow-Gnawer, Intruder Alarm

**Ruling.** Tap Marrow-Gnawer and sacrifice a Rat to make X Rats, where X is the Rats you control on resolution. Intruder Alarm untaps all creatures once per token, so Marrow-Gnawer can go again with more Rats each time (Spellbook 1636-3126; needs at least two other Rats). Each Rat token also triggers Wick, so the Snail grows by a counter per Rat. Intruder Alarm also stops your creatures from untapping normally, but Wick's ability doesn't tap.

**Citations**

- Oracle, *Intruder Alarm*: “Whenever a creature enters, untap all creatures.”
- Scryfall ruling, *Marrow-Gnawer*: “Marrow-Gnawer's ability counts the number of Rats on the battlefield when it resolves, so you don't count the sacrificed Rat.”
- Scryfall ruling, *Intruder Alarm*: “If multiple creatures enter the battlefield at one time, this ability triggers once for each of those creatures.”
- [CR 603.2c](#cr-6032c)
- Commander Spellbook [1636-3126](https://commanderspellbook.com/combo/1636-3126/) (community-maintained, retrieved 2026-10-16): “Intruder Alarm triggers once for each creature token created, untapping all creatures that many times.”
- Source (re-verified): [`Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md) → “**Marrow-Gnawer + Intruder Alarm:** with at least two Rats available to tap with Marrow-Gnawer”

## Engines and payoffs

### wick-05: Growing and keeping Snail power: Bulk Up, Blade of the Bloodchief, Lich's Relic, The Ozolith

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Wick, the Whorled Mind, Bulk Up, Blade of the Bloodchief, Lich's Relic, The Ozolith

**Ruling.** Growing the Snail:
- **Bulk Up** doubles the Snail's power for the turn, and flashback gives a second use.
- **Blade of the Bloodchief** adds a counter whenever any creature dies. Snails aren't Vampires, so it's one counter.
- **Lich's Relic** adds +2/+1.

**The Ozolith** stores the counters when you sacrifice a Snail with counters. At your beginning of combat you can move all of them onto the new Snail, but not just some. Its trigger needs a legal target when it resolves.

**Citations**

- Oracle, *The Ozolith*: “Whenever a creature you control leaves the battlefield, if it had counters on it, put those counters on The Ozolith.”
- Oracle, *Blade of the Bloodchief*: “Whenever a creature dies, put a +1/+1 counter on equipped creature. If equipped creature is a Vampire, put two +1/+1 counters on it instead.”
- Scryfall ruling, *The Ozolith*: “You can't move only some of the counters from The Ozolith onto the target creature.”
- [CR 122.1](#cr-1221), [CR 613.4c](#cr-6134c)
- Source (re-verified): [`Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md) → “**The Ozolith:** when a Snail with +1/+1 counters leaves the battlefield, those counters can be stored on The Ozolith”

## Key card-pair interactions

### wick-04: Tainted Strike: Wick's damage becomes poison

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Wick, the Whorled Mind, Tainted Strike

**Ruling.** Wick is the source of the activated damage, so Tainted Strike on Wick before the ability resolves turns that damage to each opponent into poison counters. A 10-power Snail gives everyone 10 poison. Infect works on noncombat damage too, and it can still be prevented. Cast Tainted Strike on Wick, not on the Snail you're sacrificing.

**Citations**

- Oracle, *Tainted Strike*: “Target creature gets +1/+0 and gains infect until end of turn. (It deals damage to creatures in the form of -1/-1 counters and to players in the form of poison counters.)”
- Scryfall ruling, *Tainted Strike*: “Infect’s effect applies to any damage, not just combat damage.”
- Scryfall ruling, *Tainted Strike*: “A player who has ten or more poison counters loses the game. This is a state-based action.”
- [CR 702.90b](#cr-70290b), [CR 704.5c](#cr-7045c)
- Source (re-verified): [`Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md) → “**Tainted Strike:** Wick, not the sacrificed Snail, is the source dealing the activated-ability damage.”

## What the list depends on

### wick-06: Cavern of Souls can't pay Wick's {U}{B}{R}

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Wick, the Whorled Mind, Cavern of Souls

**Ruling.** Cavern of Souls naming Rat makes Wick and Rat creature spells uncounterable. Its colored mana can only be spent to cast creature spells of that type, so it can't pay Wick's {U}{B}{R} activation. Count it as {C} for the combo. The approval-ready note says the same.

**Citations**

- Oracle, *Cavern of Souls*: “{T}: Add one mana of any color. Spend this mana only to cast a creature spell of the chosen type, and that spell can't be countered.”
- [CR 106.6](#cr-1066)
- Source (re-verified): [`Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md) → “its restricted colored mana cannot pay Wick's `{U}{B}{R}` activated ability.”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 106.6

Some spells or abilities that produce mana restrict how that mana can be spent, have an additional effect that affects the spell or ability that mana is spent on, or create a delayed triggered ability (see rule 603.7a) that triggers when that mana is spent. This doesn’t affect the mana’s type.

#### CR 113.7a

Once activated or triggered, an ability exists on the stack independently of its source. Destruction or removal of the source after that time won’t affect the ability. Note that some abilities cause a source to do something (for example, “This creature deals 1 damage to any target”) rather than the ability doing anything directly. In these cases, any activated or triggered ability that references information about the source for use while announcing an activated ability or putting a triggered ability on the stack checks that information when the ability is put onto the stack. Otherwise, it …

#### CR 122.1

A counter is a marker placed on an object or player that modifies its characteristics and/or interacts with a rule, ability, or effect. Counters are not objects and have no characteristics. Notably, a counter is not a token, and a token is not a counter. Counters with the same name or description are interchangeable.

#### CR 205.1b

Some effects change an object’s card type, supertype, or subtype but specify that the object retains a prior card type, supertype, or subtype. In such cases, all the object’s prior card types, supertypes, and subtypes are retained. This rule applies to effects that use phrases such as “in addition to its other types” or that state that something is “still a [type, supertype, or subtype].” Some effects state that an object becomes an “artifact creature”; these effects also allow the object to retain all of its prior card types and subtypes. Some effects state that an object becomes a …

#### CR 603.2c

An ability triggers only once each time its trigger event occurs. However, it can trigger repeatedly if one event contains multiple occurrences.

#### CR 603.3b

If multiple abilities have triggered since the last time a player received priority, the abilities are placed on the stack in a two-part process. First, each player, in APNAP order, puts each triggered ability they control with a trigger condition that isn’t another ability triggering on the stack in any order they choose. (See rule 101.4.) Second, each player, in APNAP order, puts all remaining triggered abilities they control on the stack in any order they choose. Then the game once again checks for and performs state-based actions until none are performed, then abilities that triggered …

#### CR 608.2h

If an effect requires information from the game (such as the number of creatures on the battlefield), the answer is determined only once, when the effect is applied. If the effect requires information from a specific object, including the source of the ability itself, the effect uses the current information of that object if it’s in the public zone it was expected to be in; if it’s no longer in that zone, or if the effect has moved it from a public zone to a hidden zone, the effect uses the object’s last known information. See rule 113.7a. If an ability states that an object does something, …

#### CR 613.1d

Layer 4: Type-changing effects are applied. These include effects that change an object’s card type, subtype, and/or supertype.

#### CR 613.4c

Layer 7c: Effects and counters that modify power and/or toughness (but don’t set power and/or toughness to a specific number or value) are applied.

#### CR 702.90b

Damage dealt to a player by a source with infect doesn’t cause that player to lose life. Rather, it causes that source’s controller to give the player that many poison counters. See rule 120.3.

#### CR 704.5c

If a player has ten or more poison counters, that player loses the game. Ignore this rule in Two-Headed Giant games; see rule 704.6b instead.

