---
title: "Kess, Dissident Mage — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Kess, Dissident Mage — Interaction Review

> Bot cycle 49 · batch C · reviewed 2026-10-16. Deck: [Kess, Dissident Mage](../decks/kess-dissident-mage.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-15), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/kess-dissident-mage.txt`](../../exports/grixis-archidekt/kess-dissident-mage.txt) · SHA-256 `94dee35afe9fdb9871ee84abc0ac616ab23e133198d7d5d0ddba090b6942f2bd` |
| Rulings | **9** (9 verified · 0 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-15 · rulings 2026-10-15 |
| Source attestations | [`Kess_Dissident_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kess_dissident_mage_2026-10-14/Kess_Dissident_Mage_Rules_Attestation.json) (13 interactions, all PASS) |

## Contents
- [Summary](#summary)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [Timing and priority](#timing-and-priority)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [What the list depends on](#what-the-list-depends-on)
- [Rules cited](#rules-cited)

## Summary

Kess, Dissident Mage lets you cast one instant or sorcery from your graveyard each of your turns, which turns every tutor into two. This review re-verifies all 13 attestation items, including the deterministic Gifts Ungiven pile (all six splits checked). Six Spellbook lines are confirmed.

Rules surprises: a Kitten-blinked Kess gets a fresh use; flashback doesn't use up Kess; Mox Diamond doesn't work as the Grinding Station + Breach artifact. No list errors.

## Commander rules text and edge cases

### kess-01: One graveyard cast per your turn, at normal timing

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Kess, Dissident Mage

**Ruling.** Kess lets you cast one instant or sorcery from your graveyard during each of your turns, never on an opponent's turn. You pay its costs (alternative costs allowed) and follow its normal timing. It's exiled instead of going to the graveyard. Flashback and other permissions are separate and don't use up Kess.

**Citations**

- Oracle, *Kess, Dissident Mage*: “Once during each of your turns, you may cast an instant or sorcery spell from your graveyard. If a spell cast this way would be put into your graveyard, exile it instead.”
- Scryfall ruling, *Kess, Dissident Mage*: “You must follow the normal timing permissions and restrictions of the card you cast from your graveyard.”
- Scryfall ruling, *Kess, Dissident Mage*: “If you cast a card from your graveyard using another permission (such as that of flashback), Kess's effect doesn't apply. You can cast another instant or sorcery card from your graveyard.”
- [CR 601.2](#cr-6012), [CR 614.1a](#cr-6141a)
- Source (re-verified): [`Kess_Dissident_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kess_dissident_mage_2026-10-14/Kess_Dissident_Mage_Rules_Attestation.json) → “Kess graveyard-cast permission and timing”
- Source (re-verified): [`Kess_Dissident_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kess_dissident_mage_2026-10-14/Kess_Dissident_Mage_Rules_Attestation.json) → “Snapcaster Mage complement to Kess”

## Combos and engine lines

### kess-03: Kess turns one tutor into both halves of the Oracle combo

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Kess, Dissident Mage, Thassa's Oracle, Demonic Consultation, Tainted Pact

**Ruling.** Cast Consultation or Pact from hand to find Thassa's Oracle. Then cast Oracle, and with its trigger on the stack, cast the same spell again from the graveyard through Kess to exile your library. Consultation's second cast names a card that isn't in the deck. Pact works because all 100 names are distinct.

**Citations**

- [CR 121.4](#cr-1214), [CR 603.3](#cr-6033)
- Commander Spellbook [742-1295](https://commanderspellbook.com/combo/742-1295/) (community-maintained, retrieved 2026-10-16): “Cast Demonic Consultation by paying {B}, naming Thassa's Oracle and thus exiling your library due to you not having a card named Thassa's Oracle in your library.”
- Commander Spellbook [1295-3093](https://commanderspellbook.com/combo/1295-3093/) (community-maintained, retrieved 2026-10-16): “No two cards in library share a name.”
- Source (re-verified): [`Kess_Dissident_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kess_dissident_mage_2026-10-14/Kess_Dissident_Mage_Rules_Attestation.json) → “Kess plus Demonic Consultation plus Thassa's Oracle”
- Source (re-verified): [`Kess_Dissident_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kess_dissident_mage_2026-10-14/Kess_Dissident_Mage_Rules_Attestation.json) → “Kess plus Tainted Pact plus Thassa's Oracle”

### kess-04: Intuition and Gifts Ungiven piles are deterministic with Kess

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Kess, Dissident Mage, Intuition, Gifts Ungiven, Thassa's Oracle, Reanimate, Demonic Consultation, Tainted Pact

**Ruling.** Cast from hand with Kess's use still available. Intuition for Oracle / Reanimate / Consultation, or Gifts for Oracle / Reanimate / Consultation / Pact, wins whatever the opponent picks. I checked all six Gifts splits: either Oracle is in hand with an exile spell in hand or graveyard (Kess), or Reanimate (from hand or via Kess) returns Oracle with an exile spell left. Reanimate costs 2 life (Oracle's mana value). This fails if Kess's use went on casting Gifts itself.

**Citations**

- Oracle, *Gifts Ungiven*: “Target opponent chooses two of those cards. Put the chosen cards into your graveyard and the rest into your hand.”
- Oracle, *Reanimate*: “Put target creature card from a graveyard onto the battlefield under your control. You lose life equal to that card's mana value.”
- [CR 601.2](#cr-6012), [CR 603.3](#cr-6033)
- Source (re-verified): [`Kess_Dissident_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kess_dissident_mage_2026-10-14/Kess_Dissident_Mage_Rules_Attestation.json) → “Intuition deterministic Kess pile”
- Source (re-verified): [`Kess_Dissident_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kess_dissident_mage_2026-10-14/Kess_Dissident_Mage_Rules_Attestation.json) → “Gifts Ungiven deterministic Kess pile”

### kess-06: Underworld Breach + Grinding Station with a zero-cost artifact

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Kess, Dissident Mage, Underworld Breach, Grinding Station, Lotus Petal, Mox Opal, Chrome Mox

**Ruling.** Grinding Station sacrifices a mana-value-0 artifact to mill three. Breach escapes the artifact for {0} plus three exiled cards. It enters and untaps Station. Lotus Petal, Mox Opal and Chrome Mox work. Mox Diamond doesn't: without a land discard it goes straight to the graveyard and never enters, so Station doesn't untap.

**Citations**

- Oracle, *Grinding Station*: “Whenever an artifact enters, you may untap this artifact.”
- Oracle, *Mox Diamond*: “If this artifact would enter, you may discard a land card instead. If you do, put this artifact onto the battlefield. If you don't, put it into its owner's graveyard.”
- [CR 702.138a](#cr-702138a), [CR 614.1a](#cr-6141a)
- Commander Spellbook [1368-3698--44](https://commanderspellbook.com/combo/1368-3698--44/) (community-maintained, retrieved 2026-10-16): “Cast the artifact from your graveyard for its escape cost by paying {0} and exiling three cards from your graveyard.”

### kess-07: Breach + LED + Brain Freeze or Wheel

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Kess, Dissident Mage, Underworld Breach, Lion's Eye Diamond, Brain Freeze, Wheel of Fortune, Lotus Petal

**Ruling.** The standard Breach lines into an Oracle finish. Each needs six other cards in hand and/or graveyard.

**Citations**

- [CR 702.138a](#cr-702138a), [CR 702.40a](#cr-70240a)
- Commander Spellbook [1368-3518-4856](https://commanderspellbook.com/combo/1368-3518-4856/) (community-maintained, retrieved 2026-10-16): “You have at least six other cards in hand and/or graveyard.”
- Commander Spellbook [1368-2706-3518](https://commanderspellbook.com/combo/1368-2706-3518/) (community-maintained, retrieved 2026-10-16): “Activate Lion's Eye Diamond by discarding your hand and sacrificing it, adding {R}{R}{R}.”
- Source (re-verified): [`Kess_Dissident_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kess_dissident_mage_2026-10-14/Kess_Dissident_Mage_Rules_Attestation.json) → “Underworld Breach plus Lion's Eye Diamond plus Brain Freeze”

## Engines and payoffs

### kess-05: Entomb and Snapcaster as graveyard-spell access

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Kess, Dissident Mage, Entomb, Snapcaster Mage, Valley Floodcaller

**Ruling.** Entomb can bin any instant or sorcery for Kess to cast right away. Snapcaster's flashback is a separate permission and works on opponents' turns at instant timing. Valley Floodcaller gives noncreature spells flash, including Kess casts, but Kess still works only on your turn.

**Citations**

- Oracle, *Snapcaster Mage*: “When this creature enters, target instant or sorcery card in your graveyard gains flashback until end of turn. The flashback cost is equal to its mana cost.”
- [CR 702.34a](#cr-70234a), [CR 702.8a](#cr-7028a)
- Source (re-verified): [`Kess_Dissident_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kess_dissident_mage_2026-10-14/Kess_Dissident_Mage_Rules_Attestation.json) → “Entomb as Kess spell tutor”
- Source (re-verified): [`Kess_Dissident_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kess_dissident_mage_2026-10-14/Kess_Dissident_Mage_Rules_Attestation.json) → “Valley Floodcaller and Kess timing”
- Source (re-verified): [`Kess_Dissident_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kess_dissident_mage_2026-10-14/Kess_Dissident_Mage_Rules_Attestation.json) → “Snapcaster Mage complement to Kess”

## Timing and priority

### kess-09: Bargained Beseech the Mirror

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Kess, Dissident Mage, Beseech the Mirror

**Ruling.** Bargained Beseech casts a found card with mana value 4 or less free during its resolution. Nothing in the list gives split second. Beseech is a sorcery, so Kess can recast it only at sorcery speed.

**Citations**

- Scryfall ruling, *Beseech the Mirror*: “Bargain represents an optional additional cost. A spell cast with that additional cost paid is "bargained."”
- [CR 608.2g](#cr-6082g), [CR 702.166a](#cr-702166a)
- Source (re-verified): [`Kess_Dissident_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kess_dissident_mage_2026-10-14/Kess_Dissident_Mage_Rules_Attestation.json) → “Beseech the Mirror bargain”

## Zones, commander tax and the command zone

### kess-02: A new Kess object resets the permission (Displacer Kitten)

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Kess, Dissident Mage, Displacer Kitten

**Ruling.** A blinked Kess is a new object with a fresh once-per-turn use. Casting a noncreature spell through Kess triggers Kitten. Blinking Kess in response gives a new permission, and the spell already cast is still exiled by the old Kess's replacement.

**Citations**

- Scryfall ruling, *Kess, Dissident Mage*: “If you cast one instant or sorcery card from your graveyard and then have a new Kess come under your control in the same turn, you may cast another instant or sorcery card from your graveyard that turn.”
- Scryfall ruling, *Kess, Dissident Mage*: “Once you begin to cast the card, losing control of Kess won't affect the spell. You can finish casting it as normal and it will be exiled if it would be put into your graveyard.”
- [CR 400.7](#cr-4007)
- Source (re-verified): [`Kess_Dissident_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kess_dissident_mage_2026-10-14/Kess_Dissident_Mage_Rules_Attestation.json) → “New Kess object resets once-per-turn permission”
- Source (re-verified): [`Kess_Dissident_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kess_dissident_mage_2026-10-14/Kess_Dissident_Mage_Rules_Attestation.json) → “Displacer Kitten with a spell cast through Kess”

## What the list depends on

### kess-08: Demonic Counsel is only a tutor with delirium

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Kess, Dissident Mage, Demonic Counsel

**Ruling.** There are no Demons in the list, so before delirium Demonic Counsel finds nothing. With four or more card types in your graveyard it finds any card.

**Citations**

- Oracle, *Demonic Counsel*: “Search your library for a Demon card, reveal it, put it into your hand, then shuffle.”
- [CR 207.2c](#cr-2072c), [CR 205.2a](#cr-2052a)
- Source (re-verified): [`Kess_Dissident_Mage_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/kess_dissident_mage_2026-10-14/Kess_Dissident_Mage_Rules_Attestation.json) → “Demonic Counsel delirium limitation”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 121.4

A player who attempts to draw a card from a library with no cards in it loses the game the next time a player would receive priority. (This is a state-based action. See rule 704.)

#### CR 205.2a

The card types are artifact, battle, conspiracy, creature, dungeon, enchantment, instant, kindred, land, phenomenon, plane, planeswalker, scheme, sorcery, and vanguard. See section 3, “Card Types.”

#### CR 207.2c

An ability word appears in italics at the beginning of some abilities. Ability words are similar to keywords in that they tie together cards that have similar functionality, but they have no special rules meaning and no individual entries in the Comprehensive Rules. The ability words are adamant, addendum, alliance, battalion, bloodrush, celebration, channel, chroma, cohort, constellation, converge, council’s dilemma, coven, delirium, descend 4, descend 8, disappear, domain, eerie, eminence, enrage, fateful hour, fathomless descent, ferocious, flurry, formidable, grandeur, hellbent, heroic, …

#### CR 400.7

An object that moves from one zone to another becomes a new object with no memory of, or relation to, its previous existence. This rule has the following exceptions.

#### CR 601.2

To cast a spell is to take it from where it is (usually the hand), put it on the stack, and pay its costs, so that it will eventually resolve and have its effect. Casting a spell includes proposal of the spell (rules 601.2a–d) and determination and payment of costs (rules 601.2f–h). To cast a spell, a player follows the steps listed below, in order. A player must be legally allowed to cast the spell to begin this process (see rule 601.3). If a player is unable to comply with the requirements of a step listed below while performing that step, the casting of the spell is illegal; the game …

#### CR 603.3

Once an ability has triggered, its controller puts it on the stack as an object that’s not a card the next time a player would receive priority. See rule 117, “Timing and Priority.” The ability becomes the topmost object on the stack. It has the text of the ability that created it, and no other characteristics. It remains on the stack until it’s countered, it resolves, a rule causes it to be removed from the stack, or an effect moves it elsewhere.

#### CR 608.2g

If an effect gives a player the option to pay mana, they may activate mana abilities before taking that action. If an effect specifically instructs or allows a player to cast a spell during resolution, they do so by following the steps in rules 601.2a–i, except no player receives priority after it’s cast. That spell becomes the topmost object on the stack, and the currently resolving spell or ability continues to resolve, which may include casting other spells this way. No other spells can normally be cast and no other abilities can normally be activated during resolution.

#### CR 614.1a

Effects that use the word “instead” are replacement effects. Most replacement effects use the word “instead” to indicate what events will be replaced with other events.

#### CR 702.8a

Flash is a static ability that functions in any zone from which you could play the card it’s on. “Flash” means “You may play this card any time you could cast an instant.”

#### CR 702.34a

Flashback appears on some instants and sorceries. It represents two static abilities: one that functions while the card is in a player’s graveyard and another that functions while the card is on the stack. “Flashback [cost]” means “You may cast this card from your graveyard if the resulting spell is an instant or sorcery spell by paying [cost] rather than paying its mana cost” and “If the flashback cost was paid, exile this card instead of putting it anywhere else any time it would leave the stack.” Casting a spell using its flashback ability follows the rules for paying alternative costs in …

#### CR 702.40a

Storm is a triggered ability that functions on the stack. “Storm” means “When you cast this spell, copy it for each other spell that was cast before it this turn. If the spell has any targets, you may choose new targets for any of the copies.”

#### CR 702.138a

Escape represents a static ability that functions while the card with escape is in a player’s graveyard. “Escape [cost]” means “You may cast this card from your graveyard by paying [cost] rather than paying its mana cost.” Casting a spell using its escape ability follows the rules for paying alternative costs in rules 601.2b and 601.2f–h.

#### CR 702.166a

Bargain is a static ability that functions while the spell with bargain is on the stack. “Bargain” means “As an additional cost to cast this spell, you may sacrifice an artifact, enchantment, or token.” Paying a spell’s bargain cost follows the rules for paying additional costs in rules 601.2b and 601.2f–h.

