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
| [#848](https://github.com/corymstover/GrokBotMTGCompanion/pull/848) | 8 | Enrichment batch 38: the remaining **1,953** priority-pool cards, so **5,362/5,362**. The 3,409 earlier records are byte-identical. 664 new records carry lore links; 1,289 are honestly marked "no lore linked yet". Readiness: enrichment MET. 346 tests | `f65fe727` (03:53) | 23/23 pass |

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
