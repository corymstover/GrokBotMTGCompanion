---
title: "Missy — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Missy — Interaction Review

> Bot cycle 51 · batch D · reviewed 2026-10-16. Deck: [Missy](../decks/missy.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/missy.txt`](../../exports/grixis-archidekt/missy.txt) · SHA-256 `6127c9e74e6e7cc22f9d98b5f93038b7cd957dd70c6bf12efb1285a8d5ac129e` |
| Rulings | **9** (9 verified · 0 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`Missy_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Missy_Approval_Ready_Verification_2026-10-15.md) (Approval-ready verification; rules sections 5–11 re-checked against Oracle, rulings and CR) |

## Contents
- [Summary](#summary)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [Trigger ordering](#trigger-ordering)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [What the list depends on](#what-the-list-depends-on)
- [Rules cited](#rules-cited)

## Summary

Missy returns any nonartifact creature that dies to your side as a face-down 2/2 artifact Cyberman. Free-reveal morphs (Ripper, Savants, Ambusher) loop with any free sac outlet, nonartifact wipes hand you opponents' creatures, and The Valeyard doubles her end-step villainous choice. All 17 Spellbook lines in the canonical list are covered.

Rules surprises: face-down Cybermen are artifacts and won't return until turned face up; Missy still returns creatures that die alongside her; opponents can pick the damage choice when you have no artifact creatures, and then nothing happens; "chaos ensues" does nothing here; Pipes forces a draw on every loop. No list errors.

## Commander rules text and edge cases

### missy-01: Any nonartifact creature that dies returns to you face down as a 2/2 Cyberman artifact

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Missy

**Ruling.** Whenever another nonartifact creature dies, yours or an opponent's, Missy returns it to the battlefield under your control, face down and tapped. It's a 2/2 colorless, nameless Cyberman artifact creature. Because it's now an artifact, it won't return a second time if it dies while face down. Turn it face up first and Missy's effect ends, so it's a nonartifact creature again. Face-down cards can be turned face up with their morph cost or with an effect. Turning one face up doesn't make it enter again. Tokens that die cease to exist, so they can't come back. If an opponent's commander dies, its owner can move it to the command zone as a state-based action before Missy's trigger resolves.

**Citations**

- Oracle, *Missy*: “Whenever another nonartifact creature dies, return it to the battlefield under your control face down and tapped. It's a 2/2 Cyberman artifact creature.”
- Scryfall ruling, *Missy*: “Each creature turned face down this way or put onto the battlefield this way is a 2/2 Cyberman artifact creature with no name and no color.”
- Scryfall ruling, *Missy*: “If, for any reason, the face-down creature is turned face up, the effect making it a Cyberman ends. It will be whatever is printed on the card.”
- Scryfall ruling, *Missy*: “If the face-down card has a morph ability, its controller may turn it face up by paying the associated morph cost.”
- [CR 708.2](#cr-7082), [CR 708.8](#cr-7088), [CR 111.7](#cr-1117), [CR 903.9a](#cr-9039a)
- Source (re-verified): [`Missy_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Missy_Approval_Ready_Verification_2026-10-15.md) → “Turning a face-down permanent face up does not cause it to leave and re-enter the battlefield.”

## Combos and engine lines

### missy-02: Free morph loops: Ruthless Ripper / Dragon's Eye Savants / Horde Ambusher + free sac outlet

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Missy, Ruthless Ripper, Dragon's Eye Savants, Horde Ambusher, Ashnod's Altar, Phyrexian Altar, Goblin Bombardment, Viscera Seer, Altar of Dementia

**Ruling.** Loop:
1. Sacrifice the face-up creature to a free outlet.
2. Missy returns it face down.
3. Turn it face up by revealing a card of its color from your hand. That's a special action, so it costs no mana and doesn't use the stack.
4. Repeat.

Ruthless Ripper also makes a target player lose 2 life each time it turns face up. Ashnod's Altar makes infinite colorless mana, Phyrexian Altar infinite colored, Goblin Bombardment infinite damage. With Altar of Dementia, Ripper (power 1) and Ambusher mill, but Savants (power 0) mills nothing. You need a black, blue or red card in hand to reveal.

**Citations**

- Oracle, *Ruthless Ripper*: “When this creature is turned face up, target player loses 2 life.”
- [CR 702.37e](#cr-70237e), [CR 116.2b](#cr-1162b), [CR 708.8](#cr-7088)
- Commander Spellbook [1794-2034-4424](https://commanderspellbook.com/combo/1794-2034-4424/) (community-maintained, retrieved 2026-10-16): “Activate Ruthless Ripper's morph ability by revealing a black card from your hand, turning it face up.”
- Commander Spellbook [3565-4050-4424](https://commanderspellbook.com/combo/3565-4050-4424/) (community-maintained, retrieved 2026-10-16): “Activate Dragon's Eye Savants's morph ability by revealing a blue card from your hand, turning it face up.”
- Commander Spellbook [1045-4424-5147](https://commanderspellbook.com/combo/1045-4424-5147/) (community-maintained, retrieved 2026-10-16): “Activate Horde Ambusher's morph ability by revealing a red card from your hand, turning it face up.”
- Source (re-verified): [`Missy_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Missy_Approval_Ready_Verification_2026-10-15.md) → “Savants has printed power 0, so Altar of Dementia alone does not mill cards in the Savants loop without a power boost.”

### missy-03: Grim Haruspex + Phyrexian Altar; Ixidor + Pitiless Plunderer + Ashnod's Altar

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Missy, Grim Haruspex, Phyrexian Altar, Ixidor, Reality Sculptor, Pitiless Plunderer, Ashnod's Altar

**Ruling.** These loops need mana instead of a reveal:
- **Grim Haruspex:** morph costs {B}, and Phyrexian Altar's {B} from sacrificing it pays for it.
- **Ixidor:** {2}{U} turns any face-down creature face up, morph or not, and you skip the morph cost. Sacrificing a nontoken nonartifact creature to Ashnod's Altar gives {C}{C}, and Pitiless Plunderer adds a Treasure for the {U}. So any of your creatures loops.

**Citations**

- Oracle, *Ixidor, Reality Sculptor*: “{2}{U}: Turn target face-down creature face up.”
- Oracle, *Pitiless Plunderer*: “Whenever another creature you control dies, create a Treasure token. (It's an artifact with "{T}, Sacrifice this token: Add one mana of any color.")”
- Scryfall ruling, *Ixidor, Reality Sculptor*: “When you turn a card face up, its controller does not have to pay its Morph cost.”
- [CR 708.8](#cr-7088), [CR 116.2b](#cr-1162b)
- Commander Spellbook [631-4050-4424](https://commanderspellbook.com/combo/631-4050-4424/) (community-maintained, retrieved 2026-10-16): “Activate Grim Haruspex's morph ability by paying {B}, turning it face up.”
- Commander Spellbook [419-2034-4424-4871](https://commanderspellbook.com/combo/419-2034-4424-4871/) (community-maintained, retrieved 2026-10-16): “Activate Ixidor by paying {2}{U}, turning the creature face up.”

## Engines and payoffs

### missy-06: Villainous choices: The Valeyard doubles them; the draw option has no chaos payoff here

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Missy, The Valeyard, The Master, Gallifrey's End, Cyberman Patrol, Cybermen Squadron

**Ruling.** At your end step, each opponent in turn order chooses: each artifact creature you control deals 1 damage to them, or you draw a card. "Chaos ensues" matters only to abilities that trigger on chaos, like plane cards, and nothing in this list has one. They can pick the damage option even if you control no artifact creatures, and then nothing happens. The Valeyard makes each opponent face the choice twice, and they can choose differently each time. The Master gives a separate choice when a nontoken artifact creature you control dies, such as a face-down Cyberman: lose 4 life, or you make a token copy of the exiled card. Cyberman Patrol (afflict 3) and Cybermen Squadron (myriad) make the Cybermen hit harder.

**Citations**

- Oracle, *Missy*: “At the beginning of your end step, each opponent faces a villainous choice — Each artifact creature you control deals 1 damage to that opponent, or you draw a card and chaos ensues.”
- Oracle, *The Valeyard*: “If an opponent would face a villainous choice, they face that choice an additional time. (They can make the same or different choices.)”
- Scryfall ruling, *Missy*: “A player facing a villainous choice can always choose either option, even if one or both of the options are impossible. For example, if one of the options is to sacrifice a creature, a player who controls no creatures can still choose that option.”
- [CR 701.55a](#cr-70155a), [CR 701.55b](#cr-70155b), [CR 701.55c](#cr-70155c), [CR 701.55d](#cr-70155d)
- Source (re-verified): [`Missy_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Missy_Approval_Ready_Verification_2026-10-15.md) → “The Valeyard directly doubles the commander-specific choice event for each opponent.”

### missy-08: Morph interaction rebuys: Willbender, Boltbender, Stratus Dancer, Kadena's Silencer

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Missy, Willbender, Boltbender, Stratus Dancer, Kadena's Silencer

**Ruling.** When one of these dies, Missy returns it face down. Turning it face up again for its morph or disguise cost ({1}{U} or {1}{R}) recasts the trigger: redirect, retarget, counter an instant or sorcery, or counter all opponents' abilities. Megamorph also adds a +1/+1 counter. These Missy returns have no ward, because ward comes from casting with disguise.

**Citations**

- Oracle, *Willbender*: “When this creature is turned face up, change the target of target spell or ability with a single target.”
- Oracle, *Kadena's Silencer*: “When this creature is turned face up, counter all abilities your opponents control.”
- [CR 702.37e](#cr-70237e), [CR 702.37b](#cr-70237b), [CR 702.168a](#cr-702168a), [CR 702.168d](#cr-702168d)

## Trigger ordering

### missy-04: Face-up multipliers: Panoptic Projektor, Pyrotechnic Performer, Aphetto Runecaster

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Missy, Panoptic Projektor, Pyrotechnic Performer, Aphetto Runecaster, Ruthless Ripper

**Ruling.** Panoptic Projektor makes each "turned face up" trigger of your permanents trigger one more time. With it, Ripper drains 4 per loop, Pyrotechnic Performer deals the creature's power twice to each opponent, and Aphetto Runecaster draws twice. Projektor's {3} discount applies only to face-down spells you cast, not to Missy's returns.

**Citations**

- Oracle, *Panoptic Projektor*: “If turning a face-down permanent face up causes a triggered ability of a permanent you control to trigger, that ability triggers an additional time.”
- Oracle, *Pyrotechnic Performer*: “Whenever this creature or another creature you control is turned face up, that creature deals damage equal to its power to each opponent.”
- Scryfall ruling, *Panoptic Projektor*: “Panoptic Projektor’s last ability affects a permanent’s own abilities that trigger when it turns face up as well as other triggered abilities that trigger when that permanent turns face up. Such triggered abilities start with “when” or “whenever”.”
- [CR 603.2](#cr-6032), [CR 708.8](#cr-7088)
- Source (re-verified): [`Missy_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Missy_Approval_Ready_Verification_2026-10-15.md) → “It does **not** pay for turning Missy-returned permanents face up.”

## Zones, commander tax and the command zone

### missy-05: Wipes and edicts become theft: Delete, Their Name Is Death, Doomsday Confluence, Grave Pact, Accursed Marauder

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Missy, Delete, Their Name Is Death, Doomsday Confluence, Grave Pact, Accursed Marauder, Toxic Deluge

**Ruling.** Your Cybermen are artifacts, so they survive the nonartifact wipes:
- **Delete:** X damage to each nonartifact creature and each player.
- **Their Name Is Death:** destroys all nonartifact creatures.
- **Doomsday Confluence:** its edict mode makes each player sacrifice a nonartifact creature.

Every nonartifact creature that dies, including opponents', comes back to you as a Cyberman. Grave Pact and Accursed Marauder edicts do the same. If Missy dies in the same wipe, she still returns the others, because her trigger looks back at the moment of death.

**Citations**

- Oracle, *Delete*: “Delete deals X damage to each nonartifact creature and each player.”
- Oracle, *Their Name Is Death*: “Destroy all nonartifact creatures.”
- Oracle, *Grave Pact*: “Whenever a creature you control dies, each other player sacrifices a creature of their choice.”
- [CR 603.10a](#cr-60310a), [CR 603.6c](#cr-6036c)
- Source (re-verified): [`Missy_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Missy_Approval_Ready_Verification_2026-10-15.md) → “asymmetric wipes”

### missy-07: Turning stolen Cybermen face up: Etrata, Skirk Alarmist, Ugin's Mastery, Ixidor

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Missy, Etrata, Deadly Fugitive, Skirk Alarmist, Ugin's Mastery, Ixidor, Reality Sculptor

**Ruling.** A creature Missy brings back stays under your control after it's turned face up, because the control effect isn't part of the Cyberman effect. Ways to flip one:
- **Etrata:** gives face-down creatures "{2}{U}{B}: turn this face up". If that's impossible, you exile it and may cast it free.
- **Skirk Alarmist:** flips one but sacrifices it at the next end step. If that's during the end step, the sacrifice waits until the following turn.
- **Ugin's Mastery:** flips one when you attack with total power 6 or more.
- **Ixidor:** flips any.

A flipped stolen creature becomes a nonartifact creature, so it returns again if it dies.

**Citations**

- Oracle, *Etrata, Deadly Fugitive*: “Face-down creatures you control have "{2}{U}{B}: Turn this creature face up. If you can't, exile it, then you may cast the exiled card without paying its mana cost."”
- Oracle, *Skirk Alarmist*: “{T}: Turn target face-down creature you control face up. At the beginning of the next end step, sacrifice it.”
- Scryfall ruling, *Skirk Alarmist*: “If this ability is used during the end step, the creature is not sacrificed until the end of the next turn.”
- [CR 708.8](#cr-7088), [CR 116.2b](#cr-1162b)

## What the list depends on

### missy-09: They Came from the Pipes draws on every face-down entry, including each loop

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Missy, They Came from the Pipes, Cybership, The Cyber-Controller, Death in Heaven

**Ruling.** Every Missy return is a face-down creature entering, so They Came from the Pipes draws a card each time. In an infinite loop that's a draw per iteration. The draws are mandatory, so stop before you deck yourself. Cybership, The Cyber-Controller and Death in Heaven also put opponents' creature cards onto the battlefield face down as Cybermen under your control, and each of those draws with Pipes too.

**Citations**

- Oracle, *They Came from the Pipes*: “Whenever a face-down creature you control enters, draw a card.”
- Oracle, *Cybership*: “Whenever this Vehicle deals combat damage to a player, put the top two cards of that player's library onto the battlefield face down under your control. They're 2/2 Cyberman artifact creatures.”
- [CR 708.2](#cr-7082), [CR 121.4](#cr-1214)
- Source (re-verified): [`Missy_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Missy_Approval_Ready_Verification_2026-10-15.md) → “Cybership is therefore a direct commander-identity theft/Cyberman engine rather than a generic six-drop.”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 111.7

A token that’s in a zone other than the battlefield ceases to exist. This is a state-based action; see rule 704. (Note that if a token changes zones, applicable triggered abilities will trigger before the token ceases to exist.)

#### CR 116.2b

Turning a face-down creature face up is a special action. A player can take this action any time they have priority. See rule 708, “Face-Down Spells and Permanents.”

#### CR 121.4

A player who attempts to draw a card from a library with no cards in it loses the game the next time a player would receive priority. (This is a state-based action. See rule 704.)

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 603.6c

Leaves-the-battlefield abilities trigger when a permanent moves from the battlefield to another zone, or when a phased-in permanent leaves the game because its owner leaves the game. These are written as, but aren’t limited to, “When [this object] leaves the battlefield, . . .” or “Whenever [something] is put into a graveyard from the battlefield, . . . .” (See also rule 603.10.) An ability that attempts to do something to the card that left the battlefield checks for it only in the first zone that it went to. An ability that triggers when a card is put into a certain zone “from anywhere” is …

#### CR 603.10a

Some zone-change triggers look back in time. These are leaves-the-battlefield abilities, abilities that trigger when a player sacrifices a permanent, abilities that trigger when a card leaves a graveyard, and abilities that trigger when an object that all players can see is put into a hand or library.

#### CR 701.55a

“[A player] faces a villainous choice — [option A], or [option B]” means “[A player] chooses [option A] or [option B]. Then all actions in the chosen option are performed.”

#### CR 701.55b

While facing a villainous choice, a player may choose an option that is illegal or impossible. In that case, they perform as much of the action as is possible. This is an exception to rule 608.2d.

#### CR 701.55c

A replacement effect may replace an instruction to face a villainous choice with an instruction to face that choice some number of additional times. In that case, the entire process described in rule 701.55a is performed for that player the appropriate number of times one at a time.

#### CR 701.55d

If more than one player is instructed to face a villainous choice, the entire process described in rule 701.55a is performed for each of those players one at a time in APNAP order. This is an exception to rule 608.2e.

#### CR 702.37b

Megamorph is a variant of the morph ability. “Megamorph [cost]” means “You may cast this card as a 2/2 face-down creature with no text, no name, no subtypes, and no mana cost by paying {3} rather than paying its mana cost” and “As this permanent is turned face up, put a +1/+1 counter on it if its megamorph cost was paid to turn it face up.” A megamorph cost is a morph cost.

#### CR 702.37e

Any time you have priority, you may turn a face-down permanent you control with a morph ability face up. This is a special action; it doesn’t use the stack (see rule 116). To do this, show all players what the permanent’s morph cost would be if it were face up, pay that cost, then turn the permanent face up. (If the permanent wouldn’t have a morph cost if it were face up, it can’t be turned face up this way.) The morph effect on it ends, and it regains its normal characteristics. Any abilities relating to the permanent entering the battlefield don’t trigger when it’s turned face up and don’t …

#### CR 702.168a

Disguise is a static ability that functions in any zone from which you could play the card it’s on, and the disguise effect works any time the card is face down. “Disguise [cost]” means “You may cast this card as a 2/2 face-down creature with ward {2}, no name, no subtypes, and no mana cost by paying {3} rather than paying its mana cost.” (See rule 708, “Face-Down Spells and Permanents.”)

#### CR 702.168d

Any time you have priority, you may turn a face-down permanent you control with a disguise ability face up. This is a special action; it doesn’t use the stack (see rule 116). To do this, show all players what the permanent’s disguise cost would be if it were face up, pay that cost, then turn the permanent face up. (If the permanent wouldn’t have a disguise cost if it were face up, it can’t be turned face up this way.) The disguise effect on it ends, and it regains its normal characteristics. Any abilities relating to the permanent entering the battlefield don’t trigger when it’s turned face …

#### CR 708.2

Face-down spells and face-down permanents have no characteristics other than those listed by the ability or rules that allowed the spell or permanent to be face down. Any listed characteristics are the copiable values of that object’s characteristics. (See rule 613, “Interaction of Continuous Effects,” and rule 707, “Copying Objects.”)

#### CR 708.8

As a face-down permanent is turned face up, its copiable values revert to its normal copiable values. Any effects that have been applied to the face-down permanent still apply to the face-up permanent. Any abilities relating to the permanent entering the battlefield don’t trigger and don’t have any effect, because the permanent has already entered the battlefield.

#### CR 903.9a

If a commander is in a graveyard or in exile and that object was put into that zone since the last time state-based actions were checked, its owner may put it into the command zone. This is a state-based action. See rule 704.

