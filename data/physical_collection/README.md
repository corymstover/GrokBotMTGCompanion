# Cory and Stefanie's physical MTG collection

This is an **owned-in-real-life inventory**, not a wishlist, a proxy inventory,
an export of the protected Grixis encyclopedia, or a deckbuilding proposal.
The authoritative starting snapshot was supplied by Cory on **2026-11-08**.

## Which files should an agent use?

| Use | File |
| --- | --- |
| All actual cards owned, **including every card in a deck** | [`2026-11-08/master_inventory.csv`](2026-11-08/master_inventory.csv) |
| Exact source ZIP, preserved without alteration | [`2026-11-08/original_six_decks.zip`](2026-11-08/original_six_decks.zip) |
| Human-readable six original CSVs | [`2026-11-08/decks/`](2026-11-08/decks/) |
| Cards free without changing any of the six decks | [`2026-11-08/available_unassigned.csv`](2026-11-08/available_unassigned.csv) |
| Cards available **if** the four proposed decks are disassembled | [`2026-11-08/available_after_proposed_disassembly.csv`](2026-11-08/available_after_proposed_disassembly.csv) |
| Source hashes, counts and per-deck status | [`2026-11-08/manifest.json`](2026-11-08/manifest.json) |
| Collection assessment | [`2026-11-08/analysis.md`](2026-11-08/analysis.md) |

## Allocation policy

- **Keep built / reserve every physical card:** Cory's **Lord Xander, the Collector** EDH deck (100-card main deck plus **Lutri, the Spellchaser** as a separately tracked companion, 101 physical cards), and Stefanie's **Dihada, Binder of Wills** EDH deck (100 cards).
- **Only a proposed disassembly, not a completed action:** **Rith, Liberated Primeval** EDH (100), **Saruman, the White Hand** EDH (100), **Cory's Orzhov Borg prerelease** (40), and **Stefanie's Jund prerelease** (**43 entries in the source CSV**, even though Cory calls it a 40-card deck). Keep all six historical CSVs unchanged.
- Master inventory = **1,332 physical cards / 751 exact names**. Six recorded deck allocations = **484 cards**, with **no allocations exceeding owned quantities**. Unassigned = **848 cards / 492 names**. The four proposed disassemblies would release **283 cards**, resulting in **1,131 available cards / 629 names**, with **201 cards reserved** for Xander and Dihada.
- The master **already includes** deck cards. Never add the deck totals to the master; that would double-count ownership.
- Never consume more copies than owned. A proposal may request cards from a keep-built deck only with an explicit disclosure and Cory's approval.
- Treat future snapshots as new dated records. Do not rewrite or erase this source evidence to describe a later trade, purchase, sale, swap, or physical disassembly.

**Important rules exception:** As of 2026-11-08, Lutri is officially banned **as a companion** in Commander, though allowed in the 99 or as a commander. Cory's Xander + Lutri setup is retained exactly as a historical/personal **Rule 0 house-rule deck**, not a certification of tournament legality. See [Wizards' February 9, 2026 announcement](https://magic.wizards.com/en/news/announcements/commander-banned-and-restricted-february-9-2026).

The snapshot lists quantities and names, **not** specific printings, condition, language, foil status, purchase price, storage box or location. Avoid fabricated price totals, print IDs, or live availability claims. The dated repository card index (2026-10-15) predates *Star Trek* prerelease and must not be used uncritically for recent card legality. Wizards lists *Star Trek* prerelease as November 6–12 and the broad tabletop release as November 13, 2026 ([official set information](https://magic.wizards.com/en/news/feature/collecting-star-trek)).

## Reproducibility

From the repository root:

```bash
python3 scripts/audit_physical_collection.py --check
```

The read-only check verifies original-vs-extracted bytes, all source quantities,
deck allocations, SHA-256 hashes and both generated pool views. Use `--write`
only when intentionally reproducing derived files from these *unchanged* sources.

This addition is separate from and makes **no changes** to the protected
62-deck Grixis Encyclopedia, lore-deck approvals, or bounded foundation
certification.
