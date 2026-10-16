---
title: "Nicol Bolas — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Nicol Bolas — Interaction Review

> Bot cycle 51 · batch D · reviewed 2026-10-16. Deck: [Nicol Bolas](../decks/nicol-bolas.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/source-baseline/nicol-bolas.txt`](../../exports/grixis-archidekt/source-baseline/nicol-bolas.txt) · SHA-256 `1c271131d2cb3f824a292391932dbb111c3eb9653051424c16db76a6c16e91b0` |
| Rulings | **9** (8 verified · 0 uncertain · 1 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`Nicol_Bolas_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nicol_Bolas_Approval_Ready_Verification_2026-10-15.md) (Approval-ready verification sections 5–16) · [`Nicol_Bolas_Whole_List_Audit_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nicol_Bolas_Whole_List_Audit_2026-10-15.md) (Whole-list audit (Megrim cut rationale)) |

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

Nicol Bolas's trigger works on any damage he deals to an opponent, so the list makes him the source of non-combat, table-wide damage. That damage comes from Ingris, Kediss, Dragon Tempest, Chandra's Ignition, Pain for All, Dagger and Longbow. The list then pays off each discarded card (Sangromancer, Waste Not, Geth's Grimoire, Raiders' Wake, Tinybones). The one Spellbook combo is Sword of Feast and Famine + Aggravated Assault.

Rules surprises: Kediss's extra damage is noncombat (no commander damage, no retrigger); Pain for All triggers once for several blockers, even on lethal damage; Sangromancer still triggers for opponents' creatures that die alongside it. Flag: Ignition also wipes your own creature payoffs. The canonical list keeps No Mercy, not the challenger's Megrim.

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [bolas-04](#bolas-04-chandras-ignition-also-hits-your-own-creatures) | 🚩 list flag (anti-synergy) | Chandra's Ignition also hits your own creatures | Chandra's Ignition with Nicol (7 power) kills every one of your own creature payoffs (Ingris, Kediss, Sangromancer, both Tinybones, Notion Thief, Hypnotic Specter). It's a sequencing cost to document, not a list error. |

## Commander rules text and edge cases

### bolas-01: Nicol Bolas: any damage to an opponent empties that hand; the upkeep tax and Command Beacon

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Nicol Bolas, Command Beacon

**Ruling.** Nicol's discard trigger works on any damage he deals to an opponent, not just combat damage. Each opponent he damages gets a separate trigger. Each upkeep you either pay {U}{B}{R} or sacrifice him. If you sacrifice him, you may put him in the command zone, and recasting him then costs {2} more each time. Command Beacon puts him in your hand. A cast from hand has no commander tax and doesn't add to it.

**Citations**

- Oracle, *Nicol Bolas*: “Whenever Nicol Bolas deals damage to an opponent, that player discards their hand.”
- Scryfall ruling, *Nicol Bolas*: “Nicol Bolas's third ability triggers whenever it deals damage to an opponent for any reason. It's not limited to combat damage.”
- Scryfall ruling, *Command Beacon*: “If you cast a commander from your hand, the additional cost based on the number of times you've cast it from your command zone (sometimes referred to as the "commander tax") doesn't apply. Additionally, that casting won't add to the tax if you later cast the commander from the command zone.”
- [CR 603.2c](#cr-6032c), [CR 903.8](#cr-9038), [CR 903.9a](#cr-9039a)
- Source (re-verified): [`Nicol_Bolas_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nicol_Bolas_Approval_Ready_Verification_2026-10-15.md) → “Nicol Bolas's discard ability triggers whenever **Nicol Bolas deals damage to an opponent for any reason**, not only combat damage.”

## Combos and engine lines

### bolas-07: Sword of Feast and Famine + Aggravated Assault: infinite combats

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Nicol Bolas, Sword of Feast and Famine, Aggravated Assault

