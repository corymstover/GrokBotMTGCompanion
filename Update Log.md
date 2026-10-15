---
title: "Update Log"
category: meta
tags: [changelog]
issues: []
generated_by: hand-written
sources: []
related: ["Contradictions & Retcons Log.md", "Knowledge Index.md", "Planeswalker Dossiers.md", "Conflicts & Arcs.md", "Front-Matter Schema.md", "Lore Primary Sources.md"]
schema: 2
---

# Update Log

> Every update records **date · summary · files affected · reason**. Newest first. See [Knowledge Index](Knowledge%20Index.md#maintenance-rules).

## Contents
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
