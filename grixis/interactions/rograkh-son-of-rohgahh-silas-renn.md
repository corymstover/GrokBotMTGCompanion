---
title: "Rograkh, Son of Rohgahh + Silas Renn, Seeker Adept — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Rograkh, Son of Rohgahh + Silas Renn, Seeker Adept — Interaction Review

> Bot cycle 54 · batch E · reviewed 2026-10-16. Deck: [Rograkh, Son of Rohgahh + Silas Renn, Seeker Adept](../decks/rograkh-son-of-rohgahh-silas-renn.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-15), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/rograkh-son-of-rohgahh-silas-renn.txt`](../../exports/grixis-archidekt/rograkh-son-of-rohgahh-silas-renn.txt) · SHA-256 `74b8f96561a79946547da9f34f1926dc4bab81b65fab224e8edb1b7198cbb57a` |
| Rulings | **8** (7 verified · 0 uncertain · 1 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-15 · rulings 2026-10-15 |
| Source attestations | [`RogSi_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/rogsi_2026-10-15/gate_output/RogSi_Rules_Attestation.json) (Rules attestation (14 items, all PASS) re-verified) · [`RogSi_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/RogSi_Approval_Ready_Verification_2026-10-15.md) (Approval-ready verification) |

## Contents
- [Summary](#summary)
- [Flags and open questions](#flags-and-open-questions)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [Timing and priority](#timing-and-priority)
- [Trigger ordering](#trigger-ordering)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [What the list depends on](#what-the-list-depends-on)
- [Legality and project exceptions](#legality-and-project-exceptions)
- [Rules cited](#rules-cited)

## Summary

RogSi pairs the free red legendary Rograkh (fuel for Mox Amber, Drum, Mantle, Culling, Plunge and Flare, and a commander for free spells) with Silas Renn's artifact recursion. It's a cEDH Breach + Oracle shell. All 7 Spellbook lines and all 14 attestation items are re-verified against the canonical list.

Rules surprises: Samut's split second locks you out too, though triggers still happen; Demonic Counsel finds nothing before delirium, since there are no Demons; Mnemonic Betrayal can't play lands. One flag: your own Vexing Bauble counters your free spells and {0} escapes unless Hexing Squelcher is out.

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [rogsi-04](#rogsi-04-vexing-bauble-counters-your-own-free-spells-rograkh-moxen-led-fierce-guardianship-flare-breach-escapes-for-0) | 🚩 list flag (dependency-risk) | Vexing Bauble counters your own free spells (Rograkh, Moxen, LED, Fierce Guardianship, Flare, Breach escapes for {0}) | Vexing Bauble counters the deck's own free spells and {0} escapes (Rograkh, Moxen, LED, Petal, Fierce Guardianship, Flare, Breach + Grinding Station). Have Hexing Squelcher out, or sacrifice Bauble first. |

## Commander rules text and edge cases

### rogsi-01: Partners: U/B/R identity, separate commander tax, a free red legendary body

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Rograkh, Son of Rohgahh, Silas Renn, Seeker Adept

**Ruling.** Rograkh (mana cost {0}, red) and Silas Renn (blue-black) are both partners. Together they give U/B/R color identity. Each commander's tax is tracked separately, so Rograkh stays free on his first cast and costs {2} after that. Effects that check whether you control a commander are happy with either one, which covers Fierce Guardianship, Deflecting Swat and both modes of Jeska's Will.

**Citations**

- Oracle, *Fierce Guardianship*: “If you control a commander, you may cast this spell without paying its mana cost.”
- Scryfall ruling, *Rograkh, Son of Rohgahh*: “Once the game begins, your two commanders are tracked separately. If you cast one, you won't have to pay an additional {2} the first time you cast the other. A player loses the game after having been dealt 21 damage from any one of them, not from both of them combined.”
- Scryfall ruling, *Rograkh, Son of Rohgahh*: “An effect that checks whether you control your commander is satisfied if you control one or both of your two commanders.”
- [CR 702.124a](#cr-702124a), [CR 903.8](#cr-9038), [CR 204.1](#cr-2041)
- Source (re-verified): [`RogSi_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/rogsi_2026-10-15/gate_output/RogSi_Rules_Attestation.json) → “Partner color identity”
- Source (re-verified): [`RogSi_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/rogsi_2026-10-15/gate_output/RogSi_Rules_Attestation.json) → “Rograkh zero-mana resource engine”

## Combos and engine lines

### rogsi-06: Thassa's Oracle + Consultation / Tainted Pact; Breach lines (LED + Brain Freeze, LED + Wheel, Wheel + Jeska's Will, Petal + Brain Freeze, Grinding Station + Mox Amber)

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Rograkh, Son of Rohgahh, Silas Renn, Seeker Adept, Thassa's Oracle, Demonic Consultation, Tainted Pact, Underworld Breach, Lion's Eye Diamond, Brain Freeze, Wheel of Fortune, Jeska's Will, Lotus Petal, Grinding Station, Mox Amber

**Ruling.** **Oracle wins:** exile your library with Consultation or Tainted Pact (100 distinct names), then Oracle's ETB wins.

**Breach loops:** LED escapes for {0} to fuel repeated Brain Freezes or Wheels. Jeska's Will counts the hand of an opponent who has just wheeled. The Grinding Station + Mox Amber loop mills three per cycle, and Amber taps for red from Rograkh.

All seven Spellbook lines are present. Vexing Bauble stops the {0} escapes (see rogsi-04).

**Citations**

- [CR 702.138a](#cr-702138a), [CR 702.40a](#cr-70240a)
- Commander Spellbook [742-1295](https://commanderspellbook.com/combo/742-1295/) (community-maintained, retrieved 2026-10-16): “Cast Demonic Consultation by paying {B}, naming Thassa's Oracle and thus exiling your library due to you not having a card named Thassa's Oracle in your library.”
- Commander Spellbook [1368-3518-4856](https://commanderspellbook.com/combo/1368-3518-4856/) (community-maintained, retrieved 2026-10-16): “Cast Lion's Eye Diamond from your graveyard for its escape cost by exiling three cards besides Brain Freeze from your graveyard.”
- Commander Spellbook [1368-3698--44](https://commanderspellbook.com/combo/1368-3698--44/) (community-maintained, retrieved 2026-10-16): “Cast the artifact from your graveyard for its escape cost by paying {0} and exiling three cards from your graveyard.”
- Source (re-verified): [`RogSi_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/rogsi_2026-10-15/gate_output/RogSi_Rules_Attestation.json) → “Thassa's Oracle + Demonic Consultation / Tainted Pact”
- Source (re-verified): [`RogSi_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/rogsi_2026-10-15/gate_output/RogSi_Rules_Attestation.json) → “Underworld Breach + Lion's Eye Diamond + Brain Freeze”
- Source (re-verified): [`RogSi_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/rogsi_2026-10-15/gate_output/RogSi_Rules_Attestation.json) → “Underworld Breach + Grinding Station + zero-mana artifact”

