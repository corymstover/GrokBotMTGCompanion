# Knowledge Index

> Master map of the MTG Companion knowledge base and the rules for maintaining it.
> Standing reference: **[Project Goal](GOAL.md)** — every cycle and structural decision must advance it.

## Contents
- [File map](#file-map)
- [Maintenance rules](#maintenance-rules)
- [Canon & verification flags](#canon--verification-flags)
- [Source hierarchy](#source-hierarchy)
- [Improvement-cycle checklist](#improvement-cycle-checklist)
- [GitHub workflow conventions](#github-workflow-conventions)

## File map
| File / folder | Purpose |
|---|---|
| [GOAL.md](GOAL.md) | Standing project goal (verbatim from the user). |
| [README.md](README.md) | Living dashboard: counts, progress, priorities, links. |
| [Progress Tracker.md](Progress%20Tracker.md) | Quantitative status per area; mirrored in README. |
| [Update Log.md](Update%20Log.md) | Every change: date, summary, files affected, reason. |
| [Characters Index.md](Characters%20Index.md) | Characters by era with status. |
| [Planes Index.md](Planes%20Index.md) | Planes with summaries, key sets, and sources. |
| [Conflicts & Arcs.md](Conflicts%20%26%20Arcs.md) | Major wars and story arcs. |
| [Master Timeline.md](Master%20Timeline.md) | In-universe eras + real-world story release chronology. |
| [EDH Standards.md](EDH%20Standards.md) | Commander deckbuilding rules: strict color identity, commander first, Archidekt format, brackets. |
| [decks/](decks/) | Deck skeletons following EDH Standards. |
| [Card Data Conventions.md](Card%20Data%20Conventions.md) | Card entry format, storage layout, source flags. |
| [Card Index.md](Card%20Index.md) | Auto-generated tracker of which cards have entries (+ category trackers). |
| [cards/](cards/) | Card entries, sharded `cards/<L>/<LL>.md`. |
| [data/](data/) | `card_index.csv`, `ingest_state.json`, `priority_cards.txt`, `categories.json`. |
| [scripts/ingest_scryfall.py](scripts/ingest_scryfall.py) | Resumable Scryfall ingestion; regenerates cards, Card Index, dashboard stats. |
| [scripts/verify_cards.py](scripts/verify_cards.py) | Verifies every card entry verbatim against Scryfall bulk (must be 0 problems). |
| [scripts/build_deck_skeleton.py](scripts/build_deck_skeleton.py) | Builds + validates EDHREC-derived deck skeletons (identity, singleton, legality, bracket floor). |
| [scripts/check_links.py](scripts/check_links.py) | Validates relative links/anchors in the hand-written docs (also run in CI). |

## Maintenance rules
1. **Accuracy over volume.** Never invent facts. Card data comes only from Scryfall; lore only from official Wizards of the Coast material (cited by URL).
2. **Flag uncertainty** with the markers below. Anything after a source's date, or not directly stated in a fetched source, is *Unverified* or an *Open Question*.
3. **Scannable files:** every file starts with a purpose blurb and a linked Contents list; use headings and tables; keep entries short and link instead of duplicating.
4. **No duplication:** each fact has one home. Card text lives only in `cards/`; other files link to it. Character details live in Characters Index; planes link to characters and vice versa.
5. **Generated files are not hand-edited** (`cards/`, `Card Index.md`, `data/card_index.csv`, `data/ingest_state.json`, and the `CARD-STATS` blocks in README/Progress Tracker).
6. **Every change gets an [Update Log](Update%20Log.md) entry** (date, summary, files, reason) and a conventional commit.
7. Opinion (deck advice, power assessments) must be labeled **Opinion** and kept out of card entries.

## Canon & verification flags
| Marker | Use |
|---|---|
| ✅ **Verified** | Directly supported by the cited official source / Scryfall. |
| ⚠️ **Unverified** | Plausible but not confirmed in a fetched source this cycle. Must be checked before relying on it. |
| ❓ **Open Question** | Unresolved in-story, ambiguous, or sources conflict. |
| 🚫 **Non-canonical** | Fan material, Un-sets, crossover (Universes Beyond) content that is not part of the Multiverse storyline, or retconned material. Keep only when useful and label it. |

## Source hierarchy
1. Scryfall API / bulk data (cards, legality, rank, sets & release dates).
2. magic.wizards.com: `/en/story/*` plane & Planeswalker profiles, `/en/news/magic-story/*` fiction, Planeswalker's Guides, "Legends of …" articles; official rules & bracket announcements.
3. Commander community data (EDHREC/Moxfield/Archidekt) — popularity and conventions only; treated as data, not canon.
4. Anything else → ⚠️ Unverified until confirmed by 1–3.

## Improvement-cycle checklist
1. `python3 scripts/ingest_scryfall.py` (adds any new Scryfall cards, default batch from `data/ingest_state.json`, and refreshes all entries) → `python3 scripts/verify_cards.py` (0 problems) → commit `feat(cards): …` / `chore(cards): refresh …` → push.
2. Pick the highest-impact open issue (labels `high-priority`, then `cards` / `lore` / `edh`), mark `in-progress`, do the work with citations.
3. Update [Update Log](Update%20Log.md), [Progress Tracker](Progress%20Tracker.md), README priorities; run `python3 scripts/check_links.py`.
4. Close finished issues with "Closed by <commit>"; open issues for new gaps; tag milestones when thresholds are crossed (`v0.N-<count>-cards`).

## GitHub workflow conventions
- Conventional commits: `feat(cards)`, `feat(lore)`, `feat(edh)`, `docs`, `chore`, `ci`, `fix`.
- Very large batches → feature branch + PR with summary; otherwise commit to `main`.
- Labels: `cards`, `lore`, `edh`, `rules`, `high-priority`, `in-progress`.
- Milestones: `v0.1 – 1,000 cards`, `v0.2 – 5,000 cards`, `v0.3 – 10,000 cards`, `v0.4 – 20,000 cards`, `v1.0 – Full card coverage`, `Lore foundation`.
- Tags: `v0.1-1000-cards`, `v0.2-5000-cards`, `v0.3-10000-cards`, … at the commit where the threshold is crossed.
