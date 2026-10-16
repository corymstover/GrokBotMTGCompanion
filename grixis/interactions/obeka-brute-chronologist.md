---
title: "Obeka, Brute Chronologist — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Obeka, Brute Chronologist — Interaction Review

> Bot cycle 54 · batch E · reviewed 2026-10-16. Deck: [Obeka, Brute Chronologist](../decks/obeka-brute-chronologist.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/obeka-brute-chronologist.txt`](../../exports/grixis-archidekt/obeka-brute-chronologist.txt) · SHA-256 `76fc5a3f9a098d4999c8ce85f8226a0ceef9a5077822b0335e01b8a594b5ea4d` |
| Rulings | **5** (5 verified · 0 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`Obeka_Brute_Chronologist_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Obeka_Brute_Chronologist_Approval_Ready_Verification_2026-10-15.md) (Approval-ready verification sections 5–6) |

## Contents
- [Summary](#summary)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Trigger ordering](#trigger-ordering)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [Rules cited](#rules-cited)

## Summary

Obeka ends the turn, so the deck plays cards that undo themselves at the next end step and keeps the benefit: Final Fortune and Last Chance extra turns, Identity Thief, Come Back Wrong, Hate Mirage, Sneak Attack, Kiki-Jiki and Venser. Scepter + Final Fortune (with Obeka or Sundial) is the infinite-turn lock. Hellkite Courser is the tax-free way to get Obeka out. All 4 Spellbook lines are in the canonical list.

Rules surprises: ending the turn before the end step only delays a 'next end step' trigger; you must let it trigger first. On an opponent's turn, they decide whether the turn ends. Courser's return trigger can't get Obeka if she ends the turn over it. No list errors.

## Commander rules text and edge cases

### obekabc-01: Obeka ends the turn: timing the activation against end-step triggers

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Obeka, Brute Chronologist

**Ruling.** Obeka's ability uses the stack. When it resolves, the player whose turn it is chooses whether to end the turn, so on an opponent's turn they can just decline. Ending the turn exiles everything on the stack, including uncounterable spells. It removes creatures from combat, checks state-based actions without putting triggers on the stack, and skips to cleanup. Triggers that were waiting to go on the stack cease to exist.

Timing matters for "at the beginning of the next end step" triggers:
- **End the turn before the end step:** the trigger hasn't happened yet, so it waits and triggers at the next turn's end step.
- **Let it trigger, then activate Obeka with it on the stack:** it's exiled and never comes back.

Anything said to last "until end of turn" still ends in cleanup.

**Citations**

- Oracle, *Obeka, Brute Chronologist*: “{T}: The player whose turn it is may end the turn. (Exile all spells and abilities from the stack. The player whose turn it is discards down to their maximum hand size. Damage wears off, and "this turn" and "until end of turn" effects end.)”
- Scryfall ruling, *Obeka, Brute Chronologist*: “If the turn ends during the end step after "At the beginning of the next end step" abilities have triggered but before they've resolved, those abilities won't trigger again next turn.”
- Scryfall ruling, *Obeka, Brute Chronologist*: “If the turn ends before the end step, any "At the beginning of the next end step" triggered abilities won't get the chance to trigger that turn because the end step has been skipped. Those abilities will trigger next turn at the beginning of the end step.”
- Scryfall ruling, *Obeka, Brute Chronologist*: “If any triggered abilities do trigger during this process, they're put onto the stack during the cleanup step. If this happens, players will have a chance to cast spells and activate abilities, then there will be another cleanup step before the turn is over.”
- [CR 724.1a](#cr-7241a), [CR 724.1b](#cr-7241b), [CR 724.1c](#cr-7241c), [CR 724.1d](#cr-7241d), [CR 603.7b](#cr-6037b)
- Source (re-verified): [`Obeka_Brute_Chronologist_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Obeka_Brute_Chronologist_Approval_Ready_Verification_2026-10-15.md) → “The correct Obeka pattern is normally to let the delayed `next end step` ability trigger on our end step and then end the turn with that ability on the stack.”

## Combos and engine lines

### obekabc-02: Isochron Scepter + Final Fortune + Obeka (or Sundial of the Infinite): infinite turns

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Obeka, Brute Chronologist, Isochron Scepter, Final Fortune, Sundial of the Infinite, Last Chance

**Ruling.** Imprint Final Fortune (an instant, MV 2) on Isochron Scepter. Each turn, the Scepter copy gives you another extra turn. At each extra turn's end step, the lose-the-game trigger goes on the stack. Respond with Obeka or Sundial (Sundial only on your own turn) to end the turn, and the trigger is exiled. Obeka and Scepter untap in each extra turn's untap step. Last Chance is a one-shot backup. A Stifle effect on the Obeka or Sundial activation leaves the lose trigger to resolve.

**Citations**

- Oracle, *Final Fortune*: “Take an extra turn after this one. At the beginning of that turn's end step, you lose the game.”
- Scryfall ruling, *Isochron Scepter*: “You cast the copy while the ability is resolving and still on the stack. You can't wait to cast it later in the turn.”
- Scryfall ruling, *Sundial of the Infinite*: “Though spells and abilities that are exiled won't get a chance to resolve, they don't count as being "countered."”
- [CR 500.7](#cr-5007), [CR 724.1b](#cr-7241b), [CR 603.7b](#cr-6037b)
- Commander Spellbook [126-1173-5261](https://commanderspellbook.com/combo/126-1173-5261/) (community-maintained, retrieved 2026-10-16): “In response, activate Obeka by tapping it, choosing to end the turn and exiling the stack in the process.”
- Commander Spellbook [1173-2160-5261](https://commanderspellbook.com/combo/1173-2160-5261/) (community-maintained, retrieved 2026-10-16): “Holding priority, activate Sundial of the Infinite by paying {1} and tapping it, ending the turn.”
- Source (re-verified): [`Obeka_Brute_Chronologist_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Obeka_Brute_Chronologist_Approval_Ready_Verification_2026-10-15.md) → “Scepter repeatedly casts Final Fortune; on each extra turn, Final Fortune's lose-the-game trigger is put on the stack during the end step; Obeka ends the turn and removes that trigger.”

### obekabc-05: Kiki-Jiki + Delina, and Dualcaster Mage + Twinflame: infinite hasty tokens

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Obeka, Brute Chronologist, Kiki-Jiki, Mirror Breaker, Delina, Wild Mage, Dualcaster Mage, Twinflame

**Ruling.** **Delina + Kiki-Jiki:** Delina's attack trigger makes a nonlegendary, tapped-and-attacking token of Kiki-Jiki. That token copies the real Kiki-Jiki, and each new copy copies the last, for unlimited hasty tokens. The Delina token is exiled at end of combat, but the Kiki copies stay.

**Dualcaster + Twinflame:** Dualcaster Mage copies Twinflame targeting itself. The token Mage copies the Twinflame copy again, without end.

Both leave "exile/sacrifice at the next end step" triggers, which Obeka can exile so the tokens stay. Delina's tokens were never declared as attackers.

**Citations**

- Scryfall ruling, *Delina, Wild Mage*: “Although the token is attacking, it was never declared as an attacking creature (for purposes of abilities that trigger whenever a creature attacks, for example).”
- Scryfall ruling, *Twinflame*: “If another creature becomes or enters the battlefield as a copy of the token, that creature will have haste, but you won't exile it. However, if Twinflame creates multiple tokens copying a single creature due to a replacement effect (like the one Doubling Season creates), you'll exile each of them.”
- [CR 707.2](#cr-7072), [CR 724.1b](#cr-7241b)
- Commander Spellbook [282-618](https://commanderspellbook.com/combo/282-618/) (community-maintained, retrieved 2026-10-16): “Delina triggers, creating at least one nonlegendary token copy of Kiki-Jiki.”
- Commander Spellbook [147-1235](https://commanderspellbook.com/combo/147-1235/) (community-maintained, retrieved 2026-10-16): “When Dualcaster Mage enters the battlefield, it triggers, copying Twinflame, targeting Dualcaster Mage.”

## Trigger ordering

### obekabc-03: Delayed liabilities become permanent: Identity Thief, Come Back Wrong, Hate Mirage, Apprentice Necromancer, Venser, Sneak Attack

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Obeka, Brute Chronologist, Identity Thief, Come Back Wrong, Hate Mirage, Apprentice Necromancer, Venser, Fervent Forger, Sneak Attack, Fable of the Mirror-Breaker // Reflection of Kiki-Jiki, Kiki-Jiki, Mirror Breaker

**Ruling.** Several cards here undo themselves at the next end step:
- Identity Thief returns the creature it exiled.
- Come Back Wrong sacrifices the stolen creature.
- Hate Mirage exiles its hasty copies.
- Apprentice Necromancer, Sneak Attack, Venser's permanent mode and Kiki-Jiki or Reflection tokens get sacrificed.

End the turn with those triggers on the stack and the effects stick. Identity Thief's target stays exiled forever. Copy effects that last "until end of turn" still end; Identity Thief stops being a copy in cleanup.

**Citations**

- Oracle, *Identity Thief*: “Whenever this creature attacks, you may exile another target nontoken creature. If you do, this creature becomes a copy of that creature until end of turn. Return the exiled card to the battlefield under its owner's control at the beginning of the next end step.”
- Oracle, *Come Back Wrong*: “Destroy target creature. If a creature card is put into a graveyard this way, return it to the battlefield under your control. Sacrifice it at the beginning of your next end step.”
- Scryfall ruling, *Sneak Attack*: “You sacrifice the creature only if you still control it. If that creature has left the battlefield, even if it came back, you don't sacrifice it.”
- [CR 603.7](#cr-6037), [CR 724.1b](#cr-7241b), [CR 514.2](#cr-5142)
- Source (re-verified): [`Obeka_Brute_Chronologist_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Obeka_Brute_Chronologist_Approval_Ready_Verification_2026-10-15.md) → “If that delayed return ability is on the stack during our end step, Obeka may end the turn and exile that ability.”

## Zones, commander tax and the command zone

### obekabc-04: Hellkite Courser puts Obeka in play hasty and tax-free; Obeka keeps herself there

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Obeka, Brute Chronologist, Hellkite Courser, Thousand-Year Elixir, Arena of Glory

**Ruling.** Hellkite Courser's ETB puts Obeka onto the battlefield from the command zone with haste. That isn't a cast, so commander tax doesn't go up. At the next end step Courser's return trigger fires, and Obeka can tap and end the turn over it, so she stays. Thousand-Year Elixir lets a freshly arrived Obeka tap without real haste. Arena of Glory's exert mana gives haste to the Obeka spell.

**Citations**

- Oracle, *Hellkite Courser*: “When this creature enters, you may put a commander you own from the command zone onto the battlefield. It gains haste. Return it to the command zone at the beginning of the next end step.”
- Scryfall ruling, *Hellkite Courser*: “Putting your commander onto the battlefield this way isn't the same as casting that commander. The "commander tax" won't increase.”
- Scryfall ruling, *Thousand-Year Elixir*: “Thousand-Year Elixir doesn’t actually grant haste to creatures you control, nor does it let you attack with them as though they had haste.”
- [CR 903.8](#cr-9038), [CR 724.1b](#cr-7241b)
- Source (re-verified): [`Obeka_Brute_Chronologist_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Obeka_Brute_Chronologist_Approval_Ready_Verification_2026-10-15.md) → “It bypasses commander tax, puts Obeka directly onto the battlefield, gives her haste, and creates a delayed return liability Obeka is built to manage.”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 500.7

Some effects can give a player extra turns. They do this by adding the turns directly after the specified turn. If a player is given multiple extra turns, the extra turns are added one at a time. If multiple players are given extra turns, the extra turns are added one at a time, in APNAP order (see rule 101.4). The most recently created turn will be taken first.

#### CR 514.2

Second, the following actions happen simultaneously: all damage marked on permanents (including phased-out permanents) is removed and all “until end of turn” and “this turn” effects end. This turn-based action doesn’t use the stack.

#### CR 603.7

An effect may create a delayed triggered ability that can do something at a later time. A delayed triggered ability will contain “when,” “whenever,” or “at,” although that word won’t usually begin the ability.

#### CR 603.7b

A delayed triggered ability will trigger only once—the next time its trigger event occurs—unless it has a stated duration, such as “this turn.” If its trigger event occurs more than once simultaneously and the ability doesn’t have a stated duration, the controller of the delayed triggered ability chooses which event causes the ability to trigger.

#### CR 707.2

When copying an object, the copy acquires the copiable values of the original object’s characteristics and, for an object on the stack, choices made when casting or activating it (mode, targets, the value of X, whether it was kicked, how it will affect multiple targets, and so on). The copiable values are the values derived from the text printed on the object (that text being name, mana cost, color indicator, card type, subtype, supertype, rules text, power, toughness, and/or loyalty), as modified by other copy effects, by its face-down status, and by “as . . . enters” and “as . . . is turned …

#### CR 724.1a

If there are any triggered abilities that triggered before this process began but haven’t been put onto the stack yet, those abilities cease to exist. They won’t be put onto the stack. This rule does not apply to abilities that trigger during this process (see rule 724.1f).

#### CR 724.1b

Exile every object on the stack, including the object that’s resolving. All objects not on the battlefield or in the command zone that aren’t represented by cards will cease to exist the next time state-based actions are checked (see rule 704, “State-Based Actions”).

#### CR 724.1c

Check state-based actions. No player gets priority, and no triggered abilities are put onto the stack.

#### CR 724.1d

The current phase and/or step ends. If this happens during combat, remove all creatures and planeswalkers from combat. The game skips straight to the cleanup step; skip any phases or steps between this phase or step and the cleanup step. If an effect ends the turn during the cleanup step, a new cleanup step begins.

#### CR 903.8

A player may cast a commander they own from the command zone. A commander cast from the command zone costs an additional {2} for each previous time the player casting it has cast it from the command zone that game. This additional cost is informally known as the “commander tax.”

