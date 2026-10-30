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

## Set-linked and starter Commander precons, fall 2020–2022

The [twelve-source Wizards evidence ledger](data/set_atlas/commander_set_linked_sources_2020_2022.json) verifies 12 additional Scryfall `commander` records against individual Wizards product announcements or Commander decklist articles: `ZNC` Zendikar Rising; `KHC` Kaldheim; `C21` Commander 2021; `AFC` Forgotten Realms; `MIC` Midnight Hunt; `VOC` Crimson Vow; `NEC` Neon Dynasty; `NCC` New Capenna; `DMC` Dominaria United; `40K` Warhammer 40,000; `BRC` The Brothers' War; and `SCD` Starter Commander Decks. For example, Wizards directly details [two Zendikar Rising preconstructed decks](https://magic.wizards.com/en/news/card-preview/zendikar-rising-commander-decklists-2020-09-09), [the Commander (2021 Edition) decks](https://magic.wizards.com/en/news/announcements/commander-2021-edition-decklists-2021-04-05), [Warhammer 40,000 Commander decklists](https://magic.wizards.com/en/news/announcements/warhammer-40000-commander-decklists), and [five Starter Commander decks](https://magic.wizards.com/en/news/announcements/starter-commander-decks-available-december-2-2022-09-29).

**Source boundary:** A Wizards decklist article supports the existence and type of the preconstructed product, but the page's interactive card images may show more recent Gatherer printings. Wizards itself cautions that interactive decklists are **not** exact card-printing displays. Therefore these sources do not independently certify the number of newly introduced designs, exact collector-number inventories, legality or that every code represents a single separately sold deck.

The [reproducible cumulative report](data/set_atlas/commander_set_linked_source_audit_2026-10-29.json) adds these 12 sources on top of the earlier 120: **132 of 848** other-category paper Scryfall records now have first-party product-family evidence, with **716** source-pending overall and **49** boxed/preconstructed pending. The remaining `commander` type queue contains 19 newer 2023–2026 records, beginning with `ONC` and `MOC`. Use `python3 scripts/audit_commander_set_linked_sources.py` and `python3 scripts/product_family_lookup.py --type commander --only-pending --all` for offline verification.

## Modern Commander release-family sources, 2023–October 2026

