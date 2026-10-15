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
| Master Timeline | 🟢 Deepened (Bot cycle 3) — 7 in-universe era tables with per-arc rows cross-linked to Conflicts & Arcs and Characters, **8 official AR-dated events** (28–85 AR + 4562 AR, from *The Brothers' War*), quoted relative markers for the Omenpath era, release chronology 2007–2027 | [Master Timeline](Master%20Timeline.md) |
| Planes | 🟡 Deepening — 15 profiled planes + 6 Omenpath-era settings + **12 detailed entries** (Kaldheim, Eldraine, Ikoria, New Capenna, Phyrexia & New Phyrexia's spheres, post-invasion Ravnica, Skalla, Vryn, Regatha, Rath; ⚠️ stubs: Mercadia, Ulgrotha — no official source found) with source notes and 72 card links | [Planes Index](Planes%20Index.md) |
| Characters | 🟢 Deepened (Bot cycle 2) — 59 per-character entries with source notes and Planes/Arcs/Timeline links; **54 ✅ sourced statuses**, 1 ❓, 3 ⚠️ (Sorin, Dihada, Dakkon), 1 🚫 Echoverse; 19 names queued for review | [Characters Index](Characters%20Index.md) |
| Conflicts & Arcs | 🟢 Deepened (Bot cycle 3) — **36 sourced arc entries** (Sets · Timeline · Planes · Characters · events · Outcome · Sources), 2019–2026 arcs per set, cross-arc threads table (Bolas, Phyrexia, Jace, Sparks, Ugin & Tarkir); ⚠️ ELD/THB/IKO not yet sourced | [Conflicts & Arcs](Conflicts%20%26%20Arcs.md) |
| EDH | 🟡 Standards (CR 903, Brackets, Game Changers, banned list) + **32 validated skeletons — every color identity** + [EDH Staples](EDH%20Staples.md) (top cards for 26 color identities and 14 roles/archetypes, GC-flagged) + 15 rulings-backed synergy notes; every deck has a Commander rules & rulings block | [EDH Standards](EDH%20Standards.md) · [EDH Staples](EDH%20Staples.md) · [decks/](decks/) |
| Rules interactions | 🟡 Started (Bot cycle 3) — 7 topics (layers, dependency, replacement vs. triggers, SBAs, copy effects, color identity, command-zone returns) quoting the **CR 2026-09-25** verbatim + 35 linked official rulings ([#9](https://github.com/corymstover/GrokBotMTGCompanion/issues/9)); all 78,943 rulings in card entries ([#10](https://github.com/corymstover/GrokBotMTGCompanion/issues/10) ✅) | [Rules Interactions](Rules%20Interactions.md) · [Card Data Conventions](Card%20Data%20Conventions.md) |

### Next priorities
1. **Rules interactions:** next topics — stack & priority, combat damage, protection/ward, mutate/merge, worked layer examples — [#9](https://github.com/corymstover/GrokBotMTGCompanion/issues/9)
2. **Lore:** review the 19 remaining profiled Planeswalkers — [#20](https://github.com/corymstover/GrokBotMTGCompanion/issues/20) (#11 ✅ done); missing planes (Mercadia/Ulgrotha need sources; Ergamon, Segovia, Muraganda, Kylem, Gobakhan …) — [#12](https://github.com/corymstover/GrokBotMTGCompanion/issues/12); ELD/THB/IKO story sources; Omenpath-era arcs — [#13](https://github.com/corymstover/GrokBotMTGCompanion/issues/13); story archive index — [#14](https://github.com/corymstover/GrokBotMTGCompanion/issues/14)
3. **EDH:** combo detection for brackets — [#15](https://github.com/corymstover/GrokBotMTGCompanion/issues/15); archetype guides beyond the 32 identity skeletons — [#19](https://github.com/corymstover/GrokBotMTGCompanion/issues/19)
4. **Maintenance:** refresh cards / ingest new sets each cycle — [#17](https://github.com/corymstover/GrokBotMTGCompanion/issues/17)

## 🗂 Key files
| File | Purpose |
|---|---|
| [Knowledge Index](Knowledge%20Index.md) | File map, maintenance rules, canon flags, source hierarchy, cycle checklist |
| [Progress Tracker](Progress%20Tracker.md) · [Update Log](Update%20Log.md) | Quantitative progress · every change with date/files/reason |
| [Card Data Conventions](Card%20Data%20Conventions.md) · [Card Index](Card%20Index.md) | Card entry format & storage · which cards have entries |
| [EDH Standards](EDH%20Standards.md) · [EDH Staples](EDH%20Staples.md) | Commander rules, color identity, Archidekt format, brackets, synergy notes · data-derived staples by identity and role |
| [Rules Interactions](Rules%20Interactions.md) | CR 2026-09-25 rules topics, quoted verbatim, with official rulings linked to card entries |
| [Master Timeline](Master%20Timeline.md) · [Planes Index](Planes%20Index.md) · [Characters Index](Characters%20Index.md) · [Conflicts & Arcs](Conflicts%20%26%20Arcs.md) | Lore |

## 🔁 Running a cycle
```bash
python3 scripts/ingest_scryfall.py          # add new Scryfall cards (default batch from data/ingest_state.json) + refresh all entries
python3 scripts/verify_cards.py             # must report 0 problems
python3 scripts/check_links.py --all        # link/anchor check (CI runs the docs-only variant)
python3 scripts/build_deck_skeleton.py "Commander Name"   # new validated deck skeleton in decks/
python3 scripts/build_staples.py            # regenerate EDH Staples.md from the Scryfall bulk
python3 scripts/deck_rules_notes.py         # refresh the Commander rules & rulings block in every deck
python3 scripts/build_rules_interactions.py # regenerate Rules Interactions.md (needs the CR .txt in .cache/)
python3 scripts/resolve_card_links.py "Planes Index.md"   # turn [[Card Name]] placeholders in hand-written pages into card-entry links
```
State: [`data/ingest_state.json`](data/ingest_state.json) · index: [`data/card_index.csv`](data/card_index.csv).

## 🏷 Releases
`v0.1-1000-cards` · `v0.2-5000-cards` · `v0.3-10000-cards` · `v0.4-20000-cards` · `v1.0-33894-cards`

*Card data © Wizards of the Coast, via [Scryfall](https://scryfall.com). Lore summaries cite official [magic.wizards.com](https://magic.wizards.com/en/story) pages. Unofficial fan project under the Wizards Fan Content Policy.*
