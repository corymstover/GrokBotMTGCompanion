---
title: "Fire Lord Azula — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Fire Lord Azula — Interaction Review

> Bot cycle 48 · batch B · reviewed 2026-10-16. Deck: [Fire Lord Azula](../decks/fire-lord-azula.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-15), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Current list | [`exports/grixis-archidekt/fire-lord-azula.txt`](../../exports/grixis-archidekt/fire-lord-azula.txt) · SHA-256 `e52f1cbbf1b17f3e3cef0ef9d466e93bdf5e85bc4d32ac5f2856b4bd2b36fda4` |
| Rulings | **11** (11 verified · 0 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-15 · rulings 2026-10-15 |
| Source attestations | [`Fire_Lord_Azula_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/fire_lord_azula_2026-10-14/Fire_Lord_Azula_Rules_Attestation.json) (15 interactions, all PASS (Samut and Final Fortune items refer to cards not in the current list)) |

## Contents
- [Summary](#summary)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Key card-pair interactions](#key-card-pair-interactions)
- [Timing and priority](#timing-and-priority)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [What the list depends on](#what-the-list-depends-on)
- [Rules cited](#rules-cited)

## Summary

Fire Lord Azula copies every spell you cast while she's attacking. The list is a cEDH-style turbo shell with Narset's Reversal, Underworld Breach and Thassa's Oracle lines. This review re-verifies the deck's rules attestation and confirms seven combo lines against cached Commander Spellbook steps.

Rules surprise: copying a sorcery (Beseech the Mirror, Wheel, Jeska's Will) with Azula needs a flash enabler during combat. The list has five. No list errors.

## Commander rules text and edge cases

### azula-01: The copy resolves first, even if the original is countered

**Status:** ✅ verified · **Cards:** Fire Lord Azula

**Ruling.** Azula's trigger goes on the stack above the spell that caused it. The copy is created when the trigger resolves, so the copy resolves before the original. The trigger and copy still resolve if the original is countered first. The copy isn't cast: it doesn't add to storm or trigger cast abilities.

**Citations**

- Oracle, *Fire Lord Azula*: “Whenever you cast a spell while Fire Lord Azula is attacking, copy that spell. You may choose new targets for the copy.”
- Scryfall ruling, *Fire Lord Azula*: “Azula's ability and the copy it creates both resolve before the spell that caused the ability to trigger. They resolve even if the spell is countered before the copy is created.”
- Scryfall ruling, *Fire Lord Azula*: “The copy is created on the stack, so it's not "cast." Abilities that trigger when a player casts a spell won't trigger.”
- [CR 707.10](#cr-70710), [CR 603.3](#cr-6033)
- Source (re-verified): [`Fire_Lord_Azula_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/fire_lord_azula_2026-10-14/Fire_Lord_Azula_Rules_Attestation.json) → “Fire Lord Azula copy timing”

### azula-03: Additional costs are paid once, but the copy counts them as paid

**Status:** ✅ verified · **Cards:** Fire Lord Azula, Big Score, Demand Answers, Redirect Lightning

**Ruling.** You can't pay additional costs for the copy. Effects that depend on an additional cost paid for the original are copied as if it were paid. Big Score (discard one): the original and the copy together draw four and make four Treasures. Demand Answers (sacrifice or discard once): four cards. Redirect Lightning's 5 life or {2} is paid once.

**Citations**

- Oracle, *Big Score*: “As an additional cost to cast this spell, discard a card.”
- Scryfall ruling, *Fire Lord Azula*: “You can't choose to pay any additional costs for a copied spell. However, effects based on any additional costs that were paid for the original spell are copied as though those same costs were paid for the copy too.”
- [CR 707.10](#cr-70710), [CR 601.2f](#cr-6012f)
- Source (re-verified): [`Fire_Lord_Azula_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/fire_lord_azula_2026-10-14/Fire_Lord_Azula_Rules_Attestation.json) → “Additional costs on copied spells”
- Source (re-verified): [`Fire_Lord_Azula_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/fire_lord_azula_2026-10-14/Fire_Lord_Azula_Rules_Attestation.json) → “Big Score with attacking Azula”
- Source (re-verified): [`Fire_Lord_Azula_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/fire_lord_azula_2026-10-14/Fire_Lord_Azula_Rules_Attestation.json) → “Demand Answers with attacking Azula”

## Combos and engine lines

### azula-05: Azula + Narset's Reversal + Frantic Search

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Fire Lord Azula, Narset's Reversal, Frantic Search

**Ruling.** Attack with Azula (firebending {R}{R}). Cast Frantic Search; Azula's copy loots and untaps three lands. Cast Narset's Reversal on the original Frantic Search; Azula copies the Reversal, targeting the original Reversal. The copied Reversal copies the original Reversal and returns it to your hand, and the chain copies Frantic Search again and returns it to your hand. Spellbook rates the result as infinite loot and draw triggers and near-infinite storm, with three lands that make {U}{U}{U}.

**Citations**

- Oracle, *Narset's Reversal*: “Copy target instant or sorcery spell, then return it to its owner's hand. You may choose new targets for the copy.”
- Scryfall ruling, *Narset's Reversal*: “If a copy of a spell is returned to its owner’s hand, it’s moved there, then it will cease to exist as a state-based action.”
- [CR 707.10](#cr-70710), [CR 702.40a](#cr-70240a)
- Commander Spellbook [11-2196-7089](https://commanderspellbook.com/combo/11-2196-7089/) (community-maintained, retrieved 2026-10-16): “You control up to three lands that can tap to produce at least {U}{U}{U}.”
- Commander Spellbook [11-2196-7089](https://commanderspellbook.com/combo/11-2196-7089/) (community-maintained, retrieved 2026-10-16): “Cast Narset's Reversal by paying {U}{U}, targeting the original Frantic Search spell.”
- Commander Spellbook [11-2196-7089](https://commanderspellbook.com/combo/11-2196-7089/) (community-maintained, retrieved 2026-10-16): “Fire Lord Azula's second ability triggers, copying Narset's Reversal, targeting the original Narset's Reversal.”
- Source (re-verified): [`Fire_Lord_Azula_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/fire_lord_azula_2026-10-14/Fire_Lord_Azula_Rules_Attestation.json) → “Azula + Narset's Reversal + Frantic Search loop”

### azula-06: Azula + Underworld Breach + Frantic Search

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Fire Lord Azula, Underworld Breach, Frantic Search

**Ruling.** While Azula attacks with Breach out, each Frantic Search (from hand or escaped) is copied. Two Frantic Search resolutions untap six lands for the {2}{U} cost and loot four cards, refilling the graveyard. Prerequisites: three lands that make {1}{U}, and three other cards in the graveyard to escape Frantic Search.

**Citations**

- Scryfall ruling, *Frantic Search*: “You choose which lands to untap as the spell resolves. They aren't targeted, and they don't have to be lands that you control.”
- [CR 702.138a](#cr-702138a)
- Commander Spellbook [1368-2196-7089](https://commanderspellbook.com/combo/1368-2196-7089/) (community-maintained, retrieved 2026-10-16): “There are at least three other cards in your graveyard if Frantic Search is in your graveyard.”
- Commander Spellbook [1368-2196-7089](https://commanderspellbook.com/combo/1368-2196-7089/) (community-maintained, retrieved 2026-10-16): “Resolve the copy of Frantic Search, causing you to loot twice and untap up to three lands.”
- Source (re-verified): [`Fire_Lord_Azula_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/fire_lord_azula_2026-10-14/Fire_Lord_Azula_Rules_Attestation.json) → “Azula + Underworld Breach + Frantic Search”

### azula-07: Breach lines without Azula

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Fire Lord Azula, Underworld Breach, Lion's Eye Diamond, Brain Freeze, Grinding Station, Wheel of Fortune, Jeska's Will

**Ruling.** Breach + LED + Brain Freeze needs six other cards in hand and/or graveyard to start. Breach + Grinding Station needs a mana value 0 artifact: escape it for {0} plus three cards, and its entering untaps the Station. Breach + Wheel of Fortune + Jeska's Will (or LED) needs an opponent with six cards in hand for Jeska's Will mana. Wheel and Jeska's Will are sorceries, cast in a main phase.

**Citations**

- [CR 702.138a](#cr-702138a)
- Commander Spellbook [1368-3518-4856](https://commanderspellbook.com/combo/1368-3518-4856/) (community-maintained, retrieved 2026-10-16): “You have at least six other cards in hand and/or graveyard.”
- Commander Spellbook [1368-3698--44](https://commanderspellbook.com/combo/1368-3698--44/) (community-maintained, retrieved 2026-10-16): “Cast the artifact from your graveyard for its escape cost by paying {0} and exiling three cards from your graveyard.”
- Commander Spellbook [1368-1878-2706](https://commanderspellbook.com/combo/1368-1878-2706/) (community-maintained, retrieved 2026-10-16): “An opponent has at least six cards in hand.”
- Source (re-verified): [`Fire_Lord_Azula_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/fire_lord_azula_2026-10-14/Fire_Lord_Azula_Rules_Attestation.json) → “Underworld Breach + Lion's Eye Diamond + Brain Freeze”

### azula-08: Thassa's Oracle + Consultation / Tainted Pact

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Fire Lord Azula, Thassa's Oracle, Demonic Consultation, Tainted Pact

**Ruling.** Same compact wins as other Grixis cEDH lists. The list has 100 distinct names, so Tainted Pact can't stop early on a duplicate. Under an attacking Azula, a copied Consultation or Pact resolves first. Name the Oracle and make sure the Oracle trigger resolves after the library is gone.

**Citations**

- [CR 121.4](#cr-1214)
- Commander Spellbook [742-1295](https://commanderspellbook.com/combo/742-1295/) (community-maintained, retrieved 2026-10-16): “Cast Demonic Consultation by paying {B}, naming Thassa's Oracle and thus exiling your library due to you not having a card named Thassa's Oracle in your library.”
- Commander Spellbook [1295-3093](https://commanderspellbook.com/combo/1295-3093/) (community-maintained, retrieved 2026-10-16): “No two cards in library share a name.”
- Source (re-verified): [`Fire_Lord_Azula_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/fire_lord_azula_2026-10-14/Fire_Lord_Azula_Rules_Attestation.json) → “Thassa's Oracle + Demonic Consultation”
- Source (re-verified): [`Fire_Lord_Azula_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/fire_lord_azula_2026-10-14/Fire_Lord_Azula_Rules_Attestation.json) → “Thassa's Oracle + Tainted Pact”

## Key card-pair interactions

### azula-04: A bargained Beseech the Mirror copy is bargained too

**Status:** ✅ verified · **Cards:** Fire Lord Azula, Beseech the Mirror

**Ruling.** Bargain is an optional additional cost. A copy of a bargained spell is bargained, so one sacrifice gives two tutors, and each can cast a mana value 4 or less card free. Beseech is a sorcery, so it needs flash timing while Azula attacks (see azula-02).

**Citations**

- Scryfall ruling, *Beseech the Mirror*: “If you copy a bargained spell, the copy is also bargained. If a card or token enters the battlefield as a copy of a permanent that's already on the battlefield, the new permanent isn't bargained, even if the original was.”
- [CR 702.166a](#cr-702166a), [CR 707.10](#cr-70710)
- Source (re-verified): [`Fire_Lord_Azula_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/fire_lord_azula_2026-10-14/Fire_Lord_Azula_Rules_Attestation.json) → “Beseech the Mirror bargain copy”

### azula-09: Arena of Glory gives Azula haste

**Status:** ✅ verified · **Cards:** Fire Lord Azula, Arena of Glory

**Ruling.** Arena of Glory's exert ability makes {R}{R}. Any of that mana spent on a creature spell gives it haste, so Azula can attack the turn she's cast. It enters tapped unless you already control a Mountain.

**Citations**

- Oracle, *Arena of Glory*: “{R}, {T}, Exert this land: Add {R}{R}. If any of that mana is spent on a creature spell, it gains haste until end of turn.”
- Scryfall ruling, *Arena of Glory*: “You must already control a Mountain as Arena of Glory enters the battlefield for it to enter untapped.”
- [CR 702.10b](#cr-70210b), [CR 701.43a](#cr-70143a)
- Source (re-verified): [`Fire_Lord_Azula_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/fire_lord_azula_2026-10-14/Fire_Lord_Azula_Rules_Attestation.json) → “Arena of Glory haste on Azula”

## Timing and priority

### azula-02: 'While attacking' means during combat: sorceries need a flash enabler

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Fire Lord Azula, Beseech the Mirror, Borne Upon a Wind, Valley Floodcaller, Quicken, Emergence Zone

**Ruling.** Azula is only attacking from declare attackers until combat ends. You can normally only cast instants and flash spells then. To copy a sorcery (Beseech the Mirror, Wheel of Fortune, Jeska's Will) or a non-flash creature, cast Borne Upon a Wind, Quicken (next sorcery only), or use Emergence Zone or Valley Floodcaller (noncreature spells) first. Firebending's {R}{R} lasts until end of combat, so it can pay for those spells.

**Citations**

- Oracle, *Fire Lord Azula*: “Firebending 2 (Whenever this creature attacks, add {R}{R}. This mana lasts until end of combat.)”
- Oracle, *Quicken*: “The next sorcery spell you cast this turn can be cast as though it had flash.”
- Scryfall ruling, *Fire Lord Azula*: “Mana from firebending abilities isn't lost until you leave combat and go to your second main phase. It can be used at any time during combat, even after combat damage has been dealt.”
- [CR 506.1](#cr-5061), [CR 307.1](#cr-3071), [CR 508.1](#cr-5081)

## Zones, commander tax and the command zone

### azula-10: Copied permanent spells become tokens, but aren't 'created'

**Status:** ✅ verified · **Cards:** Fire Lord Azula

**Ruling.** A copy of a permanent spell becomes a token as it resolves. It isn't 'created', so 'whenever you create a token' effects don't see it. A copy of a legendary permanent hits the legend rule.

**Citations**

- Scryfall ruling, *Fire Lord Azula*: “A resolving copy of a permanent spell becomes a token. That token isn't "created" and won't interact with abilities that care about tokens being created.”
- [CR 707.10f](#cr-70710f), [CR 704.5j](#cr-7045j)
- Source (re-verified): [`Fire_Lord_Azula_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/fire_lord_azula_2026-10-14/Fire_Lord_Azula_Rules_Attestation.json) → “Permanent spell copies”

## What the list depends on

### azula-11: Mox Opal metalcraft density

**Status:** ✅ verified · **Evidence:** derived_metric · **Cards:** Fire Lord Azula, Mox Opal

**Ruling.** Mox Opal needs three artifacts. Counting Oracle type lines in the current list, there are 15 artifact cards including Opal, matching the source, plus Harnfel, Horn of Bounty, the artifact back face of Birgi. That's enough to turn on metalcraft regularly, but not reliably early.

**Citations**

- Oracle, *Mox Opal*: “Metalcraft — {T}: Add one mana of any color. Activate only if you control three or more artifacts.”
- [CR 207.2c](#cr-2072c)
- Source (re-verified): [`Fire_Lord_Azula_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/fire_lord_azula_2026-10-14/Fire_Lord_Azula_Rules_Attestation.json) → “Mox Opal metalcraft structural support”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 121.4

A player who attempts to draw a card from a library with no cards in it loses the game the next time a player would receive priority. (This is a state-based action. See rule 704.)

#### CR 207.2c

An ability word appears in italics at the beginning of some abilities. Ability words are similar to keywords in that they tie together cards that have similar functionality, but they have no special rules meaning and no individual entries in the Comprehensive Rules. The ability words are adamant, addendum, alliance, battalion, bloodrush, celebration, channel, chroma, cohort, constellation, converge, council’s dilemma, coven, delirium, descend 4, descend 8, disappear, domain, eerie, eminence, enrage, fateful hour, fathomless descent, ferocious, flurry, formidable, grandeur, hellbent, heroic, …

#### CR 307.1

A player who has priority may cast a sorcery card from their hand during a main phase of their turn when the stack is empty. Casting a sorcery as a spell uses the stack. (See rule 601, “Casting Spells.”)

#### CR 506.1

The combat phase has five steps, which proceed in order: beginning of combat, declare attackers, declare blockers, combat damage, and end of combat. The declare blockers and combat damage steps are skipped if no creatures are declared as attackers or put onto the battlefield attacking (see rule 508.8). There are two combat damage steps if any attacking or blocking creature has first strike (see rule 702.7) or double strike (see rule 702.4).

#### CR 508.1

First, the active player declares attackers. This turn-based action doesn’t use the stack. To declare attackers, the active player follows the steps below, in order. If at any point during the declaration of attackers, the active player is unable to comply with any of the steps listed below, the declaration is illegal; the game returns to the moment before the declaration (see rule 733, “Handling Illegal Actions”).

#### CR 601.2f

The player determines the total cost of the spell. Usually this is just the mana cost. Some spells have additional or alternative costs. Some effects may increase or reduce the cost to pay, or may provide other alternative costs. Costs may include paying mana, tapping permanents, sacrificing permanents, discarding cards, and so on. The total cost is the mana cost or alternative cost (as determined in rule 601.2b), plus all additional costs and cost increases, and minus all cost reductions. If multiple cost reductions apply, the player may apply them in any order. If the mana component of the …

#### CR 603.3

Once an ability has triggered, its controller puts it on the stack as an object that’s not a card the next time a player would receive priority. See rule 117, “Timing and Priority.” The ability becomes the topmost object on the stack. It has the text of the ability that created it, and no other characteristics. It remains on the stack until it’s countered, it resolves, a rule causes it to be removed from the stack, or an effect moves it elsewhere.

#### CR 701.43a

To exert a permanent, you choose to have it not untap during your next untap step.

#### CR 702.10b

If a creature has haste, it can attack even if it hasn’t been controlled by its controller continuously since their most recent turn began. (See rule 302.6.)

#### CR 702.40a

Storm is a triggered ability that functions on the stack. “Storm” means “When you cast this spell, copy it for each other spell that was cast before it this turn. If the spell has any targets, you may choose new targets for any of the copies.”

#### CR 702.138a

Escape represents a static ability that functions while the card with escape is in a player’s graveyard. “Escape [cost]” means “You may cast this card from your graveyard by paying [cost] rather than paying its mana cost.” Casting a spell using its escape ability follows the rules for paying alternative costs in rules 601.2b and 601.2f–h.

#### CR 702.166a

Bargain is a static ability that functions while the spell with bargain is on the stack. “Bargain” means “As an additional cost to cast this spell, you may sacrifice an artifact, enchantment, or token.” Paying a spell’s bargain cost follows the rules for paying additional costs in rules 601.2b and 601.2f–h.

#### CR 704.5j

If two or more legendary permanents with the same name are controlled by the same player, that player chooses one of them, and the rest are put into their owners’ graveyards. This is called the “legend rule.”

#### CR 707.10

To copy a spell, activated ability, or triggered ability means to put a copy of it onto the stack; a copy of a spell isn’t cast and a copy of an activated ability isn’t activated. A copy of a spell or ability copies both the characteristics of the spell or ability and all decisions made for it, including modes, targets, the value of X, and additional or alternative costs. (See rule 601, “Casting Spells.”) Choices that are normally made on resolution are not copied. If an effect of the copy refers to objects used to pay its costs, it uses the objects used to pay the costs of the original spell …

#### CR 707.10f

Some effects copy a permanent spell. As that copy resolves, it ceases being a copy of a spell and becomes a token permanent. (See rule 608.3f.)

