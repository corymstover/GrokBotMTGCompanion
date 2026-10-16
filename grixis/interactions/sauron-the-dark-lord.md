---
title: "Sauron, the Dark Lord — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Sauron, the Dark Lord — Interaction Review

> Bot cycle 54 · batch E · reviewed 2026-10-16. Deck: [Sauron, the Dark Lord](../decks/sauron-the-dark-lord.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-15), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/sauron-the-dark-lord.txt`](../../exports/grixis-archidekt/sauron-the-dark-lord.txt) · SHA-256 `1d553979b827147118b5262797ae38dea83be27e2f5f045b371046a33076b11d` |
| Rulings | **5** (5 verified · 0 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-15 · rulings 2026-10-15 |
| Source attestations | [`Sauron_the_Dark_Lord_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sauron_dark_lord_2026-10-15/gate_output/Sauron_the_Dark_Lord_Rules_Attestation.json) (Rules attestation (13 items, all PASS) re-verified) · [`Sauron_the_Dark_Lord_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Sauron_the_Dark_Lord_Approval_Ready_Verification_2026-10-15.md) (Approval-ready verification) |

## Contents
- [Summary](#summary)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Engines and payoffs](#engines-and-payoffs)
- [Layers and continuous effects](#layers-and-continuous-effects)
- [Replacement and prevention effects](#replacement-and-prevention-effects)
- [Trigger ordering](#trigger-ordering)
- [Rules cited](#rules-cited)

## Summary

Sauron, the Dark Lord grows an Orc Army off every opponent spell and turns Army hits into Ring temptations, each one an optional discard-and-draw-four. The list runs seven Nazgûl (legal under their own text) for repeated temptations and Wraith counters, uses Minas Morgul to make the Army an evasive Wraith, Roaming Throne to double Sauron (Avatar) or the Nazgûl (Wraith), and Mauhúr, both Great Goblins and Widespread Brutality on the Army. There are no Spellbook lines. All 13 attestation items are re-verified against the canonical list; the Force of Will pitch count is taken from the source, not re-derived.

Rules surprises: a shadow-counter Army is both Wraith and Army; Throne can double only one type; Widespread Brutality spares the Army but hits your own Nazgûl and Sauron. No list errors.

## Commander rules text and edge cases

### saurondl-01: Sauron's loop: opponents' spells feed the Army, Army hits tempt the Ring, each temptation offers discard-hand / draw four

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Sauron, the Dark Lord

**Ruling.** Every spell an opponent casts triggers amass Orcs 1, and the trigger resolves even if that spell is countered. When your Army deals combat damage to a player, the Ring tempts you, even if you control no creatures. Each temptation, from any source, triggers Sauron's optional "discard your hand, draw four" separately. Sauron's ward costs the opponent a legendary artifact or legendary creature sacrifice, or their spell or ability is countered.

**Citations**

- Oracle, *Sauron, the Dark Lord*: “Whenever an opponent casts a spell, amass Orcs 1.”
- Oracle, *Sauron, the Dark Lord*: “Whenever the Ring tempts you, you may discard your hand. If you do, draw four cards.”
- Scryfall ruling, *Sauron, the Dark Lord*: “The Ring can tempt you even if you don't control a creature. In this case, abilities that trigger "whenever the Ring tempts you" will still trigger.”
- [CR 702.21a](#cr-70221a), [CR 701.54a](#cr-70154a), [CR 113.7a](#cr-1137a)
- Source (re-verified): [`Sauron_the_Dark_Lord_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sauron_dark_lord_2026-10-15/gate_output/Sauron_the_Dark_Lord_Rules_Attestation.json) → “Sauron ward”
- Source (re-verified): [`Sauron_the_Dark_Lord_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sauron_dark_lord_2026-10-15/gate_output/Sauron_the_Dark_Lord_Rules_Attestation.json) → “Opponent-spell amass trigger”
- Source (re-verified): [`Sauron_the_Dark_Lord_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sauron_dark_lord_2026-10-15/gate_output/Sauron_the_Dark_Lord_Rules_Attestation.json) → “Army combat into Ring engine”

## Engines and payoffs

### saurondl-02: Seven Nazgûl: legal, and every temptation is a counter wave plus a Sauron draw

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Sauron, the Dark Lord, Nazgûl

**Ruling.** Nazgûl allows up to nine copies, and the canonical list runs seven. Each Nazgûl ETB tempts you, so Sauron offers a wheel each time. Each Nazgûl also triggers on every temptation, putting a counter on each Wraith. With k Nazgûl out, one temptation gives each Wraith k counters.

**Citations**

