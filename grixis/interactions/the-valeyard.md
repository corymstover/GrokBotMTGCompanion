---
title: "The Valeyard — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# The Valeyard — Interaction Review

> Bot cycle 56 · batch F · reviewed 2026-10-16. Deck: [The Valeyard](../decks/the-valeyard.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/the-valeyard.txt`](../../exports/grixis-archidekt/the-valeyard.txt) · SHA-256 `f68cb26275da3a765e1009fc62fd6de4bb834cab57770dc6ed4f3f74578dc404` |
| Rulings | **5** (5 verified · 0 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`The_Valeyard_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/The_Valeyard_Approval_Ready_Verification_2026-10-15.md) (Approval-ready verification (no rules attestation JSON in source)) |

## Contents
- [Summary](#summary)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Layers and continuous effects](#layers-and-continuous-effects)
- [What the list depends on](#what-the-list-depends-on)
- [Legality and project exceptions](#legality-and-project-exceptions)
- [Rules cited](#rules-cited)

## Summary

The Valeyard makes opponents face each villainous choice an additional time and gives you an extra vote. The deck runs 13 villainous-choice sources plus voting cards (will of the council, council's dilemma, secret council), Valeyard copies (Spark Double, Quantum Misalignment, Sakashima, Auton Soldier) and vote payoffs (Grudge Keeper, Model of Unity, Illusion of Choice). The source has no rules attestation JSON, so this review uses the approval-ready verification. The canonical list matches its delta (Force of Will, Messenger Jays, Spark Double, Quantum Misalignment, Sakashima, Auton Soldier, Arid Mesa, City of Brass, Mana Confluence in; Prisoner's Dilemma, Windswept Heath out). No Spellbook lines.

Rules surprises: Prisoner's Dilemma isn't a vote; each Valeyard copy adds another full choice; splitting your extra vote turns off Grudge Keeper; Arid Mesa also finds basic Mountains. No list errors.

## Commander rules text and edge cases

### valeyard-01: Villainous choices are faced again, one at a time; copies add more

**Status:** ✅ verified · **Evidence:** fact · **Cards:** The Valeyard, Hunted by The Family, Great Intelligence's Plan, Damocles Base, Sword of Kang, Davros, Dalek Creator, Dr. Eggman, Ensnared by the Mara, Genesis of the Daleks, This Is How It Ends, Midnight Crusader Shuttle

**Ruling.** The Valeyard's first ability is a replacement effect. When an opponent would face a villainous choice, they face it an additional time. They complete the whole choice and its actions, then face it again, and they can pick differently each time. Each additional Valeyard (Spark Double, Quantum Misalignment, Sakashima) applies its own replacement, adding one more time.

On Hunted by The Family, each targeted creature is a separate choice. Choosing "token copy" twice gives you two tokens, and choosing "becomes 1/1" twice changes nothing more. Only opponents are affected.

**Citations**

- Oracle, *The Valeyard*: “If an opponent would face a villainous choice, they face that choice an additional time. (They can make the same or different choices.)”
- [CR 701.55a](#cr-70155a), [CR 701.55c](#cr-70155c), [CR 614.1a](#cr-6141a)
- Source (re-verified): [`The_Valeyard_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/The_Valeyard_Approval_Ready_Verification_2026-10-15.md) → “Multiple Valeyard effects stack additively: each replacement effect causes an additional villainous choice, performed one at a time under rule 701.55c”

### valeyard-02: Extra votes: only real votes count (Prisoner's Dilemma correctly cut); secret council counts

**Status:** ✅ verified · **Evidence:** fact · **Cards:** The Valeyard, Messenger Jays, Expropriate, Capital Punishment, Fateful Tempest, Mob Verdict, Trap the Trespassers, Truth or Consequences, Tyrant's Choice, Coercive Portal

**Ruling.** "While voting" applies only to actual votes. Prisoner's Dilemma has players choose silence or snitch without voting, so it never worked with Valeyard and was correctly cut. Messenger Jays is a real council's dilemma vote, so it was correctly added. Secret council cards (Mob Verdict, Trap the Trespassers, Truth or Consequences) are votes too, and your extra votes are written down at the same time. On council's dilemma each vote adds an effect: two time votes on Expropriate are two extra turns. On will of the council an extra vote can swing the majority.

**Citations**

- Oracle, *The Valeyard*: “While voting, you may vote an additional time.”
- Scryfall ruling, *Messenger Jays*: “Unlike the will of the council cards from the original Conspiracy set, where a majority of votes determined what happened, each vote made for a council’s dilemma card adds to the ultimate effect.”
- Scryfall ruling, *Mob Verdict*: “To secretly vote, each player writes down their chosen option without showing it to anyone else. Each player then keeps their vote secret until all players simultaneously reveal their votes.”
- [CR 701.38a](#cr-70138a), [CR 701.38c](#cr-70138c), [CR 701.38d](#cr-70138d)
- Source (re-verified): [`The_Valeyard_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/The_Valeyard_Approval_Ready_Verification_2026-10-15.md) → “Prisoner's Dilemma does not currently interact with The Valeyard's extra-vote ability.”
- Source (re-verified): [`The_Valeyard_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/The_Valeyard_Approval_Ready_Verification_2026-10-15.md) → “Messenger Jays is a real voting card.”

## Layers and continuous effects

### valeyard-04: Copying The Valeyard: Spark Double, Quantum Misalignment, Sakashima, Auton Soldier

**Status:** ✅ verified · **Evidence:** fact · **Cards:** The Valeyard, Spark Double, Quantum Misalignment, Sakashima of a Thousand Faces, Auton Soldier

**Ruling.** Each copy of The Valeyard has both abilities, so it adds one more villainous choice and one more vote.
- **Spark Double and Quantum Misalignment** copies aren't legendary, so the legend rule doesn't apply. Misalignment rebounds for a second token next upkeep.
- **Sakashima** stays legendary, but the legend rule doesn't apply to you while it's out. If Sakashima leaves, you must keep only one.
- **Auton Soldier** copies aren't legendary and have myriad. The myriad tokens enter attacking, and are exiled at end of combat, so they help only with instant-speed votes and choices during that combat (Split Decision, Trap the Trespassers).

**Citations**

- Oracle, *Quantum Misalignment*: “Create a token that's a copy of target creature you control, except it isn't legendary.”
- Scryfall ruling, *Spark Double*: “Spark Double isn’t legendary if it copies a legendary permanent, and this exception is copiable. If something else copies Spark Double later, that copy also won’t be legendary. If you control two or more permanents with the same name but only one is legendary, the “legend rule” doesn’t apply.”
- Scryfall ruling, *Sakashima of a Thousand Faces*: “If you control more than one legendary permanent with the same name and the "legend rule" begins applying again (perhaps because Sakashima of a Thousand Faces leaves the battlefield), you'll immediately have to comply with the rule and put all but one of those permanents into the graveyard.”
- [CR 707.2](#cr-7072), [CR 704.5j](#cr-7045j), [CR 702.116a](#cr-702116a)
- Source (re-verified): [`The_Valeyard_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/The_Valeyard_Approval_Ready_Verification_2026-10-15.md) → “The accepted copy package directly multiplies the commander's text without immediately losing copies to the legend rule.”

## What the list depends on

### valeyard-03: Grudge Keeper and Model of Unity: split votes weaken them

**Status:** ✅ verified · **Evidence:** fact · **Cards:** The Valeyard, Grudge Keeper, Model of Unity, Illusion of Choice

**Ruling.** Grudge Keeper drains an opponent only if they voted for none of your choices. If you split your extra Valeyard vote across both options, every opponent matched one of them and nobody loses life. Put both votes on the same option to keep the drain. Model of Unity works the other way: split votes let more opponents scry with you. Illusion of Choice lets you set every vote, including your own extra ones, so you can pick exactly who matches.

**Citations**

- Oracle, *Grudge Keeper*: “Whenever players finish voting, each opponent who voted for a choice you didn't vote for loses 2 life.”
- Scryfall ruling, *Grudge Keeper*: “If you have additional votes because of Brago’s Representative, and you vote for more than one choice, an opponent will lose 2 life only if they voted for none of those choices.”
- Scryfall ruling, *Illusion of Choice*: “If another player controls Ballot Broker, that player first takes their “normal” vote with you choosing the result, then that player decides whether they are taking the additional vote. If there is an additional vote, you again choose the result.”
- [CR 701.38d](#cr-70138d)

## Legality and project exceptions

### valeyard-05: Mana fix: Arid Mesa replaces a dead Windswept Heath

**Status:** ✅ verified · **Evidence:** fact · **Cards:** The Valeyard, Arid Mesa, City of Brass, Mana Confluence

**Ruling.** Windswept Heath finds only a Forest or Plains, and this list has neither, so it was a dead land. Arid Mesa finds a Mountain or Plains. Its targets are Badlands, Blood Crypt, Steam Vents, Volcanic Island and Xander's Lounge, plus the 2 basic Mountains, which the approval-ready note doesn't list. City of Brass and Mana Confluence replace the conditional checklands. The canonical list matches the approval-ready delta.

**Citations**

- Oracle, *Arid Mesa*: “{T}, Pay 1 life, Sacrifice this land: Search your library for a Mountain or Plains card, put it onto the battlefield, then shuffle.”
- [CR 205.3i](#cr-2053i), [CR 701.23a](#cr-70123a)
- Source (re-verified): [`The_Valeyard_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/The_Valeyard_Approval_Ready_Verification_2026-10-15.md) → “Windswept Heath has zero fetchable lands in the authoritative current list.”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 205.3i

Lands have their own unique set of subtypes; these subtypes are called land types. The land types are Cave, Desert, Forest, Gate, Island, Lair, Locus, Mine, Mountain, Plains, Planet, Power-Plant, Sphere, Swamp, Tower, Town, and Urza’s. Of that list, Forest, Island, Mountain, Plains, and Swamp are the basic land types. See rule 305.6.

#### CR 614.1a

Effects that use the word “instead” are replacement effects. Most replacement effects use the word “instead” to indicate what events will be replaced with other events.

#### CR 701.23a

To search for a card in a zone, look at all cards in that zone (even if it’s a hidden zone) and find a card that matches the given description.

#### CR 701.38a

Some spells and abilities instruct players to vote for one choice from a list of options to determine some aspect of the effect of that spell or ability. To vote, each player, starting with a specified player and proceeding in turn order, chooses one of those choices.

#### CR 701.38c

If the text of a spell or ability refers to “voting,” it refers only to an actual vote, not to any spell or ability that involves the players making choices or decisions without using the word “vote.”

#### CR 701.38d

If an effect gives a player multiple votes, those votes all happen at the same time the player would otherwise have voted.

#### CR 701.55a

“[A player] faces a villainous choice — [option A], or [option B]” means “[A player] chooses [option A] or [option B]. Then all actions in the chosen option are performed.”

#### CR 701.55c

A replacement effect may replace an instruction to face a villainous choice with an instruction to face that choice some number of additional times. In that case, the entire process described in rule 701.55a is performed for that player the appropriate number of times one at a time.

#### CR 702.116a

Myriad is a triggered ability that may also create a delayed triggered ability. “Myriad” means “Whenever this creature attacks, for each opponent other than defending player, you may create a token that’s a copy of this creature that’s tapped and attacking that player or a planeswalker they control. If one or more tokens are created this way, exile the tokens at end of combat.”

#### CR 704.5j

If two or more legendary permanents with the same name are controlled by the same player, that player chooses one of them, and the rest are put into their owners’ graveyards. This is called the “legend rule.”

#### CR 707.2

When copying an object, the copy acquires the copiable values of the original object’s characteristics and, for an object on the stack, choices made when casting or activating it (mode, targets, the value of X, whether it was kicked, how it will affect multiple targets, and so on). The copiable values are the values derived from the text printed on the object (that text being name, mana cost, color indicator, card type, subtype, supertype, rules text, power, toughness, and/or loyalty), as modified by other copy effects, by its face-down status, and by “as . . . enters” and “as . . . is turned …

