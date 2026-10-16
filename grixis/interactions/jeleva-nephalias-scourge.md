---
title: "Jeleva, Nephalia's Scourge — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Jeleva, Nephalia's Scourge — Interaction Review

> Bot cycle 49 · batch C · reviewed 2026-10-16. Deck: [Jeleva, Nephalia's Scourge](../decks/jeleva-nephalias-scourge.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-15), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/jeleva-nephalias-scourge.txt`](../../exports/grixis-archidekt/jeleva-nephalias-scourge.txt) · SHA-256 `900a09d494293665662756ef2be07998b9d86af42c2a23ea54900953f9f181af` |
| Rulings | **10** (10 verified · 0 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-15 · rulings 2026-10-15 |
| Source attestations | [`Jeleva_Nephalia_s_Scourge_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/jeleva_nephalia_s_scourge_2026-10-14/Jeleva_Nephalia_s_Scourge_Rules_Attestation.json) (17 interactions, all PASS) |

## Contents
- [Summary](#summary)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [Timing and priority](#timing-and-priority)
- [Replacement and prevention effects](#replacement-and-prevention-effects)
- [Trigger ordering](#trigger-ordering)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [Rules cited](#rules-cited)

## Summary

Jeleva, Nephalia's Scourge exiles the top X cards of every library (X = mana spent, tax included). When she attacks, she casts an instant or sorcery from that pile for free. This review re-verifies all 17 attestation items. Seven Spellbook lines are confirmed (the Oracle, Doomsday and Breach lines).

The main rules surprises: the commander tax raises X; Greaves' shroud blocks Torch Courier; casting Jeleva after Doomsday exiles your own pile. No list errors.

## Commander rules text and edge cases

### jeleva-01: X counts the mana actually spent, including commander tax

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Jeleva, Nephalia's Scourge

**Ruling.** Jeleva exiles X cards from each library, where X is the mana spent to cast her. Commander tax counts, so the first cast is X = 4, the second is X = 6, and so on. You can't overpay on purpose. If she enters without being cast, X = 0.

**Citations**

- Scryfall ruling, *Jeleva, Nephalia's Scourge*: “The amount of mana you spent to cast this creature is usually equal to its mana value. However, you also include any additional costs you pay, including the cost imposed for casting your commander from the command zone.”
- Scryfall ruling, *Jeleva, Nephalia's Scourge*: “If Jeleva enters the battlefield without being cast, then no mana was spent to cast it. This means X will be 0, so no cards will be exiled.”
- [CR 903.8](#cr-9038), [CR 601.2f](#cr-6012f)
- Source (re-verified): [`Jeleva_Nephalia_s_Scourge_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/jeleva_nephalia_s_scourge_2026-10-14/Jeleva_Nephalia_s_Scourge_Rules_Attestation.json) → “Jeleva ETB uses actual mana spent including commander tax”

## Combos and engine lines

### jeleva-08: Oracle lines and Doomsday; don't cast Jeleva onto your own pile

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Jeleva, Nephalia's Scourge, Thassa's Oracle, Demonic Consultation, Tainted Pact, Doomsday

**Ruling.** Consultation or Tainted Pact with Oracle works: the list has 100 distinct names. Doomsday + Oracle needs at least 2 life and devotion to blue of at least three. Sequencing trap: once a Doomsday pile is built, casting Jeleva exiles X cards (4+) of it from the top of your own library. Jeleva can cast Doomsday from her exile, though.

**Citations**

- [CR 121.4](#cr-1214), [CR 608.2g](#cr-6082g)
- Commander Spellbook [1295-3189](https://commanderspellbook.com/combo/1295-3189/) (community-maintained, retrieved 2026-10-16): “You have at least three devotion to blue.”
- Commander Spellbook [742-1295](https://commanderspellbook.com/combo/742-1295/) (community-maintained, retrieved 2026-10-16): “Cast Demonic Consultation by paying {B}, naming Thassa's Oracle and thus exiling your library due to you not having a card named Thassa's Oracle in your library.”
- Commander Spellbook [1295-3093](https://commanderspellbook.com/combo/1295-3093/) (community-maintained, retrieved 2026-10-16): “No two cards in library share a name.”
- Source (re-verified): [`Jeleva_Nephalia_s_Scourge_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/jeleva_nephalia_s_scourge_2026-10-14/Jeleva_Nephalia_s_Scourge_Rules_Attestation.json) → “Thassa's Oracle plus Demonic Consultation”
- Source (re-verified): [`Jeleva_Nephalia_s_Scourge_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/jeleva_nephalia_s_scourge_2026-10-14/Jeleva_Nephalia_s_Scourge_Rules_Attestation.json) → “Thassa's Oracle plus Tainted Pact and singleton structure”
- Source (re-verified): [`Jeleva_Nephalia_s_Scourge_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/jeleva_nephalia_s_scourge_2026-10-14/Jeleva_Nephalia_s_Scourge_Rules_Attestation.json) → “Doomsday role is supported without asserting an undocumented fixed pile”

### jeleva-09: Breach lines: LED + Brain Freeze, Wheel + Jeska's Will

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Jeleva, Nephalia's Scourge, Underworld Breach, Lion's Eye Diamond, Brain Freeze, Wheel of Fortune, Jeska's Will, Lotus Petal

**Ruling.** Breach escapes LED and Brain Freeze to mill yourself into an Oracle finish. Jeska's Will + Wheel loops off an opponent's six-card hand. Jeska's Will gets both modes because you control Jeleva, or any commander.

**Citations**

- Scryfall ruling, *Jeska's Will*: “Even though the card is named after a specific character, controlling any commander will satisfy its condition.”
- [CR 702.138a](#cr-702138a)
- Commander Spellbook [1368-1878-2706](https://commanderspellbook.com/combo/1368-1878-2706/) (community-maintained, retrieved 2026-10-16): “An opponent has at least six cards in hand.”
- Commander Spellbook [1368-3518-4856](https://commanderspellbook.com/combo/1368-3518-4856/) (community-maintained, retrieved 2026-10-16): “You have at least six other cards in hand and/or graveyard.”
- Source (re-verified): [`Jeleva_Nephalia_s_Scourge_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/jeleva_nephalia_s_scourge_2026-10-14/Jeleva_Nephalia_s_Scourge_Rules_Attestation.json) → “Underworld Breach plus Lion's Eye Diamond plus Brain Freeze”

## Engines and payoffs

### jeleva-05: Staging the top of the library for Jeleva's exile

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Jeleva, Nephalia's Scourge, Vampiric Tutor, Imperial Seal, Mystical Tutor, Personal Tutor, Long-Term Plans, Scheming Symmetry, Brainstorm, Scroll Rack

**Ruling.** Top-deck tutors, Brainstorm and Scroll Rack put a chosen spell on top. Long-Term Plans puts it third, which X = 4 still reaches. Then Jeleva's ETB exiles it for a free cast on attack. Scheming Symmetry also stages a card on an opponent's library, and Jeleva exiles that one too. This is setup, not protected: a shuffle, draw or mill before the ETB resolves breaks it.

**Citations**

- Oracle, *Long-Term Plans*: “Search your library for a card, then shuffle and put that card third from the top.”
- [CR 401.2](#cr-4012), [CR 701.24a](#cr-70124a)
- Source (re-verified): [`Jeleva_Nephalia_s_Scourge_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/jeleva_nephalia_s_scourge_2026-10-14/Jeleva_Nephalia_s_Scourge_Rules_Attestation.json) → “Top-deck tutors deliberately stage Jeleva exile targets”
- Source (re-verified): [`Jeleva_Nephalia_s_Scourge_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/jeleva_nephalia_s_scourge_2026-10-14/Jeleva_Nephalia_s_Scourge_Rules_Attestation.json) → “Long-Term Plans third-from-top setup”
- Source (re-verified): [`Jeleva_Nephalia_s_Scourge_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/jeleva_nephalia_s_scourge_2026-10-14/Jeleva_Nephalia_s_Scourge_Rules_Attestation.json) → “Scheming Symmetry becomes Jeleva setup and potential denial”
- Source (re-verified): [`Jeleva_Nephalia_s_Scourge_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/jeleva_nephalia_s_scourge_2026-10-14/Jeleva_Nephalia_s_Scourge_Rules_Attestation.json) → “Brainstorm and Scroll Rack convert hand cards into Jeleva targets”

## Timing and priority

### jeleva-03: The attack-trigger cast happens during resolution, before blockers

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Jeleva, Nephalia's Scourge

**Ruling.** You cast the spell while the attack trigger resolves, or you lose the chance. Type-based timing is ignored, so sorceries are fine, but you can't pick alternative costs like overload. You can pay additional costs, and X is 0.

**Citations**

- Scryfall ruling, *Jeleva, Nephalia's Scourge*: “If you cast an instant or sorcery card using Jeleva's last ability, you do so while that ability is resolving. If you choose not to (or you can't), you won't get a chance to cast it later unless the ability triggers again.”
- Scryfall ruling, *Jeleva, Nephalia's Scourge*: “When casting an instant or sorcery card this way, ignore all timing restrictions based on the card's type. Other timing restrictions, such as "Cast [this spell] only during combat," must be followed.”
- Scryfall ruling, *Jeleva, Nephalia's Scourge*: “The card is cast before blocking creatures are declared.”
- [CR 608.2g](#cr-6082g), [CR 118.9](#cr-1189)
- Source (re-verified): [`Jeleva_Nephalia_s_Scourge_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/jeleva_nephalia_s_scourge_2026-10-14/Jeleva_Nephalia_s_Scourge_Rules_Attestation.json) → “Jeleva casts during attack-trigger resolution”

### jeleva-06: Haste package; Greaves' shroud blocks Torch Courier

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Jeleva, Nephalia's Scourge, Arena of Glory, Torch Courier, Lightning Greaves

**Ruling.** Exerted Arena of Glory mana spent on Jeleva gives her haste. Torch Courier can sacrifice to give her haste, and so can equipping Lightning Greaves. Sequence these: once Greaves gives Jeleva shroud, Torch Courier can't target her.

**Citations**

- Oracle, *Arena of Glory*: “{R}, {T}, Exert this land: Add {R}{R}. If any of that mana is spent on a creature spell, it gains haste until end of turn.”
- Scryfall ruling, *Arena of Glory*: “If mana generated with Arena of Glory's last ability is spent to pay any part of a creature spell's cost, including an alternative or additional cost, that creature spell (and the resulting creature) will gain haste until end of turn.”
- [CR 702.10a](#cr-70210a), [CR 702.18a](#cr-70218a)
- Source (re-verified): [`Jeleva_Nephalia_s_Scourge_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/jeleva_nephalia_s_scourge_2026-10-14/Jeleva_Nephalia_s_Scourge_Rules_Attestation.json) → “Immediate-attack package: Arena of Glory, Torch Courier, Lightning Greaves”

## Replacement and prevention effects

### jeleva-10: Hexing Squelcher's protection scope

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Jeleva, Nephalia's Scourge, Hexing Squelcher

**Ruling.** Hexing Squelcher makes your spells uncounterable and gives your other creatures ward (pay 2 life). It doesn't protect Jeleva's triggered abilities, or stop removal that isn't a counterspell (though removal targeting Jeleva costs that player 2 life).

**Citations**

- Oracle, *Hexing Squelcher*: “Spells you control can't be countered.”
- [CR 702.21a](#cr-70221a), [CR 101.2](#cr-1012)
- Source (re-verified): [`Jeleva_Nephalia_s_Scourge_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/jeleva_nephalia_s_scourge_2026-10-14/Jeleva_Nephalia_s_Scourge_Rules_Attestation.json) → “Hexing Squelcher protection scope”

## Trigger ordering

### jeleva-04: Harmonic Prodigy doubles both Jeleva triggers

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Jeleva, Nephalia's Scourge, Harmonic Prodigy

**Ruling.** Jeleva is a Wizard, so Harmonic Prodigy makes her ETB trigger twice (two exiles of X each) and her attack trigger twice (two free casts). The same card can't be cast twice, because the first cast takes it out of exile.

**Citations**

- Oracle, *Harmonic Prodigy*: “If a triggered ability of a Shaman or another Wizard you control triggers, that ability triggers an additional time.”
- [CR 603.2](#cr-6032), [CR 603.3b](#cr-6033b)
- Source (re-verified): [`Jeleva_Nephalia_s_Scourge_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/jeleva_nephalia_s_scourge_2026-10-14/Jeleva_Nephalia_s_Scourge_Rules_Attestation.json) → “Harmonic Prodigy doubles Jeleva ETB and attack triggers”

### jeleva-07: Free-cast payoffs: Mind's Desire storm, Final Fortune, Peer into the Abyss

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Jeleva, Nephalia's Scourge, Mind's Desire, Final Fortune, Peer into the Abyss

**Ruling.** Casting through Jeleva is still casting, so Mind's Desire's storm triggers and counts every spell cast earlier that turn. Final Fortune's extra turn still ends with you losing unless you win first. A skipped extra turn doesn't cause the loss. Peer into the Abyss is a seven-mana spell you cast for free.

**Citations**

- Scryfall ruling, *Mind's Desire*: “Spells cast from zones other than a player's hand and spells that were countered are counted by the storm ability.”
- Scryfall ruling, *Final Fortune*: “If you end up skipping the extra turn that is gained, you do not lose the game.”
- Scryfall ruling, *Peer into the Abyss*: “The life lost is rounded up, not the remaining life total. For example, if the target player has 7 life, they lose 4 life and end up with 3. Similarly, the number of cards drawn is rounded up, not the number of cards remaining in the library.”
- [CR 702.40a](#cr-70240a), [CR 500.7](#cr-5007), [CR 107.1a](#cr-1071a)
- Source (re-verified): [`Jeleva_Nephalia_s_Scourge_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/jeleva_nephalia_s_scourge_2026-10-14/Jeleva_Nephalia_s_Scourge_Rules_Attestation.json) → “Mind's Desire cast through Jeleva still has storm”
- Source (re-verified): [`Jeleva_Nephalia_s_Scourge_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/jeleva_nephalia_s_scourge_2026-10-14/Jeleva_Nephalia_s_Scourge_Rules_Attestation.json) → “Final Fortune extra-turn risk”
- Source (re-verified): [`Jeleva_Nephalia_s_Scourge_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/jeleva_nephalia_s_scourge_2026-10-14/Jeleva_Nephalia_s_Scourge_Rules_Attestation.json) → “Peer into the Abyss free-cast target”

## Zones, commander tax and the command zone

### jeleva-02: Each Jeleva object only knows its own exiled cards

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Jeleva, Nephalia's Scourge

**Ruling.** If Jeleva leaves the battlefield, the cards she exiled stay exiled for good. A re-cast Jeleva is a new object, so she can only cast from her own new exile pile.

**Citations**

- Scryfall ruling, *Jeleva, Nephalia's Scourge*: “If Jeleva leaves the battlefield, the exiled cards will remain exiled indefinitely. If Jeleva enters the battlefield again, it won't be associated with the cards the "other" Jeleva exiled. The new Jeleva will exile a new set of cards. Only those cards can be cast using Jeleva's last ability.”
- [CR 607.2a](#cr-6072a), [CR 400.7](#cr-4007)
- Source (re-verified): [`Jeleva_Nephalia_s_Scourge_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/jeleva_nephalia_s_scourge_2026-10-14/Jeleva_Nephalia_s_Scourge_Rules_Attestation.json) → “Each Jeleva object tracks only its own exiled cards”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 101.2

When a rule or effect allows or directs something to happen, and another effect states that it can’t happen, the “can’t” effect takes precedence.

#### CR 107.1a

You can’t choose a fractional number, deal fractional damage, gain fractional life, and so on. If a spell or ability could generate a fractional number, the spell or ability will tell you whether to round up or down.

#### CR 118.9

Some spells have alternative costs. An alternative cost is a cost listed in a spell’s text, or applied to it from another effect, that its controller may pay rather than paying the spell’s mana cost. Alternative costs are usually phrased, “You may [action] rather than pay [this object’s] mana cost,” or “You may cast [this object] without paying its mana cost.” Note that some alternative costs are listed in keywords; see rule 702.

#### CR 121.4

A player who attempts to draw a card from a library with no cards in it loses the game the next time a player would receive priority. (This is a state-based action. See rule 704.)

#### CR 400.7

An object that moves from one zone to another becomes a new object with no memory of, or relation to, its previous existence. This rule has the following exceptions.

#### CR 401.2

Each library must be kept in a single face-down pile. Players can’t look at or change the order of cards in a library.

#### CR 500.7

Some effects can give a player extra turns. They do this by adding the turns directly after the specified turn. If a player is given multiple extra turns, the extra turns are added one at a time. If multiple players are given extra turns, the extra turns are added one at a time, in APNAP order (see rule 101.4). The most recently created turn will be taken first.

#### CR 601.2f

The player determines the total cost of the spell. Usually this is just the mana cost. Some spells have additional or alternative costs. Some effects may increase or reduce the cost to pay, or may provide other alternative costs. Costs may include paying mana, tapping permanents, sacrificing permanents, discarding cards, and so on. The total cost is the mana cost or alternative cost (as determined in rule 601.2b), plus all additional costs and cost increases, and minus all cost reductions. If multiple cost reductions apply, the player may apply them in any order. If the mana component of the …

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 603.3b

If multiple abilities have triggered since the last time a player received priority, the abilities are placed on the stack in a two-part process. First, each player, in APNAP order, puts each triggered ability they control with a trigger condition that isn’t another ability triggering on the stack in any order they choose. (See rule 101.4.) Second, each player, in APNAP order, puts all remaining triggered abilities they control on the stack in any order they choose. Then the game once again checks for and performs state-based actions until none are performed, then abilities that triggered …

#### CR 607.2a

If an object has an activated or triggered ability printed on it that instructs a player to exile one or more cards and an ability printed on it that refers either to “the exiled cards” or to cards “exiled with [this object],” these abilities are linked. The second ability refers only to cards in the exile zone that were put there as a result of an instruction to exile them in the first ability.

#### CR 608.2g

If an effect gives a player the option to pay mana, they may activate mana abilities before taking that action. If an effect specifically instructs or allows a player to cast a spell during resolution, they do so by following the steps in rules 601.2a–i, except no player receives priority after it’s cast. That spell becomes the topmost object on the stack, and the currently resolving spell or ability continues to resolve, which may include casting other spells this way. No other spells can normally be cast and no other abilities can normally be activated during resolution.

#### CR 701.24a

To shuffle a library or a face-down pile of cards, randomize the cards within it so that no player knows their order.

#### CR 702.10a

Haste is a static ability.

#### CR 702.18a

Shroud is a static ability. “Shroud” means “This permanent or player can’t be the target of spells or abilities.”

#### CR 702.21a

Ward is a triggered ability. Ward [cost] means “Whenever this permanent becomes the target of a spell or ability an opponent controls, counter that spell or ability unless that player pays [cost].”

#### CR 702.40a

Storm is a triggered ability that functions on the stack. “Storm” means “When you cast this spell, copy it for each other spell that was cast before it this turn. If the spell has any targets, you may choose new targets for any of the copies.”

#### CR 702.138a

Escape represents a static ability that functions while the card with escape is in a player’s graveyard. “Escape [cost]” means “You may cast this card from your graveyard by paying [cost] rather than paying its mana cost.” Casting a spell using its escape ability follows the rules for paying alternative costs in rules 601.2b and 601.2f–h.

#### CR 903.8

A player may cast a commander they own from the command zone. A commander cast from the command zone costs an additional {2} for each previous time the player casting it has cast it from the command zone that game. This additional cost is informally known as the “commander tax.”

