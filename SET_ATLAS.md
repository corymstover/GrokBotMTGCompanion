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

## Official Wizards release-family review (first bounded batch)

A [2023–October 2026 Wizards-backed classification](data/set_atlas/wotc_release_classification_2026-10-29.json) tracks **30 exact set codes** using the [primary-source per-code evidence ledger](data/set_atlas/wotc_reviewed_release_evidence_2026-10-29.json). The source scope and counting criteria are reproducible with `python3 scripts/audit_wotc_premier_sets.py`. Primary sources include [Wizards' product releases](https://magic.wizards.com/en/products), its [Standard release notes](https://magic.wizards.com/en/news/feature/phyrexia-all-will-be-one-release-notes), and [Mark Rosewater's terminology explanation](https://magic.wizards.com/en/news/making-magic/odds-ends-strixhaven-part-1-2021-05-03).

**Confirmed in the reviewed period:** 21 official main releases through October 29, 2026 (13 on Wizards' `Set Releases` page, six on the `Universes Beyond Set Releases` page, and two additional main sets supported by 2023 Wizards release notes).

**Important exclusions and category differences:** `MAT` is an independently released, Standard-legal **epilogue micro set**, not a typical main release. `BIG` is a separately coded **subset** within the Outlaws of Thunder Junction product. `OM1` is a **digital Universes Within counterpart**, not another tabletop premier release. `MH3`, `ACR`, `PIP`, and `INR` are independently listed by Wizards as **special products**. `TRK` and `MDD` were future-dated as of the cutoff. Source links and exact statements are preserved per code.

Of the **142** released, nondigital `expansion`/`core` Scryfall category candidates in the entire snapshot, **21** have source-backed regular-main-release classification, **two** are documented as an epilogue/subset, and **119** older candidates remain unreviewed. **Do not report 142, or 21, as Magic's all-time premier set count.** The archive's 1,062 set codes include many tokens, promos, supplemental products, and digital releases.

## Historical regular-set census: 1993–2002

The [Wizards-source evidence file](data/set_atlas/wotc_early_release_evidence_1993_2002.json) and [deterministic 38-code audit](data/set_atlas/wotc_early_release_audit_1993_2002.json) review every 1993–2002 set code in Scryfall's *released non-digital expansion/core* category against Wizards' [year-by-year historical booster retrospective](https://magic.wizards.com/en/news/making-magic/looking-back-part-1) and [enumeration of regular core editions](https://magic.wizards.com/en/news/making-magic/trivial-pursuit-more-or-less).

- **35** codes are supported as historically regular expansion/core releases, including Limited Edition Alpha, Beta and Unlimited as separately sold core editions.
- **Summer Magic/Edgar (`sum`)** is separately listed in Scryfall but Wizards [describes it as an abandoned Revised print run](https://magic.wizards.com/en/news/making-magic/25-more-random-things-about-magic-2016-06-20), with a small amount distributed accidentally. It is not counted as another regularly published core edition.
- **`fbb` and `4bb`** represent localized black-border variations in Scryfall. Wizards' regular core edition enumeration omits them, but their exact production/edition classification is **provisional** pending more direct primary-source verification; neither is silently declared definitively excluded.
- Arabian Nights is indexed by Scryfall as December 1993, with [Wizards acknowledging geographic release timing across late 1993 and early 1994](https://magic.wizards.com/en/news/making-magic/25-random-things-about-magic-2009-02-16).

Across this early review and the 2023–October 2026 review, the published **142** released non-digital Scryfall expansion/core candidates break down into **56 primary-source-supported mainline/regular releases**, **3 directly documented auxiliary/discarded products**, **2 provisional localized variants**, and **81 entirely unreviewed 2003–2022 candidates**. **This does not yet constitute an all-time count of premier Magic sets.** The older era predates the modern Wizards marketing term *premier release*, and Scryfall `set_type` is not the same as a historical product taxonomy.

The regeneration command is `python3 scripts/audit_wotc_early_sets.py` (use `--write` only to intentionally update the dated report). Passing tests reject unreviewed, duplicate, mismatched or unofficially sourced classifications.

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
