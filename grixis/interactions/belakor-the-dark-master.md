---
title: "Be'lakor, the Dark Master — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Be'lakor, the Dark Master — Interaction Review

> Bot cycle 46 · batch A · reviewed 2026-10-16. Deck: [Be'lakor, the Dark Master](../decks/belakor-the-dark-master.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-15), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Current list | [`exports/grixis-archidekt/belakor-the-dark-master.txt`](../../exports/grixis-archidekt/belakor-the-dark-master.txt) · SHA-256 `75543f31a16d5398fabe73ce29a2ca2999ea9e1c33f2f62b11a33b3ad7f21eb0` |
| Rulings | **13** (12 verified · 0 uncertain · 1 list flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-15 · rulings 2026-10-15 |
| Source attestations | [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) (deck #7: RULES PASS) |

## Contents
- [Summary](#summary)
- [Flags and open questions](#flags-and-open-questions)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Key card-pair interactions](#key-card-pair-interactions)
- [Timing and priority](#timing-and-priority)
- [Replacement and prevention effects](#replacement-and-prevention-effects)
- [Trigger ordering](#trigger-ordering)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [Legality and project exceptions](#legality-and-project-exceptions)
- [Rules cited](#rules-cited)

## Summary

Be'lakor, the Dark Master is a Demon tribal deck that converts Demons entering into card draw and damage. This review re-verifies the retrospective attestation (another Demon, Spark Double, Roaming Throne, Liliana's Contract names, Heartless Summoning).

Rules surprise: Be'lakor + Rite of Replication is a damage kill. The legend rule bounds the 'near-infinite card draw' label.

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [belakor-03](#belakor-03-rite-of-replication-on-belakor-legend-rule-then-the-damage) | 🚩 list flag (documentation) | Rite of Replication on Be'lakor: legend rule, then the damage | The deck page's combo guidance says the Rite line gives 'Near-infinite card draw' (Spellbook's label). The damage is the real kill (25 triggers × 6 power). The draw is bounded: the legend rule leaves one Be'lakor before Prince of Chaos resolves, and X is counted on resolution. Unkicked Rite (one token) gives two Lord triggers. No list change. |

## Commander rules text and edge cases

### belakor-01: Prince of Chaos counts Demons on resolution

**Status:** ✅ verified · **Cards:** Be'lakor, the Dark Master

**Ruling.** X is counted as the trigger resolves, including Be'lakor itself if it's still on the battlefield. You both draw and lose X life. A large X late in the game can be lethal to you, so check your life total. Vilis turns that life loss into more cards.

**Citations**

- Oracle, *Be'lakor, the Dark Master*: “Prince of Chaos — When Be'lakor enters, you draw X cards and you lose X life, where X is the number of Demons you control.”
- Scryfall ruling, *Be'lakor, the Dark Master*: “The number of Demons you control is counted only as Be'lakor, the Dark Master's ability resolves.”
- [CR 608.2h](#cr-6082h), [CR 603.2](#cr-6032)

### belakor-02: Lord of Torment: another Demon, its own power, last known information

**Status:** ✅ verified · **Cards:** Be'lakor, the Dark Master, Warstorm Surge

**Ruling.** Lord of Torment triggers only for *another* Demon entering, so Be'lakor doesn't trigger itself. The entering Demon is the damage source and deals damage equal to its power when the trigger resolves. If it has left, its last known power is used (compare Warstorm Surge's ruling). Warstorm Surge adds a second, separate trigger.

**Citations**

- Oracle, *Be'lakor, the Dark Master*: “Lord of Torment — Whenever another Demon you control enters, it deals damage equal to its power to any target.”
- Scryfall ruling, *Warstorm Surge*: “If it's no longer on the battlefield, its last known existence on the battlefield is checked to determine its power.”
- [CR 608.2h](#cr-6082h), [CR 603.2](#cr-6032)
- Source (re-verified): [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) → “Be'lakor entering does not trigger its own Lord of Torment because that ability requires another Demon.”

## Combos and engine lines

### belakor-03: Rite of Replication on Be'lakor: legend rule, then the damage

**Status:** 🚩 list flag · **Cards:** Be'lakor, the Dark Master, Rite of Replication

**Ruling.** Kicked Rite makes five token Be'lakors at once. They see each other enter. The original's Lord triggers five times and each token's triggers four times: 25 Lord triggers, each 6 damage by last known information, about 150 damage. There are also five Prince triggers.

Before any trigger goes on the stack, the legend rule leaves you one Be'lakor; the triggers still resolve. Each Prince counts only the Demons you control *on resolution*, so the draw is your surviving Demon count times five, not 'near-infinite'.

**List flag (documentation).** The deck page's combo guidance says the Rite line gives 'Near-infinite card draw' (Spellbook's label). The damage is the real kill (25 triggers × 6 power). The draw is bounded: the legend rule leaves one Be'lakor before Prince of Chaos resolves, and X is counted on resolution. Unkicked Rite (one token) gives two Lord triggers. No list change.

**Citations**

- Oracle, *Rite of Replication*: “Create a token that's a copy of target creature. If this spell was kicked, create five of those tokens instead.”
- Scryfall ruling, *Be'lakor, the Dark Master*: “The number of Demons you control is counted only as Be'lakor, the Dark Master's ability resolves.”
- Scryfall ruling, *Rite of Replication*: “Any enters-the-battlefield abilities of the copied creature will trigger when the token enters the battlefield.”
- [CR 704.5j](#cr-7045j), [CR 603.3](#cr-6033), [CR 603.6a](#cr-6036a), [CR 608.2h](#cr-6082h), [CR 117.5](#cr-1175)

## Key card-pair interactions

### belakor-04: Spark Double copies Be'lakor without the legend rule

**Status:** ✅ verified · **Cards:** Be'lakor, the Dark Master, Spark Double

**Ruling.** Spark Double copying Be'lakor isn't legendary and enters with an extra +1/+1 counter (7/6). It triggers its own Prince of Chaos (counting both Be'lakors), and the original's Lord sees another Demon enter. Spark Double can't copy something that enters at the same time as it.

**Citations**

- Scryfall ruling, *Spark Double*: “Spark Double isn’t legendary if it copies a legendary permanent, and this exception is copiable.”
- [CR 707.9b](#cr-7079b), [CR 704.5j](#cr-7045j)
- Source (re-verified): [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) → “`Spark Double` may enter as a copy of Be'lakor you control; its modification makes the copy nonlegendary and gives it an additional +1/+1 counter.”

### belakor-06: Liliana's Contract needs four different names

**Status:** ✅ verified · **Cards:** Be'lakor, the Dark Master, Liliana's Contract, Molten Echoes

**Ruling.** Liliana's Contract wins only with four or more Demons with *different names* at the start of your upkeep and again on resolution. Molten Echoes tokens (exiled at end step anyway), Rite tokens and Spark Double copies share names. Count distinct Demons, not total Demons.

**Citations**

- Oracle, *Liliana's Contract*: “At the beginning of your upkeep, if you control four or more Demons with different names, you win the game.”
- Scryfall ruling, *Liliana's Contract*: “If the second ability does trigger, but you no longer control four Demons with different names as the ability resolves, you won't win the game.”
- [CR 603.4](#cr-6034)
- Source (re-verified): [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) → “token / copy quantity alone does not bypass the different-name condition.”

### belakor-07: Heartless Summoning shrinks Lord damage

**Status:** ✅ verified · **Cards:** Be'lakor, the Dark Master, Heartless Summoning

**Ruling.** Heartless Summoning's −1/−1 lowers each entering Demon's power, so each Lord trigger deals 1 less. It reduces only generic mana costs. It also kills your own 1-toughness creatures.

**Citations**

- Oracle, *Heartless Summoning*: “Creatures you control get -1/-1.”
- [CR 613.4c](#cr-6134c)
- Source (re-verified): [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) → “`Heartless Summoning` power reduction is a real interaction cost because Be'lakor's Lord trigger uses the entering Demon's power”

### belakor-09: Vilis draws for Be'lakor's life loss

**Status:** ✅ verified · **Cards:** Be'lakor, the Dark Master, Vilis, Broker of Blood, Doom Whisperer

**Ruling.** Vilis draws a card for each life you lose: Prince of Chaos's X, Doom Whisperer's 2 life per activation, and damage dealt to you. Life paid as a cost draws after you finish activating.

**Citations**

- Oracle, *Vilis, Broker of Blood*: “Whenever you lose life, draw that many cards.”
- Scryfall ruling, *Vilis, Broker of Blood*: “If you pay life to cast a spell or activate an ability, you don't draw cards until after you've finished casting that spell or activating that ability.”
- [CR 119.3](#cr-1193), [CR 603.2](#cr-6032)

### belakor-10: Copy enablers: Molten Echoes and Reflections of Littjara

**Status:** ✅ verified · **Cards:** Be'lakor, the Dark Master, Molten Echoes, Reflections of Littjara

**Ruling.** - **Molten Echoes (Demon):** copies each nontoken Demon that enters as a hasty token, exiled at the next end step. The token is another Demon entering, so it causes another Lord trigger.
- **Reflections of Littjara (Demon):** copies Demon *spells*. The copy becomes a token, which still enters (Lord, Prince) but isn't 'created'.

Copying Be'lakor itself (a cast from the command zone with Reflections, or Molten Echoes) triggers the legend rule, but the enter triggers still happen.

**Citations**

- Oracle, *Molten Echoes*: “Whenever a nontoken creature you control of the chosen type enters, create a token that's a copy of that creature. That token gains haste.”
- Scryfall ruling, *Reflections of Littjara*: “The token that a resolving copy of a permanent spell becomes isn't "created."”
- [CR 111.13](#cr-11113), [CR 704.5j](#cr-7045j), [CR 603.6a](#cr-6036a)

## Timing and priority

### belakor-11: Cheat-in Demons still trigger Lord

**Status:** ✅ verified · **Cards:** Be'lakor, the Dark Master, Sneak Attack, Whip of Erebos, Patriarch's Bidding, Reanimate, Ghostly Flicker

**Ruling.** Lord of Torment triggers however the Demon enters. Sneak Attack (sacrificed at end step), Whip of Erebos (exiled at end step), Reanimate, Patriarch's Bidding (each player picks a type) and Ghostly Flicker on Be'lakor plus a Demon (both re-enter at once, so both Prince and Lord trigger) all count. Whip also gives lifelink to your creatures, and the Lord damage is dealt by your creature.

**Citations**

- Oracle, *Sneak Attack*: “{R}: You may put a creature card from your hand onto the battlefield. That creature gains haste. Sacrifice the creature at the beginning of the next end step.”
- [CR 603.6a](#cr-6036a), [CR 702.15b](#cr-70215b)

## Replacement and prevention effects

### belakor-08: Bloodletter doubles life loss; Sower of Discord passes it on

**Status:** ✅ verified · **Cards:** Be'lakor, the Dark Master, Bloodletter of Aclazotz, Sower of Discord, Archfiend of Despair

**Ruling.** - **Bloodletter of Aclazotz:** opponents' life loss on your turn is doubled. The damage dealt isn't doubled, so lifelink gains are unchanged.
- **Sower of Discord:** when one chosen player is dealt damage, the other chosen player loses that much life. That's loss, not damage, from no source.
- **Archfiend of Despair:** at end step each opponent loses again the life they lost that turn.

A Lord trigger on your turn can therefore cost opponents several times its power.

**Citations**

- Scryfall ruling, *Bloodletter of Aclazotz*: “Bloodletter of Aclazotz's last ability doesn't change the amount of damage dealt to opponents.”
- Scryfall ruling, *Sower of Discord*: “Sower of Discord’s triggered ability causes the second player to lose life. This isn’t damage and it’s not caused by the source that dealt damage to the first player.”
- [CR 614.1a](#cr-6141a), [CR 120.3](#cr-1203)

## Trigger ordering

### belakor-05: Roaming Throne and Panharmonicon stack

**Status:** ✅ verified · **Cards:** Be'lakor, the Dark Master, Roaming Throne, Panharmonicon

**Ruling.** Roaming Throne (Demon) and Panharmonicon each add one extra trigger for Be'lakor's two abilities. Throne covers triggered abilities of other Demon creatures; Panharmonicon covers triggers caused by an artifact or creature entering. With both, each Prince and Lord trigger happens three times. Each instance picks its own target.

**Citations**

- Oracle, *Panharmonicon*: “If an artifact or creature entering causes a triggered ability of a permanent you control to trigger, that ability triggers an additional time.”
- Scryfall ruling, *Roaming Throne*: “Roaming Throne's last ability doesn't copy the triggered ability; it just causes the ability to trigger an additional time.”
- [CR 603.2](#cr-6032), [CR 603.3b](#cr-6033b)
- Source (re-verified): [`Retrospective_1_to_8_Rules_Attestation_2026-10-14.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Rules_Attestation_2026-10-14.md) → “`Roaming Throne` choosing Demon causes triggered abilities of another Demon creature you control to trigger an additional time”

## Zones, commander tax and the command zone

### belakor-13: Commander tax at six mana

**Status:** ✅ verified · **Cards:** Be'lakor, the Dark Master, Herald of Slaanesh, Urza's Incubator, Ancient Cellarspawn

**Ruling.** Be'lakor costs {3}{U}{B}{R} (6), then 8, then 10. Demon cost reducers (Herald of Slaanesh −2, Urza's Incubator −2 on Demon creature spells, Ancient Cellarspawn −1) apply to Be'lakor because it's a Demon. Reductions reduce only generic mana, tax included.

**Citations**

- Oracle, *Herald of Slaanesh*: “Locus of Slaanesh — Demon spells you cast cost {2} less to cast.”
- [CR 903.8](#cr-9038), [CR 601.2f](#cr-6012f)

## Legality and project exceptions

### belakor-12: Gyruda in the 99, not as companion

**Status:** ✅ verified · **Cards:** Be'lakor, the Dark Master, Gyruda, Doom of Depths

**Ruling.** Gyruda is played in the main deck, so its companion condition (even mana values only) doesn't apply. It's a Demon Kraken, so it triggers Lord on entering.

**Citations**

- Oracle, *Gyruda, Doom of Depths*: “Companion — Your starting deck contains only cards with even mana values.”
- [CR 702.139a](#cr-702139a)

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 111.13

A copy of a permanent spell becomes a token as it resolves. The token has the characteristics of the spell that became that token. The token is not “created” for the purposes of any replacement effects or triggered abilities that refer to creating a token.

#### CR 117.5

Each time a player would get priority, the game first performs all applicable state-based actions as a single event (see rule 704, “State-Based Actions”), then repeats this process until no state-based actions are performed. Then triggered abilities are put on the stack (see rule 603, “Handling Triggered Abilities”). These steps repeat in order until no further state-based actions are performed and no abilities trigger. Then the player who would have received priority does so.

#### CR 119.3

If an effect causes a player to gain life or lose life, that player’s life total is adjusted accordingly.

#### CR 120.3

Damage may have one or more of the following results, depending on whether the recipient of the damage is a player or permanent, the characteristics of the damage’s source, and the characteristics of the damage’s recipient (if it’s a permanent).

#### CR 601.2f

The player determines the total cost of the spell. Usually this is just the mana cost. Some spells have additional or alternative costs. Some effects may increase or reduce the cost to pay, or may provide other alternative costs. Costs may include paying mana, tapping permanents, sacrificing permanents, discarding cards, and so on. The total cost is the mana cost or alternative cost (as determined in rule 601.2b), plus all additional costs and cost increases, and minus all cost reductions. If multiple cost reductions apply, the player may apply them in any order. If the mana component of the …

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 603.3

Once an ability has triggered, its controller puts it on the stack as an object that’s not a card the next time a player would receive priority. See rule 117, “Timing and Priority.” The ability becomes the topmost object on the stack. It has the text of the ability that created it, and no other characteristics. It remains on the stack until it’s countered, it resolves, a rule causes it to be removed from the stack, or an effect moves it elsewhere.

#### CR 603.3b

If multiple abilities have triggered since the last time a player received priority, the abilities are placed on the stack in a two-part process. First, each player, in APNAP order, puts each triggered ability they control with a trigger condition that isn’t another ability triggering on the stack in any order they choose. (See rule 101.4.) Second, each player, in APNAP order, puts all remaining triggered abilities they control on the stack in any order they choose. Then the game once again checks for and performs state-based actions until none are performed, then abilities that triggered …

#### CR 603.4

A triggered ability may read “When/Whenever/At [trigger event], if [condition], [effect].” When the trigger event occurs, the ability checks whether the stated condition is true. The ability triggers only if it is; otherwise it does nothing. If the ability triggers, it checks the stated condition again as it resolves. If the condition isn’t true at that time, the ability is removed from the stack and does nothing. Note that this mirrors the check for legal targets. This rule is referred to as the “intervening ‘if’ clause” rule. (The word “if” has only its normal English meaning anywhere else …

#### CR 603.6a

Enters-the-battlefield abilities trigger when a permanent enters the battlefield. These are written, “When [this object] enters, . . . “ or “Whenever a [type] enters, . . .” Each time an event puts one or more permanents onto the battlefield, all permanents on the battlefield (including the newcomers) are checked for any enters-the-battlefield triggers that match the event.

#### CR 608.2h

If an effect requires information from the game (such as the number of creatures on the battlefield), the answer is determined only once, when the effect is applied. If the effect requires information from a specific object, including the source of the ability itself, the effect uses the current information of that object if it’s in the public zone it was expected to be in; if it’s no longer in that zone, or if the effect has moved it from a public zone to a hidden zone, the effect uses the object’s last known information. See rule 113.7a. If an ability states that an object does something, …

#### CR 613.4c

Layer 7c: Effects and counters that modify power and/or toughness (but don’t set power and/or toughness to a specific number or value) are applied.

#### CR 614.1a

Effects that use the word “instead” are replacement effects. Most replacement effects use the word “instead” to indicate what events will be replaced with other events.

#### CR 702.15b

Damage dealt by a source with lifelink causes that source’s controller, or its owner if it has no controller, to gain that much life (in addition to any other results that damage causes). See rule 120.3.

#### CR 702.139a

Companion is a keyword ability that functions outside the game. It’s written as “Companion—[Condition].” Before the game begins, you may reveal one card you own from outside the game with a companion ability whose condition is fulfilled by your starting deck. (See rule 103.2b.) Once during the game, any time you have priority and the stack is empty, but only during a main phase of your turn, you may pay {3} and put that card into your hand. This is a special action that doesn’t use the stack (see rule 116.2g). This is a change from previous rules.

#### CR 704.5j

If two or more legendary permanents with the same name are controlled by the same player, that player chooses one of them, and the rest are put into their owners’ graveyards. This is called the “legend rule.”

#### CR 707.9b

Some copy effects modify a characteristic as part of the copying process. The final set of values for that characteristic becomes part of the copiable values of the copy.

#### CR 903.8

A player may cast a commander they own from the command zone. A commander cast from the command zone costs an additional {2} for each previous time the player casting it has cast it from the command zone that game. This additional cost is informally known as the “commander tax.”

