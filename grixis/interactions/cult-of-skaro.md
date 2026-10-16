---
title: "Cult of Skaro — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Cult of Skaro — Interaction Review

> Bot cycle 46 · batch A · reviewed 2026-10-16. Deck: [Cult of Skaro](../decks/cult-of-skaro.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/cult-of-skaro.txt`](../../exports/grixis-archidekt/cult-of-skaro.txt) · SHA-256 `e17919e46769952d0318157693b278c29ba9a39a352105fa76df9abb9a868e7d` |
| Rulings | **10** (10 verified · 0 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`Cult_of_Skaro_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cult_of_skaro_2026-10-14/Cult_of_Skaro_Rules_Attestation.json) (11 interactions, all PASS) |

## Contents
- [Summary](#summary)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Key card-pair interactions](#key-card-pair-interactions)
- [Layers and continuous effects](#layers-and-continuous-effects)
- [Timing and priority](#timing-and-priority)
- [Trigger ordering](#trigger-ordering)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [Rules cited](#rules-cited)

## Summary

Cult of Skaro is a Dalek artifact-aggro deck whose attack trigger picks a random mode. This review re-verifies all eleven items of the deck's rules attestation.

Rules points:
- Copies (Strionic Resonator, Scientist Supreme) repeat the rolled mode; Roaming Throne gives a fresh roll.
- The Master, Multiplied keeps myriad tokens.

No list errors.

## Commander rules text and edge cases

### skaro-01: The random mode is chosen as the trigger goes on the stack

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Cult of Skaro

**Ruling.** Cult of Skaro's attack trigger is modal, with the mode chosen at random. Modes are chosen when a triggered ability is put on the stack, so everyone knows the result before anyone responds. It triggers on being *declared* as an attacker, not on entering attacking.
- **Thay:** +1/+1 counter on each artifact creature you control.
- **Caan:** draw two.
- **Sec:** a 3/3 menace Dalek token.
- **Jast:** each opponent loses 4.

**Citations**

- Oracle, *Cult of Skaro*: “Whenever Cult of Skaro attacks, choose one at random —”
- [CR 603.3c](#cr-6033c), [CR 700.2](#cr-7002), [CR 508.1m](#cr-5081m)
- Source (re-verified): [`Cult_of_Skaro_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cult_of_skaro_2026-10-14/Cult_of_Skaro_Rules_Attestation.json) → “Cult of Skaro attack trigger and random mode timing”

## Combos and engine lines

### skaro-05: Sword of Feast and Famine + Aggravated Assault

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Cult of Skaro, Sword of Feast and Famine, Aggravated Assault

**Ruling.** When the equipped creature connects, Sword untaps all your lands. In the next main phase, Aggravated Assault ({3}{R}{R}, sorcery speed) untaps your creatures and adds another combat and main phase. Repeat for unlimited combats, with each Cult attack rolling again. You need lands producing {3}{R}{R} and a creature that connects.

**Citations**

- Oracle, *Aggravated Assault*: “{3}{R}{R}: Untap all creatures you control. After this main phase, there is an additional combat phase followed by an additional main phase. Activate only as a sorcery.”
- [CR 500.8](#cr-5008), [CR 505.1a](#cr-5051a)
- Source (re-verified): [`Cult_of_Skaro_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cult_of_skaro_2026-10-14/Cult_of_Skaro_Rules_Attestation.json) → “Aggravated Assault + Sword of Feast and Famine”

## Key card-pair interactions

### skaro-03: Helm of the Host, Spark Double, Sakashima, Auton Soldier copies

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Cult of Skaro, Helm of the Host, Spark Double, Sakashima of a Thousand Faces, Auton Soldier

**Ruling.** These copies of Cult each have the attack trigger:
- **Helm of the Host:** a hasty nonlegendary token copy at each beginning of combat on your turn, including extra combats.
- **Spark Double and Auton Soldier:** nonlegendary copies.
- **Sakashima:** turns off the legend rule for your permanents.

Each copy declared as an attacker rolls its own mode. Myriad tokens (from Auton Soldier) enter attacking and weren't declared, so their copied Cult trigger doesn't fire that combat.

**Citations**

- Oracle, *Helm of the Host*: “At the beginning of combat on your turn, create a token that's a copy of equipped creature, except the token isn't legendary. That token gains haste.”
- [CR 707.9b](#cr-7079b), [CR 702.116a](#cr-702116a), [CR 508.4](#cr-5084)
- Source (re-verified): [`Cult_of_Skaro_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cult_of_skaro_2026-10-14/Cult_of_Skaro_Rules_Attestation.json) → “Cult of Skaro + Helm of the Host”
- Source (re-verified): [`Cult_of_Skaro_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cult_of_skaro_2026-10-14/Cult_of_Skaro_Rules_Attestation.json) → “Auton Soldier copy of Cult and myriad tokens”

### skaro-04: The Master, Multiplied keeps myriad tokens

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Cult of Skaro, The Master, Multiplied, Dalek Squadron, Auton Soldier, Cybermen Squadron

**Ruling.** The Master stops your triggered abilities from sacrificing or exiling your creature tokens, so myriad's 'exile at end of combat' trigger does nothing. Dalek Squadron, Auton Soldier and Cybermen Squadron's myriad tokens stay. It also turns off the legend rule for creature tokens. Those tokens weren't declared attackers the combat they appeared, but they can attack in later combats and trigger their own abilities (myriad, a copied Cult trigger).

**Citations**

- Oracle, *The Master, Multiplied*: “Triggered abilities you control can't cause you to sacrifice or exile creature tokens you control.”
- Scryfall ruling, *The Master, Multiplied*: “Notably, the part of myriad that makes you exile the creature tokens at end of combat is a triggered ability. This means that the ability will trigger, but you won't exile the tokens when it resolves.”
- [CR 702.116a](#cr-702116a), [CR 704.5j](#cr-7045j)

### skaro-07: Arena of Glory haste; Plaza of Heroes protection

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Cult of Skaro, Arena of Glory, Plaza of Heroes

**Ruling.** Arena of Glory's exert mana gives haste to a creature spell it's spent on, so a fresh Cult can attack that turn. Plaza of Heroes can exile itself to give a legendary creature hexproof and indestructible until end of turn.

**Citations**

- Oracle, *Arena of Glory*: “If any of that mana is spent on a creature spell, it gains haste until end of turn.”
- [CR 701.43a](#cr-70143a), [CR 702.12b](#cr-70212b)
- Source (re-verified): [`Cult_of_Skaro_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cult_of_skaro_2026-10-14/Cult_of_Skaro_Rules_Attestation.json) → “Arena of Glory haste line”
- Source (re-verified): [`Cult_of_Skaro_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cult_of_skaro_2026-10-14/Cult_of_Skaro_Rules_Attestation.json) → “Plaza of Heroes protection line”

### skaro-08: Exterminate! replicates by tapping Daleks

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Cult of Skaro, Exterminate!, Davros, Dalek Creator

**Ruling.** Exterminate!'s replicate cost is tapping an untapped Dalek. Cult, Davros's tokens, Dalek Squadron and the Sec tokens all count. Each payment adds a copy (destroy a creature, its controller loses 3). Daleks that attacked are tapped unless untapped again, so cast it before combat or after an untap.

**Citations**

- Oracle, *Exterminate!*: “Replicate—Tap an untapped Dalek you control.”
- [CR 702.56a](#cr-70256a)

## Layers and continuous effects

### skaro-09: Biotransference and Their Name Is Death or Delete

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Cult of Skaro, Biotransference, Their Name Is Death, Delete

**Ruling.** Biotransference makes your creatures artifacts, so Their Name Is Death (nonartifact creatures) and Delete (nonartifact creatures) spare them. Cult and the Daleks are artifacts already. Thay's counters go on every artifact creature you control, so with Biotransference that's every creature.

**Citations**

- Oracle, *Biotransference*: “Creatures you control are artifacts in addition to their other types.”
- [CR 613.1d](#cr-6131d)

## Timing and priority

### skaro-06: Full Throttle and Great Train Heist extra combats

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Cult of Skaro, Full Throttle, Great Train Heist

**Ruling.** - **Full Throttle:** cast in a main phase, it adds two combats (no main phase between them) and untaps the creatures that attacked at the start of each combat that turn.
- **Great Train Heist:** the first spree mode during your combat untaps your creatures and adds one more combat right after, with no main phase.

Each new attack with Cult rolls again.

**Citations**

- Scryfall ruling, *Full Throttle*: “There is no main phase between the two additional combat phases.”
- Scryfall ruling, *Great Train Heist*: “Notably, Great Train Heist’s first mode doesn’t give you any additional main phases.”
- [CR 500.8](#cr-5008), [CR 702.172a](#cr-702172a)
- Source (re-verified): [`Cult_of_Skaro_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cult_of_skaro_2026-10-14/Cult_of_Skaro_Rules_Attestation.json) → “Full Throttle additional combats”
- Source (re-verified): [`Cult_of_Skaro_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cult_of_skaro_2026-10-14/Cult_of_Skaro_Rules_Attestation.json) → “Great Train Heist additional combat mode”

## Trigger ordering

### skaro-02: Copies keep the mode; extra triggers re-roll

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Cult of Skaro, Strionic Resonator, Scientist Supreme of A.I.M., Roaming Throne

**Ruling.** - **Strionic Resonator ({2}, {T}) and Scientist Supreme (pay 2 life, once per turn, your turn, artifact source):** these *copy* the trigger, and a copy keeps the already chosen mode.
- **Roaming Throne (naming Dalek):** makes Cult trigger an additional time, a separate trigger that rolls its own random mode.

Use copies when you like the roll; Throne gives more chances.

**Citations**

- Oracle, *Scientist Supreme of A.I.M.*: “Pay 2 life: Copy target activated or triggered ability you control from an artifact source. You may choose new targets for the copy. Activate only during your turn and only once each turn.”
- [CR 707.10](#cr-70710), [CR 603.3c](#cr-6033c), [CR 603.2](#cr-6032)
- Source (re-verified): [`Cult_of_Skaro_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cult_of_skaro_2026-10-14/Cult_of_Skaro_Rules_Attestation.json) → “Cult of Skaro + Strionic Resonator”
- Source (re-verified): [`Cult_of_Skaro_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cult_of_skaro_2026-10-14/Cult_of_Skaro_Rules_Attestation.json) → “Cult of Skaro + Scientist Supreme of A.I.M.”
- Source (re-verified): [`Cult_of_Skaro_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cult_of_skaro_2026-10-14/Cult_of_Skaro_Rules_Attestation.json) → “Cult of Skaro + Roaming Throne”

## Zones, commander tax and the command zone

### skaro-10: Commander tax and artifact recursion

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Cult of Skaro, Academy Ruins

**Ruling.** Cult costs {1}{U}{B}{R}, then 6, then 8. It's an artifact, so if you leave it in the graveyard Academy Ruins can put it on top of your library.

**Citations**

- Oracle, *Academy Ruins*: “{1}{U}, {T}: Put target artifact card from your graveyard on top of your library.”
- [CR 903.8](#cr-9038), [CR 903.9a](#cr-9039a)

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 500.8

Some effects can add phases to a turn. They do this by adding the phases directly after the specified phase. If multiple extra phases are created after the same phase, the most recently created phase will occur first.

#### CR 505.1a

Only the first main phase of the turn is a precombat main phase. All other main phases are postcombat main phases. This includes the second main phase of a turn in which the combat phase has been skipped. It is also true of a turn in which an effect has caused an additional combat phase and an additional main phase to be created.

#### CR 508.1m

Any abilities that trigger on attackers being declared trigger.

#### CR 508.4

If a creature is put onto the battlefield attacking, its controller chooses which defending player, planeswalker a defending player controls, or battle a defending player protects it’s attacking as it enters the battlefield (unless the effect that put it onto the battlefield specifies what it’s attacking). Similarly, if an effect states that a creature is attacking, its controller chooses which defending player, planeswalker a defending player controls, or battle a defending player protects it’s attacking (unless the effect has already specified). Such creatures are “attacking” but, for the …

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 603.3c

If a triggered ability is modal, its controller announces the mode choice when putting the ability on the stack. If one of the modes would be illegal (due to an inability to choose legal targets, for example), that mode can’t be chosen. If no mode is chosen, the ability is removed from the stack. (See rule 700.2.)

#### CR 613.1d

Layer 4: Type-changing effects are applied. These include effects that change an object’s card type, subtype, and/or supertype.

#### CR 700.2

A spell or ability is modal if it has two or more options in a bulleted list preceded by instructions for a player to choose a number of those options, such as “Choose one —.” Each of those options is a mode. Modal cards printed prior to the Khans of Tarkir™ set didn’t use bulleted lists for the modes; these cards have received errata in the Oracle card reference so the modes do appear in a bulleted list.

#### CR 701.43a

To exert a permanent, you choose to have it not untap during your next untap step.

#### CR 702.12b

A permanent with indestructible can’t be destroyed. Such permanents aren’t destroyed by lethal damage, and they ignore the state-based action that checks for lethal damage (see rule 704.5g).

#### CR 702.56a

Replicate is a keyword that represents two abilities. The first is a static ability that functions while the spell with replicate is on the stack. The second is a triggered ability that functions while the spell with replicate is on the stack. “Replicate [cost]” means “As an additional cost to cast this spell, you may pay [cost] any number of times” and “When you cast this spell, if a replicate cost was paid for it, copy it for each time its replicate cost was paid. If the spell has any targets, you may choose new targets for any of the copies.” Paying a spell’s replicate cost follows the …

#### CR 702.116a

Myriad is a triggered ability that may also create a delayed triggered ability. “Myriad” means “Whenever this creature attacks, for each opponent other than defending player, you may create a token that’s a copy of this creature that’s tapped and attacking that player or a planeswalker they control. If one or more tokens are created this way, exile the tokens at end of combat.”

#### CR 702.172a

Spree is a static ability found on some modal spells (see rule 700.2) that applies while the spell on the stack. Spree means “Choose one or more modes. As an additional cost to cast this spell, pay the costs associated with those modes.”

#### CR 704.5j

If two or more legendary permanents with the same name are controlled by the same player, that player chooses one of them, and the rest are put into their owners’ graveyards. This is called the “legend rule.”

#### CR 707.9b

Some copy effects modify a characteristic as part of the copying process. The final set of values for that characteristic becomes part of the copiable values of the copy.

#### CR 707.10

To copy a spell, activated ability, or triggered ability means to put a copy of it onto the stack; a copy of a spell isn’t cast and a copy of an activated ability isn’t activated. A copy of a spell or ability copies both the characteristics of the spell or ability and all decisions made for it, including modes, targets, the value of X, and additional or alternative costs. (See rule 601, “Casting Spells.”) Choices that are normally made on resolution are not copied. If an effect of the copy refers to objects used to pay its costs, it uses the objects used to pay the costs of the original spell …

#### CR 903.8

A player may cast a commander they own from the command zone. A commander cast from the command zone costs an additional {2} for each previous time the player casting it has cast it from the command zone that game. This additional cost is informally known as the “commander tax.”

#### CR 903.9a

If a commander is in a graveyard or in exile and that object was put into that zone since the last time state-based actions were checked, its owner may put it into the command zone. This is a state-based action. See rule 704.

