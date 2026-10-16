---
title: "Lynde, Cheerful Tormentor — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Lynde, Cheerful Tormentor — Interaction Review

> Bot cycle 49 · batch C · reviewed 2026-10-16. Deck: [Lynde, Cheerful Tormentor](../decks/lynde-cheerful-tormentor.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-15), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/lynde-cheerful-tormentor.txt`](../../exports/grixis-archidekt/lynde-cheerful-tormentor.txt) · SHA-256 `f1d4ed17411a4229260f39f4e79f6f014bffb29f3c601fedf3488d03676abf82` |
| Rulings | **8** (7 verified · 0 uncertain · 1 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-15 · rulings 2026-10-15 |
| Source attestations | [`Lynde_Cheerful_Tormentor_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lynde_cheerful_tormentor_2026-10-14/Lynde_Cheerful_Tormentor_Rules_Attestation.json) (11 interactions, all PASS) |

## Contents
- [Summary](#summary)
- [Flags and open questions](#flags-and-open-questions)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Engines and payoffs](#engines-and-payoffs)
- [Key card-pair interactions](#key-card-pair-interactions)
- [Trigger ordering](#trigger-ordering)
- [Rules cited](#rules-cited)

## Summary

Lynde, Cheerful Tormentor returns dead Curses attached to you at the next end step. At your upkeep she moves one Curse to an opponent and draws two. Sacrifice and destroy effects recycle the Curses, and extra upkeeps (Paradox Haze, The Ninth Doctor, Obeka) repeat the move-and-draw. This review re-verifies all 11 attestation items. There are no Spellbook combos for this list.

One flag: returned Curses punish you until they're moved, one per upkeep. Rules surprises: an end-step sacrifice returns a turn late (CR 513.2); Curse of Bloodletting doubles Obeka's extra upkeeps. No list errors.

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [lynde-06](#lynde-06-curses-returned-to-you-hit-you-until-they-move) | 🚩 list flag (anti-synergy) | Curses returned to you hit you until they move | Pilot note, not a list error: Lynde's return puts Curses on you, and only one moves per upkeep. Recycle the self-harming Curses (Cruel Reality, Torment of Scarabs, Curse of Thirst, Bloodletting, Death's Hold, Echoes) last, or have an extra upkeep (Paradox Haze/Ninth Doctor/Obeka) ready to move them. Ordering Lynde first doesn't stop an upkeep Curse's trigger that is already on the stack. |

## Commander rules text and edge cases

### lynde-01: Return trigger: battlefield to graveyard only, back at the next end step, attached to you

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Lynde, Cheerful Tormentor

**Ruling.** Lynde only triggers when a Curse goes from the battlefield to your graveyard. Discarding or milling one doesn't count. The Curse returns at the beginning of the next end step attached to you, not to an opponent. If the player a Curse enchants leaves the game, the Curse goes to your graveyard and triggers Lynde.

**Citations**

- Oracle, *Lynde, Cheerful Tormentor*: “Whenever a Curse is put into your graveyard from the battlefield, return it to the battlefield attached to you at the beginning of the next end step.”
- Scryfall ruling, *Lynde, Cheerful Tormentor*: “In a multiplayer game, if a player enchanted by one of your Curses leaves the game, perhaps because they have been tormented too much by Lynde, that Curse will be put into your graveyard and cause Lynde's first triggered ability to trigger.”
- [CR 603.7a](#cr-6037a), [CR 603.10a](#cr-60310a), [CR 303.4f](#cr-3034f), [CR 303.4c](#cr-3034c)
- Source (re-verified): [`Lynde_Cheerful_Tormentor_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lynde_cheerful_tormentor_2026-10-14/Lynde_Cheerful_Tormentor_Rules_Attestation.json) → “Lynde trigger condition and delayed return”
- Source (re-verified): [`Lynde_Cheerful_Tormentor_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lynde_cheerful_tormentor_2026-10-14/Lynde_Cheerful_Tormentor_Rules_Attestation.json) → “Curse of Vengeance and opponent departure”

### lynde-02: Upkeep move: one Curse, no targeting, draw two

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Lynde, Cheerful Tormentor

**Ruling.** At your upkeep Lynde may move one Curse that's attached to you onto an opponent, and if it does you draw two. It doesn't target, so hexproof doesn't stop it. Only one Curse moves per upkeep, so each extra upkeep moves another one and draws two more.

**Citations**

- Oracle, *Lynde, Cheerful Tormentor*: “At the beginning of your upkeep, you may attach a Curse attached to you to one of your opponents. If you do, draw two cards.”
- Scryfall ruling, *Lynde, Cheerful Tormentor*: “Lynde's last ability doesn't target, so you can use it to attach a Curse to a player who has hexproof.”
- [CR 303.4e](#cr-3034e), [CR 115.10a](#cr-11510a)
- Source (re-verified): [`Lynde_Cheerful_Tormentor_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lynde_cheerful_tormentor_2026-10-14/Lynde_Cheerful_Tormentor_Rules_Attestation.json) → “Lynde upkeep redeployment”

## Engines and payoffs

### lynde-03: Resetting Curses: Despotic Scepter, Claws of Gix, Braids, Demon of Fate's Design, Perilous Research

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Lynde, Cheerful Tormentor, Despotic Scepter, Claws of Gix, Braids, Arisen Nightmare, Demon of Fate's Design, Perilous Research

**Ruling.** You still own a Curse attached to an opponent, so Despotic Scepter can destroy it. Claws of Gix, Demon of Fate's Design and Perilous Research can sacrifice a Curse you control. Each puts it in your graveyard, so Lynde brings it back. Timing: a Curse sacrificed during an end step (Braids' trigger) creates its 'next end step' return too late for this turn. It comes back at the next turn's end step, which is still before your next upkeep.

**Citations**

- Oracle, *Despotic Scepter*: “{T}: Destroy target permanent you own. It can't be regenerated.”
- Oracle, *Braids, Arisen Nightmare*: “At the beginning of your end step, you may sacrifice an artifact, creature, enchantment, land, or planeswalker.”
- Scryfall ruling, *Despotic Scepter*: “You own a nontoken permanent if it started the game in your deck.”
- [CR 108.3](#cr-1083), [CR 513.2](#cr-5132), [CR 701.21a](#cr-70121a)
- Source (re-verified): [`Lynde_Cheerful_Tormentor_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lynde_cheerful_tormentor_2026-10-14/Lynde_Cheerful_Tormentor_Rules_Attestation.json) → “Despotic Scepter as Curse reset engine”
- Source (re-verified): [`Lynde_Cheerful_Tormentor_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lynde_cheerful_tormentor_2026-10-14/Lynde_Cheerful_Tormentor_Rules_Attestation.json) → “Claws of Gix, Braids, Demon of Fate's Design, and Perilous Research”

### lynde-04: Extra upkeeps: Paradox Haze, The Ninth Doctor, Obeka (+ Curse of Bloodletting)

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Lynde, Cheerful Tormentor, Paradox Haze, The Ninth Doctor, Obeka, Splitter of Seconds, Curse of Bloodletting

**Ruling.** Every additional upkeep triggers Lynde (another move + draw two) and every other 'beginning of your upkeep' ability again. Paradox Haze gives one extra after your first upkeep. The Ninth Doctor gives one after the step its trigger resolves in. Obeka's combat damage gives that many extra beginning phases after combat (no untap or draw steps). Curse of Bloodletting on the player Obeka hits doubles the damage, and so the upkeep count.

**Citations**

- Oracle, *Obeka, Splitter of Seconds*: “Whenever Obeka deals combat damage to a player, you get that many additional upkeep steps after this phase.”
- Oracle, *Curse of Bloodletting*: “If a source would deal damage to enchanted player, it deals double that damage to that player instead.”
- Scryfall ruling, *Paradox Haze*: “Abilities that trigger "at the beginning of [your] upkeep" will trigger at the beginning of each additional upkeep as well.”
- Scryfall ruling, *Obeka, Splitter of Seconds*: “Since the upkeep step can only occur during the beginning phase, getting one or more additional upkeep steps outside of the beginning phase actually means you get an additional beginning phase for each of those upkeeps after this phase.”
- Scryfall ruling, *The Ninth Doctor*: “The Ninth Doctor's ability triggers during the untap step and goes onto the stack at the beginning of the next step (usually the upkeep). The additional upkeep is taken after that step, not after the untap step.”
- [CR 500.8](#cr-5008), [CR 614.1a](#cr-6141a)
- Source (re-verified): [`Lynde_Cheerful_Tormentor_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lynde_cheerful_tormentor_2026-10-14/Lynde_Cheerful_Tormentor_Rules_Attestation.json) → “Paradox Haze and The Ninth Doctor”
- Source (re-verified): [`Lynde_Cheerful_Tormentor_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lynde_cheerful_tormentor_2026-10-14/Lynde_Cheerful_Tormentor_Rules_Attestation.json) → “Obeka, Splitter of Seconds”
- Source (re-verified): [`Lynde_Cheerful_Tormentor_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lynde_cheerful_tormentor_2026-10-14/Lynde_Cheerful_Tormentor_Rules_Attestation.json) → “Curse of Bloodletting plus Obeka”

## Key card-pair interactions

### lynde-07: Harmless on yourself: Fool's Wisdom, Surveillance, Unbinding

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Lynde, Cheerful Tormentor, Curse of Fool's Wisdom, Curse of Surveillance, Curse of Unbinding

**Ruling.** Some Curses are neutral or good on you. Curse of Fool's Wisdom on you means lose 2, gain 2 per draw, and you don't lose at 0 in between. Curse of Surveillance's controller (you) picks its targets, and 'any number' includes none. Curse of Unbinding gives its controller (you) the revealed creature, but mills the cards above it.

**Citations**

- Scryfall ruling, *Curse of Fool's Wisdom*: “If you become enchanted by your own Curse of Fool's Wisdom, you'll lose 2 life and gain 2 life whenever you draw a card. You won't lose the game if your life total is 0 or less between those events.”
- Scryfall ruling, *Curse of Surveillance*: “The controller of Curse of Surveillance chooses the targets for its triggered ability, no matter which player it is attached to.”
- Scryfall ruling, *Curse of Unbinding*: “The controller of Curse of Unbinding puts the creature card onto the battlefield under their control. This may not be the same player as the enchanted player.”
- [CR 119.3](#cr-1193), [CR 601.2c](#cr-6012c)

## Trigger ordering

### lynde-05: Curse of Misfortunes on yourself: order it before Lynde

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Lynde, Cheerful Tormentor, Curse of Misfortunes

**Ruling.** With Curse of Misfortunes attached to you, it and Lynde both trigger at your upkeep. You control both, so resolve Misfortunes first: it fetches a Curse onto you (a different name from the Curses already on you). Then Lynde's trigger can move that one or another. A Curse that enters during the upkeep doesn't trigger its own upkeep abilities that step.

**Citations**

- Oracle, *Curse of Misfortunes*: “At the beginning of your upkeep, you may search your library for a Curse card that doesn't have the same name as a Curse attached to enchanted player, put it onto the battlefield attached to that player, then shuffle.”
- Scryfall ruling, *Curse of Misfortunes*: “The Curse card you put onto the battlefield must have a different name than each other Curse enchanting the enchanted player when the triggered ability resolves.”
- [CR 603.3b](#cr-6033b), [CR 603.2](#cr-6032)
- Source (re-verified): [`Lynde_Cheerful_Tormentor_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lynde_cheerful_tormentor_2026-10-14/Lynde_Cheerful_Tormentor_Rules_Attestation.json) → “Curse of Misfortunes plus Lynde on self”

### lynde-06: Curses returned to you hit you until they move

**Status:** 🚩 list flag · **Evidence:** fact · **Cards:** Lynde, Cheerful Tormentor, Cruel Reality, Torment of Scarabs, Curse of Thirst, Curse of Bloodletting, Curse of Death's Hold, Curse of Echoes, Curse of Shaken Faith, Maddening Hex

**Ruling.** Lynde returns Curses attached to *you*, and only one moves per upkeep. In the meantime they work against you:
- **At your upkeep:** Cruel Reality, Torment of Scarabs and Curse of Thirst trigger together with Lynde. Moving the Curse doesn't remove a trigger already on the stack.
- **While attached to you:** Curse of Bloodletting doubles damage to you. Curse of Death's Hold shrinks your creatures. Curse of Echoes lets opponents copy your instants and sorceries. Shaken Faith and Maddening Hex punish your spells (Hex then jumps to a random opponent).

**List flag (anti-synergy).** Pilot note, not a list error: Lynde's return puts Curses on you, and only one moves per upkeep. Recycle the self-harming Curses (Cruel Reality, Torment of Scarabs, Curse of Thirst, Bloodletting, Death's Hold, Echoes) last, or have an extra upkeep (Paradox Haze/Ninth Doctor/Obeka) ready to move them. Ordering Lynde first doesn't stop an upkeep Curse's trigger that is already on the stack.

**Citations**

- Oracle, *Cruel Reality*: “At the beginning of enchanted player's upkeep, that player sacrifices a creature or planeswalker of their choice. If the player can't, they lose 5 life.”
- Oracle, *Curse of Thirst*: “At the beginning of enchanted player's upkeep, this Aura deals damage to that player equal to the number of Curses attached to them.”
- Scryfall ruling, *Curse of Thirst*: “The number of Curses attached to the player is counted when the ability resolves.”
- [CR 113.7a](#cr-1137a), [CR 603.3b](#cr-6033b)

### lynde-08: Curse of Echoes copies aren't cast; Curse of Vengeance pays out on a loss

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Lynde, Cheerful Tormentor, Curse of Echoes, Curse of Vengeance

**Ruling.** Curse of Echoes copies are created, not cast, so no cast triggers. Curse of Vengeance gains a spite counter each time the enchanted player casts a spell, even if that spell is countered. When that player loses, you gain life and draw for each counter. Because they've left the game, the Curse also goes to your graveyard and returns to you through Lynde.

**Citations**

- Scryfall ruling, *Curse of Echoes*: “All the copies are created on the stack, so none of them are cast. Abilities that trigger when a player casts a spell won’t trigger.”
- Scryfall ruling, *Curse of Vengeance*: “Curse of Vengeance's first triggered ability resolves before the spell that caused it to trigger. The ability will resolve even if that spell is countered.”
- [CR 707.10](#cr-70710), [CR 303.4c](#cr-3034c), [CR 704.5m](#cr-7045m)
- Source (re-verified): [`Lynde_Cheerful_Tormentor_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lynde_cheerful_tormentor_2026-10-14/Lynde_Cheerful_Tormentor_Rules_Attestation.json) → “Curse of Echoes and spell copies”
- Source (re-verified): [`Lynde_Cheerful_Tormentor_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lynde_cheerful_tormentor_2026-10-14/Lynde_Cheerful_Tormentor_Rules_Attestation.json) → “Curse of Vengeance and opponent departure”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 108.3

The owner of a card in the game is the player who started the game with it in their deck. If a card is brought into the game from outside the game rather than starting in a player’s deck, its owner is the player who brought it into the game. If a card starts the game in the command zone, its owner is the player who put it into the command zone to start the game. Legal ownership of a card in the game is irrelevant to the game rules except for the rules for ante. (See rule 407.)

#### CR 113.7a

Once activated or triggered, an ability exists on the stack independently of its source. Destruction or removal of the source after that time won’t affect the ability. Note that some abilities cause a source to do something (for example, “This creature deals 1 damage to any target”) rather than the ability doing anything directly. In these cases, any activated or triggered ability that references information about the source for use while announcing an activated ability or putting a triggered ability on the stack checks that information when the ability is put onto the stack. Otherwise, it …

#### CR 115.10a

Just because an object or player is being affected by a spell or ability doesn’t make that object or player a target of that spell or ability. Unless that object or player is identified by the word “target” in the text of that spell or ability, or the rule for that keyword ability, it’s not a target.

#### CR 119.3

If an effect causes a player to gain life or lose life, that player’s life total is adjusted accordingly.

#### CR 303.4c

If an Aura is enchanting an illegal object or player as defined by its enchant ability and other applicable effects, the object it was attached to no longer exists, or the player it was attached to has left the game, the Aura is put into its owner’s graveyard. (This is a state-based action. See rule 704.)

#### CR 303.4e

An Aura’s controller is separate from the enchanted object’s controller or the enchanted player; the two need not be the same. If an Aura enchants an object, changing control of the object doesn’t change control of the Aura, and vice versa. Only the Aura’s controller can activate its abilities. However, if the Aura grants an ability to the enchanted object (with “gains” or “has”), the enchanted object’s controller is the only one who can activate that ability.

#### CR 303.4f

If an Aura is entering the battlefield under a player’s control by any means other than by resolving as an Aura spell, and the effect putting it onto the battlefield doesn’t specify the object or player the Aura will enchant, that player chooses what it will enchant as the Aura enters the battlefield. The player must choose a legal object or player according to the Aura’s enchant ability and any other applicable effects.

#### CR 500.8

Some effects can add phases to a turn. They do this by adding the phases directly after the specified phase. If multiple extra phases are created after the same phase, the most recently created phase will occur first.

#### CR 513.2

If a permanent with an ability that triggers “at the beginning of the end step” enters the battlefield during this step, that ability won’t trigger until the next turn’s end step. Likewise, if a delayed triggered ability that triggers “at the beginning of the next end step” is created during this step, that ability won’t trigger until the next turn’s end step. In other words, the step doesn’t “back up” so those abilities can go on the stack. This rule applies only to triggered abilities; it doesn’t apply to continuous effects whose durations say “until end of turn” or “this turn.” (See rule …

#### CR 601.2c

The player announces their choice of an appropriate object or player for each target the spell requires. A spell may require some targets only if an alternative or additional cost (such as a kicker cost) or a particular mode was chosen for it; otherwise, the spell is cast as though it did not require those targets. Similarly, a spell may require alternative targets only if an alternative or additional cost was chosen for it. If the spell has a variable number of targets, the player announces how many targets they will choose before they announce those targets. In some cases, the number of …

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 603.3b

If multiple abilities have triggered since the last time a player received priority, the abilities are placed on the stack in a two-part process. First, each player, in APNAP order, puts each triggered ability they control with a trigger condition that isn’t another ability triggering on the stack in any order they choose. (See rule 101.4.) Second, each player, in APNAP order, puts all remaining triggered abilities they control on the stack in any order they choose. Then the game once again checks for and performs state-based actions until none are performed, then abilities that triggered …

#### CR 603.7a

Delayed triggered abilities are created during the resolution of spells or abilities, as the result of a replacement effect being applied, or as a result of a static ability that allows a player to take an action. A delayed triggered ability won’t trigger until it has actually been created, even if its trigger event occurred just beforehand. Other events that happen earlier may make the trigger event impossible.

#### CR 603.10a

Some zone-change triggers look back in time. These are leaves-the-battlefield abilities, abilities that trigger when a player sacrifices a permanent, abilities that trigger when a card leaves a graveyard, and abilities that trigger when an object that all players can see is put into a hand or library.

#### CR 614.1a

Effects that use the word “instead” are replacement effects. Most replacement effects use the word “instead” to indicate what events will be replaced with other events.

#### CR 701.21a

To sacrifice a permanent, its controller moves it from the battlefield directly to its owner’s graveyard. A player can’t sacrifice something that isn’t a permanent, or something that’s a permanent they don’t control. Sacrificing a permanent doesn’t destroy it, so regeneration or other effects that replace destruction can’t affect this action.

#### CR 704.5m

If an Aura is attached to an illegal object or player, or is not attached to an object or player, that Aura is put into its owner’s graveyard.

#### CR 707.10

To copy a spell, activated ability, or triggered ability means to put a copy of it onto the stack; a copy of a spell isn’t cast and a copy of an activated ability isn’t activated. A copy of a spell or ability copies both the characteristics of the spell or ability and all decisions made for it, including modes, targets, the value of X, and additional or alternative costs. (See rule 601, “Casting Spells.”) Choices that are normally made on resolution are not copied. If an effect of the copy refers to objects used to pay its costs, it uses the objects used to pay the costs of the original spell …

