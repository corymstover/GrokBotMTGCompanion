---
title: "Mai and Zuko — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Mai and Zuko — Interaction Review

> Bot cycle 49 · batch C · reviewed 2026-10-16. Deck: [Mai and Zuko](../decks/mai-and-zuko.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/mai-and-zuko.txt`](../../exports/grixis-archidekt/mai-and-zuko.txt) · SHA-256 `0e399fea73acb804044395007e7bb9d9416863b41e09c9f10cd1c3f4c5b9651e` |
| Rulings | **9** (9 verified · 0 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`Mai_and_Zuko_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/mai_and_zuko_2026-10-14/Mai_and_Zuko_Rules_Attestation.json) (17 interactions, all PASS) |

## Contents
- [Summary](#summary)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [Timing and priority](#timing-and-priority)
- [Replacement and prevention effects](#replacement-and-prevention-effects)
- [Rules cited](#rules-cited)

## Summary

Mai and Zuko give Allies and artifacts flash, and firebending 3 makes {R}{R}{R} that lasts all combat. The list leans on flashed artifacts, opponent-turn payoffs (Katara, Unwinding Clock) and artifact combos. This review re-verifies all 17 attestation items. Eight Spellbook lines are confirmed (Monolith + Rings, the Top loops, Breach).

Rules surprises: Urza's Saga can't find Walking Ballista; Unwinding Clock untaps Mana Vault on opponents' turns; Mai and Zuko's flash lets Mystic Forge cast Top from the library at instant speed. No list errors.

## Commander rules text and edge cases

### maizuko-01: Flash for Allies and artifacts; firebending mana lasts through combat

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mai and Zuko

**Ruling.** You may cast Ally and artifact spells at instant speed. That changes timing only, not cost. Firebending 3 is an attack trigger, not a mana ability, so it uses the stack. Its {R}{R}{R} lasts until combat ends, so you can spend it on flashed artifacts and Allies at any point in combat, even after damage. Other mana you make in combat still empties between steps.

**Citations**

- Oracle, *Mai and Zuko*: “You may cast Ally spells and artifact spells as though they had flash.”
- Scryfall ruling, *Mai and Zuko*: “Firebending abilities aren't mana abilities. They use the stack and can be responded to.”
- Scryfall ruling, *Mai and Zuko*: “Mana from firebending abilities isn't lost until you leave combat and go to your second main phase. It can be used at any time during combat, even after combat damage has been dealt.”
- [CR 702.189a](#cr-702189a), [CR 702.8a](#cr-7028a), [CR 106.4](#cr-1064)
- Source (re-verified): [`Mai_and_Zuko_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/mai_and_zuko_2026-10-14/Mai_and_Zuko_Rules_Attestation.json) → “Mai and Zuko flash permission”
- Source (re-verified): [`Mai_and_Zuko_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/mai_and_zuko_2026-10-14/Mai_and_Zuko_Rules_Attestation.json) → “Firebending 3 and combat casting”

## Combos and engine lines

### maizuko-07: Basalt Monolith + Rings of Brighthearth → Walking Ballista

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mai and Zuko, Basalt Monolith, Rings of Brighthearth, Walking Ballista

**Ruling.** Tap Monolith for {C}{C}{C}, activate its {3} untap, and pay {2} for Rings to copy the untap. The copy untaps it, you tap again for three, and the original untaps it once more. That nets colorless mana each loop, and Walking Ballista turns it into damage. Rings can't copy mana abilities, but the untap isn't one.

**Citations**

- Scryfall ruling, *Rings of Brighthearth*: “An activated mana ability is one that produces mana as it resolves, not one that costs mana to activate.”
- [CR 605.1a](#cr-6051a), [CR 707.10](#cr-70710)
- Commander Spellbook [4131-4235](https://commanderspellbook.com/combo/4131-4235/) (community-maintained, retrieved 2026-10-16): “Rings of Brighthearth triggers, causing you to pay {2} to copy Basalt Monolith's last ability.”
- Source (re-verified): [`Mai_and_Zuko_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/mai_and_zuko_2026-10-14/Mai_and_Zuko_Rules_Attestation.json) → “Basalt Monolith plus Rings of Brighthearth”

### maizuko-08: Sensei's Divining Top loops: Citadel + Aetherflux, or Mystic Forge + a cost reducer

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mai and Zuko, Sensei's Divining Top, Bolas's Citadel, Aetherflux Reservoir, Mystic Forge, Foundry Inspector, Etherium Sculptor, Enthusiastic Mechanaut, Longshot, Rebel Bowman

**Ruling.** Top's draw puts Top back on top of your library. Recast it from there: with Bolas's Citadel it costs 1 life and Aetherflux gains more each time; with Mystic Forge and a {1} reducer (Foundry Inspector, Etherium Sculptor, Enthusiastic Mechanaut, Longshot) it's free. The recast Top is a new, untapped artifact, so it can tap right away. Longshot pings each opponent for 2 per cast. Mai and Zuko's flash lets Top be cast from the library on an opponent's turn too, which Forge alone wouldn't allow.

**Citations**

- Oracle, *Mystic Forge*: “You may cast artifact spells and colorless spells from the top of your library.”
- Oracle, *Longshot, Rebel Bowman*: “Whenever you cast a noncreature spell, Longshot deals 2 damage to each opponent.”
- Scryfall ruling, *Mystic Forge*: “You must follow the normal timing permissions and restrictions of the spells you cast from your library.”
- [CR 400.7](#cr-4007), [CR 302.6](#cr-3026), [CR 601.2f](#cr-6012f)
- Commander Spellbook [2173-4740-5078](https://commanderspellbook.com/combo/2173-4740-5078/) (community-maintained, retrieved 2026-10-16): “Cast Sensei's Divining Top from the top of your library by paying 1 life.”
- Commander Spellbook [985-5078-7356](https://commanderspellbook.com/combo/985-5078-7356/) (community-maintained, retrieved 2026-10-16): “Longshot triggers, dealing 2 damage to each opponent.”
- Commander Spellbook [777-985-5078](https://commanderspellbook.com/combo/777-985-5078/) (community-maintained, retrieved 2026-10-16): “Cast Sensei's Divining Top from the top of your library by paying {0}.”
- Source (re-verified): [`Mai_and_Zuko_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/mai_and_zuko_2026-10-14/Mai_and_Zuko_Rules_Attestation.json) → “Bolas's Citadel / Sensei's Divining Top / Aetherflux Reservoir”

### maizuko-09: Breach + LED + Brain Freeze

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mai and Zuko, Underworld Breach, Lion's Eye Diamond, Brain Freeze, Lotus Petal

**Ruling.** The standard Breach backup. LED is an artifact, so Mai and Zuko let you escape it from the graveyard at instant speed too. It needs six other cards in hand and/or graveyard.

**Citations**

- [CR 702.138a](#cr-702138a)
- Commander Spellbook [1368-3518-4856](https://commanderspellbook.com/combo/1368-3518-4856/) (community-maintained, retrieved 2026-10-16): “You have at least six other cards in hand and/or graveyard.”
- Source (re-verified): [`Mai_and_Zuko_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/mai_and_zuko_2026-10-14/Mai_and_Zuko_Rules_Attestation.json) → “Underworld Breach / Lion's Eye Diamond / Brain Freeze”

## Engines and payoffs

### maizuko-02: Combat and opponent-turn payoffs: The Blue Spirit, Katara, Uthros Research Craft

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mai and Zuko, The Blue Spirit, Katara, Waterbending Master, Uthros Research Craft

**Ruling.** The Blue Spirit draws whenever a nontoken creature you control enters during combat, so flash an Ally or artifact creature with firebending mana. Tokens don't count. Katara gives an experience counter for each spell you cast on an opponent's turn, and Mai and Zuko's flash makes those common. To station Uthros Research Craft, tap Mai and Zuko (power 3) at sorcery speed. That reaches 3+ right away, and then every artifact spell, including flashed ones, draws a card.

**Citations**

- Oracle, *The Blue Spirit*: “Whenever a nontoken creature you control enters during combat, draw a card.”
- Oracle, *Katara, Waterbending Master*: “Whenever you cast a spell during an opponent's turn, you get an experience counter.”
- Oracle, *Uthros Research Craft*: “3+ | Whenever you cast an artifact spell, draw a card. Put a charge counter on this Spacecraft.”
- Scryfall ruling, *Uthros Research Craft*: “The triggered ability granted by Uthros Research Craft’s second ability resolves before the spell that caused it to trigger. It resolves even if that spell is countered or otherwise leaves the stack without resolving.”
- [CR 702.184a](#cr-702184a), [CR 721.2](#cr-7212), [CR 122.1](#cr-1221)
- Source (re-verified): [`Mai_and_Zuko_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/mai_and_zuko_2026-10-14/Mai_and_Zuko_Rules_Attestation.json) → “The Blue Spirit combat draw”
- Source (re-verified): [`Mai_and_Zuko_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/mai_and_zuko_2026-10-14/Mai_and_Zuko_Rules_Attestation.json) → “Katara, Waterbending Master experience engine”
- Source (re-verified): [`Mai_and_Zuko_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/mai_and_zuko_2026-10-14/Mai_and_Zuko_Rules_Attestation.json) → “Uthros Research Craft station threshold”

### maizuko-04: Unwinding Clock untaps Mana Vault and Basalt Monolith on others' turns

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mai and Zuko, Unwinding Clock, Mana Vault, Basalt Monolith

**Ruling.** Unwinding Clock untaps all your artifacts during each other player's untap step. 'Doesn't untap during your untap step' (Mana Vault, Basalt Monolith) doesn't stop that, so you get their mana on every opponent's turn for flashed spells. The untap isn't optional.

**Citations**

- Oracle, *Unwinding Clock*: “Untap all artifacts you control during each other player's untap step.”
- Scryfall ruling, *Unwinding Clock*: “Some effects, such as the one generated by Rust Tick's ability, state that an artifact doesn't untap during its controller's untap step. These effects won't apply and stop the artifact from untapping during another player's untap step.”
- [CR 502.3](#cr-5023)
- Source (re-verified): [`Mai_and_Zuko_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/mai_and_zuko_2026-10-14/Mai_and_Zuko_Rules_Attestation.json) → “Unwinding Clock with artifact mana”

### maizuko-06: Ally support: Boiling Rock Rioter, Ally Encampment, Roaming Throne

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mai and Zuko, Boiling Rock Rioter, Ally Encampment, Roaming Throne

**Ruling.** Boiling Rock Rioter taps an Ally to exile a card from a graveyard. On attack it can cast an Ally you own that it exiled. Ally Encampment's restricted mana pays for Mai and Zuko, and it can sacrifice to bounce the commander to hand (cast from hand later, no tax). Roaming Throne on Ally doubles firebending: six {R}.

**Citations**

- Oracle, *Ally Encampment*: “{1}, {T}, Sacrifice this land: Return target Ally you control to its owner's hand.”
- Oracle, *Roaming Throne*: “If a triggered ability of another creature you control of the chosen type triggers, it triggers an additional time.”
- Scryfall ruling, *Mai and Zuko*: “Multiple instances of firebending on the same creature trigger separately, each granting you the appropriate amount of mana.”
- [CR 603.2](#cr-6032), [CR 903.8](#cr-9038)
- Source (re-verified): [`Mai_and_Zuko_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/mai_and_zuko_2026-10-14/Mai_and_Zuko_Rules_Attestation.json) → “Boiling Rock Rioter graveyard and attack permissions”
- Source (re-verified): [`Mai_and_Zuko_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/mai_and_zuko_2026-10-14/Mai_and_Zuko_Rules_Attestation.json) → “Ally Encampment commander protection”
- Source (re-verified): [`Mai_and_Zuko_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/mai_and_zuko_2026-10-14/Mai_and_Zuko_Rules_Attestation.json) → “Roaming Throne and Ally triggers”

## Timing and priority

### maizuko-03: Flash artifacts as interaction: Tundra Tank, The Fire Nation Drill, Thought Monitor

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mai and Zuko, Tundra Tank, The Fire Nation Drill, Thought Monitor

**Ruling.** With Mai and Zuko out, these become instant-speed plays:
- **Tundra Tank:** its ETB gives indestructible in response to destroy effects or lethal damage, but not exile, bounce, sacrifice or -X/-X.
- **The Fire Nation Drill:** its ETB tap (reflexive trigger) kills a creature with power 4 or less, and {1} strips hexproof and indestructible.
- **Thought Monitor:** affinity reduces only the generic part of its cost.

**Citations**

- Oracle, *Tundra Tank*: “When this Vehicle enters, target creature you control gains indestructible until end of turn.”
- Oracle, *The Fire Nation Drill*: “When The Fire Nation Drill enters, you may tap it. When you do, destroy target creature with power 4 or less.”
- [CR 702.12b](#cr-70212b), [CR 603.12](#cr-60312), [CR 702.41a](#cr-70241a)
- Source (re-verified): [`Mai_and_Zuko_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/mai_and_zuko_2026-10-14/Mai_and_Zuko_Rules_Attestation.json) → “Tundra Tank as commander-enabled protection”
- Source (re-verified): [`Mai_and_Zuko_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/mai_and_zuko_2026-10-14/Mai_and_Zuko_Rules_Attestation.json) → “The Fire Nation Drill as flash interaction”
- Source (re-verified): [`Mai_and_Zuko_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/mai_and_zuko_2026-10-14/Mai_and_Zuko_Rules_Attestation.json) → “Thought Monitor timing and affinity”

## Replacement and prevention effects

### maizuko-05: Urza's Saga finds mana cost {0} or {1}, not mana value

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mai and Zuko, Urza's Saga, Walking Ballista, Sensei's Divining Top, Mana Vault

**Ruling.** Chapter III needs an artifact whose printed mana cost is exactly {0} or {1}. Sensei's Divining Top and Mana Vault ({1}) qualify. Walking Ballista ({X}{X}) doesn't, even though its mana value is 0.

**Citations**

- Oracle, *Urza's Saga*: “III — Search your library for an artifact card with mana cost {0} or {1}, put it onto the battlefield, then shuffle.”
- Scryfall ruling, *Urza's Saga*: “While resolving the chapter III ability, you can find only a card with actual mana cost {0} or {1}, not mana value 0 or 1. For example, you couldn't find a card with mana cost {U} or one with mana cost {X}.”
- [CR 202.1](#cr-2021), [CR 107.3](#cr-1073)
- Source (re-verified): [`Mai_and_Zuko_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/mai_and_zuko_2026-10-14/Mai_and_Zuko_Rules_Attestation.json) → “Urza's Saga chapter III search restriction”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 106.4

When an effect instructs a player to add mana, that mana goes into a player’s mana pool. From there, it can be used to pay costs immediately, or it can stay in the player’s mana pool as unspent mana. Each player’s mana pool empties at the end of each step and phase, and the player is said to lose this mana. Cards with abilities that produce mana or refer to unspent mana have received errata in the Oracle™ card reference to no longer explicitly refer to the mana pool.

#### CR 107.3

Many objects use the letter X as a placeholder for a number that needs to be determined. Some objects have abilities that define the value of X; the rest let their controller choose the value of X.

#### CR 122.1

A counter is a marker placed on an object or player that modifies its characteristics and/or interacts with a rule, ability, or effect. Counters are not objects and have no characteristics. Notably, a counter is not a token, and a token is not a counter. Counters with the same name or description are interchangeable.

#### CR 202.1

A card’s mana cost is indicated by mana symbols near the top of the card. (See rule 107.4.) On most cards, these symbols are printed in the upper right corner. Some cards from the Future Sight set have alternate frames in which the mana symbols appear to the left of the illustration.

#### CR 302.6

A creature’s activated ability with the tap symbol or the untap symbol in its activation cost can’t be activated unless the creature has been under its controller’s control continuously since their most recent turn began. A creature can’t attack unless it has been under its controller’s control continuously since their most recent turn began. This rule is informally called the “summoning sickness” rule.

#### CR 400.7

An object that moves from one zone to another becomes a new object with no memory of, or relation to, its previous existence. This rule has the following exceptions.

#### CR 502.3

Third, the active player determines which permanents they control will untap. Then they untap them all simultaneously. This turn-based action doesn’t use the stack. Normally, all of a player’s permanents untap, but effects can keep one or more of a player’s permanents from untapping.

#### CR 601.2f

The player determines the total cost of the spell. Usually this is just the mana cost. Some spells have additional or alternative costs. Some effects may increase or reduce the cost to pay, or may provide other alternative costs. Costs may include paying mana, tapping permanents, sacrificing permanents, discarding cards, and so on. The total cost is the mana cost or alternative cost (as determined in rule 601.2b), plus all additional costs and cost increases, and minus all cost reductions. If multiple cost reductions apply, the player may apply them in any order. If the mana component of the …

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 603.12

A resolving spell or ability may allow or instruct a player to take an action and create a triggered ability that triggers “when [a player] [does or doesn’t]” take that action or “when [something happens] this way.” These reflexive triggered abilities follow the rules for delayed triggered abilities (see rule 603.7), except that they’re checked immediately after being created and trigger based on whether the trigger event or events occurred earlier during the resolution of the spell or ability that created them.

#### CR 605.1a

An activated ability is a mana ability if it meets all of the following criteria: it doesn’t require a target (see rule 115.6), it could add mana to a player’s mana pool when it resolves, it’s not a loyalty ability (see rule 606, “Loyalty Abilities”), and its cost and effect don’t move any card to or from a library. Do not take into account replacement effects that may apply, other than self-replacement effects, when evaluating these criteria.

#### CR 702.8a

Flash is a static ability that functions in any zone from which you could play the card it’s on. “Flash” means “You may play this card any time you could cast an instant.”

#### CR 702.12b

A permanent with indestructible can’t be destroyed. Such permanents aren’t destroyed by lethal damage, and they ignore the state-based action that checks for lethal damage (see rule 704.5g).

#### CR 702.41a

Affinity is a static ability that functions while the spell with affinity is on the stack. “Affinity for [text]” means “This spell costs {1} less to cast for each [text] you control.”

#### CR 702.138a

Escape represents a static ability that functions while the card with escape is in a player’s graveyard. “Escape [cost]” means “You may cast this card from your graveyard by paying [cost] rather than paying its mana cost.” Casting a spell using its escape ability follows the rules for paying alternative costs in rules 601.2b and 601.2f–h.

#### CR 702.184a

Station is an activated ability. “Station” means “Tap another untapped creature you control: Put a number of charge counters on this permanent equal to the tapped creature’s power. Activate only as a sorcery.”

#### CR 702.189a

Firebending is a triggered ability. “Firebending N” means “Whenever this creature attacks, add N {R}. Until end of combat, you don’t lose this mana as steps and phases end.”

#### CR 707.10

To copy a spell, activated ability, or triggered ability means to put a copy of it onto the stack; a copy of a spell isn’t cast and a copy of an activated ability isn’t activated. A copy of a spell or ability copies both the characteristics of the spell or ability and all decisions made for it, including modes, targets, the value of X, and additional or alternative costs. (See rule 601, “Casting Spells.”) Choices that are normally made on resolution are not copied. If an effect of the copy refers to objects used to pay its costs, it uses the objects used to pay the costs of the original spell …

#### CR 721.2

A station symbol represents a static ability. The station symbol includes a single number followed by a plus sign, indicated here as “{N+}.” Any abilities printed within the same text box striation as a station symbol are part of its static ability. The same is true of any power and toughness boxes printed within that striation, indicated here as [P/T].

#### CR 903.8

A player may cast a commander they own from the command zone. A commander cast from the command zone costs an additional {2} for each previous time the player casting it has cast it from the command zone that game. This additional cost is informally known as the “commander tax.”

