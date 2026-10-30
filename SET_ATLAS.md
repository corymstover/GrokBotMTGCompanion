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

## Historical regular/mainline release review: 2003–2022

The [81-code Wizards evidence ledger](data/set_atlas/wotc_mid_release_evidence_2003_2022.json) and [reproducible 2003–2022 audit](data/set_atlas/wotc_mid_release_audit_2003_2022.json) link exact set codes to Wizards' yearly release retrospectives [Part 1](https://magic.wizards.com/en/news/making-magic/looking-back-part-1), [Part 2](https://magic.wizards.com/en/news/making-magic/looking-back-part-2), and the [complete regular core-edition list](https://magic.wizards.com/en/news/making-magic/trivial-pursuit-more-or-less).

Of 81 dated, released, nondigital Scryfall `expansion`/`core` candidates, **80** are directly supported as regular historical expansion/core releases; **`tsb` (Time Spiral Timeshifted)** is an integrated *bonus sheet* described as such by Wizards, not a separately launched main expansion. The evidence is historical: neither editorial 2024 retrospective automatically labels every earlier product with the modern marketing term *premier*.

### Snapshot-wide reconciliation

| Defined category | Count |
| --- | ---: |
| Released, nondigital Scryfall `expansion`/`core` candidate codes | **142** |
| Sourced historically regular/mainline releases across reviewed eras | **136** |
| Directly documented micro/subset/abandoned/bonus codes (`mat`, `big`, `sum`, `tsb`) | **4** |
| Foreign-border localized variant codes still requiring direct corroboration (`fbb`, `4bb`) | **2** |
| Unreviewed codes *within this 142-code Scryfall category* | **0** |

**This is not yet an all-time Wizards premier-set census.** It is a rigorous classification of a particular Scryfall category in a dated snapshot. Official main products outside `expansion`/`core` (for example other drafting or supplemental product families) must be considered under a separately stated definition. Early foreign-border variants remain provisional, and Wizards did not use modern product terminology for the full 1993–2022 history.

Read-only replay: `python3 scripts/audit_wotc_mid_sets.py`; unit tests: `python3 -m unittest discover -s tests -p test_wotc_mid_sets.py -v`.

## Cross-category release and product-family audit

The [complete 1,062-code October 29 Scryfall category audit](data/set_atlas/cross_category_audit_2026-10-29.json) is generated from the dated, normalized [Scryfall product catalog](data/set_atlas/product_catalog_2026-10-29.json) and conserves all codes in **four mutually exclusive buckets**:

| October 29, 2026 category | Codes |
| --- | ---: |
| Released paper, Scryfall `expansion` or `core` | 142 |
| Released paper, **all other Scryfall categories** | 848 |
| Released digital-only codes | 62 |
| Announced but future-dated codes | 10 |
| **All Scryfall set codes** | **1,062** |

The 848 includes promos, tokens, reprints, Masters, Commander, Jumpstart, and other categories. This does **not** mean there are 848 additional premiere sets.

A [12-code, Wizards-source-backed supplemental review](data/set_atlas/cross_category_evidence_2026-10-29.json) demonstrates why category distinctions matter. It recognizes *The Lord of the Rings: Tales of Middle-earth* (`LTR`) as a large **Modern-legal, non-Standard** 2023 booster release, not a 2023 Standard-premier set; *Assassin's Creed* (`ACR`) and the three Modern Horizons sets as non-Standard Modern releases; Commander Masters and remastered sets as reprint products; and Jumpstart, Commander, and Commander Legends as different release families. Their official product or release notes and the exact support for each classification are linked in the evidence ledger.

