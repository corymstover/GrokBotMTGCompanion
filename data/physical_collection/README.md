# Cory and Stefanie's physical Magic collection

**Latest owner-confirmed allocation: November 23, 2026 (Mono-Black Pauper disassembly).** The [current status](current_status.json) and [available pool](current_available.csv) reflect **five built decks**, not six. The previously submitted [November 23 six-deck source snapshot](2026-11-23/) remains immutable, including the intact historical Mono-Black Devotion list. The [disassembly event](updates/2026-11-23_monoblack_devotion_disassembly.json) records exactly what returned to circulation. Older November 14 and November 8 history is preserved.

## Physical ownership and allocation

| Metric | Nov 14 | Original Nov 23 | Current Nov 23 after disassembly |
| --- | ---: | ---: | ---: |
| Physical copies owned | 1,348 | 1,395 | **1,395** |
| Distinct owned names | 766 | 793 | **793** |
| Built decks | 6 | 6 | **5** |
| Decklist slots including Lutri companion | 521 | 521 | **461** |
| Owned cards reserved in built decks | 521 | 508 | **448** |
| Incoming Mono-Red proxy copies | 0 | 13 | **13** |
| Unassigned physically owned copies | 827 | 887 | **947** |
| Distinct available names | 508 | 537 | **549** |

The user confirmed that **Stefanie's 60-card Mono-Black Devotion Control Pauper deck is being disassembled**, releasing **all 60 physical cards across 15 card names** for reuse. It is no longer a reserved/active deck; the list is **preserved** at [2026-11-23/Mono_Black_Devotion_Control.csv](2026-11-23/Mono_Black_Devotion_Control.csv) for a possible future rebuild. This is a deck-allocation change, **not** a removal of cards from the owned collection. The owner reported a first-place finish using Mono-Red Burn/Madness at a recent Pauper event; that deck remains built.

## Five current built decks

| Format | Current deck | Count |
| --- | --- | ---: |
| Commander / Grixis | [Lord Xander](current_decks/Xander_EDH_IRL.csv) | 100 + separate Lutri companion |
| Commander / Mardu | [Dihada](current_decks/Dihada_EDH_IRL.csv) | 100 |
| Commander / Jund | [Korvold](current_decks/Korvold_Jund_EDH_IRL.csv) | 100 |
| Commander / Orzhov Borg | [Locutus](current_decks/Locutus_Orzhov_Borg_EDH_IRL.csv) | 100 |
| Pauper | [Mono-Red Burn/Madness](current_decks/MonoRed_Pauper_IRL.csv) | 60 (13 incoming copies) |

**Lutri:** Xander's source contains 101 entries because Lutri, the Spellchaser is a separate physically owned companion, outside the Commander deck's 100-card limit. Lutri is banned in official Commander; the user's local store permits it by explicit Rule 0 house rule. It stays reserved.

**Incoming Mono-Red proxies:** 2 Fireblast, 4 Grab the Prize, 1 Kessig Flamebreather, 2 Lava Dart, and 4 Voldaren Epicure. The 13 incoming copies remain excluded from owned physical copies until delivery is confirmed.

## Source integrity and maintenance

The corrected master inventory [Every_Card_we_own_IRL_corrected.csv](2026-11-23/Every_Card_we_own_IRL_corrected.csv) remains unchanged and authoritative for the 1,395 physical copies. The original source archive and six submitted deck CSVs are validated by [the November 23 manifest](2026-11-23/manifest.json). The retired Mono-Black file is removed from `current_decks/` but not from the source snapshot.

Use these checks for the live five-deck allocation and the intact historical source:

```bash
python3 scripts/audit_physical_collection.py --check
python3 scripts/audit_physical_collection_2026_11_23.py --check
python3 -m unittest tests/test_physical_collection.py
```

The separate November 8 Oracle/printing knowledge catalogue is historical, not current evidence for all 793 names. The protected 62-deck Grixis Encyclopedia and approved lore decks remain untouched.
