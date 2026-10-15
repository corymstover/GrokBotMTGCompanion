# Rules Interactions

> **Source of truth:** Magic: The Gathering **Comprehensive Rules, effective 2026-09-25** ([official text](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt), Wizards of the Coast). Rule text below is **quoted verbatim** (long rules trimmed with "…"); card rulings are **official WotC rulings** from the Scryfall rulings bulk (2026-10-15), quoted verbatim and linked to the card entries that carry them. Plain-language summaries are labeled **Summary** and are paraphrase, not rules text. Started Bot cycle 3 (issue [#9](https://github.com/corymstover/GrokBotMTGCompanion/issues/9)).

## Contents
- [Layers & timestamps](#layers--timestamps) — CR 613
- [Dependency](#dependency) — CR 613.8
- [Replacement effects vs. triggered abilities](#replacement-effects-vs-triggered-abilities) — CR 614
- [State-based actions](#state-based-actions) — CR 704
- [Copy effects](#copy-effects) — CR 707
- [Commander: color identity](#commander-color-identity) — CR 903.4
- [Commander: returning to the command zone](#commander-returning-to-the-command-zone) — CR 903.9
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

## Open questions / next topics
- Next (cycle 4): priority & the stack (CR 117, 405, 608), combat damage assignment (510), protection (702.16), ward (702.21), mutate/merge (702.140, 730), saga & class layers, and a worked example per layer using the card files.
- ❓ Any rule summary here that disagrees with the quoted text is an error: the quoted CR text wins.
