---
title: "Marchesa, Dealer of Death — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Marchesa, Dealer of Death — Interaction Review

> Bot cycle 51 · batch D · reviewed 2026-10-16. Deck: [Marchesa, Dealer of Death](../decks/marchesa-dealer-of-death.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-15), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/marchesa-dealer-of-death.txt`](../../exports/grixis-archidekt/marchesa-dealer-of-death.txt) · SHA-256 `0f07ba66bdbfb883b3513098988621df7b83092eb5cc08cf01669416b961d4cb` |
| Rulings | **8** (8 verified · 0 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-15 · rulings 2026-10-15 |
| Source attestations | [`Marchesa_Dealer_of_Death_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Marchesa_Dealer_of_Death_Approval_Ready_Verification_2026-10-15.md) (Approval-ready verification; rules sections re-checked against Oracle, rulings and CR) |

## Contents
- [Summary](#summary)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [Key card-pair interactions](#key-card-pair-interactions)
- [Timing and priority](#timing-and-priority)
- [Rules cited](#rules-cited)

## Summary

Marchesa turns every targeted interaction into an optional {1} top-two dig, and fills the graveyard for Breach. Repeatable crimes come from Spatial Binding, Hex Parasite and Spellskite (paid in life), utility lands, Forbidden Orchard and Lapis Lazuli Talisman. It wins with Tainted Pact + Oracle, Breach + Brain Freeze, or Aphetto Alchemist + Hawkeye's Bow. All four Spellbook lines are confirmed against the canonical list.

Rules surprises: Spellskite works as a crime even with no target to change; Forbidden Orchard's mana trigger is a crime; Brain Freeze's storm copies aren't crimes; stacking Final Fortune and Last Chance doesn't give two clean turns.

## Commander rules text and edge cases

### marchdod-01: Crimes: one per spell or ability, on cast or activation, before it resolves

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Marchesa, Dealer of Death

**Ruling.** A crime is any spell, activated ability or triggered ability you control that targets an opponent, something an opponent controls, or a card in an opponent's graveyard. You commit it as soon as the spell is cast or the ability is put on the stack. Marchesa's trigger resolves first, and the crime still counts if that spell or ability is later countered or fizzles. Only the initial targets matter. One spell or ability is at most one crime, however many opposing things it targets. Each trigger is "may pay {1}": you choose one of the top two cards for your hand, and the other goes to your graveyard.

**Citations**

- Oracle, *Marchesa, Dealer of Death*: “Whenever you commit a crime, you may pay {1}. If you do, look at the top two cards of your library. Put one of them into your hand and the other into your graveyard.”
- Scryfall ruling, *Marchesa, Dealer of Death*: “A player can commit only one crime per spell or ability they control. Targeting multiple opponents, permanents, spells, abilities, and/or cards with the same spell or ability doesn’t constitute committing multiple crimes.”
- Scryfall ruling, *Marchesa, Dealer of Death*: “The spell or ability that constituted a crime doesn’t have to have resolved yet or at all. As soon as you’re finished casting the spell, activating the ability, or putting the triggered ability on the stack, you’ve committed a crime.”
- Scryfall ruling, *Marchesa, Dealer of Death*: “Changing the target or targets of a spell or ability won’t affect whether or not the controller of that spell or ability has committed a crime. Only the initial targets chosen for that spell or ability are used to determine whether or not its controller committed a crime.”
- [CR 700.13](#cr-70013), [CR 601.2i](#cr-6012i), [CR 405.2](#cr-4052)
- Source (re-verified): [`Marchesa_Dealer_of_Death_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Marchesa_Dealer_of_Death_Approval_Ready_Verification_2026-10-15.md) → “A single spell or ability can cause at most one crime.”

## Combos and engine lines

### marchdod-04: Aphetto Alchemist + Hawkeye's Bow: infinite pings

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Marchesa, Dealer of Death, Aphetto Alchemist, Hawkeye's Bow, Tezzeret, Cruel Captain

**Ruling.** Equip Hawkeye's Bow to Aphetto Alchemist (sorcery speed). Then tap the Alchemist to untap itself. Tapping is part of the cost, so the Bow triggers and deals 1 damage to each opponent. The Alchemist's ability then untaps it. The Bow's trigger has no target, so these pings aren't crimes. The Alchemist must not be summoning sick. Tezzeret's −3 finds the Bow (mana value 1).

**Citations**

- Oracle, *Hawkeye's Bow*: “Whenever equipped creature becomes tapped, it deals 1 damage to each opponent.”
- Oracle, *Aphetto Alchemist*: “{T}: Untap target artifact or creature.”
- [CR 302.6](#cr-3026), [CR 602.2b](#cr-6022b), [CR 702.6a](#cr-7026a)
- Commander Spellbook [4091-7786](https://commanderspellbook.com/combo/4091-7786/) (community-maintained, retrieved 2026-10-16): “Activate Aphetto Alchemist by tapping it, targeting itself.”
- Source (re-verified): [`Marchesa_Dealer_of_Death_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Marchesa_Dealer_of_Death_Approval_Ready_Verification_2026-10-15.md) → “Repeating this loop deals deterministic lethal damage to all opponents.”

### marchdod-05: Tainted Pact + Thassa's Oracle; Breach + LED / Lotus Petal + Brain Freeze

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Marchesa, Dealer of Death, Tainted Pact, Thassa's Oracle, Underworld Breach, Lion's Eye Diamond, Lotus Petal, Brain Freeze

**Ruling.** The list has no basic lands and no duplicate names, so Tainted Pact exiles your whole library. Thassa's Oracle then wins with devotion 1 or more. For Breach lines, Brain Freeze's copies target yourself to mill and fuel escape. Copies aimed at an opponent aren't crimes, because copies are created, not cast. The original Brain Freeze is a crime only if you target an opponent with it. Marchesa's own trigger fills the graveyard for escape.

**Citations**

- Oracle, *Tainted Pact*: “Repeat this process until you put a card into your hand or you exile two cards with the same name, whichever comes first.”
- [CR 702.138a](#cr-702138a), [CR 702.40a](#cr-70240a), [CR 707.10](#cr-70710)
- Commander Spellbook [1295-3093](https://commanderspellbook.com/combo/1295-3093/) (community-maintained, retrieved 2026-10-16): “No two cards in library share a name.”
- Commander Spellbook [1368-3518-4856](https://commanderspellbook.com/combo/1368-3518-4856/) (community-maintained, retrieved 2026-10-16): “You have at least six other cards in hand and/or graveyard.”
- Commander Spellbook [1368-1414-4856](https://commanderspellbook.com/combo/1368-1414-4856/) (community-maintained, retrieved 2026-10-16): “Cast Lotus Petal from your graveyard for its escape cost by exiling three cards besides Brain Freeze from your graveyard.”
- Source (re-verified): [`Marchesa_Dealer_of_Death_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Marchesa_Dealer_of_Death_Approval_Ready_Verification_2026-10-15.md) → “candidate has no duplicate card names, so Tainted Pact supports the established Oracle line.”

## Engines and payoffs

### marchdod-02: Free repeatable crimes: Spatial Binding, Hex Parasite (X=0), Spellskite

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Marchesa, Dealer of Death, Spatial Binding, Hex Parasite, Spellskite

**Ruling.** These turn life into crimes, with no limit on how often:
- **Spatial Binding:** pay 1 life and target an opposing permanent.
- **Hex Parasite:** with X = 0, pay 2 life for {B/P} and target an opposing permanent. X can be larger than the number of counters there.
- **Spellskite:** pay 2 life for {U/P} and target an opponent's spell or ability. You can do this even if Spellskite can't become a legal target, or the spell has no targets at all. Then nothing changes, but the crime is still committed.

Each activation lets you pay {1} for another Marchesa dig, so your mana sets the limit, not the number of cards.

**Citations**

- Oracle, *Spatial Binding*: “Pay 1 life: Until your next upkeep, target permanent can't phase out.”
- Oracle, *Hex Parasite*: “{X}{B/P}: Remove up to X counters from target permanent.”
- Oracle, *Spellskite*: “{U/P}: Change a target of target spell or ability to this creature.”
- Scryfall ruling, *Spellskite*: “You can activate Spellskite's ability even if Spellskite isn't a legal target for the target spell or ability—or even if that spell or ability has no targets. In this case, no targets are changed.”
- Scryfall ruling, *Hex Parasite*: “You may choose a value for X that’s greater than the number of counters on the targeted permanent. However, Hex Parasite only gets the bonus for counters actually removed.”
- [CR 700.13](#cr-70013), [CR 107.4f](#cr-1074f), [CR 602.2b](#cr-6022b)
- Source (re-verified): [`Marchesa_Dealer_of_Death_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Marchesa_Dealer_of_Death_Approval_Ready_Verification_2026-10-15.md) → “Targeting an opposing permanent is therefore a repeatable, mana-free crime source while Marchesa is present.”
- Source (re-verified): [`Marchesa_Dealer_of_Death_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Marchesa_Dealer_of_Death_Approval_Ready_Verification_2026-10-15.md) → “X may be zero.”

### marchdod-03: Crime from lands and triggers: Urborg, Hammerheim, Talon Gates, Forbidden Orchard, Lapis Lazuli Talisman, Orcish Bowmasters

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Marchesa, Dealer of Death, Urborg, Hammerheim, Talon Gates of Madara, Forbidden Orchard, Lapis Lazuli Talisman, Orcish Bowmasters

**Ruling.** Crimes can come from lands and triggers too:
- **Urborg and Hammerheim:** the {T} ability can target an opposing creature that has none of the abilities it removes.
- **Talon Gates of Madara:** its ETB can target an opposing creature.
- **Forbidden Orchard:** whenever you tap it for mana, its trigger targets an opponent. That's a crime every time, and the mana can pay Marchesa's {1}.
- **Lapis Lazuli Talisman:** it triggers whenever any player casts a blue spell. Targeting an opposing permanent is a crime even if you don't pay {3}.
- **Orcish Bowmasters:** each of its pings that targets an opponent or their creature is a crime.

Copy Enchantment doesn't target, so it's never a crime.

**Citations**

- Oracle, *Urborg*: “{T}: Target creature loses first strike or swampwalk until end of turn.”
- Oracle, *Forbidden Orchard*: “Whenever you tap this land for mana, target opponent creates a 1/1 colorless Spirit creature token.”
- Oracle, *Lapis Lazuli Talisman*: “Whenever a player casts a blue spell, you may pay {3}. If you do, untap target permanent.”
- Scryfall ruling, *Urborg*: “The ability can be used on a creature without First Strike or Swampwalk but has no effect.”
- [CR 700.13](#cr-70013), [CR 603.3d](#cr-6033d)
- Source (re-verified): [`Marchesa_Dealer_of_Death_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Marchesa_Dealer_of_Death_Approval_Ready_Verification_2026-10-15.md) → “The target may legally be a creature without either ability; targeting an opposing creature can therefore create a crime from a land slot.”

## Key card-pair interactions

### marchdod-08: Magda: once-per-turn Treasure; Mox Amber reads Marchesa

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Marchesa, Dealer of Death, Magda, the Hoardmaster, Mox Amber

**Ruling.** Magda makes one tapped Treasure for your first crime each turn, not for every crime. Mox Amber makes any of {U}, {B} or {R} while Marchesa is on the battlefield, since she's a legendary creature. Tezzeret is a colorless planeswalker, so with only Tezzeret, Amber makes no mana.

**Citations**

- Oracle, *Magda, the Hoardmaster*: “Whenever you commit a crime, create a tapped Treasure token. This ability triggers only once each turn.”
- Oracle, *Mox Amber*: “{T}: Add one mana of any color among legendary creatures and planeswalkers you control.”
- [CR 700.13](#cr-70013), [CR 106.1b](#cr-1061b)

## Timing and priority

### marchdod-06: Tezzeret's 0 is a crime; Displacer Kitten resets loyalty

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Marchesa, Dealer of Death, Tezzeret, Cruel Captain, Displacer Kitten

**Ruling.** Tezzeret's 0 ("untap target artifact or creature") is a crime when you target an opposing creature or artifact. Normally you get one loyalty ability per permanent per turn. If Displacer Kitten blinks Tezzeret when you cast a noncreature spell, it returns as a new object and can activate a loyalty ability again. That still has to be in your main phase with an empty stack.

**Citations**

- Oracle, *Tezzeret, Cruel Captain*: “0: Untap target artifact or creature. If it's an artifact creature, put a +1/+1 counter on it.”
- Scryfall ruling, *Displacer Kitten*: “When the card returns to the battlefield, it will be a new object with no connection to the card that was exiled. Auras attached to the exiled creature will be put into their owners' graveyards. Any Equipment will become unattached and remain on the battlefield. Any counters on the exiled permanent will cease to exist.”
- [CR 606.3](#cr-6063), [CR 400.7](#cr-4007)
- Source (re-verified): [`Marchesa_Dealer_of_Death_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Marchesa_Dealer_of_Death_Approval_Ready_Verification_2026-10-15.md) → “the returned Tezzeret is a new object and may activate a loyalty ability again that turn, subject to normal timing and priority.”

### marchdod-07: Final Fortune / Last Chance: the most recent extra turn comes first

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Marchesa, Dealer of Death, Final Fortune, Last Chance

**Ruling.** Each spell gives one extra turn, and you lose at the beginning of that turn's end step. If you cast both, the later one's turn comes first and you lose at the end of it, so stacking them doesn't buy a clean double turn. Use them only when the extra turn wins. Valley Floodcaller lets you cast Last Chance at instant speed. If the extra turn gets skipped, you don't lose.

**Citations**

- Oracle, *Final Fortune*: “Take an extra turn after this one. At the beginning of that turn's end step, you lose the game.”
- Scryfall ruling, *Final Fortune*: “If multiple "extra turn" effects resolve in the same turn, take them in the reverse of the order that the effects resolved. In other words, the most recently created extra turn is taken first.”
- Scryfall ruling, *Final Fortune*: “If you end up skipping the extra turn that is gained, you do not lose the game.”
- [CR 500.7](#cr-5007), [CR 603.7](#cr-6037)

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 106.1b

There are six types of mana: white, blue, black, red, green, and colorless.

#### CR 107.4f

Phyrexian mana symbols are colored mana symbols: {W/P} is white, {U/P} is blue, {B/P} is black, {R/P} is red, and {G/P} is green. A Phyrexian mana symbol represents a cost that can be paid either with one mana of its color or by paying 2 life. There are also ten hybrid Phyrexian mana symbols. A hybrid Phyrexian mana symbol represents a cost that can be paid with one mana of either of its component colors or by paying 2 life. A hybrid Phyrexian mana symbol is both of its component colors.

#### CR 302.6

A creature’s activated ability with the tap symbol or the untap symbol in its activation cost can’t be activated unless the creature has been under its controller’s control continuously since their most recent turn began. A creature can’t attack unless it has been under its controller’s control continuously since their most recent turn began. This rule is informally called the “summoning sickness” rule.

#### CR 400.7

An object that moves from one zone to another becomes a new object with no memory of, or relation to, its previous existence. This rule has the following exceptions.

#### CR 405.2

The stack keeps track of the order that spells and/or abilities were added to it. Each time an object is put on the stack, it’s put on top of all objects already there.

#### CR 500.7

Some effects can give a player extra turns. They do this by adding the turns directly after the specified turn. If a player is given multiple extra turns, the extra turns are added one at a time. If multiple players are given extra turns, the extra turns are added one at a time, in APNAP order (see rule 101.4). The most recently created turn will be taken first.

#### CR 601.2i

Once the steps described in 601.2a–h are completed, effects that modify the characteristics of the spell as it’s cast are applied, then the spell becomes cast. Any abilities that trigger when a spell is cast or put onto the stack trigger at this time. If the spell’s controller had priority before casting it, they get priority.

#### CR 602.2b

The remainder of the process for activating an ability is identical to the process for casting a spell listed in rules 601.2b–i. Those rules apply to activating an ability just as they apply to casting a spell. An activated ability’s analog to a spell’s mana cost (as referenced in rule 601.2f) is its activation cost.

#### CR 603.3d

The remainder of the process for putting a triggered ability on the stack is identical to the process for casting a spell listed in rules 601.2c–d. If a choice is required when the triggered ability goes on the stack but no legal choices can be made for it, or if a rule or a continuous effect otherwise makes the ability illegal, the ability is simply removed from the stack.

#### CR 603.7

An effect may create a delayed triggered ability that can do something at a later time. A delayed triggered ability will contain “when,” “whenever,” or “at,” although that word won’t usually begin the ability.

#### CR 606.3

A player may activate a loyalty ability of a permanent they control any time they have priority and the stack is empty during a main phase of their turn, but only if no player has previously activated a loyalty ability of that permanent that turn.

#### CR 700.13

Some cards refer to committing a crime. A player commits a crime as that player casts a spell, activates an ability, or puts a triggered ability on the stack and that spell or ability targets at least one opponent; at least one permanent, spell, or ability an opponent controls; and/or at least one card in an opponent’s graveyard.

#### CR 702.6a

Equip is an activated ability of Equipment cards. “Equip [cost]” means “[Cost]: Attach this permanent to target creature you control. Activate only as a sorcery.”

#### CR 702.40a

Storm is a triggered ability that functions on the stack. “Storm” means “When you cast this spell, copy it for each other spell that was cast before it this turn. If the spell has any targets, you may choose new targets for any of the copies.”

#### CR 702.138a

Escape represents a static ability that functions while the card with escape is in a player’s graveyard. “Escape [cost]” means “You may cast this card from your graveyard by paying [cost] rather than paying its mana cost.” Casting a spell using its escape ability follows the rules for paying alternative costs in rules 601.2b and 601.2f–h.

#### CR 707.10

To copy a spell, activated ability, or triggered ability means to put a copy of it onto the stack; a copy of a spell isn’t cast and a copy of an activated ability isn’t activated. A copy of a spell or ability copies both the characteristics of the spell or ability and all decisions made for it, including modes, targets, the value of X, and additional or alternative costs. (See rule 601, “Casting Spells.”) Choices that are normally made on resolution are not copied. If an effect of the copy refers to objects used to pay its costs, it uses the objects used to pay the costs of the original spell …

