---
title: "EDH Packages"
category: edh
tags: [packages, ramp, card-advantage]
issues: [26]
generated_by: scripts/build_packages.py
sources: [scryfall, edhrec]
related: ["EDH Interaction.md", "EDH Win Conditions.md", "Rules Interactions.md", "EDH Archetypes.md", "EDH Mana Bases.md", "EDH Standards.md"]
schema: 2
---

# EDH Packages

> **Auto-generated** by `scripts/build_packages.py` (Bot cycle 6, issue [#26](https://github.com/corymstover/GrokBotMTGCompanion/issues/26)) from Scryfall Oracle bulk 2026-10-15. Do not hand-edit.
> **Data:** every card listed is **Commander-legal** per Scryfall. *Identity* is its color identity: it fits a deck only if that identity is a subset of the commander's ([CR 903.4](Rules%20Interactions.md#commander-color-identity)). Lists are ordered by Scryfall `edhrec_rank` (EDHREC popularity, lower = more played); popularity is not power. **GC** = official Game Changer, which affects the [Commander Brackets](EDH%20Standards.md#power-bracket-assessment). *Cheapest USD* is the lowest current paper price across printings in Scryfall's default-cards bulk (2026-10-15 snapshot; prices move daily). Categories are Oracle-text pattern matches; the patterns are listed in each section.
> **Guidance** paragraphs are strategy advice (opinion), not rules or fact. Bracket notes: **GC** cards count toward the Bracket 3 limit of three; see [EDH Standards → brackets](EDH%20Standards.md#power-bracket-assessment). Pick cards whose identity fits your commander.

## Contents
- [Ramp](#ramp)
- [Card advantage](#card-advantage)
- [Aristocrats](#aristocrats)
- [+1/+1 counters](#11-counters)
- [Spellslinger](#spellslinger)
- [Graveyard](#graveyard)
- [Tokens](#tokens)
- [Blink](#blink)
- [Lands / landfall](#lands--landfall)
- [Artifacts](#artifacts)
- [Enchantress](#enchantress)
- [Voltron (equipment & auras)](#voltron-equipment--auras)
- [Treasure](#treasure)
- [Method](#method)

## Ramp

**Guidance:** Plan: accelerate into the commander and big spells. Guidance: about 10 pieces; cheap rocks for colorless or artifact decks, land ramp for green.

### Ramp: Mana rocks (MV ≤ 2)

Pattern: `\{T\}: Add` · 65 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Sol Ring](cards/S/so.md#sol-ring) | C | 1 | 1 | $1.28 |  |
| [Arcane Signet](cards/A/arc.md#arcane-signet) | C | 2 | 3 | $0.34 |  |
| [Fellwar Stone](cards/F/fe.md#fellwar-stone) | C | 2 | 17 | $0.61 |  |
| [Thought Vessel](cards/T/tho.md#thought-vessel) | C | 2 | 21 | $2.27 |  |
| [Mind Stone](cards/M/min.md#mind-stone) | C | 2 | 32 | $0.22 |  |
| [Talisman of Dominance](cards/T/ta.md#talisman-of-dominance) | UB | 2 | 92 | $0.50 |  |
| [Talisman of Creativity](cards/T/ta.md#talisman-of-creativity) | UR | 2 | 125 | $0.49 |  |
| [Talisman of Indulgence](cards/T/ta.md#talisman-of-indulgence) | BR | 2 | 127 | $0.50 |  |
| [Talisman of Hierarchy](cards/T/ta.md#talisman-of-hierarchy) | WB | 2 | 135 | $0.40 |  |
| [Talisman of Progress](cards/T/ta.md#talisman-of-progress) | WU | 2 | 136 | $0.29 |  |

Budget options beyond the top 10 (≤ $1.00): [Talisman of Conviction](cards/T/ta.md#talisman-of-conviction) (WR, $0.35) · [Dimir Signet](cards/D/di.md#dimir-signet) (UB, $0.29) · [Rakdos Signet](cards/R/rak.md#rakdos-signet) (BR, $0.40) · [Izzet Signet](cards/I/iz.md#izzet-signet) (UR, $0.28)

### Ramp: Land ramp (puts lands onto the battlefield)

Pattern: `search your library for (up to (one|two) )?(a |an )?(basic land|land) cards?[^.]*put (it|them|those cards|one) onto the battlefield` · 120 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Cultivate](cards/C/cu.md#cultivate) | G | 3 | 20 | $0.39 |  |
| [Kodama's Reach](cards/K/ko.md#kodamas-reach) | G | 3 | 37 | $1.55 |  |
| [Sword of the Animist](cards/S/sw.md#sword-of-the-animist) | C | 2 | 234 | $2.70 |  |
| [Harrow](cards/H/ha.md#harrow) | G | 3 | 249 | $0.31 |  |
| [Entish Restoration](cards/E/en.md#entish-restoration) | G | 3 | 455 | $2.58 |  |
| [Burnished Hart](cards/B/bu.md#burnished-hart) | C | 3 | 505 | $0.13 |  |
| [Springbloom Druid](cards/S/spr.md#springbloom-druid) | G | 3 | 782 | $0.14 |  |
| [Kodama of the West Tree](cards/K/ko.md#kodama-of-the-west-tree) | G | 3 | 855 | $19.61 |  |
| [Shared Roots](cards/S/sha.md#shared-roots) | G | 2 | 1,006 | $0.38 |  |
| [Roiling Regrowth](cards/R/ro.md#roiling-regrowth) | G | 3 | 1,054 | $0.27 |  |

Budget options beyond the top 10 (≤ $1.00): [Migration Path](cards/M/mig.md#migration-path) (G, $0.29) · [Explosive Vegetation](cards/E/ex.md#explosive-vegetation) (G, $0.28) · [Topiary Stomper](cards/T/to.md#topiary-stomper) (G, $0.66) · [Wight of the Reliquary](cards/W/wi.md#wight-of-the-reliquary) (BG, $0.43)

### Ramp: Mana creatures (MV ≤ 2)

Pattern: `\{T\}: Add` · 168 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Birds of Paradise](cards/B/bi.md#birds-of-paradise) | G | 1 | 35 | $4.98 |  |
| [Llanowar Elves](cards/L/ll.md#llanowar-elves) | G | 1 | 56 | $0.25 |  |
| [Elvish Mystic](cards/E/el.md#elvish-mystic) | G | 1 | 102 | $0.42 |  |
| [Delighted Halfling](cards/D/del.md#delighted-halfling) | G | 1 | 148 | $24.33 |  |
| [Fyndhorn Elves](cards/F/fy.md#fyndhorn-elves) | G | 1 | 217 | $1.13 |  |
| [Ornithopter of Paradise](cards/O/or.md#ornithopter-of-paradise) | C | 2 | 220 | $0.34 |  |
| [Fanatic of Rhonas](cards/F/fa.md#fanatic-of-rhonas) | G | 2 | 404 | $12.38 |  |
| [Avacyn's Pilgrim](cards/A/av.md#avacyns-pilgrim) | WG | 1 | 501 | $0.28 |  |
| [Ignoble Hierarch](cards/I/ig.md#ignoble-hierarch) | BRG | 1 | 535 | $0.92 |  |
| [Incubation Druid](cards/I/inc.md#incubation-druid) | G | 2 | 642 | $0.78 |  |

Budget options beyond the top 10 (≤ $1.00): [Gyre Sage](cards/G/gy.md#gyre-sage) (G, $0.64) · [Iron Myr](cards/I/ir.md#iron-myr) (R, $0.75) · [Silver Myr](cards/S/si.md#silver-myr) (U, $0.24) · [Gold Myr](cards/G/gol.md#gold-myr) (W, $0.72)

### Ramp: Cost reducers

Pattern: `spells you cast cost \{\d\} less|cost \{\d\} less to cast` · 180 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Herald's Horn](cards/H/he.md#heralds-horn) | C | 3 | 151 | $2.87 |  |
| [Foundry Inspector](cards/F/fo.md#foundry-inspector) | C | 3 | 250 | $0.27 |  |
| [Jet Medallion](cards/J/je.md#jet-medallion) | C | 2 | 274 | $13.27 |  |
| [Ruby Medallion](cards/R/ru.md#ruby-medallion) | C | 2 | 293 | $14.04 |  |
| [Urza's Incubator](cards/U/ur.md#urzas-incubator) | C | 3 | 311 | $19.96 |  |
| [Sapphire Medallion](cards/S/sap.md#sapphire-medallion) | C | 2 | 354 | $8.11 |  |
| [Etherium Sculptor](cards/E/et.md#etherium-sculptor) | U | 2 | 415 | $0.39 |  |
| [Pearl Medallion](cards/P/pe.md#pearl-medallion) | C | 2 | 430 | $7.40 |  |
| [Emerald Medallion](cards/E/em.md#emerald-medallion) | C | 2 | 582 | $5.16 |  |
| [Cloud Key](cards/C/cl.md#cloud-key) | C | 3 | 606 | $1.52 |  |

Budget options beyond the top 10 (≤ $1.00): [Goblin Electromancer](cards/G/gob.md#goblin-electromancer) (UR, $0.23) · [Danitha Capashen, Paragon](cards/D/da.md#danitha-capashen-paragon) (W, $0.34) · [Stormcatch Mentor](cards/S/sto.md#stormcatch-mentor) (UR, $0.28) · [Nightscape Familiar](cards/N/ni.md#nightscape-familiar) (B, $0.42)

## Card advantage

**Guidance:** Plan: keep the hand full over a long multiplayer game. Guidance: about 10 sources, mostly repeatable engines.

### Card advantage: Repeatable draw engines (permanents)

Pattern: `(whenever|at the beginning of)[^.]*draw (a|one) card` · 728 Commander-legal matches · 1 Game Changer(s) in the top 10

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Rhystic Study](cards/R/rh.md#rhystic-study) | U | 3 | 46 | $67.12 | **GC** |
| [Esper Sentinel](cards/E/es.md#esper-sentinel) | W | 1 | 80 | $55.19 |  |
| [Garruk's Uprising](cards/G/ga.md#garruks-uprising) | G | 3 | 91 | $0.41 |  |
| [Mystic Remora](cards/M/my.md#mystic-remora) | U | 1 | 101 | $10.99 |  |
| [Phyrexian Arena](cards/P/ph.md#phyrexian-arena) | B | 3 | 104 | $2.51 |  |
| [Beast Whisperer](cards/B/be.md#beast-whisperer) | G | 4 | 213 | $4.91 |  |
| [The Great Henge](cards/T/theg.md#the-great-henge) | G | 9 | 228 | $62.23 |  |
| [Morbid Opportunist](cards/M/mor.md#morbid-opportunist) | B | 3 | 246 | $0.22 |  |
| [Archmage Emeritus](cards/A/arc.md#archmage-emeritus) | U | 4 | 253 | $0.64 |  |
| [Faerie Mastermind](cards/F/fa.md#faerie-mastermind) | U | 2 | 288 | $11.95 |  |

Budget options beyond the top 10 (≤ $1.00): [Psychosis Crawler](cards/P/ps.md#psychosis-crawler) (C, $0.68) · [Bident of Thassa](cards/B/bi.md#bident-of-thassa) (U, $0.43) · [Tatyova, Benthic Druid](cards/T/ta.md#tatyova-benthic-druid) (UG, $0.24) · [Curiosity](cards/C/cu.md#curiosity) (U, $0.71)

### Card advantage: Burst draw (instants & sorceries)

Pattern: `draw (two|three|four|five|seven|X) cards` · 294 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Brainstorm](cards/B/br.md#brainstorm) | U | 1 | 72 | $0.62 |  |
| [Frantic Search](cards/F/fr.md#frantic-search) | U | 3 | 98 | $0.67 |  |
| [Faithless Looting](cards/F/fa.md#faithless-looting) | R | 1 | 99 | $0.38 |  |
| [Deadly Dispute](cards/D/dea.md#deadly-dispute) | B | 2 | 131 | $0.29 |  |
| [Big Score](cards/B/bi.md#big-score) | R | 4 | 138 | $0.42 |  |
| [Night's Whisper](cards/N/ni.md#nights-whisper) | B | 2 | 180 | $0.22 |  |
| [Village Rites](cards/V/vi.md#village-rites) | B | 1 | 204 | $0.29 |  |
| [Thrill of Possibility](cards/T/thr.md#thrill-of-possibility) | R | 2 | 212 | $0.20 |  |
| [Unexpected Windfall](cards/U/un.md#unexpected-windfall) | R | 4 | 269 | $1.88 |  |
| [Harmonize](cards/H/ha.md#harmonize) | G | 4 | 327 | $0.19 |  |

Budget options beyond the top 10 (≤ $1.00): [Demand Answers](cards/D/dem.md#demand-answers) (R, $0.46) · [Read the Bones](cards/R/rea.md#read-the-bones) (B, $0.19) · [Corrupted Conviction](cards/C/cor.md#corrupted-conviction) (B, $0.36) · [Treasure Cruise](cards/T/tre.md#treasure-cruise) (U, $0.25)

### Card advantage: Impulse / exile-to-play

Pattern: `exile the top[^.]*\. (Until|You may) [^.]*(play|cast)` · 209 Commander-legal matches · 1 Game Changer(s) in the top 10

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Jeska's Will](cards/J/je.md#jeskas-will) | R | 3 | 107 | $39.74 | **GC** |
| [Professional Face-Breaker](cards/P/pr.md#professional-face-breaker) | R | 3 | 207 | $4.95 |  |
| [Ragavan, Nimble Pilferer](cards/R/rag.md#ragavan-nimble-pilferer) | R | 1 | 282 | $39.33 |  |
| [Birgi, God of Storytelling // Harnfel, Horn of Bounty](cards/B/bi.md#birgi-god-of-storytelling--harnfel-horn-of-bounty) | R | 3 | 498 | $25.35 |  |
| [Urza, Lord High Artificer](cards/U/ur.md#urza-lord-high-artificer) | U | 4 | 802 | $15.26 |  |
| [Light Up the Stage](cards/L/li.md#light-up-the-stage) | R | 3 | 1,240 | $0.29 |  |
| [Laelia, the Blade Reforged](cards/L/la.md#laelia-the-blade-reforged) | R | 3 | 1,347 | $0.28 |  |
| [Atsushi, the Blazing Sky](cards/A/at.md#atsushi-the-blazing-sky) | R | 4 | 1,364 | $0.28 |  |
| [Bonehoard Dracosaur](cards/B/bo.md#bonehoard-dracosaur) | R | 5 | 1,394 | $15.19 |  |
| [Chandra, Torch of Defiance](cards/C/cha.md#chandra-torch-of-defiance) | R | 4 | 1,480 | $1.94 |  |

Budget options beyond the top 10 (≤ $1.00): [Grenzo, Havoc Raiser](cards/G/gre.md#grenzo-havoc-raiser) (R, $0.30) · [Gix, Yawgmoth Praetor](cards/G/gi.md#gix-yawgmoth-praetor) (B, $0.68) · [Party Thrasher](cards/P/pa.md#party-thrasher) (R, $0.58) · [Reckless Impulse](cards/R/rec.md#reckless-impulse) (R, $0.87)

## Aristocrats

**Guidance:** Plan: make fodder, sacrifice it for value, and drain with death triggers. See [EDH Archetypes → Aristocrats](EDH%20Archetypes.md).

### Aristocrats: Free sacrifice outlets

Pattern: `(^|\. |\n)Sacrifice (a|another) creature: ` · 41 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Ashnod's Altar](cards/A/as.md#ashnods-altar) | C | 3 | 134 | $8.15 |  |
| [Viscera Seer](cards/V/vi.md#viscera-seer) | B | 1 | 257 | $0.51 |  |
| [Phyrexian Altar](cards/P/ph.md#phyrexian-altar) | C | 3 | 307 | $53.51 |  |
| [Goblin Bombardment](cards/G/gob.md#goblin-bombardment) | R | 2 | 463 | $2.96 |  |
| [Carrion Feeder](cards/C/car.md#carrion-feeder) | B | 1 | 609 | $1.67 |  |
| [Greater Good](cards/G/gre.md#greater-good) | G | 4 | 634 | $1.61 |  |
| [Altar of Dementia](cards/A/al.md#altar-of-dementia) | C | 2 | 641 | $15.98 |  |
| [Yahenni, Undying Partisan](cards/Y/ya.md#yahenni-undying-partisan) | B | 3 | 1,034 | $0.28 |  |
| [Woe Strider](cards/W/wo.md#woe-strider) | B | 3 | 1,676 | $0.28 |  |
| [Spawning Pit](cards/S/spa.md#spawning-pit) | C | 2 | 4,270 | $1.56 |  |

Budget options beyond the top 10 (≤ $1.00): [Fanatical Devotion](cards/F/fa.md#fanatical-devotion) (W, $0.51) · [Immersturm Predator](cards/I/im.md#immersturm-predator) (BR, $0.23) · [Bloodflow Connoisseur](cards/B/blo.md#bloodflow-connoisseur) (B, $0.10) · [Bloodthrone Vampire](cards/B/blo.md#bloodthrone-vampire) (B, $0.14)

### Aristocrats: Death-trigger drain payoffs

Pattern: `whenever (a|another) (nontoken )?creature (you control )?dies[^.]*(loses? \d+ life|each opponent loses)` · 16 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Bastion of Remembrance](cards/B/bas.md#bastion-of-remembrance) | B | 3 | 331 | $0.27 |  |
| [The Meathook Massacre](cards/T/them.md#the-meathook-massacre) | B | 2 | 516 | $24.18 |  |
| [Elas il-Kor, Sadistic Pilgrim](cards/E/el.md#elas-il-kor-sadistic-pilgrim) | WB | 2 | 617 | $0.72 |  |
| [Sephiroth, Fabled SOLDIER // Sephiroth, One-Winged Angel](cards/S/sep.md#sephiroth-fabled-soldier--sephiroth-one-winged-angel) | B | 3 | 1,242 | $27.94 |  |
| [Poison-Tip Archer](cards/P/po.md#poison-tip-archer) | BG | 4 | 1,674 | $0.59 |  |
| [Cauldron of Essence](cards/C/cau.md#cauldron-of-essence) | BG | 3 | 2,084 | $2.29 |  |
| [Funeral Room // Awakening Hall](cards/F/fu.md#funeral-room--awakening-hall) | B | 11 | 2,123 | $5.72 |  |
| [Vein Ripper](cards/V/ve.md#vein-ripper) | B | 6 | 2,767 | $6.29 |  |
| [Grave Venerations](cards/G/gra.md#grave-venerations) | B | 4 | 4,101 | $0.36 |  |
| [Dark Prophecy](cards/D/da.md#dark-prophecy) | B | 3 | 4,331 | $5.43 |  |

Budget options beyond the top 10 (≤ $1.00): [Dreadhound](cards/D/dre.md#dreadhound) (B, $0.17) · [Life Insurance](cards/L/li.md#life-insurance) (WB, $0.31) · [Agent Venom](cards/A/ag.md#agent-venom) (B, $0.36) · [Relic Vial](cards/R/rel.md#relic-vial) (C, $0.26)

### Aristocrats: Fodder makers (multiple creature tokens)

Pattern: `create (two|three|four|X|a number of) [^.]*creature tokens` · 555 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Voice of Victory](cards/V/vo.md#voice-of-victory) | W | 2 | 499 | $18.19 |  |
| [Chasm Skulker](cards/C/cha.md#chasm-skulker) | U | 3 | 704 | $0.31 |  |
| [Elspeth, Sun's Champion](cards/E/el.md#elspeth-suns-champion) | W | 6 | 786 | $0.38 |  |
| [Krenko, Tin Street Kingpin](cards/K/kr.md#krenko-tin-street-kingpin) | R | 3 | 916 | $2.95 |  |
| [Myr Battlesphere](cards/M/my.md#myr-battlesphere) | C | 7 | 927 | $0.25 |  |
| [Krenko, Mob Boss](cards/K/kr.md#krenko-mob-boss) | R | 4 | 1,088 | $2.19 |  |
| [Anim Pakal, Thousandth Moon](cards/A/an.md#anim-pakal-thousandth-moon) | WR | 3 | 1,107 | $4.13 |  |
| [Secure the Wastes](cards/S/sec.md#secure-the-wastes) | W | 1 | 1,196 | $0.30 |  |
| [Arachnogenesis](cards/A/ara.md#arachnogenesis) | G | 3 | 1,236 | $1.77 |  |
| [Grand Crescendo](cards/G/gra.md#grand-crescendo) | W | 2 | 1,251 | $0.75 |  |

Budget options beyond the top 10 (≤ $1.00): [Martial Coup](cards/M/mar.md#martial-coup) (W, $0.26) · [Grave Titan](cards/G/gra.md#grave-titan) (B, $0.25) · [Siege-Gang Commander](cards/S/si.md#siege-gang-commander) (R, $0.26) · [Hornet Queen](cards/H/ho.md#hornet-queen) (G, $0.23)

## +1/+1 counters

**Guidance:** Plan: grow the board with counters and multiply them.

### +1/+1 counters: Counter doublers

Pattern: `(twice that many|that many plus one) \+1/\+1 counters|twice that many counters|one or more counters would be put[^.]*that many plus` · 31 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Hardened Scales](cards/H/ha.md#hardened-scales) | G | 1 | 185 | $1.80 |  |
| [Branching Evolution](cards/B/br.md#branching-evolution) | G | 3 | 374 | $7.30 |  |
| [Kami of Whispered Hopes](cards/K/ka.md#kami-of-whispered-hopes) | G | 3 | 403 | $4.51 |  |
| [Ozolith, the Shattered Spire](cards/O/oz.md#ozolith-the-shattered-spire) | G | 2 | 644 | $6.61 |  |
| [The Earth Crystal](cards/T/thee.md#the-earth-crystal) | G | 4 | 681 | $12.82 |  |
| [Primal Vigor](cards/P/pr.md#primal-vigor) | G | 5 | 1,225 | $6.27 |  |
| [Corpsejack Menace](cards/C/cor.md#corpsejack-menace) | BG | 4 | 1,569 | $0.35 |  |
| [Winding Constrictor](cards/W/wi.md#winding-constrictor) | BG | 2 | 2,088 | $0.45 |  |
| [Mycoloth](cards/M/my.md#mycoloth) | G | 5 | 2,103 | $0.56 |  |
| [Conclave Mentor](cards/C/con.md#conclave-mentor) | WG | 2 | 2,378 | $0.35 |  |

Budget options beyond the top 10 (≤ $1.00): [Benevolent Hydra](cards/B/be.md#benevolent-hydra) (G, $0.76) · [Mauhúr, Uruk-hai Captain](cards/M/mau.md#mauhúr-uruk-hai-captain) (BR, $0.26) · [Mowu, Loyal Companion](cards/M/mow.md#mowu-loyal-companion) (G, $0.22) · [Galloping Lizrog](cards/G/ga.md#galloping-lizrog) (UG, $0.31)

### +1/+1 counters: Proliferate

Pattern: `\bproliferate\b` · 95 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Evolution Sage](cards/E/ev.md#evolution-sage) | G | 3 | 402 | $2.08 |  |
| [Cankerbloom](cards/C/can.md#cankerbloom) | G | 2 | 827 | $0.36 |  |
| [Thrummingbird](cards/T/thr.md#thrummingbird) | U | 2 | 830 | $0.25 |  |
| [Yawgmoth, Thran Physician](cards/Y/ya.md#yawgmoth-thran-physician) | B | 4 | 834 | $23.44 |  |
| [Ripples of Potential](cards/R/ri.md#ripples-of-potential) | U | 2 | 880 | $5.49 |  |
| [Tezzeret's Gambit](cards/T/te.md#tezzerets-gambit) | U | 4 | 947 | $0.19 |  |
| [Inexorable Tide](cards/I/ine.md#inexorable-tide) | U | 5 | 1,001 | $0.92 |  |
| [Tekuthal, Inquiry Dominus](cards/T/te.md#tekuthal-inquiry-dominus) | U | 4 | 1,183 | $1.92 |  |
| [Dreamtide Whale](cards/D/dre.md#dreamtide-whale) | U | 3 | 1,186 | $3.43 |  |
| [Flux Channeler](cards/F/fl.md#flux-channeler) | U | 3 | 1,250 | $2.65 |  |

Budget options beyond the top 10 (≤ $1.00): [Experimental Augury](cards/E/ex.md#experimental-augury) (U, $0.21) · [Contagion Clasp](cards/C/con.md#contagion-clasp) (C, $0.35) · [Metastatic Evangel](cards/M/me.md#metastatic-evangel) (W, $0.37) · [Grateful Apparition](cards/G/gra.md#grateful-apparition) (W, $0.18)

### +1/+1 counters: Counter payoffs

Pattern: `for each \+1/\+1 counter on|creatures? you control with (a|one or more) \+1/\+1 counters? on (it|them)` · 97 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Inspiring Call](cards/I/ins.md#inspiring-call) | G | 3 | 280 | $0.27 |  |
| [Gyre Sage](cards/G/gy.md#gyre-sage) | G | 2 | 847 | $0.64 |  |
| [Abzan Falconer](cards/A/ab.md#abzan-falconer) | W | 3 | 1,400 | $0.26 |  |
| [Duskshell Crawler](cards/D/du.md#duskshell-crawler) | G | 2 | 1,408 | $0.29 |  |
| [Hangarback Walker](cards/H/ha.md#hangarback-walker) | C | 0 | 1,516 | $0.27 |  |
| [Lion Sash](cards/L/li.md#lion-sash) | W | 2 | 1,810 | $2.08 |  |
| [Mycoloth](cards/M/my.md#mycoloth) | G | 5 | 2,103 | $0.56 |  |
| [Animar, Soul of Elements](cards/A/an.md#animar-soul-of-elements) | URG | 3 | 2,380 | $18.90 |  |
| [Bred for the Hunt](cards/B/br.md#bred-for-the-hunt) | UG | 3 | 2,676 | $0.23 |  |
| [Uncivil Unrest](cards/U/un.md#uncivil-unrest) | R | 5 | 3,000 | $18.79 |  |

Budget options beyond the top 10 (≤ $1.00): [Herald of War](cards/H/he.md#herald-of-war) (W, $0.78) · [Hooded Hydra](cards/H/ho.md#hooded-hydra) (G, $0.72) · [Nyxborn Hydra](cards/N/ny.md#nyxborn-hydra) (G, $0.30) · [Hamza, Guardian of Arashin](cards/H/ha.md#hamza-guardian-of-arashin) (WG, $0.30)

## Spellslinger

**Guidance:** Plan: chain cheap instants and sorceries and win through cast triggers.

### Spellslinger: Instant/sorcery cost reducers

Pattern: `instant and sorcery spells you cast cost \{1\} less|instant or sorcery spells you cast cost` · 20 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Goblin Electromancer](cards/G/gob.md#goblin-electromancer) | UR | 2 | 671 | $0.23 |  |
| [Archmage of Runes](cards/A/arc.md#archmage-of-runes) | U | 5 | 928 | $3.64 |  |
| [Stormcatch Mentor](cards/S/sto.md#stormcatch-mentor) | UR | 2 | 948 | $0.28 |  |
| [Baral, Chief of Compliance](cards/B/bar.md#baral-chief-of-compliance) | U | 2 | 1,344 | $3.93 |  |
| [Primal Amulet // Primal Wellspring](cards/P/pr.md#primal-amulet--primal-wellspring) | C | 4 | 2,171 | $11.25 |  |
| [Thunderclap Drake](cards/T/thu.md#thunderclap-drake) | U | 2 | 2,175 | $0.51 |  |
| [Haughty Djinn](cards/H/ha.md#haughty-djinn) | U | 3 | 2,546 | $0.29 |  |
| [Case of the Ransacked Lab](cards/C/cas.md#case-of-the-ransacked-lab) | U | 3 | 2,833 | $0.62 |  |
| [Mocking Sprite](cards/M/moc.md#mocking-sprite) | U | 3 | 2,894 | $0.20 |  |
| [Mindsplice Apparatus](cards/M/min.md#mindsplice-apparatus) | U | 4 | 2,999 | $1.10 |  |

Budget options beyond the top 10 (≤ $1.00): [Jace's Sanctum](cards/J/ja.md#jaces-sanctum) (U, $0.58) · [Mizzix of the Izmagnus](cards/M/miz.md#mizzix-of-the-izmagnus) (UR, $0.83) · [Dirgur Focusmage // Braingeyser](cards/D/di.md#dirgur-focusmage--braingeyser) (U, $0.27) · [Curious Homunculus // Voracious Reader](cards/C/cu.md#curious-homunculus--voracious-reader) (U, $0.31)

### Spellslinger: Spell copiers

Pattern: `copy (target|that) (instant or sorcery|instant|sorcery) spell` · 34 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Return the Favor](cards/R/ret.md#return-the-favor) | R | 2 | 572 | $0.64 |  |
| [Dualcaster Mage](cards/D/du.md#dualcaster-mage) | R | 3 | 682 | $3.69 |  |
| [Narset's Reversal](cards/N/na.md#narsets-reversal) | U | 2 | 716 | $2.14 |  |
| [Flare of Duplication](cards/F/fl.md#flare-of-duplication) | R | 3 | 1,136 | $2.41 |  |
| [Reverberate](cards/R/rev.md#reverberate) | R | 2 | 1,425 | $2.92 |  |
| [Twinning Staff](cards/T/tw.md#twinning-staff) | C | 3 | 1,703 | $13.89 |  |
| [Lithoform Engine](cards/L/li.md#lithoform-engine) | C | 4 | 1,759 | $5.73 |  |
| [Kitsa, Otterball Elite](cards/K/ki.md#kitsa-otterball-elite) | U | 2 | 2,181 | $4.38 |  |
| [Reiterate](cards/R/rei.md#reiterate) | R | 3 | 2,557 | $18.13 |  |
| [Increasing Vengeance](cards/I/inc.md#increasing-vengeance) | R | 2 | 3,076 | $0.86 |  |

Budget options beyond the top 10 (≤ $1.00): [Expansion // Explosion](cards/E/ex.md#expansion--explosion) (UR, $0.19) · [Naru Meha, Master Wizard](cards/N/na.md#naru-meha-master-wizard) (U, $0.96) · [Gandalf the Grey](cards/G/ga.md#gandalf-the-grey) (UR, $0.37) · [Insidious Will](cards/I/ins.md#insidious-will) (U, $0.46)

### Spellslinger: Cast-trigger payoffs

Pattern: `whenever you cast (an|a) (instant or sorcery|instant|sorcery|noncreature) spell|\bmagecraft\b` · 396 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Storm-Kiln Artist](cards/S/sto.md#storm-kiln-artist) | R | 4 | 196 | $1.81 |  |
| [Archmage Emeritus](cards/A/arc.md#archmage-emeritus) | U | 4 | 253 | $0.64 |  |
| [Guttersnipe](cards/G/gu.md#guttersnipe) | R | 3 | 408 | $0.23 |  |
| [Pinnacle Monk // Mystic Peak](cards/P/pi.md#pinnacle-monk--mystic-peak) | R | 5 | 531 | $2.10 |  |
| [Displacer Kitten](cards/D/di.md#displacer-kitten) | U | 4 | 549 | $28.22 |  |
| [Harmonic Prodigy](cards/H/ha.md#harmonic-prodigy) | R | 2 | 640 | $5.02 |  |
| [Veyran, Voice of Duality](cards/V/ve.md#veyran-voice-of-duality) | UR | 3 | 745 | $1.83 |  |
| [Valley Floodcaller](cards/V/va.md#valley-floodcaller) | U | 3 | 761 | $3.77 |  |
| [Talrand, Sky Summoner](cards/T/ta.md#talrand-sky-summoner) | U | 4 | 804 | $0.41 |  |
| [Coruscation Mage](cards/C/cor.md#coruscation-mage) | R | 2 | 805 | $2.16 |  |

Budget options beyond the top 10 (≤ $1.00): [Young Pyromancer](cards/Y/yo.md#young-pyromancer) (R, $0.24) · [Stormcatch Mentor](cards/S/sto.md#stormcatch-mentor) (UR, $0.28) · [Firebrand Archer](cards/F/fi.md#firebrand-archer) (R, $0.25) · [Fiery Inscription](cards/F/fi.md#fiery-inscription) (R, $0.46)

## Graveyard

**Guidance:** Plan: fill the graveyard, then reanimate or recur. ⚠️ Graveyard hate punishes it; see [EDH Interaction](EDH%20Interaction.md#graveyard-hate).

### Graveyard: Self-mill

Pattern: `\bmill (two|three|four|five|X|\w+) cards\b|you mill` · 260 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Ripples of Undeath](cards/R/ri.md#ripples-of-undeath) | B | 2 | 534 | $8.12 |  |
| [Six](cards/S/si.md#six) | G | 3 | 590 | $5.09 |  |
| [Emry, Lurker of the Loch](cards/E/em.md#emry-lurker-of-the-loch) | U | 3 | 604 | $0.66 |  |
| [Stitcher's Supplier](cards/S/sti.md#stitchers-supplier) | B | 1 | 618 | $0.27 |  |
| [Aftermath Analyst](cards/A/af.md#aftermath-analyst) | G | 2 | 630 | $0.88 |  |
| [Life from the Loam](cards/L/li.md#life-from-the-loam) | G | 2 | 713 | $4.95 |  |
| [Combustible Gearhulk](cards/C/com.md#combustible-gearhulk) | R | 6 | 1,033 | $0.25 |  |
| [Lumra, Bellow of the Woods](cards/L/lu.md#lumra-bellow-of-the-woods) | G | 6 | 1,128 | $27.17 |  |
| [Hedge Shredder](cards/H/he.md#hedge-shredder) | G | 4 | 1,277 | $2.49 |  |
| [Palantír of Orthanc](cards/P/pa.md#palantír-of-orthanc) | C | 3 | 1,339 | $18.11 |  |

Budget options beyond the top 10 (≤ $1.00): [Skull Prophet](cards/S/sk.md#skull-prophet) (BG, $0.64) · [Nyx Weaver](cards/N/ny.md#nyx-weaver) (BG, $0.23) · [Perpetual Timepiece](cards/P/pe.md#perpetual-timepiece) (C, $0.30) · [Liliana, Death's Majesty](cards/L/li.md#liliana-deaths-majesty) (B, $0.36)

### Graveyard: Reanimation

Pattern: `(return|put) target creature card from (a|your) graveyard (on)?to the battlefield` · 125 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Reanimate](cards/R/rea.md#reanimate) | B | 1 | 53 | $6.34 |  |
| [Dread Return](cards/D/dre.md#dread-return) | B | 4 | 539 | $0.51 |  |
| [Whip of Erebos](cards/W/wh.md#whip-of-erebos) | B | 4 | 714 | $8.97 |  |
| [Sheoldred, Whispering One](cards/S/she.md#sheoldred-whispering-one) | B | 7 | 723 | $18.68 |  |
| [The Soul Stone](cards/T/thes.md#the-soul-stone) | B | 2 | 866 | $85.20 |  |
| [Karmic Guide](cards/K/ka.md#karmic-guide) | W | 5 | 979 | $0.36 |  |
| [Necromancy](cards/N/ne.md#necromancy) | B | 3 | 1,032 | $19.31 |  |
| [Portal to Phyrexia](cards/P/po.md#portal-to-phyrexia) | C | 9 | 1,071 | $50.11 |  |
| [Artisan of Kozilek](cards/A/art.md#artisan-of-kozilek) | C | 9 | 1,207 | $0.43 |  |
| [Cleric Class](cards/C/cl.md#cleric-class) | W | 1 | 1,416 | $0.94 |  |

Budget options beyond the top 10 (≤ $1.00): [Liliana, Death's Majesty](cards/L/li.md#liliana-deaths-majesty) (B, $0.36) · [Priest of Fell Rites](cards/P/pr.md#priest-of-fell-rites) (WB, $0.25) · [Vat of Rebirth](cards/V/va.md#vat-of-rebirth) (B, $0.32) · [Kenrith, the Returned King](cards/K/ke.md#kenrith-the-returned-king) (WUBRG, $0.51)

### Graveyard: Recursion to hand

Pattern: `return (target|up to \w+ target) [a-z ]*cards? from your graveyard to your hand` · 332 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Eternal Witness](cards/E/et.md#eternal-witness) | G | 3 | 121 | $1.10 |  |
| [Bala Ged Recovery // Bala Ged Sanctuary](cards/B/bal.md#bala-ged-recovery--bala-ged-sanctuary) | G | 3 | 318 | $6.80 |  |
| [Pinnacle Monk // Mystic Peak](cards/P/pi.md#pinnacle-monk--mystic-peak) | R | 5 | 531 | $2.10 |  |
| [Life from the Loam](cards/L/li.md#life-from-the-loam) | G | 2 | 713 | $4.95 |  |
| [Evolution Witness](cards/E/ev.md#evolution-witness) | G | 3 | 943 | $0.26 |  |
| [Phyrexian Reclamation](cards/P/ph.md#phyrexian-reclamation) | B | 1 | 960 | $2.94 |  |
| [Archaeomancer](cards/A/arc.md#archaeomancer) | U | 4 | 974 | $0.31 |  |
| [Timeless Witness](cards/T/ti.md#timeless-witness) | G | 4 | 1,323 | $0.33 |  |
| [Regrowth](cards/R/reg.md#regrowth) | G | 2 | 1,393 | $0.48 |  |
| [Unnatural Restoration](cards/U/un.md#unnatural-restoration) | G | 2 | 1,530 | $1.35 |  |

Budget options beyond the top 10 (≤ $1.00): [Stitch Together](cards/S/sti.md#stitch-together) (B, $0.30) · [Oversold Cemetery](cards/O/ov.md#oversold-cemetery) (B, $0.48) · [Nyx Weaver](cards/N/ny.md#nyx-weaver) (BG, $0.23) · [Honest Rutstein](cards/H/ho.md#honest-rutstein) (BG, $0.33)

## Tokens

**Guidance:** Plan: go wide, then pump or convert the tokens.

### Tokens: Token doublers

Pattern: `twice that many (of those )?tokens|create (twice|double) that many` · 11 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Doubling Season](cards/D/do.md#doubling-season) | G | 5 | 189 | $29.95 |  |
| [Anointed Procession](cards/A/an.md#anointed-procession) | W | 4 | 364 | $54.51 |  |
| [Parallel Lives](cards/P/pa.md#parallel-lives) | G | 4 | 405 | $27.71 |  |
| [Mondrak, Glory Dominus](cards/M/mon.md#mondrak-glory-dominus) | W | 4 | 431 | $44.65 |  |
| [Elspeth, Storm Slayer](cards/E/el.md#elspeth-storm-slayer) | W | 5 | 663 | $42.66 |  |
| [Primal Vigor](cards/P/pr.md#primal-vigor) | G | 5 | 1,225 | $6.27 |  |
| [Exalted Sunborn](cards/E/ex.md#exalted-sunborn) | W | 5 | 1,308 | $18.24 |  |
| [Adrix and Nev, Twincasters](cards/A/ad.md#adrix-and-nev-twincasters) | UG | 4 | 1,409 | $7.77 |  |
| [Kaya, Geist Hunter](cards/K/ka.md#kaya-geist-hunter) | WB | 3 | 4,513 | $0.36 |  |
| [Bard, King of Dale](cards/B/bar.md#bard-king-of-dale) | WU | 6 | 7,293 | $3.37 |  |

### Tokens: Anthems

Pattern: `creatures you control get \+\d+/\+\d+` · 223 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Beastmaster Ascension](cards/B/be.md#beastmaster-ascension) | G | 3 | 568 | $4.41 |  |
| [Mirari's Wake](cards/M/mir.md#miraris-wake) | WG | 5 | 712 | $3.09 |  |
| [Rising of the Day](cards/R/ri.md#rising-of-the-day) | R | 3 | 733 | $0.56 |  |
| [Elspeth, Sun's Champion](cards/E/el.md#elspeth-suns-champion) | W | 6 | 786 | $0.38 |  |
| [Flowering of the White Tree](cards/F/fl.md#flowering-of-the-white-tree) | W | 2 | 811 | $8.80 |  |
| [Elesh Norn, Grand Cenobite](cards/E/el.md#elesh-norn-grand-cenobite) | W | 7 | 857 | $15.64 |  |
| [Forsaken Monument](cards/F/fo.md#forsaken-monument) | C | 5 | 882 | $3.43 |  |
| [Elvish Archdruid](cards/E/el.md#elvish-archdruid) | G | 3 | 883 | $0.48 |  |
| [Warleader's Call](cards/W/war.md#warleaders-call) | WR | 3 | 913 | $4.08 |  |
| [Bastion Protector](cards/B/bas.md#bastion-protector) | W | 3 | 935 | $0.29 |  |

Budget options beyond the top 10 (≤ $1.00): [Thunderfoot Baloth](cards/T/thu.md#thunderfoot-baloth) (G, $0.40) · [Cemetery Reaper](cards/C/ce.md#cemetery-reaper) (B, $0.21) · [Master of Etherium](cards/M/mas.md#master-of-etherium) (U, $0.25) · [It That Heralds the End](cards/I/it.md#it-that-heralds-the-end) (C, $0.34)

### Tokens: Mass pump finishers

Pattern: `creatures you control get \+X/\+X|creatures you control get \+\d+/\+\d+ and gain trample until end of turn` · 10 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Finale of Devastation](cards/F/fi.md#finale-of-devastation) | G | 2 | 301 | $32.52 |  |
| [Overrun](cards/O/ov.md#overrun) | G | 5 | 1,710 | $0.19 |  |
| [Esper Origins // Summon: Esper Maduin](cards/E/es.md#esper-origins--summon-esper-maduin) | G | 2 | 5,150 | $1.67 |  |
| [Become the Avalanche](cards/B/be.md#become-the-avalanche) | G | 6 | 6,103 | $0.31 |  |
| [Lorehold Charm](cards/L/lo.md#lorehold-charm) | WR | 2 | 6,336 | $0.20 |  |
| [Cabaretti Charm](cards/C/cab.md#cabaretti-charm) | WRG | 3 | 7,835 | $0.17 |  |
| [Overcome](cards/O/ov.md#overcome) | G | 5 | 12,481 | $0.07 |  |
| [Klothys's Design](cards/K/kl.md#klothyss-design) | G | 6 | 18,464 | $0.19 |  |
| [Hustle // Bustle](cards/H/hu.md#hustle--bustle) | URG | 7 | 28,225 | $0.09 |  |
| [Kjeldoran War Cry](cards/K/kj.md#kjeldoran-war-cry) | W | 2 | 32,118 | $0.07 |  |

## Blink

**Guidance:** Plan: re-use enters-the-battlefield triggers. Rules: [ETB/LTB](Rules%20Interactions.md#etb--ltb--look-back-triggers).

### Blink: Blink effects

Pattern: `exile (up to one )?(another )?target (nontoken )?(creature|permanent|nonland permanent|artifact or creature)[^.]*(you control|you own)?[^.]*\. (Return|Then return) (it|that card|those cards|the exiled card)` · 27 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Charming Prince](cards/C/cha.md#charming-prince) | W | 2 | 1,775 | $0.39 |  |
| [The Eternal Wanderer](cards/T/thee.md#the-eternal-wanderer) | W | 6 | 1,801 | $1.26 |  |
| [Touch the Spirit Realm](cards/T/to.md#touch-the-spirit-realm) | W | 3 | 1,867 | $0.62 |  |
| [Flickerwisp](cards/F/fl.md#flickerwisp) | W | 3 | 2,207 | $0.22 |  |
| [Teferi's Time Twist](cards/T/te.md#teferis-time-twist) | U | 2 | 2,687 | $0.32 |  |
| [Oath of Teferi](cards/O/oa.md#oath-of-teferi) | WU | 5 | 2,700 | $6.99 |  |
| [Kykar, Zephyr Awakener](cards/K/ky.md#kykar-zephyr-awakener) | WU | 4 | 4,189 | $0.30 |  |
| [Abuelo, Ancestral Echo](cards/A/ab.md#abuelo-ancestral-echo) | WU | 3 | 5,903 | $0.28 |  |
| [Getaway Glamer](cards/G/ge.md#getaway-glamer) | W | 1 | 6,036 | $0.31 |  |
| [Venser, the Sojourner](cards/V/ve.md#venser-the-sojourner) | WU | 5 | 6,384 | $4.55 |  |

Budget options beyond the top 10 (≤ $1.00): [Salvation Swan](cards/S/sal.md#salvation-swan) (W, $0.30) · [Voyager Staff](cards/V/vo.md#voyager-staff) (C, $0.29) · [Twining Twins // Swift Spiral](cards/T/tw.md#twining-twins--swift-spiral) (WU, $0.23) · [Turn to Mist](cards/T/tu.md#turn-to-mist) (WU, $0.16)

### Blink: ETB doublers

Pattern: `(entering|enters)[^.]*causes? a triggered ability[^.]*triggers? an additional time` · 9 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Panharmonicon](cards/P/pa.md#panharmonicon) | C | 4 | 271 | $4.43 |  |
| [Ancient Greenwarden](cards/A/an.md#ancient-greenwarden) | G | 6 | 700 | $12.33 |  |
| [Elesh Norn, Mother of Machines](cards/E/el.md#elesh-norn-mother-of-machines) | W | 5 | 1,046 | $22.73 |  |
| [Starfield Vocalist](cards/S/sta.md#starfield-vocalist) | U | 4 | 1,834 | $1.38 |  |
| [Traveling Chocobo](cards/T/tra.md#traveling-chocobo) | G | 3 | 1,874 | $17.49 |  |
| [Virtue of Knowledge // Vantress Visions](cards/V/vi.md#virtue-of-knowledge--vantress-visions) | U | 5 | 2,275 | $5.41 |  |
| [Yarok, the Desecrated](cards/Y/ya.md#yarok-the-desecrated) | UBG | 5 | 2,459 | $0.28 |  |
| [Gandalf the White](cards/G/ga.md#gandalf-the-white) | W | 5 | 2,692 | $8.84 |  |
| [Naban, Dean of Iteration](cards/N/na.md#naban-dean-of-iteration) | U | 2 | 6,024 | $0.29 |  |

## Lands / landfall

**Guidance:** Plan: extra land drops plus landfall payoffs.

### Lands / landfall: Extra land drops

Pattern: `play an additional land|play two additional lands` · 36 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Explore](cards/E/ex.md#explore) | G | 2 | 237 | $0.18 |  |
| [Exploration](cards/E/ex.md#exploration) | G | 1 | 305 | $29.14 |  |
| [Dryad of the Ilysian Grove](cards/D/dry.md#dryad-of-the-ilysian-grove) | G | 3 | 312 | $9.42 |  |
| [Azusa, Lost but Seeking](cards/A/az.md#azusa-lost-but-seeking) | G | 3 | 330 | $11.18 |  |
| [Oracle of Mul Daya](cards/O/or.md#oracle-of-mul-daya) | G | 4 | 509 | $2.40 |  |
| [Icetill Explorer](cards/I/ic.md#icetill-explorer) | G | 4 | 611 | $21.00 |  |
| [Aesi, Tyrant of Gyre Strait](cards/A/ae.md#aesi-tyrant-of-gyre-strait) | UG | 6 | 848 | $11.24 |  |
| [Loot, Exuberant Explorer](cards/L/lo.md#loot-exuberant-explorer) | G | 3 | 871 | $1.00 |  |
| [The Gitrog Monster](cards/T/theg.md#the-gitrog-monster) | BG | 5 | 911 | $0.42 |  |
| [Wayward Swordtooth](cards/W/way.md#wayward-swordtooth) | G | 3 | 1,062 | $3.74 |  |

Budget options beyond the top 10 (≤ $1.00): [Rites of Flourishing](cards/R/ri.md#rites-of-flourishing) (G, $0.54) · [Escape to the Wilds](cards/E/es.md#escape-to-the-wilds) (RG, $0.29) · [Urban Evolution](cards/U/ur.md#urban-evolution) (UG, $0.12) · [Ghirapur Orrery](cards/G/gh.md#ghirapur-orrery) (C, $0.39)

### Lands / landfall: Landfall payoffs

Pattern: `\blandfall\b|whenever a land (you control )?enters` · 207 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Tireless Provisioner](cards/T/ti.md#tireless-provisioner) | G | 3 | 187 | $2.37 |  |
| [Scute Swarm](cards/S/sc.md#scute-swarm) | G | 3 | 240 | $8.37 |  |
| [Avenger of Zendikar](cards/A/av.md#avenger-of-zendikar) | G | 7 | 299 | $0.45 |  |
| [Lotus Cobra](cards/L/lo.md#lotus-cobra) | G | 2 | 329 | $6.08 |  |
| [Rampaging Baloths](cards/R/ram.md#rampaging-baloths) | G | 6 | 386 | $0.29 |  |
| [Evolution Sage](cards/E/ev.md#evolution-sage) | G | 3 | 402 | $2.08 |  |
| [Tatyova, Benthic Druid](cards/T/ta.md#tatyova-benthic-druid) | UG | 5 | 481 | $0.24 |  |
| [Felidar Retreat](cards/F/fe.md#felidar-retreat) | W | 4 | 519 | $1.11 |  |
| [Icetill Explorer](cards/I/ic.md#icetill-explorer) | G | 4 | 611 | $21.00 |  |
| [Tireless Tracker](cards/T/ti.md#tireless-tracker) | G | 3 | 666 | $0.24 |  |

Budget options beyond the top 10 (≤ $1.00): [Omnath, Locus of Rage](cards/O/om.md#omnath-locus-of-rage) (RG, $0.34) · [Bloodghast](cards/B/blo.md#bloodghast) (B, $0.95) · [Retreat to Coralhelm](cards/R/ret.md#retreat-to-coralhelm) (U, $0.41) · [Emeria Angel](cards/E/em.md#emeria-angel) (W, $0.26)

### Lands / landfall: Lands from graveyard

Pattern: `play lands from your graveyard|return (target|all) land cards? from your graveyard` · 34 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Ramunap Excavator](cards/R/ram.md#ramunap-excavator) | G | 3 | 491 | $4.39 |  |
| [Conduit of Worlds](cards/C/con.md#conduit-of-worlds) | G | 4 | 567 | $1.21 |  |
| [Crucible of Worlds](cards/C/cr.md#crucible-of-worlds) | C | 3 | 599 | $27.97 |  |
| [Icetill Explorer](cards/I/ic.md#icetill-explorer) | G | 4 | 611 | $21.00 |  |
| [Aftermath Analyst](cards/A/af.md#aftermath-analyst) | G | 2 | 630 | $0.88 |  |
| [Ancient Greenwarden](cards/A/an.md#ancient-greenwarden) | G | 6 | 700 | $12.33 |  |
| [Splendid Reclamation](cards/S/spl.md#splendid-reclamation) | G | 4 | 877 | $0.37 |  |
| [Lumra, Bellow of the Woods](cards/L/lu.md#lumra-bellow-of-the-woods) | G | 6 | 1,128 | $27.17 |  |
| [Titania, Protector of Argoth](cards/T/ti.md#titania-protector-of-argoth) | G | 5 | 1,171 | $0.32 |  |
| [World Shaper](cards/W/wo.md#world-shaper) | G | 4 | 1,524 | $5.51 |  |

Budget options beyond the top 10 (≤ $1.00): [The Mending of Dominaria](cards/T/them.md#the-mending-of-dominaria) (G, $0.32) · [Szarel, Genesis Shepherd](cards/S/sz.md#szarel-genesis-shepherd) (BRG, $0.53) · [Perennial Behemoth](cards/P/pe.md#perennial-behemoth) (G, $0.48) · [Glacierwood Siege](cards/G/gl.md#glacierwood-siege) (UG, $0.33)

## Artifacts

**Guidance:** Plan: artifact density with cast or enter payoffs.

### Artifacts: Artifact payoffs

Pattern: `whenever (an|another|one or more) (nontoken )?artifacts? (you control )?(enters|is put into a graveyard)|whenever you cast an artifact spell` · 89 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Reckless Fireweaver](cards/R/rec.md#reckless-fireweaver) | R | 2 | 668 | $0.41 |  |
| [Sai, Master Thopterist](cards/S/sai.md#sai-master-thopterist) | U | 3 | 814 | $0.31 |  |
| [Tezzeret, Cruel Captain](cards/T/te.md#tezzeret-cruel-captain) | C | 3 | 1,174 | $19.47 |  |
| [Forensic Gadgeteer](cards/F/fo.md#forensic-gadgeteer) | U | 3 | 1,405 | $2.01 |  |
| [Marionette Master](cards/M/mar.md#marionette-master) | B | 6 | 1,586 | $1.63 |  |
| [Uthros Research Craft](cards/U/ut.md#uthros-research-craft) | U | 3 | 1,705 | $1.83 |  |
| [Grinding Station](cards/G/gri.md#grinding-station) | C | 2 | 2,173 | $11.57 |  |
| [Mirrodin Besieged](cards/M/mir.md#mirrodin-besieged) | U | 3 | 2,473 | $3.76 |  |
| [Disciple of the Vault](cards/D/di.md#disciple-of-the-vault) | B | 1 | 2,500 | $0.90 |  |
| [Efficient Construction](cards/E/ef.md#efficient-construction) | U | 4 | 2,611 | $0.46 |  |

Budget options beyond the top 10 (≤ $1.00): [Surge Conductor](cards/S/sur.md#surge-conductor) (C, $0.31) · [Mendicant Core, Guidelight](cards/M/me.md#mendicant-core-guidelight) (WU, $0.59) · [Golbez, Crystal Collector](cards/G/gol.md#golbez-crystal-collector) (UB, $0.35) · [Sarinth Steelseeker](cards/S/sar.md#sarinth-steelseeker) (G, $0.23)

### Artifacts: Artifact cost reducers

Pattern: `artifact spells you cast cost` · 6 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Foundry Inspector](cards/F/fo.md#foundry-inspector) | C | 3 | 250 | $0.27 |  |
| [Etherium Sculptor](cards/E/et.md#etherium-sculptor) | U | 2 | 415 | $0.39 |  |
| [Enthusiastic Mechanaut](cards/E/en.md#enthusiastic-mechanaut) | UR | 2 | 1,367 | $0.25 |  |
| [Voyager Quickwelder](cards/V/vo.md#voyager-quickwelder) | W | 3 | 2,592 | $0.31 |  |
| [Shuri, Wakandan Inventor](cards/S/shu.md#shuri-wakandan-inventor) | U | 2 | 5,752 | $0.34 |  |
| [Saheeli, Filigree Master](cards/S/sah.md#saheeli-filigree-master) | UR | 4 | 9,636 | $0.90 |  |

## Enchantress

**Guidance:** Plan: enchantment density plus draw-on-cast or draw-on-enter.

### Enchantress: Enchantress draw

Pattern: `whenever you cast an enchantment spell, draw|whenever an enchantment (you control )?enters[^.]*draw` · 6 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Enchantress's Presence](cards/E/en.md#enchantresss-presence) | G | 3 | 1,030 | $1.04 |  |
| [Setessan Champion](cards/S/set.md#setessan-champion) | G | 3 | 1,055 | $3.63 |  |
| [Entity Tracker](cards/E/en.md#entity-tracker) | U | 3 | 2,217 | $0.30 |  |
| [Satyr Enchanter](cards/S/sat.md#satyr-enchanter) | WG | 3 | 2,301 | $0.82 |  |
| [Argothian Enchantress](cards/A/arg.md#argothian-enchantress) | G | 2 | 3,814 | $64.51 |  |
| [Shoal Kraken](cards/S/sho.md#shoal-kraken) | U | 5 | 22,832 | $0.11 |  |

## Voltron (equipment & auras)

**Guidance:** Plan: suit up one creature, often the commander (21 commander damage; [rules](Rules%20Interactions.md#commander-damage)).

### Voltron (equipment & auras): Protective equipment/auras

Pattern: `(equipped|enchanted) creature (gets [^.]*and )?(has|gains) (hexproof|shroud|indestructible|protection|ward)` · 87 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Swiftfoot Boots](cards/S/sw.md#swiftfoot-boots) | C | 2 | 12 | $1.76 |  |
| [Mithril Coat](cards/M/mit.md#mithril-coat) | C | 3 | 238 | $24.71 |  |
| [Commander's Plate](cards/C/com.md#commanders-plate) | C | 1 | 475 | $30.85 |  |
| [Sword of Feast and Famine](cards/S/sw.md#sword-of-feast-and-famine) | C | 3 | 545 | $36.71 |  |
| [Brotherhood Regalia](cards/B/br.md#brotherhood-regalia) | C | 2 | 563 | $9.77 |  |
| [Hammer of Nazahn](cards/H/ha.md#hammer-of-nazahn) | C | 4 | 722 | $4.11 |  |
| [Sword of Hearth and Home](cards/S/sw.md#sword-of-hearth-and-home) | C | 3 | 910 | $13.30 |  |
| [Darksteel Plate](cards/D/da.md#darksteel-plate) | C | 3 | 912 | $3.18 |  |
| [Sword of Fire and Ice](cards/S/sw.md#sword-of-fire-and-ice) | C | 3 | 1,340 | $17.41 |  |
| [Caduceus, Staff of Hermes](cards/C/cad.md#caduceus-staff-of-hermes) | W | 3 | 1,439 | $7.63 |  |

Budget options beyond the top 10 (≤ $1.00): [Thran Power Suit](cards/T/thr.md#thran-power-suit) (C, $0.95) · [Spirit Mantle](cards/S/spi.md#spirit-mantle) (W, $0.30) · [Royal Treatment](cards/R/ro.md#royal-treatment) (G, $0.31) · [Shielded by Faith](cards/S/shi.md#shielded-by-faith) (W, $0.41)

### Voltron (equipment & auras): Evasion & double strike

Pattern: `(equipped|enchanted) creature (gets [^.]*and )?(has|gains) (double strike|flying|trample|shadow)|can't be blocked` · 261 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Shadowspear](cards/S/sha.md#shadowspear) | C | 1 | 306 | $20.91 |  |
| [Whispersilk Cloak](cards/W/wh.md#whispersilk-cloak) | C | 3 | 333 | $2.20 |  |
| [The Reaver Cleaver](cards/T/ther.md#the-reaver-cleaver) | R | 3 | 530 | $24.48 |  |
| [Brotherhood Regalia](cards/B/br.md#brotherhood-regalia) | C | 2 | 563 | $9.77 |  |
| [Trailblazer's Boots](cards/T/tra.md#trailblazers-boots) | C | 2 | 656 | $1.03 |  |
| [Aqueous Form](cards/A/aq.md#aqueous-form) | U | 1 | 758 | $0.29 |  |
| [Rancor](cards/R/ran.md#rancor) | G | 1 | 853 | $1.02 |  |
| [Loxodon Warhammer](cards/L/lo.md#loxodon-warhammer) | C | 3 | 987 | $1.22 |  |
| [Genji Glove](cards/G/ge.md#genji-glove) | C | 5 | 1,058 | $7.25 |  |
| [Fireshrieker](cards/F/fi.md#fireshrieker) | C | 3 | 1,142 | $0.23 |  |

Budget options beyond the top 10 (≤ $1.00): [Sticky Fingers](cards/S/sti.md#sticky-fingers) (R, $0.23) · [Beamtown Beatstick](cards/B/be.md#beamtown-beatstick) (R, $0.82) · [Wrecking Ball Arm](cards/W/wr.md#wrecking-ball-arm) (C, $0.28) · [Glasswing Grace // Age-Graced Chapel](cards/G/gl.md#glasswing-grace--age-graced-chapel) (WB, $0.36)

## Treasure

**Guidance:** Plan: make Treasure for ramp, fixing and artifact synergies.

### Treasure: Repeatable Treasure makers

Pattern: `(whenever|at the beginning)[^.]*create (a|one|two|X|that many) Treasure tokens?` · 97 Commander-legal matches

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Black Market Connections](cards/B/bla.md#black-market-connections) | B | 3 | 129 | $10.94 |  |
| [Storm-Kiln Artist](cards/S/sto.md#storm-kiln-artist) | R | 4 | 196 | $1.81 |  |
| [Professional Face-Breaker](cards/P/pr.md#professional-face-breaker) | R | 3 | 207 | $4.95 |  |
| [Pitiless Plunderer](cards/P/pi.md#pitiless-plunderer) | B | 4 | 224 | $2.90 |  |
| [Ragavan, Nimble Pilferer](cards/R/rag.md#ragavan-nimble-pilferer) | R | 1 | 282 | $39.33 |  |
| [Goldspan Dragon](cards/G/gol.md#goldspan-dragon) | R | 5 | 365 | $11.18 |  |
| [Lotho, Corrupt Shirriff](cards/L/lo.md#lotho-corrupt-shirriff) | WB | 2 | 410 | $9.05 |  |
| [The Reaver Cleaver](cards/T/ther.md#the-reaver-cleaver) | R | 3 | 530 | $24.48 |  |
| [Grim Hireling](cards/G/gri.md#grim-hireling) | B | 4 | 902 | $10.17 |  |
| [Old Gnawbone](cards/O/ol.md#old-gnawbone) | G | 7 | 932 | $48.53 |  |

Budget options beyond the top 10 (≤ $1.00): [Captain Lannery Storm](cards/C/cap.md#captain-lannery-storm) (R, $0.26) · [Mahadi, Emporium Master](cards/M/mah.md#mahadi-emporium-master) (BR, $0.44) · [Shiny Impetus](cards/S/shi.md#shiny-impetus) (R, $0.13) · [Sticky Fingers](cards/S/sti.md#sticky-fingers) (R, $0.23)

## Method

- Each sub-package is a regex on Oracle text over Commander-legal cards (case-insensitive), shown with the section. Matches are heuristics, so some cards fit loosely.
- Related: [EDH Mana Bases](EDH%20Mana%20Bases.md) · [EDH Win Conditions](EDH%20Win%20Conditions.md) · [EDH Interaction](EDH%20Interaction.md) · [EDH Archetypes](EDH%20Archetypes.md) · [EDH Staples](EDH%20Staples.md).