## Engines and payoffs

### rogsi-02: Rograkh as a resource: Mox Amber, Springleaf Drum, Paradise Mantle, Culling the Weak, Infernal Plunge, Flare of Duplication

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Rograkh, Son of Rohgahh, Mox Amber, Springleaf Drum, Paradise Mantle, Culling the Weak, Infernal Plunge, Diabolic Intent, Flare of Duplication

**Ruling.** A free legendary red creature fuels several cards:
- **Mox Amber:** taps for red, and blue or black once Silas is out too.
- **Springleaf Drum:** taps him for mana.
- **Paradise Mantle:** makes him tap for any color, though only once he no longer has summoning sickness.
- **Sacrifice outlets:** Culling the Weak ({B}{B}{B}{B}), Infernal Plunge ({R}{R}{R}) and Diabolic Intent all sacrifice him as an additional cost.
- **Flare of Duplication:** a free copy spell if you sacrifice him, since he's a nontoken red creature.

After he's sacrificed he can go to the command zone and come back for {2}.

**Citations**

- Oracle, *Flare of Duplication*: “You may sacrifice a nontoken red creature rather than pay this spell's mana cost.”
- Oracle, *Mox Amber*: “{T}: Add one mana of any color among legendary creatures and planeswalkers you control.”
- Scryfall ruling, *Culling the Weak*: “Players can only respond once this spell has been cast and all its costs have been paid. No one can try to destroy the creature you sacrificed to prevent you from casting this spell.”
- [CR 302.6](#cr-3026), [CR 601.2f](#cr-6012f), [CR 903.9a](#cr-9039a)
- Source (re-verified): [`RogSi_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/rogsi_2026-10-15/gate_output/RogSi_Rules_Attestation.json) → “Rograkh zero-mana resource engine”

## Timing and priority

### rogsi-05: Samut gives your instants and sorceries split second, but triggers still happen

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Rograkh, Son of Rohgahh, Samut, Tyrant of Naktamun, Vexing Bauble, Brain Freeze, Flare of Duplication, Deflecting Swat

**Ruling.** While one of your Samut-boosted spells is on the stack, no one can cast spells or activate non-mana abilities. That includes you: you can't Flare, Swat or Guardianship on top of your own split-second spell. Mana abilities like LED and Lotus Petal still work. Triggers still happen: storm copies Brain Freeze, and Vexing Bauble still counters a free split-second spell. Once the split-second spell leaves the stack, everyone can act again.

**Citations**

- Oracle, *Samut, Tyrant of Naktamun*: “Instant and sorcery spells you control have split second. (As long as a spell with split second is on the stack, players can't cast spells or activate abilities that aren't mana abilities.)”
- Scryfall ruling, *Samut, Tyrant of Naktamun*: “Split second doesn't stop triggered abilities from triggering. If one does, its controller puts it on the stack and chooses targets for it, if any. Those abilities will resolve as normal.”
- Scryfall ruling, *Samut, Tyrant of Naktamun*: “If the resolution of a triggered ability involves casting a spell, that spell can't be cast if a spell with split second is on the stack.”
- [CR 702.61a](#cr-70261a), [CR 702.61b](#cr-70261b)
- Source (re-verified): [`RogSi_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/rogsi_2026-10-15/gate_output/RogSi_Rules_Attestation.json) → “Samut, Tyrant of Naktamun split second”
- Source (re-verified): [`RogSi_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/rogsi_2026-10-15/gate_output/RogSi_Rules_Attestation.json) → “Vexing Bauble + Samut”

## Trigger ordering

### rogsi-07: Final Fortune / Warrior's Oath: the lose trigger is real here

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Rograkh, Son of Rohgahh, Final Fortune, Warrior's Oath

**Ruling.** Both give an extra turn with a delayed "you lose the game" trigger at that turn's end step. This list has no Obeka or Sundial, so the extra turn must win or the trigger has to be answered some other way. If the extra turn is skipped, you don't lose.

**Citations**

- Oracle, *Warrior's Oath*: “Take an extra turn after this one. At the beginning of that turn's end step, you lose the game.”
- Scryfall ruling, *Final Fortune*: “If you end up skipping the extra turn that is gained, you do not lose the game.”
- [CR 500.7](#cr-5007), [CR 603.7](#cr-6037)
- Source (re-verified): [`RogSi_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/rogsi_2026-10-15/gate_output/RogSi_Rules_Attestation.json) → “Final Fortune / Warrior's Oath”

## Zones, commander tax and the command zone

### rogsi-03: Silas Renn: cast one artifact card from your graveyard this turn, at normal timing

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Silas Renn, Seeker Adept, Lion's Eye Diamond, Grinding Station, Mox Amber

**Ruling.** When Silas deals combat damage to a player, his trigger targets an artifact card in your graveyard, and you may cast it that turn. That holds even if Silas has left the battlefield. You pay its costs, and alternative costs are allowed. The trigger doesn't change timing, so a non-flash artifact still needs your main phase with an empty stack. Once cast, the card is a new object, so you can't cast it twice. It doesn't work on lands.

**Citations**

- Oracle, *Silas Renn, Seeker Adept*: “Whenever Silas Renn deals combat damage to a player, choose target artifact card in your graveyard. You may cast that card this turn.”
- Scryfall ruling, *Silas Renn, Seeker Adept*: “Silas Renn doesn't change when you can cast the target artifact card. For example, if you target an artifact card without flash, you can cast it only during your main phase when the stack is empty.”
- Scryfall ruling, *Silas Renn, Seeker Adept*: “Casting the card causes it to leave your graveyard and become a new object. You can't cast it multiple times.”
- Scryfall ruling, *Silas Renn, Seeker Adept*: “You may cast that card this turn even if Silas Renn leaves the battlefield.”
- [CR 601.2](#cr-6012), [CR 400.7](#cr-4007)
- Source (re-verified): [`RogSi_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/rogsi_2026-10-15/gate_output/RogSi_Rules_Attestation.json) → “Silas Renn artifact recursion”

## What the list depends on

### rogsi-04: Vexing Bauble counters your own free spells (Rograkh, Moxen, LED, Fierce Guardianship, Flare, Breach escapes for {0})

**Status:** 🚩 list flag · **Evidence:** fact · **Cards:** Rograkh, Son of Rohgahh, Vexing Bauble, Hexing Squelcher, Fierce Guardianship, Deflecting Swat, Flare of Duplication, Lion's Eye Diamond, Lotus Petal, Mox Amber, Underworld Breach

**Ruling.** Vexing Bauble counters any spell cast with no mana spent, including yours. That covers:
- the first Rograkh cast;
- {0} artifacts (LED, Lotus Petal, Mox Amber);
- Fierce Guardianship, Deflecting Swat and Flare of Duplication cast for free;
- {0} Breach escapes, such as the Mox Amber + Grinding Station loop.

Paying any mana, like a Rograkh recast with {2} of tax, or a kicker, gets past it. Hexing Squelcher makes your spells uncounterable, so Bauble still triggers but does nothing. Otherwise, sacrifice Bauble ({1}, draw) before going off.

**List flag (dependency-risk).** Vexing Bauble counters the deck's own free spells and {0} escapes (Rograkh, Moxen, LED, Petal, Fierce Guardianship, Flare, Breach + Grinding Station). Have Hexing Squelcher out, or sacrifice Bauble first.

**Citations**

- Oracle, *Vexing Bauble*: “Whenever a player casts a spell, if no mana was spent to cast it, counter that spell.”
- Oracle, *Hexing Squelcher*: “Spells you control can't be countered.”
- Scryfall ruling, *Vexing Bauble*: “If a spell is cast with an alternative cost that includes mana (such as flashback), Vexing Bauble's first ability won't trigger and won't counter that spell. Similarly, if a spell is cast without paying its mana cost, but the player did pay mana for additional costs such as from kicker or from Thorn of Amethyst, Vexing Bauble's first ability won't trigger and won't counter that spell.”
- Scryfall ruling, *Hexing Squelcher*: “A spell or ability that counters spells can still target any spell that can't be countered. When that spell or ability resolves, the spell that can't be countered won't be countered, but any additional effects of the countering spell or ability will still happen.”
- [CR 603.4](#cr-6034), [CR 702.138a](#cr-702138a)
- Source (re-verified): [`RogSi_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/rogsi_2026-10-15/gate_output/RogSi_Rules_Attestation.json) → “Vexing Bauble symmetry”
- Source (re-verified): [`RogSi_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/rogsi_2026-10-15/gate_output/RogSi_Rules_Attestation.json) → “Vexing Bauble + Hexing Squelcher”

## Legality and project exceptions

### rogsi-08: Demonic Counsel needs delirium; Mnemonic Betrayal casts but never plays lands; Undercity Sewers is fetchable

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Rograkh, Son of Rohgahh, Demonic Counsel, Mnemonic Betrayal, Undercity Sewers

**Ruling.** **Demonic Counsel:** without delirium it finds only a Demon, and the canonical list has none. With four or more card types in your graveyard, it finds any card.

**Mnemonic Betrayal:** lets you cast spells from opponents' exiled graveyards this turn, with any mana, at normal timing. You can't play their lands. Cards you don't cast go back at the next end step, and a permanent you cast stays.

**Undercity Sewers:** an Island Swamp, so your fetchlands can find it.

**Citations**

- Oracle, *Demonic Counsel*: “Delirium — If there are four or more card types among cards in your graveyard, instead search your library for any card, put it into your hand, then shuffle.”
- Scryfall ruling, *Mnemonic Betrayal*: “You can’t play land cards exiled this way.”
- Scryfall ruling, *Mnemonic Betrayal*: “Only the cards that remain in exile are returned to their owners’ graveyards. For example, a permanent spell cast this way will remain on the battlefield.”
- [CR 207.2c](#cr-2072c), [CR 305.6](#cr-3056)
- Source (re-verified): [`RogSi_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/rogsi_2026-10-15/gate_output/RogSi_Rules_Attestation.json) → “Demonic Counsel”
- Source (re-verified): [`RogSi_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/rogsi_2026-10-15/gate_output/RogSi_Rules_Attestation.json) → “Mnemonic Betrayal”
- Source (re-verified): [`RogSi_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/rogsi_2026-10-15/gate_output/RogSi_Rules_Attestation.json) → “Undercity Sewers”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 204.1

The color indicator is printed to the left of the type line directly below the illustration. It consists of a circular symbol filled in with one or more colors. A color indicator is usually found on nonland cards without a mana cost.

#### CR 207.2c

An ability word appears in italics at the beginning of some abilities. Ability words are similar to keywords in that they tie together cards that have similar functionality, but they have no special rules meaning and no individual entries in the Comprehensive Rules. The ability words are adamant, addendum, alliance, battalion, bloodrush, celebration, channel, chroma, cohort, constellation, converge, council’s dilemma, coven, delirium, descend 4, descend 8, disappear, domain, eerie, eminence, enrage, fateful hour, fathomless descent, ferocious, flurry, formidable, grandeur, hellbent, heroic, …

#### CR 302.6

A creature’s activated ability with the tap symbol or the untap symbol in its activation cost can’t be activated unless the creature has been under its controller’s control continuously since their most recent turn began. A creature can’t attack unless it has been under its controller’s control continuously since their most recent turn began. This rule is informally called the “summoning sickness” rule.

#### CR 305.6

The basic land types are Plains, Island, Swamp, Mountain, and Forest. If an object uses the words “basic land type,” it’s referring to one of these subtypes. An object with the land card type and a basic land type has the intrinsic ability “{T}: Add [mana symbol],” even if the text box doesn’t actually contain that text or the object has no text box. For Plains, [mana symbol] is {W}; for Islands, {U}; for Swamps, {B}; for Mountains, {R}; and for Forests, {G}. See rule 107.4a. See also rule 605, “Mana Abilities.”

#### CR 400.7

An object that moves from one zone to another becomes a new object with no memory of, or relation to, its previous existence. This rule has the following exceptions.

#### CR 500.7

Some effects can give a player extra turns. They do this by adding the turns directly after the specified turn. If a player is given multiple extra turns, the extra turns are added one at a time. If multiple players are given extra turns, the extra turns are added one at a time, in APNAP order (see rule 101.4). The most recently created turn will be taken first.

#### CR 601.2

To cast a spell is to take it from where it is (usually the hand), put it on the stack, and pay its costs, so that it will eventually resolve and have its effect. Casting a spell includes proposal of the spell (rules 601.2a–d) and determination and payment of costs (rules 601.2f–h). To cast a spell, a player follows the steps listed below, in order. A player must be legally allowed to cast the spell to begin this process (see rule 601.3). If a player is unable to comply with the requirements of a step listed below while performing that step, the casting of the spell is illegal; the game …

#### CR 601.2f

The player determines the total cost of the spell. Usually this is just the mana cost. Some spells have additional or alternative costs. Some effects may increase or reduce the cost to pay, or may provide other alternative costs. Costs may include paying mana, tapping permanents, sacrificing permanents, discarding cards, and so on. The total cost is the mana cost or alternative cost (as determined in rule 601.2b), plus all additional costs and cost increases, and minus all cost reductions. If multiple cost reductions apply, the player may apply them in any order. If the mana component of the …

#### CR 603.4

A triggered ability may read “When/Whenever/At [trigger event], if [condition], [effect].” When the trigger event occurs, the ability checks whether the stated condition is true. The ability triggers only if it is; otherwise it does nothing. If the ability triggers, it checks the stated condition again as it resolves. If the condition isn’t true at that time, the ability is removed from the stack and does nothing. Note that this mirrors the check for legal targets. This rule is referred to as the “intervening ‘if’ clause” rule. (The word “if” has only its normal English meaning anywhere else …

#### CR 603.7

An effect may create a delayed triggered ability that can do something at a later time. A delayed triggered ability will contain “when,” “whenever,” or “at,” although that word won’t usually begin the ability.

#### CR 702.40a

Storm is a triggered ability that functions on the stack. “Storm” means “When you cast this spell, copy it for each other spell that was cast before it this turn. If the spell has any targets, you may choose new targets for any of the copies.”

#### CR 702.61a

Split second is a static ability that functions only while the spell with split second is on the stack. “Split second” means “As long as this spell is on the stack, players can’t cast other spells or activate abilities that aren’t mana abilities.”

#### CR 702.61b

Players may activate mana abilities and take special actions while a spell with split second is on the stack. Triggered abilities trigger and are put on the stack as normal while a spell with split second is on the stack.

#### CR 702.124a

Partner abilities are keyword abilities that modify the rules for deck construction in the Commander variant (see rule 903), and they function before the game begins. Each partner ability allows you to designate two legendary cards as your commander rather than one. Each partner ability has its own requirements for those two commanders. The partner abilities are: partner, partner—[text], partner with [name], choose a Background, and Doctor’s companion.

#### CR 702.138a

Escape represents a static ability that functions while the card with escape is in a player’s graveyard. “Escape [cost]” means “You may cast this card from your graveyard by paying [cost] rather than paying its mana cost.” Casting a spell using its escape ability follows the rules for paying alternative costs in rules 601.2b and 601.2f–h.

#### CR 903.8

A player may cast a commander they own from the command zone. A commander cast from the command zone costs an additional {2} for each previous time the player casting it has cast it from the command zone that game. This additional cost is informally known as the “commander tax.”

#### CR 903.9a

If a commander is in a graveyard or in exile and that object was put into that zone since the last time state-based actions were checked, its owner may put it into the command zone. This is a state-based action. See rule 704.

