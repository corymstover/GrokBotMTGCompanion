---
title: "Crosis, the Purger — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Crosis, the Purger — Interaction Review

> Bot cycle 46 · batch A · reviewed 2026-10-16. Deck: [Crosis, the Purger](../decks/crosis-the-purger.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-15), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Current list | [`exports/grixis-archidekt/crosis-the-purger.txt`](../../exports/grixis-archidekt/crosis-the-purger.txt) · SHA-256 `04784e892c930bb5e60f8551ffffa7e9527634359db38378fd1bd7e4c8e3647d` |
| Rulings | **11** (9 verified · 1 uncertain · 1 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-15 · rulings 2026-10-15 |
| Source attestations | [`Crosis_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/crosis_2026-10-14/Crosis_Rules_Attestation.json) (10 interactions, all PASS) |

## Contents
- [Summary](#summary)
- [Flags and open questions](#flags-and-open-questions)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Key card-pair interactions](#key-card-pair-interactions)
- [Layers and continuous effects](#layers-and-continuous-effects)
- [Replacement and prevention effects](#replacement-and-prevention-effects)
- [Trigger ordering](#trigger-ordering)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [Rules cited](#rules-cited)

## Summary

Crosis, the Purger is a discard/control deck that turns combat damage into color-based hand wipes, with Painter's Servant as the full-hand version. This review re-verifies all ten items of the deck's rules attestation.

Flag: Painter set to black or green knocks Sword of Feast and Famine off Crosis. Rules note: Lightning Greaves' shroud blocks your own later equips (Swiftfoot Boots' hexproof doesn't). No list errors.

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [crosis-03](#crosis-03-painters-color-can-knock-sword-of-feast-and-famine-off-crosis) | 🚩 list flag (anti-synergy) | Painter's color can knock Sword of Feast and Famine off Crosis | A conditional non-bo: Painter's Servant set to black (the obvious Grixis pick) or green makes Sword of Feast and Famine fall off Crosis. Choose a non-black, non-green color when both are in play. No list change. |
| [crosis-10](#crosis-10-oppression-is-symmetric) | ⚠️ uncertain | Oppression is symmetric | Whether Oppression is net positive is a strategic judgment, not a rules question; recorded so the symmetry is visible. |

## Commander rules text and edge cases

### crosis-01: Pay {2}{B} on resolution, then choose the color

**Status:** ✅ verified · **Cards:** Crosis, the Purger

**Ruling.** Crosis triggers after it deals combat damage to a player. On resolution you may pay {2}{B}; you can't prepay, and it isn't an attack cost. Then you choose a color, so the opponent can't respond knowing it. They reveal and discard all cards of that color. Colorless cards (artifacts, lands) are safe unless Painter's Servant is out.

**Citations**

- Oracle, *Crosis, the Purger*: “Whenever Crosis deals combat damage to a player, you may pay {2}{B}. If you do, choose a color, then that player reveals their hand and discards all cards of that color.”
- Scryfall ruling, *Crosis, the Purger*: “You choose the color during resolution. This means your opponent does not get to react after knowing the color you chose.”
- [CR 603.2](#cr-6032), [CR 608.2b](#cr-6082b), [CR 105.2c](#cr-1052c)
- Source (re-verified): [`Crosis_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/crosis_2026-10-14/Crosis_Rules_Attestation.json) → “Crosis combat-damage trigger”

## Combos and engine lines

### crosis-02: Painter's Servant makes Crosis a full-hand discard

**Status:** ✅ verified · **Cards:** Crosis, the Purger, Painter's Servant

**Ruling.** Painter's Servant makes every card not on the battlefield (hands included) the chosen color in addition to its own colors, colorless cards included. Naming the Painter color with Crosis discards the whole hand. If Painter leaves before Crosis's trigger resolves, the cards revert. Another color-setting effect overrides Painter on that object.

**Citations**

- Oracle, *Painter's Servant*: “All cards that aren't on the battlefield, spells, and permanents are the chosen color in addition to their other colors.”
- Scryfall ruling, *Painter's Servant*: “This ability affects every card in every game zone, all tokens on the battlefield, and all spell copies on the stack, regardless of who controls or owns them.”
- [CR 105.3](#cr-1053), [CR 613.1e](#cr-6131e)
- Source (re-verified): [`Crosis_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/crosis_2026-10-14/Crosis_Rules_Attestation.json) → “Crosis + Painter's Servant”

### crosis-07: Notion Thief + Teferi's Puzzle Box lock

**Status:** ✅ verified · **Cards:** Crosis, the Purger, Notion Thief, Teferi's Puzzle Box

**Ruling.** On each opponent's draw step, after their normal draw, Puzzle Box puts their hand on the bottom and has them draw that many. Notion Thief replaces those draws, so you draw instead. Opponents end each draw step with one card. Puzzle Box is symmetric: it also cycles *your* hand on your draw step, and your draws aren't stolen.

**Citations**

- Oracle, *Teferi's Puzzle Box*: “At the beginning of each player's draw step, that player puts the cards in their hand on the bottom of their library in any order, then draws that many cards.”
- Scryfall ruling, *Teferi's Puzzle Box*: “You do your normal draw before this ability is put on the stack.”
- [CR 614.1a](#cr-6141a), [CR 121.6](#cr-1216)
- Source (re-verified): [`Crosis_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/crosis_2026-10-14/Crosis_Rules_Attestation.json) → “Notion Thief + Teferi's Puzzle Box”

## Key card-pair interactions

### crosis-05: Brotherhood Regalia: unblockable for {1}

**Status:** ✅ verified · **Cards:** Crosis, the Purger, Brotherhood Regalia

**Ruling.** Brotherhood Regalia equips a legendary creature for {1} and gives ward {2} and 'can't be blocked', so Crosis connects. It doesn't change the {2}{B} payment.

**Citations**

- Oracle, *Brotherhood Regalia*: “Equipped creature has ward {2}, is an Assassin in addition to its other types, and can't be blocked.”
- [CR 702.6a](#cr-7026a), [CR 702.21a](#cr-70221a)
- Source (re-verified): [`Crosis_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/crosis_2026-10-14/Crosis_Rules_Attestation.json) → “Brotherhood Regalia + Crosis”

### crosis-09: Recoil and Dream Salvage

**Status:** ✅ verified · **Cards:** Crosis, the Purger, Recoil, Dream Salvage

**Ruling.** - **Recoil:** bounces a permanent, then its owner discards a card. With an empty hand, the bounced card is the only choice.
- **Dream Salvage:** draws for every card the target opponent discarded *this turn*, so cast it after Crosis, Painter or a wheel.

**Citations**

- Oracle, *Recoil*: “Return target permanent to its owner's hand. Then that player discards a card.”
- Oracle, *Dream Salvage*: “Draw cards equal to the number of cards target opponent discarded this turn.”
- [CR 608.2c](#cr-6082c)
- Source (re-verified): [`Crosis_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/crosis_2026-10-14/Crosis_Rules_Attestation.json) → “Recoil on a player with no other cards in hand”
- Source (re-verified): [`Crosis_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/crosis_2026-10-14/Crosis_Rules_Attestation.json) → “Dream Salvage after Crosis or mass discard”

### crosis-10: Oppression is symmetric

**Status:** ⚠️ uncertain · **Cards:** Crosis, the Purger, Oppression

**Ruling.** Oppression makes *every* player who casts a spell discard, you included. In a deck with many instants and rituals, that costs you cards too. Its value comes from opponents casting from smaller hands, and Waste Not and Tergrid reward their discards.

**Uncertain.** Whether Oppression is net positive is a strategic judgment, not a rules question; recorded so the symmetry is visible.

**Citations**

- Oracle, *Oppression*: “Whenever a player casts a spell, that player discards a card.”
- [CR 603.2](#cr-6032)

## Layers and continuous effects

### crosis-03: Painter's color can knock Sword of Feast and Famine off Crosis

**Status:** 🚩 list flag · **Cards:** Crosis, the Purger, Painter's Servant, Sword of Feast and Famine

**Ruling.** Painter also colors permanents. If it names black or green, Sword of Feast and Famine becomes black or green and can't stay attached to a creature with protection from black and from green. It falls off as a state-based action. Name blue, red or white with Sword equipped.

**List flag (anti-synergy).** A conditional non-bo: Painter's Servant set to black (the obvious Grixis pick) or green makes Sword of Feast and Famine fall off Crosis. Choose a non-black, non-green color when both are in play. No list change.

**Citations**

- Oracle, *Sword of Feast and Famine*: “Equipped creature gets +2/+2 and has protection from black and from green.”
- [CR 702.16d](#cr-70216d), [CR 704.5n](#cr-7045n)
- Source (re-verified): [`Crosis_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/crosis_2026-10-14/Crosis_Rules_Attestation.json) → “Painter's Servant + Sword of Feast and Famine protection caveat”

## Replacement and prevention effects

### crosis-08: Notion Thief turns wheels one-sided

**Status:** ✅ verified · **Cards:** Crosis, the Purger, Notion Thief, Wheel of Fortune, Windfall, Dark Deal

**Ruling.** Wheel of Fortune, Windfall and Dark Deal make opponents discard their hands; Notion Thief takes their redraws. Waste Not and Tergrid profit from the discards.

**Citations**

- Oracle, *Notion Thief*: “If an opponent would draw a card except the first one they draw in each of their draw steps, instead that player skips that draw and you draw a card.”
- [CR 614.1a](#cr-6141a)
- Source (re-verified): [`Crosis_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/crosis_2026-10-14/Crosis_Rules_Attestation.json) → “Notion Thief + Wheel of Fortune / Windfall / Dark Deal”

## Trigger ordering

### crosis-04: Sword of Feast and Famine above Crosis: untapped lands pay {2}{B}

**Status:** ✅ verified · **Cards:** Crosis, the Purger, Sword of Feast and Famine

**Ruling.** Both trigger on combat damage. Put Crosis's trigger on the stack first and Sword's on top. Sword resolves first (one discard, untap all lands), and the untapped lands pay {2}{B} for Crosis. Mana made while the triggers are on the stack empties at the end of the combat damage step.

**Citations**

- Scryfall ruling, *Sword of Feast and Famine*: “You'll untap all lands you control even if the player can't discard a card.”
- [CR 603.3b](#cr-6033b), [CR 106.4](#cr-1064)
- Source (re-verified): [`Crosis_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/crosis_2026-10-14/Crosis_Rules_Attestation.json) → “Sword of Feast and Famine + Crosis trigger ordering”

### crosis-06: Tergrid and Tinybones: order Tergrid on top

**Status:** ✅ verified · **Cards:** Crosis, the Purger, Tergrid, God of Fright // Tergrid's Lantern, Tinybones, Bauble Burglar

**Ruling.** When an opponent discards a permanent card, Tergrid and Tinybones both trigger. Put Tinybones first and Tergrid on top: Tergrid resolves first and puts the permanent onto the battlefield under your control. Tinybones then finds the card gone. Tinybones still exiles non-permanent cards (instants, sorceries) for you to play during your turn.

**Citations**

- Scryfall ruling, *Tergrid, God of Fright // Tergrid's Lantern*: “If the card leaves the graveyard before Tergrid's ability resolves, you can't put it onto the battlefield, even if it returns to the graveyard before the ability resolves.”
- [CR 603.3b](#cr-6033b), [CR 400.7](#cr-4007)
- Source (re-verified): [`Crosis_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/crosis_2026-10-14/Crosis_Rules_Attestation.json) → “Tergrid + Tinybones, Bauble Burglar discard triggers”

## Zones, commander tax and the command zone

### crosis-11: Commander tax at six mana

**Status:** ✅ verified · **Cards:** Crosis, the Purger, Lightning Greaves, Swiftfoot Boots

**Ruling.** Crosis costs {3}{U}{B}{R} (6), then 8, then 10. Lightning Greaves and Swiftfoot Boots give haste so it can connect the turn it lands. Equip targets 'creature you control', so Greaves' shroud stops your own later equips (Regalia, Sword) while it's attached; Boots' hexproof only stops opponents. Equip the other Equipment first, or use Boots.

**Citations**

- Oracle, *Lightning Greaves*: “Equipped creature has haste and shroud.”
- [CR 702.18a](#cr-70218a), [CR 702.11b](#cr-70211b), [CR 903.8](#cr-9038)

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 105.2c

A colorless object has no color.

#### CR 105.3

Effects may change an object’s color or give a color to a colorless object. If an effect gives an object a new color, the new color replaces all previous colors the object had (unless the effect said the object became that color “in addition” to its other colors). Effects may also make a colored object become colorless.

#### CR 106.4

When an effect instructs a player to add mana, that mana goes into a player’s mana pool. From there, it can be used to pay costs immediately, or it can stay in the player’s mana pool as unspent mana. Each player’s mana pool empties at the end of each step and phase, and the player is said to lose this mana. Cards with abilities that produce mana or refer to unspent mana have received errata in the Oracle™ card reference to no longer explicitly refer to the mana pool.

#### CR 121.6

Some effects replace card draws.

#### CR 400.7

An object that moves from one zone to another becomes a new object with no memory of, or relation to, its previous existence. This rule has the following exceptions.

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 603.3b

If multiple abilities have triggered since the last time a player received priority, the abilities are placed on the stack in a two-part process. First, each player, in APNAP order, puts each triggered ability they control with a trigger condition that isn’t another ability triggering on the stack in any order they choose. (See rule 101.4.) Second, each player, in APNAP order, puts all remaining triggered abilities they control on the stack in any order they choose. Then the game once again checks for and performs state-based actions until none are performed, then abilities that triggered …

#### CR 608.2b

If the spell or ability specifies targets, it checks whether the targets are still legal. A target that’s no longer in the zone it was in when it was targeted is illegal. Other changes to the game state may cause a target to no longer be legal; for example, its characteristics may have changed or an effect may have changed the text of the spell. If the source of an ability has left the zone it was in, its last known information is used during this process. If all its targets, for every instance of the word “target,” are now illegal, the spell or ability doesn’t resolve. It’s removed from the …

#### CR 608.2c

The controller of the spell or ability follows its instructions in the order written. However, replacement effects may modify these actions. In some cases, later text on the card may modify the meaning of earlier text (for example, “Destroy target creature. It can’t be regenerated” or “Counter target spell. If that spell is countered this way, put it on top of its owner’s library instead of into its owner’s graveyard.”) Don’t just apply effects step by step without thinking in these cases—read the whole text and apply the rules of English to the text.

#### CR 613.1e

Layer 5: Color-changing effects are applied.

#### CR 614.1a

Effects that use the word “instead” are replacement effects. Most replacement effects use the word “instead” to indicate what events will be replaced with other events.

#### CR 702.6a

Equip is an activated ability of Equipment cards. “Equip [cost]” means “[Cost]: Attach this permanent to target creature you control. Activate only as a sorcery.”

#### CR 702.11b

“Hexproof” on a permanent means “This permanent can’t be the target of spells or abilities your opponents control.”

#### CR 702.16d

A permanent with protection can’t be equipped by Equipment that have the stated quality or fortified by Fortifications that have the stated quality. Such Equipment or Fortifications become unattached from that permanent as a state-based action, but remain on the battlefield. (See rule 704, “State-Based Actions.”)

#### CR 702.18a

Shroud is a static ability. “Shroud” means “This permanent or player can’t be the target of spells or abilities.”

#### CR 702.21a

Ward is a triggered ability. Ward [cost] means “Whenever this permanent becomes the target of a spell or ability an opponent controls, counter that spell or ability unless that player pays [cost].”

#### CR 704.5n

If an Equipment or Fortification is attached to an illegal permanent or to a player, it becomes unattached from that permanent or player. It remains on the battlefield.

#### CR 903.8

A player may cast a commander they own from the command zone. A commander cast from the command zone costs an additional {2} for each previous time the player casting it has cast it from the command zone that game. This additional cost is informally known as the “commander tax.”

