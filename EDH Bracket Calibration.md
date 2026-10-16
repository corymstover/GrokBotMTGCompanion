---
title: "EDH Bracket Calibration"
category: edh
tags: [brackets, calibration, game-changers, combos, pilot-notes]
issues: [68, 95]
generated_by: scripts/deck_calibration.py
sources: [scryfall, spellbook, edhrec, wotc-articles]
related: ["EDH Standards.md", "EDH Lore-Themed Deckbuilding.md", "cEDH Primer.md", "grixis/README.md"]
schema: 2
---

# EDH Bracket Calibration

> **Auto-generated** by `scripts/deck_calibration.py` (Bot cycle 19, issue [#68](https://github.com/corymstover/GrokBotMTGCompanion/issues/68)). One row per deck in [decks/](decks/) and [grixis/decks/](grixis/README.md). Floors are facts from the official barometers ([EDH Standards → Power bracket assessment](EDH%20Standards.md#power-bracket-assessment)); stated targets and community data are context; every deck page carries the full rationale and pilot notes (guidance).

## Contents
- [Summary](#summary)
- [All decks](#all-decks)
- [Targets below the floor](#targets-below-the-floor)
- [Lore decks](#lore-decks)
- [Method](#method)

## Summary

- **110 decks**: floor Bracket 2: **12** · Bracket 3: **32** · Bracket 4: **66**.
- Set by Game Changers (> 3): 66 · mass land denial: 1 · two-card infinites: 52 decks (193 combos).
- Decks with extra-turn cards: 24 · median tutors per deck: 3.
- Pending legality (Bot cycle 38): 2 deck(s), calibrated here but not Commander-legal yet (marked ⏳).
- Grixis source targets: 53 stated; 0 below the floor.

## All decks

| Deck | Kind | Identity | Floor | GC | 2-card ∞ | MLD | Extra turns | Tutors | Lands | Avg MV | Stated target | EDHREC mode |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Animar, Soul of Elements](decks/animar-soul-of-elements.md#bracket-calibration--pilot-notes) | core | URG | **4** | 5 | 3 | 0 | 0 | 3 | 36 | 3.83 | — | 3 |
| [Atraxa, Praetors' Voice](decks/atraxa-praetors-voice.md#bracket-calibration--pilot-notes) | core | WUBG | **4** | 5 | 0 | 0 | 1 | 4 | 36 | 2.76 | — | 3 |
| [Chulane, Teller of Tales](decks/chulane-teller-of-tales.md#bracket-calibration--pilot-notes) | core | WUG | **4** | 6 | 3 | 0 | 0 | 5 | 36 | 2.48 | — | 3 |
| [K'rrik, Son of Yawgmoth](decks/krrik-son-of-yawgmoth.md#bracket-calibration--pilot-notes) | core | B | **4** | 7 | 5 | 0 | 0 | 15 | 36 | 3.11 | — | 4 |
| [Korvold, Fae-Cursed King](decks/korvold-fae-cursed-king.md#bracket-calibration--pilot-notes) | core | BRG | **4** | 4 | 1 | 0 | 0 | 6 | 36 | 2.67 | — | 3 |
| [Kykar, Wind's Fury](decks/kykar-winds-fury.md#bracket-calibration--pilot-notes) | core | WUR | **4** | 6 | 0 | 0 | 0 | 1 | 36 | 2.25 | — | 3 |
| [Niv-Mizzet, Parun](decks/niv-mizzet-parun.md#bracket-calibration--pilot-notes) | core | UR | **4** | 4 | 8 | 0 | 0 | 1 | 36 | 2.51 | — | 3 |
| [Yuriko, the Tiger's Shadow](decks/yuriko-the-tigers-shadow.md#bracket-calibration--pilot-notes) | core | UB | **4** | 4 | 0 | 0 | 1 | 3 | 36 | 3.06 | — | 3 |
| [Zur the Enchanter](decks/zur-the-enchanter.md#bracket-calibration--pilot-notes) | core | WUB | **4** | 8 | 0 | 0 | 0 | 4 | 36 | 2.32 | — | 4 |
| [Abaddon the Despoiler](grixis/decks/abaddon-the-despoiler.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 14 | 0 | 0 | 0 | 6 | 34 | 2.58 | 4 | — |
| [Admiral Beckett Brass](grixis/decks/admiral-beckett-brass.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 6 | 0 | 0 | 0 | 3 | 35 | 2.75 | — | — |
| [Admiral Brass, Unsinkable](grixis/decks/admiral-brass-unsinkable.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 6 | 0 | 0 | 0 | 5 | 34 | 2.95 | — | — |
| [Anhelo, the Painter](grixis/decks/anhelo-the-painter.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 7 | 5 | 0 | 1 | 4 | 34 | 2.83 | — | — |
| [Ashnod the Uncaring](grixis/decks/ashnod-the-uncaring.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 6 | 0 | 0 | 1 | 5 | 33 | 2.21 | — | — |
| [Be'lakor, the Dark Master](grixis/decks/belakor-the-dark-master.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 5 | 1 | 0 | 0 | 4 | 36 | 4.08 | — | — |
| [Bjorna, Nightfall Alchemist + Cecily, Haunted Mage](grixis/decks/bjorna-nightfall-alchemist-cecily.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 10 | 2 | 0 | 0 | 4 | 33 | 3.34 | — | — |
| [Cormela, Glamour Thief](grixis/decks/cormela-glamour-thief.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 20 | 2 | 0 | 0 | 8 | 30 | 1.84 | — | — |
| [Crosis, the Purger](grixis/decks/crosis-the-purger.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 14 | 0 | 0 | 0 | 4 | 36 | 2.29 | 4 | — |
| [Davros, Dalek Creator](grixis/decks/davros-dalek-creator.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 5 | 0 | 0 | 0 | 1 | 34 | 3.18 | 4 | — |
| [Doctor Doom, King of Latveria](grixis/decks/doctor-doom-king-of-latveria.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 6 | 0 | 0 | 0 | 3 | 38 | 2.85 | 4 | — |
| [Don Andres, the Renegade](grixis/decks/don-andres-the-renegade.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 5 | 0 | 0 | 0 | 1 | 35 | 3.31 | 4 | — |
| [Edward Kenway](grixis/decks/edward-kenway.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 10 | 5 | 0 | 1 | 3 | 35 | 2.8 | 4 | — |
| [Evelyn, the Covetous](grixis/decks/evelyn-the-covetous.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 19 | 3 | 0 | 1 | 8 | 26 | 1.84 | 5 | — |
| [Fire Lord Azula](grixis/decks/fire-lord-azula.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 20 | 1 | 0 | 0 | 7 | 26 | 1.85 | 5 | — |
| [Garza Zol, Plague Queen](grixis/decks/garza-zol-plague-queen.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 9 | 2 | 0 | 0 | 2 | 38 | 2.21 | 4 | — |
| [Goro-Goro and Satoru](grixis/decks/goro-goro-and-satoru.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 6 | 5 | 0 | 0 | 2 | 33 | 2.53 | 4 | — |
| [Gwendlyn Di Corci](grixis/decks/gwendlyn-di-corci.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 17 | 0 | 0 | 0 | 5 | 35 | 2.33 | 4 | — |
| [Inalla, Archmage Ritualist](grixis/decks/inalla-archmage-ritualist.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 18 | 0 | 0 | 1 | 14 | 27 | 2.0 | 5 | — |
| [Jeleva, Nephalia's Scourge](grixis/decks/jeleva-nephalias-scourge.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 20 | 0 | 0 | 1 | 8 | 27 | 1.9 | 5 | — |
| [Kefka, Court Mage // Kefka, Ruler of Ruin](grixis/decks/kefka-court-mage.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 20 | 0 | 0 | 1 | 9 | 28 | 1.94 | 5 | — |
| [Kess, Dissident Mage](grixis/decks/kess-dissident-mage.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 21 | 1 | 0 | 1 | 11 | 27 | 1.85 | 5 | — |
| [Kraum, Ludevic's Opus + Tevesh Szat, Doom of Fools](grixis/decks/grixistax-october-2026.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 22 | 0 | 1 | 0 | 8 | 26 | 2.06 | 5 | — |
| [Loki, the Deceiver](grixis/decks/loki-the-deceiver.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 5 | 0 | 0 | 0 | 1 | 34 | 3.38 | 4 | — |
| [Lord Xander, the Collector](grixis/decks/lord-xander-the-collector.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 20 | 7 | 0 | 0 | 6 | 33 | 2.33 | 4 | — |
| [Lynde, Cheerful Tormentor](grixis/decks/lynde-cheerful-tormentor.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 8 | 0 | 0 | 0 | 5 | 35 | 3.22 | 4 | — |
| [Mai and Zuko](grixis/decks/mai-and-zuko.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 15 | 1 | 0 | 0 | 4 | 31 | 2.6 | 4 | — |
| [Mairsil, the Pretender](grixis/decks/mairsil-the-pretender.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 13 | 0 | 0 | 0 | 9 | 32 | 2.81 | 4 | — |
| [Marchesa, Dealer of Death](grixis/decks/marchesa-dealer-of-death.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 18 | 1 | 0 | 2 | 5 | 29 | 1.87 | 5 | — |
| [Marchesa, the Black Rose](grixis/decks/marchesa-the-black-rose.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 5 | 38 | 0 | 0 | 4 | 34 | 2.82 | 4 | — |
| [Mishra, Artificer Prodigy](grixis/decks/mishra-artificer-prodigy.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 15 | 1 | 0 | 0 | 10 | 29 | 2.66 | 5 | — |
| [Mishra, Eminent One](grixis/decks/mishra-eminent-one.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 14 | 1 | 0 | 1 | 8 | 34 | 2.78 | 4 | — |
| [Missy](grixis/decks/missy.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 7 | 0 | 0 | 0 | 3 | 35 | 2.72 | 4 | — |
| [Nathan Drake, Treasure Hunter](grixis/decks/nathan-drake-treasure-hunter.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 9 | 0 | 0 | 0 | 2 | 34 | 2.91 | 4 | — |
| [Nekusar, the Mindrazer](grixis/decks/nekusar-the-mindrazer.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 15 | 5 | 0 | 0 | 3 | 35 | 2.67 | 4 | — |
| [Nicol Bolas](grixis/decks/nicol-bolas.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 14 | 1 | 0 | 0 | 2 | 37 | 2.48 | 4 | — |
| [Nicol Bolas, the Ravager // Nicol Bolas, the Arisen](grixis/decks/nicol-bolas-the-ravager.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 16 | 1 | 0 | 2 | 5 | 34 | 3.14 | 4 | — |
| [Norman Osborn // Green Goblin](grixis/decks/norman-osborn.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 19 | 1 | 0 | 1 | 9 | 23 | 1.87 | 5 | — |
| [Obeka, Brute Chronologist](grixis/decks/obeka-brute-chronologist.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 13 | 2 | 0 | 4 | 4 | 34 | 2.78 | 4 | — |
| [Obeka, Splitter of Seconds](grixis/decks/obeka-splitter-of-seconds.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 6 | 0 | 0 | 1 | 4 | 35 | 2.89 | 4 | — |
| [Rograkh, Son of Rohgahh + Silas Renn, Seeker Adept](grixis/decks/rograkh-son-of-rohgahh-silas-renn.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 19 | 1 | 0 | 2 | 9 | 24 | 1.82 | 5 | — |
| [Saruman, the White Hand](grixis/decks/saruman-the-white-hand.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 11 | 1 | 0 | 0 | 4 | 31 | 3.35 | 4 | — |
| [Sauron, Lord of the Rings](grixis/decks/sauron-lord-of-the-rings.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 11 | 0 | 0 | 0 | 5 | 32 | 3.53 | 4 | — |
| [Sauron, the Dark Lord](grixis/decks/sauron-the-dark-lord.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 12 | 0 | 0 | 0 | 5 | 34 | 2.97 | 4 | — |
| [Sedris, the Traitor King](grixis/decks/sedris-the-traitor-king.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 12 | 1 | 0 | 0 | 9 | 31 | 3.43 | 4 | — |
| [Sol'Kanar the Tainted](grixis/decks/solkanar-the-tainted.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 7 | 0 | 0 | 0 | 2 | 35 | 3.03 | 4 | — |
| [Sol'kanar the Swamp King](grixis/decks/solkanar-the-swamp-king.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 13 | 11 | 0 | 0 | 4 | 35 | 2.66 | 4 | — |
| [Tetsuo Umezawa](grixis/decks/tetsuo-umezawa.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 4 | 1 | 0 | 0 | 2 | 35 | 2.75 | 4 | — |
| [Tetsuo, Imperial Champion](grixis/decks/tetsuo-imperial-champion.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 5 | 2 | 0 | 0 | 4 | 35 | 3.19 | 4 | — |
| [The Madcap Jester](grixis/decks/the-madcap-jester.md#bracket-calibration--pilot-notes) ⏳ *pending legality* | grixis | UBR | **4** | 17 | 0 | 0 | 0 | 6 | 34 | 2.4 | 5 | — |
| [The Rani](grixis/decks/the-rani.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 8 | 0 | 0 | 1 | 3 | 33 | 3.02 | 4 | — |
| [The Valeyard](grixis/decks/the-valeyard.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 6 | 0 | 0 | 2 | 2 | 36 | 3.6 | 4 | — |
| [Thraximundar](grixis/decks/thraximundar.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 8 | 1 | 0 | 0 | 3 | 36 | 2.78 | 4 | — |
| [Wick, the Whorled Mind](grixis/decks/wick-the-whorled-mind.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 5 | 1 | 0 | 0 | 3 | 35 | 2.55 | 4 | — |
| [Zevlor, Elturel Exile](grixis/decks/zevlor-elturel-exile.md#bracket-calibration--pilot-notes) | grixis | UBR | **4** | 11 | 1 | 0 | 0 | 4 | 34 | 2.74 | 4 | — |
| [Atraxa, Praetors' Voice — Planeswalkers theme](decks/theme-atraxa-praetors-voice-planeswalkers.md#bracket-calibration--pilot-notes) | theme | WUBG | **4** | 7 | 2 | 0 | 2 | 4 | 36 | 3.43 | — | 3 |
| [Edgar Markov — Lifegain theme](decks/theme-edgar-markov-lifegain.md#bracket-calibration--pilot-notes) | theme | WBR | **4** | 4 | 6 | 0 | 0 | 4 | 36 | 2.95 | — | 3 |
| [Brago, King Eternal](decks/brago-king-eternal.md#bracket-calibration--pilot-notes) | core | WU | **3** | 1 | 4 | 0 | 0 | 1 | 36 | 2.95 | — | 3 |
| [Breya, Etherium Shaper](decks/breya-etherium-shaper.md#bracket-calibration--pilot-notes) | core | WUBR | **3** | 3 | 0 | 0 | 1 | 3 | 36 | 3.05 | — | 3 |
| [Edgar Markov](decks/edgar-markov.md#bracket-calibration--pilot-notes) | core | WBR | **3** | 3 | 6 | 0 | 0 | 3 | 36 | 2.81 | — | 3 |
| [Giada, Font of Hope](decks/giada-font-of-hope.md#bracket-calibration--pilot-notes) | core | W | **3** | 3 | 0 | 0 | 0 | 2 | 36 | 3.68 | — | 3 |
| [Gishath, Sun's Avatar](decks/gishath-suns-avatar.md#bracket-calibration--pilot-notes) | core | WRG | **3** | 0 | 1 | 0 | 0 | 4 | 36 | 4.35 | — | 2 |
| [Kozilek, the Great Distortion](decks/kozilek-the-great-distortion.md#bracket-calibration--pilot-notes) | core | C | **3** | 1 | 1 | 0 | 2 | 2 | 36 | 5.32 | — | 3 |
| [Kynaios and Tiro of Meletis](decks/kynaios-and-tiro-of-meletis.md#bracket-calibration--pilot-notes) | core | WURG | **3** | 1 | 0 | 0 | 0 | 3 | 36 | 3.03 | — | 3 |
| [Lathril, Blade of the Elves](decks/lathril-blade-of-the-elves.md#bracket-calibration--pilot-notes) | core | BG | **3** | 1 | 0 | 0 | 0 | 2 | 36 | 3.13 | — | 2 |
| [Muldrotha, the Gravetide](decks/muldrotha-the-gravetide.md#bracket-calibration--pilot-notes) | core | UBG | **3** | 1 | 0 | 0 | 0 | 4 | 36 | 2.65 | — | 3 |
| [Nekusar, the Mindrazer](decks/nekusar-the-mindrazer.md#bracket-calibration--pilot-notes) | core | UBR | **3** | 2 | 5 | 0 | 0 | 0 | 36 | 2.95 | — | 3 |
| [Prosper, Tome-Bound](decks/prosper-tome-bound.md#bracket-calibration--pilot-notes) | core | BR | **3** | 1 | 0 | 0 | 0 | 0 | 36 | 3.08 | — | 3 |
| [Saskia the Unyielding](decks/saskia-the-unyielding.md#bracket-calibration--pilot-notes) | core | WBRG | **3** | 1 | 0 | 0 | 0 | 3 | 36 | 3.11 | — | 2 |
| [Selvala, Heart of the Wilds](decks/selvala-heart-of-the-wilds.md#bracket-calibration--pilot-notes) | core | G | **3** | 2 | 9 | 0 | 0 | 9 | 36 | 3.33 | — | 4 |
| [Talrand, Sky Summoner](decks/talrand-sky-summoner.md#bracket-calibration--pilot-notes) | core | U | **3** | 3 | 1 | 0 | 0 | 1 | 36 | 2.51 | — | 2 |
| [Tatyova, Benthic Druid](decks/tatyova-benthic-druid.md#bracket-calibration--pilot-notes) | core | UG | **3** | 2 | 0 | 0 | 0 | 4 | 36 | 2.79 | — | 2 |
| [Teysa Karlov](decks/teysa-karlov.md#bracket-calibration--pilot-notes) | core | WB | **3** | 2 | 0 | 0 | 0 | 1 | 36 | 2.76 | — | 3 |
| [The Ur-Dragon](decks/the-ur-dragon.md#bracket-calibration--pilot-notes) | core | WUBRG | **3** | 3 | 1 | 0 | 0 | 4 | 36 | 4.48 | — | 3 |
| [Trostani, Selesnya's Voice](decks/trostani-selesnyas-voice.md#bracket-calibration--pilot-notes) | core | WG | **3** | 1 | 0 | 0 | 0 | 3 | 36 | 3.1 | — | 2 |
| [Xenagos, God of Revels](decks/xenagos-god-of-revels.md#bracket-calibration--pilot-notes) | core | RG | **3** | 0 | 3 | 0 | 0 | 3 | 36 | 4.05 | — | 3 |
| [Ashad, the Lone Cyberman](grixis/decks/ashad-the-lone-cyberman.md#bracket-calibration--pilot-notes) | grixis | UBR | **3** | 3 | 0 | 0 | 0 | 2 | 30 | 3.41 | — | — |
| [Cult of Skaro](grixis/decks/cult-of-skaro.md#bracket-calibration--pilot-notes) | grixis | UBR | **3** | 3 | 1 | 0 | 0 | 0 | 34 | 3.35 | 4 | — |
| [Dr. Eggman](grixis/decks/dr-eggman.md#bracket-calibration--pilot-notes) | grixis | UBR | **3** | 3 | 0 | 0 | 0 | 3 | 31 | 4.21 | 4 | — |
| [Edea, Possessed Sorceress](grixis/decks/edea-possessed-sorceress.md#bracket-calibration--pilot-notes) | grixis | UBR | **3** | 3 | 0 | 0 | 0 | 2 | 35 | 3.2 | 4 | — |
| [Lord of Tresserhorn](grixis/decks/lord-of-tresserhorn.md#bracket-calibration--pilot-notes) | grixis | UBR | **3** | 2 | 1 | 0 | 0 | 3 | 35 | 2.44 | 4 | — |
| [Parnesse, the Subtle Brush](grixis/decks/parnesse-the-subtle-brush.md#bracket-calibration--pilot-notes) | grixis | UBR | **3** | 3 | 21 | 0 | 0 | 1 | 35 | 3.0 | 4 | — |
| [Tresserhorn's Lord, Returned](grixis/decks/tresserhorns-lord-returned.md#bracket-calibration--pilot-notes) ⏳ *pending legality* | grixis | UBR | **3** | 2 | 1 | 0 | 0 | 4 | 33 | 2.7 | — | — |
| [Aurelia, the Warleader — Ravnica-only](decks/plane-ravnica-aurelia-the-warleader.md#bracket-calibration--pilot-notes) | plane | WR | **3** | 1 | 0 | 0 | 1 | 1 | 36 | 3.78 | — | 2 |
| [Braids, Arisen Nightmare — Dominaria-only](decks/plane-dominaria-braids-arisen-nightmare.md#bracket-calibration--pilot-notes) | plane | B | **3** | 0 | 1 | 0 | 0 | 3 | 36 | 3.24 | — | 3 |
| [Elesh Norn, Mother of Machines — Mirrodin/New Phyrexia-only](decks/plane-new-phyrexia-elesh-norn-mother-of-machines.md#bracket-calibration--pilot-notes) | plane | W | **3** | 1 | 0 | 0 | 0 | 0 | 36 | 3.32 | — | 3 |
| [Isshin, Two Heavens as One — Kamigawa-only](decks/plane-kamigawa-isshin-two-heavens-as-one.md#bracket-calibration--pilot-notes) | plane | WBR | **3** | 1 | 0 | 0 | 0 | 4 | 36 | 3.25 | — | 2 |
| [Uro, Titan of Nature's Wrath — Theros-only](decks/plane-theros-uro-titan-of-natures-wrath.md#bracket-calibration--pilot-notes) | plane | UG | **3** | 1 | 0 | 0 | 0 | 0 | 36 | 3.44 | — | 3 |
| [Chulane, Teller of Tales — Landfall theme](decks/theme-chulane-teller-of-tales-landfall.md#bracket-calibration--pilot-notes) | theme | WUG | **3** | 1 | 3 | 0 | 0 | 3 | 36 | 3.11 | — | — |
| [Feather, the Redeemed](decks/feather-the-redeemed.md#bracket-calibration--pilot-notes) | core | WR | **2** | 0 | 0 | 0 | 0 | 1 | 36 | 2.11 | — | 2 |
| [Karador, Ghost Chieftain](decks/karador-ghost-chieftain.md#bracket-calibration--pilot-notes) | core | WBG | **2** | 0 | 0 | 0 | 0 | 6 | 36 | 2.68 | — | 3 |
| [Krenko, Mob Boss](decks/krenko-mob-boss.md#bracket-calibration--pilot-notes) | core | R | **2** | 0 | 0 | 0 | 0 | 1 | 36 | 2.59 | — | 2 |
| [Yidris, Maelstrom Wielder](decks/yidris-maelstrom-wielder.md#bracket-calibration--pilot-notes) | core | UBRG | **2** | 0 | 0 | 0 | 0 | 4 | 36 | 3.63 | — | 2 |
| [Lore Deck — Nahiri, the Lithomancer](decks/lore-nahiri-the-lithomancer.md#bracket-calibration--pilot-notes) | lore | W | **2** | 0 | 0 | 0 | 0 | 4 | 36 | 2.57 | — | — |
| [Lore Deck — The Brothers' War (Urza, Lord High Artificer)](decks/lore-brothers-war-urza-lord-high-artificer.md#bracket-calibration--pilot-notes) | lore | U | **2** | 0 | 0 | 0 | 0 | 2 | 37 | 2.98 | — | — |
| [Atarka, World Render — Tarkir-only](decks/plane-tarkir-atarka-world-render.md#bracket-calibration--pilot-notes) | plane | RG | **2** | 0 | 0 | 0 | 0 | 3 | 36 | 3.86 | — | 2 |
| [Ghalta, Primal Hunger — Ixalan-only](decks/plane-ixalan-ghalta-primal-hunger.md#bracket-calibration--pilot-notes) | plane | G | **2** | 0 | 0 | 0 | 0 | 2 | 36 | 3.9 | — | 2 |
| [Omnath, Locus of Rage — Zendikar-only](decks/plane-zendikar-omnath-locus-of-rage.md#bracket-calibration--pilot-notes) | plane | RG | **2** | 0 | 0 | 0 | 0 | 0 | 36 | 3.41 | — | 2 |
| [Syr Konrad, the Grim — Eldraine-only](decks/plane-eldraine-syr-konrad-the-grim.md#bracket-calibration--pilot-notes) | plane | B | **2** | 0 | 0 | 0 | 0 | 2 | 36 | 2.79 | — | 3 |
| [The Gitrog Monster — Innistrad-only](decks/plane-innistrad-the-gitrog-monster.md#bracket-calibration--pilot-notes) | plane | BG | **2** | 0 | 0 | 0 | 1 | 1 | 36 | 3.52 | — | 3 |
| [Muldrotha, the Gravetide — Self Mill theme](decks/theme-muldrotha-the-gravetide-self-mill.md#bracket-calibration--pilot-notes) | theme | UBG | **2** | 0 | 0 | 0 | 0 | 3 | 36 | 2.7 | — | 3 |

## Targets below the floor

None: every stated target is at or above the deck's floor.

## Lore decks

Story-first decks ([EDH Lore-Themed Deckbuilding](EDH%20Lore-Themed%20Deckbuilding.md)). They are calibrated like every other deck. *Lore score* = story-linked share of non-basic cards (≥ 85% standard, `scripts/build_lore_decks.py --check`). *Story map* = non-playability packages that point at a [lore entry](Lore%20Entry%20Index.md) (each entry links the deck back; `scripts/check_lore.py`).

| Deck | Floor | GC | 2-card ∞ | Lands | Avg MV | Lore score | Story map | Pilot & story notes |
|---|---|---|---|---|---|---|---|---|
| [Nahiri, the Lithomancer](decks/lore-nahiri-the-lithomancer.md#bracket-calibration--pilot-notes) | **2** | 0 | 0 | 36 | 2.57 | 86.8% | 10/10 packages | [calibration](decks/lore-nahiri-the-lithomancer.md#pilot-notes-guidance) · [story map](decks/lore-nahiri-the-lithomancer.md#story-map) |
| [The Brothers' War (Urza, Lord High Artificer)](decks/lore-brothers-war-urza-lord-high-artificer.md#bracket-calibration--pilot-notes) | **2** | 0 | 0 | 37 | 2.98 | 93.8% | 9/10 packages | [calibration](decks/lore-brothers-war-urza-lord-high-artificer.md#pilot-notes-guidance) · [story map](decks/lore-brothers-war-urza-lord-high-artificer.md#story-map) |

## Method

- **Floor (fact):** 0 Game Changers → 2 · 1–3 → 3 · 4+ → 4; any mass land denial → 4; any two-card infinite (Commander Spellbook, complete in the list) → at least 3. The highest applies. Game Changer and Oracle data: Scryfall bulk; combos: each deck's Spellbook block.
- **Not a floor input:** tutors (the Oct 2025 update removed tutor limits) and extra turns beyond Bracket 1 ("low quantity" is a judgment). Both are shown.
- **Bracket 5** (cEDH) depends on intent and metagame, so no list is floored at 5; see [cEDH Primer](cEDH%20Primer.md).
- **Role counts** are Oracle-text pattern matches (ramp, draw, removal, wipes, counterspells, protection, tutors), so a card can count in several roles or fit loosely.
- **Pilot notes** are guidance built from those counts and the hypergeometric opening-hand odds (99-card library, 7-card hand).
