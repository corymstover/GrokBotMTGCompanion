---
title: "EDH Packages"
category: edh
tags: [packages, ramp, card-advantage]
issues: [26, 102]
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

Used in decks (≥ 3 matching cards, 91): [Nicol Bolas (Grixis)](grixis/decks/nicol-bolas.md) 13 · [Mairsil, the Pretender (Grixis)](grixis/decks/mairsil-the-pretender.md) 12 · [Mishra, Artificer Prodigy (Grixis)](grixis/decks/mishra-artificer-prodigy.md) 12 · [Nicol Bolas, the Ravager // Nicol Bolas, the Arisen (Grixis)](grixis/decks/nicol-bolas-the-ravager.md) 12 · [Crosis, the Purger (Grixis)](grixis/decks/crosis-the-purger.md) 11 · [Garza Zol, Plague Queen (Grixis)](grixis/decks/garza-zol-plague-queen.md) 11 · [Kykar, Wind's Fury](decks/kykar-winds-fury.md) 10 · [Nekusar, the Mindrazer](decks/nekusar-the-mindrazer.md) 10 · [Fire Lord Azula (Grixis)](grixis/decks/fire-lord-azula.md) 10 · [Kess, Dissident Mage (Grixis)](grixis/decks/kess-dissident-mage.md) 10 · [Norman Osborn // Green Goblin (Grixis)](grixis/decks/norman-osborn.md) 10 · [Sedris, the Traitor King (Grixis)](grixis/decks/sedris-the-traitor-king.md) 10 · …79 more

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 1): [Thaumatic Compass // Spires of Orazca](cards/T/tha.md#thaumatic-compass--spires-of-orazca)

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

Used in decks (≥ 3 matching cards, 5): [Tatyova, Benthic Druid](decks/tatyova-benthic-druid.md) 7 · [Gishath, Sun's Avatar](decks/gishath-suns-avatar.md) 5 · [Korvold, Fae-Cursed King](decks/korvold-fae-cursed-king.md) 3 · [Ghalta, Primal Hunger (Ixalan-only)](decks/plane-ixalan-ghalta-primal-hunger.md) 3 · [Omnath, Locus of Rage (Zendikar-only)](decks/plane-zendikar-omnath-locus-of-rage.md) 3

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 13): [Burnished Hart](cards/B/bu.md#burnished-hart) · [Dawntreader Elk](cards/D/da.md#dawntreader-elk) · [Font of Fertility](cards/F/fo.md#font-of-fertility) · [Gladiolus Amicitia](cards/G/gl.md#gladiolus-amicitia) · [Harrow](cards/H/ha.md#harrow) · [Hour of Promise](cards/H/ho.md#hour-of-promise) · [Khalni Heart Expedition](cards/K/kh.md#khalni-heart-expedition) · [Kodama of the West Tree](cards/K/ko.md#kodama-of-the-west-tree) · [Peregrination](cards/P/pe.md#peregrination) · [Sami's Curiosity](cards/S/sam.md#samis-curiosity) · [Spider-Man, Brooklyn Visionary](cards/S/spi.md#spider-man-brooklyn-visionary) · [Sutina, Speaker of the Tajuru](cards/S/sut.md#sutina-speaker-of-the-tajuru) · [Sword of the Animist](cards/S/sw.md#sword-of-the-animist)

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

Used in decks (≥ 3 matching cards, 13): [Chulane, Teller of Tales](decks/chulane-teller-of-tales.md) 8 · [Animar, Soul of Elements](decks/animar-soul-of-elements.md) 7 · [Selvala, Heart of the Wilds](decks/selvala-heart-of-the-wilds.md) 7 · [Chulane, Teller of Tales (landfall theme)](decks/theme-chulane-teller-of-tales-landfall.md) 6 · [Xenagos, God of Revels](decks/xenagos-god-of-revels.md) 6 · [Karador, Ghost Chieftain](decks/karador-ghost-chieftain.md) 5 · [Lathril, Blade of the Elves](decks/lathril-blade-of-the-elves.md) 5 · [Trostani, Selesnya's Voice](decks/trostani-selesnyas-voice.md) 5 · [Ghalta, Primal Hunger (Ixalan-only)](decks/plane-ixalan-ghalta-primal-hunger.md) 4 · [Saskia the Unyielding](decks/saskia-the-unyielding.md) 4 · [Korvold, Fae-Cursed King](decks/korvold-fae-cursed-king.md) 3 · [Muldrotha, the Gravetide](decks/muldrotha-the-gravetide.md) 3 · …1 more

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 13): [Bugenhagen, Wise Elder](cards/B/bu.md#bugenhagen-wise-elder) · [Freya Crescent](cards/F/fr.md#freya-crescent) · [Giada, Font of Hope](cards/G/gi.md#giada-font-of-hope) · [Jenson Carthalion, Druid Exile](cards/J/je.md#jenson-carthalion-druid-exile) · [Katilda, Dawnhart Prime](cards/K/ka.md#katilda-dawnhart-prime) · [Radha, Heir to Keld](cards/R/rad.md#radha-heir-to-keld) · [Rattleclaw Mystic](cards/R/rat.md#rattleclaw-mystic) · [Redshift, Rocketeer Chief](cards/R/red.md#redshift-rocketeer-chief) · [Ruby, Daring Tracker](cards/R/ru.md#ruby-daring-tracker) · [Shang-Chi, Master of Kung Fu](cards/S/sha.md#shang-chi-master-of-kung-fu) · [The Emperor of Palamecia // The Lord Master of Hell](cards/T/thee.md#the-emperor-of-palamecia--the-lord-master-of-hell) · [Torgal, A Fine Hound](cards/T/to.md#torgal-a-fine-hound) · [Whisperer of the Wilds](cards/W/wh.md#whisperer-of-the-wilds)

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

Used in decks (≥ 3 matching cards, 17): [Giada, Font of Hope](decks/giada-font-of-hope.md) 6 · [Gishath, Sun's Avatar](decks/gishath-suns-avatar.md) 6 · [The Ur-Dragon](decks/the-ur-dragon.md) 6 · [Talrand, Sky Summoner](decks/talrand-sky-summoner.md) 5 · [Mishra, Artificer Prodigy (Grixis)](grixis/decks/mishra-artificer-prodigy.md) 5 · [Breya, Etherium Shaper](decks/breya-etherium-shaper.md) 4 · [Ashad, the Lone Cyberman (Grixis)](grixis/decks/ashad-the-lone-cyberman.md) 4 · [Be'lakor, the Dark Master (Grixis)](grixis/decks/belakor-the-dark-master.md) 4 · [Loki, the Deceiver (Grixis)](grixis/decks/loki-the-deceiver.md) 4 · [Mai and Zuko (Grixis)](grixis/decks/mai-and-zuko.md) 4 · [Parnesse, the Subtle Brush (Grixis)](grixis/decks/parnesse-the-subtle-brush.md) 4 · [Kozilek, the Great Distortion](decks/kozilek-the-great-distortion.md) 3 · …5 more

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 53): [Animar, Soul of Elements](cards/A/an.md#animar-soul-of-elements) · [Baral, Chief of Compliance](cards/B/bar.md#baral-chief-of-compliance) · [Baron Strucker, HYDRA Overlord](cards/B/bar.md#baron-strucker-hydra-overlord) · [Bilbo, Thief in the Night](cards/B/bi.md#bilbo-thief-in-the-night) · [Bontu's Monument](cards/B/bo.md#bontus-monument) · [Cid, Freeflier Pilot](cards/C/ci.md#cid-freeflier-pilot) · [Danitha Capashen, Paragon](cards/D/da.md#danitha-capashen-paragon) · [Doc Aurlock, Grizzled Genius](cards/D/do.md#doc-aurlock-grizzled-genius) · [Emet-Selch of the Third Seat](cards/E/em.md#emet-selch-of-the-third-seat) · [Gargos, Vicious Watcher](cards/G/ga.md#gargos-vicious-watcher) · [Geist of Saint Thalia](cards/G/ge.md#geist-of-saint-thalia) · [Gonti, Canny Acquisitor](cards/G/gon.md#gonti-canny-acquisitor) · [Goreclaw, Terror of Qal Sisma](cards/G/gor.md#goreclaw-terror-of-qal-sisma) · [Gran-Gran](cards/G/gra.md#gran-gran) · [Grand Arbiter Augustin IV](cards/G/gra.md#grand-arbiter-augustin-iv) · [Hazoret's Monument](cards/H/ha.md#hazorets-monument) · [Heliod, the Radiant Dawn // Heliod, the Warped Eclipse](cards/H/he.md#heliod-the-radiant-dawn--heliod-the-warped-eclipse) · [Honest Rutstein](cards/H/ho.md#honest-rutstein) · [Jace's Sanctum](cards/J/ja.md#jaces-sanctum) · [Jhoira's Familiar](cards/J/jh.md#jhoiras-familiar) · [Kethis, the Hidden Hand](cards/K/ke.md#kethis-the-hidden-hand) · [Killian, Ink Duelist](cards/K/ki.md#killian-ink-duelist) · [Longshot, Rebel Bowman](cards/L/lo.md#longshot-rebel-bowman) · [Lyse Hext](cards/L/ly.md#lyse-hext) · [Magnus the Red](cards/M/mag.md#magnus-the-red) · [Mizzix of the Izmagnus](cards/M/miz.md#mizzix-of-the-izmagnus) · [Nogi, Draco-Zealot](cards/N/no.md#nogi-draco-zealot) · [Norman Osborn // Green Goblin](cards/N/no.md#norman-osborn--green-goblin) · [Nylea, Keen-Eyed](cards/N/ny.md#nylea-keen-eyed) · [Oath of Ajani](cards/O/oa.md#oath-of-ajani) · [Pearl-Ear, Imperial Advisor](cards/P/pe.md#pearl-ear-imperial-advisor) · [Rakdos, Lord of Riots](cards/R/rak.md#rakdos-lord-of-riots) · [Ral, Monsoon Mage // Ral, Leyline Prodigy](cards/R/ral.md#ral-monsoon-mage--ral-leyline-prodigy) · [Rowan, Scholar of Sparks // Will, Scholar of Frost](cards/R/ro.md#rowan-scholar-of-sparks--will-scholar-of-frost) · [Saheeli, Filigree Master](cards/S/sah.md#saheeli-filigree-master) · [Sami, Wildcat Captain](cards/S/sam.md#sami-wildcat-captain) · [Sarkhan, Soul Aflame](cards/S/sar.md#sarkhan-soul-aflame) · [Shuri, Wakandan Inventor](cards/S/shu.md#shuri-wakandan-inventor) · [Stenn, Paranoid Partisan](cards/S/ste.md#stenn-paranoid-partisan) · [Tam, the Possibility](cards/T/ta.md#tam-the-possibility) · [Tamiyo, Compleated Sage](cards/T/ta.md#tamiyo-compleated-sage) · [Tezzeret, Master of the Bridge](cards/T/te.md#tezzeret-master-of-the-bridge) · [The Immortal Sun](cards/T/thei.md#the-immortal-sun) · [The Ur-Dragon](cards/T/theu.md#the-ur-dragon) · [Thryx, the Sudden Storm](cards/T/thr.md#thryx-the-sudden-storm) · [Tombstone, Career Criminal](cards/T/to.md#tombstone-career-criminal) · [Ugin, the Ineffable](cards/U/ug.md#ugin-the-ineffable) · [Uncle Iroh](cards/U/un.md#uncle-iroh) · [Unesh, Criosphinx Sovereign](cards/U/un.md#unesh-criosphinx-sovereign) · [Urianger Augurelt](cards/U/ur.md#urianger-augurelt) · [Urza, Lord Protector](cards/U/ur.md#urza-lord-protector) · [Urza, Planeswalker](cards/U/ur.md#urza-planeswalker) · [Will Kenrith](cards/W/wi.md#will-kenrith)

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

Used in decks (≥ 3 matching cards, 66): [Niv-Mizzet, Parun](decks/niv-mizzet-parun.md) 10 · [Kynaios and Tiro of Meletis](decks/kynaios-and-tiro-of-meletis.md) 8 · [Saskia the Unyielding](decks/saskia-the-unyielding.md) 8 · [Talrand, Sky Summoner](decks/talrand-sky-summoner.md) 8 · [Chulane, Teller of Tales (landfall theme)](decks/theme-chulane-teller-of-tales-landfall.md) 8 · [Goro-Goro and Satoru (Grixis)](grixis/decks/goro-goro-and-satoru.md) 8 · [The Rani (Grixis)](grixis/decks/the-rani.md) 8 · [Animar, Soul of Elements](decks/animar-soul-of-elements.md) 7 · [Chulane, Teller of Tales](decks/chulane-teller-of-tales.md) 7 · [Muldrotha, the Gravetide](decks/muldrotha-the-gravetide.md) 7 · [Xenagos, God of Revels](decks/xenagos-god-of-revels.md) 7 · [Uro, Titan of Nature's Wrath (Theros-only)](decks/plane-theros-uro-titan-of-natures-wrath.md) 6 · …54 more

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 199): [Aesi, Tyrant of Gyre Strait](cards/A/ae.md#aesi-tyrant-of-gyre-strait) · [Agent Venom](cards/A/ag.md#agent-venom) · [Akiri, Fearless Voyager](cards/A/ak.md#akiri-fearless-voyager) · [Alania, Divergent Storm](cards/A/al.md#alania-divergent-storm) · [Alphinaud Leveilleur](cards/A/al.md#alphinaud-leveilleur) · [Altanak, the Thrice-Called](cards/A/al.md#altanak-the-thrice-called) · [Arcades, the Strategist](cards/A/arc.md#arcades-the-strategist) · [Ashling, Flame Dancer](cards/A/as.md#ashling-flame-dancer) · [Auntie Ool, Cursewretch](cards/A/au.md#auntie-ool-cursewretch) · [Aurelia, the Law Above](cards/A/au.md#aurelia-the-law-above) · [Avatar Aang // Aang, Master of Elements](cards/A/av.md#avatar-aang--aang-master-of-elements) · [Baral, Chief of Compliance](cards/B/bar.md#baral-chief-of-compliance) · [Barrin, Tolarian Archmage](cards/B/bar.md#barrin-tolarian-archmage) · [Basim Ibn Ishaq](cards/B/bas.md#basim-ibn-ishaq) · [Baxter, Fly in the Ointment](cards/B/bax.md#baxter-fly-in-the-ointment) · [Bello, Bard of the Brambles](cards/B/be.md#bello-bard-of-the-brambles) · [Bennie Bracks, Zoologist](cards/B/be.md#bennie-bracks-zoologist) · [Betor, Kin to All](cards/B/be.md#betor-kin-to-all) · [Bident of Thassa](cards/B/bi.md#bident-of-thassa) · [Black Widow, Agile Avenger](cards/B/bla.md#black-widow-agile-avenger) · [Bonny Pall, Clearcutter](cards/B/bo.md#bonny-pall-clearcutter) · [Bugenhagen, Wise Elder](cards/B/bu.md#bugenhagen-wise-elder) · [Captain Howler, Sea Scourge](cards/C/cap.md#captain-howler-sea-scourge) · [Chandra, Chill of Compliance](cards/C/cha.md#chandra-chill-of-compliance) · [Chevill, Bane of Monsters](cards/C/che.md#chevill-bane-of-monsters) · [Chulane, Teller of Tales](cards/C/chu.md#chulane-teller-of-tales) · [Cleopatra, Exiled Pharaoh](cards/C/cl.md#cleopatra-exiled-pharaoh) · [Cloud, Ex-SOLDIER](cards/C/cl.md#cloud-ex-soldier) · [Danny Pink](cards/D/da.md#danny-pink) · [Deepfathom Skulker](cards/D/dee.md#deepfathom-skulker) · [Dina, Essence Brewer](cards/D/di.md#dina-essence-brewer) · [Dr. Eggman](cards/D/dre.md#dr-eggman) · [Edric, Spymaster of Trest](cards/E/ed.md#edric-spymaster-of-trest) · [Ellivere of the Wild Court](cards/E/el.md#ellivere-of-the-wild-court) · [Elrond, Master of Healing](cards/E/el.md#elrond-master-of-healing) · [Emet-Selch, Unsundered // Hades, Sorcerer of Eld](cards/E/em.md#emet-selch-unsundered--hades-sorcerer-of-eld) · [Ephara, God of the Polis](cards/E/ep.md#ephara-god-of-the-polis) · [Extraordinary Journey](cards/E/ex.md#extraordinary-journey) · [Ezio, Blade of Vengeance](cards/E/ez.md#ezio-blade-of-vengeance) · [Ezuri, Stalker of Spheres](cards/E/ez.md#ezuri-stalker-of-spheres) · [Fang, Fearless l'Cie](cards/F/fa.md#fang-fearless-lcie) · [Faramir, Prince of Ithilien](cards/F/fa.md#faramir-prince-of-ithilien) · [Firkraag, Cunning Instigator](cards/F/fi.md#firkraag-cunning-instigator) · [Flubs, the Fool](cards/F/fl.md#flubs-the-fool) · [Gandalf, Friend of the Shire](cards/G/ga.md#gandalf-friend-of-the-shire) · [Garna, Bloodfist of Keld](cards/G/ga.md#garna-bloodfist-of-keld) · [Garruk's Packleader](cards/G/ga.md#garruks-packleader) · [Garruk, Curse Breaker](cards/G/ga.md#garruk-curse-breaker) · [Glissa Sunslayer](cards/G/gl.md#glissa-sunslayer) · [Gran-Gran](cards/G/gra.md#gran-gran) · [Grazilaxx, Illithid Scholar](cards/G/gra.md#grazilaxx-illithid-scholar) · [Guild Summit](cards/G/gu.md#guild-summit) · [Haliya, Ascendant Cadet](cards/H/ha.md#haliya-ascendant-cadet) · [Haliya, Guided by Light](cards/H/ha.md#haliya-guided-by-light) · [Helga, Skittish Seer](cards/H/he.md#helga-skittish-seer) · [Heroes in a Half Shell](cards/H/he.md#heroes-in-a-half-shell) · [Huatli, Radiant Champion](cards/H/hu.md#huatli-radiant-champion) · [Inga and Esika](cards/I/ing.md#inga-and-esika) · [Iron Man, Armored Avenger](cards/I/ir.md#iron-man-armored-avenger) · [Isperia, Supreme Judge](cards/I/is.md#isperia-supreme-judge) · [Iymrith, Desert Doom](cards/I/iy.md#iymrith-desert-doom) · [Jace, Cunning Castaway](cards/J/ja.md#jace-cunning-castaway) · [Jason Bright, Glowing Prophet](cards/J/ja.md#jason-bright-glowing-prophet) · [Jeskai Elder](cards/J/je.md#jeskai-elder) · [Jhessian Thief](cards/J/jh.md#jhessian-thief) · [Jhoira, Weatherlight Captain](cards/J/jh.md#jhoira-weatherlight-captain) · [Jiang Yanggu, Alone](cards/J/ji.md#jiang-yanggu-alone) · [Jin Sakai, Ghost of Tsushima](cards/J/ji.md#jin-sakai-ghost-of-tsushima) · [Jin-Gitaxias // The Great Synthesis](cards/J/ji.md#jin-gitaxias--the-great-synthesis) · [Jon Irenicus, Shattered One](cards/J/jo.md#jon-irenicus-shattered-one) · [Jori En, Ruin Diver](cards/J/jo.md#jori-en-ruin-diver) · [Karazikar, the Eye Tyrant](cards/K/ka.md#karazikar-the-eye-tyrant) · [Kassandra, Eagle Bearer](cards/K/ka.md#kassandra-eagle-bearer) · [Katara, Waterbending Master](cards/K/ka.md#katara-waterbending-master) · [Keranos, God of Storms](cards/K/ke.md#keranos-god-of-storms) · [Ketramose, the New Dawn](cards/K/ke.md#ketramose-the-new-dawn) · [Killian, Decisive Mentor](cards/K/ki.md#killian-decisive-mentor) · [King T'Challa // Black Panther, Hope Enduring](cards/K/ki.md#king-tchalla--black-panther-hope-enduring) · [Kiora, Behemoth Beckoner](cards/K/ki.md#kiora-behemoth-beckoner) · [Korvold, Fae-Cursed King](cards/K/ko.md#korvold-fae-cursed-king) · [Kothophed, Soul Hoarder](cards/K/ko.md#kothophed-soul-hoarder) · [Kraum, Ludevic's Opus](cards/K/kr.md#kraum-ludevics-opus) · [Kraum, Violent Cacophony](cards/K/kr.md#kraum-violent-cacophony) · [Kutzil, Malamet Exemplar](cards/K/ku.md#kutzil-malamet-exemplar) · [Kynaios and Tiro of Meletis](cards/K/ky.md#kynaios-and-tiro-of-meletis) · [Kíli the Resourceful](cards/K/ki.md#kíli-the-resourceful) · [Legolas Greenleaf](cards/L/le.md#legolas-greenleaf) · [Liliana, Dreadhorde General](cards/L/li.md#liliana-dreadhorde-general) · [Loki, God of Mischief](cards/L/lo.md#loki-god-of-mischief) · [Losheel, Clockwork Scholar](cards/L/lo.md#losheel-clockwork-scholar) · [Lyla, Holographic Assistant](cards/L/ly.md#lyla-holographic-assistant) · [Mangara, the Diplomat](cards/M/man.md#mangara-the-diplomat) · [Marchesa's Infiltrator](cards/M/mar.md#marchesas-infiltrator) · [Marcus, Mutant Mayor](cards/M/mar.md#marcus-mutant-mayor) · [Marneus Calgar](cards/M/mar.md#marneus-calgar) · [Marvo, Deep Operative](cards/M/mar.md#marvo-deep-operative) · [Mary Jane Watson](cards/M/mar.md#mary-jane-watson) · [Massacre Girl, Known Killer](cards/M/mas.md#massacre-girl-known-killer) · [Mastermind Plum](cards/M/mas.md#mastermind-plum) · [Matoya, Archon Elder](cards/M/mat.md#matoya-archon-elder) · [Merry, Esquire of Rohan](cards/M/me.md#merry-esquire-of-rohan) · [Mikey & Leo, Chaos & Order](cards/M/mik.md#mikey--leo-chaos--order) · [Mila, Crafty Companion // Lukka, Wayward Bonder](cards/M/mil.md#mila-crafty-companion--lukka-wayward-bonder) · [Mister Fantastic, Reed Richards](cards/M/mis.md#mister-fantastic-reed-richards) · [Moonring Mirror](cards/M/moo.md#moonring-mirror) · [Mu Yanling, Wind Rider](cards/M/mu.md#mu-yanling-wind-rider) · [Narci, Fable Singer](cards/N/na.md#narci-fable-singer) · [Neerdiv, Devious Diver](cards/N/ne.md#neerdiv-devious-diver) · [Nelly Borca, Impulsive Accuser](cards/N/ne.md#nelly-borca-impulsive-accuser) · [Neyith of the Dire Hunt](cards/N/ne.md#neyith-of-the-dire-hunt) · [Nezahal, Primal Tide](cards/N/ne.md#nezahal-primal-tide) · [Nissa, Leyline Tamer](cards/N/ni.md#nissa-leyline-tamer) · [Nissa, Vital Force](cards/N/ni.md#nissa-vital-force) · [Niv-Mizzet, Dracogenius](cards/N/ni.md#niv-mizzet-dracogenius) · [Niv-Mizzet, Parun](cards/N/ni.md#niv-mizzet-parun) · [Niv-Mizzet, the Firemind](cards/N/ni.md#niv-mizzet-the-firemind) · [Padeem, Consul of Innovation](cards/P/pa.md#padeem-consul-of-innovation) · [Paladin Elizabeth Taggerdy](cards/P/pa.md#paladin-elizabeth-taggerdy) · [Pearl-Ear, Imperial Advisor](cards/P/pe.md#pearl-ear-imperial-advisor) · [Phyrexian Arena](cards/P/ph.md#phyrexian-arena) · [Professor Hojo](cards/P/pr.md#professor-hojo) · [Queza, Augur of Agonies](cards/Q/qu.md#queza-augur-of-agonies) · [Ray Fillet, Wave Warrior](cards/R/ray.md#ray-fillet-wave-warrior) · [Reki, the History of Kamigawa](cards/R/rek.md#reki-the-history-of-kamigawa) · [Roshan, Hidden Magister](cards/R/ro.md#roshan-hidden-magister) · [SP//dr, Piloted by Peni](cards/S/spd.md#spdr-piloted-by-peni) · [Samut, Vizier of Naktamun](cards/S/sam.md#samut-vizier-of-naktamun) · [Satoru, the Infiltrator](cards/S/sat.md#satoru-the-infiltrator) · [Selvala, Heart of the Wilds](cards/S/sel.md#selvala-heart-of-the-wilds) · [Seshiro the Anointed](cards/S/ses.md#seshiro-the-anointed) · [Shabraz, the Skyshark](cards/S/sha.md#shabraz-the-skyshark) · [Shadow the Hedgehog](cards/S/sha.md#shadow-the-hedgehog) · [Shanid, Sleepers' Scourge](cards/S/sha.md#shanid-sleepers-scourge) · [Shapers' Sanctuary](cards/S/sha.md#shapers-sanctuary) · [Sharae of Numbing Depths](cards/S/sha.md#sharae-of-numbing-depths) · [Sheoldred, the Apocalypse](cards/S/she.md#sheoldred-the-apocalypse) · [Sidar Jabari of Zhalfir](cards/S/si.md#sidar-jabari-of-zhalfir) · [Smaug, Wicked Worm](cards/S/sm.md#smaug-wicked-worm) · [Sokka, Lateral Strategist](cards/S/so.md#sokka-lateral-strategist) · [Sphinx's Tutelage](cards/S/sph.md#sphinxs-tutelage) · [Spider-UK](cards/S/spi.md#spider-uk) · [Sram, Senior Edificer](cards/S/sr.md#sram-senior-edificer) · [Starscream, Power Hungry // Starscream, Seeker Leader](cards/S/sta.md#starscream-power-hungry--starscream-seeker-leader) · [Subira, Tulzidi Caravanner](cards/S/sub.md#subira-tulzidi-caravanner) · [Surrak, Elusive Hunter](cards/S/sur.md#surrak-elusive-hunter) · [Svyelun of Sea and Sky](cards/S/sv.md#svyelun-of-sea-and-sky) · [Sygg, River Cutthroat](cards/S/sy.md#sygg-river-cutthroat) · [Sythis, Harvest's Hand](cards/S/sy.md#sythis-harvests-hand) · [Taii Wakeen, Perfect Shot](cards/T/ta.md#taii-wakeen-perfect-shot) · [Take Flight](cards/T/ta.md#take-flight) · [Talion, the Kindly Lord](cards/T/ta.md#talion-the-kindly-lord) · [Tamiyo, Field Researcher](cards/T/ta.md#tamiyo-field-researcher) · [Tatyova, Benthic Druid](cards/T/ta.md#tatyova-benthic-druid) · [Teferi, Hero of Dominaria](cards/T/te.md#teferi-hero-of-dominaria) · [Teferi, Temporal Pilgrim](cards/T/te.md#teferi-temporal-pilgrim) · [Tegwyll, Duke of Splendor](cards/T/te.md#tegwyll-duke-of-splendor) · [Temmet, Naktamun's Will](cards/T/te.md#temmet-naktamuns-will) · [Tezzeret, Betrayer of Flesh](cards/T/te.md#tezzeret-betrayer-of-flesh) · [Thalia and The Gitrog Monster](cards/T/tha.md#thalia-and-the-gitrog-monster) · [The Blue Spirit](cards/T/theb.md#the-blue-spirit) · [The Council of Four](cards/T/thec.md#the-council-of-four) · [The Endstone](cards/T/thee.md#the-endstone) · [The Gaffer](cards/T/theg.md#the-gaffer) · [The Gitrog Monster](cards/T/theg.md#the-gitrog-monster) · [The Locust God](cards/T/thel.md#the-locust-god) · [The Magic Mirror](cards/T/them.md#the-magic-mirror) · [The Odd Acorn Gang](cards/T/theo.md#the-odd-acorn-gang) · [The Scorpion God](cards/T/thes.md#the-scorpion-god) · [The Second Doctor](cards/T/thes.md#the-second-doctor) · [The Theorist, Jace Beleren](cards/T/thet.md#the-theorist-jace-beleren) · [The Watcher in the Water](cards/T/thew.md#the-watcher-in-the-water) · [Thopter Spy Network](cards/T/tho.md#thopter-spy-network) · [Tidus, Yuna's Guardian](cards/T/ti.md#tidus-yunas-guardian) · [Tinybones, Trinket Thief](cards/T/ti.md#tinybones-trinket-thief) · [Tippy-Toe, Terrific Partner](cards/T/ti.md#tippy-toe-terrific-partner) · [Tocasia's Welcome](cards/T/to.md#tocasias-welcome) · [Tome of the Guildpact](cards/T/to.md#tome-of-the-guildpact) · [Tomik, Wielder of Law](cards/T/to.md#tomik-wielder-of-law) · [Toothy, Imaginary Friend](cards/T/to.md#toothy-imaginary-friend) · [Toski, Bearer of Secrets](cards/T/to.md#toski-bearer-of-secrets) · [Tovolar, Dire Overlord // Tovolar, the Midnight Scourge](cards/T/to.md#tovolar-dire-overlord--tovolar-the-midnight-scourge) · [Tuvasa the Sunlit](cards/T/tu.md#tuvasa-the-sunlit) · [Ultimecia, Temporal Threat](cards/U/ul.md#ultimecia-temporal-threat) · [Unctus, Grand Metatect](cards/U/un.md#unctus-grand-metatect) · [Up the Beanstalk](cards/U/up.md#up-the-beanstalk) · [Urabrask, Heretic Praetor](cards/U/ur.md#urabrask-heretic-praetor) · [Uro, Titan of Nature's Wrath](cards/U/ur.md#uro-titan-of-natures-wrath) · [Valeron Wardens](cards/V/va.md#valeron-wardens) · [Valgavoth, Harrower of Souls](cards/V/va.md#valgavoth-harrower-of-souls) · [Vega, the Watcher](cards/V/ve.md#vega-the-watcher) · [Venat, Heart of Hydaelyn // Hydaelyn, the Mothercrystal](cards/V/ve.md#venat-heart-of-hydaelyn--hydaelyn-the-mothercrystal) · [Vraska Joins Up](cards/V/vr.md#vraska-joins-up) · [Wan Shi Tong, Librarian](cards/W/wan.md#wan-shi-tong-librarian) · [Wyleth, Soul of Steel](cards/W/wy.md#wyleth-soul-of-steel) · [Wylie Duke, Atiin Hero](cards/W/wy.md#wylie-duke-atiin-hero) · [Y'shtola, Night's Blessed](cards/Y/ys.md#yshtola-nights-blessed) · [Zendikar Resurgent](cards/Z/ze.md#zendikar-resurgent) · [Zurgo Stormrender](cards/Z/zu.md#zurgo-stormrender) · [Zurzoth, Chaos Rider](cards/Z/zu.md#zurzoth-chaos-rider)

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

Used in decks (≥ 3 matching cards, 15): [Niv-Mizzet, Parun](decks/niv-mizzet-parun.md) 6 · [Norman Osborn // Green Goblin (Grixis)](grixis/decks/norman-osborn.md) 6 · [Bjorna, Nightfall Alchemist (Grixis)](grixis/decks/bjorna-nightfall-alchemist-cecily.md) 5 · [Doctor Doom, King of Latveria (Grixis)](grixis/decks/doctor-doom-king-of-latveria.md) 5 · [Zevlor, Elturel Exile (Grixis)](grixis/decks/zevlor-elturel-exile.md) 5 · [Talrand, Sky Summoner](decks/talrand-sky-summoner.md) 4 · [Saruman, the White Hand (Grixis)](grixis/decks/saruman-the-white-hand.md) 4 · [Kykar, Wind's Fury](decks/kykar-winds-fury.md) 3 · [Teysa Karlov](decks/teysa-karlov.md) 3 · [Yidris, Maelstrom Wielder](decks/yidris-maelstrom-wielder.md) 3 · [Edea, Possessed Sorceress (Grixis)](grixis/decks/edea-possessed-sorceress.md) 3 · [Fire Lord Azula (Grixis)](grixis/decks/fire-lord-azula.md) 3 · …3 more

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 35): [Blast of Genius](cards/B/bla.md#blast-of-genius) · [Calamitous Tide](cards/C/cal.md#calamitous-tide) · [Camaraderie](cards/C/cam.md#camaraderie) · [Cast Away Doubt](cards/C/cas.md#cast-away-doubt) · [Cathartic Reunion](cards/C/cat.md#cathartic-reunion) · [Corrupted Conviction](cards/C/cor.md#corrupted-conviction) · [Cruel Ultimatum](cards/C/cr.md#cruel-ultimatum) · [Crushing Disappointment](cards/C/cr.md#crushing-disappointment) · [Demand Answers](cards/D/dem.md#demand-answers) · [Distant Memories](cards/D/di.md#distant-memories) · [Fanatical Offering](cards/F/fa.md#fanatical-offering) · [Glimmer of Genius](cards/G/gl.md#glimmer-of-genius) · [Gruesome Realization](cards/G/gru.md#gruesome-realization) · [Into the Fae Court](cards/I/int.md#into-the-fae-court) · [Izzet Charm](cards/I/iz.md#izzet-charm) · [Jace's Ingenuity](cards/J/ja.md#jaces-ingenuity) · [Live Fast](cards/L/li.md#live-fast) · [Magmatic Insight](cards/M/mag.md#magmatic-insight) · [Merciless Resolve](cards/M/me.md#merciless-resolve) · [Plan the Heist](cards/P/pl.md#plan-the-heist) · [Pore Over the Pages](cards/P/po.md#pore-over-the-pages) · [Practical Research](cards/P/pr.md#practical-research) · [Rowan's Grim Search](cards/R/ro.md#rowans-grim-search) · [Seize the Secrets](cards/S/sei.md#seize-the-secrets) · [Silver Scrutiny](cards/S/si.md#silver-scrutiny) · [Stern Lesson](cards/S/ste.md#stern-lesson) · [Tezzeret's Ambition](cards/T/te.md#tezzerets-ambition) · [Thrill of Possibility](cards/T/thr.md#thrill-of-possibility) · [Thrilling Discovery](cards/T/thr.md#thrilling-discovery) · [Transcendent Message](cards/T/tra.md#transcendent-message) · [Treasure Cruise](cards/T/tre.md#treasure-cruise) · [Ugin's Insight](cards/U/ug.md#ugins-insight) · [Unexpected Assistance](cards/U/un.md#unexpected-assistance) · [Unexplained Vision](cards/U/un.md#unexplained-vision) · [Weight of Memory](cards/W/we.md#weight-of-memory)

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

Used in decks (≥ 3 matching cards, 14): [Prosper, Tome-Bound](decks/prosper-tome-bound.md) 15 · [Don Andres, the Renegade (Grixis)](grixis/decks/don-andres-the-renegade.md) 12 · [Nathan Drake, Treasure Hunter (Grixis)](grixis/decks/nathan-drake-treasure-hunter.md) 11 · [Edward Kenway (Grixis)](grixis/decks/edward-kenway.md) 6 · [The Madcap Jester (Grixis)](grixis/decks/the-madcap-jester.md) 6 · [Abaddon the Despoiler (Grixis)](grixis/decks/abaddon-the-despoiler.md) 5 · [Admiral Beckett Brass (Grixis)](grixis/decks/admiral-beckett-brass.md) 5 · [Admiral Brass, Unsinkable (Grixis)](grixis/decks/admiral-brass-unsinkable.md) 4 · [Goro-Goro and Satoru (Grixis)](grixis/decks/goro-goro-and-satoru.md) 4 · [Isshin, Two Heavens as One (Kamigawa-only)](decks/plane-kamigawa-isshin-two-heavens-as-one.md) 3 · [Fire Lord Azula (Grixis)](grixis/decks/fire-lord-azula.md) 3 · [Jeleva, Nephalia's Scourge (Grixis)](grixis/decks/jeleva-nephalias-scourge.md) 3 · …2 more

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 57): [Abbot of Keral Keep](cards/A/ab.md#abbot-of-keral-keep) · [Apex of Power](cards/A/ap.md#apex-of-power) · [Araña, Heart of the Spider](cards/A/ara.md#araña-heart-of-the-spider) · [Atsushi, the Blazing Sky](cards/A/at.md#atsushi-the-blazing-sky) · [Birgi, God of Storytelling // Harnfel, Horn of Bounty](cards/B/bi.md#birgi-god-of-storytelling--harnfel-horn-of-bounty) · [Blazing Crescendo](cards/B/bla.md#blazing-crescendo) · [Breeches, Brazen Plunderer](cards/B/br.md#breeches-brazen-plunderer) · [Breeches, Eager Pillager](cards/B/br.md#breeches-eager-pillager) · [Cait Sith, Fortune Teller](cards/C/cai.md#cait-sith-fortune-teller) · [Chandra, Dressed to Kill](cards/C/cha.md#chandra-dressed-to-kill) · [Chandra, Fire Artisan](cards/C/cha.md#chandra-fire-artisan) · [Chandra, Heart of Fire](cards/C/cha.md#chandra-heart-of-fire) · [Chandra, Hope's Beacon](cards/C/cha.md#chandra-hopes-beacon) · [Chandra, Pyromaster](cards/C/cha.md#chandra-pyromaster) · [Chandra, Torch of Defiance](cards/C/cha.md#chandra-torch-of-defiance) · [Chiss-Goria, Forge Tyrant](cards/C/chi.md#chiss-goria-forge-tyrant) · [Commander Liara Portyr](cards/C/com.md#commander-liara-portyr) · [Commune with Lava](cards/C/com.md#commune-with-lava) · [Count on Luck](cards/C/cou.md#count-on-luck) · [Dogmeat, Ever Loyal](cards/D/do.md#dogmeat-ever-loyal) · [Dragonhawk, Fate's Tempest](cards/D/dra.md#dragonhawk-fates-tempest) · [Eruth, Tormented Prophet](cards/E/er.md#eruth-tormented-prophet) · [Faldorn, Dread Wolf Herald](cards/F/fa.md#faldorn-dread-wolf-herald) · [Gix, Yawgmoth Praetor](cards/G/gi.md#gix-yawgmoth-praetor) · [Grenzo, Havoc Raiser](cards/G/gre.md#grenzo-havoc-raiser) · [Gwen Stacy // Ghost-Spider](cards/G/gw.md#gwen-stacy--ghost-spider) · [Headliner Scarlett](cards/H/he.md#headliner-scarlett) · [Hidetsugu, Devouring Chaos](cards/H/hi.md#hidetsugu-devouring-chaos) · [Hugs, Grisly Guardian](cards/H/hu.md#hugs-grisly-guardian) · [Inti, Seneschal of the Sun](cards/I/int.md#inti-seneschal-of-the-sun) · [Kellan, Planar Trailblazer](cards/K/ke.md#kellan-planar-trailblazer) · [Kotis, the Fangkeeper](cards/K/ko.md#kotis-the-fangkeeper) · [Laelia, the Blade Reforged](cards/L/la.md#laelia-the-blade-reforged) · [Laughing Jasper Flint](cards/L/la.md#laughing-jasper-flint) · [Meeting of the Five](cards/M/me.md#meeting-of-the-five) · [Mr. Monopoly, On the Go](cards/M/mr.md#mr-monopoly-on-the-go) · [Muerra, Trash Tactician](cards/M/mu.md#muerra-trash-tactician) · [Nahiri, Forged in Fury](cards/N/na.md#nahiri-forged-in-fury) · [Narset, Enlightened Master](cards/N/na.md#narset-enlightened-master) · [Nashi, Moon Sage's Scion](cards/N/na.md#nashi-moon-sages-scion) · [Ob Nixilis, Captive Kingpin](cards/O/ob.md#ob-nixilis-captive-kingpin) · [Outpost Siege](cards/O/ou.md#outpost-siege) · [Prosper, Tome-Bound](cards/P/pr.md#prosper-tome-bound) · [Ragavan, Nimble Pilferer](cards/R/rag.md#ragavan-nimble-pilferer) · [Ral, Monsoon Mage // Ral, Leyline Prodigy](cards/R/ral.md#ral-monsoon-mage--ral-leyline-prodigy) · [Ramirez DePietro, Pillager](cards/R/ram.md#ramirez-depietro-pillager) · [Rose, Cutthroat Raider](cards/R/ro.md#rose-cutthroat-raider) · [Spinneret and Spiderling](cards/S/spi.md#spinneret-and-spiderling) · [Stella Lee, Wild Card](cards/S/ste.md#stella-lee-wild-card) · [The Great Goblin](cards/T/theg.md#the-great-goblin) · [Urabrask, Heretic Praetor](cards/U/ur.md#urabrask-heretic-praetor) · [Urza, Lord High Artificer](cards/U/ur.md#urza-lord-high-artificer) · [Vaan, Street Thief](cards/V/va.md#vaan-street-thief) · [Veronica, Dissident Scribe](cards/V/ve.md#veronica-dissident-scribe) · [Visions of Phyrexia](cards/V/vi.md#visions-of-phyrexia) · [Wrenn's Resolve](cards/W/wr.md#wrenns-resolve) · [Zuko, Exiled Prince](cards/Z/zu.md#zuko-exiled-prince)

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

Used in decks (≥ 3 matching cards, 10): [Marchesa, the Black Rose (Grixis)](grixis/decks/marchesa-the-black-rose.md) 7 · [Thraximundar (Grixis)](grixis/decks/thraximundar.md) 6 · [Tresserhorn's Lord, Returned (Grixis)](grixis/decks/tresserhorns-lord-returned.md) 6 · [Wick, the Whorled Mind (Grixis)](grixis/decks/wick-the-whorled-mind.md) 6 · [Teysa Karlov](decks/teysa-karlov.md) 5 · [Edea, Possessed Sorceress (Grixis)](grixis/decks/edea-possessed-sorceress.md) 5 · [Lord of Tresserhorn (Grixis)](grixis/decks/lord-of-tresserhorn.md) 5 · [Missy (Grixis)](grixis/decks/missy.md) 5 · [Karador, Ghost Chieftain](decks/karador-ghost-chieftain.md) 3 · [Korvold, Fae-Cursed King](decks/korvold-fae-cursed-king.md) 3

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 4): [Grimgrin, Corpse-Born](cards/G/gri.md#grimgrin-corpse-born) · [Rakdos, the Muscle](cards/R/rak.md#rakdos-the-muscle) · [Scarland Thrinax](cards/S/sc.md#scarland-thrinax) · [Yahenni, Undying Partisan](cards/Y/ya.md#yahenni-undying-partisan)

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

Used in decks (≥ 3 matching cards, 1): [Teysa Karlov](decks/teysa-karlov.md) 4

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 4): [Agent Venom](cards/A/ag.md#agent-venom) · [Elas il-Kor, Sadistic Pilgrim](cards/E/el.md#elas-il-kor-sadistic-pilgrim) · [Sephiroth, Fabled SOLDIER // Sephiroth, One-Winged Angel](cards/S/sep.md#sephiroth-fabled-soldier--sephiroth-one-winged-angel) · [Sifa Grent](cards/S/si.md#sifa-grent)

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

Used in decks (≥ 3 matching cards, 8): [Krenko, Mob Boss](decks/krenko-mob-boss.md) 9 · [Tresserhorn's Lord, Returned (Grixis)](grixis/decks/tresserhorns-lord-returned.md) 6 · [Wick, the Whorled Mind (Grixis)](grixis/decks/wick-the-whorled-mind.md) 6 · [Breya, Etherium Shaper](decks/breya-etherium-shaper.md) 4 · [Syr Konrad, the Grim (Eldraine-only)](decks/plane-eldraine-syr-konrad-the-grim.md) 3 · [Elesh Norn, Mother of Machines (New-only)](decks/plane-new-phyrexia-elesh-norn-mother-of-machines.md) 3 · [Teysa Karlov](decks/teysa-karlov.md) 3 · [Trostani, Selesnya's Voice](decks/trostani-selesnyas-voice.md) 3

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 87): [Aang and Katara](cards/A/aa.md#aang-and-katara) · [Ajani, Adversary of Tyrants](cards/A/aj.md#ajani-adversary-of-tyrants) · [Ajani, Caller of the Pride](cards/A/aj.md#ajani-caller-of-the-pride) · [Anim Pakal, Thousandth Moon](cards/A/an.md#anim-pakal-thousandth-moon) · [Apothecary White](cards/A/ap.md#apothecary-white) · [Arlinn, the Pack's Hope // Arlinn, the Moon's Fury](cards/A/arl.md#arlinn-the-packs-hope--arlinn-the-moons-fury) · [Ashiok, Wicked Manipulator](cards/A/as.md#ashiok-wicked-manipulator) · [Awaken the Woods](cards/A/aw.md#awaken-the-woods) · [B.O.B. (Bevy of Beebles)](cards/B/bo.md#bob-bevy-of-beebles) · [Beza, the Bounding Spring](cards/B/be.md#beza-the-bounding-spring) · [Breya, Etherium Shaper](cards/B/br.md#breya-etherium-shaper) · [Caesar, Legion's Emperor](cards/C/cae.md#caesar-legions-emperor) · [Captain of the Watch](cards/C/cap.md#captain-of-the-watch) · [Chandra, Acolyte of Flame](cards/C/cha.md#chandra-acolyte-of-flame) · [Chandra, Flamecaller](cards/C/cha.md#chandra-flamecaller) · [Comet, Stellar Pup](cards/C/com.md#comet-stellar-pup) · [Eiganjo Uprising](cards/E/ei.md#eiganjo-uprising) · [Elenda and Azor](cards/E/el.md#elenda-and-azor) · [Elenda, the Dusk Rose](cards/E/el.md#elenda-the-dusk-rose) · [Elminster](cards/E/el.md#elminster) · [Elspeth Tirel](cards/E/el.md#elspeth-tirel) · [Elspeth, Sun's Champion](cards/E/el.md#elspeth-suns-champion) · [Elspeth, Sun's Nemesis](cards/E/el.md#elspeth-suns-nemesis) · [Emrakul's Hatcher](cards/E/em.md#emrakuls-hatcher) · [Endrek Sahr, Master Breeder](cards/E/en.md#endrek-sahr-master-breeder) · [Eyeless Watcher](cards/E/ey.md#eyeless-watcher) · [Faramir, Prince of Ithilien](cards/F/fa.md#faramir-prince-of-ithilien) · [Faramir, Steward of Gondor](cards/F/fa.md#faramir-steward-of-gondor) · [Farmer Cotton](cards/F/fa.md#farmer-cotton) · [Felisa, Fang of Silverquill](cards/F/fe.md#felisa-fang-of-silverquill) · [Feroz, Ulgrotha's Warden](cards/F/fe.md#feroz-ulgrothas-warden) · [Ferrafor, Young Yew](cards/F/fe.md#ferrafor-young-yew) · [Garruk, Cursed Huntsman](cards/G/ga.md#garruk-cursed-huntsman) · [Ghalta and Mavren](cards/G/gh.md#ghalta-and-mavren) · [Ghoulcaller Gisa](cards/G/gh.md#ghoulcaller-gisa) · [Gideon's Phalanx](cards/G/gi.md#gideons-phalanx) · [Gisa's Bidding](cards/G/gi.md#gisas-bidding) · [Gisa, the Hellraiser](cards/G/gi.md#gisa-the-hellraiser) · [Hanweir, the Writhing Township](cards/H/ha.md#hanweir-the-writhing-township) · [Hazezon, Shaper of Sand](cards/H/ha.md#hazezon-shaper-of-sand) · [Hour of Promise](cards/H/ho.md#hour-of-promise) · [Huatli, Poet of Unity // Roar of the Fifth People](cards/H/hu.md#huatli-poet-of-unity--roar-of-the-fifth-people) · [Imotekh the Stormlord](cards/I/im.md#imotekh-the-stormlord) · [Invasion of New Phyrexia // Teferi Akosa of Zhalfir](cards/I/inv.md#invasion-of-new-phyrexia--teferi-akosa-of-zhalfir) · [Ishkanah, Grafwidow](cards/I/is.md#ishkanah-grafwidow) · [Jan Jansen, Chaos Crafter](cards/J/ja.md#jan-jansen-chaos-crafter) · [Kiora, Master of the Depths](cards/K/ki.md#kiora-master-of-the-depths) · [Koma, World-Eater](cards/K/ko.md#koma-world-eater) · [Krenko's Command](cards/K/kr.md#krenkos-command) · [Krenko, Mob Boss](cards/K/kr.md#krenko-mob-boss) · [Krenko, Tin Street Kingpin](cards/K/kr.md#krenko-tin-street-kingpin) · [Liliana, the Last Hope](cards/L/li.md#liliana-the-last-hope) · [Lolth, Spider Queen](cards/L/lo.md#lolth-spider-queen) · [Marneus Calgar](cards/M/mar.md#marneus-calgar) · [Marrow-Gnawer](cards/M/mar.md#marrow-gnawer) · [Mausoleum Guard](cards/M/mau.md#mausoleum-guard) · [Ministrant of Obligation](cards/M/min.md#ministrant-of-obligation) · [Myrel, Shield of Argive](cards/M/my.md#myrel-shield-of-argive) · [Neriv, Crackling Vanguard](cards/N/ne.md#neriv-crackling-vanguard) · [Oath of Gideon](cards/O/oa.md#oath-of-gideon) · [Oko, Lorwyn Liege // Oko, Shadowmoor Scion](cards/O/ok.md#oko-lorwyn-liege--oko-shadowmoor-scion) · [Ovika, Enigma Goliath](cards/O/ov.md#ovika-enigma-goliath) · [Pashalik Mons](cards/P/pa.md#pashalik-mons) · [Pia and Kiran Nalaar](cards/P/pi.md#pia-and-kiran-nalaar) · [Prossh, Skyraider of Kher](cards/P/pr.md#prossh-skyraider-of-kher) · [Rally the Monastery](cards/R/ral.md#rally-the-monastery) · [Release the Gremlins](cards/R/rel.md#release-the-gremlins) · [Rise of the Dread Marn](cards/R/ri.md#rise-of-the-dread-marn) · [Saheeli, Filigree Master](cards/S/sah.md#saheeli-filigree-master) · [Sarkhan, Fireblood](cards/S/sar.md#sarkhan-fireblood) · [Sorin, Grim Nemesis](cards/S/so.md#sorin-grim-nemesis) · [Sunset Revelry](cards/S/sun.md#sunset-revelry) · [Take Up Arms](cards/T/ta.md#take-up-arms) · [Tevesh Szat, Doom of Fools](cards/T/te.md#tevesh-szat-doom-of-fools) · [Thalisse, Reverent Medium](cards/T/tha.md#thalisse-reverent-medium) · [The Mycotyrant](cards/T/them.md#the-mycotyrant) · [The Swarmweaver](cards/T/thes.md#the-swarmweaver) · [The Unbeatable Squirrel Girl](cards/T/theu.md#the-unbeatable-squirrel-girl) · [Trostani Discordant](cards/T/tro.md#trostani-discordant) · [Urza, Planeswalker](cards/U/ur.md#urza-planeswalker) · [Verdeloth the Ancient](cards/V/ve.md#verdeloth-the-ancient) · [Vishgraz, the Doomhive](cards/V/vi.md#vishgraz-the-doomhive) · [Vraska the Unseen](cards/V/vr.md#vraska-the-unseen) · [Vren, the Relentless](cards/V/vr.md#vren-the-relentless) · [Weaponcraft Enthusiast](cards/W/we.md#weaponcraft-enthusiast) · [Zurgo, Thunder's Decree](cards/Z/zu.md#zurgo-thunders-decree) · [Éowyn, Shieldmaiden](cards/E/eo.md#éowyn-shieldmaiden)

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

Used in decks (≥ 3 matching cards, 1): [Animar, Soul of Elements](decks/animar-soul-of-elements.md) 4

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 4): [Mauhúr, Uruk-hai Captain](cards/M/mau.md#mauhúr-uruk-hai-captain) · [Michelangelo, Weirdness to 11](cards/M/mic.md#michelangelo-weirdness-to-11) · [Mowu, Loyal Companion](cards/M/mow.md#mowu-loyal-companion) · [Pir, Imaginative Rascal](cards/P/pi.md#pir-imaginative-rascal)

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

Used in decks (≥ 3 matching cards, 3): [Atraxa, Praetors' Voice](decks/atraxa-praetors-voice.md) 24 · [Atraxa, Praetors' Voice (planeswalkers theme)](decks/theme-atraxa-praetors-voice-planeswalkers.md) 12 · [Nicol Bolas, the Ravager // Nicol Bolas, the Arisen (Grixis)](grixis/decks/nicol-bolas-the-ravager.md) 8

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 17): [Agent Frank Horrigan](cards/A/ag.md#agent-frank-horrigan) · [Atraxa, Praetors' Voice](cards/A/at.md#atraxa-praetors-voice) · [Brimaz, Blight of Oreskos](cards/B/br.md#brimaz-blight-of-oreskos) · [Cayth, Famed Mechanist](cards/C/cay.md#cayth-famed-mechanist) · [Ezuri, Stalker of Spheres](cards/E/ez.md#ezuri-stalker-of-spheres) · [High Perfect Morcant](cards/H/hi.md#high-perfect-morcant) · [Kilo, Apogee Mind](cards/K/ki.md#kilo-apogee-mind) · [Lulu, Stern Guardian](cards/L/lu.md#lulu-stern-guardian) · [Planewide Celebration](cards/P/pl.md#planewide-celebration) · [Tam, the Possibility](cards/T/ta.md#tam-the-possibility) · [Tekuthal, Inquiry Dominus](cards/T/te.md#tekuthal-inquiry-dominus) · [Tidus, Yuna's Guardian](cards/T/ti.md#tidus-yunas-guardian) · [Tromell, Seymour's Butler](cards/T/tro.md#tromell-seymours-butler) · [Venser, Corpse Puppet](cards/V/ve.md#venser-corpse-puppet) · [Vraska, Betrayal's Sting](cards/V/vr.md#vraska-betrayals-sting) · [Xavier Sal, Infested Captain](cards/X/xa.md#xavier-sal-infested-captain) · [Yawgmoth, Thran Physician](cards/Y/ya.md#yawgmoth-thran-physician)

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

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 20): [Animar, Soul of Elements](cards/A/an.md#animar-soul-of-elements) · [Armorcraft Judge](cards/A/arm.md#armorcraft-judge) · [Byrke, Long Ear of the Law](cards/B/by.md#byrke-long-ear-of-the-law) · [Crowned Ceratok](cards/C/cr.md#crowned-ceratok) · [Elrond, Master of Healing](cards/E/el.md#elrond-master-of-healing) · [Haldir, Lórien Lieutenant](cards/H/ha.md#haldir-lórien-lieutenant) · [Hamza, Guardian of Arashin](cards/H/ha.md#hamza-guardian-of-arashin) · [High Sentinels of Arashin](cards/H/hi.md#high-sentinels-of-arashin) · [Ivorytusk Fortress](cards/I/iv.md#ivorytusk-fortress) · [Jiang Yanggu, Wildcrafter](cards/J/ji.md#jiang-yanggu-wildcrafter) · [Marchesa, the Black Rose](cards/M/mar.md#marchesa-the-black-rose) · [Mer-Ek Nightblade](cards/M/me.md#mer-ek-nightblade) · [Nissa's Judgment](cards/N/ni.md#nissas-judgment) · [Patron of the Valiant](cards/P/pa.md#patron-of-the-valiant) · [Scale Blessing](cards/S/sc.md#scale-blessing) · [Sunbringer's Touch](cards/S/sun.md#sunbringers-touch) · [Toothy, Imaginary Friend](cards/T/to.md#toothy-imaginary-friend) · [Unity of Purpose](cards/U/un.md#unity-of-purpose) · [Zegana, Utopian Speaker](cards/Z/ze.md#zegana-utopian-speaker) · [Zimone, Infinite Analyst](cards/Z/zi.md#zimone-infinite-analyst)

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

Used in decks (≥ 3 matching cards, 4): [Talrand, Sky Summoner](decks/talrand-sky-summoner.md) 4 · [Niv-Mizzet, Parun](decks/niv-mizzet-parun.md) 3 · [Anhelo, the Painter (Grixis)](grixis/decks/anhelo-the-painter.md) 3 · [Parnesse, the Subtle Brush (Grixis)](grixis/decks/parnesse-the-subtle-brush.md) 3

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 6): [Baral, Chief of Compliance](cards/B/bar.md#baral-chief-of-compliance) · [Jace's Sanctum](cards/J/ja.md#jaces-sanctum) · [Magnus the Red](cards/M/mag.md#magnus-the-red) · [Mizzix of the Izmagnus](cards/M/miz.md#mizzix-of-the-izmagnus) · [Ral, Monsoon Mage // Ral, Leyline Prodigy](cards/R/ral.md#ral-monsoon-mage--ral-leyline-prodigy) · [Rowan, Scholar of Sparks // Will, Scholar of Frost](cards/R/ro.md#rowan-scholar-of-sparks--will-scholar-of-frost)

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

Used in decks (≥ 3 matching cards, 2): [Parnesse, the Subtle Brush (Grixis)](grixis/decks/parnesse-the-subtle-brush.md) 7 · [Anhelo, the Painter (Grixis)](grixis/decks/anhelo-the-painter.md) 4

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 7): [Gandalf the Grey](cards/G/ga.md#gandalf-the-grey) · [Kitsa, Otterball Elite](cards/K/ki.md#kitsa-otterball-elite) · [League Guildmage](cards/L/le.md#league-guildmage) · [Lithoform Engine](cards/L/li.md#lithoform-engine) · [Naru Meha, Master Wizard](cards/N/na.md#naru-meha-master-wizard) · [Stella Lee, Wild Card](cards/S/ste.md#stella-lee-wild-card) · [Venser, Fervent Forger](cards/V/ve.md#venser-fervent-forger)

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

Used in decks (≥ 3 matching cards, 16): [Feather, the Redeemed](decks/feather-the-redeemed.md) 14 · [Kykar, Wind's Fury](decks/kykar-winds-fury.md) 14 · [Niv-Mizzet, Parun](decks/niv-mizzet-parun.md) 10 · [Anhelo, the Painter (Grixis)](grixis/decks/anhelo-the-painter.md) 9 · [Parnesse, the Subtle Brush (Grixis)](grixis/decks/parnesse-the-subtle-brush.md) 9 · [Saruman, the White Hand (Grixis)](grixis/decks/saruman-the-white-hand.md) 7 · [Abaddon the Despoiler (Grixis)](grixis/decks/abaddon-the-despoiler.md) 5 · [Talrand, Sky Summoner](decks/talrand-sky-summoner.md) 4 · [Bjorna, Nightfall Alchemist (Grixis)](grixis/decks/bjorna-nightfall-alchemist-cecily.md) 4 · [Zevlor, Elturel Exile (Grixis)](grixis/decks/zevlor-elturel-exile.md) 4 · [Aurelia, the Warleader (Ravnica-only)](decks/plane-ravnica-aurelia-the-warleader.md) 3 · [Kefka, Court Mage // Kefka, Ruler of Ruin (Grixis)](grixis/decks/kefka-court-mage.md) 3 · …4 more

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 85): [Abbot of Keral Keep](cards/A/ab.md#abbot-of-keral-keep) · [Ashling, Flame Dancer](cards/A/as.md#ashling-flame-dancer) · [Balmor, Battlemage Captain](cards/B/bal.md#balmor-battlemage-captain) · [Black Waltz No. 3](cards/B/bla.md#black-waltz-no-3) · [Bria, Riptide Rogue](cards/B/br.md#bria-riptide-rogue) · [Chandra, Hope's Beacon](cards/C/cha.md#chandra-hopes-beacon) · [Cunning Breezedancer](cards/C/cu.md#cunning-breezedancer) · [Deekah, Fractal Theorist](cards/D/dee.md#deekah-fractal-theorist) · [Don Andres, the Renegade](cards/D/do.md#don-andres-the-renegade) · [Dovin's Acuity](cards/D/do.md#dovins-acuity) · [Dragon-Style Twins](cards/D/dra.md#dragon-style-twins) · [Electro, Assaulting Battery](cards/E/el.md#electro-assaulting-battery) · [Elsha of the Infinite](cards/E/el.md#elsha-of-the-infinite) · [Elsha, Threefold Master](cards/E/el.md#elsha-threefold-master) · [Extus, Oriq Overlord // Awaken the Blood Avatar](cards/E/ex.md#extus-oriq-overlord--awaken-the-blood-avatar) · [Fandaniel, Telophoroi Ascian](cards/F/fa.md#fandaniel-telophoroi-ascian) · [Feather, the Redeemed](cards/F/fe.md#feather-the-redeemed) · [Firemind's Research](cards/F/fi.md#fireminds-research) · [G'raha Tia, Scion Reborn](cards/G/gra.md#graha-tia-scion-reborn) · [Gale, Waterdeep Prodigy](cards/G/ga.md#gale-waterdeep-prodigy) · [Gandalf the Grey](cards/G/ga.md#gandalf-the-grey) · [Gandalf, Goblins' Bane // Flameshape](cards/G/ga.md#gandalf-goblins-bane--flameshape) · [Hermes, Overseer of Elpis](cards/H/he.md#hermes-overseer-of-elpis) · [Hraesvelgr of the First Brood](cards/H/hr.md#hraesvelgr-of-the-first-brood) · [Jace's Sanctum](cards/J/ja.md#jaces-sanctum) · [Jeskai Elder](cards/J/je.md#jeskai-elder) · [Jhessian Thief](cards/J/jh.md#jhessian-thief) · [Jin-Gitaxias // The Great Synthesis](cards/J/ji.md#jin-gitaxias--the-great-synthesis) · [Judith, Carnage Connoisseur](cards/J/ju.md#judith-carnage-connoisseur) · [Kitsa, Otterball Elite](cards/K/ki.md#kitsa-otterball-elite) · [Krark, the Thumbless](cards/K/kr.md#krark-the-thumbless) · [Krile Baldesion](cards/K/kr.md#krile-baldesion) · [Kuja, Genome Sorcerer // Trance Kuja, Fate Defied](cards/K/ku.md#kuja-genome-sorcerer--trance-kuja-fate-defied) · [Kykar, Wind's Fury](cards/K/ky.md#kykar-winds-fury) · [Kykar, Zephyr Awakener](cards/K/ky.md#kykar-zephyr-awakener) · [Livaan, Cultist of Tiamat](cards/L/li.md#livaan-cultist-of-tiamat) · [Longshot, Rebel Bowman](cards/L/lo.md#longshot-rebel-bowman) · [Lord of the Nazgûl](cards/L/lo.md#lord-of-the-nazgûl) · [Lunar Mystic](cards/L/lu.md#lunar-mystic) · [Lyse Hext](cards/L/ly.md#lyse-hext) · [Melek, Izzet Paragon](cards/M/me.md#melek-izzet-paragon) · [Mizzix of the Izmagnus](cards/M/miz.md#mizzix-of-the-izmagnus) · [Narset of the Ancient Way](cards/N/na.md#narset-of-the-ancient-way) · [Noyan Dar, Roil Shaper](cards/N/no.md#noyan-dar-roil-shaper) · [Octavia, Living Thesis](cards/O/oc.md#octavia-living-thesis) · [Ojer Pakpatiq, Deepest Epoch // Temple of Cyclical Time](cards/O/oj.md#ojer-pakpatiq-deepest-epoch--temple-of-cyclical-time) · [Orvar, the All-Form](cards/O/or.md#orvar-the-all-form) · [Ovika, Enigma Goliath](cards/O/ov.md#ovika-enigma-goliath) · [Papalymo Totolymo](cards/P/pa.md#papalymo-totolymo) · [Prismari, the Inspiration](cards/P/pr.md#prismari-the-inspiration) · [Professor Onyx](cards/P/pr.md#professor-onyx) · [Queen Brahne](cards/Q/qu.md#queen-brahne) · [Quiet Contemplation](cards/Q/qu.md#quiet-contemplation) · [Ral, Crackling Wit](cards/R/ral.md#ral-crackling-wit) · [Ral, Izzet Viceroy](cards/R/ral.md#ral-izzet-viceroy) · [Ringwarden Owl](cards/R/ri.md#ringwarden-owl) · [Rowan, Scholar of Sparks // Will, Scholar of Frost](cards/R/ro.md#rowan-scholar-of-sparks--will-scholar-of-frost) · [Saheeli, Jewel of Avishkar](cards/S/sah.md#saheeli-jewel-of-avishkar) · [Saheeli, Sublime Artificer](cards/S/sah.md#saheeli-sublime-artificer) · [Saruman, the White Hand](cards/S/sar.md#saruman-the-white-hand) · [Scroll of the Masters](cards/S/sc.md#scroll-of-the-masters) · [Shu Yun, the Silent Tempest](cards/S/shu.md#shu-yun-the-silent-tempest) · [Smelt-Ward Minotaur](cards/S/sm.md#smelt-ward-minotaur) · [Sokka, Tenacious Tactician](cards/S/so.md#sokka-tenacious-tactician) · [Spectacular Skywhale](cards/S/spe.md#spectacular-skywhale) · [Spellweaver Eternal](cards/S/spe.md#spellweaver-eternal) · [Student of Ojutai](cards/S/stu.md#student-of-ojutai) · [Talrand, Sky Summoner](cards/T/ta.md#talrand-sky-summoner) · [Tellah, Great Sage](cards/T/te.md#tellah-great-sage) · [Thancred Waters](cards/T/tha.md#thancred-waters) · [The Destined Black Mage](cards/T/thed.md#the-destined-black-mage) · [The Emperor of Palamecia // The Lord Master of Hell](cards/T/thee.md#the-emperor-of-palamecia--the-lord-master-of-hell) · [The Mechanist, Aerial Artisan](cards/T/them.md#the-mechanist-aerial-artisan) · [The Vision](cards/T/thev.md#the-vision) · [Thor, God of Thunder](cards/T/tho.md#thor-god-of-thunder) · [Thousand-Year Storm](cards/T/tho.md#thousand-year-storm) · [Tor Wauki the Younger](cards/T/to.md#tor-wauki-the-younger) · [Ty Lee, Chi Blocker](cards/T/ty.md#ty-lee-chi-blocker) · [Urabrask // The Great Work](cards/U/ur.md#urabrask--the-great-work) · [Veyran, Voice of Duality](cards/V/ve.md#veyran-voice-of-duality) · [Vivi Ornitier](cards/V/vi.md#vivi-ornitier) · [Vraska, Soul of Stone](cards/V/vr.md#vraska-soul-of-stone) · [Will Kenrith](cards/W/wi.md#will-kenrith) · [Y'shtola, Night's Blessed](cards/Y/ys.md#yshtola-nights-blessed) · [Zada, Hedron Grinder](cards/Z/za.md#zada-hedron-grinder)

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

Used in decks (≥ 3 matching cards, 4): [Muldrotha, the Gravetide (self mill theme)](decks/theme-muldrotha-the-gravetide-self-mill.md) 14 · [Muldrotha, the Gravetide](decks/muldrotha-the-gravetide.md) 11 · [Karador, Ghost Chieftain](decks/karador-ghost-chieftain.md) 8 · [Sauron, Lord of the Rings (Grixis)](grixis/decks/sauron-lord-of-the-rings.md) 3

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 43): [Admiral Brass, Unsinkable](cards/A/ad.md#admiral-brass-unsinkable) · [Ashcoat of the Shadow Swarm](cards/A/as.md#ashcoat-of-the-shadow-swarm) · [Combustible Gearhulk](cards/C/com.md#combustible-gearhulk) · [Crow of Dark Tidings](cards/C/cr.md#crow-of-dark-tidings) · [Dogmeat, Ever Loyal](cards/D/do.md#dogmeat-ever-loyal) · [Emry, Lurker of the Loch](cards/E/em.md#emry-lurker-of-the-loch) · [Estrid, the Masked](cards/E/es.md#estrid-the-masked) · [Gisa and Geralf](cards/G/gi.md#gisa-and-geralf) · [Greensleeves](cards/G/gre.md#greensleeves) · [Grist, Voracious Larva // Grist, the Plague Swarm](cards/G/gri.md#grist-voracious-larva--grist-the-plague-swarm) · [Grolnok, the Omnivore](cards/G/gro.md#grolnok-the-omnivore) · [Kagha, Shadow Archdruid](cards/K/ka.md#kagha-shadow-archdruid) · [Kairi, the Swirling Sky](cards/K/ka.md#kairi-the-swirling-sky) · [Liliana the Repentant](cards/L/li.md#liliana-the-repentant) · [Liliana's Indignation](cards/L/li.md#lilianas-indignation) · [Liliana, Death's Majesty](cards/L/li.md#liliana-deaths-majesty) · [Liliana, Untouched by Death](cards/L/li.md#liliana-untouched-by-death) · [Liliana, the Last Hope](cards/L/li.md#liliana-the-last-hope) · [Lluwen, Imperfect Naturalist](cards/L/ll.md#lluwen-imperfect-naturalist) · [Lumra, Bellow of the Woods](cards/L/lu.md#lumra-bellow-of-the-woods) · [Nashi, Searcher in the Dark](cards/N/na.md#nashi-searcher-in-the-dark) · [Oko, Lorwyn Liege // Oko, Shadowmoor Scion](cards/O/ok.md#oko-lorwyn-liege--oko-shadowmoor-scion) · [Sauron, Lord of the Rings](cards/S/sau.md#sauron-lord-of-the-rings) · [Seed of Hope](cards/S/see.md#seed-of-hope) · [Sidisi, Brood Tyrant](cards/S/si.md#sidisi-brood-tyrant) · [Siegfried, Famed Swordsman](cards/S/si.md#siegfried-famed-swordsman) · [Six](cards/S/si.md#six) · [Stillness in Motion](cards/S/sti.md#stillness-in-motion) · [Tasigur, the Golden Fang](cards/T/ta.md#tasigur-the-golden-fang) · [Terra, Herald of Hope](cards/T/te.md#terra-herald-of-hope) · [Terra, Magical Adept // Esper Terra](cards/T/te.md#terra-magical-adept--esper-terra) · [Teval, the Balanced Scale](cards/T/te.md#teval-the-balanced-scale) · [The Necrobloom](cards/T/then.md#the-necrobloom) · [Thranduil, Sindarin Liege // Silvan Rally](cards/T/thr.md#thranduil-sindarin-liege--silvan-rally) · [Titania, Nature's Force](cards/T/ti.md#titania-natures-force) · [Tyvar, Jubilant Brawler](cards/T/ty.md#tyvar-jubilant-brawler) · [Vanille, Cheerful l'Cie](cards/V/va.md#vanille-cheerful-lcie) · [Vivien on the Hunt](cards/V/vi.md#vivien-on-the-hunt) · [Vorinclex // The Grand Evolution](cards/V/vo.md#vorinclex--the-grand-evolution) · [Wasteful Harvest](cards/W/was.md#wasteful-harvest) · [Winter, Cynical Opportunist](cards/W/wi.md#winter-cynical-opportunist) · [Wrenn and Realmbreaker](cards/W/wr.md#wrenn-and-realmbreaker) · [Zask, Skittering Swarmlord](cards/Z/za.md#zask-skittering-swarmlord)

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

Used in decks (≥ 3 matching cards, 6): [Karador, Ghost Chieftain](decks/karador-ghost-chieftain.md) 5 · [Sauron, Lord of the Rings (Grixis)](grixis/decks/sauron-lord-of-the-rings.md) 5 · [Sedris, the Traitor King (Grixis)](grixis/decks/sedris-the-traitor-king.md) 4 · [K'rrik, Son of Yawgmoth](decks/krrik-son-of-yawgmoth.md) 3 · [Be'lakor, the Dark Master (Grixis)](grixis/decks/belakor-the-dark-master.md) 3 · [Obeka, Brute Chronologist (Grixis)](grixis/decks/obeka-brute-chronologist.md) 3

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 25): [Anti-Venom, Horrifying Healer](cards/A/an.md#anti-venom-horrifying-healer) · [Ashiok, Sculptor of Fears](cards/A/as.md#ashiok-sculptor-of-fears) · [Chainer, Dementia Master](cards/C/cha.md#chainer-dementia-master) · [Dose of Dawnglow](cards/D/do.md#dose-of-dawnglow) · [Edgar's Awakening](cards/E/ed.md#edgars-awakening) · [Endless Obedience](cards/E/en.md#endless-obedience) · [Fearsome Awakening](cards/F/fe.md#fearsome-awakening) · [It Doesn't Add Up](cards/I/it.md#it-doesnt-add-up) · [Kenrith, the Returned King](cards/K/ke.md#kenrith-the-returned-king) · [Liliana, Death's Majesty](cards/L/li.md#liliana-deaths-majesty) · [Liliana, Waker of the Dead](cards/L/li.md#liliana-waker-of-the-dead) · [Mila, Crafty Companion // Lukka, Wayward Bonder](cards/M/mil.md#mila-crafty-companion--lukka-wayward-bonder) · [Olivia, Crimson Bride](cards/O/ol.md#olivia-crimson-bride) · [One Last Job](cards/O/on.md#one-last-job) · [Portal to Phyrexia](cards/P/po.md#portal-to-phyrexia) · [Reya Dawnbringer](cards/R/rey.md#reya-dawnbringer) · [Rise from the Grave](cards/R/ri.md#rise-from-the-grave) · [Sefris of the Hidden Ways](cards/S/sef.md#sefris-of-the-hidden-ways) · [Sheoldred's Restoration](cards/S/she.md#sheoldreds-restoration) · [Sheoldred, Whispering One](cards/S/she.md#sheoldred-whispering-one) · [Teneb, the Harvester](cards/T/te.md#teneb-the-harvester) · [The Cauldron of Eternity](cards/T/thec.md#the-cauldron-of-eternity) · [Whip of Erebos](cards/W/wh.md#whip-of-erebos) · [Whisper, Blood Liturgist](cards/W/wh.md#whisper-blood-liturgist) · [Xu-Ifit, Osteoharmonist](cards/X/xu.md#xu-ifit-osteoharmonist)

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

Used in decks (≥ 3 matching cards, 2): [Muldrotha, the Gravetide (self mill theme)](decks/theme-muldrotha-the-gravetide-self-mill.md) 4 · [Karador, Ghost Chieftain](decks/karador-ghost-chieftain.md) 3

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 39): [Aerith, Last Ancient](cards/A/ae.md#aerith-last-ancient) · [Cemetery Recruitment](cards/C/ce.md#cemetery-recruitment) · [Cid, Freeflier Pilot](cards/C/ci.md#cid-freeflier-pilot) · [Cormela, Glamour Thief](cards/C/cor.md#cormela-glamour-thief) · [Cruel Revival](cards/C/cr.md#cruel-revival) · [Dead Revels](cards/D/dea.md#dead-revels) · [Dutiful Return](cards/D/du.md#dutiful-return) · [Edgar's Awakening](cards/E/ed.md#edgars-awakening) · [Excavation Elephant](cards/E/ex.md#excavation-elephant) · [Extus, Oriq Overlord // Awaken the Blood Avatar](cards/E/ex.md#extus-oriq-overlord--awaken-the-blood-avatar) · [Flood of Recollection](cards/F/fl.md#flood-of-recollection) · [Glissa, the Traitor](cards/G/gl.md#glissa-the-traitor) · [Golbez, Crystal Collector](cards/G/gol.md#golbez-crystal-collector) · [Grub, Storied Matriarch // Grub, Notorious Auntie](cards/G/gru.md#grub-storied-matriarch--grub-notorious-auntie) · [Hanna, Ship's Navigator](cards/H/ha.md#hanna-ships-navigator) · [Honest Rutstein](cards/H/ho.md#honest-rutstein) · [Jared Carthalion](cards/J/ja.md#jared-carthalion) · [Kolaghan's Command](cards/K/ko.md#kolaghans-command) · [Layla Hassan](cards/L/la.md#layla-hassan) · [Liliana, Death Mage](cards/L/li.md#liliana-death-mage) · [Liliana, the Necromancer](cards/L/li.md#liliana-the-necromancer) · [Nature's Spiral](cards/N/na.md#natures-spiral) · [Nissa, Vital Force](cards/N/ni.md#nissa-vital-force) · [Palace Siege](cards/P/pa.md#palace-siege) · [Planewide Celebration](cards/P/pl.md#planewide-celebration) · [Pull from the Grave](cards/P/pu.md#pull-from-the-grave) · [Ravos, Soultender](cards/R/rav.md#ravos-soultender) · [Red XIII, Proud Warrior](cards/R/red.md#red-xiii-proud-warrior) · [Remember the Fallen](cards/R/rem.md#remember-the-fallen) · [Restore with Empathy](cards/R/res.md#restore-with-empathy) · [Samwise Gamgee](cards/S/sam.md#samwise-gamgee) · [Satsuki, the Living Lore](cards/S/sat.md#satsuki-the-living-lore) · [Sibsig Muckdraggers](cards/S/si.md#sibsig-muckdraggers) · [Tamiyo, Collector of Tales](cards/T/ta.md#tamiyo-collector-of-tales) · [Tamiyo, Inquisitive Student // Tamiyo, Seasoned Scholar](cards/T/ta.md#tamiyo-inquisitive-student--tamiyo-seasoned-scholar) · [Tezzeret, Master of the Bridge](cards/T/te.md#tezzeret-master-of-the-bridge) · [Tombstone, Career Criminal](cards/T/to.md#tombstone-career-criminal) · [Toph, Hardheaded Teacher](cards/T/to.md#toph-hardheaded-teacher) · [Wrenn and Six](cards/W/wr.md#wrenn-and-six)

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

Used in decks (≥ 3 matching cards, 1): [Trostani, Selesnya's Voice](decks/trostani-selesnyas-voice.md) 3

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 6): [Adrix and Nev, Twincasters](cards/A/ad.md#adrix-and-nev-twincasters) · [Anointed Procession](cards/A/an.md#anointed-procession) · [Bard, King of Dale](cards/B/bar.md#bard-king-of-dale) · [Elspeth, Storm Slayer](cards/E/el.md#elspeth-storm-slayer) · [Kaya, Geist Hunter](cards/K/ka.md#kaya-geist-hunter) · [Mondrak, Glory Dominus](cards/M/mon.md#mondrak-glory-dominus)

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

Used in decks (≥ 3 matching cards, 4): [Edgar Markov](decks/edgar-markov.md) 3 · [Giada, Font of Hope](decks/giada-font-of-hope.md) 3 · [Kozilek, the Great Distortion](decks/kozilek-the-great-distortion.md) 3 · [Edgar Markov (lifegain theme)](decks/theme-edgar-markov-lifegain.md) 3

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 40): [A Tale for the Ages](cards/A/at.md#a-tale-for-the-ages) · [Ajani Resolute](cards/A/aj.md#ajani-resolute) · [Always Watching](cards/A/al.md#always-watching) · [Arvad the Cursed](cards/A/arv.md#arvad-the-cursed) · [Call for Unity](cards/C/cal.md#call-for-unity) · [Captain of the Watch](cards/C/cap.md#captain-of-the-watch) · [Chief of the Foundry](cards/C/chi.md#chief-of-the-foundry) · [Chief of the Scale](cards/C/chi.md#chief-of-the-scale) · [Domri, Anarch of Bolas](cards/D/do.md#domri-anarch-of-bolas) · [Dwynen, Gilt-Leaf Daen](cards/D/dw.md#dwynen-gilt-leaf-daen) · [Elesh Norn, Grand Cenobite](cards/E/el.md#elesh-norn-grand-cenobite) · [Elspeth, Sun's Champion](cards/E/el.md#elspeth-suns-champion) · [Ethereal Absolution](cards/E/et.md#ethereal-absolution) · [Garruk, Cursed Huntsman](cards/G/ga.md#garruk-cursed-huntsman) · [Jetmir, Nexus of Revels](cards/J/je.md#jetmir-nexus-of-revels) · [Jor Kadeen, the Prevailer](cards/J/jo.md#jor-kadeen-the-prevailer) · [Judith, the Scourge Diva](cards/J/ju.md#judith-the-scourge-diva) · [Kellan, the Fae-Blooded // Birthright Boon](cards/K/ke.md#kellan-the-fae-blooded--birthright-boon) · [Kozilek, the Broken Reality](cards/K/ko.md#kozilek-the-broken-reality) · [Maja, Bretagard Protector](cards/M/maj.md#maja-bretagard-protector) · [Mikaeus, the Unhallowed](cards/M/mik.md#mikaeus-the-unhallowed) · [Minthara, Merciless Soul](cards/M/min.md#minthara-merciless-soul) · [Nadaar, Selfless Paladin](cards/N/na.md#nadaar-selfless-paladin) · [Raiders' Spoils](cards/R/rai.md#raiders-spoils) · [Ravos, Soultender](cards/R/rav.md#ravos-soultender) · [Reaper King](cards/R/rea.md#reaper-king) · [Rienne, Angel of Rebirth](cards/R/ri.md#rienne-angel-of-rebirth) · [Sentinel Sarah Lyons](cards/S/sen.md#sentinel-sarah-lyons) · [Serah Farron // Crystallized Serah](cards/S/ser.md#serah-farron--crystallized-serah) · [Seshiro the Anointed](cards/S/ses.md#seshiro-the-anointed) · [Sorin, Lord of Innistrad](cards/S/so.md#sorin-lord-of-innistrad) · [Sorin, Solemn Visitor](cards/S/so.md#sorin-solemn-visitor) · [Suki, Courageous Rescuer](cards/S/suk.md#suki-courageous-rescuer) · [The Cyber-Controller](cards/T/thec.md#the-cyber-controller) · [The Immortal Sun](cards/T/thei.md#the-immortal-sun) · [Tolsimir Wolfblood](cards/T/to.md#tolsimir-wolfblood) · [Trostani Discordant](cards/T/tro.md#trostani-discordant) · [Urza, Prince of Kroog](cards/U/ur.md#urza-prince-of-kroog) · [Vivien Reid](cards/V/vi.md#vivien-reid) · [Warleader's Call](cards/W/war.md#warleaders-call)

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

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 7): [Abuelo, Ancestral Echo](cards/A/ab.md#abuelo-ancestral-echo) · [Explosive Getaway](cards/E/ex.md#explosive-getaway) · [Getaway Glamer](cards/G/ge.md#getaway-glamer) · [Kykar, Zephyr Awakener](cards/K/ky.md#kykar-zephyr-awakener) · [Oath of Teferi](cards/O/oa.md#oath-of-teferi) · [The Eternal Wanderer](cards/T/thee.md#the-eternal-wanderer) · [Venser, the Sojourner](cards/V/ve.md#venser-the-sojourner)

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

Used in decks (≥ 3 matching cards, 1): [Brago, King Eternal](decks/brago-king-eternal.md) 3

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 4): [Elesh Norn, Mother of Machines](cards/E/el.md#elesh-norn-mother-of-machines) · [Gandalf the White](cards/G/ga.md#gandalf-the-white) · [Naban, Dean of Iteration](cards/N/na.md#naban-dean-of-iteration) · [Yarok, the Desecrated](cards/Y/ya.md#yarok-the-desecrated)

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

Used in decks (≥ 3 matching cards, 3): [Tatyova, Benthic Druid](decks/tatyova-benthic-druid.md) 10 · [Kynaios and Tiro of Meletis](decks/kynaios-and-tiro-of-meletis.md) 3 · [Omnath, Locus of Rage (Zendikar-only)](decks/plane-zendikar-omnath-locus-of-rage.md) 3

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 12): [Aesi, Tyrant of Gyre Strait](cards/A/ae.md#aesi-tyrant-of-gyre-strait) · [Azusa, Lost but Seeking](cards/A/az.md#azusa-lost-but-seeking) · [Explore](cards/E/ex.md#explore) · [Flubs, the Fool](cards/F/fl.md#flubs-the-fool) · [Hugs, Grisly Guardian](cards/H/hu.md#hugs-grisly-guardian) · [Kellan, Inquisitive Prodigy // Tail the Suspect](cards/K/ke.md#kellan-inquisitive-prodigy--tail-the-suspect) · [Kiora, the Crashing Wave](cards/K/ki.md#kiora-the-crashing-wave) · [Loot, Exuberant Explorer](cards/L/lo.md#loot-exuberant-explorer) · [Mina and Denn, Wildborn](cards/M/min.md#mina-and-denn-wildborn) · [Thalia and The Gitrog Monster](cards/T/tha.md#thalia-and-the-gitrog-monster) · [The Gitrog Monster](cards/T/theg.md#the-gitrog-monster) · [Zell Dincht](cards/Z/ze.md#zell-dincht)

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

Used in decks (≥ 3 matching cards, 6): [Omnath, Locus of Rage (Zendikar-only)](decks/plane-zendikar-omnath-locus-of-rage.md) 20 · [Chulane, Teller of Tales (landfall theme)](decks/theme-chulane-teller-of-tales-landfall.md) 17 · [Tatyova, Benthic Druid](decks/tatyova-benthic-druid.md) 15 · [Chulane, Teller of Tales](decks/chulane-teller-of-tales.md) 7 · [Nahiri, the Lithomancer](decks/lore-nahiri-the-lithomancer.md) 3 · [Muldrotha, the Gravetide (self mill theme)](decks/theme-muldrotha-the-gravetide-self-mill.md) 3

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 41): [Aesi, Tyrant of Gyre Strait](cards/A/ae.md#aesi-tyrant-of-gyre-strait) · [Ambrosia Whiteheart](cards/A/am.md#ambrosia-whiteheart) · [Bristly Bill, Spine Sower](cards/B/br.md#bristly-bill-spine-sower) · [Choco, Seeker of Paradise](cards/C/cho.md#choco-seeker-of-paradise) · [Cosima, God of the Voyage // The Omenkeel](cards/C/cos.md#cosima-god-of-the-voyage--the-omenkeel) · [Gladiolus Amicitia](cards/G/gl.md#gladiolus-amicitia) · [Greensleeves, Maro-Sorcerer](cards/G/gre.md#greensleeves-maro-sorcerer) · [Groundswell](cards/G/gro.md#groundswell) · [Khalni Heart Expedition](cards/K/kh.md#khalni-heart-expedition) · [Koth of the Homestead](cards/K/ko.md#koth-of-the-homestead) · [Koth, the Geomancer](cards/K/ko.md#koth-the-geomancer) · [Maja, Bretagard Protector](cards/M/maj.md#maja-bretagard-protector) · [Mole Man, Moloid Master](cards/M/mol.md#mole-man-moloid-master) · [Moraug, Fury of Akoum](cards/M/mor.md#moraug-fury-of-akoum) · [Nissa of Shadowed Boughs](cards/N/ni.md#nissa-of-shadowed-boughs) · [Nissa, Leyline Tamer](cards/N/ni.md#nissa-leyline-tamer) · [Nissa, Resurgent Animist](cards/N/ni.md#nissa-resurgent-animist) · [Nissa, Vastwood Seer // Nissa, Sage Animist](cards/N/ni.md#nissa-vastwood-seer--nissa-sage-animist) · [Nissa, Vital Force](cards/N/ni.md#nissa-vital-force) · [Nissa, Worldsoul Speaker](cards/N/ni.md#nissa-worldsoul-speaker) · [Ob Nixilis, the Fallen](cards/O/ob.md#ob-nixilis-the-fallen) · [Omnath, Locus of Creation](cards/O/om.md#omnath-locus-of-creation) · [Omnath, Locus of Rage](cards/O/om.md#omnath-locus-of-rage) · [Omnath, Locus of the Roil](cards/O/om.md#omnath-locus-of-the-roil) · [Phylath, World Sculptor](cards/P/ph.md#phylath-world-sculptor) · [Retreat to Coralhelm](cards/R/ret.md#retreat-to-coralhelm) · [Rydia, Summoner of Mist](cards/R/ry.md#rydia-summoner-of-mist) · [Surrakar Marauder](cards/S/sur.md#surrakar-marauder) · [Svega, the Unconventional](cards/S/sv.md#svega-the-unconventional) · [Tam, Observant Sequencer // Deep Sight](cards/T/ta.md#tam-observant-sequencer--deep-sight) · [Tannuk, Memorial Ensign](cards/T/ta.md#tannuk-memorial-ensign) · [Tatyova, Benthic Druid](cards/T/ta.md#tatyova-benthic-druid) · [Tatyova, Steward of Tides](cards/T/ta.md#tatyova-steward-of-tides) · [The Necrobloom](cards/T/then.md#the-necrobloom) · [Thranduil, Sindarin Liege // Silvan Rally](cards/T/thr.md#thranduil-sindarin-liege--silvan-rally) · [Tifa Lockhart](cards/T/ti.md#tifa-lockhart) · [Toggo, Goblin Weaponsmith](cards/T/to.md#toggo-goblin-weaponsmith) · [Toph, Earthbending Master](cards/T/to.md#toph-earthbending-master) · [Zendikar's Roil](cards/Z/ze.md#zendikars-roil) · [Zimone, Mystery Unraveler](cards/Z/zi.md#zimone-mystery-unraveler) · [Zo-Zu the Punisher](cards/Z/zo.md#zo-zu-the-punisher)

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

Used in decks (≥ 3 matching cards, 4): [Tatyova, Benthic Druid](decks/tatyova-benthic-druid.md) 6 · [Karador, Ghost Chieftain](decks/karador-ghost-chieftain.md) 4 · [Muldrotha, the Gravetide](decks/muldrotha-the-gravetide.md) 3 · [Muldrotha, the Gravetide (self mill theme)](decks/theme-muldrotha-the-gravetide-self-mill.md) 3

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 7): [Altanak, the Thrice-Called](cards/A/al.md#altanak-the-thrice-called) · [Crucible of Worlds](cards/C/cr.md#crucible-of-worlds) · [Erinis, Gloom Stalker](cards/E/er.md#erinis-gloom-stalker) · [Lumra, Bellow of the Woods](cards/L/lu.md#lumra-bellow-of-the-woods) · [Mole Man, Moloid Master](cards/M/mol.md#mole-man-moloid-master) · [Szarel, Genesis Shepherd](cards/S/sz.md#szarel-genesis-shepherd) · [Titania, Protector of Argoth](cards/T/ti.md#titania-protector-of-argoth)

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

Used in decks (≥ 3 matching cards, 6): [Ashad, the Lone Cyberman (Grixis)](grixis/decks/ashad-the-lone-cyberman.md) 7 · [Breya, Etherium Shaper](decks/breya-etherium-shaper.md) 6 · [Ashnod the Uncaring (Grixis)](grixis/decks/ashnod-the-uncaring.md) 5 · [Prosper, Tome-Bound](decks/prosper-tome-bound.md) 3 · [Dr. Eggman (Grixis)](grixis/decks/dr-eggman.md) 3 · [Mishra, Artificer Prodigy (Grixis)](grixis/decks/mishra-artificer-prodigy.md) 3

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 15): [Captain Storm, Cosmium Raider](cards/C/cap.md#captain-storm-cosmium-raider) · [Chandra, Spark Hunter](cards/C/cha.md#chandra-spark-hunter) · [Contraband Kingpin](cards/C/con.md#contraband-kingpin) · [Dr. Madison Li](cards/D/drm.md#dr-madison-li) · [Golbez, Crystal Collector](cards/G/gol.md#golbez-crystal-collector) · [Iron Man, Bleeding Edge](cards/I/ir.md#iron-man-bleeding-edge) · [Krenko, Baron of Tin Street](cards/K/kr.md#krenko-baron-of-tin-street) · [Mendicant Core, Guidelight](cards/M/me.md#mendicant-core-guidelight) · [Mishra, Artificer Prodigy](cards/M/mis.md#mishra-artificer-prodigy) · [Mm'menon, Uthros Exile](cards/M/mm.md#mmmenon-uthros-exile) · [Ovalchase Daredevil](cards/O/ov.md#ovalchase-daredevil) · [Sai, Master Thopterist](cards/S/sai.md#sai-master-thopterist) · [Syr Ginger, the Meal Ender](cards/S/sy.md#syr-ginger-the-meal-ender) · [Tezzeret, Cruel Captain](cards/T/te.md#tezzeret-cruel-captain) · [Ultron, Artificial Malevolence](cards/U/ul.md#ultron-artificial-malevolence)

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

Used in decks (≥ 3 matching cards, 6): [Breya, Etherium Shaper](decks/breya-etherium-shaper.md) 3 · [Ashad, the Lone Cyberman (Grixis)](grixis/decks/ashad-the-lone-cyberman.md) 3 · [Ashnod the Uncaring (Grixis)](grixis/decks/ashnod-the-uncaring.md) 3 · [Cult of Skaro (Grixis)](grixis/decks/cult-of-skaro.md) 3 · [Mai and Zuko (Grixis)](grixis/decks/mai-and-zuko.md) 3 · [Mishra, Artificer Prodigy (Grixis)](grixis/decks/mishra-artificer-prodigy.md) 3

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 2): [Saheeli, Filigree Master](cards/S/sah.md#saheeli-filigree-master) · [Shuri, Wakandan Inventor](cards/S/shu.md#shuri-wakandan-inventor)

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

Used in decks (≥ 3 matching cards, 6): [Garza Zol, Plague Queen (Grixis)](grixis/decks/garza-zol-plague-queen.md) 6 · [Obeka, Splitter of Seconds (Grixis)](grixis/decks/obeka-splitter-of-seconds.md) 5 · [Tetsuo, Imperial Champion (Grixis)](grixis/decks/tetsuo-imperial-champion.md) 5 · [Zur the Enchanter](decks/zur-the-enchanter.md) 3 · [Crosis, the Purger (Grixis)](grixis/decks/crosis-the-purger.md) 3 · [Nicol Bolas (Grixis)](grixis/decks/nicol-bolas.md) 3

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 3): [Fae Flight](cards/F/fa.md#fae-flight) · [Mask of Avacyn](cards/M/mas.md#mask-of-avacyn) · [Shardmage's Rescue](cards/S/sha.md#shardmages-rescue)

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

Used in decks (≥ 3 matching cards, 5): [Tetsuo, Imperial Champion (Grixis)](grixis/decks/tetsuo-imperial-champion.md) 5 · [Yidris, Maelstrom Wielder](decks/yidris-maelstrom-wielder.md) 4 · [Garza Zol, Plague Queen (Grixis)](grixis/decks/garza-zol-plague-queen.md) 4 · [Obeka, Splitter of Seconds (Grixis)](grixis/decks/obeka-splitter-of-seconds.md) 4 · [Uro, Titan of Nature's Wrath (Theros-only)](decks/plane-theros-uro-titan-of-natures-wrath.md) 3

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 7): [Angelic Gift](cards/A/an.md#angelic-gift) · [Call of the Full Moon](cards/C/cal.md#call-of-the-full-moon) · [Consecrated by Blood](cards/C/con.md#consecrated-by-blood) · [Ephara's Enlightenment](cards/E/ep.md#epharas-enlightenment) · [Fae Flight](cards/F/fa.md#fae-flight) · [Luxior, Ignited](cards/L/lu.md#luxior-ignited) · [Take Flight](cards/T/ta.md#take-flight)

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

Used in decks (≥ 3 matching cards, 12): [Edward Kenway (Grixis)](grixis/decks/edward-kenway.md) 10 · [Korvold, Fae-Cursed King](decks/korvold-fae-cursed-king.md) 8 · [Prosper, Tome-Bound](decks/prosper-tome-bound.md) 8 · [Admiral Brass, Unsinkable (Grixis)](grixis/decks/admiral-brass-unsinkable.md) 7 · [Admiral Beckett Brass (Grixis)](grixis/decks/admiral-beckett-brass.md) 6 · [Don Andres, the Renegade (Grixis)](grixis/decks/don-andres-the-renegade.md) 6 · [Nathan Drake, Treasure Hunter (Grixis)](grixis/decks/nathan-drake-treasure-hunter.md) 5 · [Goro-Goro and Satoru (Grixis)](grixis/decks/goro-goro-and-satoru.md) 4 · [The Ur-Dragon](decks/the-ur-dragon.md) 3 · [The Rani (Grixis)](grixis/decks/the-rani.md) 3 · [Thraximundar (Grixis)](grixis/decks/thraximundar.md) 3 · [Tresserhorn's Lord, Returned (Grixis)](grixis/decks/tresserhorns-lord-returned.md) 3

Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, 27): [Baeloth Barrityl, Entertainer](cards/B/bae.md#baeloth-barrityl-entertainer) · [Bilbo, Retired Burglar](cards/B/bi.md#bilbo-retired-burglar) · [Breeches, Eager Pillager](cards/B/br.md#breeches-eager-pillager) · [Burakos, Party Leader](cards/B/bu.md#burakos-party-leader) · [Captain Lannery Storm](cards/C/cap.md#captain-lannery-storm) · [Edward Kenway](cards/E/ed.md#edward-kenway) · [Gadrak, the Crown-Scourge](cards/G/ga.md#gadrak-the-crown-scourge) · [Ganax, Astral Hunter](cards/G/ga.md#ganax-astral-hunter) · [Gimli of the Glittering Caves](cards/G/gi.md#gimli-of-the-glittering-caves) · [Glóin, Dwarf Emissary](cards/G/gl.md#glóin-dwarf-emissary) · [Iron Man, Titan of Innovation](cards/I/ir.md#iron-man-titan-of-innovation) · [J. Jonah Jameson](cards/J/jj.md#j-jonah-jameson) · [Kellogg, Dangerous Mind](cards/K/ke.md#kellogg-dangerous-mind) · [Knuckles the Echidna](cards/K/kn.md#knuckles-the-echidna) · [Lotho, Corrupt Shirriff](cards/L/lo.md#lotho-corrupt-shirriff) · [Magda, Brazen Outlaw](cards/M/mag.md#magda-brazen-outlaw) · [Mahadi, Emporium Master](cards/M/mah.md#mahadi-emporium-master) · [Malcolm, Keen-Eyed Navigator](cards/M/mal.md#malcolm-keen-eyed-navigator) · [Old Gnawbone](cards/O/ol.md#old-gnawbone) · [Olivia, Opulent Outlaw](cards/O/ol.md#olivia-opulent-outlaw) · [Prosper, Tome-Bound](cards/P/pr.md#prosper-tome-bound) · [Ragavan, Nimble Pilferer](cards/R/rag.md#ragavan-nimble-pilferer) · [Rev, Tithe Extractor](cards/R/rev.md#rev-tithe-extractor) · [Smaug the Impenetrable](cards/S/sm.md#smaug-the-impenetrable) · [Smaug the Magnificent](cards/S/sm.md#smaug-the-magnificent) · [Ultimate Green Goblin](cards/U/ul.md#ultimate-green-goblin) · [Zidane, Tantalus Thief](cards/Z/zi.md#zidane-tantalus-thief)

Budget options beyond the top 10 (≤ $1.00): [Captain Lannery Storm](cards/C/cap.md#captain-lannery-storm) (R, $0.26) · [Mahadi, Emporium Master](cards/M/mah.md#mahadi-emporium-master) (BR, $0.44) · [Shiny Impetus](cards/S/shi.md#shiny-impetus) (R, $0.13) · [Sticky Fingers](cards/S/sti.md#sticky-fingers) (R, $0.23)

## Method

- Each sub-package is a regex on Oracle text over Commander-legal cards (case-insensitive), shown with the section. Matches are heuristics, so some cards fit loosely.
- Related: [EDH Mana Bases](EDH%20Mana%20Bases.md) · [EDH Win Conditions](EDH%20Win%20Conditions.md) · [EDH Interaction](EDH%20Interaction.md) · [EDH Archetypes](EDH%20Archetypes.md) · [EDH Staples](EDH%20Staples.md).
