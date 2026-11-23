# Cory and Stefanie's physical Magic collection

**Latest owner-confirmed physical snapshot: November 23, 2026.** Use [current_status.json](current_status.json) and [current_available.csv](current_available.csv) for the current six-deck allocation and cards available for new builds. Exact owner-submitted source CSVs are kept in [2026-11-23/](2026-11-23/), with [manifest](2026-11-23/manifest.json) checksums. Older [November 14](2026-11-14/) and [November 8](2026-11-08/) snapshots remain historical and unchanged.

## Physical inventory and allocation

| Metric | Nov 14 | Nov 23 current |
| --- | ---: | ---: |
| Physical copies recorded | 1,348 | **1,395** |
| Distinct owned names | 766 | **793** |
| Active built decks | 6 | **6** |
| Decklist slots including companion | 521 | **521** |
| Owned copies reserved in active decks | 521 | **508** |
| Incoming Mono-Red proxy copies | 0 | **13** |
| Unassigned physically owned copies | 827 | **887** |
| Distinct available names | 508 | **537** |

**Important:** The 508 owned copies allocated to decks include the one physically owned Lutri companion. The six CSV decklists contain 521 total entries by quantity: 508 actual owned copies + 13 incoming/proxy placeholders. Do not count those placeholders as copies in the physical collection; keep those named deck slots reserved for their arriving cards.

## Current six decks

| Format | Current deck | Source CSV | Count |
| --- | --- | --- | ---: |
| Commander / Grixis | [Lord Xander](current_decks/Xander_EDH_IRL.csv) | [source](2026-11-23/Cory_s_Lord_Xander_IRL_EDH.csv) | 100 + 1 separate companion |
| Commander / Mardu | [Dihada](current_decks/Dihada_EDH_IRL.csv) | [source](2026-11-23/Stefanie_Dihada_EDH_IRL.csv) | 100 |
| Commander / Jund | [Korvold](current_decks/Korvold_Jund_EDH_IRL.csv) | [source](2026-11-23/Stefanie_s_IRL_Jund_EDH.csv) | 100 |
| Commander / Orzhov Borg | [Locutus](current_decks/Locutus_Orzhov_Borg_EDH_IRL.csv) | [source](2026-11-23/Cory_s_IRL_Orzhov_Borg_EDH.csv) | 100 |
| Pauper | [Mono-Black Devotion Control](current_decks/MonoBlack_Pauper_IRL.csv) | [source](2026-11-23/Mono_Black_Devotion_Control.csv) | 60 |
| Pauper | [Mono-Red Burn/Madness](current_decks/MonoRed_Pauper_IRL.csv) | [source](2026-11-23/Mono_Red_Madness.csv) | 60 (13 incoming) |

**Lutri companion exception:** Lord Xander's CSV contains 101 physical card entries, including **Lutri, the Spellchaser** as a separate companion; the Commander plus the other 99 cards total 100. Lutri is banned in official Commander. Cory's local game shop permits it as a **Rule 0 house-rule exception**, not a general legality precedent. Lutri is owned, reserved, and excluded from the main-deck count.

**Mono-Red pending arrivals:** 2 Fireblast, 4 Grab the Prize, 1 Kessig Flamebreather, 2 Lava Dart, and 4 Voldaren Epicure (13 total). They are currently proxies and are **not** counted as owned physical copies. All other deck slots are covered by the corrected inventory. Reconcile arrivals only after confirmation that the cards arrived.

## Source authority

The original November 23 full-collection ZIP was superseded by the owner's corrected upload **`every_card we own irl (1).csv`**. The corrected source is [saved verbatim](2026-11-23/Every_Card_we_own_IRL_corrected.csv) alongside exact deck CSVs extracted from **`Real_Life_Decks-11-23-2026.zip`**. The ZIPs are identified by SHA-256 in the new manifest, but their binary archives are not committed. No unlisted basic lands, proxies, or cards on order were silently inserted.

## Validation and history

```bash
python3 scripts/audit_physical_collection.py --check
python3 scripts/audit_physical_collection_2026_11_23.py --check
python3 scripts/build_owned_card_knowledge.py check
```

The first two commands check the **current allocation**. The separate November 8 Oracle/printing knowledge catalogue and its Scryfall evidence stay historical, not proof of live coverage for 793 owned names; the third command checks only that historical snapshot.

The approved 62-deck Grixis Encyclopedia, its hashes and exceptions, and approved historical lore-deck lists were not modified.
