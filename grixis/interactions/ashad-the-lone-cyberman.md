---
title: "Ashad, the Lone Cyberman — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Ashad, the Lone Cyberman — Interaction Review

> Bot cycle 46 · batch A · reviewed 2026-10-16. Deck: [Ashad, the Lone Cyberman](../decks/ashad-the-lone-cyberman.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-15), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/ashad-the-lone-cyberman.txt`](../../exports/grixis-archidekt/ashad-the-lone-cyberman.txt) · SHA-256 `13fa3b590700b08a41783ab763a1055f9f82103db01a3757a3662be7a092637c` |
| Rulings | **14** (13 verified · 1 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-15 · rulings 2026-10-15 |
| Source attestations | [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) (deck #5: RULES PASS) |

## Contents
- [Summary](#summary)
- [Flags and open questions](#flags-and-open-questions)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [Key card-pair interactions](#key-card-pair-interactions)
- [Layers and continuous effects](#layers-and-continuous-effects)
- [Timing and priority](#timing-and-priority)
- [Replacement and prevention effects](#replacement-and-prevention-effects)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [Rules cited](#rules-cited)

## Summary

Ashad, the Lone Cyberman is an artifact engine. Casualty 2 on the first nonlegendary artifact spell each turn turns it into a token copy. This review re-verifies the retrospective attestation (Twinning Staff, Solemn and Ichor Wellspring copies, flash timing, 'another creature').

Rules surprises:
- Casualty copies aren't 'created' tokens, so Worldwalker Helm adds no Map.
- Biotransference makes your creatures artifacts, so your own Delete and Their Name Is Death spare them.

No list errors.

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [ashad-14](#ashad-14-ashads-casualty-copy-of-worldwalker-helm-as-the-starting-token) | ⚠️ uncertain | Ashad's casualty copy of Worldwalker Helm as the starting token | Reconstructed from Oracle text and CR 111.13; not a Commander Spellbook variant. It needs a second untapped artifact for the first {U}{U}. |

## Commander rules text and edge cases

### ashad-01: Casualty 2 on your first nonlegendary artifact spell

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Ashad, the Lone Cyberman

**Ruling.** The first nonlegendary artifact spell you cast each turn has casualty 2. Sacrificing a creature with power 2 or greater as you cast it copies the spell. The copy of a permanent spell resolves into a token. Only the *first* nonlegendary artifact spell each turn qualifies. Legendary artifacts (The Cyber-Controller, Mox Opal, Iron Man) neither get casualty nor use up the 'first'. Artifact lands are played, not cast.

**Citations**

- Oracle, *Ashad, the Lone Cyberman*: “The first nonlegendary artifact spell you cast each turn has casualty 2.”
- Scryfall ruling, *Ashad, the Lone Cyberman*: “You may sacrifice only one creature to pay a spell's casualty cost, and you copy the spell only once.”
- Scryfall ruling, *Ashad, the Lone Cyberman*: “The copy of the spell is created on the stack, so it's not "cast." Abilities that trigger when a player casts a spell won't trigger.”
- [CR 702.153a](#cr-702153a), [CR 707.10f](#cr-70710f), [CR 608.3f](#cr-6083f)
- Source (re-verified): [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) → “the copied permanent spell is not cast and becomes a token as it resolves.”

### ashad-02: The +1/+1 trigger needs *another* creature sacrificed

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Ashad, the Lone Cyberman, Ashnod's Altar, Phyrexian Altar

**Ruling.** Ashad gets a +1/+1 counter whenever you sacrifice another creature: casualty payments, Ashnod's Altar, Phyrexian Altar, Krark-Clan Ironworks on an artifact creature. Sacrificing Ashad itself doesn't count.

**Citations**

- Oracle, *Ashad, the Lone Cyberman*: “Whenever you sacrifice another creature, put a +1/+1 counter on Ashad.”
- [CR 701.21a](#cr-70121a)
- Source (re-verified): [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) → “Ashad's +1/+1 trigger is for sacrificing **another** creature”

## Combos and engine lines

### ashad-05: Urza + Worldwalker Helm + Artificer Class

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Ashad, the Lone Cyberman, Urza, Lord High Artificer, Worldwalker Helm, Artificer Class

**Ruling.** Commander Spellbook (66-457-5491, cached) lists this as infinite artifact tokens and blue mana. Its line, with Artificer Class at level 3:
1. At your end step, the Class makes a token copy of Worldwalker Helm plus a Map.
2. Urza taps a Helm and a Map for {U}{U}.
3. A Helm token copies itself ({1}{U}, {T}), creating another Helm token plus a Map *for each Helm you control*.
4. Urza taps two Maps for {U}{U}. Repeat from step 3.

Urza's {5} then exiles and plays the library.

**Citations**

- Oracle, *Worldwalker Helm*: “{1}{U}, {T}: Create a token that's a copy of target artifact token you control.”
- Oracle, *Urza, Lord High Artificer*: “Tap an untapped artifact you control: Add {U}.”
- Oracle, *Artificer Class*: “At the beginning of your end step, create a token that's a copy of target artifact you control.”
- Scryfall ruling, *Worldwalker Helm*: “Worldwaker Helm's first ability applies to all kinds of artifact tokens that its controller creates, not just Map tokens.”
- [CR 605.1a](#cr-6051a), [CR 614.1a](#cr-6141a)
- Commander Spellbook [66-457-5491](https://commanderspellbook.com/combo/66-457-5491/) (community-maintained, retrieved 2026-10-16): “Activate a Worldwalker Helm by paying {1}{U} and tapping it, creating a token copy of the Worldwalker Helm token plus a Map token for each Worldwalker Helm you control.”

### ashad-14: Ashad's casualty copy of Worldwalker Helm as the starting token

**Status:** ⚠️ uncertain · **Evidence:** hypothesis · **Cards:** Ashad, the Lone Cyberman, Urza, Lord High Artificer, Worldwalker Helm

**Ruling.** Our derivation, not a Spellbook line. Casting Worldwalker Helm as your first nonlegendary artifact spell with casualty gives a token Helm. It isn't 'created', so no Map, but it's an artifact token that Helm's ability can target. With Urza, tap the nontoken Helm and another artifact for {U}{U}, then activate the token Helm. It copies itself and gets two Maps (two Helms on the battlefield), and steps 3–4 of the Spellbook line follow without Artificer Class.

**Uncertain.** Reconstructed from Oracle text and CR 111.13; not a Commander Spellbook variant. It needs a second untapped artifact for the first {U}{U}.

**Citations**

- Oracle, *Ashad, the Lone Cyberman*: “The first nonlegendary artifact spell you cast each turn has casualty 2.”
- [CR 111.13](#cr-11113), [CR 608.3f](#cr-6083f), [CR 702.153a](#cr-702153a)

## Engines and payoffs

### ashad-09: Sacrifice and artifact-death drains

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Ashad, the Lone Cyberman, Disciple of the Vault, Marionette Master, Mayhem Devil, Ingenious Artillerist, Reckless Fireweaver

**Ruling.** - **Artifact leaves the battlefield:** artifact tokens are put into the graveyard before ceasing to exist, so Disciple of the Vault and Marionette Master trigger for each sacrificed Treasure, Servo or casualty token.
- **Any sacrifice:** Mayhem Devil triggers on each one, including the casualty payment and opponents' sacrifices.
- **Artifacts entering:** Ingenious Artillerist and Reckless Fireweaver trigger on each artifact that enters, tokens from casualty included.

**Citations**

- Oracle, *Disciple of the Vault*: “Whenever an artifact is put into a graveyard from the battlefield, you may have target opponent lose 1 life.”
- Oracle, *Mayhem Devil*: “Whenever a player sacrifices a permanent, this creature deals 1 damage to any target.”
- [CR 700.4](#cr-7004), [CR 603.10a](#cr-60310a), [CR 704.5d](#cr-7045d)

## Key card-pair interactions

### ashad-07: Iron Man copies legendary artifacts as nonlegendary

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Ashad, the Lone Cyberman, Iron Man, Bleeding Edge, The Cyber-Controller

**Ruling.** Iron Man's once-per-turn copy works on any artifact spell, including legendary ones (the copy isn't legendary). It covers The Cyber-Controller, which Ashad can't copy; the copy keeps X. On a nonlegendary spell, Ashad's casualty copy and Iron Man's copy stack. Twinning Staff adds one to each copy event.

**Citations**

- Oracle, *Iron Man, Bleeding Edge*: “Whenever you cast an artifact spell, you may copy it, except the copy isn't legendary. Do this only once each turn.”
- [CR 707.10](#cr-70710), [CR 707.9b](#cr-7079b)

### ashad-10: Myriad: Cybermen Squadron and Auton Soldier

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Ashad, the Lone Cyberman, Cybermen Squadron, Auton Soldier

**Ruling.** Cybermen Squadron gives nonlegendary artifact creatures myriad, so Ashad (legendary) doesn't get it. Myriad tokens enter attacking but weren't declared as attackers, so 'whenever attacks' abilities don't trigger for them. The tokens are exiled at end of combat. With only one opponent left, myriad makes nothing.

**Citations**

- Scryfall ruling, *Cybermen Squadron*: “Although the tokens enter the battlefield attacking, they were never declared as attackers.”
- Scryfall ruling, *Cybermen Squadron*: “If the defending player is your only opponent, no tokens are put onto the battlefield.”
- [CR 702.116a](#cr-702116a), [CR 508.4](#cr-5084)

### ashad-11: Esoteric Duplicator rebuys sacrificed artifacts

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Ashad, the Lone Cyberman, Esoteric Duplicator, Ashnod's Altar

**Ruling.** Whenever you sacrifice Duplicator or another artifact (artifact creatures to an altar or casualty, Treasures, KCI fodder), you may pay {2} for an end-step token copy. The copy copies the printed card (or the original token characteristics) without counters. Its enter triggers work.

**Citations**

- Scryfall ruling, *Esoteric Duplicator*: “If the copied artifact was a token, the token that’s created copies the original characteristics of that token as stated by the effect that created that token.”
- [CR 707.2](#cr-7072), [CR 603.6a](#cr-6036a)

### ashad-12: Portal to Phyrexia with casualty

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Ashad, the Lone Cyberman, Portal to Phyrexia

**Ruling.** Portal to Phyrexia is a nonlegendary artifact spell. A casualty copy resolves into a token Portal with its own enter trigger, so each opponent sacrifices three creatures twice, and you get two upkeep reanimation triggers.

**Citations**

- Oracle, *Portal to Phyrexia*: “When this artifact enters, each opponent sacrifices three creatures of their choice.”
- [CR 608.3f](#cr-6083f)

## Layers and continuous effects

### ashad-06: Biotransference makes creature spells artifact spells

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Ashad, the Lone Cyberman, Biotransference, Delete, Their Name Is Death

**Ruling.** Biotransference makes your creature spells, your creatures and your creature cards in other zones artifacts too.
- Nonlegendary creature spells (Mayhem Devil, Marionette Master, Pitiless Plunderer) become eligible for Ashad's casualty, artifact cost reducers and Jhoira.
- Delete and Their Name Is Death hit only nonartifact creatures, so they spare your board.

The effect is a layer 4 type change. Replacement effects that modify artifacts entering apply after it.

**Citations**

- Oracle, *Biotransference*: “Creatures you control are artifacts in addition to their other types. The same is true for creature spells you control and creature cards you own that aren't on the battlefield.”
- Oracle, *Delete*: “Delete deals X damage to each nonartifact creature and each player.”
- Scryfall ruling, *Biotransference*: “Replacement effects that modify artifacts as they enter the battlefield will apply after you apply Biotransference's effect.”
- [CR 613.1d](#cr-6131d), [CR 205.1b](#cr-2051b)

## Timing and priority

### ashad-08: Flash artifacts reuse 'first each turn' on other turns

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Ashad, the Lone Cyberman, Shimmer Myr

**Ruling.** Ashad's casualty resets every turn, not just yours. With Shimmer Myr, artifact spells can be cast at instant speed, so you can cast a nonlegendary artifact with casualty on each opponent's turn. Artifact lands aren't affected (they're played).

**Citations**

- Oracle, *Shimmer Myr*: “You may cast artifact spells as though they had flash.”
- Scryfall ruling, *Shimmer Myr*: “Shimmer Myr has no effect on artifact lands because they aren't cast as spells.”
- [CR 702.8a](#cr-7028a), [CR 702.153a](#cr-702153a)
- Source (re-verified): [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) → “Flash-granting artifact infrastructure can exploit Ashad's “first ... each turn” wording on other players' turns”

## Replacement and prevention effects

### ashad-03: Casualty tokens aren't 'created': no Worldwalker Helm Map

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Ashad, the Lone Cyberman, Worldwalker Helm, Simulacrum Synthesizer, Ichor Wellspring, Solemn Simulacrum

**Ruling.** A copy of a permanent spell becomes a token as it resolves but isn't 'created' for replacement effects or triggers that refer to creating tokens. Worldwalker Helm adds no Map for Ashad's copy.

Enter triggers still work: the token Solemn Simulacrum fetches a land, the token Ichor Wellspring draws, and Simulacrum Synthesizer sees an artifact with MV 3 or more enter, because the copy keeps the mana cost.

**Citations**

- Oracle, *Worldwalker Helm*: “If you would create one or more artifact tokens, instead create those tokens plus an additional Map token.”
- [CR 111.13](#cr-11113), [CR 608.3f](#cr-6083f)
- Source (re-verified): [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) → “A copied `Solemn Simulacrum` spell resolves as its own token permanent and supplies its own enter-the-battlefield trigger.”

### ashad-04: Twinning Staff applies to artifact spell copies

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Ashad, the Lone Cyberman, Twinning Staff

**Ruling.** Twinning Staff's replacement covers copying any spell, so an Ashad casualty copy becomes two copies (two tokens). Staff's {7} activated ability is the part limited to instants and sorceries.

**Citations**

- Oracle, *Twinning Staff*: “If you would copy a spell one or more times, instead copy it that many times plus an additional time.”
- [CR 614.1a](#cr-6141a), [CR 707.10](#cr-70710)
- Source (re-verified): [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) → “That replacement effect is not limited to instants and sorceries; therefore it applies to Ashad copying a nonlegendary artifact permanent spell.”

## Zones, commander tax and the command zone

### ashad-13: Commander tax and Ashad's artifact type

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Ashad, the Lone Cyberman, Academy Ruins

**Ruling.** Ashad is a four-mana legendary artifact creature ({1}{U}{B}{R}, then 6, 8). As a legendary it doesn't trigger its own casualty, and Cybermen Squadron doesn't give it myriad. If Ashad goes to the graveyard you may move it to the command zone. If you leave it there, Academy Ruins can put it on top of the library because it's an artifact card.

**Citations**

- Oracle, *Academy Ruins*: “{1}{U}, {T}: Put target artifact card from your graveyard on top of your library.”
- [CR 903.8](#cr-9038), [CR 903.9a](#cr-9039a)

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 111.13

A copy of a permanent spell becomes a token as it resolves. The token has the characteristics of the spell that became that token. The token is not “created” for the purposes of any replacement effects or triggered abilities that refer to creating a token.

#### CR 205.1b

Some effects change an object’s card type, supertype, or subtype but specify that the object retains a prior card type, supertype, or subtype. In such cases, all the object’s prior card types, supertypes, and subtypes are retained. This rule applies to effects that use phrases such as “in addition to its other types” or that state that something is “still a [type, supertype, or subtype].” Some effects state that an object becomes an “artifact creature”; these effects also allow the object to retain all of its prior card types and subtypes. Some effects state that an object becomes a …

#### CR 508.4

If a creature is put onto the battlefield attacking, its controller chooses which defending player, planeswalker a defending player controls, or battle a defending player protects it’s attacking as it enters the battlefield (unless the effect that put it onto the battlefield specifies what it’s attacking). Similarly, if an effect states that a creature is attacking, its controller chooses which defending player, planeswalker a defending player controls, or battle a defending player protects it’s attacking (unless the effect has already specified). Such creatures are “attacking” but, for the …

#### CR 603.6a

Enters-the-battlefield abilities trigger when a permanent enters the battlefield. These are written, “When [this object] enters, . . . “ or “Whenever a [type] enters, . . .” Each time an event puts one or more permanents onto the battlefield, all permanents on the battlefield (including the newcomers) are checked for any enters-the-battlefield triggers that match the event.

#### CR 603.10a

Some zone-change triggers look back in time. These are leaves-the-battlefield abilities, abilities that trigger when a player sacrifices a permanent, abilities that trigger when a card leaves a graveyard, and abilities that trigger when an object that all players can see is put into a hand or library.

#### CR 605.1a

An activated ability is a mana ability if it meets all of the following criteria: it doesn’t require a target (see rule 115.6), it could add mana to a player’s mana pool when it resolves, it’s not a loyalty ability (see rule 606, “Loyalty Abilities”), and its cost and effect don’t move any card to or from a library. Do not take into account replacement effects that may apply, other than self-replacement effects, when evaluating these criteria.

#### CR 608.3f

If the object that’s resolving is a copy of a permanent spell, it will become a token permanent as it is put onto the battlefield in any of the steps above. A token put onto the battlefield this way is no longer a copy of a spell and is not “created” for the purposes of any rules or effects that refer to creating a token.

#### CR 613.1d

Layer 4: Type-changing effects are applied. These include effects that change an object’s card type, subtype, and/or supertype.

#### CR 614.1a

Effects that use the word “instead” are replacement effects. Most replacement effects use the word “instead” to indicate what events will be replaced with other events.

#### CR 700.4

The term dies means “is put into a graveyard from the battlefield.”

#### CR 701.21a

To sacrifice a permanent, its controller moves it from the battlefield directly to its owner’s graveyard. A player can’t sacrifice something that isn’t a permanent, or something that’s a permanent they don’t control. Sacrificing a permanent doesn’t destroy it, so regeneration or other effects that replace destruction can’t affect this action.

#### CR 702.8a

Flash is a static ability that functions in any zone from which you could play the card it’s on. “Flash” means “You may play this card any time you could cast an instant.”

#### CR 702.116a

Myriad is a triggered ability that may also create a delayed triggered ability. “Myriad” means “Whenever this creature attacks, for each opponent other than defending player, you may create a token that’s a copy of this creature that’s tapped and attacking that player or a planeswalker they control. If one or more tokens are created this way, exile the tokens at end of combat.”

#### CR 702.153a

Casualty is a keyword that represents two abilities. The first is a static ability that functions while the spell with casualty is on the stack. The second is a triggered ability that functions while the spell with casualty is on the stack. Casualty N means “As an additional cost to cast this spell, you may sacrifice a creature with power N or greater,” and “When you cast this spell, if a casualty cost was paid for it, copy it. If the spell has any targets, you may choose new targets for the copy.” Paying a spell’s casualty cost follows the rules for paying additional costs in rules 601.2b …

#### CR 704.5d

If a token is in a zone other than the battlefield, it ceases to exist.

#### CR 707.2

When copying an object, the copy acquires the copiable values of the original object’s characteristics and, for an object on the stack, choices made when casting or activating it (mode, targets, the value of X, whether it was kicked, how it will affect multiple targets, and so on). The copiable values are the values derived from the text printed on the object (that text being name, mana cost, color indicator, card type, subtype, supertype, rules text, power, toughness, and/or loyalty), as modified by other copy effects, by its face-down status, and by “as . . . enters” and “as . . . is turned …

#### CR 707.9b

Some copy effects modify a characteristic as part of the copying process. The final set of values for that characteristic becomes part of the copiable values of the copy.

#### CR 707.10

To copy a spell, activated ability, or triggered ability means to put a copy of it onto the stack; a copy of a spell isn’t cast and a copy of an activated ability isn’t activated. A copy of a spell or ability copies both the characteristics of the spell or ability and all decisions made for it, including modes, targets, the value of X, and additional or alternative costs. (See rule 601, “Casting Spells.”) Choices that are normally made on resolution are not copied. If an effect of the copy refers to objects used to pay its costs, it uses the objects used to pay the costs of the original spell …

#### CR 707.10f

Some effects copy a permanent spell. As that copy resolves, it ceases being a copy of a spell and becomes a token permanent. (See rule 608.3f.)

#### CR 903.8

A player may cast a commander they own from the command zone. A commander cast from the command zone costs an additional {2} for each previous time the player casting it has cast it from the command zone that game. This additional cost is informally known as the “commander tax.”

#### CR 903.9a

If a commander is in a graveyard or in exile and that object was put into that zone since the last time state-based actions were checked, its owner may put it into the command zone. This is a state-based action. See rule 704.

