---
title: "Inalla, Archmage Ritualist — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Inalla, Archmage Ritualist — Interaction Review

> Bot cycle 49 · batch C · reviewed 2026-10-16. Deck: [Inalla, Archmage Ritualist](../decks/inalla-archmage-ritualist.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/inalla-archmage-ritualist.txt`](../../exports/grixis-archidekt/inalla-archmage-ritualist.txt) · SHA-256 `45924e0eabb7a253004d5cdf69c32f7ab82d1e0e7406938a033a8f8b39026598` |
| Rulings | **10** (9 verified · 1 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`Inalla_Archmage_Ritualist_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/inalla_archmage_ritualist_2026-10-14/Inalla_Archmage_Ritualist_Rules_Attestation.json) (15 interactions, all PASS (the Kefka and Samut items refer to cards not in the current list)) |

## Contents
- [Summary](#summary)
- [Flags and open questions](#flags-and-open-questions)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [Timing and priority](#timing-and-priority)
- [Trigger ordering](#trigger-ordering)
- [Rules cited](#rules-cited)

## Summary

Inalla, Archmage Ritualist copies each nontoken Wizard that enters, even from the command zone, and taps five Wizards to drain 7. This review re-verifies the deck's rules attestation, and confirms fifteen combo lines (Bloodline/Ruthless, the Scholar of the Ages loops, the Oracle and Breach lines) against cached Commander Spellbook steps.

The source's Spellseeker chain stays an uncertain hypothesis. The attestation's Kefka item is about a card that isn't in the current list. No list errors.

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [inalla-06](#inalla-06-spellseeker-one-card-line) | ⚠️ uncertain | Spellseeker one-card line | Rebuilt multi-step line from the source attestation; no cached Spellbook variant confirms the whole sequence, so it stays a hypothesis. |

## Commander rules text and edge cases

### inalla-01: Eminence works from the command zone, once per trigger

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Inalla, Archmage Ritualist

**Ruling.** Inalla's copy ability works while she's in the command zone or on the battlefield. She has to be in one of those zones both when the Wizard enters and when the trigger resolves. If she moves between them in between (say she dies and goes to the command zone), the trigger does nothing, because she's a new object. You can pay {1} only once per trigger. The hasty token is exiled at the next end step. If the Wizard has already left when the trigger resolves, you can still pay and copy its last-known version.

**Citations**

- Oracle, *Inalla, Archmage Ritualist*: “Eminence — Whenever another nontoken Wizard you control enters, if Inalla is in the command zone or on the battlefield, you may pay {1}. If you do, create a token that's a copy of that Wizard. The token gains haste. Exile it at the beginning of the next end step.”
- Scryfall ruling, *Inalla, Archmage Ritualist*: “You can pay {1} only once each time Inalla's first ability resolves. You can't pay more to get more than one token.”
- Scryfall ruling, *Inalla, Archmage Ritualist*: “Notably, if your commander is on the battlefield and its eminence ability triggers, but it's put into the command zone before that ability resolves, that ability won't do anything as it resolves. This is because an object that changes zones is considered a new object.”
- [CR 207.2c](#cr-2072c), [CR 400.7](#cr-4007), [CR 707.2](#cr-7072)
- Source (re-verified): [`Inalla_Archmage_Ritualist_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/inalla_archmage_ritualist_2026-10-14/Inalla_Archmage_Ritualist_Rules_Attestation.json) → “Inalla Eminence functions from the command zone”

### inalla-02: The five-Wizard tap ignores summoning sickness

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Inalla, Archmage Ritualist

**Ruling.** 'Tap five untapped Wizards you control' isn't a {T} cost of those Wizards, so new tokens and Inalla herself can be tapped for it the turn they arrive. Inalla must be on the battlefield to activate it. Target player loses 7.

**Citations**

- Oracle, *Inalla, Archmage Ritualist*: “Tap five untapped Wizards you control: Target player loses 7 life.”
- Scryfall ruling, *Inalla, Archmage Ritualist*: “To activate Inalla's last ability, you may tap any untapped Wizards you control, including ones you haven't controlled continuously since the beginning of your most recent turn, such as Inalla itself.”
- [CR 302.6](#cr-3026), [CR 602.2](#cr-6022)
- Source (re-verified): [`Inalla_Archmage_Ritualist_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/inalla_archmage_ritualist_2026-10-14/Inalla_Archmage_Ritualist_Rules_Attestation.json) → “Inalla five-Wizard activation and new tokens”

## Combos and engine lines

### inalla-03: Inalla + Bloodline Necromancer + Ruthless Technomancer

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Inalla, Archmage Ritualist, Bloodline Necromancer, Ruthless Technomancer

**Ruling.** Both are Wizards. Bloodline Necromancer (3/2) returns Ruthless Technomancer, which sacrifices Bloodline for three Treasures. Order the pending Inalla triggers: pay {1} for a Ruthless token, which sacrifices the nontoken Ruthless (power 2) for two Treasures. Then pay {1} for a Bloodline token, which returns the nontoken Bloodline, and repeat. Each loop nets Treasures and hasty Wizard tokens. Finish by casting Inalla if needed and tapping five Wizards for 7 life at a time.

**Citations**

- Oracle, *Ruthless Technomancer*: “When this creature enters, you may sacrifice another creature you control. If you do, create a number of Treasure tokens equal to that creature's power.”
- Oracle, *Bloodline Necromancer*: “When this creature enters, you may return target Vampire or Wizard creature card from your graveyard to the battlefield.”
- [CR 603.3b](#cr-6033b), [CR 707.2](#cr-7072)
- Commander Spellbook [1869-2721-3719](https://commanderspellbook.com/combo/1869-2721-3719/) (community-maintained, retrieved 2026-10-16): “Resolve the Ruthless Technomancer trigger, causing you to sacrifice Bloodline Necromancer and create three Treasure tokens.”
- Commander Spellbook [1869-2721-3719](https://commanderspellbook.com/combo/1869-2721-3719/) (community-maintained, retrieved 2026-10-16): “Resolve the Inalla trigger from step 4, causing you to pay {1} to create a token copy of Ruthless Technomancer with haste.”
- Commander Spellbook [1869-2721-3719](https://commanderspellbook.com/combo/1869-2721-3719/) (community-maintained, retrieved 2026-10-16): “Activate Inalla by tapping five untapped Wizards you control, causing target player to lose 7 life.”
- Source (re-verified): [`Inalla_Archmage_Ritualist_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/inalla_archmage_ritualist_2026-10-14/Inalla_Archmage_Ritualist_Rules_Attestation.json) → “Bloodline Necromancer plus Ruthless Technomancer loop”

### inalla-04: Scholar of the Ages + a sacrifice ritual + Shallow Grave or Persist

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Inalla, Archmage Ritualist, Scholar of the Ages, Sacrifice, Burnt Offering, Culling the Weak, Shallow Grave, Persist

**Ruling.** Sacrifice Scholar (mana value 7) to Sacrifice for seven {B}, Burnt Offering for seven {B}/{R}, or Culling the Weak for four {B}. Return it with Persist ({1}{B}, nonlegendary, -1/-1 counter) or Shallow Grave ({1}{B}). Its ETB returns both spells. Each loop nets mana and an ETB. Shallow Grave takes the top creature card of your graveyard, and you can't reorder a graveyard, so Scholar must be the last creature card put there. Each nontoken Scholar entering also triggers Inalla.

**Citations**

- Oracle, *Scholar of the Ages*: “When this creature enters, return up to two target instant and/or sorcery cards from your graveyard to your hand.”
- Oracle, *Sacrifice*: “Add an amount of {B} equal to the sacrificed creature's mana value.”
- Oracle, *Shallow Grave*: “Return the top creature card of your graveyard to the battlefield.”
- Scryfall ruling, *Scholar of the Ages*: “The triggered ability of Scholar of the Ages can return at most two cards, not two instant cards plus two sorcery cards.”
- [CR 202.3](#cr-2023), [CR 404.2](#cr-4042), [CR 601.2f](#cr-6012f)
- Commander Spellbook [813-1181-2171](https://commanderspellbook.com/combo/813-1181-2171/) (community-maintained, retrieved 2026-10-16): “Cast Persist by paying its mana cost, returning Scholar of the Ages from your graveyard to the battlefield.”
- Commander Spellbook [813-1777-1893](https://commanderspellbook.com/combo/813-1777-1893/) (community-maintained, retrieved 2026-10-16): “Cast Burnt Offering by paying {B} and sacrificing Scholar of the Ages, adding seven mana in any combination of {B} and/or {R}.”
- Commander Spellbook [813-1893-2081](https://commanderspellbook.com/combo/813-1893-2081/) (community-maintained, retrieved 2026-10-16): “Cast Culling the Weak by paying {B} and sacrificing Scholar of the Ages, adding {B}{B}{B}{B}.”

### inalla-05: Saw in Half + Scholar: the tokens keep mana value 7

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Inalla, Archmage Ritualist, Saw in Half, Scholar of the Ages, Sacrifice

**Ruling.** Saw in Half's tokens are copies with halved power and toughness, but they copy the mana cost, so each has mana value 7. Both tokens' ETBs return Saw in Half and the ritual (and up to two more spells). Sacrificing a token to Sacrifice adds seven {B}, which pays for the next Saw in Half on the other token.

**Citations**

- Oracle, *Saw in Half*: “its controller creates two tokens that are copies of that creature, except their power is half that creature's power and their toughness is half that creature's toughness”
- [CR 707.2](#cr-7072), [CR 202.3](#cr-2023)
- Commander Spellbook [500-813-1181](https://commanderspellbook.com/combo/500-813-1181/) (community-maintained, retrieved 2026-10-16): “Cast Sacrifice by paying {B} and sacrificing a Scholar of the Ages token, adding seven {B}.”
- Source (re-verified): [`Inalla_Archmage_Ritualist_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/inalla_archmage_ritualist_2026-10-14/Inalla_Archmage_Ritualist_Rules_Attestation.json) → “Hoarding Broodlord plus Saw in Half”

### inalla-06: Spellseeker one-card line

**Status:** ⚠️ uncertain · **Evidence:** hypothesis · **Cards:** Inalla, Archmage Ritualist, Spellseeker, Culling the Weak, Unearth, Burnt Offering, Finale of Promise, Entomb, Reanimate, Scholar of the Ages

**Ruling.** The source's chain: Spellseeker and its Inalla copy each tutor an instant or sorcery with mana value 2 or less, in sequence (Culling the Weak, Unearth, Burnt Offering, Finale of Promise, Entomb, Reanimate). It recurs Spellseeker and assembles a Scholar of the Ages mana loop. Each step is rules-legal: Finale X = 1 casts Culling and Unearth from the graveyard during its resolution. But there's no Spellbook variant for the whole chain, and it depends on mana, life and library contents.

**Uncertain.** Rebuilt multi-step line from the source attestation; no cached Spellbook variant confirms the whole sequence, so it stays a hypothesis.

**Citations**

- Oracle, *Spellseeker*: “When this creature enters, you may search your library for an instant or sorcery card with mana value 2 or less, reveal it, put it into your hand, then shuffle.”
- Oracle, *Finale of Promise*: “You may cast up to one target instant card and/or up to one target sorcery card from your graveyard each with mana value X or less without paying their mana costs.”
- Scryfall ruling, *Finale of Promise*: “As Finale of Promise resolves, first you cast the target instant card and/or the target sorcery card in either order.”
- [CR 608.2g](#cr-6082g), [CR 601.2](#cr-6012)
- Source (re-verified): [`Inalla_Archmage_Ritualist_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/inalla_archmage_ritualist_2026-10-14/Inalla_Archmage_Ritualist_Rules_Attestation.json) → “Spellseeker plus Scholar of the Ages one-card Inalla line”
- Source (re-verified): [`Inalla_Archmage_Ritualist_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/inalla_archmage_ritualist_2026-10-14/Inalla_Archmage_Ritualist_Rules_Attestation.json) → “Finale of Promise casting during resolution”

### inalla-09: Thassa's Oracle and Breach lines

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Inalla, Archmage Ritualist, Thassa's Oracle, Demonic Consultation, Tainted Pact, Underworld Breach, Lion's Eye Diamond, Brain Freeze

**Ruling.** The standard cEDH finishes are all in the list: Consultation or Tainted Pact with Oracle (100 distinct names), and Breach + LED + Brain Freeze, which needs six other cards in hand and/or graveyard.

**Citations**

- [CR 121.4](#cr-1214), [CR 702.138a](#cr-702138a)
- Commander Spellbook [742-1295](https://commanderspellbook.com/combo/742-1295/) (community-maintained, retrieved 2026-10-16): “Cast Demonic Consultation by paying {B}, naming Thassa's Oracle and thus exiling your library due to you not having a card named Thassa's Oracle in your library.”
- Commander Spellbook [1295-3093](https://commanderspellbook.com/combo/1295-3093/) (community-maintained, retrieved 2026-10-16): “No two cards in library share a name.”
- Commander Spellbook [1368-3518-4856](https://commanderspellbook.com/combo/1368-3518-4856/) (community-maintained, retrieved 2026-10-16): “You have at least six other cards in hand and/or graveyard.”
- Source (re-verified): [`Inalla_Archmage_Ritualist_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/inalla_archmage_ritualist_2026-10-14/Inalla_Archmage_Ritualist_Rules_Attestation.json) → “Thassa's Oracle plus Demonic Consultation”
- Source (re-verified): [`Inalla_Archmage_Ritualist_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/inalla_archmage_ritualist_2026-10-14/Inalla_Archmage_Ritualist_Rules_Attestation.json) → “Thassa's Oracle plus Tainted Pact and singleton structure”
- Source (re-verified): [`Inalla_Archmage_Ritualist_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/inalla_archmage_ritualist_2026-10-14/Inalla_Archmage_Ritualist_Rules_Attestation.json) → “Underworld Breach plus Lion's Eye Diamond plus Brain Freeze”

## Engines and payoffs

### inalla-08: Hasty Wizard copies: Apprentice Necromancer and Thundertrap Trainer

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Inalla, Archmage Ritualist, Apprentice Necromancer, Thundertrap Trainer

**Ruling.** An Inalla copy of Apprentice Necromancer has haste, so it can use its {B}, {T}, sacrifice ability at once to reanimate a creature with haste. It can't target itself, because targets are chosen before the sacrifice. A Thundertrap Trainer copy gets its own top-four ETB. It wasn't cast, so there's no offspring.

**Citations**

- Oracle, *Apprentice Necromancer*: “{B}, {T}, Sacrifice this creature: Return target creature card from your graveyard to the battlefield. That creature gains haste. At the beginning of the next end step, sacrifice it.”
- Scryfall ruling, *Apprentice Necromancer*: “Apprentice Necromancer can’t be the target of its own ability. This is because targets are chosen for activated abilities before costs (such as “Sacrifice Apprentice Necromancer”) are paid.”
- [CR 602.2](#cr-6022), [CR 601.2c](#cr-6012c), [CR 702.175a](#cr-702175a)
- Source (re-verified): [`Inalla_Archmage_Ritualist_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/inalla_archmage_ritualist_2026-10-14/Inalla_Archmage_Ritualist_Rules_Attestation.json) → “Apprentice Necromancer plus Inalla haste”
- Source (re-verified): [`Inalla_Archmage_Ritualist_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/inalla_archmage_ritualist_2026-10-14/Inalla_Archmage_Ritualist_Rules_Attestation.json) → “Thundertrap Trainer duplicated ETB”

## Timing and priority

### inalla-07: Finale and Beseech cast during resolution; split second would stop them

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Inalla, Archmage Ritualist, Finale of Promise, Beseech the Mirror

**Ruling.** Finale of Promise and a bargained Beseech the Mirror cast cards while they're still resolving on the stack. Split second (for example from Samut, Tyrant of Naktamun) would forbid those casts, which is why the source cut Samut. Nothing in the current list gives split second. A spell cast free with {X} has X = 0.

**Citations**

- Scryfall ruling, *Finale of Promise*: “If a spell has {X} in its mana cost, you must choose 0 as the value of X when casting it without paying its mana cost.”
- Scryfall ruling, *Beseech the Mirror*: “Bargain represents an optional additional cost. A spell cast with that additional cost paid is "bargained."”
- [CR 702.61a](#cr-70261a), [CR 608.2g](#cr-6082g)
- Source (re-verified): [`Inalla_Archmage_Ritualist_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/inalla_archmage_ritualist_2026-10-14/Inalla_Archmage_Ritualist_Rules_Attestation.json) → “Samut red-team exclusion”
- Source (re-verified): [`Inalla_Archmage_Ritualist_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/inalla_archmage_ritualist_2026-10-14/Inalla_Archmage_Ritualist_Rules_Attestation.json) → “Beseech the Mirror bargain casting”

## Trigger ordering

### inalla-10: Kefka token copy: both enters triggers happen, then the legend rule

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Inalla, Archmage Ritualist, Kefka, Court Mage

**Ruling.** Kefka is a nontoken legendary Wizard, so when it enters, Inalla's eminence triggers along with Kefka's own enters ability. If you pay {1}, the token copy enters and its copy of Kefka's enters ability triggers too. The legend rule then makes you keep only one Kefka. The token's trigger was already waiting, so it goes on the stack after the legend rule is applied. Triggers already on the stack, like the original's, stay there (they exist independently of their source). So you get two Kefka triggers: each makes every player discard a card, then you draw for each card type discarded. The token is a double-faced copy of Kefka. The deck doesn't need both Kefkas to stay.

**Citations**

- Oracle, *Kefka, Court Mage*: “Whenever Kefka enters or attacks, each player discards a card. Then you draw a card for each card type among cards discarded this way.”
- Oracle, *Inalla, Archmage Ritualist*: “Whenever another nontoken Wizard you control enters, if Inalla is in the command zone or on the battlefield, you may pay {1}. If you do, create a token that's a copy of that Wizard.”
- Scryfall ruling, *Inalla, Archmage Ritualist*: “If a copied creature is legendary, any triggered abilities it has will trigger if appropriate before the "legend rule" causes one of those legendary creatures to be put into its owner's graveyard. Those abilities will be put on the stack after the "legend rule" is applied.”
- Scryfall ruling, *Kefka, Court Mage*: “A token that is created as a copy of a double-faced permanent or a double-faced card in another zone is a double-faced token.”
- [CR 704.5j](#cr-7045j), [CR 113.7a](#cr-1137a), [CR 603.3](#cr-6033)
- Source (re-verified): [`Inalla_Archmage_Ritualist_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/inalla_archmage_ritualist_2026-10-14/Inalla_Archmage_Ritualist_Rules_Attestation.json) → “Kefka legendary-copy handling”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 113.7a

Once activated or triggered, an ability exists on the stack independently of its source. Destruction or removal of the source after that time won’t affect the ability. Note that some abilities cause a source to do something (for example, “This creature deals 1 damage to any target”) rather than the ability doing anything directly. In these cases, any activated or triggered ability that references information about the source for use while announcing an activated ability or putting a triggered ability on the stack checks that information when the ability is put onto the stack. Otherwise, it …

#### CR 121.4

A player who attempts to draw a card from a library with no cards in it loses the game the next time a player would receive priority. (This is a state-based action. See rule 704.)

#### CR 202.3

The mana value of an object is a number equal to the total amount of mana in its mana cost, regardless of color.

#### CR 207.2c

An ability word appears in italics at the beginning of some abilities. Ability words are similar to keywords in that they tie together cards that have similar functionality, but they have no special rules meaning and no individual entries in the Comprehensive Rules. The ability words are adamant, addendum, alliance, battalion, bloodrush, celebration, channel, chroma, cohort, constellation, converge, council’s dilemma, coven, delirium, descend 4, descend 8, disappear, domain, eerie, eminence, enrage, fateful hour, fathomless descent, ferocious, flurry, formidable, grandeur, hellbent, heroic, …

#### CR 302.6

A creature’s activated ability with the tap symbol or the untap symbol in its activation cost can’t be activated unless the creature has been under its controller’s control continuously since their most recent turn began. A creature can’t attack unless it has been under its controller’s control continuously since their most recent turn began. This rule is informally called the “summoning sickness” rule.

#### CR 400.7

An object that moves from one zone to another becomes a new object with no memory of, or relation to, its previous existence. This rule has the following exceptions.

#### CR 404.2

Each graveyard is kept in a single face-up pile. A player can examine the cards in any graveyard at any time but normally can’t change their order. Additional rules applying to sanctioned tournaments may allow a player to change the order of cards in their graveyard.

#### CR 601.2

To cast a spell is to take it from where it is (usually the hand), put it on the stack, and pay its costs, so that it will eventually resolve and have its effect. Casting a spell includes proposal of the spell (rules 601.2a–d) and determination and payment of costs (rules 601.2f–h). To cast a spell, a player follows the steps listed below, in order. A player must be legally allowed to cast the spell to begin this process (see rule 601.3). If a player is unable to comply with the requirements of a step listed below while performing that step, the casting of the spell is illegal; the game …

#### CR 601.2c

The player announces their choice of an appropriate object or player for each target the spell requires. A spell may require some targets only if an alternative or additional cost (such as a kicker cost) or a particular mode was chosen for it; otherwise, the spell is cast as though it did not require those targets. Similarly, a spell may require alternative targets only if an alternative or additional cost was chosen for it. If the spell has a variable number of targets, the player announces how many targets they will choose before they announce those targets. In some cases, the number of …

#### CR 601.2f

The player determines the total cost of the spell. Usually this is just the mana cost. Some spells have additional or alternative costs. Some effects may increase or reduce the cost to pay, or may provide other alternative costs. Costs may include paying mana, tapping permanents, sacrificing permanents, discarding cards, and so on. The total cost is the mana cost or alternative cost (as determined in rule 601.2b), plus all additional costs and cost increases, and minus all cost reductions. If multiple cost reductions apply, the player may apply them in any order. If the mana component of the …

#### CR 602.2

To activate an ability is to put it onto the stack and pay its costs, so that it will eventually resolve and have its effect. Only an object’s controller (or its owner, if it doesn’t have a controller) can activate its activated ability unless the object specifically says otherwise. Activating an ability follows the steps listed below, in order. If, at any point during the activation of an ability, a player is unable to comply with any of those steps, the activation is illegal; the game returns to the moment before that ability started to be activated (see rule 733, “Handling Illegal …

#### CR 603.3

Once an ability has triggered, its controller puts it on the stack as an object that’s not a card the next time a player would receive priority. See rule 117, “Timing and Priority.” The ability becomes the topmost object on the stack. It has the text of the ability that created it, and no other characteristics. It remains on the stack until it’s countered, it resolves, a rule causes it to be removed from the stack, or an effect moves it elsewhere.

#### CR 603.3b

If multiple abilities have triggered since the last time a player received priority, the abilities are placed on the stack in a two-part process. First, each player, in APNAP order, puts each triggered ability they control with a trigger condition that isn’t another ability triggering on the stack in any order they choose. (See rule 101.4.) Second, each player, in APNAP order, puts all remaining triggered abilities they control on the stack in any order they choose. Then the game once again checks for and performs state-based actions until none are performed, then abilities that triggered …

#### CR 608.2g

If an effect gives a player the option to pay mana, they may activate mana abilities before taking that action. If an effect specifically instructs or allows a player to cast a spell during resolution, they do so by following the steps in rules 601.2a–i, except no player receives priority after it’s cast. That spell becomes the topmost object on the stack, and the currently resolving spell or ability continues to resolve, which may include casting other spells this way. No other spells can normally be cast and no other abilities can normally be activated during resolution.

#### CR 702.61a

Split second is a static ability that functions only while the spell with split second is on the stack. “Split second” means “As long as this spell is on the stack, players can’t cast other spells or activate abilities that aren’t mana abilities.”

#### CR 702.138a

Escape represents a static ability that functions while the card with escape is in a player’s graveyard. “Escape [cost]” means “You may cast this card from your graveyard by paying [cost] rather than paying its mana cost.” Casting a spell using its escape ability follows the rules for paying alternative costs in rules 601.2b and 601.2f–h.

#### CR 702.175a

Offspring represents two abilities. “Offspring [cost]” means “You may pay an additional [cost] as you cast this spell” and “When this permanent enters, if its offspring cost was paid, create a token that’s a copy of it, except it’s 1/1.”

#### CR 704.5j

If two or more legendary permanents with the same name are controlled by the same player, that player chooses one of them, and the rest are put into their owners’ graveyards. This is called the “legend rule.”

#### CR 707.2

When copying an object, the copy acquires the copiable values of the original object’s characteristics and, for an object on the stack, choices made when casting or activating it (mode, targets, the value of X, whether it was kicked, how it will affect multiple targets, and so on). The copiable values are the values derived from the text printed on the object (that text being name, mana cost, color indicator, card type, subtype, supertype, rules text, power, toughness, and/or loyalty), as modified by other copy effects, by its face-down status, and by “as . . . enters” and “as . . . is turned …

