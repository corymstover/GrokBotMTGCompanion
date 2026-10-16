---
title: "The Madcap Jester — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# The Madcap Jester — Interaction Review

> Bot cycle 56 · batch F · reviewed 2026-10-16. Deck: [The Madcap Jester](../decks/the-madcap-jester.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/the-madcap-jester.txt`](../../exports/grixis-archidekt/the-madcap-jester.txt) · SHA-256 `1ce93f38a1dc81a07c3f499beb168ba2ac0512da1718ea02ab4204cefb0d8f03` |
| Rulings | **7** (6 verified · 1 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`The_Madcap_Jester_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/the_madcap_jester_2026-10-15/gate_output/The_Madcap_Jester_Rules_Attestation.json) (Rules attestation (13 items, all PASS) re-verified) · [`The_Madcap_Jester_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/The_Madcap_Jester_Approval_Ready_Verification_2026-10-15.md) (Approval-ready verification) |

## Contents
- [Summary](#summary)
- [Flags and open questions](#flags-and-open-questions)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [Replacement and prevention effects](#replacement-and-prevention-effects)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [Legality and project exceptions](#legality-and-project-exceptions)
- [Rules cited](#rules-cited)

## Summary

The Madcap Jester attacks to make each opponent exile their top card. Any library exile your spells or abilities cause lets you play those cards until the end of your next turn with any mana. Exile effects (Ashiok, Circu, Scepter, Extract, Bitter Ordeal, Tasha's) and cast-from-exile payoffs (Dragon's Smile, Bilbo, Archaeologist, Nalfeshnee, Prosper, Wild-Magic Sorcerer) are the engine. Thassa's Oracle + Consultation / Tainted Pact and Breach + LED / Petal + Brain Freeze are the wins. All 4 Spellbook lines and all 13 attestation items are checked against the canonical list. The deck stays PENDING_RELEASE: Jester and Dragon's Smile are 2026-11-13 project exceptions, and Jester has no official rulings yet.

Rules surprises: the opponent doing the exiling still counts as your ability causing it; Scepter's face-down cards are playable because you can look at them; Dragon's Smile's own exile gets Jester's longer window. One uncertain item: whether Dauthi-replaced mill counts. No list errors.

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [jester-02](#jester-02-dauthi-voidwalker-turns-your-mill-into-exile-does-jester-see-it) | ⚠️ uncertain | Dauthi Voidwalker turns your mill into exile: does Jester see it? | No official ruling (Jester unreleased) on whether a mill replaced by Dauthi counts as your spell "causing" cards to be exiled from an opponent's library; rules-derived from CR 614.6. |

## Commander rules text and edge cases

### jester-01: Jester's access trigger: any library exile caused by a spell or ability you control

**Status:** ✅ verified · **Evidence:** fact · **Cards:** The Madcap Jester, Ashiok, Nightmare Weaver, Circu, Dimir Lobotomist, Extract, Sadistic Sacrament, Bitter Ordeal, Tasha's Hideous Laughter, Jester's Cap, Psychic Surgery, Inside Information

**Ruling.** Jester's first ability is an ability you control. Even though each opponent does the exiling, your ability caused it, so the second ability triggers. The same goes for any spell or ability you control that exiles cards straight from an opponent's library:
- Ashiok's +2, Circu's cast triggers when they target an opponent, and Psychic Surgery.
- Extract, Sadistic Sacrament, Jester's Cap and Tasha's Hideous Laughter.
- Bitter Ordeal and each of its gravestorm copies, since copies are spells you control.

Those cards can be played until the end of your next turn with mana of any type, but normal timing, costs and land drops still apply. Exiling from your own library (Prosper's Mystic Arcanum, Wild-Magic Sorcerer's cascade) doesn't count.

Inside Information grants its own this-turn permission with a pay-life cost. Its cards are also covered by Jester, so you choose which permission to use. Jester has no official rulings yet (future release). This reading follows directly from the Oracle text and CR 603.2.

**Citations**

- Oracle, *The Madcap Jester*: “Whenever The Madcap Jester attacks, each opponent exiles the top card of their library.”
- Oracle, *The Madcap Jester*: “Whenever a spell or ability you control causes one or more cards to be exiled from an opponent's library, you may play those cards until the end of your next turn. Mana of any type can be spent to cast spells this way.”
- Scryfall ruling, *Inside Information*: “You must follow all normal timing rules when playing a land or casting a spell for cards exiled with Inside Information. For example, if an exiled card is a land card, you may play it only during your main phase while the stack is empty and only if you have an available land play remaining.”
- [CR 603.2](#cr-6032), [CR 109.4](#cr-1094), [CR 707.10](#cr-70710), [CR 305.2](#cr-3052)
- Source (re-verified): [`The_Madcap_Jester_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/the_madcap_jester_2026-10-15/gate_output/The_Madcap_Jester_Rules_Attestation.json) → “Madcap attack and access triggers”
- Source (re-verified): [`The_Madcap_Jester_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/the_madcap_jester_2026-10-15/gate_output/The_Madcap_Jester_Rules_Attestation.json) → “Ashiok Nightmare Weaver”
- Source (re-verified): [`The_Madcap_Jester_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/the_madcap_jester_2026-10-15/gate_output/The_Madcap_Jester_Rules_Attestation.json) → “Direct exile suite”
- Source (re-verified): [`The_Madcap_Jester_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/the_madcap_jester_2026-10-15/gate_output/The_Madcap_Jester_Rules_Attestation.json) → “Lightning Greaves”

## Combos and engine lines

### jester-04: Thassa's Oracle + Demonic Consultation / Tainted Pact

**Status:** ✅ verified · **Evidence:** fact · **Cards:** The Madcap Jester, Thassa's Oracle, Demonic Consultation, Tainted Pact

**Ruling.** Respond to Thassa's Oracle's trigger, or cast first and then Oracle, with Demonic Consultation naming a card not in your library, or with Tainted Pact. Your library is exiled, Oracle's devotion check sees 0 cards, and you win (Spellbook 742-1295, 1295-3093). Every card in the exported list is a different card (100 lines of one copy each), so Tainted Pact never hits a duplicate name. Consultation can't be pointed at an opponent.

**Citations**

- Scryfall ruling, *Thassa's Oracle*: “If your devotion to blue is zero at the time the triggered ability of Thassa's Oracle resolves, you don't look at or move any cards in your library. If you have no cards in your library, you win the game.”
- Scryfall ruling, *Demonic Consultation*: “There is no way to make this card affect your opponent. It affects "you", and "you" means the controller of the spell. It has no targets.”
- [CR 104.2b](#cr-1042b)
- Commander Spellbook [1295-3093](https://commanderspellbook.com/combo/1295-3093/) (community-maintained, retrieved 2026-10-16): “No two cards in library share a name.”
- Commander Spellbook [742-1295](https://commanderspellbook.com/combo/742-1295/) (community-maintained, retrieved 2026-10-16): “Thassa's Oracle enters the battlefield, causing you to win the game.”
- Source (re-verified): [`The_Madcap_Jester_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/the_madcap_jester_2026-10-15/gate_output/The_Madcap_Jester_Rules_Attestation.json) → “Thassa Oracle plus Demonic Consultation”
- Source (re-verified): [`The_Madcap_Jester_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/the_madcap_jester_2026-10-15/gate_output/The_Madcap_Jester_Rules_Attestation.json) → “Thassa Oracle plus Tainted Pact”

### jester-05: Underworld Breach + Lion's Eye Diamond / Lotus Petal + Brain Freeze

**Status:** ✅ verified · **Evidence:** fact · **Cards:** The Madcap Jester, Underworld Breach, Lion's Eye Diamond, Lotus Petal, Brain Freeze

**Ruling.** Breach gives cards in your graveyard escape. Recasting LED or Lotus Petal grows the storm count while making mana, and Brain Freeze's copies mill your own library or an opponent's (Spellbook 1368-3518-4856, 1368-1414-4856). Then win with Oracle. Storm copies aren't cast, so they don't add to storm. Escape exiles cards from your own graveyard, so Dauthi doesn't affect this line.

**Citations**

- Scryfall ruling, *Brain Freeze*: “The copies are put directly onto the stack. They aren't cast and won't be counted by other spells with storm cast later in the turn.”
- Scryfall ruling, *Underworld Breach*: “If you cast a spell with its escape permission, you can't choose to apply any other alternative costs or to cast it without paying its mana cost. If it has any additional costs, you must pay those.”
- [CR 702.138a](#cr-702138a), [CR 702.40a](#cr-70240a)
- Commander Spellbook [1368-3518-4856](https://commanderspellbook.com/combo/1368-3518-4856/) (community-maintained, retrieved 2026-10-16): “Activate Lion's Eye Diamond by discarding your hand and sacrificing it, adding {U}{U}{U}.”
- Source (re-verified): [`The_Madcap_Jester_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/the_madcap_jester_2026-10-15/gate_output/The_Madcap_Jester_Rules_Attestation.json) → “Underworld Breach LED Brain Freeze”

