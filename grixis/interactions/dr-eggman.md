---
title: "Dr. Eggman — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Dr. Eggman — Interaction Review

> Bot cycle 48 · batch B · reviewed 2026-10-16. Deck: [Dr. Eggman](../decks/dr-eggman.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-15), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/dr-eggman.txt`](../../exports/grixis-archidekt/dr-eggman.txt) · SHA-256 `7110223f41570f87c3e5aa879cb46f2727ab94c43f96163cd861f2561882744a` |
| Rulings | **10** (10 verified · 0 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-15 · rulings 2026-10-15 |
| Source attestations | [`Dr_Eggman_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/dr_eggman_2026-10-14/Dr_Eggman_Rules_Attestation.json) (17 interactions, all PASS) |

## Contents
- [Summary](#summary)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Engines and payoffs](#engines-and-payoffs)
- [Timing and priority](#timing-and-priority)
- [Replacement and prevention effects](#replacement-and-prevention-effects)
- [Trigger ordering](#trigger-ordering)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [Rules cited](#rules-cited)

## Summary

Dr. Eggman draws at your end step, then each opponent chooses: discard, or you may put a Construct, Robot or Vehicle from your hand onto the battlefield. This review re-verifies the seventeen items of the deck's rules attestation.

Key rules: empty-handed opponents can choose 'discard' at no cost, Eggman's placement isn't a cast, and Y'shtola Rhul only adds extra end steps from the first end step. No list errors.

## Commander rules text and edge cases

### eggman-01: Opponents choose one at a time, in turn order

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Dr. Eggman

**Ruling.** Eggman's trigger draws you a card first. Then each opponent, one at a time in APNAP order, picks an option and it's carried out before the next opponent chooses. Later opponents see any Construct, Robot or Vehicle already put onto the battlefield.

**Citations**

- Oracle, *Dr. Eggman*: “At the beginning of your end step, draw a card. Then each opponent faces a villainous choice — That player discards a card, or you may put a Construct, Robot, or Vehicle card from your hand onto the battlefield.”
- [CR 701.55a](#cr-70155a), [CR 701.55d](#cr-70155d), [CR 101.4](#cr-1014)
- Source (re-verified): [`Dr_Eggman_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/dr_eggman_2026-10-14/Dr_Eggman_Rules_Attestation.json) → “Dr. Eggman villainous-choice sequencing”

### eggman-02: An empty-handed opponent can choose to discard and lose nothing

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Dr. Eggman, Tinybones, Bauble Burglar

**Ruling.** A player facing a villainous choice may pick an impossible option and do as much as possible. An opponent with no cards in hand can choose 'discard' and nothing happens. There's no fallback that forces the other option. Eggman's own placement is also a 'may'. Tinybones only triggers on an actual discard, so it gets nothing from an empty-handed 'discard' choice.

**Citations**

- Oracle, *Tinybones, Bauble Burglar*: “Whenever an opponent discards a card, exile it from their graveyard with a stash counter on it.”
- [CR 701.55b](#cr-70155b)
- Source (re-verified): [`Dr_Eggman_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/dr_eggman_2026-10-14/Dr_Eggman_Rules_Attestation.json) → “Impossible villainous-choice branch”
- Source (re-verified): [`Dr_Eggman_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/dr_eggman_2026-10-14/Dr_Eggman_Rules_Attestation.json) → “Tinybones and actual Eggman discards”

## Engines and payoffs

### eggman-09: Construct, Robot and Vehicle supply

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Dr. Eggman, Scrapyard Recombiner, Master Transmuter, Ultron, Artificial Malevolence

**Ruling.** Scrapyard Recombiner is a Construct (a legal Eggman placement) and tutors Constructs to hand; it can sacrifice itself to pay its own cost. Master Transmuter returns an artifact to pay its cost and puts one from hand onto the battlefield; it can be the same card, which returns as a new object. Ultron, Artificial Malevolence can copy any nontoken artifact that enters, including one Eggman placed, for {2}; a noncreature copy becomes a 2/2 Robot.

**Citations**

- Oracle, *Scrapyard Recombiner*: “{T}, Sacrifice an artifact: Search your library for a Construct card, reveal it, put it into your hand, then shuffle.”
- Oracle, *Ultron, Artificial Malevolence*: “Whenever another nontoken artifact you control enters, you may pay {2}. If you do, create a token that's a copy of it.”
- Scryfall ruling, *Scrapyard Recombiner*: “You can sacrifice Scrapyard Recombiner to pay the cost of its second ability.”
- Scryfall ruling, *Master Transmuter*: “The artifact card you put onto the battlefield when the ability resolves may be the same card that you returned to your hand when you paid the cost.”
- [CR 602.2](#cr-6022), [CR 400.7](#cr-4007), [CR 707.2](#cr-7072)
- Source (re-verified): [`Dr_Eggman_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/dr_eggman_2026-10-14/Dr_Eggman_Rules_Attestation.json) → “Scrapyard Recombiner feeds Eggman targets”
- Source (re-verified): [`Dr_Eggman_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/dr_eggman_2026-10-14/Dr_Eggman_Rules_Attestation.json) → “Ultron, Artificial Malevolence artifact-copy trigger”
- Source (re-verified): [`Dr_Eggman_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/dr_eggman_2026-10-14/Dr_Eggman_Rules_Attestation.json) → “Master Transmuter and artifact-enter engines”

### eggman-10: One with the Machine counts on resolution

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Dr. Eggman, One with the Machine

**Ruling.** One with the Machine draws equal to the highest mana value among your artifacts, checked as it resolves. A big artifact Eggman put out raises it. {X} in a permanent's mana cost counts as 0.

**Citations**

- Oracle, *One with the Machine*: “Draw cards equal to the greatest mana value among artifacts you control.”
- Scryfall ruling, *One with the Machine*: “If a permanent has {X} in its mana cost, X is considered to be 0.”
- [CR 202.3](#cr-2023), [CR 608.2h](#cr-6082h)
- Source (re-verified): [`Dr_Eggman_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/dr_eggman_2026-10-14/Dr_Eggman_Rules_Attestation.json) → “One with the Machine draw scaling”

## Timing and priority

### eggman-06: Y'shtola Rhul's extra end step retriggers Eggman

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Dr. Eggman, Y'shtola Rhul

**Ruling.** If Y'shtola's ability resolves during the first end step, there's an additional end step and every 'beginning of your end step' trigger fires again. If its only target is illegal on resolution, nothing happens, so there's no extra step. Several Y'shtola triggers in the first end step (including a Spark Double copy) each add an extra step. Ones triggering in the extra steps don't, because it's no longer the first end step. Damage and 'until end of turn' effects last until cleanup, after the last end step.

**Citations**

- Oracle, *Y'shtola Rhul*: “Then if it's the first end step of the turn, there is an additional end step after this step.”
- Scryfall ruling, *Y'shtola Rhul*: “Abilities that trigger "at the beginning of [your/the] end step" will trigger at the beginning of each of your additional end steps as well.”
- Scryfall ruling, *Y'shtola Rhul*: “If the target creature is an illegal target as Y'shtola Rhul's ability tries to resolve, it won't resolve and none of its effects will happen. There won't be an additional end step.”
- Scryfall ruling, *Y'shtola Rhul*: “Damage marked on permanents won't be removed until you actually get to the cleanup step (which will happen after your second end step), and "until end of turn" and "this turn" effects won't end until the cleanup step either.”
- [CR 500.8](#cr-5008), [CR 513.1](#cr-5131), [CR 608.2b](#cr-6082b)
- Source (re-verified): [`Dr_Eggman_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/dr_eggman_2026-10-14/Dr_Eggman_Rules_Attestation.json) → “Y'shtola Rhul additional end step”
- Source (re-verified): [`Dr_Eggman_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/dr_eggman_2026-10-14/Dr_Eggman_Rules_Attestation.json) → “Multiple first-end-step Y'shtola effects”

## Replacement and prevention effects

### eggman-04: The Valeyard makes each opponent choose twice

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Dr. Eggman, The Valeyard, Davros, Dalek Creator

**Ruling.** The Valeyard replaces 'face a villainous choice' with facing it an additional time. Each instance is chosen and performed separately, and the choices can differ. This works for Davros's end-step villainous choice too.

**Citations**

- Oracle, *The Valeyard*: “If an opponent would face a villainous choice, they face that choice an additional time. (They can make the same or different choices.)”
- [CR 701.55c](#cr-70155c)
- Source (re-verified): [`Dr_Eggman_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/dr_eggman_2026-10-14/Dr_Eggman_Rules_Attestation.json) → “The Valeyard with Dr. Eggman”

## Trigger ordering

### eggman-05: Extra Eggman triggers: Roaming Throne, Spark Double, Strionic Resonator

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Dr. Eggman, Roaming Throne, Spark Double, Strionic Resonator

**Ruling.** Eggman is a Human Scientist. Roaming Throne naming Scientist makes his trigger trigger again; that's not a copy, and Davros (also a Scientist) benefits too. Spark Double copies him as a nonlegendary creature with its own trigger. Strionic Resonator copies the trigger on the stack. Each instance resolves fully: one draw and a new round of choices.

**Citations**

- Scryfall ruling, *Roaming Throne*: “Roaming Throne's last ability doesn't copy the triggered ability; it just causes the ability to trigger an additional time.”
- Scryfall ruling, *Strionic Resonator*: “Any choices made when the triggered ability resolves won't have been made yet when it's copied.”
- [CR 603.2](#cr-6032), [CR 707.10](#cr-70710)
- Source (re-verified): [`Dr_Eggman_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/dr_eggman_2026-10-14/Dr_Eggman_Rules_Attestation.json) → “Roaming Throne naming Scientist”
- Source (re-verified): [`Dr_Eggman_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/dr_eggman_2026-10-14/Dr_Eggman_Rules_Attestation.json) → “Spark Double copying Dr. Eggman”
- Source (re-verified): [`Dr_Eggman_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/dr_eggman_2026-10-14/Dr_Eggman_Rules_Attestation.json) → “Strionic Resonator copying Dr. Eggman”

### eggman-08: Thopter Fabricator triggers only on the second draw

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Dr. Eggman, Thopter Fabricator

**Ruling.** On a normal turn your draw step is the first card, and Eggman's end-step draw is the second, so it makes one Thopter. Extra Eggman draws later that turn are the third and beyond and don't trigger Fabricator.

**Citations**

- Oracle, *Thopter Fabricator*: “Whenever you draw your second card each turn, create a 1/1 colorless Thopter artifact creature token with flying.”
- [CR 121.2](#cr-1212), [CR 603.2](#cr-6032)
- Source (re-verified): [`Dr_Eggman_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/dr_eggman_2026-10-14/Dr_Eggman_Rules_Attestation.json) → “Thopter Fabricator and Eggman's draw”

## Zones, commander tax and the command zone

### eggman-03: Eggman's placement isn't a cast

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Dr. Eggman, Vision, Spectral Synthezoid, Mechan Assembler, Weapons Manufacturing, Simulacrum Synthesizer

**Ruling.** The card goes from hand directly to the battlefield, so cast triggers don't happen, but every 'enters' trigger does: Mechan Assembler (once per turn), Weapons Manufacturing (nontoken artifact), Simulacrum Synthesizer (artifact with MV 3+). Vision's free spell is a real cast, so cast triggers apply to it.

**Citations**

- Oracle, *Mechan Assembler*: “Whenever another artifact you control enters, create a 2/2 colorless Robot artifact creature token. This ability triggers only once each turn.”
- Oracle, *Vision, Spectral Synthezoid*: “Once during each of your turns, you may cast a noncreature or Robot spell from your hand without paying its mana cost.”
- [CR 601.2](#cr-6012), [CR 603.6a](#cr-6036a)
- Source (re-verified): [`Dr_Eggman_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/dr_eggman_2026-10-14/Dr_Eggman_Rules_Attestation.json) → “Eggman placement is not casting”
- Source (re-verified): [`Dr_Eggman_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/dr_eggman_2026-10-14/Dr_Eggman_Rules_Attestation.json) → “Vision, Spectral Synthezoid”

### eggman-07: Blinking Eggman with Y'shtola doesn't cancel the trigger already on the stack

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Dr. Eggman, Y'shtola Rhul

**Ruling.** Triggered abilities exist independently of their source. Blink Eggman in response to his end-step trigger and that trigger still resolves. The returned Eggman is a new object, and it triggers again in the extra end step.

**Citations**

- Scryfall ruling, *Y'shtola Rhul*: “If a permanent with an ability that triggers "at the beginning of the end step" enters during your first end step, that ability won't trigger during that end step, but it will trigger during your second end step.”
- [CR 113.7a](#cr-1137a), [CR 400.7](#cr-4007)
- Source (re-verified): [`Dr_Eggman_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/dr_eggman_2026-10-14/Dr_Eggman_Rules_Attestation.json) → “Y'shtola blinking Eggman”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 101.4

If multiple players would make choices and/or take actions at the same time, the active player (the player whose turn it is) makes any choices required, then the next player in turn order (usually the player seated to the active player’s left) makes any choices required, followed by the remaining nonactive players in turn order. Then the actions happen simultaneously. This rule is often referred to as the “Active Player, Nonactive Player (APNAP) order” rule.

#### CR 113.7a

Once activated or triggered, an ability exists on the stack independently of its source. Destruction or removal of the source after that time won’t affect the ability. Note that some abilities cause a source to do something (for example, “This creature deals 1 damage to any target”) rather than the ability doing anything directly. In these cases, any activated or triggered ability that references information about the source for use while announcing an activated ability or putting a triggered ability on the stack checks that information when the ability is put onto the stack. Otherwise, it …

#### CR 121.2

Cards may only be drawn one at a time. If a player is instructed to draw multiple cards, that player performs that many individual card draws.

#### CR 202.3

The mana value of an object is a number equal to the total amount of mana in its mana cost, regardless of color.

#### CR 400.7

An object that moves from one zone to another becomes a new object with no memory of, or relation to, its previous existence. This rule has the following exceptions.

#### CR 500.8

Some effects can add phases to a turn. They do this by adding the phases directly after the specified phase. If multiple extra phases are created after the same phase, the most recently created phase will occur first.

#### CR 513.1

The end step has no turn-based actions. Once it begins, the active player gets priority. (See rule 117, “Timing and Priority.”)

#### CR 601.2

To cast a spell is to take it from where it is (usually the hand), put it on the stack, and pay its costs, so that it will eventually resolve and have its effect. Casting a spell includes proposal of the spell (rules 601.2a–d) and determination and payment of costs (rules 601.2f–h). To cast a spell, a player follows the steps listed below, in order. A player must be legally allowed to cast the spell to begin this process (see rule 601.3). If a player is unable to comply with the requirements of a step listed below while performing that step, the casting of the spell is illegal; the game …

#### CR 602.2

To activate an ability is to put it onto the stack and pay its costs, so that it will eventually resolve and have its effect. Only an object’s controller (or its owner, if it doesn’t have a controller) can activate its activated ability unless the object specifically says otherwise. Activating an ability follows the steps listed below, in order. If, at any point during the activation of an ability, a player is unable to comply with any of those steps, the activation is illegal; the game returns to the moment before that ability started to be activated (see rule 733, “Handling Illegal …

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 603.6a

Enters-the-battlefield abilities trigger when a permanent enters the battlefield. These are written, “When [this object] enters, . . . “ or “Whenever a [type] enters, . . .” Each time an event puts one or more permanents onto the battlefield, all permanents on the battlefield (including the newcomers) are checked for any enters-the-battlefield triggers that match the event.

#### CR 608.2b

If the spell or ability specifies targets, it checks whether the targets are still legal. A target that’s no longer in the zone it was in when it was targeted is illegal. Other changes to the game state may cause a target to no longer be legal; for example, its characteristics may have changed or an effect may have changed the text of the spell. If the source of an ability has left the zone it was in, its last known information is used during this process. If all its targets, for every instance of the word “target,” are now illegal, the spell or ability doesn’t resolve. It’s removed from the …

#### CR 608.2h

If an effect requires information from the game (such as the number of creatures on the battlefield), the answer is determined only once, when the effect is applied. If the effect requires information from a specific object, including the source of the ability itself, the effect uses the current information of that object if it’s in the public zone it was expected to be in; if it’s no longer in that zone, or if the effect has moved it from a public zone to a hidden zone, the effect uses the object’s last known information. See rule 113.7a. If an ability states that an object does something, …

#### CR 701.55a

“[A player] faces a villainous choice — [option A], or [option B]” means “[A player] chooses [option A] or [option B]. Then all actions in the chosen option are performed.”

#### CR 701.55b

While facing a villainous choice, a player may choose an option that is illegal or impossible. In that case, they perform as much of the action as is possible. This is an exception to rule 608.2d.

#### CR 701.55c

A replacement effect may replace an instruction to face a villainous choice with an instruction to face that choice some number of additional times. In that case, the entire process described in rule 701.55a is performed for that player the appropriate number of times one at a time.

#### CR 701.55d

If more than one player is instructed to face a villainous choice, the entire process described in rule 701.55a is performed for each of those players one at a time in APNAP order. This is an exception to rule 608.2e.

#### CR 707.2

When copying an object, the copy acquires the copiable values of the original object’s characteristics and, for an object on the stack, choices made when casting or activating it (mode, targets, the value of X, whether it was kicked, how it will affect multiple targets, and so on). The copiable values are the values derived from the text printed on the object (that text being name, mana cost, color indicator, card type, subtype, supertype, rules text, power, toughness, and/or loyalty), as modified by other copy effects, by its face-down status, and by “as . . . enters” and “as . . . is turned …

#### CR 707.10

To copy a spell, activated ability, or triggered ability means to put a copy of it onto the stack; a copy of a spell isn’t cast and a copy of an activated ability isn’t activated. A copy of a spell or ability copies both the characteristics of the spell or ability and all decisions made for it, including modes, targets, the value of X, and additional or alternative costs. (See rule 601, “Casting Spells.”) Choices that are normally made on resolution are not copied. If an effect of the copy refers to objects used to pay its costs, it uses the objects used to pay the costs of the original spell …

