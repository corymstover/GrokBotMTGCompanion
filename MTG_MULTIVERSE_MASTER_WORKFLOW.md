# MTG Multiverse Companion — Master Workflow & Progress Checklist

**Version:** 2.1
**Checkpoint date:** 2026-10-29  
**Repository:** [corymstover/GrokBotMTGCompanion](https://github.com/corymstover/GrokBotMTGCompanion)  
**Purpose:** Durable project roadmap and handoff document. Update this file after verified milestone work; do not treat historical figures as live counters.

## Mission

Develop a comprehensive, evidence-backed Magic: The Gathering companion spanning cards, rules, mechanics, lore, the timeline, characters, planes, factions, relationships and lore-first Commander deckbuilding. Reuse and improve existing repository records and tools. Preserve the finished Grixis Commander Encyclopedia as a separate, approved collection.

**Owner preferences:** Prioritize English/default-language card and printing data. There is **no need to ingest every foreign-language printing**. Keep lore fidelity and maximum realistic strategic optimization together in future decks. Explain uncertainties; never elevate a name match or thematic proxy into canonical fact without evidence.

## Verified status at this checkpoint

| Area | Verified checkpoint | Meaning / caveat |
| --- | --- | --- |
| Grixis Encyclopedia | **62/62 finalized** | Historical approvals and exact lists remain protected. |
| Oracle Cards snapshot | **39,164 Oracle IDs** | October 29 Scryfall source includes digital/special objects; not all are tabletop-playable cards. |
| Individual card index | **33,894 records** | The 5,270 Oracle IDs outside the index are now classified from the verified October 29 Oracle snapshot: 4,154 excluded layouts, 811 outside paper/eternal scope, 305 future-dated eligible objects, **0 already-released eligible omissions**. |
| Set/printing inventory | **1,062 set codes; 119,701 default-language printings; 107,898 English paper printings** | Verified October 29 Scryfall Default Cards snapshot and new `data/set_atlas/` Phase 1B pilot. The October 28 shard manifest held 119,509 / 107,700; five set codes changed. Includes **1,051 future-dated printings**, not 1,051 newly released cards. Set/product and shard certification remains incomplete. |
| Priority card enrichment | **3,409 / 5,362 (63.6%)** | **1,953 remaining** on the verified October 29 priority-pool definition; twelve reviewed *Reality Fracture* records added without changing any of the earlier 3,397. |
| Official Wizards story inventory | **660/660 recovered and strictly audited** | Hash/URL provenance committed; full article text was cached outside Git and must be refetched/audited in a new environment. |
| Uncertain character links | **341 name-only links triaged** | Two official-page leads warrant review; triage is not canon approval. |
| Cards without a linked lore entry | **~1,220** | Investigate or preserve as documented unknowns; never fabricate lore. |
| Historical Scryfall lock | **Preserved** | `data/grixis/dev_snapshot_lock.json` records `snap-20261016`; exact old bulk bytes remain unconfirmed. |
| Active Scryfall release | **Archived, re-downloaded, verified** | [snap-20261029-40848334824-1](https://github.com/corymstover/GrokBotMTGCompanion/releases/tag/snap-20261029-40848334824-1): Oracle Cards, Default Cards, Rulings and SHA-256 manifest. |
| Snapshot reconciliation | **Passed read-only** | [PR #784](https://github.com/corymstover/GrokBotMTGCompanion/pull/784) and [report workflow](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40848889092): 0 previously indexed/enriched IDs disappeared; 0 differences in indexed type, color identity, Commander legality, Game Changer status or ruling counts. It is **not** a complete historical Oracle-text diff. |

Infrastructure checkpoint: [PR #783](https://github.com/corymstover/GrokBotMTGCompanion/pull/783) separated current Multiverse ingestion from the historical Grixis lock, added the durable snapshot capture/verification workflow, and passed CI. [PR #784](https://github.com/corymstover/GrokBotMTGCompanion/pull/784) added the read-only research reconciliation and passed CI. [PR #789](https://github.com/corymstover/GrokBotMTGCompanion/pull/789) merged the verified first Phase 8 generated batch; [lore/Phase 8 CI](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40858943537), [Multiverse snapshot CI](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40858943744) and [focused Grixis CI](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40858943638) all passed.

## Phase 1 — Card database and research inputs

- [x] Preserve the original 62 Grixis approved decks separately.
- [x] Archive a current Scryfall Oracle Cards, Default Cards and Rulings snapshot with hashes.
- [x] Independently download the release assets again and verify them.
- [x] Separate historical and modern Scryfall caches and validation modes.
- [x] Compare the new snapshot against the committed card index and enrichment inventory without mutating either.
- [x] Classify the **5,270 currently unindexed Oracle records** against the independently verified October 29 snapshot and existing ingest policy; see `data/multiverse_audits/oracle_index_2026-10-29.json` and `scripts/audit_oracle_index.py`.
- [x] Audit eligible released missing records: **0** under the documented October 29 index predicate. Re-audit future-dated cards after release; do not force-add intentionally excluded objects.
- [ ] Finish the **1,953 remaining priority-card lore/synergy enrichments** without flattening existing curated data.
- [ ] Document a repeatable update process for future Scryfall changes, current legality, and official rules.
- [ ] Recount coverage and verify representative lookup queries after each published batch.

**2026-10-29 first generated batch (cycle 37):** The twelve exact-name notes from the already registered official *Legends of Reality Fracture* source are now present in `data/card_enrichment.json`, `Card Enrichment.md`, and the nine affected card shards. Eight are explicitly labeled Echoverse alternate-continuity portrayals. The current Oracle, Default Cards, and Rulings archives passed SHA-256 manifest verification; all **660/660** official story sources passed strict cache auditing; EDHREC and Commander Spellbook source caches were recovered for the batch. The generator's replay from those offline caches passed with **0** consistency problems. A full JSON record-by-record comparison against the previous 3,397-card baseline found **0 changed, 0 removed, 12 added**; priority coverage is now **3,409/5,362 (63.6%)**. Three new package backlinks were updated without refreshing unrelated prices or EDHREC rankings. Source article text and third-party caches remain uncommitted and must be recovered and verified again in another environment. This is a batch-level verification, not completion of the entire Phase 8 backlog.

**2026-10-29 index-exclusion audit:** The archived Oracle Cards file matches SHA-256 `0358af62f92ac10f685d5ee6ad9ab23dfbff6f41bc32dfe81b5ab18cf3088adb` in the release manifest. The read-only classifier partitions all **5,270** non-indexed IDs into **4,154** intentionally excluded layouts (tokens, art cards, etc.), **811** nonpaper/non-eternal objects, and **305** eligible but future-dated objects; **0** eligible released objects are missing and **0** already indexed IDs disappear or violate the documented predicate. The future-dated set-code distribution is `trk=190`, `trc=112`, `slc=2`, `pf26=1`, based on Scryfall's October 29 release dates. **Do not ingest these future records now**; re-audit after their release using a newly verified snapshot and explicit cutoff. This is an index-policy audit, not a universal card/playability or set census.

## Phase 1B — MTG Set & Printing Atlas (official milestone)

**Goal:** Make every recorded MTG release independently discoverable, countable, and searchable by set, while retaining accurate card-by-card printing histories. This is a distinct catalog/data-quality milestone within Phase 1, not a replacement for the existing card and lore work.

**Existing foundation:** Reuse `Printing History.md`, `data/printings_summary.csv`, `data/printing_lore/manifest.json`, its per-set printing shards, and the independently archived Scryfall Default Cards snapshot. The October 28 manifest reports **1,062 Scryfall set codes**, **119,509 default-language printing records**, and **107,700 English paper printing records**. These are historical input counts, **not** a verified number of main expansions, unique cards, or newly introduced designs.

**2026-10-29 first Phase 1B catalog/audit checkpoint:** `scripts/audit_set_printing_atlas.py` verifies the independently archived October 29 Default Cards file's SHA-256 and count against its release manifest, then compares its full **119,701** printings to the older manifest's **119,509**. Both snapshots cover **1,062 Scryfall set codes**. The older manifest's set and shard row arithmetic is internally consistent; **105 historic shard file bytes were not available to hash here**. Only **five** set-code totals changed (`trk`, `trc`, `sds`, `pf26`, `pw26`); the net differences are **+192** printing records and **+198** English paper records. The source has **107,898** English paper printings, of which future previews must be excluded when asking what was released as of October 29; **1,051 total printing records** have future `released_at` dates. See `data/set_atlas/audit_2026-10-29.json` for Scryfall `set_type` category counts and `data/set_atlas/catalog_2026-10-29.json` for a dated all-1,062-code set catalog with English-paper distinct Oracle IDs, single-set debuts, same-day tied debuts, and reprints. A verified read-only `scripts/set_atlas_lookup.py` supports **set → cards** and **card → chronological printings/sets**, including exact card-name/Oracle-ID queries. These are first-pass, explicitly snapshot-dated measures; not yet a certified classification of premier releases or canonical set/product associations.

**2026-10-29 historical-shard publication checkpoint:** The 105 committed October 28 shard files are now **all verified against their saved SHA-256 hashes, byte counts, row counts and manifest set links**. A deterministic read-only validator, `scripts/publish_historical_set_index.py`, reconstructs **119,509 distinct printing IDs**, **1,062 set codes**, **107,700 English paper printing records**, and **39,099 stable Oracle identities**; it finds **0 missing Oracle IDs in the normalized historical shards**. As of October 29, the historical snapshot has **106,855 released English paper printings** and **859 future-dated printings across all media**. The generated 32 compact `data/set_atlas/historical_sets_*.json` and `historical_cards_*.json` buckets are now committed and the independent read-only `scripts/historical_set_lookup.py` works without an uncommitted Scryfall bulk download. See `data/set_atlas/historical_shard_audit_2026-10-29.json` for exact per-file hashes and per-set totals. This certifies **the committed historical shards**, not the missing October 28 original bulk file; cross-source byte/ID reconciliation remains unverified. The separate October 29 Scryfall atlas remains authoritative for its later snapshot date.

**2026-10-29 sourced set/product metadata checkpoint:** Scryfall's official `/sets` API supplied a dated Set-object metadata snapshot (UTC 2026-10-29 23:38:34); all **1,062** codes from the October 29 card-printing atlas matched set metadata with **0 conflicts/missing codes**. The API listed **1,063** codes at fetch time; the one extra, `nau` (2027-02-05), was not in the earlier bulk and is kept out of that snapshot's printing totals. Scryfall explicitly supplies **560 `parent_set_code` relations** and **10 future-dated set codes**. Under the strict cutoff of October 29, **142** non-digital entries were typed `expansion` or `core`; that is a *source category candidate count*, **not** a Wizards-certified number of premier sets. No unnamed or inferred product links were created. Immutable source metadata: `data/set_atlas/scryfall_set_metadata_2026-10-29.json`; normalized joins and audit: `data/set_atlas/product_catalog_2026-10-29.json`, `data/set_atlas/product_audit_2026-10-29.json`. Read-only `scripts/set_product_lookup.py` filters by code/name/year/type/date/parent without network access. `scripts/audit_set_product_links.py --check` and `tests/test_set_product_links.py` validate reproducibility. Human index: `SET_ATLAS.md`. Scryfall Set API metadata was fetched later than the archived same-day Default Cards bulk; source times and counters are not interchangeable.

**2026-10-29 Wizards release-family classification checkpoint:** A bounded **30-code** exact-match review now cross-references Wizards' primary product archive, release notes and official product-family explanations against the October 29 1,062-code Scryfall product catalog. It verifies **21 officially documented main releases from 2023 through October 29, 2026** (13 first-party main set releases, six Universes Beyond main releases, and two earlier 2023 main-set release notes). It explicitly separates `mat` (Standard-legal epilogue micro set), `big` (OTJ's subset), `om1` (digital Universes Within counterpart), four special products (`mh3`, `acr`, `pip`, `inr`) and two future main releases (`trk`, `mdd`). A **142**-entry full-history, released, non-digital Scryfall expansion/core category contains **21 reviewed regular main releases**, **two documented auxiliary exceptions** and **119 not-yet-reviewed category candidates**. This is **not** an all-time premier release count. Sources and per-code evidence: `data/set_atlas/wotc_reviewed_release_evidence_2026-10-29.json`; deterministic result: `data/set_atlas/wotc_release_classification_2026-10-29.json`. Rebuild/check with `scripts/audit_wotc_premier_sets.py`; user guide `SET_ATLAS.md`. Future history must be explicitly reviewed against Wizards evidence instead of automatically accepting Scryfall's `set_type`.

**2026-10-29 historical release-census checkpoint (1993–2002):** Wizards' [Looking Back, Part 1](https://magic.wizards.com/en/news/making-magic/looking-back-part-1) lists year-by-year historical randomized booster products; its [official core set enumeration](https://magic.wizards.com/en/news/making-magic/trivial-pursuit-more-or-less) explicitly recognizes 21 regular core editions over the historical span. Against the Oct. 29 Scryfall metadata, all **38** eligible 1993–2002 `expansion`/`core` codes received a bounded review: **35 historically regular expansion/core releases**, **1 direct-source excluded discarded printing** (`sum`, Summer Magic/Edgar; [Wizards](https://magic.wizards.com/en/news/making-magic/25-more-random-things-about-magic-2016-06-20)), and **2 provisional foreign-border variants** (`fbb`, `4bb`; *not yet directly source-certified*). The 1993–2002 classification uses historical **regular expansion/core release**, not the modern term *premier set*, and preserves the region-dependent Arabian Nights 1993/1994 release caveat. Combined across the two primary-source batches, **56** qualifying released mainline editions/sets are source-reviewed, **3** products are directly documented auxiliary/discarded, **2** foreign-border variants remain provisional and **81** candidates dated 2003–2022 remain unreviewed. These are qualified evidence partitions of **142** Scryfall non-digital released `expansion`/`core` codes; the **all-time premier count is NOT yet certified**. Evidence and reproducible report: `data/set_atlas/wotc_early_release_evidence_1993_2002.json`, `data/set_atlas/wotc_early_release_audit_1993_2002.json`, `scripts/audit_wotc_early_sets.py`, `tests/test_wotc_early_sets.py`; `SET_ATLAS.md` records the interpretation.

**2026-10-29 historical release-census checkpoint (2003–2022):** [Wizards' Looking Back, Part 1](https://magic.wizards.com/en/news/making-magic/looking-back-part-1), [Part 2](https://magic.wizards.com/en/news/making-magic/looking-back-part-2), and the [official core edition enumeration](https://magic.wizards.com/en/news/making-magic/trivial-pursuit-more-or-less) corroborate all **81** remaining released/non-digital `expansion`/`core` codes from 2003–2022: **80 historical regular expansions/core editions** and one specifically documented **Time Spiral Timeshifted (`tsb`) bonus sheet**, not a standalone main release. The complete 142-code Scryfall category reconciles as **136 source-reviewed historically regular or contemporary mainline releases**, **4 directly documented auxiliary, discarded, or integrated bonus-product codes** (`mat`, `big`, `sum`, `tsb`), and **2 provisional localized printing variants** (`fbb`, `4bb`). **Zero** of the 142 codes remain wholly unreviewed, but those two variants still lack independent primary-source certification. This **does not** certify the total number of all-time premier sets across all Scryfall categories or reconcile retroactive terminology; treat 136 only as the defined **regular/mainline-within-Scryfall-expansion/core candidate subset**. Per-code primary sources and exact reproducible audits: `data/set_atlas/wotc_mid_release_evidence_2003_2022.json`, `data/set_atlas/wotc_mid_release_audit_2003_2022.json`, `scripts/audit_wotc_mid_sets.py`, `tests/test_wotc_mid_sets.py`. The separate 1,062-code set/printing atlas continues to catalog all supplemental sets.

**2026-10-29 cross-category product-family checkpoint:** A deterministic whole-catalog audit (`scripts/audit_set_cross_category.py`, `data/set_atlas/cross_category_audit_2026-10-29.json`) divides all **1,062** Scryfall set codes into **142** released non-digital expansion/core candidates, **848** released non-digital codes in other `set_type` categories, **62** already-released digital-only codes and **10** future-dated codes; no overlap or omissions. A **12-product** bounded Wizards source review now distinguishes the substantial Modern-legal but non-Standard-2023 `ltr` (Lord of the Rings), Modern-only `acr`, the `mh1`/`mh2`/`mh3` Modern Horizons supplemental line, `cmm`, `inr`, `rvr`, `j22`, `pip`, `ltc`, and `cmr`. The **836** other released, non-digital non-expansion/core codes have **not** each had official individual-product review and MUST NOT be called 836 additional premier sets. Key sources: [Wizards 2022 premier/Standard description](https://magic.wizards.com/en/news/announcements/magic-the-gathering-pricing-update), [2025 forward-only Universes Beyond policy](https://magic.wizards.com/en/news/announcements/aligning-the-universes-making-all-our-sets-legal-in-all-our-formats), plus exact Wizards product/release links in `data/set_atlas/cross_category_evidence_2026-10-29.json`. External specialist [Cardmarket Core Sets](https://help.cardmarket.com/en/CoreSets) corroborates `fbb` and `4bb` as foreign-language black-border versions of existing core editions, but they **remain provisional** pending a Wizards primary citation. This is a **cross-category scope and exception audit**, not a certified all-time premier-set census; don't reinterpret the separate 136 historical regular/mainline expansion/core count as every standalone Magic booster release.

**2026-10-29 complete outside-category research triage checkpoint:** The read-only, deterministic `scripts/audit_product_family_triage.py` generated `data/set_atlas/product_family_triage_2026-10-29.json` from the **frozen October 29** Scryfall product catalog and the prior official-example ledger. All **848** released non-digital set codes outside `expansion`/`core` now have exactly one explicit **Scryfall-type-derived research cohort**: **645** promotional/records/extras, **112** preconstructed/boxed, **51** draft/starter variants, **34** reprint/curated products, **6** special inserts/Eternal subsets. The previously **12 individually Wizards-reviewed** codes retain their primary-source links; **836** remain individually source-pending, with a reproducible sortable priority queue and distinct known exceptions (`plst`, localized Chronicles border variants, Universes Within, Modern-only LTR and Modern Horizons). These cohorts are **research triage**, NOT Wizards' official product classification, an additional premier-set count, or a proven list of physically standalone booster products. Explicit `parent_set_code` is retained; absence of parent does not prove standalone. A separate `scripts/product_family_lookup.py` offers offline `--summary`, `--cohort`, `--type`, `--parent`, `--priority` and `--only-pending` lookups. Five focused integrity tests and a dedicated CI rebuild protect the entire 1,062-code partition and forbid silently upgrading the 836 unreviewed entries into official facts. This is a source-preserving triage milestone; **source review remains necessary** for each officially certified product-family or premier claim.

**Phase 1B pilot checks completed:**

- [x] SHA-256 verification of the October 29 Scryfall Default Cards source and its reported record count; no duplicate printing IDs or conflicting set name/`set_type` values.
- [x] Internal arithmetic and shard-reference audit of the October 28 baseline manifest, with missing historical shard-byte verification explicitly recorded.
- [x] Reproducible `set_type` category totals, all-code dated catalog, and explicit treatment of future-dated printing records.
- [x] First source-backed, bidirectional set/card lookup CLI; Alpha and Black Lotus spot checks, date-gated Star Trek example, and six portable unit tests.
- [x] Verify all 105 **committed** historical shard file hashes, sizes, row counts, printing-ID uniqueness and set joins; reconstruct stable card/set lookup indexes.
- [ ] Independently reconcile individual printing IDs against the **unavailable original October 28 bulk**; do not call that source verified until recovered.
- [x] Import and freeze Scryfall Set API `released_at`, `digital`, `set_type` and **560 explicit `parent_set_code` links** for all 1,062 printing-atlas codes; validate against the independent October 29 printing catalog.
- [x] Review a bounded 2023–October 2026 official-main-release sample (21 verified), plus nine reviewed exceptions/upcoming/special products, with direct Wizards citations and tests.
- [x] Review all 38 early 1993–2002 Scryfall non-digital expansion/core codes against Wizards' historical booster/core enumerations; certify 35 regular releases, directly document Summer Magic's rejected print run, and flag 2 localized editions as provisional.
- [x] Review all 81 2003–2022 Scryfall non-digital expansion/core codes against Wizards historical annual release retrospectives and core enumerations; classify 80 as regular sets and `tsb` as an integrated bonus sheet.
- [x] Partition the **entire** October 29 1,062-code Scryfall Set API catalog by release status, paper/digital, and expansion/core versus other categories without overlap; review 12 major non-expansion/core products against exact official Wizards articles and release notes.
- [ ] Independently corroborate `fbb` and `4bb` foreign-border variants with Wizards primary documentation; third-party Cardmarket corroboration is recorded but does not close this gate.
- [x] Exhaustively triage all **848** released non-digital other-category codes into five transparent Scryfall-metadata research cohorts and a sortable, source-linked queue covering the **836** items still awaiting individual Wizards review; preserve the 12 earlier primary-source examples without reclassification.
- [ ] Work the 836-code queue in priority order, starting with the **44** source-pending draft/starter variants and **31** source-pending reprint/curated codes; separately define *premier*, *Standard-legal*, *full-booster*, *reprint edition*, and *any set code* totals before a universal set count.
- [x] Publish complete, GitHub-readable historical set-to-card and card-to-set indexes without a local bulk snapshot (32 deterministic JSON buckets and read-only CLI); the October 29 current-snapshot lookup remains separately dated.

**Counting rules (mandatory in every answer/export):**

- A **set-code count** includes every Scryfall set code in the selected snapshot; distinguish expansion/core sets, Masters/supplemental, Commander products, promos, tokens, digital and other categories. Never present the all-category count as the number of regular expansion sets.
- A **printing count** counts distinct set/collector-number printing entries (including variants when present); a **unique-card count** deduplicates by the selected stable card identity (normally Scryfall Oracle ID). Report both when relevant and document multi-face/special-object handling.
- **Cards appearing in a set** means all included printings or distinct card identities in that release; **cards first introduced in a set** means identities whose earliest eligible release is that set. Separate debuts from reprints and label any ties, preview/promotional-date ambiguities, or digital-versus-paper differences.
- Respect Cory's preference for **English/default-language cards**. Do not imply exhaustive foreign-language coverage. Distinguish physical from digital, released from announced, and snapshot date from current live data.

**Deliverables and verification gates:**

- [ ] Audit the existing printing index and per-set shards against the archived Default Cards snapshot; document missing categories, duplicates, and stable joins.
- [ ] Establish a normalized set catalog: canonical name/code, `set_type`, release date, paper/digital status, parent set/product associations and authoritative source provenance.
- [ ] Publish reproducible totals for **all Scryfall set codes** and separately for **premier expansion/core sets**, plus other clearly defined product categories; never report an unqualified "total sets" figure.
- [ ] Publish for **each set** all English/default-language printing records and a deduplicated card inventory, with counts for printings, unique identities, first appearances and reprints.
- [ ] Build bidirectional searches: **set → card list/counts** and **card → first printing, all sets, chronological printing history**. Support set code, name, year, product type and date-range filters.
- [ ] Verify debut/reprint attribution using dated, stable card identities; document edge cases such as promos, same-day releases, digital-first objects, variants, tokens and double-faced cards.
- [ ] Maintain two separately labeled timelines: **real-world set/product release chronology** and **in-universe lore chronology**; link them only with sourced claims, not assumed chronological equivalence.
- [ ] Connect sets to supported planes, story arcs, factions, characters, mechanics and Commander-relevant releases without inventing lore connections.
- [ ] Add automated checks for per-set counts, uniqueness, category totals, date order, broken references, and sample queries (including Alpha, Legends, a Commander product, a promo set and a digital release).
- [ ] Publish a user-facing set index with an explicit snapshot date, coverage/exception report, source links and exportable English card lists; keep it maintainable as new releases arrive.

**Acceptance:** A user can ask "How many sets have been released?" and receive category-specific counts; request every card in any set; distinguish originals from reprints; find every set containing a card; and compare publication history with lore chronology. Counts must be reproducible from the named, verified snapshot.

## Phase 2 — Lore enrichment and primary-source integrity

- [x] Recover and strictly audit all **660** official Wizards source URLs in the original inventory.
- [x] Commit a metadata-only provenance record without republishing copyrighted article bodies.
- [x] Perform initial bounded triage of **341** uncertain name-matched character links.
- [ ] Ensure future environments can reliably refetch and strictly audit official story text before using it as evidence.
- [ ] Review the two additional official-source leads (Koth and Wrenn) for exact printing-specific relationships.
- [ ] Investigate the approximately **1,220** enriched cards that lack a cited lore entry.
- [ ] Link direct printed depictions, official story references, artwork, flavor text, characters and important events where evidence supports them.
- [ ] Keep unsupported matches explicitly unresolved; track sources and reasoning for changes.
- [ ] Expand the primary-source inventory and rerun targeted reference-integrity checks.

## Phase 3 — Searchable Multiverse relationship graph

- [ ] Audit existing repository entity structures before creating redundant schemas.
- [ ] Stabilize IDs for Character, Plane, Event, Faction, Artifact, CardRepresentation and Claim records.
- [ ] Record directional, dated, cited relationships (e.g. allied_with, fought, created, present_at, depicted_by).
- [ ] Separate `CANON_CONFIRMED`, `CANON_IMPLIED`, `CANON_DISPUTED`, `ALTERNATE_CONTINUITY` and hypothetical connections.
- [ ] Make relationships searchable in both directions, with canonical source links.
- [ ] Add duplicate, broken-link and unsupported-claim regression checks.

## Phase 4 — Foundational lore research packs

- [ ] **Pack A: Ugin, Nicol Bolas, Elder Dragon origins and the Elder Dragon War.** Chronology, rivalries, allies, factions, planes, cards and primary sources.
- [ ] **Pack B: Thran civilization → Yawgmoth → Old Phyrexia → Brothers' War.** People, artifacts, conflicts and consequences.
- [ ] **Pack C: Dominaria → Weatherlight → the Legacy → Phyrexian invasion.** Historical transitions and connections.
- [ ] For each pack, publish a verified chronology, relationship map, source bibliography, explicit uncertainties and lore-deck candidates.

## Phase 5 — Full-history and plane-by-plane expansion

- [ ] Expand the Mending, major planeswalkers and the Gatewatch.
- [ ] Expand Bolas's schemes and the War of the Spark.
- [ ] Expand Mirrodin/New Phyrexia and March of the Machine.
- [ ] Expand Omenpaths and later canonical stories.
- [ ] Audit major planes, regions, factions, artifacts and overlooked characters.
- [ ] Connect cross-plane histories and document contradictions/retcons.
- [ ] Use the Phase 1B Set & Printing Atlas to navigate published sets and storylines while keeping real-world release dates separate from in-universe event order.
- [ ] Maintain an explicit coverage/gaps inventory as new sets and stories arrive.

## Phase 6 — Lore-first Commander deckbuilding engine

- [ ] Retrieve lore-relevant cards with grades: direct depiction, canon reference, lore-inspired, mechanical stand-in.
- [ ] Compare eligible commander choices with verified color identity and relevant story context.
- [ ] Build mechanically coherent, realistic-power Commander strategies around the narrative.
- [ ] Support optional set/era/first-printed-in restrictions using verified Phase 1B data without confusing reprints with original debuts.
- [ ] Verify each final 100-card list, singleton restrictions, relevant rules/combinations, legality and current bracket.
- [ ] Provide three Archidekt tags and one clean commander-first `1x Name` import list.
- [ ] Pilot 1: **Ugin & Nicol Bolas — Elder Dragon Duality**.
- [ ] Pilot 2: **Original Primeval Dragons**.
- [ ] Pilot 3: **Ugin's Allies and Heroes**.
- [ ] Preserve the original approved 62 decks; a new pilot never overwrites them.

## Phase 7 — Ultimate MTG question-answering companion

- [ ] Support precise lookups for card names, Oracle text, types, identities, mechanics, printings and relevant rulings.
- [ ] Answer set questions with category-qualified totals, full set card lists, printing/debut/reprint distinctions and cited snapshot dates from Phase 1B.
- [ ] Answer obscure lore and chronology questions through cited evidence and dated canon status.
- [ ] Explain ambiguous/retconned narratives rather than inventing certainty.
- [ ] Integrate card, lore and strategic search for Commander recommendation and deckbuilding questions.
- [ ] Test difficult representative queries, cross-references, and interaction explanations.
- [ ] Flag unavailable, stale or low-confidence information explicitly.

## Phase 8 — Release quality and continuing upkeep

- [ ] Keep targeted CI checks for card counts, source integrity, relationship claims, and deck legality.
- [ ] Monitor new official stories, Oracle changes, releases, rules and Commander format updates.
- [ ] Rebuild and reconcile the Phase 1B set catalog and bidirectional printing lookups when new sets or printings appear, retaining historical snapshots.
- [ ] Update snapshot manifests with actual download bytes and stable hashes.
- [ ] Maintain an honest progress tracker: completed, under review, blocked, and not started.
- [ ] Define an MTG Multiverse Companion milestone release based on verified features, not an arbitrary percentage of all lore.
- [ ] Treat continual future MTG releases as an ongoing maintenance track rather than a permanently finishable backlog.

## Immediate execution queue — DO THESE NEXT

1. **Continue Phase 8:** the first twelve-card generated batch is reviewed; select the next bounded, directly evidenced slice toward the remaining **1,953** priority enrichments. Preserve all previous records and rerun the full guarded source verification for each publication.
2. **Index exclusions — completed for the October 29 snapshot:** retain the verified 5,270-record classification and review the 305 future-dated IDs after release, rather than prematurely importing them.
3. **Continue Phase 1B Set & Printing Atlas:** all 1,062 codes are audited, and the 848 released paper other-type entries now have five explicit Scryfall-source research cohorts: 645 promotional/extras, 112 boxed/preconstructed, 51 draft/starter, 34 curated/reprint, and 6 special inserts. Prioritize the 44 draft/starter and 31 reprint/curated codes still lacking official individual source review; maintain the 12 reviewed examples and the FBB/4BB primary-source gate. Keep premier versus full booster versus all-code counts separate; preserve the 62 Grixis approvals.
4. **Close meaningful lore gaps:** review the **341** uncertain links and the **~1,220** cards with no identified lore connection while preserving unsupported entries as unknowns.
5. **Build the relationship layer:** use and extend current schemas for claim provenance, card depictions, people, events and planes.
6. **Deliver the first research pack:** Ugin/Nicol Bolas and Elder Dragon origins, with canon distinctions and verified card ties.
7. **Demonstrate the deckbuilder:** build the first evidence-backed lore-first Commander list from the research pack.
8. Expand the timeline, other packs, and everyday MTG question-answering capabilities in subsequent focused milestones.

## Rules for every future work session

1. Read **this checklist** and the latest GitHub state before acting. Check merged PRs, live tracker and current snapshot manifests; do not assume a remembered milestone was published.
2. Work in bounded, reviewable batches with actual artifacts, tests and post-merge verification. Prefer substantive progress to repeated planning cycles.
3. Preserve the canonical `corymstover/grixis-commander-encyclopediaGPT` approved decklists, hashes and exceptions; do not replace them without Cory's explicit new approval.
4. Do not use a newer Scryfall bulk as if it were the missing historical `snap-20261016`. Use the independent modern snapshot path for the broad Companion.
5. Keep official lore citations, confidence and continuity distinctions. Never promote a name match to canon automatically.
6. Keep Oracle text, card legality, format policy and brackets current; annotate dates and rule-version assumptions.
7. After every milestone merge, update the completed checkboxes and checkpoint counts in this file, link the exact PR/commit/CI evidence, and state what remains. If the project Source copy is older, **GitHub's latest verified file is the workflow authority**.

## Definition of the first major Companion release

- [ ] Priority-card enrichment backlog fully accounted for (completed or explicitly documented exceptions/gaps).
- [ ] Searchable cited connections across the three foundational lore packs.
- [ ] Reliable lookup and rules checks backed by current Scryfall and official sources.
- [ ] A verified Phase 1B set catalog with category-specific counts, set → card and card → set lookups, debut/reprint identification and English export support.
- [ ] At least one complete, reviewed lore-first Commander deck built from the new graph.
- [ ] No regression in the 62 archived approved Grixis decks.
- [ ] Passing focused CI and an up-to-date, source-backed coverage report.

*This is a living workflow, not a claim that all of Magic lore can be declared permanently finished. Preserve this file and revise the verified checkpoint after every substantive work batch.*
