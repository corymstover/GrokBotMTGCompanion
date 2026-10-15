# Update Log

> Every update records **date · summary · files affected · reason**. Newest first. See [Knowledge Index](Knowledge%20Index.md#maintenance-rules).

## Contents
- [2026-10-15 — Cycle 1 (repository bootstrap)](#2026-10-15--cycle-1-repository-bootstrap)

## 2026-10-15 — Cycle 1 (repository bootstrap)

| # | Summary | Files affected | Reason |
|---|---|---|---|
| 1.1 | Added standing project goal, Knowledge Index (maintenance rules, flags, source hierarchy), Card Data Conventions (sharded storage, entry format incl. flavor text). | `GOAL.md`, `Knowledge Index.md`, `Card Data Conventions.md`, `.gitignore` | Establish structure mirroring the Grok project and the user's goal. |
| 1.2 | Added resumable Scryfall ingestion script, link checker, curated priority/category inputs. | `scripts/ingest_scryfall.py`, `scripts/check_links.py`, `data/priority_cards.txt`, `data/categories.json` | Reusable, idempotent high-volume card ingestion for every future cycle. |
| 1.3 | Card batch 1: 1,000 cards (243 priority/category cards + top Commander-legal cards by EDHREC rank). | `cards/**`, `Card Index.md`, `data/card_index.csv`, `data/ingest_state.json`, `README.md`, `Progress Tracker.md` | Brief priority #1: complete card entries first. |
| 1.4 | Card batch 2a: +4,000 cards → 5,000 total (EDHREC-rank order). | `cards/**`, `Card Index.md`, `data/*`, `README.md`, `Progress Tracker.md` | Issue #2; v0.2 threshold. |
| 1.5 | Card batch 2b: +5,000 cards → 10,000 total (EDHREC-rank order). | `cards/**`, `Card Index.md`, `data/*`, `README.md`, `Progress Tracker.md` | Issue #2; v0.3 threshold. |
| 1.6 | Stable adaptive sharding (2→5-letter prefixes, ≤350 cards/shard at full coverage); shards regenerated. | `scripts/ingest_scryfall.py`, `cards/**`, `Card Data Conventions.md`, `Card Index.md`, `data/card_index.csv` | Keep shard files GitHub-renderable at ~34k cards without ever moving a card. |
