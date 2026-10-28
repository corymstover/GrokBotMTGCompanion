---
title: "Norman Osborn // Green Goblin — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Norman Osborn // Green Goblin — Interaction Review

> Bot cycle 54 · batch E · reviewed 2026-10-16. Deck: [Norman Osborn // Green Goblin](../decks/norman-osborn.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/source-baseline/norman-osborn.txt`](../../exports/grixis-archidekt/source-baseline/norman-osborn.txt) · SHA-256 `6017ff8c9557b58ede769d4a467093fb84f780b3e3fe09cd580880cd7c91382f` |
| Rulings | **9** (9 verified · 0 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md) (Approval-ready verification sections 5–16) · [`Norman_Osborn_Green_Goblin_Whole_List_Audit_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Norman_Osborn_Green_Goblin_Whole_List_Audit_2026-10-15.md) (Whole-list audit) |

## Contents
- [Summary](#summary)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [Timing and priority](#timing-and-priority)
- [Replacement and prevention effects](#replacement-and-prevention-effects)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [Legality and project exceptions](#legality-and-project-exceptions)
- [Rules cited](#rules-cited)

## Summary

Norman Osborn // Green Goblin is a modal double-faced card that transforms. Norman connives on unblockable hits. Green Goblin gives every nonland card in your graveyard mayhem and discounts graveyard casts by {2}. The canonical list (source baseline) floods the graveyard with discard outlets (LED, Breakthrough, Attunement, Artist's Talent, Dark Deal), uses flash enablers for off-turn mayhem, and closes with Thassa's Oracle and Underworld Breach. All 7 Spellbook lines are present.

Rules surprises: mayhem only needs a discard earlier this turn, even before the transform; Yawgmoth's Will exiles that turn's discards; Green Goblin makes Mox Amber tap for black and red, not just blue; Goblin may be cast as the back face directly from the command zone, so Cavern naming Human can protect either face's creature spell. No list errors.

## Commander rules text and edge cases

### norman-01: A modal DFC that transforms: Norman front face, Green Goblin back face

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Norman Osborn // Green Goblin

**Ruling.** Norman Osborn // Green Goblin is a modal double-faced card. Under the current rules it can still transform: {1}{U}{B}{R}, at sorcery speed, flips Norman (unblockable 1/1, connives on combat damage) into Green Goblin (3/3 flying, menace). On the battlefield, only the face that's up counts, so Green Goblin has his own mana cost ({1}{U}{B}{R}), colors, types and mana value. Outside the stack/battlefield, only the front face's characteristics normally apply; however, when casting this modal double-faced card (including from the command zone), you may choose to cast either face. Green Goblin may be cast directly for {1}{U}{B}{R} plus applicable commander tax, or Norman may be cast for {1}{U} and then transformed by paying {1}{U}{B}{R} at sorcery speed. Commander tax counts prior casts of the card regardless of face. Color identity uses both faces: U/B/R.

**Citations**

- Oracle, *Norman Osborn // Green Goblin*: “{1}{U}{B}{R}: Transform Norman Osborn. Activate only as a sorcery.”
- Scryfall ruling, *Norman Osborn // Green Goblin*: “A modal double-faced card can be transformed or be put onto the battlefield transformed. This is a change from previous rules. If an effect instructs you to transform a modal double-faced card on the battlefield, it transforms only if its other face has a permanent type (that is, if its other face isn't an instant or sorcery). If it doesn't, it simply won't transform. Similarly, if an effect attempts to put a modal double-faced card onto the battlefield transformed, it will enter transformed if its back face has a permanent type. If it doesn't, it will simply stay in its current zone.”
- Scryfall ruling, *Norman Osborn // Green Goblin*: “The mana value of a modal double-faced card is based on the characteristics of the face that's being considered. On the stack or the battlefield, consider whichever face is up. In all other zones, consider only the front face. This is different than how the mana value of other double-faced cards is determined.”
- Scryfall ruling, *Norman Osborn // Green Goblin*: “In the Commander variant, a double-faced card's color identity is determined by the mana costs and mana symbols in the rules text of both faces combined. If either face has a color indicator or basic land type, those are also considered.”
- [CR 712.8a](#cr-7128a), [CR 712.8f](#cr-7128f), [CR 903.4](#cr-9034)
- Source (re-verified): [`Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md) → “Color identity is determined using both faces and is **U/B/R**.”

## Combos and engine lines

### norman-06: Thassa's Oracle + Demonic Consultation / Tainted Pact

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Norman Osborn // Green Goblin, Thassa's Oracle, Demonic Consultation, Tainted Pact

**Ruling.** These are the standard two-card wins. Exile your library with Consultation (naming Thassa's Oracle) or with Tainted Pact. The canonical list has 100 distinct names, so Pact never stops early on a duplicate. Then Oracle's ETB wins with zero cards in library. Both work without the commander.

**Citations**

- Commander Spellbook [742-1295](https://commanderspellbook.com/combo/742-1295/) (community-maintained, retrieved 2026-10-16): “Cast Demonic Consultation by paying {B}, naming Thassa's Oracle and thus exiling your library due to you not having a card named Thassa's Oracle in your library.”
- Commander Spellbook [1295-3093](https://commanderspellbook.com/combo/1295-3093/) (community-maintained, retrieved 2026-10-16): “Cast Tainted Pact by paying {1}{B}, exiling your library.”
- Source (re-verified): [`Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md) → “The exact approval-ready list contains **100 distinct card names**, so Tainted Pact has no duplicate-name stopping condition introduced by the decklist itself.”

### norman-07: Underworld Breach lines: LED + Brain Freeze, LED + Wheel, Wheel + Jeska's Will, Lotus Petal + Brain Freeze

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Norman Osborn // Green Goblin, Underworld Breach, Lion's Eye Diamond, Brain Freeze, Wheel of Fortune, Jeska's Will, Lotus Petal

**Ruling.** With Breach, LED adds three mana and can be escaped again for {0} plus exiling three. That powers repeated Brain Freezes (self-mill for fuel, then mill the opponents) or repeated Wheels of Fortune. Breach can also loop Wheel + Jeska's Will, or Lotus Petal + Brain Freeze. Green Goblin isn't needed, but he cuts each escaped spell's generic cost by {2}. Each escape still exiles three other cards from your graveyard.

**Citations**

- Scryfall ruling, *Underworld Breach*: “If you cast a spell with its escape permission, you can't choose to apply any other alternative costs or to cast it without paying its mana cost. If it has any additional costs, you must pay those.”
- [CR 702.138a](#cr-702138a)
- Commander Spellbook [1368-3518-4856](https://commanderspellbook.com/combo/1368-3518-4856/) (community-maintained, retrieved 2026-10-16): “Cast Lion's Eye Diamond from your graveyard for its escape cost by exiling three cards besides Brain Freeze from your graveyard.”
- Commander Spellbook [1368-2706-3518](https://commanderspellbook.com/combo/1368-2706-3518/) (community-maintained, retrieved 2026-10-16): “Resolve Wheel of Fortune, causing each player to discard their hand and draw seven cards.”
- Commander Spellbook [1368-1878-2706](https://commanderspellbook.com/combo/1368-1878-2706/) (community-maintained, retrieved 2026-10-16): “Cast Jeska's Will from your graveyard for its escape cost by paying {2}{R} and exiling three other cards from your graveyard, adding at least six {R}.”
- Commander Spellbook [1368-1414-4856](https://commanderspellbook.com/combo/1368-1414-4856/) (community-maintained, retrieved 2026-10-16): “Activate Lotus Petal by tapping and sacrificing it, adding {U}.”
- Source (re-verified): [`Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md) → “Green Goblin can improve the rate of graveyard-cast spells by reducing generic mana, but the Breach package does not require the commander to function.”

### norman-08: Breach + Grinding Station + Mox Amber: Goblin makes Amber tap for any Grixis color

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Norman Osborn // Green Goblin, Underworld Breach, Grinding Station, Mox Amber

**Ruling.** Grinding Station sacrifices Mox Amber to mill three. Escape Amber for {0} plus exiling three, and its entry untaps the Station. Each cycle nets +3 cards milled; it isn't a win on its own. Amber's mana depends on the face up. Front-face Norman is only blue. Green Goblin's face has its own mana cost {1}{U}{B}{R}, so he is blue, black and red, and Amber can tap for any of the three. Amber gives one color of your choice, not one of each.

**Citations**

- Oracle, *Mox Amber*: “{T}: Add one mana of any color among legendary creatures and planeswalkers you control.”
- Oracle, *Grinding Station*: “Whenever an artifact enters, you may untap this artifact.”
- Scryfall ruling, *Mox Amber*: “Mox Amber's ability adds one mana of the color of your choice from among the colors of legendary creatures and legendary planeswalkers you control. It doesn't add one mana of each of those colors.”
- [CR 105.2](#cr-1052), [CR 712.8f](#cr-7128f)
- Commander Spellbook [1368-3698--44](https://commanderspellbook.com/combo/1368-3698--44/) (community-maintained, retrieved 2026-10-16): “Cast the artifact from your graveyard for its escape cost by paying {0} and exiling three cards from your graveyard.”
- Source (re-verified): [`Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md) → “With Norman Osborn on the battlefield, Mox Amber can produce blue mana before being sacrificed because Norman is a blue legendary permanent.”

## Engines and payoffs

### norman-03: Cost stacking: Goblin's {2} plus Artist's Talent's {1}, generic only, on top of mayhem or escape

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Norman Osborn // Green Goblin, Artist's Talent, Big Score, Dark Deal, Unstable Experiment, Brain Freeze, Underworld Breach

**Ruling.** Cost reductions apply to whichever alternative cost you pay, mayhem or escape. Only one alternative cost applies per spell, so you pick between them. Goblin takes {2} off and level-2 Artist's Talent takes off {1} more, for noncreature spells. Both reduce only generic mana. Examples:
- Big Score from the graveyard costs {R}, and you still discard a card.
- Dark Deal costs {B}.
- Brain Freeze escaped under Breach costs {U} plus exiling three.

Artist's Talent level 1 is also a discard outlet each time you cast a noncreature spell.

**Citations**

- Oracle, *Big Score*: “As an additional cost to cast this spell, discard a card.”
- Scryfall ruling, *Norman Osborn // Green Goblin*: “Green Goblin's cost-reduction ability reduces only the generic mana component of a spell's cost. For example, if you cast a spell from your graveyard that would normally cost {1}{B}, you will have to pay {B} to cast it.”
- Scryfall ruling, *Artist's Talent*: “The cost reduction applies only to generic mana in the total cost of noncreature spells you cast.”
- Scryfall ruling, *Underworld Breach*: “If a card has multiple abilities giving you permission to cast it, such as two escape abilities or an escape ability and a flashback ability, you choose which one to apply. The others have no effect.”
- [CR 118.9a](#cr-1189a), [CR 118.9d](#cr-1189d), [CR 601.2f](#cr-6012f)
- Source (re-verified): [`Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md) → “**Big Score:** mayhem cost `{3}{R}` becomes `{1}{R}` with Green Goblin. Its additional discard cost remains mandatory.”

## Timing and priority

### norman-02: Goblin Formula: mayhem needs only a discard this turn, and still follows timing rules

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Norman Osborn // Green Goblin, Borne Upon a Wind, Valley Floodcaller, Faithless Looting

**Ruling.** Green Goblin gives each nonland card in your graveyard mayhem, with a cost equal to its mana cost. Mayhem is an alternative cost: you may cast the card from your graveyard if you discarded it this turn. Mayhem only checks that you discarded the card this turn, not that Goblin was out at the time. So you can discard on the front face (a Norman connive, or Faithless Looting), transform, then cast. Mayhem doesn't change timing. A sorcery still needs your main phase with an empty stack unless Borne Upon a Wind or Valley Floodcaller gives flash; Floodcaller also works for cards cast from the graveyard. Goblin's {2} reduction never grants permission to cast on its own.

**Citations**

- Oracle, *Norman Osborn // Green Goblin*: “Goblin Formula — Each nonland card in your graveyard has mayhem. The mayhem cost is equal to its mana cost. (You may cast a card from your graveyard for its mayhem cost if you discarded it this turn. Timing rules still apply.)”
- Scryfall ruling, *Norman Osborn // Green Goblin*: “Green Goblin's cost-reduction ability doesn't itself allow you to cast any spells from your graveyard. It only reduces the cost of spells that another effect (such as that of Green Goblin's last ability) has allowed you to cast.”
- Scryfall ruling, *Valley Floodcaller*: “Valley Floodcaller’s second ability applies to noncreature cards in any zone, provided something is allowing you to cast them. For example, you could cast a sorcery with flashback as though it had flash.”
- Scryfall ruling, *Borne Upon a Wind*: “This applies only to casting spells. It does not, for example, change when you can activate abilities that can be activated "only as a sorcery."”
- [CR 702.187a](#cr-702187a), [CR 702.187b](#cr-702187b), [CR 118.9d](#cr-1189d), [CR 117.1a](#cr-1171a)
- Source (re-verified): [`Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md) → “Mayhem changes where and for what alternative cost a card may be cast; it does not itself let a sorcery be cast at instant speed.”

## Replacement and prevention effects

### norman-05: Yawgmoth's Will exiles new discards; Necropotence (not in list) would race mayhem

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Norman Osborn // Green Goblin, Yawgmoth's Will

**Ruling.** Yawgmoth's Will sends any card that would go to your graveyard this turn to exile instead, discards included. So on a Will turn, newly discarded cards never land in the graveyard and can't use mayhem. Will replays what's already in the graveyard; it doesn't help that turn's discards. The source correctly leaves out Necropotence: its exile is a trigger, so instant-speed or flash mayhem could only answer it in response.

**Citations**

- Oracle, *Yawgmoth's Will*: “If a card would be put into your graveyard from anywhere this turn, exile that card instead.”
- Scryfall ruling, *Yawgmoth's Will*: “The second ability creates a replacement effect. It applies to both costs and effects.”
- [CR 614.1a](#cr-6141a), [CR 702.187a](#cr-702187a)
- Source (re-verified): [`Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md) → “New cards discarded while its replacement effect applies will not normally remain available in the graveyard for Green Goblin's Mayhem plan.”

## Zones, commander tax and the command zone

### norman-04: Mass discard outlets: Lion's Eye Diamond, Breakthrough, Attunement, Dark Deal, Wheel of Fortune

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Norman Osborn // Green Goblin, Lion's Eye Diamond, Breakthrough, Attunement, Dark Deal, Wheel of Fortune, Reckless Handling

**Ruling.** Each of these discards several cards at once, and all of them become mayhem-eligible for the rest of the turn:
- **Lion's Eye Diamond:** a mana ability usable only at instant timing. Because it says activate only as an instant, it cannot be activated during another spell's 601.2g cost-payment step. Activate in a legal priority window before or after casting a spell; then any same-turn discarded nonlands can use Mayhem if permitted.
- **Breakthrough:** for X=0 it costs {U}, draws four, then discards the whole hand.
- **Attunement:** returns itself to hand as its cost, then you draw three and discard four, or your whole hand if you have fewer.
- **Reckless Handling:** the tutored artifact can be the random discard, and nothing can happen in between. That card can still be mayhem-cast later.

**Citations**

- Scryfall ruling, *Lion's Eye Diamond*: “The ability is a mana ability, so it is activated and resolves as a mana ability, but it can only be activated at times when you can cast an instant. Yes, this is a bit weird.”
- Scryfall ruling, *Attunement*: “If you have less than 4 cards, discard all you have.”
- Scryfall ruling, *Reckless Handling*: “You can't do anything between putting the artifact card you found in your hand and discarding. You may end up discarding that card. But hey, if you do, 2 damage!”
- [CR 605.3b](#cr-6053b), [CR 601.2g](#cr-6012g), [CR 702.187b](#cr-702187b)
- Source (re-verified): [`Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md) → “**Attunement** can return itself to hand as the cost of its activated ability, then draw three cards and discard four.”

## Legality and project exceptions

### norman-09: Cavern of Souls naming Human protects either creature-face cast

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Norman Osborn // Green Goblin, Cavern of Souls

**Ruling.** Norman Osborn is a Human Scientist Villain, so Cavern naming Human makes him uncounterable and pays a colored mana toward him. Green Goblin can also be chosen and cast directly from the command zone as the back face; because he is a Human too, Cavern naming Human can make either face's creature spell uncounterable when its restricted mana pays for that spell. Cavern does not protect the transform activated ability.

**Citations**

- Scryfall ruling, *Cavern of Souls*: “You must choose an existing creature type, such as Human or Warrior. Card types such as artifact can't be chosen.”
- [CR 712.11b](#cr-71211b), [CR 712.8f](#cr-7128f)
- Source (front-face Human type only): [`Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md) → “legendary Human Scientist Villain”. **Correction:** The same historical source erroneously said the back face could not be cast; current CR 712.11b and 903.8 supersede that outdated inference.

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 105.2

An object can be one or more of the five colors, or it can be no color at all. An object is the color or colors of the mana symbols in its mana cost, regardless of the color of its frame. An object’s color or colors may also be defined by a color indicator or a characteristic-defining ability. See rule 202.2.

#### CR 117.1a

A player may cast an instant spell any time they have priority. A player may cast a noninstant spell during their main phase any time they have priority and the stack is empty.

#### CR 118.9a

Only one alternative cost can be applied to any one spell as it’s being cast. The controller of the spell announces their intentions to pay that cost as described in rule 601.2b.

#### CR 118.9d

If an alternative cost is being paid to cast a spell, any additional costs, cost increases, and cost reductions that affect that spell are applied to that alternative cost. (See rule 601.2f.)

#### CR 601.2f

The player determines the total cost of the spell. Usually this is just the mana cost. Some spells have additional or alternative costs. Some effects may increase or reduce the cost to pay, or may provide other alternative costs. Costs may include paying mana, tapping permanents, sacrificing permanents, discarding cards, and so on. The total cost is the mana cost or alternative cost (as determined in rule 601.2b), plus all additional costs and cost increases, and minus all cost reductions. If multiple cost reductions apply, the player may apply them in any order. If the mana component of the …

#### CR 601.2g

If the total cost includes a mana payment, the player then has a chance to activate mana abilities (see rule 605, “Mana Abilities”). Mana abilities must be activated before costs are paid.

#### CR 605.3b

An activated mana ability doesn’t go on the stack, so it can’t be targeted, countered, or otherwise responded to. Rather, it resolves immediately after it is activated. (See rule 405.6c.)

#### CR 614.1a

Effects that use the word “instead” are replacement effects. Most replacement effects use the word “instead” to indicate what events will be replaced with other events.

#### CR 702.138a

Escape represents a static ability that functions while the card with escape is in a player’s graveyard. “Escape [cost]” means “You may cast this card from your graveyard by paying [cost] rather than paying its mana cost.” Casting a spell using its escape ability follows the rules for paying alternative costs in rules 601.2b and 601.2f–h.

#### CR 702.187a

Mayhem is a static ability that functions while the card with mayhem is in a player’s graveyard.

#### CR 702.187b

“Mayhem [cost]” means “As long as you discarded this card this turn, you may cast it from your graveyard by paying [cost] rather than paying its mana cost.” Casting a spell using its mayhem ability follows the rules for paying alternative costs in rules 601.2b and 601.2f–h.

#### CR 712.8a

While a double-faced card is outside the game or in a zone other than the battlefield or stack, it has only the characteristics of its front face.

#### CR 712.8f

While a modal double-faced spell is on the stack or a modal double-faced permanent is on the battlefield, it has only the characteristics of the face that’s up.

#### CR 712.11b

A player casting a modal double-faced card or a copy of a modal double-faced card as a spell chooses which face they are casting before putting it onto the stack.

#### CR 903.4

The Commander variant uses color identity to determine what cards can be in a deck with a certain commander. The color identity of a card is the color or colors of any mana symbols in that card’s mana cost or rules text, plus any colors defined by its characteristic-defining abilities (see rule 604.3) or color indicator (see rule 204).

