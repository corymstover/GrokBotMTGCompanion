---
title: "Rules Interactions"
category: rules
tags: [rules, interactions, rulings]
issues: [9]
generated_by: scripts/build_rules_interactions.py
sources: [cr, scryfall]
related: ["EDH Archetypes.md", "EDH Win Conditions.md", "EDH Pairings.md", "EDH Packages.md", "EDH Interaction.md", "cEDH Primer.md"]
schema: 2
---

# Rules Interactions

> **Source of truth:** Magic: The Gathering **Comprehensive Rules, effective 2026-09-25** ([official text](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt), Wizards of the Coast). Rule text below is **quoted verbatim** (long rules trimmed with "…"); card rulings are **official WotC rulings** from the Scryfall rulings bulk (2026-10-15), quoted verbatim and linked to the card entries that carry them. Plain-language summaries are labeled **Summary** and are paraphrase, not rules text. Started Bot cycle 3, extended Bot cycles 4–5 (issue [#9](https://github.com/corymstover/GrokBotMTGCompanion/issues/9)).

## Contents
- [Layers & timestamps](#layers--timestamps) — CR 613
- [Dependency](#dependency) — CR 613.8
- [Replacement effects vs. triggered abilities](#replacement-effects-vs-triggered-abilities) — CR 614
- [State-based actions](#state-based-actions) — CR 704
- [Copy effects](#copy-effects) — CR 707
- [Commander: color identity](#commander-color-identity) — CR 903.4
- [Commander: returning to the command zone](#commander-returning-to-the-command-zone) — CR 903.9
- [Worked layer examples (official CR examples)](#worked-layer-examples-official-cr-examples) — CR 613
- [Stack & priority](#stack--priority) — CR 117 / 405 / 608
- [Casting vs. copying a spell](#casting-vs-copying-a-spell) — CR 601 / 707.10 / 707.12
- [Combat damage assignment](#combat-damage-assignment) — CR 510
- [Deathtouch + trample](#deathtouch--trample) — CR 702.2 / 702.19
- [Protection](#protection) — CR 702.16
- [Hexproof, shroud & ward](#hexproof-shroud--ward) — CR 702.11 / 702.18 / 702.21
- [ETB / LTB & look-back triggers](#etb--ltb--look-back-triggers) — CR 603.6 / 603.10
- [Mutate & merged permanents](#mutate--merged-permanents) — CR 702.140 / 730
- [Commander tax](#commander-tax) — CR 903.8
- [Sagas](#sagas) — CR 714
- [Classes](#classes) — CR 716
- [Phasing](#phasing) — CR 702.26
- [Double-faced cards & transform](#double-faced-cards--transform) — CR 712 / 701.27
- [The legend rule](#the-legend-rule) — CR 704.5j
- ["Can't" beats "can" (and impossible instructions)](#cant-beats-can-and-impossible-instructions) — CR 101.2 / 101.3
- [Ordering replacement effects (worked examples)](#ordering-replacement-effects-worked-examples) — CR 616
- [Commander damage](#commander-damage) — CR 903.10a / 704.6c
- [Partner & Backgrounds](#partner--backgrounds) — CR 702.124
- [When a player leaves a multiplayer game](#when-a-player-leaves-a-multiplayer-game) — CR 800.4
- [Open questions / next topics](#open-questions--next-topics)

## Layers & timestamps

**Summary:** Continuous effects are applied in seven layers (and sublayers for 1 and 7); within a layer, timestamp order decides unless a dependency exists.

> **CR 613.1** — The values of an object’s characteristics are determined by starting with the actual object. For a card, that means the values of the characteristics printed on that card. For a token or a copy of a spell or card, that means the values of the characteristics defined by the effect that created it. Then all applicable continuous effects are applied in a series of layers in the following order:
>
> **CR 613.1a** — Layer 1: Rules and effects that modify copiable values are applied.
>
> **CR 613.1b** — Layer 2: Control-changing effects are applied.
>
> **CR 613.1c** — Layer 3: Text-changing effects are applied. See rule 612, “Text-Changing Effects.”
>
> **CR 613.1d** — Layer 4: Type-changing effects are applied. These include effects that change an object’s card type, subtype, and/or supertype.
>
> **CR 613.1e** — Layer 5: Color-changing effects are applied.
>
> **CR 613.1f** — Layer 6: Ability-adding effects, keyword counters, ability-removing effects, and effects that say an object can’t have an ability are applied.
>
> **CR 613.1g** — Layer 7: Power- and/or toughness-changing effects are applied.
>
> **CR 613.4** — Within layer 7, apply effects in a series of sublayers in the order described below. Within each sublayer, apply effects in timestamp order. (See rule 613.7.) Note that dependency may alter the order in which effects are applied within a sublayer. (See rule 613.8.)
>
> **CR 613.4a** — Layer 7a: Effects from characteristic-defining abilities that define power and/or toughness are applied. See rule 604.3.
>
> **CR 613.4b** — Layer 7b: Effects that set power and/or toughness to a specific number or value are applied. Effects that refer to the base power and/or toughness of a creature apply in this layer.
>
> **CR 613.4c** — Layer 7c: Effects and counters that modify power and/or toughness (but don’t set power and/or toughness to a specific number or value) are applied.
>
> **CR 613.4d** — Layer 7d: Effects that switch a creature’s power and toughness are applied. Such effects take the value of power and apply it to the creature’s toughness, and take the value of toughness and apply it to the creature’s power.
>
> **CR 613.7** — Within a layer or sublayer, determining which order effects are applied in is usually done using a timestamp system. An effect with an earlier timestamp is applied before an effect with a later timestamp.

**Official rulings that apply these rules** (WotC, most-played cards first by EDHREC rank):

- [Graaz, Unstoppable Juggernaut](cards/G/gra.md#graaz-unstoppable-juggernaut) — *2023-02-04* — "If Graaz loses its abilities for some reason, then Juggernauts you control will not have to attack each combat and will be able to be blocked by Walls. However, due to how continuous effects are applied in layers, other creatures you control will continue to be 5/3 Juggernauts in addition to their other types. Unstoppable, indeed!"
- [Humility](cards/H/hu.md#humility) — *2009-10-01* — "This is the current interaction between Humility and Opalescence: The type-changing effect applies at layer 4, but the rest happens in the applicable layers. The rest of it will apply even if the permanent loses its ability before it's finished applying. So if Opalescence, Humility, and Worship are on the battlefield and Opalescence entered before Humility, the following is true: Layer 4: Humility and Worship each become creatures that are still enchantments. (Opalescence). Layer 6: Humility and Worship each lose their abilities. (Humility) Layer 7b: Humility becomes 4/4 and Worship becomes 4/4. (Opalescence). Humility becomes 1/1 and Worship becomes 1/1 (Humility). But if Humility entered before Opalescence, the following is true: Layer 4: Humility and Worship each become creatures that are still enchantments (Opalescence). Layer 6: Humility and Worship each lose their abilities (Humility). Layer 7b: Humility becomes 1/1 and Worship becomes 1/1 (Humility). Humility becomes 4/4 and Worship becomes 4/4 (Opalescence)."
- [Mistform Ultimus](cards/M/mis.md#mistform-ultimus) — *2006-09-25* — "Mistform Ultimus has all creature types even if an effect removes its ability. Type-changing static abilities will apply in layer 4 before effects such as Sudden Spoiling’s remove them in layer 6."
- [Two by Four](cards/T/tw.md#two-by-four) — *2024-11-08* — "The effect of a base power 4 counter or base toughness 4 counter overrides any existing effects that set that creature’s base power or toughness, as appropriate. Any existing effects or counters that raise, lower, or switch a creature’s power and/or toughness continue to apply to the creature’s new base power or toughness. Any base power- or toughness-setting effects that start to apply after the counter is placed on the creature will overwrite the counter’s effect. (For the rules-savvy, yes, this applies in layer 7b.)"

## Dependency

**Summary:** A dependency overrides timestamp order inside the same layer/sublayer. Official card rulings rarely use the word "dependency"; the rulings below are the ones in the bulk that settle classic dependency/layer cases (Humility + Opalescence; Blood Moon + Urborg). ⚠️ Any card pair not listed here should be worked through CR 613.8 directly.

> **CR 613.8** — Within a layer or sublayer, determining which order effects are applied in is sometimes done using a dependency system. If a dependency exists, it will override the timestamp system.
>
> **CR 613.8a** — An effect is said to “depend on” another if (a) it’s applied in the same layer (and, if applicable, sublayer) as the other effect; (b) applying the other would change the text or the existence of the first effect, what it applies to, or what it does to any of the things it applies to; and (c) neither effect is from a characteristic-defining ability or both effects are from characteristic-defining abilities. …
>
> **CR 613.8b** — An effect dependent on one or more other effects waits to apply until just after all of those effects have been applied. If multiple dependent effects would apply simultaneously in this way, they’re applied in timestamp order relative to each other. If several dependent effects form a dependency loop, then this rule is ignored and the effects in the dependency loop are applied in timestamp order.
>
> **CR 613.8c** — After each effect is applied, the order of remaining effects is reevaluated and may change if an effect that has not yet been applied becomes dependent on or independent of one or more other effects that have not yet been applied.

**Official rulings that apply these rules** (WotC, most-played cards first by EDHREC rank):

- [Humility](cards/H/hu.md#humility) — *2006-02-01* — "With a Humility and two Opalescences on the battlefield, if Humility has the latest timestamp, then all creatures are 1/1 with no abilities. If the timestamp order is Opalescence, Humility, Opalescence, the second Opalescence is 1/1, and the Humility and first Opalescence are 4/4. If Humility has the earliest timestamp, then everything is 4/4."

## Replacement effects vs. triggered abilities

**Summary:** A replacement effect modifies an event as it happens (often "instead") and never uses the stack; a triggered ability ("when/whenever/at") goes on the stack after the event. When several replacement effects apply, the affected object's controller (or the affected player) picks the order.

> **CR 614.1** — Some continuous effects are replacement effects. Like prevention effects (see rule 615), replacement effects apply continuously as events happen—they aren’t locked in ahead of time. Such effects watch for a particular event that would happen and completely or partially replace that event with a different event. They act like “shields” around whatever they’re affecting.
>
> **CR 614.1a** — Effects that use the word “instead” are replacement effects. Most replacement effects use the word “instead” to indicate what events will be replaced with other events.
>
> **CR 603.1** — Triggered abilities have a trigger condition and an effect. They are written as “[When/Whenever/At] [trigger condition or event], [effect]. [Instructions (if any).]”
>
> **CR 616.1** — If two or more replacement and/or prevention effects are attempting to modify the way an event affects an object or player, the affected object’s controller (or its owner if it has no controller) or the affected player chooses one to apply, following the steps listed below. If two or more players have to make these choices at the same time, choices are made in APNAP order (see rule 101.4).
>
> **CR 616.1e** — Any of the applicable replacement and/or prevention effects may be chosen.
>
> **CR 616.1f** — Once the chosen effect has been applied, this process is repeated (taking into account only replacement or prevention effects that would now be applicable) until there are no more left to apply.

**Official rulings that apply these rules** (WotC, most-played cards first by EDHREC rank):

- [Exotic Orchard](cards/E/ex.md#exotic-orchard) — *2009-02-01* — "When determining what colors of mana your opponents' lands could produce, Exotic Orchard takes into account any applicable replacement effects that would apply to those lands' mana abilities (such as Contamination's effect, for example). If there are more than one, consider them in any possible order."
- [Fellwar Stone](cards/F/fe.md#fellwar-stone) — *2009-10-01* — "When determining what colors of mana your opponents' lands could produce, take into account any applicable replacement effects that would apply to those lands' mana abilities (such as Contamination's effect, for example). If there is more than one, consider them in any possible order."
- [Garruk's Uprising](cards/G/ga.md#garruks-uprising) — *2024-11-08* — "If one or more static abilities that apply to a creature entering change its power, those abilities are considered when determining whether Garruk's Uprising's last ability triggers. The same is true for replacement effects that apply to it, such as entering with one or more +1/+1 counters or entering as a copy of another creature."
- [Doubling Season](cards/D/do.md#doubling-season) — *2024-11-08* — "Everything that is specified by the effect creating the original token or tokens will also be true about the additional token or tokens created by Doubling Season's replacement effect. For example, if an effect tells you to create a token "tapped and attacking," the additional tokens will also be tapped and attacking."
- [Rhythm of the Wild](cards/R/rh.md#rhythm-of-the-wild) — *2019-01-25* — "Riot is a replacement effect. Players can't respond to your choice of +1/+1 counter or haste, and they can't take actions while the creature is on the battlefield without one or the other."
- [Academy Manufactor](cards/A/ac.md#academy-manufactor) — *2021-06-18* — "Creating a Clue token this way isn't the same thing as investigating. Notably, an ability that triggers whenever you investigate won't trigger because you created a Clue token due to this replacement effect. If the original token creation was because you investigated once, those abilities will still each trigger once, no matter how many Clue tokens you end up creating."

## State-based actions

**Summary:** SBAs are checked whenever a player would get priority and all applicable ones happen simultaneously; they don't use the stack.

> **CR 704.3** — Whenever a player would get priority (see rule 117, “Timing and Priority”), the game checks for any of the listed conditions for state-based actions, then performs all applicable state-based actions simultaneously as a single event. If any state-based actions are performed as a result of a check, the check is repeated; otherwise all triggered abilities that are waiting to be put on the stack are put on the stack, …
>
> **CR 704.5a** — If a player has 0 or less life, that player loses the game.

**Official rulings that apply these rules** (WotC, most-played cards first by EDHREC rank):

- [Teferi's Protection](cards/T/te.md#teferis-protection) — *2017-08-25* — "Each Aura and Equipment you control attached to a permanent that isn't phasing out phases in attached to that permanent if it can still be attached to that permanent. If not, it phases in unattached. An Aura that phases in unattached will be put into its owner's graveyard as a state-based action. The same is true with Auras attached to players."
- [Sink into Stupor // Soporific Springs](cards/S/si.md#sink-into-stupor--soporific-springs) — *2024-06-07* — "If a copy of a spell is returned to its owner's hand, it's moved there, then it will cease to exist as a state-based action. It can't be recast."
- [Karn's Bastion](cards/K/ka.md#karns-bastion) — *2023-02-04* — "If a permanent ever has both +1/+1 counters and -1/-1 counters on it at the same time, they're removed in pairs as a state-based action so that the permanent has only one of those kinds of counters on it."
- [Animate Dead](cards/A/an.md#animate-dead) — *2016-06-08* — "If the creature put onto the battlefield has protection from black—or if the creature can't legally be enchanted by Animate Dead for another reason—Animate Dead won't be able to attach to it. It will be put into the graveyard as a state-based action, causing its delayed triggered ability to trigger. When the trigger resolves, if the creature's still on the battlefield, its controller will sacrifice it."
- [Phyrexian Metamorph](cards/P/ph.md#phyrexian-metamorph) — *2011-06-01* — "You can choose not to copy anything. In that case, Phyrexian Metamorph simply enters as a 0/0 artifact creature and is put into its owner's graveyard as a state-based action (unless something else is raising its toughness)."
- [Torment of Hailfire](cards/T/to.md#torment-of-hailfire) — *2017-07-14* — "State-based actions aren’t checked in between repetitions of this process, so the game state may be a little unusual while making the choice. For example, a player may sacrifice a creature and then later sacrifice an Aura that was attached to that creature."

## Copy effects

**Summary:** Copies take only copiable values (printed values as modified by other copy effects), not counters, Auras, or other effects.

> **CR 707.2** — When copying an object, the copy acquires the copiable values of the original object’s characteristics and, for an object on the stack, choices made when casting or activating it (mode, targets, the value of X, whether it was kicked, how it will affect multiple targets, and so on). The copiable values are the values derived from the text printed on the object (that text being name, mana cost, color indicator, card …
>
> **CR 707.2a** — A copy acquires the color of the object it’s copying because that value is derived from its mana cost or color indicator. A copy acquires the abilities of the object it’s copying because those values are derived from its rules text. A copy doesn’t wind up with two values of each ability (that is, it doesn’t copy the object’s abilities and its rules text, then have that rules text define a new set of abilities).
>
> **CR 707.2b** — Once an object has been copied, changing the copiable values of the original object won’t cause the copy to change.
>
> **CR 707.2c** — If a static ability generates a continuous effect that’s a copy effect, the copiable values that effect grants are determined only at the time that effect first starts to apply.

**Official rulings that apply these rules** (WotC, most-played cards first by EDHREC rank):

- [Scute Swarm](cards/S/sc.md#scute-swarm) — *2020-09-25* — "If Scute Swarm leaves the battlefield before its triggered ability resolves, the token will still enter the battlefield as a copy of Scute Swarm, using Scute Swarm's copiable values from when it was last on the battlefield."
- [Everflowing Chalice](cards/E/ev.md#everflowing-chalice) — *2024-11-08* — "If a card or token enters as a copy of a permanent, the new permanent isn't kicked, even if the original was."
- [Ragavan, Nimble Pilferer](cards/R/rag.md#ragavan-nimble-pilferer) — *2021-06-18* — "If a creature enters the battlefield as a copy of or becomes a copy of a creature whose dash cost was paid, the copy won't have haste and won't be returned to its owner's hand."
- [Reality Shift](cards/R/rea.md#reality-shift) — *2014-11-24* — "Any time you have priority, you may turn a manifested creature face up by revealing that it's a creature card (ignoring any copy effects or type-changing effects that might be applying to it) and paying its mana cost. This is a special action. It doesn't use the stack and can't be responded to."
- [Phyrexian Metamorph](cards/P/ph.md#phyrexian-metamorph) — *2011-06-01* — "If Phyrexian Metamorph somehow enters at the same time as another permanent (due to Mass Polymorph or Liliana Vess's third ability, for example), Phyrexian Metamorph can't become a copy of that permanent. You may choose only a permanent that's already on the battlefield."
- [Dawn's Truce](cards/D/da.md#dawns-truce) — *2024-07-26* — "If you copy a spell for which the gift was promised, the gift was also promised to the same opponent for the copy. If a card or token enters as a copy of a permanent that's already on the battlefield, the gift isn't promised for that new permanent, even if it was promised for the original."

## Commander: color identity

**Summary:** Color identity is mana symbols in the cost and rules text (plus color indicators/characteristic-defining abilities), including back faces; reminder text is ignored.

> **CR 903.4** — The Commander variant uses color identity to determine what cards can be in a deck with a certain commander. The color identity of a card is the color or colors of any mana symbols in that card’s mana cost or rules text, plus any colors defined by its characteristic-defining abilities (see rule 604.3) or color indicator (see rule 204).
>
> **CR 903.4a** — Color identity is established before the game begins. If a rule or effect refers to the color identity of an object in the game represented by a card, it uses the color identity established for that card as the game began.
>
> **CR 903.4b** — If a commander has a static ability that causes a player to choose its color before the game begins, that choice applies during deck construction and throughout the game, even as the commander changes zones. That choice affects the commander’s color identity. The player reveals that choice as they put their commander into the command zone before the game begins. See rules 103.2c and 607.2p.
>
> **CR 903.4c** — Reminder text is ignored when determining a card’s color identity. See rule 207.2.
>
> **CR 903.4d** — The back face of a double-faced card (see rule 712) is included when determining a card’s color identity. This is an exception to rule 712.8a.
>
> **CR 903.4e** — If a card has any alternative characteristics, such as those of adventurer cards (see rule 715, “Adventurer Cards”), those characteristics are included when determining the card’s color identity.
>
> **CR 903.4f** — If an ability refers to the colors or number of colors in a commander’s color identity, that quality is undefined if that player doesn’t have a commander. That part of the ability won’t do anything. Costs that refer to that quality are unpayable.

**Official rulings that apply these rules** (WotC, most-played cards first by EDHREC rank):

- [Command Tower](cards/C/com.md#command-tower) — *2020-11-10* — "If your commander is a card that has no colors in its color identity, Command Tower's ability produces no mana. It doesn't produce {C}."
- [Arcane Signet](cards/A/arc.md#arcane-signet) — *2020-11-10* — "If your commander is a card that has no colors in its color identity, Arcane Signet's ability produces no mana. It doesn't produce {C}."
- [Path of Ancestry](cards/P/pa.md#path-of-ancestry) — *2020-11-10* — "If your commander is a card that has no colors in its color identity, Path of Ancestry's ability produces no mana. It doesn't produce {C}."
- [Commander's Sphere](cards/C/com.md#commanders-sphere) — *2020-11-10* — "If your commander is a card that has no colors in its color identity, Commander's Sphere's first ability produces no mana. It doesn't produce {C}."
- [War Room](cards/W/war.md#war-room) — *2020-11-10* — "If your commander has no colors in its color identity, you pay no life to activate War Room's last ability."
- [Malakir Rebirth // Malakir Mire](cards/M/mal.md#malakir-rebirth--malakir-mire) — *2020-09-25* — "In the Commander variant, a double-faced card's color identity is determined by the mana costs and mana symbols in the rules text of both faces combined. If either face has a color indicator or basic land type, those are also considered."

## Commander: returning to the command zone

**Summary:** From graveyard or exile, the owner *may* move the commander to the command zone as a state-based action (so "dies"/"leaves" triggers still see it go to the graveyard first); from hand or library it's a replacement effect.

> **CR 903.9** — A commander may return to the command zone during a Commander game.
>
> **CR 903.9a** — If a commander is in a graveyard or in exile and that object was put into that zone since the last time state-based actions were checked, its owner may put it into the command zone. This is a state-based action. See rule 704.
>
> **CR 903.9b** — If a commander would be put into its owner’s hand or library from anywhere, its owner may put it into the command zone instead. This replacement effect may apply more than once to the same event. This is an exception to rule 614.5.
>
> **CR 903.9c** — If a commander is a melded permanent or a merged permanent and its owner chooses to put it into the command zone using the replacement effect described in rule 903.9b, that permanent and each component representing it that isn’t a commander are put into the appropriate zone, and the card that represents it and is a commander is put into the command zone.

**Official rulings that apply these rules** (WotC, most-played cards first by EDHREC rank):

- [Hellkite Courser](cards/H/he.md#hellkite-courser) — *2020-11-10* — "You'll return the commander to the command zone only if it's still on the battlefield as the delayed triggered ability resolves. If it's in another zone, it will stay where it is."
- [God-Eternal Oketra](cards/G/god.md#god-eternal-oketra) — *2019-05-03* — "If one of these Gods dies and it's your commander, you may put it into the command zone before its ability puts it into your library. If you save your commander this way, it won't put it into your library. The same is true if it would be exiled."
- [Gisela, the Broken Blade](cards/G/gi.md#gisela-the-broken-blade) — *2016-07-13* — "In a Commander game, your commander may be Bruna, the Fading Light or Gisela, the Broken Blade, and the other may be in your deck. If they meld into Brisela, Voice of Nightmares, Brisela will also be your commander; but if Brisela leaves the battlefield, only the card chosen as your commander at the start of the game may be put into the command zone."
- [Edgar Markov](cards/E/ed.md#edgar-markov) — *2025-01-24* — "Notably, if Edgar Markov is on the battlefield and its eminence ability triggers, but it’s put into the command zone before that ability resolves, that ability won’t do anything as it resolves. This is because an object that changes zones is considered a new object."
- [Tevesh Szat, Doom of Fools](cards/T/te.md#tevesh-szat-doom-of-fools) — *2020-11-10* — "If you leave the game, each commander you gained control of is returned to its previous controller's control. Each commander that entered the battlefield under your control is exiled (from there, its owner may return it to the command zone)."
- [Sauron, Lord of the Rings](cards/S/sau.md#sauron-lord-of-the-rings) — *2023-06-16* — "Sauron, Lord of the Rings's last ability will trigger even if the owner of the commander that died chooses to return it to the command zone after it dies."

## Worked layer examples (official CR examples)

**Summary:** Every example below is an **official Example paragraph from the CR**, printed under the rule it illustrates; they are the safest worked layer cases because Wizards wrote them.


**Official CR examples** (12):

- *CR 613.4d example* — A 1/3 creature is given +0/+1 by an effect. Then another effect switches the creature’s power and toughness. Its new power and toughness is 4/1. A new effect gives the creature +5/+0. Its “unswitched” power and toughness would be 6/4, so its actual power and toughness is 4/6.
- *CR 613.4d example* — A 1/3 creature is given +0/+1 by an effect. Then another effect switches the creature’s power and toughness. Its new power and toughness is 4/1. If the +0/+1 effect ends before the switch effect ends, the creature becomes 3/1.
- *CR 613.4d example* — A 1/3 creature is given +0/+1 by an effect. Then another effect switches the creature’s power and toughness. Then another effect switches its power and toughness again. The two switches essentially cancel each other, and the creature becomes 1/4.
- *CR 613.5 example* — Honor of the Pure is an enchantment that reads “White creatures you control get +1/+1.” Honor of the Pure and a 2/2 black creature are on the battlefield under your control. If an effect then turns the creature white (layer 5), it gets +1/+1 from Honor of the Pure (layer 7c), becoming 3/3. If the creature’s color is later changed to red (layer 5), Honor of the Pure’s effect stops applying to it, and it will return to being 2/2.
- *CR 613.5 example* — Gray Ogre, a 2/2 creature, is on the battlefield. An effect puts a +1/+1 counter on it (layer 7c), making it 3/3. A spell targeting it that says “Target creature gets +4/+4 until end of turn” resolves (layer 7c), making it 7/7. An enchantment that says “Creatures you control get +0/+2” enters the battlefield (layer 7c), making it 7/9. An effect that says “Target creature becomes 0/1 until end of turn” is applied to it (layer 7b), making it 5/8 (0/1, with +4/+4 from the resolved spell, +0/+2 from the enchantment, and +1/+1 from the counter).
- *CR 613.6 example* — An effect that reads “This creature gets +1/+1 and becomes the color of your choice until end of turn” is both a power- and toughness-changing effect and a color-changing effect. The “becomes the color of your choice” part is applied in layer 5, and then the “gets +1/+1” part is applied in layer 7c.
- *CR 613.6 example* — Act of Treason has an effect that reads “Gain control of target creature until end of turn. Untap that creature. It gains haste until end of turn.” This is both a control-changing effect and an effect that adds an ability to an object. The “gain control” part is applied in layer 2, and then the “it gains haste” part is applied in layer 6.
- *CR 613.6 example* — An effect that reads “All noncreature artifacts become 2/2 artifact creatures until end of turn” is both a type-changing effect and a power- and toughness-setting effect. The type-changing effect is applied to all noncreature artifacts in layer 4 and the power- and toughness-setting effect is applied to those same permanents in layer 7b, even though those permanents aren’t noncreature artifacts by then.
- *CR 613.6 example* — Svogthos, the Restless Tomb, is on the battlefield. An effect that says “Until end of turn, target land becomes a 3/3 creature that’s still a land” is applied to it (layers 4 and 7b). An effect that says “Target creature gets +1/+1 until end of turn” is applied to it (layer 7c), making it a 4/4 land creature. Then while you have ten creature cards in your graveyard, you activate Svogthos’s ability: “Until end of turn, this land becomes a black and green Plant Zombie creature with ‘This creature’s power and toughness are each equal to the number of creature cards in your graveyard.’ It’s still a land.” (layers 4, 5, and 7b). It becomes an 11/11 land creature. If a creature card enters or leaves your graveyard, Svogthos’s power and toughness will be modified accordingly. If the first effect is applied to it again, it will become a 4/4 land creature again.
- *CR 613.7a example* — Rune of Flight is an Aura that grants enchanted Equipment “Equipped creature has flying.” A player attaches Rune of Flight to Colossus Hammer, an Equipment with “Equipped creature gets +10/+10 and loses flying.” The ability granted by Rune of Flight shares Rune of Flight’s timestamp because it is later than Colossus Hammer’s timestamp. If Colossus Hammer becomes attached to a creature, both of its abilities receive new timestamps (see rule 613.7e), but the relative order of those timestamps remains the same.
- *CR 613.9 example* — Two effects are affecting the same creature: one from an Aura that says “Enchanted creature has flying” and one from an Aura that says “Enchanted creature loses flying.” Neither of these depends on the other, since nothing changes what they affect or what they’re doing to it. Applying them in timestamp order means the one that was generated last “wins.” The same process would be followed, and the same result reached, if either of the effects had a duration (such as “Target creature loses flying until end of turn”) or came from a non-Aura source (such as “All creatures lose flying”).
- *CR 613.9 example* — One effect reads, “White creatures get +1/+1,” and another reads, “Enchanted creature is white.” The enchanted creature gets +1/+1 from the first effect, regardless of its previous color.

**Official rulings that apply these rules** (WotC, most-played cards first by EDHREC rank):

- [Humility](cards/H/hu.md#humility) — *2009-10-01* — "This is the current interaction between Humility and Opalescence: The type-changing effect applies at layer 4, but the rest happens in the applicable layers. The rest of it will apply even if the permanent loses its ability before it's finished applying. So if Opalescence, Humility, and Worship are on the battlefield and Opalescence entered before Humility, the following is true: Layer 4: Humility and Worship each become creatures that are still enchantments. (Opalescence). Layer 6: Humility and Worship each lose their abilities. (Humility) Layer 7b: Humility becomes 4/4 and Worship becomes 4/4. (Opalescence). Humility becomes 1/1 and Worship becomes 1/1 (Humility). But if Humility entered before Opalescence, the following is true: Layer 4: Humility and Worship each become creatures that are still enchantments (Opalescence). Layer 6: Humility and Worship each lose their abilities (Humility). Layer 7b: Humility becomes 1/1 and Worship becomes 1/1 (Humility). Humility becomes 4/4 and Worship becomes 4/4 (Opalescence)."
- [Mistform Ultimus](cards/M/mis.md#mistform-ultimus) — *2006-09-25* — "Mistform Ultimus has all creature types even if an effect removes its ability. Type-changing static abilities will apply in layer 4 before effects such as Sudden Spoiling’s remove them in layer 6."
- [Two by Four](cards/T/tw.md#two-by-four) — *2024-11-08* — "The effect of a base power 4 counter or base toughness 4 counter overrides any existing effects that set that creature’s base power or toughness, as appropriate. Any existing effects or counters that raise, lower, or switch a creature’s power and/or toughness continue to apply to the creature’s new base power or toughness. Any base power- or toughness-setting effects that start to apply after the counter is placed on the creature will overwrite the counter’s effect. (For the rules-savvy, yes, this applies in layer 7b.)"

## Stack & priority

**Summary:** The active player gets priority first; a player who casts a spell or activates an ability gets priority again afterward (117.3c). The top object of the stack resolves only when all players pass in succession (117.4, 405.5). Some things don't use the stack (405.6). On resolution a spell or ability rechecks its targets; if all are illegal it doesn't resolve (608.2b).

> **CR 117.1a** — A player may cast an instant spell any time they have priority. A player may cast a noninstant spell during their main phase any time they have priority and the stack is empty.
>
> **CR 117.3a** — The active player receives priority at the beginning of most steps and phases, after any turn-based actions (such as drawing a card during the draw step; see rule 703) have been dealt with and abilities that trigger at the beginning of that phase or step have been put on the stack. No player receives priority during the untap step. Players usually don’t get priority during the cleanup step (see rule 514.3).
>
> **CR 117.3b** — The active player receives priority after a spell or ability (other than a mana ability) resolves.
>
> **CR 117.3c** — If a player has priority when they cast a spell, activate an ability, or take a special action, that player receives priority afterward.
>
> **CR 117.3d** — If a player has priority and chooses not to take any actions, that player passes. If any mana is in that player’s mana pool, they announce what mana is there. Then the next player in turn order receives priority.
>
> **CR 117.4** — If all players pass in succession (that is, if all players pass without taking any actions in between passing), the spell or ability on top of the stack resolves or, if the stack is empty, the phase or step ends.
>
> **CR 405.1** — When a spell is cast, the physical card is put on the stack (see rule 601.2a). When an ability is activated or triggers, it goes on top of the stack without any card associated with it (see rules 602.2a and 603.3).
>
> **CR 405.2** — The stack keeps track of the order that spells and/or abilities were added to it. Each time an object is put on the stack, it’s put on top of all objects already there.
>
> **CR 405.5** — When all players pass in succession, the top (last-added) spell or ability on the stack resolves. If the stack is empty when all players pass, the current step or phase ends and the next begins.
>
> **CR 405.6** — Some things that happen during the game don’t use the stack.
>
> **CR 608.2b** — If the spell or ability specifies targets, it checks whether the targets are still legal. A target that’s no longer in the zone it was in when it was targeted is illegal. Other changes to the game state may cause a target to no longer be legal; for example, its characteristics may have changed or an effect may have changed the text of the spell. If the source of an ability has left the zone it was in, its last known …

**Official rulings that apply these rules** (WotC, most-played cards first by EDHREC rank):

- [Sensei's Divining Top](cards/S/sen.md#senseis-divining-top) — *2016-06-08* — "Sensei's Divining Top's second ability may be activated in response to its first ability. If so, you'll draw a card, put Sensei's Divining Top on top of your library, and then look at the top three cards and rearrange them."
- [Sylvan Library](cards/S/sy.md#sylvan-library) — *2022-12-08* — "Any cards drawn prior to Sylvan Library’s ability resolving, including in your upkeep or in response to Sylvan Library’s triggered ability, can be chosen to be put back using this effect. Sylvan Library’s controller is responsible for keeping these cards distinguishable in hand, such as by keeping them separate from cards that began the turn in hand."
- [Ranger-Captain of Eos](cards/R/ran.md#ranger-captain-of-eos) — *2019-06-14* — "Your opponents may cast spells in response to the last ability of Ranger-Captain of Eos. The ability won’t affect those spells and it won’t affect spells that those players cast before you activated it. (In other words, the ability can’t be used to counter a spell.)"
- [Gyre Sage](cards/G/gy.md#gyre-sage) — *2013-04-15* — "When comparing the stats as the evolve ability resolves, it's possible that the stat that's greater changes from power to toughness or vice versa. If this happens, the ability will still resolve and you'll put a +1/+1 counter on the creature with evolve. For example, if you control a 2/2 creature with evolve and a 1/3 creature enters the battlefield under your control, it toughness is greater so evolve will trigger. In response, the 1/3 creature gets +2/-2. When the evolve trigger tries to resolve, its power is greater. You'll put a +1/+1 counter on the creature with evolve."
- [Mechanized Production](cards/M/me.md#mechanized-production) — *2017-02-09* — "If the enchanted artifact leaves the battlefield in response to Mechanized Production's triggered ability but Mechanized Production does not, Mechanized Production is put into its owner's graveyard as a state-based action with no enchanted artifact. The triggered ability creates no token, but you can still win the game if you control enough artifacts with the same name."
- [Twilight Prophet](cards/T/tw.md#twilight-prophet) — *2018-01-19* — "Some cards have triggered abilities with an intervening "if" clause that checks whether you have the city's blessing. These are worded "[Trigger condition], if you have the city's blessing, [effect]." You must already have the city's blessing in order for these abilities to trigger; otherwise they do nothing. In other words, there's no way to have the ability trigger if you don't have the city's blessing, even if you intend to get it in response to the triggered ability."

## Casting vs. copying a spell

**Summary:** A copy of a spell put onto the stack **isn't cast** (707.10), so "whenever you cast" triggers don't see it; it copies modes, targets, X and costs paid. An effect that says **cast a copy** follows casting steps 601.2a–h and the copy **is** cast (707.12).

> **CR 601.2** — To cast a spell is to take it from where it is (usually the hand), put it on the stack, and pay its costs, so that it will eventually resolve and have its effect. Casting a spell includes proposal of the spell (rules 601.2a–d) and determination and payment of costs (rules 601.2f–h). To cast a spell, a player follows the steps listed below, in order. A player must be legally allowed to cast the spell to begin this …
>
> **CR 601.2a** — To propose the casting of a spell, a player first moves that card (or that copy of a card) from where it is to the stack. It becomes the topmost object on the stack. It has all the characteristics of the card (or the copy of a card) associated with it, and that player becomes its controller. Any continuous effects that modify the characteristics of the spell as you start casting it begin as it is put on the stack …
>
> **CR 601.2f** — The player determines the total cost of the spell. Usually this is just the mana cost. Some spells have additional or alternative costs. Some effects may increase or reduce the cost to pay, or may provide other alternative costs. Costs may include paying mana, tapping permanents, sacrificing permanents, discarding cards, and so on. The total cost is the mana cost or alternative cost (as determined in rule 601.2b), …
>
> **CR 601.2h** — The player pays the total cost. First, they pay all costs that don’t involve random elements or moving objects from the library to a public zone, in any order. Then they pay all remaining costs in any order. Partial payments are not allowed. Unpayable costs can’t be paid.
>
> **CR 601.2i** — Once the steps described in 601.2a–h are completed, effects that modify the characteristics of the spell as it’s cast are applied, then the spell becomes cast. Any abilities that trigger when a spell is cast or put onto the stack trigger at this time. If the spell’s controller had priority before casting it, they get priority.
>
> **CR 707.10** — To copy a spell, activated ability, or triggered ability means to put a copy of it onto the stack; a copy of a spell isn’t cast and a copy of an activated ability isn’t activated. A copy of a spell or ability copies both the characteristics of the spell or ability and all decisions made for it, including modes, targets, the value of X, and additional or alternative costs. (See rule 601, “Casting Spells.”) Choices …
>
> **CR 707.10a** — If a copy of a spell is in a zone other than the stack, it ceases to exist. If a copy of a card is in any zone other than the stack or the battlefield, it ceases to exist. These are state-based actions. See rule 704.
>
> **CR 707.10c** — Some effects copy a spell or ability and state that its controller may choose new targets for the copy. The player may leave any number of the targets unchanged, even if those targets would be illegal. If the player chooses to change some or all of the targets, the new targets must be legal. Once the player has decided what the copy’s targets will be, the copy is put onto the stack with those targets.
>
> **CR 707.12** — An effect that instructs a player to cast a copy of an object (and not just copy a spell) follows the rules for casting spells, except that the copy is created in the same zone the object is in and then cast while another spell or ability is resolving. Casting a copy of an object follows steps 601.2a–h of rule 601, “Casting Spells,” and then the copy becomes cast. Once cast, the copy is a spell on the stack, and …

**Official CR examples** (3):

- *CR 707.10 example* — A player casts Fork, targeting an Emerald Charm. Fork reads, “Copy target instant or sorcery spell, except that the copy is red. You may choose new targets for the copy.” Emerald Charm is a modal green instant. When the Fork resolves, it puts a copy of the Emerald Charm on the stack except the copy is red, not green. The copy has the same mode that was chosen for the original Emerald Charm. It does not necessarily have the same target, but only because Fork allows choosing of new targets.
- *CR 707.10 example* — Fling is an instant that reads, “As an additional cost to cast this spell, sacrifice a creature” and “Fling deals damage equal to the sacrificed creature’s power to any target.” When determining how much damage a copy of Fling deals, it checks the power of the creature sacrificed to pay for the original Fling.
- *CR 707.10 example* — Dawnglow Infusion is a sorcery that reads, “You gain X life if {G} was spent to cast this spell and X life if {W} was spent to cast it.” Because mana isn’t an object, a copy of Dawnglow Infusion won’t cause you to gain any life, no matter what mana was spent to cast the original spell.

**Official rulings that apply these rules** (WotC, most-played cards first by EDHREC rank):

- [Sink into Stupor // Soporific Springs](cards/S/si.md#sink-into-stupor--soporific-springs) — *2024-06-07* — "If a copy of a spell is returned to its owner's hand, it's moved there, then it will cease to exist as a state-based action. It can't be recast."
- [Everflowing Chalice](cards/E/ev.md#everflowing-chalice) — *2024-11-08* — "If you copy a kicked spell on the stack, the copy is also kicked. If the copied spell is a permanent spell, the token the copy of that spell becomes when it enters is also kicked."
- [Flusterstorm](cards/F/fl.md#flusterstorm) — *2022-12-08* — "A copy of a spell can be countered like any other spell, but it must be countered individually. Countering a spell with storm won't affect the copies."
- [Sevinne's Reclamation](cards/S/sev.md#sevinnes-reclamation) — *2019-08-23* — "The copy that Sevinne's Reclamation creates is created on the stack, so it's not "cast." Abilities that trigger when a player casts a spell won't trigger. The copy wasn't cast from a graveyard, so it won't make another copy of itself."
- [The Meathook Massacre](cards/T/them.md#the-meathook-massacre) — *2021-09-24* — "If The Meathook Massacre enters the battlefield and it wasn't cast (or it was cast without paying its mana cost), X will be 0. The first ability will trigger, but it won't be much of a massacre."
- [Unbreakable Formation](cards/U/un.md#unbreakable-formation) — *2024-01-12* — "If an effect copies a spell with an addendum ability while it's on the stack, the copy wasn't cast at all, so you won't get the addendum bonus."

## Combat damage assignment

**Summary:** Each creature assigns combat damage equal to its power; a blocked creature divides damage among its blockers as its controller chooses (510.1c), and all combat damage is dealt simultaneously (510.2). First or double strike creates an extra combat damage step (510.4).

> **CR 510.1** — First, the active player announces how each attacking creature assigns its combat damage, then the defending player announces how each blocking creature assigns its combat damage. This turn-based action doesn’t use the stack. A player assigns a creature’s combat damage according to the following rules:
>
> **CR 510.1a** — Each attacking creature and each blocking creature assigns combat damage equal to its power. Creatures that would assign 0 or less damage this way don’t assign combat damage at all.
>
> **CR 510.1b** — An unblocked creature assigns its combat damage to the player, planeswalker, or battle it’s attacking. If it isn’t currently attacking anything (if, for example, it was attacking a planeswalker that has left the battlefield), it assigns no combat damage.
>
> **CR 510.1c** — A blocked creature assigns its combat damage to the creatures blocking it. If no creatures are currently blocking it (if, for example, they were destroyed or removed from combat), it assigns no combat damage. If exactly one creature is blocking it, it assigns all its combat damage to that creature. If two or more creatures are blocking it, it assigns its combat damage to those creatures divided as its controller …
>
> **CR 510.1d** — A blocking creature assigns combat damage to the creatures it’s blocking. If it isn’t currently blocking any creatures (if, for example, they were destroyed or removed from combat), it assigns no combat damage. If it’s blocking exactly one creature, it assigns all its combat damage to that creature. If it’s blocking two or more creatures, it assigns its combat damage divided as its controller chooses among them.
>
> **CR 510.1e** — Once a player has assigned combat damage from each attacking or blocking creature they control, the total damage assignment (not solely the damage assignment of any individual attacking or blocking creature) is checked to see if it complies with the above rules. If it doesn’t, the combat damage assignment is illegal; the game returns to the moment before that player began to assign combat damage. (See rule 733, …
>
> **CR 510.2** — Second, all combat damage that’s been assigned is dealt simultaneously. This turn-based action doesn’t use the stack. No player has the chance to cast spells or activate abilities between the time combat damage is assigned and the time it’s dealt.
>
> **CR 510.4** — If at least one attacking or blocking creature has first strike (see rule 702.7) or double strike (see rule 702.4) as the combat damage step begins, the only creatures that assign combat damage in that step are those with first strike or double strike. After that step, instead of proceeding to the end of combat step, the phase gets a second combat damage step. The only creatures that assign combat damage in that …
>
> **CR 702.7b** — If at least one attacking or blocking creature has first strike or double strike (see rule 702.4) as the combat damage step begins, the only creatures that assign combat damage in that step are those with first strike or double strike. After that step, instead of proceeding to the end of combat step, the phase gets a second combat damage step. The only creatures that assign combat damage in that step are the …

**Official CR examples** (1):

- *CR 510.1c example* — An attacking Elvish Regrower (a 4/3 creature) is blocked by Vampire Spawn (a 2/3 creature) and Helpful Hunter (a 1/1 creature). Elvish Regrower’s controller can assign all 4 damage to the Hunter, 1 damage to the Spawn and 3 damage to the Hunter, 2 damage to each creature, 3 damage to the Spawn and 1 damage to the Hunter, or all 4 damage to the Spawn.

**Official rulings that apply these rules** (WotC, most-played cards first by EDHREC rank):

- [Viscera Seer](cards/V/vi.md#viscera-seer) — *2010-08-15* — "If you sacrifice an attacking or blocking creature during the declare blockers step, it won't deal combat damage. If you wait until the combat damage step, but that creature is dealt lethal damage, it'll be destroyed before you get a chance to sacrifice it."
- [Sword of Feast and Famine](cards/S/sw.md#sword-of-feast-and-famine) — *2020-08-07* — "You can tap your lands for mana while the triggered ability is on the stack. However, you'll lose any mana you produce this way if you don't spend it before the end of the current combat damage step."
- [Maze of Ith](cards/M/maz.md#maze-of-ith) — *2022-12-08* — "You can activate Maze of Ith's ability targeting an attacking creature you control during the combat damage step or the end of combat step, even though it will already have dealt combat damage. This will untap the creature. The damage it dealt will be unaffected."
- [Thopter Spy Network](cards/T/tho.md#thopter-spy-network) — *2015-06-22* — "The last ability will trigger, at most, once per combat damage step per player. However, if at least one artifact creature you control has first strike and others don't, or if an artifact creature you control has double strike, the ability could trigger twice per combat: once in each combat damage step."
- [Invasion of Ikoria // Zilortha, Apex of Ikoria](cards/I/inv.md#invasion-of-ikoria--zilortha-apex-of-ikoria) — *2023-04-14* — "You decide whether to assign a non-Human creature’s combat damage as though it weren’t blocked just before it assigns that damage. You may make a different choice for each non-Human creature you control—that is, you may have none, some, or all of those creatures assign combat damage as though they weren’t blocked."
- [Drana, Liberator of Malakir](cards/D/dra.md#drana-liberator-of-malakir) — *2015-08-25* — "The +1/+1 counter won't change how much damage Drana or any other attacking creature with first strike or double strike deals during that combat damage step. However, the +1/+1 counters that are put on attacking creatures without first strike will affect the damage those creatures deal during the regular combat damage step."

## Deathtouch + trample

**Summary:** With deathtouch, any nonzero combat damage assigned to a creature counts as lethal for assigning excess (702.2c), so a deathtouch + trample attacker needs to assign only 1 damage to each blocker and can assign the rest to the player, planeswalker or battle (702.19b).

> **CR 702.2b** — A creature with toughness greater than 0 that’s been dealt damage by a source with deathtouch since the last time state-based actions were checked is destroyed as a state-based action. See rule 704.
>
> **CR 702.2c** — Any nonzero amount of combat damage assigned to a creature by a source with deathtouch is considered to be lethal damage for the purposes of determining if excess damage is being dealt.
>
> **CR 702.19b** — The controller of an attacking creature with trample first assigns damage to the creature(s) blocking it. Once all those blocking creatures are assigned lethal damage, any excess damage is assigned as its controller chooses among those blocking creatures and the player, planeswalker, or battle the creature is attacking. When checking for assigned lethal damage, take into account damage already marked on the creature …
>
> **CR 702.19c** — Trample over planeswalkers is a variant of trample that modifies the rules for assigning combat damage to planeswalkers. The controller of a creature with trample over planeswalkers assigns that creature’s combat damage as described in rule 702.19b, with one exception. If that creature is attacking a planeswalker, after lethal damage is assigned to all blocking creatures and damage at least equal to the loyalty of …

**Official CR examples** (3):

- *CR 702.19b example* — A 2/2 creature that can block an additional creature blocks two attackers: a 1/1 with no abilities and a 3/3 with trample. The active player could assign 1 damage from the first attacker and 1 damage from the second to the blocking creature, and 2 damage to the defending player from the creature with trample.
- *CR 702.19b example* — A 6/6 green creature with trample is blocked by a 2/2 creature with protection from green. The attacking creature’s controller must assign at least 2 damage to the blocker, even though that damage will be prevented by the blocker’s protection ability. The attacking creature’s controller can divide the rest of the damage as they choose between the blocking creature and the defending player.
- *CR 702.19c example* — A player controls a planeswalker with three loyalty counters that is being attacked by a 1/1 with no abilities and a 7/7 with trample over planeswalkers. The active player could assign 1 damage from the first attacker and 2 damage from the second to the planeswalker and 5 damage to the defending player from the creature with trample over planeswalkers.

**Official rulings that apply these rules** (WotC, most-played cards first by EDHREC rank):

- [Aveline de Grandpré](cards/A/av.md#aveline-de-grandpré) — *2024-07-05* — "If a creature you control with deathtouch deals combat damage to a player at the same time it’s dealt lethal damage (perhaps because it has trample and was blocked), it will die before Aveline’s triggered ability resolves and puts +1/+1 counters on it."

## Protection

**Summary:** Protection from a quality means: can't be targeted by spells/abilities with that quality, enchanted or equipped by such Auras/Equipment, blocked by such creatures (when attacking), and damage from such sources is prevented (702.16b–f).

> **CR 702.16a** — Protection is a static ability, written “Protection from [quality].” This quality is usually a color (as in “protection from black”) but can be any characteristic value or information. If the quality happens to be a card name, it is treated as such only if the protection ability specifies that the quality is a name. If the quality is a card type, subtype, or supertype, the ability applies to sources that are …
>
> **CR 702.16b** — A permanent or player with protection can’t be targeted by spells with the stated quality and can’t be targeted by abilities from a source with the stated quality.
>
> **CR 702.16c** — A permanent or player with protection can’t be enchanted by Auras that have the stated quality. Such Auras attached to the permanent or player with protection will be put into their owners’ graveyards as a state-based action. (See rule 704, “State-Based Actions.”)
>
> **CR 702.16d** — A permanent with protection can’t be equipped by Equipment that have the stated quality or fortified by Fortifications that have the stated quality. Such Equipment or Fortifications become unattached from that permanent as a state-based action, but remain on the battlefield. (See rule 704, “State-Based Actions.”)
>
> **CR 702.16e** — Any damage that would be dealt by sources that have the stated quality to a permanent or player with protection is prevented.
>
> **CR 702.16f** — Attacking creatures with protection can’t be blocked by creatures that have the stated quality.
>
> **CR 702.16j** — “Protection from everything” is a variant of the protection ability. A permanent or player with protection from everything has protection from each object regardless of that object’s characteristic values. Such a permanent or player can’t be targeted by spells or abilities and can’t be enchanted by Auras. Such a permanent can’t be equipped by Equipment, fortified by Fortifications, or blocked by creatures. All …
>
> **CR 702.16k** — “Protection from [a player]” is a variant of the protection ability. A permanent or player with protection from a specific player has protection from each object that player controls and protection from each object that player owns not controlled by another player, regardless of that object’s characteristic values. Such a permanent or player can’t be targeted by spells or abilities the specified player controls and …

**Official rulings that apply these rules** (WotC, most-played cards first by EDHREC rank):

- [Cyclonic Rift](cards/C/cy.md#cyclonic-rift) — *2024-01-12* — "Because a spell with overload doesn't target when its overload cost is paid, it may affect permanents with hexproof or with protection from the appropriate color."
- [The One Ring](cards/T/theo.md#the-one-ring) — *2023-06-16* — "Nothing other than the specified events are prevented or illegal. An effect that doesn't target you could still cause you to discard cards, for example. Creatures can still attack you while you have protection from everything, although combat damage that they would deal to you will be prevented."
- [Teferi's Protection](cards/T/te.md#teferis-protection) — *2017-08-25* — "Gaining protection from everything causes a spell or ability on the stack to have an illegal target if it targets you. As a spell or ability tries to resolve, if all its targets are illegal, that spell or ability doesn't resolve and none of its effects happen, including effects unrelated to the target. If at least one target is still legal, the spell or ability does as much as it can to the remaining legal targets, and its other effects still happen."
- [Akroma's Will](cards/A/ak.md#akromas-will) — *2025-11-17* — ""Protection from each color" is shorthand for protection from white, from blue, from black, from red, and from green. Colorless is not a color."
- [Animate Dead](cards/A/an.md#animate-dead) — *2016-06-08* — "If the creature put onto the battlefield has protection from black—or if the creature can't legally be enchanted by Animate Dead for another reason—Animate Dead won't be able to attach to it. It will be put into the graveyard as a state-based action, causing its delayed triggered ability to trigger. When the trigger resolves, if the creature's still on the battlefield, its controller will sacrifice it."
- [Chandra's Ignition](cards/C/cha.md#chandras-ignition) — *2015-06-22* — "The creature is the source of the damage, not Chandra's Ignition. For example, Chandra's Ignition can have a white creature deal damage to a creature with protection from red."

## Hexproof, shroud & ward

**Summary:** Hexproof stops targeting by spells/abilities **opponents** control (702.11b); shroud stops targeting by **any** player (702.18a); ward is a **triggered ability** that counters an opponent's spell or ability targeting the permanent unless they pay the cost (702.21a) — so it uses the stack and can be responded to.

> **CR 702.11b** — “Hexproof” on a permanent means “This permanent can’t be the target of spells or abilities your opponents control.”
>
> **CR 702.11c** — “Hexproof” on a player means “You can’t be the target of spells or abilities your opponents control.”
>
> **CR 702.11d** — “Hexproof from [quality]” is a variant of the hexproof ability. “Hexproof from [quality]” on a permanent means “This permanent can’t be the target of [quality] spells your opponents control or abilities your opponents control from [quality] sources.” A “hexproof from [quality]” ability is a hexproof ability.
>
> **CR 702.11e** — Any effect that causes an object to lose hexproof will cause an object to lose all “hexproof from [quality]” abilities. Any effect that allows a player to choose a creature with hexproof as a target as though it didn’t have hexproof will allow a player to choose a creature with a “hexproof from [quality]” ability. Any effect that looks for a card with hexproof will find a card with a “hexproof from [quality]” …
>
> **CR 702.18a** — Shroud is a static ability. “Shroud” means “This permanent or player can’t be the target of spells or abilities.”
>
> **CR 702.21a** — Ward is a triggered ability. Ward [cost] means “Whenever this permanent becomes the target of a spell or ability an opponent controls, counter that spell or ability unless that player pays [cost].”
>
> **CR 702.21b** — Some ward abilities include an X in their cost and state what X is equal to. This value is determined at the time the ability resolves, not locked in as the ability triggers.

**Official rulings that apply these rules** (WotC, most-played cards first by EDHREC rank):

- [Heroic Intervention](cards/H/he.md#heroic-intervention) — *2020-06-23* — "The set of permanents affected by Heroic Intervention is determined as the spell resolves. Permanents you begin to control later in the turn won't gain hexproof and indestructible."
- [Cyclonic Rift](cards/C/cy.md#cyclonic-rift) — *2024-01-12* — "Because a spell with overload doesn't target when its overload cost is paid, it may affect permanents with hexproof or with protection from the appropriate color."
- [Animate Dead](cards/A/an.md#animate-dead) — *2016-06-08* — "Abilities such as shroud and protection function only on the battlefield unless otherwise specified. A creature card with shroud may be targeted by Animate Dead, and Animate Dead will become attached to the creature that enters the battlefield."
- [The Ozolith](cards/T/theo.md#the-ozolith) — *2020-04-17* — "+1/+1 counters on The Ozolith have no effect unless it becomes a creature. Keyword counters on The Ozolith will grant it keywords that may have no practical effect. For example, flying on a noncreature artifact is just strange, but hexproof on a noncreature artifact is entirely useful."
- [Shadowspear](cards/S/sha.md#shadowspear) — *2020-01-24* — "If a permanent enters the battlefield under an opponent's control with hexproof or indestructible after Shadowspear's second ability resolves, it won't lose that ability unless you activate Shadowspear's second ability again. The same is true if an opponent's permanent gains indestructible or hexproof after Shadowspear's second ability resolves."
- [Grave Pact](cards/G/gra.md#grave-pact) — *2023-09-01* — "None of the players are targeted. A player with hexproof would still sacrifice a creature."

## ETB / LTB & look-back triggers

**Summary:** Enters-the-battlefield triggers check the battlefield after the event, including the newcomers (603.6a). Leaves-the-battlefield triggers "look back in time" (603.10a), so they see the game as it was just before the permanent left. "Enters with …" / "enters tapped" text is a static ability, not a triggered ability; its effect happens as part of the event (603.6d).

> **CR 603.2** — Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.
>
> **CR 603.6a** — Enters-the-battlefield abilities trigger when a permanent enters the battlefield. These are written, “When [this object] enters, . . . “ or “Whenever a [type] enters, . . .” Each time an event puts one or more permanents onto the battlefield, all permanents on the battlefield (including the newcomers) are checked for any enters-the-battlefield triggers that match the event.
>
> **CR 603.6c** — Leaves-the-battlefield abilities trigger when a permanent moves from the battlefield to another zone, or when a phased-in permanent leaves the game because its owner leaves the game. These are written as, but aren’t limited to, “When [this object] leaves the battlefield, . . .” or “Whenever [something] is put into a graveyard from the battlefield, . . . .” (See also rule 603.10.) An ability that attempts to do …
>
> **CR 603.6d** — Some permanents have text that reads “[This permanent] enters with . . . ,” “As [this permanent] enters . . . ,” “[This permanent] enters as . . . ,” or “[This permanent] enters tapped.” Such text is a static ability—not a triggered ability—whose effect occurs as part of the event that puts the permanent onto the battlefield.
>
> **CR 603.10** — Normally, objects that exist immediately after an event are checked to see if the event matched any trigger conditions, and continuous effects that exist at that time are used to determine what the trigger conditions are and what the objects involved in the event look like. However, some triggered abilities are exceptions to this rule; the game “looks back in time” to determine if those abilities trigger, using the …
>
> **CR 603.10a** — Some zone-change triggers look back in time. These are leaves-the-battlefield abilities, abilities that trigger when a player sacrifices a permanent, abilities that trigger when a card leaves a graveyard, and abilities that trigger when an object that all players can see is put into a hand or library.

**Official CR examples** (1):

- *CR 603.10a example* — Two creatures are on the battlefield along with an artifact that has the ability “Whenever a creature dies, you gain 1 life.” Someone casts a spell that destroys all artifacts, creatures, and enchantments. The artifact’s ability triggers twice, even though the artifact goes to its owner’s graveyard at the same time as the creatures.

**Official rulings that apply these rules** (WotC, most-played cards first by EDHREC rank):

- [Teferi's Protection](cards/T/te.md#teferis-protection) — *2017-08-25* — "Any one-shot effects that are waiting "until [this] leaves the battlefield," such as that of Banishing Light, won't happen when a permanent phases out."
- [Austere Command](cards/A/au.md#austere-command) — *2020-11-10* — "If a card is exiled "until" another permanent leaves the battlefield, the exiled card returns to the battlefield immediately after that permanent leaves the battlefield during Austere Command's resolution, and it may be destroyed by a later mode."
- [Rhythm of the Wild](cards/R/rh.md#rhythm-of-the-wild) — *2019-05-03* — "If Rhythm of the Wild leaves the battlefield at the same time that a nontoken creature enters the battlefield (most likely because that creature has a replacement effect, such as that of Rescuer Sphinx), that creature still gets a +1/+1 counter or haste."
- [Sensei's Divining Top](cards/S/sen.md#senseis-divining-top) — *2016-06-08* — "If Sensei's Divining Top leaves the battlefield while its second ability is on the stack, you'll draw a card and leave Sensei's Divining Top in the zone it's moved to."
- [Scute Swarm](cards/S/sc.md#scute-swarm) — *2020-09-25* — "If Scute Swarm leaves the battlefield before its triggered ability resolves, the token will still enter the battlefield as a copy of Scute Swarm, using Scute Swarm's copiable values from when it was last on the battlefield."
- [Reality Shift](cards/R/rea.md#reality-shift) — *2014-11-24* — "If a face-down permanent you control leaves the battlefield, you must reveal it. You must also reveal all face-down spells and permanents you control if you leave the game or if the game ends."

## Mutate & merged permanents

**Summary:** A mutating creature spell with a legal target doesn't enter the battlefield; it merges with the target (702.140c). The merged permanent is the **same object** it was before — it hasn't just come under your control and existing effects keep applying (730.2c) — and uses the characteristics of its topmost component (730.2a) plus all abilities of every component (702.140e).

> **CR 702.140a** — Mutate appears on some creature cards. It represents a static ability that functions while the spell with mutate is on the stack. “Mutate [cost]” means “You may pay [cost] rather than pay this spell’s mana cost. If you do, it becomes a mutating creature spell and targets a non-Human creature with the same owner as this spell.” Casting a spell using its mutate ability follows the rules for paying alternative costs …
>
> **CR 702.140b** — As a mutating creature spell begins resolving, if its target is illegal, it ceases to be a mutating creature spell and continues resolving as a creature spell and will be put onto the battlefield under the control of the spell’s controller.
>
> **CR 702.140c** — As a mutating creature spell resolves, if its target is legal, it doesn’t enter the battlefield. Rather, it merges with the target creature and becomes one object represented by more than one card or token (see rule 730, “Merging with Permanents”). The spell’s controller chooses whether the spell is put on top of the creature or on the bottom. The resulting permanent is a mutated permanent.
>
> **CR 702.140d** — An ability that triggers whenever a creature mutates triggers when a spell merges with a creature as a result of a resolving mutating creature spell.
>
> **CR 702.140e** — A mutated permanent has all abilities of each card and token that represents it. Its other characteristics are derived from the topmost card or token.
>
> **CR 730.2** — To merge an object with a permanent, place that object on top of or under that permanent. That permanent becomes a merged permanent represented by the card or copy that represented that object in addition to any other components that were representing it.
>
> **CR 730.2a** — A merged permanent has only the characteristics of its topmost component, unless otherwise specified by the effect that caused them to merge. This is a copiable effect whose timestamp is the time the objects merged. (See rule 613.2.)
>
> **CR 730.2b** — As an object merges with a permanent, that object leaves its previous zone and becomes part of an object on the battlefield, but the resulting permanent isn’t considered to have just entered the battlefield.
>
> **CR 730.2c** — Because a merged permanent is the same object that it was before, it hasn’t just come under a player’s control, any continuous effects that affected it continue to do so, and so on.
>
> **CR 730.3** — If a merged permanent leaves the battlefield, one permanent leaves the battlefield and each of the individual components are put into the appropriate zone.

**Official rulings that apply these rules** (WotC, most-played cards first by EDHREC rank):

- [Luminous Broodmoth](cards/L/lu.md#luminous-broodmoth) — *2020-04-17* — "If a merged creature dies and that creature didn't have flying, each card that was part of that merged creature is returned to the battlefield. Each one has a flying counter on it."
- [Lithoform Engine](cards/L/li.md#lithoform-engine) — *2020-09-25* — "Lithoform Engine can copy any spell or ability on the stack, not just one with targets. If a permanent spell is copied, new targets can't be chosen for it, if it has any (perhaps because it's an Aura or a mutating creature spell)."
- [Duplicant](cards/D/du.md#duplicant) — *2020-08-07* — "If a melded permanent or a merged permanent is exiled by Duplicant's triggered ability, that ability's controller chooses the relative timestamp of the exiled cards. Duplicant looks at the information of the one with the latest timestamp."
- [Vivien, Monsters' Advocate](cards/V/vi.md#vivien-monsters-advocate) — *2020-04-17* — "If you cast a mutating creature spell, you must choose a target for it before the triggered ability from Vivien's last ability puts a creature onto the battlefield. The creature you find can't be the target of the mutating creature spell."
- [Paradoxical Outcome](cards/P/pa.md#paradoxical-outcome) — *2021-03-19* — "If a melded or merged permanent is returned to your hand this way, you'll draw a card for each of its components that are cards."
- [Death's Oasis](cards/D/dea.md#deaths-oasis) — *2020-04-17* — "Use the mana value of the creature as it last existed on the battlefield and the mana value of the creature card as it exists in your graveyard to determine which cards may be returned to your hand. This may result in a creature's death bringing itself back to your hand; perhaps it was one card of a merged creature, or it had become a copy of a more expensive creature."

## Commander tax

**Summary:** Casting your commander from the command zone costs {2} more for each previous time **you** cast it from the command zone this game (903.8); casts from anywhere else don't count.

> **CR 903.8** — A player may cast a commander they own from the command zone. A commander cast from the command zone costs an additional {2} for each previous time the player casting it has cast it from the command zone that game. This additional cost is informally known as the “commander tax.”

**Official rulings that apply these rules** (WotC, most-played cards first by EDHREC rank):

- [Command Beacon](cards/C/com.md#command-beacon) — *2015-11-04* — "If you cast a commander from your hand, the additional cost based on the number of times you've cast it from your command zone (sometimes referred to as the "commander tax") doesn't apply. Additionally, that casting won't add to the tax if you later cast the commander from the command zone."
- [Opal Palace](cards/O/op.md#opal-palace) — *2020-11-10* — "If Opal Palace's last ability produces two mana (most likely due to Mana Reflection) and you spend them to cast a commander, that commander enters with two counters for each time it's been cast from the command zone this game."
- [Hellkite Courser](cards/H/he.md#hellkite-courser) — *2020-11-10* — "Putting your commander onto the battlefield this way isn't the same as casting that commander. The "commander tax" won't increase."
- [Yuriko, the Tiger's Shadow](cards/Y/yu.md#yuriko-the-tigers-shadow) — *2020-11-10* — "Activating Yuriko's commander ninjutsu ability isn't the same as casting Yuriko as a spell. You won't have to pay the commander tax to activate that ability, and activating that ability won't increase the commander tax to pay later."
- [Rakdos, Lord of Riots](cards/R/rak.md#rakdos-lord-of-riots) — *2020-11-10* — "If there are additional costs to cast a creature spell, such as a kicker cost or the commander tax, apply those increases before applying cost reductions."
- [Derevi, Empyrial Tactician](cards/D/der.md#derevi-empyrial-tactician) — *2020-11-10* — "When you activate Derevi's last ability, you're not casting Derevi as a spell. The ability can't be countered by something that counters only spells. The ability isn't subject to the commander tax, nor does it increase the tax if you cast Derevi from the command zone later in the game."

## Sagas

**Summary:** A Saga enters with a lore counter (714.3a). As your precombat main phase begins you add another lore counter as a turn-based action that doesn't use the stack (714.3c). Each chapter is a **triggered ability** that triggers when the count reaches its number (714.2b). Once the counters are at least the final chapter number and no chapter ability from it is still on the stack, the Saga is sacrificed as a state-based action (714.4).

> **CR 714.2** — A chapter symbol is a keyword ability that represents a triggered ability referred to as a chapter ability.
>
> **CR 714.2b** — “{rN}—[Effect]” means “When one or more lore counters are put onto this Saga, if the number of lore counters on it was less than N and became at least N, [effect].”
>
> **CR 714.2d** — A Saga’s final chapter number is the greatest value among chapter abilities it has. If a Saga somehow has no chapter abilities, its final chapter number is 0.
>
> **CR 714.3a** — Each Saga without read ahead has the intrinsic ability “This Saga enters with a lore counter on it.” This ability creates a replacement effect (see rule 614.1c).
>
> **CR 714.3c** — As a player’s precombat main phase begins, that player puts a lore counter on each Saga they control with one or more chapter abilities. This turn-based action doesn’t use the stack.
>
> **CR 714.4** — If the number of lore counters on a Saga permanent with one or more chapter abilities is greater than or equal to its final chapter number, and it isn’t the source of a chapter ability that has triggered but not yet left the stack, that Saga’s controller sacrifices it. This state-based action doesn’t use the stack.

**Official rulings that apply these rules** (WotC, most-played cards first by EDHREC rank):

- [Urza's Saga](cards/U/ur.md#urzas-saga) — *2021-06-18* — "Even though Urza's Saga is a land, it is also still a Saga, and it will be sacrificed after its last chapter ability resolves."
- [Summon: Bahamut](cards/S/sum.md#summon-bahamut) — *2025-06-06* — "Once a chapter ability has triggered, the ability on the stack won't be affected if the Saga gains or loses counters, or if it leaves the battlefield."
- [Binding the Old Gods](cards/B/bi.md#binding-the-old-gods) — *2021-02-05* — "Each symbol on the left of a Saga's text box represents a chapter ability. A chapter ability is a triggered ability that triggers when a lore counter that is put on the Saga causes the number of lore counters on the Saga to become equal to or greater than the ability's chapter number. Chapter abilities are put onto the stack and may be responded to."
- [Summon: Titan](cards/S/sum.md#summon-titan) — *2025-06-06* — "Once the number of lore counters on a Saga is greater than or equal to the greatest number among its chapter abilities, the Saga's controller sacrifices it as soon as its chapter ability has left the stack, most likely by resolving or being countered. This state-based action doesn't use the stack."
- [The Eldest Reborn](cards/T/thee.md#the-eldest-reborn) — *2018-04-27* — "A chapter ability doesn't trigger if a lore counter is put on a Saga that already had a number of lore counters greater than or equal to that chapter's number. For example, the third lore counter put on a Saga causes the III chapter ability to trigger, but I and II won't trigger again."
- [Summon: Primal Odin](cards/S/sum.md#summon-primal-odin) — *2025-06-06* — "As a Saga enters, its controller puts a lore counter on it. As your first main phase begins (immediately after your draw step), you put another lore counter on each Saga you control. Putting a lore counter on a Saga in either of these ways doesn't use the stack."

## Classes

**Summary:** Gaining a Class level is an **activated ability, sorcery speed only**, and you can level only from N-1 to N, so you can't skip levels (716.2a). Abilities from earlier levels stay. A level is not a copiable value (716.2b). Class levels are not level counters (716.4).

> **CR 716.1** — Each Class card has a striated text box containing two class level bars. Its illustration is vertically oriented on the left side of the card, and its type line is along the bottom of the card.
>
> **CR 716.2** — A class level bar is a keyword ability that represents both an activated ability and a static ability. A class level bar includes the activation cost of its activated ability and a level number. Any abilities printed within the same text box section as the class level bar are part of its static ability.
>
> **CR 716.2a** — “[Cost]: Level N — [Abilities]” means “[Cost]: This Class’s level becomes N. Activate only if this Class is level N-1 and only as a sorcery” and “As long as this Class is level N or greater, it has [abilities].”
>
> **CR 716.2b** — A level is a designation that any permanent can have. A Class retains its level even if it stops being a Class. Levels are not a copiable characteristic.
>
> **CR 716.2d** — If a rule or effect refers to a permanent’s level and that permanent doesn’t have a level, it is treated as though its level is 1.
>
> **CR 716.3** — Any ability printed on a Class card that isn’t preceded by a class level bar is treated normally. In particular, the Class has the ability printed in its top text box section at all times. That ability may affect the game if it’s a static ability, it may trigger if it’s a triggered ability, and it can be activated if it’s an activated ability.
>
> **CR 716.4** — Some older creature cards, called leveler cards, have level up abilities that add level counters to them. These are not the same as class level abilities. Level counters do not interact with Class cards, and class levels do not interact with leveler cards. See rule 702.87, “Level Up,” and rule 711, “Leveler Cards.”

**Official rulings that apply these rules** (WotC, most-played cards first by EDHREC rank):

- [Caretaker's Talent](cards/C/car.md#caretakers-talent) — *2024-07-26* — "You can't activate the first level ability of a Class unless that Class is level 1. Similarly, you can't activate the second level ability of a Class unless that Class is level 2."
- [Wizard Class](cards/W/wi.md#wizard-class) — *2021-07-23* — "Each Class starts with only the first of three class abilities. As the first level ability resolves, the Class becomes level 2 and gains the second class ability. As the second level ability resolves, the Class becomes level 3 and gains the third class ability."
- [Barbarian Class](cards/B/bar.md#barbarian-class) — *2021-07-23* — "Each Class has five abilities. The three in the major sections of its text box are class abilities. Class abilities can be static, activated, or triggered abilities. The other two are level abilities, one activated ability to advance the Class to level 2 and another to advance the Class to level 3."
- [Cool but Rude](cards/C/coo.md#cool-but-rude) — *2026-01-27* — "Class cards have multiple text box sections. Other than the top section, each section contains a class level bar that includes a cost and a level number. Each represents an activated ability with the listed cost that advances the Class to the level listed in that bar."

## Phasing

**Summary:** A phased-out permanent is treated as though it doesn't exist and is removed from combat (702.26b). It **doesn't change zones**, so no enter/leave triggers fire and its counters stay (702.26d). Attached Auras and Equipment phase out with it (702.26g). It phases back in during its controller's next untap step (702.26a).

> **CR 702.26a** — Phasing is a static ability that modifies the rules of the untap step. During each player’s untap step, before the active player untaps permanents, all phased-in permanents with phasing that player controls “phase out.” Simultaneously, all phased-out permanents that had phased out under that player’s control “phase in.”
>
> **CR 702.26b** — If a permanent phases out, its status changes to “phased out.” Except for rules and effects that specifically mention phased-out permanents, a phased-out permanent is treated as though it does not exist. It can’t affect or be affected by anything else in the game. A permanent that phases out is removed from combat. (See rule 506.4.)
>
> **CR 702.26d** — The phasing event doesn’t actually cause a permanent to change zones or control, even though it’s treated as though it’s not on the battlefield and not under its controller’s control while it’s phased out. Zone-change triggers don’t trigger when a permanent phases in or out. Tokens continue to exist on the battlefield while phased out. Counters and stickers remain on a permanent while it’s phased out. Effects that …
>
> **CR 702.26g** — When a permanent phases out, any Auras, Equipment, or Fortifications attached to that permanent phase out at the same time. This alternate way of phasing out is known as phasing out “indirectly.” An Aura, Equipment, or Fortification that phased out indirectly won’t phase in by itself, but instead phases in along with the permanent it’s attached to.
>
> **CR 702.26k** — Phased-out permanents owned by a player who leaves the game also leave the game. This doesn’t cause zone-change abilities to trigger. See rule 800.4.
>
> **CR 702.26m** — If an effect causes a player to skip their untap step, the phasing event simply doesn’t occur that turn.

**Official CR examples** (2):

- *CR 702.26b example* — You control three creatures, one of which is phased out. You cast a spell that says “Draw a card for each creature you control.” You draw two cards.
- *CR 702.26b example* — You control a phased-out creature. You cast a spell that says “Destroy all creatures.” The phased-out creature is not destroyed.

**Official rulings that apply these rules** (WotC, most-played cards first by EDHREC rank):

- [Teferi's Protection](cards/T/te.md#teferis-protection) — *2017-08-25* — "Any one-shot effects that are waiting "until [this] leaves the battlefield," such as that of Banishing Light, won't happen when a permanent phases out."
- [Clever Concealment](cards/C/cl.md#clever-concealment) — *2023-02-04* — "An attacking or blocking creature that phases out is removed from combat."
- [Talon Gates of Madara](cards/T/ta.md#talon-gates-of-madara) — *2024-06-07* — "Phasing out doesn't cause any "leaves the battlefield" abilities to trigger. Similarly, phasing in won't cause any "enters the battlefield" abilities to trigger."
- [Ripples of Potential](cards/R/ri.md#ripples-of-potential) — *2023-11-10* — "Choices made for permanents as they entered the battlefield are remembered even after they phase in."
- [March of Swirling Mist](cards/M/mar.md#march-of-swirling-mist) — *2022-02-18* — "Phased out permanents are treated as though they don't exist. They can't be the target of spells or abilities, their static abilities have no effect on the game, their triggered abilities can't trigger, they can't attack or block, and so on."
- [Galadriel's Dismissal](cards/G/ga.md#galadriels-dismissal) — *2023-11-03* — "Choices made for permanents as they entered the battlefield are remembered when they phase in."

## Double-faced cards & transform

**Summary:** Outside the battlefield and stack a DFC has only its front face's characteristics (712.8a), so for example its mana value is the front face's. A transforming permanent is the **same object**, so effects on it keep applying (712.18). An ability that would transform a permanent does nothing if the permanent already transformed since that ability went on the stack (701.27f).

> **CR 712.8a** — While a double-faced card is outside the game or in a zone other than the battlefield or stack, it has only the characteristics of its front face.
>
> **CR 712.8d** — While a double-faced permanent has its front face up, it has only the characteristics of its front face.
>
> **CR 712.8e** — While a nonmodal double-faced permanent has its back face up, it has only the characteristics of its back face. However, its mana value is calculated using the mana cost of its front face. If a permanent is copying the back face of a nonmodal double-faced permanent (even if the object representing that copy is itself a double-faced permanent), the mana value of that permanent is 0. See rule 202.3b.
>
> **CR 712.11** — A double-faced spell is cast with its front face up by default. See rule 601, “Casting Spells.”
>
> **CR 712.14** — A double-faced card put onto the battlefield from a zone other than the stack enters the battlefield with its front face up by default.
>
> **CR 712.18** — When a double-faced permanent transforms or converts, it doesn’t become a new object. Any effects that applied to that permanent will continue to apply to it.
>
> **CR 701.27a** — To transform a permanent, turn it over so that its other face is up. Only permanents represented by double-faced tokens and double-faced cards can transform. (See rule 712, “Double-Faced Cards.”)
>
> **CR 701.27c** — If a spell or ability instructs a player to transform a permanent that isn’t represented by a double-faced token or a double-faced card, nothing happens.
>
> **CR 701.27f** — If an activated or triggered ability of a permanent that isn’t a delayed triggered ability of that permanent tries to transform it, the permanent does so only if it hasn’t transformed or converted since the ability was put onto the stack. If a delayed triggered ability of a permanent tries to transform that permanent, the permanent does so only if it hasn’t transformed or converted since that delayed triggered …

**Official CR examples** (4):

- *CR 712.9 example* — A Clone enters the battlefield as a copy of Wildblood Pack (the back face of a double-faced card). The Clone will be a copy of the Wildblood Pack. Because the Clone is itself not a double-faced card, it can’t transform.
- *CR 712.9 example* — A player casts Cytoshape, causing a Kruin Outlaw (the front face of a double-faced card) to become a copy of Elite Vanguard (a 2/1 Human Soldier creature) until end of turn. The player then casts Moonmist, which reads, in part, “Transform all Humans.” Because the copy of Elite Vanguard is a double-faced card, it will transform. The resulting permanent will have its back face up, but it will still be a copy of Elite Vanguard that turn.
- *CR 712.13a example* — A player controls both Mycosynth Lattice and March of the Machines, the combined effects of which make all permanents artifact creatures in addition to their other types. They also control a Clone on the battlefield that is a copy of Bird Admirer, a creature with daybound. It is currently night, but that permanent can’t transform because it isn’t represented by a double-faced card. Its controller casts Mystic Reflection targeting it, then casts Invasion of Kylem, a Siege battle whose back face is a sorcery. Because Invasion of Kylem is entering the battlefield as a creature, Mystic Reflection’s replacement effect applies to it and it tries to enter the battlefield as a copy of Bird Admirer. Since it is night, the daybound ability would normally cause it to enter with its back face up. However, since its back face is a sorcery, it is instead put into its owner’s graveyard.
- *CR 712.18 example* — An effect gives Village Ironsmith (the front face of a double-faced card) +2/+2 until end of turn and then Village Ironsmith transforms into Ironfang. Ironfang will continue to get +2/+2 until end of turn.

**Official rulings that apply these rules** (WotC, most-played cards first by EDHREC rank):

- [Sink into Stupor // Soporific Springs](cards/S/si.md#sink-into-stupor--soporific-springs) — *2024-06-07* — "If an effect allows you to play a land or cast a spell from among a group of cards, you may play or cast a modal double-faced card with any face that fits the criteria of that effect. For example, if an effect allows you to play lands from your graveyard, you can play Garden of Freyalise, but you can't cast Disciple of Freyalise."
- [Fell the Profane // Fell Mire](cards/F/fe.md#fell-the-profane--fell-mire) — *2024-06-07* — "A modal double-faced card can't be transformed or be put onto the battlefield transformed. Ignore any instruction to transform a modal double-faced card or to put one onto the battlefield transformed."
- [Malakir Rebirth // Malakir Mire](cards/M/mal.md#malakir-rebirth--malakir-mire) — *2020-09-25* — "There is a single triangle icon in the top left corner of the front face. There is a double triangle icon in the top left corner of the back face."
- [Reality Shift](cards/R/rea.md#reality-shift) — *2014-11-24* — "If a double-faced card is manifested, it will be put onto the battlefield face down. While face down, it can't transform. If the front face of the card is a creature card, you can turn it face up by paying its mana cost. If you do, its front face will be up."
- [Bala Ged Recovery // Bala Ged Sanctuary](cards/B/bal.md#bala-ged-recovery--bala-ged-sanctuary) — *2020-09-25* — "In the Commander variant, a double-faced card’s color identity is determined by the mana costs and mana symbols in the rules text of both faces combined. If either face has a color indicator or basic land type, those are also considered."
- [Disciple of Freyalise // Garden of Freyalise](cards/D/di.md#disciple-of-freyalise--garden-of-freyalise) — *2024-06-07* — "To determine whether it is legal to play a modal double-faced card, consider only the characteristics of the face you're playing and ignore the other face's characteristics. For example, if an effect stops you from casting creature spells, you can't cast Disciple of Freyalise, but you can still play Garden of Freyalise."

## The legend rule

**Summary:** If you control two or more legendary permanents with the same name, you choose one and the rest go to their owners' graveyards as a state-based action (704.5j). Different players can each control one with the same name. Planeswalkers follow the same rule (306.4).

> **CR 704.5j** — If two or more legendary permanents with the same name are controlled by the same player, that player chooses one of them, and the rest are put into their owners’ graveyards. This is called the “legend rule.”
>
> **CR 306.4** — Previously, planeswalkers were subject to a “planeswalker uniqueness rule” that stopped a player from controlling two planeswalkers of the same planeswalker type. This rule has been removed and planeswalker cards printed before this change have received errata in the Oracle card reference to have the legendary supertype. Like other legendary permanents, they are subject to the “legend rule” (see rule 704.5j).

**Official rulings that apply these rules** (WotC, most-played cards first by EDHREC rank):

- [Gemstone Caverns](cards/G/ge.md#gemstone-caverns) — *2021-03-19* — "If multiple Gemstone Caverns are put onto the battlefield under a single player's control before the game begins, the "legend rule" won't put the extras into that player's graveyard until just before the starting player gets priority during the game's first upkeep step. There's no opportunity to tap the extras for mana."
- [Mox Opal](cards/M/mox.md#mox-opal) — *2020-08-07* — "If you control Mox Opal and one other artifact, then have a second Mox Opal enter the battlefield as your third artifact, you can't activate either one's mana ability before putting one into your graveyard due to the “legend rule.”"
- [Spark Double](cards/S/spa.md#spark-double) — *2019-05-03* — "Spark Double isn’t legendary if it copies a legendary permanent, and this exception is copiable. If something else copies Spark Double later, that copy also won’t be legendary. If you control two or more permanents with the same name but only one is legendary, the “legend rule” doesn’t apply."
- [Helm of the Host](cards/H/he.md#helm-of-the-host) — *2018-04-27* — "The token isn't legendary, and this exception is copiable. If something else copies the token later, that copy also won't be legendary. If you control two or more permanents with the same name but only one is legendary, the "legend rule" doesn't apply."
- [Mayhem Devil](cards/M/may.md#mayhem-devil) — *2019-05-03* — "A legendary permanent that is put into a graveyard because of the "legend rule" isn't sacrificed."
- [Elesh Norn, Grand Cenobite](cards/E/el.md#elesh-norn-grand-cenobite) — *2017-11-17* — "If a second Elesh Norn, Grand Cenobite comes under your control, you'll put one into its owner's graveyard due to the “legend rule” at the same time that any of your opponents' creatures getting -4/-4 are put into their owner's graveyard for having 0 or less toughness."

## "Can't" beats "can" (and impossible instructions)

**Summary:** When one effect allows something and another says it **can't** happen, the "can't" wins (101.2). The parts of an instruction that are impossible are ignored (101.3). Simultaneous choices are made in APNAP order (101.4).

> **CR 101.1** — Whenever a card’s text directly contradicts these rules, the card takes precedence. The card overrides only the rule that applies to that specific situation. The only exception is that a player can concede the game at any time (see rule 104.3a).
>
> **CR 101.2** — When a rule or effect allows or directs something to happen, and another effect states that it can’t happen, the “can’t” effect takes precedence.
>
> **CR 101.3** — Any part of an instruction that’s impossible to perform is ignored. (In many cases the card will specify consequences for this; if it doesn’t, there’s no effect.)
>
> **CR 101.4** — If multiple players would make choices and/or take actions at the same time, the active player (the player whose turn it is) makes any choices required, then the next player in turn order (usually the player seated to the active player’s left) makes any choices required, followed by the remaining nonactive players in turn order. Then the actions happen simultaneously. This rule is often referred to as the “Active …

**Official CR examples** (2):

- *CR 101.2 example* — If one effect reads “You may play an additional land this turn” and another reads “You can’t play lands this turn,” the effect that precludes you from playing lands wins.
- *CR 101.4 example* — A card reads “Each player sacrifices a creature.” First, the active player chooses a creature they control. Then each of the nonactive players, in turn order, chooses a creature they control. Then all creatures chosen this way are sacrificed simultaneously.

**Official rulings that apply these rules** (WotC, most-played cards first by EDHREC rank):

- ⚠️ No official card ruling in the bulk matched this topic; rely on the quoted CR text.

## Ordering replacement effects (worked examples)

**Summary:** The affected player, or the controller of the affected object, chooses the order. Self-replacement effects come first (616.1a, 614.15), then effects that change who controls an entering object (616.1b), then copy-as-it-enters effects (616.1c) and back-face-up effects (616.1d), then any others (616.1e). After each one is applied, re-check which effects still apply (616.1f).

> **CR 616.1** — If two or more replacement and/or prevention effects are attempting to modify the way an event affects an object or player, the affected object’s controller (or its owner if it has no controller) or the affected player chooses one to apply, following the steps listed below. If two or more players have to make these choices at the same time, choices are made in APNAP order (see rule 101.4).
>
> **CR 616.1a** — If any of the replacement and/or prevention effects are self-replacement effects (see rule 614.15), one of them must be chosen. If not, proceed to rule 616.1b.
>
> **CR 616.1b** — If any of the replacement and/or prevention effects would modify under whose control an object would enter the battlefield, one of them must be chosen. If not, proceed to rule 616.1c.
>
> **CR 616.1c** — If any of the replacement and/or prevention effects would cause an object to become a copy of another object as it enters the battlefield, one of them must be chosen. If not, proceed to rule 616.1d.
>
> **CR 616.1d** — If any of the replacement and/or prevention effects would cause a card to enter the battlefield with its back face up, one of them must be chosen (See rule 701.27, “Transform,” and rule 701.28, “Convert.”). If not, proceed to 616.1e.
>
> **CR 616.1e** — Any of the applicable replacement and/or prevention effects may be chosen.
>
> **CR 616.1f** — Once the chosen effect has been applied, this process is repeated (taking into account only replacement or prevention effects that would now be applicable) until there are no more left to apply.
>
> **CR 616.1g** — While following the steps in 616.1a–f, one replacement or prevention effect may apply to an event, and another may apply to an event contained within the first event. In this case, the second effect can’t be chosen until after the first effect has been chosen.
>
> **CR 614.15** — Some replacement effects are not continuous effects. Rather, they are an effect of a resolving spell or ability that replace part or all of that spell or ability’s own effect(s). Such effects are called self-replacement effects. The text creating a self-replacement effect is usually part of the ability whose effect is being replaced, but the text can be a separate ability, particularly when preceded by an ability …

**Official CR examples** (4):

- *CR 616.1f example* — Two permanents are on the battlefield. One is an enchantment that reads “If a card would be put into a graveyard from anywhere, instead exile it,” and the other is a creature that reads “If this creature would die, instead shuffle it into its owner’s library.” If the creature is destroyed, its controller decides which replacement to apply first; the other does nothing.
- *CR 616.1f example* — Essence of the Wild reads “Creatures you control enter as a copy of this creature.” A player who controls Essence of the Wild casts Rusted Sentinel, which normally enters the battlefield tapped. As it enters the battlefield, the copy effect from Essence of the Wild is applied first. As a result, it no longer has the ability that causes it to enter the battlefield tapped. Rusted Sentinel will enter the battlefield as an untapped copy of Essence of the Wild.
- *CR 616.1g example* — A player is instructed to create a token that’s a copy of Voice of All, which has the ability “As this creature enters, choose a color.” Doubling Season has an ability that reads “If an effect would create one or more tokens under your control, it creates twice that many of those tokens instead.” Because entering the battlefield is an event contained within the event of creating a token, the effect of Doubling Season must be applied first, and then the effects of the two Voice of All tokens may be applied in either order.
- *CR 616.2 example* — One effect reads “If you would gain life, draw that many cards instead,” and another reads “If you would draw a card, return a card from your graveyard to your hand instead.” Both effects combine (regardless of the order they came into existence): Instead of gaining 1 life, the player puts a card from their graveyard into their hand.

**Official rulings that apply these rules** (WotC, most-played cards first by EDHREC rank):

- [Teferi's Ageless Insight](cards/T/te.md#teferis-ageless-insight) — *2020-06-23* — "If two or more replacement effects would apply to a card-drawing event, the player drawing the card chooses the order in which to apply them."
- [Memory Lapse](cards/M/me.md#memory-lapse) — *2016-06-08* — "Memory Lapse has a self-replacement effect that replaces the spell going to the graveyard before any other effect can replace that event. If the spell was cast using flashback, however, flashback will change the spell's destination from its owner's library to exile."
- [Mystic Reflection](cards/M/my.md#mystic-reflection) — *2021-02-05* — "Replacement effects that modify how a creature enters the battlefield are applied in the following order: first, control-changing effects (such as Gather Specimens), then copy effects (such as the abilities of Mystic Reflection and Clone), then all other effects."
- [Bard, King of Dale](cards/B/bar.md#bard-king-of-dale) — *2026-06-29* — "If an effect creates more than one kind of token, it'll create twice as many of each kind. For example, if you control Bilbo, Fellow Conspirator and Bard, King of Dale and you create a Food token, you'll create two Food tokens and two Treasure tokens (regardless of the order you chose to apply the replacement effects)."
- [Archelos, Lagoon Mystic](cards/A/arc.md#archelos-lagoon-mystic) — *2020-11-10* — "If more than one Archelos is on the battlefield, the controller of an entering permanent chooses how to order the replacement effects."
- [Infinite Reflection](cards/I/inf.md#infinite-reflection) — *2012-05-01* — "Replacement effects that modify how a permanent enters are now applied in the following order: control-changing effects (such as Gather Specimens), then copy effects (such as the abilities of Infinite Reflection and Clone), then all other effects."

## Commander damage

**Summary:** A player who has been dealt **21 or more combat damage by the same commander** over the game loses. This is a state-based action (903.10a, 704.6c). Only **combat** damage counts. Partner commanders are tracked separately (702.124d).

> **CR 903.10a** — A player who’s been dealt 21 or more combat damage by the same commander over the course of the game loses the game. (This is a state-based action. See rule 704.)
>
> **CR 704.6c** — In a Commander game, a player who’s been dealt 21 or more combat damage by the same commander over the course of the game loses the game. See rule 903, “Commander.”
>
> **CR 702.124d** — Except for determining the color identity of your commander, the two commanders function independently. When casting a commander with partner, ignore how many times your other commander has been cast (see rule 903.8). When determining whether a player has been dealt 21 or more combat damage by the same commander, consider damage from each of your two commanders separately (see rule 903.10a).

**Official rulings that apply these rules** (WotC, most-played cards first by EDHREC rank):

- [Angel's Grace](cards/A/an.md#angels-grace) — *2021-03-19* — "In a Commander game, combat damage you're dealt by a commander is still tracked, even if it doesn't change your life total."
- [Archon of Coronation](cards/A/arc.md#archon-of-coronation) — *2020-11-10* — "Combat damage dealt to you by a commander is still tracked, even if it didn't cause you to lose life."
- [Courageous Resolve](cards/C/cou.md#courageous-resolve) — *2023-11-03* — "In a Commander game, combat damage you're dealt by a commander is still tracked, even if you don't lose life as a result."
- [Elderscale Wurm](cards/E/el.md#elderscale-wurm) — *2012-07-01* — "In a Commander game, combat damage you’re dealt by a commander is still tracked, even if it doesn’t change your life total."
- [Aethersnatch](cards/A/ae.md#aethersnatch) — *2015-11-04* — "Combat damage dealt by a commander is tracked without regard to who controlled the commander at the time it dealt damage. For example, say a commander deals 10 combat damage to a player, leaves the battlefield, is recast, and you gain control of it with Aethersnatch. If it deals another 11 combat damage to that same player, they will lose the game."
- [Tahngarth, First Mate](cards/T/ta.md#tahngarth-first-mate) — *2019-08-23* — "Commander damage is tracked for each commander. It doesn't matter who controls the commander as it deals damage. If Tahngarth deals 10 damage to one player while under your control and another 11 damage to that same player while under a third player's control, the player loses the game."

## Partner & Backgrounds

**Summary:** Partner variants let you have two commanders (100 cards total, 702.124b). Your color identity is the combined identity of both (702.124c). Each commander has its own commander tax and its own commander-damage count (702.124d). Different partner abilities can't be combined (702.124f).

> **CR 702.124a** — Partner abilities are keyword abilities that modify the rules for deck construction in the Commander variant (see rule 903), and they function before the game begins. Each partner ability allows you to designate two legendary cards as your commander rather than one. Each partner ability has its own requirements for those two commanders. The partner abilities are: partner, partner—[text], partner with [name], choose …
>
> **CR 702.124b** — Your deck must contain exactly 100 cards, including its two commanders. Both commanders begin the game in the command zone.
>
> **CR 702.124c** — A rule or effect that refers to your commander’s color identity refers to the combined color identities of your two commanders. See rule 903.4.
>
> **CR 702.124d** — Except for determining the color identity of your commander, the two commanders function independently. When casting a commander with partner, ignore how many times your other commander has been cast (see rule 903.8). When determining whether a player has been dealt 21 or more combat damage by the same commander, consider damage from each of your two commanders separately (see rule 903.10a).
>
> **CR 702.124f** — Different partner abilities are distinct from one another and cannot be combined. For example, you cannot designate two cards as your commander if one of them has “partner” and the other has “partner with [name].”
>
> **CR 702.124h** — “Partner” means “You may designate two legendary cards as your commander rather than one if each of them has partner.”
>
> **CR 702.124j** — “Partner with [name]” represents two abilities. It means “You may designate two legendary cards as your commander rather than one if each has a ‘partner with [name]’ ability with the other’s name” and “When this permanent enters, target player may search their library for a card named [name], reveal it, put it into their hand, then shuffle.”
>
> **CR 702.124k** — “Choose a Background” means “You may designate two cards as your commander rather than one if one of them is this card and the other is a legendary Background enchantment card.” You can’t designate two cards as your commander if one has a “choose a Background” ability and the other is not a legendary Background enchantment card, and legendary Background enchantment cards can’t be your commander unless you have also …

**Official rulings that apply these rules** (WotC, most-played cards first by EDHREC rank):

- [Command Beacon](cards/C/com.md#command-beacon) — *2016-11-08* — "If you have two commanders with the partner ability in the command zone, Command Beacon's effect puts one of your choice into your hand, not both."
- [Loyal Apprentice](cards/L/lo.md#loyal-apprentice) — *2018-07-13* — "The lieutenant effect happens only once each combat, even if you somehow control multiple commanders (perhaps because you have two commanders with a partner ability from the Battlebond™ set)."
- [Jaheira, Friend of the Forest](cards/J/ja.md#jaheira-friend-of-the-forest) — *2022-06-10* — "If your commander loses the choose a Background ability or stops being a Background during the game, as appropriate, it is still your commander."
- [Kodama of the East Tree](cards/K/ko.md#kodama-of-the-east-tree) — *2020-11-10* — "You can choose two commanders with partner that are the same color or colors. In Commander Draft, you can even choose two of the same commander with partner if you drafted them. If you do this, make sure you keep the number of times you've cast each from the command zone clear for "commander tax" purposes."
- [Karlach, Fury of Avernus](cards/K/ka.md#karlach-fury-of-avernus) — *2022-06-10* — "Choose a Background is a variant of the partner ability. You may have two commanders if one of them is a legendary creature with the choose a background ability and the other is a legendary Background enchantment. Backgrounds and cards with choose a Background do not interact with cards which have any other partner ability."
- [Kediss, Emberclaw Familiar](cards/K/ke.md#kediss-emberclaw-familiar) — *2020-11-10* — "To have two commanders, both must have the partner ability as the game begins. Losing the ability during the game doesn't cause either to cease to be your commander."

## When a player leaves a multiplayer game

**Summary:** When a player leaves a multiplayer game, everything they **own** leaves with them, and effects that gave them control of something end. Anything they still control after that is exiled (800.4a). Damage that would be assigned to a player who has left isn't assigned (800.4e).

> **CR 800.4a** — When a player leaves the game, all objects (see rule 109) owned by that player leave the game and any effects which give that player control of any objects or players end. Then, if that player controlled any objects on the stack not represented by cards, those objects cease to exist. Then, if there are any objects still controlled by that player, those objects are exiled. This is not a state-based action. It happens …
>
> **CR 800.4b** — If an object would change to the control of a player who has left the game, it doesn’t. If a token would be created under the control of a player who has left the game, no token is created. If an object would be put onto the battlefield or onto the stack under the control of a player who has left the game, that object remains in its current zone. If a player would be controlled by a player who has left the game, …
>
> **CR 800.4d** — If an object that would be owned by a player who has left the game would be created in any zone, it isn’t created. If a triggered ability that would be controlled by a player who has left the game would be put onto the stack, it isn’t put on the stack.
>
> **CR 800.4e** — If combat damage would be assigned to a player who has left the game, that damage isn’t assigned.
>
> **CR 800.4j** — If a player leaves the game during their turn, that turn continues to its completion without an active player. If the active player would receive priority, instead the next player in turn order receives priority, or the top object on the stack resolves, or the phase or step ends, whichever is appropriate.
>
> **CR 800.4m** — When a player leaves the game, any continuous effects with durations that last until that player’s next turn or until a specific point in that turn will last until that turn would have begun. They neither expire immediately nor last indefinitely.

**Official CR examples** (5):

- *CR 800.4a example* — Alex casts Mind Control, an Aura that reads, “You control enchanted creature,” on Bianca’s Assault Griffin. If Alex leaves the game, so does Mind Control, and Assault Griffin reverts to Bianca’s control. If, instead, Bianca leaves the game, so does Assault Griffin, and Mind Control is put into Alex’s graveyard.
- *CR 800.4a example* — Alex casts Act of Treason, which reads, in part, “Gain control of target creature until end of turn,” targeting Bianca’s Runeclaw Bears. If Alex leaves the game, Act of Treason’s change-of-control effect ends and Runeclaw Bears reverts to Bianca’s control.
- *CR 800.4a example* — Alex casts Bribery, which reads, “Search target opponent’s library for a creature card and put that card onto the battlefield under your control. Then that player shuffles their library,” targeting Bianca. Alex puts Serra Angel onto the battlefield from Bianca’s library. If Bianca leaves the game, Serra Angel also leaves the game. If, instead, Alex leaves the game, Serra Angel is exiled.
- *CR 800.4a example* — Alex controls Genesis Chamber, which reads, “Whenever a nontoken creature enters, if Genesis Chamber is untapped, that creature’s controller creates a 1/1 colorless Myr artifact creature token.” If Alex leaves the game, all such Myr tokens that entered the battlefield under Alex’s control leave the game, and all such Myr tokens that entered the battlefield under any other player’s control remain in the game.
- *CR 800.4d example* — Astral Slide is an enchantment that reads, “Whenever a player cycles a card, you may exile target creature. If you do, return that creature to the battlefield under its owner’s control at the beginning of the next end step.” During Alex’s turn, Bianca uses Astral Slide’s ability to exile Alex’s Hypnotic Specter. Before the end of that turn, Bianca leaves the game. At the beginning of the end step, the delayed triggered ability generated by Astral Slide that would return Hypnotic Specter to the battlefield triggers, but it isn’t put on the stack. Hypnotic Specter never returns to the battlefield.

**Official rulings that apply these rules** (WotC, most-played cards first by EDHREC rank):

- [Reanimate](cards/R/rea.md#reanimate) — *2025-09-19* — "In a multiplayer game, if a player leaves the game, all cards that player owns leave as well. If you leave the game, the creature you control from Reanimate is exiled."
- [Teferi's Protection](cards/T/te.md#teferis-protection) — *2017-08-25* — "If you gain control of another player's permanent and it phases out, if the duration of the control-change effect expires before it phases in, that permanent phases in under that other player's control as your next untap step begins. If you leave the game before your next untap step, it phases in as the next untap step begins after your turn would have begun."
- [Etali, Primal Storm](cards/E/et.md#etali-primal-storm) — *2021-03-19* — "In a multiplayer game, if a player leaves the game, all cards that player owns leave as well. If you leave the game, any spells or permanents you control from Etali's ability are exiled."
- [Reality Shift](cards/R/rea.md#reality-shift) — *2014-11-24* — "If a face-down permanent you control leaves the battlefield, you must reveal it. You must also reveal all face-down spells and permanents you control if you leave the game or if the game ends."
- [Conjurer's Closet](cards/C/con.md#conjurers-closet) — *2020-08-07* — "When an effect returns the exiled card “under your control,” you control it indefinitely after that. In a multiplayer game, if a player leaves the game, all cards that player owns leave as well. If you leave the game, any creatures you control from Conjurer's Closet effect are exiled."
- [Wishclaw Talisman](cards/W/wi.md#wishclaw-talisman) — *2019-10-04* — "You choose which opponent gains control of Wishclaw Talisman while its ability is resolving. If that player later leaves the game, you regain control of Wishclaw Talisman."

## Open questions / next topics
- Possible further topics: morph/disguise & face-down (708), split/adventure/omen cards (709, 715), the monarch & initiative (724, 725), day/night (726), dungeons (309), banding (702.22).
- ❓ Any rule summary here that disagrees with the quoted text is an error: the quoted CR text wins.
