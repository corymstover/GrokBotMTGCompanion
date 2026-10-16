---
title: "Mishra, Artificer Prodigy — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Mishra, Artificer Prodigy — Interaction Review

> Bot cycle 51 · batch D · reviewed 2026-10-16. Deck: [Mishra, Artificer Prodigy](../decks/mishra-artificer-prodigy.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-15), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/mishra-artificer-prodigy.txt`](../../exports/grixis-archidekt/mishra-artificer-prodigy.txt) · SHA-256 `33e1354d2064b12b56108f4cbc4b663e0d1bb51c1449d40588172a2c1a2680b7` |
| Rulings | **10** (8 verified · 0 uncertain · 2 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-15 · rulings 2026-10-15 |
| Source attestations | [`Mishra_Artificer_Prodigy_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mishra_Artificer_Prodigy_Approval_Ready_Verification_2026-10-15.md) (Approval-ready verification; rules sections 5–8 re-checked against Oracle, rulings and CR) |

## Contents
- [Summary](#summary)
- [Flags and open questions](#flags-and-open-questions)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [Timing and priority](#timing-and-priority)
- [Trigger ordering](#trigger-ordering)
- [What the list depends on](#what-the-list-depends-on)
- [Rules cited](#rules-cited)

## Summary

Mishra lets you counter your own artifact spells and still get them. The list's stax pieces (Void Mirror, Vexing Bauble, Chalice, Nether Void, Nullstone Gargoyle, Blood Funnel, Planar Chaos, Possibility Storm) counter or tuck your artifacts, and Mishra's trigger, ordered below, puts them onto the battlefield. It closes with Top loops, KCI recursion, Karn + Lattice and Lattice + Vandalblast. Twenty Spellbook lines are confirmed; representative ones are cited.

Rules surprises: in singleton Mishra finds only the spell itself; a Chalice Mishra returns comes in at X=0; Possibility Storm stops overloaded Vandalblast. Flags: your stax hits your own instants and sorceries; Void Mirror and Bauble cut off your own loops when Mishra is gone.

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [mishraap-04](#mishraap-04-your-own-stax-hits-your-non-artifact-spells-and-possibility-storm-breaks-overloaded-vandalblast) | 🚩 list flag (anti-synergy) | Your own stax hits your non-artifact spells, and Possibility Storm breaks overloaded Vandalblast | Blood Funnel, Nether Void, Nullstone Gargoyle, Planar Chaos and Possibility Storm counter or replace your own instants and sorceries (Mishra saves only artifacts), and Possibility Storm stops the Lattice + overloaded Vandalblast kill. |
| [mishraap-05](#mishraap-05-without-mishra-void-mirror-and-vexing-bauble-break-your-own-top-and-kci-loops) | 🚩 list flag (dependency-risk) | Without Mishra, Void Mirror and Vexing Bauble break your own Top and KCI loops | With Void Mirror or Vexing Bauble out, the Top/Forge/Citadel/Reality Chip and KCI loops only continue while Mishra is on the battlefield. |

## Commander rules text and edge cases

### mishraap-01: In singleton, Mishra only finds the spell itself after it's countered or moved

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mishra, Artificer Prodigy

**Ruling.** Mishra triggers when you cast an artifact spell. It looks for a card with the same name in your graveyard, hand or library. The list is singleton, so the only such card is the spell itself, and while it's on the stack Mishra finds nothing. The trigger pays off only when another trigger you control moves the spell first, by countering it into the graveyard or tucking it into the library. Put Mishra's trigger on the stack first and the counter or exile trigger on top, so that one resolves first. The trigger doesn't need the spell to resolve.

**Citations**

- Oracle, *Mishra, Artificer Prodigy*: “Whenever you cast an artifact spell, you may search your graveyard, hand, and/or library for a card with the same name as that spell and put it onto the battlefield. If you search your library this way, shuffle.”
- [CR 603.3b](#cr-6033b), [CR 405.2](#cr-4052), [CR 701.23a](#cr-70123a)
- Source (re-verified): [`Mishra_Artificer_Prodigy_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mishra_Artificer_Prodigy_Approval_Ready_Verification_2026-10-15.md) → “His trigger does not require that artifact spell to resolve.”
- Source (re-verified): [`Mishra_Artificer_Prodigy_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mishra_Artificer_Prodigy_Approval_Ready_Verification_2026-10-15.md) → “the controller may order the relevant triggers so the counter effect resolves first and Mishra's trigger resolves afterward.”

## Combos and engine lines

### mishraap-03: Possibility Storm + Void Mirror / Vexing Bauble lock; Mishra recovers the tucked artifact

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mishra, Artificer Prodigy, Possibility Storm, Void Mirror, Vexing Bauble

**Ruling.** Every spell cast from hand is exiled, and its caster may cast a random card of the same type for free. Void Mirror or Vexing Bauble then counters that free spell, because no mana was spent on it. That shuts off spells cast from hand for everyone.

You can still use Mishra. When you cast an artifact from hand, put Possibility Storm's trigger above Mishra's. Storm puts the original on the bottom of your library, then Mishra searches your library and puts it onto the battlefield. If the free replacement is also an artifact, it triggers Mishra too, and when it gets countered into the graveyard Mishra can recover it.

It's not a total lock. Spells cast from other zones (Mystic Forge, Bolas's Citadel, Emry) and spells where mana was spent on additional costs get through.

**Citations**

- Oracle, *Possibility Storm*: “Whenever a player casts a spell from their hand, that player exiles it, then exiles cards from the top of their library until they exile a card that shares a card type with it. That player may cast that card without paying its mana cost. Then they put all cards exiled with this enchantment on the bottom of their library in a random order.”
- Scryfall ruling, *Possibility Storm*: “The original spell is part of the group of exiled cards put on the bottom of the library in a random order. If the exiled card that shared a card type with that card wasn't cast, it's also part of this group.”
- [CR 603.3b](#cr-6033b), [CR 601.2f](#cr-6012f)
- Commander Spellbook [507-3741](https://commanderspellbook.com/combo/507-3741/) (community-maintained, retrieved 2026-10-16): “If the player chooses to cast the spell, Void Mirror triggers, countering that spell since no colored mana was spent to cast it.”
- Commander Spellbook [507-6614](https://commanderspellbook.com/combo/507-6614/) (community-maintained, retrieved 2026-10-16): “If the player chooses to cast the spell, Vexing Bauble triggers, countering that spell since no colored mana was spent to cast it.”
- Source (re-verified): [`Mishra_Artificer_Prodigy_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mishra_Artificer_Prodigy_Approval_Ready_Verification_2026-10-15.md) → “Mishra's original trigger resolves afterward and can find the original named artifact card now in the library and put it directly onto the battlefield.”

### mishraap-07: Karn + Mycosynth Lattice lock; Lattice + overloaded Vandalblast

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mishra, Artificer Prodigy, Karn, the Great Creator, Mycosynth Lattice, Vandalblast, Encroaching Mycosynth

**Ruling.** Lattice makes every permanent an artifact, so Karn's static stops opponents from activating any ability of their permanents, including land mana abilities. Your own permanents aren't affected. Overloaded Vandalblast with Lattice out destroys every permanent you don't control. Lattice doesn't make spells artifacts, so it doesn't add Mishra triggers. Encroaching Mycosynth does: your nonland permanent spells and cards become artifacts, so creature spells trigger Mishra too. Karn's −2 for a card from outside the game isn't relied on.

**Citations**

- Oracle, *Karn, the Great Creator*: “Activated abilities of artifacts your opponents control can't be activated.”
- Oracle, *Mycosynth Lattice*: “All permanents are artifacts in addition to their other types.”
- Scryfall ruling, *Mycosynth Lattice*: “Mycosynth Lattice turns all permanents on the battlefield into artifacts. Spells on the stack and cards in other zones aren’t permanents, so those spells and cards don’t become artifacts.”
- Scryfall ruling, *Encroaching Mycosynth*: “Encroaching Mycosynth turns all permanents you control into artifacts. Permanent spells you control become artifact spells in addition to their other types, and nonland permanent cards you own in other zones become artifact cards in addition to their other types.”
- [CR 101.2](#cr-1012), [CR 702.96a](#cr-70296a)
- Commander Spellbook [3263-5089](https://commanderspellbook.com/combo/3263-5089/) (community-maintained, retrieved 2026-10-16): “Mycosynth Lattice turns all permanents into artifacts.”
- Commander Spellbook [2552-3263](https://commanderspellbook.com/combo/2552-3263/) (community-maintained, retrieved 2026-10-16): “Cast Vandalblast for its overload cost, paying {5} to destroy all permanents opponents control.”
- Source (re-verified): [`Mishra_Artificer_Prodigy_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mishra_Artificer_Prodigy_Approval_Ready_Verification_2026-10-15.md) → “Karn prevents opponents from activating abilities of artifacts, including mana abilities of their lands.”

### mishraap-08: Top loops: Forge or Reality Chip + {1} reducer; Citadel + Aetherflux

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mishra, Artificer Prodigy, Sensei's Divining Top, Mystic Forge, The Reality Chip, Bolas's Citadel, Aetherflux Reservoir, Foundry Inspector, Etherium Sculptor, Cloud Key, Enthusiastic Mechanaut

**Ruling.** Tap Top to draw and put it on top of your library. Then cast it again from the library: with Mystic Forge, or Reality Chip attached to a creature, and a {1} reducer, it costs {0}. With Bolas's Citadel it costs 1 life, and Aetherflux Reservoir gains more each cast. The recast Top is a new untapped object. Each cast also triggers Jhoira, and Uthros at 3+. See mishraap-05 for Void Mirror and Vexing Bauble.

**Citations**

- Oracle, *The Reality Chip*: “As long as The Reality Chip is attached to a creature, you may play lands and cast spells from the top of your library.”
- Oracle, *Mystic Forge*: “You may cast artifact spells and colorless spells from the top of your library.”
- [CR 400.7](#cr-4007), [CR 601.2f](#cr-6012f)
- Commander Spellbook [1976-5078-5243](https://commanderspellbook.com/combo/1976-5078-5243/) (community-maintained, retrieved 2026-10-16): “Activate Sensei's Divining Top by tapping it, causing you to draw a card and put Sensei's Divining Top on top of your library.”
- Commander Spellbook [2173-4740-5078](https://commanderspellbook.com/combo/2173-4740-5078/) (community-maintained, retrieved 2026-10-16): “Aetherflux Reservoir triggers, gaining you 1 life for each spell you have cast this turn.”
- Source (re-verified): [`Mishra_Artificer_Prodigy_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mishra_Artificer_Prodigy_Approval_Ready_Verification_2026-10-15.md) → “Mystic Forge + Sensei's Divining Top + an artifact cost reducer + Aetherflux Reservoir.”

### mishraap-09: KCI + Scrap Trawler + Myr Retriever (+ reducer / Junk Diver + Sol Ring); Emry + The One Ring

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mishra, Artificer Prodigy, Krark-Clan Ironworks, Scrap Trawler, Myr Retriever, Junk Diver, Sol Ring, Emry, Lurker of the Loch, The One Ring

**Ruling.** Sacrifice Myr Retriever to KCI. It returns Scrap Trawler to your hand, and Trawler returns the lower-mana-value piece when it dies, so the pieces cycle through your hand. Recasting them is mana-neutral with one {1} reducer. The Junk Diver + Sol Ring version makes infinite colorless mana with no reducer. Each recast is an artifact spell, so Aetherflux, Jhoira and Uthros trigger.

With Emry, sacrifice The One Ring to KCI and recast it from your graveyard each turn. Ring's protection needs it to be cast, so the Emry line gives protection from everything every turn.

**Citations**

- Oracle, *Scrap Trawler*: “Whenever this creature dies or another artifact you control is put into a graveyard from the battlefield, return to your hand target artifact card in your graveyard with lesser mana value.”
- Oracle, *The One Ring*: “When The One Ring enters, if you cast it, you gain protection from everything until your next turn.”
- [CR 603.10a](#cr-60310a), [CR 601.2f](#cr-6012f)
- Commander Spellbook [777-1020-2866-4659](https://commanderspellbook.com/combo/777-1020-2866-4659/) (community-maintained, retrieved 2026-10-16): “When Myr Retriever dies, it triggers, returning Scrap Trawler from your graveyard to your hand.”
- Commander Spellbook [1329-3363-4659](https://commanderspellbook.com/combo/1329-3363-4659/) (community-maintained, retrieved 2026-10-16): “Activate Emry by tapping it, allowing you to cast The One Ring from your graveyard this turn.”
- Source (re-verified): [`Mishra_Artificer_Prodigy_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mishra_Artificer_Prodigy_Approval_Ready_Verification_2026-10-15.md) → “Krark-Clan Ironworks + Scrap Trawler + Myr Retriever / Junk Diver recursion structures”

## Engines and payoffs

### mishraap-02: Self-counters as parity breakers: Blood Funnel, Nether Void, Nullstone Gargoyle, Chalice, Void Mirror, Vexing Bauble, Planar Chaos

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mishra, Artificer Prodigy, Blood Funnel, Nether Void, Nullstone Gargoyle, Chalice of the Void, Void Mirror, Vexing Bauble, Planar Chaos

**Ruling.** Each of these can counter your own artifact spell before Mishra's trigger resolves, and then Mishra puts the card onto the battlefield from your graveyard:
- **Blood Funnel:** decline the sacrifice. The artifact still got its {2} discount.
- **Nether Void:** decline the {3}.
- **Nullstone Gargoyle:** your first noncreature spell of the turn.
- **Chalice:** mana value equal to its counters.
- **Void Mirror:** no colored mana spent.
- **Vexing Bauble:** no mana spent.
- **Planar Chaos:** a lost coin flip.

A countered artifact ends up on the battlefield anyway. Opponents have no Mishra, so their spells just stay countered.

**Citations**

- Oracle, *Blood Funnel*: “Whenever you cast a noncreature spell, counter that spell unless you sacrifice a creature.”
- Oracle, *Void Mirror*: “Whenever a player casts a spell, if no colored mana was spent to cast it, counter that spell.”
- Oracle, *Vexing Bauble*: “Whenever a player casts a spell, if no mana was spent to cast it, counter that spell.”
- Scryfall ruling, *Vexing Bauble*: “Players may cast spells that they know Vexing Bauble will counter. Any abilities that trigger when spells are cast will still trigger and resolve if appropriate, and any effects that count how many spells are cast will still count those spells if appropriate.”
- [CR 603.3b](#cr-6033b), [CR 701.6a](#cr-7016a)
- Source (re-verified): [`Mishra_Artificer_Prodigy_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mishra_Artificer_Prodigy_Approval_Ready_Verification_2026-10-15.md) → “a noncreature artifact spell can be countered when its controller declines/fails the sacrifice”

## Timing and priority

### mishraap-06: Chalice of the Void returned by Mishra has X = 0

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mishra, Artificer Prodigy, Chalice of the Void

**Ruling.** If Mishra puts a countered Chalice onto the battlefield from your graveyard, it wasn't cast, so X is 0 and it enters with no charge counters. A Chalice on 0 counters every mana value 0 spell, including your own Moxen (Chrome, Diamond, Opal, Amber) and Lotus-style rocks. Mishra's search is optional, so decline it unless you want Chalice on 0.

**Citations**

- Oracle, *Chalice of the Void*: “This artifact enters with X charge counters on it.”
- Scryfall ruling, *Chalice of the Void*: “If there are zero charge counters on Chalice of the Void, it counters each spell with a mana value of 0. This includes face-down creature spells cast with morph's alternative cost.”
- [CR 107.3g](#cr-1073g), [CR 107.3m](#cr-1073m)

## Trigger ordering

### mishraap-10: Uthros Research Craft: Mishra stations 4; draw resolves first, even if the artifact is countered

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Mishra, Artificer Prodigy, Uthros Research Craft

**Ruling.** Station by tapping Mishra (power 4, sorcery speed). That's 4 charge counters, past the 3+ threshold in one go. After that, every artifact spell you cast draws a card. The draw resolves before the spell, so it still happens when your own Void Mirror or Bauble counters it on the way to Mishra.

**Citations**

- Oracle, *Uthros Research Craft*: “3+ | Whenever you cast an artifact spell, draw a card. Put a charge counter on this Spacecraft.”
- Scryfall ruling, *Uthros Research Craft*: “The triggered ability granted by Uthros Research Craft’s second ability resolves before the spell that caused it to trigger. It resolves even if that spell is countered or otherwise leaves the stack without resolving.”
- [CR 702.184a](#cr-702184a), [CR 721.2](#cr-7212)
- Source (re-verified): [`Mishra_Artificer_Prodigy_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mishra_Artificer_Prodigy_Approval_Ready_Verification_2026-10-15.md) → “The draw trigger is independent of whether the artifact spell later resolves or is countered.”

## What the list depends on

### mishraap-04: Your own stax hits your non-artifact spells, and Possibility Storm breaks overloaded Vandalblast

**Status:** 🚩 list flag · **Evidence:** fact · **Cards:** Mishra, Artificer Prodigy, Blood Funnel, Nether Void, Nullstone Gargoyle, Planar Chaos, Possibility Storm, Vandalblast, Mycosynth Lattice, Force of Will, Demonic Tutor, Cyclonic Rift

**Ruling.** Mishra rescues only artifacts. Your instants and sorceries (Force of Will, Mana Drain, Demonic Tutor, Toxic Deluge, Cyclonic Rift, Swan Song) face your own taxes:
- **Blood Funnel:** sacrifice a creature or the spell is countered.
- **Nether Void:** pay {3} or it's countered.
- **Nullstone Gargoyle:** your first noncreature spell each turn is countered.
- **Planar Chaos:** each spell has a 50% chance to be countered.
- **Possibility Storm:** each spell from hand becomes a random one of the same type.

Overloaded Vandalblast is half of the Mycosynth Lattice line. With Possibility Storm out, Vandalblast from hand gets exiled, and a free sorcery can't be cast for its overload cost. Have these pieces off the table, or Mishra plus enough mana ready, before you cast key non-artifact spells.

**List flag (anti-synergy).** Blood Funnel, Nether Void, Nullstone Gargoyle, Planar Chaos and Possibility Storm counter or replace your own instants and sorceries (Mishra saves only artifacts), and Possibility Storm stops the Lattice + overloaded Vandalblast kill.

**Citations**

- Oracle, *Nether Void*: “Whenever a player casts a spell, counter it unless that player pays {3}.”
- Oracle, *Nullstone Gargoyle*: “Whenever the first noncreature spell of a turn is cast, counter that spell.”
- Scryfall ruling, *Possibility Storm*: “If you cast a spell without paying its mana cost, you can't choose to cast it for any alternative costs, such as overload costs. You can pay additional costs, such as kicker costs. If the spell has any mandatory additional costs, you must pay those.”
- [CR 118.9a](#cr-1189a), [CR 702.96a](#cr-70296a)
- Source (re-verified): [`Mishra_Artificer_Prodigy_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mishra_Artificer_Prodigy_Approval_Ready_Verification_2026-10-15.md) → “Additional costs paid with mana, uncounterable effects, trigger interaction, and spells not cast from hand can change the outcome.”

### mishraap-05: Without Mishra, Void Mirror and Vexing Bauble break your own Top and KCI loops

**Status:** 🚩 list flag · **Evidence:** fact · **Cards:** Mishra, Artificer Prodigy, Sensei's Divining Top, Mystic Forge, Bolas's Citadel, The Reality Chip, Krark-Clan Ironworks, Void Mirror, Vexing Bauble, Foundry Inspector, Etherium Sculptor, Cloud Key, Enthusiastic Mechanaut

**Ruling.** Your Top loops cast Sensei's Divining Top for {0} (Forge or Reality Chip plus a {1} reducer) or for 1 life (Citadel). No mana is spent, so Vexing Bauble and Void Mirror counter it. KCI recasts paid only with colorless mana get hit by Void Mirror too. With Mishra out, each countered Top or loop piece goes from the graveyard to the battlefield. Mishra's trigger is ordered below the counter, so the loop keeps going, and cast triggers (Aetherflux, Jhoira, Uthros) still count each cast. Without Mishra, the loop stops at the first counter.

**List flag (dependency-risk).** With Void Mirror or Vexing Bauble out, the Top/Forge/Citadel/Reality Chip and KCI loops only continue while Mishra is on the battlefield.

**Citations**

- Oracle, *Sensei's Divining Top*: “{T}: Draw a card, then put this artifact on top of its owner's library.”
- Oracle, *Bolas's Citadel*: “If you cast a spell this way, pay life equal to its mana value rather than pay its mana cost.”
- Scryfall ruling, *Vexing Bauble*: “If a spell is cast with an alternative cost that includes mana (such as flashback), Vexing Bauble's first ability won't trigger and won't counter that spell. Similarly, if a spell is cast without paying its mana cost, but the player did pay mana for additional costs such as from kicker or from Thorn of Amethyst, Vexing Bauble's first ability won't trigger and won't counter that spell.”
- [CR 603.3b](#cr-6033b), [CR 601.2f](#cr-6012f)
- Commander Spellbook [777-985-5078](https://commanderspellbook.com/combo/777-985-5078/) (community-maintained, retrieved 2026-10-16): “Cast Sensei's Divining Top from the top of your library by paying {0}.”
- Commander Spellbook [2173-4740-5078](https://commanderspellbook.com/combo/2173-4740-5078/) (community-maintained, retrieved 2026-10-16): “Cast Sensei's Divining Top from the top of your library by paying 1 life.”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 101.2

When a rule or effect allows or directs something to happen, and another effect states that it can’t happen, the “can’t” effect takes precedence.

#### CR 107.3g

If a card in any zone other than the stack has an {X} in its mana cost, the value of {X} is treated as 0, even if the value of X is defined somewhere within its text.

#### CR 107.3m

If an object’s enters-the-battlefield triggered ability or replacement effect refers to X, and the spell that became that object as it resolved had a value of X chosen for any of its costs, the value of X for that ability is the same as the value of X for that spell, although the value of X for that permanent is 0. This is an exception to rule 107.3i.

#### CR 118.9a

Only one alternative cost can be applied to any one spell as it’s being cast. The controller of the spell announces their intentions to pay that cost as described in rule 601.2b.

#### CR 400.7

An object that moves from one zone to another becomes a new object with no memory of, or relation to, its previous existence. This rule has the following exceptions.

#### CR 405.2

The stack keeps track of the order that spells and/or abilities were added to it. Each time an object is put on the stack, it’s put on top of all objects already there.

#### CR 601.2f

The player determines the total cost of the spell. Usually this is just the mana cost. Some spells have additional or alternative costs. Some effects may increase or reduce the cost to pay, or may provide other alternative costs. Costs may include paying mana, tapping permanents, sacrificing permanents, discarding cards, and so on. The total cost is the mana cost or alternative cost (as determined in rule 601.2b), plus all additional costs and cost increases, and minus all cost reductions. If multiple cost reductions apply, the player may apply them in any order. If the mana component of the …

#### CR 603.3b

If multiple abilities have triggered since the last time a player received priority, the abilities are placed on the stack in a two-part process. First, each player, in APNAP order, puts each triggered ability they control with a trigger condition that isn’t another ability triggering on the stack in any order they choose. (See rule 101.4.) Second, each player, in APNAP order, puts all remaining triggered abilities they control on the stack in any order they choose. Then the game once again checks for and performs state-based actions until none are performed, then abilities that triggered …

#### CR 603.10a

Some zone-change triggers look back in time. These are leaves-the-battlefield abilities, abilities that trigger when a player sacrifices a permanent, abilities that trigger when a card leaves a graveyard, and abilities that trigger when an object that all players can see is put into a hand or library.

#### CR 701.6a

To counter a spell or ability means to cancel it, removing it from the stack. It doesn’t resolve and none of its effects occur. A countered spell is put into its owner’s graveyard.

#### CR 701.23a

To search for a card in a zone, look at all cards in that zone (even if it’s a hidden zone) and find a card that matches the given description.

#### CR 702.96a

Overload is a keyword that represents two static abilities that function while the spell with overload is on the stack. Overload [cost] means “You may choose to pay [cost] rather than pay this spell’s mana cost” and “If you chose to pay this spell’s overload cost, change its text by replacing all instances of the word ‘target’ with the word ‘each.’” Casting a spell using its overload ability follows the rules for paying alternative costs in rules 601.2b and 601.2f–h.

#### CR 702.184a

Station is an activated ability. “Station” means “Tap another untapped creature you control: Put a number of charge counters on this permanent equal to the tapped creature’s power. Activate only as a sorcery.”

#### CR 721.2

A station symbol represents a static ability. The station symbol includes a single number followed by a plus sign, indicated here as “{N+}.” Any abilities printed within the same text box striation as a station symbol are part of its static ability. The same is true of any power and toughness boxes printed within that striation, indicated here as [P/T].

