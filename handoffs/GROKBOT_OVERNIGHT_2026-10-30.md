# Grok Bot overnight handoff — 2026-10-30

This file mirrors the Grok Bot batch log (PROGRESS.md) so ChatGPT or Cory can pick up the work from GitHub alone. All times are America/Chicago (CDT).

Scope rules for this overnight run:
- The Grixis area is finished; no Grixis deck, ledger, branch or PR was touched.
- Approved lore decks and locks are untouched.
- Nothing is marked APPROVED, LOCKED or CERTIFIED.
- No spending.

## Batch 1 — 2026-10-30 ~00:10–01:35 CDT

**Milestone:** Phase 6 Pilot 1, *Ugin & Nicol Bolas — Elder Dragon Duality*. This is a complete, verified 100-card proposal, and it is **UNAPPROVED**.

- Branch: `grokbot-ugin-bolas-duality-pilot-20261030`
- PR: https://github.com/corymstover/GrokBotMTGCompanion/pull/823
- Commits:
  - `41462756` (pilot)
  - `1bcbfd86` (workflow v2.27)
  - this handoff commit
- Files added:
  - `data/lore_decks/drafts/ugin_bolas_elder_dragon_duality_{proposal.json,proposal.md,decklist.txt,printing_evidence.json,archidekt_import.txt}`
  - `research/PHASE6_PILOT1_Ugin_Bolas_Elder_Dragon_Duality.md`
  - `scripts/build_ugin_bolas_duality_pilot.py` (scripted builder; reads printings from the modern snapshot `snap-20261029-40848334824-1`, never the Grixis lock)
  - `scripts/audit_ugin_bolas_duality_pilot.py` (offline audit)
  - `tests/test_ugin_bolas_duality_pilot.py` (9 tests)
  - `.github/workflows/phase6-pilot1-ugin-bolas-duality.yml`
  - `MTG_MULTIVERSE_MASTER_WORKFLOW.md` bumped to v2.27
- The deck:
  - Commander: Nicol Bolas, the Ravager (m19/218).
  - The 99 includes Ugin, the Spirit Dragon (frf/1, the exact story art from Pack A4), Ugin, the Ineffable and Ugin, Eye of the Storms.
  - Seven story acts.
  - Tiers: 6 DIRECT_DEPICTION (official story art captions), 54 CANON_REFERENCE, 8 LORE_INSPIRED and 15 MECHANICAL_SYMBOL, plus 17 basics.
