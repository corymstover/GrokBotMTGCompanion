---
title: "EDH Mana Bases"
category: edh
tags: [lands, mana-base, color-identity]
issues: [25]
generated_by: scripts/build_mana_bases.py
sources: [scryfall, edhrec]
related: ["EDH Packages.md", "EDH Standards.md", "EDH Mulligans.md", "EDH Staples.md", "Rules Interactions.md", "grixis/README.md"]
schema: 2
---

# EDH Mana Bases

> **Auto-generated** by `scripts/build_mana_bases.py` (Bot cycle 6, issue [#25](https://github.com/corymstover/GrokBotMTGCompanion/issues/25)) from Scryfall Oracle bulk 2026-10-15. Do not hand-edit.
> **Data:** every card listed is **Commander-legal** per Scryfall. *Identity* is its color identity: it fits a deck only if that identity is a subset of the commander's ([CR 903.4](Rules%20Interactions.md#commander-color-identity)). Lists are ordered by Scryfall `edhrec_rank` (EDHREC popularity, lower = more played); popularity is not power. **GC** = official Game Changer, which affects the [Commander Brackets](EDH%20Standards.md#power-bracket-assessment). *Cheapest USD* is the lowest current paper price across printings in Scryfall's default-cards bulk (2026-10-15 snapshot; prices move daily). Categories are Oracle-text pattern matches; the patterns are listed in each section.
> **Guidance** paragraphs are strategy advice (opinion), not rules or fact.

## Contents
- [Land counts](#land-counts)
- [Universal fixing (any identity)](#universal-fixing-any-identity)
- [Colorless utility lands](#colorless-utility-lands)
- [By color identity](#by-color-identity): [Colorless](#colorless-c) · [White](#white-w) · [Blue](#blue-u) · [Black](#black-b) · [Red](#red-r) · [Green](#green-g) · [Azorius](#azorius-wu) · [Dimir](#dimir-ub) · [Rakdos](#rakdos-br) · [Gruul](#gruul-rg) · [Selesnya](#selesnya-wg) · [Orzhov](#orzhov-wb) · [Izzet](#izzet-ur) · [Golgari](#golgari-bg) · [Boros](#boros-wr) · [Simic](#simic-ug) · [Bant](#bant-wug) · [Esper](#esper-wub) · [Grixis](#grixis-ubr) · [Jund](#jund-brg) · [Naya](#naya-wrg) · [Abzan](#abzan-wbg) · [Jeskai](#jeskai-wur) · [Sultai](#sultai-ubg) · [Mardu](#mardu-wbr) · [Temur](#temur-urg) · [Glint (non-W)](#glint-non-w-ubrg) · [Dune (non-U)](#dune-non-u-wbrg) · [Ink (non-B)](#ink-non-b-wurg) · [Witch (non-R)](#witch-non-r-wubg) · [Yore (non-G)](#yore-non-g-wubr) · [Five-color](#five-color-wubrg)
- [Method](#method)

## Land counts

**Data (this repo's 32 validated skeletons):** all use 36 lands, the default of `scripts/build_deck_skeleton.py`. See the [decks/](decks/) files.

**Guidance (opinion):**
- A common starting point for a 100-card deck is about **36–38 lands** plus roughly **10 ramp pieces**.
- Go lower (33–35) with a low curve, many cheap rocks or a mana-producing commander.
- Go higher (38–40+) for lands-matter/landfall decks or a commander that costs 6+ mana.
- **Basics:** keep enough basics for land-search ramp (Cultivate-style spells and the fetches below) and for the checklands' land types. Mono-color decks can run mostly basics plus utility lands.
- **Budget vs. optimized:** the *Budget picks* rows use the cheapest current printings. Optimized mana bases usually move toward untapped duals: originals, shocks, fetches, fast/slow/check, pain, horizon, bond. Taplands are the first cuts.

## Universal fixing (any identity)

Lands with colorless identity that can produce three or more colors (pattern: Scryfall `produced_mana` ≥ 3 colors). Some are limited by their own text (for example [Command Tower](cards/C/com.md#command-tower) adds only colors in your commander's identity), while others such as City of Brass make any color. Guidance: most valuable in 3+ color decks.

| Card | Kind | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|
| [Command Tower](cards/C/com.md#command-tower) | other | 2 | $0.23 |  |
| [Exotic Orchard](cards/E/ex.md#exotic-orchard) | other | 9 | $0.23 |  |
| [Path of Ancestry](cards/P/pa.md#path-of-ancestry) | tapland | 14 | $0.18 |  |
| [City of Brass](cards/C/ci.md#city-of-brass) | pain | 94 | $9.17 |  |
| [Cavern of Souls](cards/C/cav.md#cavern-of-souls) | other | 110 | $47.61 |  |
| [Mana Confluence](cards/M/man.md#mana-confluence) | horizon | 116 | $35.63 |  |
| [Nykthos, Shrine to Nyx](cards/N/ny.md#nykthos-shrine-to-nyx) | other | 163 | $39.39 |  |
| [Reflecting Pool](cards/R/ref.md#reflecting-pool) | other | 164 | $4.78 |  |
| [Three Tree City](cards/T/thr.md#three-tree-city) | other | 178 | $28.73 |  |
| [Gemstone Caverns](cards/G/ge.md#gemstone-caverns) | other | 181 | $60.64 |  |
| [Secluded Courtyard](cards/S/sec.md#secluded-courtyard) | other | 221 | $0.25 |  |
| [Unclaimed Territory](cards/U/un.md#unclaimed-territory) | other | 247 | $0.33 |  |
| [Spire of Industry](cards/S/spi.md#spire-of-industry) | horizon | 392 | $0.23 |  |
| [Plaza of Heroes](cards/P/pl.md#plaza-of-heroes) | other | 471 | $2.98 |  |
| [Talon Gates of Madara](cards/T/ta.md#talon-gates-of-madara) | other | 569 | $34.66 |  |

## Colorless utility lands

Non-basic colorless-identity lands with a non-mana ability, grouped by the first pattern they match.

### Fetch lands & land search
Pattern: `Search your library for`

| Card | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|
| [Evolving Wilds](cards/E/ev.md#evolving-wilds) | 19 | $0.10 |  |
| [Terramorphic Expanse](cards/T/te.md#terramorphic-expanse) | 30 | $0.10 |  |
| [Myriad Landscape](cards/M/my.md#myriad-landscape) | 31 | $0.24 |  |
| [Polluted Delta](cards/P/po.md#polluted-delta) | 36 | $20.36 |  |
| [Flooded Strand](cards/F/fl.md#flooded-strand) | 38 | $12.78 |  |
| [Misty Rainforest](cards/M/mis.md#misty-rainforest) | 42 | $36.99 |  |
| [Bloodstained Mire](cards/B/blo.md#bloodstained-mire) | 43 | $14.54 |  |
| [Fabled Passage](cards/F/fa.md#fabled-passage) | 44 | $0.86 |  |

### Land destruction / utility removal
Pattern: `destroy target (nonbasic )?land|Sacrifice this land: .*destroy`

| Card | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|
| [Demolition Field](cards/D/dem.md#demolition-field) | 394 | $0.29 |  |
| [Strip Mine](cards/S/str.md#strip-mine) | 529 | $10.71 |  |
| [Ghost Quarter](cards/G/gh.md#ghost-quarter) | 835 | $0.43 |  |
| [Field of Ruin](cards/F/fi.md#field-of-ruin) | 914 | $0.27 |  |
| [Wasteland](cards/W/was.md#wasteland) | 1,217 | $9.15 |  |
| [Blast Zone](cards/B/bla.md#blast-zone) | 1,667 | $0.34 |  |
| [Volatile Fault](cards/V/vo.md#volatile-fault) | 2,696 | $0.28 |  |
| [Tectonic Edge](cards/T/te.md#tectonic-edge) | 4,187 | $0.32 |  |

### Card advantage
Pattern: `draw a card|Scry \d|surveil`

| Card | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|
| [War Room](cards/W/war.md#war-room) | 139 | $0.81 |  |
| [Bonders' Enclave](cards/B/bo.md#bonders-enclave) | 542 | $0.24 |  |
| [Fountainport](cards/F/fo.md#fountainport) | 933 | $2.82 |  |
| [Arid Archway](cards/A/ari.md#arid-archway) | 1,499 | $1.32 |  |
| [Zhalfirin Void](cards/Z/zh.md#zhalfirin-void) | 2,514 | $0.34 |  |
| [Arch of Orazca](cards/A/arc.md#arch-of-orazca) | 2,622 | $0.34 |  |
| [The Gold Saucer](cards/T/theg.md#the-gold-saucer) | 3,331 | $0.26 |  |
| [Avishkar Raceway](cards/A/av.md#avishkar-raceway) | 3,803 | $0.21 |  |

### Graveyard interaction
Pattern: `graveyard`

| Card | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|
| [Buried Ruin](cards/B/bu.md#buried-ruin) | 193 | $0.35 |  |
| [Scavenger Grounds](cards/S/sc.md#scavenger-grounds) | 294 | $0.21 |  |
| [Drownyard Temple](cards/D/dro.md#drownyard-temple) | 1,989 | $0.24 |  |
| [Echoing Deeps](cards/E/ec.md#echoing-deeps) | 2,519 | $0.51 |  |
| [Eden, Seat of the Sanctum](cards/E/ed.md#eden-seat-of-the-sanctum) | 3,616 | $0.26 |  |
| [Dunes of the Dead](cards/D/du.md#dunes-of-the-dead) | 5,856 | $0.29 |  |
| [Tocasia's Dig Site](cards/T/to.md#tocasias-dig-site) | 6,333 | $0.28 |  |
| [Scorched Ruins](cards/S/sc.md#scorched-ruins) | 6,398 | $62.96 |  |

### Creature lands
Pattern: `becomes? an? .*creature`

| Card | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|
| [Mutavault](cards/M/mu.md#mutavault) | 1,910 | $3.99 |  |
| [Inkmoth Nexus](cards/I/ink.md#inkmoth-nexus) | 1,957 | $11.78 |  |
| [Blinkmoth Nexus](cards/B/bli.md#blinkmoth-nexus) | 3,084 | $1.09 |  |
| [Mishra's Factory](cards/M/mis.md#mishras-factory) | 3,256 | $0.19 |  |
| [Soulstone Sanctuary](cards/S/so.md#soulstone-sanctuary) | 5,669 | $0.61 |  |
| [Crawling Barrens](cards/C/cr.md#crawling-barrens) | 6,615 | $0.17 |  |
| [Mishra's Foundry](cards/M/mis.md#mishras-foundry) | 7,842 | $0.34 |  |
| [Faceless Haven](cards/F/fa.md#faceless-haven) | 7,940 | $0.33 |  |

### Mana & untapping
Pattern: `Add \{C\}\{C\}|for each|untap target`

| Card | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|
| [Ancient Tomb](cards/A/an.md#ancient-tomb) | 69 | $57.03 | **GC** |
| [Temple of the False God](cards/T/te.md#temple-of-the-false-god) | 84 | $0.19 |  |
| [Urza's Saga](cards/U/ur.md#urzas-saga) | 117 | $35.21 |  |
| [Maze of Ith](cards/M/maz.md#maze-of-ith) | 556 | $8.82 |  |
| [Urza's Tower](cards/U/ur.md#urzas-tower) | 832 | $0.87 |  |
| [Urza's Mine](cards/U/ur.md#urzas-mine) | 840 | $0.66 |  |
| [Urza's Power Plant](cards/U/ur.md#urzas-power-plant) | 842 | $0.61 |  |
| [City of Traitors](cards/C/ci.md#city-of-traitors) | 1,157 | $49.73 |  |

### Other utility
Pattern: `.`

| Card | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|
| [Reliquary Tower](cards/R/rel.md#reliquary-tower) | 10 | $4.36 |  |
| [Rogue's Passage](cards/R/ro.md#rogues-passage) | 18 | $0.35 |  |
| [Windswept Heath](cards/W/wi.md#windswept-heath) | 45 | $11.19 |  |
| [Wooded Foothills](cards/W/wo.md#wooded-foothills) | 47 | $17.90 |  |
| [Verdant Catacombs](cards/V/ve.md#verdant-catacombs) | 48 | $29.78 |  |
| [Scalding Tarn](cards/S/sc.md#scalding-tarn) | 49 | $35.64 |  |
| [Marsh Flats](cards/M/mar.md#marsh-flats) | 51 | $31.55 |  |
| [Arid Mesa](cards/A/ari.md#arid-mesa) | 55 | $29.27 |  |

## By color identity

For each identity, the table lists non-basic lands with **exactly** that color identity, most-played first. *Kind* is a heuristic label from Oracle text (fetch, shock, check …); "tapland" means it always or usually enters tapped. A deck can also use the lands of every **subset** of its identity, so a 3+ color deck should start from the sections for its color pairs.

### Colorless C

**Most played** (354 lands with this exact identity):

| Card | Kind | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|
| [Command Tower](cards/C/com.md#command-tower) | other | 2 | $0.23 |  |
| [Exotic Orchard](cards/E/ex.md#exotic-orchard) | other | 9 | $0.23 |  |
| [Reliquary Tower](cards/R/rel.md#reliquary-tower) | other | 10 | $4.36 |  |
| [Path of Ancestry](cards/P/pa.md#path-of-ancestry) | tapland | 14 | $0.18 |  |
| [Rogue's Passage](cards/R/ro.md#rogues-passage) | other | 18 | $0.35 |  |
| [Evolving Wilds](cards/E/ev.md#evolving-wilds) | other | 19 | $0.10 |  |
| [Terramorphic Expanse](cards/T/te.md#terramorphic-expanse) | other | 30 | $0.10 |  |
| [Myriad Landscape](cards/M/my.md#myriad-landscape) | tapland | 31 | $0.24 |  |
| [Polluted Delta](cards/P/po.md#polluted-delta) | fetch | 36 | $20.36 |  |
| [Flooded Strand](cards/F/fl.md#flooded-strand) | fetch | 38 | $12.78 |  |
| [Misty Rainforest](cards/M/mis.md#misty-rainforest) | fetch | 42 | $36.99 |  |
| [Bloodstained Mire](cards/B/blo.md#bloodstained-mire) | fetch | 43 | $14.54 |  |

**Budget picks (≤ $1.00):**

| Card | Kind | EDHREC rank | Cheapest USD |
|---|---|---|---|
| [Command Tower](cards/C/com.md#command-tower) | other | 2 | $0.23 |
| [Exotic Orchard](cards/E/ex.md#exotic-orchard) | other | 9 | $0.23 |
| [Path of Ancestry](cards/P/pa.md#path-of-ancestry) | tapland | 14 | $0.18 |
| [Rogue's Passage](cards/R/ro.md#rogues-passage) | other | 18 | $0.35 |
| [Evolving Wilds](cards/E/ev.md#evolving-wilds) | other | 19 | $0.10 |
| [Terramorphic Expanse](cards/T/te.md#terramorphic-expanse) | other | 30 | $0.10 |

### White W

**Most played** (47 lands with this exact identity):

| Card | Kind | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|
| [Eiganjo, Seat of the Empire](cards/E/ei.md#eiganjo-seat-of-the-empire) | other | 376 | $6.51 |  |
| [Minas Tirith](cards/M/min.md#minas-tirith) | tapland | 416 | $6.47 |  |
| [Hall of Heliod's Generosity](cards/H/ha.md#hall-of-heliods-generosity) | other | 433 | $10.33 |  |
| [Ancient Den](cards/A/an.md#ancient-den) | other | 483 | $1.52 |  |
| [Windbrisk Heights](cards/W/wi.md#windbrisk-heights) | tapland | 661 | $0.21 |  |
| [Castle Ardenvale](cards/C/cas.md#castle-ardenvale) | check | 715 | $0.25 |  |
| [Emeria, the Sky Ruin](cards/E/em.md#emeria-the-sky-ruin) | tapland | 942 | $7.49 |  |
| [Thriving Heath](cards/T/thr.md#thriving-heath) | tapland | 1,098 | $0.12 |  |
| [Abandoned Air Temple](cards/A/ab.md#abandoned-air-temple) | tapland | 1,126 | $6.83 |  |
| [Ishgard, the Holy See // Faith & Grief](cards/I/is.md#ishgard-the-holy-see--faith--grief) | tapland | 1,421 | $1.65 |  |
| [Secluded Steppe](cards/S/sec.md#secluded-steppe) | cycling tapland | 1,459 | $0.11 |  |
| [Monumental Henge](cards/M/mon.md#monumental-henge) | check | 1,482 | $0.58 |  |

**Budget picks (≤ $1.00):**

| Card | Kind | EDHREC rank | Cheapest USD |
|---|---|---|---|
| [Windbrisk Heights](cards/W/wi.md#windbrisk-heights) | tapland | 661 | $0.21 |
| [Castle Ardenvale](cards/C/cas.md#castle-ardenvale) | check | 715 | $0.25 |
| [Thriving Heath](cards/T/thr.md#thriving-heath) | tapland | 1,098 | $0.12 |
| [Secluded Steppe](cards/S/sec.md#secluded-steppe) | cycling tapland | 1,459 | $0.11 |
| [Monumental Henge](cards/M/mon.md#monumental-henge) | check | 1,482 | $0.58 |
| [Mistveil Plains](cards/M/mis.md#mistveil-plains) | tapland | 2,791 | $0.26 |

### Blue U

**Most played** (49 lands with this exact identity):

| Card | Kind | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|
| [Otawara, Soaring City](cards/O/ot.md#otawara-soaring-city) | other | 89 | $27.94 |  |
| [Mystic Sanctuary](cards/M/my.md#mystic-sanctuary) | tapland | 175 | $1.15 |  |
| [Seat of the Synod](cards/S/sea.md#seat-of-the-synod) | other | 310 | $0.93 |  |
| [Mistrise Village](cards/M/mis.md#mistrise-village) | check | 375 | $7.35 |  |
| [Academy Ruins](cards/A/ac.md#academy-ruins) | other | 459 | $4.41 |  |
| [Minamo, School at Water's Edge](cards/M/min.md#minamo-school-at-waters-edge) | other | 612 | $57.98 |  |
| [Cephalid Coliseum](cards/C/ce.md#cephalid-coliseum) | pain | 854 | $0.31 |  |
| [Archway of Innovation](cards/A/arc.md#archway-of-innovation) | check | 925 | $1.08 |  |
| [Thriving Isle](cards/T/thr.md#thriving-isle) | tapland | 1,010 | $0.13 |  |
| [Rivendell](cards/R/ri.md#rivendell) | tapland | 1,013 | $1.11 |  |
| [Castle Vantress](cards/C/cas.md#castle-vantress) | check | 1,014 | $0.31 |  |
| [Lonely Sandbar](cards/L/lo.md#lonely-sandbar) | cycling tapland | 1,146 | $0.18 |  |

**Budget picks (≤ $1.00):**

| Card | Kind | EDHREC rank | Cheapest USD |
|---|---|---|---|
| [Seat of the Synod](cards/S/sea.md#seat-of-the-synod) | other | 310 | $0.93 |
| [Cephalid Coliseum](cards/C/ce.md#cephalid-coliseum) | pain | 854 | $0.31 |
| [Thriving Isle](cards/T/thr.md#thriving-isle) | tapland | 1,010 | $0.13 |
| [Castle Vantress](cards/C/cas.md#castle-vantress) | check | 1,014 | $0.31 |
| [Lonely Sandbar](cards/L/lo.md#lonely-sandbar) | cycling tapland | 1,146 | $0.18 |
| [Halimar Depths](cards/H/ha.md#halimar-depths) | tapland | 1,352 | $0.34 |

### Black B

**Most played** (55 lands with this exact identity):

| Card | Kind | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|
| [Bojuka Bog](cards/B/bo.md#bojuka-bog) | tapland | 24 | $1.31 |  |
| [Phyrexian Tower](cards/P/ph.md#phyrexian-tower) | other | 194 | $29.06 |  |
| [Cabal Coffers](cards/C/cab.md#cabal-coffers) | other | 200 | $21.00 |  |
| [Takenuma, Abandoned Mire](cards/T/ta.md#takenuma-abandoned-mire) | other | 245 | $11.26 |  |
| [Vault of Whispers](cards/V/va.md#vault-of-whispers) | other | 620 | $1.75 |  |
| [Shizo, Death's Storehouse](cards/S/shi.md#shizo-deaths-storehouse) | other | 623 | $35.64 |  |
| [Mortuary Mire](cards/M/mor.md#mortuary-mire) | tapland | 707 | $0.28 |  |
| [Castle Locthwain](cards/C/cas.md#castle-locthwain) | check | 790 | $1.38 |  |
| [Witch's Cottage](cards/W/wi.md#witchs-cottage) | tapland | 875 | $0.38 |  |
| [Cabal Stronghold](cards/C/cab.md#cabal-stronghold) | other | 971 | $13.54 |  |
| [Barren Moor](cards/B/bar.md#barren-moor) | cycling tapland | 1,060 | $0.16 |  |
| [Spymaster's Vault](cards/S/spy.md#spymasters-vault) | check | 1,154 | $1.99 |  |

**Budget picks (≤ $1.00):**

| Card | Kind | EDHREC rank | Cheapest USD |
|---|---|---|---|
| [Mortuary Mire](cards/M/mor.md#mortuary-mire) | tapland | 707 | $0.28 |
| [Witch's Cottage](cards/W/wi.md#witchs-cottage) | tapland | 875 | $0.38 |
| [Barren Moor](cards/B/bar.md#barren-moor) | cycling tapland | 1,060 | $0.16 |
| [Thriving Moor](cards/T/thr.md#thriving-moor) | tapland | 1,223 | $0.12 |
| [Dakmor Salvage](cards/D/da.md#dakmor-salvage) | tapland | 1,302 | $0.35 |
| [Black Dragon Gate](cards/B/bla.md#black-dragon-gate) | tapland | 2,593 | $0.47 |

### Red R

**Most played** (52 lands with this exact identity):

| Card | Kind | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|
| [Great Furnace](cards/G/gre.md#great-furnace) | other | 371 | $2.49 |  |
| [Arena of Glory](cards/A/are.md#arena-of-glory) | check | 372 | $7.75 |  |
| [Spinerock Knoll](cards/S/spi.md#spinerock-knoll) | tapland | 783 | $0.45 |  |
| [Forgotten Cave](cards/F/fo.md#forgotten-cave) | cycling tapland | 869 | $0.13 |  |
| [Sokenzan, Crucible of Defiance](cards/S/so.md#sokenzan-crucible-of-defiance) | other | 992 | $3.00 |  |
| [Mines of Moria](cards/M/min.md#mines-of-moria) | tapland | 994 | $3.39 |  |
| [Castle Embereth](cards/C/cas.md#castle-embereth) | check | 1,096 | $0.36 |  |
| [Thriving Bluff](cards/T/thr.md#thriving-bluff) | tapland | 1,204 | $0.17 |  |
| [Valakut, the Molten Pinnacle](cards/V/va.md#valakut-the-molten-pinnacle) | tapland | 1,320 | $13.42 |  |
| [Lindblum, Industrial Regency // Mage Siege](cards/L/li.md#lindblum-industrial-regency--mage-siege) | tapland | 1,384 | $1.84 |  |
| [Kher Keep](cards/K/kh.md#kher-keep) | other | 1,617 | $0.20 |  |
| [Fire Nation Palace](cards/F/fi.md#fire-nation-palace) | tapland | 1,646 | $2.17 |  |

**Budget picks (≤ $1.00):**

| Card | Kind | EDHREC rank | Cheapest USD |
|---|---|---|---|
| [Spinerock Knoll](cards/S/spi.md#spinerock-knoll) | tapland | 783 | $0.45 |
| [Forgotten Cave](cards/F/fo.md#forgotten-cave) | cycling tapland | 869 | $0.13 |
| [Castle Embereth](cards/C/cas.md#castle-embereth) | check | 1,096 | $0.36 |
| [Thriving Bluff](cards/T/thr.md#thriving-bluff) | tapland | 1,204 | $0.17 |
| [Kher Keep](cards/K/kh.md#kher-keep) | other | 1,617 | $0.20 |
| [Dwarven Mine](cards/D/dw.md#dwarven-mine) | tapland | 2,753 | $0.49 |

### Green G

**Most played** (49 lands with this exact identity):

| Card | Kind | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|
| [Boseiju, Who Endures](cards/B/bo.md#boseiju-who-endures) | other | 77 | $48.52 |  |
| [Mosswort Bridge](cards/M/mos.md#mosswort-bridge) | tapland | 197 | $0.25 |  |
| [Shifting Woodland](cards/S/shi.md#shifting-woodland) | check | 361 | $7.53 |  |
| [Gaea's Cradle](cards/G/ga.md#gaeas-cradle) | other | 448 | $303.59 | **GC** |
| [Castle Garenbrig](cards/C/cas.md#castle-garenbrig) | check | 720 | $9.00 |  |
| [Oran-Rief, the Vastwood](cards/O/or.md#oran-rief-the-vastwood) | tapland | 740 | $0.41 |  |
| [Dryad Arbor](cards/D/dry.md#dryad-arbor) | other | 778 | $3.34 |  |
| [Evendo, Waking Haven](cards/E/ev.md#evendo-waking-haven) | tapland | 905 | $17.70 |  |
| [Blighted Woodland](cards/B/bli.md#blighted-woodland) | other | 945 | $0.28 |  |
| [Tranquil Thicket](cards/T/tra.md#tranquil-thicket) | cycling tapland | 1,078 | $0.11 |  |
| [Thriving Grove](cards/T/thr.md#thriving-grove) | tapland | 1,175 | $0.11 |  |
| [The Shire](cards/T/thes.md#the-shire) | tapland | 1,184 | $2.60 |  |

**Budget picks (≤ $1.00):**

| Card | Kind | EDHREC rank | Cheapest USD |
|---|---|---|---|
| [Mosswort Bridge](cards/M/mos.md#mosswort-bridge) | tapland | 197 | $0.25 |
| [Oran-Rief, the Vastwood](cards/O/or.md#oran-rief-the-vastwood) | tapland | 740 | $0.41 |
| [Blighted Woodland](cards/B/bli.md#blighted-woodland) | other | 945 | $0.28 |
| [Tranquil Thicket](cards/T/tra.md#tranquil-thicket) | cycling tapland | 1,078 | $0.11 |
| [Thriving Grove](cards/T/thr.md#thriving-grove) | tapland | 1,175 | $0.11 |
| [Llanowar Reborn](cards/L/ll.md#llanowar-reborn) | tapland | 2,422 | $0.24 |

### Azorius WU

**Most played** (51 lands with this exact identity):

| Card | Kind | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|
| [Hallowed Fountain](cards/H/ha.md#hallowed-fountain) | shock | 61 | $7.13 |  |
| [Glacial Fortress](cards/G/gl.md#glacial-fortress) | check | 88 | $0.20 |  |
| [Prairie Stream](cards/P/pr.md#prairie-stream) | tapland | 103 | $0.18 |  |
| [Adarkar Wastes](cards/A/ad.md#adarkar-wastes) | pain | 143 | $0.33 |  |
| [Sea of Clouds](cards/S/sea.md#sea-of-clouds) | bond (multiplayer) | 165 | $19.54 |  |
| [Deserted Beach](cards/D/des.md#deserted-beach) | slow | 267 | $1.36 |  |
| [Temple of Enlightenment](cards/T/te.md#temple-of-enlightenment) | tapland | 320 | $0.14 |  |
| [Port Town](cards/P/po.md#port-town) | tapland | 338 | $0.19 |  |
| [Skycloud Expanse](cards/S/sk.md#skycloud-expanse) | filter (two-color) | 347 | $0.19 |  |
| [Tundra](cards/T/tu.md#tundra) | original dual | 350 | $302.90 |  |
| [Azorius Chancery](cards/A/az.md#azorius-chancery) | bounce | 478 | $0.16 |  |
| [Floodfarm Verge](cards/F/fl.md#floodfarm-verge) | other | 619 | $8.87 |  |

**On-color fetches** (colorless identity; can find a land with the Plains or Island type, so they also find the typed duals above):

| Card | EDHREC rank | Cheapest USD |
|---|---|---|
| [Flooded Strand](cards/F/fl.md#flooded-strand) | 38 | $12.78 |
| [Bant Panorama](cards/B/ban.md#bant-panorama) | 5,012 | $0.33 |
| [Flood Plain](cards/F/fl.md#flood-plain) | 5,558 | $0.39 |
| [Esper Panorama](cards/E/es.md#esper-panorama) | 6,292 | $0.28 |

**Budget picks (≤ $1.00):**

| Card | Kind | EDHREC rank | Cheapest USD |
|---|---|---|---|
| [Glacial Fortress](cards/G/gl.md#glacial-fortress) | check | 88 | $0.20 |
| [Prairie Stream](cards/P/pr.md#prairie-stream) | tapland | 103 | $0.18 |
| [Adarkar Wastes](cards/A/ad.md#adarkar-wastes) | pain | 143 | $0.33 |
| [Temple of Enlightenment](cards/T/te.md#temple-of-enlightenment) | tapland | 320 | $0.14 |
| [Port Town](cards/P/po.md#port-town) | tapland | 338 | $0.19 |
| [Skycloud Expanse](cards/S/sk.md#skycloud-expanse) | filter (two-color) | 347 | $0.19 |

### Dimir UB

**Most played** (49 lands with this exact identity):

| Card | Kind | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|
| [Watery Grave](cards/W/wat.md#watery-grave) | shock | 50 | $10.01 |  |
| [Sunken Hollow](cards/S/sun.md#sunken-hollow) | tapland | 86 | $0.30 |  |
| [Drowned Catacomb](cards/D/dro.md#drowned-catacomb) | check | 105 | $0.40 |  |
| [Underground River](cards/U/un.md#underground-river) | pain | 141 | $0.55 |  |
| [Morphic Pool](cards/M/mor.md#morphic-pool) | bond (multiplayer) | 149 | $28.95 |  |
| [Shipwreck Marsh](cards/S/shi.md#shipwreck-marsh) | slow | 227 | $1.52 |  |
| [Choked Estuary](cards/C/cho.md#choked-estuary) | tapland | 292 | $0.30 |  |
| [Underground Sea](cards/U/un.md#underground-sea) | original dual | 297 | $475.00 |  |
| [Darkwater Catacombs](cards/D/da.md#darkwater-catacombs) | filter (two-color) | 328 | $0.28 |  |
| [Temple of Deceit](cards/T/te.md#temple-of-deceit) | tapland | 360 | $0.19 |  |
| [Dimir Aqueduct](cards/D/di.md#dimir-aqueduct) | bounce | 387 | $0.25 |  |
| [Undercity Sewers](cards/U/un.md#undercity-sewers) | surveil tapland | 421 | $9.26 |  |

**On-color fetches** (colorless identity; can find a land with the Island or Swamp type, so they also find the typed duals above):

| Card | EDHREC rank | Cheapest USD |
|---|---|---|
| [Polluted Delta](cards/P/po.md#polluted-delta) | 36 | $20.36 |
| [Grixis Panorama](cards/G/gri.md#grixis-panorama) | 6,039 | $0.36 |
| [Esper Panorama](cards/E/es.md#esper-panorama) | 6,292 | $0.28 |
| [Bad River](cards/B/bad.md#bad-river) | 6,876 | $1.36 |

**Budget picks (≤ $1.00):**

| Card | Kind | EDHREC rank | Cheapest USD |
|---|---|---|---|
| [Sunken Hollow](cards/S/sun.md#sunken-hollow) | tapland | 86 | $0.30 |
| [Drowned Catacomb](cards/D/dro.md#drowned-catacomb) | check | 105 | $0.40 |
| [Underground River](cards/U/un.md#underground-river) | pain | 141 | $0.55 |
| [Choked Estuary](cards/C/cho.md#choked-estuary) | tapland | 292 | $0.30 |
| [Darkwater Catacombs](cards/D/da.md#darkwater-catacombs) | filter (two-color) | 328 | $0.28 |
| [Temple of Deceit](cards/T/te.md#temple-of-deceit) | tapland | 360 | $0.19 |

### Rakdos BR

**Most played** (50 lands with this exact identity):

| Card | Kind | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|
| [Blood Crypt](cards/B/blo.md#blood-crypt) | shock | 68 | $9.22 |  |
| [Dragonskull Summit](cards/D/dra.md#dragonskull-summit) | check | 83 | $0.43 |  |
| [Smoldering Marsh](cards/S/sm.md#smoldering-marsh) | tapland | 95 | $0.25 |  |
| [Sulfurous Springs](cards/S/sul.md#sulfurous-springs) | pain | 144 | $0.42 |  |
| [Luxury Suite](cards/L/lu.md#luxury-suite) | bond (multiplayer) | 161 | $8.53 |  |
| [Haunted Ridge](cards/H/ha.md#haunted-ridge) | slow | 270 | $1.40 |  |
| [Foreboding Ruins](cards/F/fo.md#foreboding-ruins) | tapland | 316 | $0.33 |  |
| [Badlands](cards/B/bad.md#badlands) | original dual | 380 | $253.79 |  |
| [Shadowblood Ridge](cards/S/sha.md#shadowblood-ridge) | filter (two-color) | 436 | $0.25 |  |
| [Temple of Malice](cards/T/te.md#temple-of-malice) | tapland | 462 | $0.22 |  |
| [Blazemire Verge](cards/B/bla.md#blazemire-verge) | other | 496 | $9.97 |  |
| [Tainted Peak](cards/T/ta.md#tainted-peak) | other | 497 | $1.21 |  |

**On-color fetches** (colorless identity; can find a land with the Swamp or Mountain type, so they also find the typed duals above):

| Card | EDHREC rank | Cheapest USD |
|---|---|---|
| [Bloodstained Mire](cards/B/blo.md#bloodstained-mire) | 43 | $14.54 |
| [Rocky Tar Pit](cards/R/ro.md#rocky-tar-pit) | 3,404 | $0.25 |
| [Jund Panorama](cards/J/ju.md#jund-panorama) | 5,252 | $0.39 |
| [Grixis Panorama](cards/G/gri.md#grixis-panorama) | 6,039 | $0.36 |

**Budget picks (≤ $1.00):**

| Card | Kind | EDHREC rank | Cheapest USD |
|---|---|---|---|
| [Dragonskull Summit](cards/D/dra.md#dragonskull-summit) | check | 83 | $0.43 |
| [Smoldering Marsh](cards/S/sm.md#smoldering-marsh) | tapland | 95 | $0.25 |
| [Sulfurous Springs](cards/S/sul.md#sulfurous-springs) | pain | 144 | $0.42 |
| [Foreboding Ruins](cards/F/fo.md#foreboding-ruins) | tapland | 316 | $0.33 |
| [Shadowblood Ridge](cards/S/sha.md#shadowblood-ridge) | filter (two-color) | 436 | $0.25 |
| [Temple of Malice](cards/T/te.md#temple-of-malice) | tapland | 462 | $0.22 |

### Gruul RG

**Most played** (47 lands with this exact identity):

| Card | Kind | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|
| [Stomping Ground](cards/S/sto.md#stomping-ground) | shock | 70 | $7.17 |  |
| [Cinder Glade](cards/C/ci.md#cinder-glade) | tapland | 87 | $0.23 |  |
| [Rootbound Crag](cards/R/ro.md#rootbound-crag) | check | 128 | $0.26 |  |
| [Spire Garden](cards/S/spi.md#spire-garden) | bond (multiplayer) | 188 | $6.20 |  |
| [Karplusan Forest](cards/K/ka.md#karplusan-forest) | pain | 219 | $0.44 |  |
| [Rockfall Vale](cards/R/ro.md#rockfall-vale) | slow | 225 | $0.63 |  |
| [Game Trail](cards/G/ga.md#game-trail) | tapland | 397 | $0.26 |  |
| [Kessig Wolf Run](cards/K/ke.md#kessig-wolf-run) | other | 406 | $0.35 |  |
| [Taiga](cards/T/ta.md#taiga) | original dual | 435 | $200.00 |  |
| [Gruul Turf](cards/G/gru.md#gruul-turf) | bounce | 466 | $0.25 |  |
| [Temple of Abandon](cards/T/te.md#temple-of-abandon) | tapland | 548 | $0.18 |  |
| [Mossfire Valley](cards/M/mos.md#mossfire-valley) | filter (two-color) | 552 | $0.21 |  |

**On-color fetches** (colorless identity; can find a land with the Mountain or Forest type, so they also find the typed duals above):

| Card | EDHREC rank | Cheapest USD |
|---|---|---|
| [Wooded Foothills](cards/W/wo.md#wooded-foothills) | 47 | $17.90 |
| [Mountain Valley](cards/M/mou.md#mountain-valley) | 3,123 | $0.22 |
| [Naya Panorama](cards/N/na.md#naya-panorama) | 4,569 | $0.21 |
| [Jund Panorama](cards/J/ju.md#jund-panorama) | 5,252 | $0.39 |

**Budget picks (≤ $1.00):**

| Card | Kind | EDHREC rank | Cheapest USD |
|---|---|---|---|
| [Cinder Glade](cards/C/ci.md#cinder-glade) | tapland | 87 | $0.23 |
| [Rootbound Crag](cards/R/ro.md#rootbound-crag) | check | 128 | $0.26 |
| [Karplusan Forest](cards/K/ka.md#karplusan-forest) | pain | 219 | $0.44 |
| [Rockfall Vale](cards/R/ro.md#rockfall-vale) | slow | 225 | $0.63 |
| [Game Trail](cards/G/ga.md#game-trail) | tapland | 397 | $0.26 |
| [Kessig Wolf Run](cards/K/ke.md#kessig-wolf-run) | other | 406 | $0.35 |

### Selesnya WG

**Most played** (49 lands with this exact identity):

| Card | Kind | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|
| [Temple Garden](cards/T/te.md#temple-garden) | shock | 81 | $6.87 |  |
| [Canopy Vista](cards/C/can.md#canopy-vista) | tapland | 108 | $0.26 |  |
| [Sunpetal Grove](cards/S/sun.md#sunpetal-grove) | check | 132 | $0.32 |  |
| [Bountiful Promenade](cards/B/bo.md#bountiful-promenade) | bond (multiplayer) | 209 | $5.03 |  |
| [Brushland](cards/B/br.md#brushland) | pain | 230 | $0.43 |  |
| [Overgrown Farmland](cards/O/ov.md#overgrown-farmland) | slow | 283 | $0.97 |  |
| [Fortified Village](cards/F/fo.md#fortified-village) | tapland | 344 | $0.20 |  |
| [Sungrass Prairie](cards/S/sun.md#sungrass-prairie) | filter (two-color) | 434 | $0.18 |  |
| [Savannah](cards/S/sav.md#savannah) | original dual | 458 | $198.21 |  |
| [Temple of Plenty](cards/T/te.md#temple-of-plenty) | tapland | 507 | $0.16 |  |
| [Selesnya Sanctuary](cards/S/sel.md#selesnya-sanctuary) | bounce | 585 | $0.19 |  |
| [Hushwood Verge](cards/H/hu.md#hushwood-verge) | other | 674 | $8.07 |  |

**On-color fetches** (colorless identity; can find a land with the Plains or Forest type, so they also find the typed duals above):

| Card | EDHREC rank | Cheapest USD |
|---|---|---|
| [Windswept Heath](cards/W/wi.md#windswept-heath) | 45 | $11.19 |
| [Krosan Verge](cards/K/kr.md#krosan-verge) | 1,008 | $0.20 |
| [Naya Panorama](cards/N/na.md#naya-panorama) | 4,569 | $0.21 |
| [Grasslands](cards/G/gra.md#grasslands) | 5,004 | $0.35 |
| [Bant Panorama](cards/B/ban.md#bant-panorama) | 5,012 | $0.33 |

**Budget picks (≤ $1.00):**

| Card | Kind | EDHREC rank | Cheapest USD |
|---|---|---|---|
| [Canopy Vista](cards/C/can.md#canopy-vista) | tapland | 108 | $0.26 |
| [Sunpetal Grove](cards/S/sun.md#sunpetal-grove) | check | 132 | $0.32 |
| [Brushland](cards/B/br.md#brushland) | pain | 230 | $0.43 |
| [Overgrown Farmland](cards/O/ov.md#overgrown-farmland) | slow | 283 | $0.97 |
| [Fortified Village](cards/F/fo.md#fortified-village) | tapland | 344 | $0.20 |
| [Sungrass Prairie](cards/S/sun.md#sungrass-prairie) | filter (two-color) | 434 | $0.18 |

### Orzhov WB

**Most played** (43 lands with this exact identity):

| Card | Kind | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|
| [Godless Shrine](cards/G/god.md#godless-shrine) | shock | 59 | $8.47 |  |
| [Isolated Chapel](cards/I/is.md#isolated-chapel) | check | 90 | $0.22 |  |
| [Caves of Koilos](cards/C/cav.md#caves-of-koilos) | pain | 124 | $0.33 |  |
| [Vault of Champions](cards/V/va.md#vault-of-champions) | bond (multiplayer) | 169 | $16.22 |  |
| [Shattered Sanctum](cards/S/sha.md#shattered-sanctum) | slow | 261 | $1.62 |  |
| [Temple of Silence](cards/T/te.md#temple-of-silence) | tapland | 308 | $0.22 |  |
| [Fetid Heath](cards/F/fe.md#fetid-heath) | filter | 322 | $0.28 |  |
| [Scrubland](cards/S/sc.md#scrubland) | original dual | 383 | $278.33 |  |
| [Orzhov Basilica](cards/O/or.md#orzhov-basilica) | bounce | 418 | $0.20 |  |
| [Shineshadow Snarl](cards/S/shi.md#shineshadow-snarl) | tapland | 422 | $0.20 |  |
| [Tainted Field](cards/T/ta.md#tainted-field) | other | 451 | $0.33 |  |
| [Vault of the Archangel](cards/V/va.md#vault-of-the-archangel) | other | 468 | $1.03 |  |

**On-color fetches** (colorless identity; can find a land with the Plains or Swamp type, so they also find the typed duals above):

| Card | EDHREC rank | Cheapest USD |
|---|---|---|
| [Marsh Flats](cards/M/mar.md#marsh-flats) | 51 | $31.55 |
| [Esper Panorama](cards/E/es.md#esper-panorama) | 6,292 | $0.28 |

**Budget picks (≤ $1.00):**

| Card | Kind | EDHREC rank | Cheapest USD |
|---|---|---|---|
| [Isolated Chapel](cards/I/is.md#isolated-chapel) | check | 90 | $0.22 |
| [Caves of Koilos](cards/C/cav.md#caves-of-koilos) | pain | 124 | $0.33 |
| [Temple of Silence](cards/T/te.md#temple-of-silence) | tapland | 308 | $0.22 |
| [Fetid Heath](cards/F/fe.md#fetid-heath) | filter | 322 | $0.28 |
| [Orzhov Basilica](cards/O/or.md#orzhov-basilica) | bounce | 418 | $0.20 |
| [Shineshadow Snarl](cards/S/shi.md#shineshadow-snarl) | tapland | 422 | $0.20 |

### Izzet UR

**Most played** (41 lands with this exact identity):

| Card | Kind | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|
| [Steam Vents](cards/S/ste.md#steam-vents) | shock | 62 | $9.81 |  |
| [Sulfur Falls](cards/S/sul.md#sulfur-falls) | check | 76 | $0.21 |  |
| [Shivan Reef](cards/S/shi.md#shivan-reef) | pain | 113 | $0.19 |  |
| [Training Center](cards/T/tra.md#training-center) | bond (multiplayer) | 154 | $18.13 |  |
| [Stormcarved Coast](cards/S/sto.md#stormcarved-coast) | slow | 184 | $2.22 |  |
| [Cascade Bluffs](cards/C/cas.md#cascade-bluffs) | filter | 291 | $0.33 |  |
| [Temple of Epiphany](cards/T/te.md#temple-of-epiphany) | tapland | 295 | $0.18 |  |
| [Frostboil Snarl](cards/F/fr.md#frostboil-snarl) | tapland | 334 | $0.27 |  |
| [Volcanic Island](cards/V/vo.md#volcanic-island) | original dual | 336 | $370.86 |  |
| [Izzet Boilerworks](cards/I/iz.md#izzet-boilerworks) | bounce | 437 | $0.26 |  |
| [Thundering Falls](cards/T/thu.md#thundering-falls) | surveil tapland | 626 | $15.51 |  |
| [Ferrous Lake](cards/F/fe.md#ferrous-lake) | filter (two-color) | 776 | $0.28 |  |

**On-color fetches** (colorless identity; can find a land with the Island or Mountain type, so they also find the typed duals above):

| Card | EDHREC rank | Cheapest USD |
|---|---|---|
| [Scalding Tarn](cards/S/sc.md#scalding-tarn) | 49 | $35.64 |
| [Grixis Panorama](cards/G/gri.md#grixis-panorama) | 6,039 | $0.36 |

**Budget picks (≤ $1.00):**

| Card | Kind | EDHREC rank | Cheapest USD |
|---|---|---|---|
| [Sulfur Falls](cards/S/sul.md#sulfur-falls) | check | 76 | $0.21 |
| [Shivan Reef](cards/S/shi.md#shivan-reef) | pain | 113 | $0.19 |
| [Cascade Bluffs](cards/C/cas.md#cascade-bluffs) | filter | 291 | $0.33 |
| [Temple of Epiphany](cards/T/te.md#temple-of-epiphany) | tapland | 295 | $0.18 |
| [Frostboil Snarl](cards/F/fr.md#frostboil-snarl) | tapland | 334 | $0.27 |
| [Izzet Boilerworks](cards/I/iz.md#izzet-boilerworks) | bounce | 437 | $0.26 |

### Golgari BG

**Most played** (44 lands with this exact identity):

| Card | Kind | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|
| [Overgrown Tomb](cards/O/ov.md#overgrown-tomb) | shock | 71 | $8.14 |  |
| [Woodland Cemetery](cards/W/wo.md#woodland-cemetery) | check | 111 | $0.86 |  |
| [Llanowar Wastes](cards/L/ll.md#llanowar-wastes) | pain | 140 | $0.59 |  |
| [Undergrowth Stadium](cards/U/un.md#undergrowth-stadium) | bond (multiplayer) | 176 | $6.05 |  |
| [Golgari Rot Farm](cards/G/gol.md#golgari-rot-farm) | bounce | 337 | $0.27 |  |
| [Deathcap Glade](cards/D/dea.md#deathcap-glade) | slow | 342 | $2.55 |  |
| [Twilight Mire](cards/T/tw.md#twilight-mire) | filter | 355 | $0.35 |  |
| [Temple of Malady](cards/T/te.md#temple-of-malady) | tapland | 377 | $0.17 |  |
| [Bayou](cards/B/bay.md#bayou) | original dual | 425 | $247.80 |  |
| [Tainted Wood](cards/T/ta.md#tainted-wood) | other | 445 | $0.29 |  |
| [Underground Mortuary](cards/U/un.md#underground-mortuary) | surveil tapland | 482 | $15.55 |  |
| [Necroblossom Snarl](cards/N/ne.md#necroblossom-snarl) | tapland | 537 | $0.34 |  |

**On-color fetches** (colorless identity; can find a land with the Swamp or Forest type, so they also find the typed duals above):

| Card | EDHREC rank | Cheapest USD |
|---|---|---|
| [Verdant Catacombs](cards/V/ve.md#verdant-catacombs) | 48 | $29.78 |
| [Jund Panorama](cards/J/ju.md#jund-panorama) | 5,252 | $0.39 |

**Budget picks (≤ $1.00):**

| Card | Kind | EDHREC rank | Cheapest USD |
|---|---|---|---|
| [Woodland Cemetery](cards/W/wo.md#woodland-cemetery) | check | 111 | $0.86 |
| [Llanowar Wastes](cards/L/ll.md#llanowar-wastes) | pain | 140 | $0.59 |
| [Golgari Rot Farm](cards/G/gol.md#golgari-rot-farm) | bounce | 337 | $0.27 |
| [Twilight Mire](cards/T/tw.md#twilight-mire) | filter | 355 | $0.35 |
| [Temple of Malady](cards/T/te.md#temple-of-malady) | tapland | 377 | $0.17 |
| [Tainted Wood](cards/T/ta.md#tainted-wood) | other | 445 | $0.29 |

### Boros WR

**Most played** (43 lands with this exact identity):

| Card | Kind | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|
| [Sacred Foundry](cards/S/sac.md#sacred-foundry) | shock | 73 | $10.03 |  |
| [Clifftop Retreat](cards/C/cl.md#clifftop-retreat) | check | 78 | $0.22 |  |
| [Battlefield Forge](cards/B/bat.md#battlefield-forge) | pain | 118 | $0.21 |  |
| [Spectator Seating](cards/S/spe.md#spectator-seating) | bond (multiplayer) | 167 | $5.29 |  |
| [Sundown Pass](cards/S/sun.md#sundown-pass) | slow | 259 | $2.51 |  |
| [Rugged Prairie](cards/R/ru.md#rugged-prairie) | filter | 281 | $0.26 |  |
| [Temple of Triumph](cards/T/te.md#temple-of-triumph) | tapland | 317 | $0.17 |  |
| [Furycalm Snarl](cards/F/fu.md#furycalm-snarl) | tapland | 343 | $0.22 |  |
| [Plateau](cards/P/pl.md#plateau) | original dual | 441 | $225.00 |  |
| [Boros Garrison](cards/B/bo.md#boros-garrison) | bounce | 512 | $0.19 |  |
| [Elegant Parlor](cards/E/el.md#elegant-parlor) | surveil tapland | 771 | $9.40 |  |
| [Sunbillow Verge](cards/S/sun.md#sunbillow-verge) | other | 801 | $11.16 |  |

**On-color fetches** (colorless identity; can find a land with the Plains or Mountain type, so they also find the typed duals above):

| Card | EDHREC rank | Cheapest USD |
|---|---|---|
| [Arid Mesa](cards/A/ari.md#arid-mesa) | 55 | $29.27 |
| [Naya Panorama](cards/N/na.md#naya-panorama) | 4,569 | $0.21 |

**Budget picks (≤ $1.00):**

| Card | Kind | EDHREC rank | Cheapest USD |
|---|---|---|---|
| [Clifftop Retreat](cards/C/cl.md#clifftop-retreat) | check | 78 | $0.22 |
| [Battlefield Forge](cards/B/bat.md#battlefield-forge) | pain | 118 | $0.21 |
| [Rugged Prairie](cards/R/ru.md#rugged-prairie) | filter | 281 | $0.26 |
| [Temple of Triumph](cards/T/te.md#temple-of-triumph) | tapland | 317 | $0.17 |
| [Furycalm Snarl](cards/F/fu.md#furycalm-snarl) | tapland | 343 | $0.22 |
| [Boros Garrison](cards/B/bo.md#boros-garrison) | bounce | 512 | $0.19 |

### Simic UG

**Most played** (43 lands with this exact identity):

| Card | Kind | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|
| [Breeding Pool](cards/B/br.md#breeding-pool) | shock | 60 | $9.16 |  |
| [Hinterland Harbor](cards/H/hi.md#hinterland-harbor) | check | 97 | $0.25 |  |
| [Yavimaya Coast](cards/Y/ya.md#yavimaya-coast) | pain | 137 | $0.35 |  |
| [Rejuvenating Springs](cards/R/rej.md#rejuvenating-springs) | bond (multiplayer) | 147 | $3.98 |  |
| [Dreamroot Cascade](cards/D/dre.md#dreamroot-cascade) | slow | 174 | $0.84 |  |
| [Flooded Grove](cards/F/fl.md#flooded-grove) | filter | 303 | $0.26 |  |
| [Simic Growth Chamber](cards/S/si.md#simic-growth-chamber) | bounce | 319 | $0.23 |  |
| [Temple of Mystery](cards/T/te.md#temple-of-mystery) | tapland | 335 | $0.15 |  |
| [Tropical Island](cards/T/tro.md#tropical-island) | original dual | 352 | $250.00 |  |
| [Vineglimmer Snarl](cards/V/vi.md#vineglimmer-snarl) | tapland | 547 | $0.19 |  |
| [Hedge Maze](cards/H/he.md#hedge-maze) | surveil tapland | 558 | $13.53 |  |
| [Overflowing Basin](cards/O/ov.md#overflowing-basin) | filter (two-color) | 725 | $0.19 |  |

**On-color fetches** (colorless identity; can find a land with the Island or Forest type, so they also find the typed duals above):

| Card | EDHREC rank | Cheapest USD |
|---|---|---|
| [Misty Rainforest](cards/M/mis.md#misty-rainforest) | 42 | $36.99 |
| [Bant Panorama](cards/B/ban.md#bant-panorama) | 5,012 | $0.33 |

**Budget picks (≤ $1.00):**

| Card | Kind | EDHREC rank | Cheapest USD |
|---|---|---|---|
| [Hinterland Harbor](cards/H/hi.md#hinterland-harbor) | check | 97 | $0.25 |
| [Yavimaya Coast](cards/Y/ya.md#yavimaya-coast) | pain | 137 | $0.35 |
| [Dreamroot Cascade](cards/D/dre.md#dreamroot-cascade) | slow | 174 | $0.84 |
| [Flooded Grove](cards/F/fl.md#flooded-grove) | filter | 303 | $0.26 |
| [Simic Growth Chamber](cards/S/si.md#simic-growth-chamber) | bounce | 319 | $0.23 |
| [Temple of Mystery](cards/T/te.md#temple-of-mystery) | tapland | 335 | $0.15 |

### Bant WUG

Pair sections to combine: [Azorius (WU)](#azorius-wu) · [Selesnya (WG)](#selesnya-wg) · [Simic (UG)](#simic-ug)

**Most played** (7 lands with this exact identity):

| Card | Kind | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|
| [Spara's Headquarters](cards/S/spa.md#sparas-headquarters) | cycling tapland | 398 | $13.41 |  |
| [Seaside Citadel](cards/S/sea.md#seaside-citadel) | tapland | 411 | $0.24 |  |
| [Tranquil Landscape](cards/T/tra.md#tranquil-landscape) | other | 2,152 | $0.17 |  |
| [Urban Retreat](cards/U/ur.md#urban-retreat) | tapland | 4,707 | $0.59 |  |
| [Treva's Ruins](cards/T/tre.md#trevas-ruins) | other | 10,530 | $0.29 |  |
| [Irrigation Ditch](cards/I/ir.md#irrigation-ditch) | tapland | 23,649 | $0.21 |  |
| [Aysen Abbey](cards/A/ay.md#aysen-abbey) | other | 27,648 | $0.32 |  |

**Budget picks (≤ $1.00):**

| Card | Kind | EDHREC rank | Cheapest USD |
|---|---|---|---|
| [Seaside Citadel](cards/S/sea.md#seaside-citadel) | tapland | 411 | $0.24 |
| [Tranquil Landscape](cards/T/tra.md#tranquil-landscape) | other | 2,152 | $0.17 |
| [Urban Retreat](cards/U/ur.md#urban-retreat) | tapland | 4,707 | $0.59 |
| [Treva's Ruins](cards/T/tre.md#trevas-ruins) | other | 10,530 | $0.29 |
| [Irrigation Ditch](cards/I/ir.md#irrigation-ditch) | tapland | 23,649 | $0.21 |
| [Aysen Abbey](cards/A/ay.md#aysen-abbey) | other | 27,648 | $0.32 |

### Esper WUB

Pair sections to combine: [Azorius (WU)](#azorius-wu) · [Dimir (UB)](#dimir-ub) · [Orzhov (WB)](#orzhov-wb)

**Most played** (6 lands with this exact identity):

| Card | Kind | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|
| [Arcane Sanctum](cards/A/arc.md#arcane-sanctum) | tapland | 351 | $0.30 |  |
| [Raffine's Tower](cards/R/raf.md#raffines-tower) | cycling tapland | 419 | $13.15 |  |
| [Contaminated Landscape](cards/C/con.md#contaminated-landscape) | other | 2,176 | $0.16 |  |
| [Dromar's Cavern](cards/D/dro.md#dromars-cavern) | other | 9,392 | $0.20 |  |
| [Ancient Spring](cards/A/an.md#ancient-spring) | tapland | 20,805 | $0.21 |  |
| [Wizards' School](cards/W/wi.md#wizards-school) | other | 27,488 | $0.34 |  |

**Budget picks (≤ $1.00):**

| Card | Kind | EDHREC rank | Cheapest USD |
|---|---|---|---|
| [Arcane Sanctum](cards/A/arc.md#arcane-sanctum) | tapland | 351 | $0.30 |
| [Contaminated Landscape](cards/C/con.md#contaminated-landscape) | other | 2,176 | $0.16 |
| [Dromar's Cavern](cards/D/dro.md#dromars-cavern) | other | 9,392 | $0.20 |
| [Ancient Spring](cards/A/an.md#ancient-spring) | tapland | 20,805 | $0.21 |
| [Wizards' School](cards/W/wi.md#wizards-school) | other | 27,488 | $0.34 |

### Grixis UBR

Pair sections to combine: [Dimir (UB)](#dimir-ub) · [Rakdos (BR)](#rakdos-br) · [Izzet (UR)](#izzet-ur)

**Most played** (8 lands with this exact identity):

| Card | Kind | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|
| [Crumbling Necropolis](cards/C/cr.md#crumbling-necropolis) | tapland | 368 | $0.34 |  |
| [Xander's Lounge](cards/X/xa.md#xanders-lounge) | cycling tapland | 472 | $14.18 |  |
| [Seething Landscape](cards/S/see.md#seething-landscape) | other | 1,984 | $0.19 |  |
| [Oscorp Industries](cards/O/os.md#oscorp-industries) | tapland | 3,487 | $0.86 |  |
| [Crosis's Catacombs](cards/C/cr.md#crosiss-catacombs) | other | 9,236 | $0.27 |  |
| [Crypt of the Eternals](cards/C/cr.md#crypt-of-the-eternals) | other | 11,283 | $0.19 |  |
| [Sulfur Vent](cards/S/sul.md#sulfur-vent) | tapland | 21,932 | $0.28 |  |
| [Castle Sengir](cards/C/cas.md#castle-sengir) | other | 26,741 | $0.28 |  |

**Budget picks (≤ $1.00):**

| Card | Kind | EDHREC rank | Cheapest USD |
|---|---|---|---|
| [Crumbling Necropolis](cards/C/cr.md#crumbling-necropolis) | tapland | 368 | $0.34 |
| [Seething Landscape](cards/S/see.md#seething-landscape) | other | 1,984 | $0.19 |
| [Oscorp Industries](cards/O/os.md#oscorp-industries) | tapland | 3,487 | $0.86 |
| [Crosis's Catacombs](cards/C/cr.md#crosiss-catacombs) | other | 9,236 | $0.27 |
| [Crypt of the Eternals](cards/C/cr.md#crypt-of-the-eternals) | other | 11,283 | $0.19 |
| [Sulfur Vent](cards/S/sul.md#sulfur-vent) | tapland | 21,932 | $0.28 |

### Jund BRG

Pair sections to combine: [Rakdos (BR)](#rakdos-br) · [Gruul (RG)](#gruul-rg) · [Golgari (BG)](#golgari-bg)

**Most played** (6 lands with this exact identity):

| Card | Kind | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|
| [Ziatora's Proving Ground](cards/Z/zi.md#ziatoras-proving-ground) | cycling tapland | 536 | $9.14 |  |
| [Savage Lands](cards/S/sav.md#savage-lands) | tapland | 647 | $0.30 |  |
| [Twisted Landscape](cards/T/tw.md#twisted-landscape) | other | 1,902 | $0.24 |  |
| [Darigaaz's Caldera](cards/D/da.md#darigaazs-caldera) | other | 11,097 | $0.27 |  |
| [Geothermal Crevice](cards/G/ge.md#geothermal-crevice) | tapland | 21,453 | $0.25 |  |
| [Koskun Keep](cards/K/ko.md#koskun-keep) | other | 28,992 | $0.25 |  |

**Budget picks (≤ $1.00):**

| Card | Kind | EDHREC rank | Cheapest USD |
|---|---|---|---|
| [Savage Lands](cards/S/sav.md#savage-lands) | tapland | 647 | $0.30 |
| [Twisted Landscape](cards/T/tw.md#twisted-landscape) | other | 1,902 | $0.24 |
| [Darigaaz's Caldera](cards/D/da.md#darigaazs-caldera) | other | 11,097 | $0.27 |
| [Geothermal Crevice](cards/G/ge.md#geothermal-crevice) | tapland | 21,453 | $0.25 |
| [Koskun Keep](cards/K/ko.md#koskun-keep) | other | 28,992 | $0.25 |

### Naya WRG

Pair sections to combine: [Gruul (RG)](#gruul-rg) · [Selesnya (WG)](#selesnya-wg) · [Boros (WR)](#boros-wr)

**Most played** (6 lands with this exact identity):

| Card | Kind | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|
| [Jungle Shrine](cards/J/ju.md#jungle-shrine) | tapland | 324 | $0.26 |  |
| [Jetmir's Garden](cards/J/je.md#jetmirs-garden) | cycling tapland | 367 | $15.26 |  |
| [Sheltering Landscape](cards/S/she.md#sheltering-landscape) | other | 2,342 | $0.32 |  |
| [Rith's Grove](cards/R/ri.md#riths-grove) | other | 9,497 | $0.27 |  |
| [Tinder Farm](cards/T/ti.md#tinder-farm) | tapland | 21,843 | $0.18 |  |
| [An-Havva Township](cards/A/an.md#an-havva-township) | other | 27,430 | $0.30 |  |

**Budget picks (≤ $1.00):**

| Card | Kind | EDHREC rank | Cheapest USD |
|---|---|---|---|
| [Jungle Shrine](cards/J/ju.md#jungle-shrine) | tapland | 324 | $0.26 |
| [Sheltering Landscape](cards/S/she.md#sheltering-landscape) | other | 2,342 | $0.32 |
| [Rith's Grove](cards/R/ri.md#riths-grove) | other | 9,497 | $0.27 |
| [Tinder Farm](cards/T/ti.md#tinder-farm) | tapland | 21,843 | $0.18 |
| [An-Havva Township](cards/A/an.md#an-havva-township) | other | 27,430 | $0.30 |

### Abzan WBG

Pair sections to combine: [Selesnya (WG)](#selesnya-wg) · [Orzhov (WB)](#orzhov-wb) · [Golgari (BG)](#golgari-bg)

**Most played** (4 lands with this exact identity):

| Card | Kind | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|
| [Indatha Triome](cards/I/ind.md#indatha-triome) | cycling tapland | 480 | $17.09 |  |
| [Sandsteppe Citadel](cards/S/san.md#sandsteppe-citadel) | tapland | 510 | $0.28 |  |
| [Deceptive Landscape](cards/D/dec.md#deceptive-landscape) | other | 2,271 | $0.18 |  |
| [Murmuring Bosk](cards/M/mu.md#murmuring-bosk) | pain | 2,717 | $0.36 |  |

**Budget picks (≤ $1.00):**

| Card | Kind | EDHREC rank | Cheapest USD |
|---|---|---|---|
| [Sandsteppe Citadel](cards/S/san.md#sandsteppe-citadel) | tapland | 510 | $0.28 |
| [Deceptive Landscape](cards/D/dec.md#deceptive-landscape) | other | 2,271 | $0.18 |
| [Murmuring Bosk](cards/M/mu.md#murmuring-bosk) | pain | 2,717 | $0.36 |

### Jeskai WUR

Pair sections to combine: [Azorius (WU)](#azorius-wu) · [Izzet (UR)](#izzet-ur) · [Boros (WR)](#boros-wr)

**Most played** (3 lands with this exact identity):

| Card | Kind | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|
| [Mystic Monastery](cards/M/my.md#mystic-monastery) | tapland | 373 | $0.13 |  |
| [Raugrin Triome](cards/R/rau.md#raugrin-triome) | cycling tapland | 477 | $15.52 |  |
| [Perilous Landscape](cards/P/pe.md#perilous-landscape) | other | 1,992 | $0.19 |  |

**Budget picks (≤ $1.00):**

| Card | Kind | EDHREC rank | Cheapest USD |
|---|---|---|---|
| [Mystic Monastery](cards/M/my.md#mystic-monastery) | tapland | 373 | $0.13 |
| [Perilous Landscape](cards/P/pe.md#perilous-landscape) | other | 1,992 | $0.19 |

### Sultai UBG

Pair sections to combine: [Dimir (UB)](#dimir-ub) · [Golgari (BG)](#golgari-bg) · [Simic (UG)](#simic-ug)

**Most played** (3 lands with this exact identity):

| Card | Kind | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|
| [Opulent Palace](cards/O/op.md#opulent-palace) | tapland | 385 | $0.24 |  |
| [Zagoth Triome](cards/Z/za.md#zagoth-triome) | cycling tapland | 400 | $21.14 |  |
| [Foreboding Landscape](cards/F/fo.md#foreboding-landscape) | other | 1,699 | $0.23 |  |

**Budget picks (≤ $1.00):**

| Card | Kind | EDHREC rank | Cheapest USD |
|---|---|---|---|
| [Opulent Palace](cards/O/op.md#opulent-palace) | tapland | 385 | $0.24 |
| [Foreboding Landscape](cards/F/fo.md#foreboding-landscape) | other | 1,699 | $0.23 |

### Mardu WBR

Pair sections to combine: [Rakdos (BR)](#rakdos-br) · [Orzhov (WB)](#orzhov-wb) · [Boros (WR)](#boros-wr)

**Most played** (4 lands with this exact identity):

| Card | Kind | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|
| [Nomad Outpost](cards/N/no.md#nomad-outpost) | tapland | 381 | $0.23 |  |
| [Savai Triome](cards/S/sav.md#savai-triome) | cycling tapland | 495 | $18.35 |  |
| [Shattered Landscape](cards/S/sha.md#shattered-landscape) | other | 1,962 | $0.17 |  |
| [Tournament Grounds](cards/T/to.md#tournament-grounds) | other | 11,954 | $0.29 |  |

**Budget picks (≤ $1.00):**

| Card | Kind | EDHREC rank | Cheapest USD |
|---|---|---|---|
| [Nomad Outpost](cards/N/no.md#nomad-outpost) | tapland | 381 | $0.23 |
| [Shattered Landscape](cards/S/sha.md#shattered-landscape) | other | 1,962 | $0.17 |
| [Tournament Grounds](cards/T/to.md#tournament-grounds) | other | 11,954 | $0.29 |

### Temur URG

Pair sections to combine: [Gruul (RG)](#gruul-rg) · [Izzet (UR)](#izzet-ur) · [Simic (UG)](#simic-ug)

**Most played** (3 lands with this exact identity):

| Card | Kind | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|
| [Ketria Triome](cards/K/ke.md#ketria-triome) | cycling tapland | 359 | $16.61 |  |
| [Frontier Bivouac](cards/F/fr.md#frontier-bivouac) | tapland | 401 | $0.24 |  |
| [Bountiful Landscape](cards/B/bo.md#bountiful-landscape) | other | 1,756 | $0.18 |  |

**Budget picks (≤ $1.00):**

| Card | Kind | EDHREC rank | Cheapest USD |
|---|---|---|---|
| [Frontier Bivouac](cards/F/fr.md#frontier-bivouac) | tapland | 401 | $0.24 |
| [Bountiful Landscape](cards/B/bo.md#bountiful-landscape) | other | 1,756 | $0.18 |

### Glint (non-W) UBRG

Pair sections to combine: [Dimir (UB)](#dimir-ub) · [Rakdos (BR)](#rakdos-br) · [Gruul (RG)](#gruul-rg) · [Izzet (UR)](#izzet-ur) · [Golgari (BG)](#golgari-bg) · [Simic (UG)](#simic-ug)

No non-basic lands have exactly this identity; build from the subsets and the universal fixers.

### Dune (non-U) WBRG

Pair sections to combine: [Rakdos (BR)](#rakdos-br) · [Gruul (RG)](#gruul-rg) · [Selesnya (WG)](#selesnya-wg) · [Orzhov (WB)](#orzhov-wb) · [Golgari (BG)](#golgari-bg) · [Boros (WR)](#boros-wr)

No non-basic lands have exactly this identity; build from the subsets and the universal fixers.

### Ink (non-B) WURG

Pair sections to combine: [Azorius (WU)](#azorius-wu) · [Gruul (RG)](#gruul-rg) · [Selesnya (WG)](#selesnya-wg) · [Izzet (UR)](#izzet-ur) · [Boros (WR)](#boros-wr) · [Simic (UG)](#simic-ug)

No non-basic lands have exactly this identity; build from the subsets and the universal fixers.

### Witch (non-R) WUBG

Pair sections to combine: [Azorius (WU)](#azorius-wu) · [Dimir (UB)](#dimir-ub) · [Selesnya (WG)](#selesnya-wg) · [Orzhov (WB)](#orzhov-wb) · [Golgari (BG)](#golgari-bg) · [Simic (UG)](#simic-ug)

No non-basic lands have exactly this identity; build from the subsets and the universal fixers.

### Yore (non-G) WUBR

Pair sections to combine: [Azorius (WU)](#azorius-wu) · [Dimir (UB)](#dimir-ub) · [Rakdos (BR)](#rakdos-br) · [Orzhov (WB)](#orzhov-wb) · [Izzet (UR)](#izzet-ur) · [Boros (WR)](#boros-wr)

No non-basic lands have exactly this identity; build from the subsets and the universal fixers.

### Five-color WUBRG

Pair sections to combine: [Azorius (WU)](#azorius-wu) · [Dimir (UB)](#dimir-ub) · [Rakdos (BR)](#rakdos-br) · [Gruul (RG)](#gruul-rg) · [Selesnya (WG)](#selesnya-wg) · [Orzhov (WB)](#orzhov-wb) · [Izzet (UR)](#izzet-ur) · [Golgari (BG)](#golgari-bg) · [Boros (WR)](#boros-wr) · [Simic (UG)](#simic-ug)

**Most played** (2 lands with this exact identity):

| Card | Kind | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|
| [The World Tree](cards/T/thew.md#the-world-tree) | tapland | 818 | $7.64 |  |
| [Crystal Quarry](cards/C/cr.md#crystal-quarry) | other | 5,958 | $0.82 |  |

**Budget picks (≤ $1.00):**

| Card | Kind | EDHREC rank | Cheapest USD |
|---|---|---|---|
| [Crystal Quarry](cards/C/cr.md#crystal-quarry) | other | 5,958 | $0.82 |

## Method

- Pool: Commander-legal cards in this repo's card index (Scryfall Oracle bulk). Basics are excluded from the tables.
- *Kind* patterns (first match wins): fetch: `Pay 1 life, Sacrifice this land: Search your library for an? .* card`; shock: `you may pay 2 life\. If you don't, it enters tapped`; fast: `enters tapped unless you control two or fewer other lands`; slow: `enters tapped unless you control two or more other lands`; check: `enters tapped unless you control an? (Plains|Island|Swamp|Mountain|Forest)`; bond (multiplayer): `enters tapped unless you have two or more opponents`; pain: `deals 1 damage to you`; filter (two-color): `\{1\}, \{T\}: Add \{[WUBRG]\}\{[WUBRG]\}`; bounce: `return a land you control to its owner's hand`; horizon: `\{T\}, Pay 1 life: Add`; filter: `\{[WUBRG]/[WUBRG]\}, \{T\}: Add`; cycling tapland: `enters tapped.*Cycling|Cycling.*enters tapped`; surveil tapland: `enters tapped.*[Ss]urveil 1`; tapland: `enters tapped`. "original dual" means the Oracle text is only the mana reminder text.
- Cheapest USD comes from Scryfall `default_cards` bulk (2026-10-15): the lowest `usd` or `usd_foil` among paper printings.
- Related: [EDH Staples](EDH%20Staples.md) · [EDH Packages](EDH%20Packages.md) · [EDH Standards](EDH%20Standards.md).
