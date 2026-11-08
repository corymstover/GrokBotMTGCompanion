# Cory and Stefanie's physical MTG collection

This is an **owned-in-real-life inventory**, not a wishlist, a proxy inventory,
an export of the protected Grixis encyclopedia, or a deckbuilding proposal.
The authoritative starting snapshot was supplied by Cory on **2026-11-08**.

**Current physical state (owner-confirmed 2026-11-08):** Cory took apart Rith,
Saruman, Orzhov Borg and Jund, then physically rebuilt Xander with 19 named
one-for-one upgrades and **Swamp → The Unicomplex**. **Only rebuilt Xander and
unchanged Dihada remain built.** The current free inventory is **1,131 cards /
621 names**, with **201 cards reserved**. Use
[`current_available.csv`](current_available.csv) for IRL-only deckbuilding and
[`current_status.json`](current_status.json) for the live deck allocation state.
The original [teardown record](2026-11-08/disassembly_confirmation.md) and the
subsequent [Xander swap event](updates/2026-11-08_xander_rebuild.json) are both
preserved.

## Which files should an agent use?

| Use | File |
| --- | --- |
| **What can actually be used in a new deck today** | [`current_available.csv`](current_available.csv) |
| **Which decks are currently built** | [`current_status.json`](current_status.json) |
| **Exact current rebuilt Xander list** | [`current_decks/Xander_EDH_IRL.csv`](current_decks/Xander_EDH_IRL.csv) |
| **20 owner-confirmed physical swaps** | [`updates/2026-11-08_xander_rebuild.json`](updates/2026-11-08_xander_rebuild.json) |
| All actual cards owned, **including every card in a deck** | [`2026-11-08/master_inventory.csv`](2026-11-08/master_inventory.csv) |
| Exact source ZIP, preserved without alteration | [`2026-11-08/original_six_decks.zip`](2026-11-08/original_six_decks.zip) |
| Human-readable six original CSVs | [`2026-11-08/decks/`](2026-11-08/decks/) |
| Cards free without changing any of the six decks | [`2026-11-08/available_unassigned.csv`](2026-11-08/available_unassigned.csv) |
| Cards available **if** the four proposed decks are disassembled | [`2026-11-08/available_after_proposed_disassembly.csv`](2026-11-08/available_after_proposed_disassembly.csv) |
| Source hashes, counts and per-deck status | [`2026-11-08/manifest.json`](2026-11-08/manifest.json) |
| Collection assessment | [`2026-11-08/analysis.md`](2026-11-08/analysis.md) |
| **Full owned-card Oracle, mana, colors, rarity history, Pauper and rules-link catalogue** | [`owned_cards/2026-11-08/manifest.json`](owned_cards/2026-11-08/manifest.json) |
| **Card-data coverage audit, limitations and commands** | [`owned_cards/2026-11-08/AUDIT_REPORT.md`](owned_cards/2026-11-08/AUDIT_REPORT.md) |

## Allocation policy

- **Keep built / reserve every physical card:** Cory's **Lord Xander, the Collector** EDH deck (100-card main deck plus **Lutri, the Spellchaser** as a separately tracked companion, 101 physical cards) **as represented by the current rebuilt list**, and Stefanie's **unchanged Dihada, Binder of Wills** EDH deck (100 cards).
- **Confirmed dismantled 2026-11-08:** **Rith, Liberated Primeval** EDH (100), **Saruman, the White Hand** EDH (100), **Cory's Orzhov Borg prerelease** (40), and **Stefanie's Jund prerelease** (**43 entries in the source CSV**, even though Cory calls it a 40-card deck). Keep all six historical CSVs unchanged.
- Master inventory = **1,332 physical cards / 751 exact names**. The historical six-deck snapshot allocated **484 cards**, without ownership shortfalls. Originally unassigned: **848 / 492 names**. The four completed disassemblies initially released **283 cards**, producing **1,131 cards / 629 names** free. Xander's subsequent 20 one-for-one swaps changed the available *names* to **621** while preserving **1,131 free copies** and **201 reserved** for Xander and Dihada.
- Removed Xander cards (including the one Swamp) return to the free pool at their exact quantities. Incoming cards are subtracted from that pool, never added to ownership. **Stefanie's Dihada card allocations are never changed.**
- The master **already includes** deck cards. Never add the deck totals to the master; that would double-count ownership.
- Never consume more copies than owned. A proposal may request cards from a keep-built deck only with an explicit disclosure and Cory's approval.
- Treat future snapshots as new dated records. Do not rewrite or erase this source evidence to describe a later trade, purchase, sale, swap, or physical disassembly.

**Important rules exception:** As of 2026-11-08, Lutri is officially banned **as a companion** in Commander, though allowed in the 99 or as a commander. Cory's Xander + Lutri setup is retained exactly as a historical/personal **Rule 0 house-rule deck**, not a certification of tournament legality. See [Wizards' February 9, 2026 announcement](https://magic.wizards.com/en/news/announcements/commander-banned-and-restricted-february-9-2026).

The snapshot lists quantities and names, **not** specific printings, condition, language, foil status, purchase price, storage box or location. Avoid fabricated price totals, print IDs, or live availability claims. The dated repository card index (2026-10-15) predates *Star Trek* prerelease and must not be used uncritically for recent card legality. Wizards lists *Star Trek* prerelease as November 6–12 and the broad tabletop release as November 13, 2026 ([official set information](https://magic.wizards.com/en/news/feature/collecting-star-trek)).

## Reproducibility

From the repository root:

```bash
python3 scripts/audit_physical_collection.py --check
python3 scripts/build_owned_card_knowledge.py check
python3 scripts/owned_cards.py stats
python3 scripts/owned_cards.py card 'Tenacious Drone'
python3 scripts/owned_cards.py pauper --available --colors WB
```

The read-only check verifies original-vs-extracted bytes, all source quantities,
deck allocations, SHA-256 hashes, both historical pool views, the exact owner-
confirmed 20-swap reconstruction, and the active availability record. Use
`--write` only when intentionally reproducing the derived live deck and pool
from the preserved sources and confirmation event.

If the active pool changes again, run
`python3 scripts/build_owned_card_knowledge.py refresh-availability` after
regenerating the physical allocation. That updates
only the owned-card catalogue's physical counts and shard checksums; Scryfall
Oracle, rarity, identity and legality metadata remains source-pinned.

**Current date-sensitive legality note:** *The Unicomplex* is physically in
Xander as confirmed, but the November 8 Scryfall source still marks it
pre-release/not yet broadly Commander-legal until the *Star Trek* tabletop
release. This is tracked separately from Cory's pre-existing Lutri-as-companion
Rule 0 exception. Physical ownership and inclusion do not establish legality.

The separate [owned-card knowledge audit](owned_cards/2026-11-08/AUDIT_REPORT.md)
indexes **all 751 names** against a newer Scryfall bulk snapshot and exposes
the **88 cards missing from the older canonical card index** without changing
that index. It includes searchable Oracle text, card faces, mana, colors,
identity, print-rarity evidence, dated format status, and authoritative rulings
links. It does **not** claim to know which specific printing Cory owns, and it
does not imply that all rulings and card combinations have been pre-verified.

This addition is separate from and makes **no changes** to the protected
62-deck Grixis Encyclopedia, lore-deck approvals, or bounded foundation
certification.
