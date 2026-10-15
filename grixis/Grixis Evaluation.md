---
title: "Grixis Evaluation — all 62 source lists"
category: edh
tags: [grixis, validation, legality]
issues: [59]
generated_by: scripts/build_grixis.py
sources: [grixis-repo, scryfall]
---

# Grixis Evaluation — all 62 source lists

> Bot cycle 16. Every decklist in [grixis-commander-encyclopediaGPT](https://github.com/corymstover/grixis-commander-encyclopediaGPT) (commit `df1abb9`), checked by `scripts/grixis_eval.py` against Scryfall Oracle bulk 2026-10-15. Checks: name resolution, commander eligibility and pairing, 100 cards, singleton (with Oracle copy exceptions such as Nazgûl), color identity, Commander legality and bans, companion, Game Changers. Oracle text recorded in the source's audit CSVs is compared with current Oracle. Back to [Grixis](README.md).

## Contents
- [Summary](#summary)
- [Per-list results](#per-list-results)
- [How the current list was chosen](#how-the-current-list-was-chosen)

## Summary

- Source lists: **62** (62 baseline FINAL lists; 40 have a newer user-approved list).
- **Integrated: 40**, i.e. every approved list that passes or could be corrected to pass. **Left out: 22** (2 future-release lists; 20 lists the source still marks UNREFINED).
- Hard problems found across all 62: 3× not Commander-legal, 2× banned.
- Oracle check: 16,137 Oracle-text rows in 34 source audit files; **0 differ** from current Oracle.

## Per-list results

| # | Source deck | Commander(s) | Source status | Cards | Hard issues | GC | Result |
|---|---|---|---|---|---|---|---|
| 1 | `Abaddon_the_Despoiler` | Abaddon the Despoiler | APPROVED | 100 | — | 14 | ✅ [integrated](decks/abaddon-the-despoiler.md) |
| 2 | `Admiral_Beckett_Brass` | Admiral Beckett Brass | APPROVED | 100 | — | 6 | ✅ [integrated](decks/admiral-beckett-brass.md) |
| 3 | `Admiral_Brass__Unsinkable` | Admiral Brass, Unsinkable | APPROVED | 100 | — | 6 | ✅ [integrated](decks/admiral-brass-unsinkable.md) |
| 4 | `Anhelo__the_Painter` | Anhelo, the Painter | APPROVED | 100 | — | 7 | ✅ [integrated](decks/anhelo-the-painter.md) |
| 5 | `Ashad__the_Lone_Cyberman` | Ashad, the Lone Cyberman | APPROVED | 100 | — | 3 | ✅ [integrated](decks/ashad-the-lone-cyberman.md) |
| 6 | `Ashnod_the_Uncaring` | Ashnod the Uncaring | APPROVED | 100 | — | 6 | ✅ [integrated](decks/ashnod-the-uncaring.md) |
| 7 | `Be_lakor__the_Dark_Master` | Be'lakor, the Dark Master | APPROVED | 100 | — | 5 | ✅ [integrated](decks/belakor-the-dark-master.md) |
| 8 | `Cecily__Bjorna__Lutri` | Bjorna, Nightfall Alchemist + Cecily, Haunted Mage | APPROVED | 100 | banned: Trade Secrets; banned: Yawgmoth's Bargain | 10 | ✅ [integrated](decks/bjorna-nightfall-alchemist-cecily.md) |
| 9 | `Cormela__Glamour_Thief` | Cormela, Glamour Thief | APPROVED | 100 | — | 20 | ✅ [integrated](decks/cormela-glamour-thief.md) |
| 10 | `Crosis__the_Purger` | Crosis, the Purger | APPROVED | 100 | — | 14 | ✅ [integrated](decks/crosis-the-purger.md) |
| 11 | `Cult_of_Skaro` | Cult of Skaro | APPROVED | 100 | — | 3 | ✅ [integrated](decks/cult-of-skaro.md) |
| 12 | `Davros__Dalek_Creator` | Davros, Dalek Creator | APPROVED | 100 | — | 5 | ✅ [integrated](decks/davros-dalek-creator.md) |
| 13 | `Doctor_Doom__King_of_Latveria` | Doctor Doom, King of Latveria | APPROVED | 100 | — | 6 | ✅ [integrated](decks/doctor-doom-king-of-latveria.md) |
| 14 | `Don_Andres__the_Renegade` | Don Andres, the Renegade | APPROVED | 100 | — | 5 | ✅ [integrated](decks/don-andres-the-renegade.md) |
| 15 | `Dr__Eggman` | Dr. Eggman | APPROVED | 100 | — | 3 | ✅ [integrated](decks/dr-eggman.md) |
| 16 | `Edea__Possessed_Sorceress` | Edea, Possessed Sorceress | APPROVED | 100 | — | 3 | ✅ [integrated](decks/edea-possessed-sorceress.md) |
| 17 | `Edward_Kenway` | Edward Kenway | APPROVED | 100 | — | 10 | ✅ [integrated](decks/edward-kenway.md) |
| 18 | `Evelyn__the_Covetous` | Evelyn, the Covetous | APPROVED | 100 | — | 19 | ✅ [integrated](decks/evelyn-the-covetous.md) |
| 19 | `Fire_Lord_Azula` | Fire Lord Azula | APPROVED | 100 | — | 20 | ✅ [integrated](decks/fire-lord-azula.md) |
| 20 | `Garza_Zol__Plague_Queen` | Garza Zol, Plague Queen | APPROVED | 100 | — | 9 | ✅ [integrated](decks/garza-zol-plague-queen.md) |
| 21 | `Goben__Gene_Splice_Savant` | Norman Osborn // Green Goblin | UNREFINED (not in current-cycle approvals) | 100 | — | 16 | ⏸ not integrated: the source repo marks this list UNREFINED (its whole-list audit has not run yet). Validation results are kept here for a later import. |
| 22 | `Goro_Goro_and_Satoru` | Goro-Goro and Satoru | APPROVED | 100 | — | 6 | ✅ [integrated](decks/goro-goro-and-satoru.md) |
| 23 | `Grixistax___October_2026` | Kraum, Ludevic's Opus + Tevesh Szat, Doom of Fools | APPROVED | 100 | — | 22 | ✅ [integrated](decks/grixistax-october-2026.md) |
| 24 | `Gwendlyn_Di_Corci` | Gwendlyn Di Corci | APPROVED | 100 | — | 17 | ✅ [integrated](decks/gwendlyn-di-corci.md) |
| 25 | `Inalla__Archmage_Ritualist` | Inalla, Archmage Ritualist | APPROVED | 100 | — | 18 | ✅ [integrated](decks/inalla-archmage-ritualist.md) |
| 26 | `Jeleva__Nephalia_s_Scourge` | Jeleva, Nephalia's Scourge | APPROVED | 100 | — | 20 | ✅ [integrated](decks/jeleva-nephalias-scourge.md) |
| 27 | `Kefka__Court_Mage` | Kefka, Court Mage // Kefka, Ruler of Ruin | APPROVED | 100 | — | 20 | ✅ [integrated](decks/kefka-court-mage.md) |
| 28 | `Kess__Dissident_Mage` | Kess, Dissident Mage | APPROVED | 100 | — | 21 | ✅ [integrated](decks/kess-dissident-mage.md) |
| 29 | `Loki__the_Deceiver` | Loki, the Deceiver | APPROVED | 100 | — | 5 | ✅ [integrated](decks/loki-the-deceiver.md) |
| 30 | `Lord_Xander__the_Collector` | Lord Xander, the Collector | APPROVED | 100 | — | 20 | ✅ [integrated](decks/lord-xander-the-collector.md) |
| 31 | `Lord_of_Tresserhorn` | Lord of Tresserhorn | APPROVED | 100 | — | 2 | ✅ [integrated](decks/lord-of-tresserhorn.md) |
| 32 | `Lynde__Cheerful_Tormentor` | Lynde, Cheerful Tormentor | APPROVED | 100 | — | 8 | ✅ [integrated](decks/lynde-cheerful-tormentor.md) |
| 33 | `Mai_and_Zuko` | Mai and Zuko | APPROVED | 100 | — | 15 | ✅ [integrated](decks/mai-and-zuko.md) |
| 34 | `Mairsil__the_Pretender` | Mairsil, the Pretender | APPROVED | 100 | — | 13 | ✅ [integrated](decks/mairsil-the-pretender.md) |
| 35 | `Marchesa__Dealer_of_Death` | Marchesa, Dealer of Death | APPROVED | 100 | — | 18 | ✅ [integrated](decks/marchesa-dealer-of-death.md) |
| 36 | `Marchesa__the_Black_Rose` | Marchesa, the Black Rose | APPROVED | 100 | — | 5 | ✅ [integrated](decks/marchesa-the-black-rose.md) |
| 37 | `Mishra__Artificer_Prodigy` | Mishra, Artificer Prodigy | APPROVED | 100 | — | 15 | ✅ [integrated](decks/mishra-artificer-prodigy.md) |
| 38 | `Mishra__Eminent_One` | Mishra, Eminent One | APPROVED | 100 | — | 14 | ✅ [integrated](decks/mishra-eminent-one.md) |
| 39 | `Missy` | Missy | APPROVED | 100 | — | 7 | ✅ [integrated](decks/missy.md) |
| 40 | `Nathan_Drake__Treasure_Hunter` | Nathan Drake, Treasure Hunter | APPROVED | 100 | — | 9 | ✅ [integrated](decks/nathan-drake-treasure-hunter.md) |
| 41 | `Nekusar__the_Mindrazer` | Nekusar, the Mindrazer | APPROVED | 100 | — | 15 | ✅ [integrated](decks/nekusar-the-mindrazer.md) |
| 42 | `Nicol_Bolas` | Nicol Bolas | UNREFINED (not in current-cycle approvals) | 100 | — | 10 | ⏸ not integrated: the source repo marks this list UNREFINED (its whole-list audit has not run yet). Validation results are kept here for a later import. |
| 43 | `Nicol_Bolas__the_Ravager` | Nicol Bolas, the Ravager // Nicol Bolas, the Arisen | UNREFINED (not in current-cycle approvals) | 100 | — | 20 | ⏸ not integrated: the source repo marks this list UNREFINED (its whole-list audit has not run yet). Validation results are kept here for a later import. |
| 44 | `Obeka__Brute_Chronologist` | Obeka, Brute Chronologist | UNREFINED (not in current-cycle approvals) | 100 | — | 13 | ⏸ not integrated: the source repo marks this list UNREFINED (its whole-list audit has not run yet). Validation results are kept here for a later import. |
| 45 | `Obeka__Splitter_of_Seconds` | Obeka, Splitter of Seconds | UNREFINED (not in current-cycle approvals) | 100 | — | 6 | ⏸ not integrated: the source repo marks this list UNREFINED (its whole-list audit has not run yet). Validation results are kept here for a later import. |
| 46 | `Parnesse__the_Subtle_Brush` | Parnesse, the Subtle Brush | UNREFINED (not in current-cycle approvals) | 100 | — | 3 | ⏸ not integrated: the source repo marks this list UNREFINED (its whole-list audit has not run yet). Validation results are kept here for a later import. |
| 47 | `RogSi` | Rograkh, Son of Rohgahh + Silas Renn, Seeker Adept | UNREFINED (not in current-cycle approvals) | 100 | — | 20 | ⏸ not integrated: the source repo marks this list UNREFINED (its whole-list audit has not run yet). Validation results are kept here for a later import. |
| 48 | `Saruman__the_White_Hand` | Saruman, the White Hand | UNREFINED (not in current-cycle approvals) | 100 | — | 10 | ⏸ not integrated: the source repo marks this list UNREFINED (its whole-list audit has not run yet). Validation results are kept here for a later import. |
| 49 | `Sauron__Lord_of_the_Rings` | Sauron, Lord of the Rings | UNREFINED (not in current-cycle approvals) | 100 | — | 9 | ⏸ not integrated: the source repo marks this list UNREFINED (its whole-list audit has not run yet). Validation results are kept here for a later import. |
| 50 | `Sauron__the_Dark_Lord` | Sauron, the Dark Lord | UNREFINED (not in current-cycle approvals) | 100 | — | 11 | ⏸ not integrated: the source repo marks this list UNREFINED (its whole-list audit has not run yet). Validation results are kept here for a later import. |
| 51 | `Sedris__the_Traitor_King` | Sedris, the Traitor King | UNREFINED (not in current-cycle approvals) | 100 | — | 11 | ⏸ not integrated: the source repo marks this list UNREFINED (its whole-list audit has not run yet). Validation results are kept here for a later import. |
| 52 | `Sol_kanar_the_Swamp_King` | Sol'kanar the Swamp King | UNREFINED (not in current-cycle approvals) | 100 | — | 13 | ⏸ not integrated: the source repo marks this list UNREFINED (its whole-list audit has not run yet). Validation results are kept here for a later import. |
| 53 | `Sol_kanar_the_Tainted` | Sol'Kanar the Tainted | UNREFINED (not in current-cycle approvals) | 100 | — | 5 | ⏸ not integrated: the source repo marks this list UNREFINED (its whole-list audit has not run yet). Validation results are kept here for a later import. |
| 54 | `Tetsuo_Umezawa` | Tetsuo Umezawa | UNREFINED (not in current-cycle approvals) | 100 | — | 4 | ⏸ not integrated: the source repo marks this list UNREFINED (its whole-list audit has not run yet). Validation results are kept here for a later import. |
| 55 | `Tetsuo__Imperial_Champion` | Tetsuo, Imperial Champion | UNREFINED (not in current-cycle approvals) | 100 | — | 4 | ⏸ not integrated: the source repo marks this list UNREFINED (its whole-list audit has not run yet). Validation results are kept here for a later import. |
| 56 | `The_Madcap_Jester` | The Madcap Jester | UNREFINED (not in current-cycle approvals) | 100 | not Commander-legal: The Madcap Jester; not Commander-legal: Dragon's Smile | 17 | ⏸ future-release: The commander and Dragon's Smile come from Scryfall set `mbc` (draft_innovation), releasing 2026-10-19. Both are `not_legal` in Commander today, and the source registers them as a *future-release* exception. Re-check after release. |
| 57 | `The_Rani` | The Rani | UNREFINED (not in current-cycle approvals) | 100 | — | 8 | ⏸ not integrated: the source repo marks this list UNREFINED (its whole-list audit has not run yet). Validation results are kept here for a later import. |
| 58 | `The_Valeyard` | The Valeyard | UNREFINED (not in current-cycle approvals) | 100 | — | 5 | ⏸ not integrated: the source repo marks this list UNREFINED (its whole-list audit has not run yet). Validation results are kept here for a later import. |
| 59 | `Thraximundar` | Thraximundar | UNREFINED (not in current-cycle approvals) | 100 | — | 8 | ⏸ not integrated: the source repo marks this list UNREFINED (its whole-list audit has not run yet). Validation results are kept here for a later import. |
| 60 | `Tresserhorn_s_Lord__Returned` | Tresserhorn's Lord, Returned | UNREFINED (not in current-cycle approvals) | 100 | not Commander-legal: Tresserhorn's Lord, Returned | 1 | ⏸ future-release: The commander is in set `mbc` (releasing 2026-10-19) and is `not_legal` in Commander today. The source registers it as a *future-release* exception. |
| 61 | `Wick__the_Whorled_Mind` | Wick, the Whorled Mind | UNREFINED (not in current-cycle approvals) | 100 | — | 5 | ⏸ not integrated: the source repo marks this list UNREFINED (its whole-list audit has not run yet). Validation results are kept here for a later import. |
| 62 | `Zevlor__Elturel_Exile` | Zevlor, Elturel Exile | UNREFINED (not in current-cycle approvals) | 100 | — | 11 | ⏸ not integrated: the source repo marks this list UNREFINED (its whole-list audit has not run yet). Validation results are kept here for a later import. |

## How the current list was chosen

- If `state/current_deck_overrides.json` marks the deck APPROVED/LOCKED, we use the approved list: the `approved_list_artifact`, or the `refinement/decklists/*.txt` file whose SHA-256 matches `approved_list_sha256`. If no file matches, we use the file that matches the deck's Card_Verification CSV card for card.
- Otherwise we use the frozen baseline `source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz → TXT/<deck>.txt`.