## Engines and payoffs

### jester-06: Casting from exile: Dragon's Smile {0}, Bilbo, Archaeologist, Nalfeshnee, Prosper, Wild-Magic Sorcerer

**Status:** ✅ verified · **Evidence:** fact · **Cards:** The Madcap Jester, Dragon's Smile, Bilbo, Thief in the Night, Passionate Archaeologist, Nalfeshnee, Prosper, Tome-Bound, Wild-Magic Sorcerer

**Ruling.** Payoffs for casting from exile:
- **Dragon's Smile:** once in each of your turns, a spell cast from exile can cost {0} instead of its mana cost. Opponents' cards under Jester count. It's an alternative cost, so it can't stack with Inside Information's pay-life cost. Its combat-damage exile is also caused by an ability you control, so Jester extends those cards to the end of your next turn.
- **Bilbo:** each of those spells costs {1} less.
- **Passionate Archaeologist:** Jester deals damage equal to the spell's mana value.
- **Nalfeshnee:** copies the spell.
- **Prosper:** makes a Treasure for any card played from exile, not only its own.
- **Wild-Magic Sorcerer:** gives cascade to the first spell you cast from exile each turn.

Dragon's Smile and Jester are unreleased cards kept only as registered project exceptions.

**Citations**

- Oracle, *Dragon's Smile*: “Once during each of your turns, you may pay {0} rather than pay the mana cost for a spell you cast from exile.”
- Oracle, *Passionate Archaeologist*: “Commander creatures you own have "Whenever you cast a spell from exile, this creature deals damage equal to that spell's mana value to target opponent."”
- Scryfall ruling, *Prosper, Tome-Bound*: “The Pact Boon ability triggers whenever you play any cards from exile, not just those exiled with the Mystic Arcanum ability.”
- Scryfall ruling, *Wild-Magic Sorcerer*: “The first spell you cast from exile each turn will have cascade, even if it's not the first spell you've cast that turn.”
- [CR 118.9](#cr-1189), [CR 702.85a](#cr-70285a)
- Source (re-verified): [`The_Madcap_Jester_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/the_madcap_jester_2026-10-15/gate_output/The_Madcap_Jester_Rules_Attestation.json) → “Dragon’s Smile alternative cost”
- Source (re-verified): [`The_Madcap_Jester_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/the_madcap_jester_2026-10-15/gate_output/The_Madcap_Jester_Rules_Attestation.json) → “Cast-from-exile payoffs”

## Replacement and prevention effects

### jester-02: Dauthi Voidwalker turns your mill into exile: does Jester see it?

**Status:** ⚠️ uncertain · **Evidence:** hypothesis · **Cards:** The Madcap Jester, Dauthi Voidwalker, Brain Freeze, Bitter Ordeal

**Ruling.** With Dauthi out, cards Brain Freeze mills from an opponent's library are exiled with void counters instead (CR 614.6: the modified event happens). Your spell caused that event, so the attestation counts it as "a spell you control causes cards to be exiled from an opponent's library." That's plausible, but no official ruling covers a replacement-modified event against a "causes ... to be exiled" trigger, and Jester has no rulings yet. Treat it as a hypothesis until Jester's release notes.

Dauthi doesn't change your own self-mill for Breach, and it doesn't make opponent-caused mill count. It also stops opponents' permanents from reaching the graveyard, which shrinks Bitter Ordeal's gravestorm count.

**Uncertain.** No official ruling (Jester unreleased) on whether a mill replaced by Dauthi counts as your spell "causing" cards to be exiled from an opponent's library; rules-derived from CR 614.6.

**Citations**

- Oracle, *Dauthi Voidwalker*: “If a card would be put into an opponent's graveyard from anywhere, instead exile it with a void counter on it.”
- Scryfall ruling, *Dauthi Voidwalker*: “If your opponent discards a card while you control Dauthi Voidwalker, abilities that function when that card is discarded still work, even though that card never reaches that player's graveyard. In addition, spells or abilities that check the characteristics of the discarded card can find that card in exile.”
- [CR 614.6](#cr-6146), [CR 701.17c](#cr-70117c)
- Source (re-verified): [`The_Madcap_Jester_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/the_madcap_jester_2026-10-15/gate_output/The_Madcap_Jester_Rules_Attestation.json) → “Dauthi replacement plus controlled mill”
- Source (re-verified): [`The_Madcap_Jester_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/the_madcap_jester_2026-10-15/gate_output/The_Madcap_Jester_Rules_Attestation.json) → “Brain Freeze with Dauthi”

## Zones, commander tax and the command zone

### jester-03: Jester's Scepter: face-down exile you can look at is playable

**Status:** ✅ verified · **Evidence:** fact · **Cards:** The Madcap Jester, Jester's Scepter

**Ruling.** Jester's Scepter exiles the top five cards of the target player's library face down and lets you look at them. If the target is an opponent, Jester's permission covers them. A face-down exiled card has no characteristics, but a player who may look at it can begin to cast it. It's turned face up just before you play it. Only you can see Scepter's cards, so opponents can't tell what you can play. If you later put a Scepter card into its owner's graveyard for the counter ability, you lose access to that card.

**Citations**

- Oracle, *Jester's Scepter*: “When this artifact enters, exile the top five cards of target player's library face down. You may look at those cards for as long as they remain exiled.”
- Scryfall ruling, *Jester's Scepter*: “You can see the cards that are exiled with Jester’s Scepter, but no one else can.”
- [CR 406.3a](#cr-4063a), [CR 601.3f](#cr-6013f)
- Source (re-verified): [`The_Madcap_Jester_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/the_madcap_jester_2026-10-15/gate_output/The_Madcap_Jester_Rules_Attestation.json) → “Jesters Scepter face-down exile”

## Legality and project exceptions

### jester-07: Pending release: The Madcap Jester and Dragon's Smile stay pending

**Status:** ✅ verified · **Evidence:** fact · **Cards:** The Madcap Jester, Dragon's Smile

**Ruling.** The Madcap Jester and Dragon's Smile are new cards not yet released. They're kept under the registered project future-release exceptions, and Wizards says they become Commander-legal on 2026-11-13. This review checks their interactions against the canonical list but doesn't change the deck's PENDING_RELEASE state or claim the deck is legal now. Their rulings should be re-checked against the release notes, especially jester-02.

**Citations**

- Oracle, *Dragon's Smile*: “Once during each of your turns, you may pay {0} rather than pay the mana cost for a spell you cast from exile.”
- Source (re-verified): [`The_Madcap_Jester_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/the_madcap_jester_2026-10-15/gate_output/The_Madcap_Jester_Rules_Attestation.json) → “Future-release project exceptions”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 104.2b

An effect may state that a player wins the game.

#### CR 109.4

Only objects on the stack or on the battlefield have a controller. Objects that are neither on the stack nor on the battlefield aren’t controlled by any player. See rule 108.4. There are six exceptions to this rule:

#### CR 118.9

Some spells have alternative costs. An alternative cost is a cost listed in a spell’s text, or applied to it from another effect, that its controller may pay rather than paying the spell’s mana cost. Alternative costs are usually phrased, “You may [action] rather than pay [this object’s] mana cost,” or “You may cast [this object] without paying its mana cost.” Note that some alternative costs are listed in keywords; see rule 702.

#### CR 305.2

A player can normally play one land during their turn; however, continuous effects may increase this number.

#### CR 406.3a

A card exiled face down has no characteristics, but the spell or ability that exiled it may allow it to be played from exile. Unless that card is being cast face down (see rule 708.4), the card is turned face up just before the player announces that they are playing the card (see rule 601.2).

#### CR 601.3f

Some effects allow a player to cast a spell with certain qualities from among face-down cards in exile. A player may begin to cast such a spell only if they can look at the face-down card in exile.

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 614.6

If an event is replaced, it never happens. A modified event occurs instead, which may in turn trigger abilities. Note that the modified event may contain instructions that can’t be carried out, in which case the impossible instruction is simply ignored.

#### CR 701.17c

An effect that refers to a milled card can find that card in the zone it moved to from the library, as long as that zone is a public zone.

#### CR 702.40a

Storm is a triggered ability that functions on the stack. “Storm” means “When you cast this spell, copy it for each other spell that was cast before it this turn. If the spell has any targets, you may choose new targets for any of the copies.”

#### CR 702.85a

Cascade is a triggered ability that functions only while the spell with cascade is on the stack. “Cascade” means “When you cast this spell, exile cards from the top of your library until you exile a nonland card whose mana value is less than this spell’s mana value. You may cast that card without paying its mana cost if the resulting spell’s mana value is less than this spell’s mana value. Then put all cards exiled this way that weren’t cast on the bottom of your library in a random order.”

#### CR 702.138a

Escape represents a static ability that functions while the card with escape is in a player’s graveyard. “Escape [cost]” means “You may cast this card from your graveyard by paying [cost] rather than paying its mana cost.” Casting a spell using its escape ability follows the rules for paying alternative costs in rules 601.2b and 601.2f–h.

#### CR 707.10

To copy a spell, activated ability, or triggered ability means to put a copy of it onto the stack; a copy of a spell isn’t cast and a copy of an activated ability isn’t activated. A copy of a spell or ability copies both the characteristics of the spell or ability and all decisions made for it, including modes, targets, the value of X, and additional or alternative costs. (See rule 601, “Casting Spells.”) Choices that are normally made on resolution are not copied. If an effect of the copy refers to objects used to pay its costs, it uses the objects used to pay the costs of the original spell …

