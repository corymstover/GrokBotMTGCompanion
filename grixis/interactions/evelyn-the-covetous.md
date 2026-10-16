---
title: "Evelyn, the Covetous — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Evelyn, the Covetous — Interaction Review

> Bot cycle 48 · batch B · reviewed 2026-10-16. Deck: [Evelyn, the Covetous](../decks/evelyn-the-covetous.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-15), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/evelyn-the-covetous.txt`](../../exports/grixis-archidekt/evelyn-the-covetous.txt) · SHA-256 `e230c85b8254f533b0a8d6e2e5699e9eac000010f594a822892c3d74cd76390f` |
| Rulings | **10** (7 verified · 1 uncertain · 2 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-15 · rulings 2026-10-15 |
| Source attestations | [`Evelyn_the_Covetous_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/evelyn_the_covetous_2026-10-14/Evelyn_the_Covetous_Rules_Attestation.json) (13 interactions, all PASS) |

## Contents
- [Summary](#summary)
- [Flags and open questions](#flags-and-open-questions)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Key card-pair interactions](#key-card-pair-interactions)
- [Timing and priority](#timing-and-priority)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [What the list depends on](#what-the-list-depends-on)
- [Rules cited](#rules-cited)

## Summary

Evelyn, the Covetous exiles the top card of each library whenever a Vampire enters, and lets you play one such card each turn. The list is a cEDH-style Grixis shell with Worldgorger Dragon, Thassa's Oracle and Underworld Breach lines. This review re-verifies the thirteen items of the deck's rules attestation, and confirms six combo lines against cached Commander Spellbook steps.

Rules surprises:
- Vexing Bauble counters escaped LED and Lotus Petal casts.
- The source's Saw in Half caveat uses the pre-2020 commander rule; Evelyn always dies (documentation flag).

No list errors.

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [evelyn-05](#evelyn-05-worldgorger--evelyn--thassas-oracle) | ⚠️ uncertain | Worldgorger + Evelyn → Thassa's Oracle | Rebuilt from the source attestation. Spellbook's cached Worldgorger variants confirm the mana loop, but not the Evelyn-to-Oracle endpoint, which is checked only against Oracle and CR. |
| [evelyn-08](#evelyn-08-vexing-bauble-counters-your-own-free-spells-including-escaped-led-and-petal) | 🚩 list flag (anti-synergy) | Vexing Bauble counters your own free spells, including escaped LED and Petal | Known and accepted by the source; the specific casualty is the Breach + LED/Petal escape loop, which spends no mana on the artifact. Pilot note: sacrifice Vexing Bauble before going off. No list change. |
| [evelyn-09](#evelyn-09-saw-in-half-on-evelyn-the-commander-rule-no-longer-prevents-dying) | 🚩 list flag (documentation) | Saw in Half on Evelyn: the commander rule no longer prevents dying | The source attestation's caveat ('If the commander replacement effect moves Evelyn directly to the command zone instead of the graveyard … no copies are created') describes the pre-2020 rule. Under current CR 903.9a the graveyard/exile move is a state-based action after the fact, so Evelyn always dies. No list change; the rest of the source item (four triggers, legend rule) is correct. |

## Commander rules text and edge cases

### evelyn-01: One play per turn, from any Evelyn's exile

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Evelyn, the Covetous

**Ruling.** Evelyn exiles the top card of each library, yours included, with a collection counter, whenever she or another Vampire enters. Once each turn you may play one of those cards, if an ability you controlled exiled it; you may spend mana as though it were any color. The permission isn't tied to the Evelyn that exiled the card, so a new Evelyn (after a blink or recast) can play cards an earlier one exiled. It's once each turn, not once on your turn, so with flash timing you get a play on each opponent's turn too.

**Citations**

- Oracle, *Evelyn, the Covetous*: “Whenever Evelyn or another Vampire you control enters, exile the top card of each player's library with a collection counter on it.”
- Oracle, *Evelyn, the Covetous*: “Once each turn, you may play a card from exile with a collection counter on it if it was exiled by an ability you controlled, and you may spend mana as though it were mana of any color to cast it.”
- [CR 400.7](#cr-4007), [CR 601.3](#cr-6013)
- Source (re-verified): [`Evelyn_the_Covetous_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/evelyn_the_covetous_2026-10-14/Evelyn_the_Covetous_Rules_Attestation.json) → “Evelyn collection-counter permission across Evelyn objects”

## Combos and engine lines

### evelyn-03: Worldgorger Dragon + Animate Dead / Dance of the Dead / Necromancy

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Evelyn, the Covetous, Worldgorger Dragon, Animate Dead, Dance of the Dead, Necromancy

**Ruling.** Reanimate Worldgorger with one of the three Auras. Its enters trigger exiles all your other permanents, including the Aura. The Aura leaving makes you sacrifice the Dragon, whose leaves trigger returns everything, and the returning Aura reanimates the Dragon again. Tap your lands for mana each iteration while holding priority: unbounded mana of any colors your lands make.

**Citations**

- Oracle, *Worldgorger Dragon*: “When this creature enters, exile all other permanents you control.”
- Oracle, *Worldgorger Dragon*: “When this creature leaves the battlefield, return the exiled cards to the battlefield under their owners' control.”
- [CR 603.6c](#cr-6036c), [CR 603.10a](#cr-60310a), [CR 303.4a](#cr-3034a)
- Commander Spellbook [4812-4846](https://commanderspellbook.com/combo/4812-4846/) (community-maintained, retrieved 2026-10-16): “Worldgorger Dragon enters the battlefield, exiling all other permanents you control.”
- Commander Spellbook [4812-4846](https://commanderspellbook.com/combo/4812-4846/) (community-maintained, retrieved 2026-10-16): “Holding priority, activate all lands you control by tapping those, adding manas of any colors those lands can produce.”
- Commander Spellbook [3605-4846](https://commanderspellbook.com/combo/3605-4846/) (community-maintained, retrieved 2026-10-16): “Dance of the Dead triggers, sacrificing Worldgorger Dragon.”
- Commander Spellbook [2896-4846](https://commanderspellbook.com/combo/2896-4846/) (community-maintained, retrieved 2026-10-16): “Cast Necromancy by paying {2}{B}.”
- Source (re-verified): [`Evelyn_the_Covetous_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/evelyn_the_covetous_2026-10-14/Evelyn_the_Covetous_Rules_Attestation.json) → “Worldgorger reanimation loop”

### evelyn-05: Worldgorger + Evelyn → Thassa's Oracle

**Status:** ⚠️ uncertain · **Evidence:** hypothesis · **Cards:** Evelyn, the Covetous, Worldgorger Dragon, Thassa's Oracle

**Ruling.** Evelyn is one of the permanents exiled and returned every iteration. Each return is a new Evelyn entering, so she exiles the top card of each library each loop. Loop until your library is exiled, break safely, then use the turn's Evelyn play to cast Thassa's Oracle from exile with any-color mana. With an empty library Oracle wins. This needs the Evelyn play unused that turn.

**Uncertain.** Rebuilt from the source attestation. Spellbook's cached Worldgorger variants confirm the mana loop, but not the Evelyn-to-Oracle endpoint, which is checked only against Oracle and CR.

**Citations**

- Oracle, *Thassa's Oracle*: “If X is greater than or equal to the number of cards in your library, you win the game.”
- Scryfall ruling, *Thassa's Oracle*: “If you have no cards in your library, you win the game.”
- [CR 400.7](#cr-4007), [CR 603.6a](#cr-6036a)
- Source (re-verified): [`Evelyn_the_Covetous_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/evelyn_the_covetous_2026-10-14/Evelyn_the_Covetous_Rules_Attestation.json) → “Worldgorger plus Evelyn repeated ETBs”
- Source (re-verified): [`Evelyn_the_Covetous_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/evelyn_the_covetous_2026-10-14/Evelyn_the_Covetous_Rules_Attestation.json) → “Worldgorger Evelyn endpoint with Thassa's Oracle”

### evelyn-06: Thassa's Oracle + Demonic Consultation or Tainted Pact

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Evelyn, the Covetous, Thassa's Oracle, Demonic Consultation, Tainted Pact

**Ruling.** Demonic Consultation naming Oracle (with Oracle not in the library) exiles your whole library. Tainted Pact exiles card by card and stops at a duplicate name; this list is 100 distinct names (one Island, one Swamp), so it exiles everything you don't take. Then cast Oracle (or have it on the stack with the tutor in response). Exiling the library isn't a loss until you draw.

**Citations**

- Oracle, *Tainted Pact*: “Repeat this process until you put a card into your hand or you exile two cards with the same name, whichever comes first.”
- Scryfall ruling, *Demonic Consultation*: “You don't lose the game at that point, but will lose the next time you're instructed to draw a card.”
- [CR 121.4](#cr-1214), [CR 608.2](#cr-6082)
- Commander Spellbook [742-1295](https://commanderspellbook.com/combo/742-1295/) (community-maintained, retrieved 2026-10-16): “Cast Demonic Consultation by paying {B}, naming Thassa's Oracle and thus exiling your library due to you not having a card named Thassa's Oracle in your library.”
- Commander Spellbook [1295-3093](https://commanderspellbook.com/combo/1295-3093/) (community-maintained, retrieved 2026-10-16): “No two cards in library share a name.”
- Source (re-verified): [`Evelyn_the_Covetous_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/evelyn_the_covetous_2026-10-14/Evelyn_the_Covetous_Rules_Attestation.json) → “Thassa's Oracle plus Demonic Consultation”
- Source (re-verified): [`Evelyn_the_Covetous_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/evelyn_the_covetous_2026-10-14/Evelyn_the_Covetous_Rules_Attestation.json) → “Thassa's Oracle plus Tainted Pact”

### evelyn-07: Underworld Breach + Lion's Eye Diamond / Lotus Petal + Brain Freeze

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Evelyn, the Covetous, Underworld Breach, Lion's Eye Diamond, Lotus Petal, Brain Freeze

**Ruling.** With Breach, LED escapes for {0} plus exiling three cards and nets {U}{U}{U}. Each escaped Brain Freeze gets a bigger storm count, milling you for more fuel. Spellbook's LED line needs at least six other cards in hand and/or graveyard to start; the Lotus Petal version needs six (ten if Brain Freeze is in the graveyard). It's not a combo from an empty graveyard.

**Citations**

- Oracle, *Underworld Breach*: “Each nonland card in your graveyard has escape.”
- [CR 702.138a](#cr-702138a), [CR 702.40a](#cr-70240a)
- Commander Spellbook [1368-3518-4856](https://commanderspellbook.com/combo/1368-3518-4856/) (community-maintained, retrieved 2026-10-16): “You have at least six other cards in hand and/or graveyard.”
- Commander Spellbook [1368-3518-4856](https://commanderspellbook.com/combo/1368-3518-4856/) (community-maintained, retrieved 2026-10-16): “Activate Lion's Eye Diamond by discarding your hand and sacrificing it, adding {U}{U}{U}.”
- Commander Spellbook [1368-1414-4856](https://commanderspellbook.com/combo/1368-1414-4856/) (community-maintained, retrieved 2026-10-16): “You have at least six other cards in your graveyard, plus an additional four cards if Brain Freeze is in your graveyard.”
- Source (re-verified): [`Evelyn_the_Covetous_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/evelyn_the_covetous_2026-10-14/Evelyn_the_Covetous_Rules_Attestation.json) → “Underworld Breach plus Lion's Eye Diamond plus Brain Freeze”

## Key card-pair interactions

### evelyn-08: Vexing Bauble counters your own free spells, including escaped LED and Petal

**Status:** 🚩 list flag · **Evidence:** fact · **Cards:** Evelyn, the Covetous, Vexing Bauble, Lion's Eye Diamond, Lotus Petal, Force of Will, Pact of Negation, Underworld Breach

**Ruling.** Vexing Bauble counters any spell cast with no mana spent, yours included: Force of Will's pitch, Pact of Negation, Lotus Petal, LED, and escape casts of LED or Petal through Breach (their escape cost is all exiling, no mana). It doesn't counter a spell where mana was spent on any part of the cost. Sacrifice the Bauble ({1}, tap: draw) before the Breach turn.

**List flag (anti-synergy).** Known and accepted by the source; the specific casualty is the Breach + LED/Petal escape loop, which spends no mana on the artifact. Pilot note: sacrifice Vexing Bauble before going off. No list change.

**Citations**

- Oracle, *Vexing Bauble*: “Whenever a player casts a spell, if no mana was spent to cast it, counter that spell.”
- Scryfall ruling, *Vexing Bauble*: “If a spell is cast with an alternative cost that includes mana (such as flashback), Vexing Bauble's first ability won't trigger and won't counter that spell.”
- [CR 601.2h](#cr-6012h), [CR 702.138a](#cr-702138a)
- Source (re-verified): [`Evelyn_the_Covetous_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/evelyn_the_covetous_2026-10-14/Evelyn_the_Covetous_Rules_Attestation.json) → “Vexing Bauble symmetry”

### evelyn-10: Party Thrasher gives Evelyn casts convoke

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Evelyn, the Covetous, Party Thrasher

**Ruling.** Noncreature spells you cast from exile have convoke, so a noncreature card from Evelyn's exile can be paid partly by tapping creatures. Convoke applies after the total cost is set and doesn't change mana value. If you sacrifice Party Thrasher while casting the spell, it loses convoke.

**Citations**

- Oracle, *Party Thrasher*: “Noncreature spells you cast from exile have convoke.”
- Scryfall ruling, *Party Thrasher*: “If you sacrifice Party Thrasher while casting a noncreature spell from exile (to activate a mana ability, for example), the spell won't have convoke when you pay its costs unless it has convoke some other way.”
- [CR 702.51a](#cr-70251a)
- Source (re-verified): [`Evelyn_the_Covetous_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/evelyn_the_covetous_2026-10-14/Evelyn_the_Covetous_Rules_Attestation.json) → “Party Thrasher with Evelyn exile casting”

## Timing and priority

### evelyn-02: Flash enablers use Evelyn on opponents' turns

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Evelyn, the Covetous, Leyline of Anticipation, Borne Upon a Wind, Valley Floodcaller

**Ruling.** Leyline of Anticipation (all spells) and Borne Upon a Wind (all spells, this turn) let you cast an exiled sorcery-speed spell on an opponent's turn, using that turn's Evelyn play. Valley Floodcaller only covers noncreature spells, in any zone. None of them change sorcery-speed activated abilities, and lands still can only be played on your own turn.

**Citations**

- Oracle, *Leyline of Anticipation*: “You may cast spells as though they had flash.”
- Oracle, *Valley Floodcaller*: “You may cast noncreature spells as though they had flash.”
- Scryfall ruling, *Valley Floodcaller*: “Valley Floodcaller’s second ability applies to noncreature cards in any zone, provided something is allowing you to cast them.”
- Scryfall ruling, *Borne Upon a Wind*: “This applies only to casting spells. It does not, for example, change when you can activate abilities that can be activated "only as a sorcery."”
- [CR 307.1](#cr-3071), [CR 305.3](#cr-3053), [CR 702.8a](#cr-7028a)
- Source (re-verified): [`Evelyn_the_Covetous_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/evelyn_the_covetous_2026-10-14/Evelyn_the_Covetous_Rules_Attestation.json) → “Leyline of Anticipation with Evelyn once-each-turn permission”
- Source (re-verified): [`Evelyn_the_Covetous_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/evelyn_the_covetous_2026-10-14/Evelyn_the_Covetous_Rules_Attestation.json) → “Borne Upon a Wind and Valley Floodcaller timing”

## Zones, commander tax and the command zone

### evelyn-09: Saw in Half on Evelyn: the commander rule no longer prevents dying

**Status:** 🚩 list flag · **Evidence:** fact · **Cards:** Evelyn, the Covetous, Saw in Half

**Ruling.** Saw in Half on Evelyn: she's destroyed and goes to the graveyard, so she dies. Only after that can you move her to the command zone, as a state-based action. Since the 2020 commander-zone change this is no longer a replacement for graveyard or exile, only for hand or library. So the copies are always created. The two legendary Evelyn tokens trigger four times (each sees itself and the other Vampire), then the legend rule removes one; the four triggers still resolve.

**List flag (documentation).** The source attestation's caveat ('If the commander replacement effect moves Evelyn directly to the command zone instead of the graveyard … no copies are created') describes the pre-2020 rule. Under current CR 903.9a the graveyard/exile move is a state-based action after the fact, so Evelyn always dies. No list change; the rest of the source item (four triggers, legend rule) is correct.

**Citations**

- Oracle, *Saw in Half*: “If that creature dies this way, its controller creates two tokens that are copies of that creature”
- Scryfall ruling, *Saw in Half*: “Any enters-the-battlefield abilities of the copied creature will trigger when the tokens enter the battlefield.”
- [CR 903.9a](#cr-9039a), [CR 903.9b](#cr-9039b), [CR 704.5j](#cr-7045j), [CR 603.10a](#cr-60310a)
- Source (re-verified): [`Evelyn_the_Covetous_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/evelyn_the_covetous_2026-10-14/Evelyn_the_Covetous_Rules_Attestation.json) → “Saw in Half plus Evelyn”

## What the list depends on

### evelyn-04: The Worldgorger loop is mandatory: have a way out

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Evelyn, the Covetous, Worldgorger Dragon, Animate Dead

**Ruling.** Every step of the loop is mandatory. If nothing can stop it, the game is a draw. The returning Aura doesn't target: whoever controls it picks any creature card in any graveyard to enchant, opponents' included. So any other creature card in any graveyard breaks the loop. Getting the Dragon off the battlefield in response to its enters trigger also ends the loop, but its leaves trigger then returns nothing and your other permanents stay exiled for good. Check for an exit before you start.

**Citations**

- Scryfall ruling, *Worldgorger Dragon*: “If an Aura is exiled with Worldgorger Dragon and then returns to the battlefield, the player who controls the Aura as it enters the battlefield chooses what it will enchant.”
- Scryfall ruling, *Worldgorger Dragon*: “If Worldgorger Dragon leaves the battlefield before its enters-the-battlefield ability resolves, the "leaves-the-battlefield" ability will trigger and resolve first.”
- [CR 104.4b](#cr-1044b), [CR 303.4f](#cr-3034f)
- Source (re-verified): [`Evelyn_the_Covetous_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/evelyn_the_covetous_2026-10-14/Evelyn_the_Covetous_Rules_Attestation.json) → “Mandatory Worldgorger loop safety condition”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 104.4b

If a game that’s not using the limited range of influence option (including a two-player game) somehow enters a “loop” of mandatory actions, repeating a sequence of events with no way to stop, the game is a draw. Loops that contain an optional action don’t result in a draw.

#### CR 121.4

A player who attempts to draw a card from a library with no cards in it loses the game the next time a player would receive priority. (This is a state-based action. See rule 704.)

#### CR 303.4a

An Aura spell requires a target, which is defined by its enchant ability.

#### CR 303.4f

If an Aura is entering the battlefield under a player’s control by any means other than by resolving as an Aura spell, and the effect putting it onto the battlefield doesn’t specify the object or player the Aura will enchant, that player chooses what it will enchant as the Aura enters the battlefield. The player must choose a legal object or player according to the Aura’s enchant ability and any other applicable effects.

#### CR 305.3

A player can’t play a land, for any reason, if it isn’t their turn. Ignore any part of an effect that instructs a player to do so.

#### CR 307.1

A player who has priority may cast a sorcery card from their hand during a main phase of their turn when the stack is empty. Casting a sorcery as a spell uses the stack. (See rule 601, “Casting Spells.”)

#### CR 400.7

An object that moves from one zone to another becomes a new object with no memory of, or relation to, its previous existence. This rule has the following exceptions.

#### CR 601.2h

The player pays the total cost. First, they pay all costs that don’t involve random elements or moving objects from the library to a public zone, in any order. Then they pay all remaining costs in any order. Partial payments are not allowed. Unpayable costs can’t be paid.

#### CR 601.3

A player can begin to cast a spell only if a rule or effect allows that player to cast it and no rule or effect prohibits that player from casting it.

#### CR 603.6a

Enters-the-battlefield abilities trigger when a permanent enters the battlefield. These are written, “When [this object] enters, . . . “ or “Whenever a [type] enters, . . .” Each time an event puts one or more permanents onto the battlefield, all permanents on the battlefield (including the newcomers) are checked for any enters-the-battlefield triggers that match the event.

#### CR 603.6c

Leaves-the-battlefield abilities trigger when a permanent moves from the battlefield to another zone, or when a phased-in permanent leaves the game because its owner leaves the game. These are written as, but aren’t limited to, “When [this object] leaves the battlefield, . . .” or “Whenever [something] is put into a graveyard from the battlefield, . . . .” (See also rule 603.10.) An ability that attempts to do something to the card that left the battlefield checks for it only in the first zone that it went to. An ability that triggers when a card is put into a certain zone “from anywhere” is …

#### CR 603.10a

Some zone-change triggers look back in time. These are leaves-the-battlefield abilities, abilities that trigger when a player sacrifices a permanent, abilities that trigger when a card leaves a graveyard, and abilities that trigger when an object that all players can see is put into a hand or library.

#### CR 608.2

If the object that’s resolving is an instant spell, a sorcery spell, or an ability, its resolution may involve several steps. The steps described in rules 608.2a and 608.2b are followed first. The steps described in rules 608.2c–m are then followed as appropriate, in no specific order. The steps described in rule 608.2n and 608.2p are followed last.

#### CR 702.8a

Flash is a static ability that functions in any zone from which you could play the card it’s on. “Flash” means “You may play this card any time you could cast an instant.”

#### CR 702.40a

Storm is a triggered ability that functions on the stack. “Storm” means “When you cast this spell, copy it for each other spell that was cast before it this turn. If the spell has any targets, you may choose new targets for any of the copies.”

#### CR 702.51a

Convoke is a static ability that functions while the spell with convoke is on the stack. “Convoke” means “For each colored mana in this spell’s total cost, you may tap an untapped creature of that color you control rather than pay that mana. For each generic mana in this spell’s total cost, you may tap an untapped creature you control rather than pay that mana.”

#### CR 702.138a

Escape represents a static ability that functions while the card with escape is in a player’s graveyard. “Escape [cost]” means “You may cast this card from your graveyard by paying [cost] rather than paying its mana cost.” Casting a spell using its escape ability follows the rules for paying alternative costs in rules 601.2b and 601.2f–h.

#### CR 704.5j

If two or more legendary permanents with the same name are controlled by the same player, that player chooses one of them, and the rest are put into their owners’ graveyards. This is called the “legend rule.”

#### CR 903.9a

If a commander is in a graveyard or in exile and that object was put into that zone since the last time state-based actions were checked, its owner may put it into the command zone. This is a state-based action. See rule 704.

#### CR 903.9b

If a commander would be put into its owner’s hand or library from anywhere, its owner may put it into the command zone instead. This replacement effect may apply more than once to the same event. This is an exception to rule 614.5.

