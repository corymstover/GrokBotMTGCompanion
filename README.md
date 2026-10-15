# GrokBotMTGCompanion — MTG Companion Knowledge Base

> Standing goal: **[GOAL.md](GOAL.md)** — the most complete, accurate, practically useful Magic: The Gathering companion (lore, card data, rules, Commander/EDH).
> Mirrors the Grok project "MTG Companion" file structure. Maintained by Grok Bot in hourly improvement cycles.

## 📊 Dashboard (updated 2026-10-15)

### Cards
<!-- CARD-STATS:START -->
**Cards with full Scryfall-verified entries: 33,894 / 33,894** (100.0%) — working target ~33,000 (Grok working total)

`██████████████████████████████`

- EDHREC coverage: every Commander-legal card ranked ≤ **32,351** has an entry
- Rulings: **78,943 / 78,943** Scryfall rulings in entries (19,889 / 19,889 cards with rulings; 33,894 / 33,894 cards processed) · next: **none — complete**
- Last batch: `2026-10-15-b6` (+14,085 cards) · last run 2026-10-15T11:04:12+00:00 · Scryfall bulk 2026-10-15
- Next card target: **none — full coverage.** Each run auto-adds newly released Scryfall cards and refreshes Oracle text/legality.
<!-- CARD-STATS:END -->

### Area status
| Area | Status | File |
|---|---|---|
| Cards | ✅ **Full coverage** — 33,894 entries (Oracle text, flavor text, cost, type, identity, Commander notes), verified verbatim against Scryfall (0 problems) | [Card Index](Card%20Index.md) · [cards/](cards/) |
| Master Timeline | 🟡 Initial — in-universe eras (source-anchored relative dates) + release chronology 2007–2027 | [Master Timeline](Master%20Timeline.md) |
| Planes | 🟡 Deepening — 15 profiled planes + 6 Omenpath-era settings + **8 detailed entries** (Kaldheim, Eldraine, Ikoria, New Capenna, Phyrexia & New Phyrexia's spheres, post-invasion Ravnica, Skalla, Vryn) with source notes and 72 card links | [Planes Index](Planes%20Index.md) |
| Characters | 🟡 Initial — 5 eras, 47 character rows (+30 more profiled names listed); 29 with a ✅ sourced status, rest ⚠️ Unverified | [Characters Index](Characters%20Index.md) |
| Conflicts & Arcs | 🟡 Initial — 15 arcs through Reality Fracture (2026-10) | [Conflicts & Arcs](Conflicts%20%26%20Arcs.md) |
| EDH | 🟡 Standards (CR 903, Brackets, Game Changers, banned list) + **8 validated skeletons** + [EDH Staples](EDH%20Staples.md) (top cards for 26 color identities and 14 roles/archetypes, GC-flagged) + rulings-backed synergy notes | [EDH Standards](EDH%20Standards.md) · [EDH Staples](EDH%20Staples.md) · [decks/](decks/) |
| Rules interactions | 🟡 Rulings: all 78,943 Scryfall rulings are inside card entries ([#10](https://github.com/corymstover/GrokBotMTGCompanion/issues/10) ✅); CR-cited interactions section not started — [#9](https://github.com/corymstover/GrokBotMTGCompanion/issues/9) | [Card Data Conventions](Card%20Data%20Conventions.md) |

### Next priorities
1. **Rules interactions** section citing the 2026-09-25 Comprehensive Rules — [#9](https://github.com/corymstover/GrokBotMTGCompanion/issues/9); rulings ingestion — [#10](https://github.com/corymstover/GrokBotMTGCompanion/issues/10)
2. **Lore:** verify post-2023 Planeswalker statuses — [#11](https://github.com/corymstover/GrokBotMTGCompanion/issues/11); missing planes — [#12](https://github.com/corymstover/GrokBotMTGCompanion/issues/12); Omenpath-era arcs — [#13](https://github.com/corymstover/GrokBotMTGCompanion/issues/13); story archive index — [#14](https://github.com/corymstover/GrokBotMTGCompanion/issues/14)
3. **EDH:** combo detection for brackets — [#15](https://github.com/corymstover/GrokBotMTGCompanion/issues/15); more skeletons & archetype guides — [#16](https://github.com/corymstover/GrokBotMTGCompanion/issues/16)
4. **Maintenance:** refresh cards / ingest new sets each cycle — [#17](https://github.com/corymstover/GrokBotMTGCompanion/issues/17)

## 🗂 Key files
| File | Purpose |
|---|---|
| [Knowledge Index](Knowledge%20Index.md) | File map, maintenance rules, canon flags, source hierarchy, cycle checklist |
| [Progress Tracker](Progress%20Tracker.md) · [Update Log](Update%20Log.md) | Quantitative progress · every change with date/files/reason |
| [Card Data Conventions](Card%20Data%20Conventions.md) · [Card Index](Card%20Index.md) | Card entry format & storage · which cards have entries |
| [EDH Standards](EDH%20Standards.md) · [EDH Staples](EDH%20Staples.md) | Commander rules, color identity, Archidekt format, brackets, synergy notes · data-derived staples by identity and role |
| [Master Timeline](Master%20Timeline.md) · [Planes Index](Planes%20Index.md) · [Characters Index](Characters%20Index.md) · [Conflicts & Arcs](Conflicts%20%26%20Arcs.md) | Lore |

## 🔁 Running a cycle
```bash
python3 scripts/ingest_scryfall.py          # add new Scryfall cards (default batch from data/ingest_state.json) + refresh all entries
python3 scripts/verify_cards.py             # must report 0 problems
python3 scripts/check_links.py --all        # link/anchor check (CI runs the docs-only variant)
python3 scripts/build_deck_skeleton.py "Commander Name"   # new validated deck skeleton in decks/
python3 scripts/build_staples.py            # regenerate EDH Staples.md from the Scryfall bulk
python3 scripts/resolve_card_links.py "Planes Index.md"   # turn [[Card Name]] placeholders in hand-written pages into card-entry links
```
State: [`data/ingest_state.json`](data/ingest_state.json) · index: [`data/card_index.csv`](data/card_index.csv).

## 🏷 Releases
`v0.1-1000-cards` · `v0.2-5000-cards` · `v0.3-10000-cards` · `v0.4-20000-cards` · `v1.0-33894-cards`

*Card data © Wizards of the Coast, via [Scryfall](https://scryfall.com). Lore summaries cite official [magic.wizards.com](https://magic.wizards.com/en/story) pages. Unofficial fan project under the Wizards Fan Content Policy.*
