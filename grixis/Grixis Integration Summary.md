---
title: "Grixis Integration Summary"
category: meta
tags: [grixis, summary, follow-ups]
issues: [59, 60, 61, 62, 63]
generated_by: hand-written
sources: [grixis-repo]
related: ["grixis/Grixis Corrections.md", "Front-Matter Schema.md", "grixis/Grixis Refinement Cycle.md", "EDH Deck Evaluation Checklist.md", "EDH Deck Template.md", "grixis/Grixis Evaluation.md"]
schema: 2
---

# Grixis Integration Summary

> **Bot cycle 16 · milestone [Grixis integration](https://github.com/corymstover/GrokBotMTGCompanion/milestone/13) · issues [#59](https://github.com/corymstover/GrokBotMTGCompanion/issues/59)–[#63](https://github.com/corymstover/GrokBotMTGCompanion/issues/63).** What we took from the user's [grixis-commander-encyclopediaGPT](https://github.com/corymstover/grixis-commander-encyclopediaGPT) repo (read-only; commit `df1abb9` in Bot cycle 16, **re-analyzed at `1836b97` in Bot cycle 37**), what was fixed, what was generalized for every color identity, and what remains. Back to [Grixis](README.md).

## Contents
- [Bot cycle 39 commander-first refinement](#bot-cycle-39-commander-first-refinement)
- [Bot cycle 38 pending-legality pages](#bot-cycle-38-pending-legality-pages)
- [Bot cycle 37 re-analysis](#bot-cycle-37-re-analysis)
- [Source repo inventory](#source-repo-inventory)
- [What was integrated](#what-was-integrated)
- [What was left out and why](#what-was-left-out-and-why)
- [Fixes](#fixes)
- [What was generalized](#what-was-generalized)
- [What we did not take](#what-we-did-not-take)
- [Recommended follow-ups](#recommended-follow-ups)
- [Reproducing](#reproducing)

## Bot cycle 39 commander-first refinement
Cory set a new [mission](Grixis%20Mission.md): each deck must be the definitive, maximally optimized version of *its commander's* deck. Batch progress, metrics for all 62 decks and the method are on the [Grixis Refinement Cycle](Grixis%20Refinement%20Cycle.md) page. Refined lists appear as a *Refined list* section on the deck pages; the source list stays credited. Final lists are exported for Archidekt in [exports/grixis-archidekt/](../exports/grixis-archidekt/README.md).

*Bot cycle 43:* batch 5 (10 decks) completes the 60 legal decks. Sol'kanar the Swamp King −Windfall +Well of Lost Dreams; The Rani −Mystic Remora +Idol of Oblivion. The [end-of-cycle summary](Grixis%20Refinement%20Cycle.md#end-of-cycle-summary-60-legal-decks) is written; tag `v2.5-grixis-refinement`. *Bot cycle 42:* batch 4 (12 decks). Nicol Bolas −No Mercy +Megrim (hand-picked, after a hand review). Source still at `1836b97`. *Bot cycle 41:* batch 3 (13 decks) and hand-picked swaps. Kefka −Final Fortune +Liliana's Caress and −Valley Floodcaller +Dauthi Voidwalker. Evelyn and Marchesa, Dealer of Death were reviewed by hand and left unchanged. Source still at `1836b97`. *Bot cycle 40:* power guard plus a written review for each swap. The batch-1 re-check reverted 3 swaps (Chandra for Deadly Rollick, Whispersilk Cloak for Deflecting Swat, Quest for the Nihil Stone for Reanimate). Batch 2 covers 13 decks. The manual overlap review is on the Refinement Cycle page. The Grixis source is still at `1836b97` (pulled 2026-10-16, no upstream changes).

## Bot cycle 38 pending-legality pages
Cory asked for all 62 Grixis decks in the companion. **62/62 deck pages: 60 legal + 2 ⏳ pending legality.**
- **Pending pages:** [The Madcap Jester](decks/the-madcap-jester.md) (not-yet-legal: The Madcap Jester, Dragon's Smile) and [Tresserhorn's Lord, Returned](decks/tresserhorns-lord-returned.md) (not-yet-legal: Tresserhorn's Lord, Returned). Set `mbc` releases 2026-10-19; on 2026-10-16 the Scryfall API and bulk list these cards as `not_legal`. Each page has a ⏳ banner at the top and `legality_status: pending`, `legal_from: 2026-10-19`, `pending_cards` in its front matter.
- **Excluded from legal counts:** the README Decks table, the [Packages](Grixis%20Packages.md) library (N = 60), and every "legal" number. The [Evaluation](Grixis%20Evaluation.md) and [Corrections](Grixis%20Corrections.md) pages list them as pending (2 `pending legality` entries).
- **Registry:** `data/grixis_pending.json` (deck id → status, legal_from, set, cards).
- **Validation:** `validate_all` accepts the listed not-legal cards only while `legality_status` is pending and `legal_from` is in the future. Once the date passes, it fails ("pending legality expired") until the deck is activated. It also fails if a listed card is already legal or the registry and page disagree.
- **Activation:** `python3 scripts/activate_pending_grixis.py` (`--check` for a read-only live check). It refreshes the Scryfall bulk, re-checks the listed cards, flips decks to `active`, and rebuilds the pages, calibration, enrichment and validate_all.

## Bot cycle 37 re-analysis
Source moved from `df1abb9` to `1836b97`: 275 commits, 400 files changed (2026-10-15 to 2026-10-16). The clone at `/workspace/grixis-src` was only fast-forwarded and never modified.
- **Status changes:** the 22 lists that were UNREFINED in Bot cycle 16 are now **APPROVED / LOCKED** (user approval 2026-10-15). All 62 are approved. **No list was removed.** The 40 lists imported in cycle 16 are byte-identical (same approved SHA-256). Only their retrospective gate files were regenerated, with new timestamps.
- **New in the source:**
  - `exports/archidekt_2026-10-15/`: a 62-deck Archidekt import package with `manifest.csv`. All 62 lists we selected match it card for card.
  - Per-deck *approval-ready verification*, *candidate decision* and mandatory *99-slot whole-list audit* records.
  - Per-deck artifact paths in `state/current_deck_overrides.json`.
  - One-shot finalizer scripts and workflows.
- **Integrated:** the **20 newly approved, currently legal lists**, so 60 decks are integrated now. These are Norman Osborn // Green Goblin (deck id `Goben__Gene_Splice_Savant`), Nicol Bolas, Nicol Bolas the Ravager, both Obekas, Parnesse, Rograkh + Silas Renn, Saruman, both Saurons, Sedris, both Sol'kanars, both Tetsuos, The Rani, The Valeyard, Thraximundar, Wick and Zevlor. All 20 pass Gate A. Commander Spellbook finds 105 more complete combos (46 two-card infinite).
- **Still left out (awaiting legality):** The Madcap Jester (with Dragon's Smile) and Tresserhorn's Lord, Returned. Set `mbc` releases 2026-10-19. On 2026-10-16 both the Scryfall API and the bulk list them as `not_legal`. The source approved both lists. Madcap is under its future-release exception. ⚠️ Tresserhorn's record already claims official legality ([finding](Grixis%20Corrections.md#source-repo-structural-findings)).
- **Re-evaluation of all 62 lists** (`grixis_eval.py`, Scryfall bulk 2026-10-15 09:02):
  - The only hard issues are the known ones: Bjorna + Cecily's 2 banned cards (already corrected) and the 3 `mbc` cards.
  - 17,683 Oracle rows in 46 source audit files: 0 outdated.
  - The newer bulk (2026-10-15 21:01) changes **no** Oracle text, Commander legality, Game Changer flag or color identity for any card, so the KB stays on the 09:02 bulk. Its EDHREC ranks drive the Phase 8 batches.
- **Bracket floors:**
  - Game Changers + combos: 54 decks at Bracket 4 and 6 at Bracket 3. No source target is below its floor.
  - 5 decks target Bracket 4 on a Game Changer floor of 3: Cult of Skaro, Dr. Eggman, Edea, Lord of Tresserhorn and Parnesse. Parnesse has 21 two-card infinites.
  - The 11 Bracket-5 (cEDH) targets all sit at floor 4 with 15–22 Game Changers. Bracket 5 is intent, not a barometer.
- **Land-count flags (guidance):** fewer than 32 lands with an average nonland MV above 3.0. **Ashad** (30 / 3.41) and **Dr. Eggman** (31 / 4.21) are unchanged in the source and stay flagged. **Saruman** (31 / 3.35) and **Sedris** (31 / 3.43) are new flags.
- **Lutri:** unchanged. The source still keeps Lutri (banned as a companion), Trade Secrets and Yawgmoth's Bargain as project exceptions. Our corrected list keeps the cycle 16 fixes.
- **Corrections:** 129 in total (cycle 16: 87). Format 60, bracket 60, legality 2, provenance 2, companion 1, structure flags 4.
- **Standards:** new [Checklist Gate F](../EDH%20Deck%20Evaluation%20Checklist.md#gate-f--approval-ready-candidate-and-lock) (approval-ready candidate by hash, audit tally, dated legality checkpoint, export manifest), with a matching [Template §6](../EDH%20Deck%20Template.md#6-finalization-record) addition, credited to the source.

## Source repo inventory
*(Bot cycle 16, commit `df1abb9`. At `1836b97`: 968 commits, 1,017 tracked files, 151 refined list files, 62 workflows, 96 scripts, 62/62 approved.)*
| Item | Count |
|---|---|
| Commits / remote branches / tracked files | 693 / 49 / 645 |
| Decks (commanders) | **62** Grixis lists (one partner pair, one two-commander "Grixistax" list) |
| Frozen FINAL baseline | `source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz`: 62 CSV + 62 TXT |
| Refined list files | 105 in `refinement/decklists/` (baselines, candidates, proposals, approved) |
| User-approved and locked lists | **40** (decks #1–40 in tracker order, per `state/current_deck_overrides.json`) |
| Commander blueprints / decision records / approval records / evidence dossiers | 20 / 54 / 32 / 11 |
| Verification artifacts / tests / rules reviews | 220 / 35 / 1 (Abaddon interaction review, 63 KB) |
| Method documents | Refinement Protocol v1, Deck Quality Gates v3, Adaptive Pipeline v2 (+ contract, freeze checklist, stopping rules), Oracle Data Access v1, Workflow Optimization Playbook, 3 templates |
| Automation | 34 scripts, 50 GitHub Actions workflows, 19 tests (baseline hash/count verification, weekly Scryfall refresh) |

## What was integrated
- **40 decklists**, i.e. every user-approved list, in [grixis/decks/](decks/). Each page has a commander block, re-validation (✅ for all 40), Game Changers and bracket floor, a corrections table, an Archidekt import block, a card breakdown keeping the source's role tags and pinned printings, and **the source's blueprint, swap decisions, approval record and evidence dossiers quoted verbatim**. Each quote names its source path (`from grixis-commander-encyclopediaGPT, path …`). Commander Spellbook finds **288 complete combos, 83 two-card infinite, in 19 of the 40 decks**.
- Coverage: 1,100 distinct cards. Combo-adjusted floors: 35 decks at Bracket 4, 5 at Bracket 3. Source targets: 23 decks Bracket 4, 9 Bracket 5, 8 not stated.
- [Grixis Packages](Grixis%20Packages.md): cross-deck package library (cards in 4 or more lists, by the source's role tags) plus four source rules insights checked against Oracle text.
- [Grixis Evaluation](Grixis%20Evaluation.md): check results for **all 62** lists. [Grixis Corrections](Grixis%20Corrections.md): every fix.

## What was left out and why
- **20 lists (#41–62 in the source's order, minus the 2 below)**: the source's own state file marks them UNREFINED. Its whole-list audit has not run on them, so they are frozen baselines that will change. All 20 pass our hard checks (100 cards, singleton including Nazgûl's nine-copy rule, identity, legality). They are ready to import once approved (see follow-ups).
- **2 future-release lists** (*Bot cycle 38: now published as ⏳ pending-legality pages, not left out; see [above](#bot-cycle-38-pending-legality-pages)*): The Madcap Jester (and Dragon's Smile) and Tresserhorn's Lord, Returned. These cards are in Scryfall set `mbc` (release 2026-10-19) and are `not_legal` in Commander today. The source registers them as future-release exceptions.

## Fixes
**87 logged corrections** ([table](Grixis%20Corrections.md#corrections-table)):
| Type | Count | What |
|---|---|---|
| legality | 2 | Bjorna + Cecily list: banned **Trade Secrets → Wizard Class** and **Yawgmoth's Bargain → Flame of Anor**. Both replacements come from the source dossier's own list of close alternatives |
| companion | 1 | Lutri as companion dropped (banned as a companion in Commander). It was already missing from the approved 100-card file |
| bracket | 40 | The source never counts Game Changers. Added counts, the floor, and the Spellbook combo floor to every deck. No source target is below its floor |
| format | 40 | `[Commander]` → `[Commander{top}]`; 3,581 untagged lines got back the role tags the source used in its FINAL baseline or other decks; 183 lines with no source tag got a type tag; 94 pinned printings moved to the breakdown table |
| provenance | 2 | Brass, Unsinkable and Anhelo: the approved SHA-256 matches no file, so the list was identified by its Card_Verification CSV |
| structure (flag) | 2 | Ashad (30 lands, average MV 3.41) and Dr. Eggman (31 lands, average MV 4.21): flagged for mana-base review as **guidance**. The lists are unchanged |

**Oracle text:** 16,137 Oracle-text rows in 34 source audit files were compared with current Oracle. **0 are outdated.** The source refreshed Scryfall data on 2026-10-12 to 2026-10-15. Quotes in its Markdown notes match Oracle, apart from one abridged quote (reminder text omitted). There is no pre-2024 "enters the battlefield" wording.

**Name resolution:** every card resolves. Note for importers: the Scryfall face names "Boltwave" and "Reanimate" also belong to digital-only or prepare-layout cards. The evaluator resolves full card names first and prefers paper cards.

## What was generalized
Everything below works for **any color identity**. The pages state what came from the Grixis repo.
| New / changed | From the Grixis repo | Repo addition |
|---|---|---|
| [EDH Deck Template](../EDH%20Deck%20Template.md) | Commander-first blueprint fields (Protocol §4), whole-list role map with CORE / STRONG RETAIN / ROLE-CONSTRAINED / CUT CANDIDATE labels (Quality Gates v3), swap ledger (decision-ledger template), 0–5 card-fit rubric and A/B/C triage (Protocol §5), finalization certificate | Commander block, link to our page layout and front-matter |
| [EDH Deck Evaluation Checklist](../EDH%20Deck%20Evaluation%20Checklist.md) | Gate order, rules-line verification, red-team categories, commander-necessity test, homogenization check, evidence labels, hypothesis-first testing, stop and reopen rules | Gate A (machine-checked correctness), Gate B (Game Changer and combo floor ≤ stated bracket), official legality vs house exceptions |
| [`scripts/evaluate_decklist.py`](../scripts/evaluate_decklist.py) | The idea of a fail-closed structural verifier (`scripts/verify_baseline.py` there) | Any-identity evaluator on our Scryfall DB: name resolution, eligibility and pairing, 100 cards, singleton with Oracle copy exceptions, identity, legality, companion, GC, extra turns, MLD, optional Spellbook combos, exit code 1 on hard failure |
| [EDH Standards](../EDH%20Standards.md#deck-evaluation-method-from-the-grixis-repo) | Method summary; "official legality and project authorization recorded separately" | Rule that published lists must be officially legal; checklist step 7; stale open question about combo detection fixed |
| `scripts/front_matter.py` | — | Registers the new pages and `grixis/decks/` (deck `kind: grixis`, `source_repo` key) |

## What we did not take
The source's process machinery is specific to running a 62-deck campaign: the content-addressed pipeline, state machine, CI telemetry, Forge-AI simulation qualification, hash manifests, and per-gate JSON packets. We link to it but did not copy it. Our checks run by script, and git history keeps provenance. The one Forge pilot result that touches a card choice (Aurora Phoenix vs Mind's Desire: inconclusive, no change) is quoted in the Abaddon decision ledger.

## Recommended follow-ups
Tracked in [#63](https://github.com/corymstover/GrokBotMTGCompanion/issues/63). None of these were started.
1. ✅ *Done in Bot cycle 37:* imported the 20 lists the source approved on 2026-10-15. Earlier text: import the remaining 20 lists as the source approves them: re-run `python3 scripts/build_grixis.py` (it picks up new approvals from the source state file), then `front_matter.py`.
2. After 2026-10-19 (follow-up scheduled for 2026-10-20), run `python3 scripts/activate_pending_grixis.py` (Bot cycle 38), then the refinement pass for the 2 decks (`grixis_refine.py --plan 6`; see the [end-of-cycle summary](Grixis%20Refinement%20Cycle.md#pending-decks-not-in-the-60)). It refreshes the Scryfall bulk, re-checks the three `mbc` cards (still `not_legal` on 2026-10-16) and flips The Madcap Jester and Tresserhorn's Lord, Returned from ⏳ pending to active. `validate_all` fails from 2026-10-19 until this is done.
3. Optional optimization pass (guidance): the low-land flags (Bot cycle 37: Ashad, Dr. Eggman, Saruman, Sedris), and the 5 decks whose source target (Bracket 4) is above their Game Changer floor of 3 (Bot cycle 37: Cult of Skaro, Dr. Eggman, Edea, Lord of Tresserhorn, Parnesse). These are not errors, but they are worth a Rule 0 note.
4. Re-run Spellbook (`build_grixis.py --refresh-combos`) during the regular maintenance cycle ([#17](https://github.com/corymstover/GrokBotMTGCompanion/issues/17)).
5. Use the new template and checklist when upgrading the 46 EDHREC-derived [decks/](../decks/) skeletons, starting with a blueprint for each.

## Reproducing
```bash
git clone https://github.com/corymstover/grixis-commander-encyclopediaGPT /workspace/grixis-src   # read-only source
python3 scripts/build_grixis.py            # runs grixis_eval.py, writes grixis/ + data/grixis_*.json (Spellbook results cached)
python3 scripts/front_matter.py && python3 scripts/front_matter.py --check
```
