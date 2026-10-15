---
title: "Grixis Integration Summary"
category: meta
tags: [grixis, summary, follow-ups]
issues: [59, 60, 61, 62, 63]
generated_by: hand-written
sources: [grixis-repo]
related: ["Front-Matter Schema.md", "grixis/Grixis Corrections.md", "grixis/README.md", "EDH Deck Evaluation Checklist.md", "EDH Deck Template.md", "EDH Standards.md"]
schema: 2
---

# Grixis Integration Summary

> **Bot cycle 16 · milestone [Grixis integration](https://github.com/corymstover/GrokBotMTGCompanion/milestone/13) · issues [#59](https://github.com/corymstover/GrokBotMTGCompanion/issues/59)–[#63](https://github.com/corymstover/GrokBotMTGCompanion/issues/63).** What we took from the user's [grixis-commander-encyclopediaGPT](https://github.com/corymstover/grixis-commander-encyclopediaGPT) repo (read-only; commit `df1abb9`), what was fixed, what was generalized for every color identity, and what remains. Back to [Grixis](README.md).

## Contents
- [Source repo inventory](#source-repo-inventory)
- [What was integrated](#what-was-integrated)
- [What was left out and why](#what-was-left-out-and-why)
- [Fixes](#fixes)
- [What was generalized](#what-was-generalized)
- [What we did not take](#what-we-did-not-take)
- [Recommended follow-ups](#recommended-follow-ups)
- [Reproducing](#reproducing)

## Source repo inventory
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
- **2 future-release lists:** The Madcap Jester (and Dragon's Smile) and Tresserhorn's Lord, Returned. These cards are in Scryfall set `mbc` (release 2026-10-19) and are `not_legal` in Commander today. The source registers them as future-release exceptions.

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
1. Import the remaining 20 lists as the source approves them: re-run `python3 scripts/build_grixis.py` (it picks up new approvals from the source state file), then `front_matter.py`.
2. Re-check the three `mbc` cards after 2026-10-19 for Commander legality.
3. Optional optimization pass (guidance): the two low-land flags, and the 5 decks whose source target (Bracket 4) is above their Game Changer floor of 3 (Ashad, Cult of Skaro, Dr. Eggman, Edea, Lord of Tresserhorn). These are not errors, but they are worth a Rule 0 note.
4. Re-run Spellbook (`build_grixis.py --refresh-combos`) during the regular maintenance cycle ([#17](https://github.com/corymstover/GrokBotMTGCompanion/issues/17)).
5. Use the new template and checklist when upgrading the 46 EDHREC-derived [decks/](../decks/) skeletons, starting with a blueprint for each.

## Reproducing
```bash
git clone https://github.com/corymstover/grixis-commander-encyclopediaGPT /workspace/grixis-src   # read-only source
python3 scripts/build_grixis.py            # runs grixis_eval.py, writes grixis/ + data/grixis_*.json (Spellbook results cached)
python3 scripts/front_matter.py && python3 scripts/front_matter.py --check
```
