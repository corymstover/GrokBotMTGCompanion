---
title: "Grixis (U/B/R) Commander"
category: edh
tags: [grixis, decks, index]
issues: [59, 60, 61]
generated_by: scripts/build_grixis.py
sources: [grixis-repo, scryfall, spellbook]
related: ["EDH Standards.md", "grixis/Grixis Evaluation.md", "grixis/Grixis Packages.md", "EDH Deck Template.md", "grixis/Grixis Corrections.md", "grixis/Grixis Refinement Cycle.md"]
schema: 2
---

# Grixis (U/B/R) Commander

> 🎯 **Mission (Cory, Bot cycle 39):** every one of the 62 decks must be the definitive, maximally optimized version of *that commander's* deck, not a strong Grixis shell. Commander identity first, optimization up to the commander's natural ceiling, no homogenization, complete verification. Full text: [Grixis Mission](Grixis%20Mission.md) · progress: [Grixis Refinement Cycle](Grixis%20Refinement%20Cycle.md) · Archidekt files: [exports/grixis-archidekt/](../exports/grixis-archidekt/README.md).

> **Bot cycle 16 import, refreshed in Bot cycle 37** (all 62 source lists are now APPROVED/LOCKED in the source). This section brings in the user's Grixis Commander work from [grixis-commander-encyclopediaGPT](https://github.com/corymstover/grixis-commander-encyclopediaGPT) (commit `1836b97`, read-only): the user-approved, refined decklists, each with its commander-first blueprint, swap decisions and approval record quoted verbatim. Each list was re-validated against our card DB, corrected where needed, and given Game Changer counts, bracket floors and Commander Spellbook combos. Source analysis is **the source author's guidance**. Our facts come from Scryfall and Commander Spellbook. Built by `scripts/build_grixis.py`. Related: [EDH Standards](../EDH%20Standards.md) · [EDH Deck Template](../EDH%20Deck%20Template.md) · [EDH Deck Evaluation Checklist](../EDH%20Deck%20Evaluation%20Checklist.md) · [Grixis mana base](../EDH%20Mana%20Bases.md) · [data-derived Nekusar skeleton](../decks/nekusar-the-mindrazer.md)

> 🗄️ **Single source of truth (Bot cycle 45):** the companion now holds the **complete source repository** in [source-archive/](source-archive/README.md): every file at commit `1836b97`, byte-identical (SHA-256 manifest, checked by `validate_all`), plus a git bundle with all branches and history. The archive is inert data; generators read it instead of a separate clone. The original GitHub repo stays untouched.

