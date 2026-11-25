# Physical Magic collection — live status

**As of November 25, 2026**, the [live inventory after the owner-confirmed Balrog sale](live_inventory/2026-11-25_after_balrog_sale.csv) contains **1,470 physical card copies / 844 card names**. The [original uploaded November 25 master](2026-11-25/Every_Card_we_own_IRL_corrected.csv) is preserved intact (1,471 copies / 845 names). Source [manifest](2026-11-25/manifest.json) and [change event](updates/2026-11-25_collection_reconciliation.json) preserve SHA-256 provenance. Previous [November 23 snapshot](2026-11-23/) is immutable.

| Metric | After Nov 23 Mono-Black disassembly | Nov 25 |
| --- | ---: | ---: |
| Owned physical copies | 1,395 | **1,470** |
| Distinct owned names | 793 | **844** |
| Built decks | 5 | **5** |
| Deck slots including separate Lutri companion | 461 | **461** |
| Owned deck cards reserved | 448 | **448** |
| Mono-Red incoming proxy cards | 13 | **13** |
| Available physical copies | 947 | **1,022** |
| Distinct available names | 549 | **610** |

**Owner-confirmed Dihada swap and sale:** 1× **The Balrog, Durin's Bane** OUT, 1× **Ingris Stingerquill** IN. The owner confirmed that the Balrog was **sold to acquire Ingris**, so the Balrog is no longer physically owned or available; Ingris remains reserved to Dihada. This correction changes inventory only—not any of the five active decklists. See the [sale event](updates/2026-11-25_balrog_sale.json).

**Sale correction:** The Balrog was originally counted as unassigned after the Dihada swap, but the owner later clarified it was sold to acquire Ingris. The live totals are reduced by exactly one Balrog copy and one unique name; reserved copies, proxies, and all five decklists remain unchanged. Original uploads, manifests, and events are retained as historical records.

**November 25 original upload reconciliation:** 77 copies added/increased, 1 removed/decreased, net +76. The new source omits **Cavern-Hoard Dragon**, which appeared once in the November 23 inventory; this absence is recorded as an inventory change, not assumed to represent a sale. New acquisitions now reserved to the owner-confirmed Xander list include Fraying Sanity, Hedron Crab, Ruin Crab, Zellix, Nicol Bolas, God-Pharaoh, and faster mana rocks; Gandalf, Goblins' Bane remains available.

**Dihada owner-confirmed upgrade (November 25, 2026):** the [current live list](current_decks/Dihada_EDH_IRL.csv) has **five additions / five cuts** relative to the uploaded November 25 source. The complete [user-approved Archidekt list, including set codes and foil markers](approvals/2026-11-25_Dihada_IRL_approved_archidekt.txt), and [exact change event](updates/2026-11-25_dihada_upgrade.json) are preserved. **OUT:** Tymaret, the Murder King; Honor-Worn Shaku; Day of Destiny; Brion Stoutarm; Blackblade Reforged. **IN:** Edgar, Ancient Bloodlord; Windcrag Siege; Hellrider; Mirror of Galadriel; Rakdos Signet. **Heroes' Podium, Piru, the Volatile, and Zeriam, Golden Wind stay in Dihada.** The live deck remains 100 cards including commander, with 36 lands; the other four decks are unchanged. Total physical inventory stays at 1,470 copies / 844 names; **1,022 available copies / 610 names**. These live deck changes do not rewrite the historical source snapshots.

## Five active decks

| Format | Link | Deck slots |
| --- | --- | ---: |
| Grixis Commander | [Lord Xander](current_decks/Xander_EDH_IRL.csv) | 100 + separate Lutri companion |
| Mardu Commander | [Dihada](current_decks/Dihada_EDH_IRL.csv) | 100 |
| Jund Commander | [Korvold](current_decks/Korvold_Jund_EDH_IRL.csv) | 100 |
| Orzhov Commander | [Locutus Borg](current_decks/Locutus_Orzhov_Borg_EDH_IRL.csv) | 100 |
| Pauper | [Mono-Red Burn/Madness](current_decks/MonoRed_Pauper_IRL.csv) | 60, 13 incoming proxies |

Stefanie's previously dismantled **Mono-Black Devotion Pauper** remains archived in [November 23 source](2026-11-23/Mono_Black_Devotion_Control.csv); its 60 cards were released for reuse, though some have since been reassigned to active decks. Xander's **Lutri, the Spellchaser** remains a locally permitted companion *outside* the 100-card deck; Lutri is officially banned **as a Commander companion** and this house-rule exception is not official format legality.

**Active verification:** `python3 scripts/audit_physical_collection.py --check`, `python3 scripts/audit_physical_collection_2026_11_25.py --check`, and `python3 -m unittest tests/test_physical_collection.py`. The historical owned-card Oracle catalogue remains dated November 8, and does not certify all 844 current names. The protected 62-deck encyclopedia and approved lore decks are untouched.
