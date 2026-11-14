# Cory and Stefanie's physical MTG collection

This is an **owned-in-real-life inventory**, not a wishlist, a proxy inventory,
an export of the protected Grixis encyclopedia, or a deckbuilding proposal.
The authoritative starting snapshot was supplied by Cory on **2026-11-08**.

**Current physical state (owner-confirmed 2026-11-08):** Cory took apart Rith,
Saruman, Orzhov Borg and Jund, then physically rebuilt Xander with 19 named
one-for-one upgrades and **Swamp → The Unicomplex**. Cory subsequently confirmed
Stefanie physically rebuilt Dihada with **15 exact one-for-one swaps**, including
four mana-base changes. Cory then confirmed his **60-card Izzet Mill–Burn Pauper**
deck is sleeved up, **without a sideboard**, and Stefanie's **60-card Mono-Black
Devotion Control Pauper** deck is also **"Sleeved up! Locked in."** There are now
**four built decks**: Xander, Dihada, Izzet Pauper and Mono-Black Pauper. The
current free inventory is **1,011 cards / 599 names**, with **321 cards reserved**. Use
[`current_available.csv`](current_available.csv) for IRL-only deckbuilding and
[`current_status.json`](current_status.json) for the live deck allocation state.
The original [teardown record](2026-11-08/disassembly_confirmation.md) and the
subsequent [Xander swap event](updates/2026-11-08_xander_rebuild.json) and
[Dihada swap event](updates/2026-11-08_dihada_rebuild.json), and
[Izzet Pauper build event](updates/2026-11-08_izzet_pauper_build.json), and
[Stefanie's Mono-Black build event](updates/2026-11-08_stefanie_monoblack_pauper_build.json) are preserved.

## Which files should an agent use?

| Use | File |
| --- | --- |
| **What can actually be used in a new deck today** | [`current_available.csv`](current_available.csv) |
| **Which decks are currently built** | [`current_status.json`](current_status.json) |
| **Exact current rebuilt Xander list** | [`current_decks/Xander_EDH_IRL.csv`](current_decks/Xander_EDH_IRL.csv) |
| **Exact current rebuilt Dihada list** | [`current_decks/Dihada_EDH_IRL.csv`](current_decks/Dihada_EDH_IRL.csv) |
| **Exact current sleeved Izzet Pauper main deck (no sideboard)** | [`current_decks/Izzet_Pauper_IRL.csv`](current_decks/Izzet_Pauper_IRL.csv) |
| **Exact current sleeved Stefanie Mono-Black Pauper main deck (no sideboard)** | [`current_decks/Stefanie_MonoBlack_Pauper_IRL.csv`](current_decks/Stefanie_MonoBlack_Pauper_IRL.csv) |
| **20 owner-confirmed physical swaps** | [`updates/2026-11-08_xander_rebuild.json`](updates/2026-11-08_xander_rebuild.json) |
| **15 owner-confirmed Dihada swaps** | [`updates/2026-11-08_dihada_rebuild.json`](updates/2026-11-08_dihada_rebuild.json) |
| **60-card Pauper build confirmation and explicit zero sideboard** | [`updates/2026-11-08_izzet_pauper_build.json`](updates/2026-11-08_izzet_pauper_build.json) |
| **Stefanie's 60-card Mono-Black Pauper confirmation** | [`updates/2026-11-08_stefanie_monoblack_pauper_build.json`](updates/2026-11-08_stefanie_monoblack_pauper_build.json) |
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

- **Keep built / reserve every physical card:** Cory's **Lord Xander, the Collector** EDH deck (100-card main deck plus **Lutri, the Spellchaser** as a separately tracked companion, 101 physical cards) and Stefanie's **Dihada, Binder of Wills** EDH deck (100 cards), **both as represented by their separately rebuilt current lists**.
- **Newly built / reserve 60 more cards:** Cory's **Izzet Mill–Burn Pauper** main deck (60 cards: 21 lands and 39 nonlands); he explicitly declined the sideboard, so there are **zero sideboard cards allocated**. The 16 exact quantities and main-deck checksum are preserved separately from the original six-deck snapshot.
- **Newly built / reserve 60 more cards:** Stefanie's **Mono-Black Devotion Control Pauper** main deck (60 cards: 24 Swamps, 21 creatures, and 15 other spells). Cory confirmed it is physically sleeved and locked in. The 15 exact quantities and main-deck checksum are separately preserved. No sideboard was included in the proposed/sleeved list or reserved.
- **Confirmed dismantled 2026-11-08:** **Rith, Liberated Primeval** EDH (100), **Saruman, the White Hand** EDH (100), **Cory's Orzhov Borg prerelease** (40), and **Stefanie's Jund prerelease** (**43 entries in the source CSV**, even though Cory calls it a 40-card deck). Keep all six historical CSVs unchanged.
- Master inventory = **1,332 physical cards / 751 exact names**. The historical six-deck snapshot allocated **484 cards**, without ownership shortfalls. Originally unassigned: **848 / 492 names**. The four completed disassemblies initially released **283 cards**, producing **1,131 cards / 629 names** free. Xander's 20 swaps changed available *names* to **621**; Dihada's subsequent 15 swaps left that name count unchanged. Cory's 60-card Izzet Pauper build brought availability to **1,071 / 611 names**, and Stefanie's subsequent 60-card Mono-Black Pauper build brought the **current state to 1,011 free copies / 599 names** and **321 reserved**.
- Removed Xander **and Dihada** cards (including the respective basic-land reductions) return to the free pool at their exact quantities. Incoming cards are subtracted, never added to ownership. Both Commander decklists are reconstructible from their untouched historical sources plus separate swap events; the two Pauper build events independently account for **60 reserved physical copies each**, with no sideboard reservations.
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
confirmed 20-swap Xander and 15-swap Dihada reconstructions, both exact 60-card
Pauper main decks with no sideboards, and the active availability record. Use `--write` only when intentionally reproducing the
derived live decks and pool from the preserved sources and confirmation events.

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
