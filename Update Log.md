---
title: "Update Log"
category: meta
tags: [changelog]
issues: []
generated_by: hand-written
sources: []
related: ["Contradictions & Retcons Log.md", "Planeswalker Dossiers.md", "Items & Artifacts Index.md", "Lore Primary Sources.md", "Planes Index.md", "EDH Deck Evaluation Checklist.md"]
schema: 2
---

# Update Log

> Every update records **date · summary · files affected · reason**. Newest first. See [Knowledge Index](Knowledge%20Index.md#maintenance-rules).

## Contents
- [2026-10-16 — Bot cycle 58 (M1: interaction edges for M4; source attestation coverage)](#2026-10-16--bot-cycle-58-m1-interaction-edges-for-m4-source-attestation-coverage)
- [2026-10-16 — Bot cycle 57.3 (M3: paired champion-vs-challenger tests)](#2026-10-16--bot-cycle-573-m3-paired-champion-vs-challenger-tests)
- [2026-10-16 — Bot cycle 57.2 (M3: goldfish simulator core)](#2026-10-16--bot-cycle-572-m3-goldfish-simulator-core)
- [2026-10-16 — Bot cycle 57.1 (M3: evidence layer)](#2026-10-16--bot-cycle-571-m3-evidence-layer)
- [2026-10-16 — Bot cycle 56 (phase 2 / M1: batch F)](#2026-10-16--bot-cycle-56-phase-2--m1-batch-f)
- [2026-10-16 — Bot cycle 55 (M2: commander blueprints, batch 4; Norman Osborn registry id)](#2026-10-16--bot-cycle-55-m2-commander-blueprints-batch-4-norman-osborn-registry-id)
- [2026-10-16 — Bot cycle 54 (phase 2 / M1: batch E)](#2026-10-16--bot-cycle-54-phase-2--m1-batch-e)
- [2026-10-16 — Bot cycle 53 (M2: commander blueprints, batch 3; EDH Packages deck labels)](#2026-10-16--bot-cycle-53-m2-commander-blueprints-batch-3-edh-packages-deck-labels)
- [2026-10-16 — Bot cycle 52 (M2: commander blueprints, batch 2)](#2026-10-16--bot-cycle-52-m2-commander-blueprints-batch-2)
- [2026-10-16 — Bot cycle 51 (phase 2 / M1: batch D)](#2026-10-16--bot-cycle-51-phase-2--m1-batch-d)
- [2026-10-16 — Bot cycle 50 (M2: commander blueprints, batch 1; M0 accepted)](#2026-10-16--bot-cycle-50-m2-commander-blueprints-batch-1-m0-accepted)
- [2026-10-16 — Bot cycle 49 (phase 2 / M1: batch C; M0 follow-ups)](#2026-10-16--bot-cycle-49-phase-2--m1-batch-c-m0-follow-ups)
- [2026-10-16 — Bot cycle 48 (phase 2 / M1: Spellbook step cache, batch B)](#2026-10-16--bot-cycle-48-phase-2--m1-spellbook-step-cache-batch-b)
- [2026-10-16 — Bot cycle 47 (M0: Grixis authority foundation)](#2026-10-16--bot-cycle-47-m0-grixis-authority-foundation)
- [2026-10-16 — Bot cycle 46 (phase 2: interaction reviews, tooling + batch A)](#2026-10-16--bot-cycle-46-phase-2-interaction-reviews-tooling--batch-a)
- [2026-10-16 — Bot cycle 45 (full Grixis source archive, single source of truth)](#2026-10-16--bot-cycle-45-full-grixis-source-archive-single-source-of-truth)
- [2026-10-16 — Bot cycle 44 follow-up (pending legality date → 2026-11-13)](#2026-10-16--bot-cycle-44-follow-up-pending-legality-date--2026-11-13)
- [2026-10-16 — Bot cycle 44 (Grixis refinement batch 6: the 2 pending decks)](#2026-10-16--bot-cycle-44-grixis-refinement-batch-6-the-2-pending-decks)
- [2026-10-16 — Bot cycle 43 (Grixis refinement batch 5, end-of-cycle summary, v2.5-grixis-refinement)](#2026-10-16--bot-cycle-43-grixis-refinement-batch-5-end-of-cycle-summary-v25-grixis-refinement)
- [2026-10-16 — Bot cycle 42 (Grixis refinement batch 4)](#2026-10-16--bot-cycle-42-grixis-refinement-batch-4)
- [2026-10-16 — Bot cycle 41 (Grixis refinement batch 3, hand-picked swaps, hand reviews)](#2026-10-16--bot-cycle-41-grixis-refinement-batch-3-hand-picked-swaps-hand-reviews)
- [2026-10-16 — Bot cycle 40 (Grixis refinement: power guard, batch-1 re-check, batch 2)](#2026-10-16--bot-cycle-40-grixis-refinement-power-guard-batch-1-re-check-batch-2)
- [2026-10-16 — Bot cycle 39 (Grixis commander-first refinement, batch 1)](#2026-10-16--bot-cycle-39-grixis-commander-first-refinement-batch-1)
- [2026-10-16 — Bot cycle 38 (Grixis: 62/62 pages, 2 pending legality)](#2026-10-16--bot-cycle-38-grixis-6262-pages-2-pending-legality)
- [2026-10-16 — Bot cycle 37 (Grixis re-analysis)](#2026-10-16--bot-cycle-37-grixis-re-analysis)
- [2026-10-16 — Bot cycle 36 (Phase 8: Legends evidence, audit pass 2, batch 4 partial)](#2026-10-16--bot-cycle-36-phase-8-legends-evidence-audit-pass-2-batch-4-partial)
- [2026-10-15 — Bot cycle 35 (Phase 8: story cache, name-match audit, batch 3)](#2026-10-15--bot-cycle-35-phase-8-story-cache-name-match-audit-batch-3)
- [2026-10-15 — Bot cycle 34 (Phase 8: batch 2, package back-links, atomic writes)](#2026-10-15--bot-cycle-34-phase-8-batch-2-package-back-links-atomic-writes)
- [2026-10-15 — Bot cycle 33 (Phase 8: card enrichment format + batch 1)](#2026-10-15--bot-cycle-33-phase-8-card-enrichment-format--batch-1)
- [2026-10-15 — Bot cycle 32 (Phase 7 complete: lore cross-refs, story maps, rules quote checks)](#2026-10-15--bot-cycle-32-phase-7-complete-lore-cross-refs-story-maps-rules-quote-checks)
- [2026-10-15 — Bot cycle 31 (Phase 7: lore retrieval + validation)](#2026-10-15--bot-cycle-31-phase-7-lore-retrieval--validation)
- [2026-10-15 — Bot cycle 30 (Phase 6: final dossiers, status, snapshot)](#2026-10-15--bot-cycle-30-phase-6-final-dossiers-status-snapshot)
- [2026-10-15 — Bot cycle 29 (Phase 6: dossiers, Omenpath-era planes, items)](#2026-10-15--bot-cycle-29-phase-6-dossiers-omenpath-era-planes-items)
- [2026-10-15 — Bot cycle 28 (Phase 6: dossiers, items, planes, retcons)](#2026-10-15--bot-cycle-28-phase-6-dossiers-items-planes-retcons)
- [2026-10-15 — Bot cycle 27 (Phase 6: dossiers, items, planes, spark refresh)](#2026-10-15--bot-cycle-27-phase-6-dossiers-items-planes-spark-refresh)
- [2026-10-15 — Bot cycle 26 (Phase 6: dossiers, planes, items index)](#2026-10-15--bot-cycle-26-phase-6-dossiers-planes-items-index)
- [2026-10-15 — Bot cycle 25 (Phase 6: last six arcs, episode upgrades, dossiers)](#2026-10-15--bot-cycle-25-phase-6-last-six-arcs-episode-upgrades-dossiers)
- [2026-10-15 — Bot cycle 24 (Phase 6: newest arcs, pre-2019 arcs, dossiers)](#2026-10-15--bot-cycle-24-phase-6-newest-arcs-pre-2019-arcs-dossiers)
- [2026-10-15 — Bot cycle 23 (lore decks: 85% standard incl. lands)](#2026-10-15--bot-cycle-23-lore-decks-85-standard-incl-lands)
- [2026-10-15 — Bot cycle 22 (Phase 6: primary-source ingestion & thin arcs)](#2026-10-15--bot-cycle-22-phase-6-primary-source-ingestion--thin-arcs)
- [2026-10-15 — Bot cycle 21 (Phase 6: lore-themed deckbuilding)](#2026-10-15--bot-cycle-21-phase-6-lore-themed-deckbuilding)
- [2026-10-15 — Bot cycle 20 (Phase 6: lore deepening — timeline & arcs, retcon log)](#2026-10-15--bot-cycle-20-phase-6-lore-deepening--timeline--arcs-retcon-log)
- [2026-10-15 — Bot cycle 19 (Phase 5 complete: bracket calibration & pilot notes)](#2026-10-15--bot-cycle-19-phase-5-complete-bracket-calibration--pilot-notes)
- [2026-10-15 — Bot cycle 18 (Phase 5: cross-references)](#2026-10-15--bot-cycle-18-phase-5-cross-references)
- [2026-10-15 — Bot cycle 17 (Phase 5: schema v2, retrieval index, validate_all)](#2026-10-15--bot-cycle-17-phase-5-schema-v2-retrieval-index-validate_all)
- [2026-10-15 — Bot cycle 16 (Grixis integration)](#2026-10-15--bot-cycle-16-grixis-integration)
- [2026-10-15 — Bot cycle 15 (Phase 4 complete; duplicate cleanup)](#2026-10-15--bot-cycle-15-phase-4-complete-duplicate-cleanup)
- [2026-10-15 — Bot cycle 14 (Phase 4: Lookup Guide)](#2026-10-15--bot-cycle-14-phase-4-lookup-guide)
- [2026-10-15 — Bot cycle 13 (Phase 3 complete: Artist Index)](#2026-10-15--bot-cycle-13-phase-3-complete-artist-index)
- [2026-10-15 — Bot cycle 12 (Phase 3: Tokens, Emblems & Dungeons)](#2026-10-15--bot-cycle-12-phase-3-tokens-emblems--dungeons)
- [2026-10-15 — Bot cycle 11 (Phase 3: Format Legality Matrix)](#2026-10-15--bot-cycle-11-phase-3-format-legality-matrix)
- [2026-10-15 — Bot cycle 10 (Phase 3: Printing History)](#2026-10-15--bot-cycle-10-phase-3-printing-history)
- [2026-10-15 — Bot cycle 9 (Phase 3: Keyword Encyclopedia complete)](#2026-10-15--bot-cycle-9-phase-3-keyword-encyclopedia-complete)
- [2026-10-15 — Bot cycle 8 (Phase 2 complete; Phase 3 keyword encyclopedia started)](#2026-10-15--bot-cycle-8-phase-2-complete-phase-3-keyword-encyclopedia-started)
- [2026-10-15 — Bot cycle 7 (Phase 1 complete; Phase 2 lore depth started)](#2026-10-15--bot-cycle-7-phase-1-complete-phase-2-lore-depth-started)
- [2026-10-15 — Bot cycle 6 (ROADMAP Phase 1: EDH & deckbuilding depth)](#2026-10-15--bot-cycle-6-roadmap-phase-1-edh--deckbuilding-depth)
- [2026-10-15 — Bot cycle 5 (sprint: rules topics, remaining planes, story archive, maintenance)](#2026-10-15--bot-cycle-5-sprint-rules-topics-remaining-planes-story-archive-maintenance)
- [2026-10-15 — Bot cycle 4 (sprint: rules topics, Planeswalker review, ELD/THB/IKO sources, combos & archetypes)](#2026-10-15--bot-cycle-4-sprint-rules-topics-planeswalker-review-eldthbiko-sources-combos--archetypes)
- [2026-10-15 — Bot cycle 3 (sprint: lore deepening, all-identity EDH, rules interactions)](#2026-10-15--bot-cycle-3-sprint-lore-deepening-all-identity-edh-rules-interactions)
- [2026-10-15 — Bot cycle 2 (rulings, Planes, EDH staples, Characters)](#2026-10-15--bot-cycle-2-rulings-planes-edh-staples-characters)
- [2026-10-15 — Bot cycle 1 (repository bootstrap)](#2026-10-15--bot-cycle-1-repository-bootstrap)

## 2026-10-16 — Bot cycle 58 (M1: interaction edges for M4; source attestation coverage)
- **Edges:** every M1 review now emits machine-readable edges, in `data/grixis_interactions/edges/<slug>.json` (62/62, 4,086 edges). Schema: `data/grixis/schemas/interaction_edges.schema.json`. Rule `edges-v1`:
  - each ruling is a hub node (`combo:` / `interaction:`);
  - each card it names gets a membership edge to the hub (`piece_of` / `member_of`, the same kinds as `graph.schema.json`);
  - each other card gets a pair edge to the ruling's anchor, which is the commander when the ruling names one (`combo_with` / `interacts_with` / `conflicts_with`, `derived_metric`);
  - optional authored edges (graph kinds) replace a ruling's pair edges.
  Every edge carries the ruling id, status, flag kind, CR cites and evidence refs, and the file records the deck and review hashes. `--check` regenerates the files and fails on drift, schema errors, a ruling without a hub or a review without pair edges. 9 new unit tests are in `tests/test_interaction_edges.py`.
- **Source attestations:** all 518 items in the archived `*_Rules_Attestation.json` files are now accounted for, and `--check` enforces it: 515 folded in, 3 dispositioned, 0 missing. Three were folded in:
  - new azula-12: Samut's split second doesn't stop Azula's trigger or copy (CR 702.61b, 707.10);
  - gwendlyn-05 extended: Tinybones's enters discard feeds the payoffs;
  - new inalla-10: a Kefka token copy gives two enters triggers before the legend rule (CR 704.5j).
  Three were dispositioned with reasons in `data/grixis_interactions/_attestation_dispositions.json`: Final Fortune exclusion (not in Azula's list), and Lynde's and Mai and Zuko's color identity (checked by the `decks` step). Overall: 594 rulings.
- **Evidence:** rebuilt only the M3 evidence snapshots made stale by this cycle's review and deck-page changes (derived files only).
- **M1:** criteria 1–5 are met (status in [Authority Model](grixis/Grixis%20Authority%20Model.md#m1)). M1 acceptance is not recorded; that is Cory's.
- **Not touched:** `data/grixis/registry*`, blueprints, existing schemas, `grixis_refine.py`, exception data and simulator code. No decklist changed.
- **Files:** `scripts/grixis_interactions.py`, `data/grixis/schemas/interaction_edges.schema.json` (new), `data/grixis_interactions/edges/` (new), `_attestation_dispositions.json` (new), 3 reviews, rendered pages, `tests/test_interaction_edges.py`, `grixis/interactions/README.md`, `grixis/Grixis Authority Model.md`, `README.md`, `data/grixis/evidence/` (stale snapshots), `data/kb_index.json`.

## 2026-10-16 — Bot cycle 57.3 (M3: paired champion-vs-challenger tests)
- **`scripts/grixis_paired.py`:** aligned libraries; both lists get the same shuffles and mulligan reshuffles on identical seeds.
  - The metrics and thresholds were pre-registered before any run (`PREREG`): primary is mana spent on turns 1–6, threshold 0.25. CI95s come from the per-game differences; the verdict rule is fixed.
  - Records validate against `test.schema.json`, with limitations in every record.
- **6 records** in `data/grixis/tests/`, one per registered GrokBot v1 challenger (Abaddon, Kefka, Nicol Bolas, Norman Osborn, Sol'kanar the Swamp King, The Rani; 2,000 paired games each).
  - Every primary is `inconclusive`: a detectable curve shift of −0.09 to +0.07 mana, below the threshold.
  - Every secondary shows no detectable difference.
  - The goldfish can't see card draw, interaction or commander triggers, which is what these swaps are for. The records are evidence and decide nothing.
- **Caching and checks:** records are keyed by list hashes + simulator sha + seed + samples + pre-registration. The new `validate_all` step `paired-tests` (23 steps) checks schema, freshness, the verdict rule and an exact re-run. `tests/test_paired.py` adds 6 tests.
- **Unchanged:** no decklist or interaction file was touched; M2 is still waiting for Cory; Tresserhorn's Lord stays `PENDING_RELEASE`.

## 2026-10-16 — Bot cycle 57.2 (M3: goldfish simulator core)
- **`scripts/grixis_sim.py` v1.0:** deterministic goldfish games on the canonical lists. The model:
  - an exact hypergeometric layer, plus an exact DP for a land drop every turn;
  - London mulligan with the multiplayer free first mulligan (CR 103.5, 103.5c) and no turn-1 draw skip in multiplayer (103.8c);
  - mana and colours by bipartite pip matching, commander tax;
  - metrics: commander turn, curve (mana available and spent by turn), first access to each blueprint package and to the tutor targets, Spellbook combo assembly, and a win-turn proxy that is never a win rate.
- **Exact-math checks:** the new `validate_all` step `simulator` (22 steps) checks 4 Monte Carlo values against exact math on Wick's list, each within 4 standard errors. `tests/test_simulator.py` adds 12 tests.
- **Smoke run:** all 62 decks load and simulate (62 × 200 games in about 5 s). The model's limits are listed in [the Authority Model, M3 criterion 5](grixis/Grixis%20Authority%20Model.md#m3); every test record will carry them.
- **Unchanged:** no decklist or interaction file was touched; M2 is still waiting for Cory; Tresserhorn's Lord stays `PENDING_RELEASE`.

## 2026-10-16 — Bot cycle 57.1 (M3: evidence layer)
- **M3 started** (`program.milestones.M3: in_progress`). The plan is five checkpointed sub-cycles: 57.1 evidence layer, 57.2 simulator core, 57.3 paired test records, 57.4 stress scenarios, 57.5 knowledge pages. The 9 numbered criteria are in [the Authority Model](grixis/Grixis%20Authority%20Model.md#m3).
- **Evidence vectors** (`scripts/grixis_evidence.py`, `data/grixis/evidence/<slug>.json`, schema `evidence_vector.schema.json`): 62 decks, 17,712 vectors. That is every canonical-list card plus every EDHREC candidate on the deck's page that fits the colour identity and isn't a basic land. They expand to 27,986 schema-valid evidence items: 16,824 `derived_metric`, 7,293 `heuristic`, 1,569 `strategic_judgment`, 1,376 `fact`.
- **EDHREC handling:**
  - EDHREC is never above `moderate`. It is `low` for small samples (549 rows), for pooled partner pages and for lift/synergy-inconsistent rows. 202 rows are `rising` and 71 `falling` (|trend z| ≥ 2).
  - Partner decks use the combined page (3 decks). Otherwise the commander pages are pooled; no deck needs that today, so it is unit-tested only.
  - Every row is checked against lift = inclusion / (inclusion − synergy). It holds to 0.1% on 51 pages and fails on 1,851 rows across 11 pages; those rows are flagged and kept `low`.
  - The retrieval date is the cache file's mtime, because the payload has no fetch time. The newest deck-save date is recorded too.
- **Snapshot-keyed caching:** each file records the sha256 of every input; `--build` skips unchanged snapshots; the new `validate_all` step `evidence` fails on stale or invalid files (21 steps). 9 new tests are in `tests/test_evidence_layer.py`: aggregation, flags, confidence cap, items vs schema, the decision rule and schema negatives.
- **Tresserhorn's Lord, Returned stays `PENDING_RELEASE`.** The Wizards date for its set, **2026-11-13**, is authoritative (confirmed by the user, relayed by MTG Bot). Two sources conflict with it:
  - the source repo's verification record (L48, L67) and approval record call it legal now;
  - the Scryfall cache shows `not_legal`, but with a set release date of 2026-10-19.
  - Neither changes the state. The exception row already records the source error.
- **M2 unchanged:** criteria 1–3 met, 4–5 wait for Cory. No blueprint is marked `cory_reviewed` and M2 is not accepted.
- **Not touched:** `grixis/interactions/`, `data/grixis_interactions/` and `scripts/grixis_interactions.py` (read only; batch F, cycle 56, runs on the other executor). No decklist changed.
- **Files:** `scripts/grixis_evidence.py`, `data/grixis/evidence/` (62), `data/grixis/schemas/evidence_vector.schema.json`, `tests/test_evidence_layer.py`, `scripts/validate_all.py`, `data/grixis/registry.json` (M3 status), `grixis/Grixis Authority Model.md`, `README.md`, this log, `data/kb_index.json`.

## 2026-10-16 — Bot cycle 56 (phase 2 / M1: batch F)
- **Batch F is done** (the last 10 decks alphabetically, Sol'Kanar the Tainted through Zevlor): **59 rulings** (52 verified, 1 uncertain, 6 flags). Overall: **62/62 decks and 592 rulings; all 6 batches are done.** Each review hashes the deck's canonical project list from the M0 registry (read-only). The Rani uses its source baseline. Every record carries an `evidence_class` (batch F: 58 fact, 1 hypothesis). No decklist changed.
- **Pending decks:** The Madcap Jester and Tresserhorn's Lord (Returned) were reviewed against their lists. Both stay `PENDING_RELEASE` (legal from 2026-11-13).
- **Flags** (pilot notes, not list errors):
  - Sol'Kanar the Tainted: cards you donate (Pact, Coil, Archfiend, Greed's Gambit) come back if the player holding them leaves the game, per CR 800.4a and the official ruling. (dependency-risk)
  - Sol'Kanar the Tainted: the source attestation says Greed's Gambit triggers at upkeep. Its Oracle text says end step. (documentation)
  - The Rani: Force of Will's pitch pool is 23 blue nonland cards, not the 28 claimed. (documentation)
  - Thraximundar: Cultist of the Absolute has a mandatory upkeep sacrifice. (dependency-risk)
  - Tresserhorn's Lord: Blasphemous Edict takes Tresserhorn unless you control 13 or more other creatures. (anti-synergy)
  - Tresserhorn's Lord: the source says the deck is legal now. Gatherer, Wizards and Scryfall say it isn't legal until 2026-11-13. It stays pending. (documentation)
- **Uncertain:** jester-02. If Dauthi Voidwalker replaces a mill, does that card still count for the Jester? There's no official ruling, so it's tagged `hypothesis`.
- **Rules surprises:**
  - Blinking Sol'Kanar the Tainted while a mode-4 trigger is waiting makes the trigger fail on the new object.
  - Excalibur's mana value stays 12.
  - Savage Beating's extra combat has no main phase before it, and Relentless Assault does nothing if cast during combat.
  - Tetsuo Umezawa only needs the creature to be tapped or blocking, and only Aura spells can't target him. Bracers plus Aphetto Alchemist untap him without limit.
  - Cards exiled face down by Jester's Scepter can be played.
  - Any goaded creature that hits your opponents makes an investigation for The Rani.
  - Prisoner's Dilemma isn't a vote. Splitting your extra vote turns off Grudge Keeper.
  - Thraximundar counts as the "other Zombie" for Gravecrawler. Rooftop Storm still makes you pay commander tax.
  - Declining Tresserhorn's enters cost still draws 1 card.
  - Wick is the source of its damage, so with infect the damage becomes poison counters. Mana from Cavern of Souls can't pay for Wick's ability.
  - Zevlor's errata adds "only". The copies happen even if the original spell is countered. An overloaded Rift doesn't count.
- **Fixes:** Several CR citations were corrected against the 2026-09-25 CR before saving (for example 301.5c → 702.6a, 603.7c → 603.7b, 722.1 → 723.5). Spellbook step quotes now match the stored text exactly. The Norman Osborn review now uses the registry id `Norman_Osborn_Green_Goblin` that cycle 55 corrected (the review content is unchanged).
- **M1 status:** reviews 62/62, hashes match canonical 62/62, citations verbatim (the checker passes), and Bjorna's review covers Trade Secrets, Yawgmoth's Bargain and Lutri. **Open:** none of the reviews emits machine-readable `edges` for M4 yet. 512 of the 518 source attestation items are cited; 6 are not yet folded in or dispositioned (Azula ×2, Gwendlyn, Inalla, Lynde, Mai and Zuko). M1 acceptance belongs to Cory.
- **Coordination:** Bot cycle 55 (M2 blueprints batch 4, Norman's registry id) belongs to the other executor and was merged from main. Bot cycle 57.1 (M3 evidence layer) was merged from main too. With Cory's one-time approval (Option A), `grixis_evidence.py --build` was re-run for the 11 decks whose M1 reviews changed (the batch F decks and Norman). Only derived snapshot files were written; no code or schema changed. This cycle didn't touch blueprints, `data/grixis/registry*`, schemas, `grixis_refine.py` or the exception data.
- **Files:** `data/grixis_interactions/` (10 new reviews, plus the Norman id), `_batches.json` (F done), the rendered pages, deck-page Rules notes, `grixis/interactions/README.md`, `README.md`, `grixis/Grixis Integration Summary.md`, `data/kb_index.json`.
- **Next:** the M1 gaps (review `edges`, the 6 attestation items), then Cory's M1 acceptance.

## 2026-10-16 — Bot cycle 55 (M2: commander blueprints, batch 4; Norman Osborn registry id)
- **Batch 4: 16 decks**, Rograkh + Silas Renn … Zevlor, Elturel Exile alphabetically (Rograkh + Silas, Saruman, Sauron (Lord of the Rings), Sauron (the Dark Lord), Sedris, Sol'kanar the Swamp King, Sol'Kanar the Tainted, Tetsuo Umezawa, Tetsuo (Imperial Champion), The Madcap Jester, The Rani, The Valeyard, Thraximundar, Tresserhorn's Lord (Returned), Wick, Zevlor). **62/62 blueprints**: M2 criteria 1–3 are met; criteria 4–5 need Cory. Same standard as batches 1–3: every field carries an `evidence_class`, a `confidence` and line-numbered evidence.
- **Ceilings:** all 16 have a source ceiling (Tresserhorn's was recovered from its verification record, L15; the registry's extractor had found none); **0 disagreements**. Bracket 5 for Rograkh + Silas and The Madcap Jester; Bracket 4 for the other 14. Across all 62 decks there are 0 disagreements, and 6 decks still have no source ceiling.
- **Honest commander roles:**
  - `supporting`: Sol'kanar the Swamp King. None of the 13 Spellbook infinites uses him, and Demon's Horn duplicates his trigger.
  - `significant`, not `central`:
    - Rograkh + Silas: a zero-mana enabler plus a color-identity partner; all 7 combos are commander-free.
    - Sol'Kanar the Tainted: all 4 Demonic Pact gifts work without him.
    - The Madcap Jester: the kills are generic Oracle/Breach lines.
    - Thraximundar: none of the 17 combos names him, though he can be Gravecrawler's other Zombie.
  - `central`, with caveats:
    - Saruman's only combo doesn't need him.
    - Both Saurons, Tetsuo Umezawa, The Rani, The Valeyard and Zevlor have no compact kill (the Valeyard is low-end B4).
    - Sedris, Tetsuo (Imperial Champion), Tresserhorn (6 of 21 combos) and Wick (12 of 13) are truly commander-native.
- **Source issues flagged (not changed):**
  - Thraximundar is called "seven-mana" in the source; Oracle {4}{U}{B}{R} is mana value 6.
  - Tresserhorn's source verification (L48, L67) says the card is legal now and the future-release exception is stale. The Scryfall cache shows `not_legal`, and the Madcap source says the same set is legal from 2026-11-13. The registry keeps `PENDING_RELEASE`; Cory decides.
  - The Rani's decisions file still reads "not user approval" (L7); the approval record is the authority.
- **Norman Osborn registry id:** `Goben__Gene_Splice_Savant` → `Norman_Osborn_Green_Goblin`.
  - The correction is made in `grixis_authority.py` (`DECK_ID_CORRECTIONS`, `registry_id()`/`source_deck_id()`). The registry entry gets a `deck_id_provenance` block: source id, cycle, date, note and evidence (the source override key, the approval record, Grixis Corrections L178).
  - The source archive and the frozen baseline still use the old key. Every source-keyed lookup (summary, Spellbook, exceptions, refine state) translates back.
  - Schema: optional `deck_id_provenance`. New test `tests/test_deck_id_corrections.py` (4 tests).
- **M1 citations:** merged batch E (cycle 54) from main. Ten blueprints now cite their M1 reviews (Norman, both Obekas, Parnesse, Rograkh + Silas, Saruman, both Saurons, Sedris, Sol'kanar the Swamp King). M1 flags are carried as their own keys: rogsi-04 (Vexing Bauble self-counter), saruman-07 (Black Gate wording), parnesse-07 (Bonus Round symmetric) and parnesse-10 (`test_required`).
- **Not touched:** `grixis/interactions/`, `data/grixis_interactions/`, `scripts/grixis_interactions.py` (read only). No decklist changed.
- **Files:** `data/grixis/blueprints/` (16 new, 10 M1-patched, Norman's id), `grixis/blueprints/`, `data/grixis/registry.json`, `data/grixis/schemas/registry.schema.json`, `scripts/grixis_authority.py`, `scripts/grixis_blueprints.py`, `scripts/grixis_refine.py`, `tests/test_deck_id_corrections.py`, `grixis/Grixis Authority Model.md`, `README.md`, `data/kb_index.json`.
- **Next:** Cory reviews a sample of blueprints (criterion 4) and accepts M2 (criterion 5). Phases 3–6 follow, with M6 gated on M2+M4.

## 2026-10-16 — Bot cycle 54 (phase 2 / M1: batch E)
- **Batch E is done** (the next 10 decks alphabetically, Norman Osborn through Sol'kanar the Swamp King): **66 rulings** (62 verified, 1 uncertain, 3 flags). Overall: 52/62 decks and 533 rulings. Each review hashes the deck's canonical project list from the M0 registry (read-only). Norman Osborn and Sol'kanar the Swamp King use their source baselines. Every record carries an `evidence_class`. No decklist changed.
- **Flags** (pilot notes, not list errors):
  - Parnesse: Bonus Round also copies opponents' instants and sorceries cast that turn. (anti-synergy)
  - Rograkh + Silas Renn: your own Vexing Bauble counters your free spells and {0} escapes unless Hexing Squelcher is out. (dependency-risk)
  - Saruman: the source attestation says The Black Gate targets a player. It doesn't. (documentation)
- **Uncertain:** parnesse-10. When an opponent retargets a shared Parnesse copy at you, the 4-life tax probably applies, but there's no official ruling.
- **Rules surprises:**
  - Mayhem only needs a discard earlier in the turn.
  - Green Goblin makes Mox Amber tap for black and red.
  - Ending the turn early only delays a "next end step" trigger that has already triggered.
  - Throne + Staff give three upkeep triggers, not four.
  - Samut's split second locks you out too.
  - An X spell cast free off Summons has X=0.
  - Countering Sauron doesn't stop his reanimation.
  - Four Nazgûl are legal in Commander.
  - Teferi's Veil skips Sedris's unearth exile.
  - Sol'kanar ignores his own cast.
  - Blanket of Night gives swampwalk against every opponent.
- **Fixes:** Mizzix's Mastery MV corrected (4). Several CR citations were checked against the 2026-09-25 CR and corrected before saving. `lib.save` now writes atomically.
- **Coordination:** Bot cycle 53 (M2 blueprints batch 3) belongs to the other executor. This cycle didn't touch `grixis/blueprints/*`, `data/grixis/blueprints/*`, `refinement/blueprints/*`, `data/grixis/registry*`, schemas, `grixis_refine.py` or the exception data. The registry was only read.
- **Files:** `data/grixis_interactions/` (10 new reviews), `_batches.json` (E done), the rendered pages, deck-page Rules notes, `grixis/interactions/README.md`, `README.md`, `grixis/Grixis Integration Summary.md`, `data/kb_index.json`.
- **Next:** batch F (10 decks, Sol'kanar the Tainted through Zevlor; The Rani is on its source baseline), then phases 3–6.

## 2026-10-16 — Bot cycle 53 (M2: commander blueprints, batch 3; EDH Packages deck labels)
- **Batch 3: 16 decks**, Lynde, Cheerful Tormentor … Parnesse, the Subtle Brush alphabetically (Lynde, Mai and Zuko, Mairsil, Marchesa (Dealer of Death), Marchesa (the Black Rose), Mishra (Artificer Prodigy), Mishra (Eminent One), Missy, Nathan Drake, Nekusar, Nicol Bolas, Nicol Bolas (the Ravager), Norman Osborn, Obeka (Brute Chronologist), Obeka (Splitter of Seconds), Parnesse). **46/62 blueprints** in total. Same standard as batches 1–2: every field carries an `evidence_class`, a `confidence` and resolvable evidence. `resolved_ceiling` stays null and every blueprint is `seeded`. Twelve of the 16 cite M1 rulings, including the cycle 51 batch D reviews merged mid-cycle; Mishra (Artificer Prodigy) gets two M1 flags as key interactions. Mairsil's Marvin line is `test_required` because M1 marks it uncertain (mairsil-10). The four decks without an M1 review (Norman Osborn, both Obekas, Parnesse) cite source verification, Oracle text and the CR.
- **Ceilings:** all 16 have a source ceiling; **0 disagreements**. Bracket 5 for Marchesa, Dealer of Death, Mishra, Artificer Prodigy and Norman Osborn; Bracket 4 for the other 13. Parnesse's calibration floor (3) is below its source ceiling (4); the blueprint supports 4 (25 two-card infinites).
- **Honest commander roles:**
  - `supporting`: Parnesse. None of the 25 Spellbook infinites uses her, and her copy-sharing gives opponents copies.
  - `significant`, not `central`:
    - Mai and Zuko: all 8 infinites are commander-free.
    - Marchesa, Dealer of Death: the exact tournament list; all wins work without her.
    - Marchesa, the Black Rose: the source says "commander-native loops", but none of its 48 Spellbook infinites needs her.
    - Nekusar: the source itself says the deck works without him.
    - Nicol Bolas, the Ravager: the Teferi/Chain Veil combos are commander-free.
    - Norman Osborn: the Oracle/Breach kills are generic.
  - `central`, with caveats:
    - Lynde and Nathan Drake have no compact win (low-end B4).
    - Nicol Bolas is an eight-drop with an upkeep tax and no combo (low-end B4).
    - Mishra, Artificer Prodigy is central to the stax, and M1 shows Void Mirror/Bauble break his own loops without him.
    - Mishra, Eminent One, Missy and Obeka (Splitter of Seconds) are truly commander-native (Missy and Splitter appear in every Spellbook combo in their lists).
    - Mairsil and Obeka (Brute Chronologist) are central too.
- **Registry quirk:** Norman Osborn's registry deck id is still the stale tracker id `Goben__Gene_Splice_Savant`, so the source files (`Norman_Osborn_Green_Goblin_*`) were cited by hand.
- **Generator fix (EDH Packages.md deck labels):** `build_grixis.py` rewrites the Grixis deck pages without front matter, and `rebuild_enrichment.sh` runs `build_crossrefs.py`/`build_packages.py` before `front_matter.py` restores it. Deck labels in `data/deck_packages.json` and [EDH Packages](EDH%20Packages.md) therefore fell back to bare slugs. Cycles 50 and 52 worked around this by reverting the file. `build_crossrefs.meta_of` now derives deck fields with `front_matter.deck_fields` when a deck page has no front matter, so a full rebuild keeps full deck names. New `tests/test_deck_labels.py` has 5 tests: labels with and without front matter, non-deck pages, no bare-slug labels in EDH Packages.md, and none in `deck_packages.json`.
- **Not touched:** `grixis/interactions/`, `data/grixis_interactions/`, `scripts/grixis_interactions.py` (read only). No decklist changed.
## 2026-10-16 — Bot cycle 52 (M2: commander blueprints, batch 2)
- **Batch 2: 15 decks**, Edea, Possessed Sorceress … Lord Xander, the Collector alphabetically (Edea, Edward Kenway, Evelyn, Fire Lord Azula, Garza Zol, Goro-Goro and Satoru, Grixistax (Kraum + Tevesh Szat), Gwendlyn Di Corci, Inalla, Jeleva, Kefka, Kess, Loki, Lord of Tresserhorn, Lord Xander). **30/62 blueprints** in total. Same standard as batch 1: every field carries an `evidence_class`, a `confidence` and resolvable evidence (source decisions/approvals with line numbers, M1 rulings, Spellbook combo ids, CR rules, Oracle text). `resolved_ceiling` stays null and every blueprint is `seeded` (not reviewed by Cory).
- **Ceilings:** all 15 have a source ceiling; **0 disagreements**. Bracket 5 for Evelyn, Fire Lord Azula, Grixistax, Inalla, Jeleva, Kefka and Kess; Bracket 4 for the other 8.
- **Honest commander roles:**
  - `significant`, not `central`: Evelyn (all three proven wins work without her; she is the deck's only Vampire, so her "another Vampire" clause is dead text), Fire Lord Azula (copies only while attacking; Breach and Oracle wins don't need her), Jeleva (a value engine; the kills are generic), Grixistax (Tevesh is the parity engine; Kraum is close to incidental because the deck's own taxes suppress his trigger).
  - `central` with caveats: Loki has no compact win at all (Spellbook finds no combos; low-end B4 by card pool); Garza is a seven-mana single threat; Inalla, Kefka, Kess and Lord Xander drive their decks, but several of their win lines also run without them; Lord of Tresserhorn's enter trigger is a real cost.
- **Checks caught:** non-Villain, non-Wizard cards in typal packages (The Master, Multiplied; Hoarding Broodlord; Hexing Squelcher), Evereth listed as theft (it's a sacrifice outlet), and CR citations that didn't match their notes; all fixed before commit.
- **Not touched:** `grixis/interactions/`, `data/grixis_interactions/`, `scripts/grixis_interactions.py`. No decklist changed. Tooling unchanged from cycle 50.
## 2026-10-16 — Bot cycle 51 (phase 2 / M1: batch D)
- **Batch D is done** (the next 10 decks alphabetically, Mairsil through Nicol Bolas): **92 rulings** (86 verified, 1 uncertain, 5 flags). Overall: 42/62 decks and 467 rulings. Each review hashes the deck's canonical project list from the M0 registry (read-only). Nicol Bolas uses its source baseline (No Mercy kept; the challenger's No Mercy → Megrim swap isn't canonical). Every record carries an `evidence_class`. No decklist changed.
- **Flags** (pilot notes, not list errors):
  - Mishra, Artificer Prodigy: your own stax (Blood Funnel, Nether Void, Nullstone Gargoyle, Planar Chaos, Possibility Storm) hits your own instants and sorceries. Possibility Storm stops overloaded Vandalblast. (anti-synergy)
  - Mishra, Artificer Prodigy: Void Mirror and Vexing Bauble break the Top/KCI loops when Mishra is gone. (dependency-risk)
  - Nathan Drake: Dauthi Voidwalker starves Tinybones. (anti-synergy)
  - Nekusar: Krang doubles Spiteful Visions and Phyrexian Tyranny on your own draws. (dependency-risk)
  - Nicol Bolas: Chandra's Ignition off Nicol also wipes your own creature payoffs. (anti-synergy)
- **Uncertain:** mairsil-10, Marvin's unrestricted copies of caged abilities (no official ruling). **Hypothesis:** bolasrav-04, the Rings + Chain Veil + Teferi, Temporal Archmage variant (rules-derived; Spellbook 787-1124 covers only the base Veil + Teferi line).
- **Rules surprises:**
  - A caged Asmodeus draws seven for real, and a caged Wishclaw can't be activated.
  - Spellskite is a crime for Marchesa, Dealer of Death even with no target to change. Brain Freeze's storm copies aren't crimes.
  - Uncivil Unrest doubles only the first Murderous Redcap shot.
  - A Chalice that Mishra returns enters at X=0.
  - Helm copies of a Warform keep the 4/4 body but lose haste.
  - Face-down Cybermen don't loop until turned face up.
  - Nathan's own top card is exiled for good if you don't cast it.
  - Krang doesn't add to Nekusar's draw-step trigger.
  - Kitten on the Arisen returns the front-face Ravager and strips its Talents.
  - Copied loyalty abilities don't move loyalty.
  - Kediss's spread damage is noncombat (no commander damage, no retrigger).
  - Pain for All triggers once for several blockers.
- **Coordination:** Bot cycle 50 belongs to the parallel M2 blueprints work. This cycle didn't touch `refinement/blueprints/*`, `data/grixis/registry*`, schemas, `grixis_refine.py` or the exception data. The registry was only read.
- **Files:** `data/grixis_interactions/` (10 new reviews), `_batches.json` (D done), the rendered pages, deck-page Rules notes, `grixis/interactions/README.md`, `README.md`, `grixis/Grixis Integration Summary.md`.
- **Next:** batches E–F (20 decks; Norman Osborn, Sol'kanar the Swamp King and The Rani are on source baselines).

## 2026-10-16 — Bot cycle 50 (M2: commander blueprints, batch 1; M0 accepted)
- **M0 accepted.** Cory accepted M0 in chat on 2026-10-16 at 10:52 UTC ("I accept M0"), relayed by MTG Bot. It is recorded in `data/grixis/registry.json → program.milestones.M0` (`accepted_by` corymstover, `accepted_at` 2026-10-16T10:52Z, `acceptance_evidence`, `scope_note`). This is milestone acceptance only: **no deck is approved**, and all 62 keep their states. `grixis_authority.py --check` now requires an accepted milestone to have a human `accepted_by`, a date and evidence. M0 criterion 11 is ✅. M2 is `in_progress`.
- **M2 started: commander blueprints.**
  - **Schema v2** (`data/grixis/schemas/blueprint.schema.json`): every field is a claim with `evidence_class`, `confidence` and at least one evidence ref. It covers all brief §3 fields: Oracle facts, plan, the commander's real role (`central` / `significant` / `supporting` / `incidental` + an honest note), win conditions, engines, packages with min counts and out-of-list candidates, key interactions linked to M1 ids, tutors, recursion, requirements, failure modes, dependency level, power (source ceiling, GrokBot estimate, expected bracket, `resolved_ceiling` always null, disagreement, EDHREC brackets), project exceptions, identity core, anti-goals, theme, construction rules, heuristic supporting features, provenance.
  - **Tool** `scripts/grixis_blueprints.py`:
    - `--scaffold SLUG` gathers the evidence.
    - `--check` is the new `validate_all` step `blueprints`. It checks the schema; Oracle text, type, id and sha against the Scryfall cache; that card refs are in the canonical list or are declared candidates that are legal and in identity; that every evidence ref resolves (`oracle:`, `source_archive:path#Lline`, `interaction:`, `spellbook:`, `cr:`, `edhrec:`, …); the class rules; the canonical hash; the ceilings vs the registry; boilerplate reasons; and that pages are current.
    - `--render` writes the pages in [grixis/blueprints/](grixis/blueprints/README.md).
    - `--m2-status` reports the acceptance criteria.
  - **Registry:** `blueprint_version` and `grok_estimated_ceiling` now come from the blueprint, and `disagreement` is computed. A source ceiling the original parse missed is stored as `source_ceiling.recovered`, with a `path#Lline` citation (recovery, not an overwrite).
- **Batch 1: 15 decks**, Abaddon … Dr. Eggman alphabetically.
  - Recovered source ceilings:
    - Ashnod: Bracket 4 (approval-gate dossier L41).
    - Cormela: cEDH / 5 (decision ledger L12).
  - Still no source ceiling: Admiral Beckett Brass, Admiral Brass, Anhelo, Ashad, Be'lakor, Bjorna/Cecily. Their source files state none.
  - **0 ceiling disagreements** in this batch: every estimate where the source states a ceiling agrees with it.
  - Honest roles: Bjorna/Cecily is `supporting`. Bjorna is near-incidental, and the source misdescribes both commanders. Anhelo and Ashad are `significant`, not `central`, because their decks' infinites run without them. Crosis and Davros are low-end Bracket 4 because of their card pools, not their engines.
- **Tests:** `tests/test_blueprints.py` adds 17 tests (63 in total): schema, Oracle mismatch, card refs and candidates, min counts, class rules, ref resolution, ceilings, review status, boilerplate, exceptions, M2 status, milestone acceptance.
- **Not touched:** `grixis/interactions/`, `data/grixis_interactions/`, `scripts/grixis_interactions.py` (the M1 executor's area; read only). No decklist changed.
## 2026-10-16 — Bot cycle 49 (phase 2 / M1: batch C; M0 follow-ups)
- **Batch C is done** (the next 10 decks alphabetically, Gwendlyn Di Corci through Mai and Zuko): **99 rulings** (94 verified, 1 uncertain, 4 flags). Overall: 32/62 decks and 375 rulings. Every batch-C deck's source attestation JSON is re-verified item by item. No decklist changed.
- **M0 landed on main during the cycle** (PR #120). The pending follow-ups are done:
  - **Canonical list.** Interaction reviews now hash the M0 registry's `canonical_project_list.export` (read-only), not the legacy export. `list_source` must name that list. A `[Companion]` line must match the record's `companion`. This affects the 7 decks whose canonical list is the source baseline.
  - **Re-reviews.** Three of those 7 decks were already reviewed, and all three were re-reviewed:
    - **Abaddon:** Mystic Remora replaces GrokBot's unapproved Stormfist Crusader. abaddon-11 is rewritten and now verified; abaddon-29 is added.
    - **Bjorna + Cecily:** the canonical list restores the three authorized exceptions (Trade Secrets, Yawgmoth's Bargain, Lutri as companion), all 🚩 NOT Commander-legal. bjorna-10 (Flame of Anor, now only in the derived projection) is retired. bjorna-11 is rewritten (`approved_decision`). New entries: bjorna-14 (Lutri companion), bjorna-15 (Trade Secrets + Notion Thief) and bjorna-16 (Yawgmoth's Bargain + Ageless Insight).
    - **Kefka:** reviewed on its canonical list in this batch (Final Fortune and Valley Floodcaller, not the challenger swaps).
  - **evidence_class required.** Every record now has an `evidence_class`. The batch A/B pass gave: verified and flag → `fact`; uncertain → `hypothesis`; brass-10 and crosis-10 → `strategic_judgment`; abaddon-11 → `derived_metric`.
  - **validate_all:** the step lists had already been merged by cycle 47 (7c `spellbook-steps`, 7d `source-archive`, 7e `authority`, 7f `unit-tests`).
- **Batch C flags** (pilot notes, not list errors; all anti-synergy):
  - Gwendlyn: Lightning Greaves' shroud stops the targeted untappers and Bracers' equip.
  - Gwendlyn: Chains of Mephistopheles hits your own wheels.
  - Lord of Tresserhorn: Greaves' shroud blocks the deck's own Lord-targeting kill spells.
  - Lynde: returned Curses attach to you and punish you until moved, one per upkeep.
- **Uncertain:** inalla-06, the Spellseeker one-card chain. It's a rebuilt line with no confirming Spellbook variant (`hypothesis`).
- **Rules surprises:**
  - Single-faced clones of Kefka can't transform (CR 701.27c).
  - Saw in Half on a commander still makes tokens (CR 903.9a).
  - Mox Diamond doesn't work as the Grinding Station + Breach artifact.
  - A Curse sacrificed during an end step returns a turn later (CR 513.2).
  - Urza's Saga can't find Walking Ballista.
  - Loki's enter-attacking tokens never get the copied creature's attack triggers.
  - Auton Soldier's myriad Xanders give enter triggers but no dies triggers.
- **Files:** `scripts/grixis_interactions.py` (canonical list via the registry, companion parsing, required `evidence_class`), `data/grixis_interactions/` (10 new reviews, the A/B evidence pass, 3 re-reviews), `_batches.json` (C done), the rendered pages, deck-page Rules notes, `grixis/interactions/README.md`, `README.md`, `grixis/Grixis Integration Summary.md`.
- **Not touched:** `data/grixis/registry*`, schemas, `grixis_refine.py` and the exception data.
- **Next:** batches D–F (30 decks).

## 2026-10-16 — Bot cycle 48 (phase 2 / M1: Spellbook step cache, batch B)
- **Batch B is done** (the next 10 decks alphabetically): **107 rulings** (99 verified, 2 uncertain, 6 flags). Overall: 22/62 decks and 273 rulings. Every batch-B deck's source attestation JSON is re-verified item by item. No decklist changed.
- **New:**
  - `scripts/spellbook_steps.py` caches Commander Spellbook variant step text (public API) for all 302 combo ids in `data/grixis_combos.json`, to `data/grixis_spellbook_steps.json`, with retrieval date 2026-10-16.
  - Its `--check` (offline, every id cached) is a new `validate_all` step, `spellbook-steps`.
  - Interaction records gain `spellbook` citations (a verbatim step or prerequisite, checked) and an optional `evidence_class`. The dossier prints each combo's steps.
- **Batch A uncertain items:** 7 of 11 resolved with the cached steps.
  - **Self-correction:** ashnod-08 had claimed a simultaneous-sacrifice requirement; Spellbook's sequential line shows it isn't needed. It's now a documentation flag.
  - New entries: beckett-17 (Breeches modes exhausted), and ashad-14, an uncertain hypothesis.
- **Batch B flags:**
  - Don Andres: Dauthi Voidwalker vs Thieving Amalgam (anti-synergy).
  - Edward Kenway: Fateful Discovery + Academy Manufactor decking during a Time Sieve lock (dependency-risk).
  - Evelyn: Vexing Bauble vs escaped LED/Petal (anti-synergy); the source's pre-2020 commander-zone caveat on Saw in Half (documentation).
  - Garza Zol: Jeska enters with 0 loyalty before any command-zone cast (dependency-risk).
  - Grixistax: Blood Moon vs its own Phyrexian Tower (anti-synergy).
- **Uncertain:** doom-09 (the Trade Routes loops) and evelyn-05 (the Worldgorger → Evelyn → Oracle endpoint). Both are rebuilt lines with no confirming Spellbook variant, marked `hypothesis`.
- **M0 coordination:** Bot cycle 47 (authority foundation) is not on main at the end of this cycle, so these steps are **pending**:
  - make `evidence_class` universal;
  - re-review Bjorna/Cecily against the restored canonical project list.

  Registry, schemas, `grixis_refine.py` and the exception data weren't touched.

## 2026-10-16 — Bot cycle 47 (M0: Grixis authority foundation)
- **Summary:** milestone M0 of Cory's authority program, after his approval of the [gap analysis](grixis/Grixis%20Authority%20Gap%20Analysis.md) and his eight binding constraints. Model and rules: [Grixis Authority Model](grixis/Grixis%20Authority%20Model.md).
  - **Registry** `data/grixis/registry.json`: all 62 decks with the §19 fields. 60 start at `SOURCE_BASELINE` and 2 at `PENDING_RELEASE`; nothing is approved. The 62/62 source approvals and the cycle 39–44 refinements are now evidence: 6 *GrokBot challengers (unapproved)*, plus 56 verdicts relabeled "heuristic: no candidate passed v1 gates (not a certificate)". Logical list hash `lh1` is authoritative; the raw hash is recorded.
  - **Approvals** `data/grixis/approvals.json` (empty). Only Cory can move a deck to APPROVED or CANONICAL_LOCKED, per exact hash. APPROVAL_READY and above also need M2 + M4 accepted and a certificate.
  - **Legality vs authorization:** separate fields everywhere. `data/grixis/exceptions.json` imports the source's 8-row registry, verified against Scryfall and Wizards; **4 rows corrected** (Lutri's companion ban, Lutri missing from the source's approved file, Nazgûl ×2 are official card rules, Tresserhorn's Lord recorded as legal while it is legal only from 2026-11-13).
  - **Bjorna + Cecily:** the canonical project list restores Trade Secrets, Yawgmoth's Bargain and Lutri (companion), labeled 🚩 NOT Commander-legal. The Bot cycle 16 replacements are now only the *derived compliance projection (not canonical)*.
  - **Schemas:** 14 JSON Schemas in `data/grixis/schemas/` (evidence classes, registry, exceptions, approvals, refine v2; v1 drafts for blueprint, graph, audit, candidate, optimizer pass, swap, test, certificate). Cory's constraints are encoded there: provisional dispositions, workload not a gate, independent optimizer passes.
  - **grixis_refine.py:** v1 is frozen (`--engine v1`). v2 (`--engine v2`) gives exploratory recommendations with gates as diagnostics and protections as priors, analyzes every slot, and reads EDHREC lift, trend, sample size and retrieval date. It never publishes a final list.
  - **Exports:** every file is labeled (`index.json` manifest). New `source-baseline/` (6 challenger decks + Bjorna) and `projections/`.
  - **Tests:** a new `tests/` suite (46 tests, including a check that M1 interaction `evidence_class` values match the seven authority classes) and `scripts/run_tests.py`. `validate_all` gained the steps `authority` and `unit-tests`.
- **Files:** `data/grixis/` (new), `data/grixis_refine_v2.json` (new), `scripts/grixis_authority.py` (new), `scripts/run_tests.py` (new), `tests/` (new), `grixis/Grixis Authority Model.md` (new), `grixis/Grixis Authority Gap Analysis.md` (new), `scripts/build_grixis.py`, `scripts/grixis_refine.py`, `scripts/front_matter.py`, `scripts/validate_all.py`, `scripts/evaluate_decklist.py` (Lutri message: dropped an unverified B&R date), `pytest.ini`, the Bjorna deck page, all 62 refinement blocks (relabeled), `exports/grixis-archidekt/`, `grixis/README.md`, `grixis/Grixis Refinement Cycle.md`, `grixis/Grixis Corrections.md`, the generated indexes.
- **Reason:** Cory's brief. Heuristics had been acting as authority, a bot-written review had been promoting "final" lists, and a user-authorized exception had been silently replaced. M0 makes authority explicit and machine-checked before any further refinement.
- **Follow-up for M1:** the interaction reviews hash the legacy export files. For the 6 challenger decks and Bjorna, those files are not the canonical list. M1 should hash `canonical_project_list.export` and review the canonical deltas, including Bjorna's 3 exceptions.

## 2026-10-16 — Bot cycle 46 (phase 2: interaction reviews, tooling + batch A)
- **Phase 2 of Cory's program:** an Abaddon-style, card-level rules review per deck, in [grixis/interactions/](grixis/interactions/README.md). Batch A (the first 12 decks alphabetically) is done: **164 rulings** (142 verified, 11 uncertain, 11 flags).
  - Every ruling is checked against current Oracle text, Scryfall rulings (bulk 2026-10-15) and the CR (2026-09-25), with rule numbers cited.
  - Source attestations (the retrospective for decks 1–8 and the deck-level JSONs for Cormela, Crosis, Cult of Skaro and Davros) are folded in and re-verified.
  - Each deck page links its review from a new **Rules notes** section.
- **New:**
  - `scripts/grixis_interactions.py` renders the reviews, the deck-page blocks and the status table; `--check` is a new `validate_all` step (`interactions`).
  - The check verifies the deck hash, every Oracle, ruling and source quote, every CR rule number, card membership, statuses and flags, rendered pages and batch coverage.
  - Data lives in `data/grixis_interactions/<slug>.json` (schema in the [README](grixis/interactions/README.md#data-format)), with batches in `_batches.json`.
  - `rebuild_enrichment.sh` re-runs it after `grixis_refine`.
- **Flags (no decklist changed):**
  - Abaddon: mandatory cascade on 0-MV spells randomizes the library, and a stacked top card is exposed to later cascades.
  - Admiral Brass: finality counters exile instead of dying, so Pitiless Plunderer and Victimize lose value.
  - Bjorna/Cecily: Peer into the Abyss + Teferi's Ageless Insight loses on an odd library, and Notion Thief starves Breach + Wheel + Jeska's Will.
  - Crosis: Painter's Servant on black or green knocks Sword of Feast and Famine off.
  - Documentation fixes: Abaddon's Call Forth the Tempest MV, Kari Zev's token type, Ashnod's stale wording, Be'lakor's 'near-infinite draw' label, the Cecily blueprint.
- **Also:** Cory's coverage audit is saved as [COVERAGE_AUDIT_2026-10-16.md](grixis/source-archive/COVERAGE_AUDIT_2026-10-16.md) and linked from the archive README.
- **Reason:** Cory's phase 2 request. Batches B–F (50 decks) follow in later cycles.

## 2026-10-16 — Bot cycle 45 (full Grixis source archive, single source of truth)
- **Phase 1 of Cory's multi-phase program.** The complete [grixis-commander-encyclopediaGPT](https://github.com/corymstover/grixis-commander-encyclopediaGPT) repo at `1836b97` (re-pulled; no upstream change) is now archived in [grixis/source-archive/](grixis/source-archive/README.md).
  - 1,017 files (14,865,126 bytes), byte-identical, with only `.git` excluded.
  - [`SHA256SUMS`](grixis/source-archive/SHA256SUMS) and `source.json` record the hashes, commit and counts.
  - `history/…bundle` (6.4 MB) holds all 49 branches and 1,726 commits.
  - Method: a plain `git archive` snapshot plus a bundle, chosen over `git subtree` so an interrupted run can simply be repeated.
- **Verified:**
  - 1,017/1,017 SHA-256 hashes match the source clone, with 0 differences, and `diff -r` is clean.
  - `sha256sum -c` passes, and a clone from the bundle restores HEAD `1836b97`.
- **New:**
  - `scripts/grixis_archive.py` (`--check`, `--against CLONE`, `--import CLONE`).
  - A `validate_all` step, `source-archive`, that re-hashes every file on each run and fails if a root `.github/workflows` appears.
- **Kept inert:**
  - The archived workflows stay under the archive path, so GitHub does not run them.
  - `pytest.ini` uses `norecursedirs`, and `.rgignore` hides the tree from plain `rg`.
  - `check_links.py` and `check_citations.py` skip the tree, so the counts are unchanged.
  - The KB index and front matter only index registered pages.
- **Single source of truth:** `build_grixis.py`, `grixis_eval.py`, `grixis_refine.py` and `lore_quotes.py` default to the archive. The cited commit comes from `source.json`. Rebuilt output is unchanged.
- **Fix:** in the Refinement Cycle's "Most shared cards" list, cards with equal counts are now sorted by name. Their order used to change between runs because set iteration is hash-randomized. The output is now deterministic.
- **Docs:** Grixis section index (archive callout + Pages row), [Integration Summary](grixis/Grixis%20Integration%20Summary.md#bot-cycle-45-full-source-archive), README, Knowledge Index.
- **Coverage pointer:** about 78% of the source's unique content was already integrated (Cory's coverage audit). The rest is archived for phases 2–6.
- Original GitHub repo untouched. `validate_all` PASS.

## 2026-10-16 — Bot cycle 44 follow-up (pending legality date → 2026-11-13)
- **`legal_from` → 2026-11-13** for The Madcap Jester and Tresserhorn's Lord, Returned (`data/grixis_pending.json`), approved by Cory. The new `legal_from_source` field cites [Wizards](https://magic.wizards.com/en/news/feature/whats-inside-mystery-booster-commander-edition): "New-to-Magic MBC cards will be legal in Commander on November 13, 2026." (What's Inside Mystery Booster Commander Edition?, Aug 3, 2026; legality dates updated per the editor's note).
- **Rebuilt:** deck pages and banners (which now cite Wizards), front matter (`legal_from: 2026-11-13`; schema doc updated), Grixis Corrections / Evaluation / README, export status and notes, the Refinement Cycle summary and flags. The README, Progress Tracker, ROADMAP, Integration Summary and earlier Update Log entries now say 2026-11-13.
- **Activation routine:** `grixis-pending-legality-activation` was moved to 2026-11-13. It only activates and re-verifies (`activate_pending_grixis.py`, then rebuild and `validate_all`); no refinement pass. If Scryfall has not updated yet, the script exits 2; re-run it later.
- Pending markers are unchanged (both decks still ⏳ pending). `validate_all` PASS.

## 2026-10-16 — Bot cycle 44 (Grixis refinement batch 6: the 2 pending decks)
- **Batch 6:** The Madcap Jester and Tresserhorn's Lord, Returned, both still ⏳ pending legality. Same method and gates as batches 1–5. The not-yet-legal cards (The Madcap Jester, Dragon's Smile, Tresserhorn's Lord, Returned) are treated as the known pending exception; every other card is judged normally.
  - **The Madcap Jester** (52%): at ceiling, unchanged.
    - Hand review: the list is built on the Jester's line, "causes one or more cards to be exiled from an opponent's library, you may play those cards". Library-exile effects include Praetor's Grasp, Extract, Bitter Ordeal and Jester's Cap; payoffs include Dragon's Smile, Bilbo and Gonti. Around that sits a cEDH Thassa's Oracle / Breach core.
    - Every generic card is a Game Changer, a combo piece or fast mana. The on-theme adds would replace free counterspells and fail the gates.
    - New hook: exiling and playing opponents' library cards.
  - **Tresserhorn's Lord, Returned** (74%): at ceiling, unchanged.
    - Hand review: a sacrifice-draw engine with free outlets, token fodder for the enter cost, and Gravecrawler / Locust God loops.
    - The few cards with no hook protect the 10-power body (Not of This World, Stubborn Denial).
- **Source legality claim re-verified and still flagged.** The source says Tresserhorn's Lord, Returned has "current official Commander legality PASS". Against that:
  - Scryfall (live, 2026-10-16) still lists all three `mbc` cards as `not_legal`.
  - Wizards' "What's Inside Mystery Booster Commander Edition?" article (updated legality dates) says "New-to-Magic MBC cards will be legal in Commander on November 13, 2026."
  - The source's own Madcap Jester verification gives the same 2026-11-13 date.
- ⚠️ **Registry date is not the legal date.** `data/grixis_pending.json` used Scryfall's set release date as `legal_from`, not Wizards' Commander date of 2026-11-13. *Resolved in the follow-up below: `legal_from` is now 2026-11-13.*
- **Activation check:** `activate_pending_grixis.py --check` passes (both decks not legal yet). A worktree simulation with the pending cards forced to legal ran the rebuild (`build_grixis.py`, then `grixis_refine.py`). It gave 62 legal pages, banners removed, both refinement blocks and hand reviews kept, exports no longer marked pending, and `--check` with 0 problems. The summary page no longer crashes if a deck drops out of the build.
- **Grixis Refinement Cycle.md:** the summary now covers all 62 decks, with the 2 pending decks marked refined but pending. New flags cover the Tresserhorn legality claim and the MBC date. The export README notes the official date.
- **Source:** pulled again, still at `1836b97`. Tagged `v2.5.1-grixis-refinement-pending` after merge. `validate_all` PASS.

## 2026-10-16 — Bot cycle 43 (Grixis refinement batch 5, end-of-cycle summary, v2.5-grixis-refinement)
- **Batch 5 (10 decks):** Sedris, Sol'kanar the Swamp King, Sol'kanar the Tainted, Tetsuo Umezawa, Tetsuo Imperial Champion, The Rani, The Valeyard, Thraximundar, Wick, Zevlor.
  - **2 refined:**
    - Sol'kanar the Swamp King: −Windfall +Well of Lost Dreams. "Whenever a player casts a black spell, you gain 1 life" becomes repeatable card draw.
    - The Rani: −Mystic Remora +Idol of Oblivion. Her Mark of the Rani Aura tokens and Clues let it draw on most turns.
  - **8 at/near ceiling.**
  - **2 automatic candidates rejected in writing:**
    - Wheel of Fortune → Ayara: Wheel stays with Underworld Dreams.
    - Reanimate → Village Rites: Thraximundar already has seven sacrifice outlets.
  - Wheel of Fortune (Sol'kanar) and Reanimate (Thraximundar) are now protected.
- **Hand reviews:**
  - Batch 5: Sol'kanar the Swamp King and Tetsuo Umezawa.
  - Thraximundar: its existing flag is kept. The source state's audit path `refinement/decisions/Thraximundar_Whole_List_Audit_v2_2026-10-15.csv` is still missing at `1836b97`.
  - Late hand reviews for two batch 2 decks that were under or near the line: Fire Lord Azula (25%; cEDH ceiling, same tradeoff as Evelyn, flagged) and Garza Zol (31%; Voltron identity confirmed). Neither list changed.
- **Scoring fixes:** new hooks for unearth (Sedris), life gain and black spells / Swamps (Sol'kanar), tapping / blocking creatures (Tetsuo Umezawa), and villainous choice / voting (The Valeyard). All four commanders matched no hook before.
- **End state:** all 60 legal decks reviewed.
  - 6 changed, with 7 swaps (3 hand-picked).
  - 54 at/near ceiling.
  - 17 written verdicts on automatic candidates (4 accepted, 13 rejected).
  - 8 hand reviews.
- **Grixis Refinement Cycle.md:** new end-of-cycle summary section. It covers the method, the changed decks with their identity impact, the decks at ceiling, flagged items (Evelyn/Azula tradeoff, Thraximundar audit path, Archidekt import not tested in Archidekt, Kefka's Monument to Endurance idea left open), homogenization and overlap findings, and the two pending decks with their activation follow-up (now 2026-11-13). The batch log now counts written verdicts for each batch.
- **Exports:**
  - The export README now carries per-deck key notes: dependence, hooks, hand-review verdict, flags, protected cards. It also has an import-notes section.
  - Final export pass in `validate_all`: every file has well-formed `N Name` lines, the commander line(s) first as `1 Name [Commander]`, exactly 100 cards, and no repeated lines.
- **Batch 4 miscount fixed:** 7 verdicts covering 6 cards (Consider twice). The merged PR #113 body was corrected the same way (one `gh api` PATCH; `gh pr edit` fails on the Projects-classic deprecation).
- **Source:** pulled again, still at `1836b97`.
- Tagged `v2.5-grixis-refinement` after merge. `validate_all` PASS.

## 2026-10-16 — Bot cycle 42 (Grixis refinement batch 4)
- **Batch 4 (12 decks):** Missy, Nathan Drake, Nekusar, Nicol Bolas, Nicol Bolas the Ravager, both Obekas, Parnesse, Rograkh + Silas Renn, Saruman, both Saurons.
  - 1 refined: Nicol Bolas, No Mercy → Megrim (hand-picked). Nicol's "deals damage to an opponent" makes that player discard their hand, so each card discarded deals 2.
  - 11 at/near ceiling.
  - Automatic candidates that passed the guard got 7 written reject verdicts covering 6 cards: Aqueous Form, Faithless Looting, Lavaspur Boots, Consider (twice: for Mystic Remora and for Windfall), Deep Analysis, Palantír of Orthanc. *(Corrected in Bot cycle 43; the original entry said 6 candidates.)* Each replaced a stronger or core card. Windfall is now protected in Sauron, Lord of the Rings as part of the reanimation core.
- **Hand review:** Nicol Bolas. The low 31% score was mostly a hook gap; with the "deals damage to an opponent" hook it is 40%. The list is a connect-and-punish deck (boots, Sword of Feast and Famine, Pain for All, Chandra's Ignition, Kediss; Liliana's Caress, Raiders' Wake, Waste Not).
- **Scoring fixes:**
  - New "opponents drawing" hook (Nekusar had no hook before).
  - The combat hook now covers "deals damage to an opponent".
  - Reminder text no longer counts for roles: ward's "counter it" is not a counterspell.
- **Source:** pulled again, still at `1836b97`.
- **Exports** regenerated. `validate_all` PASS.

## 2026-10-16 — Bot cycle 41 (Grixis refinement batch 3, hand-picked swaps, hand reviews)
- **Hand-picked swaps:** new `manual_swaps` input in `data/grixis_refine_review.json`. It goes through the same gates as automatic swaps: legality, color identity, bracket, combo-piece protection, role and MV parity, power guard, and a verbatim check on the Oracle quotes. Failures are logged on the deck page.
- **Batch 3 (13 decks, Jeleva through Mishra, Eminent One):**
  - 1 refined: Kefka, with 2 hand-picked swaps.
    - Final Fortune → Liliana's Caress: every Kefka enter/attack discard drains each opponent 2. 33.4% of Kefka decks vs 11.1%; one fewer extra-turn card.
    - Valley Floodcaller → Dauthi Voidwalker: opponents' discards and Brain Freeze mills are exiled with void counters, so one can be cast. 33.1% vs 16.1%.
    - Monument to Endurance was rejected by the gates (MV 3 vs Mystic Remora's 1).
    - The proposed Brain Freeze and Borne Upon a Wind cuts were replaced: Brain Freeze is a Breach combo piece, and Borne is a flash enabler.
  - 12 at/near ceiling. Lord of Tresserhorn is the legal deck; the pending one is Tresserhorn's Lord, Returned, whose markers are untouched.
- **Hand reviews:**
  - Evelyn: an identity-first Vampire version would clearly be weaker. Her "once each turn" play limit means extra Vampire triggers add little, and every candidate would replace a cEDH combo or protection piece. Left unchanged and flagged.
  - Marchesa, Dealer of Death: the low score was our gap. A new crimes hook raised her dependence from 14% to 56%. The list (recorded by the source as a 2026-10-11 tournament-winning configuration) is identity-driven. Gitaxian Probe was considered and not swapped in.
- **Source:** pulled again, still at `1836b97`.
- **Exports** regenerated. `validate_all` PASS.

## 2026-10-16 — Bot cycle 40 (Grixis refinement: power guard, batch-1 re-check, batch 2)
Cory tightened the method: precision over speed, no artificial weakening.
- **Power guard** (`scripts/grixis_refine.py`). An add must:
  - match or beat the cut's inclusion on the commander's EDHREC page;
  - keep its overall EDHREC rank within 4× / +2000 of the cut's;
  - not replace a free spell (pitch or commander-free) with one that costs mana.
- **Manual review.** Every guard-passing swap needs a written accept/reject reason in `data/grixis_refine_review.json`. That file can also protect deck-core cards from cuts. Trigger doublers such as Roaming Throne are now protected automatically for triggered commanders.
- **Batch-1 re-check:** 3 swaps reverted and logged:
  - Abaddon: Chandra, Torch of Defiance for Deadly Rollick (free spell lost; lower Abaddon inclusion);
  - Crosis: Whispersilk Cloak for Deflecting Swat (free spell lost) and Quest for the Nihil Stone for Reanimate (rank 10,497 vs 53; lower Crosis inclusion);
  - Admiral Brass, Unsinkable: Lethal Scheme for Deadly Rollick (free spell lost).
  - Kept, with a written review: Abaddon −Mystic Remora +Stormfist Crusader.
- **Evelyn scoring gap fixed** with new hooks for playing cards from exile, flash, and "or another … enters". Her score went from 1% to 15%. The remaining gap is real: the list is a generic cEDH reanimator/Thoracle shell (flagged).
- **Overlap review** (manual, on the [Refinement Cycle](grixis/Grixis%20Refinement%20Cycle.md#overlap-review-manual) page):
  - Kess/Kefka is partly homogenization for Kefka. Identity-driven proposals for his batch: Liliana's Caress, Monument to Endurance, Dauthi Voidwalker.
  - Cormela/Kess and Jeleva/Kess are identity-justified (shared spellslinger engines).
- **Batch 2 (13 decks, Doctor Doom through Inalla):**
  - 1 refined: Norman Osborn −Mystic Remora +Thrill of Possibility. Thrill's discard cost gives the discarded card mayhem from Green Goblin at {2} less.
  - 12 at/near ceiling. 17 candidate swaps were rejected by the guard and 3 by review.
- **Source:** `git pull` on the read-only Grixis clone. It is still at `1836b97`, so there are no upstream changes to fold in.
- **Exports** regenerated (62 files + ALL-DECKS.txt + README). `validate_all` PASS.

## 2026-10-16 — Bot cycle 39 (Grixis commander-first refinement, batch 1)
Cory's mission: every Grixis deck must be the definitive, maximally optimized version of its commander's deck, not a Grixis shell ([Grixis Mission](grixis/Grixis%20Mission.md), also at the top of the [Grixis index](grixis/README.md)).
- **Measurement:** new `scripts/grixis_refine.py` scores all 62 decks; the 2 pending ones are included and noted. It measures:
  - commander dependence: Oracle hooks from the commander's own text, plus EDHREC synergy ≥ 15%;
  - generic share, pairwise overlap, and Thoracle-core and control-core counts.
  - Results are on the [Grixis Refinement Cycle](grixis/Grixis%20Refinement%20Cycle.md) page and in `data/grixis_refinement.json`.
- **Batch 1 (12 decks: Abaddon through Davros):**
  - 3 refined: Abaddon, Admiral Brass Unsinkable and Crosis, with 5 swaps.
  - 9 flagged at/near their ceiling and left unchanged.
  - Every swap quotes both Oracle texts and cites EDHREC data. Every refined list passes `evaluate_decklist.check`, keeps every Commander Spellbook combo, and does not raise the bracket floor.
  - Swaps are frozen in `data/grixis_refine_batches.json`. Each deck page has a per-deck *Refinement log*.
- **Exports:** `exports/grixis-archidekt/` has one Archidekt import file per deck (`1 Card Name`, with the commander as `[Commander]`), `ALL-DECKS.txt` and a README noting status and changes. The format was checked against the source repo's `exports/archidekt_2026-10-15/` package.
- **Method:** new [Checklist Gate G — commander identity](EDH%20Deck%20Evaluation%20Checklist.md#gate-g--commander-identity) and a measured-dependence row in the [EDH Deck Template](EDH%20Deck%20Template.md) blueprint.
- **Validation:** new `grixis-refine` step in `validate_all`: refined lists are re-verified and every export must match its deck page's final list (100 cards, singleton, color identity).

## 2026-10-16 — Bot cycle 38 (Grixis: 62/62 pages, 2 pending legality)
Cory wants all 62 Grixis decks in the companion. **62/62 deck pages: 60 legal + 2 ⏳ pending legality** ([#63](https://github.com/corymstover/GrokBotMTGCompanion/issues/63)).
- **New pages:** [The Madcap Jester](grixis/decks/the-madcap-jester.md) and [Tresserhorn's Lord, Returned](grixis/decks/tresserhorns-lord-returned.md). Same format as the others, plus a ⏳ PENDING LEGALITY banner and front matter `legality_status: pending`, `legal_from` (now 2026-11-13; corrected in Bot cycle 44), `pending_cards`. Set `mbc` is still `not_legal` on 2026-10-16 (Scryfall API and bulk).
- **Counts:** the pending decks are excluded from the README Decks table, Packages (N = 60) and all legal counts. Corrections: 135 (+2 format, +2 bracket, +2 pending legality). Calibration: 110 decks, the 2 pending ones marked ⏳.
- **Validation:** `validate_all` accepts the listed cards only while `legal_from` is in the future. After that it fails until activation. Tested with a simulated date past `legal_from`: 5 problems, as intended.
- **Activation:** new `scripts/activate_pending_grixis.py` with registry `data/grixis_pending.json`. `--check` runs a live Scryfall API check. The full run refreshes the bulk, flips decks to active and rebuilds. Phase 8 enrichment batch membership is now sticky, so a bulk refresh never drops enriched cards.

## 2026-10-16 — Bot cycle 37 (Grixis re-analysis)
Cory resumed the Grixis work. The read-only source [grixis-commander-encyclopediaGPT](https://github.com/corymstover/grixis-commander-encyclopediaGPT) moved from `df1abb9` (v1.9) to `1836b97`: 275 commits and 400 files. The clone was only fast-forwarded.

- **Source changes:**
  - All 62 lists are now APPROVED / LOCKED; 22 were UNREFINED before. No list was removed.
  - The 40 lists imported in cycle 16 are byte-identical.
  - New: a 62-deck Archidekt export with `manifest.csv`, per-deck 99-slot whole-list audits and approval-ready verifications, artifact paths in the state file, and one-shot finalizers.
- **Re-evaluation ([#59](https://github.com/corymstover/GrokBotMTGCompanion/issues/59), [#60](https://github.com/corymstover/GrokBotMTGCompanion/issues/60)):**
  - All 62 lists checked with `grixis_eval.py` against the card DB. The only hard issues are Bjorna + Cecily's 2 banned cards (already corrected) and the 3 `mbc` cards.
  - New `mbc` cards become Commander-legal on 2026-11-13 (Wizards; corrected in Bot cycle 44). The Scryfall API and bulk still say `not_legal` on 2026-10-16.
  - 17,683 source Oracle rows: 0 outdated.
  - The newer Scryfall bulk (2026-10-15 21:01) changes no Oracle text, legality, Game Changer flag or identity, so the KB stays on the 09:02 bulk (its EDHREC ranks drive the Phase 8 batches).
- **Integrated:** 20 newly approved lists, **60 decks** in total. They include Norman Osborn // Green Goblin (deck id `Goben__…`), both Nicol Bolases, both Obekas, Parnesse, Rograkh + Silas Renn, Saruman, both Saurons, Sedris, both Sol'kanars, both Tetsuos, The Rani, The Valeyard, Thraximundar, Wick and Zevlor. The Madcap Jester and Tresserhorn's Lord, Returned wait for `mbc` legality.
- **Corrections:** 129 (+42): 60 format, 60 bracket, 2 legality, 2 provenance, 1 companion, 4 low-land flags (Ashad and Dr. Eggman unchanged; Saruman and Sedris new). No source bracket target is below its floor. The Lutri companion is still dropped.
- **Source structural findings** ([Grixis Corrections](grixis/Grixis%20Corrections.md#source-repo-structural-findings)):
  - The Tresserhorn approval claims official legality before release.
  - One state artifact path is missing (Thraximundar's audit).
  - Deck id `Goben__Gene_Splice_Savant` holds Norman Osborn.
  - The export README confirms the Admiral Brass and Anhelo digest explanation.
- **Tooling:**
  - `build_grixis.py` now finds deck records through the state's `*_artifact` paths, labels cycle 16 vs cycle 37 imports (`data/grixis_c16_ids.json`) and links `refinement/audits/`.
  - `grixis_eval.py` writes indented JSON again.
- **Standards:** new [Checklist Gate F](EDH%20Deck%20Evaluation%20Checklist.md#gate-f--approval-ready-candidate-and-lock): an approval-ready candidate approved by its SHA-256, a 99-slot audit tally, a dated legality checkpoint, and an export manifest. Also a [Template §6](EDH%20Deck%20Template.md#6-finalization-record) addition and an [EDH Standards](EDH%20Standards.md#deck-evaluation-method-from-the-grixis-repo) note, all credited to the source. The Lore-Themed guide needed no change.
- **Downstream:** bracket calibration now covers 108 decks (B2 12, B3 31, B4 65). Cross-references, card enrichment (KB-deck synergy) and package back-links were rebuilt.
- `validate_all` PASS (13 steps).

## 2026-10-16 — Bot cycle 36 (Phase 8: Legends evidence, audit pass 2, batch 4 partial)
Last Phase 8 cycle for now (Cory: stop after cycle 36). Slices 3–10 were not run.

- **Official Legends / Story Spotlight articles ([#100](https://github.com/corymstover/GrokBotMTGCompanion/issues/100)):** 26 Wizards articles (17 *Legends of …* set articles, 3 *Story Spotlight Cards*, 6 more legendary-character previews: Modern Horizons 2 ×2, Commander Legends ×2, March of the Machine team-ups, Thunder Junction crew) listed in the new `data/story_extra_sources.csv` and fetched by `scripts/fetch_story_pages.py` into `.cache/story/extra/`. They are kept apart from the story cache, so the quote ledger and the priority tiers do not shift.
  - New Lore evidence: a card whose front-face name is a heading line on one of these articles renders ✅ *Presented with an official backstory on* (Legends) or ✅ *Listed on* (Spotlight). 495 cards. Batch-35 cards with the ❓ no-lore-yet line fell from 1,045 to 809.
  - Planeswalker's Guide card galleries are images only, so they are not evidence.
- **Name-match audit, second pass:** the 401 kept ⚠️ links were re-tested. A link is confirmed when the card is presented on a Legends / Spotlight article that also names the character. 60 more confirmed. Totals for the 702 links: 353 confirmed (156 page, 131 art, 62 Legends / Spotlight article, 3 flavor, 1 Story Spotlight printing), 341 ⚠️, 8 removed.
- **Curated notes:** 8 Story Spotlight notes (Assemble the Players, Matzalantli, Huatli's Final Strike, Warleader's Call, Audience with Trostani, Expose the Culprit, Bitter Triumph, Canonized in Blood), 28 total. Quotes are verbatim in the cited Spotlight articles. The note check now also reads `.cache/story/extra/`.
- **Batch 4 / batch 36 ([#101](https://github.com/corymstover/GrokBotMTGCompanion/issues/101)):** slices 1–2 of 10: 500 legendary creatures to EDHREC rank 9,647. EDHREC 500, as-commander 500, Spellbook combos 233, KB decks 46, 124 flagged 🚫 Universes Beyond; 89 have lore evidence, 411 carry the ❓ line.
- **Coverage:** planeswalkers 338/338; entry-linked 128/128; character cards 414/414; story-flavor 1,431/1,431; legendary creatures 1,822/3,786 (48.1%); priority pool 3,397/5,361 (63.4%).
- **Remaining gaps:** 1,964 legendary creatures (ranks 9,648–32,347, then 281 unranked); 341 ⚠️ links; 1,220 ❓ cards; more Spotlight notes. See [ROADMAP → Phase 8](ROADMAP.md#phase-8--card-level-lore--synergy-deepening-bot-cycles-33-cory-2026-10-15).
- `validate_all` PASS (13 steps).

## 2026-10-15 — Bot cycle 35 (Phase 8: story cache, name-match audit, batch 3)
- **Story-page cache:**
  - New `scripts/fetch_story_pages.py` rebuilds `.cache/story/` from `data/primary_sources.csv` (626 pages) plus the 8 cited articles. It is rate-limited (1 s), resumable, retries, and writes atomically.
  - Inline markup is merged before extraction, so sentences are not split. 463 of the 626 pages reproduce the recorded word counts exactly.
  - `lore_quotes` is back to full verification: all 2,719 quotes, 0 misses. All 19 kept flavor-text matches were re-verified.
- **Name-match audit ([#100](https://github.com/corymstover/GrokBotMTGCompanion/issues/100)):** all 702 links that rested only on a name match were tested against the cached pages, the entries' citations and the cards' printings.
  - 293 confirmed as *depicts*, with the evidence on the card's line:
    - 156: an official page names the card (e.g. the "Legends of …" articles);
    - 131: the card's art is captioned on a page that names the character;
    - 4: the flavor text names the character;
    - 2: Story Spotlight printings.
  - A name the entry itself uses for the character (e.g. "Rowan Kenrith") does not count as evidence.
  - 401 kept as ⚠️ name match only. 6 of these links sit on Un-/playtest cards and are now flagged 🚫 (Urza, Academy Headmaster; Chandra, Gremlin Wrangler; Kaya, Ghost Haunter; Tibalt the Chaotic).
  - 8 removed: Niv-Mizzet cards repeated under the Duskmourn support-team group heading. Group headings no longer repeat cards that sit under a character's own heading.
  - The new [Card Enrichment → Name-match audit](Card%20Enrichment.md#name-match-audit) table records the results, and a validation check covers the confirmation evidence.
- **Curated notes:** 8 Story Spotlight notes (Settle the Score, In Bolas's Clutches, Vraska's Contempt, Deadlock Trap, Oath of Kaya, Unlikely Aid, Gideon's Intervention, Mastermind's Acquisition), 20 in total. Each quotes the scene captioned with the card verbatim.
- **Batch 3 ([#101](https://github.com/corymstover/GrokBotMTGCompanion/issues/101)):** 1,047 cards: every remaining planeswalker (46) and the top 1,000 not-yet-enriched legendary creatures by EDHREC rank (≤ 6,915; 1,001 cards).
  - Enriched in four checkpointed slices of about 250 cards, each pushed with `validate_all` PASS.
  - Synergy: Spellbook combos 611, EDHREC 1,033, as-commander 1,017, KB decks 289, package guidance 334.
  - Lore: 1,045 cards have no lore link yet and carry a ❓ line. 217 are flagged 🚫 Universes Beyond.
- **Tooling:**
  - `scripts/rebuild_enrichment.sh` runs the Phase 8 chain.
  - Flags now apply to every printing: 🚫 when every printing is Un-/playtest, ⚠️ for digital-only cards.
  - `--fetch` now only fetches cards that have no stored synergy.
- **Coverage:** planeswalkers 338/338; legendary creatures 1,322/3,786; priority pool 2,897/5,361 (54.0%).
- `validate_all` PASS (13 steps).

## 2026-10-15 — Bot cycle 34 (Phase 8: batch 2, package back-links, atomic writes)
Batch 2 of [Phase 8](https://github.com/corymstover/GrokBotMTGCompanion/milestone/17). The first run was interrupted by a box reset, so this cycle also covers the recovery.

- **P8.2 ([#100](https://github.com/corymstover/GrokBotMTGCompanion/issues/100)) batch 2 lore:** 1,757 more cards: every remaining lore-entry-linked card, all 414 name-matched character cards and every story-flavor card. 1,850 cards are now enriched.
  - By type: 317 creatures, 270 legendary creatures, 270 planeswalkers, 270 sorceries, 267 instants, 160 enchantments, 107 lands, 58 artifacts, 20 legendary artifacts, 13 other legendaries, 4 legendary lands, 1 battle.
  - 713 new lore relations: 7 *depicts*, 29 *featured*, 677 *name match only* ⚠️.
  - New evidence kind: **art shown on an official story page**, counted only when the `data/story_art_captions.csv` caption names the card and its artist matches a printing (1,077 cards). There are also 381 Story Spotlight cards, 268 Art & Flavor section back-links and 19 cards whose flavor text appears verbatim on an official page.
  - 7 new curated notes in `data/card_lore_notes.json`: Golgothian Sylex (🔄 origin retcon), Moonsilver Key, Crucible of the Spirit Dragon, Hedron Archive, The World Tree, Halo Fountain and Halo Forager. All 15 quotations in the 12 notes were re-checked against the live official pages after the reset.
  - Creatures named for an item (Halo Forager → Halo) are now *featured*, not *depicts*.
- **P8.3 ([#101](https://github.com/corymstover/GrokBotMTGCompanion/issues/101)) batch 2 synergy:**
  - Proven tier: KB decks 302, Commander Spellbook combos 487, EDHREC co-occurrence 1,747, EDHREC as-commander 284. Guidance tier (EDH Packages): 321.
  - EDHREC/Spellbook were fetched in the background, one thread per host, 1 s apart. The fetch now follows EDHREC redirect stubs, which fixes split cards such as Integrity // Intervention. A 403 from EDHREC (no page) is cached as a miss.
  - 10 cards have no EDHREC page. Most are meld results or digital-only cards.
- **P8.4 ([#102](https://github.com/corymstover/GrokBotMTGCompanion/issues/102)) done:**
  - Each EDH Packages sub-package lists the enriched cards that name it.
  - The `card-enrichment` step now checks package ↔ card reciprocity, Art & Flavor back-links and curated-note flags.
- **Recovery and robustness:**
  - The box reset wiped the gitignored `.cache/` and `/tmp`. `data/card_enrichment.json` survived complete and was kept. The partially rewritten generated files were restored from HEAD with `git restore`.
  - Caches rebuilt:
    - the identical Scryfall bulks (2026-10-15 09:02, still hosted);
    - CR 2026-09-25;
    - the price snapshot, via new `scripts/build_min_usd.py`, which reproduces the EDH Packages prices exactly.
  - The story-page cache is not rebuilt yet. Until it is, `lore_quotes --check` compares fingerprints with the ledger, and the enrichment build keeps the flavor-text matches verified in an earlier run.
  - New `scripts/atomic_io.py`: every generator now writes through a temp file plus `os.replace`, so a killed run leaves each file either old or new.
  - The branch was pushed in checkpoint commits.
- **Coverage:** entry-linked 128/128, character cards 414/414, story-flavor 1,431/1,431, planeswalkers 291/338, legendary creatures 322/3,786. Priority pool: 1,850/5,361 (34.5%). The pool grew from 4,549 because art on official pages now counts as story-flavor evidence.
- `validate_all` PASS (13 steps).

## 2026-10-15 — Bot cycle 33 (Phase 8: card enrichment format + batch 1)
New milestone [Phase 8 — Card-level lore & synergy deepening](https://github.com/corymstover/GrokBotMTGCompanion/milestone/17) with issues #99–#103 (Cory's request). This cycle covers the format, the tooling and batch 1.

- **P8.1 (#99) format and tooling:**
  - New `scripts/build_card_enrichment.py` writes `data/card_enrichment.json` and two lines per enriched card entry, **Lore** and **Synergy**, placed before *Referenced in*. `ingest_scryfall.py` renders them from the JSON, so a re-import keeps them.
  - New generated page [Card Enrichment](Card%20Enrichment.md): format, coverage of the priority pool, cards by lore entry, cards by package, and EDHREC clusters.
  - Curated notes go in `data/card_lore_notes.json`. Each needs official sources, and every quotation in it must be verbatim on a cited cached page.
  - [Card Data Conventions](Card%20Data%20Conventions.md) documents the lines.
- **P8.2 (#100) batch 1 lore:** 93 legendary cards and planeswalkers already linked from lore entries (64 legendary creatures, 18 legendary artifacts, 9 planeswalkers, 1 legendary land, 1 other legendary). They have 121 lore relations: 14 *depicts*, 82 *featured*, 25 *name match only* ⚠️. 28 relations carry a citation on the linking line itself; 68 use the entry's own citations (*via entry*). 19 cards show the entry line's ⚠️/❓ flags.
  - Story Spotlight printings: Lithoform Engine (ZNR), Niv-Mizzet Reborn (WAR), The Celestus (MID).
  - Curated notes, quotes verified against the cached pages: Godsend (THB Story on Cards), Blackblade Reforged (DOM Ep. 5), The Mightstone and Weakstone (BRO Ep. 5), Helvault (PW Guide to AVR), The Immortal Sun (PW Guide to Ixalan).
- **P8.3 (#101) batch 1 synergy:**
  - *Proven* tier: 29 cards are in KB decks; 49 have Commander Spellbook combos (Commander-legal variants, most popular shown); all 93 have EDHREC co-occurrence (decks and top commanders); 64 have EDHREC as-commander data (highest-synergy cards).
  - *Guidance* tier: EDH Packages Oracle-pattern matches for 22 cards.
  - Clusters: Esika (Kaldheim gods), Jodah, Be'lakor, Cloud (equipment), Ramos (Ikoria Apexes), Zhulodok (legendary artifacts).
- **P8.4 (#102) links and validation:**
  - New `validate_all` step **card-enrichment**: the JSON, shard lines and page are current; every lore relation is cited and its entry links the card back (for name matches, the *Character cards* table does); every listed deck contains the card; tiers are labelled; curated quotes are verbatim.
  - The reverse index lists each enriched card's lore entries.
  - The Lore Entry Index has an *Enriched cards* column and the tag `has-enriched-cards`.
- **Coverage:** entry-linked cards 93/128 (72.7%); character cards 18/414; legendary creatures 62/3,786; planeswalkers 11/338; story-flavor cards 3/396. Whole priority pool: 93/4,549 (2.0%).
- `validate_all.py` PASS (13 steps). Grixis #63 remains ON HOLD.

## 2026-10-15 — Bot cycle 32 (Phase 7 complete: lore cross-refs, story maps, rules quote checks)
Phase 7 priorities 2 + 4 and the rest of the gap audit. Phase 7 is complete; snapshot tag `v2.2-phase7-optimization`.

- **P7.2 (#93) bidirectional cross-refs:**
  - New `scripts/build_lore_xrefs.py`. It relates lore entries through hand-written links and name mentions (case-sensitive, whole-word; ambiguous names such as "Ravnica", group entries and common first names are not matched), makes every relation symmetric, and writes a generated *Cross-references* block at the end of each entry: 1,460 relations, blocks on 269 of 280 entries. Items also get same-name cards ("name match", not a canon claim); entries used by a lore deck link the deck's story map.
  - `check_lore.py` now fails if a block is stale or any entry→entry link (2,943) or deck pointer (23) has no way back.
  - Fix: an entry now ends before another generator's region, so the last Characters Index entry no longer pushed its block into the `CHARCARDS` table (the two generators had been undoing each other).
- **P7.4 (#95) lore-deck calibration + pilot notes:**
  - Each lore deck spec has a `story_map` (package → lore entries) and a `plane_anchor`. Both deck pages now have **Story pilot notes (guidance) → Story map**. Urza's "Lat-Nam & the Third Path" package has no lore entry yet and is flagged ⚠️.
  - [EDH Bracket Calibration](EDH%20Bracket%20Calibration.md#lore-decks) has a new **Lore decks** section: Urza floor 2, lore score 93.8%, story map 9/10; Nahiri floor 2, 86.8%, 10/10.
  - Fix: `build_lore_decks.py` counts lands by front face, as calibration does. The Nahiri deck is 36 lands + 1 MDFC (Emeria's Call), not 37.
  - [EDH Lore-Themed Deckbuilding](EDH%20Lore-Themed%20Deckbuilding.md) documents the story-map standard.
- **P7.5 (#96) gap audit:**
  - `lore_quotes.py` now also checks 12 rules/FAQ/EDH pages: FAQ, Rules Interactions, Keyword Encyclopedia, EDH Standards, EDH Mulligans, EDH Deck Evaluation Checklist, EDH Deck Template, Card Data Conventions, Tokens/Emblems/Dungeons, Format Legality Matrix, Printing History, EDH Win Conditions. That is 1,044 quotes, all verified against the cached CR, Scryfall rulings, card text, cached Wizards pages or (for the two Grixis-derived method pages) the read-only Grixis source, except 3 documented terms/code. In total, 2,719 quotes on 25 pages.
  - 8 cited Wizards pages were fetched into a new gitignored `.cache/story/articles/`: B&R list, keyword glossary, reprint policy, ward preview, M21 release notes, two Making Magic columns, the Commander format page.
  - Fixes:
    - The EDH Deck Template swap question is now verbatim from the Grixis Refinement Protocol ("For this named role or package, …").
    - The EDH Standards Game Changers definition and the "choose a legendary creature or artifact" quote now cite the Commander format page, where both are verbatim.
    - `" / "` between Oracle lines is treated as a joiner.
  - [Story Arc Summaries](Story%20Arc%20Summaries.md) is split into entries: 20 entries, kind `summary`, with Phase 7 issue numbers in its front matter. It is in the Lore Entry Index and kb_find (`--kind summary`), and has cross-reference blocks.
  - [Knowledge Snapshots](Knowledge%20Snapshots.md) had no `v2.1-phase6-lore` row. Added it, plus `v2.2`.
- `validate_all.py` PASS (12 steps). Grixis #63 remains ON HOLD.

## 2026-10-15 — Bot cycle 31 (Phase 7: lore retrieval + validation)
New milestone [Phase 7 — Lore optimization pass](https://github.com/corymstover/GrokBotMTGCompanion/milestone/16) and issues #92–#96 (Cory's request: Phase 5's 4 priorities applied to the Phase 6 material). This cycle covers priorities 1 + 3.

- **P7.1 (#92) retrieval:**
  - Every lore page now carries the `lore` tag and its Phase 6/7 issue numbers.
  - The 7 lore entry pages carry `entry_kind` and `entries` (schema v2, additive keys; [Front-Matter Schema](Front-Matter%20Schema.md) regenerated).
  - New `scripts/lore_lib.py` (entry parsing) and `scripts/build_lore_index.py`, which writes [Lore Entry Index](Lore%20Entry%20Index.md) and `data/lore_entries.json`: 260 entries, each with computed tags (kind, ⚠️/❓/🚫/🔄 flags, spark state, `has-cards`), citation count and links by target.
  - `kb_find.py` indexes these entries (`--kind`, e.g. `--tag spark-lost`).
  - [Lookup Guide](Lookup%20Guide.md) gained lore lookups.
- **P7.3 (#94) validation:**
  - New `scripts/check_lore.py` (`validate_all` step **lore-entries**): every entry cites an official page; dossier timeline and retcon statement rows are cited; anchors resolve; spark state is consistent across the Characters Index (glance table + sparks table), the dossier summary and the retcon log's KB treatment rows; the index is current.
  - New `scripts/lore_quotes.py` (step **lore-quotes**): 1,675 quotations on 13 lore pages are checked against the cited cached page, then any cached official page, then Scryfall card text. NFKC ligatures and nested quotation marks are folded. Ledger: `data/lore_quotes.json`.
  - Documented exceptions are in `data/lore_quote_exceptions.json`: IKO Story-on-Cards image text, Apple Books / Netflix Tudum, and labels in quotation marks.
  - Without the gitignored cache, the step compares quote fingerprints with the ledger.
- **Fixes found by the new checks (P7.5, #96):**
  - **30 cited official pages had never been cached**: 19 Planeswalker profile pages, 9 feature articles (incl. the Jace, Liliana and Gideon origin stories) and 2 Making Magic columns. They are now fetched, so Lore Primary Sources has 626 pages.
  - **Paraphrases shown as quotations corrected to the verbatim text:**
    - Tarkir "dragon tempests kept birthing dragons" (Conflicts & Arcs, Retcons Log).
    - Teferi's profile line (Dossiers).
    - The Gideon's Memorial listing (Characters Index).
    - Three profile date phrases (Master Timeline).
    - The Deepest Night D&D line (Side-Media).
    - "the Edge (of Eternity)" (Planes).
    - "the stripping of her spark" (Characters).
  - Elspeth retcon row now cites its page directly.
  - Stale lore counts fixed in Knowledge Index (Conflicts 39→40, Retcons, Planes, Primary Sources 538→626) and Progress Tracker (588→626).
- `validate_all.py` PASS (12 steps). Grixis #63 remains ON HOLD.

## 2026-10-15 — Bot cycle 30 (Phase 6: final dossiers, status, snapshot)
Issues [#72](https://github.com/corymstover/GrokBotMTGCompanion/issues/72)–[#77](https://github.com/corymstover/GrokBotMTGCompanion/issues/77); milestone 15. Cycle 29 merged as PR #90.

- [Planeswalker Dossiers](Planeswalker%20Dossiers.md) (#74): **final 7 dossiers**: Dovin Baan, Angrath, Venser, Xenagos, Ashiok (incl. the BRO letter to Elspeth), Rowan & Will Kenrith, Teyo Verada (23 rows) → **38 dossiers**. Summary table +7 rows. Echoverse Venser 🚫 excluded.
- [Items & Artifacts Index](Items%20%26%20Artifacts%20Index.md) (#75): **+2 (26)**: a piece of the House (Kaito's artificial Omenpath), Stormnexus Ritual & Crucible of the Spirit Dragon. No other officially named Duskmourn or dragonstorm relics were found.
- [Contradictions & Retcons Log](Contradictions%20%26%20Retcons%20Log.md): **29 entries** (+which "Ashiok" is Ashiok ⚠️; Venser canon vs Echoverse 🚫).
- New **Phase 6 status** sections in [ROADMAP](ROADMAP.md#phase-6) and [Progress Tracker](Progress%20Tracker.md#phase-6-status): totals and blocked work (novels, image-only text, open ❓).
- Issues #72, #74, #75 closed as done; #73, #76, #77 stay open for blocked work. Snapshot tag `v2.1-phase6-lore`. Maintenance mode not started.
- Every new quote was checked verbatim against the fetched text (0 new misses). `validate_all.py` PASS. Grixis #63 remains ON HOLD.

## 2026-10-15 — Bot cycle 29 (Phase 6: dossiers, Omenpath-era planes, items)
Issues [#73](https://github.com/corymstover/GrokBotMTGCompanion/issues/73), [#74](https://github.com/corymstover/GrokBotMTGCompanion/issues/74), [#75](https://github.com/corymstover/GrokBotMTGCompanion/issues/75), [#76](https://github.com/corymstover/GrokBotMTGCompanion/issues/76); milestone 15. Cycle 28 merged as PR #89.

- [Planeswalker Dossiers](Planeswalker%20Dossiers.md) (#74): **6 new dossiers** — Kiora, Koth, Narset, Saheeli Rai, Huatli, Samut (25 timeline rows; spark moments ✅ for Narset and Samut) → **31 dossiers**. Vraska gains an OTJ row; summary table +6 rows.
- **Spark fix:** Vraska → **lost** ("only without her Planeswalker's spark", official OTJ crew feature). Characters Index status row, entry and sparks table updated.
- [Planes Index](Planes%20Index.md) (#74): **Thunder Junction** (⚠️ no Planeswalker's Guide was published; sourced from the announcement, crew feature and episodes), **Bloomburrow**, **Duskmourn**, **Sothera system (the Edge)** → 42 detailed entries.
- [Items & Artifacts Index](Items%20%26%20Artifacts%20Index.md) (#75): **+2 (24)** — Mana Rig / powerstones / Thran steel (DMU), singularity beads (EOE). The Endstone entry now covers the "Metalman's artifact" (Tezzeret) and the unnamed maker ❓; the sylex entry lists three origin statements.
- [Contradictions & Retcons Log](Contradictions%20%26%20Retcons%20Log.md): **27 entries** (+who made the sylex ❓, Vraska's spark ✅); queue +1 (the Endstone's maker).
- [Lore Primary Sources](Lore%20Primary%20Sources.md) (#73): OTJ episodes 1, 3–5, the OTJ announcement and the crew feature fetched → 596 pages.
- Every new quote was checked verbatim against the fetched text (0 new misses). `validate_all.py` PASS. Grixis #63 remains ON HOLD.

## 2026-10-15 — Bot cycle 28 (Phase 6: dossiers, items, planes, retcons)
Issues [#73](https://github.com/corymstover/GrokBotMTGCompanion/issues/73), [#74](https://github.com/corymstover/GrokBotMTGCompanion/issues/74), [#75](https://github.com/corymstover/GrokBotMTGCompanion/issues/75), [#76](https://github.com/corymstover/GrokBotMTGCompanion/issues/76); milestone 15. Cycle 27 merged as PR #88.

- [Planeswalker Dossiers](Planeswalker%20Dossiers.md) (#74): **+7 rows** for Jace (RTR, WAR Living Guildpact loss, DSK), Elspeth (THB return, the sylex into the Blind Eternities) and Ajani (JOU, Beyond Repair). **New dossiers:** Garruk Wildspeaker, Wrenn (spark moment ✅ from profile) and Niv-Mizzet (📝 not a Planeswalker) → **25 dossiers**. Spark summary: fixed the stale Nahiri row (now "lost") and added 3 rows.
- [Items & Artifacts Index](Items%20%26%20Artifacts%20Index.md) (#75): **+3 entries (22)**: Reality Chip, World Tree & the Sword of the Realms, Theros god weapons (Dekella, Mastix, Akmon, Ephixis). The sylex entry now records the copy's fate (detonated in the Blind Eternities). Ozolith re-checked: still ⚠️ (image text only).
- [Planes Index](Planes%20Index.md) (#74): **Dominaria (before DMU)**, **Kamigawa (Kami War era)**, **Fiora**, **Shandalar** → 38 detailed entries; all 15 planes with official profiles now have one.
- [Characters Index](Characters%20Index.md): Teyo, Will Kenrith and Bolas spark statements re-checked. Bolas is unknown even in-story ("we don't know whether his spark is intact", LE Ep. 2); Will's shared-spark context added ⚠️; Teyo stays ❓.
- [Contradictions & Retcons Log](Contradictions%20%26%20Retcons%20Log.md): **25 entries** (+sylex blast vs spark loss ❓, Elspeth's death and return ✅, Living Guildpact Jace → Niv-Mizzet 🔄).
- [Lore Primary Sources](Lore%20Primary%20Sources.md) (#73): 6 more official pages fetched (Garruk, Wrenn, Teyo, Will and Rowan profiles; Legends of Kaldheim) → 594 pages.
- Every new quote was checked verbatim against the fetched text (0 new misses). `validate_all.py` PASS. Grixis #63 remains ON HOLD.

## 2026-10-15 — Bot cycle 27 (Phase 6: dossiers, items, planes, spark refresh)
Issues [#74](https://github.com/corymstover/GrokBotMTGCompanion/issues/74), [#75](https://github.com/corymstover/GrokBotMTGCompanion/issues/75), [#76](https://github.com/corymstover/GrokBotMTGCompanion/issues/76); milestone 15. Cycle 26 merged as PR #87.

- [Planeswalker Dossiers](Planeswalker%20Dossiers.md) (#74): **+14 timeline rows**: Vraska (Bolas's Golgari offer, WAR), Tamiyo (SOI, EMN moon binding, NEO compleation setup), Sarkhan (Fate Reforged duel, WAR spear), Ugin (absence a thousand years ago, Fate Reforged magic), Bolas (original-timeline murder of Ugin, Tezzeret and Vraska hires), Kaito (NEO search for the emperor) and Oko (arrival on Eldraine, OTJ with Kellan).
- [Items & Artifacts Index](Items%20%26%20Artifacts%20Index.md) (#75): **+5 entries (19)**: Halo, Lithoform Core, Mightstone & Weakstone, Celestus / Sungold Lock / Moonsilver Key, Biblioplex & the Blood Avatar. "Strixhaven Archives" has no exact match in the fetched text, so it is covered as the Biblioplex. Queue refreshed.
- [Planes Index](Planes%20Index.md) (#74): **Ravnica (before the invasion)**, **Alara**, **Mirrodin (before Phyrexia)**, **Lorwyn-Shadowmoor** (34 detailed entries).
- [Characters Index](Characters%20Index.md): spark refresh. **Nahiri → spark lost** ("Then again, she was no longer a Planeswalker", Beyond Repair); the open question is closed. Teferi's reclaim is now cited (DOM Ep. 11). Teyo, Will Kenrith and Bolas stay ❓.
- [Contradictions & Retcons Log](Contradictions%20%26%20Retcons%20Log.md): **22 entries** (+Nahiri's spark ✅ resolved; Moonsilver Key: Innistrad relic, then Teferi's artifact ⚠️ inferred).
- Every new quote was checked verbatim against the fetched text (0 new misses). `validate_all.py` PASS. Grixis #63 remains ON HOLD.

## 2026-10-15 — Bot cycle 26 (Phase 6: dossiers, planes, items index)
Issues [#74](https://github.com/corymstover/GrokBotMTGCompanion/issues/74), [#75](https://github.com/corymstover/GrokBotMTGCompanion/issues/75), [#76](https://github.com/corymstover/GrokBotMTGCompanion/issues/76); milestone 15. Cycle 25 merged as PR #86.

- [Planeswalker Dossiers](Planeswalker%20Dossiers.md) (#74): **+14 timeline rows** for Karn (DOM sylex dig, WAR, BRO dissection), Teferi (DOM spark, BRO time travel), Kaya (WAR oath, BRO), Nahiri (the Helvault, MAT spark), Sorin (Helvault, SOI), Ral (WAR) and Tezzeret (AER, BRO with the Planar Bridge in his chest). Teferi's spark-reclaim is now cited.
- [Planes Index](Planes%20Index.md) (#74): new detailed entries for **Innistrad**, **Zendikar (Eldrazi era)**, **Theros** and **Tarkir** (30 detailed entries).
- New **[Items & Artifacts Index](Items%20%26%20Artifacts%20Index.md)** (#75 started): 14 entries (Golgothian Sylex, Blackblade, Immortal Sun, Chain Veil, Godsend & Khrusor, Helvault, Hedrons, Planar Bridge, Spear of Hazoret, Temporal Anchor, Ozolith ⚠️, Endstone, Elderspell, Realmbreaker), each with verbatim-cited uses, arc links and card links.
- [Contradictions & Retcons Log](Contradictions%20%26%20Retcons%20Log.md): 20 entries.
  - **Resolved:** Teferi's spark. He reclaims it in DOM Ep. 11: "One of the reasons I took my spark back was to come with you." It was ❓ open in cycle 25.
  - **New:** the sylex plan (Karn's 2018 plan vs the invasion-era copy).
  - **New ❓:** the Immortal Sun was built for Torrezon but found in Orazca.
  - Searching all 588 fetched pages found no spark restored after the invasion; that item stays queued.
- [Master Timeline](Master%20Timeline.md): the ELD, THB, IKO and MAT rows are deepened with sources. Lukka's later Oriq and compleation appearances are now cited.
- Every new quote was checked verbatim against the fetched text (0 new misses; the Ozolith lines are ⚠️ image text). `validate_all.py` PASS. Grixis #63 remains ON HOLD.

## 2026-10-15 — Bot cycle 25 (Phase 6: last six arcs, episode upgrades, dossiers)
Issues [#72](https://github.com/corymstover/GrokBotMTGCompanion/issues/72), [#73](https://github.com/corymstover/GrokBotMTGCompanion/issues/73), [#74](https://github.com/corymstover/GrokBotMTGCompanion/issues/74), [#76](https://github.com/corymstover/GrokBotMTGCompanion/issues/76); milestone 15.

- [Conflicts & Arcs](Conflicts%20%26%20Arcs.md): the **last 6 short arcs** are rewritten in Cause · Key beats · Outcome · Lasting consequences · Sources format, so all **40/40** entries are now in full format:
  - Throne of Eldraine (PW Guide + publisher listing + Story Spotlights; ⚠️ novel not fetched).
  - Theros Beyond Death (Story Summary + Story on Cards + Journey's End).
  - Ikoria (PW Guide + Story on Cards; image text kept, ⚠️ not machine-verifiable).
  - The Brothers' War frame story (5 chapters + 5 episodes).
  - March of the Machine: The Aftermath (both official side stories).
  - The Lost Caverns of Ixalan (PW Guide + 6 episodes + Pawns).
- Episode-cited beats were added to **BFZ/OGW** (Sea Gate, Kiora vs Ulamog, the hedron prison), **SOI/EMN** (the Helvault, Avacyn's death, the moon binding) and **Dominaria/WAR** (Teferi's spark, Belzenlok, Jace's rally, Gideon's Blackblade).
- `build_primary_sources.py` gains 10 arc codes (33 total): ELD, THB, IKO, BRO, MAT, LCI, BFZ/OGW, SOI/EMN, DOM/WAR. 588 pages in [Lore Primary Sources](Lore%20Primary%20Sources.md).
- [Planeswalker Dossiers](Planeswalker%20Dossiers.md) (#74): **+19 timeline rows** for Chandra (AER, HOU, DOM, WAR, BRO, MAT), Nissa (BFZ, AKH, DOM, WAR, MAT), Liliana (SOI, EMN, AER, HOU, DOM, WAR) and Gideon (EMN, WAR oath).
- [Planes Index](Planes%20Index.md) (#74): new detailed entries for **Kaladesh → Avishkar**, **Amonkhet** and **Ixalan**, including the Core of Paradise and Chimil.
- [Contradictions & Retcons Log](Contradictions%20%26%20Retcons%20Log.md): **+3 cited entries** (18 total):
  - Rivals of Ixalan alternate endings vs LCI canon. The Sun Empire ending is canon; this resolves a queued item.
  - Spark loss after the invasion (Nissa, Nahiri, Teferi, Koth, Huatli, Saheeli).
  - Teferi's spark: given up, then a Planeswalker again. ❓ The return is undated.
- Fixes:
  - Inti dies in LCI **Ep. 5**, not Ep. 6.
  - Liliana's Gatewatch oath is now cited from *The Promised End*; the dossier had said it was not covered.
  - The BRO frame outcome now cites Ch. 5 and Ep. 5 directly.
- Every new quote was checked verbatim against the fetched text (0 misses in the new material; the remaining misses are older quotes from uncached profiles, card flavor text and image text). `validate_all.py` PASS. Grixis #63 remains ON HOLD.

## 2026-10-15 — Bot cycle 24 (Phase 6: newest arcs, pre-2019 arcs, dossiers)
Issues [#72](https://github.com/corymstover/GrokBotMTGCompanion/issues/72), [#73](https://github.com/corymstover/GrokBotMTGCompanion/issues/73), [#74](https://github.com/corymstover/GrokBotMTGCompanion/issues/74), [#76](https://github.com/corymstover/GrokBotMTGCompanion/issues/76); milestone 15.

- [Conflicts & Arcs](Conflicts%20%26%20Arcs.md): the **5 newest arcs** are rewritten in Cause · Key beats · Outcome · Lasting consequences · Sources format from every fetched episode plus the Planeswalker's Guide and Legends pages: Tarkir: Dragonstorm (7 eps.), Edge of Eternities (11), Lorwyn Eclipsed (7), Secrets of Strixhaven (6), Reality Fracture (10).
- Pre-2019 arcs: **Kaladesh**, **Amonkhet** and **Ixalan** were rewritten from the 2016–18 web fiction (14 + 12 + 12 episodes). **Alara** got Ajani/Sarkhan beats and **Mirrodin** got the New Phyrexia faction guides. A **new Theros (2013–14) arc** draws on the Born of the Gods / Journey into Nyx guides and the THB summary (⚠️ the *Godsend* novella was not fetched). Totals: **34 arcs** in full format, 40 entries. Master Timeline row 4a added.
- +46 official pages fetched, for **584** in [Lore Primary Sources](Lore%20Primary%20Sources.md). `build_primary_sources.py` gains the THS, KLD/AER, AKH/HOU and XLN/RIX arc codes.
- [Contradictions & Retcons Log](Contradictions%20%26%20Retcons%20Log.md): **+4 cited entries** (15 total):
  - Jace: dead → fragments → dead. This resolves a queued item.
  - Oko's origin revealed (Oona's first avatar).
  - Tam revealed as Jace's creation.
  - Did Bolas create Amonkhet? (Liliana's belief vs later text).
- Fixes:
  - Ixalan profile misquote corrected ("strength of empire, command over nature").
  - Jace's death is now dated to RF Ep. 9, not Ep. 10, and the spark leaves in Ep. 10 (Characters Index).
  - The Lorwyn Eclipsed claim that Ajani said Jace was "unmade" is replaced with the verbatim exchange ("Who died?" / "Jace.").
  - The unverified "Liliana and Vraska carry his body out" line is removed.
- [Planeswalker Dossiers](Planeswalker%20Dossiers.md) (#74 started):
  - New **Tam** dossier.
  - New timeline rows for Jace (Ixalan; LE/RF), Elspeth (Theros 2014), Ajani (Alara, Aether Revolt oath) and Vraska (Ixalan, Reality Fracture).
  - Oko's spark/origin is now cited. Characters Index entries for Oko and Jace are updated.
- Every new quote was checked verbatim against the fetched text (0 misses in the new sections). `validate_all.py` PASS. Grixis #63 remains ON HOLD.

## 2026-10-15 — Bot cycle 23 (lore decks: 85% standard incl. lands)
Cory's request (run before the planned lore cycle, now renumbered cycle 24); follows [#79](https://github.com/corymstover/GrokBotMTGCompanion/issues/79)–[#81](https://github.com/corymstover/GrokBotMTGCompanion/issues/81).

- **Standard raised 60% → 85%** and re-based on **all non-basic cards**: commander + non-land cards + non-basic lands; basics excluded. Counting tests (facts): name, flavor text of any paper printing, story-set printing, or a note citing an official Wizards story page. Mechanical and type echoes are still shown but **no longer count** (guidance). Updated [EDH Lore-Themed Deckbuilding](EDH%20Lore-Themed%20Deckbuilding.md), [EDH Deck Template §8](EDH%20Deck%20Template.md#8-lore-themed-story-first-extension), [Gate L](EDH%20Deck%20Evaluation%20Checklist.md#gate-l--lore-themed-story-first).
- `scripts/build_lore_decks.py`: new classifier, land-aware Lore score section, `--check` fails below 85%; new `validate_all` step **`lore`**; `front_matter.py` adds `lore_score` / `lore_standard_met` to `kind: lore` decks ([Front-Matter Schema](Front-Matter%20Schema.md)).
- Decks rebuilt (Scryfall-verified; still valid, 37 lands, floor 2, 0 Game Changers, no two-card infinites): [Urza](decks/lore-brothers-war-urza-lord-high-artificer.md) 73.8% → **93.8%** (75/80; non-basic lands 17/17), 4 swaps incl. Mishra's Factory, Strip Mine, Tawnos's Coffin, Transmute Artifact. [Nahiri](decks/lore-nahiri-the-lithomancer.md) 64.5% → **86.8%** (66/76; lands 13/13), 15 swaps: Zendikar fetches, Evolving Wilds, Ghost Quarter, Tectonic Edge, Seraph Sanctuary, Everflowing Chalice, Journey to Nowhere, Emeria Shepherd and six story-set Equipment. (Old 60% measure had shown 73% / 76%.)
- `validate_all.py` PASS. Grixis #63 remains ON HOLD.

## 2026-10-15 — Bot cycle 22 (Phase 6: primary-source ingestion & thin arcs)
Issue [#73](https://github.com/corymstover/GrokBotMTGCompanion/issues/73) (P6.2), with [#72](https://github.com/corymstover/GrokBotMTGCompanion/issues/72) (arcs) and [#76](https://github.com/corymstover/GrokBotMTGCompanion/issues/76) (retcons); milestone 15.

- Fetched **538** official story/feature pages from the magic.wizards.com sitemap (incl. **60 Planeswalker's Guides**). The text is cached locally only (`.cache/story/text22/`, gitignored). New generated index: [Lore Primary Sources](Lore%20Primary%20Sources.md) + `data/primary_sources.csv` (`scripts/build_primary_sources.py`).
- [Conflicts & Arcs](Conflicts%20%26%20Arcs.md): **14 arcs** rewritten to Cause · Key beats · Outcome · Lasting consequences from primary text: KHM, STX, MID/VOW, NEO, SNC, DMU, ONE, MOM, WOE, MKM, OTJ, BLB, DSK, DFT. **28 arcs** now use that format (STX, SNC and BLB were re-deepened). All new quotes were matched against the fetched text.
- [Contradictions & Retcons Log](Contradictions%20%26%20Retcons%20Log.md): **+6 cited entries** (11 total): Omenpath term (Kaldheim → Multiverse), Tibalt as Valki, the Wanderer = Emperor of Kamigawa, Tamiyo after compleation, Jace compleated then healed, "Ashiok" on Eldraine was Jace.
- Quote audit of lore pages against the fetched sources: **7 misquotes corrected** (Retcons Log TDM Bolas/Ugin line; Conflicts Emrakul glyph line; Story Arc Summaries ×4; Planeswalker Dossiers Tamiyo line).
- [Master Timeline](Master%20Timeline.md): KHM, MID/VOW, NEO, DMU and MOM rows deepened. [Characters Index](Characters%20Index.md): the Wanderer and Tamiyo cited.
- ⚠️ Flagged gaps: Bloomburrow episodes after Ep. 5 are not in the sitemap; novels/e-books not fetched; Tibalt's KHM fate and the SNC Crescendo sequence are not quoted.
- `validate_all.py` PASS. Grixis #63 remains ON HOLD.

## 2026-10-15 — Bot cycle 21 (Phase 6: lore-themed deckbuilding)
Issues [#79](https://github.com/corymstover/GrokBotMTGCompanion/issues/79)–[#81](https://github.com/corymstover/GrokBotMTGCompanion/issues/81); milestone 15.

- New guide: [EDH Lore-Themed Deckbuilding](EDH%20Lore-Themed%20Deckbuilding.md) (story-first, arc vs character, evidence table, ≥60% lore score, facts vs guidance).
- Worked decks: [Brothers' War — Urza, Lord High Artificer](decks/lore-brothers-war-urza-lord-high-artificer.md) (arc, U, floor 2, story 58/79 = 73%); [Nahiri, the Lithomancer](decks/lore-nahiri-the-lithomancer.md) (character, W, floor 2, story 57/75 = 76%).
- Generator: `scripts/build_lore_decks.py` + `data/lore_decks/lore_decks.json`.
- Template §8 + Gate L on Evaluation Checklist; front_matter `kind: lore` for `lore-*.md`.
- Cross-links from Conflicts & Arcs (Brothers' War, Ancient Eldrazi), Master Timeline, Characters Index (Urza, Nahiri), Planeswalker Dossiers (Nahiri), Planes Index (Dominaria, Zendikar).
- `validate_all.py` PASS (links/schema/index/crossrefs/calibration/citations/oracle/decks/freshness).
- Grixis #63 and other non-lore work remain ON HOLD; Phase 6 lore deepening continues next (Bot cycle 22).

## 2026-10-15 — Bot cycle 20 (Phase 6: lore deepening — timeline & arcs, retcon log)

> All entries are **Bot cycle 20** (Grok Bot) changes on branch `bot-cycle20-lore-timeline`. Milestone: [Phase 6 — Lore deepening sprint](https://github.com/corymstover/GrokBotMTGCompanion/milestone/15). Other queued work (#63) on hold per Cory's brief.

| # | Change | Files | Issue |
|---|---|---|---|
| 20.1 | **Conflicts & Arcs deepened**: 13 major H2 arcs (Ancient Eldrazi → Return to Dominaria/WAR) rewritten to **Cause · Key beats · Outcome · Lasting consequences · Sources**, plus 4 thin H3s (ZNR, STX, SNC, BLB). 17 arcs now carry an explicit cause and consequences. Earlier accurate content kept; anchors unchanged. Unfetched material flagged ⚠️. Sources re-fetched 2026-10-15: 10 plane profiles, BFZ and Tarkir block summaries, PW Guides (Fate Reforged, Dominaria 2022), Chronicle of Bolas: The Unwritten Now, The Promised End, Hour of Devastation, Revolution Begins. | `Conflicts & Arcs.md` | [#72](https://github.com/corymstover/GrokBotMTGCompanion/issues/72) |
| 20.2 | **Master Timeline deepened**: era summaries with lasting consequences on all 6 era tables; the Post-Mending table gains an *Outcome / lasting* column (18 rows); retcon log cross-links. | `Master Timeline.md` | [#72](https://github.com/corymstover/GrokBotMTGCompanion/issues/72) |
| 20.3 | **New [Contradictions & Retcons Log](Contradictions%20%26%20Retcons%20Log.md)** skeleton: 5 seeded, cited entries (Tarkir rewrite, Kaladesh→Avishkar, AR expansion, Emrakul's path, Bolas after WAR), 5 queued candidates, schema of fields/flags. Registered in front-matter. | `Contradictions & Retcons Log.md`, `scripts/front_matter.py` | [#76](https://github.com/corymstover/GrokBotMTGCompanion/issues/76) |
| 20.4 | Milestone 15 and issues #72–#77 (P6.1–P6.6) opened; dashboards updated. | README, Progress Tracker, ROADMAP, Knowledge Index | [#77](https://github.com/corymstover/GrokBotMTGCompanion/issues/77) |

## 2026-10-15 — Bot cycle 19 (Phase 5 complete: bracket calibration & pilot notes)

> All entries are **Bot cycle 19** (Grok Bot) changes on branch `bot-cycle19-calibration`, issue [#68](https://github.com/corymstover/GrokBotMTGCompanion/issues/68). Closes the Phase 5 milestone; snapshot `v2.0-phase5-optimization`.

| # | Summary | Files affected | Reason |
|---|---|---|---|
| 19.1 | **Bracket calibration & pilot notes** block in all 86 decks (after *Bracket assessment*): floor-rationale table (Game Changers, mass land denial, extra turns, two-card infinites from the deck's Spellbook block, tutors as information only since the Oct 2025 update), the calibrated floor and what sets it, context (Grixis stated target vs floor; EDHREC community bracket shares for core decks; combos one card away), lower-bracket cut paths (guidance; minimum cut set that breaks every two-card infinite), and pilot notes (guidance) built on facts: lands, ramp, average MV, exact opening-hand odds, interaction budget, combo lines and the tutors that find them, pregame talk. Grixis decks point to the source author's verbatim reasoning. | `decks/*.md`, `grixis/decks/*.md`, `scripts/deck_calibration.py` (new), `data/deck_calibration.json` (new) | The user asked for floor rationale, Game Changers, combos and pilot tips labeled as guidance on every deck. |
| 19.2 | Core decks' stale bullet *"Two-card infinite combos: ⚠️ not machine-checked"* (written before Spellbook detection existed) replaced with the actual count and pairs in 46 decks. | `decks/*.md` | Correctness: Spellbook data was already on the page. |
| 19.3 | **[EDH Bracket Calibration](EDH%20Bracket%20Calibration.md)**: one row per deck (floor, GC, two-card infinites, MLD, extra turns, tutors, lands, average MV, stated target, EDHREC mode), summary and method. Results: floors B2 **10** · B3 **30** · B4 **46** (all equal to the existing front-matter floors); 146 two-card infinites in 37 decks; 1 MLD deck (Grixistax, *Back to Basics*); 17 decks with extra-turn cards; 0 Grixis stated targets below the floor. | `EDH Bracket Calibration.md` (new), `scripts/front_matter.py`, `EDH Standards.md` | Calibration across all material in one place. |
| 19.4 | `validate_all.py` gains the `calibration` step (`deck_calibration.py --check`). Docs: README (Phase 5 complete, commands, key files, releases), Lookup Guide, Knowledge Index, Progress Tracker, ROADMAP, Knowledge Snapshots (`v2.0-phase5-optimization`). | `scripts/validate_all.py`, listed docs | Single gate stays complete; dashboards current. |

## 2026-10-15 — Bot cycle 18 (Phase 5: cross-references)

> All entries are **Bot cycle 18** (Grok Bot) changes on branch `bot-cycle18-crossrefs`, issue [#66](https://github.com/corymstover/GrokBotMTGCompanion/issues/66). Everything is generated by `scripts/build_crossrefs.py` (idempotent; `--check` is step 4 of `validate_all.py`).

| # | Summary | Files affected | Reason |
|---|---|---|---|
| 18.1 | **Reverse card index** `references/` (README + 28 letter pages): for each of **8,468** cards cited outside the card shards, every page and section citing it, grouped as decks · EDH guides · rules · lore & story · card data · meta (18,631 card–page links; Card Index excluded). `data/card_refs.json` holds the counts; `kb_find.py "Card"` prints them. | `references/*.md` (new), `data/card_refs.json` (new), `scripts/build_crossrefs.py` (new), `scripts/kb_find.py` | Card → everything that cites it, without bloating shards. |
| 18.2 | **One *Referenced in* line per cited card entry** (8,468 lines in 564 shards): page count by kind + link to the reverse-index section. `ingest_scryfall.render_entry` renders the identical line from `data/card_refs.json`, so re-ingests keep it (tested on Sol Ring, Jace Beleren, Cyclonic Rift). | `cards/**`, `scripts/ingest_scryfall.py` | The back-link from cards to decks, packages, rules and lore. |
| 18.3 | **Deck *Cross-references* block** in all 86 decks: EDH Packages sub-packages present (Oracle-pattern matches with the same patterns), keywords → Keyword Encyclopedia anchors, rules / lore & story / EDH-guide sections that cite cards in the list, and the 4 decks sharing the most cards. | `decks/*.md`, `grixis/decks/*.md` | Deck → packages, rules topics, story spotlight and sibling decks. |
| 18.4 | **EDH Packages *Used in decks*** lines on 28 of 33 sub-packages (decks with ≥ 3 matching cards), from `data/deck_packages.json`; `build_packages.py` reads it on every run. | `EDH Packages.md`, `scripts/build_packages.py`, `data/deck_packages.json` (new) | Package → decks (the reverse of 18.3). |
| 18.5 | **Character cards (name-matched)** tables: Characters Index (77 of 78 characters, 417 card links) and Planeswalker Dossiers (21 of 21, 199 links). Legendary cards whose Scryfall name is or starts with the character's name; labeled as a name match, not a canon claim. Group headings are split into names; `Mirri` is skipped inside the Sothera group (those cards are the Weatherlight's Mirri). | `Characters Index.md`, `Planeswalker Dossiers.md` | Lore → cards and back (through *Referenced in*). |
| 18.6 | **Keyword Encyclopedia examples linked**: 1,077 `[[Card]]` placeholders were never resolved after Bot cycle 9; resolved now, and `build_keywords.py` resolves them on every run. | `Keyword Encyclopedia.md`, `scripts/build_keywords.py` | Rules topics → cards (and back). |
| 18.7 | Front-matter kind **`reference`** for `references/` pages; schema page, Lookup Guide (reverse index, packages, character cards), Knowledge Index, Card Data Conventions, README, Progress Tracker, ROADMAP updated. | `scripts/front_matter.py`, `Front-Matter Schema.md`, listed docs | Schema covers the new pages; docs stay current. |

## 2026-10-15 — Bot cycle 17 (Phase 5: schema v2, retrieval index, validate_all)

> All entries are **Bot cycle 17** (Grok Bot) changes on branch `bot-cycle17-schema-validation`, for the user's optimization-pass task. Milestone: [Phase 5 — Optimization pass](https://github.com/corymstover/GrokBotMTGCompanion/milestone/14).

| # | Summary | Files affected | Reason |
|---|---|---|---|
| 17.1 | **Front-matter schema v2** ([#65](https://github.com/corymstover/GrokBotMTGCompanion/issues/65)): one typed `SCHEMA` for pages, decks and card shards. `--check` now validates types (int/bool/list/enum), kebab-case tags, source keys, generator paths and related-page registration, plus staleness. Decks gain `combos`, `two_card_infinites` and computed `tags` (kind, identity name, `bracket-floor-N`, Game Changer/combo flags, plane/theme) and a `theme` key; `color_identity` is now always WUBRG order (it was alphabetical for the 46 core decks, e.g. `BRW` → `WBR`). Pages gain `related` (up to 6 pages from the link graph) and `schema`. **684 card shards** now carry front-matter (`ingest_scryfall.py` calls `front_matter.apply_shards()` after each render). | `scripts/front_matter.py`, `scripts/ingest_scryfall.py`, all 45 pages, 86 decks, 684 shards | Consistent, machine-checkable metadata on every major entry. |
| 17.2 | **[Front-Matter Schema](Front-Matter%20Schema.md)** generated from the script: key tables per kind, source keys, the page and deck tag vocabulary with counts, validation rules and filter commands. `--check` fails if it is stale. | `Front-Matter Schema.md` (new) | A documented schema that cannot drift from the enforcement code. |
| 17.3 | **Retrieval index**: `scripts/kb_find.py --build` writes `data/kb_index.json` (131 pages and decks, every `##`/`###` heading with its anchor); `kb_find.py "query"` ranks by title, tag, commander and heading, filters by `--category`/`--tag`, and resolves exact card names to their entries. | `scripts/kb_find.py`, `data/kb_index.json` (new), `Lookup Guide.md` | Faster, section-level lookups. |
| 17.4 | **Citation check** ([#67](https://github.com/corymstover/GrokBotMTGCompanion/issues/67)): every Wizards URL in any .md (725) must be in the official sitemap (674), resolve (14, incl. 11 redirects) or be a resolving Internet Archive copy (37); every `CR nnn.nx` citation (478 distinct rules) must exist in the cached CR 2026-09-25. Results in `data/citations.json`; offline by default, `--online` re-tests all, `--recheck` only new/broken. First run found no dead citations: the 5 `http://` URLs inside verbatim Scryfall ruling text resolve over https, and the Wayback timeouts were transient (availability-API fallback added). | `scripts/check_citations.py`, `data/citations.json` (new) | Every cited source is reachable. |
| 17.5 | **`scripts/validate_all.py`**: one entry point for links, schema, retrieval index, cross-refs (from cycle 18), citations, Oracle drift (`verify_cards.py`), deck re-checks (all 86 lists re-validated, plus Game Changer drift vs the stored count) and generator freshness. Offline by default via the new `SCRYFALL_OFFLINE=1` mode in `ingest_scryfall.get_bulk` (newest cached bulk, dated from its file name); `--online` verifies against Scryfall's newest bulk and live citations. Result: **all steps PASS**. | `scripts/validate_all.py` (new), `scripts/ingest_scryfall.py` | A single gate before every merge. |
| 17.6 | Docs: README (area row, commands, key files), Lookup Guide (kb_find, validation, WUBRG identity filter fix), Knowledge Index, Card Data Conventions, Progress Tracker, ROADMAP (Phase 5 table). | listed files | Dashboards stay current. |

## 2026-10-15 — Bot cycle 16 (Grixis integration)

> All entries in this section are **Bot cycle 16** (Grok Bot) changes, on branch `bot-cycle16-grixis`. The source, [corymstover/grixis-commander-encyclopediaGPT](https://github.com/corymstover/grixis-commander-encyclopediaGPT) at commit `df1abb9`, was cloned read-only to `/workspace/grixis-src` and not modified.

| # | Summary | Files affected | Reason |
|---|---|---|---|
| 16.1 | Bot cycle 16: **evaluated all 62 Grixis source lists** against our card DB. The current list is the user-approved one where the source state file has it (40), else the frozen FINAL baseline (22). Checks: name resolution, eligibility and pairing, 100 cards, singleton with Oracle copy exceptions, identity, legality and bans, companion, Game Changers; plus 16,137 source Oracle-text rows vs current Oracle (0 outdated). | `scripts/grixis_eval.py`, `data/grixis_eval.json`, `grixis/Grixis Evaluation.md` | #59 |
| 16.2 | Bot cycle 16: **integrated 40 decks** into `grixis/decks/`. Each has a commander block, validation, GC and bracket floor, corrections, Archidekt list, card breakdown with the source's role tags and printings, the source blueprint, decisions, approval and evidence **quoted verbatim with path attribution**, and Commander Spellbook combos (288; 83 two-card infinite in 19 decks). Left out: 20 lists still UNREFINED in the source and 2 future-release (`mbc`) lists. | `scripts/build_grixis.py`, `grixis/README.md`, `grixis/decks/*.md` (40), `data/grixis_combos.json`, `data/grixis_summary.json` | #59 |
| 16.3 | Bot cycle 16: **87 corrections logged**. Bjorna + Cecily: Trade Secrets → Wizard Class and Yawgmoth's Bargain → Flame of Anor (banned; both replacements are close alternatives from the source dossier); Lutri companion dropped. Game Changer counts and floors added to all 40 (the source never tracks them). List-format normalization on 40 decks (3,581 role tags restored from the source baseline). 2 provenance notes (approved hash matches no file). 2 low-land structure flags (guidance). | `grixis/Grixis Corrections.md`, deck pages | #60 |
| 16.4 | Bot cycle 16: **Grixis package library**: cards shared by 4 or more of the 40 lists by role, with identity, MV and GC, plus 4 source rules insights checked against Oracle text and CR 118.9a/d. | `grixis/Grixis Packages.md` | #61 |
| 16.5 | Bot cycle 16: **generalized the Grixis method** for any identity: [EDH Deck Template](EDH%20Deck%20Template.md) (blueprint, role map, swap ledger, rubric, finalization record), [EDH Deck Evaluation Checklist](EDH%20Deck%20Evaluation%20Checklist.md) (gates A–E), `scripts/evaluate_decklist.py` (shared evaluator, also used by the Grixis import). EDH Standards gains the method summary, an official-legality-vs-house-exceptions rule and checklist step 7. Its stale open question on combo detection is fixed. | `EDH Deck Template.md`, `EDH Deck Evaluation Checklist.md`, `scripts/evaluate_decklist.py`, `EDH Standards.md` | #62 |
| 16.6 | Bot cycle 16: front-matter registry extended (7 new pages; `grixis/decks` as `kind: grixis` with `source_repo`; unregistered pages in `grixis/` now fail `--check`). Dashboard, tracker, index, lookup guide, roadmap and snapshots updated. Milestone 13 and issues #59–#63 opened. | `scripts/front_matter.py`, `README.md`, `Progress Tracker.md`, `Knowledge Index.md`, `Lookup Guide.md`, `ROADMAP.md`, `Knowledge Snapshots.md` | #59–#63 |

## 2026-10-15 — Bot cycle 15 (Phase 4 complete; duplicate cleanup)

> All entries in this section are **Bot cycle 15** (Grok Bot) changes, on branch `bot-cycle15`.

| # | Summary | Files affected | Reason |
|---|---|---|---|
| 15.1 | Bot cycle 15: **duplicate cleanup**. My commit 5f899da (labelled "Bot cycle 9") landed on main after the parallel Bot cycle 9–14 PRs (#51–#57) had already logged the same Phase 3 work. Removed its duplicate Update Log section, the duplicate Progress Tracker rows (3 card rows, 1 legality row), 4 duplicate Knowledge Index rows and a duplicate README key-files row. ROADMAP now credits #40–#43 to the cycles that merged them (10–13, PRs #52–#55). No generated page or data file was changed. | `Update Log.md`, `Progress Tracker.md`, `Knowledge Index.md`, `README.md`, `ROADMAP.md` | dedupe |
| 15.2 | Bot cycle 15: **YAML front-matter** on 37 major pages and 46 decks. Pages: title, category, tags, issues, generator, sources. Decks: kind, commander, identity, bracket floor (combo-adjusted), GC count, validated, all parsed from the deck body. `scripts/front_matter.py --check` verifies presence, required keys and staleness. Lookup Guide gains a filter section. | `scripts/front_matter.py`, all registry pages, `decks/*.md`, `Lookup Guide.md` | #44 |
| 15.3 | Bot cycle 15: **FAQ**, 29 Q&As (9 lore, 9 rules, 7 Commander, 4 cards & collecting). Each answer summarizes existing cited pages and links to the exact section. | `FAQ.md` | #45 |
| 15.4 | Bot cycle 15: **Knowledge Snapshots**: tag policy plus all 14 snapshots with commits. Created the missing `v1.7-cycle9-phase3-complete` on 63dbeb7 (PR #55 merge) and closed the Phase 3 milestone. `v1.8-cycle15-phase4-complete` goes on this cycle's merge. | `Knowledge Snapshots.md` | #47 |
| 15.5 | Bot cycle 15: README (Phase 4 complete; queued follow-ups noted as not started), Progress Tracker, Knowledge Index, ROADMAP, Update Log. | `README.md`, `Progress Tracker.md`, `Knowledge Index.md`, `ROADMAP.md`, `Update Log.md` | docs |

## 2026-10-15 — Bot cycle 14 (Phase 4: Lookup Guide)

> **Bot cycle 14** (Grok Bot): closed [#46](https://github.com/corymstover/GrokBotMTGCompanion/issues/46) and synced the dashboard after the Lookup Guide landed.

| # | Summary | Files affected | Reason |
|---|---|---|---|
| 14.1 | Bot cycle 14: mark Lookup Guide ✅ on ROADMAP/README/Progress Tracker and close the open-issue wording for #46. | `Lookup Guide.md`, `README.md`, `Progress Tracker.md`, `ROADMAP.md`, `Update Log.md` | #46 |

## 2026-10-15 — Bot cycle 13 (Phase 3 complete: Artist Index)

> All entries in this section are **Bot cycle 13** (Grok Bot) changes, on branch `bot-cycle13`.

| # | Summary | Files affected | Reason |
|---|---|---|---|
| 13.1 | Bot cycle 13: **Artist Index** for [#43](https://github.com/corymstover/GrokBotMTGCompanion/issues/43). **2,440** artists and **50,956** artist-illustration credits from Scryfall default-cards. CSV plus alphabetical Markdown with most-prolific list and top cards by EDHREC. Joint credits count for each artist; alternate spellings are flagged ⚠️. | `Artist Index.md`, `data/artists.csv`, `scripts/build_artists.py` | #43 |
| 13.2 | Bot cycle 13: corrected Tokens noncreature count (105, not 133) after a cleaner Scryfall filter, and closed Phase 3 on the dashboard. | `Tokens, Emblems & Dungeons.md`, `scripts/build_tokens.py`, `data/tokens.json`, docs | Accuracy |
| 13.3 | Bot cycle 13: README, Progress Tracker, Knowledge Index, ROADMAP, Update Log (**Phase 3 complete**; Phase 4 #44–#47 next). | `README.md`, `Progress Tracker.md`, `Knowledge Index.md`, `ROADMAP.md`, `Update Log.md` | docs |

## 2026-10-15 — Bot cycle 12 (Phase 3: Tokens, Emblems & Dungeons)

> All entries in this section are **Bot cycle 12** (Grok Bot) changes, on branch `bot-cycle12`.

| # | Summary | Files affected | Reason |
|---|---|---|---|
| 12.1 | Bot cycle 12: **Tokens, Emblems & Dungeons** for [#42](https://github.com/corymstover/GrokBotMTGCompanion/issues/42). Structured `data/tokens.json` plus Markdown tables: 780 creature tokens, 105 noncreature tokens, 89 emblems, 5 dungeons, and 159 adventurer cards (real cards, CR 715). Marked 🚫 not cards where they cannot go in a deck (CR 111.1, 114.1, 309.2). Creators linked via Scryfall `all_parts`. | `Tokens, Emblems & Dungeons.md`, `data/tokens.json`, `scripts/build_tokens.py` | #42 |
| 12.2 | Bot cycle 12: README, Progress Tracker, Knowledge Index, ROADMAP, Update Log (#42 ✅; Phase 3 left with #43). | `README.md`, `Progress Tracker.md`, `Knowledge Index.md`, `ROADMAP.md`, `Update Log.md` | docs |

## 2026-10-15 — Bot cycle 11 (Phase 3: Format Legality Matrix)

> All entries in this section are **Bot cycle 11** (Grok Bot) changes, on branch `bot-cycle11`.

| # | Summary | Files affected | Reason |
|---|---|---|---|
| 11.1 | Bot cycle 11: **Format Legality Matrix** for [#41](https://github.com/corymstover/GrokBotMTGCompanion/issues/41). CSV of 33,894 cards × 23 Scryfall formats (L/N/B/R). Markdown page: per-format totals and complete banned/restricted lists (1,390 entries across 21 formats). Notes that non-Wizards formats have their own committees ⚠️, and that Commander still needs color identity and singleton rules. | `Format Legality Matrix.md`, `data/legality_matrix.csv`, `scripts/build_legality.py` | #41 |
| 11.2 | Bot cycle 11: README, Progress Tracker, Knowledge Index, ROADMAP, Update Log (#41 ✅; Phase 3 continues with #42–#43). | `README.md`, `Progress Tracker.md`, `Knowledge Index.md`, `ROADMAP.md`, `Update Log.md` | docs |

## 2026-10-15 — Bot cycle 10 (Phase 3: Printing History)

> All entries in this section are **Bot cycle 10** (Grok Bot) changes, on branch `bot-cycle10`.

| # | Summary | Files affected | Reason |
|---|---|---|---|
| 10.1 | Bot cycle 10: **Printing History** for [#40](https://github.com/corymstover/GrokBotMTGCompanion/issues/40). One CSV row per card entry (33,894) with paper/digital printing counts, first/latest set, longest gap, set-type mix and Reserved List flag. The Markdown page covers distribution, most-printed cards, longest gaps, single-printing Commander staples and the Reserved List (571 entries). Kept outside card shards so entries stay compact. | `Printing History.md`, `data/printings_summary.csv`, `scripts/build_printings.py` | #40 |
| 10.2 | Bot cycle 10: README, Progress Tracker, Knowledge Index, ROADMAP, Update Log (#40 ✅; Phase 3 continues with #41–#43). | `README.md`, `Progress Tracker.md`, `Knowledge Index.md`, `ROADMAP.md`, `Update Log.md` | docs |

## 2026-10-15 — Bot cycle 9 (Phase 3: Keyword Encyclopedia complete)

> All entries in this section are **Bot cycle 9** (Grok Bot) changes, on branch `bot-cycle9`.

| # | Summary | Files affected | Reason |
|---|---|---|---|
| 9.1 | Bot cycle 9: **Keyword Encyclopedia** finish for [#39](https://github.com/corymstover/GrokBotMTGCompanion/issues/39). Added **44** status labels (🌲 evergreen / 🍂 deciduous / 🍁 retired from evergreen / mill note) only where official Wizards articles name the term (Evergreen Eggs & Ham 2015, Introducing Ward 2021, Deciduous 2022, M21 release notes). Everything else stays unlabeled. Added shared WotC **ruling excerpts** on **217** entries (top shared comments among that keyword's cards). | `Keyword Encyclopedia.md`, `scripts/build_keywords.py` | #39 |
| 9.2 | Bot cycle 9: README dashboard, Progress Tracker, Knowledge Index, ROADMAP tracking table, Update Log (#39 ✅; Phase 3 continues with #40–#43). | `README.md`, `Progress Tracker.md`, `Knowledge Index.md`, `ROADMAP.md`, `Update Log.md` | docs |

## 2026-10-15 — Bot cycle 8 (Phase 2 complete; Phase 3 keyword encyclopedia started)

> All entries in this section are **Bot cycle 8** (Grok Bot) changes, on branch `bot-cycle8`.

| # | Summary | Files affected | Reason |
|---|---|---|---|
| 8.1 | Bot cycle 8: **Story Arc Summaries**, 19 arcs and 135 beats (was 7 / 52). Added BFZ/OGW, SOI/EMN, KLD/AER, AKH/HOU, DOM, WAR, WOE, LCI, DFT, EOE, ECL, SOS and Reality Fracture, each beat with an episode citation and verbatim quotes. ⚠️ flags: SOS (the white-robed man is Jace only by implication) and EOE (interactive structure). ❓ RF: Jadzi's fate. | `Story Arc Summaries.md` | #34 |
| 8.2 | Bot cycle 8: **corrections in Conflicts & Arcs**. The BFZ and Innistrad outcome ⚠️ flags are replaced with sourced statements (the leyline fire destroys Ulamog and Kozilek; Emrakul is bound in the silver moon, per *The Promised End*). | `Conflicts & Arcs.md` | #34 |
| 8.3 | Bot cycle 8: **Planeswalker Dossiers**, 21 (was 13). Added Gideon, Nahiri, Sorin, Ugin, Nicol Bolas, Ral Zarek, Oko and Tezzeret. Newly sourced spark moments: Gideon (Kytheon origin), Sorin (VOW Ep. 4), Ugin and Bolas (*Chronicle of Bolas*), plus Karn's partial (Venser's spark, DMU Ep. 1; the Echoverse Mishra version is 🚫). Remaining ❓ are listed. | `Planeswalker Dossiers.md` | #35 |
| 8.4 | Bot cycle 8: **Art & Flavor Story Links** (generator). 269 Story Spotlight cards in 17 arcs with verbatim Scryfall flavor and artist. 32 link to the official story page that captions their art (the artist must match). Also 263 captioned cards on 53 cited story pages. 1,716 captions harvested from the lore corpus. | `Art & Flavor Story Links.md`, `scripts/build_art_flavor.py`, `data/story_art_captions.csv` | #37 |
| 8.5 | Bot cycle 8: **Side-Media Index**. 22 items (novels, e-book collections, comics, D&D adventure, 1994 short story, Netflix series), with relevance notes and quotes from official Wizards pages. Partner sources are ⚠️ and gaps ❓ (e.g. IDW comics, the *Wildered Quest* author). | `Side-Media Index.md` | #38 |
| 8.6 | Bot cycle 8: **Keyword Encyclopedia** (Phase 3 start, generator). 194 CR 702 abilities and 70 CR 701 actions, with verbatim definitions, card counts, earliest printing and 3 Commander-legal examples each (their entries carry the rulings). ✅ marks come from Wizards' Common Keywords glossary; no evergreen label was invented. | `Keyword Encyclopedia.md`, `scripts/build_keywords.py` | #39 |
| 8.7 | Bot cycle 8: README dashboard, Progress Tracker (Phase 2 closed, Phase 3 open), Knowledge Index, ROADMAP tracking table, Update Log. | `README.md`, `Progress Tracker.md`, `Knowledge Index.md`, `ROADMAP.md`, `Update Log.md` | docs |

## 2026-10-15 — Bot cycle 7 (Phase 1 complete; Phase 2 lore depth started)

> All entries in this section are **Bot cycle 7** (Grok Bot) changes, on branch `bot-cycle7` (commit 2b629f0 and the lore/docs commit).

| # | Summary | Files affected | Reason |
|---|---|---|---|
| 7.1 | Bot cycle 7: **EDH Upgrade Paths**. For 32 commanders, EDHREC budget vs expensive pages; an upgrade is an inclusion delta ≥ 0.10. Rows are grouped into Step 1 ≤ $5, Step 2 $5–20, Step 3 > $20, with likely cuts and a bracket note. 576 upgrade rows (58 GC), 256 cuts; every card is legality- and identity-checked. | `EDH Upgrade Paths.md`, `data/upgrade_paths.json`, `scripts/build_upgrade_paths.py` | #30 |
| 7.2 | Bot cycle 7: deck builder gains `--sets`/`--plane` (paper printings in the plane's sets only; filler is labeled) and `--theme` (EDHREC theme pages). **10 plane-restricted decks** (Innistrad, Ravnica, Zendikar, Kamigawa, Theros, Eldraine, Ixalan, Tarkir, Dominaria, Mirrodin/New Phyrexia) and **4 themed decks** (Atraxa planeswalkers, Muldrotha self-mill, Chulane landfall, Edgar Markov lifegain). All validate at 100 cards. | `scripts/build_deck_skeleton.py`, `decks/plane-*.md`, `decks/theme-*.md`, `EDH Themed Decks.md`, `scripts/build_themed_index.py` | #33 |
| 7.3 | Bot cycle 7: reran combo detection and rules notes for the 46 decks: 218 combos, 63 two-card infinites in 18 decks (was 189 / 51 / 14). Braids' plane deck floor rose 2 → 3 (Sheoldred + Lich's Mastery). | `data/combos.json`, `decks/*.md` | #15 upkeep |
| 7.4 | Bot cycle 7: **Story Arc Summaries**. 7 arcs and 52 beats (ONE, MOM, MKM, OTJ, BLB, DSK, TDM), each with an episode citation and verbatim quotes, plus outcome and lasting consequences. Gaps are marked ❓. | `Story Arc Summaries.md` | #34 |
| 7.5 | Bot cycle 7: **Planeswalker Dossiers**. 13 dossiers with identity, spark moment, cited timeline, allegiances and a status link. | `Planeswalker Dossiers.md` | #35 |
| 7.6 | Bot cycle 7: **Omenpath & Multiverse Connections**. The term's 2021 Kaldheim origin vs post-invasion portals, known connections, infrastructure, artificial paths, Loot's map and open questions. | `Omenpath & Multiverse Connections.md` | #36 |
| 7.7 | Bot cycle 7: **correction**. The MKM outcome in Conflicts & Arcs said "Teysa turns out to be alive". MKM Ep. 10 says she was "Murdered by a grief-poisoned Trostani" and her ghost remains with Kaya. Fixed, with cross-links to the new lore files. | `Conflicts & Arcs.md`, `Characters Index.md` | Accuracy |
| 7.8 | Bot cycle 7: README dashboard (also fixed a malformed status/key-files table), Progress Tracker, Knowledge Index, ROADMAP tracking table, Update Log. | `README.md`, `Progress Tracker.md`, `Knowledge Index.md`, `ROADMAP.md`, `Update Log.md` | Keep the dashboard current |

## 2026-10-15 — Bot cycle 6 (ROADMAP Phase 1: EDH & deckbuilding depth)

> All entries in this section are **Bot cycle 6** (Grok Bot) changes. The commits are ef3084d, 5075887 and the docs commit, all on branch `bot-cycle6`.

| # | Summary | Files affected | Reason |
|---|---|---|---|
| 6.1 | Bot cycle 6: **ROADMAP**. The user's refinement brief is copied verbatim with a tracking table. Created label `structure`, 4 milestones (one per phase) and 23 issues (#25–#47, one per bullet). | `ROADMAP.md`, `README.md`, `Knowledge Index.md` | User request: make sprint progress visible on GitHub. |
| 6.2 | Bot cycle 6: shared generator library `edh_lib.py`. The pool is the 32,116 Commander-legal indexed cards; the cheapest paper USD comes from Scryfall default-cards bulk. A standard header covers legality, identity, the GC/brackets flag, the price snapshot and the guidance label. | `scripts/edh_lib.py` | Every guide applies the same legality and identity rules. |
| 6.3 | Bot cycle 6: **EDH Mana Bases**. Land-count guidance (36–38 lands, about 10 ramp), universal fixing, 7 colorless utility categories, and for each of the 32 identities the most-played lands (by land type), on-color fetches and budget (≤ $1) picks. 1,118 non-basic lands. | `EDH Mana Bases.md`, `scripts/build_mana_bases.py` | #25 |
| 6.4 | Bot cycle 6: **EDH Packages**. 13 packages, 33 sub-packages, 321 rows. Each sub-package shows its Oracle-text pattern, match count, GC count and budget alternatives. | `EDH Packages.md`, `scripts/build_packages.py` | #26 |
| 6.5 | Bot cycle 6: **EDH Win Conditions**. 8 categories, 146 rows, plus 46 two-card combo kills from `data/combos.json` with Spellbook links. CR 704.5a–c are cited for the loss conditions. | `EDH Win Conditions.md`, `scripts/build_wincons.py` | #27 |
| 6.6 | Bot cycle 6: **EDH Interaction**. 6 hierarchies (targeted removal, wipes, stack, graveyard hate, artifact/enchantment hate, stax), 19 buckets, 183 rows with speed column. Mass land denial is flagged as not allowed at Brackets 1–3. | `EDH Interaction.md`, `scripts/build_interaction.py` | #28 |
| 6.7 | Bot cycle 6: **cEDH Primer**, a separate file with a COMPETITIVE / Bracket 5 banner. Fast mana, tutors, free interaction, stax (129 rows) and 61 compact combos from Commander Spellbook `find-my-combos` (cached in `data/cedh_combos.json`; all cards Commander-legal). It notes that Mana Crypt, Dockside Extortionist, Jeweled Lotus and Nadu are banned per Scryfall. | `cEDH Primer.md`, `scripts/build_cedh.py`, `data/cedh_combos.json` | #29 |
| 6.8 | Bot cycle 6: **EDH Pairings**. CR 702.124 rules, card and legal-pair counts for 8 partner abilities (3,104 legal pairs), a 32-identity matrix, and the most-played pair per identity. | `EDH Pairings.md`, `scripts/build_pairings.py` | #32 |
| 6.9 | Bot cycle 6: **EDH Mulligans**. CR 103.5/103.5c/103.6 quoted from the cached CR. Exact hypergeometric land and key-piece odds for 99 cards, 19 opening-hand cards, and keep/mulligan plus per-archetype priorities (12 archetypes, labeled guidance). | `EDH Mulligans.md`, `scripts/build_mulligans.py` | #31 |
| 6.10 | Bot cycle 6: README dashboard, run commands and releases; Progress Tracker; Knowledge Index; Update Log. | `README.md`, `Progress Tracker.md`, `Knowledge Index.md`, `Update Log.md` | Keep the dashboard current. |

## 2026-10-15 — Bot cycle 5 (sprint: rules topics, remaining planes, story archive, maintenance)

> All entries in this section are **Bot cycle 5** (Grok Bot) changes. Sprint mode: the only committing process.

| # | Summary | Files affected | Reason |
|---|---|---|---|
| 5.1 | Bot cycle 5: **Rules Interactions 17 → 27 topics**: sagas (714), classes (716), phasing (702.26), DFCs/transform (712/701.27), legend rule (704.5j), "can't" beats "can" (101.2–101.4), replacement-effect ordering (616 + 614.15), commander damage (903.10a/704.6c), partner & Backgrounds (702.124), and leaving a multiplayer game (800.4). Now 37 official CR examples (was 20) and 139 linked rulings (was 87). Topics with no matching official ruling say so instead of using weak matches. | `Rules Interactions.md`, `scripts/build_rules_interactions.py` | Issue #9. |
| 5.2 | Bot cycle 5: **Planes Index 18 → 23 detailed entries**. Mercadia and Ulgrotha are now ✅ sourced from Wizards' *The Known Multiverse* (2008); the official pages still 404, and no archived copy was needed. Added Ergamon (*Known Multiverse* + Rosewater's *Choosing Your Battles, Part 3*), Zendikar (ZNR guide + Ep. 1/5), Kamigawa (NEO Planeswalker's Guide + Ep. 1/5), Dominaria (DMU Planeswalker's Guide + Ep. 1/5), and the Arcavios colleges table (SOS Planeswalker's Guide; color pairs from Scryfall Campus lands). Vryn's mage-rings and factions are sourced from *The Worlds of Magic Origins* and *Absent Minds*. | `Planes Index.md` | Issue #12. |
| 5.3 | Bot cycle 5: **story archive index**. The Wayback Machine CDX lists 292 Uncharted Realms slugs and 193 old magic-story slugs (the first CDX results page; the full query timed out). Each one is fetched live if it still resolves, otherwise from a 🗄️ archived snapshot. **612 pages indexed** (575 live, 37 archived); 104 candidates were unresolved, mostly translations or listing pages. No full text is committed. | `scripts/crawl_story_index.py`, `data/story_index.csv`, `Story Archive Index.md` | Issue #14. |
| 5.4 | Bot cycle 5: **maintenance**. `ingest_scryfall.py` refresh against the newest Scryfall bulk (2026-10-15 09:02 UTC; no newer bulk published): 0 new and 0 changed cards. Commander Spellbook re-run: 189 combos and 51 two-card infinites, unchanged. Deck legality recheck: 3,200 cards across 32 decks, 0 not Commander-legal. | `data/ingest_state.json`, `README.md`, `Progress Tracker.md`, `decks/*` | Issue #17. |
| 5.5 | Bot cycle 5: README dashboard, Progress Tracker, Knowledge Index and Update Log refreshed; milestones updated. | `README.md`, `Progress Tracker.md`, `Knowledge Index.md`, `Update Log.md` | Keep the dashboard current. |

## 2026-10-15 — Bot cycle 4 (sprint: rules topics, Planeswalker review, ELD/THB/IKO sources, combos & archetypes)

> All entries in this section are **Bot cycle 4** (Grok Bot) changes. Sprint mode: the only committing process.

| # | Summary | Files affected | Reason |
|---|---|---|---|
| 4.1 | Bot cycle 4: **Rules Interactions 7 → 17 topics**: stack & priority, casting vs. copying, combat damage, deathtouch + trample, protection, hexproof/shroud/ward, ETB/LTB look-back, mutate/merge, commander tax, worked layer examples. CR 2026-09-25 is quoted verbatim. The generator now attaches the CR's own *Example* paragraphs: 20 official examples (was 0) and 87 linked rulings (was 35). | `Rules Interactions.md`, `scripts/build_rules_interactions.py` | Issue #9. |
| 4.2 | Bot cycle 4: **Characters Index — the 19 remaining profiled Planeswalkers reviewed** (59 → 78 entries). Each status comes from the profile plus the latest fetched story naming the character. Echoverse versions in *Legends of Reality Fracture* (Dack "Helping Hand", Ob Nixilis "Ascended Angel") are flagged and not used as Multiverse status. Totals: 61 ✅ / 10 ❓ / 6 ⚠️ / 1 🚫. | `Characters Index.md` | Issue #20. |
| 4.3 | Bot cycle 4: **ELD/THB/IKO sourced** (was ⚠️). THB: official Story Summary and Story on Cards pages. IKO: Story on Cards page, with the plot read from its 14 story images. ELD: official ebook publisher listing plus Story Spotlight card flavor text (Scryfall ELD printings). Now 39 sourced arcs; Master Timeline gains 3 post-Mending rows; Xenagos status sourced (✅ dead, THB Story on Cards). | `Conflicts & Arcs.md`, `Master Timeline.md`, `Characters Index.md` | User priority (2). |
| 4.4 | Bot cycle 4: **Planes Index 12 → 18 detailed entries**: Theros Underworld, Muraganda, Kylem, Gobakhan, Shenmeng, Segovia. Content from the Echoverse-mixed *Legends of Reality Fracture* article is flagged ⚠️. | `Planes Index.md` | Issue #12. |
| 4.5 | Bot cycle 4: **combo detection** via the Commander Spellbook public API (`find-my-combos`) for all 32 decks: 189 complete combos, 51 two-card infinite combos in 14 decks. Each deck gets a Combos block; EDH Standards gains combo columns and combo-adjusted floors (Xenagos and Gishath 2 → 3). | `scripts/detect_combos.py`, `data/combos.json`, `decks/*`, `EDH Standards.md` | Issue #15. |
| 4.6 | Bot cycle 4: **12 archetype guides** (`EDH Archetypes.md`, generated from repo data only; plans labeled Opinion). | `EDH Archetypes.md`, `scripts/build_archetypes.py`, `EDH Standards.md` | Issue #19. |
| 4.7 | Bot cycle 4: README dashboard, Progress Tracker, Knowledge Index, Update Log refreshed. | `README.md`, `Progress Tracker.md`, `Knowledge Index.md`, `Update Log.md` | Keep the dashboard current. |

## 2026-10-15 — Bot cycle 3 (sprint: lore deepening, all-identity EDH, rules interactions)

> All entries in this section are **Bot cycle 3** (Grok Bot) changes. Sprint mode: the scheduled routine was paused and this was the only committing process.

| # | Summary | Files affected | Reason |
|---|---|---|---|
| 3.1 | Bot cycle 3: card-data polish — deck-skeleton mass-land-denial pattern fixed (All Is Dust was a false positive; Kozilek rebuilt, floor 4 → 3); new `scripts/deck_rules_notes.py` adds a Commander rules & rulings block (Oracle text, every official ruling verbatim, ruled deck cards) to every deck. Cards/rulings unchanged: 33,894 entries, 78,943 rulings, verify 0 problems. | `scripts/build_deck_skeleton.py`, `scripts/deck_rules_notes.py`, `decks/*` | Accuracy of bracket floors; rulings surfaced where decks are used. |
| 3.2 | Bot cycle 3: EDH — 20 new validated skeletons (PR #21), then 4 four-color skeletons (Breya WUBR, Yidris UBRG, Saskia BRGW, Kynaios & Tiro RGWU) → **32 skeletons covering all 32 color identities** (was 8); synergy notes 3 → 15 (Niv-Mizzet two-card loop ⚠️ flagged). | `decks/*`, `EDH Standards.md` | Issue #19. |
| 3.3 | Bot cycle 3: **Conflicts & Arcs deepened** — 15 one-paragraph arcs → **36 sourced entries / 40 headings** (Sets · Timeline · Planes · Characters · events · Outcome · Sources), per-set 2019–2026 arcs, cross-arc threads table, open questions; original anchors preserved. Claims re-checked against the fetched story text; unverifiable details removed or ⚠️-flagged (ELD/THB/IKO unsourced; Emrakul's containment; fate of Ulamog/Kozilek). | `Conflicts & Arcs.md` | User priority (2): deepen lore. |
| 3.4 | Bot cycle 3: **Master Timeline deepened** — 7 era tables with arc/character cross-links (56 links into Conflicts & Arcs), new **Dated events (AR)** table (28, 44, 63, 64, 69, 79, 85 AR and the 4562 AR frame, all quoted from *The Brothers' War* episodes), Omenpath-era relative markers quoted from sources ("One Year Prior", "nearly two years"). All cited Wizards URLs in both files validated against the official sitemap. | `Master Timeline.md` | User priority (2). |
| 3.5 | Bot cycle 3: **Planes Index** +Regatha and +Rath (sourced from official Magic Story pages); Mercadia and Ulgrotha added as ⚠️ stubs (no official page in the sitemap; `/en/story/<plane>-plane` returns 404). | `Planes Index.md` | Issue #12. |
| 3.6 | Bot cycle 3: **Rules Interactions** started — 7 topics (layers 613.1–613.7, dependency 613.8, replacement vs. triggered 614/603/616, SBAs 704, copy 707, color identity 903.4, command-zone returns 903.9) quoting the CR 2026-09-25 verbatim, 35 official WotC rulings linked to card entries; generator `scripts/build_rules_interactions.py`. | `Rules Interactions.md`, `scripts/build_rules_interactions.py`, `EDH Standards.md` | Issue #9. |
| 3.7 | Bot cycle 3: README dashboard, Progress Tracker, Knowledge Index, Update Log refreshed. | `README.md`, `Progress Tracker.md`, `Knowledge Index.md`, `Update Log.md` | Keep the dashboard current. |

## 2026-10-15 — Bot cycle 2 (rulings, Planes, EDH staples, Characters)

> All entries in this section are **Bot cycle** (Grok Bot) changes.

| # | Summary | Files affected | Reason |
|---|---|---|---|
| 2.1 | Bot cycle: rulings support — Scryfall `rulings` bulk joined by oracle_id, rendered inside card entries, resumable via `rulings` CSV column + `data/ingest_state.json` → `rulings`; verifier checks every ruling verbatim. Rulings batch R1: first 1,000 cards in priority/EDHREC order (2,604 rulings on 686 cards). | `scripts/ingest_scryfall.py`, `scripts/verify_cards.py`, `cards/**`, `data/*`, `Card Index.md`, `README.md`, `Progress Tracker.md` | Issue #10. |
| 2.2 | Bot cycle: rulings batch R2: +9,000 cards → 10,000 processed (32,675 rulings on 7,385 cards). | `cards/**`, `data/*`, `Card Index.md`, `README.md`, `Progress Tracker.md` | Issue #10. |
| 2.3 | Bot cycle: rulings batch R3: remaining 23,894 cards → **all 33,894 processed; 78,943 / 78,943 rulings on 19,889 / 19,889 cards** (verify_cards: 0 problems). Rulings format documented. | `cards/**`, `data/*`, `Card Index.md`, `Card Data Conventions.md`, `README.md`, `Progress Tracker.md` | Issue #10 complete. |
| 2.4 | Bot cycle 2: coordination note — a second concurrent Grok Bot session claimed Planes Index + EDH work so the rulings/Characters session would not overlap. | `Update Log.md` | Avoid duplicate work between concurrent sessions. |
| 2.5 | Bot cycle 2: **Planes Index — 8 detailed entries** (new: Kaldheim, Eldraine, Ikoria, New Capenna, Skalla, Vryn; deepened: Phyrexia/Old Phyrexia + New Phyrexia's nine spheres, Ravnica after the invasion), each with ✅/⚠️/🗣️ (in-universe narrator) flags, story/set dates (Scryfall sets), cross-links to Characters / Conflicts & Arcs / Master Timeline and **72 card-entry links**. Sources: 8 official articles fetched 2026-10-15 (Planeswalker's Guides to Kaldheim pts 1–2, Eldraine, Ikoria, Streets of New Capenna, Phyrexia: All Will Be One, Murders at Karlov Manor; profiles; Magic Story episodes). New `scripts/resolve_card_links.py` (`[[Card]]` → exact entry link). check_links: 0 broken. | `Planes Index.md`, `scripts/resolve_card_links.py` | Issue #12 (partial); brief priority 2. |
| 2.6 | Bot cycle 2: **EDH Staples** (auto-generated, `scripts/build_staples.py`): top 15 Commander-legal cards per color identity (colorless, 5 mono, 10 two-color, 10 three-color) and per role/archetype (ramp, draw, removal, wipes, counterspells, tutors, protection, recursion, tokens, aristocrats, +1/+1 counters, spellslinger, landfall, utility lands) from 32,048 ranked cards, EDHREC-rank ordered, Game Changer flags, patterns documented. | `EDH Staples.md`, `scripts/build_staples.py` | Brief priority 3 (staples by color/archetype). |
| 2.7 | Bot cycle 2: 3 new validated deck skeletons — Talrand, Sky Summoner (U, 3 GC, bracket floor 3), Teysa Karlov (WB, 2 GC, floor 3), Tatyova, Benthic Druid (GU, 2 GC, floor 3) — all 100 cards, singleton, strict identity, Commander-legal; **Synergy notes** section in EDH Standards quoting Oracle text + official WotC rulings (e.g. Teysa does not double “whenever you sacrifice” triggers). | `decks/talrand-sky-summoner.md`, `decks/teysa-karlov.md`, `decks/tatyova-benthic-druid.md`, `EDH Standards.md` | Issue #16 (closed) → follow-up #19. |
| 2.8 | Bot cycle 2: dashboard/tracker/index refresh (Planes, EDH, rulings status), issue updates (#16 closed, #19 opened, progress on #12 and #14). | `README.md`, `Progress Tracker.md`, `Knowledge Index.md`, `Update Log.md` | Keep GitHub dashboard current. |
| 2.9 | Bot cycle 2: **Characters Index deepened** — 47 table rows → **59 per-character entries** (who / late-2026 status / detail / See also: Planes, Arcs, Timeline / Sources with notes). Statuses resolved from fetched official stories: 29 ✅ / 20 ⚠️ → **54 ✅ / 1 ❓ (Sarkhan) / 3 ⚠️ (Sorin, Dihada, Dakkon) / 1 🚫**. New sections: Status at a glance, Sparks after the Phyrexian Invasion, Echoverse counterparts, Not yet reviewed (19 names). All 90 cited Wizards URLs are in the magic.wizards.com sitemap; check_links 0 broken. | `Characters Index.md` | Issue #11 (closed); follow-up #20. |
| 2.10 | Bot cycle 2: dashboard/tracker/index rows for Characters; README priorities now point to #20. | `README.md`, `Progress Tracker.md`, `Knowledge Index.md`, `Update Log.md` | Keep the dashboard current. |

## 2026-10-15 — Bot cycle 1 (repository bootstrap)

> All entries in this section are **Bot cycle** (Grok Bot) changes. Entries from other automations should be labeled with their source.

| # | Summary | Files affected | Reason |
|---|---|---|---|
| 1.1 | Added standing project goal, Knowledge Index (maintenance rules, flags, source hierarchy), Card Data Conventions (sharded storage, entry format incl. flavor text). | `GOAL.md`, `Knowledge Index.md`, `Card Data Conventions.md`, `.gitignore` | Establish structure mirroring the Grok project and the user's goal. |
| 1.2 | Added resumable Scryfall ingestion script, link checker, curated priority/category inputs. | `scripts/ingest_scryfall.py`, `scripts/check_links.py`, `data/priority_cards.txt`, `data/categories.json` | Reusable, idempotent high-volume card ingestion for every future cycle. |
| 1.3 | Card batch 1: 1,000 cards (243 priority/category cards + top Commander-legal cards by EDHREC rank). | `cards/**`, `Card Index.md`, `data/card_index.csv`, `data/ingest_state.json`, `README.md`, `Progress Tracker.md` | Brief priority #1: complete card entries first. |
| 1.4 | Card batch 2a: +4,000 cards → 5,000 total (EDHREC-rank order). | `cards/**`, `Card Index.md`, `data/*`, `README.md`, `Progress Tracker.md` | Issue #2; v0.2 threshold. |
| 1.5 | Card batch 2b: +5,000 cards → 10,000 total (EDHREC-rank order). | `cards/**`, `Card Index.md`, `data/*`, `README.md`, `Progress Tracker.md` | Issue #2; v0.3 threshold. |
| 1.6 | Stable adaptive sharding (2→5-letter prefixes, ≤350 cards/shard at full coverage); shards regenerated. | `scripts/ingest_scryfall.py`, `cards/**`, `Card Data Conventions.md`, `Card Index.md`, `data/card_index.csv` | Keep shard files GitHub-renderable at ~34k cards without ever moving a card. |
| 1.7 | Card batch 2c: +10,000 cards → 20,000 total (EDHREC-rank order). | `cards/**`, `Card Index.md`, `data/*`, `README.md`, `Progress Tracker.md` | Issue #2 extended; v0.4 threshold. |
| 1.8 | Commander-eligibility flag now follows Comprehensive Rules 903.3 (2026-09-25): legendary Vehicles and legendary Spacecraft with P/T count; 31 entries changed. | `scripts/ingest_scryfall.py`, `cards/**`, `Card Data Conventions.md` | Accuracy: verified against the current CR text. |
| 1.9 | EDH Standards (CR 903 rules, strict color identity, Archidekt format, official Commander Brackets incl. Oct 2025 & Feb 2026 updates, auto-generated banned & Game Changers lists); deck-skeleton builder/validator; five validated skeletons (Krenko, Lathril, Edgar Markov, Atraxa, The Ur-Dragon). | `EDH Standards.md`, `decks/*.md`, `scripts/build_deck_skeleton.py`, `scripts/ingest_scryfall.py` | Brief priority #3 (EDH utility) with verifiable sources only. |
| 1.10 | Ingestion order now puts Commander-banned cards right after priority cards; +100 cards (83 banned + 17 next by rank) → 20,100. | `scripts/ingest_scryfall.py`, `Card Data Conventions.md`, `cards/**`, `data/*`, `Card Index.md` | Banned-card legality questions need full entries. |
| 1.11 | Card batch 3: ingested the entire remaining universe (+13,794 net) → **33,894 / 33,894** paper Oracle cards; excluded Jumpstart `front_card` layout; disambiguated duplicate-name headings; added `scripts/verify_cards.py` (all 33,894 entries verified verbatim, 0 problems). | `cards/**`, `Card Index.md`, `data/*`, `scripts/ingest_scryfall.py`, `scripts/verify_cards.py`, `Card Data Conventions.md`, `Knowledge Index.md`, `README.md`, `Progress Tracker.md` | User follow-up: maximum-volume cycle, card ingestion top priority. |
| 1.12 | Lore foundation: Master Timeline (source-anchored in-universe eras + Scryfall release chronology), Planes Index (15 profiled planes + 6 Omenpath-era settings), Characters Index (5 eras + Open Questions, ✅/⚠️ status), Conflicts & Arcs (15 arcs through Reality Fracture). Every Wizards URL cited was checked against the magic.wizards.com sitemap. | `Master Timeline.md`, `Planes Index.md`, `Characters Index.md`, `Conflicts & Arcs.md` | Brief priority #2 (major lore gaps); only fetched official sources, uncertain items flagged. |
| 1.13 | Bot cycle: README dashboard (area status, priorities linked to issues #9–#17, cycle commands, tags), Progress Tracker (all areas quantified), issues #1–#17, milestones (5 closed), tags v0.1→v1.0. | `README.md`, `Progress Tracker.md`, `Update Log.md`, `data/ingest_state.json` | Brief item 3: use GitHub as an active dashboard. |
| 1.14 | Bot cycle: Knowledge Index — commit/push coordination rules ("Bot cycle" tag, pull --rebase, no force-push); CI note. | `Knowledge Index.md`, `Update Log.md` | Coordination with the separate Grok Project Automation. |