Official contemporaneous policy: [Wizards' 2022 definition of premier releases](https://magic.wizards.com/en/news/announcements/magic-the-gathering-pricing-update) refers to four major annual Standard releases, while excluding supplemental lines. [Wizards' change announced in 2024 for Universes Beyond releases in 2025 and later](https://magic.wizards.com/en/news/announcements/aligning-the-universes-making-all-our-sets-legal-in-all-our-formats) was explicitly forward-only; it does not retroactively add LTR or ACR to the original Standard releases.

**Remaining research:** 836 outside-category paper set codes still lack this individual Wizards-source review, and the two early foreign-language border sets `FBB` and `4BB` still need direct Wizards verification. [Cardmarket's Core Sets guide](https://help.cardmarket.com/en/CoreSets) independently corroborates their status as localized black-border printings of existing Revised and Fourth Edition, but this **third-party account is not primary evidence** and does not close the official-source gate. The headline **136** remains the scoped historically regular/mainline `expansion`/`core` total—not a universal all-time premier-set count.

Regenerate or verify the dated category report with `python3 scripts/audit_set_cross_category.py`. It does not require a Scryfall download and does not mutate the historical Grixis snapshot.

## Reproducible five-cohort product-family research queue

The [complete October 29 family triage](data/set_atlas/product_family_triage_2026-10-29.json) uses **only** the verified frozen Scryfall `set_type` metadata to assign each of the **848 released non-digital outside-expansion/core set codes** to one *research queue*:

| Metadata-based queue | Codes | Individually Wizards-reviewed | Still pending |
| --- | ---: | ---: | ---: |
| Promotional records and extras | 645 | 0 | 645 |
| Preconstructed and boxed | 112 | 2 | 110 |
| Draft and starter variants | 51 | 7 | 44 |
| Reprint and curated products | 34 | 3 | 31 |
| Special inserts and Eternal subsets | 6 | 0 | 6 |
| **All outside-category released paper codes** | **848** | **12** | **836** |

**These five group names are *research-cohort labels*, not Wizards classifications.** The underlying exact `set_type`, date, direct Scryfall `parent_set_code` (when given), snapshot printing counts, and individual primary-source review status remain separately available for every code. A missing parent association **does not** mean a standalone release. For example, Scryfall puts *The List* (`PLST`), localized *Chronicles Foreign Black Border* (`BCHR`), Renaissance (`REN`), Rinascimento (`RIN`), and *Universes Within* (`SLX`) in the Masters category; we do **not** automatically claim each is a separately sold draft set.

The database includes a priority-sorted list of **836 source-pending codes**. The first research tier contains only the **44 source-pending** draft/starter codes (including Conspiracy, Battlebond and Jumpstart); **31 reprint/curated codes** follow. This is intended to reduce repetitive official-source lookups without converting metadata assumptions into certified facts.

Offline commands (no bulk Scryfall download required):

```bash
python3 scripts/product_family_lookup.py --summary
python3 scripts/product_family_lookup.py --cohort draft_and_starter_variants --only-pending --all
python3 scripts/product_family_lookup.py --type masters --only-pending --all
python3 scripts/product_family_lookup.py --parent afr --all
python3 scripts/product_family_lookup.py --code ltr
python3 scripts/audit_product_family_triage.py
```

The Atlas draws the original counts from the [dated Scryfall `/sets` API](https://scryfall.com/docs/api/sets). Wizards' [product guide](https://magic.wizards.com/en/product-guide) describes the distinct product purposes for boosters, Commander decks and Jumpstart, but that product guide is not a source certifying each of the 836 individual set codes. The original twelve Wizards-reviewed examples retain their own official primary-source citations in the [cross-category source ledger](data/set_atlas/cross_category_evidence_2026-10-29.json).

## Wizards source review: first 23 draft/starter products

The [first 23-code Wizards primary-source ledger](data/set_atlas/draft_starter_primary_sources_2026-10-29.json) includes **23 additional reviewed products** originally found in the 44-code draft/starter source queue. Its [deterministic audit](data/set_atlas/draft_starter_primary_audit_2026-10-29.json) accounts for earlier reviews and publishes the updated **35 reviewed / 813 individually source-pending** status across the original 848 outside-category paper codes. **21** of those pending are still in the draft/starter research cohort.

The reviewed group distinctions are grounded directly in Wizards' published articles:

- [Portal, Portal Second Age, Portal Three Kingdoms, and Starter 1999/2000](https://magic.wizards.com/en/news/making-magic/starting-with-a-good-foundations-part-1) were introductory products with distinct designs and beginner-oriented rules or play experiences.
- [Unglued/Unhinged/Unstable/Unfinity](https://magic.wizards.com/en/news/making-magic/lessons-learned-part-7) are supplemental Un- releases; [Unsanctioned](https://magic.wizards.com/en/news/announcements/announcing-unsanctioned-2019-10-10) is a preconstructed five-deck box, not another booster set. [Unfinity sticker sheets](https://magic.wizards.com/en/news/feature/unfinity-release-notes-2022-10-07) are components of Unfinity packs, not independent set releases.
- [Conspiracy](https://magic.wizards.com/en/news/feature/conspiracy-mechanics), [Conspiracy: Take the Crown](https://magic.wizards.com/en/news/feature/conspiracy-take-crown-mechanics-2016-08-15), and [Battlebond](https://magic.wizards.com/en/news/feature/battlebond-mechanics-2018-05-21) were intended for multiplayer Limited games.
- [Jumpstart](https://magic.wizards.com/en/news/announcements/introducing-jumpstart-new-way-play-magic-2020-02-20) and [Foundations Jumpstart](https://magic.wizards.com/en/news/announcements/foundations-jumpstart-booster-themes) have separately sold themed 20-card boosters and are not additional Standard premier releases.
- [Innistrad Double Feature](https://magic.wizards.com/en/news/feature/innistrad-double-feature-product-overview-2021-11-15) combines cards from two earlier releases into a draft-ready product; [Commander Legends: Battle for Baldur's Gate](https://magic.wizards.com/en/news/feature/commander-legends-battle-for-baldurs-gate-product-overview) supports Commander Draft; [Ravnica: Clue Edition](https://magic.wizards.com/en/news/announcements/ravnica-clue-edition-ravnica-cluedo-edition-booster-contents) is a themed boxed multiplayer game.
- Mystery Booster's [2019](https://magic.wizards.com/en/news/feature/mystery-booster-release-notes-2019-11-11) and [2021 Convention Edition](https://magic.wizards.com/en/news/announcements/mystery-booster-convention-edition-returns-store-events-2021-06-21) playtest sheets are differentiated from the main Mystery Booster printings. The [Magic Origins Clash Pack](https://magic.wizards.com/en/news/feature/magic-origins-clash-pack-and-intro-pack-decklists-2015-07-09) comprises two prebuilt decks.

**Legality caution:** [Wizards' Mystery Booster Commander Edition product article](https://www.magic.wizards.com/en/news/feature/whats-inside-mystery-booster-commander-edition) states that the new-to-Magic cards become **Commander-legal on November 13, 2026**, and enter other Eternal formats on January 1, 2027. The Scryfall set-level date **October 19, 2026** is not evidence that those new cards were Commander-legal at that time. A set's release date is not its entire card-pool legality schedule.

The [offline product-family lookup](scripts/product_family_lookup.py) now overlays the source-backed review records so it displays **35/813**, while retaining the original 12/836 frozen triage as a historical file. This avoids overwriting previously verified sources. Reproduce with `python3 scripts/audit_draft_starter_sources.py`, and inspect examples using `python3 scripts/product_family_lookup.py --code mbc` or `--cohort draft_and_starter_variants --only-pending --all`.

**Not yet reviewed individually:** `cp1`, `cp2`, `h17`, `h1r`, `h2r`, `hho`, `itp`, `ph17`, `ph18`, `ph19`, `ph20`, `ph21`, `ph22`, `ph23`, `phtr`, `ptg`, `punk`, `ulst`, `unk`, `w16`, and `w17`. No official-source or premier conclusion is invented for these 21 codes.

## Additional Wizards evidence — graded eight-code draft/starter batch

The [second eight-code evidence ledger](data/set_atlas/draft_starter_evidence_batch2_2026-10-29.json) and [deterministic audit](data/set_atlas/draft_starter_batch2_audit_2026-10-29.json) extend the earlier 23-product report without overwriting it. Across the **848 released nondigital outside-expansion/core Scryfall codes**, now **43** have direct Wizards *product-family* evidence and **805** remain source-pending. Of the 43, eight were added in this batch, and the **draft/starter** review queue is down to **13**.

For source integrity, the new ledger distinguishes two kinds of claims:

- **Wizards names the exact set code:** `H2R` is expressly named as a group of Modern Horizons 1/2 retro-frame reprints in [Collecting Modern Horizons 3](https://magic.wizards.com/en/news/feature/collecting-modern-horizons-3); `W17` is expressly called the ancillary Welcome Deck code in [Ixalan Release Notes](https://magic.wizards.com/en/news/feature/ixalan-release-notes).
- **Wizards establishes the product family, while Scryfall supplies the archived set code:** `H1R` is a retro-reprint component within [Modern Horizons 2](https://magic.wizards.com/en/news/feature/collecting-modern-horizons-2-2021-05-21); `ULST` denotes [The List reprints in Unfinity Collector Boosters](https://magic.wizards.com/en/news/feature/list-unfinity-un-usual-twist-list-2022-09-20); `H17` covers the [HASCON crossover card collaboration](https://magic.wizards.com/en/news/making-magic/unstable-scraps-part-3-2017-12-11); `HHO` traces Wizards' [employee/business holiday cards](https://magic.wizards.com/en/news/making-magic/seeing-forest-treefolk-2007-12-17-0); `PTG` identifies the limited [Extra Life charity Ponies product](https://magic.wizards.com/en/news/announcements/magic-extra-life-2019-10-03); and `UNK` tracks [Gavin's Unknown Event playtest cards](https://magic.wizards.com/en/news/feature/whats-inside-mystery-booster-2).

**Do not turn a family citation into an assertion that Wizards published the precise Scryfall set code.** The remaining **13** are `CP1`, `CP2`, `ITP`, `PH17`–`PH23`, `PHTR`, `PUNK`, and `W16`. None is automatically premier or Standard-legal based on its Scryfall category. Consult the dated [graded review report](data/set_atlas/draft_starter_batch2_audit_2026-10-29.json) and the current [offline lookup](scripts/product_family_lookup.py) for exact evidence flags. A replay check is `python3 scripts/audit_draft_starter_batch2.py`.

## Wizards reprint and curated-product review (28 source-backed additions)

The [28-code Wizards source ledger](data/set_atlas/reprint_curated_sources_2026-10-29.json) and [deterministic reprint/curated audit](data/set_atlas/reprint_curated_source_audit_2026-10-29.json) extend the earlier 43 outside-category evidence entries. This dated October 29, 2026 milestone brings the full **848** released non-digital outside-category set-code research pool to **71 official product-family source reviews** and **777 still source-pending**. Only **3** in this 34-code cohort lack sufficient individual evidence: **`BCHR` (Chronicles Foreign Black Border), `RIN` (Rinascimento), and `SS2` (Signature Spellbook: Gideon)**.

**The reviewed reprint families are not interchangeable:**

- **10 fixed From the Vault collections:** Wizards [explicitly enumerates all ten releases](https://magic.wizards.com/en/news/making-magic/trivial-pursuit-more-or-less), from *Dragons* through *Transform*. These are fixed collector compilations, not draft booster expansions. Wizards [describes Transform](https://magic.wizards.com/en/news/announcements/see-cards-vault-transform-2017-11-06) as 15 premium-foil transforming reprints.
- **Randomized Masters reprint boosters:** Wizards' [Double Deal](https://magic.wizards.com/en/news/making-magic/double-deal-2020-07-20) confirms the 2013/2015 Modern Masters, Eternal Masters, 2017 Modern Masters and Iconic Masters, 2018 Masters 25 and Ultimate Masters, and 2020 Double Masters product line. The [historical release retrospective](https://magic.wizards.com/en/news/making-magic/looking-back-part-2) separately identifies *Time Spiral Remastered*, *Double Masters 2022*, and *Dominaria Remastered* as randomized releases. These products are not automatically Standard-premier expansions.
- **Other independently released reprint boosters:** Wizards' [Mystery Booster 2 product guide](https://magic.wizards.com/en/news/feature/whats-inside-mystery-booster-2) details its event-based distribution and reprint/playtest booster construction. Wizards' [1995 retrospective](https://magic.wizards.com/en/news/making-magic/looking-back-part-1) names both *Chronicles* and *Renaissance*; the latter's precise localized release history needs further dedicated research.
- **Embedded reprint groups, not standalone booster sets:** [The List](https://magic.wizards.com/en/news/announcements/whats-new-on-the-list-for-wilds-of-eldraine) is a rotating selection of reprints inserted in other releases' Set Boosters. **`SLX` (Universes Within)** is a code Wizards itself prints for mechanically equivalent in-Magic versions of Universes Beyond Secret Lair cards found in The List. Neither `PLST` nor `SLX` represents a standalone new draft booster line.
- **Fixed Signature Spellbooks:** Wizards' [Jace](https://magic.wizards.com/en/news/announcements/signature-spellbook-jace-packaging-and-contents-2018-03-20) and [Chandra](https://magic.wizards.com/en/news/announcements/signature-spellbook-chandra-packaging-and-contents-2020-06-03) articles specify eight fixed cards plus a randomly selected premium foil. `SS2` (Gideon) remains individually source-pending in this strict ledger rather than inferring verification from adjacent Spellbooks.

**Provenance:** One new reviewed record (`SLX`) has its exact Scryfall code explicitly named in a Wizards publication. For the other **27**, Wizards' source backs the *product family or name* while the code mapping comes from the frozen Scryfall catalog. The [offline product lookup](scripts/product_family_lookup.py) applies the new source overlay without rewriting the older 12-, 23-, or eight-code evidence snapshots. Run `python3 scripts/audit_reprint_curated_sources.py` for a byte-for-byte reproducibility check. These **71** source-backed product families must not be presented as 71 premier sets or 71 original card designs.

## Boxed products versus scheme/planar card component archives

The [15-code Wizards source ledger](data/set_atlas/boxed_precon_sources_2026-10-29.json) and [reproducible boxed-product audit](data/set_atlas/boxed_precon_source_audit_2026-10-29.json) document **ten packaged products/collections** and **five subordinate Scryfall component codes** in the preconstructed/boxed research cohort.

| Packaged game or collection | Scryfall code | Separate internal card archive |
| --- | --- | --- |
| Original Archenemy game packs (2010) | `ARC` | `OARC` — oversized schemes |
| Archenemy: Nicol Bolas (2017) | `E01` | `OE01` — oversized schemes |
| Planechase (2009) | `HOP` | `OHOP` — plane cards |
| Planechase (2012) | `PC2` | `OPC2` — planes and phenomena |
| Planechase Anthology (2016) | `PCA` | `OPCA` — 86 oversized planar cards |

**These paired codes are not two separately sold expansion releases.** Wizards documents how [Archenemy game packs](https://magic.wizards.com/en/news/feature/archenemy-rules-revealed-2010-05-17) bundle 60-card decks with 20-card scheme decks; [Archenemy: Nicol Bolas](https://magic.wizards.com/en/news/feature/archenemy-nicol-bolas-release-notes-2017-06-16) contains four 60-card decks and 20 oversized schemes. [Planechase Anthology](https://magic.wizards.com/en/news/feature/planechase-anthology-celebration-magics-history-2016-11-14) includes four 2012 Planechase decks and 78 plane plus eight phenomenon cards. The component-to-product set-code links come from Scryfall's **explicit `parent_set_code`**, with no guessed links.

Five additional boxed/collection products were reviewed against direct Wizards articles: [Commander Anthology](https://magic.wizards.com/en/news/announcements/commander-anthology-vol-ii-legends-and-decklists-2018-05-08) and Volume II (four previously released decks in each), [Commander Collection: Green](https://magic.wizards.com/en/news/card-preview/commander-collection-green-packaging-and-contents-2020-08-22) and [Black](https://magic.wizards.com/en/news/announcements/commander-collection-black-packaging-and-contents-2021-08-24) (eight fixed reprints each), and [Commander's Arsenal](https://magic.wizards.com/en/news/making-magic/command-2012-10-25) (18 premium cards, ten oversized legendary cards, and accessories). They are **not** additional independently drafted premier expansion booster releases.

The 15-code review increases the cumulative **848** outside-category paper corpus to **86** product-family codes with Wizards evidence and **762** still awaiting individual source review. Within the boxed/preconstructed cohort, **95** remain (down from 110). Run `python3 scripts/audit_boxed_precon_sources.py` to check byte-for-byte reproduction, or `python3 scripts/product_family_lookup.py --cohort preconstructed_and_boxed --only-pending --all` to see that dated review queue. Neither a fixed box nor a distinct record for scheme/planar components independently certifies Standard legality, format legality, or a premier release count.

## Historical Duel Decks and the 2014 Anthology: 25 more code reviews

The [per-code Duel Decks primary-source ledger](data/set_atlas/duel_decks_sources_2026-10-29.json) links **21** individual 2007–2018 Duel Decks matchups to their own product pages in the [Wizards of the Coast official Japanese product archive](https://mtg-jp.com/products/other/). The [2018 final product listing](https://mtg-jp.com/products/0000161/) and [official retirement announcement](https://mtg-jp.com/reading/publicity/0030099/) establish the end of that paired-preconstructed-deck series. The repository's card names and exact set codes still come independently from the frozen Scryfall snapshot; Wizards' product pages are not presented as printing Scryfall codes.

The **four** extra Scryfall codes `DVD`, `EVG`, `GVL`, and `JVC` are **not four more separately sold boxes**. Wizards' [Duel Decks: Anthology](https://mtg-jp.com/products/0000095/) contains the first four matchups (Divine vs. Demonic; Elves vs. Goblins; Garruk vs. Liliana; Jace vs. Chandra) as eight ready-to-play decks **in one 2014 product**, officially marked `DD3`. These four Scryfall subcatalog codes have **no explicit `parent_set_code`** in this frozen snapshot; the product-level relationship is represented separately as Wizards evidence, never fabricated as a Scryfall parent link.

| Cited Scryfall records | Actual sold products represented | Counting rule |
| --- | ---: | --- |
| 21 original paired Duel Decks code records | 21 | One named preconstructed matchup box each |
| 4 Anthology matchup subcatalog records | 1 | All four segments belong to the one eight-deck `DD3` box |
| **25 reviewed code records** | **22 sold boxes** | Neither count represents new premier sets |

The [deterministic report](data/set_atlas/duel_decks_source_audit_2026-10-29.json) preserves all prior 86 source records and classifies **111 of 848** outside-category paper codes with Wizards family evidence; **737 remain pending**, including **70** in the original boxed/preconstructed research cohort (down from 95). Of the frozen **26** Scryfall `duel_deck` codes in the pending queue before this batch, only `GS1` (*Global Series: Jiang Yanggu & Mu Yanling*) remains: it is a separate product family and was not silently classified as part of the historical Duel Decks series.

Offline check: `python3 scripts/audit_duel_decks_sources.py`. Lookup: `python3 scripts/product_family_lookup.py --type duel_deck --all`, or `--cohort preconstructed_and_boxed --only-pending --all`. The official Japanese product pages are first-party Wizards sources, not foreign-language card printing ingestion; no other-language card inventory is added. Product-family evidence does not certify card legality, set debuts or premier-set status.

## Annual Commander preconstructed release families, 2011 and 2013–2020

The [nine-code annual Commander evidence ledger](data/set_atlas/commander_series_sources_2011_2020.json) uses individual first-party Wizards Japanese product pages for *Commander (2011)* and each of *Commander 2013* through *Commander 2020*. The [official product index](https://mtg-jp.com/products/other/) preserves these annual editions; the [2020 product page](https://mtg-jp.com/products/0000193/) explicitly documents ready-made decks alongside its contents and distinguishes those Commander-exclusive cards from the Ikoria main set.

These are **nine annual release-family Scryfall codes**, not necessarily nine individual decks or boxes—an annual Commander product can contain multiple separately packaged preconstructed decks. Their exact Scryfall code mappings and release/first-card dates remain separately attributed to the frozen Set API. No card legality or unique-new-design counts are inferred from the existence of a Commander set code, and the absence of a `C12` code is not treated as a missing year.

The [deterministic cumulative audit](data/set_atlas/commander_series_source_audit_2026-10-29.json) adds **nine individually documented Commander family codes** without changing the earlier 111. The October 29 outside-category corpus now has **120 source-backed / 728 source-pending**, including **61** remaining boxed/preconstructed code records. Later set-tied Commander series (beginning with `C21`, `ZNC`, `KHC` and related products) remain research-pending and are the next priority; the 645 promotional/extras are a separate long-term queue.

Replay: `python3 scripts/audit_commander_series_sources.py`; offline lookup: `python3 scripts/product_family_lookup.py --type commander --all`. No other-language card data was ingested; the Japanese pages serve strictly as primary product-family evidence.

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
