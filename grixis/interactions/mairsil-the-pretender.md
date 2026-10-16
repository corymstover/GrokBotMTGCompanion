---
title: "Mairsil, the Pretender — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Mairsil, the Pretender — Interaction Review

> Bot cycle 51 · batch D · reviewed 2026-10-16. Deck: [Mairsil, the Pretender](../decks/mairsil-the-pretender.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/mairsil-the-pretender.txt`](../../exports/grixis-archidekt/mairsil-the-pretender.txt) · SHA-256 `843c09811f41b7bcdf5d7e4aec1c27de69d48dfa071cd3cc905541618bf10e94` |
| Rulings | **11** (10 verified · 1 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md) (Approval-ready verification; rules conclusions re-checked against Oracle, rulings and CR) |

## Contents
- [Summary](#summary)
- [Flags and open questions](#flags-and-open-questions)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [Layers and continuous effects](#layers-and-continuous-effects)
- [Timing and priority](#timing-and-priority)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [What the list depends on](#what-the-list-depends-on)
- [Rules cited](#rules-cited)

## Summary

Mairsil cages artifacts and creatures from hand or graveyard and uses their activated abilities, once per instance per turn. The list combines Quicksilver Elemental loops with Gilded Lotus and untappers, Tree of Perdition + Hateflayer, the Aetherling + Disk + Anger lock, and blink/copy resets (Pack Rat, Spark Double, Essence Flux, Displacer Kitten). Five Spellbook lines are confirmed against the canonical list.

Rules surprises: caged Asmodeus draws seven for real; Rings copies the Pack Rat activation without the discard; Spark Double gets the caged abilities on its own; a caged Wishclaw can't be activated. The Marvin line is unconfirmed.

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [mairsil-10](#mairsil-10-marvin-murderous-mimic-copies-mairsils-acquired-abilities--without-the-once-per-turn-limit) | ⚠️ uncertain | Marvin, Murderous Mimic copies Mairsil's acquired abilities — without the once-per-turn limit? | No official ruling on whether Mairsil's once-each-turn restriction applies to Marvin's instances; this list's Marvin line depends on it. |

## Commander rules text and edge cases

### mairsil-01: Cage from hand or graveyard; one activation per caged ability instance per turn

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mairsil, the Pretender

**Ruling.** When Mairsil enters, you may exile an artifact or creature card from your hand or graveyard with a cage counter. Mairsil then has every activated ability of the cards you own in exile with cage counters. Triggered and static abilities don't come along. Self-references on a caged ability mean Mairsil (Pack Rat's "copy of this creature" copies Mairsil). Each instance can be activated once each turn. If two caged cards share an ability, Mairsil has two instances. Caged cards stay caged when Mairsil leaves, and a returning Mairsil sees them all again.

**Citations**

- Oracle, *Mairsil, the Pretender*: “Mairsil has all activated abilities of all cards you own in exile with cage counters on them. You may activate each of those abilities only once each turn.”
- Scryfall ruling, *Mairsil, the Pretender*: “If an activated ability of a card in exile with a cage counter on it references the card it's printed on by name, treat Mairsil's instance of that ability as though it referenced Mairsil by name instead. For instance, if Mairsil exiles Magus of the Mind, the cost to activate the ability includes sacrificing Mairsil, not sacrificing Magus of the Mind.”
- Scryfall ruling, *Mairsil, the Pretender*: “The exiled cards remain exiled with cage counters when Mairsil leaves the battlefield. If Mairsil returns to the battlefield, it will see all of those exiled cards with cage counters on them.”
- Scryfall ruling, *Mairsil, the Pretender*: “If multiple cards exiled with cage counters on them have the same ability, Mairsil will have multiple instances of that ability. Each may be activated once each turn.”
- [CR 113.3b](#cr-1133b), [CR 400.7](#cr-4007), [CR 602.5b](#cr-6025b)
- Source (re-verified): [`Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md) → “Mairsil cages an artifact or creature card from hand or graveyard on entry”

## Combos and engine lines

### mairsil-02: Quicksilver Elemental + Gilded Lotus + Morphling / Horseshoe Crab / Staff of Domination

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mairsil, the Pretender, Quicksilver Elemental, Gilded Lotus, Morphling, Horseshoe Crab, Staff of Domination

