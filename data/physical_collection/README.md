# Physical Magic collection — live status

**As of November 25, 2026**, the corrected [master inventory](2026-11-25/Every_Card_we_own_IRL_corrected.csv) contains **1,471 physical card copies / 845 card names**. Source [manifest](2026-11-25/manifest.json) and [change event](updates/2026-11-25_collection_reconciliation.json) preserve SHA-256 provenance. Previous [November 23 snapshot](2026-11-23/) is immutable.

| Metric | After Nov 23 Mono-Black disassembly | Nov 25 |
| --- | ---: | ---: |
| Owned physical copies | 1,395 | **1,471** |
| Distinct owned names | 793 | **845** |
| Built decks | 5 | **5** |
| Deck slots including separate Lutri companion | 461 | **461** |
| Owned deck cards reserved | 448 | **448** |
| Mono-Red incoming proxy cards | 13 | **13** |
| Available physical copies | 947 | **1,023** |
| Distinct available names | 549 | **611** |

**Owner-confirmed Dihada swap:** 1× **The Balrog, Durin's Bane** OUT, 1× **Ingris Stingerquill** IN. The Balrog is available again; Ingris is reserved to Dihada. The other four active decks are **byte-for-byte unchanged**.

**New inventory reconciliation:** 77 copies added/increased, 1 removed/decreased, net +76. The new source omits **Cavern-Hoard Dragon**, which appeared once in the November 23 inventory; this absence is recorded as an inventory change, not assumed to represent a sale. New acquisitions now reserved to the owner-confirmed Xander list include Fraying Sanity, Hedron Crab, Ruin Crab, Zellix, Nicol Bolas, God-Pharaoh, and faster mana rocks; Gandalf, Goblins' Bane remains available.

## Five active decks

| Format | Link | Deck slots |
| --- | --- | ---: |
| Grixis Commander | [Lord Xander](current_decks/Xander_EDH_IRL.csv) | 100 + separate Lutri companion |
| Mardu Commander | [Dihada](current_decks/Dihada_EDH_IRL.csv) | 100 |
| Jund Commander | [Korvold](current_decks/Korvold_Jund_EDH_IRL.csv) | 100 |
| Orzhov Commander | [Locutus Borg](current_decks/Locutus_Orzhov_Borg_EDH_IRL.csv) | 100 |
| Pauper | [Mono-Red Burn/Madness](current_decks/MonoRed_Pauper_IRL.csv) | 60, 13 incoming proxies |

Stefanie's previously dismantled **Mono-Black Devotion Pauper** remains archived in [November 23 source](2026-11-23/Mono_Black_Devotion_Control.csv); its 60 cards remain available. Xander's **Lutri, the Spellchaser** remains a locally permitted companion *outside* the 100-card deck; Lutri is officially banned **as a Commander companion** and this house-rule exception is not official format legality.

**Active verification:** `python3 scripts/audit_physical_collection.py --check`, `python3 scripts/audit_physical_collection_2026_11_25.py --check`, and `python3 -m unittest tests/test_physical_collection.py`. The historical owned-card Oracle catalogue remains dated November 8, and does not certify all 845 current names. The protected 62-deck encyclopedia and approved lore decks are untouched.
