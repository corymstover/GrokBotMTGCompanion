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
- Last batch: `2026-10-15-b6` (+14,085 cards) · last run 2026-10-15T12:07:15+00:00 · Scryfall bulk 2026-10-15
- Next card target: **none — full coverage.** Each run auto-adds newly released Scryfall cards and refreshes Oracle text/legality.
<!-- CARD-STATS:END -->

### Area status
| Area | Status | File |
|---|---|---|
| Cards | ✅ **Full coverage** — 33,894 entries (Oracle text, flavor text, cost, type, identity, Commander notes), verified verbatim against Scryfall (0 problems) | [Card Index](Card%20Index.md) · [cards/](cards/) |
| Master Timeline | 🟢 Deepened (Bot cycle 3) — 7 in-universe era tables with per-arc rows cross-linked to Conflicts & Arcs and Characters, **8 official AR-dated events** (28–85 AR + 4562 AR, from *The Brothers' War*), quoted relative markers for the Omenpath era, release chronology 2007–2027 | [Master Timeline](Master%20Timeline.md) |
| Planes | 🟢 Complete for named targets (Bot cycle 5) — 15 profiled planes + 6 Omenpath-era settings + **23 detailed entries**. Cycle 5 sourced Mercadia and Ulgrotha from Wizards' official *Known Multiverse* overview, and added Ergamon, Zendikar Rising-era Zendikar, Neon Dynasty Kamigawa, Dominaria United-era Dominaria and the Strixhaven colleges (with story outcomes), plus Vryn's mage-rings. Only Nauctis (no story yet) remains | [Planes Index](Planes%20Index.md) |
| Characters | 🟢 Complete for profiled Planeswalkers (Bot cycle 4) — **78 entries** (was 59): all 19 remaining profiled Planeswalkers reviewed ([#20](https://github.com/corymstover/GrokBotMTGCompanion/issues/20)). **61 ✅ · 10 ❓ · 6 ⚠️ · 1 🚫**; Echoverse versions from *Reality Fracture* are flagged | [Characters Index](Characters%20Index.md) |
| Conflicts & Arcs | 🟢 Deepened — **39 sourced arc entries** (was 36). Throne of Eldraine, Theros Beyond Death and Ikoria are now sourced from official Wizards story summary and story-on-cards pages and Story Spotlight cards. Includes a cross-arc threads table | [Conflicts & Arcs](Conflicts%20%26%20Arcs.md) |
| EDH | 🟢 Standards + **32 validated skeletons (every color identity)** + **12 [archetype guides](EDH%20Archetypes.md)** ([#19](https://github.com/corymstover/GrokBotMTGCompanion/issues/19)) + **Commander Spellbook combo detection** on every deck (189 complete combos, 51 two-card infinite in 14 decks; combo-adjusted bracket floors, [#15](https://github.com/corymstover/GrokBotMTGCompanion/issues/15)) + [EDH Staples](EDH%20Staples.md) + 15 rulings-backed synergy notes | [EDH Standards](EDH%20Standards.md) · [EDH Archetypes](EDH%20Archetypes.md) · [EDH Staples](EDH%20Staples.md) · [decks/](decks/) |
| Story archive | 🟢 **612 official story/lore pages indexed** (575 live, 37 🗄️ archived from the Internet Archive), from the sitemap plus the Wayback Machine index of the retired Uncharted Realms and magic-story paths ([#14](https://github.com/corymstover/GrokBotMTGCompanion/issues/14)) | [Story Archive Index](Story%20Archive%20Index.md) |
| EDH depth (Bot cycle 6) | 🟢 **Phase 1 of the [ROADMAP](ROADMAP.md)**, all data-derived from Scryfall and every card Commander-legal with GC flags: [Mana Bases](EDH%20Mana%20Bases.md) for all 32 identities (1,118 non-basic lands classified) · [Packages](EDH%20Packages.md) (13 packages, 33 sub-packages) · [Win Conditions](EDH%20Win%20Conditions.md) (8 categories, 46 two-card combo kills) · [Interaction](EDH%20Interaction.md) (6 hierarchies, 19 buckets) · [Pairings](EDH%20Pairings.md) (8 partner abilities, 3,104 legal pairs, identity matrix) · [Mulligans](EDH%20Mulligans.md) (CR 103.5 plus exact odds) · ⚠️ [cEDH Primer](cEDH%20Primer.md) (competitive/Bracket 5, 61 Spellbook combos) ([#25](https://github.com/corymstover/GrokBotMTGCompanion/issues/25)–[#29](https://github.com/corymstover/GrokBotMTGCompanion/issues/29), [#31](https://github.com/corymstover/GrokBotMTGCompanion/issues/31), [#32](https://github.com/corymstover/GrokBotMTGCompanion/issues/32)) | [ROADMAP](ROADMAP.md) |
| Rules interactions | 🟢 **27 topics** (was 17). Cycle 5 added sagas, classes, phasing, DFCs/transform, the legend rule, "can't" beats "can", replacement-effect ordering, commander damage, partner/backgrounds, and leaving a multiplayer game. CR 2026-09-25 quoted verbatim, **37 official CR examples**, **139 linked rulings** ([#9](https://github.com/corymstover/GrokBotMTGCompanion/issues/9)) | [ROADMAP](ROADMAP.md) | Refinement sprint brief: 4 phases, each tracked as a GitHub milestone with one issue per item |
| [EDH Mana Bases](EDH%20Mana%20Bases.md) · [EDH Packages](EDH%20Packages.md) · [EDH Win Conditions](EDH%20Win%20Conditions.md) · [EDH Interaction](EDH%20Interaction.md) · [EDH Pairings](EDH%20Pairings.md) · [EDH Mulligans](EDH%20Mulligans.md) · [cEDH Primer](cEDH%20Primer.md) | Phase 1 deckbuilding guides (Bot cycle 6). The cEDH primer is competitive-only and kept separate |
| [Rules Interactions](Rules%20Interactions.md) |

### Next priorities
0. **[ROADMAP](ROADMAP.md) Phase 1 remainder:** upgrade paths [#30](https://github.com/corymstover/GrokBotMTGCompanion/issues/30), themed & plane-restricted decks [#33](https://github.com/corymstover/GrokBotMTGCompanion/issues/33). Then Phases 2–4 ([milestones](https://github.com/corymstover/GrokBotMTGCompanion/milestones))
1. **Rules (optional extras):** morph/disguise & face-down, split/adventure cards, monarch & initiative, day/night, dungeons — [#9](https://github.com/corymstover/GrokBotMTGCompanion/issues/9)
2. **Lore (as stories release):** Nauctis when its story publishes; re-check ❓ character statuses; re-run `scripts/crawl_story_index.py` — [#12](https://github.com/corymstover/GrokBotMTGCompanion/issues/12), [#14](https://github.com/corymstover/GrokBotMTGCompanion/issues/14)
3. **EDH:** more skeletons per archetype (optional); re-run combo detection each cycle (`scripts/detect_combos.py`)
4. **Maintenance (main ongoing work):** each cycle, refresh cards, ingest new sets (Star Trek 2026-11, Nauctis 2027-02), re-run combos, and check the B&R list — [#17](https://github.com/corymstover/GrokBotMTGCompanion/issues/17)

## 🗂 Key files
| File | Purpose |
|---|---|
| [Knowledge Index](Knowledge%20Index.md) | File map, maintenance rules, canon flags, source hierarchy, cycle checklist |
| [Progress Tracker](Progress%20Tracker.md) · [Update Log](Update%20Log.md) | Quantitative progress · every change with date/files/reason |
| [Card Data Conventions](Card%20Data%20Conventions.md) · [Card Index](Card%20Index.md) | Card entry format & storage · which cards have entries |
| [EDH Standards](EDH%20Standards.md) · [EDH Archetypes](EDH%20Archetypes.md) · [EDH Staples](EDH%20Staples.md) | Commander rules, color identity, Archidekt format, brackets, synergy notes · 12 archetype guides · data-derived staples by identity and role |
| [Rules Interactions](Rules%20Interactions.md) | CR 2026-09-25 rules topics, quoted verbatim, with official rulings linked to card entries |
| [Master Timeline](Master%20Timeline.md) · [Planes Index](Planes%20Index.md) · [Characters Index](Characters%20Index.md) · [Conflicts & Arcs](Conflicts%20%26%20Arcs.md) · [Story Archive Index](Story%20Archive%20Index.md) | Lore |

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
python3 scripts/build_mana_bases.py && python3 scripts/build_packages.py && python3 scripts/build_wincons.py && python3 scripts/build_interaction.py && python3 scripts/build_pairings.py && python3 scripts/build_mulligans.py   # Phase 1 EDH guides
python3 scripts/build_cedh.py [--refresh]   # cEDH Primer (--refresh re-queries Commander Spellbook)
python3 scripts/crawl_story_index.py enumerate && python3 scripts/crawl_story_index.py fetch && python3 scripts/crawl_story_index.py index   # story archive index
python3 scripts/resolve_card_links.py "Planes Index.md"   # turn [[Card Name]] placeholders in hand-written pages into card-entry links
```
State: [`data/ingest_state.json`](data/ingest_state.json) · index: [`data/card_index.csv`](data/card_index.csv).

## 🏷 Releases
`v0.1-1000-cards` · `v0.2-5000-cards` · `v0.3-10000-cards` · `v0.4-20000-cards` · `v1.0-33894-cards` · `v1.1-cycle3-lore-edh-rules` · `v1.2-cycle4-rules-lore-edh` · `v1.3-cycle5-rules-lore-maintenance` · `v1.4-cycle6-edh-depth`

*Card data © Wizards of the Coast, via [Scryfall](https://scryfall.com). Lore summaries cite official [magic.wizards.com](https://magic.wizards.com/en/story) pages. Unofficial fan project under the Wizards Fan Content Policy.*
