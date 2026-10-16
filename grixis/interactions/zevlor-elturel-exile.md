---
title: "Zevlor, Elturel Exile — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Zevlor, Elturel Exile — Interaction Review

> Bot cycle 56 · batch F · reviewed 2026-10-16. Deck: [Zevlor, Elturel Exile](../decks/zevlor-elturel-exile.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/zevlor-elturel-exile.txt`](../../exports/grixis-archidekt/zevlor-elturel-exile.txt) · SHA-256 `6a8966fca69ad99c1796104a14f6aae186446c80db5cc2e2744ee283aad5e022` |
| Rulings | **4** (4 verified · 0 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md) (Approval-ready verification (no rules attestation JSON in source)) |

## Contents
- [Summary](#summary)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Engines and payoffs](#engines-and-payoffs)
- [Trigger ordering](#trigger-ordering)
- [Rules cited](#rules-cited)

## Summary

Zevlor, Elturel Exile copies your next instant or sorcery that targets only a single opponent or opponent's permanent, once for each other opponent. The deck stacks activations (Bracers, Pemmin's Aura, Minamo, Patriar's Seal, Training Grounds, Omen Hawker) and copy multipliers (Twinning Staff, Exterminator Magmarch, magecraft), and runs target-opponent payloads (Cruel Ultimatum, Worst Fears, River's Rebuke, Acquire, Jeska's Will). The source has no rules attestation JSON, so this review uses the approval-ready verification. The canonical list matches its 21-card delta. The one Spellbook line has every piece in the list.

Rules surprises: errata adds "only", so multi-target spells don't count; copies happen even if the original is countered and keep its modes and X; overloaded Rift doesn't count; Pemmin's shroud blocks your own Minamo and Seal; Twinning Staff adds one copy per copy event. No flags. No list errors.

## Commander rules text and edge cases

### zevlor-01: Zevlor's delayed trigger: "only" a single target; copies aren't cast; copies survive a countered original

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Zevlor, Elturel Exile, Rakdos Charm, Cyclonic Rift, Jeska's Will

**Ruling.** Zevlor's activation sets up a delayed trigger for your next instant or sorcery this turn that targets only one opponent or one permanent an opponent controls. The Oracle text was corrected to add "only", so a spell with two or more chosen targets doesn't count, even if one of them is an opponent. A spell that could take more targets counts if you chose just one.

The copies are created on the stack, not cast. They keep the original's modes and X, and count any additional costs as paid. The trigger can copy the spell even if the original has already been countered.

On individual cards:
- **Rakdos Charm:** its graveyard and artifact modes qualify. Its third mode has no target.
- **Cyclonic Rift:** qualifies cast normally. Overloaded, it has no targets.
- **Jeska's Will:** with both modes chosen it still targets one opponent. Each copy adds {R} for that opponent's hand and exiles three more of your cards.

**Citations**

- Oracle, *Zevlor, Elturel Exile*: “{2}, {T}: When you next cast an instant or sorcery spell that targets only a single opponent or a single permanent an opponent controls this turn, for each other opponent, choose that player or a permanent they control, copy that spell, and the copy targets the chosen player or permanent.”
- Scryfall ruling, *Zevlor, Elturel Exile*: “Zevlor, Elturel Exile has received an update to its Oracle text. The word “only” was inadvertently left off the printed card. The updated text is included above. Notably, an instant or sorcery spell with multiple targets will not cause the delayed triggered ability to trigger, even if only one of those targets is an opponent or an permanent an opponent controls.”
- Scryfall ruling, *Zevlor, Elturel Exile*: “The delayed triggered ability can copy the spell that caused it to trigger even if that spell has been countered by the time that ability resolves.”
- Scryfall ruling, *Zevlor, Elturel Exile*: “If the spell is modal (that is, it has a bulleted list of choices), the copies will have the same mode(s). You can't choose different ones.”
- [CR 603.7a](#cr-6037a), [CR 707.10](#cr-70710), [CR 702.96b](#cr-70296b)
- Source (re-verified): [`Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md) → “**Cyclonic Rift** qualifies in normal single-target mode.”
- Source (re-verified): [`Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md) → “**Jeska's Will** qualifies when both modes are chosen while controlling Zevlor”

## Engines and payoffs

### zevlor-03: Activation economy: Training Grounds, Omen Hawker, Pemmin's Aura, Minamo, Patriar's Seal, Swiftfoot Boots

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Zevlor, Elturel Exile, Training Grounds, Omen Hawker, Pemmin's Aura, Minamo, School at Water's Edge, Patriar's Seal, Swiftfoot Boots

**Ruling.** Making activations cheaper and untapping Zevlor:
- **Training Grounds** cuts the {2} to {1}, which is the minimum.
- **Omen Hawker's** {C}{U} for abilities pays the whole activation.
- **Pemmin's Aura** on Zevlor untaps him for {U} as often as you can pay, without targeting.
- **Minamo and Patriar's Seal** target and untap legendary Zevlor.
- **Omen Hawker + Pemmin's Aura on Hawker** gives unlimited ability-only mana (Spellbook 3525-3772). That pays Zevlor's {2} every time, but Zevlor still needs his own untaps.

Pemmin's shroud blocks your own Minamo and Seal. Swiftfoot Boots' hexproof doesn't, which is why it replaced Lightning Greaves.

**Citations**

- Oracle, *Pemmin's Aura*: “{U}: Untap enchanted creature.”
- Oracle, *Omen Hawker*: “{T}: Add {C}{U}. Spend this mana only to activate abilities.”
- Scryfall ruling, *Training Grounds*: “Training Grounds can reduce the part of an activation cost represented by generic mana symbols down to nothing, as long as it still costs at least one mana. For example, if an activation cost is {2}{G}, you'd have to pay only {G}. If an activation cost is {2}, though, you'd still have to pay {1}.”
- [CR 602.1](#cr-6021), [CR 702.11b](#cr-70211b), [CR 702.18a](#cr-70218a)
- Commander Spellbook [3525-3772](https://commanderspellbook.com/combo/3525-3772/) (community-maintained, retrieved 2026-10-16): “Activate Pemmin's Aura's first ability by paying {U}, untapping Omen Hawker.”
- Source (re-verified): [`Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md) → “**Pemmin's Aura** can untap enchanted Zevlor repeatedly for {U} in the same turn.”
- Source (re-verified): [`Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md) → “**Swiftfoot Boots** is deliberately used instead of Lightning Greaves”

### zevlor-04: Target-opponent payloads at table scale: Cruel Ultimatum, Great Intelligence's Plan, River's Rebuke, Acquire, Portent, Worst Fears

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Zevlor, Elturel Exile, Cruel Ultimatum, Great Intelligence's Plan, River's Rebuke, Acquire, Portent, Worst Fears, Blue Sun's Twilight

**Ruling.** Each copy hits a different opponent, and the "you" parts happen for every copy:
- **Cruel Ultimatum:** across three resolutions you draw nine, gain 15 and return three creature cards.
- **Great Intelligence's Plan:** draws three for you each time.
- **River's Rebuke:** bounces every opponent's nonland permanents.
- **Acquire:** takes an artifact from each opponent's library.
- **Portent:** each resolution makes its own delayed draw.
- **Worst Fears:** each copy controls a different opponent's next turn. Player-control effects only overwrite each other on the same player.
- **Blue Sun's Twilight:** copies keep X.

**Citations**

- Oracle, *Cruel Ultimatum*: “Target opponent sacrifices a creature of their choice, discards three cards, then loses 5 life. You return a creature card from your graveyard to your hand, draw three cards, then gain 5 life.”
- Oracle, *Worst Fears*: “You control target player during that player's next turn. Exile Worst Fears. (You see all cards that player could see and make all decisions for them.)”
- Scryfall ruling, *Worst Fears*: “Multiple player-controlling effects that affect the same player overwrite each other. The last one to be created is the one that works.”
- Scryfall ruling, *Zevlor, Elturel Exile*: “If the spell has an X whose value was determined as it was cast (like Fireball does), the copy has the same value of X.”
- [CR 707.10](#cr-70710), [CR 723.5](#cr-7235)
- Source (re-verified): [`Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md) → “**Cruel Ultimatum** targets one opponent.”
- Source (re-verified): [`Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md) → “**Worst Fears** remains a high-end identity finisher”

## Trigger ordering

### zevlor-02: Stacking Zevlor: several activations, Illusionist's Bracers, Twinning Staff, Exterminator Magmarch

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Zevlor, Elturel Exile, Illusionist's Bracers, Twinning Staff, Exterminator Magmarch, Archmage Emeritus, Storm-Kiln Artist

**Ruling.** Ways to get more copies:
- **More activations:** each one before the spell is a separate delayed trigger, and all of them trigger on the same next spell. Illusionist's Bracers on Zevlor copies the activation, giving a second delayed trigger.
- **Twinning Staff:** each copy event gets one extra copy with new targets of your choice. The extra copy can go between the others on the stack.
- **Exterminator Magmarch:** triggers on the same cast, but only for single-nonland-permanent targets, and adds one copy at a permanent of another opponent.
- **Magecraft:** Archmage Emeritus and Storm-Kiln Artist trigger on every copy. Cast-only triggers don't.

**Citations**

- Oracle, *Twinning Staff*: “If you would copy a spell one or more times, instead copy it that many times plus an additional time. You may choose new targets for the additional copy.”
- Oracle, *Archmage Emeritus*: “Magecraft — Whenever you cast or copy an instant or sorcery spell, draw a card.”
- Scryfall ruling, *Twinning Staff*: “You choose whether the additional copy is put onto the stack before or after the original copy. If a spell is being copied more than once, you can even have the additional copy put onto the stack in between the original copies.”
- Scryfall ruling, *Exterminator Magmarch*: “The copy is created even if the spell that caused the ability to trigger has been countered by the time the ability resolves. The copy resolves before the original spell.”
- [CR 603.7b](#cr-6037b), [CR 707.10](#cr-70710), [CR 614.1a](#cr-6141a)
- Source (re-verified): [`Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md) → “Multiple Zevlor activated abilities resolved before a qualifying spell create independent delayed triggers.”
- Source (re-verified): [`Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md) → “**Illusionist's Bracers** copies Zevlor's nonmana activated ability.”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 602.1

Activated abilities have a cost and an effect. They are written as “[Cost]: [Effect.] [Activation instructions (if any).]”

#### CR 603.7a

Delayed triggered abilities are created during the resolution of spells or abilities, as the result of a replacement effect being applied, or as a result of a static ability that allows a player to take an action. A delayed triggered ability won’t trigger until it has actually been created, even if its trigger event occurred just beforehand. Other events that happen earlier may make the trigger event impossible.

#### CR 603.7b

A delayed triggered ability will trigger only once—the next time its trigger event occurs—unless it has a stated duration, such as “this turn.” If its trigger event occurs more than once simultaneously and the ability doesn’t have a stated duration, the controller of the delayed triggered ability chooses which event causes the ability to trigger.

#### CR 614.1a

Effects that use the word “instead” are replacement effects. Most replacement effects use the word “instead” to indicate what events will be replaced with other events.

#### CR 702.11b

“Hexproof” on a permanent means “This permanent can’t be the target of spells or abilities your opponents control.”

#### CR 702.18a

Shroud is a static ability. “Shroud” means “This permanent or player can’t be the target of spells or abilities.”

#### CR 702.96b

If a player chooses to pay the overload cost of a spell, that spell won’t require any targets. It may affect objects that couldn’t be chosen as legal targets if the spell were cast without its overload cost being paid.

#### CR 707.10

To copy a spell, activated ability, or triggered ability means to put a copy of it onto the stack; a copy of a spell isn’t cast and a copy of an activated ability isn’t activated. A copy of a spell or ability copies both the characteristics of the spell or ability and all decisions made for it, including modes, targets, the value of X, and additional or alternative costs. (See rule 601, “Casting Spells.”) Choices that are normally made on resolution are not copied. If an effect of the copy refers to objects used to pay its costs, it uses the objects used to pay the costs of the original spell …

#### CR 723.5

While controlling another player, a player makes all choices and decisions the controlled player is allowed to make or is told to make by the rules or by any objects. This includes choices and decisions about what to play, and choices and decisions called for by spells and abilities.

