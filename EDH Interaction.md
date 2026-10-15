---
title: "EDH Interaction"
category: edh
tags: [removal, interaction, stax]
issues: [28]
generated_by: scripts/build_interaction.py
sources: [scryfall, edhrec]
related: ["EDH Packages.md", "EDH Standards.md", "EDH Win Conditions.md", "Rules Interactions.md", "cEDH Primer.md"]
schema: 2
---

# EDH Interaction

> **Auto-generated** by `scripts/build_interaction.py` (Bot cycle 6, issue [#28](https://github.com/corymstover/GrokBotMTGCompanion/issues/28)) from Scryfall Oracle bulk 2026-10-15. Do not hand-edit.
> **Data:** every card listed is **Commander-legal** per Scryfall. *Identity* is its color identity: it fits a deck only if that identity is a subset of the commander's ([CR 903.4](Rules%20Interactions.md#commander-color-identity)). Lists are ordered by Scryfall `edhrec_rank` (EDHREC popularity, lower = more played); popularity is not power. **GC** = official Game Changer, which affects the [Commander Brackets](EDH%20Standards.md#power-bracket-assessment). *Cheapest USD* is the lowest current paper price across printings in Scryfall's default-cards bulk (2026-10-15 snapshot; prices move daily). Categories are Oracle-text pattern matches; the patterns are listed in each section.
> **Guidance** paragraphs are strategy advice (opinion), not rules or fact. Hierarchies list buckets from most to least flexible. The bucket order is **guidance**; the card order inside each bucket is EDHREC data.

## Contents
- [Targeted removal](#targeted-removal)
- [Mass removal (board wipes)](#mass-removal-board-wipes)
- [Stack interaction](#stack-interaction)
- [Graveyard hate](#graveyard-hate)
- [Artifact & enchantment hate (static)](#artifact--enchantment-hate-static)
- [Stax & taxes](#stax--taxes)
- [How much interaction (guidance)](#how-much-interaction-guidance)

## Targeted removal

**Hierarchy (guidance):** Most flexible first: any nonland permanent > two or more types > creature only. Instant speed and low mana value are better.

### 1. Any permanent / nonland permanent

Pattern: `(destroy|exile) target (nonland )?permanent|(destroy|exile) target (artifact, creature, enchantment, or planeswalker|nonland permanent)` · 154 matches (40 instant or flash)

| Card | Speed | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|---|
| [Beast Within](cards/B/be.md#beast-within) | instant | G | 3 | 25 | $0.53 |  |
| [Generous Gift](cards/G/ge.md#generous-gift) | instant | W | 3 | 63 | $0.96 |  |
| [Assassin's Trophy](cards/A/as.md#assassins-trophy) | instant | BG | 2 | 122 | $0.96 |  |
| [Anguished Unmaking](cards/A/an.md#anguished-unmaking) | instant | WB | 3 | 153 | $1.64 |  |
| [Stroke of Midnight](cards/S/str.md#stroke-of-midnight) | instant | W | 3 | 199 | $0.25 |  |
| [Despark](cards/D/des.md#despark) | instant | WB | 2 | 407 | $0.23 |  |
| [Pyroblast](cards/P/py.md#pyroblast) | instant | R | 1 | 479 | $3.24 |  |
| [Abrupt Decay](cards/A/ab.md#abrupt-decay) | instant | BG | 2 | 751 | $1.02 |  |
| [Void Rend](cards/V/vo.md#void-rend) | instant | WUB | 3 | 757 | $0.30 |  |
| [Meteor Golem](cards/M/me.md#meteor-golem) | sorcery speed / permanent | C | 7 | 800 | $0.15 |  |

### 2. Artifact or enchantment

Pattern: `(destroy|exile) target (artifact or enchantment|artifact, enchantment|enchantment or artifact)` · 161 matches (53 instant or flash)

| Card | Speed | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|---|
| [Witch Enchanter // Witch-Blessed Meadow](cards/W/wi.md#witch-enchanter--witch-blessed-meadow) | sorcery speed / permanent | W | 4 | 290 | $6.08 |  |
| [Reclamation Sage](cards/R/rec.md#reclamation-sage) | sorcery speed / permanent | G | 3 | 332 | $0.17 |  |
| [Nature's Claim](cards/N/na.md#natures-claim) | instant | G | 1 | 382 | $0.65 |  |
| [Archdruid's Charm](cards/A/arc.md#archdruids-charm) | instant | G | 3 | 622 | $8.78 |  |
| [Krosan Grip](cards/K/kr.md#krosan-grip) | instant | G | 3 | 660 | $0.77 |  |
| [Tear Asunder](cards/T/te.md#tear-asunder) | instant | BG | 2 | 858 | $0.24 |  |
| [Aura Shards](cards/A/au.md#aura-shards) | sorcery speed / permanent | WG | 3 | 1,061 | $18.92 | **GC** |
| [Disenchant](cards/D/di.md#disenchant) | instant | W | 2 | 1,114 | $0.08 |  |
| [Kogla, the Titan Ape](cards/K/ko.md#kogla-the-titan-ape) | sorcery speed / permanent | G | 6 | 1,231 | $2.53 |  |
| [Fracture](cards/F/fr.md#fracture) | instant | WB | 2 | 1,259 | $0.35 |  |

### 3. Creature

Pattern: `(destroy|exile) target creature\b(?! card)` · 439 matches (193 instant or flash)

| Card | Speed | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|---|
| [Swords to Plowshares](cards/S/sw.md#swords-to-plowshares) | instant | W | 1 | 11 | $1.07 |  |
| [Path to Exile](cards/P/pa.md#path-to-exile) | instant | W | 1 | 15 | $0.93 |  |
| [Feed the Swarm](cards/F/fe.md#feed-the-swarm) | sorcery speed / permanent | B | 2 | 93 | $0.20 |  |
| [Pongify](cards/P/po.md#pongify) | instant | U | 1 | 155 | $2.26 |  |
| [Fell the Profane // Fell Mire](cards/F/fe.md#fell-the-profane--fell-mire) | instant | B | 4 | 198 | $5.05 |  |
| [Rapid Hybridization](cards/R/rap.md#rapid-hybridization) | instant | U | 1 | 208 | $0.83 |  |
| [Terminate](cards/T/te.md#terminate) | instant | BR | 2 | 226 | $0.27 |  |
| [Infernal Grasp](cards/I/inf.md#infernal-grasp) | instant | B | 2 | 264 | $0.26 |  |
| [Withering Torment](cards/W/wi.md#withering-torment) | instant | B | 3 | 265 | $0.93 |  |
| [Reality Shift](cards/R/rea.md#reality-shift) | instant | U | 2 | 285 | $0.26 |  |

### 4. Bounce (tempo)

Pattern: `return target (nonland permanent|creature|permanent) to its owner's hand` · 162 matches (83 instant or flash)

| Card | Speed | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|---|
| [Snap](cards/S/sn.md#snap) | instant | U | 2 | 277 | $3.28 |  |
| [Hullbreaker Horror](cards/H/hu.md#hullbreaker-horror) | instant | U | 7 | 278 | $6.06 |  |
| [Chain of Vapor](cards/C/cha.md#chain-of-vapor) | instant | U | 1 | 990 | $7.97 |  |
| [Mystic Confluence](cards/M/my.md#mystic-confluence) | instant | U | 5 | 1,473 | $0.48 |  |
| [Cryptic Command](cards/C/cr.md#cryptic-command) | instant | U | 4 | 1,610 | $3.84 |  |
| [Sublime Epiphany](cards/S/sub.md#sublime-epiphany) | instant | U | 6 | 1,688 | $0.27 |  |
| [Aether Spellbomb](cards/A/ae.md#aether-spellbomb) | sorcery speed / permanent | U | 1 | 2,713 | $0.19 |  |
| [Unsummon](cards/U/un.md#unsummon) | instant | U | 1 | 2,841 | $0.08 |  |
| [Simic Charm](cards/S/si.md#simic-charm) | instant | UG | 2 | 2,954 | $0.85 |  |
| [Jace, the Mind Sculptor](cards/J/ja.md#jace-the-mind-sculptor) | sorcery speed / permanent | U | 4 | 3,304 | $19.51 |  |

## Mass removal (board wipes)

**Hierarchy (guidance):** Guidance: run 2–4. One-sided or flexible wipes first.

### 1. Creature wipes

Pattern: `(destroy|exile) all (other )?creatures|all creatures get -\d+/-\d+|each creature gets -X/-X|deals? (\d+|X) damage to each creature` · 393 matches (55 instant or flash)

| Card | Speed | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|---|
| [Blasphemous Act](cards/B/bla.md#blasphemous-act) | sorcery speed / permanent | R | 9 | 22 | $0.76 |  |
| [Austere Command](cards/A/au.md#austere-command) | sorcery speed / permanent | W | 6 | 170 | $0.31 |  |
| [Farewell](cards/F/fa.md#farewell) | sorcery speed / permanent | W | 6 | 177 | $4.13 | **GC** |
| [Damnation](cards/D/da.md#damnation) | sorcery speed / permanent | B | 4 | 391 | $17.45 |  |
| [Supreme Verdict](cards/S/sup.md#supreme-verdict) | sorcery speed / permanent | WU | 4 | 469 | $1.52 |  |
| [The Meathook Massacre](cards/T/them.md#the-meathook-massacre) | sorcery speed / permanent | B | 2 | 516 | $24.18 |  |
| [Wrath of God](cards/W/wr.md#wrath-of-god) | sorcery speed / permanent | W | 4 | 684 | $1.03 |  |
| [Kindred Dominance](cards/K/ki.md#kindred-dominance) | sorcery speed / permanent | B | 7 | 696 | $4.58 |  |
| [Chain Reaction](cards/C/cha.md#chain-reaction) | sorcery speed / permanent | R | 4 | 708 | $0.20 |  |
| [Elspeth, Sun's Champion](cards/E/el.md#elspeth-suns-champion) | sorcery speed / permanent | W | 6 | 786 | $0.38 |  |

### 2. Everything / nonland wipes

Pattern: `(destroy|exile) all (nonland )?permanents|(destroy|exile) all artifacts, creatures, and enchantments|return all nonland permanents to their owners' hands` · 34 matches (1 instant or flash)

| Card | Speed | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|---|
| [Ruinous Ultimatum](cards/R/ru.md#ruinous-ultimatum) | sorcery speed / permanent | WBR | 7 | 651 | $0.37 |  |
| [Urza's Ruinous Blast](cards/U/ur.md#urzas-ruinous-blast) | sorcery speed / permanent | W | 5 | 1,615 | $0.97 |  |
| [Season of Gathering](cards/S/sea.md#season-of-gathering) | sorcery speed / permanent | G | 6 | 1,766 | $6.12 |  |
| [Nevinyrral's Disk](cards/N/ne.md#nevinyrrals-disk) | sorcery speed / permanent | C | 4 | 2,027 | $0.35 |  |
| [Ondu Inversion // Ondu Skyruins](cards/O/on.md#ondu-inversion--ondu-skyruins) | sorcery speed / permanent | W | 8 | 2,220 | $1.06 |  |
| [Hour of Revelation](cards/H/ho.md#hour-of-revelation) | sorcery speed / permanent | W | 6 | 3,804 | $1.31 |  |
| [Devastation Tide](cards/D/dev.md#devastation-tide) | sorcery speed / permanent | U | 5 | 4,044 | $0.33 |  |
| [Flood of Tears](cards/F/fl.md#flood-of-tears) | sorcery speed / permanent | U | 6 | 4,627 | $1.19 |  |
| [Boompile](cards/B/bo.md#boompile) | sorcery speed / permanent | C | 4 | 5,277 | $0.67 |  |
| [Akroma's Vengeance](cards/A/ak.md#akromas-vengeance) | sorcery speed / permanent | W | 6 | 6,523 | $0.43 |  |

### 3. Artifact / enchantment wipes

Pattern: `(destroy|exile) all (artifacts|enchantments|artifacts and enchantments|noncreature artifacts)` · 57 matches (7 instant or flash)

| Card | Speed | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|---|
| [Austere Command](cards/A/au.md#austere-command) | sorcery speed / permanent | W | 6 | 170 | $0.31 |  |
| [Farewell](cards/F/fa.md#farewell) | sorcery speed / permanent | W | 6 | 177 | $4.13 | **GC** |
| [Bane of Progress](cards/B/ban.md#bane-of-progress) | sorcery speed / permanent | G | 6 | 1,244 | $0.31 |  |
| [Cleansing Nova](cards/C/cl.md#cleansing-nova) | sorcery speed / permanent | W | 5 | 1,270 | $0.20 |  |
| [Nevinyrral's Disk](cards/N/ne.md#nevinyrrals-disk) | sorcery speed / permanent | C | 4 | 2,027 | $0.35 |  |
| [Merciless Eviction](cards/M/me.md#merciless-eviction) | sorcery speed / permanent | WB | 6 | 3,225 | $0.54 |  |
| [Dismantling Wave](cards/D/di.md#dismantling-wave) | sorcery speed / permanent | W | 3 | 4,196 | $0.27 |  |
| [Fade from History](cards/F/fa.md#fade-from-history) | sorcery speed / permanent | G | 4 | 4,837 | $3.78 |  |
| [Brotherhood's End](cards/B/br.md#brotherhoods-end) | sorcery speed / permanent | R | 3 | 6,218 | $1.06 |  |
| [Akroma's Vengeance](cards/A/ak.md#akromas-vengeance) | sorcery speed / permanent | W | 6 | 6,523 | $0.43 |  |

## Stack interaction

**Hierarchy (guidance):** Most flexible first: hard counter > soft counter > narrow counter. Free spells matter at high power.

### 1. Hard counters (any spell)

Pattern: `^Counter target spell\.|Counter target spell\. ` · 90 matches (90 instant or flash)

| Card | Speed | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|---|
| [Counterspell](cards/C/cou.md#counterspell) | instant | U | 2 | 16 | $1.34 |  |
| [Arcane Denial](cards/A/arc.md#arcane-denial) | instant | U | 2 | 52 | $1.83 |  |
| [Mana Drain](cards/M/man.md#mana-drain) | instant | U | 2 | 119 | $51.87 |  |
| [Pact of Negation](cards/P/pa.md#pact-of-negation) | instant | U | 0 | 370 | $16.22 |  |
| [Tibalt's Trickery](cards/T/ti.md#tibalts-trickery) | instant | R | 2 | 600 | $10.04 |  |
| [Rewind](cards/R/rew.md#rewind) | instant | U | 4 | 1,016 | $0.35 |  |
| [Three Steps Ahead](cards/T/thr.md#three-steps-ahead) | instant | U | 1 | 1,072 | $4.32 |  |
| [Cryptic Command](cards/C/cr.md#cryptic-command) | instant | U | 4 | 1,610 | $3.84 |  |
| [Sublime Epiphany](cards/S/sub.md#sublime-epiphany) | instant | U | 6 | 1,688 | $0.27 |  |
| [Archmage's Charm](cards/A/arc.md#archmages-charm) | instant | U | 3 | 1,741 | $1.73 |  |

### 2. Free / alternative-cost counters

Pattern: `rather than pay this spell's mana cost[^.]*|If you control a commander, you may cast this spell without paying` · 9 matches (9 instant or flash)

| Card | Speed | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|---|
| [Fierce Guardianship](cards/F/fi.md#fierce-guardianship) | instant | U | 3 | 82 | $60.84 | **GC** |
| [Force of Will](cards/F/fo.md#force-of-will) | instant | U | 5 | 202 | $26.56 | **GC** |
| [Force of Negation](cards/F/fo.md#force-of-negation) | instant | U | 3 | 272 | $44.31 |  |
| [Flare of Denial](cards/F/fl.md#flare-of-denial) | instant | U | 3 | 1,444 | $3.53 |  |
| [Daze](cards/D/da.md#daze) | instant | U | 2 | 3,002 | $0.88 |  |
| [Foil](cards/F/fo.md#foil) | instant | U | 4 | 4,263 | $1.67 |  |
| [Disrupting Shoal](cards/D/di.md#disrupting-shoal) | instant | U | 2 | 9,431 | $15.99 |  |
| [Admiral's Order](cards/A/ad.md#admirals-order) | instant | U | 3 | 11,499 | $0.30 |  |
| [Thwart](cards/T/thw.md#thwart) | instant | U | 4 | 15,512 | $0.79 |  |

### 3. Soft & conditional counters

Pattern: `counter target (noncreature|creature|instant|sorcery|activated|spell)[^.]*(unless|with mana value)|counter target noncreature spell` · 116 matches (116 instant or flash)

| Card | Speed | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|---|
| [An Offer You Can't Refuse](cards/A/an.md#an-offer-you-cant-refuse) | instant | U | 1 | 34 | $2.82 |  |
| [Negate](cards/N/ne.md#negate) | instant | U | 2 | 57 | $0.14 |  |
| [Fierce Guardianship](cards/F/fi.md#fierce-guardianship) | instant | U | 3 | 82 | $60.84 | **GC** |
| [Dovin's Veto](cards/D/do.md#dovins-veto) | instant | WU | 2 | 229 | $2.33 |  |
| [Force of Negation](cards/F/fo.md#force-of-negation) | instant | U | 3 | 272 | $44.31 |  |
| [Flusterstorm](cards/F/fl.md#flusterstorm) | instant | U | 1 | 309 | $4.89 |  |
| [Mental Misstep](cards/M/me.md#mental-misstep) | instant | U | 1 | 473 | $5.87 |  |
| [Spell Pierce](cards/S/spe.md#spell-pierce) | instant | U | 1 | 903 | $0.25 |  |
| [Unwind](cards/U/un.md#unwind) | instant | U | 3 | 1,063 | $1.61 |  |
| [Drown in the Loch](cards/D/dro.md#drown-in-the-loch) | instant | UB | 2 | 1,460 | $1.07 |  |

### 4. Ability counters (Stifle effects)

Pattern: `counter target (activated or triggered ability|activated ability|triggered ability)` · 23 matches (16 instant or flash)

| Card | Speed | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|---|
| [Sublime Epiphany](cards/S/sub.md#sublime-epiphany) | instant | U | 6 | 1,688 | $0.27 |  |
| [Stifle](cards/S/sti.md#stifle) | instant | U | 1 | 4,596 | $8.24 |  |
| [Tale's End](cards/T/ta.md#tales-end) | instant | U | 2 | 4,854 | $3.17 |  |
| [Green Slime](cards/G/gre.md#green-slime) | instant | G | 3 | 5,601 | $1.57 |  |
| [Louisoix's Sacrifice](cards/L/lo.md#louisoixs-sacrifice) | instant | U | 1 | 6,026 | $0.31 |  |
| [Nimble Obstructionist](cards/N/ni.md#nimble-obstructionist) | instant | U | 3 | 6,362 | $0.37 |  |
| [Defabricate](cards/D/def.md#defabricate) | instant | U | 2 | 6,512 | $0.22 |  |
| [Trickbind](cards/T/tri.md#trickbind) | instant | U | 2 | 6,544 | $10.32 |  |
| [Consign to Memory](cards/C/con.md#consign-to-memory) | instant | U | 1 | 7,268 | $3.46 |  |
| [Adric, Mathematical Genius](cards/A/ad.md#adric-mathematical-genius) | sorcery speed / permanent | U | 2 | 8,096 | $0.36 |  |

## Graveyard hate

**Hierarchy (guidance):** Permanent hate > repeatable > one-shot. ⚠️ It also hurts your own graveyard plans.

### 1. Static graveyard hate

Pattern: `(If a card|If a nontoken creature|cards?)[^.]*would be put into (a|an opponent's|your opponents') graveyard[^.]*exile it instead|Cards in graveyards (lose|can't)|Players can't cast spells from graveyards` · 16 matches (0 instant or flash)

| Card | Speed | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|---|
| [Valgavoth, Terror Eater](cards/V/va.md#valgavoth-terror-eater) | sorcery speed / permanent | B | 9 | 1,298 | $17.66 |  |
| [Grafdigger's Cage](cards/G/gra.md#grafdiggers-cage) | sorcery speed / permanent | C | 1 | 2,151 | $2.23 |  |
| [Rest in Peace](cards/R/res.md#rest-in-peace) | sorcery speed / permanent | W | 2 | 2,314 | $0.74 |  |
| [Soulless Jailer](cards/S/so.md#soulless-jailer) | sorcery speed / permanent | C | 2 | 3,298 | $1.36 |  |
| [Leyline of the Void](cards/L/le.md#leyline-of-the-void) | sorcery speed / permanent | B | 4 | 3,534 | $0.36 |  |
| [Ashes of the Abhorrent](cards/A/as.md#ashes-of-the-abhorrent) | sorcery speed / permanent | W | 2 | 8,298 | $0.71 |  |
| [Weathered Runestone](cards/W/we.md#weathered-runestone) | sorcery speed / permanent | C | 2 | 8,321 | $0.34 |  |
| [Kunoros, Hound of Athreos](cards/K/ku.md#kunoros-hound-of-athreos) | sorcery speed / permanent | WB | 3 | 9,329 | $0.39 |  |
| [Tomik, Distinguished Advokist](cards/T/to.md#tomik-distinguished-advokist) | sorcery speed / permanent | W | 2 | 11,139 | $0.33 |  |
| [Ground Seal](cards/G/gro.md#ground-seal) | sorcery speed / permanent | G | 2 | 11,242 | $0.19 |  |

### 2. Repeatable / instant-speed exile

Pattern: `exile (target card from a graveyard|all cards from target player's graveyard|target player's graveyard|each opponent's graveyard|all graveyards|all cards from all graveyards|up to \w+ target cards? from (a single graveyard|graveyards))` · 114 matches (31 instant or flash)

| Card | Speed | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|---|
| [Rakdos Charm](cards/R/rak.md#rakdos-charm) | instant | BR | 2 | 326 | $0.38 |  |
| [Boggart Trawler // Boggart Bog](cards/B/bo.md#boggart-trawler--boggart-bog) | sorcery speed / permanent | B | 3 | 632 | $1.74 |  |
| [Return to Nature](cards/R/ret.md#return-to-nature) | instant | G | 2 | 785 | $0.17 |  |
| [Soul-Guide Lantern](cards/S/so.md#soul-guide-lantern) | sorcery speed / permanent | C | 1 | 1,346 | $0.21 |  |
| [Agatha's Soul Cauldron](cards/A/ag.md#agathas-soul-cauldron) | sorcery speed / permanent | C | 2 | 1,382 | $37.95 |  |
| [Scavenging Ooze](cards/S/sc.md#scavenging-ooze) | sorcery speed / permanent | G | 2 | 1,603 | $0.18 |  |
| [Lion Sash](cards/L/li.md#lion-sash) | sorcery speed / permanent | W | 2 | 1,810 | $2.08 |  |
| [Tormod's Crypt](cards/T/to.md#tormods-crypt) | sorcery speed / permanent | C | 0 | 1,841 | $0.40 |  |
| [Kozilek's Command](cards/K/ko.md#kozileks-command) | instant | C | 2 | 2,066 | $7.90 |  |
| [Rest in Peace](cards/R/res.md#rest-in-peace) | sorcery speed / permanent | W | 2 | 2,314 | $0.74 |  |

## Artifact & enchantment hate (static)

**Hierarchy (guidance):** Static or repeatable answers to artifacts and enchantments.

### 1. Repeatable answers on permanents

Pattern: `(destroy|exile) target (artifact|enchantment)[^.]*\.|artifacts (your opponents control )?(don't|can't)|activated abilities of artifacts can't` · 208 matches (4 instant or flash)

| Card | Speed | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|---|
| [Witch Enchanter // Witch-Blessed Meadow](cards/W/wi.md#witch-enchanter--witch-blessed-meadow) | sorcery speed / permanent | W | 4 | 290 | $6.08 |  |
| [Reclamation Sage](cards/R/rec.md#reclamation-sage) | sorcery speed / permanent | G | 3 | 332 | $0.17 |  |
| [Cankerbloom](cards/C/can.md#cankerbloom) | sorcery speed / permanent | G | 2 | 827 | $0.36 |  |
| [Aura Shards](cards/A/au.md#aura-shards) | sorcery speed / permanent | WG | 3 | 1,061 | $18.92 | **GC** |
| [Kogla, the Titan Ape](cards/K/ko.md#kogla-the-titan-ape) | sorcery speed / permanent | G | 6 | 1,231 | $2.53 |  |
| [Glissa Sunslayer](cards/G/gl.md#glissa-sunslayer) | sorcery speed / permanent | BG | 3 | 1,379 | $0.78 |  |
| [Cathar Commando](cards/C/cat.md#cathar-commando) | instant | W | 2 | 1,436 | $0.23 |  |
| [Acidic Slime](cards/A/ac.md#acidic-slime) | sorcery speed / permanent | G | 5 | 1,520 | $0.13 |  |
| [Zacama, Primal Calamity](cards/Z/za.md#zacama-primal-calamity) | sorcery speed / permanent | WRG | 9 | 1,814 | $1.58 |  |
| [Touch the Spirit Realm](cards/T/to.md#touch-the-spirit-realm) | sorcery speed / permanent | W | 3 | 1,867 | $0.62 |  |

## Stax & taxes

**Hierarchy (guidance):** Pieces that slow opponents' resources. ⚠️ Many are Game Changers. Mass land denial is outside Brackets 1–3 ([brackets](EDH%20Standards.md#power-bracket-assessment)).

### 1. Search / tutor hate

Pattern: `can't search libraries|If (an opponent|a player) would search a library` · 5 matches (2 instant or flash)

| Card | Speed | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|---|
| [Aven Mindcensor](cards/A/av.md#aven-mindcensor) | instant | W | 3 | 1,264 | $0.42 |  |
| [Stranglehold](cards/S/str.md#stranglehold) | sorcery speed / permanent | R | 4 | 6,843 | $7.03 |  |
| [Leonin Arbiter](cards/L/le.md#leonin-arbiter) | sorcery speed / permanent | W | 2 | 7,230 | $0.38 |  |
| [Mindlock Orb](cards/M/min.md#mindlock-orb) | sorcery speed / permanent | U | 4 | 19,090 | $0.48 |  |
| [Shadow of Doubt](cards/S/sha.md#shadow-of-doubt) | instant | UB | 2 | 19,378 | $3.65 |  |

### 2. Spell-count limits

Pattern: `(each player|players) can't cast more than one spell each turn|can't cast more than one spell each turn` · 9 matches (0 instant or flash)

| Card | Speed | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|---|
| [Archon of Emeria](cards/A/arc.md#archon-of-emeria) | sorcery speed / permanent | W | 3 | 2,134 | $1.06 |  |
| [Rule of Law](cards/R/ru.md#rule-of-law) | sorcery speed / permanent | W | 3 | 3,465 | $0.40 |  |
| [Eidolon of Rhetoric](cards/E/ei.md#eidolon-of-rhetoric) | sorcery speed / permanent | W | 3 | 3,562 | $0.47 |  |
| [High Noon](cards/H/hi.md#high-noon) | sorcery speed / permanent | WR | 2 | 7,826 | $4.69 |  |
| [Curse of Exhaustion](cards/C/cu.md#curse-of-exhaustion) | sorcery speed / permanent | W | 4 | 9,057 | $0.37 |  |
| [Arcane Laboratory](cards/A/arc.md#arcane-laboratory) | sorcery speed / permanent | U | 3 | 9,801 | $0.52 |  |
| [Moderation](cards/M/mod.md#moderation) | sorcery speed / permanent | WU | 3 | 15,428 | $0.26 |  |
| [Colfenor's Plans](cards/C/col.md#colfenors-plans) | sorcery speed / permanent | B | 4 | 19,506 | $0.37 |  |
| [Yawgmoth's Agenda](cards/Y/ya.md#yawgmoths-agenda) | sorcery speed / permanent | B | 5 | 27,168 | $0.34 |  |

### 3. Taxes

Pattern: `(spells|noncreature spells|creature spells|activated abilities)[^.]{0,40}cost \{\d\} more` · 31 matches (1 instant or flash)

| Card | Speed | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|---|
| [Grand Arbiter Augustin IV](cards/G/gra.md#grand-arbiter-augustin-iv) | sorcery speed / permanent | WU | 4 | 1,804 | $18.35 | **GC** |
| [Aura of Silence](cards/A/au.md#aura-of-silence) | sorcery speed / permanent | W | 3 | 2,201 | $2.39 |  |
| [Thalia, Guardian of Thraben](cards/T/tha.md#thalia-guardian-of-thraben) | sorcery speed / permanent | W | 2 | 2,375 | $0.42 |  |
| [God-Pharaoh's Statue](cards/G/god.md#god-pharaohs-statue) | sorcery speed / permanent | C | 6 | 2,450 | $0.67 |  |
| [Elspeth Conquers Death](cards/E/el.md#elspeth-conquers-death) | sorcery speed / permanent | W | 5 | 3,114 | $0.61 |  |
| [Charix, the Raging Isle](cards/C/cha.md#charix-the-raging-isle) | sorcery speed / permanent | U | 4 | 3,690 | $0.38 |  |
| [Paladin Class](cards/P/pa.md#paladin-class) | sorcery speed / permanent | W | 1 | 4,776 | $0.45 |  |
| [Thorn of Amethyst](cards/T/tho.md#thorn-of-amethyst) | sorcery speed / permanent | C | 2 | 6,675 | $0.55 |  |
| [Charitable Levy](cards/C/cha.md#charitable-levy) | sorcery speed / permanent | W | 2 | 7,078 | $0.19 |  |
| [Lodestone Golem](cards/L/lo.md#lodestone-golem) | sorcery speed / permanent | C | 4 | 7,247 | $0.30 |  |

### 4. Untap restriction

Pattern: `(artifacts|creatures|lands|permanents)[^.]{0,30} don't untap during (their|its controllers?') untap steps?|(creatures|artifacts|nonbasic lands|permanents|lands) (your opponents control )?enter (the battlefield )?tapped` · 21 matches (0 instant or flash)

| Card | Speed | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|---|
| [Authority of the Consuls](cards/A/au.md#authority-of-the-consuls) | sorcery speed / permanent | W | 1 | 315 | $3.90 |  |
| [Blind Obedience](cards/B/bli.md#blind-obedience) | sorcery speed / permanent | W | 2 | 504 | $4.83 |  |
| [Thalia, Heretic Cathar](cards/T/tha.md#thalia-heretic-cathar) | sorcery speed / permanent | W | 3 | 1,485 | $0.94 |  |
| [Urabrask the Hidden](cards/U/ur.md#urabrask-the-hidden) | sorcery speed / permanent | R | 5 | 1,790 | $4.37 |  |
| [Archon of Emeria](cards/A/arc.md#archon-of-emeria) | sorcery speed / permanent | W | 3 | 2,134 | $1.06 |  |
| [Manglehorn](cards/M/man.md#manglehorn) | sorcery speed / permanent | G | 3 | 2,328 | $1.32 |  |
| [Kinjalli's Sunwing](cards/K/ki.md#kinjallis-sunwing) | sorcery speed / permanent | W | 3 | 3,356 | $0.70 |  |
| [Thalia and The Gitrog Monster](cards/T/tha.md#thalia-and-the-gitrog-monster) | sorcery speed / permanent | WBG | 4 | 3,982 | $5.58 |  |
| [Dauntless Dismantler](cards/D/da.md#dauntless-dismantler) | sorcery speed / permanent | W | 2 | 4,354 | $0.30 |  |
| [Phyrexian Censor](cards/P/ph.md#phyrexian-censor) | sorcery speed / permanent | W | 3 | 4,540 | $0.38 |  |

### 5. ⚠️ Mass land denial

Pattern: `destroy all lands|each player sacrifices (all|\w+) lands|destroy all nonbasic lands|lands don't untap` · 26 matches (1 instant or flash)

| Card | Speed | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|---|
| [Armageddon](cards/A/arm.md#armageddon) | sorcery speed / permanent | W | 4 | 4,059 | $2.53 |  |
| [Back to Basics](cards/B/bac.md#back-to-basics) | sorcery speed / permanent | U | 3 | 5,445 | $2.98 |  |
| [Ruination](cards/R/ru.md#ruination) | sorcery speed / permanent | R | 4 | 8,423 | $0.74 |  |
| [Ravages of War](cards/R/rav.md#ravages-of-war) | sorcery speed / permanent | W | 4 | 11,748 | $23.31 |  |
| [Decree of Annihilation](cards/D/dec.md#decree-of-annihilation) | sorcery speed / permanent | R | 10 | 12,147 | $2.26 |  |
| [From the Ashes](cards/F/fr.md#from-the-ashes) | sorcery speed / permanent | R | 4 | 12,466 | $3.14 |  |
| [Catastrophe](cards/C/cat.md#catastrophe) | sorcery speed / permanent | W | 6 | 12,597 | $2.99 |  |
| [Wildfire](cards/W/wi.md#wildfire) | sorcery speed / permanent | R | 6 | 12,851 | $0.32 |  |
| [Impending Disaster](cards/I/im.md#impending-disaster) | sorcery speed / permanent | R | 2 | 12,920 | $0.95 |  |
| [Boom // Bust](cards/B/bo.md#boom--bust) | sorcery speed / permanent | R | 8 | 13,014 | $1.64 |  |

## How much interaction (guidance)

**Guidance (opinion):**
- Casual 100-card decks often run about **8–12 targeted answers** and **2–4 board wipes**.
- Counterspells are worth more in blue-heavy decks and at higher brackets.
- Bring at least 2–3 graveyard-hate pieces if your playgroup reanimates, or run flexible ones (artifact or land based).
- At Brackets 1–3, don't play mass land denial, and disclose heavy stax in the pre-game talk.

Related: [EDH Packages](EDH%20Packages.md) · [EDH Win Conditions](EDH%20Win%20Conditions.md) · [cEDH Primer](cEDH%20Primer.md) · [Rules: stack & priority](Rules%20Interactions.md#stack--priority).
