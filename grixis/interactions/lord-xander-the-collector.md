---
title: "Lord Xander, the Collector — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Lord Xander, the Collector — Interaction Review

> Bot cycle 49 · batch C · reviewed 2026-10-16. Deck: [Lord Xander, the Collector](../decks/lord-xander-the-collector.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/lord-xander-the-collector.txt`](../../exports/grixis-archidekt/lord-xander-the-collector.txt) · SHA-256 `26b1674fef88552f6e5f2eaff5c85bcefb05ac1a4afb90b728ae8218f24fab63` |
| Rulings | **11** (11 verified · 0 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`Lord_Xander_the_Collector_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_xander_the_collector_2026-10-14/Lord_Xander_the_Collector_Rules_Attestation.json) (18 interactions, all PASS) |

## Contents
- [Summary](#summary)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [Layers and continuous effects](#layers-and-continuous-effects)
- [Trigger ordering](#trigger-ordering)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [Rules cited](#rules-cited)

## Summary

Lord Xander, the Collector has three halving triggers: discard on enter, mill on attack, sacrifice on death. The deck multiplies them with clones, myriad, Helm of the Host and Roaming Throne, and finishes the mill with Bruvac, Riverchurn Monument or Fraying Sanity. This review re-verifies all 18 attestation items. Eleven Spellbook lines are confirmed.

Rules surprises: legendary copies give a dies trigger through the legend rule, but Auton Soldier's exiled myriad tokens don't; Feign Death needs Xander left in the graveyard; Xander's 'half, rounded down' leaves one card on an odd library. No list errors.

## Commander rules text and edge cases

### xander-01: Three separate triggers: enter, attack, dies

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Lord Xander, the Collector

**Ruling.** Xander has three triggers: on enter, a target opponent discards half their hand (rounded down); on attack, the defending player mills half their library (rounded down); on death, a target opponent sacrifices half their nonland permanents of their choice (rounded down). Every copy, clone and recursion card here is judged by which of these it actually triggers. A token that enters attacking triggers enter (and dies, if it dies) but not attack.

**Citations**

- Oracle, *Lord Xander, the Collector*: “Whenever Lord Xander attacks, defending player mills half their library, rounded down.”
- Oracle, *Lord Xander, the Collector*: “When Lord Xander dies, target opponent sacrifices half the nonland permanents they control of their choice, rounded down.”
- [CR 603.6a](#cr-6036a), [CR 603.10a](#cr-60310a), [CR 508.3a](#cr-5083a), [CR 107.1a](#cr-1071a)
- Source (re-verified): [`Lord_Xander_the_Collector_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_xander_the_collector_2026-10-14/Lord_Xander_the_Collector_Rules_Attestation.json) → “Lord Xander trigger structure”

## Combos and engine lines

### xander-05: Finishing the mill: Bruvac, Riverchurn Monument, Fraying Sanity, Maddening Cacophony

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Lord Xander, the Collector, Bruvac the Grandiloquent, Riverchurn Monument, Fraying Sanity, Maddening Cacophony

**Ruling.** - **Bruvac** doubles Xander's half (rounded down): an even library mills completely, an odd one leaves 1 card.
- **Riverchurn Monument's exhaust** mills as many cards as are already in that graveyard. After Xander, that's at least the rest of the library, unless the graveyard was empty and the library odd (1 left).
- **Fraying Sanity** mills, at end step, as many as went to that graveyard this turn.
- **Kicked Maddening Cacophony** mills half rounded *up*, so with Bruvac or Monument it always finishes.

**Citations**

- Oracle, *Bruvac the Grandiloquent*: “If an opponent would mill one or more cards, they mill twice that many cards instead.”
- Oracle, *Riverchurn Monument*: “Exhaust — {2}{U}{U}, {T}: Any number of target players each mill cards equal to the number of cards in their graveyard.”
- Oracle, *Maddening Cacophony*: “If this spell was kicked, instead each opponent mills half their library, rounded up.”
- Scryfall ruling, *Fraying Sanity*: “Fraying Sanity's triggered ability counts the number of cards that were put into the enchanted player's graveyard during the turn, even if Fraying Sanity wasn't on the battlefield at the time those cards were put there, and even if those cards have left that graveyard.”
- [CR 701.17a](#cr-70117a), [CR 614.1a](#cr-6141a), [CR 107.1a](#cr-1071a)
- Commander Spellbook [95-1022](https://commanderspellbook.com/combo/95-1022/) (community-maintained, retrieved 2026-10-16): “Declare Lord Xander as an attacker, triggering its ability, causing an opponent to mill a number of cards equal to half their library, rounded down, times two due to Bruvac.”
- Commander Spellbook [1022-6285](https://commanderspellbook.com/combo/1022-6285/) (community-maintained, retrieved 2026-10-16): “Activate Riverchurn Monument's exhaust ability by paying {2}{U}{U} and tapping it, causing each player to mill cards equal to the number of cards in their graveyard.”
- Commander Spellbook [95-5080](https://commanderspellbook.com/combo/95-5080/) (community-maintained, retrieved 2026-10-16): “Cast Maddening Cacophony with kicker by paying {4}{U}{U}, causing each opponent to mill their library due to Bruvac.”
- Source (re-verified): [`Lord_Xander_the_Collector_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_xander_the_collector_2026-10-14/Lord_Xander_the_Collector_Rules_Attestation.json) → “Bruvac plus Lord Xander attack”
- Source (re-verified): [`Lord_Xander_the_Collector_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_xander_the_collector_2026-10-14/Lord_Xander_the_Collector_Rules_Attestation.json) → “Riverchurn Monument plus Lord Xander attack”
- Source (re-verified): [`Lord_Xander_the_Collector_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_xander_the_collector_2026-10-14/Lord_Xander_the_Collector_Rules_Attestation.json) → “Fraying Sanity plus Lord Xander attack”

### xander-10: Sword of Feast and Famine + Aggravated Assault: extra combats, extra Xander mills

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Lord Xander, the Collector, Sword of Feast and Famine, Aggravated Assault

**Ruling.** The Sword's hit untaps all your lands. In the following main phase, Aggravated Assault ({3}{R}{R}, sorcery speed) untaps your creatures and adds another combat. Repeat: each combat Xander is declared as an attacker again and mills half again.

**Citations**

- Oracle, *Aggravated Assault*: “{3}{R}{R}: Untap all creatures you control. After this main phase, there is an additional combat phase followed by an additional main phase. Activate only as a sorcery.”
- [CR 505.1a](#cr-5051a), [CR 500.8](#cr-5008)
- Commander Spellbook [900-3750](https://commanderspellbook.com/combo/900-3750/) (community-maintained, retrieved 2026-10-16): “Lands you control can tap to produce at least {3}{R}{R}.”
- Source (re-verified): [`Lord_Xander_the_Collector_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_xander_the_collector_2026-10-14/Lord_Xander_the_Collector_Rules_Attestation.json) → “Aggravated Assault plus Sword of Feast and Famine”

### xander-11: Duskmantle Guildmage + Mindcrank, and the Breach line

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Lord Xander, the Collector, Duskmantle Guildmage, Mindcrank, Maddening Cacophony, Underworld Breach, Lion's Eye Diamond, Brain Freeze

**Ruling.** After Duskmantle's first ability resolves this turn, each card put into an opponent's graveyard drains 1. Mindcrank mills them for each life lost, and that repeats until they're dead. Xander's attack or Duskmantle's own mill starts it; tokens don't count. Maddening Cacophony + Duskmantle works without Mindcrank if a player's life is at most half their library. Breach + LED + Brain Freeze is the backup.

**Citations**

- Oracle, *Mindcrank*: “Whenever an opponent loses life, that player mills that many cards.”
- Oracle, *Duskmantle Guildmage*: “{1}{U}{B}: Whenever a card is put into an opponent's graveyard from anywhere this turn, that player loses 1 life.”
- Scryfall ruling, *Duskmantle Guildmage*: “The delayed triggered ability created won’t trigger if a token permanent is put into an opponent’s graveyard.”
- [CR 603.7a](#cr-6037a), [CR 702.138a](#cr-702138a)
- Commander Spellbook [936-5069](https://commanderspellbook.com/combo/936-5069/) (community-maintained, retrieved 2026-10-16): “Activate Duskmantle Guildmage's second ability by paying {2}{U}{B}, causing an opponent to mill two cards.”
- Commander Spellbook [5069-5080](https://commanderspellbook.com/combo/5069-5080/) (community-maintained, retrieved 2026-10-16): “Each opponent has a life total that is less than or equal to half their library size, rounded up.”
- Commander Spellbook [1368-3518-4856](https://commanderspellbook.com/combo/1368-3518-4856/) (community-maintained, retrieved 2026-10-16): “You have at least six other cards in hand and/or graveyard.”
- Source (re-verified): [`Lord_Xander_the_Collector_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_xander_the_collector_2026-10-14/Lord_Xander_the_Collector_Rules_Attestation.json) → “Duskmantle Guildmage plus Mindcrank”
- Source (re-verified): [`Lord_Xander_the_Collector_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_xander_the_collector_2026-10-14/Lord_Xander_the_Collector_Rules_Attestation.json) → “Underworld Breach, Lion's Eye Diamond, and Brain Freeze”

## Engines and payoffs

### xander-06: Cruel Calculations counts the mill

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Lord Xander, the Collector, Cruel Calculations

**Ruling.** Cruel Calculations draws one card per card put from the target player's library into their graveyard this turn. That includes Xander's mill and Bruvac's doubled count. Cards replaced into exile don't count.

**Citations**

- Oracle, *Cruel Calculations*: “Draw X cards, where X is the number of cards that were put into target player's graveyard from their library this turn.”
- [CR 701.17a](#cr-70117a)
- Source (re-verified): [`Lord_Xander_the_Collector_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_xander_the_collector_2026-10-14/Lord_Xander_the_Collector_Rules_Attestation.json) → “Cruel Calculations after Xander mill”

### xander-09: Tergrid steals Xander's discards and sacrifices

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Lord Xander, the Collector, Tergrid, God of Fright // Tergrid's Lantern

**Ruling.** Tergrid triggers for each permanent card an opponent discards to Xander's enter trigger, and for each nontoken permanent they sacrifice to his dies trigger. You can put each one onto the battlefield under your control. Each Tergrid trigger fails if the card has left the graveyard by the time it resolves.

**Citations**

- Oracle, *Tergrid, God of Fright // Tergrid's Lantern*: “Whenever an opponent sacrifices a nontoken permanent or discards a permanent card, you may put that card from a graveyard onto the battlefield under your control.”
- Scryfall ruling, *Tergrid, God of Fright // Tergrid's Lantern*: “If the card leaves the graveyard before Tergrid's ability resolves, you can't put it onto the battlefield, even if it returns to the graveyard before the ability resolves.”
- [CR 603.2](#cr-6032), [CR 701.9a](#cr-7019a)
- Source (re-verified): [`Lord_Xander_the_Collector_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_xander_the_collector_2026-10-14/Lord_Xander_the_Collector_Rules_Attestation.json) → “Tergrid with Xander discard and sacrifice”

## Layers and continuous effects

### xander-04: Hall of Echoes and Helm of the Host

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Lord Xander, the Collector, Hall of Echoes, Helm of the Host

**Ruling.** Hall of Echoes becoming Xander isn't entering, so no enter trigger. If you've controlled it since the turn began, it can attack for its own mill trigger. Helm of the Host's token is non-legendary and hasty. It's made at beginning of combat, so it gets an enter trigger and can then be declared as an attacker for an attack trigger.

**Citations**

- Scryfall ruling, *Helm of the Host*: “The token isn't legendary, and this exception is copiable. If something else copies the token later, that copy also won't be legendary. If you control two or more permanents with the same name but only one is legendary, the "legend rule" doesn't apply.”
- [CR 707.2](#cr-7072), [CR 302.6](#cr-3026)
- Source (re-verified): [`Lord_Xander_the_Collector_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_xander_the_collector_2026-10-14/Lord_Xander_the_Collector_Rules_Attestation.json) → “Hall of Echoes copying Lord Xander”
- Source (re-verified): [`Lord_Xander_the_Collector_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_xander_the_collector_2026-10-14/Lord_Xander_the_Collector_Rules_Attestation.json) → “Helm of the Host on Lord Xander”

## Trigger ordering

### xander-03: Myriad copies: Blade of Selves vs. Auton Soldier

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Lord Xander, the Collector, Blade of Selves, Auton Soldier

**Ruling.** Myriad tokens enter tapped and attacking (one per other opponent), so they trigger enter but not attack. Blade of Selves on the real Xander makes legendary tokens: each gives an enter trigger, then the legend rule leaves one, and each Xander that dies gives a dies trigger. Auton Soldier as Xander isn't legendary and has myriad itself. Its tokens give enter triggers but are exiled at end of combat, which isn't dying, so no dies triggers. Auton-Xander's own attack gives an attack trigger.

**Citations**

- Oracle, *Auton Soldier*: “You may have this creature enter as a copy of any creature on the battlefield, except it isn't legendary, is an artifact in addition to its other types, and has myriad.”
- Scryfall ruling, *Blade of Selves*: “If the equipped creature is legendary, the tokens will all enter the battlefield. Then you'll choose one of them to remain on the battlefield. The others will be put into your graveyard. Any enters-the-battlefield or dies triggers of the tokens will work.”
- Scryfall ruling, *Auton Soldier*: “Although the tokens enter the battlefield attacking, they were never declared as attackers. Abilities that trigger whenever a creature attacks won't trigger, including the myriad ability of the tokens.”
- [CR 702.116a](#cr-702116a), [CR 704.5j](#cr-7045j), [CR 508.4](#cr-5084)
- Source (re-verified): [`Lord_Xander_the_Collector_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_xander_the_collector_2026-10-14/Lord_Xander_the_Collector_Rules_Attestation.json) → “Blade of Selves on Lord Xander”
- Source (re-verified): [`Lord_Xander_the_Collector_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_xander_the_collector_2026-10-14/Lord_Xander_the_Collector_Rules_Attestation.json) → “Auton Soldier copying Lord Xander”

### xander-07: Roaming Throne and Strionic Resonator

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Lord Xander, the Collector, Roaming Throne, Strionic Resonator

**Ruling.** Xander is a Vampire Demon Noble, so a Roaming Throne naming any of those makes all three triggers trigger twice. Strionic Resonator copies one trigger on the stack: two mill-half triggers mill three-quarters.

**Citations**

- Oracle, *Strionic Resonator*: “{2}, {T}: Copy target triggered ability you control. You may choose new targets for the copy.”
- Scryfall ruling, *Roaming Throne*: “Roaming Throne's last ability doesn't copy the triggered ability; it just causes the ability to trigger an additional time. Any choices made as you put the ability onto the stack, such as modes and targets, are made separately for each instance of the ability.”
- [CR 603.2](#cr-6032), [CR 707.10](#cr-70710)
- Source (re-verified): [`Lord_Xander_the_Collector_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_xander_the_collector_2026-10-14/Lord_Xander_the_Collector_Rules_Attestation.json) → “Roaming Throne and Strionic Resonator”

## Zones, commander tax and the command zone

### xander-02: Clones and the legend rule: Phantasmal Image, Molten Duplication, Saw in Half

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Lord Xander, the Collector, Phantasmal Image, Molten Duplication, Saw in Half

**Ruling.** A legendary Xander copy entering gives an enter trigger. The legend rule then puts one Xander into the graveyard, and that counts as dying: a dies trigger, using last-known information. Molten Duplication's hasty token can be the one you keep: the original dies now, the token attacks and dies again at end step. Saw in Half on Xander: one dies trigger, two token enter triggers, then a third Xander dies to the legend rule. A commander that dies can still go to the command zone afterward.

**Citations**

- Scryfall ruling, *Saw in Half*: “Any enters-the-battlefield abilities of the copied creature will trigger when the tokens enter the battlefield. Any "as [this creature] enters" or "[this creature] enters with" abilities of the copied creature will also work.”
- [CR 704.5j](#cr-7045j), [CR 603.10a](#cr-60310a), [CR 903.9a](#cr-9039a)
- Source (re-verified): [`Lord_Xander_the_Collector_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_xander_the_collector_2026-10-14/Lord_Xander_the_Collector_Rules_Attestation.json) → “Phantasmal Image copying Lord Xander”
- Source (re-verified): [`Lord_Xander_the_Collector_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_xander_the_collector_2026-10-14/Lord_Xander_the_Collector_Rules_Attestation.json) → “Molten Duplication on Lord Xander”
- Source (re-verified): [`Lord_Xander_the_Collector_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_xander_the_collector_2026-10-14/Lord_Xander_the_Collector_Rules_Attestation.json) → “Saw in Half on Lord Xander”

### xander-08: Feign Death on your commander: leave it in the graveyard

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Lord Xander, the Collector, Feign Death

**Ruling.** When a Feign Death'd Xander dies, both the dies trigger and the return trigger fire. To get him back you must decline the command-zone move. That move is a state-based action that happens before the triggers resolve, and if he's in the command zone the return finds nothing. The return gives another enter trigger, and he comes back tapped with a +1/+1 counter.

**Citations**

- Oracle, *Feign Death*: “Until end of turn, target creature gains "When this creature dies, return it to the battlefield tapped under its owner's control with a +1/+1 counter on it."”
- [CR 903.9a](#cr-9039a), [CR 400.7](#cr-4007), [CR 704.3](#cr-7043)
- Source (re-verified): [`Lord_Xander_the_Collector_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/lord_xander_the_collector_2026-10-14/Lord_Xander_the_Collector_Rules_Attestation.json) → “Feign Death and commander-zone sequencing”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 107.1a

You can’t choose a fractional number, deal fractional damage, gain fractional life, and so on. If a spell or ability could generate a fractional number, the spell or ability will tell you whether to round up or down.

#### CR 302.6

A creature’s activated ability with the tap symbol or the untap symbol in its activation cost can’t be activated unless the creature has been under its controller’s control continuously since their most recent turn began. A creature can’t attack unless it has been under its controller’s control continuously since their most recent turn began. This rule is informally called the “summoning sickness” rule.

#### CR 400.7

An object that moves from one zone to another becomes a new object with no memory of, or relation to, its previous existence. This rule has the following exceptions.

#### CR 500.8

Some effects can add phases to a turn. They do this by adding the phases directly after the specified phase. If multiple extra phases are created after the same phase, the most recently created phase will occur first.

#### CR 505.1a

Only the first main phase of the turn is a precombat main phase. All other main phases are postcombat main phases. This includes the second main phase of a turn in which the combat phase has been skipped. It is also true of a turn in which an effect has caused an additional combat phase and an additional main phase to be created.

#### CR 508.3a

An ability that reads “Whenever [a creature] attacks, . . .” triggers if that creature is declared as an attacker. Similarly, “Whenever [a creature] attacks [a player, planeswalker, or battle], . . .” triggers if that creature is declared as an attacker attacking that player or permanent. Such abilities won’t trigger if a creature is put onto the battlefield attacking.

#### CR 508.4

If a creature is put onto the battlefield attacking, its controller chooses which defending player, planeswalker a defending player controls, or battle a defending player protects it’s attacking as it enters the battlefield (unless the effect that put it onto the battlefield specifies what it’s attacking). Similarly, if an effect states that a creature is attacking, its controller chooses which defending player, planeswalker a defending player controls, or battle a defending player protects it’s attacking (unless the effect has already specified). Such creatures are “attacking” but, for the …

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 603.6a

Enters-the-battlefield abilities trigger when a permanent enters the battlefield. These are written, “When [this object] enters, . . . “ or “Whenever a [type] enters, . . .” Each time an event puts one or more permanents onto the battlefield, all permanents on the battlefield (including the newcomers) are checked for any enters-the-battlefield triggers that match the event.

#### CR 603.7a

Delayed triggered abilities are created during the resolution of spells or abilities, as the result of a replacement effect being applied, or as a result of a static ability that allows a player to take an action. A delayed triggered ability won’t trigger until it has actually been created, even if its trigger event occurred just beforehand. Other events that happen earlier may make the trigger event impossible.

#### CR 603.10a

Some zone-change triggers look back in time. These are leaves-the-battlefield abilities, abilities that trigger when a player sacrifices a permanent, abilities that trigger when a card leaves a graveyard, and abilities that trigger when an object that all players can see is put into a hand or library.

#### CR 614.1a

Effects that use the word “instead” are replacement effects. Most replacement effects use the word “instead” to indicate what events will be replaced with other events.

#### CR 701.9a

To discard a card, move it from its owner’s hand to that player’s graveyard.

#### CR 701.17a

For a player to mill a number of cards, that player puts that many cards from the top of their library into their graveyard.

#### CR 702.116a

Myriad is a triggered ability that may also create a delayed triggered ability. “Myriad” means “Whenever this creature attacks, for each opponent other than defending player, you may create a token that’s a copy of this creature that’s tapped and attacking that player or a planeswalker they control. If one or more tokens are created this way, exile the tokens at end of combat.”

#### CR 702.138a

Escape represents a static ability that functions while the card with escape is in a player’s graveyard. “Escape [cost]” means “You may cast this card from your graveyard by paying [cost] rather than paying its mana cost.” Casting a spell using its escape ability follows the rules for paying alternative costs in rules 601.2b and 601.2f–h.

#### CR 704.3

Whenever a player would get priority (see rule 117, “Timing and Priority”), the game checks for any of the listed conditions for state-based actions, then performs all applicable state-based actions simultaneously as a single event. If any state-based actions are performed as a result of a check, the check is repeated; otherwise all triggered abilities that are waiting to be put on the stack are put on the stack, then the check is repeated. Once no more state-based actions have been performed as the result of a check and no triggered abilities are waiting to be put on the stack, the …

#### CR 704.5j

If two or more legendary permanents with the same name are controlled by the same player, that player chooses one of them, and the rest are put into their owners’ graveyards. This is called the “legend rule.”

#### CR 707.2

When copying an object, the copy acquires the copiable values of the original object’s characteristics and, for an object on the stack, choices made when casting or activating it (mode, targets, the value of X, whether it was kicked, how it will affect multiple targets, and so on). The copiable values are the values derived from the text printed on the object (that text being name, mana cost, color indicator, card type, subtype, supertype, rules text, power, toughness, and/or loyalty), as modified by other copy effects, by its face-down status, and by “as . . . enters” and “as . . . is turned …

#### CR 707.10

To copy a spell, activated ability, or triggered ability means to put a copy of it onto the stack; a copy of a spell isn’t cast and a copy of an activated ability isn’t activated. A copy of a spell or ability copies both the characteristics of the spell or ability and all decisions made for it, including modes, targets, the value of X, and additional or alternative costs. (See rule 601, “Casting Spells.”) Choices that are normally made on resolution are not copied. If an effect of the copy refers to objects used to pay its costs, it uses the objects used to pay the costs of the original spell …

#### CR 903.9a

If a commander is in a graveyard or in exile and that object was put into that zone since the last time state-based actions were checked, its owner may put it into the command zone. This is a state-based action. See rule 704.

