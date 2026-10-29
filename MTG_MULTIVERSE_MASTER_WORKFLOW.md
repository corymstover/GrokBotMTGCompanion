# MTG Multiverse Companion — Master Workflow & Progress Checklist

**Version:** 1.1  
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
| Individual card index | **33,894 records** | The 5,270 Oracle IDs outside the index require classification before assuming a gap. |
| Set/printing inventory | **1,062 set codes; 119,509 default-language printing records; 107,700 English paper records** | October 28, 2026 `data/printing_lore/manifest.json` baseline. Set codes include promos and supplemental products; these are **not** 1,062 premier expansions. Printing records are not distinct card designs. Phase 1B certification is still pending. |
| Priority card enrichment | **3,397 / 5,361 (63.4%)** | **1,964 remaining** as of the historical Phase 8 scope. |
| Official Wizards story inventory | **660/660 recovered and strictly audited** | Hash/URL provenance committed; full article text was cached outside Git and must be refetched/audited in a new environment. |
| Uncertain character links | **341 name-only links triaged** | Two official-page leads warrant review; triage is not canon approval. |
| Cards without a linked lore entry | **~1,220** | Investigate or preserve as documented unknowns; never fabricate lore. |
| Historical Scryfall lock | **Preserved** | `data/grixis/dev_snapshot_lock.json` records `snap-20261016`; exact old bulk bytes remain unconfirmed. |
| Active Scryfall release | **Archived, re-downloaded, verified** | [snap-20261029-40848334824-1](https://github.com/corymstover/GrokBotMTGCompanion/releases/tag/snap-20261029-40848334824-1): Oracle Cards, Default Cards, Rulings and SHA-256 manifest. |
| Snapshot reconciliation | **Passed read-only** | [PR #784](https://github.com/corymstover/GrokBotMTGCompanion/pull/784) and [report workflow](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40848889092): 0 previously indexed/enriched IDs disappeared; 0 differences in indexed type, color identity, Commander legality, Game Changer status or ruling counts. It is **not** a complete historical Oracle-text diff. |

Infrastructure checkpoint: [PR #783](https://github.com/corymstover/GrokBotMTGCompanion/pull/783) separated current Multiverse ingestion from the historical Grixis lock, added the durable snapshot capture/verification workflow, and passed CI. [PR #784](https://github.com/corymstover/GrokBotMTGCompanion/pull/784) added the read-only research reconciliation and passed CI.

## Phase 1 — Card database and research inputs

- [x] Preserve the original 62 Grixis approved decks separately.
- [x] Archive a current Scryfall Oracle Cards, Default Cards and Rulings snapshot with hashes.
- [x] Independently download the release assets again and verify them.
- [x] Separate historical and modern Scryfall caches and validation modes.
- [x] Compare the new snapshot against the committed card index and enrichment inventory without mutating either.
- [ ] Classify the **5,270 currently unindexed Oracle records** (intentional exclusions, digital/special objects, genuinely missing cards).
- [ ] Add eligible missing records to the normal card index in bounded, verified batches.
- [ ] Finish the **1,964 remaining priority-card lore/synergy enrichments** without flattening existing curated data.
- [ ] Document a repeatable update process for future Scryfall changes, current legality, and official rules.
- [ ] Recount coverage and verify representative lookup queries after each published batch.

## Phase 1B — MTG Set & Printing Atlas (official milestone)

**Goal:** Make every recorded MTG release independently discoverable, countable, and searchable by set, while retaining accurate card-by-card printing histories. This is a distinct catalog/data-quality milestone within Phase 1, not a replacement for the existing card and lore work.

**Existing foundation:** Reuse `Printing History.md`, `data/printings_summary.csv`, `data/printing_lore/manifest.json`, its per-set printing shards, and the independently archived Scryfall Default Cards snapshot. The October 28 manifest reports **1,062 Scryfall set codes**, **119,509 default-language printing records**, and **107,700 English paper printing records**. These are historical input counts, **not** a verified number of main expansions, unique cards, or newly introduced designs.

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

1. **Resume Phase 8:** establish a bounded first batch toward the remaining **1,964** priority enrichments; compare current source evidence and publish only reviewed differences.
2. **Classify index exclusions:** inspect the **5,270** non-indexed Oracle records; do not assume they're all missing playable cards.
3. **Begin Phase 1B Set & Printing Atlas:** audit the existing 1,062-code printing manifest; define category and count rules; ship a verified first set-index/lookup batch before claiming the feature complete.
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
