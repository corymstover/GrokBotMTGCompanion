---
title: "Kraum, Ludevic's Opus + Tevesh Szat, Doom of Fools — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Kraum, Ludevic's Opus + Tevesh Szat, Doom of Fools — Interaction Review

> Bot cycle 48 · batch B · reviewed 2026-10-16. Deck: [Kraum, Ludevic's Opus + Tevesh Szat, Doom of Fools](../decks/grixistax-october-2026.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-15), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Current list | [`exports/grixis-archidekt/grixistax-october-2026.txt`](../../exports/grixis-archidekt/grixistax-october-2026.txt) · SHA-256 `f0a28f936c03705df0e215738e4ad314d337bb3e713dcf7b2c50beba5a2f9a08` |
| Rulings | **11** (10 verified · 0 uncertain · 1 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-15 · rulings 2026-10-15 |
| Source attestations | [`Grixistax_October_2026_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/grixistax_october_2026_2026-10-14/Grixistax_October_2026_Rules_Attestation.json) (18 interactions, all PASS) |

## Contents
- [Summary](#summary)
- [Flags and open questions](#flags-and-open-questions)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [Key card-pair interactions](#key-card-pair-interactions)
- [Layers and continuous effects](#layers-and-continuous-effects)
- [Timing and priority](#timing-and-priority)
- [Replacement and prevention effects](#replacement-and-prevention-effects)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [What the list depends on](#what-the-list-depends-on)
- [Rules cited](#rules-cited)

## Summary

Grixistax (October 2026) is a Kraum + Tevesh Szat partner prison deck: Contamination, Blood Moon, Back to Basics, Trinisphere and Chalice, with artifact mana to break parity. Tevesh's Thrulls pay for everything. This review re-verifies the eighteen items of the deck's rules attestation, and confirms the Helm of Obedience and Breach lines against cached Commander Spellbook steps.

Rules surprise: Blood Moon switches off the deck's own Phyrexian Tower and other utility lands (anti-synergy flag, no list change).

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [grixistax-05](#grixistax-05-blood-moon-strips-your-own-utility-lands-back-to-basics-still-locks-them) | 🚩 list flag (anti-synergy) | Blood Moon strips your own utility lands; Back to Basics still locks them | Accepted prison cost, documented by the source for Back to Basics. The extra point here is that Blood Moon switches off the deck's own Phyrexian Tower (the Thrull mana outlet). Sequence Tower activations before Moon. No list change. |

## Commander rules text and edge cases

### grixistax-01: Partners: Kraum + Tevesh Szat

**Status:** ✅ verified · **Cards:** Kraum, Ludevic's Opus, Tevesh Szat, Doom of Fools

**Ruling.** Both have partner, so they can be co-commanders; combined identity is blue, black and red. Either one satisfies 'if you control a commander' (Fierce Guardianship, Deflecting Swat, Deadly Rollick). Commander tax is tracked separately for each. Mox Amber makes one mana of a color among your legendary creatures and planeswalkers: Kraum gives blue or red, Tevesh gives black.

**Citations**

- Scryfall ruling, *Kraum, Ludevic's Opus*: “An effect that checks whether you control your commander is satisfied if you control one or both of your two commanders.”
- Scryfall ruling, *Mox Amber*: “Mox Amber's ability adds one mana of the color of your choice from among the colors of legendary creatures and legendary planeswalkers you control. It doesn't add one mana of each of those colors.”
- [CR 702.124a](#cr-702124a), [CR 903.4](#cr-9034), [CR 903.8](#cr-9038)
- Source (re-verified): [`Grixistax_October_2026_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/grixistax_october_2026_2026-10-14/Grixistax_October_2026_Rules_Attestation.json) → “Partner commanders and combined color identity”
- Source (re-verified): [`Grixistax_October_2026_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/grixistax_october_2026_2026-10-14/Grixistax_October_2026_Rules_Attestation.json) → “Commander-dependent free spells and Mox Amber”

### grixistax-02: Kraum: once per opponent per turn, under Damping Sphere too

**Status:** ✅ verified · **Cards:** Kraum, Ludevic's Opus, Damping Sphere

**Ruling.** Kraum draws when one opponent casts their second spell in a turn. It's once per opponent per turn, two spells from different opponents don't count, and it looks at the whole turn even if Kraum arrived late. Damping Sphere taxes each extra spell but doesn't forbid it, so an opponent who pays still gives you a card.

**Citations**

- Scryfall ruling, *Kraum, Ludevic's Opus*: “One opponent must cast two spells for Kraum's triggered ability to trigger. Two spells from different opponents won't cause it to trigger.”
- Scryfall ruling, *Kraum, Ludevic's Opus*: “Kraum's triggered ability can trigger only once each turn for each opponent.”
- Scryfall ruling, *Damping Sphere*: “Damping Sphere’s second ability counts spells that were cast during a turn even if Damping Sphere wasn’t on the battlefield as they were cast.”
- [CR 603.2](#cr-6032)
- Source (re-verified): [`Grixistax_October_2026_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/grixistax_october_2026_2026-10-14/Grixistax_October_2026_Rules_Attestation.json) → “Damping Sphere and Kraum's second-spell trigger”

## Combos and engine lines

### grixistax-09: Helm of Obedience + Leyline of the Void or Dauthi Voidwalker

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Tevesh Szat, Doom of Fools, Helm of Obedience, Leyline of the Void, Dauthi Voidwalker

**Ruling.** With Leyline or Voidwalker exiling cards that would go to the opponent's graveyard, Helm's mill never puts a card there. The stop condition is never met, so X = 1 exiles the opponent's whole library. Voidwalker's exiled cards also get void counters.

**Citations**

- Scryfall ruling, *Helm of Obedience*: “If an effect like that of Leyline of the Void prevents cards from being put into your opponent’s graveyard, the process described in the first sentence of Helm of Obedience’s effect will never stop. Your opponent’s entire library will be exiled, even if X is 1.”
- [CR 614.6](#cr-6146), [CR 701.17a](#cr-70117a)
- Commander Spellbook [2163-5065](https://commanderspellbook.com/combo/2163-5065/) (community-maintained, retrieved 2026-10-16): “Activate Helm of Obedience by paying {1} and tapping it, causing target opponent to mill a card.”
- Commander Spellbook [2581-5065](https://commanderspellbook.com/combo/2581-5065/) (community-maintained, retrieved 2026-10-16): “Due to Dauthi Voidwalker's replacement effect, the milled card is exiled instead of going to the graveyard, and that opponents repeats that process until their library is empty.”
- Source (re-verified): [`Grixistax_October_2026_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/grixistax_october_2026_2026-10-14/Grixistax_October_2026_Rules_Attestation.json) → “Helm of Obedience plus Leyline of the Void or Dauthi Voidwalker”

## Engines and payoffs

### grixistax-03: Tevesh Thrulls feed every sacrifice outlet

**Status:** ✅ verified · **Cards:** Tevesh Szat, Doom of Fools, Contamination, Skullclamp, Phyrexian Tower, Culling the Weak, Diabolic Intent

**Ruling.** Tevesh's +2 makes two 0/1 Thrulls. They pay Contamination's upkeep, die at once to Skullclamp (+1/-1 makes them 1/0, a state-based death, draw two), and are sacrifice fodder for Phyrexian Tower ({B}{B}), Culling the Weak ({B}{B}{B}{B}) and Diabolic Intent. Tevesh's +1 can also sacrifice one to draw two (three if it was a commander). You choose what to sacrifice as the ability resolves.

**Citations**

- Oracle, *Tevesh Szat, Doom of Fools*: “+2: Create two 0/1 black Thrull creature tokens.”
- Oracle, *Skullclamp*: “Whenever equipped creature dies, draw two cards.”
- Scryfall ruling, *Tevesh Szat, Doom of Fools*: “For the second ability of Tevesh Szat, Doom of Fools, you choose whether to sacrifice anything and what to sacrifice as the ability resolves.”
- [CR 704.5f](#cr-7045f), [CR 701.21a](#cr-70121a)
- Source (re-verified): [`Grixistax_October_2026_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/grixistax_october_2026_2026-10-14/Grixistax_October_2026_Rules_Attestation.json) → “Tevesh Szat plus Contamination”
- Source (re-verified): [`Grixistax_October_2026_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/grixistax_october_2026_2026-10-14/Grixistax_October_2026_Rules_Attestation.json) → “Tevesh Szat plus Skullclamp”
- Source (re-verified): [`Grixistax_October_2026_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/grixistax_october_2026_2026-10-14/Grixistax_October_2026_Rules_Attestation.json) → “Tevesh Szat plus Phyrexian Tower / Culling the Weak / Diabolic Intent”

## Key card-pair interactions

### grixistax-08: Karn locks the Wishclaw you hand over

**Status:** ✅ verified · **Cards:** Tevesh Szat, Doom of Fools, Karn, the Great Creator, Wishclaw Talisman

**Ruling.** After Wishclaw's tutor resolves, an opponent gains control of it. With Karn out, opponents can't activate abilities of artifacts they control, so they can't use it. Karn doesn't stop triggered abilities. His -2 needs an artifact you own from outside the game or face-up in exile; the deck doesn't plan on a wishboard.

**Citations**

- Oracle, *Karn, the Great Creator*: “Activated abilities of artifacts your opponents control can't be activated.”
- Scryfall ruling, *Karn, the Great Creator*: “Triggered abilities (starting with "when," "whenever," or "at") are unaffected by Karn.”
- [CR 602.5](#cr-6025), [CR 108.3](#cr-1083)
- Source (re-verified): [`Grixistax_October_2026_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/grixistax_october_2026_2026-10-14/Grixistax_October_2026_Rules_Attestation.json) → “Karn, the Great Creator plus Wishclaw Talisman”

## Layers and continuous effects

### grixistax-05: Blood Moon strips your own utility lands; Back to Basics still locks them

**Status:** 🚩 list flag · **Evidence:** fact · **Cards:** Tevesh Szat, Doom of Fools, Blood Moon, Back to Basics, Phyrexian Tower

**Ruling.** Blood Moon makes nonbasic lands Mountains: they lose every other ability, enters-tapped clauses included. Your Phyrexian Tower stops being a sacrifice outlet, and fetchlands and Ancient Tomb stop working. They remain nonbasic (Blood Moon doesn't change supertypes or names), so Back to Basics still keeps them from untapping. That locks your own nonbasics as hard as your opponents'.

**List flag (anti-synergy).** Accepted prison cost, documented by the source for Back to Basics. The extra point here is that Blood Moon switches off the deck's own Phyrexian Tower (the Thrull mana outlet). Sequence Tower activations before Moon. No list change.

**Citations**

- Oracle, *Blood Moon*: “Nonbasic lands are Mountains.”
- Oracle, *Back to Basics*: “Nonbasic lands don't untap during their controllers' untap steps.”
- Scryfall ruling, *Blood Moon*: “This effect doesn't affect names or supertypes. It won't turn any land into a basic land or remove the legendary supertype from a legendary land, and the lands won't be named "Mountain."”
- Scryfall ruling, *Blood Moon*: “Nonbasic lands will lose any other land types and abilities they had. They will gain the land type Mountain and gain the ability "{T}: Add {R}."”
- [CR 305.7](#cr-3057), [CR 613.1d](#cr-6131d), [CR 205.4a](#cr-2054a)
- Source (re-verified): [`Grixistax_October_2026_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/grixistax_october_2026_2026-10-14/Grixistax_October_2026_Rules_Attestation.json) → “Blood Moon plus Back to Basics”

## Timing and priority

### grixistax-06: Overburden and Tangle Wire with Thrull tokens

**Status:** ✅ verified · **Cards:** Tevesh Szat, Doom of Fools, Overburden, Tangle Wire

**Ruling.** Overburden only triggers on nontoken creatures, so Thrulls are free; casting Kraum bounces one of your lands. At your upkeep, Tangle Wire's fading trigger and tap trigger are both yours to order. Resolve fading first so the tap trigger counts one fewer counter. Untapped Thrulls can be the permanents you tap.

**Citations**

- Oracle, *Overburden*: “Whenever a player puts a nontoken creature onto the battlefield, that player returns a land they control to its owner's hand.”
- Oracle, *Tangle Wire*: “At the beginning of each player's upkeep, that player taps an untapped artifact, creature, or land they control for each fade counter on this artifact.”
- [CR 603.3b](#cr-6033b), [CR 702.32a](#cr-70232a)
- Source (re-verified): [`Grixistax_October_2026_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/grixistax_october_2026_2026-10-14/Grixistax_October_2026_Rules_Attestation.json) → “Overburden and Tevesh tokens”
- Source (re-verified): [`Grixistax_October_2026_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/grixistax_october_2026_2026-10-14/Grixistax_October_2026_Rules_Attestation.json) → “Tangle Wire with Tevesh tokens”

### grixistax-07: Trinisphere and Chalice tax your own free spells

**Status:** ✅ verified · **Cards:** Tevesh Szat, Doom of Fools, Trinisphere, Chalice of the Void, Force of Will, Fierce Guardianship, Lion's Eye Diamond

**Ruling.** An untapped Trinisphere applies after alternative costs and reductions. Force of Will's pitch, a free Fierce Guardianship or Pact, and 0-cost artifacts all cost three mana. Chalice checks mana value as the spell is cast, not what was paid. At 0 it counters your Moxen, LED and Lotus Petal; at 1 it counters your Sol Ring, Vampiric Tutor and similar.

**Citations**

- Oracle, *Trinisphere*: “As long as this artifact is untapped, each spell that would cost less than three mana to cast costs three mana to cast.”
- Oracle, *Chalice of the Void*: “Whenever a player casts a spell with mana value equal to the number of charge counters on this artifact, counter that spell.”
- Scryfall ruling, *Trinisphere*: “Finally, apply Trinisphere's effect if the mana component of the spell's cost is less than three mana.”
- Scryfall ruling, *Chalice of the Void*: “If there are zero charge counters on Chalice of the Void, it counters each spell with a mana value of 0.”
- [CR 601.2f](#cr-6012f), [CR 202.3](#cr-2023)
- Source (re-verified): [`Grixistax_October_2026_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/grixistax_october_2026_2026-10-14/Grixistax_October_2026_Rules_Attestation.json) → “Trinisphere and free/alternative-cost interaction”
- Source (re-verified): [`Grixistax_October_2026_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/grixistax_october_2026_2026-10-14/Grixistax_October_2026_Rules_Attestation.json) → “Chalice of the Void sequencing”

## Replacement and prevention effects

### grixistax-04: Contamination, Damping Sphere and Blood Moon on the same land

**Status:** ✅ verified · **Cards:** Tevesh Szat, Doom of Fools, Contamination, Damping Sphere, Blood Moon, Ancient Tomb

**Ruling.** Contamination makes every land produce exactly {B}. Damping Sphere turns a land that would make two or more into {C}. When both apply to one tap, the land's controller picks which applies first, and either way Ancient Tomb gives one mana. Blood Moon makes nonbasics Mountains ({T}: Add {R}), and Contamination still turns that into {B}. Artifact mana is untouched by all three.

**Citations**

- Oracle, *Contamination*: “If a land is tapped for mana, it produces {B} instead of any other type and amount.”
- Oracle, *Damping Sphere*: “If a land is tapped for two or more mana, it produces {C} instead of any other type and amount.”
- Scryfall ruling, *Damping Sphere*: “If multiple replacement effects would modify the mana an ability you control produces, choose one to apply. After that, determine if any others are applicable.”
- Scryfall ruling, *Contamination*: “The second ability of this card is a replacement effect, not a triggered ability.”
- [CR 616.1](#cr-6161), [CR 613.1d](#cr-6131d), [CR 106.12](#cr-10612)
- Source (re-verified): [`Grixistax_October_2026_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/grixistax_october_2026_2026-10-14/Grixistax_October_2026_Rules_Attestation.json) → “Damping Sphere and Ancient Tomb”
- Source (re-verified): [`Grixistax_October_2026_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/grixistax_october_2026_2026-10-14/Grixistax_October_2026_Rules_Attestation.json) → “Contamination with Blood Moon and artifact mana”

## Zones, commander tax and the command zone

### grixistax-11: Tainted Pact as a tutor, and Tevesh's −10

**Status:** ✅ verified · **Cards:** Tevesh Szat, Doom of Fools, Tainted Pact

**Ruling.** The list has 100 distinct names, two partners included, so Tainted Pact never stops on a duplicate; it's a tutor here, since there's no Thassa's Oracle. Tevesh's −10 takes control of every commander on the battlefield first, then puts all commanders from command zones onto the battlefield under your control. If you leave the game, the ones you put onto the battlefield are exiled.

**Citations**

- Oracle, *Tevesh Szat, Doom of Fools*: “−10: Gain control of all commanders. Put all commanders from the command zone onto the battlefield under your control.”
- Scryfall ruling, *Tevesh Szat, Doom of Fools*: “As the third ability is resolving, you'll gain control of all commanders that were already on the battlefield before the commanders from the command zone enter the battlefield under your control.”
- [CR 903.3](#cr-9033), [CR 800.4a](#cr-8004a)
- Source (re-verified): [`Grixistax_October_2026_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/grixistax_october_2026_2026-10-14/Grixistax_October_2026_Rules_Attestation.json) → “Tainted Pact singleton condition”

## What the list depends on

### grixistax-10: The Breach finish needs your own prison pieces gone

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Tevesh Szat, Doom of Fools, Underworld Breach, Lion's Eye Diamond, Brain Freeze, Necropotence, Trinisphere, Damping Sphere

**Ruling.** Breach + LED + Brain Freeze needs six other cards in hand and/or graveyard. Under your own Trinisphere, every escaped LED costs three mana. Damping Sphere taxes each successive spell. Chalice on 0 counters LED, and Contamination turns lands black-only. Necropotence exiles discarded cards (LED's discard), cutting Breach fuel. Remove or sequence around these before going off.

**Citations**

- Oracle, *Necropotence*: “Whenever you discard a card, exile that card from your graveyard.”
- [CR 702.138a](#cr-702138a), [CR 601.2f](#cr-6012f)
- Commander Spellbook [1368-3518-4856](https://commanderspellbook.com/combo/1368-3518-4856/) (community-maintained, retrieved 2026-10-16): “You have at least six other cards in hand and/or graveyard.”
- Commander Spellbook [1368-3518-4856](https://commanderspellbook.com/combo/1368-3518-4856/) (community-maintained, retrieved 2026-10-16): “Cast Lion's Eye Diamond from your graveyard for its escape cost by exiling three cards besides Brain Freeze from your graveyard.”
- Source (re-verified): [`Grixistax_October_2026_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/grixistax_october_2026_2026-10-14/Grixistax_October_2026_Rules_Attestation.json) → “Underworld Breach plus Lion's Eye Diamond plus Brain Freeze”
- Source (re-verified): [`Grixistax_October_2026_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/grixistax_october_2026_2026-10-14/Grixistax_October_2026_Rules_Attestation.json) → “Necropotence with commander draw and Breach”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 106.12

To “tap [a permanent] for mana” is to activate a mana ability of that permanent that includes the {T} symbol in its activation cost. See rule 605, “Mana Abilities.”

#### CR 108.3

The owner of a card in the game is the player who started the game with it in their deck. If a card is brought into the game from outside the game rather than starting in a player’s deck, its owner is the player who brought it into the game. If a card starts the game in the command zone, its owner is the player who put it into the command zone to start the game. Legal ownership of a card in the game is irrelevant to the game rules except for the rules for ante. (See rule 407.)

#### CR 202.3

The mana value of an object is a number equal to the total amount of mana in its mana cost, regardless of color.

#### CR 205.4a

An object can have one or more supertypes. A card’s supertypes are printed directly before its card types. The supertypes are basic, legendary, ongoing, snow, and world.

#### CR 305.7

If an effect sets a land’s subtype to one or more of the basic land types, the land no longer has its old land type. It loses all abilities generated from its rules text, its old land types, and any copiable effects affecting that land, and it gains the appropriate mana ability for each new basic land type. Note that this doesn’t remove any abilities that were granted to the land by other effects. Setting a land’s subtype doesn’t add or remove any card types (such as creature) or supertypes (such as basic, legendary, and snow) the land may have. If a land gains one or more land types in …

#### CR 601.2f

The player determines the total cost of the spell. Usually this is just the mana cost. Some spells have additional or alternative costs. Some effects may increase or reduce the cost to pay, or may provide other alternative costs. Costs may include paying mana, tapping permanents, sacrificing permanents, discarding cards, and so on. The total cost is the mana cost or alternative cost (as determined in rule 601.2b), plus all additional costs and cost increases, and minus all cost reductions. If multiple cost reductions apply, the player may apply them in any order. If the mana component of the …

#### CR 602.5

A player can’t begin to activate an ability that’s prohibited from being activated.

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 603.3b

If multiple abilities have triggered since the last time a player received priority, the abilities are placed on the stack in a two-part process. First, each player, in APNAP order, puts each triggered ability they control with a trigger condition that isn’t another ability triggering on the stack in any order they choose. (See rule 101.4.) Second, each player, in APNAP order, puts all remaining triggered abilities they control on the stack in any order they choose. Then the game once again checks for and performs state-based actions until none are performed, then abilities that triggered …

#### CR 613.1d

Layer 4: Type-changing effects are applied. These include effects that change an object’s card type, subtype, and/or supertype.

#### CR 614.6

If an event is replaced, it never happens. A modified event occurs instead, which may in turn trigger abilities. Note that the modified event may contain instructions that can’t be carried out, in which case the impossible instruction is simply ignored.

#### CR 616.1

If two or more replacement and/or prevention effects are attempting to modify the way an event affects an object or player, the affected object’s controller (or its owner if it has no controller) or the affected player chooses one to apply, following the steps listed below. If two or more players have to make these choices at the same time, choices are made in APNAP order (see rule 101.4).

#### CR 701.17a

For a player to mill a number of cards, that player puts that many cards from the top of their library into their graveyard.

#### CR 701.21a

To sacrifice a permanent, its controller moves it from the battlefield directly to its owner’s graveyard. A player can’t sacrifice something that isn’t a permanent, or something that’s a permanent they don’t control. Sacrificing a permanent doesn’t destroy it, so regeneration or other effects that replace destruction can’t affect this action.

#### CR 702.32a

Fading is a keyword that represents two abilities. “Fading N” means “This permanent enters with N fade counters on it” and “At the beginning of your upkeep, remove a fade counter from this permanent. If you can’t, sacrifice the permanent.”

#### CR 702.124a

Partner abilities are keyword abilities that modify the rules for deck construction in the Commander variant (see rule 903), and they function before the game begins. Each partner ability allows you to designate two legendary cards as your commander rather than one. Each partner ability has its own requirements for those two commanders. The partner abilities are: partner, partner—[text], partner with [name], choose a Background, and Doctor’s companion.

#### CR 702.138a

Escape represents a static ability that functions while the card with escape is in a player’s graveyard. “Escape [cost]” means “You may cast this card from your graveyard by paying [cost] rather than paying its mana cost.” Casting a spell using its escape ability follows the rules for paying alternative costs in rules 601.2b and 601.2f–h.

#### CR 704.5f

If a creature has toughness 0 or less, it’s put into its owner’s graveyard. Regeneration can’t replace this event.

#### CR 800.4a

When a player leaves the game, all objects (see rule 109) owned by that player leave the game and any effects which give that player control of any objects or players end. Then, if that player controlled any objects on the stack not represented by cards, those objects cease to exist. Then, if there are any objects still controlled by that player, those objects are exiled. This is not a state-based action. It happens as soon as the player leaves the game. If the player who left the game had priority at the time they left, priority passes to the next player in turn order who’s still in the game.

#### CR 903.3

Each deck has a legendary card designated as its commander. That card must be either (a) a creature card, (b) a Vehicle card, or (c) a Spacecraft card with one or more power/toughness boxes. This designation is not a characteristic of the object represented by the card; rather, it is an attribute of the card itself. The card retains this designation even when it changes zones.

#### CR 903.4

The Commander variant uses color identity to determine what cards can be in a deck with a certain commander. The color identity of a card is the color or colors of any mana symbols in that card’s mana cost or rules text, plus any colors defined by its characteristic-defining abilities (see rule 604.3) or color indicator (see rule 204).

#### CR 903.8

A player may cast a commander they own from the command zone. A commander cast from the command zone costs an additional {2} for each previous time the player casting it has cast it from the command zone that game. This additional cost is informally known as the “commander tax.”