The [nineteen-record primary-source ledger](data/set_atlas/commander_modern_sources_2023_2026.json) adds official Wizards decklist/announcement links for every later `commander`-typed Scryfall product code: `ONC`, `MOC`, `WOC`, `WHO`, `LCC`, `MKC`, `OTC`, `M3C`, `BLC`, `DSC`, `FDC`, `DRC`, `TDC`, `FIC`, `EOC`, `ECC`, `SOC`, `MSC`, and `FRC`. These are preconstructed **product families**, not nineteen individual decks or premier expansion sets. For illustrative primary sources, see [Doctor Who](https://magic.wizards.com/en/news/announcements/magic-the-gathering-doctor-who-commander-decklists), [Final Fantasy](https://magic.wizards.com/en/news/announcements/final-fantasy-commander-decklists), [Marvel Super Heroes](https://magic.wizards.com/en/news/announcements/marvel-super-heroes-commander-decklists) and [Reality Fracture](https://magic.wizards.com/en/news/announcements/reality-fracture-multiverse-reforged-commander-decklist).

**Cross-year exception, Foundations Commander (`FDC`):** The frozen Scryfall Set API has an earliest set-level card/printing date of **2024-11-15** and explicit parent `fdn`. However, [Wizards' Foundations Commander decklist article](https://magic.wizards.com/en/news/announcements/foundations-commander-decklists) describes five *physical Commander decks* debuting with *Reality Fracture* on **2026-10-02**. These are different evidence attributes, and the catalog preserves both. Neither official boxed-deck date nor first Scryfall card date should be substituted for the other; this audit does **not** assert there were five Foundations Commander decks released in 2024.

The [deterministic cumulative audit](data/set_atlas/commander_modern_source_audit_2026-10-29.json) advances the 848 outside-category paper Scryfall codes to **151 source-backed / 697 source-pending**. The previously 49 pending boxed/preconstructed research records are down to **30** and **zero** Scryfall `commander`-typed records remain pending primary family citation. Review is bounded to publicly documented product-family existence; card-by-card printing, new-card counts, individual legality, and official confirmation of every Scryfall code still require independent evidence. Reproduce via `python3 scripts/audit_commander_modern_sources.py` and `python3 scripts/product_family_lookup.py --type commander --all`.

## Historical specialty boxes, premium decks, Guild Kits and Game Night

The [14-product first-party evidence ledger](data/set_atlas/boxed_specialty_sources_2006_2022.json) covers `CST` (Coldsnap theme decks), `H09`/`PD2`/`PD3` (three Premium Deck Series foil decks), `MD1` (Modern Event Deck 2014), `E02` (Explorers of Ixalan), `GK1`/`GK2` (Guild Kits), `G18` (2018 Gift Pack), `GNT`/`GN2`/`GN3` (Game Night editions), `Q06` (Pioneer Challenger Decks 2021) and `Q07` (Challenger Decks 2022). Wizards' official Japanese product pages explicitly identify [H09 Slivers](https://mtg-jp.com/products/0000145/), [PD2 Fire & Lightning](https://mtg-jp.com/products/0000146/), [PD3 Graveborn](https://mtg-jp.com/products/0000147/) and [MD1 Modern Event Deck](https://mtg-jp.com/products/0000148/) by three-letter code, release date and packaged format. That is **stronger code-level evidence** than a Wizards product-page name matched to frozen Scryfall metadata.

The other ten official articles identify a named boxed/deck product family but usually do **not** explicitly print the Scryfall code. The 2018 [Game Night and Gift Pack announcement](https://magic.wizards.com/en/news/announcements/introducing-magic-game-night-and-updated-gift-pack-2018-08-27) deliberately supports **two separate family records** (`GNT` and `G18`) from different sections of the same source. The [Wizards correction for a Game Night: Free-for-All decklist insert](https://magic.wizards.com/en/news/announcements/game-night-free-for-all-contents-update) is a further reason to distinguish the product family from exact packaged paper printings. Booster gift collections, Standard/Pioneer challenger decks, and preconstructed multiplayer games are not interchangeable with premiered Magic expansions.

The [conserved 848-code audit](data/set_atlas/boxed_specialty_source_audit_2026-10-29.json) now reports **165 reviewed / 683 source-pending**, with **16** boxed/preconstructed records still in the research queue. The snapshot card and printing counts are unchanged; neither format legality nor a new-card total is inferred. Reproduce with `python3 scripts/audit_boxed_specialty_sources.py` and `python3 scripts/product_family_lookup.py --cohort preconstructed_and_boxed --only-pending --all`.

## Secret Lair collection types and Global Series

The [five-source ledger](data/set_atlas/boxed_special_lair_global_sources_2018_2026.json) validates the distinct marketed product lines `SLD`, `SLU`, `SLC`, `SLZ`, and `GS1`, using first-party Wizards articles. **Only GS1** receives the stronger *Wizards explicitly printed this set code* grade, via the [official Japanese Global Series product entry](https://mtg-jp.com/products/0000172/), which identifies a two-deck introductory Planeswalker product. Its frozen Scryfall `duel_deck` type does not mean that it was marketed as part of the original Duel Decks matchup series, and Wizards' original 2018 regional Standard-legality discussion is historical context, not a current legality claim.

For the Secret Lair entries, Wizards documents [2019's first individual drop campaign](https://magic.wizards.com/en/news/announcements/secret-lair-recap-2019-11-25), [Ultimate Edition's retail display box](https://magic.wizards.com/en/news/announcements/making-fetch-happen-secret-lair-ultimate-edition-2020-03-13), the [30th Anniversary Countdown Kit's 30 themed card packets](https://magic.wizards.com/en/news/announcements/kicking-magics-30th-anniversary-celebration-2022-10-04), and [The Zeta Set's September 2, 2026 Chaos Vault campaign](https://magic.wizards.com/en/news/announcements/chaos-vault-the-zeta-set-puts-the-playtest-in-your-hands). `SLD` indexes an ongoing **series of separate drops**, not one physical box; the source family type is more precise than Scryfall's coarse `box` metadata. The Zeta article notes a correction to its Pauper information, so no card legality is derived from the product citation.

The [reproducible report](data/set_atlas/boxed_special_lair_global_audit_2026-10-29.json) advances the 848 released paper non-expansion/core codes to **170 first-party source-backed / 678 source-pending**, with **11** boxed/preconstructed pending. Those remaining historical/regional codes are `RQS`, `MGB`, `ATH`, `BRB`, `BTD`, `DKM`, `PSAL`, `PHUK`, `DPA`, `PS11` and `G17`. Secondary collector descriptions exist for some, but they are not a substitute for independently reviewed Wizards product evidence. `DPA` is specifically the physical 2010 Duels of the Planeswalkers decks, **not** the similarly named digital game or its later decklists. Reproduce with `python3 scripts/audit_boxed_special_lair_global_sources.py` and `python3 scripts/product_family_lookup.py --cohort preconstructed_and_boxed --only-pending --all`.

## Officially coded booster inserts/Eternal subsets and two Clash Packs

The [nine-source graded Wizards ledger](data/set_atlas/inserts_clash_spellbook_sources_2014_2026.json) adds six explicit official `eternal`-type insert/subset codes: [Transformers `BOT` in Brothers' War boosters](https://magic.wizards.com/en/news/feature/whats-inside-the-brothers-war-boosters), [Jurassic World Collection `REX`](https://magic.wizards.com/en/news/feature/collecting-the-lost-caverns-of-ixalan), [Spider-Man Eternal `SPE`](https://magic.wizards.com/en/news/feature/collecting-marvels-spider-man), [Avatar Eternal `TLE`](https://magic.wizards.com/en/news/feature/collecting-avatar-the-last-airbender), [Teenage Mutant Ninja Turtles Eternal `TMC`](https://magic.wizards.com/en/news/feature/collecting-teenage-mutant-ninja-turtles), and [The Hobbit Eternal `HOC`](https://magic.wizards.com/en/news/feature/collecting-the-hobbit). In each case, Wizards explicitly gives the supplemental subset code; the set's relation to its parent main product does **not** make the subset an additional premier expansion. The complete six-code `special_inserts_and_eternal_subsets` source review queue is now cleared.

Additionally, Wizards' own Japanese articles document [Magic 2015's two-deck Clash Pack](https://mtg-jp.com/reading/publicity/0008624/) (`CP1`) and [Fate Reforged's two-deck Clash Pack](https://mtg-jp.com/reading/products/individual/0011836/) (`CP2`). These are **named product family** matches, not independently printed `CP1`/`CP2` set codes. The latter official product page lists a January **30**, 2015 Japanese sale date; frozen Scryfall `CP2` earliest-card metadata says January **23**, and the audit preserves both. The [Signature Spellbook: Gideon boxed product](https://mtg-jp.com/products/0000183/) (`SS2`) contains eight featured cards plus a foil variant; [Wizards' own card-printing gallery](https://mtg-jp.com/products/card-gallery/0000183/470542/) explicitly displays the **SS2 printing code**. This is stronger than a family name match but different from the official product page printing a three-letter box SKU.

The [reproducible report](data/set_atlas/inserts_clash_spellbook_source_audit_2026-10-29.json) now conserves the full 848-code outside-category paper catalog as **179 primary-source-backed / 669 source-pending**. The **11** pending draft/starter codes exclude the two Clash Packs, and the **2** remaining reprint/curated records are the historical localized `BCHR` and `RIN`. The 11 other boxed cases remain pending. No current card legality, debut count, exact printing inventory or premier-set total is asserted by these product-family citations. Check with `python3 scripts/audit_inserts_clash_spellbook_sources.py` and `python3 scripts/product_family_lookup.py --summary`.

## Masterpiece bonus sheets and historic collectibles: nineteen primary-source reviews

Wizards' release notes or official collecting guides now directly document **all 17** frozen Scryfall `masterpiece`-typed codes: `BRR`, `EOS`, `EXP`, `FCA`, `MAR`, `MED`, `MP2`, `MPS`, `MUL`, `OTP`, `PUMA`, `PZA`, `SOA`, `SPG`, `STA`, `WOT`, and `ZNE`. These include reprinted cards inside boosters, promotional box toppers, artwork treatments, and the ongoing Special Guests series; they are **not 17 additional premier expansions**. Twelve direct Wizards articles actually print the applicable code (including [STA](https://magic.wizards.com/en/news/feature/strixhaven-school-mages-and-commander-2021-edition-release-notes-2021-04-16), [MUL](https://magic.wizards.com/en/news/feature/march-of-the-machine-release-notes), [BRR](https://magic.wizards.com/en/news/feature/the-brothers-war-release-notes), [WOT](https://magic.wizards.com/en/news/feature/wilds-of-eldraine-release-notes), and [SOA](https://magic.wizards.com/en/news/feature/secrets-of-strixhaven-release-notes)); five others are named-family matches to independently recorded Scryfall codes. In particular, **`SPG`, `MAR`, and `MED` encompass multiple products or release contexts**, so their code count cannot be converted into a single-box count.

Two additional historic `memorabilia`-typed records are individually source-reviewed: [30th Anniversary Edition](https://magic.wizards.com/en/news/announcements/celebrate-30-years-magic-gathering-30th-anniversary-edition-2022-10-04) (`30A`), which Wizards expressly calls **non-tournament-legal**, and [Collector's Edition](https://magic.wizards.com/en/news/feature/buyer-beware-2004-04-26) (`CED`). Wizards does **not** print either Scryfall code in those pages; the distinct international `CEI` still lacks equivalent first-party product corroboration.

The [19-record source ledger](data/set_atlas/masterpiece_memorabilia_sources_1993_2026.json), [deterministic cumulative audit](data/set_atlas/masterpiece_memorabilia_source_audit_2026-10-29.json), and `scripts/audit_masterpiece_memorabilia_sources.py` / `tests/test_masterpiece_memorabilia_sources.py` now preserve **198 official product-family source reviews / 650 source-pending records**, with **zero** `masterpiece`-typed codes remaining. The large promotional/extras group is down from **645** to **626** pending. Of those 626, **457 have an explicit Scryfall `parent_set_code`** and **169 have no explicit parent**; absence of a parent is not proof of an independently sold set. Those are metadata relationships, not 457 separate Wizards certifications. The 11 older boxed, 11 draft/starter and two curated/reprint cases remain source-pending. Replay with `python3 scripts/audit_masterpiece_memorabilia_sources.py` and inspect `python3 scripts/product_family_lookup.py --type masterpiece --all`. All exact printings, card debut counts and live legality must still be independently checked.

## Annual event promos, physical Vanguard and historical World Championship Decks

The next [ten-row graded Wizards source ledger](data/set_atlas/historical_promo_series_sources_1997_2024.json) identifies three differently documented families among previously pending promotional/extras records:

- **Physical Vanguard (`PVAN`):** Wizards' [official historical Vanguard reference](https://magic.wizards.com/en/news/feature/vanguard-2008-08-14) describes oversized supplementary player-modifier cards introduced during the 1997 Arena era. A Vanguard card is not an ordinary Magic deck card or another premier booster expansion.
- **Five specific World Championship Deck product years (`WC97`, `WC98`, `WC99`, `WC00`, `WC04`):** Wizards' Japanese website independently names [1997](https://mtg-jp.com/reading/iwashowdeck/0016981/), [1998](https://mtg-jp.com/reading/iwashowdeck/0019047/), [1999](https://mtg-jp.com/reading/translated/rc/0004310/), [2000](https://mtg-jp.com/reading/iwashowdeck/0035903/), and [2004](https://mtg-jp.com/reading/iwashowdeck/0019017/) card-product years in later historical essays. These are **graded retrospective product mentions**, not recovered original box pages or first-party exact Scryfall code declarations. Unverified `WC01`, `WC02`, and `WC03` remain pending; a retrospective Worlds *tournament* decklist by itself would not be enough.
- **Four Love Your Local Game Store promo years (`PLG20`, `PLG21`, `PLG22`, `PLG24`):** Contemporary Wizards [2020 WPN launch](https://wpn.wizards.com/en/news/announcing-love-your-local-game-store-promotion), [2021 Summer of Legend promos](https://magic.wizards.com/en/news/announcements/love-your-local-game-store-more-summer-legend-promos-2021-06-23), [2022 Sol Ring reward](https://magic.wizards.com/en/news/announcements/love-your-local-game-store-returns-with-double-masters-2022), and [2024 draft-event promo](https://wpn.wizards.com/en/news/love-your-local-game-store-2024-begins-july-5-with-all-new-lylgs-draft-event) document separate dated promo programs. The cited pages do **not** explicitly print `PLG20` and similar Scryfall codes, and do not certify complete year-by-year card inventories; `PLG25` remains pending.

All **ten** rows are **official named-family crosswalks**, **zero** are explicit Wizards set-code certifications. Their [deterministic audit](data/set_atlas/historical_promo_series_source_audit_2026-10-29.json), guarded lookup, and focused tests now report **208 of 848** non-mainline paper category codes with direct Wizards family evidence and **640 remaining pending**. The promotional/extras cohort is down to **616 pending**, including **457** still explicitly parent-linked by frozen Scryfall metadata and **159** without an explicit parent. The 11 boxed, 11 draft/starter, and two curated/reprint records remain unresolved. Source family evidence still does not certify physical product printing inventories, card debuts, release legality or an all-time premier set count. Reproduce with `python3 scripts/audit_historical_promo_series_sources.py` and `python3 scripts/product_family_lookup.py --code wc97`.

## APAC Lunar New Year annual promotion families, 2021–2026

Six additional released English-paper promo catalog codes now have an independently reviewed Wizards *named annual program* source each: [2021 Year of the Ox](https://magic.wizards.com/en/news/announcements/year-ox-store-challenger-series-2021-promos-2021-05-17) (`PL21`), [2022 Year of the Tiger](https://magic.wizards.com/en/news/announcements/celebrate-year-tiger-apac-league-events-and-promos-2022-02-09) (`PL22`), [2023 Year of the Rabbit](https://magic.wizards.com/en/news/announcements/2023-apac-league-and-the-year-of-the-rabbit) (`PL23`), [2024 Year of the Dragon](https://www.magic.gg/news/play-standard-get-promos-jump-into-the-action-with-these-year-of-the-dragon) (`PL24`), [2025 Year of the Snake](https://magic.wizards.com/en/news/announcements/earn-sweet-year-of-the-snake-promos-at-your-local-game-store) (`PL25`), and [2026 Year of the Horse](https://magic.wizards.com/zh-Hant/news/announcements/celebrate-the-year-of-the-horse-at-your-local-game-store-and-more) (`PL26`). The 2026 source is first-party Wizards in **Traditional Chinese**; its analogous English path redirects, and the event evidence is not an import of non-English card-printing data. The 2024 program was previewed in December **2023**, whereas Scryfall's first-card record remains dated February **2024**; both dates remain separate.

Each annual program is a **family-only Scryfall crosswalk**: none of these official sources prints the exact `PL21`–`PL26` Scryfall code or certifies complete printing variants, debut counts or legality. These six series codes have no explicit Scryfall parent link; that absence does **not** make them additional expansion sets. The [six-source provenance ledger](data/set_atlas/apac_lunar_year_promos_sources_2021_2026.json), [deterministic cumulative audit](data/set_atlas/apac_lunar_year_promos_source_audit_2026-10-29.json), guarded offline lookup, regression tests and focused CI advance the frozen 848-code research review to **214 Wizards family-backed / 634 source-pending**. Within the promo/extras cohort **610** are pending (**457** explicitly parent-linked, **153** without an explicit parent). The older 2018 `PLNY` remains *pending*: secondary descriptions of a Treasure token are not sufficient for first-party source certification. Reproduce with `python3 scripts/audit_apac_lunar_year_promos_sources.py` and inspect `python3 scripts/product_family_lookup.py --code pl26`.

## Event and collaboration promo families: seven targeted program records

Seven further independent catalog records have first-party Wizards evidence for their **named event or collaboration**, not any hypothetical new booster expansion:

- **`GDY` Game Day and `SCH` Store Championships:** Different explicitly named participation/placement promo programs, described in separate sections of one [Wizards WPN *Dominaria United* marketing kit article](https://wpn.wizards.com/en/news/whats-coming-dmu-marketing-kit) in August 2022; the article is *not* a complete inventory of all seasons in either ongoing grouping.
- **`PRCQ` 2022 and `PR23` 2023 Regional Championship Qualifiers:** The [March 2022 organized-play restart](https://wpn.wizards.com/en/news/pro-tour-returns-re-ignite-your-stores-competitive-play) names Lava Spike/Nykthos local-qualifier prizes; the [October 2022 30th Anniversary WPN announcement](https://wpn.wizards.com/en/news/magic-30th-anniversary-kicks-off-with-promos-products-more) previews **January 2023** qualifier promos. An advance announcement's publication year is not its promotional card-release year.
- **`PMDA` Magic × Duel Masters:** A [2023 Wizards Japan FNM Standard event article](https://mtg-jp.com/reading/kochima/0037149/) identifies September–December distribution of an original regional promo collaboration; Japanese-language program evidence does **not** enlarge our English-paper printing scope.
- **`PCBB` Cowboy Bebop:** [Wizards' English announcement](https://magic.wizards.com/en/news/announcements/announcing-cowboy-bebop-collaboration-promo-cards) confirms five Traditional Foil Standard Showdown promo cards issued **August 2024–May 2025** in a named crossover campaign.
- **`PSPL` Spotlight Series:** [Wizards' August 2024 competitive-play launch article](https://magic.gg/news/announcing-the-magic-spotlight-series) identifies the **January 2025** inaugural Foundations tournament and a Terror of the Peaks participation promo, part of an ongoing event series.

All **seven** are *family-only* Wizards-to-Scryfall crosswalks; none of these sources literally prints the Scryfall code or confirms complete card printing inventory, new card debuts, current legality or premier-set status. Their seven code records all lack an explicit Scryfall parent link, but remain **promo catalog records**. [Source ledger](data/set_atlas/event_collab_promos_sources_2022_2025.json), [reproducible audit](data/set_atlas/event_collab_promos_source_audit_2026-10-29.json), offline lookup, tests and CI now report **221 source-backed / 627 pending** among the frozen **848** paper other-category records. **603** promo/extras codes remain source-pending (**457** explicitly parent-linked, **146** without links). The **11 boxed**, **11 draft/starter** and **2 curated/reprint** remaining cohorts did not change. Run `python3 scripts/audit_event_collab_promos_sources.py` or look up `pcbb` and `pmda` using `scripts/product_family_lookup.py`.

### Art Series: illustration-only collectible product components (v2.17)

An additional **38 individually identified Art Series catalog records** now have named-release primary-source citations, from [*Modern Horizons* release notes](https://magic.wizards.com/en/news/feature/modern-horizons-release-notes-2019-05-31) (which explicitly describe the art cards as **not playable**), set-specific Wizards [art-card image galleries](https://magic.wizards.com/en/news/card-image-gallery/modern-horizons-3-art-cards) and the [*Innistrad: Midnight Hunt* product page](https://magic.wizards.com/en/products/midnight-hunt). Each record remains a Scryfall `memorabilia` subgroup with its **existing explicit `parent_set_code` unchanged**. The links describe collectible art inserts or art-card families; they **do not declare Scryfall's exact `a...` codes**, certify the complete artwork printing inventory, establish new playable card debuts, or prove format legality. Art Series inserts are not separate regular expansions.

We deliberately leave **`atla`, `atle` and `ahoc` pending** because the source review did not establish official first-party references for those precise subgroups. The [38-row source ledger](data/set_atlas/art_series_primary_sources_2019_2026.json), [reproducible cumulative audit](data/set_atlas/art_series_primary_source_audit_2026-10-29.json), lookup overlay, five tests and focused CI bring the frozen 848-code other-category review to **259 first-party family-backed / 589 pending**. The promotional/extras cohort now has **565 pending**, comprising **419** explicit Scryfall parent-linked and **146** without an explicit parent. The other pending cohorts stay at **11 boxed**, **11 draft/starter** and **2 curated/reprint**. Reproduce with `python3 scripts/audit_art_series_primary_sources.py`; inspect `python3 scripts/product_family_lookup.py --code amh1` or `--code atla` to compare sourced versus pending records.

### First-party booster, Commander and supplemental token families (v2.18)

Source-review **34 Scryfall `token`-typed records**, using **18 directly relevant Wizards token-focused articles** covering 2023–2026 releases. Each cited article describes a specifically named set's booster tokens, Commander deck tokens, or named supplemental token group. Notable distinct groups include [*Outlaws of Thunder Junction*](https://magic.wizards.com/en/news/card-preview/the-tokens-of-outlaws-of-thunder-junction), which explicitly distinguishes OTJ booster tokens, OTC Commander tokens, seven BIG tokens and five OTP tokens; [*Modern Horizons 3*](https://magic.wizards.com/en/news/card-preview/the-tokens-of-modern-horizons-3), which separates booster, Commander and premium Commander editions; and [*Reality Fracture*](https://magic.wizards.com/en/news/card-preview/reality-fracture-tokens-and-art-cards), which separately identifies Multiverse Reforged Commander tokens and a later-printing variation. The complete 34-row evidence ledger records individual codes, product contexts and specific official URL citations.

**Evidence boundary:** These are **34 verified *named token family crosswalks***, not 34 separate booster expansion sets, and **zero Wizards pages declare the exact Scryfall `t...` token catalog code**. The 34 explicit `parent_set_code` relationships and first-card dates remain unmodified from the frozen Scryfall catalog; neither exact individual collector-number printing completeness nor legality/debut counts are certified. Regional Japanese promo-token groupings, substitute cards, and the ambiguous `ttmc` (*Teenage Mutant Ninja Turtles Eternal Tokens*) family stay pending. The [first-party token source ledger](data/set_atlas/token_families_primary_sources_2023_2026.json), [deterministic cumulative audit](data/set_atlas/token_families_primary_source_audit_2026-10-29.json), guarded offline lookup, five regression tests and focused CI bring this 848-code research cohort to **293 family source-backed / 555 pending**. Of the **531 remaining promotional/extras**, **385** have explicit Scryfall parent links and **146** lack one. Other categories remain at **11 boxed, 11 draft/starter and 2 curated/reprint** pending. Reproduce with `python3 scripts/audit_token_families_primary_sources.py` and examine `python3 scripts/product_family_lookup.py --code totc`.

### Fast-track functional release audit (Master Workflow v2.19)

The old metric **293 of 848 first-party source-reviewed other-category product families** is an *optional provenance-depth research measure*, **not the percentage of Phase 1B completed**. All 555 outstanding other-category source-review records remain in their existing named queue with the same uncertainties; none are magically upgraded to Wizards-certified, and none need block a functional, accurately qualified Set Atlas release.

An [independent deterministic read-only readiness report](data/set_atlas/phase1b_fasttrack_readiness_2026-10-29.json), from `python3 scripts/audit_phase1b_fasttrack.py`, now checks the **32 published historical lookup shard SHA-256 hashes**, 1,062 linked Scryfall metadata codes and 560 explicit `parent_set_code` references, partition counts and representative set/card lookups. Most importantly, **all 1,062 released English-paper per-set printing counts match exactly** between the historical October 28 published index and October 29 audit: **106,855 released English-paper printings at the October 29 cutoff**. Although the newer snapshot has **192 more default printing records** and **198 more English-paper records**, those 198 net English-paper entries fall entirely into future-dated *counts*. Only `pf26`, `pw26`, `sds`, `trc`, `trk` change their all-printing totals. No dated currently released inventory-count gap appears.

**Unverified boundary:** This is an aggregate/per-set count comparison, **not proof of exact printing-ID equality** or a new cryptographic verification of both original bulk files. The source artifacts' previous verification remains documented; current exact-ID parity needs a separate test if required for stronger certification. This v2.19 checkpoint preceded the v2.20 full-export and v2.21 category/story-series evidence below. Final release CI, a dated release report and transparent cross-snapshot ID limits remain separate gates. Do not mark Phase 1B complete merely because this preliminary audit passed.

### All-1,062-set card-list export acceptance (Master Workflow v2.20)

All **1,062 set codes** in the committed October 28 historical indexes have now passed offline, full set-to-printings and set-to-unique-card export checks. A separate reverse join verifies all **119,509 printing IDs** across the set and card-history indexes, encompassing **39,099 stable Oracle identities**. By the October 29, 2026 cutoff, the default filter exports **106,855 released English-paper printing rows**. Exactly **105** historical set codes correctly produce an empty default printing list, because some records are future-dated, digital-only, localized, or otherwise excluded by the default eligibility filter. An empty default list **does not** mean that the set code is missing.

From the repository checkout, with no internet request or fresh Scryfall download:

```bash
# Every printing of an Alpha card within LEA, in CSV form
python3 scripts/export_phase1b_set_cards.py lea --mode printings --format csv
# Each distinct Oracle card identity in Alpha, with debut/reprint classification
python3 scripts/export_phase1b_set_cards.py lea --mode unique --format json
# A Commander release, written to a caller-chosen output file
python3 scripts/export_phase1b_set_cards.py c21 --mode unique --output c21-cards.csv
# Include products normally excluded by the release/language/medium cutoff
python3 scripts/export_phase1b_set_cards.py trk --include-future
python3 scripts/export_phase1b_set_cards.py ydmu --include-digital
python3 scripts/export_phase1b_set_cards.py fbb --include-foreign
```

Defaults: English-language paper printings released **on or before 2026-10-29**; `--as-of YYYY-MM-DD` changes the cutoff, and `--include-future`, `--include-digital`, `--include-foreign` explicitly expand scope. `--mode printings` exports all selected printing IDs, while `--mode unique` deduplicates selected printings by their stable Oracle identity (or an explicitly unresolved identity where applicable). Both formats retain the set code; debut versus reprint classifications use the historical index's chronology, not story chronology. The exporter does **not** claim an exact-ID match against October 29's separately archived, later bulk snapshot: that cross-snapshot boundary remains open even though released per-set printing counts agree.

Reproduce the [1,062-code export acceptance report](data/set_atlas/phase1b_export_acceptance_2026-10-29.json) with `python3 scripts/audit_phase1b_export_acceptance.py`; focused CI and unit tests verify edge cases as well as full enumeration. The **555 outstanding source-pending promo/other-family research entries** remain a separate optional source-depth queue, not a release blocker or verified primary-source product inventory. Category labels and bounded first-party story-series links follow in v2.21 below; final release and cross-snapshot proof boundaries remain separate gates.

### Every set code has an evidence-qualified release scope (Master Workflow v2.21)

The [dated classification and official story-series crosswalk](data/set_atlas/phase1b_release_scope_story_bridge_2026-10-29.json) labels **every one of the 1,062 recorded set codes** with exactly one of the following scopes, reconstructing and cross-checking the existing Wizards-primary release ledgers and Scryfall Set API category partition.

| Scope among all 1,062 Scryfall codes | Codes | What the label means |
| --- | ---: | --- |
| Historical regular/mainline expansion or core release | **136** | Primary-source-supported members of the **142-code, released, nondigital Scryfall expansion/core subset**; not a retroactive official count of every Wizards *premier* set. |
| Directly documented auxiliary, discarded, or integrated code | **4** | `mat` epilogue, `big` integrated subset, `sum` discarded Summer Magic printing, `tsb` integrated timeshifted sheet; none silently promoted to an additional regular main release. |
| Provisional localized printing variant | **2** | `fbb` and `4bb` have specialist corroboration but are not independently certified by a Wizards primary source as distinct regular core editions. |
| Other released paper-category catalog code | **848** | Commander, Masters, supplementary, promotions, bonus sheets, tokens, memorabilia, and other source-specific Scryfall types. **Not 848 independent booster set releases.** |
| Released digital-only code | **62** | Distinct catalog records without the default English-paper scope. |
| Announced future code | **10** | Not counted as released on the October 29, 2026 snapshot cutoff. |
| **All code records** | **1,062** | Six mutually exclusive classifications; no gaps or overlaps. |

This scope audit is **a clearly labeled Scryfall-code census**, not a promise that 1,062 separately boxed products, 1,062 physical expansion sets or an all-time official Wizards "premier" count exist. Individual printing inventories, actual product quantities and story-world chronologies are separate dimensions. The **555 optional first-party source-pending other-category records** retain their historical research statuses. The full per-code JSON identifies name, category, date, Scryfall parent when explicit, graded scope and any applicable Wizards release-evidence URL.

**Official story bridge:** Twelve manually scoped release codes (`bro`, `one`, `mom`, `mat`, `woe`, `lci`, `mkm`, `otj`, `blb`, `dft`, `tdm`, `eoe`) link only to **directly title-matched official Wizards Magic Story series** already present in `data/story_index.csv`. Examples: [*The Brothers' War*, Episode 1](https://magic.wizards.com/en/news/magic-story/the-brothers-war-episode-1-the-end), [*March of the Machine*, Episode 1](https://magic.wizards.com/en/news/magic-story/episode-1-triumph-of-the-fleshless), and [*Tarkir: Dragonstorm*, Episode 1](https://magic.wizards.com/en/news/magic-story/tarkir-dragonstorm-episode-1-stories-and-their-bones). The report includes published story titles, dates, official links and the number of exact-prefix stories in the recovered index. A *publication-series* association is **not** proof that an arbitrary card appears in that story, or proof that its narrative events happened in release-date order. No other set is auto-matched by a loose name similarity.

To reproduce all 1,062 labels and inspect a sample story link offline:

```bash
python3 scripts/audit_phase1b_release_scope.py
python3 scripts/audit_phase1b_release_scope.py --code bro
python3 scripts/audit_phase1b_release_scope.py --code fbb
python3 scripts/audit_phase1b_release_scope.py --code c21
```

The new focused CI verifies exact reproducibility, all six denominators, all 142 reviewed candidate classifications, provisional border variants, no silent promotion of supplemental products and official-story title/URL integrity. The final release/coverage gate and cross-snapshot printing-ID claim remain separately pending.

### Qualified offline functional release checkpoint (Master Workflow v2.22)

The final [dated Phase 1B functional coverage report](data/set_atlas/phase1b_qualified_functional_release_2026-10-29.json) cross-checks the independent historical-index, fast-track, all-export and release-scope reports. Its deliberately narrow verdict is **`QUALIFIED_OFFLINE_FUNCTIONAL_RELEASE_READY`**, covering usable English-paper **set-to-card and card-to-set lookups, complete 1,062-code card lists, CSV/JSON exports, release-date/digital/language opt-ins, debut/reprint distinctions and evidence-graded category labels**. Twelve directly named first-party Magic Story publication-series links are included as a small curated seed, not a universal lore atlas.

Reproduce that release report and its applicable acceptance tests:

```bash
python3 scripts/audit_phase1b_functional_release.py
python3 -m unittest discover -s tests -p 'test_*set*.py' -q
python3 -m unittest discover -s tests -p 'test_*sources.py' -q
python3 -m unittest discover -s tests -p 'test_phase1b*.py' -q
```

All three local Phase 1B test group invocations passed at the v2.22 checkpoint (**35**, **80**, **13** test executions respectively; patterns can overlap). The targeted GitHub release acceptance workflow and separate Grixis CI must also pass at the exact published head before this checkpoint is considered merged.

**What this is not:** It is *not* a reverified original October 28 bulk (the original bulk bytes remain unavailable), proof that individual October 28 and October 29 printing IDs are identical, an authoritative count of every Wizards-designated premier set in all history, proof every promo/boxed component has an individual Wizards citation, or evidence that every printed card is directly associated with a canon story. Those are clearly recorded future evidence upgrades, not claims hidden in a summary percentage. The **555 optional product-family source gaps** remain open without preventing the functional Set Atlas from being used.

## Read-only lookups

On a checkout of this repository, no Scryfall download is needed for the following commands:

```bash
python3 scripts/set_product_lookup.py --code lea
python3 scripts/set_product_lookup.py --year 1994 --type expansion --all
python3 scripts/set_product_lookup.py --parent dmu --all
python3 scripts/set_product_lookup.py --name Commander --all
python3 scripts/historical_set_lookup.py set lea --all
python3 scripts/historical_set_lookup.py card "Black Lotus" --all
python3 scripts/export_phase1b_set_cards.py lea --mode unique --format csv
```

The last two commands read the [32 historical GitHub-readable index shards](data/set_atlas) from the **October 28 committed shard collection**, not the October 29 bulk. See the [historical 105-shard audit](data/set_atlas/historical_shard_audit_2026-10-29.json) for exact hashes and counts. Keep dates and denominators separate.

**Integrity checks:** `python3 scripts/audit_set_product_links.py --check`, `python3 scripts/publish_historical_set_index.py`, and focused Phase 1B GitHub Actions. The first command deliberately replays the frozen October 29 metadata and **never silently refreshes** Scryfall data.
