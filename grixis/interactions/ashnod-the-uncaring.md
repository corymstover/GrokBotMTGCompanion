---
title: "Ashnod the Uncaring — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Ashnod the Uncaring — Interaction Review

> Bot cycle 46 · batch A · reviewed 2026-10-16. Deck: [Ashnod the Uncaring](../decks/ashnod-the-uncaring.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-15), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Current list | [`exports/grixis-archidekt/ashnod-the-uncaring.txt`](../../exports/grixis-archidekt/ashnod-the-uncaring.txt) · SHA-256 `b96f2d08a8659c3e51611c2203ca4599c4c606f927280f1b7515abb96385ce39` |
| Rulings | **12** (9 verified · 2 uncertain · 1 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-15 · rulings 2026-10-15 |
| Source attestations | [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) (Ashnod the Uncaring — RULES PASS WITH DOCUMENTATION CORRECTION) · [`Ashnod_Oracle_Correction_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Ashnod_Oracle_Correction_2026-10-14.md) () |

## Contents
- [Summary](#summary)
- [Flags and open questions](#flags-and-open-questions)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [Key card-pair interactions](#key-card-pair-interactions)
- [Trigger ordering](#trigger-ordering)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [Rules cited](#rules-cited)

## Summary

Ashnod the Uncaring copies every non-mana artifact or creature ability that sacrificed a permanent to activate. The source's correction (no once-per-turn limit, tokens count) is re-verified against current Oracle.

The main rules surprise: the Scrap Trawler + Myr Retriever loops need both artifacts sacrificed during a single cost payment. The list is unchanged; one documentation flag records the stale source wording.

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [ashnod-01](#ashnod-01-current-oracle-no-once-per-turn-limit-tokens-count) | 🚩 list flag (documentation) | Current Oracle: no once-per-turn limit, tokens count | The source's older Ashnod notes describe a once-per-turn, nontoken restriction that current Oracle doesn't have. The retrospective and Ashnod_Oracle_Correction_2026-10-14.md already repair it; noted so older source text isn't reused. |
| [ashnod-08](#ashnod-08-scrap-trawler--myr-retriever-loops-need-a-simultaneous-sacrifice) | ⚠️ uncertain | Scrap Trawler + Myr Retriever loops need a simultaneous sacrifice | The simultaneous-sacrifice sequencing is our reading of the CR (Spellbook step text isn't cached). Sai and Crime Novelist variants follow the same pattern. |
| [ashnod-09](#ashnod-09-nim-deathmantle-loops-apprentice-urza-farid) | ⚠️ uncertain | Nim Deathmantle loops (Apprentice, Urza, Farid) | The per-loop accounting is reconstructed from Oracle text; Spellbook step text isn't cached. |

## Commander rules text and edge cases

### ashnod-01: Current Oracle: no once-per-turn limit, tokens count

**Status:** 🚩 list flag · **Cards:** Ashnod the Uncaring

**Ruling.** Ashnod copies any non-mana activated ability of an artifact or creature whose cost included sacrificing one or more permanents. The copy is free and may get new targets. There is no once-per-turn limit. The sacrificed permanent can be a token (Clue, Treasure, Servo). The source repo's older notes assumed a once-per-turn, nontoken version; the retrospective corrected that.

**List flag (documentation).** The source's older Ashnod notes describe a once-per-turn, nontoken restriction that current Oracle doesn't have. The retrospective and Ashnod_Oracle_Correction_2026-10-14.md already repair it; noted so older source text isn't reused.

**Citations**

- Oracle, *Ashnod the Uncaring*: “Whenever you activate an ability of an artifact or creature that isn't a mana ability, if one or more permanents were sacrificed to activate it, you may copy that ability.”
- [CR 602.2b](#cr-6022b), [CR 707.10](#cr-70710)
- Source (re-verified): [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) → “Current Ashnod has **no once-per-turn restriction** and does **not** require the sacrificed permanent to be nontoken.”

### ashnod-02: Mana abilities and resolution-time sacrifices don't count

**Status:** ✅ verified · **Cards:** Ashnod the Uncaring, Ashnod's Altar, Krark-Clan Ironworks, Lotus Petal, Goblin Welder

**Ruling.** Ashnod's Altar, Krark-Clan Ironworks, Lotus Petal and Treasures are mana abilities, so they're never copied. Sacrificing a Treasure *for the mana* to pay a cost doesn't count either. Goblin Welder's sacrifice happens on resolution, not as a cost, so Ashnod doesn't copy it.

**Citations**

- Oracle, *Ashnod the Uncaring*: “(Sacrificing an artifact for mana to activate an ability doesn't count.)”
- Scryfall ruling, *Ashnod the Uncaring*: “Sacrificing an artifact, such as a Treasure token, to create mana that you used to pay an activation cost doesn’t count.”
- [CR 605.1a](#cr-6051a), [CR 605.3a](#cr-6053a)
- Source (re-verified): [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) → “the prior `Goblin Welder` noninteraction conclusion therefore remains correct.”

## Combos and engine lines

### ashnod-08: Scrap Trawler + Myr Retriever loops need a simultaneous sacrifice

**Status:** ⚠️ uncertain · **Cards:** Ashnod the Uncaring, Scrap Trawler, Myr Retriever, Ashnod's Altar, Krark-Clan Ironworks, Etherium Sculptor, Enthusiastic Mechanaut, Foundry Inspector

**Ruling.** Spellbook lists Trawler + Retriever + a sacrifice-for-mana outlet (Altar or KCI) + a cost reducer as infinite artifact enters and leaves.

The returns only work if both leave together. Retriever returns Trawler, and Trawler's own death trigger returns Retriever (MV 2 < 3). If Retriever dies alone while Trawler is on the battlefield, Trawler can't return it, because its MV isn't lesser.

After each mana ability you activate while holding priority, triggers go on the stack before you can activate the next one. So sacrifice both while paying a single cost, letting both triggers see the other card in the graveyard. With one reducer, recasting both costs 3; the sacrifices give 4.

**Uncertain.** The simultaneous-sacrifice sequencing is our reading of the CR (Spellbook step text isn't cached). Sai and Crime Novelist variants follow the same pattern.

**Citations**

- Oracle, *Scrap Trawler*: “Whenever this creature dies or another artifact you control is put into a graveyard from the battlefield, return to your hand target artifact card in your graveyard with lesser mana value.”
- Oracle, *Myr Retriever*: “When this creature dies, return another target artifact card from your graveyard to your hand.”
- [CR 601.2g](#cr-6012g), [CR 605.3a](#cr-6053a), [CR 117.3c](#cr-1173c), [CR 117.5](#cr-1175), [CR 603.10a](#cr-60310a)

### ashnod-09: Nim Deathmantle loops (Apprentice, Urza, Farid)

**Status:** ⚠️ uncertain · **Cards:** Ashnod the Uncaring, Nim Deathmantle, Ashnod's Altar, Marionette Apprentice, Urza, Lord High Artificer, Farid, Enterprising Salvager, Krark-Clan Ironworks

**Ruling.** Nim Deathmantle returns a nontoken creature put into your graveyard for {4}.
- **Marionette Apprentice:** sacrifice it and its Servo to the Altar for {C}{C}{C}{C}, then pay {4} to return it, making a new Servo. Each loop drains through Apprentice.
- **Urza:** sacrifice Urza and its Construct (after tapping the Construct for {U}) for 4 mana plus {U}, so each loop nets mana.
- **Farid with KCI:** works the same way using Scrap tokens.

The Altar is a mana ability, so Ashnod doesn't copy it.

**Uncertain.** The per-loop accounting is reconstructed from Oracle text; Spellbook step text isn't cached.

**Citations**

- Oracle, *Nim Deathmantle*: “Whenever a nontoken creature is put into your graveyard from the battlefield, you may pay {4}. If you do, return that card to the battlefield and attach this Equipment to it.”
- [CR 605.1a](#cr-6051a), [CR 603.10a](#cr-60310a)

### ashnod-10: Dross Scorpion + Retrofitter Foundry + Altar or KCI

**Status:** ✅ verified · **Cards:** Ashnod the Uncaring, Dross Scorpion, Retrofitter Foundry, Ashnod's Altar, Krark-Clan Ironworks

**Ruling.** Retrofitter Foundry makes a Servo for {2}, {T}. Sacrificing that Servo (an artifact creature) to the Altar gives {C}{C}, and Dross Scorpion untaps Foundry. Repeating this is mana-neutral and gives unlimited death and enter/leave triggers (Marionette Apprentice, Disciple of the Vault drains). Foundry's Thopter and Construct modes sacrifice tokens to activate, so Ashnod copies those (a second Thopter or Construct).

**Citations**

- Oracle, *Dross Scorpion*: “Whenever this creature or another artifact creature dies, you may untap target artifact.”
- Oracle, *Retrofitter Foundry*: “{2}, {T}: Create a 1/1 colorless Servo artifact creature token.”
- [CR 700.4](#cr-7004), [CR 605.1a](#cr-6051a)

## Engines and payoffs

### ashnod-03: Sacrifice-cost artifacts become two-for-one

**Status:** ✅ verified · **Cards:** Ashnod the Uncaring, Mishra's Bauble, Wayfarer's Bauble, Moonsilver Key, Pyrite Spellbomb, Executioner's Capsule, Mind Stone, Mnemonic Sphere, Dross Skullbomb, Dockside Chef

**Ruling.** Each of these sacrifices itself (or another permanent) as a cost, so Ashnod copies the ability:
- Bauble: two delayed draws.
- Wayfarer's Bauble: two basic lands.
- Moonsilver Key: two tutors.
- Executioner's Capsule and Pyrite Spellbomb: a second target.
- Mind Stone, Mnemonic Sphere, Skullbomb, Dockside Chef: extra cards.

The copy keeps the original's targets unless you change them.

**Citations**

- Oracle, *Mishra's Bauble*: “{T}, Sacrifice this artifact: Look at the top card of target player's library. Draw a card at the beginning of the next turn's upkeep.”
- [CR 707.10](#cr-70710), [CR 707.10c](#cr-70710c)

### ashnod-11: Leave-the-battlefield payoffs

**Status:** ✅ verified · **Cards:** Ashnod the Uncaring, Oni-Cult Anvil, Disciple of the Vault, Marionette Apprentice, Mayhem Devil, Esoteric Duplicator

**Ruling.** - **Oni-Cult Anvil:** its {T}, sacrifice ability is copied by Ashnod. Its Construct trigger happens once per turn, on your turn only.
- **Disciple of the Vault and Marionette Apprentice:** trigger on artifacts (tokens included) going to the graveyard.
- **Mayhem Devil:** pings on every sacrifice by any player.
- **Esoteric Duplicator:** offers a {2} end-step copy of each sacrificed artifact.

**Citations**

- Oracle, *Oni-Cult Anvil*: “This ability triggers only once each turn.”
- [CR 603.10a](#cr-60310a), [CR 704.5d](#cr-7045d)

## Key card-pair interactions

### ashnod-04: Time Sieve copied: two extra turns

**Status:** ✅ verified · **Cards:** Ashnod the Uncaring, Time Sieve

**Ruling.** Time Sieve's ability sacrifices five artifacts (it can be one of them), so Ashnod copies it: you take two extra turns. If Time Sieve itself was sacrificed, the copy still resolves. Abilities exist independently of their source.

**Citations**

- Oracle, *Time Sieve*: “{T}, Sacrifice five artifacts: Take an extra turn after this one.”
- Scryfall ruling, *Time Sieve*: “You may sacrifice Time Sieve as one of the artifacts to pay the cost of its own ability.”
- [CR 113.7a](#cr-1137a), [CR 500.7](#cr-5007)
- Source (re-verified): [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) → “`Oni-Cult Anvil`, `Arcbound Ravager`, `Trading Post` sacrifice modes, `Repurposing Bay`, `Time Sieve`, and other nonmana artifact/creature activated abilities qualify”

### ashnod-05: Copies use the original's sacrificed-object information

**Status:** ✅ verified · **Cards:** Ashnod the Uncaring, Repurposing Bay, Altar of Dementia, Kuldotha Forgemaster

**Ruling.** A copied ability copies the decisions made for it, including costs paid. The copy of Repurposing Bay looks for MV 1 + the sacrificed artifact's MV, and the copy of Altar of Dementia mills equal to the sacrificed creature's power, without a new sacrifice. Kuldotha Forgemaster's copy fetches a second artifact. A mana value with X counts X as 0.

**Citations**

- Oracle, *Repurposing Bay*: “Search your library for an artifact card with mana value equal to 1 plus the sacrificed artifact's mana value”
- Scryfall ruling, *Repurposing Bay*: “If there’s an {X} in the sacrificed artifact’s mana cost, X is 0 when determining its mana value.”
- [CR 707.10](#cr-70710)

### ashnod-07: Clan Crafter on Ashnod

**Status:** ✅ verified · **Cards:** Ashnod the Uncaring, Clan Crafter

**Ruling.** Clan Crafter is a Background in the 99, cast as a normal enchantment. Ashnod has no Choose a Background, so it isn't a second commander. It gives commander creatures you own '{2}, Sacrifice an artifact: +1/+1 counter and draw'. That's an activated ability of a creature with a sacrifice cost, so Ashnod copies it: two counters, two cards.

**Citations**

- Oracle, *Clan Crafter*: “Commander creatures you own have "{2}, Sacrifice an artifact: Put a +1/+1 counter on this creature and draw a card."”
- [CR 702.124a](#cr-702124a), [CR 113.10](#cr-11310)

## Trigger ordering

### ashnod-06: Rings of Brighthearth and Ashnod both copy

**Status:** ✅ verified · **Cards:** Ashnod the Uncaring, Rings of Brighthearth

**Ruling.** Rings ({2} for any non-mana ability) and Ashnod trigger separately on the same activation, and you order the triggers. Each makes one copy. Copies aren't activated, so they don't retrigger either card. If Rings was sacrificed to pay the cost, its trigger doesn't happen.

**Citations**

- Oracle, *Rings of Brighthearth*: “Whenever you activate an ability, if it isn't a mana ability, you may pay {2}. If you do, copy that ability.”
- Scryfall ruling, *Rings of Brighthearth*: “If paying the activation cost of the ability includes sacrificing Rings of Brighthearth, the ability won't be copied.”
- [CR 603.3b](#cr-6033b), [CR 707.10](#cr-70710)

## Zones, commander tax and the command zone

### ashnod-12: Commander tax and Ashnod's deathtouch

**Status:** ✅ verified · **Cards:** Ashnod the Uncaring, Blasting Station, Walking Ballista

**Ruling.** Ashnod costs {2}{U}{B}{R}, then 7, then 9. Deathtouch applies only to damage Ashnod deals itself. Blasting Station's and Walking Ballista's pings come from those sources. Walking Ballista's counter removal isn't a sacrifice, so Ashnod doesn't copy it. Blasting Station's sacrifice ability is copied (an extra point of damage).

**Citations**

- Oracle, *Blasting Station*: “{T}, Sacrifice a creature: This artifact deals 1 damage to any target.”
- [CR 903.8](#cr-9038), [CR 702.2b](#cr-7022b)

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 113.7a

Once activated or triggered, an ability exists on the stack independently of its source. Destruction or removal of the source after that time won’t affect the ability. Note that some abilities cause a source to do something (for example, “This creature deals 1 damage to any target”) rather than the ability doing anything directly. In these cases, any activated or triggered ability that references information about the source for use while announcing an activated ability or putting a triggered ability on the stack checks that information when the ability is put onto the stack. Otherwise, it …

#### CR 113.10

Effects can add or remove abilities of objects. An effect that adds an ability will state that the object “gains” or “has” that ability, or similar. An effect that removes an ability will state that the object “loses” that ability.

#### CR 117.3c

If a player has priority when they cast a spell, activate an ability, or take a special action, that player receives priority afterward.

#### CR 117.5

Each time a player would get priority, the game first performs all applicable state-based actions as a single event (see rule 704, “State-Based Actions”), then repeats this process until no state-based actions are performed. Then triggered abilities are put on the stack (see rule 603, “Handling Triggered Abilities”). These steps repeat in order until no further state-based actions are performed and no abilities trigger. Then the player who would have received priority does so.

#### CR 500.7

Some effects can give a player extra turns. They do this by adding the turns directly after the specified turn. If a player is given multiple extra turns, the extra turns are added one at a time. If multiple players are given extra turns, the extra turns are added one at a time, in APNAP order (see rule 101.4). The most recently created turn will be taken first.

#### CR 601.2g

If the total cost includes a mana payment, the player then has a chance to activate mana abilities (see rule 605, “Mana Abilities”). Mana abilities must be activated before costs are paid.

#### CR 602.2b

The remainder of the process for activating an ability is identical to the process for casting a spell listed in rules 601.2b–i. Those rules apply to activating an ability just as they apply to casting a spell. An activated ability’s analog to a spell’s mana cost (as referenced in rule 601.2f) is its activation cost.

#### CR 603.3b

If multiple abilities have triggered since the last time a player received priority, the abilities are placed on the stack in a two-part process. First, each player, in APNAP order, puts each triggered ability they control with a trigger condition that isn’t another ability triggering on the stack in any order they choose. (See rule 101.4.) Second, each player, in APNAP order, puts all remaining triggered abilities they control on the stack in any order they choose. Then the game once again checks for and performs state-based actions until none are performed, then abilities that triggered …

#### CR 603.10a

Some zone-change triggers look back in time. These are leaves-the-battlefield abilities, abilities that trigger when a player sacrifices a permanent, abilities that trigger when a card leaves a graveyard, and abilities that trigger when an object that all players can see is put into a hand or library.

#### CR 605.1a

An activated ability is a mana ability if it meets all of the following criteria: it doesn’t require a target (see rule 115.6), it could add mana to a player’s mana pool when it resolves, it’s not a loyalty ability (see rule 606, “Loyalty Abilities”), and its cost and effect don’t move any card to or from a library. Do not take into account replacement effects that may apply, other than self-replacement effects, when evaluating these criteria.

#### CR 605.3a

A player may activate an activated mana ability whenever they have priority, whenever they are casting a spell or activating an ability that requires a mana payment, or whenever a rule or effect asks for a mana payment, even if it’s in the middle of casting or resolving a spell or activating or resolving an ability.

#### CR 700.4

The term dies means “is put into a graveyard from the battlefield.”

#### CR 702.2b

A creature with toughness greater than 0 that’s been dealt damage by a source with deathtouch since the last time state-based actions were checked is destroyed as a state-based action. See rule 704.

#### CR 702.124a

Partner abilities are keyword abilities that modify the rules for deck construction in the Commander variant (see rule 903), and they function before the game begins. Each partner ability allows you to designate two legendary cards as your commander rather than one. Each partner ability has its own requirements for those two commanders. The partner abilities are: partner, partner—[text], partner with [name], choose a Background, and Doctor’s companion.

#### CR 704.5d

If a token is in a zone other than the battlefield, it ceases to exist.

#### CR 707.10

To copy a spell, activated ability, or triggered ability means to put a copy of it onto the stack; a copy of a spell isn’t cast and a copy of an activated ability isn’t activated. A copy of a spell or ability copies both the characteristics of the spell or ability and all decisions made for it, including modes, targets, the value of X, and additional or alternative costs. (See rule 601, “Casting Spells.”) Choices that are normally made on resolution are not copied. If an effect of the copy refers to objects used to pay its costs, it uses the objects used to pay the costs of the original spell …

#### CR 707.10c

Some effects copy a spell or ability and state that its controller may choose new targets for the copy. The player may leave any number of the targets unchanged, even if those targets would be illegal. If the player chooses to change some or all of the targets, the new targets must be legal. Once the player has decided what the copy’s targets will be, the copy is put onto the stack with those targets.

#### CR 903.8

A player may cast a commander they own from the command zone. A commander cast from the command zone costs an additional {2} for each previous time the player casting it has cast it from the command zone that game. This additional cost is informally known as the “commander tax.”

