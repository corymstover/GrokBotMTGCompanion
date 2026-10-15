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
| Planes | 🟢 Deepened — 15 profiled planes + 6 Omenpath-era settings + **18 detailed entries** (cycle 4 added the Theros Underworld, Muraganda, Kylem, Gobakhan, Shenmeng and Segovia; ⚠️ Mercadia and Ulgrotha are stubs with no official source) with source notes and card links | [Planes Index](Planes%20Index.md) |
| Characters | 🟢 Complete for profiled Planeswalkers (Bot cycle 4) — **78 entries** (was 59): all 19 remaining profiled Planeswalkers reviewed ([#20](https://github.com/corymstover/GrokBotMTGCompanion/issues/20)). **61 ✅ · 10 ❓ · 6 ⚠️ · 1 🚫**; Echoverse versions from *Reality Fracture* are flagged | [Characters Index](Characters%20Index.md) |
| Conflicts & Arcs | 🟢 Deepened — **39 sourced arc entries** (was 36). Throne of Eldraine, Theros Beyond Death and Ikoria are now sourced from official Wizards story summary and story-on-cards pages and Story Spotlight cards. Includes a cross-arc threads table | [Conflicts & Arcs](Conflicts%20%26%20Arcs.md) |
| EDH | 🟢 Standards + **32 validated skeletons (every color identity)** + **12 [archetype guides](EDH%20Archetypes.md)** ([#19](https://github.com/corymstover/GrokBotMTGCompanion/issues/19)) + **Commander Spellbook combo detection** on every deck (189 complete combos, 51 two-card infinite in 14 decks; combo-adjusted bracket floors, [#15](https://github.com/corymstover/GrokBotMTGCompanion/issues/15)) + [EDH Staples](EDH%20Staples.md) + 15 rulings-backed synergy notes | [EDH Standards](EDH%20Standards.md) · [EDH Archetypes](EDH%20Archetypes.md) · [EDH Staples](EDH%20Staples.md) · [decks/](decks/) |
| Rules interactions | 🟢 **17 topics** (was 7): layers + official worked examples, dependency, replacement vs. triggers, SBAs, copy, stack & priority, cast vs. copy, combat damage, deathtouch + trample, protection, hexproof/shroud/ward, ETB/LTB, mutate/merge, commander tax, color identity, command zone. CR 2026-09-25 quoted verbatim, **20 official CR examples**, **87 linked rulings** ([#9](https://github.com/corymstover/GrokBotMTGCompanion/issues/9)) | [Rules Interactions](Rules%20Interactions.md) |

### Next priorities
1. **Rules interactions:** sagas & classes, phasing, DFCs/transform, the legend rule, "can't" vs. "can", and worked replacement-ordering examples — [#9](https://github.com/corymstover/GrokBotMTGCompanion/issues/9)
2. **Lore:** sources for Mercadia, Ulgrotha and Ergamon; DMU-era Dominaria, Zendikar Rising, NEO Kamigawa and the Strixhaven colleges — [#12](https://github.com/corymstover/GrokBotMTGCompanion/issues/12); story archive crawl beyond the sitemap — [#14](https://github.com/corymstover/GrokBotMTGCompanion/issues/14)
3. **EDH:** tune archetype guides with more skeletons per archetype; re-run combo detection each cycle (`scripts/detect_combos.py`)
4. **Maintenance:** refresh cards / ingest new sets each cycle — [#17](https://github.com/corymstover/GrokBotMTGCompanion/issues/17)

## 🗂 Key files
| File | Purpose |
|---|---|
| [Knowledge Index](Knowledge%20Index.md) | File map, maintenance rules, canon flags, source hierarchy, cycle checklist |
| [Progress Tracker](Progress%20Tracker.md) · [Update Log](Update%20Log.md) | Quantitative progress · every change with date/files/reason |
| [Card Data Conventions](Card%20Data%20Conventions.md) · [Card Index](Card%20Index.md) | Card entry format & storage · which cards have entries |
| [EDH Standards](EDH%20Standards.md) · [EDH Archetypes](EDH%20Archetypes.md) · [EDH Staples](EDH%20Staples.md) | Commander rules, color identity, Archidekt format, brackets, synergy notes · 12 archetype guides · data-derived staples by identity and role |
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
python3 scripts/detect_combos.py           # Commander Spellbook combo check for every deck → decks/*, data/combos.json
python3 scripts/build_archetypes.py         # regenerate EDH Archetypes.md
python3 scripts/resolve_card_links.py "Planes Index.md"   # turn [[Card Name]] placeholders in hand-written pages into card-entry links
```
State: [`data/ingest_state.json`](data/ingest_state.json) · index: [`data/card_index.csv`](data/card_index.csv).

## 🏷 Releases
`v0.1-1000-cards` · `v0.2-5000-cards` · `v0.3-10000-cards` · `v0.4-20000-cards` · `v1.0-33894-cards` · `v1.1-cycle3-lore-edh-rules`

*Card data © Wizards of the Coast, via [Scryfall](https://scryfall.com). Lore summaries cite official [magic.wizards.com](https://magic.wizards.com/en/story) pages. Unofficial fan project under the Wizards Fan Content Policy.*