- Oracle, *Nazgûl*: “A deck can have up to nine cards named Nazgûl.”
- Oracle, *Nazgûl*: “When this creature enters, the Ring tempts you.”
- Scryfall ruling, *Nazgûl*: “The last ability of Nazgûl also lets you ignore the "singleton" rule in formats like Commander.”
- [CR 903.5b](#cr-9035b), [CR 701.54a](#cr-70154a)
- Source (re-verified): [`Sauron_the_Dark_Lord_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sauron_dark_lord_2026-10-15/gate_output/Sauron_the_Dark_Lord_Rules_Attestation.json) → “Nazgûl construction and Ring triggers”

## Layers and continuous effects

### saurondl-03: Minas Morgul turns the Army into a Wraith with shadow, so it stays an Army for Sauron

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Sauron, the Dark Lord, Minas Morgul, Dark Fortress, Nazgûl

**Ruling.** Minas Morgul's {3}{B}, {T} ability puts a shadow counter on a creature. While the counter stays, the creature is a Wraith in addition to its other types and has shadow, which is a keyword counter. A shadow Army can be blocked only by creatures with shadow. It remains an Army, so its hits tempt the Ring, and as a Wraith it gets every Nazgûl counter.

**Citations**

- Oracle, *Minas Morgul, Dark Fortress*: “{3}{B}, {T}: Put a shadow counter on target creature. For as long as that creature has a shadow counter on it, it's a Wraith in addition to its other types. (A creature with shadow can block or be blocked by only creatures with shadow.)”
- Scryfall ruling, *Minas Morgul, Dark Fortress*: “A permanent with a shadow counter on it has shadow.”
- [CR 122.1b](#cr-1221b), [CR 702.28b](#cr-70228b), [CR 205.1b](#cr-2051b)
- Source (re-verified): [`Sauron_the_Dark_Lord_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sauron_dark_lord_2026-10-15/gate_output/Sauron_the_Dark_Lord_Rules_Attestation.json) → “Minas Morgul Army-Wraith bridge”

## Replacement and prevention effects

### saurondl-05: Army counter support: Mauhúr, The Great Goblin, Great Goblin, Foul-Hearted, Widespread Brutality

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Sauron, the Dark Lord, Mauhúr, Uruk-hai Captain, The Great Goblin, Great Goblin, Foul-Hearted, Widespread Brutality

**Ruling.** These grow or use the Army:
- **Mauhúr:** each amass Orcs 1 becomes 2 counters.
- **The Great Goblin:** deals 2 damage per counter event, not per counter.
- **Great Goblin, Foul-Hearted:** amasses Goblins 3 on entering and attacking. That makes the Army a Goblin Orc, and he gives Armies trample.
- **Widespread Brutality:** amasses, then the Army deals its power to each non-Army creature. The Army is spared, but your Nazgûl and Sauron aren't.

**Citations**

- Oracle, *Great Goblin, Foul-Hearted*: “Whenever Great Goblin enters or attacks, amass Goblins 3. (Put three +1/+1 counters on an Army you control. It's also a Goblin. If you don't control an Army, create a 0/0 black Goblin Army creature token first.)
Armies you control have trample.”
- Scryfall ruling, *Mauhúr, Uruk-hai Captain*: “Mauhúr's last ability applies to counters placed on Army tokens when you amass Orcs (or Zombies, or anything else.)”
- [CR 614.1a](#cr-6141a), [CR 701.47a](#cr-70147a)
- Source (re-verified): [`Sauron_the_Dark_Lord_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sauron_dark_lord_2026-10-15/gate_output/Sauron_the_Dark_Lord_Rules_Attestation.json) → “Mauhúr replacement”
- Source (re-verified): [`Sauron_the_Dark_Lord_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sauron_dark_lord_2026-10-15/gate_output/Sauron_the_Dark_Lord_Rules_Attestation.json) → “The Great Goblin counter trigger”
- Source (re-verified): [`Sauron_the_Dark_Lord_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sauron_dark_lord_2026-10-15/gate_output/Sauron_the_Dark_Lord_Rules_Attestation.json) → “Great Goblin, Foul-Hearted”
- Source (re-verified): [`Sauron_the_Dark_Lord_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sauron_dark_lord_2026-10-15/gate_output/Sauron_the_Dark_Lord_Rules_Attestation.json) → “Widespread Brutality”
- Source (re-verified): [`Sauron_the_Dark_Lord_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sauron_dark_lord_2026-10-15/gate_output/Sauron_the_Dark_Lord_Rules_Attestation.json) → “Wonder and Anger”
- Source (re-verified): [`Sauron_the_Dark_Lord_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sauron_dark_lord_2026-10-15/gate_output/Sauron_the_Dark_Lord_Rules_Attestation.json) → “Force of Will support”

## Trigger ordering

### saurondl-04: Roaming Throne: name Avatar to double Sauron, or Wraith to double Nazgûl, not both

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Sauron, the Dark Lord, Roaming Throne, Nazgûl

**Ruling.** Roaming Throne doubles triggers of one creature type, so pick:
- **Avatar:** Sauron is an Avatar Horror, so each of his triggers (amass, tempt, discard/draw) happens twice.
- **Wraith:** each Nazgûl's tempt and counter triggers happen twice. Throne also becomes a Wraith, so Nazgûl counters land on it too.

There's only one choice per Throne.

**Citations**

- Oracle, *Roaming Throne*: “If a triggered ability of another creature you control of the chosen type triggers, it triggers an additional time.”
- Scryfall ruling, *Roaming Throne*: “Roaming Throne's last ability doesn't copy the triggered ability; it just causes the ability to trigger an additional time. Any choices made as you put the ability onto the stack, such as modes and targets, are made separately for each instance of the ability. Any choices made on resolution, such as whether to put counters on a permanent, are also made individually.”
- [CR 603.2d](#cr-6032d)
- Source (re-verified): [`Sauron_the_Dark_Lord_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sauron_dark_lord_2026-10-15/gate_output/Sauron_the_Dark_Lord_Rules_Attestation.json) → “Roaming Throne — Avatar mode”
- Source (re-verified): [`Sauron_the_Dark_Lord_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sauron_dark_lord_2026-10-15/gate_output/Sauron_the_Dark_Lord_Rules_Attestation.json) → “Roaming Throne — Wraith mode”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 113.7a

Once activated or triggered, an ability exists on the stack independently of its source. Destruction or removal of the source after that time won’t affect the ability. Note that some abilities cause a source to do something (for example, “This creature deals 1 damage to any target”) rather than the ability doing anything directly. In these cases, any activated or triggered ability that references information about the source for use while announcing an activated ability or putting a triggered ability on the stack checks that information when the ability is put onto the stack. Otherwise, it …

#### CR 122.1b

A keyword counter on a permanent or on a card in a zone other than the battlefield causes that object to gain that keyword. The keywords that a keyword counter can be are flying, first strike, double strike, deathtouch, decayed, exalted, haste, hexproof, indestructible, lifelink, menace, reach, shadow, trample, and vigilance, as well as any variants of those keywords. See rule 613.1f.

#### CR 205.1b

Some effects change an object’s card type, supertype, or subtype but specify that the object retains a prior card type, supertype, or subtype. In such cases, all the object’s prior card types, supertypes, and subtypes are retained. This rule applies to effects that use phrases such as “in addition to its other types” or that state that something is “still a [type, supertype, or subtype].” Some effects state that an object becomes an “artifact creature”; these effects also allow the object to retain all of its prior card types and subtypes. Some effects state that an object becomes a …

#### CR 603.2d

An ability may state that a triggered ability triggers additional times. In this case, rather than simply determining that such an ability has triggered, determine how many times it should trigger, then that ability triggers that many times. An effect that states that an ability triggers additional times doesn’t invoke itself repeatedly and doesn’t apply to other effects that affect how many times an ability triggers. An effect that states a triggered ability of an object triggers additional times refers only to triggered abilities that object has, not to any delayed or reflexive triggered …

#### CR 614.1a

Effects that use the word “instead” are replacement effects. Most replacement effects use the word “instead” to indicate what events will be replaced with other events.

#### CR 701.47a

To amass [subtype] N means “If you don’t control an Army creature, create a 0/0 black [subtype] Army creature token. Choose an Army creature you control. Put N +1/+1 counters on that creature. If it isn’t a [subtype], it becomes a [subtype] in addition to its other types.”

#### CR 701.54a

Certain spells and abilities have the text “the Ring tempts you.” Each time the Ring tempts you, choose a creature you control. That creature becomes your Ring-bearer until another creature becomes your Ring-bearer or another player gains control of it.

#### CR 702.21a

Ward is a triggered ability. Ward [cost] means “Whenever this permanent becomes the target of a spell or ability an opponent controls, counter that spell or ability unless that player pays [cost].”

#### CR 702.28b

A creature with shadow can’t be blocked by creatures without shadow, and a creature without shadow can’t be blocked by creatures with shadow. (See rule 509, “Declare Blockers Step.”)

#### CR 903.5b

Other than basic lands, each card in a Commander deck must have a different English name. For the purposes of deck construction, cards with interchangeable names have the same English name (see rule 201.3).

