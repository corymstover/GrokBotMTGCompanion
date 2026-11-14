# Cory and Stefanie's physical Magic collection

**Latest owner-confirmed inventory: November 14, 2026.** This folder tracks actual
copies owned and their allocation to physically constructed decks. The repository
contains no proxies or assumed extra copies; the owner's separately available
basic lands are not silently added to the submitted CSV snapshot.

## Current verified allocation

| Metric | 2026-11-08 | 2026-11-14 |
| --- | ---: | ---: |
| Owned cards | 1,332 | **1,348** |
| Distinct owned names | 751 | **766** |
| Built decks | 4 | **6** |
| Physical cards reserved | 321 | **521** |
| Unassigned copies | 1,011 | **827** |
| Distinct unassigned names | 599 | **508** |

Use [current_available.csv](current_available.csv) for **free copies** and
[current_status.json](current_status.json) for the current allocation. Both are
calculated from the exact **November 14 source** in
[2026-11-14/](2026-11-14/), not from November 8's older master.
All six active cardlists are in [current_decks/](current_decks/).

| Owner | Format / commander | Current CSV | Physical cards |
| --- | --- | --- | ---: |
| Cory | Lord Xander, the Collector — Grixis Commander | [Xander](current_decks/Xander_EDH_IRL.csv) | 101 including separate Lutri companion |
| Stefanie | Dihada, Binder of Wills — Mardu Commander | [Dihada](current_decks/Dihada_EDH_IRL.csv) | 100 |
| Stefanie | Wasitora, Nekoru Queen — Jund Commander | [Wasitora](current_decks/Wasitora_Jund_EDH_IRL.csv) | 100 |
| Cory | Locutus, the One Who Speaks — Orzhov Borg Commander | [Locutus](current_decks/Locutus_Orzhov_Borg_EDH_IRL.csv) | 100 |
| Cory | Izzet Mill/Burn Pauper (no sideboard) | [Izzet](current_decks/Izzet_Pauper_IRL.csv) | 60 |
| Stefanie | Mono-Black Devotion Control Pauper (no sideboard allocated) | [Mono-Black](current_decks/Stefanie_MonoBlack_Pauper_IRL.csv) | 60 |

The two new Commander decks each reserve 100 cards. The other four previously
built lists have **no card-count or card-identity changes** relative to the
existing repository. Xander's newly supplied source only interchanges two Jace
CSV row positions, without a card swap. No six-deck overlap exceeds ownership.

## November 14 purchase reconciliation

The master grew by **16 copies**: 15 newly recorded names and one more
*Sol'kanar the Swamp King*. See
[updates/2026-11-14_collection_reconciliation.json](updates/2026-11-14_collection_reconciliation.json)
for the exact named quantities. Three new cards are already in Stefanie's
Wasitora deck: *Slimefoot and Squee*, *Vazi, Keen Negotiator* and
*Yurlok of Scorch Thrash*.

The original uploaded ZIP is identified by SHA-256 in the November 14
[manifest](2026-11-14/manifest.json). The ZIP itself is **not committed**;
all seven original CSV member files are committed at their **exact source
bytes**, individually SHA-256 verified. Previous November 8 source files,
historical decklists, swap events, and manifest remain unchanged. The earlier
README is preserved at
[2026-11-08/README_state_2026-11-08.md](2026-11-08/README_state_2026-11-08.md).

## Verification and data status

```bash
python3 scripts/audit_physical_collection.py --check
python3 scripts/audit_physical_collection_2026_11_14.py --check
python3 scripts/build_owned_card_knowledge.py check
```

The physical-allocation checks use the new 2026-11-14 snapshot. The
[2026-11-08 owned-card Oracle knowledge](owned_cards/2026-11-08/) is **historical**:
its Scryfall data and 38 shards cover only the former 751 names. The archived
[2026-11-08 free pool](2026-11-08/available_as_of_2026-11-08.csv)
allows that historical catalogue to be checked without falsely labeling it
current. Do **not** use its old per-card available quantities for 2026-11-14
deckbuilding; use the live current_available.csv. Newly acquired card Oracle,
rarity and legality enrichment still requires a separately verified, dated
Scryfall refresh. Do not mix old printed facts with the new purchase count.

**Rules exception:** Cory's Xander list contains **Lutri, the Spellchaser**
as a separate companion, a Rule 0 exception: Lutri is banned as a Commander
companion. A physical list is not an official legality certification.

This collection update does not alter the protected 62-deck Grixis
Encyclopedia, its approvals or hashes, or approved lore decks.
