---
title: "Knowledge Snapshots"
category: meta
tags: [tags, releases, snapshots]
issues: [47]
generated_by: hand-written
sources: []
related: ["Front-Matter Schema.md", "Knowledge Index.md", "Progress Tracker.md", "ROADMAP.md", "Update Log.md"]
schema: 2
---

# Knowledge Snapshots

> **Bot cycle 15 · issue [#47](https://github.com/corymstover/GrokBotMTGCompanion/issues/47) (Phase 4).** Every git tag in this repo is a **knowledge snapshot**: a fixed point you can check out or cite, with what it contained. Tags are annotated and never moved. Most have a GitHub [release](https://github.com/corymstover/GrokBotMTGCompanion/releases).

## Contents
- [Snapshot policy](#snapshot-policy)
- [Snapshots](#snapshots)
- [Using a snapshot](#using-a-snapshot)

## Snapshot policy
Tag a snapshot when one of these happens:
1. **A ROADMAP phase or GitHub milestone closes:** `vX.Y-cycleN-phaseK-complete`.
2. **A card-coverage milestone:** `vX.Y-<count>-cards`.
3. **A major data refresh that changes answers:** a new set ingested, a new Comprehensive Rules version, or a banned/restricted update, all via the [#17](https://github.com/corymstover/GrokBotMTGCompanion/issues/17) maintenance cycle. Name it `vX.Y-cycleN-<what>`.
4. **A large sprint batch:** a cycle that adds several major pages (e.g. `v1.2-cycle4-rules-lore-edh`).

Rules: tag the **merge commit on `main`** after `verify_cards.py` and `check_links.py --all` pass. Use an annotated tag whose message starts with the Bot cycle. Never force-move or delete a tag. Record it here and in the [Progress Tracker](Progress%20Tracker.md#milestones--tags).

## Snapshots
| Tag | Commit | What it captures |
|---|---|---|
| `v0.1-1000-cards` | e10fbdf | 1,000 Scryfall-verified card entries |
| `v0.2-5000-cards` | 45b0304 | 5,000 card entries |
| `v0.3-10000-cards` | 4841f1b | 10,000 card entries |
| `v0.4-20000-cards` | d36aad7 | 20,000 card entries |
| `v1.0-33894-cards` | 9ece392 | Full card coverage: 33,894 verified entries |
| `v1.1-rulings` | 642c236 | Scryfall rulings in all card entries (78,943) |
| `v1.1-cycle3-lore-edh-rules` | 3b034af | Bot cycle 3: deeper Timeline and Arcs, 32-identity EDH skeletons, Rules Interactions |
| `v1.2-cycle4-rules-lore-edh` | 70d0c26 | Bot cycle 4: 17 rules topics, 78 characters, 39 arcs, combos and 12 archetypes |
| `v1.3-cycle5-rules-lore-maintenance` | ef9f20f | Bot cycle 5: 27 rules topics, 23 detailed planes, 612-page story archive |
| `v1.4-cycle6-edh-depth` | 6f1331f | Bot cycle 6: ROADMAP plus Phase 1 EDH depth (7 of 9 issues) |
| `v1.5-cycle7-phase1-complete` | a38591c | Phase 1 (EDH & deckbuilding depth) complete |
| `v1.6-cycle8-phase2-complete` | a2e241b | Phase 2 (Lore & Story depth) complete |
| `v1.7-cycle9-phase3-complete` | 63dbeb7 | Phase 3 (Card & Rules enrichment) complete. Merge of PR #55 (Bot cycles 9–13: keywords, printings, legality, tokens, artists). Tagged in Bot cycle 15 |
| `v1.8-cycle15-phase4-complete` | merge of the Bot cycle 15 PR | Phase 4 (Structure & usability) complete: front-matter, FAQ, Lookup Guide, this page |
| `v1.9-grixis-integration` | merge of the Bot cycle 16 PR | Grixis section (40 decks, corrections, packages, evaluation of all 62 source lists) and the any-identity deck template, evaluation checklist and `evaluate_decklist.py` |
| `v2.2-phase7-optimization` | merge of the Bot cycle 32 PR | Phase 7 lore optimization pass (Bot cycles 31–32, #92–#96): 280 lore entries indexed with computed tags; bidirectional lore cross-references (1,460 symmetric relations, reciprocity checked); lore-deck story maps + Lore decks section in EDH Bracket Calibration; verbatim quote checks on 25 lore and rules/EDH pages (2,719 quotes) |
| `v2.1-phase6-lore` | 5ec2486 (Bot cycle 30) | Phase 6 lore deepening: 40 arcs, 38 dossiers, 42 planes, 26 items, 29 retcons, 596 primary pages (row added in Bot cycle 32; it was missing) |
| `v2.0-phase5-optimization` | merge of the Bot cycle 19 PR | Phase 5 optimization pass: front-matter schema v2 on pages, decks, card shards and reverse-index pages; `kb_find` retrieval index; `validate_all.py` (links, schema, index, cross-refs, calibration, citations, Oracle drift, decks, freshness); reverse card index and cross-references; bracket calibration & pilot notes in all 86 decks |

## Using a snapshot
- See the KB as it was: `git checkout v1.6-cycle8-phase2-complete` (then `git checkout main` to return).
- See what changed between snapshots: `git diff --stat v1.6-cycle8-phase2-complete v1.7-cycle9-phase3-complete`.
- Cite a snapshot in an answer: `https://github.com/corymstover/GrokBotMTGCompanion/tree/<tag>/<file>`.
