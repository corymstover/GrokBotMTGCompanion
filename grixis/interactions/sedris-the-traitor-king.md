---
title: "Sedris, the Traitor King — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Sedris, the Traitor King — Interaction Review

> Bot cycle 54 · batch E · reviewed 2026-10-16. Deck: [Sedris, the Traitor King](../decks/sedris-the-traitor-king.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-15), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/sedris-the-traitor-king.txt`](../../exports/grixis-archidekt/sedris-the-traitor-king.txt) · SHA-256 `ddcd18ab4826834cde491cd21b8f9697c77677dc8890a696b3ad6bd5f4e96aa0` |
| Rulings | **6** (6 verified · 0 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-15 · rulings 2026-10-15 |
| Source attestations | [`Sedris_the_Traitor_King_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sedris_2026-10-15/gate_output/Sedris_the_Traitor_King_Rules_Attestation.json) (Rules attestation (12 items, all PASS) re-verified) · [`Sedris_the_Traitor_King_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Sedris_the_Traitor_King_Approval_Ready_Verification_2026-10-15.md) (Approval-ready verification) |

## Contents
- [Summary](#summary)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Key card-pair interactions](#key-card-pair-interactions)
- [Timing and priority](#timing-and-priority)
- [Trigger ordering](#trigger-ordering)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [Rules cited](#rules-cited)

## Summary

Sedris gives every creature card in your graveyard unearth {2}{B}, which Convergence of Dominion cuts to {B}. The list keeps unearthed creatures with Obeka, Sundial, Teferi's Veil or Deadeye Navigator, cashes in their arrival with River Kelpie, Twilight Diviner and Panharmonicon, and runs Peregrine Drake + Deadeye for infinite mana. All 12 attestation items and the Spellbook line are re-verified against the canonical list.

Rules surprises: Stifling the exile trigger keeps the creature, but the leave-the-battlefield exile stays; Teferi's Veil phase-out skips the end-step exile; a Deadeye blink resets the creature as a new object; Diviner tokens are never exiled by unearth. Note: the attestation's reason Embalmer's Tools couldn't reduce further is off (Tools isn't in the list).

## Commander rules text and edge cases

### sedris-01: Sedris-granted unearth: an activated ability of each card, sorcery speed, with two exile clauses

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Sedris, the Traitor King

**Ruling.** Each creature card in your graveyard has unearth {2}{B}. It's an activated ability of the card, not of Sedris, and can be used only at sorcery speed. Unearthing isn't casting, so spell counters can't stop it, but Stifle can. The creature returns with haste and has two exile clauses:
- **A delayed end-step exile trigger:** if it's countered or removed, it never comes back.
- **A replacement effect:** if the creature would leave the battlefield, it's exiled instead. This always stays.

A card with its own unearth has both, and you choose which to use.

**Citations**

- Oracle, *Sedris, the Traitor King*: “Each creature card in your graveyard has unearth {2}{B}. ({2}{B}: Return the card to the battlefield. The creature gains haste. Exile it at the beginning of the next end step or if it would leave the battlefield. Unearth only as a sorcery.)”
- Scryfall ruling, *Sedris, the Traitor King*: “At the beginning of the end step, a creature returned to the battlefield with unearth is exiled. This is a delayed triggered ability, and it can be countered by effects such as Stifle or Voidslime that counter triggered abilities. If the ability is countered, the creature will stay on the battlefield and the delayed trigger won't trigger again. However, the replacement effect will still exile the creature when it eventually leaves the battlefield.”
- Scryfall ruling, *Sedris, the Traitor King*: “Activating a creature card's unearth ability isn't the same as casting the creature card. The unearth ability is put on the stack, but the creature card is not. Spells and abilities that interact with activated abilities (such as Stifle) will interact with unearth, but spells and abilities that interact with spells (such as Remove Soul) will not.”
- [CR 702.84a](#cr-70284a), [CR 602.5d](#cr-6025d), [CR 603.7](#cr-6037)
- Source (re-verified): [`Sedris_the_Traitor_King_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sedris_2026-10-15/gate_output/Sedris_the_Traitor_King_Rules_Attestation.json) → “Sedris-granted unearth”