- Local verification:
  - Planner `--validate` against the Oct 29 oracle bulk: passed. 100 cards, UBR identity, 35 lands, 0 hard issues.
  - `evaluate_decklist --combos`: hard checks PASS. One Game Changer (Bolas's Citadel). No mass land denial. Local Spellbook data finds no two-card infinites. Bracket 3.
  - Decklist SHA-256: `01d087aa2819b1ed3c7ac1f64843f76f36b551b72fda62d64218d19c40b0ab45`.
- New official sources verified this batch:
  - Hour of Devastation story (2017-07-26): captions for the Defeat cards and Hour of Devastation; Tezzeret calls Bolas "master".
  - War of the Spark "Ashes" story: Bontu harvests Bolas's sparks; Liliana's Triumph caption.
  - Devastation Information Part 3: Bolas's three gods.
  - More War Games: the God-Eternals.
  - Amonkhet plane page and Sarkhan profile.
- **Merged:** 2026-10-30 01:30 CDT as merge commit `831ebf8f1e2ac76e32aab5b8adeb57650be6cdfb`. This was a normal merge, with no admin bypass and no force. Before merging, all 10 checks on the exact head `a3e0c3a5` were green, main was still at `c727e4c7`, and no files overlapped with any open chatgpt-* PR.
- Post-merge CI on `831ebf8f`: all 9 workflows passed (Pack A/A2/A3/A4, Phase 1B gates, and the Pilot 1 audit).
- Protected-path diff (`grixis/`, `data/grixis/`, `state/current_deck_overrides.json`, `data/lore_decks/approvals/`): empty.
- **Being merged is not owner approval.** The deck stays an UNAPPROVED proposal until Cory approves it.

### Exact next steps
1. PR #823 is merged; nothing is left to do for it.
2. Cory reviews the pilot. Only Cory can approve it. Do not edit PR #776 (ChatGPT's Deck #9 Ugin life story); this pilot is independent of it.
3. Throughput: turn `build_ugin_bolas_duality_pilot.py` and its audit into a spec-driven generic `scripts/build_lore_pilot.py` plus `audit_lore_pilot.py`. Pilots 2 and 3 (Original Primeval Dragons; Ugin's Allies and Heroes) then become JSON specs.
4. Close the Pack A genealogy gaps (A003/A004 disputed, A011 open), then start Packs B and C.

## Batch 1 follow-up
- [PR #824](https://github.com/corymstover/GrokBotMTGCompanion/pull/824), *Overnight handoff: batch 1 merge record* (docs only), merged at 2026-10-30 01:34 CDT as `dfc8891de03c11ba91adf81effc5ca08e2fef10f`.

## Batch 2 — 2026-10-30 ~01:35–02:30 CDT

The aim was to spread work across phases (Cory's request). Every PR used a normal merge with `--match-head-commit`, and all checks on the exact head were green. There were no admin bypasses or force-pushes, and no chatgpt-* PR or branch was touched.

| PR | Phase | What | Merge commit (CDT) |
|---|---|---|---|
| [#825](https://github.com/corymstover/GrokBotMTGCompanion/pull/825) | 3 | Cited Multiverse claim graph v1: `scripts/build_multiverse_graph.py` (`--check`), `scripts/query_multiverse_graph.py`, CI workflow | `096486c6` (01:40) |
| [#826](https://github.com/corymstover/GrokBotMTGCompanion/pull/826) | 4 | Pack B v1, Thran → Yawgmoth → Brothers' War: 18 claims, 23 entities, 8 Wizards sources | `8ebe31e9` (01:44) |
| [#827](https://github.com/corymstover/GrokBotMTGCompanion/pull/827) | 7 | `scripts/mv_ask.py` companion: card + lore answers with VERIFIED / QUALIFIED / NOT_FOUND (exit 3) | `d9611cd6` (01:47) |
| [#828](https://github.com/corymstover/GrokBotMTGCompanion/pull/828) | 4 | Pack C v1, Weatherlight → Invasion → New Phyrexia: 28 claims, 26 entities, 6 Wizards sources; "who defeated / who created" asks | `185b5146` (01:50) |
| [#829](https://github.com/corymstover/GrokBotMTGCompanion/pull/829) | 1 / 8 | Oracle text drift, Oct 28 shards vs Oct 29 snapshot: **0 changes across 33,894 cards**; 305 new paper IDs are future-dated (`trk`/`trc`, 2026-11-13) | `b5ff3a2f` (01:52) |
| [#830](https://github.com/corymstover/GrokBotMTGCompanion/pull/830) | 8 | `scripts/release_readiness.py`: 7 first-release criteria → **NOT_RELEASE_READY** (MET 1 · PARTIAL 3 · NOT_MET 1 · EXTERNAL 2) | `f6a91349` (01:54) |
| [#831](https://github.com/corymstover/GrokBotMTGCompanion/pull/831) | — | Master workflow v2.28 and this handoff (docs only) | `ada2501c` (01:57) |
| [#832](https://github.com/corymstover/GrokBotMTGCompanion/pull/832) | 6 | Spec-driven lore pilot builder and audit, plus **Pilot 2, Original & Primeval Dragons** (commander The Ur-Dragon): 100 cards, of which 85 are named and 15 basics. Tiers: 35 CANON_REFERENCE, 12 LORE_INSPIRED, 38 MECHANICAL_SYMBOL, 0 DIRECT_DEPICTION. **UNAPPROVED** | `95729905` (02:03) |
| [#833](https://github.com/corymstover/GrokBotMTGCompanion/pull/833) | 4 | Pack A open-question evidence review of A003, A004 and A011. Grades are retained and the review is preliminary | `e68ee68d` (02:08) |
| [#834](https://github.com/corymstover/GrokBotMTGCompanion/pull/834) | 3 | Pilot 2 (UNAPPROVED) linked into the claim graph as a DeckProposal | `0eb00a06` (02:09) |
| [#835](https://github.com/corymstover/GrokBotMTGCompanion/pull/835) | 4 | Pack A review correction. A003 now records that Wizards sources disagree: Piru survives per the MH2 "Returning Legends" article but is absent from Bolas's list. Adds A-PROP-04 (Elder Dragons spawned by the Ur-Dragon, editorial source), **unapplied** | `09d010af` (02:16) |
| [#836](https://github.com/corymstover/GrokBotMTGCompanion/pull/836) | 7 / 8 | Commander deck-construction rules, built on a verbatim excerpt of the official CR dated 2026-09-25 (sha256 `8d860e45…`). Covers 903.3–903.5d and 702.124 partner, partner—[text], partner with, Background and Doctor's companion. `scripts/commander_rules.py` has `commander`, `include` and `audit-eligibility`. The eligibility audit agrees with the index on **all 33,894 cards (0 disagreements)**: 3,884 can be a commander and 29 are Background-only. mv_ask routes rules questions there, and a CI step was added. Release readiness for lookup/rules stays **PARTIAL** because gameplay interaction checks are not built | `84130ca8` (02:21) |
| this PR | — | Master workflow v2.29 and this handoff (docs only) | — |

Graph after #830: 305 nodes, 488 edges and 78 claims (69 confirmed, 4 disputed, 2 implied, 2 open, 1 alternate). There are 37 sources, none of them non-Wizards. **Packs A, B and C are all PRELIMINARY_RESEARCH**; none is owner approved or certified.

After #834 the graph has **376 nodes and 573 edges**: 78 claims, 37 sources (all Wizards) and 2 DeckProposal nodes. The `--check` passes.

Pack A review status: A003 and A004 **stay CANON_DISPUTED** and A011 **stays OPEN_QUESTION**. There are **4 proposals, none applied**, waiting for Cory. Nothing was approved, locked or certified.

### Discoveries
- The MH2 "Returning Legends" article (Wizards) calls Piru a surviving Elder Dragon, which contradicts the A003 survivor list. The first review (#833) missed this, and #835 corrected it.
- The owner-approved Karn and Yawgmoth lore decks contain cards banned per Scryfall: Tolarian Academy, Yawgmoth's Bargain and Sundering Titan. These are documented intentional exceptions in `data/lore_decks/approvals/`, which was read only. The new test honours them, and no deck was changed.
- Before this batch, "Who is Ugin's brother?" returned NOT_FOUND in mv_ask because the graph relation is `twin_sibling_of`. #836 adds the fallback.
- A "Partner with" name containing a comma (Pir and Toothy) broke naive parsing. It is now parsed before splitting.
- The box was replaced at about 02:15 CDT. Lost with it: `/workspace/out/multiverse/` (the overnight brief and PROGRESS.md), the local oracle cache, the CR download and some uncommitted work. The work was recreated, and the CR text was re-verified against the same sha256 from the read-only Grixis cache. The store mount was absent at that point. Everything in GitHub was unaffected.

### Blockers
- 1,953 priority-card enrichments: the guarded rebuild needs the story-text, EDHREC and Commander Spellbook caches, which are not on the box.
- Release criterion "reviewed deck built from the graph" needs Cory to review Pilot 1 (#823). Approval files are written only by the owner.

### Not started (next steps, in value order)
1. Pilot 3, Ugin's Allies and Heroes: Narset, Elspeth and others first need graded Pack A claims, then a spec for `build_lore_pilot.py`. The result stays UNAPPROVED.
2. Cory's review of Pilot 1 (#823), Pilot 2 (#832) and the 4 unapplied Pack A proposals. If A-PROP-04 is accepted, the Pilot 2 commander may move from LORE_INSPIRED to CANON_REFERENCE.
3. Pack C: *Return to Dominaria* episode extraction, March of the Machine, and card anchors for Pack B/C claims (CardRepresentation nodes).
4. Edge dates (in-universe era) on graph relationships.
5. Phase 7 gameplay rules-interaction checks. Deck-construction checks are done (#836); this is the remaining PARTIAL in the lookup/rules criterion.
6. After 2026-11-13: re-snapshot, rerun `oracle_drift_report.py`, and admit the 305 `trk`/`trc` cards.

Protected-path check (`git diff --stat dfc8891d origin/main -- grixis/ data/grixis/ state/current_deck_overrides.json data/lore_decks/approvals/`): empty.

## Batch 3 — 2026-10-30 ~02:24–04:00 CDT (final; interrupted ~03:14 and resumed)

Owner steering at 02:24: commit the brief first; skip store copies (the store mount is gone, so the repo is the backup); try rebuilding the enrichment caches from free public bulk data; otherwise pick by leverage.

| PR | Phase | What | Merge (CDT) | CI on the exact head |
|---|---|---|---|---|
| [#838](https://github.com/corymstover/GrokBotMTGCompanion/pull/838) | — | Overnight brief committed at `handoffs/GROKBOT_OVERNIGHT_BRIEF_2026-10-30.md` (docs) | `f46facdb` (02:26) | 1/1 pass |
| [#839](https://github.com/corymstover/GrokBotMTGCompanion/pull/839) | 3 | Card-name anchors for Pack A/B/C entities from the Scryfall snapshot (navigation only) | `44f493d4` (02:33) | 8/8 pass |
| [#840](https://github.com/corymstover/GrokBotMTGCompanion/pull/840) | 7 | Gameplay rules-interaction checks built on published Scryfall rulings and verbatim CR 701/702 | `0920dd67` (02:40) | 21/21 pass |
| [#841](https://github.com/corymstover/GrokBotMTGCompanion/pull/841) | 3 | Pack C2 *Return to Dominaria* extraction: 39 verbatim-quoted claims, PRELIMINARY_RESEARCH | `943e06e4` (02:48) | 25/25 pass |
| [#842](https://github.com/corymstover/GrokBotMTGCompanion/pull/842) | 3 | Pack A5 Ugin's allies: 16 verbatim-quoted claims for Pilot 3, PRELIMINARY_RESEARCH | `74a0d7a4` (02:52) | 25/25 pass |
| [#843](https://github.com/corymstover/GrokBotMTGCompanion/pull/843) | 3 | Story-art caption atlas: 1,060 verified captions, 823 cards, 165 official pages, 70 rejected; 143 `art_captioned_in_story` edges | `6917bc86` (02:58) | 23/23 pass |
| [#844](https://github.com/corymstover/GrokBotMTGCompanion/pull/844) | 6 | Pilot 3 "Ugin's Allies and Heroes". Commander Jace, Multiverse Architect; 15 CANON_REFERENCE, 32 LORE_INSPIRED, 40 MECHANICAL_SYMBOL, 13 basics, 0 Game Changers. **UNAPPROVED proposal** | `0344cd53` (03:08) | 24/24 pass |
| [#845](https://github.com/corymstover/GrokBotMTGCompanion/pull/845) | 3 | In-universe `era` labels plus an `era_basis` disclaimer on all 149/149 claim edges. An `in_universe_date` is accepted only with a quote and a cited source; there are 0 such dates. 334 tests | `a10a5349` (03:14) | 23/23 pass (the path-filtered `lore-pilots` check is not triggered) |
| [#846](https://github.com/corymstover/GrokBotMTGCompanion/pull/846) | — | Interim Batch 3 handoff (docs) | `59ebed06` (~03:17) | 1/1 pass |
| [#847](https://github.com/corymstover/GrokBotMTGCompanion/pull/847) | 3 | Pack C3 *Assault on New Phyrexia* (Episodes 1–5): 19 verbatim-quoted claims, 27/27 quotes, 21 entities, stage `one_strike_2023`, PRELIMINARY_RESEARCH. Graph now 841 nodes, 1,330 edges; anchors cover 75 entities | `b313494f` (03:32) | 25/25 pass |
| [#848](https://github.com/corymstover/GrokBotMTGCompanion/pull/848) | 8 | Enrichment batch 38: the remaining **1,953** priority-pool cards, so **5,362/5,362**. The 3,409 earlier records are byte-identical. 202 new records carry official-story links; 462 carry only an outside-canon flag; 1,289 have neither (all 1,751 unlinked are honestly marked "no lore linked yet"; corrected in batch 4 from a "664 linked" miscount). Readiness: enrichment MET. 346 tests | `f65fe727` (03:53) | 23/23 pass |

Graph after #845: 767 nodes, 1,215 edges, with `--check` passing. The rules-interaction audit covers 6 draft decks, 17 links and 0 unresolved items.

### Discoveries
- **War of the Spark allies (negative result):** none of the six cached official WAR web stories, nor the Kaya or Teyo bio pages, mentions Ugin. The only hit (beyond-repair) is about Zendikar. Kaya and Teyo were therefore **not** included as Ugin allies, and nothing was fabricated.
- General Tazri is WUBRG, outside Jace's colour identity. It is recorded as unrepresentable and replaced by Jace, Unraveler of Secrets.
- No official pack quotes a Dominarian AR year. The era labels are story-stage names, not dates, and none were inferred.
- Pilot audits enforce the A4 exact-art printing. Ugin now uses the frf/1 Swanland printing.

### Enrichment caches (done)
The caches were rebuilt from free public sources with a polite, rate-limited prefetch:
- EDHREC public JSON: 3,931/3,931 pages.
- Commander Spellbook: 1,976/1,980 (4 failed; those render as unknown).
- Card data: the pinned Scryfall 2026-10-29 snapshot.

The caches live under the git-ignored `.cache/` and are not committed. The pipeline was:
1. `build_card_enrichment.py --batch 38 --defer-package-backlinks`
2. `build_packages.py --enrichment-backlinks-only`
3. A rebuild, then `--check`, which reported 0 problems.

**Discovery:** the prefetch's `load_bulk()` downloaded a newer oracle bulk file (`20261029210158`) into the pinned snapshot dir. It was moved out to `/workspace/scryfall-stray/` (reversible), and no repo file references it. Always export `MTG_SCRYFALL_MODE=multiverse SCRYFALL_OFFLINE=1` before running enrichment or anchor scripts.

### Blockers
- Owner review is still needed for Pilots 1–3 and the 4 unapplied Pack A proposals. Every lore deck and pack is still UNAPPROVED or PRELIMINARY_RESEARCH.
- `trk`/`trc` admission waits until after 2026-11-13.
- Readiness: NOT_RELEASE_READY (MET 2, PARTIAL 2, NOT_MET 1, EXTERNAL 2). The NOT_MET item is owner review of a graph-built deck.

### Next steps (value order)
1. Pack C4, *March of the Machine*, from the official episodes. This continues C3.
2. Deepen lore links for the 1,289 batch-38 records marked "no lore linked yet", using official story evidence only.
3. Claim-level card anchors for Packs C2 and C3.
4. An exhaustive pass over the RtD and ONE episodes.

Store copies were skipped per the owner. Protected-path check `git diff --stat dfc8891d origin/main -- grixis/ data/grixis/ state/current_deck_overrides.json data/lore_decks/approvals/`: **empty** (run after #848 merged, main `f65fe727`).

## Batch 4 — 2026-10-30 03:57–~04:45 CDT (final)

### Corrections
- **Batch-38 lore-link count corrected.** Of the 1,953 batch-38 records, **202** carry official-story links (201 presented-on, 1 spotlight). **462** carry only an outside-canon flag (276 Un-/playtest, 186 Universes Beyond) and no link. **1,289** have neither. All 1,751 without a link show the honest "no lore linked yet" line. The batch-3 report's "664 lore-linked" figure counted flag-only records as linked. The PR #848 body is left as written; this handoff and the workflow doc carry the correction.
- The repo brief copy now includes the owner's "Batch-3 lesson" section.

### Diagnosis: the 1,289
Every one of the 1,289 is tiered only `legendary-creature`. None appears in the story-art caption CSV, in verbatim flavor on a cached official page, or in a lore entry. 66 of the 284 caption-CSV story URLs are not in the current story cache. None of those 66 is in `primary_sources.csv`: they are 2012–2017 archive and Uncharted Realms URLs, and 7 are non-English translations. Fetching them was therefore not attempted.

### PRs (batch 4)
| PR | Phase | What | Merge (CDT) | CI on the exact head |
|---|---|---|---|---|
| [#850](https://github.com/corymstover/GrokBotMTGCompanion/pull/850) | — | Brief copy synced with the Batch-3 lesson; interim batch-4 handoff (docs) | `53652c48` (04:12) | 18/18 pass |
| [#851](https://github.com/corymstover/GrokBotMTGCompanion/pull/851) | 2/8 | Bulk official-story lore links. 123 records gain *Named verbatim in official story text* and 24 gain artist-matched *Card art shown on*. This newly links 136 records (b35 73, b36 22, b38 41); unlinked records fall from 2,971 to 2,835, all changes additive | `5ac4b048` (04:16) | 22/22 pass |
| [#852](https://github.com/corymstover/GrokBotMTGCompanion/pull/852) | 3/5 | Pack C4 *March of the Machine*: 21 verbatim-quoted claims (41/41 quotes), all 10 main-story episodes cited, stage `mom_invasion_2023`, PRELIMINARY_RESEARCH. Five claims are CANON_IMPLIED, each with a written limitation. Graph now 911 nodes, 1,444 edges; card-name anchors cover 81 entities | `1f1882ca` (04:23) | 25/25 pass |
| [#853](https://github.com/corymstover/GrokBotMTGCompanion/pull/853) | 3 | Claim-level card anchors for all 9 claim packs: 155/173 claims, 884 pairs. ART_IN_CITED_SOURCE 25, PRINTED_IN_STORY_SET 33 (C2→DOM, C3→ONE, C4→MOM), NAMED_PARTICIPANT 826. By pack: C2 33/39, C3 17/19, C4 19/21. Navigation only; anchors never claim a card depicts the event | `d45dd3ab` (04:26) | 22/22 pass |
| [#854](https://github.com/corymstover/GrokBotMTGCompanion/pull/854) | 2 | Koth/Wrenn printing-level lead review: 10 verbatim leads, 6 printing-specific, 13 printings. FRA #248/#199 come from image labels, ONE #138 and MID #208 from art credits, and MOM #217/#322 from frame captions. Workflow v2.31 | `43edb99e` (04:31) | 22/22 pass |
| [#855](https://github.com/corymstover/GrokBotMTGCompanion/pull/855) | 7 | `mv_ask` now answers "who killed X", "who is X's mother" and "who struck down X" from cited claim relations. Before, "Who killed Elesh Norn?" returned NOT_FOUND. Added 4 regression tests | `a89a7901` (04:35) | 20/20 pass |
| [#856](https://github.com/corymstover/GrokBotMTGCompanion/pull/856) | 5 | Story coverage/gaps inventory: 57/626 inventoried pages are cited by a claim pack. Of 33 arc buckets, 1 is fully cited, 9 partial and 23 not started. CI rebuilds and compares it | `67dc7a75` (04:39) | 22/22 pass |

Local full suite: 383 tests OK on the #856 head. One earlier full-suite run had a single failure in `test_multiverse_snapshots.test_modern_fetch_does_not_evict_previous_files`. The test passed alone and in 3 later full runs, so it is a likely flaky test and is recorded, not fixed.

### Discoveries
- The MOM episodes were already in the story cache (`text22`), so C4 needed no fetching.
- The caption atlas has no ONE or MOM art-caption pages, so C3 and C4 have no ART-tier anchors. Only the set-printing and named tiers apply to them.
- Card-name substrings can be character prose. "Wrenn and Six/Seven" in the Tangles, MOM Ep 5 and BRO Ch 5 prose names the characters, not the cards. The Koth/Wrenn review grades these CHARACTER_PROSE_ONLY.
- The Legends of Reality Fracture image labels (`0248_MTGFRA_MainPair`) encode exact collector numbers. This is a reusable printing-specific signal for future bulk work.
- Scryfall's artist credit can be shorter than the official caption ('Heonhwa' vs 'Heonhwa Choe'). The review records this rather than hiding it.
- The ask router had a relation-name gap: claim packs use `killed`, while the router looked only for `destroyed`. It now falls back through a chain of relation names.
- Coverage: the official story for 23 arcs (KLD/AER, AKH/HOU, XLN/RIX, EOE, RF, …) is entirely uncited by any claim pack. This is the main Phase 5 gap.

### Blockers
- Owner review is still needed for Pilots 1–3 and the 4 unapplied Pack A proposals. Every lore deck and pack is still UNAPPROVED or PRELIMINARY_RESEARCH.
- `trk`/`trc` admission waits until after 2026-11-13.
- Readiness: NOT_RELEASE_READY. The NOT_MET item is owner review of a graph-built deck.

### Next steps (value order)
1. Phase 5 not-started arcs, driven by the coverage inventory. Start with KLD/AER (17 pages), XLN/RIX (17) and AKH/HOU (16) as targeted claim packs with verbatim quotes.
2. Exhaustive passes over the RtD, ONE and MOM episodes and the uncited Planeswalker's Guide to MOM. C2, C3 and C4 are targeted, not exhaustive.
3. Use the FRA image-label collector numbers to add printing-specific art links for other Reality Fracture legends.
4. A broader Phase 7 hard-query suite that runs the ask router over every claim-pack predicate.
5. Investigate the flaky snapshot test.

Store copies were skipped per the owner. Protected-path check `git diff --stat dfc8891d origin/main -- grixis/ data/grixis/ state/current_deck_overrides.json data/lore_decks/approvals/`: **empty** (run after #856 merged, main `67dc7a75`).

## Batch 5 — 2026-10-30 04:43–~05:15 CDT (final)

Owner request: build a reusable bulk claim-pack pipeline for the uncited Phase 5 arcs (KLD/AER, XLN/RIX, AKH/HOU, then others), check every quote word-for-word, grade conservatively and mark everything PRELIMINARY_RESEARCH. Also do the Reality Fracture collector-number links, the broader Phase 7 relation tests and the flaky-test fix where cheap.

### PRs (batch 5)
| PR | Phase | What | Merge (CDT) | CI on the exact head |
|---|---|---|---|---|
| [#858](https://github.com/corymstover/GrokBotMTGCompanion/pull/858) | 5/3 | `scripts/story_claim_pipeline.py` (spec → pack + self-hashed audit, verbatim/grade/limitation/page gates, cache-free `check` in CI). KLD/AER: 25 claims, 29/29 quotes. XLN/RIX: 16 claims, 23/23 quotes. AKH/HOU: 17 claims, 23/23 quotes. 12 pipeline tests. Snapshot test hardened. Workflow v2.32 | `681bd3b4` (04:58) | 26/26 pass |
| [#859](https://github.com/corymstover/GrokBotMTGCompanion/pull/859) | 7 | `tests/test_mv_ask_relations.py`: every claim edge (256 at the time) round-trips through `mv_ask` lore with its grade and source, confidence never overstates the grade, and IMPLIED/DISPUTED/OPEN claims carry limitations. Natural-language questions are checked too. Router fallbacks: `created ← designed/invented`, `defeated_by ← defeated` | `0e199c14` (05:03) | 3/3 pass |
| [#860](https://github.com/corymstover/GrokBotMTGCompanion/pull/860) | 2/1B | Story image-label → printing links: 577 labels on 57 pages. 570 MATCHED (560 printings); FRA 159/160 (146 fra + 13 frc commander companion). 6 NAME_MISMATCH and 1 NO_PRINTING are kept unresolved. Agrees with the Koth leads (#199, #248). 7 tests | `aeb80393` (05:07) | 5/5 pass |
| [#861](https://github.com/corymstover/GrokBotMTGCompanion/pull/861) | 5 | NEO claim pack: 12 claims, 19/19 quotes verbatim, 6 pages (episodes 1–5 + Planeswalker's Guide). 9 CONFIRMED and 3 IMPLIED, each with a limitation. NEO→`neo` set anchors. Graph 1,241 nodes / 1,966 edges | `67a946d7` (05:11) | 7/7 pass |

Local full suite: 395 tests OK (#858), 402 (#860 branch), 411 OK on the merged NEO branch.

### Status (keep distinct)
- **Research:** the 4 new packs (KLD/AER, XLN/RIX, AKH/HOU, NEO) are PRELIMINARY_RESEARCH. They are targeted, not exhaustive, not owner approved and not certified.
- **Tests:** green locally and in CI on each exact head.
- **Merged:** #858–#861.
- **Owner approved / certified:** nothing new.

### Discoveries
- Coverage after NEO: 94 of 626 pages cited, 243 claims, 2 arcs fully cited, 12 partial and 19 not started.
- Image-label set codes do not always match Scryfall. OTJ-labelled "Loot" art is printed in `big`, and a BLB Dragonhawk label (#135) is #132 in Scryfall. These are recorded as NAME_MISMATCH.
- Commander precon labels (`Cmdr*`/`Comm*`) resolve to the "<set> Commander" companion set. The snapshot's default-cards has no `parent_set_code`, so the set is derived from `set_name`, and a number+name match is still required.
- The graph grows with art-caption card nodes as packs cite new pages. The ALT and coverage count tests pin these numbers.
- Flaky snapshot test: hardened in #858, but the root cause was **not** reproduced, so treat it as mitigated, not proven fixed.
- Jin-Gitaxias's fate in NEO episode 5 is deliberately not claimed: he is badly wounded but appears alive in the epilogue.

### Blockers
Unchanged: owner review of Pilots 1–3 and the Pack A proposals; `trk`/`trc` admission after 2026-11-13; readiness NOT_RELEASE_READY.

### Next steps
1. More Phase 5 arcs via the pipeline: MID/VOW, SNC, then EOE, RF and other not-started arcs. Add the missing pages of the partial arcs (KLD/AER 3, XLN/RIX 7, AKH/HOU 9).
2. Resolve the 6 image-label NAME_MISMATCH entries by owner/editorial review, and use the 570 matched labels as printing-specific art evidence in enrichment records.
3. A Phase 7 free-text paraphrase suite beyond the relation round-trip.

Store copies were skipped per the owner.

## Batch 6 — 2026-10-30, merges 05:28–06:24 CDT

Owner request: finish #867 (KHM, STX, IKO) and ship THB; write this handoff section and bump the workflow; keep extending Phase 5 (not-started arcs first, then the missing pages of partial arcs, several packs per PR); commit the spec generator scripts so nothing lives only on the box.

### PRs (batch 6)
| PR | Phase | What | Merge commit (CDT) | CI on the exact head |
|---|---|---|---|---|
| [#863](https://github.com/corymstover/GrokBotMTGCompanion/pull/863) | 5 | MID/VOW 12 claims (25 quotes), SNC 16 (31), EOE 17 (31); pipeline sentences helper | `16b51c0c` (05:28) | 8/8 pass on `a77ba4b1` |
| [#864](https://github.com/corymstover/GrokBotMTGCompanion/pull/864) | 5 | RF 13 (26), WOE 14 (28), MKM 14 (23); page-key collision gate | `6cbf9d99` (05:38) | 8/8 pass on `74e65010` |
| [#865](https://github.com/corymstover/GrokBotMTGCompanion/pull/865) | 5 | BLB 12 (19), DSK 11 (17), OTJ 12 (20), LCI 12 (18), DFT 12 (17); entity alias gate | `284a43c0` (05:51) | 8/8 pass on `5ee82d41` |
| [#866](https://github.com/corymstover/GrokBotMTGCompanion/pull/866) | 7 | `tests/test_mv_ask_rephrased.py` rephrased-question suite + `mv_ask` synonym routes | `44446b26` (06:01) | 3/3 pass on `633d0856` |
| [#867](https://github.com/corymstover/GrokBotMTGCompanion/pull/867) | 5 | KHM 14 (19), STX 11 (17), IKO 5 (7). Branch updated from main by a normal merge after #866; rebuild produced no artifact diff | `e983da31` (06:11) | 7/7 pass on `538df47d` |
| [#868](https://github.com/corymstover/GrokBotMTGCompanion/pull/868) | 5 | THB 14 (18), THS 20 (22, the three Theros Planeswalker's Guides), MAT 12 (17), ELD 11 (12, Planeswalker's Guide to Eldraine). Adds `scripts/claim_spec_sources/` (generator for every Phase 5 spec plus `rebuild.sh`) | `9c68bfac` (06:19) | 8/8 pass on `95277b76` |
| [#869](https://github.com/corymstover/GrokBotMTGCompanion/pull/869) | 5 | SOS 17 (22: Legends page, Planeswalker's Guide, Episode 6), SOI/EMN 9 (14: I Am Avacyn, Campaign of Vengeance, Innistrad's Last Hope, The Promised End) | `37c91a45` (06:24) | 8/8 pass on `7d446b9b` |

Every merge was a normal merge with `--match-head-commit`; no force-push and no admin bypass. Local suites on the #869 head: `tests/` 419 OK, `scripts/` 18 OK.

### Checklist
- [x] #867 green on its exact head and merged
- [x] THB shipped (#868)
- [x] Spec generator scripts committed (`scripts/claim_spec_sources/`); re-running the older scripts reproduces the committed specs byte-for-byte. KLD/XLN/AKH/NEO specs predate the scripts and have no generator
- [x] Every arc in the inventory now has at least one cited page
- [ ] Partial arcs filled (26 still partial)
- [ ] Owner review of any Phase 5 pack (none requested or given)

### Coverage (generated, `story_coverage_inventory_2026-10-30.json` on main after #869)
- 195 of 626 pages cited (94 after Batch 5; 179 after #867). 33 arcs: 0 not started, 26 partial, 7 all pages cited. 501 graph claims.
- Claim anchors: 452 of 501 claims anchored, 2,131 anchors (ART_IN_CITED_SOURCE 34, PRINTED_IN_STORY_SET 347, NAMED_PARTICIPANT 1,750).
- Largest gaps: untagged 17/305, SOI/EMN 5/21, BFZ/OGW 3/19, EOE 6/18, AKH/HOU 7/16, TDM 2/14, SOS 3/14, ECL 1/12, RF 5/12, BRO 4/10.

### Status (keep distinct)
- **Research:** all 24 `pack_p5_*` packs are PRELIMINARY_RESEARCH: targeted, not exhaustive.
- **Tests:** green locally and in CI on each exact head.
- **Merged:** #863–#869.
- **Owner approved / certified:** nothing new. No approval boxes were checked.

### Discoveries
- Entity types must match across packs: `zhalfir` is `Place` in C2/C4, so a `Plane` typing in MAT failed the graph's consistency check until aligned.
- Spark loss after March of the Machine is modelled as `lost_spark_after` → `mom_invasion` (Teferi, Koth, Nissa, Nahiri) rather than overloading `spark_ignited`/`gave_up`.
- ELD has only the Planeswalker's Guide in the cached inventory, and that guide is an in-universe traveller's account. Its claims carry that limitation where they rest on what the realm's folk believe.
- SOS Episode 6: Tam pushes Jadzi into the not-snarl and says "I was made to do this." Tam's maker and Jadzi's fate are deliberately left unclaimed.
- The SOS set (April 2026) may have few printings in the offline snapshot, so SOS claims anchor mostly by name.

### Blockers
Unchanged: owner review of Pilots 1–3 and the Pack A proposals; `trk`/`trc` admission after 2026-11-13; readiness NOT_RELEASE_READY.

### Next steps
1. Fill the partial arcs through `scripts/claim_spec_sources/` + `rebuild.sh`: SOI/EMN (16 pages left), BFZ/OGW, EOE, TDM, SOS episodes 1–5 and side stories, ECL, then the untagged 288.
2. Resolve the 6 image-label NAME_MISMATCH entries (owner/editorial), then use the matched labels as printing evidence.
3. A Phase 7 free-text paraphrase suite over the new Batch 6 relations.

Protected-path check: `git diff --stat dfc8891d origin/main -- grixis/ data/grixis/ state/current_deck_overrides.json data/lore_decks/approvals/` is empty after #869.

## Batch 7 — 2026-10-30, merges 06:53–07:18 CDT

Owner request: bulk-close the partial arcs and triage the untagged pages; commit a generating spec script for every pack (including the older KLD/AER, XLN/RIX, AKH/HOU and NEO specs); keep the handoff current because workers are interrupted every 45–60 minutes.

### PRs (batch 7)
| PR | Phase | What | Merge commit (CDT) | CI on the exact head |
|---|---|---|---|---|
| [#871](https://github.com/corymstover/GrokBotMTGCompanion/pull/871) | 5 | Bulk fills: SOI/EMN 21/21, EOE 18/18, AKH/HOU 16/16, SOS 14/14 (29 claims), RF 12/12 (21 claims). New packs: BFZ/OGW (19/19 pages at the time), TDM 14/14, ECL 12/12 (18 claims), BRO extension (`pack_p5_brothers_war`, 9 claims, BRO 10/10). Generating spec scripts for KLD/AER, XLN/RIX, AKH/HOU and NEO plus `tests/test_claim_spec_sources.py` (every spec regenerates byte-for-byte) | `f1735276` (06:53) | 8/8 pass on `b08d1359` |
| [#872](https://github.com/corymstover/GrokBotMTGCompanion/pull/872) | 5 | 78 untagged pages tagged to arcs via exact-slug alternatives in `scripts/build_primary_sources.py` (only the `arc` column of `data/primary_sources.csv` changed; title-prefix or ≥2 plane/locale mentions inside the set's release window). Side-story packs: ONE 6, MOM 8, OTJ 8, DSK 6, MKM 1, SNC 5, DMU 5 claims. Weak/ambiguous pages deliberately left untagged | `80c4caf7` (07:15) | 8/8 pass on `feef0181` |
| [#873](https://github.com/corymstover/GrokBotMTGCompanion/pull/873) | 5 | Closes BFZ/OGW (27/27, new `pack_p5_bfz_2015_stories`), DMU (`pack_p5_dominaria_united`), NEO (`pack_p5_neo_side_stories`), DSK, MKM and MOM (Planeswalker's Guide to MOM). Branch updated from main by a normal merge | `676ea40d` (07:18) | 6/6 pass on `8448a3c9` |

Every merge was a normal merge with `--match-head-commit`; no force-push and no admin bypass. Local suites on the #873 head: `tests/` 420 OK, `scripts/` 18 OK, `rebuild.sh` checks all ok.

### Checklist
- [x] Generating spec script for every Phase 5 pack, including KLD/AER, XLN/RIX, AKH/HOU and NEO, with a byte-for-byte regeneration test
- [x] 78 untagged pages triaged into arcs, with an evidence rule; ambiguous pages left untagged
- [x] #873 green on its exact head and merged
- [ ] Partial arcs filled (13 still partial)
- [ ] Untagged pages packed (210 of 227 still uncited)
- [ ] Phase 7 free-text paraphrase suite over the Batch 6/7 relations (next)
- [ ] Owner review of any Phase 5 pack (none requested or given)

### Coverage (generated, `story_coverage_inventory_2026-10-30.json` on main after #873)
- 350 of 626 pages cited (195 after Batch 6). 33 arcs: 0 not started, 13 partial, 20 all pages cited. 711 graph claims, 47 claim packs.
- Graph: 2,887 nodes, 4,537 edges, 0 problems.
- Claim anchors: 628 of 711 claims anchored, 2,902 anchors (ART_IN_CITED_SOURCE 62, PRINTED_IN_STORY_SET 468, NAMED_PARTICIPANT 2,372).
- Still partial: BLB 6/8, DFT 6/10, DOM/WAR 12/18, IKO 1/3, KHM 6/13, KLD/AER 14/17, LCI 7/8, MID/VOW 8/19, STX 5/11, THB 1/4, THS 5/19, XLN/RIX 10/17, untagged 17/227.

### Status (keep distinct)
- **Research:** every `pack_p5_*` pack is PRELIMINARY_RESEARCH: targeted, not exhaustive.
- **Tests:** green locally and in CI on each exact head.
- **Merged:** #871–#873.
- **Owner approved / certified:** nothing new. No approval boxes were checked.

### Discoveries
- TDM episodes 6/7 use page keys `tdm_e6`/`tdm_e7` because `pack_a5_ugin_allies` already owns `tdm_ep6`/`tdm_ep7` with a different source kind, so that URL has two source nodes.
- Word counts in `primary_sources.csv` drift when the cache is rescanned, so the triage changed only the `arc` column.
- Re-tagging moves pages between buckets: BFZ/OGW fell back to PARTIAL (19/27) after the 2015 side stories were tagged, until #873 packed them.
- `STORY_SETS` should list a pack only where its participants have printings in the set; otherwise PRINTED_IN_STORY_SET is 0 (MOM and DSK side packs are left out).

### Blockers
Unchanged: owner review of Pilots 1–3 and the Pack A proposals; `trk`/`trc` admission after 2026-11-13; readiness NOT_RELEASE_READY.

### Next steps
1. Close the 12 remaining partial arcs (smallest gaps first: LCI, BLB, IKO, THB, KLD/AER, DFT, DOM/WAR, STX, XLN/RIX, KHM, MID/VOW, THS).
2. Pack untagged pages in bulk, and keep tagging only where the evidence rule holds.
3. Phase 7 free-text paraphrase suite over the new relations; re-run release readiness and Phase 8 checks.

Protected-path check: `git diff --stat dfc8891d origin/main -- grixis/ data/grixis/ state/current_deck_overrides.json data/lore_decks/approvals/` is empty after #873 (main `676ea40d`).

## Batch 8 — 2026-10-30, from 07:20 CDT (updated early; Phase 7 PR open)

### PRs (batch 8)
| PR | Phase | What | Merge commit (CDT) | CI on the exact head |
|---|---|---|---|---|
| [#875](https://github.com/corymstover/GrokBotMTGCompanion/pull/875) | 5 | Closes LCI, BLB, THB, KLD/AER, DFT, XLN/RIX and DOM/WAR (new `pack_p5_war_spark_ravnica`); adds `scripts/claim_spec_sources/patch_spec.py` | `35392813` 07:37 CDT | 8/8 pass on `1c2937cb` |
| [#876](https://github.com/corymstover/GrokBotMTGCompanion/pull/876) | 5 | Closes KHM (+10 claims) and STX (+8) | `1fb8b782` 07:42 CDT | 8/8 pass on `754c875c` |
| [#877](https://github.com/corymstover/GrokBotMTGCompanion/pull/877) | 5 | Closes MID/VOW (+13) and THS (+17); handoff | `111fd90a` 07:48 CDT | 8/8 pass on `9a9cf337` |
| this branch (`grokbot-p7-paraphrase-b8-20261030`) | 7/8 | Batch 8 paraphrase suite + router phrasings; refreshed readiness report; workflow v2.36 | open | pending |

### Coverage (on main after #877)
- 414 of 626 pages cited (350 after Batch 7). 31 of 33 arcs have every page cited. 838 claims.
- Still partial: IKO 1/3 (the 2 uncited pages have no lore content, so they need a reviewed-no-claim marker rather than a claim), untagged 17/227.

### Status (keep distinct)
- **Research:** PRELIMINARY_RESEARCH. **Tests:** green locally and in CI on each exact head. **Merged:** #875, #876, #877. **Owner approved / certified:** nothing.

### Next steps
### Phase 7 (this branch)
- `tests/test_mv_ask_rephrased_b8.py`: 27 cases, 42 phrasings; 5 CANON_IMPLIED cases must be QUALIFIED with a limitation; 8 nonsense-entity probes must stay NOT_FOUND.
- `scripts/mv_ask.py`: a relation filter may be `a|b`; new phrasings beheaded, the leader of X, governs/rules, mentored / X's mentor, founded, guards, fought, serves, worships, attacked, who did X meet; "X's friends" also reads friend_of/childhood_friend_of (Zimone's friend now reaches SX012 Amaka as well as SS008).
- Discovery: faction short names ("Who leads the Izzet?") do not resolve to the faction node; not faked.
- Tests: 424 OK in `tests/`, 18 OK in `scripts/`.

### Phase 8 re-run (07:5x CDT, on this branch)
- `release_readiness.py`: **NOT_RELEASE_READY** — MET 2, PARTIAL 2, NOT_MET 1, EXTERNAL 2 (unchanged statuses). NOT_MET: no graph-built lore deck has owner review (3 drafts await review). Committed report refreshed: graph stats now 3305 nodes / 5224 edges; claims 664 CONFIRMED, 163 IMPLIED, 7 DISPUTED, 2 ALTERNATE_CONTINUITY, 2 OPEN_QUESTION.
- `phase8_status.py --json`: 5362 enrichment records; `rebuild_enrichment.sh --plan`: every bucket 100%, 0 remaining. Phase 8 tests (release_readiness, phase8_batch38, enrichment_story_links_b4) OK.

### Next steps
Untagged pages in bulk (210 uncited); IKO's 2 non-narrative pages need a reviewed-no-claim marker (owner decision on format); faction short-name aliases in mv_ask; owner review of the 3 graph-linked lore deck drafts (the only NOT_MET readiness criterion).