**Ruling.** When the Sword-equipped attacker deals combat damage to a player, the Sword untaps all your lands. That happens even if the player has no cards to discard, which is usually the case after Nicol's own trigger. In the postcombat main phase, tap at least {3}{R}{R} from lands for Aggravated Assault. That untaps your creatures and adds another combat and main phase. Repeat as long as the attacker keeps connecting. Mana from lands tapped while the Sword trigger is on the stack is lost at the end of the combat damage step, so tap for Assault in the main phase. Pro-black and the Sword's +2/+2 on Nicol (9/9) help him connect.

**Citations**

- Scryfall ruling, *Sword of Feast and Famine*: “You'll untap all lands you control even if the player can't discard a card.”
- Scryfall ruling, *Sword of Feast and Famine*: “You can tap your lands for mana while the triggered ability is on the stack. However, you'll lose any mana you produce this way if you don't spend it before the end of the current combat damage step.”
- Scryfall ruling, *Aggravated Assault*: “If you have enough mana, the ability may be activated more than once in a turn.”
- [CR 506.1](#cr-5061), [CR 500.8](#cr-5008)
- Commander Spellbook [900-3750](https://commanderspellbook.com/combo/900-3750/) (community-maintained, retrieved 2026-10-16): “Activate Aggravated Assault by paying {3}{R}{R}, untapping all creatures you control and causing you to get an additional combat and main phase after this phase.”
- Commander Spellbook [900-3750](https://commanderspellbook.com/combo/900-3750/) (community-maintained, retrieved 2026-10-16): “Lands you control can tap to produce at least {3}{R}{R}.”
- Source (re-verified): [`Nicol_Bolas_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nicol_Bolas_Approval_Ready_Verification_2026-10-15.md) → “If the equipped attacker connects and the untapped lands can produce at least five usable mana in the following main phase, Aggravated Assault can create another combat.”

## Engines and payoffs

### bolas-03: Chandra's Ignition, Pain for All, Quicksilver Dagger, Viridian Longbow and Curiosity: the creature is the source

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Nicol Bolas, Chandra's Ignition, Pain for All, Quicksilver Dagger, Viridian Longbow, Curiosity

**Ruling.** Each of these has the enchanted, equipped or targeted creature deal the damage, so Nicol's trigger applies:
- **Chandra's Ignition:** Nicol deals 7 to each opponent, using his power when it resolves.
- **Pain for All:** its ETB damage makes Nicol deal 7. After that, whenever Nicol is dealt damage, he deals that much to each opponent. Damage from several sources at once, like multiple blockers, triggers it only once with the total. It still triggers if the damage is lethal.
- **Quicksilver Dagger and Viridian Longbow:** tap to ping for 1 without attacking.
- **Curiosity:** draws one card per damage event to an opponent, combat or not. It doesn't trigger on damage to planeswalkers.

**Citations**

- Scryfall ruling, *Chandra's Ignition*: “The creature is the source of the damage, not Chandra's Ignition. For example, Chandra's Ignition can have a white creature deal damage to a creature with protection from red.”
- Scryfall ruling, *Quicksilver Dagger*: “The enchanted creature is the source of both the damage ability and the resulting damage, not Quicksilver Dagger.”
- Scryfall ruling, *Pain for All*: “If lethal damage is dealt to the enchanted creature, Pain for All’s last ability still triggers.”
- Scryfall ruling, *Pain for All*: “If the enchanted creature is dealt damage by multiple sources at once, such as by two creatures blocking it, Pain for All’s last ability triggers only once. When that triggered ability resolves, the enchanted creature deals damage equal to the total amount of damage dealt to it to each opponent.”
- Scryfall ruling, *Curiosity*: “Any damage dealt by the enchanted creature to an opponent will cause Curiosity to trigger, not just combat damage.”
- [CR 120.2](#cr-1202), [CR 603.2c](#cr-6032c)
- Source (re-verified): [`Nicol_Bolas_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nicol_Bolas_Approval_Ready_Verification_2026-10-15.md) → “The creature, not the sorcery, is the damage source.”

## Timing and priority

### bolas-08: Haste for an eight-drop: Arena of Glory, Dragon Tempest, Greaves/Boots, Hall of the Bandit Lord

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Nicol Bolas, Arena of Glory, Dragon Tempest, Lightning Greaves, Swiftfoot Boots, Hall of the Bandit Lord

**Ruling.** Arena of Glory's exert mana gives haste to a creature spell it helps pay for, including any part of an additional cost. The mana itself can be spent on anything. Exert means Arena stays tapped during your next untap step. Arena enters untapped only if you already control a Mountain; one entering at the same time doesn't count. Dragon Tempest gives Nicol haste as he enters because he has flying.

**Citations**

- Oracle, *Arena of Glory*: “{R}, {T}, Exert this land: Add {R}{R}. If any of that mana is spent on a creature spell, it gains haste until end of turn. (An exerted permanent won't untap during your next untap step.)”
- Scryfall ruling, *Arena of Glory*: “If mana generated with Arena of Glory's last ability is spent to pay any part of a creature spell's cost, including an alternative or additional cost, that creature spell (and the resulting creature) will gain haste until end of turn.”
- Scryfall ruling, *Arena of Glory*: “You must already control a Mountain as Arena of Glory enters the battlefield for it to enter untapped. If it enters the battlefield at the same time as a Mountain when you control no other Mountains, it will enter tapped.”
- [CR 702.10](#cr-70210)
- Source (re-verified): [`Nicol_Bolas_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nicol_Bolas_Approval_Ready_Verification_2026-10-15.md) → “Arena of Glory can grant Nicol haste when its exerted mana is spent on his creature spell.”

## Trigger ordering

### bolas-02: Ingris, Kediss and Dragon Tempest make Nicol the source of table-wide damage

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Nicol Bolas, Ingris Stingerquill, Kediss, Emberclaw Familiar, Dragon Tempest, Cavern of Souls

**Ruling.** Here's how each card makes Nicol deal damage:
- **Ingris:** when Nicol attacks, he deals 1 damage to each opponent. That happens before blockers, so the whole table discards even if he's later blocked.
- **Kediss:** when Nicol deals combat damage to one opponent, he deals the same amount to each other opponent. That extra damage is noncombat, so it doesn't count as commander damage and doesn't retrigger Kediss. It still makes every opponent discard.
- **Dragon Tempest:** gives Nicol haste when he enters and has him deal X damage to any target. X is counted when the trigger resolves, and the damage happens even if Nicol has left by then.

Ingris is an Elder Sphinx, so Cavern of Souls naming Elder covers both Ingris and Nicol.

**Citations**

- Oracle, *Ingris Stingerquill*: “Whenever a creature you control attacks, that creature deals 1 damage to each opponent.”
- Oracle, *Kediss, Emberclaw Familiar*: “Whenever a commander you control deals combat damage to an opponent, it deals that much damage to each other opponent.”
- Scryfall ruling, *Kediss, Emberclaw Familiar*: “The damage the commander deals as a result of Kediss's triggered ability isn't combat damage. It isn't tracked with combat damage dealt by commanders and won't cause Kediss's ability to trigger again.”
- Scryfall ruling, *Dragon Tempest*: “If a Dragon entering the battlefield causes Dragon Tempest’s second ability to trigger but leaves the battlefield before that ability resolves, that Dragon still deals damage.”
- Scryfall ruling, *Dragon Tempest*: “The two abilities aren’t mutually exclusive. If a Dragon with flying (which is most of them) enters the battlefield under your control, both abilities will trigger.”
- [CR 508.1m](#cr-5081m), [CR 510.2](#cr-5102), [CR 603.2c](#cr-6032c)
- Source (re-verified): [`Nicol_Bolas_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nicol_Bolas_Approval_Ready_Verification_2026-10-15.md) → “Ingris is also an Elder creature, so Cavern of Souls naming Elder can cast both Nicol Bolas and Ingris with uncounterable colored mana.”

### bolas-05: Whole-hand discard sets off per-card payoffs

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Nicol Bolas, Sangromancer, Waste Not, Geth's Grimoire, Raiders' Wake, Tinybones, Bauble Burglar, Tinybones, Trinket Thief

**Ruling.** "Discards their hand" is one event made of many discards. Each "whenever an opponent discards a card" ability triggers once per card. A five-card hand gives five Sangromancer triggers (3 life each), five Geth's Grimoire draws, five Raiders' Wake losses of 2 life, and five Tinybones exiles. Waste Not triggers once per card too, by card type. Tinybones, Trinket Thief checks only once, at the end step, whether anyone discarded.

**Citations**

- Oracle, *Sangromancer*: “Whenever an opponent discards a card, you may gain 3 life.”
- Oracle, *Raiders' Wake*: “Whenever an opponent discards a card, that player loses 2 life.”
- [CR 603.2c](#cr-6032c), [CR 701.9a](#cr-7019a)
- Source (re-verified): [`Nicol_Bolas_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nicol_Bolas_Approval_Ready_Verification_2026-10-15.md) → “A five-card hand discarded through Nicol therefore creates five separate Sangromancer triggers for that opponent.”

### bolas-06: Tinybones, Bauble Burglar vs Tergrid on the same discarded permanent

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Nicol Bolas, Tinybones, Bauble Burglar, Tergrid, God of Fright // Tergrid's Lantern

**Ruling.** When an opponent discards a permanent card, both Tinybones (exile it) and Tergrid (put it onto the battlefield) trigger. You control both, so you choose their order on the stack, and the one that resolves first gets the card. Use Tergrid for permanents you want right away. Use Tinybones for spells, or permanents you'd rather cast later on your turn, paying their costs and following timing rules.

**Citations**

- Oracle, *Tinybones, Bauble Burglar*: “Whenever an opponent discards a card, exile it from their graveyard with a stash counter on it.”
- Oracle, *Tergrid, God of Fright // Tergrid's Lantern*: “Whenever an opponent sacrifices a nontoken permanent or discards a permanent card, you may put that card from a graveyard onto the battlefield under your control.”
- Scryfall ruling, *Tinybones, Bauble Burglar*: “You pay all costs and follow all normal timing rules for cards played with the permission granted by Tinybones's second ability. For example, if the exiled card is a land card, you may play it only during your main phase while the stack is empty.”
- [CR 603.3b](#cr-6033b)
- Source (re-verified): [`Nicol_Bolas_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nicol_Bolas_Approval_Ready_Verification_2026-10-15.md) → “If Tergrid moves the permanent first, Tinybones can no longer exile that card from the graveyard; if Tinybones exiles it first, Tergrid can no longer return it from the graveyard.”

## What the list depends on

### bolas-04: Chandra's Ignition also hits your own creatures

**Status:** 🚩 list flag · **Evidence:** fact · **Cards:** Nicol Bolas, Chandra's Ignition, Ingris Stingerquill, Kediss, Emberclaw Familiar, Sangromancer, Tinybones, Bauble Burglar, Tinybones, Trinket Thief, Notion Thief, Hypnotic Specter

**Ruling.** Ignition has Nicol deal 7 damage to each other creature, yours included. It kills Ingris, Kediss, Sangromancer, both Tinybones, Notion Thief and Hypnotic Specter along with the opponents' board. There's one upside: Sangromancer's dies trigger looks back in time, so it still triggers for each opponent's creature that dies alongside it. Cast Ignition as a reset when your own payoffs aren't needed, not as a free hand wipe.

**List flag (anti-synergy).** Chandra's Ignition with Nicol (7 power) kills every one of your own creature payoffs (Ingris, Kediss, Sangromancer, both Tinybones, Notion Thief, Hypnotic Specter). It's a sequencing cost to document, not a list error.

**Citations**

- Oracle, *Chandra's Ignition*: “Target creature you control deals damage equal to its power to each other creature and each opponent.”
- Scryfall ruling, *Sangromancer*: “If one or more creatures an opponent controls are put into the graveyard at the same time as Sangromancer, Sangromancer's first ability will trigger that many times.”
- [CR 603.10a](#cr-60310a)
- Source (re-verified): [`Nicol_Bolas_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nicol_Bolas_Approval_Ready_Verification_2026-10-15.md) → “This simultaneously acts as a commander-native table hand wipe and a broad creature sweeper.”

### bolas-09: No Mercy is symmetric toward your own creatures (canonical list keeps No Mercy, not Megrim)

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Nicol Bolas, No Mercy

**Ruling.** No Mercy destroys any creature that deals damage to you, including your own creatures. Nothing in this list makes your own creatures damage you, so in practice it only punishes attackers. The canonical source-baseline list keeps No Mercy, and Megrim was cut for Sangromancer. The later challenger swap (No Mercy → Megrim) is not in the canonical list, so this review covers No Mercy.

**Citations**

- Scryfall ruling, *No Mercy*: “No Mercy’s ability triggers whenever any creature, including creatures you control, deals damage to you, not only combat damage.”
- Source (re-verified): [`Nicol_Bolas_Whole_List_Audit_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nicol_Bolas_Whole_List_Audit_2026-10-15.md) → “| Megrim | Redundant three-mana version of retained Liliana's Caress; Sangromancer adds a distinct discard payoff instead. |”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 120.2

Any object can deal damage.

#### CR 500.8

Some effects can add phases to a turn. They do this by adding the phases directly after the specified phase. If multiple extra phases are created after the same phase, the most recently created phase will occur first.

#### CR 506.1

The combat phase has five steps, which proceed in order: beginning of combat, declare attackers, declare blockers, combat damage, and end of combat. The declare blockers and combat damage steps are skipped if no creatures are declared as attackers or put onto the battlefield attacking (see rule 508.8). There are two combat damage steps if any attacking or blocking creature has first strike (see rule 702.7) or double strike (see rule 702.4).

#### CR 508.1m

Any abilities that trigger on attackers being declared trigger.

#### CR 510.2

Second, all combat damage that’s been assigned is dealt simultaneously. This turn-based action doesn’t use the stack. No player has the chance to cast spells or activate abilities between the time combat damage is assigned and the time it’s dealt.

#### CR 603.2c

An ability triggers only once each time its trigger event occurs. However, it can trigger repeatedly if one event contains multiple occurrences.

#### CR 603.3b

If multiple abilities have triggered since the last time a player received priority, the abilities are placed on the stack in a two-part process. First, each player, in APNAP order, puts each triggered ability they control with a trigger condition that isn’t another ability triggering on the stack in any order they choose. (See rule 101.4.) Second, each player, in APNAP order, puts all remaining triggered abilities they control on the stack in any order they choose. Then the game once again checks for and performs state-based actions until none are performed, then abilities that triggered …

#### CR 603.10a

Some zone-change triggers look back in time. These are leaves-the-battlefield abilities, abilities that trigger when a player sacrifices a permanent, abilities that trigger when a card leaves a graveyard, and abilities that trigger when an object that all players can see is put into a hand or library.

#### CR 701.9a

To discard a card, move it from its owner’s hand to that player’s graveyard.

#### CR 702.10

Haste

#### CR 903.8

A player may cast a commander they own from the command zone. A commander cast from the command zone costs an additional {2} for each previous time the player casting it has cast it from the command zone that game. This additional cost is informally known as the “commander tax.”

#### CR 903.9a

If a commander is in a graveyard or in exile and that object was put into that zone since the last time state-based actions were checked, its owner may put it into the command zone. This is a state-based action. See rule 704.

