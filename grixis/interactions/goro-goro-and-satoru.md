---
title: "Goro-Goro and Satoru — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Goro-Goro and Satoru — Interaction Review

> Bot cycle 48 · batch B · reviewed 2026-10-16. Deck: [Goro-Goro and Satoru](../decks/goro-goro-and-satoru.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/goro-goro-and-satoru.txt`](../../exports/grixis-archidekt/goro-goro-and-satoru.txt) · SHA-256 `bdc129bcd94c00b293ddaabb4585ac3130fb4eca7ca8646177335900e7aedfec` |
| Rulings | **9** (9 verified · 0 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`Goro_Goro_and_Satoru_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/goro_goro_and_satoru_2026-10-14/Goro_Goro_and_Satoru_Rules_Attestation.json) (12 interactions, all PASS) |

## Contents
- [Summary](#summary)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [Timing and priority](#timing-and-priority)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [Rules cited](#rules-cited)

## Summary

Goro-Goro and Satoru makes a 5/5 flying Dragon Spirit whenever creatures that entered this turn deal combat damage to a player, and can give your team haste. The list runs Ninjutsu, enters-attacking creatures and extra combats. This review re-verifies the twelve items of the deck's rules attestation, and confirms the five Breath of Fury loops against cached Commander Spellbook steps.

Key rule: Goro-Goro's haste only covers creatures you control when it resolves, so each new Dragon needs another {1}{R} (Spellbook repeats it each combat), or haste from Samut or Dragon Tempest. No list errors.

## Commander rules text and edge cases

### goro-01: One Dragon per player per damage step

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Goro-Goro and Satoru

**Ruling.** The trigger says 'one or more creatures … deal combat damage to a player', so several fresh creatures hitting the same player in one damage step make one Dragon. Hitting two players makes two. A first-strike damage step and a regular one are separate events, so double strike can trigger it twice. Only creatures that entered this turn count, however they entered.

**Citations**

- Oracle, *Goro-Goro and Satoru*: “Whenever one or more creatures you control that entered this turn deal combat damage to a player, create a 5/5 red Dragon Spirit creature token with flying.”
- [CR 603.2c](#cr-6032c), [CR 510.4](#cr-5104)
- Source (re-verified): [`Goro_Goro_and_Satoru_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/goro_goro_and_satoru_2026-10-14/Goro_Goro_and_Satoru_Rules_Attestation.json) → “Goro-Goro and Satoru combat-damage trigger scope”

### goro-02: The haste ability only covers creatures you control when it resolves

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Goro-Goro and Satoru, Samut, Hazoret's Champion, Dragon Tempest

**Ruling.** Goro-Goro's {1}{R} gives haste only to creatures you control as it resolves. A Dragon Spirit made later needs another activation before it can attack in the next combat; the activation has no timing restriction, so it can be done between combats. Samut gives haste continuously, including to later Dragons. Dragon Tempest gives every flying creature that enters haste, and the Dragon Spirits have flying.

**Citations**

- Oracle, *Goro-Goro and Satoru*: “{1}{R}: Creatures you control gain haste until end of turn.”
- Oracle, *Samut, Hazoret's Champion*: “Creatures you control have haste.”
- Oracle, *Dragon Tempest*: “Whenever a creature you control with flying enters, it gains haste until end of turn.”
- Scryfall ruling, *Goro-Goro and Satoru*: “The set of creatures affected by the last ability is determined as that ability resolves. Creatures you begin to control later in the turn and permanents that become creatures later in the turn won’t gain haste.”
- [CR 611.2c](#cr-6112c), [CR 604.2](#cr-6042)
- Source (re-verified): [`Goro_Goro_and_Satoru_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/goro_goro_and_satoru_2026-10-14/Goro_Goro_and_Satoru_Rules_Attestation.json) → “Samut continuous haste versus Goro-Goro activated haste”

## Combos and engine lines

### goro-05: Goro-Goro + Breath of Fury: order Goro-Goro's trigger on top

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Goro-Goro and Satoru, Breath of Fury

**Ruling.** Put Breath of Fury on a creature that entered this turn and give it haste. When it connects, both Breath and Goro-Goro trigger. Put Goro-Goro's trigger on top so it resolves first and makes the Dragon Spirit. Breath then sacrifices its creature, attaches to the new Dragon, untaps your creatures and adds a combat. The Dragon entered this turn, so it carries the loop, but it needs haste: Spellbook repeats the {1}{R} haste step every combat, or use Samut or Dragon Tempest.

**Citations**

- Oracle, *Breath of Fury*: “When enchanted creature deals combat damage to a player, sacrifice it and attach this Aura to a creature you control. If you do, untap all creatures you control and after this phase, there is an additional combat phase.”
- Oracle, *Goro-Goro and Satoru*: “{1}{R}: Creatures you control gain haste until end of turn.”
- Scryfall ruling, *Breath of Fury*: “If there isn’t a legal creature to attach Breath of Fury to after the enchanted creature is sacrificed, you don’t untap your creatures or get an additional combat phase, and Breath of Fury is put into its owner’s graveyard as a state-based action.”
- [CR 603.3b](#cr-6033b), [CR 500.8](#cr-5008)
- Commander Spellbook [2237-3259](https://commanderspellbook.com/combo/2237-3259/) (community-maintained, retrieved 2026-10-16): “Resolve the Goro-Goro and Satoru trigger, creating a 5/5 Dragon Spirit creature token.”
- Commander Spellbook [2237-3259](https://commanderspellbook.com/combo/2237-3259/) (community-maintained, retrieved 2026-10-16): “Repeat from step 3 each combat phase.”
- Commander Spellbook [2237-3259](https://commanderspellbook.com/combo/2237-3259/) (community-maintained, retrieved 2026-10-16): “Activate Goro-Goro and Satoru by paying {1}{R}, giving creatures you control haste until end of turn.”
- Source (re-verified): [`Goro_Goro_and_Satoru_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/goro_goro_and_satoru_2026-10-14/Goro_Goro_and_Satoru_Rules_Attestation.json) → “Goro-Goro and Satoru plus Breath of Fury loop”

### goro-06: Breath of Fury + a beginning-of-combat token maker

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Goro-Goro and Satoru, Breath of Fury, Urabrask's Forge, Daring Piracy, Loyal Apprentice, Determined Iteration

**Ruling.** Each of these makes a hasty creature token at the beginning of each combat on your turn, including extra combats. When Breath's creature connects, Breath moves to the new token and adds another combat, which makes another token. Every line needs the attacker to connect each time: Spellbook's prerequisite is that an opponent can't block. Loyal Apprentice needs you to control your commander. Determined Iteration needs a nonlegendary creature token to populate. Urabrask's Forge's token grows with each oil counter.

**Citations**

- Oracle, *Daring Piracy*: “At the beginning of combat on your turn, create a 1/1 red Pirate creature token with menace and haste.”
- Scryfall ruling, *Determined Iteration*: “If you control no creature tokens when you populate, nothing will happen.”
- [CR 500.8](#cr-5008), [CR 701.36a](#cr-70136a)
- Commander Spellbook [1347-3259](https://commanderspellbook.com/combo/1347-3259/) (community-maintained, retrieved 2026-10-16): “An opponent cannot block creatures you control.”
- Commander Spellbook [1347-3259](https://commanderspellbook.com/combo/1347-3259/) (community-maintained, retrieved 2026-10-16): “At the beginning of your combat phase, Urabrask's Forge triggers, creating a creature token.”
- Commander Spellbook [3259-3934](https://commanderspellbook.com/combo/3259-3934/) (community-maintained, retrieved 2026-10-16): “You control a nonlegendary creature token.”
- Source (re-verified): [`Goro_Goro_and_Satoru_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/goro_goro_and_satoru_2026-10-14/Goro_Goro_and_Satoru_Rules_Attestation.json) → “Daring Piracy, Loyal Apprentice and Urabrask's Forge”

## Engines and payoffs

### goro-08: Dragon payoffs: Terror of the Peaks and Dragon Tempest

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Goro-Goro and Satoru, Terror of the Peaks, Dragon Tempest

**Ruling.** Each 5/5 Dragon Spirit entering makes Terror of the Peaks deal 5 to any target. Dragon Tempest makes it deal damage equal to the number of Dragons you control (counted on resolution) and gives it haste. This damage isn't combat damage, so it doesn't trigger Goro-Goro.

**Citations**

- Oracle, *Terror of the Peaks*: “Whenever another creature you control enters, this creature deals damage equal to that creature's power to any target.”
- Oracle, *Dragon Tempest*: “Whenever a Dragon you control enters, it deals X damage to any target, where X is the number of Dragons you control.”
- Scryfall ruling, *Dragon Tempest*: “The amount of damage dealt by the Dragon that entered the battlefield is based on the number of Dragons you control when the ability resolves.”
- [CR 120.2](#cr-1202), [CR 603.2](#cr-6032)
- Source (re-verified): [`Goro_Goro_and_Satoru_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/goro_goro_and_satoru_2026-10-14/Goro_Goro_and_Satoru_Rules_Attestation.json) → “Dragon Tempest and Terror of the Peaks”

### goro-09: Waterbender Ascension counts each creature

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Goro-Goro and Satoru, Waterbender Ascension

**Ruling.** Ascension triggers once for each creature that deals combat damage to a player, unlike Goro-Goro's 'one or more'. From the fourth quest counter, each trigger also draws. Waterbend {4} (tap artifacts or creatures for the generic) makes a creature unblockable, which helps satisfy the Breath of Fury loops' 'can't be blocked' prerequisite.

**Citations**

- Oracle, *Waterbender Ascension*: “Whenever a creature you control deals combat damage to a player, put a quest counter on this enchantment. Then if it has four or more quest counters on it, draw a card.”
- Scryfall ruling, *Waterbender Ascension*: “You can tap any untapped creature or artifact you control to pay a waterbend cost, even one you haven't controlled continuously since the beginning of your most recent turn.”
- [CR 603.2c](#cr-6032c)
- Source (re-verified): [`Goro_Goro_and_Satoru_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/goro_goro_and_satoru_2026-10-14/Goro_Goro_and_Satoru_Rules_Attestation.json) → “Waterbender Ascension trigger granularity”

## Timing and priority

### goro-04: Raphael's sneak gives double strike before first-strike damage

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Goro-Goro and Satoru, Raphael, the Nightwatcher, Fire Navy Trebuchet

**Ruling.** Sneak casts Raphael during the declare blockers step by returning an unblocked attacker. He enters tapped and attacking after blocks, so he's unblocked, and attacking creatures you control have double strike. That's before damage, so there are two damage steps. Fresh attackers (Raphael, a Ballistic Boulder) connecting in both steps trigger Goro-Goro twice for that player.

**Citations**

- Oracle, *Raphael, the Nightwatcher*: “Attacking creatures you control have double strike.”
- [CR 702.190a](#cr-702190a), [CR 702.4b](#cr-7024b), [CR 510.4](#cr-5104)
- Source (re-verified): [`Goro_Goro_and_Satoru_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/goro_goro_and_satoru_2026-10-14/Goro_Goro_and_Satoru_Rules_Attestation.json) → “Raphael sneak plus double strike”
- Source (re-verified): [`Goro_Goro_and_Satoru_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/goro_goro_and_satoru_2026-10-14/Goro_Goro_and_Satoru_Rules_Attestation.json) → “Raphael plus Fire Navy Trebuchet”

### goro-07: Fresh creatures stay fresh through extra combats

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Goro-Goro and Satoru, Karlach, Fury of Avernus, Great Train Heist, Aggravated Assault

**Ruling.** 'Entered this turn' lasts the whole turn, so a creature from the first combat can trigger Goro-Goro again in every extra combat. Karlach adds one combat after the first, Great Train Heist's first mode adds one if cast during combat, and Aggravated Assault adds a combat and main phase at sorcery speed.

**Citations**

- Oracle, *Great Train Heist*: “If it's your combat phase, there is an additional combat phase after this phase.”
- Oracle, *Aggravated Assault*: “After this main phase, there is an additional combat phase followed by an additional main phase.”
- [CR 500.8](#cr-5008)
- Source (re-verified): [`Goro_Goro_and_Satoru_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/goro_goro_and_satoru_2026-10-14/Goro_Goro_and_Satoru_Rules_Attestation.json) → “Extra-combat effects and commander retriggering”

## Zones, commander tax and the command zone

### goro-03: Ninjutsu, sneak and 'enters attacking' creatures all qualify

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Goro-Goro and Satoru, Ninja of the Deep Hours, Thousand-Faced Shadow, Fire Navy Trebuchet, Phoenix Chick

**Ruling.** Ninjutsu puts the Ninja onto the battlefield tapped and attacking the same player as the creature you returned. It entered this turn, so its combat damage triggers Goro-Goro. The same goes for Thousand-Faced Shadow's token copy, Fire Navy Trebuchet's Ballistic Boulder, and Phoenix Chick returning attacking. None of them were declared as attackers, so 'whenever attacks' triggers don't see them.

**Citations**

- Oracle, *Fire Navy Trebuchet*: “Whenever you attack, create a 2/1 colorless Construct artifact creature token with flying named Ballistic Boulder that's tapped and attacking.”
- Scryfall ruling, *Phoenix Chick*: “If Phoenix Chick enters the battlefield attacking, it wasn't declared as an attacking creature that turn. Abilities that trigger when a creature attacks won't trigger.”
- Scryfall ruling, *Fire Navy Trebuchet*: “Fire Navy Trebuchet's controller chooses which player, planeswalker, or battle the token is attacking.”
- [CR 702.49a](#cr-70249a), [CR 702.49c](#cr-70249c), [CR 508.4](#cr-5084)
- Source (re-verified): [`Goro_Goro_and_Satoru_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/goro_goro_and_satoru_2026-10-14/Goro_Goro_and_Satoru_Rules_Attestation.json) → “Ninjutsu entrants satisfy the commander condition”
- Source (re-verified): [`Goro_Goro_and_Satoru_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/goro_goro_and_satoru_2026-10-14/Goro_Goro_and_Satoru_Rules_Attestation.json) → “Fire Navy Trebuchet fresh-attacker engine”
- Source (re-verified): [`Goro_Goro_and_Satoru_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/goro_goro_and_satoru_2026-10-14/Goro_Goro_and_Satoru_Rules_Attestation.json) → “Phoenix Chick recursion”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 120.2

Any object can deal damage.

#### CR 500.8

Some effects can add phases to a turn. They do this by adding the phases directly after the specified phase. If multiple extra phases are created after the same phase, the most recently created phase will occur first.

#### CR 508.4

If a creature is put onto the battlefield attacking, its controller chooses which defending player, planeswalker a defending player controls, or battle a defending player protects it’s attacking as it enters the battlefield (unless the effect that put it onto the battlefield specifies what it’s attacking). Similarly, if an effect states that a creature is attacking, its controller chooses which defending player, planeswalker a defending player controls, or battle a defending player protects it’s attacking (unless the effect has already specified). Such creatures are “attacking” but, for the …

#### CR 510.4

If at least one attacking or blocking creature has first strike (see rule 702.7) or double strike (see rule 702.4) as the combat damage step begins, the only creatures that assign combat damage in that step are those with first strike or double strike. After that step, instead of proceeding to the end of combat step, the phase gets a second combat damage step. The only creatures that assign combat damage in that step are the remaining attackers and blockers that had neither first strike nor double strike as the first combat damage step began, as well as the remaining attackers and blockers …

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 603.2c

An ability triggers only once each time its trigger event occurs. However, it can trigger repeatedly if one event contains multiple occurrences.

#### CR 603.3b

If multiple abilities have triggered since the last time a player received priority, the abilities are placed on the stack in a two-part process. First, each player, in APNAP order, puts each triggered ability they control with a trigger condition that isn’t another ability triggering on the stack in any order they choose. (See rule 101.4.) Second, each player, in APNAP order, puts all remaining triggered abilities they control on the stack in any order they choose. Then the game once again checks for and performs state-based actions until none are performed, then abilities that triggered …

#### CR 604.2

Static abilities create continuous effects, some of which are prevention effects or replacement effects. These effects are active as long as the permanent with the ability remains on the battlefield and has the ability, or as long as the object with the ability remains in the appropriate zone, as described in rule 113.6.

#### CR 611.2c

If a continuous effect generated by the resolution of a spell or ability modifies the characteristics or changes the controller of any objects, the set of objects it affects is determined when that continuous effect begins. After that point, the set won’t change. (Note that this works differently than a continuous effect from a static ability.) A continuous effect generated by the resolution of a spell or ability that doesn’t modify the characteristics or change the controller of any objects modifies the rules of the game, so it can affect objects that weren’t affected when that continuous …

#### CR 701.36a

To populate means to choose a creature token you control and create a token that’s a copy of that creature token.

#### CR 702.4b

If at least one attacking or blocking creature has first strike (see rule 702.7) or double strike as the combat damage step begins, the only creatures that assign combat damage in that step are those with first strike or double strike. After that step, instead of proceeding to the end of combat step, the phase gets a second combat damage step. The only creatures that assign combat damage in that step are the remaining attackers and blockers that had neither first strike nor double strike as the first combat damage step began, as well as the remaining attackers and blockers that currently have …

#### CR 702.49a

Ninjutsu is an activated ability that functions only while the card with ninjutsu is in a player’s hand. “Ninjutsu [cost]” means “[Cost], Reveal this card from your hand, Return an unblocked attacking creature you control to its owner’s hand: Put this card onto the battlefield from your hand tapped and attacking.”

#### CR 702.49c

The creature put onto the battlefield with the ninjutsu ability enters attacking the same player, planeswalker, or battle as the creature that was returned to its owner’s hand.

#### CR 702.190a

Sneak is a keyword that represents a static ability that functions while the spell with sneak is on the stack. “Sneak [cost]” means “Any time you could cast an instant during your declare blockers step, you may cast this spell by paying [cost] and returning an unblocked creature you control to its owner’s hand rather than paying this spell’s mana cost.”