**Ruling.** With Gilded Lotus, Quicksilver Elemental and one untapper caged:
1. Tap Mairsil with Lotus's ability for {U}{U}{U}.
2. Untap it with the untapper: {U} for Morphling or Horseshoe Crab, or {1} for Staff of Domination.
3. Pay {U} for Quicksilver Elemental's ability, targeting Mairsil itself. Mairsil gains new instances of all its activated abilities until end of turn, so the once-per-turn limit is spent on old instances only.

Each loop nets {U}. With Staff, the {5} draw and {2} lifegain abilities go infinite too. Mairsil needs to have been under your control since your turn began (or have haste), because Lotus's ability uses {T}. Walking Ballista (cast for huge X) is the main mana outlet.

**Citations**

- Oracle, *Quicksilver Elemental*: “{U}: This creature gains all activated abilities of target creature until end of turn.”
- Oracle, *Gilded Lotus*: “{T}: Add three mana of any one color.”
- Scryfall ruling, *Quicksilver Elemental*: “If you make two copies of an ability that can be activated once a turn, you can activate each of them once a turn.”
- Scryfall ruling, *Quicksilver Elemental*: “You can activate the ability more than once, collecting abilities from multiple creatures (or the same creature more than once).”
- [CR 302.6](#cr-3026), [CR 602.5b](#cr-6025b)
- Commander Spellbook [1369-5112-5116-5137](https://commanderspellbook.com/combo/1369-5112-5116-5137/) (community-maintained, retrieved 2026-10-16): “Activate Mairsil using Quicksilver Elemental's ability by paying {U}, causing Mairsil to gain all activated abilities of itself until end of turn.”
- Commander Spellbook [1369-3995-5112-5116](https://commanderspellbook.com/combo/1369-3995-5112-5116/) (community-maintained, retrieved 2026-10-16): “Activate Mairsil using Horseshoe Crab's ability by paying {U}, untapping it.”
- Commander Spellbook [1369-2645-5112-5116](https://commanderspellbook.com/combo/1369-2645-5112-5116/) (community-maintained, retrieved 2026-10-16): “Activate Mairsil using Staff of Domination's first ability by paying {1}, untapping it.”
- Source (re-verified): [`Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md) → “established Mairsil combo engine that can create fresh instances of acquired activated abilities”

### mairsil-03: Tree of Perdition + Hateflayer: swap life, then {Q} for power

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mairsil, the Pretender, Tree of Perdition, Hateflayer

**Ruling.** With both caged:
1. Tap Mairsil with Tree of Perdition's ability. The target opponent's life total and Mairsil's toughness are exchanged. Mairsil is printed 4/4, so the opponent goes to 4.
2. Pay {2}{R} and untap Mairsil ({Q}) for Hateflayer's ability. It deals damage equal to Mairsil's power (4) to that opponent.

The line needs Mairsil's toughness to be no higher than its power, and both {T} and {Q} need Mairsil free of summoning sickness. Endling, Torchling and Morphling's caged +1/-1 abilities can fix the stats. If Mairsil leaves the battlefield before the exchange resolves, nothing happens.

**Citations**

- Oracle, *Tree of Perdition*: “{T}: Exchange target opponent's life total with this creature's toughness.”
- Oracle, *Hateflayer*: “{2}{R}, {Q}: This creature deals damage equal to its power to any target.”
- Scryfall ruling, *Hateflayer*: “The "summoning sickness" rule applies to {Q}. If a creature with an {Q} ability hasn't been under your control since your most recent turn began, you can't activate that ability. Ignore this rule if the creature also has haste.”
- Scryfall ruling, *Tree of Perdition*: “If Tree of Perdition isn't on the battlefield when the ability resolves, the exchange can't happen and the ability will have no effect. Notably, activating the ability and giving Tree of Perdition -13/-13 in response won't cause your opponent to lose the game.”
- [CR 302.6](#cr-3026), [CR 701.12a](#cr-70112a), [CR 701.12c](#cr-70112c)
- Commander Spellbook [2615-4449-5112](https://commanderspellbook.com/combo/2615-4449-5112/) (community-maintained, retrieved 2026-10-16): “Mairsil's toughness is less than or equal to its power.”
- Commander Spellbook [2615-4449-5112](https://commanderspellbook.com/combo/2615-4449-5112/) (community-maintained, retrieved 2026-10-16): “Activate Mairsil using Hateflayer's ability by paying {2}{R} and untapping it, dealing damage equal to Mairsil's power to the opponent.”

### mairsil-04: Aetherling + Nevinyrral's Disk + Anger: a wrath every turn

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mairsil, the Pretender, Aetherling, Nevinyrral's Disk, Anger

**Ruling.** With Disk and Aetherling caged, Anger in your graveyard and a Mountain in play:
1. Activate Disk's ability ({1}, {T}) on Mairsil.
2. Holding priority, pay {U} for Aetherling's exile ability. Mairsil is exiled and returns at the beginning of the next end step.
3. The wrath resolves without Mairsil on the battlefield.

When Mairsil returns, its cage trigger fires again. As a new object it has fresh activations, and Anger's haste lets it tap for Disk on the next turn, so you can repeat on every player's turn. Exiling your commander gives you the option to put it into the command zone; decline it. Only Mountain-typed lands keep Anger working (Volcanic Island, Badlands, Steam Vents, Blood Crypt). Your own artifacts die to every wrath too.

**Citations**

- Oracle, *Aetherling*: “{U}: Exile this creature. Return it to the battlefield under its owner's control at the beginning of the next end step.”
- Oracle, *Anger*: “As long as this card is in your graveyard and you control a Mountain, creatures you control have haste.”
- Scryfall ruling, *Aetherling*: “Aetherling's first ability will return it to the battlefield only if that ability also exiled it. If Aetherling left the battlefield in response to that ability, it won't return, even if it was exiled by another spell or ability.”
- [CR 903.9a](#cr-9039a), [CR 400.7](#cr-4007), [CR 702.10c](#cr-70210c)
- Commander Spellbook [1050-4068-4439-5112](https://commanderspellbook.com/combo/1050-4068-4439-5112/) (community-maintained, retrieved 2026-10-16): “Holding priority, activate Mairsil using Aetherling's first ability by paying {U}, exiling it and returning it to the battlefield at beginning of the next end step.”

### mairsil-05: Rings of Brighthearth + Aphetto Alchemist + Gilded Lotus

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Rings of Brighthearth, Aphetto Alchemist, Gilded Lotus

**Ruling.** This combo doesn't need Mairsil, and all three cards are on the battlefield. Tap Gilded Lotus for three mana, then tap Aphetto Alchemist to untap Lotus. Pay {2} to Rings to copy that ability, and point the copy at the Alchemist. Each loop nets one mana. Lotus's ability is a mana ability, so Rings can't copy it, but the Alchemist's ability is targeted, so it's not a mana ability and can be copied. Rings's {2} is paid when its trigger resolves, so it isn't an activation cost and Training Grounds can't reduce it.

**Citations**

- Oracle, *Rings of Brighthearth*: “Whenever you activate an ability, if it isn't a mana ability, you may pay {2}. If you do, copy that ability. You may choose new targets for the copy.”
- Scryfall ruling, *Rings of Brighthearth*: “You can't pay {2} more than once for each time the triggered ability of Rings of Brighthearth resolves.”
- [CR 605.1a](#cr-6051a), [CR 707.10](#cr-70710)
- Commander Spellbook [4091-4235-5116](https://commanderspellbook.com/combo/4091-4235-5116/) (community-maintained, retrieved 2026-10-16): “Rings of Brighthearth triggers, allowing you to pay {2} to copy Aphetto Alchemist's ability and choose a new target for the copy.”

## Engines and payoffs

### mairsil-06: Pack Rat caged: discard to copy Mairsil; Rings copies the activation

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mairsil, the Pretender, Pack Rat, Rings of Brighthearth, Training Grounds, Anger, Thousand-Year Elixir

**Ruling.** Caged Pack Rat gives Mairsil "{2}{B}, Discard a card: Create a token that's a copy of Mairsil." The token copies Mairsil's printed static ability, so it has all caged abilities too. Its cage trigger fires even though the legend rule then removes one copy, and it can cage the card you just discarded. If you keep the token, its abilities are new instances, but tap abilities need haste (Anger) or Thousand-Year Elixir. The original Mairsil then goes to the graveyard or command zone, and recasting it later costs commander tax. Rings copies the Pack Rat activation without the discard. A copied ability isn't activated, so it doesn't use up Mairsil's once-per-turn limit. Training Grounds makes the activation cost just {B}.

**Citations**

- Oracle, *Pack Rat*: “{2}{B}, Discard a card: Create a token that's a copy of this creature.”
- Oracle, *Training Grounds*: “Activated abilities of creatures you control cost {2} less to activate. This effect can't reduce the mana in that cost to less than one mana.”
- Scryfall ruling, *Mairsil, the Pretender*: “If you have a creature enter the battlefield as a copy of Mairsil, its first ability triggers. You won't be able to activate any abilities before the "legend rule" applies, but the triggered ability will still let you exile another card with a cage counter regardless of which Mairsil you keep.”
- Scryfall ruling, *Training Grounds*: “Training Grounds won't affect a cost that isn't the cost to activate a creature's activated ability. For example, it won't affect Flameblast Dragon's {X}{R} cost, since that's a cost paid when a triggered ability resolves, and it won't affect a kicker cost, since that's an additional cost to cast a spell.”
- [CR 704.5j](#cr-7045j), [CR 707.2](#cr-7072), [CR 707.10](#cr-70710)
- Source (re-verified): [`Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md) → “Rings can copy the Pack Rat activation; the copied ability does not require paying the discard cost again”

## Layers and continuous effects

### mairsil-07: Spark Double copies the cage ability, not the gained abilities

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mairsil, the Pretender, Spark Double

**Ruling.** Spark Double enters as a nonlegendary copy of Mairsil with a +1/+1 counter, so the legend rule doesn't apply and the cage trigger fires. It doesn't copy the abilities Mairsil has gained. It does copy Mairsil's printed static ability, though, so on its own it has every caged ability with its own once-per-turn limits. That counter also gives a caged Walking Ballista's "remove a +1/+1 counter" ability something to remove. Spark Double needs haste to use the {T} abilities on the turn it enters.

**Citations**

- Oracle, *Spark Double*: “You may have this creature enter as a copy of a creature or planeswalker you control, except it enters with an additional +1/+1 counter on it if it's a creature, it enters with an additional loyalty counter on it if it's a planeswalker, and it isn't legendary.”
- Scryfall ruling, *Spark Double*: “Spark Double copies exactly what was printed on the original permanent (unless that permanent is copying something else or is a token; see below). It doesn’t copy whether that permanent is tapped or untapped, whether it has any counters on it or any Auras and Equipment attached to it, or any non-copy effects that have changed its power, toughness, types, color, or so on.”
- [CR 707.2](#cr-7072), [CR 707.9b](#cr-7079b), [CR 302.6](#cr-3026)
- Source (re-verified): [`Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md) → “Spark Double copies Mairsil's printed static cage ability, so once on the battlefield it independently gains all activated abilities from the owner's caged cards”

## Timing and priority

### mairsil-11: Thousand-Year Elixir lets new Mairsils tap but not attack; Wishclaw can't be used from the cage

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mairsil, the Pretender, Thousand-Year Elixir, Wishclaw Talisman, Lightning Greaves

**Ruling.** Thousand-Year Elixir lets a Mairsil that just entered (a recast, blinked or Pack Rat copy) use {T} abilities at once, but it doesn't give haste for attacking. Lightning Greaves gives real haste, plus shroud. Your own Minamo, Patriar's Seal and Elixir untaps can't target a shrouded Mairsil, though its abilities still work. Don't cage Wishclaw Talisman: on Mairsil its cost asks you to remove a wish counter from Mairsil, which has none. Cast Wishclaw as a tutor instead.

**Citations**

- Oracle, *Thousand-Year Elixir*: “You may activate abilities of creatures you control as though those creatures had haste.”
- Oracle, *Wishclaw Talisman*: “{1}, {T}, Remove a wish counter from this artifact: Search your library for a card, put it into your hand, then shuffle. An opponent gains control of this artifact. Activate only during your turn.”
- Scryfall ruling, *Thousand-Year Elixir*: “Thousand-Year Elixir doesn’t actually grant haste to creatures you control, nor does it let you attack with them as though they had haste.”
- [CR 302.6](#cr-3026), [CR 702.18a](#cr-70218a), [CR 118.3](#cr-1183)

## Zones, commander tax and the command zone

### mairsil-08: Blink resets: Essence Flux, Displacer Kitten, Arcanis, Minamo / Patriar's Seal untaps

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mairsil, the Pretender, Essence Flux, Displacer Kitten, Arcanis the Omnipotent, Minamo, School at Water's Edge, Patriar's Seal

**Ruling.** Blinked by Essence Flux or Displacer Kitten, Mairsil comes back as a new object. You get another cage trigger and fresh instances of every caged ability. Caged cards stay caged. Kitten triggers on every noncreature spell, and that includes Faithless Looting's flashback. A blinked Mairsil needs haste for {T} abilities that turn. Caged Arcanis gives "{2}{U}{U}: Return Mairsil to its owner's hand" for a recast-and-cage. Minamo ({U},{T}) and Patriar's Seal ({1},{T}) untap Mairsil because it's legendary, which gives a second use of a caged tap ability.

**Citations**

- Oracle, *Displacer Kitten*: “Whenever you cast a noncreature spell, exile up to one target nonland permanent you control, then return that card to the battlefield under its owner's control.”
- Oracle, *Minamo, School at Water's Edge*: “{U}, {T}: Untap target legendary permanent.”
- Scryfall ruling, *Displacer Kitten*: “When the card returns to the battlefield, it will be a new object with no connection to the card that was exiled. Auras attached to the exiled creature will be put into their owners' graveyards. Any Equipment will become unattached and remain on the battlefield. Any counters on the exiled permanent will cease to exist.”
- [CR 400.7](#cr-4007), [CR 302.6](#cr-3026)
- Source (re-verified): [`Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md) → “the returned card is explicitly a new object, producing another cage ETB and fresh activation instances”

## What the list depends on

### mairsil-09: Drawbacks stay behind: Asmodeus, Minion of Leshrac, Shauku

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mairsil, the Pretender, Asmodeus the Archfiend, Minion of Leshrac, Shauku, Endbringer

**Ruling.** Mairsil gains only activated abilities, so the drawbacks don't come along:
- **Asmodeus:** {B}{B}{B} draws seven real cards, because Binding Contract is a static replacement on Asmodeus. Asmodeus's {B} return ability is linked to that static ability, so on Mairsil it returns nothing.
- **Minion of Leshrac:** Mairsil gets "{T}: Destroy target creature or land" with no upkeep damage.
- **Shauku:** Mairsil gets "{T}: Exile target creature" with no life loss or attack restriction.

**Citations**

- Oracle, *Asmodeus the Archfiend*: “{B}{B}{B}: Draw seven cards.”
- Oracle, *Minion of Leshrac*: “{T}: Destroy target creature or land.”
- Oracle, *Shauku, Endbringer*: “{T}: Exile target creature and put a +1/+1 counter on Shauku.”
- Scryfall ruling, *Mairsil, the Pretender*: “Activated abilities contain a colon. They're generally written "[Cost]: [Effect]." Some keyword abilities (such as equip) are activated abilities and will have colons in their reminder text. Mairsil won't gain triggered abilities (which start with "when," "whenever," or "at").”
- Scryfall ruling, *Mairsil, the Pretender*: “If Mairsil gains an activated ability that's normally linked to a non-activated ability of the card it came from, the ability Mairsil has isn't linked to any ability. For example, if Mairsil exiles Prototype Portal, the activated ability creates no tokens at all; it doesn't create Prototype Portal tokens.”
- [CR 113.3b](#cr-1133b), [CR 607.1](#cr-6071)
- Source (re-verified): [`Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md) → “the caged `{B}{B}{B}: Draw seven cards` therefore draws normally”

### mairsil-10: Marvin, Murderous Mimic copies Mairsil's acquired abilities — without the once-per-turn limit?

**Status:** ⚠️ uncertain · **Evidence:** hypothesis · **Cards:** Mairsil, the Pretender, Marvin, Murderous Mimic

**Ruling.** Marvin has all activated abilities of your other creatures, so it has the caged abilities Mairsil has. Marvin's ruling confirms it doesn't gain static abilities. The source argues that Mairsil's once-each-turn restriction is a separate static ability, so Marvin's instances aren't limited. If so, Marvin with caged Gilded Lotus and Morphling or Horseshoe Crab untaps itself for {U} and nets {U}{U} per loop with no Quicksilver Elemental. No official ruling covers whether "those abilities" in Mairsil's restriction reach the abilities Marvin gets.

**Uncertain.** No official ruling on whether Mairsil's once-each-turn restriction applies to Marvin's instances; this list's Marvin line depends on it.

**Citations**

- Oracle, *Marvin, Murderous Mimic*: “Marvin has all activated abilities of creatures you control that don't have the same name as this creature.”
- Scryfall ruling, *Marvin, Murderous Mimic*: “Marvin gains only activated abilities. It doesn't gain triggered abilities or static abilities. Activated abilities contain a colon. They're generally written "[Cost]: [Effect]." Some keywords are activated abilities and may have colons in their reminder text.”
- [CR 113.3b](#cr-1133b), [CR 602.5b](#cr-6025b)
- Source (re-verified): [`Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md) → “Mairsil's separate once-per-turn restriction is static, so Marvin provides a parallel activated-ability engine without inheriting that restriction”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 113.3b

Activated abilities have a cost and an effect. They are written as “[Cost]: [Effect.] [Activation instructions (if any).]” A player may activate such an ability whenever they have priority. Doing so puts it on the stack, where it remains until it’s countered, it resolves, or it otherwise leaves the stack. See rule 602, “Activating Activated Abilities.”

#### CR 118.3

A player can’t pay a cost without having the necessary resources to pay it fully. For example, a player with only 1 life can’t pay a cost of 2 life, and a permanent that’s already tapped can’t be tapped to pay a cost. See rule 202, “Mana Cost and Color,” and rule 602, “Activating Activated Abilities.”

#### CR 302.6

A creature’s activated ability with the tap symbol or the untap symbol in its activation cost can’t be activated unless the creature has been under its controller’s control continuously since their most recent turn began. A creature can’t attack unless it has been under its controller’s control continuously since their most recent turn began. This rule is informally called the “summoning sickness” rule.

#### CR 400.7

An object that moves from one zone to another becomes a new object with no memory of, or relation to, its previous existence. This rule has the following exceptions.

#### CR 602.5b

If an activated ability has a restriction on its use (for example, “Activate only once each turn”), the restriction continues to apply to that object even if its controller changes.

#### CR 605.1a

An activated ability is a mana ability if it meets all of the following criteria: it doesn’t require a target (see rule 115.6), it could add mana to a player’s mana pool when it resolves, it’s not a loyalty ability (see rule 606, “Loyalty Abilities”), and its cost and effect don’t move any card to or from a library. Do not take into account replacement effects that may apply, other than self-replacement effects, when evaluating these criteria.

#### CR 607.1

An object may have two abilities printed on it such that one of them causes actions to be taken or objects or players to be affected and the other one directly refers to those actions, objects, or players. If so, these two abilities are linked: the second refers only to actions that were taken or objects or players that were affected by the first, and not by any other ability.

#### CR 701.12a

A spell or ability may instruct players to exchange something (for example, life totals or control of two permanents) as part of its resolution. When such a spell or ability resolves, if the entire exchange can’t be completed, no part of the exchange occurs.

#### CR 701.12c

When life totals are exchanged, each player gains or loses the amount of life necessary to equal the other player’s previous life total. Replacement effects may modify these gains and losses, and triggered abilities may trigger on them. A player who can’t gain life can’t be given a higher life total this way, and a player who can’t lose life can’t be given a lower life total this way (see rules 119.7–8).

#### CR 702.10c

If a creature has haste, its controller can activate its activated abilities whose cost includes the tap symbol or the untap symbol even if that creature hasn’t been controlled by that player continuously since their most recent turn began. (See rule 302.6.)

#### CR 702.18a

Shroud is a static ability. “Shroud” means “This permanent or player can’t be the target of spells or abilities.”

#### CR 704.5j

If two or more legendary permanents with the same name are controlled by the same player, that player chooses one of them, and the rest are put into their owners’ graveyards. This is called the “legend rule.”

#### CR 707.2

When copying an object, the copy acquires the copiable values of the original object’s characteristics and, for an object on the stack, choices made when casting or activating it (mode, targets, the value of X, whether it was kicked, how it will affect multiple targets, and so on). The copiable values are the values derived from the text printed on the object (that text being name, mana cost, color indicator, card type, subtype, supertype, rules text, power, toughness, and/or loyalty), as modified by other copy effects, by its face-down status, and by “as . . . enters” and “as . . . is turned …

#### CR 707.9b

Some copy effects modify a characteristic as part of the copying process. The final set of values for that characteristic becomes part of the copiable values of the copy.

#### CR 707.10

To copy a spell, activated ability, or triggered ability means to put a copy of it onto the stack; a copy of a spell isn’t cast and a copy of an activated ability isn’t activated. A copy of a spell or ability copies both the characteristics of the spell or ability and all decisions made for it, including modes, targets, the value of X, and additional or alternative costs. (See rule 601, “Casting Spells.”) Choices that are normally made on resolution are not copied. If an effect of the copy refers to objects used to pay its costs, it uses the objects used to pay the costs of the original spell …

#### CR 903.9a

If a commander is in a graveyard or in exile and that object was put into that zone since the last time state-based actions were checked, its owner may put it into the command zone. This is a state-based action. See rule 704.

