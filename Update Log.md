# Update Log

> Every update records **date · summary · files affected · reason**. Newest first. See [Knowledge Index](Knowledge%20Index.md#maintenance-rules).

## Contents
- [2026-10-15 — Bot cycle 1 (repository bootstrap)](#2026-10-15--bot-cycle-1-repository-bootstrap)

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