## Combos and engine lines

### sedris-05: Peregrine Drake + Deadeye Navigator: infinite mana and blinks

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Sedris, the Traitor King, Peregrine Drake, Deadeye Navigator

**Ruling.** Pair Deadeye with Peregrine Drake, then pay {1}{U} to blink Drake. Drake untaps up to five lands, which is a net mana gain if they make at least {2}{U}, and Deadeye re-pairs. Repeat for unlimited mana and ETBs. Either piece can be unearthed from the graveyard with Sedris. A blinked unearthed creature is a new object, so the unearth exile no longer applies.

**Citations**

- Scryfall ruling, *Deadeye Navigator*: “If you activate the ability granted by Deadeye Navigator, the creature will be exiled, the pair will immediately be broken, and then the card will be returned to the battlefield. Deadeye Navigator’s soulbond ability triggers when that card enters the battlefield and the pair can then be reunited.”
- [CR 702.95a](#cr-70295a), [CR 400.7](#cr-4007)
- Commander Spellbook [1409-3821](https://commanderspellbook.com/combo/1409-3821/) (community-maintained, retrieved 2026-10-16): “Resolve the Peregrine Drake trigger, untapping up to five lands you control.”
- Source (re-verified): [`Sedris_the_Traitor_King_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sedris_2026-10-15/gate_output/Sedris_the_Traitor_King_Rules_Attestation.json) → “Deadeye Navigator + Peregrine Drake”

## Key card-pair interactions

### sedris-02: Convergence of Dominion makes unearth cost {B}

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Sedris, the Traitor King, Convergence of Dominion

**Ruling.** While you control Sedris, Convergence makes activated abilities of cards in your graveyard cost {2} less, so unearth {2}{B} costs {B}. It can't enable an ability you couldn't already activate. The attestation says Convergence's one-mana floor stops Embalmer's Tools from reducing it further. The result is right, but the real reason is that no generic mana is left to reduce. Embalmer's Tools isn't in the canonical list anyway.

**Citations**

- Oracle, *Convergence of Dominion*: “Dynastic Command Node — As long as you control your commander, activated abilities of cards in your graveyard cost {2} less to activate. This effect can't reduce the mana in that ability's activation cost to less than one mana.”
- Scryfall ruling, *Convergence of Dominion*: “Convergence of Dominion doesn't allow you to activate abilities of cards in graveyards unless you could already activate those abilities.”
- [CR 601.2f](#cr-6012f), [CR 602.2b](#cr-6022b)
- Source (re-verified): [`Sedris_the_Traitor_King_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sedris_2026-10-15/gate_output/Sedris_the_Traitor_King_Rules_Attestation.json) → “Convergence of Dominion”

## Timing and priority

### sedris-03: Keeping unearthed creatures: Obeka / Sundial on the exile trigger, Teferi's Veil phase-out, Deadeye blink

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Sedris, the Traitor King, Obeka, Brute Chronologist, Sundial of the Infinite, Teferi's Veil, Deadeye Navigator

**Ruling.** Three ways to keep an unearthed creature:
- **Obeka or Sundial:** end the turn while the unearth exile trigger is on the stack. It's exiled and never triggers again. Ending the turn earlier only pushes it to the next end step.
- **Teferi's Veil:** attackers phase out at end of combat, after combat damage, so they're still out when the end-step exile trigger resolves and can't be found. They phase back in during your next untap step.
- **Deadeye Navigator:** blinking is itself an exile, so the replacement doesn't change it. The card returns as a new object with no unearth tracking.

In the first two cases the leave-the-battlefield replacement still applies later.

**Citations**

- Oracle, *Teferi's Veil*: “Whenever a creature you control attacks, it phases out at end of combat. (While it's phased out, it's treated as though it doesn't exist. It phases in before you untap during your next untap step.)”
- Scryfall ruling, *Sedris, the Traitor King*: “If a creature returned to the battlefield with unearth would leave the battlefield for any reason, it's exiled instead — unless the spell or ability that's causing the creature to leave the battlefield is actually trying to exile it! In that case, it succeeds at exiling it. If it later returns the creature card to the battlefield (as Oblivion Ring or Flickerwisp might, for example), the creature card will return to the battlefield as a new object with no relation to its previous existence. The unearth effect will no longer apply to it.”
- Scryfall ruling, *Teferi's Veil*: “The “at end of combat” ability triggers after combat damage resolves. Creatures dealt lethal damage in combat won’t be saved this way.”
- Scryfall ruling, *Obeka, Brute Chronologist*: “If the turn ends during the end step after "At the beginning of the next end step" abilities have triggered but before they've resolved, those abilities won't trigger again next turn.”
- [CR 724.1b](#cr-7241b), [CR 702.26b](#cr-70226b), [CR 400.7](#cr-4007)
- Source (re-verified): [`Sedris_the_Traitor_King_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sedris_2026-10-15/gate_output/Sedris_the_Traitor_King_Rules_Attestation.json) → “Obeka / Sundial timing”
- Source (re-verified): [`Sedris_the_Traitor_King_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sedris_2026-10-15/gate_output/Sedris_the_Traitor_King_Rules_Attestation.json) → “Teferi's Veil”
- Source (re-verified): [`Sedris_the_Traitor_King_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sedris_2026-10-15/gate_output/Sedris_the_Traitor_King_Rules_Attestation.json) → “Deadeye Navigator rescue”

## Trigger ordering

### sedris-04: Enter-from-graveyard payoffs: River Kelpie, Twilight Diviner, Panharmonicon

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Sedris, the Traitor King, River Kelpie, Twilight Diviner, Panharmonicon

**Ruling.** Unearth puts creatures onto the battlefield from the graveyard:
- **River Kelpie** draws for each one, plus one more if Kelpie itself returns at the same time.
- **Twilight Diviner** makes a token copy of one of them, once per turn. The token isn't the unearthed card, so neither exile clause touches it.
- **Panharmonicon** doubles their artifact and creature ETB triggers.

**Citations**

- Oracle, *Twilight Diviner*: “Whenever one or more other creatures you control enter, if they entered or were cast from a graveyard, create a token that's a copy of one of them. This ability triggers only once each turn.”
- Oracle, *River Kelpie*: “Whenever this creature or another permanent enters from a graveyard, draw a card.”
- Scryfall ruling, *Twilight Diviner*: “Any enters abilities of the copied creature will trigger when the token enters. Any "as [this creature] enters" or "[this creature] enters with" abilities of the copied permanent will also work.”
- [CR 603.6a](#cr-6036a), [CR 111.1](#cr-1111)
- Source (re-verified): [`Sedris_the_Traitor_King_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sedris_2026-10-15/gate_output/Sedris_the_Traitor_King_Rules_Attestation.json) → “River Kelpie”
- Source (re-verified): [`Sedris_the_Traitor_King_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sedris_2026-10-15/gate_output/Sedris_the_Traitor_King_Rules_Attestation.json) → “Twilight Diviner”
- Source (re-verified): [`Sedris_the_Traitor_King_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sedris_2026-10-15/gate_output/Sedris_the_Traitor_King_Rules_Attestation.json) → “Panharmonicon ETB package”

## Zones, commander tax and the command zone

### sedris-06: Graveyard setup: Ripples of Undeath, Undercity Sewers; Grim Monolith is just ramp

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Sedris, the Traitor King, Ripples of Undeath, Undercity Sewers, Grim Monolith

**Ruling.** Ripples of Undeath mills three at the start of your first main phase, then you may pay {1} and 3 life to take one into hand. The rest stay in the graveyard for unearth. Undercity Sewers is an Island Swamp, so fetchlands find it, and it surveils 1 on entering. Grim Monolith only helps cast six-mana Sedris; the list has no Power Artifact package.

**Citations**

- Oracle, *Ripples of Undeath*: “At the beginning of your first main phase, mill three cards. Then you may pay {1} and 3 life. If you do, put a card from among those cards into your hand.”
- [CR 701.17a](#cr-70117a), [CR 701.25a](#cr-70125a)
- Source (re-verified): [`Sedris_the_Traitor_King_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sedris_2026-10-15/gate_output/Sedris_the_Traitor_King_Rules_Attestation.json) → “Ripples of Undeath”
- Source (re-verified): [`Sedris_the_Traitor_King_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sedris_2026-10-15/gate_output/Sedris_the_Traitor_King_Rules_Attestation.json) → “Undercity Sewers”
- Source (re-verified): [`Sedris_the_Traitor_King_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/sedris_2026-10-15/gate_output/Sedris_the_Traitor_King_Rules_Attestation.json) → “Grim Monolith role”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 111.1

Some effects put tokens onto the battlefield. A token is a marker used to represent any permanent that isn’t represented by a card.

#### CR 400.7

An object that moves from one zone to another becomes a new object with no memory of, or relation to, its previous existence. This rule has the following exceptions.

#### CR 601.2f

The player determines the total cost of the spell. Usually this is just the mana cost. Some spells have additional or alternative costs. Some effects may increase or reduce the cost to pay, or may provide other alternative costs. Costs may include paying mana, tapping permanents, sacrificing permanents, discarding cards, and so on. The total cost is the mana cost or alternative cost (as determined in rule 601.2b), plus all additional costs and cost increases, and minus all cost reductions. If multiple cost reductions apply, the player may apply them in any order. If the mana component of the …

#### CR 602.2b

The remainder of the process for activating an ability is identical to the process for casting a spell listed in rules 601.2b–i. Those rules apply to activating an ability just as they apply to casting a spell. An activated ability’s analog to a spell’s mana cost (as referenced in rule 601.2f) is its activation cost.

#### CR 602.5d

Activated abilities that read “Activate only as a sorcery” mean the player must follow the timing rules for casting a sorcery spell, though the ability isn’t actually a sorcery. The player doesn’t actually need to have a sorcery card that they could cast.

#### CR 603.6a

Enters-the-battlefield abilities trigger when a permanent enters the battlefield. These are written, “When [this object] enters, . . . “ or “Whenever a [type] enters, . . .” Each time an event puts one or more permanents onto the battlefield, all permanents on the battlefield (including the newcomers) are checked for any enters-the-battlefield triggers that match the event.

#### CR 603.7

An effect may create a delayed triggered ability that can do something at a later time. A delayed triggered ability will contain “when,” “whenever,” or “at,” although that word won’t usually begin the ability.

#### CR 701.17a

For a player to mill a number of cards, that player puts that many cards from the top of their library into their graveyard.

#### CR 701.25a

To “surveil N” means to look at the top N cards of your library, then put any number of them into your graveyard and the rest on top of your library in any order.

#### CR 702.26b

If a permanent phases out, its status changes to “phased out.” Except for rules and effects that specifically mention phased-out permanents, a phased-out permanent is treated as though it does not exist. It can’t affect or be affected by anything else in the game. A permanent that phases out is removed from combat. (See rule 506.4.)

#### CR 702.84a

Unearth is an activated ability that functions while the card with unearth is in a graveyard. “Unearth [cost]” means “[Cost]: Return this card from your graveyard to the battlefield. It gains haste. Exile it at the beginning of the next end step. If it would leave the battlefield, exile it instead of putting it anywhere else. Activate only as a sorcery.”

#### CR 702.95a

Soulbond is a keyword that represents two triggered abilities. “Soulbond” means “When this creature enters, if you control both this creature and another creature and both are unpaired, you may pair this creature with another unpaired creature you control for as long as both remain creatures on the battlefield under your control” and “Whenever another creature you control enters, if you control both that creature and this one and both are unpaired, you may pair that creature with this creature for as long as both remain creatures on the battlefield under your control.”

#### CR 724.1b

Exile every object on the stack, including the object that’s resolving. All objects not on the battlefield or in the command zone that aren’t represented by cards will cease to exist the next time state-based actions are checked (see rule 704, “State-Based Actions”).

