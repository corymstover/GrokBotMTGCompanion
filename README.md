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
| EDH | 🟢 Standards + **46 validated decks (32 core skeletons covering every color identity + 10 plane-restricted + 4 themed)** + **12 [archetype guides](EDH%20Archetypes.md)** ([#19](https://github.com/corymstover/GrokBotMTGCompanion/issues/19)) + **Commander Spellbook combo detection** on every deck (218 complete combos, 63 two-card infinite in 18 decks; combo-adjusted bracket floors, [#15](https://github.com/corymstover/GrokBotMTGCompanion/issues/15)) + [EDH Staples](EDH%20Staples.md) + 15 rulings-backed synergy notes | [EDH Standards](EDH%20Standards.md) · [EDH Archetypes](EDH%20Archetypes.md) · [EDH Staples](EDH%20Staples.md) · [decks/](decks/) |
| Story archive | 🟢 **612 official story/lore pages indexed** (575 live, 37 🗄️ archived from the Internet Archive), from the sitemap plus the Wayback Machine index of the retired Uncharted Realms and magic-story paths ([#14](https://github.com/corymstover/GrokBotMTGCompanion/issues/14)) | [Story Archive Index](Story%20Archive%20Index.md) |
| EDH depth (Bot cycle 6) | 🟢 **Phase 1 of the [ROADMAP](ROADMAP.md)**, all data-derived from Scryfall and every card Commander-legal with GC flags: [Mana Bases](EDH%20Mana%20Bases.md) for all 32 identities (1,118 non-basic lands classified) · [Packages](EDH%20Packages.md) (13 packages, 33 sub-packages) · [Win Conditions](EDH%20Win%20Conditions.md) (8 categories, 46 two-card combo kills) · [Interaction](EDH%20Interaction.md) (6 hierarchies, 19 buckets) · [Pairings](EDH%20Pairings.md) (8 partner abilities, 3,104 legal pairs, identity matrix) · [Mulligans](EDH%20Mulligans.md) (CR 103.5 plus exact odds) · ⚠️ [cEDH Primer](cEDH%20Primer.md) (competitive/Bracket 5, 61 Spellbook combos) · **Bot cycle 7:** [Upgrade Paths](EDH%20Upgrade%20Paths.md) (32 commanders, 576 upgrade rows in 3 price steps, 256 likely cuts; EDHREC budget vs expensive) · [Themed & Plane-Restricted Decks](EDH%20Themed%20Decks.md) (10 plane-only + 4 themed, all validated; **Phase 1 complete**) ([#25](https://github.com/corymstover/GrokBotMTGCompanion/issues/25)–[#33](https://github.com/corymstover/GrokBotMTGCompanion/issues/33)) | [ROADMAP](ROADMAP.md) |
| Lore depth (Bot cycles 7–8) | 🟢 **Phase 2 complete (Bot cycle 8):** [Story Arc Summaries](Story%20Arc%20Summaries.md) (19 arcs and 135 cited beats, from BFZ/OGW to Reality Fracture) · [Planeswalker Dossiers](Planeswalker%20Dossiers.md) (21 dossiers; cycle 8 added Gideon, Nahiri, Sorin, Ugin, Bolas, Ral, Oko and Tezzeret, and sourced 4 more spark moments) · [Omenpath & Multiverse Connections](Omenpath%20%26%20Multiverse%20Connections.md) · [Art & Flavor Story Links](Art%20%26%20Flavor%20Story%20Links.md) (269 Story Spotlight cards across 17 arcs, verbatim Scryfall flavor and artist; 32 matched to the story page captioning their art, plus 263 captioned cards on 53 cited story pages) · [Side-Media Index](Side-Media%20Index.md) (22 items: novels, e-books, comics and other media, each citing an official Wizards page and flagged ✅/⚠️/❓) ([#34](https://github.com/corymstover/GrokBotMTGCompanion/issues/34)–[#38](https://github.com/corymstover/GrokBotMTGCompanion/issues/38)) | [Story Arc Summaries](Story%20Arc%20Summaries.md) |
| Card & rules enrichment (Bot cycles 8–12) | 🟡 **Phase 3 nearly done:** keywords · printings · legality · [Tokens, Emblems & Dungeons](Tokens%2C%20Emblems%20%26%20Dungeons.md) ✅ ([#39](https://github.com/corymstover/GrokBotMTGCompanion/issues/39)–[#42](https://github.com/corymstover/GrokBotMTGCompanion/issues/42)). Next: artist index [#43](https://github.com/corymstover/GrokBotMTGCompanion/issues/43) | [Keyword Encyclopedia](Keyword%20Encyclopedia.md) · [Printing History](Printing%20History.md) · [Format Legality Matrix](Format%20Legality%20Matrix.md) · [Tokens, Emblems & Dungeons](Tokens%2C%20Emblems%20%26%20Dungeons.md) |
| Rules interactions | 🟢 **27 topics** (was 17). Cycle 5 added sagas, classes, phasing, DFCs/transform, the legend rule, "can't" beats "can", replacement-effect ordering, commander damage, partner/backgrounds, and leaving a multiplayer game. CR 2026-09-25 quoted verbatim, **37 official CR examples**, **139 linked rulings** ([#9](https://github.com/corymstover/GrokBotMTGCompanion/issues/9)) | [Rules Interactions](Rules%20Interactions.md) |

### Next priorities
0. **[ROADMAP](ROADMAP.md) Phase 3:** artist index [#43](https://github.com/corymstover/GrokBotMTGCompanion/issues/43) (#39–#42 done through Bot cycle 12), then Phase 4 [#44](https://github.com/corymstover/GrokBotMTGCompanion/issues/44)–[#47](https://github.com/corymstover/GrokBotMTGCompanion/issues/47)
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
| [EDH Upgrade Paths](EDH%20Upgrade%20Paths.md) · [EDH Themed Decks](EDH%20Themed%20Decks.md) · [EDH Mana Bases](EDH%20Mana%20Bases.md) · [EDH Packages](EDH%20Packages.md) · [EDH Win Conditions](EDH%20Win%20Conditions.md) · [EDH Interaction](EDH%20Interaction.md) · [EDH Pairings](EDH%20Pairings.md) · [EDH Mulligans](EDH%20Mulligans.md) · [cEDH Primer](cEDH%20Primer.md) | Phase 1 deckbuilding guides (Bot cycles 6–7). The cEDH primer is competitive-only and kept separate |
| [ROADMAP](ROADMAP.md) | Refinement sprint brief: 4 phases, each tracked as a GitHub milestone with one issue per item |
| [Rules Interactions](Rules%20Interactions.md) · [Keyword Encyclopedia](Keyword%20Encyclopedia.md) · [Printing History](Printing%20History.md) · [Format Legality Matrix](Format%20Legality%20Matrix.md) · [Tokens, Emblems & Dungeons](Tokens%2C%20Emblems%20%26%20Dungeons.md) | CR topics, keywords, printings, legality, tokens/emblems/dungeons |
| [Story Arc Summaries](Story%20Arc%20Summaries.md) · [Planeswalker Dossiers](Planeswalker%20Dossiers.md) · [Omenpath & Multiverse Connections](Omenpath%20%26%20Multiverse%20Connections.md) · [Art & Flavor Story Links](Art%20%26%20Flavor%20Story%20Links.md) · [Side-Media Index](Side-Media%20Index.md) · [Master Timeline](Master%20Timeline.md) · [Planes Index](Planes%20Index.md) · [Characters Index](Characters%20Index.md) · [Conflicts & Arcs](Conflicts%20%26%20Arcs.md) · [Story Archive Index](Story%20Archive%20Index.md) | Lore |

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
python3 scripts/build_upgrade_paths.py [--refresh]   # EDH Upgrade Paths (EDHREC budget/expensive pages)
python3 scripts/build_deck_skeleton.py "Commander" --sets <codes> --plane <Plane> --out plane-<slug>   # plane-restricted deck (or --theme <edhrec-theme>)
python3 scripts/build_themed_index.py      # EDH Themed Decks index
python3 scripts/build_cedh.py [--refresh]   # cEDH Primer (--refresh re-queries Commander Spellbook)
python3 scripts/crawl_story_index.py enumerate && python3 scripts/crawl_story_index.py fetch && python3 scripts/crawl_story_index.py index   # story archive index
python3 scripts/resolve_card_links.py "Planes Index.md"   # turn [[Card Name]] placeholders in hand-written pages into card-entry links
```
State: [`data/ingest_state.json`](data/ingest_state.json) · index: [`data/card_index.csv`](data/card_index.csv).

## 🏷 Releases
`v0.1-1000-cards` · `v0.2-5000-cards` · `v0.3-10000-cards` · `v0.4-20000-cards` · `v1.0-33894-cards` · `v1.1-cycle3-lore-edh-rules` · `v1.2-cycle4-rules-lore-edh` · `v1.3-cycle5-rules-lore-maintenance` · `v1.4-cycle6-edh-depth` · `v1.5-cycle7-phase1-complete` · `v1.6-cycle8-phase2-complete`

*Card data © Wizards of the Coast, via [Scryfall](https://scryfall.com). Lore summaries cite official [magic.wizards.com](https://magic.wizards.com/en/story) pages. Unofficial fan project under the Wizards Fan Content Policy.*
