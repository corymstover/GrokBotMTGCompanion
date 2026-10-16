---
title: "Sol'Kanar the Tainted — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Sol'Kanar the Tainted — Interaction Review

> Bot cycle 56 · batch F · reviewed 2026-10-16. Deck: [Sol'Kanar the Tainted](../decks/solkanar-the-tainted.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-15), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/solkanar-the-tainted.txt`](../../exports/grixis-archidekt/solkanar-the-tainted.txt) · SHA-256 `b1e622ad8c0a49e626d9df8cc87c0def392bb9c13e907216a8b212b790f3fc24` |
| Rulings | **8** (6 verified · 0 uncertain · 2 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-15 · rulings 2026-10-15 |
| Source attestations | [`Solkanar_the_Tainted_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/solkanar_tainted_2026-10-15/gate_output/Solkanar_the_Tainted_Rules_Attestation.json) (Rules attestation (14 items, all PASS) re-verified) · [`Solkanar_the_Tainted_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Solkanar_the_Tainted_Approval_Ready_Verification_2026-10-15.md) (Approval-ready verification) |

## Contents
- [Summary](#summary)
- [Flags and open questions](#flags-and-open-questions)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [Replacement and prevention effects](#replacement-and-prevention-effects)
- [Trigger ordering](#trigger-ordering)
- [What the list depends on](#what-the-list-depends-on)
- [Rules cited](#rules-cited)

## Summary

Sol'Kanar the Tainted is a donate deck. Blink Sol'Kanar with Thassa or Conjurer's Closet to reuse its draw, drain and damage modes; give away Demonic Pact after three modes; donate Immortal Coil and exile the holder's graveyard; or push Captive Audience, Xantcha, Khârn and other liabilities onto opponents. All 4 Spellbook lines and all 14 attestation items are re-verified against the canonical list.

Rules surprises: blinking Sol'Kanar above a pending mode-4 trigger makes it fail on the new object; the earlier modes stay with the Pact no matter who controls it; a donated Pact, Coil, Archfiend or Gambit comes back to you if its holder leaves the game (CR 800.4a), while Captive Audience and Xantcha are exiled instead. One dependency-risk flag (returned liabilities) and one documentation flag (Gambit's trigger is end step, not upkeep). No list errors.

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [tainted-06](#tainted-06-donated-liabilities-come-home-if-the-holder-leaves-the-game) | 🚩 list flag (dependency-risk) | Donated liabilities come home if the holder leaves the game | In multiplayer, killing a Pact / Archfiend / Coil / Gambit holder some other way returns the liability to you (CR 800.4a). Sequence the kills or have removal ready. |
| [tainted-07](#tainted-07-greeds-gambit-the-liabilities-follow-the-controller-and-theyre-at-the-end-step-not-upkeep) | 🚩 list flag (documentation) | Greed's Gambit: the liabilities follow the controller, and they're at the end step, not upkeep | Source attestation says Greed's Gambit's recurring liability is at upkeep; Oracle says end step. |

## Commander rules text and edge cases

### tainted-01: Sol'Kanar's "hasn't been chosen" modes belong to the object; whoever controls it makes the choices

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Sol'Kanar the Tainted

**Ruling.** Sol'Kanar's end-step trigger is modal, and the mode is chosen as it goes on the stack. The record of chosen modes belongs to that Sol'Kanar object. If Sol'Kanar leaves the battlefield and returns, it's a new object and all four modes are available again. A plain control change keeps the history. Once an opponent controls Sol'Kanar, it triggers in their end step and they make every choice: they draw, they drain their opponents (you included), and they pick which of their opponents gets it next.

**Citations**

- Oracle, *Sol'Kanar the Tainted*: “At the beginning of your end step, choose one that hasn't been chosen —”
- Scryfall ruling, *Sol'Kanar the Tainted*: “Once Sol'kanar the Tainted is controlled by your opponent, its ability triggers during that player's end step and that player makes all choices for it. That player draws a card for its first mode and gains life for its second mode, that player's opponents lose life for its second mode, and that player chooses one of their opponents for its last mode.”
- [CR 700.2](#cr-7002), [CR 400.7](#cr-4007), [CR 603.3c](#cr-6033c)
- Source (re-verified): [`Solkanar_the_Tainted_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/solkanar_tainted_2026-10-15/gate_output/Solkanar_the_Tainted_Rules_Attestation.json) → “Sol'Kanar mode history and modal timing”
- Source (re-verified): [`Solkanar_the_Tainted_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/solkanar_tainted_2026-10-15/gate_output/Solkanar_the_Tainted_Rules_Attestation.json) → “Homeward Path and Coveted Falcon recovery”

## Combos and engine lines

### tainted-03: Demonic Pact donation: the recipient inherits the mode history and must take "You lose the game"

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Sol'Kanar the Tainted, Demonic Pact, Donate, Harmless Offering, Blim, Comedic Genius, Coveted Falcon

**Ruling.** Choose Demonic Pact's first three modes yourself, then hand it over with Donate, Harmless Offering, Blim's combat trigger or a face-up Coveted Falcon. It doesn't matter who chose the earlier modes. At the recipient's next upkeep the only mode left is the fourth, so they have to choose it and lose. This is in Spellbook (2770-6676, 3090-6676, 3769-6676, 6676-6922). A Pact trigger that was countered still counts its mode as chosen.

**Citations**

- Scryfall ruling, *Demonic Pact*: “It doesn't matter who has chosen any particular mode. For example, say you control Demonic Pact and have chosen the first two modes. If an opponent gains control of Demonic Pact, that player can choose only the third or fourth mode.”
- Scryfall ruling, *Demonic Pact*: “Yes, if the fourth mode is the only one remaining, you must choose it. You read the whole contract, right?”
- Scryfall ruling, *Demonic Pact*: “If the ability doesn't resolve (either for having its target become illegal or because a spell or ability counters it), the mode chosen for that instance of the ability still counts as being chosen.”
- [CR 700.2](#cr-7002), [CR 613.1b](#cr-6131b)
- Commander Spellbook [2770-6676](https://commanderspellbook.com/combo/2770-6676/) (community-maintained, retrieved 2026-10-16): “The first three modes of Demonic Pact have been selected.”
- Commander Spellbook [2770-6676](https://commanderspellbook.com/combo/2770-6676/) (community-maintained, retrieved 2026-10-16): “At the beginning of the opponent's upkeep, Demonic Pact triggers, causing them to select the fourth mode and lose the game.”
- Source (re-verified): [`Solkanar_the_Tainted_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/solkanar_tainted_2026-10-15/gate_output/Solkanar_the_Tainted_Rules_Attestation.json) → “Demonic Pact transfer”

### tainted-04: Immortal Coil gift: give it away, exile their graveyard, and the state trigger can't be undone

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Sol'Kanar the Tainted, Immortal Coil, Fateful Handoff, Bojuka Bog, Rakdos Charm, Donate

**Ruling.** Give Immortal Coil to an opponent. Fateful Handoff on Coil draws four (MV 4), then hands it over. Then exile their graveyard with Bojuka Bog or Rakdos Charm. Coil's "no cards in your graveyard" is a state trigger for its current controller. Once it has triggered, putting a card into the graveyard doesn't stop it. If the trigger is countered while the graveyard is still empty, it just triggers again. While they hold Coil, damage to them is prevented, so this route kills by the trigger, not by damage.

**Citations**

- Oracle, *Immortal Coil*: “When there are no cards in your graveyard, you lose the game.”
- Oracle, *Fateful Handoff*: “Draw cards equal to the mana value of target artifact or creature you control. An opponent gains control of that permanent.”
- Scryfall ruling, *Immortal Coil*: “The third ability checks whether your graveyard is empty only at the time it triggers. Putting a card into your graveyard after that doesn’t help. You’ll lose the game when the ability resolves.”
- Scryfall ruling, *Immortal Coil*: “If the third ability is countered, but your graveyard is still empty, the ability will immediately trigger again.”
- [CR 603.8](#cr-6038), [CR 202.3](#cr-2023)
- Source (re-verified): [`Solkanar_the_Tainted_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/solkanar_tainted_2026-10-15/gate_output/Solkanar_the_Tainted_Rules_Attestation.json) → “Immortal Coil gift kill”
- Source (re-verified): [`Solkanar_the_Tainted_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/solkanar_tainted_2026-10-15/gate_output/Solkanar_the_Tainted_Rules_Attestation.json) → “Fateful Handoff + Immortal Coil”

## Engines and payoffs

### tainted-08: Support pieces: Mana Vault, Withering Torment, Deflecting Swat

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Sol'Kanar the Tainted, Mana Vault, Withering Torment, Deflecting Swat

**Ruling.** Mana Vault is just three colorless toward the five-mana commander; there's no Vault combo here. Withering Torment is instant-speed creature or enchantment removal and can kill a Pact or Audience you no longer want. You lose 2 only if it resolves. Deflecting Swat is free while you control a commander and protects without shroud.

**Citations**

- Oracle, *Deflecting Swat*: “If you control a commander, you may cast this spell without paying its mana cost.”
- Scryfall ruling, *Withering Torment*: “If the target creature or enchantment is an illegal target as Withering Torment tries to resolve, it won't resolve and none of its effects will happen. You won't lose life.”
- [CR 118.9](#cr-1189)
- Source (re-verified): [`Solkanar_the_Tainted_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/solkanar_tainted_2026-10-15/gate_output/Solkanar_the_Tainted_Rules_Attestation.json) → “Mana Vault role”
- Source (re-verified): [`Solkanar_the_Tainted_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/solkanar_tainted_2026-10-15/gate_output/Solkanar_the_Tainted_Rules_Attestation.json) → “Withering Torment”

## Replacement and prevention effects

### tainted-05: Enters-under-opponent liabilities: Captive Audience, Xantcha, Khârn

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Sol'Kanar the Tainted, Captive Audience, Xantcha, Sleeper Agent, Khârn the Betrayer, Kain, Traitorous Dragoon, Jon Irenicus, Shattered One

**Ruling.** **Captive Audience and Xantcha** enter under an opponent's control as a replacement effect, so there's no moment when you control them. The new controller makes all of Captive Audience's choices in their upkeep. Anyone, including you, can activate Xantcha's {3} ability: Xantcha's controller loses 2 and the activator draws.

**Khârn** changes controller as part of the damage-prevention replacement, in the middle of resolution. Its Sigil draw trigger waits until that resolution finishes.

**Jon Irenicus's** gift can't be sacrificed in response, because "can't be sacrificed" applies right away. Jon also draws you a card whenever a creature you own but don't control attacks.

**Citations**

- Oracle, *Captive Audience*: “This enchantment enters under the control of an opponent of your choice.”
- Oracle, *Xantcha, Sleeper Agent*: “{3}: Xantcha's controller loses 2 life and you draw a card. Any player may activate this ability.”
- Scryfall ruling, *Captive Audience*: “Once Captive Audience is controlled by your opponent, its ability triggers during that player’s upkeep and that player makes all choices for it. That player is affected by its first two modes, and that player’s opponents create the tokens for its last mode.”
- Scryfall ruling, *Xantcha, Sleeper Agent*: “Xantcha's first ability is a replacement effect that modifies how it enters the battlefield, not a triggered ability. Players can't take actions (such as activating its last ability) while Xantcha's on the battlefield before it's controlled by another player.”
- Scryfall ruling, *Khârn the Betrayer*: “An opponent gaining control of it is part of the replacement effect and happens immediately, even if you are in the middle of resolving the spell or ability and it has more instructions to perform after taking damage.”
- Scryfall ruling, *Jon Irenicus, Shattered One*: “When Jon Irenicus's first ability resolves, the opponent will gain control of a creature and that creature will immediately gain “This creature can't be sacrificed” as part of the resolution of the ability. There is no window of opportunity for that player to sacrifice that creature before it gains the ability.”
- [CR 614.12](#cr-61412), [CR 603.2](#cr-6032)
- Source (re-verified): [`Solkanar_the_Tainted_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/solkanar_tainted_2026-10-15/gate_output/Solkanar_the_Tainted_Rules_Attestation.json) → “Captive Audience”

## Trigger ordering

### tainted-02: Thassa / Conjurer's Closet: order the blink below Sol'Kanar to repeat the first three modes, or above it to dodge mode 4

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Sol'Kanar the Tainted, Thassa, Deep-Dwelling, Conjurer's Closet, Planar Incision

**Ruling.** Sol'Kanar and Thassa (or Conjurer's Closet) trigger at the same time in your end step, and you choose the order.
- **Blink on the bottom:** the Sol'Kanar mode (draw, drain or 3 damage) resolves first. Then the blink returns a new object with no modes chosen, so every end step can use a first-three mode again.
- **Blink on top, when you had to choose mode 4:** Sol'Kanar is exiled and returned first. The pending trigger's "Exile Sol'Kanar" can't find the new object, so nothing is given away.

Planar Incision can also exile an opponent-controlled Sol'Kanar. It returns under its owner's control as a new object with a +1/+1 counter. Lightning Greaves is correctly out of the list, since shroud would stop your own Thassa, Closet and Incision from targeting it.

**Citations**

- Oracle, *Thassa, Deep-Dwelling*: “At the beginning of your end step, exile up to one other target creature you control, then return that card to the battlefield under your control.”
- Oracle, *Planar Incision*: “Exile target artifact or creature, then return it to the battlefield under its owner's control with a +1/+1 counter on it.”
- Scryfall ruling, *Conjurer's Closet*: “Once the exiled creature returns, it's considered a new object with no relation to the object that it was. Auras attached to the exiled creature will be put into their owners' graveyards. Equipment attached to the exiled creature will become unattached and remain on the battlefield. Any counters on the exiled creature will cease to exist.”
- [CR 603.3b](#cr-6033b), [CR 400.7](#cr-4007), [CR 702.18a](#cr-70218a)
- Source (re-verified): [`Solkanar_the_Tainted_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/solkanar_tainted_2026-10-15/gate_output/Solkanar_the_Tainted_Rules_Attestation.json) → “Thassa / Conjurer's Closet — reuse first three modes”
- Source (re-verified): [`Solkanar_the_Tainted_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/solkanar_tainted_2026-10-15/gate_output/Solkanar_the_Tainted_Rules_Attestation.json) → “Blinking before the fourth-mode trigger resolves”
- Source (re-verified): [`Solkanar_the_Tainted_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/solkanar_tainted_2026-10-15/gate_output/Solkanar_the_Tainted_Rules_Attestation.json) → “Fourth mode itself resets Sol'Kanar”
- Source (re-verified): [`Solkanar_the_Tainted_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/solkanar_tainted_2026-10-15/gate_output/Solkanar_the_Tainted_Rules_Attestation.json) → “Planar Incision recovery”
- Source (re-verified): [`Solkanar_the_Tainted_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/solkanar_tainted_2026-10-15/gate_output/Solkanar_the_Tainted_Rules_Attestation.json) → “Lightning Greaves exclusion”

## What the list depends on

### tainted-06: Donated liabilities come home if the holder leaves the game

**Status:** 🚩 list flag · **Evidence:** fact · **Cards:** Sol'Kanar the Tainted, Demonic Pact, Immortal Coil, Archfiend of the Dross, Greed's Gambit, Donate, Harmless Offering, Blim, Comedic Genius

**Ruling.** When a player leaves the game, every effect giving them control of something ends. A permanent you own that you gave away with Donate, Harmless Offering, Fateful Handoff or Blim comes back to you; Blim's ruling confirms this. That's dangerous for the liabilities:
- **Demonic Pact:** if the holder dies to something else before their upkeep, it comes back with only "You lose the game" left.
- **Archfiend of the Dross:** comes back with its remaining oil counters.
- **Immortal Coil:** comes back and triggers if your own graveyard is empty.
- **Greed's Gambit:** comes back with its end-step liabilities, and its leave liabilities if it later leaves.

Captive Audience and Xantcha are different: they entered under the other player's control, so they're exiled instead. Plan kill order so you aren't the next holder, or remove the returned card quickly.

**List flag (dependency-risk).** In multiplayer, killing a Pact / Archfiend / Coil / Gambit holder some other way returns the liability to you (CR 800.4a). Sequence the kills or have removal ready.

**Citations**

- Oracle, *Archfiend of the Dross*: “At the beginning of your upkeep, remove an oil counter from this creature. Then if it has no oil counters on it, you lose the game.”
- Scryfall ruling, *Blim, Comedic Genius*: “The control-change effect of Blim's ability lasts indefinitely. It doesn't wear off during the cleanup step, and it doesn't expire if Blim leaves the battlefield. In a multiplayer game, it does expire if the current controller leaves the game.”
- Scryfall ruling, *Captive Audience*: “In a multiplayer game, if Captive Audience’s owner leaves the game, Captive Audience leaves the game with them. If Captive Audience’s controller leaves the game, Captive Audience is exiled (assuming that player wasn’t also Captive Audience’s owner).”
- [CR 800.4a](#cr-8004a)

### tainted-07: Greed's Gambit: the liabilities follow the controller, and they're at the end step, not upkeep

**Status:** 🚩 list flag · **Evidence:** fact · **Cards:** Sol'Kanar the Tainted, Greed's Gambit, Fateful Handoff, Donate

**Ruling.** Greed's Gambit gives its controller three cards, 6 life and three Bats when it enters. After that, its end-step trigger and leave trigger affect whoever controls it then. Give it away and the recipient discards, loses 2 and sacrifices a creature each end step, plus discards three, loses 6 and sacrifices three when it leaves. The attestation calls these the "later upkeep" liabilities, but the Oracle trigger is at the beginning of your end step. The strategy is unaffected.

**List flag (documentation).** Source attestation says Greed's Gambit's recurring liability is at upkeep; Oracle says end step.

**Citations**

- Oracle, *Greed's Gambit*: “At the beginning of your end step, you discard a card, lose 2 life, and sacrifice a creature.”
- Oracle, *Greed's Gambit*: “When this enchantment leaves the battlefield, you discard three cards, lose 6 life, and sacrifice three creatures.”
- [CR 109.5](#cr-1095)
- Source (re-verified): [`Solkanar_the_Tainted_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/solkanar_tainted_2026-10-15/gate_output/Solkanar_the_Tainted_Rules_Attestation.json) → “Greed's Gambit donation”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 109.5

The words “you” and “your” on an object refer to the object’s controller, its would-be controller (if a player is attempting to play, cast, or activate it), or its owner (if it has no controller). For a static ability, this is the current controller of the object it’s on. For an activated ability, this is the player who activated the ability. For a triggered ability, this is the controller of the object when the ability triggered, unless it’s a delayed triggered ability. To determine the controller of a delayed triggered ability, see rules 603.7d–f.

#### CR 118.9

Some spells have alternative costs. An alternative cost is a cost listed in a spell’s text, or applied to it from another effect, that its controller may pay rather than paying the spell’s mana cost. Alternative costs are usually phrased, “You may [action] rather than pay [this object’s] mana cost,” or “You may cast [this object] without paying its mana cost.” Note that some alternative costs are listed in keywords; see rule 702.

#### CR 202.3

The mana value of an object is a number equal to the total amount of mana in its mana cost, regardless of color.

#### CR 400.7

An object that moves from one zone to another becomes a new object with no memory of, or relation to, its previous existence. This rule has the following exceptions.

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 603.3b

If multiple abilities have triggered since the last time a player received priority, the abilities are placed on the stack in a two-part process. First, each player, in APNAP order, puts each triggered ability they control with a trigger condition that isn’t another ability triggering on the stack in any order they choose. (See rule 101.4.) Second, each player, in APNAP order, puts all remaining triggered abilities they control on the stack in any order they choose. Then the game once again checks for and performs state-based actions until none are performed, then abilities that triggered …

#### CR 603.3c

If a triggered ability is modal, its controller announces the mode choice when putting the ability on the stack. If one of the modes would be illegal (due to an inability to choose legal targets, for example), that mode can’t be chosen. If no mode is chosen, the ability is removed from the stack. (See rule 700.2.)

#### CR 603.8

Some triggered abilities trigger when a game state (such as a player controlling no permanents of a particular card type) is true, rather than triggering when an event occurs. These abilities trigger as soon as the game state matches the condition. They’ll go onto the stack at the next available opportunity. These are called state triggers. (Note that state triggers aren’t the same as state-based actions.) A state-triggered ability doesn’t trigger again until the ability has resolved, has been countered, or has otherwise left the stack. Then, if the object with the ability is still in the …

#### CR 613.1b

Layer 2: Control-changing effects are applied.

#### CR 614.12

Some replacement effects modify how a permanent enters the battlefield. (See rules 614.1c–d.) Such effects may come from the permanent itself if they affect only that permanent (as opposed to a general subset of permanents that includes it). They may also come from other sources. To determine which replacement effects apply and how they apply, check the characteristics of the permanent as it would exist on the battlefield, taking into account replacement effects that have already modified how it enters the battlefield (see rule 616.1), continuous effects from the permanent’s own static …

#### CR 700.2

A spell or ability is modal if it has two or more options in a bulleted list preceded by instructions for a player to choose a number of those options, such as “Choose one —.” Each of those options is a mode. Modal cards printed prior to the Khans of Tarkir™ set didn’t use bulleted lists for the modes; these cards have received errata in the Oracle card reference so the modes do appear in a bulleted list.

#### CR 702.18a

Shroud is a static ability. “Shroud” means “This permanent or player can’t be the target of spells or abilities.”

#### CR 800.4a

When a player leaves the game, all objects (see rule 109) owned by that player leave the game and any effects which give that player control of any objects or players end. Then, if that player controlled any objects on the stack not represented by cards, those objects cease to exist. Then, if there are any objects still controlled by that player, those objects are exiled. This is not a state-based action. It happens as soon as the player leaves the game. If the player who left the game had priority at the time they left, priority passes to the next player in turn order who’s still in the game.

