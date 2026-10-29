# MTG Set & Printing Atlas — October 29, 2026

## Snapshot and scope

This Atlas documents **1,062 Scryfall set codes present in the independently verified October 29 Default Cards bulk snapshot**, not 1,062 premier expansion sets. The October 29 bulk contains **119,701 default-language printing records** and **107,898 English paper printing records**, including announced future-dated printings. Details: [October 29 set catalog](data/set_atlas/catalog_2026-10-29.json).

On October 29 at 23:38:34 UTC, the Scryfall **Set API** was fetched once and its selected metadata fields were frozen in [the sourced set metadata snapshot](data/set_atlas/scryfall_set_metadata_2026-10-29.json). All 1,062 codes in the card-printing Atlas mapped to its 1,063 reported set codes. The additional API-only set code is `nau`, *Nauctis: The Sunken Realm*, dated 2027-02-05; it is **not** retroactively included in the October 29 printing Atlas.

**Source:** [Scryfall /sets API](https://api.scryfall.com/sets) and [Set object documentation](https://scryfall.com/docs/api/sets). The Set object provides `released_at`, `set_type`, `digital`, `parent_set_code`, `card_count`, and `printed_size`. These are distinct from individual-card printing metadata.

## Validated product metadata

- [Complete normalized product catalog](data/set_atlas/product_catalog_2026-10-29.json) — names, set codes, category, release/first-print date, digital status, explicit parent links, and direct joins to printing counts.
- [Reproducible product audit](data/set_atlas/product_audit_2026-10-29.json) — 1,062 matched codes, **560 explicit parent-set relationships**, zero conflicts, ten future-dated set codes, and 142 released non-digital sets *classified by Scryfall* as `expansion` or `core`.
- **Not a premier release certification:** 142 is the number of category-qualified candidates under this snapshot and date policy, **not** an officially certified count of premier expansions. Reclassify only with independently sourced Wizards product taxonomy and dates.
- `parent_set_code` is interpreted literally. Names, shared codes, thematic links, and release proximity do not prove parentage. Missing parent links remain unresolved.
- `released_at` is the Set API's release-or-first-card date; it does **not** represent every printing's first availability or prove a mainline story chronology.
- The Set API was fetched later than the archived October 29 card bulk; the sources are independently time-stamped. The original historical October 28 bulk download is not independently available.

## Read-only lookups

On a checkout of this repository, no Scryfall download is needed for the following commands:

```bash
python3 scripts/set_product_lookup.py --code lea
python3 scripts/set_product_lookup.py --year 1994 --type expansion --all
python3 scripts/set_product_lookup.py --parent dmu --all
python3 scripts/set_product_lookup.py --name Commander --all
python3 scripts/historical_set_lookup.py set lea --all
python3 scripts/historical_set_lookup.py card "Black Lotus" --all
```

The last two commands read the [32 historical GitHub-readable index shards](data/set_atlas) from the **October 28 committed shard collection**, not the October 29 bulk. See the [historical 105-shard audit](data/set_atlas/historical_shard_audit_2026-10-29.json) for exact hashes and counts. Keep dates and denominators separate.

**Integrity checks:** `python3 scripts/audit_set_product_links.py --check`, `python3 scripts/publish_historical_set_index.py`, and focused Phase 1B GitHub Actions. The first command deliberately replays the frozen October 29 metadata and **never silently refreshes** Scryfall data.
