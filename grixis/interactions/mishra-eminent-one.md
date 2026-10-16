---
title: "Mishra, Eminent One — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Mishra, Eminent One — Interaction Review

> Bot cycle 51 · batch D · reviewed 2026-10-16. Deck: [Mishra, Eminent One](../decks/mishra-eminent-one.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/mishra-eminent-one.txt`](../../exports/grixis-archidekt/mishra-eminent-one.txt) · SHA-256 `13f54e4dd95e420371a70b002cd959c580fcbc9d7f360367288c8784da86caaf` |
| Rulings | **9** (9 verified · 0 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`Mishra_Eminent_One_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mishra_Eminent_One_Approval_Ready_Verification_2026-10-15.md) (Approval-ready verification; rules sections 5–12 re-checked against Oracle, rulings and CR) |

## Contents
- [Summary](#summary)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [Layers and continuous effects](#layers-and-continuous-effects)
- [Timing and priority](#timing-and-priority)
- [Trigger ordering](#trigger-ordering)
- [Rules cited](#rules-cited)

## Summary

Each combat, Mishra makes a hasty 4/4 Warform copy of a noncreature artifact. The list copies Gonti's Aether Heart for infinite turns, Worldwalker Helm (with Urza and Elixir) for infinite mana, and Mindslaver for turn control, plus value and removal artifacts that trigger on both entering and dying. All 22 Spellbook lines in the canonical list are covered; representative ones are cited.

Rules surprises: Helm copies of the Warform keep the name and 4/4 body but lose haste, and they aren't sacrificed; Esoteric Duplicator copies from Mishra's end-step sacrifice arrive a turn later; a One Ring Warform gives no protection; a Portal to Phyrexia Warform edicts but never reanimates. No list errors.

## Combos and engine lines

### mishraeo-02: Gonti's Aether Heart infinite turns: Determined Iteration / Strionic Resonator / Lithoform Engine / Worldwalker Helm / Brudiclad

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mishra, Eminent One, Gonti's Aether Heart, Determined Iteration, Strionic Resonator, Lithoform Engine, Worldwalker Helm, Brudiclad, Telchor Engineer

**Ruling.** A Warform copy of Gonti's Aether Heart has the Heart's energy trigger, and "Gonti's Aether Heart" in it now means the Warform. When it enters, both the original and the Warform trigger, for {E}{E}{E}{E}. One more artifact entering after that gives 4+ more, enough for eight. Options:
- Copy Mishra's trigger with Strionic Resonator or Lithoform Engine.
- Determined Iteration's populate: order Mishra's trigger to resolve first. Populate doesn't target, so it can copy the new Warform.
- Worldwalker Helm's extra Map.
- Brudiclad's Myr.

Then pay eight energy and exile the Warform (not the original) for an extra turn. The original Heart stays, so you repeat it every turn.

**Citations**

- Oracle, *Gonti's Aether Heart*: “Whenever Gonti's Aether Heart or another artifact you control enters, you get {E}{E} (two energy counters).”
- Oracle, *Determined Iteration*: “At the beginning of combat on your turn, populate. The token created this way gains haste. Sacrifice it at the beginning of the next end step.”
- Scryfall ruling, *Determined Iteration*: “Populate doesn't target the creature token you're copying. You choose that creature token as you're taking the populate action. You can choose any creature token you control. If a spell or ability causes you to create a creature token and then instructs you to populate, you may choose to copy the token you just created, or you may choose to copy another creature token you control.”
- Scryfall ruling, *Gonti's Aether Heart*: “Energy counters aren't mana. They don't go away as steps, phases, and turns end, and effects that add mana "of any type" can't give you energy counters.”
- [CR 603.3b](#cr-6033b), [CR 701.36a](#cr-70136a), [CR 500.7](#cr-5007)
- Commander Spellbook [3934-4636-5159](https://commanderspellbook.com/combo/3934-4636-5159/) (community-maintained, retrieved 2026-10-16): “Resolve the Mishra trigger, creating a 4/4 artifact creature token copy of Gonti's Aether Heart named Mishra's Warform.”
- Commander Spellbook [2751-4636-5159](https://commanderspellbook.com/combo/2751-4636-5159/) (community-maintained, retrieved 2026-10-16): “Holding priority, activate Strionic Resonator by paying {2} and tapping it, copying Mishra's trigger.”
- Commander Spellbook [4636-5159-5491](https://commanderspellbook.com/combo/4636-5159-5491/) (community-maintained, retrieved 2026-10-16): “Activate Mishra's Warform by paying eight {E} and exiling it, causing you to take an extra turn after this one.”
- Source (re-verified): [`Mishra_Eminent_One_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mishra_Eminent_One_Approval_Ready_Verification_2026-10-15.md) → “Determined Iteration's populate instruction does not target the token in advance; on resolution it can copy the newly created creature token.”

### mishraeo-03: Worldwalker Helm + Urza + Thousand-Year Elixir: infinite Warforms, Maps and {U}

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mishra, Eminent One, Worldwalker Helm, Urza, Lord High Artificer, Thousand-Year Elixir

**Ruling.** Mishra copies Worldwalker Helm. Helm's replacement adds a Map to every artifact token you create, including the Warform. Urza taps artifacts for {U}. The Warform's {1}{U},{T} copies an artifact token, so it copies itself, plus Maps. Copies of the Warform keep the Warform's name and 4/4 body, but not the haste (that came from Mishra's effect), so Thousand-Year Elixir lets them tap right away. Mishra's end-step sacrifice covers only the original Warform, so the copies stay.

**Citations**

- Oracle, *Worldwalker Helm*: “If you would create one or more artifact tokens, instead create those tokens plus an additional Map token. (It's an artifact with "{1}, {T}, Sacrifice this token: Target creature you control explores. Activate only as a sorcery.")”
- Oracle, *Thousand-Year Elixir*: “You may activate abilities of creatures you control as though those creatures had haste.”
- Scryfall ruling, *Worldwalker Helm*: “Worldwaker Helm's first ability applies to all kinds of artifact tokens that its controller creates, not just Map tokens.”
- [CR 707.9b](#cr-7079b), [CR 614.1a](#cr-6141a), [CR 603.7c](#cr-6037c)
- Commander Spellbook [457-5159-5295-5491](https://commanderspellbook.com/combo/457-5159-5295-5491/) (community-maintained, retrieved 2026-10-16): “Activate Mishra's Warform by paying {1}{U} and tapping it, creating a token copy of it and a Map token for each Mishra's Warform and/or Worldwalker Helm you control.”
- Source (re-verified): [`Mishra_Eminent_One_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mishra_Eminent_One_Approval_Ready_Verification_2026-10-15.md) → “Thousand-Year Elixir allows the newly created non-hasty copies to activate tap abilities immediately.”

### mishraeo-04: Mindslaver Warforms: Strionic + Lithoform, Esoteric Duplicator, Emry, Academy Ruins

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mishra, Eminent One, Mindslaver, Strionic Resonator, Lithoform Engine, Esoteric Duplicator, Emry, Lurker of the Loch, Academy Ruins

**Ruling.** A hasty Mindslaver Warform can pay {4}, tap and sacrifice itself the turn it's made, so you control an opponent's next turn while the real Mindslaver stays. Copying Mishra's trigger (Strionic Resonator) and the Warform's ability (Lithoform Engine) takes up to three opponents' turns each turn cycle. If one player-control effect overlaps another on the same player, the most recent one wins. Esoteric Duplicator turns each Mindslaver sacrifice into a token copy at the next end step. Emry or Academy Ruins recast or restack the real Mindslaver.

**Citations**

- Oracle, *Mindslaver*: “{4}, {T}, Sacrifice Mindslaver: You control target player during that player's next turn. (You see all cards that player could see and make all decisions for them.)”
- Scryfall ruling, *Mindslaver*: “Multiple player-controlling effects that affect the same player overwrite each other. The last one to be created is the one that works.”
- Scryfall ruling, *Mindslaver*: “You can use only the affected player's resources (cards, mana, and so on) to pay costs for that player; you can't use your own. Similarly, you can use the affected player's resources only to pay that player's costs; you can't spend them on your costs.”
- [CR 723.1](#cr-7231), [CR 723.8](#cr-7238)
- Commander Spellbook [1167-2751-3094-5159](https://commanderspellbook.com/combo/1167-2751-3094-5159/) (community-maintained, retrieved 2026-10-16): “Resolve the first Mishra trigger, creating a token copy of Mindslaver that is a 4/4 artifact creature named Mishra's Warform in addition to it's other types.”
- Commander Spellbook [1167-5483](https://commanderspellbook.com/combo/1167-5483/) (community-maintained, retrieved 2026-10-16): “Esoteric Duplicator triggers, causing you to pay {2} to create a copy of Mindslaver at the beginning of the next end step.”

### mishraeo-09: Strionic Resonator / Lithoform Engine Warform + KCI loop; KCI + Scrap Trawler; Emry + One Ring

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mishra, Eminent One, Strionic Resonator, Lithoform Engine, Krark-Clan Ironworks, Scrap Trawler, Myr Retriever, Emry, Lurker of the Loch, The One Ring

**Ruling.** Copy Mishra's trigger with Strionic Resonator (or Lithoform Engine), aimed at the Resonator itself. The new Resonator Warform has haste, so while that trigger copy is still on the stack it can pay {2} and tap to copy it again. Then sacrifice the Warform to KCI for {C}{C}. That's mana-neutral, with infinite artifact ETBs and deaths. The KCI + Scrap Trawler + Myr Retriever loops and Emry + The One Ring also fit this list. A One Ring Warform wasn't cast, so it doesn't give protection.

**Citations**

- Oracle, *Strionic Resonator*: “{2}, {T}: Copy target triggered ability you control. You may choose new targets for the copy.”
- Scryfall ruling, *Strionic Resonator*: “Strionic Resonator targets a triggered ability that has triggered and is on the stack and creates another instance of that ability on the stack. It doesn't cause any object to gain an ability.”
- [CR 707.10](#cr-70710), [CR 603.10a](#cr-60310a)
- Commander Spellbook [2751-4659-5159](https://commanderspellbook.com/combo/2751-4659-5159/) (community-maintained, retrieved 2026-10-16): “Holding priority, activate Krark-Clan Ironworks by sacrificing Mishra's Warform, adding {C}{C}.”
- Commander Spellbook [1329-3363-4659](https://commanderspellbook.com/combo/1329-3363-4659/) (community-maintained, retrieved 2026-10-16): “The One Ring triggers, giving you protection from everything until your next turn.”

## Engines and payoffs

### mishraeo-06: Removal Warforms: Lich's Relic, Portal to Phyrexia, Spine of Ish Sah

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mishra, Eminent One, Lich's Relic, Portal to Phyrexia, Spine of Ish Sah

**Ruling.** Each of these gives removal on every combat:
- **Lich's Relic:** a Warform copy's ETB lets you pay {2}, then destroy up to one creature or planeswalker per opponent.
- **Portal to Phyrexia:** a Warform copy makes each opponent sacrifice three creatures. It's sacrificed at end step, before your upkeep, so you don't get the reanimation trigger.
- **Spine of Ish Sah:** a Warform copy destroys a target permanent. Its return-to-hand trigger does nothing for a token.

**Citations**

- Oracle, *Lich's Relic*: “When this Equipment enters, you may pay {2}. When you do, for each opponent, destroy up to one target creature or planeswalker that player controls.”
- Oracle, *Portal to Phyrexia*: “When this artifact enters, each opponent sacrifices three creatures of their choice.”
- Oracle, *Spine of Ish Sah*: “When this artifact is put into a graveyard from the battlefield, return it to its owner's hand.”
- [CR 603.12](#cr-60312), [CR 111.8](#cr-1118)
- Source (re-verified): [`Mishra_Eminent_One_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mishra_Eminent_One_Approval_Ready_Verification_2026-10-15.md) → “This converts each Mishra combat into repeatable multiplayer creature/planeswalker removal while the source Relic remains available to copy again.”

## Layers and continuous effects

### mishraeo-01: Mishra's Warform: a hasty 4/4 copy of a noncreature artifact, sacrificed at end step

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mishra, Eminent One

**Ruling.** At the beginning of combat on your turn, Mishra copies target noncreature artifact you control. The token is named Mishra's Warform and is a 4/4 Construct artifact creature in addition to its other types. Those exceptions are part of its copiable values. It keeps the original's abilities, mana cost and mana value, but not counters or tapped status. X in the cost counts as 0. ETB abilities trigger, and haste lets you use {T} abilities right away. A Warform of a legendary artifact is still legendary. It doesn't clash with the original, which has a different name, but two legendary Warforms do.

**Citations**

- Oracle, *Mishra, Eminent One*: “At the beginning of combat on your turn, create a token that's a copy of target noncreature artifact you control, except its name is Mishra's Warform and it's a 4/4 Construct artifact creature in addition to its other types. It gains haste until end of turn. Sacrifice it at the beginning of the next end step.”
- Scryfall ruling, *Mishra, Eminent One*: “Except for name, power, toughness, and types, the token copies exactly what was printed on the original permanent and nothing else (unless that permanent is copying something else or it is a token; see below). It doesn’t copy whether that permanent is tapped or untapped, whether it has any counters on it or Auras attached to it, and so on.”
- Scryfall ruling, *Mishra, Eminent One*: “If the copied permanent has {X} in its mana cost, X is 0.”
- [CR 707.9b](#cr-7079b), [CR 707.2](#cr-7072), [CR 704.5j](#cr-7045j)
- Source (re-verified): [`Mishra_Eminent_One_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mishra_Eminent_One_Approval_Ready_Verification_2026-10-15.md) → “A copied legendary artifact produces a legendary Warform; multiple legendary permanents named Mishra's Warform are subject to the legend rule.”

### mishraeo-08: Machine God's Effigy turns creatures into Warform targets

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mishra, Eminent One, Machine God's Effigy, Master Transmuter, Goblin Welder, Goblin Engineer

**Ruling.** Machine God's Effigy can enter as a copy of a creature, except it's only an artifact (not a creature) with "{T}: Add {U}." Those exceptions are copiable, so Mishra can copy the Effigy. The Warform is a 4/4 hasty creature with the copied creature's abilities and the {U} mana ability. Copying Master Transmuter or Goblin Welder gives a hasty extra activation each combat. The Effigy also keeps a legendary creature's supertype and name.

**Citations**

- Oracle, *Machine God's Effigy*: “You may have this artifact enter as a copy of any creature on the battlefield, except it's an artifact and it has "{T}: Add {U}." (It's not a creature.)”
- Scryfall ruling, *Machine God's Effigy*: “If Machine God’s Effigy somehow enters the battlefield at the same time as another creature, it can’t become a copy of that creature. You may choose only a creature that’s already on the battlefield.”
- [CR 707.9a](#cr-7079a), [CR 707.9b](#cr-7079b)
- Source (re-verified): [`Mishra_Eminent_One_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mishra_Eminent_One_Approval_Ready_Verification_2026-10-15.md) → “Mishra can therefore later copy a noncreature Effigy; the resulting Warform becomes an artifact creature and retains the copied creature abilities plus the Effigy's added mana ability.”

## Timing and priority

### mishraeo-07: Sorcery-speed sinks: Repurposing Bay, Uthros station, Esoteric Duplicator at end step

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mishra, Eminent One, Repurposing Bay, Uthros Research Craft, Esoteric Duplicator, Transmute Artifact

**Ruling.** Use the Warform after combat:
- **Repurposing Bay:** at sorcery speed in your postcombat main phase, sacrifice the Warform to find an artifact with mana value one higher.
- **Uthros Research Craft:** station it precombat by tapping Mishra (power 5) for 5 counters. Mishra's combat trigger still fires while he's tapped.
- **Esoteric Duplicator:** if the Warform is sacrificed to Mishra's own end-step trigger, the Duplicator's copy comes at the next turn's end step, because "the next end step" made during an end step is the following turn's.
- **Transmute Artifact:** sacrifices on resolution, not as a cost.

**Citations**

- Oracle, *Repurposing Bay*: “{2}, {T}, Sacrifice another artifact: Search your library for an artifact card with mana value equal to 1 plus the sacrificed artifact's mana value, put that card onto the battlefield, then shuffle. Activate only as a sorcery.”
- Oracle, *Esoteric Duplicator*: “Whenever you sacrifice this artifact or another artifact, you may pay {2}. If you do, at the beginning of the next end step, create a token that's a copy of that artifact.”
- [CR 513.2](#cr-5132), [CR 702.184a](#cr-702184a), [CR 602.5d](#cr-6025d)
- Source (re-verified): [`Mishra_Eminent_One_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mishra_Eminent_One_Approval_Ready_Verification_2026-10-15.md) → “Tapping Mishra this way does not prevent his beginning-of-combat triggered ability from triggering.”
- Source (re-verified): [`Mishra_Eminent_One_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mishra_Eminent_One_Approval_Ready_Verification_2026-10-15.md) → “Warform retains the copied artifact's mana cost and mana value.”

## Trigger ordering

### mishraeo-05: Value Warforms: Ichor Wellspring, Prized Statue, Cryogen Relic, Nihil Spellbomb, Coveted Jewel, The Mightstone and Weakstone

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mishra, Eminent One, Ichor Wellspring, Prized Statue, Cryogen Relic, Nihil Spellbomb, Coveted Jewel, The Mightstone and Weakstone

**Ruling.** A Warform of one of these triggers once when it enters and again when it's sacrificed at end step. Leaves-the-battlefield and dies triggers look back in time, so they fire before the token ceases to exist:
- **Ichor Wellspring, Cryogen Relic:** draw twice.
- **Prized Statue:** two Treasures.
- **Nihil Spellbomb:** haste lets it sacrifice itself right away to exile a graveyard, then pay {B} to draw.
- **Coveted Jewel:** draws three and can tap for three mana immediately.
- **The Mightstone and Weakstone:** draw two or -5/-5, then taps for {C}{C}.

**Citations**

- Oracle, *Ichor Wellspring*: “When this artifact enters or is put into a graveyard from the battlefield, draw a card.”
- Oracle, *Nihil Spellbomb*: “When this artifact is put into a graveyard from the battlefield, you may pay {B}. If you do, draw a card.”
- Scryfall ruling, *Ichor Wellspring*: “The ability will trigger when Ichor Wellspring is put into a graveyard from the battlefield, even if the ability that triggered when it entered hasn't resolved yet.”
- [CR 603.10a](#cr-60310a), [CR 111.7](#cr-1117), [CR 702.10c](#cr-70210c)
- Source (re-verified): [`Mishra_Eminent_One_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mishra_Eminent_One_Approval_Ready_Verification_2026-10-15.md) → “The token ceasing to exist after reaching the graveyard does not prevent the graveyard-from-battlefield trigger.”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 111.7

A token that’s in a zone other than the battlefield ceases to exist. This is a state-based action; see rule 704. (Note that if a token changes zones, applicable triggered abilities will trigger before the token ceases to exist.)

#### CR 111.8

A token that has left the battlefield can’t move to another zone or come back onto the battlefield. If such a token would change zones, it remains in its current zone instead. It ceases to exist the next time state-based actions are checked; see rule 704.

#### CR 500.7

Some effects can give a player extra turns. They do this by adding the turns directly after the specified turn. If a player is given multiple extra turns, the extra turns are added one at a time. If multiple players are given extra turns, the extra turns are added one at a time, in APNAP order (see rule 101.4). The most recently created turn will be taken first.

#### CR 513.2

If a permanent with an ability that triggers “at the beginning of the end step” enters the battlefield during this step, that ability won’t trigger until the next turn’s end step. Likewise, if a delayed triggered ability that triggers “at the beginning of the next end step” is created during this step, that ability won’t trigger until the next turn’s end step. In other words, the step doesn’t “back up” so those abilities can go on the stack. This rule applies only to triggered abilities; it doesn’t apply to continuous effects whose durations say “until end of turn” or “this turn.” (See rule …

#### CR 602.5d

Activated abilities that read “Activate only as a sorcery” mean the player must follow the timing rules for casting a sorcery spell, though the ability isn’t actually a sorcery. The player doesn’t actually need to have a sorcery card that they could cast.

#### CR 603.3b

If multiple abilities have triggered since the last time a player received priority, the abilities are placed on the stack in a two-part process. First, each player, in APNAP order, puts each triggered ability they control with a trigger condition that isn’t another ability triggering on the stack in any order they choose. (See rule 101.4.) Second, each player, in APNAP order, puts all remaining triggered abilities they control on the stack in any order they choose. Then the game once again checks for and performs state-based actions until none are performed, then abilities that triggered …

#### CR 603.7c

A delayed triggered ability that refers to a particular object still affects it even if the object changes characteristics. However, if that object is no longer in the zone it’s expected to be in at the time the delayed triggered ability resolves, the ability won’t affect it. (Note that if that object left that zone and then returned, it’s a new object and thus won’t be affected. See rule 400.7.)

#### CR 603.10a

Some zone-change triggers look back in time. These are leaves-the-battlefield abilities, abilities that trigger when a player sacrifices a permanent, abilities that trigger when a card leaves a graveyard, and abilities that trigger when an object that all players can see is put into a hand or library.

#### CR 603.12

A resolving spell or ability may allow or instruct a player to take an action and create a triggered ability that triggers “when [a player] [does or doesn’t]” take that action or “when [something happens] this way.” These reflexive triggered abilities follow the rules for delayed triggered abilities (see rule 603.7), except that they’re checked immediately after being created and trigger based on whether the trigger event or events occurred earlier during the resolution of the spell or ability that created them.

#### CR 614.1a

Effects that use the word “instead” are replacement effects. Most replacement effects use the word “instead” to indicate what events will be replaced with other events.

#### CR 701.36a

To populate means to choose a creature token you control and create a token that’s a copy of that creature token.

#### CR 702.10c

If a creature has haste, its controller can activate its activated abilities whose cost includes the tap symbol or the untap symbol even if that creature hasn’t been controlled by that player continuously since their most recent turn began. (See rule 302.6.)

#### CR 702.184a

Station is an activated ability. “Station” means “Tap another untapped creature you control: Put a number of charge counters on this permanent equal to the tapped creature’s power. Activate only as a sorcery.”

#### CR 704.5j

If two or more legendary permanents with the same name are controlled by the same player, that player chooses one of them, and the rest are put into their owners’ graveyards. This is called the “legend rule.”

#### CR 707.2

When copying an object, the copy acquires the copiable values of the original object’s characteristics and, for an object on the stack, choices made when casting or activating it (mode, targets, the value of X, whether it was kicked, how it will affect multiple targets, and so on). The copiable values are the values derived from the text printed on the object (that text being name, mana cost, color indicator, card type, subtype, supertype, rules text, power, toughness, and/or loyalty), as modified by other copy effects, by its face-down status, and by “as . . . enters” and “as . . . is turned …

#### CR 707.9a

Some copy effects cause the copy to gain an ability as part of the copying process. This ability becomes part of the copiable values for the copy, along with any other abilities that were copied.

#### CR 707.9b

Some copy effects modify a characteristic as part of the copying process. The final set of values for that characteristic becomes part of the copiable values of the copy.

#### CR 707.10

To copy a spell, activated ability, or triggered ability means to put a copy of it onto the stack; a copy of a spell isn’t cast and a copy of an activated ability isn’t activated. A copy of a spell or ability copies both the characteristics of the spell or ability and all decisions made for it, including modes, targets, the value of X, and additional or alternative costs. (See rule 601, “Casting Spells.”) Choices that are normally made on resolution are not copied. If an effect of the copy refers to objects used to pay its costs, it uses the objects used to pay the costs of the original spell …

#### CR 723.1

Some cards allow a player to control another player during that player’s next turn. This effect applies to the next turn that the affected player actually takes. The affected player is controlled during the entire turn; the effect doesn’t end until the beginning of the next turn.

#### CR 723.8

A player who controls another player also continues to make their own choices and decisions.