## Contents
- [Pages](#pages)
- [Decks](#decks)
- [Pending legality](#pending-legality)
- [What was left out](#what-was-left-out)

## Pages

| Page | What it holds |
|---|---|
| [Grixis Integration Summary](Grixis%20Integration%20Summary.md) | What was integrated, what was generalized, and follow-ups |
| [Grixis Mission](Grixis%20Mission.md) | Cory's commander-first mission and principles (Bot cycle 39) |
| [Grixis Refinement Cycle](Grixis%20Refinement%20Cycle.md) | Commander-dependence and homogenization metrics for all 62 decks, batch log, per-deck swaps |
| [exports/grixis-archidekt/](../exports/grixis-archidekt/README.md) | Archidekt import file per deck (final list) and ALL-DECKS.txt |
| [interactions/](interactions/README.md) | Phase 2 (Bot cycle 46+): card-level rules review per deck, with Oracle, Scryfall rulings and CR citations, flags and open questions; batch status |
| [source-archive/](source-archive/README.md) | Full byte-identical archive of the source repo (Bot cycle 45): area map, SHA-256 manifest, history bundle |
| [Grixis Evaluation](Grixis%20Evaluation.md) | Check results for all 62 source lists, and how each current list was chosen |
| [Grixis Corrections](Grixis%20Corrections.md) | All 135 corrections (deck, issue, fix), the Oracle-text check, source-repo structural findings |
| [Grixis Packages](Grixis%20Packages.md) | Cross-deck package library (cards shared by 4 or more of the 60 lists, by role) and verified rules insights |
| [decks/](decks/) | 62 deck pages: 60 validated (legal) + 2 ⏳ pending legality |

## Decks

*Themes* are the source's Archidekt tags where it recorded them. *Source bracket* is the source author's stated target (guidance). *Floor* is the minimum by the official barometers (Game Changers, mass land denial, two-card infinites).

| Deck | Themes (source) | GC | Floor | Source bracket | Spellbook combos / 2-card ∞ | Lands | Avg MV | Fixes |
|---|---|---|---|---|---|---|---|---|
| [Abaddon the Despoiler](decks/abaddon-the-despoiler.md) | — | 14 | 4 | 4 — Optimized | 4 / 0 | 34 | 2.58 | 2 |
| [Admiral Beckett Brass](decks/admiral-beckett-brass.md) | — | 6 | 4 | — | 0 / 0 | 35 | 2.75 | 2 |
| [Admiral Brass, Unsinkable](decks/admiral-brass-unsinkable.md) | — | 6 | 4 | — | 0 / 0 | 34 | 2.95 | 3 |
| [Anhelo, the Painter](decks/anhelo-the-painter.md) | — | 7 | 4 | — | 8 / 5 | 34 | 2.83 | 3 |
| [Ashad, the Lone Cyberman](decks/ashad-the-lone-cyberman.md) | — | 3 | 3 | — | 1 / 0 | 30 | 3.41 | 3 |
| [Ashnod the Uncaring](decks/ashnod-the-uncaring.md) | — | 6 | 4 | — | 15 / 0 | 33 | 2.21 | 2 |
| [Be'lakor, the Dark Master](decks/belakor-the-dark-master.md) | — | 5 | 4 | — | 1 / 1 | 36 | 4.08 | 2 |
| [Bjorna, Nightfall Alchemist + Cecily, Haunted Mage](decks/bjorna-nightfall-alchemist-cecily.md) | — | 10 | 4 | — | 3 / 2 | 33 | 3.26 | 5 |
| [Cormela, Glamour Thief](decks/cormela-glamour-thief.md) | — | 20 | 4 | — | 23 / 2 | 30 | 1.84 | 2 |
| [Crosis, the Purger](decks/crosis-the-purger.md) | — | 14 | 4 | 4 — Optimized | 1 / 0 | 36 | 2.29 | 2 |
| [Cult of Skaro](decks/cult-of-skaro.md) | — | 3 | 3 | 4 — Optimized | 1 / 1 | 34 | 3.35 | 2 |
| [Davros, Dalek Creator](decks/davros-dalek-creator.md) | — | 5 | 4 | 4 — Optimized | 0 / 0 | 34 | 3.18 | 2 |
| [Doctor Doom, King of Latveria](decks/doctor-doom-king-of-latveria.md) | Land Discard / Villains / Connive | 6 | 4 | 4 — Optimized | 1 / 0 | 38 | 2.85 | 2 |
| [Don Andres, the Renegade](decks/don-andres-the-renegade.md) | — | 5 | 4 | 4 — Optimized | 0 / 0 | 35 | 3.31 | 2 |
| [Dr. Eggman](decks/dr-eggman.md) | Villainous Choice / Robots / Artifact Cheat | 3 | 3 | 4 — Optimized | 0 / 0 | 31 | 4.21 | 3 |
| [Edea, Possessed Sorceress](decks/edea-possessed-sorceress.md) | Theft / Sacrifice / Extra Combats | 3 | 3 | 4 — Optimized | 0 / 0 | 35 | 3.20 | 2 |
| [Edward Kenway](decks/edward-kenway.md) | — | 10 | 4 | 4 — Optimized | 6 / 5 | 35 | 2.80 | 2 |
| [Evelyn, the Covetous](decks/evelyn-the-covetous.md) | Worldgorger / Exile / Combo | 19 | 4 | 5 — cEDH | 7 / 3 | 26 | 1.84 | 2 |
| [Fire Lord Azula](decks/fire-lord-azula.md) | Combat-Flash / Spell Copy / Combo | 20 | 4 | 5 — cEDH | 9 / 1 | 26 | 1.85 | 2 |
| [Garza Zol, Plague Queen](decks/garza-zol-plague-queen.md) | Voltron / Commander Damage / Deathtouch-Control | 9 | 4 | 4 — Optimized | 3 / 2 | 38 | 2.21 | 2 |
| [Goro-Goro and Satoru](decks/goro-goro-and-satoru.md) | Ninjutsu / Dragon Tokens / Extra Combats | 6 | 4 | 4 — Optimized | 5 / 5 | 33 | 2.53 | 2 |
| [Gwendlyn Di Corci](decks/gwendlyn-di-corci.md) | Random Discard / Activated Ability / Wheels | 17 | 4 | 4 — Optimized | 1 / 0 | 35 | 2.33 | 2 |
| [Inalla, Archmage Ritualist](decks/inalla-archmage-ritualist.md) | Spellseeker Combo / Reanimator / Turbo | 18 | 4 | 5 — cEDH | 15 / 0 | 27 | 2.00 | 2 |
| [Jeleva, Nephalia's Scourge](decks/jeleva-nephalias-scourge.md) | Topdeck / Free-Cast / Storm | 20 | 4 | 5 — fringe cEDH | 7 / 0 | 27 | 1.90 | 2 |
| [Kefka, Court Mage // Kefka, Ruler of Ruin](decks/kefka-court-mage.md) | Discard / Trigger Copy / Turbo | 20 | 4 | 5 — cEDH | 6 / 0 | 28 | 1.94 | 2 |
| [Kess, Dissident Mage](decks/kess-dissident-mage.md) | — | 21 | 4 | 5 — fringe cEDH | 6 / 1 | 27 | 1.85 | 2 |
| [Kraum, Ludevic's Opus + Tevesh Szat, Doom of Fools](decks/grixistax-october-2026.md) | — | 22 | 4 | 5 — fringe / rogue cEDH | 6 / 0 | 26 | 2.06 | 2 |
| [Loki, the Deceiver](decks/loki-the-deceiver.md) | — | 5 | 4 | 4 — Optimized | 0 / 0 | 34 | 3.38 | 2 |
| [Lord Xander, the Collector](decks/lord-xander-the-collector.md) | — | 20 | 4 | 4 — Optimized | 11 / 7 | 33 | 2.33 | 2 |
| [Lord of Tresserhorn](decks/lord-of-tresserhorn.md) | — | 2 | 3 | 4 — Optimized | 19 / 1 | 35 | 2.44 | 2 |
| [Lynde, Cheerful Tormentor](decks/lynde-cheerful-tormentor.md) | — | 8 | 4 | 4 — Optimized | 0 / 0 | 35 | 3.22 | 2 |
| [Mai and Zuko](decks/mai-and-zuko.md) | — | 15 | 4 | 4 — Optimized | 8 / 1 | 31 | 2.60 | 2 |
| [Mairsil, the Pretender](decks/mairsil-the-pretender.md) | — | 13 | 4 | 4 — Optimized | 6 / 0 | 32 | 2.81 | 2 |
| [Marchesa, Dealer of Death](decks/marchesa-dealer-of-death.md) | Crimes / Control / Storm | 18 | 4 | 5 — cEDH | 4 / 1 | 29 | 1.87 | 2 |
| [Marchesa, the Black Rose](decks/marchesa-the-black-rose.md) | +1/+1 Counters / Aristocrats / Combo | 5 | 4 | 4 — Optimized | 48 / 38 | 34 | 2.82 | 2 |
| [Mishra, Artificer Prodigy](decks/mishra-artificer-prodigy.md) | Artifacts / Stax / Combo | 15 | 4 | 5 — cEDH (fringe / commander-centric artifact stax-combo | 20 / 1 | 29 | 2.66 | 2 |
| [Mishra, Eminent One](decks/mishra-eminent-one.md) | Artifacts / Tokens / Combo | 14 | 4 | 4 — Optimized | 19 / 1 | 34 | 2.78 | 2 |
| [Missy](decks/missy.md) | Cybermen / Morph / Aristocrats | 7 | 4 | 4 — Optimized | 17 / 0 | 35 | 2.72 | 2 |
| [Nathan Drake, Treasure Hunter](decks/nathan-drake-treasure-hunter.md) | Theft / Attack Triggers / Exile | 9 | 4 | 4 — Optimized | 0 / 0 | 34 | 2.91 | 2 |
| [Nekusar, the Mindrazer](decks/nekusar-the-mindrazer.md) | Wheels / Draw Punishment / Group Slug | 15 | 4 | 4 — Optimized | 7 / 5 | 35 | 2.67 | 2 |
| [Nicol Bolas](decks/nicol-bolas.md) | Discard / Commander Damage / Control | 14 | 4 | 4 — Optimized | 1 / 1 | 37 | 2.48 | 2 |
| [Nicol Bolas, the Ravager // Nicol Bolas, the Arisen](decks/nicol-bolas-the-ravager.md) | Superfriends / Transform / Proliferate | 16 | 4 | 4 — Optimized | 3 / 1 | 34 | 3.14 | 2 |
| [Norman Osborn // Green Goblin](decks/norman-osborn.md) | Mayhem / Graveyard Casting / Turbo Combo | 19 | 4 | 5 — cEDH | 7 / 1 | 23 | 1.87 | 2 |
| [Obeka, Brute Chronologist](decks/obeka-brute-chronologist.md) | Extra Turns / Delayed Triggers / Clones | 13 | 4 | 4 — Optimized | 4 / 2 | 34 | 2.78 | 2 |
| [Obeka, Splitter of Seconds](decks/obeka-splitter-of-seconds.md) | Extra Upkeeps / Combat Damage / Upkeep Triggers | 6 | 4 | 4 — Optimized | 5 / 0 | 35 | 2.89 | 2 |
| [Parnesse, the Subtle Brush](decks/parnesse-the-subtle-brush.md) | Spell Copy / Politics / Spellslinger | 3 | 3 | 4 — Optimized | 25 / 21 | 35 | 3.00 | 2 |
| [Rograkh, Son of Rohgahh + Silas Renn, Seeker Adept](decks/rograkh-son-of-rohgahh-silas-renn.md) | Turbo Naus / Underworld Breach / Fast Mana | 19 | 4 | 5 — cEDH | 7 / 1 | 24 | 1.82 | 2 |
| [Saruman, the White Hand](decks/saruman-the-white-hand.md) | Spellslinger / Amass / Orc Army | 11 | 4 | 4 — Optimized | 1 / 1 | 31 | 3.35 | 3 |
| [Sauron, Lord of the Rings](decks/sauron-lord-of-the-rings.md) | Reanimator / Graveyard Setup / Amass Orcs | 11 | 4 | 4 — Optimized | 0 / 0 | 32 | 3.51 | 2 |
| [Sauron, the Dark Lord](decks/sauron-the-dark-lord.md) | Amass Orcs / Ring Temptation / Wraiths | 12 | 4 | 4 — Optimized | 0 / 0 | 34 | 2.97 | 2 |
| [Sedris, the Traitor King](decks/sedris-the-traitor-king.md) | Unearth / Reanimator / End-Step Control | 12 | 4 | 4 — Optimized | 1 / 1 | 31 | 3.43 | 3 |
| [Sol'Kanar the Tainted](decks/solkanar-the-tainted.md) | Donate / Blink / Giftable Curses | 7 | 4 | 4 — Optimized | 4 / 0 | 35 | 3.03 | 2 |
| [Sol'kanar the Swamp King](decks/solkanar-the-swamp-king.md) | Black Spells / Lifegain / Swamp Matters | 13 | 4 | 4 — Optimized | 13 / 11 | 35 | 2.66 | 2 |
| [Tetsuo Umezawa](decks/tetsuo-umezawa.md) | Tap/Untap / Forced Combat / Activated Abilities | 4 | 4 | 4 — Optimized | 1 / 1 | 35 | 2.75 | 2 |
| [Tetsuo, Imperial Champion](decks/tetsuo-imperial-champion.md) | Equipment / Free-Cast Spells / Extra Combats | 5 | 4 | 4 — Optimized | 2 / 2 | 35 | 3.19 | 2 |
| [The Rani](decks/the-rani.md) | Goad / Clues / Forced Combat | 8 | 4 | 4 — Optimized | 0 / 0 | 33 | 3.02 | 2 |
| [The Valeyard](decks/the-valeyard.md) | Villainous Choice / Voting / Political Control | 6 | 4 | 4 — Optimized | 0 / 0 | 36 | 3.60 | 2 |
| [Thraximundar](decks/thraximundar.md) | Sacrifice / Zombie Aristocrats / Commander Damage | 8 | 4 | 4 — Optimized | 17 / 1 | 36 | 2.78 | 2 |
| [Wick, the Whorled Mind](decks/wick-the-whorled-mind.md) | — | 5 | 4 | 4 — Optimized | 13 / 1 | 35 | 2.55 | 2 |
| [Zevlor, Elturel Exile](decks/zevlor-elturel-exile.md) | — | 11 | 4 | 4 — natural ceiling | 1 / 1 | 34 | 2.74 | 2 |

## Pending legality

2 deck page(s) are published with `legality_status: pending`. They are **not counted** among the 60 legal decks above or in [Grixis Packages](Grixis%20Packages.md). Each lists the cards that are not Commander-legal yet. Activation: `python3 scripts/activate_pending_grixis.py` (Bot cycle 38).

| Deck | Not yet legal | Legal from | GC | Floor | Source bracket | Lands |
|---|---|---|---|---|---|---|
| ⏳ [The Madcap Jester](decks/the-madcap-jester.md) | The Madcap Jester, Dragon's Smile | 2026-11-13 | 17 | 4 | 5 — cEDH | 34 |
| ⏳ [Tresserhorn's Lord, Returned](decks/tresserhorns-lord-returned.md) | Tresserhorn's Lord, Returned | 2026-11-13 | 2 | 3 | — | 33 |

## What was left out

0 of 62 source lists are left out. Their check results are in [Grixis Evaluation](Grixis%20Evaluation.md#per-list-results).


