---
title: "Marchesa, the Black Rose — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Marchesa, the Black Rose — Interaction Review

> Bot cycle 51 · batch D · reviewed 2026-10-16. Deck: [Marchesa, the Black Rose](../decks/marchesa-the-black-rose.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-15), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/marchesa-the-black-rose.txt`](../../exports/grixis-archidekt/marchesa-the-black-rose.txt) · SHA-256 `cbea04a72dd309e4d99dcbffc8d4c8674a6c0d5ba4533a668a28e2dcd564131a` |
| Rulings | **11** (11 verified · 0 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-15 · rulings 2026-10-15 |
| Source attestations | [`Marchesa_the_Black_Rose_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/marchesa_the_black_rose_2026-10-15/Marchesa_the_Black_Rose_Rules_Attestation.json) (13 interactions, all PASS) |

## Contents
- [Summary](#summary)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [Key card-pair interactions](#key-card-pair-interactions)
- [Timing and priority](#timing-and-priority)
- [Replacement and prevention effects](#replacement-and-prevention-effects)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [Rules cited](#rules-cited)

## Summary

Marchesa gives the team dethrone and brings back any creature that dies with a +1/+1 counter. The list is built around persist: Murderous Redcap, Glen Elendra, River Kelpie, Puppeteer Clique and Spark Double, reset by Gev, Metallic Mimic, Uncivil Unrest or Thran Vigil, plus free sac outlets and Mikaeus. Draw comes from Satoru, Kelpie and Danny Pink. All 13 attestation items are re-verified; 48 Spellbook lines have all pieces in the canonical list, and representative ones are cited.

Rules surprises: Thran Vigil resets work only on your turn; Uncivil Unrest doubles only the first Redcap shot; deaths during the end step return a turn later, which makes Sneak Attack permanent; Agatha's Soul Cauldron can't share Ashnod's Altar.

## Commander rules text and edge cases

### marchbr-01: Dethrone for the team; creatures with +1/+1 counters return at the next end step

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Marchesa, the Black Rose

**Ruling.** Your other creatures have dethrone, so each attack on the player with the most life (or tied) adds a +1/+1 counter before blockers. Each instance triggers separately. Attacking a planeswalker or battle doesn't count. When a creature you control dies with a +1/+1 counter on it, Marchesa sets up a delayed return at the beginning of the next end step. That includes Marchesa herself. If the card leaves the graveyard first, it doesn't return, even if it comes back to the graveyard. If the death happens during an end step, the return waits until the next turn's end step.

**Citations**

- Oracle, *Marchesa, the Black Rose*: “Whenever a creature you control with a +1/+1 counter on it dies, return that card to the battlefield under your control at the beginning of the next end step.”
- Scryfall ruling, *Marchesa, the Black Rose*: “If the creature card leaves the graveyard before the delayed triggered ability resolves, that card won't return to the battlefield, even if it's back in the graveyard when the delayed triggered ability resolves.”
- Scryfall ruling, *Marchesa, the Black Rose*: “If Marchesa has a +1/+1 counter on it when it dies, it will return to the battlefield under your control because of its own ability.”
- Scryfall ruling, *Marchesa, the Black Rose*: “Dethrone doesn't trigger if the creature attacks a planeswalker, even if its controller has the most life. The same is true if the creature attacks a battle, even if its protector has the most life.”
- [CR 702.105a](#cr-702105a), [CR 603.7c](#cr-6037c), [CR 513.2](#cr-5132)
- Source (re-verified): [`Marchesa_the_Black_Rose_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/marchesa_the_black_rose_2026-10-15/Marchesa_the_Black_Rose_Rules_Attestation.json) → “Marchesa death trigger and delayed return”

## Combos and engine lines

### marchbr-03: Murderous Redcap loops: Gev / Mimic (Goblin) / Uncivil Unrest, no outlet needed

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Marchesa, the Black Rose, Murderous Redcap, Gev, Scaled Scorch, Metallic Mimic, Uncivil Unrest, Blood Artist, Zulaport Cutthroat, Syr Konrad, the Grim

**Ruling.** Redcap enters with a +1/+1 counter and aims its ETB damage at itself. It dies with no -1/-1 counter, so persist returns it. The new -1/-1 counter is cancelled by the next +1/+1 counter, so it dies to its own ETB again, and so on. Each loop is a death and ETB, and Blood Artist, Zulaport Cutthroat or Syr Konrad turns those into the kill.

With Uncivil Unrest, the first Redcap's damage is doubled because it has a counter. Later returns have no counters left after the cancellation, so their damage isn't doubled. Gev's version needs an opponent to have lost life earlier in the turn.

**Citations**

- Oracle, *Murderous Redcap*: “When this creature enters, it deals damage equal to its power to any target.”
- Oracle, *Metallic Mimic*: “Each other creature you control of the chosen type enters with an additional +1/+1 counter on it.”
- Scryfall ruling, *Uncivil Unrest*: “The damage is dealt by the same source as the original source of damage. The doubled damage isn’t dealt by Uncivil Unrest unless it was somehow the original source of damage.”
- [CR 702.79a](#cr-70279a), [CR 704.5q](#cr-7045q), [CR 704.5g](#cr-7045g)
- Commander Spellbook [1657-5805](https://commanderspellbook.com/combo/1657-5805/) (community-maintained, retrieved 2026-10-16): “Murderous Redcap enters, triggering itself, dealing damage to itself equal to its power.”
- Commander Spellbook [345-1657](https://commanderspellbook.com/combo/345-1657/) (community-maintained, retrieved 2026-10-16): “"Goblin" or "Assassin" chosen with Metallic Mimic.”
- Commander Spellbook [1657-5961](https://commanderspellbook.com/combo/1657-5961/) (community-maintained, retrieved 2026-10-16): “Murderous Redcap dies as a state-based action due to having 0 toughness.”
- Source (re-verified): [`Marchesa_the_Black_Rose_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/marchesa_the_black_rose_2026-10-15/Marchesa_the_Black_Rose_Rules_Attestation.json) → “Murderous Redcap + Gev, Scaled Scorch”
- Source (re-verified): [`Marchesa_the_Black_Rose_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/marchesa_the_black_rose_2026-10-15/Marchesa_the_Black_Rose_Rules_Attestation.json) → “Murderous Redcap + Metallic Mimic”

### marchbr-04: Free sac outlets close any persist reset: Ashnod's, Phyrexian Altar, Altar of Dementia, Goblin Bombardment, Viscera Seer, Carrion Feeder, Yahenni

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Marchesa, the Black Rose, Ashnod's Altar, Phyrexian Altar, Altar of Dementia, Goblin Bombardment, Viscera Seer, Carrion Feeder, Yahenni, Undying Partisan, Glen Elendra Archmage, River Kelpie, Puppeteer Clique

**Ruling.** Any persist creature (Redcap, Glen Elendra Archmage, River Kelpie, Puppeteer Clique) plus any persist reset (marchbr-02) plus any free sac outlet is an infinite loop. The outlet decides the result:
- Ashnod's Altar: infinite colorless mana.
- Phyrexian Altar: infinite colored mana.
- Goblin Bombardment: infinite damage.
- Altar of Dementia: mill.
- Viscera Seer: scry.
- Carrion Feeder: counters.
- Yahenni: indestructible.

Thran Vigil works only on your turn, because its trigger needs cards leaving your graveyard during your turn. The other resets also work on opponents' turns.

**Citations**

- [CR 702.79a](#cr-70279a), [CR 704.5q](#cr-7045q), [CR 701.21a](#cr-70121a)
- Commander Spellbook [2034-5961--5](https://commanderspellbook.com/combo/2034-5961--5/) (community-maintained, retrieved 2026-10-16): “Activate Ashnod's Altar by sacrificing the persist creature.”
- Commander Spellbook [4050-5961--5](https://commanderspellbook.com/combo/4050-5961--5/) (community-maintained, retrieved 2026-10-16): “Activate Phyrexian Altar by sacrificing the persist creature.”
- Commander Spellbook [5147-5961--5](https://commanderspellbook.com/combo/5147-5961--5/) (community-maintained, retrieved 2026-10-16): “Activate Goblin Bombardment by sacrificing the persist creature.”
- Source (re-verified): [`Marchesa_the_Black_Rose_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/marchesa_the_black_rose_2026-10-15/Marchesa_the_Black_Rose_Rules_Attestation.json) → “Altar of Dementia as sacrifice outlet and payoff”

### marchbr-05: Mikaeus, the Unhallowed: undying + persist alternate forever

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Marchesa, the Black Rose, Mikaeus, the Unhallowed, Ashnod's Altar, Viscera Seer, Yawgmoth, Thran Physician, Gray Merchant of Asphodel

**Ruling.** Mikaeus gives your other non-Human creatures undying. Sacrifice a non-Human persist creature: it has no -1/-1 counter, so persist returns it with one. Sacrifice it again: it has no +1/+1 counter, so undying returns it with one. Repeat. Mikaeus's +1/+1 bonus isn't a counter, so it doesn't turn undying off. Marchesa, Mikaeus and Yawgmoth are Human, so they don't get undying. Marchesa's own trigger also fires on the undying-counter deaths, but the immediate return beats her end-step one. Mikaeus + Yawgmoth + Gray Merchant is its own line (Spellbook 328-628-4279).

**Citations**

- Oracle, *Mikaeus, the Unhallowed*: “Other non-Human creatures you control get +1/+1 and have undying.”
- Scryfall ruling, *Mikaeus, the Unhallowed*: “The +1/+1 bonus that Mikaeus gives to other non-Human creatures you control isn’t a counter. It won’t prevent undying from triggering.”
- [CR 702.79a](#cr-70279a), [CR 702.93a](#cr-70293a)
- Commander Spellbook [628-2034--5](https://commanderspellbook.com/combo/628-2034--5/) (community-maintained, retrieved 2026-10-16): “When the persist creature dies, its undying ability triggers, returning it from your graveyard to the battlefield with a +1/+1 counter on it.”

### marchbr-06: Spark Double copying Glen Elendra / Redcap / Kelpie / Clique

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Marchesa, the Black Rose, Spark Double, Glen Elendra Archmage, Murderous Redcap, River Kelpie, Puppeteer Clique, Ashnod's Altar

**Ruling.** Spark Double enters as a copy with an extra +1/+1 counter, so it is its own persist reset. When it dies, persist returns the Spark Double card with a -1/-1 counter. It enters as a fresh copy, and its new +1/+1 counter cancels the -1/-1. So Spark Double + any persist creature + a free outlet loops. Copying Glen Elendra lets you sacrifice it to its own ability ({U}) or to Ashnod's Altar. With River Kelpie, each return from the graveyard draws. With Puppeteer Clique, each return reanimates an opponent's creature (Spellbook 3020-3908-5256 with Altar of Dementia).

**Citations**

- Scryfall ruling, *Spark Double*: “If it copies a planeswalker, Spark Double enters with the appropriate number of loyalty counters as printed on the card plus one. If it copies a creature, Spark Double enters with a +1/+1 counter on it, plus any counters that will be put on it from abilities it copied and other abilities of other objects.”
- [CR 707.2](#cr-7072), [CR 702.79a](#cr-70279a), [CR 704.5q](#cr-7045q)
- Commander Spellbook [1657-2034-3908](https://commanderspellbook.com/combo/1657-2034-3908/) (community-maintained, retrieved 2026-10-16): “As Spark Double enters the battlefield, choose to have it enter the battlefield as a copy of Murderous Redcap with a +1/+1 counter on it.”
- Commander Spellbook [2034-2831-3908](https://commanderspellbook.com/combo/2034-2831-3908/) (community-maintained, retrieved 2026-10-16): “As Spark Double enters the battlefield, choose to have it enter the battlefield as a copy of Glen Elendra Archmage with a +1/+1 counter on it.”
- Source (re-verified): [`Marchesa_the_Black_Rose_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/marchesa_the_black_rose_2026-10-15/Marchesa_the_Black_Rose_Rules_Attestation.json) → “Spark Double + Glen Elendra Archmage + Ashnod's Altar”

### marchbr-07: Flayer of the Hatebound + Sage of Fables + Ashnod's Altar

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Marchesa, the Black Rose, Flayer of the Hatebound, Sage of Fables, Ashnod's Altar

**Ruling.** Sacrifice Flayer to Ashnod's Altar for {C}{C}. Undying returns it with a +1/+1 counter. Flayer entered from your graveyard, so it deals damage equal to its power to any target. Then pay {2} to Sage of Fables to remove that counter and draw, which re-arms undying. The loop is mana-neutral and gives infinite damage. You can hold priority over the draws so you don't deck yourself. Flayer is a Devil, so Sage's Wizard counter doesn't apply.

**Citations**

- Oracle, *Flayer of the Hatebound*: “Whenever this creature or another creature enters from your graveyard, that creature deals damage equal to its power to any target.”
- Oracle, *Sage of Fables*: “{2}, Remove a +1/+1 counter from a creature you control: Draw a card.”
- [CR 702.93a](#cr-70293a), [CR 603.6a](#cr-6036a)
- Commander Spellbook [1123-2034-4866](https://commanderspellbook.com/combo/1123-2034-4866/) (community-maintained, retrieved 2026-10-16): “Pay {2} to activate Sage of Fables, removing the counter from Flayer and drawing a card.”

## Engines and payoffs

### marchbr-09: Return payoffs: Satoru, Twilight Diviner, River Kelpie, Danny Pink

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Marchesa, the Black Rose, Satoru, the Infiltrator, Twilight Diviner, River Kelpie, Danny Pink

**Ruling.** These pay off returns from the graveyard:
- **Satoru:** draws when nontoken creatures enter without being cast, which covers Marchesa, persist and undying returns.
- **Twilight Diviner:** once each turn, makes a token copy of a creature that entered from a graveyard. The token copies the printed card only, with no counters.
- **River Kelpie:** draws whenever any permanent enters from a graveyard.
- **Danny Pink:** gives each creature "draw the first time counters are put on it each turn". Counters a creature enters with count, so riot, Gev and Mimic draws work, and a creature that returns is a new object with a fresh first time.

**Citations**

- Oracle, *Satoru, the Infiltrator*: “Whenever Satoru and/or one or more other nontoken creatures you control enter, if none of them were cast or no mana was spent to cast them, draw a card.”
- Oracle, *Danny Pink*: “Creatures you control have "Whenever one or more counters are put on this creature for the first time each turn, draw a card."”
- Scryfall ruling, *Twilight Diviner*: “The token created by Twilight Diviner's last ability copies exactly what was printed on the original permanent and nothing else (unless that permanent is copying something else; see below). It doesn't copy whether that permanent is tapped or untapped, whether it has any counters on it or Auras and Equipment attached to it, or any non-copy effects that have changed its power, toughness, types, color, and so on.”
- [CR 122.6](#cr-1226), [CR 400.7](#cr-4007)
- Source (re-verified): [`Marchesa_the_Black_Rose_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/marchesa_the_black_rose_2026-10-15/Marchesa_the_Black_Rose_Rules_Attestation.json) → “Satoru, the Infiltrator with Marchesa returns”
- Source (re-verified): [`Marchesa_the_Black_Rose_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/marchesa_the_black_rose_2026-10-15/Marchesa_the_Black_Rose_Rules_Attestation.json) → “Twilight Diviner with graveyard returns”
- Source (re-verified): [`Marchesa_the_Black_Rose_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/marchesa_the_black_rose_2026-10-15/Marchesa_the_Black_Rose_Rules_Attestation.json) → “Danny Pink counter draw”

## Key card-pair interactions

### marchbr-10: Counter tools: Forge of Heroes, Agatha's Soul Cauldron, Unspeakable Symbol, Iron Apprentice, The Ozolith

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Marchesa, the Black Rose, Forge of Heroes, Agatha's Soul Cauldron, Unspeakable Symbol, Iron Apprentice, The Ozolith, Scorn-Blade Berserker

**Ruling.** These keep +1/+1 counters coming:
- **Forge of Heroes:** targets any commander that entered this turn, cast or not, so Marchesa gets her protective counter right away.
- **Agatha's Soul Cauldron:** {T} exiles a card from any graveyard. If it's a creature card, put a +1/+1 counter on a creature, and every creature you control with a counter gains that card's activated abilities. Exiling Ashnod's Altar doesn't work, because it's not a creature card. Exiling Carrion Feeder or Viscera Seer gives your countered creatures a sac outlet.
- **Unspeakable Symbol:** 3 life per counter, at instant speed.
- **Iron Apprentice and The Ozolith:** carry counters over when creatures die.
- **Scorn-Blade Berserker:** backup puts a counter on a target.

**Citations**

- Oracle, *Forge of Heroes*: “{T}: Choose target commander that entered this turn. Put a +1/+1 counter on it if it's a creature and a loyalty counter on it if it's a planeswalker.”
- Oracle, *Agatha's Soul Cauldron*: “Creatures you control with +1/+1 counters on them have all activated abilities of all creature cards exiled with Agatha's Soul Cauldron.”
- Scryfall ruling, *Agatha's Soul Cauldron*: “Agatha's Soul Cauldron grants only activated abilities. It doesn't grant keyword abilities (unless those keyword abilities are activated), triggered abilities, or static abilities.”
- [CR 122.6](#cr-1226), [CR 702.165a](#cr-702165a)
- Source (re-verified): [`Marchesa_the_Black_Rose_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/marchesa_the_black_rose_2026-10-15/Marchesa_the_Black_Rose_Rules_Attestation.json) → “Forge of Heroes on Marchesa”
- Source (re-verified): [`Marchesa_the_Black_Rose_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/marchesa_the_black_rose_2026-10-15/Marchesa_the_Black_Rose_Rules_Attestation.json) → “Agatha's Soul Cauldron counter and ability sharing”

## Timing and priority

### marchbr-08: Sneak Attack + Marchesa: the end-step sacrifice returns a turn later, permanently

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Marchesa, the Black Rose, Sneak Attack

**Ruling.** A Sneak Attacked creature has haste, and it gets a dethrone counter if it attacks the player with the most life. At the beginning of the end step it's sacrificed with the counter on it. Marchesa's delayed return is created during that end step, so it waits for the next turn's end step. Then the creature returns under your control with no sacrifice clause. If the creature left and came back before the end step, Sneak Attack doesn't sacrifice it.

**Citations**

- Oracle, *Sneak Attack*: “{R}: You may put a creature card from your hand onto the battlefield. That creature gains haste. Sacrifice the creature at the beginning of the next end step.”
- Scryfall ruling, *Sneak Attack*: “You sacrifice the creature only if you still control it. If that creature has left the battlefield, even if it came back, you don't sacrifice it.”
- [CR 513.2](#cr-5132), [CR 603.7c](#cr-6037c), [CR 702.105a](#cr-702105a)
- Source (re-verified): [`Marchesa_the_Black_Rose_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/marchesa_the_black_rose_2026-10-15/Marchesa_the_Black_Rose_Rules_Attestation.json) → “Sneak Attack and Marchesa end-step timing”

## Replacement and prevention effects

### marchbr-02: Persist resets: Gev, Metallic Mimic, Uncivil Unrest, Thran Vigil cancel the -1/-1 counter

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Marchesa, the Black Rose, Murderous Redcap, Gev, Scaled Scorch, Metallic Mimic, Uncivil Unrest, Thran Vigil

**Ruling.** A persist creature comes back with a -1/-1 counter. Any +1/+1 counter cancels it as a state-based action, so persist works again:
- **Gev:** an extra counter only if an opponent lost life this turn, one per such opponent.
- **Metallic Mimic:** the chosen creature type (Goblin for Murderous Redcap).
- **Uncivil Unrest:** riot. Choose the counter, not haste.
- **Thran Vigil:** its trigger adds the counter after the creature leaves your graveyard, but only during your turn.

Gev, Mimic and riot put the counter on as the creature enters, together with persist's -1/-1. A creature that enters at the same time as Gev or Mimic doesn't get their counter.

**Citations**

- Oracle, *Gev, Scaled Scorch*: “Other creatures you control enter with an additional +1/+1 counter on them for each opponent who lost life this turn.”
- Oracle, *Thran Vigil*: “Whenever one or more artifact and/or creature cards leave your graveyard during your turn, put a +1/+1 counter on target creature you control.”
- Scryfall ruling, *Gev, Scaled Scorch*: “In the case where Gev and one or more other creatures enter at the same time, those creatures won't enter with additional +1/+1 counters, even if one or more opponents lost life this turn.”
- Scryfall ruling, *Metallic Mimic*: “Creatures of the chosen type that enter the battlefield at the same time as Metallic Mimic won't enter with an additional +1/+1 counter.”
- [CR 702.79a](#cr-70279a), [CR 704.5q](#cr-7045q), [CR 614.1c](#cr-6141c), [CR 702.136a](#cr-702136a)
- Commander Spellbook [2131-2292--5](https://commanderspellbook.com/combo/2131-2292--5/) (community-maintained, retrieved 2026-10-16): “Thran Vigil triggers, putting a +1/+1 counter on that creature.”
- Commander Spellbook [1657-5805](https://commanderspellbook.com/combo/1657-5805/) (community-maintained, retrieved 2026-10-16): “An opponent has lost life this turn.”
- Source (re-verified): [`Marchesa_the_Black_Rose_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/marchesa_the_black_rose_2026-10-15/Marchesa_the_Black_Rose_Rules_Attestation.json) → “Persist plus +1/+1 counter support”

## Zones, commander tax and the command zone

### marchbr-11: Flare of Denial pitches a countered blue creature that comes back

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Marchesa, the Black Rose, Flare of Denial, Glen Elendra Archmage, River Kelpie, Puppeteer Clique, Spark Double

**Ruling.** Flare's alternative cost sacrifices a nontoken blue creature. If it has a +1/+1 counter, Marchesa returns it at the next end step. A persist creature without a -1/-1 counter comes back right away instead. That makes Glen Elendra, Kelpie and Clique nearly free pitches.

**Citations**

- Oracle, *Flare of Denial*: “You may sacrifice a nontoken blue creature rather than pay this spell's mana cost.”
- [CR 118.9](#cr-1189), [CR 702.79a](#cr-70279a)
- Source (re-verified): [`Marchesa_the_Black_Rose_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/marchesa_the_black_rose_2026-10-15/Marchesa_the_Black_Rose_Rules_Attestation.json) → “Flare of Denial alternate cost”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 118.9

Some spells have alternative costs. An alternative cost is a cost listed in a spell’s text, or applied to it from another effect, that its controller may pay rather than paying the spell’s mana cost. Alternative costs are usually phrased, “You may [action] rather than pay [this object’s] mana cost,” or “You may cast [this object] without paying its mana cost.” Note that some alternative costs are listed in keywords; see rule 702.

#### CR 122.6

Some spells and abilities refer to counters being put on an object. This refers to putting counters on that object while it’s on the battlefield and also to an object that’s given counters as it enters the battlefield.

#### CR 400.7

An object that moves from one zone to another becomes a new object with no memory of, or relation to, its previous existence. This rule has the following exceptions.

#### CR 513.2

If a permanent with an ability that triggers “at the beginning of the end step” enters the battlefield during this step, that ability won’t trigger until the next turn’s end step. Likewise, if a delayed triggered ability that triggers “at the beginning of the next end step” is created during this step, that ability won’t trigger until the next turn’s end step. In other words, the step doesn’t “back up” so those abilities can go on the stack. This rule applies only to triggered abilities; it doesn’t apply to continuous effects whose durations say “until end of turn” or “this turn.” (See rule …

#### CR 603.6a

Enters-the-battlefield abilities trigger when a permanent enters the battlefield. These are written, “When [this object] enters, . . . “ or “Whenever a [type] enters, . . .” Each time an event puts one or more permanents onto the battlefield, all permanents on the battlefield (including the newcomers) are checked for any enters-the-battlefield triggers that match the event.

#### CR 603.7c

A delayed triggered ability that refers to a particular object still affects it even if the object changes characteristics. However, if that object is no longer in the zone it’s expected to be in at the time the delayed triggered ability resolves, the ability won’t affect it. (Note that if that object left that zone and then returned, it’s a new object and thus won’t be affected. See rule 400.7.)

#### CR 614.1c

Effects that read “[This permanent] enters with . . . ,” “As [this permanent] enters . . . ,” or “[This permanent] enters as . . . “ are replacement effects.

#### CR 701.21a

To sacrifice a permanent, its controller moves it from the battlefield directly to its owner’s graveyard. A player can’t sacrifice something that isn’t a permanent, or something that’s a permanent they don’t control. Sacrificing a permanent doesn’t destroy it, so regeneration or other effects that replace destruction can’t affect this action.

#### CR 702.79a

Persist is a triggered ability. “Persist” means “When this permanent is put into a graveyard from the battlefield, if it had no -1/-1 counters on it, return it to the battlefield under its owner’s control with a -1/-1 counter on it.”

#### CR 702.93a

Undying is a triggered ability. “Undying” means “When this permanent is put into a graveyard from the battlefield, if it had no +1/+1 counters on it, return it to the battlefield under its owner’s control with a +1/+1 counter on it.”

#### CR 702.105a

Dethrone is a triggered ability. “Dethrone” means “Whenever this creature attacks the player with the most life or tied for most life, put a +1/+1 counter on this creature.”

#### CR 702.136a

Riot is a static ability. “Riot” means “You may have this permanent enter with an additional +1/+1 counter on it. If you don’t, it gains haste.”

#### CR 702.165a

Backup is a triggered ability. “Backup N” means “When this creature enters, put N +1/+1 counters on target creature. If that’s another creature, it also gains the non-backup abilities of this creature printed below this one until end of turn.” Cards with backup have one or more abilities printed after the backup ability. (Some cards with backup also have abilities printed before the backup ability.)

#### CR 704.5g

If a creature has toughness greater than 0, it has damage marked on it, and the total damage marked on it is greater than or equal to its toughness, that creature has been dealt lethal damage and is destroyed. Regeneration can replace this event.

#### CR 704.5q

If a permanent has both a +1/+1 counter and a -1/-1 counter on it, N +1/+1 and N -1/-1 counters are removed from it, where N is the smaller of the number of +1/+1 and -1/-1 counters on it.

#### CR 707.2

When copying an object, the copy acquires the copiable values of the original object’s characteristics and, for an object on the stack, choices made when casting or activating it (mode, targets, the value of X, whether it was kicked, how it will affect multiple targets, and so on). The copiable values are the values derived from the text printed on the object (that text being name, mana cost, color indicator, card type, subtype, supertype, rules text, power, toughness, and/or loyalty), as modified by other copy effects, by its face-down status, and by “as . . . enters” and “as . . . is turned …

