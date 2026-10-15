---
title: "EDH Deck Template"
category: edh
tags: [template, blueprint, swap-ledger, methodology]
issues: [62, 81, 96]
generated_by: hand-written
sources: [grixis-repo, cr]
related: ["EDH Deck Evaluation Checklist.md", "EDH Standards.md", "EDH Lore-Themed Deckbuilding.md", "grixis/README.md", "EDH Win Conditions.md", "grixis/Grixis Packages.md"]
schema: 2
---

# EDH Deck Template

> **Bot cycle 16 ([#62](https://github.com/corymstover/GrokBotMTGCompanion/issues/62)).** A commander-first template for building or refining a deck in **any color identity**. It is generalized from the user's Grixis project, [grixis-commander-encyclopediaGPT](https://github.com/corymstover/grixis-commander-encyclopediaGPT), mainly `refinement/Grixis_Refinement_Protocol_v1.md` §4–7, `architecture/DECK_QUALITY_GATES_V3.md` and `refinement/Deck_Finalization_Certificate_TEMPLATE.md`. Sections marked **(from the Grixis repo)** keep its method. Sections marked **(repo addition)** connect it to this knowledge base. The method is a **process standard, not rules of the game**. Every strategic answer you write into it is guidance and must be labeled so ([EDH Standards](EDH%20Standards.md)). Check a finished list with the [EDH Deck Evaluation Checklist](EDH%20Deck%20Evaluation%20Checklist.md). Worked examples: the 40 [Grixis decks](grixis/README.md).

## Contents
- [1. Commander block](#1-commander-block)
- [2. Commander-first blueprint](#2-commander-first-blueprint)
- [3. Role and package map (whole-list audit)](#3-role-and-package-map-whole-list-audit)
- [4. Swap ledger](#4-swap-ledger)
- [5. Card-fit rubric](#5-card-fit-rubric)
- [6. Finalization record](#6-finalization-record)
- [7. Page layout for a finished deck](#7-page-layout-for-a-finished-deck)
- [8. Lore-themed (story-first) extension](#8-lore-themed-story-first-extension)

## 1. Commander block
**(repo addition, per [EDH Standards → Commander first](EDH%20Standards.md#commander-first))**
```text
Commander(s):   [Name](cards/<L>/<prefix>.md#anchor) — {mana cost} — type line
Color identity: <WUBRG letters> (from the card entry, Scryfall color_identity)
Eligibility:    CR 903.3 basis (legendary creature / Vehicle / Spacecraft / "can be your commander")
Pairing:        Partner / Friends forever / Choose a Background / Doctor's companion / none
Companion:      none, or name + Commander legality as a companion (e.g. Lutri is banned as a companion)
```

## 2. Commander-first blueprint
**(from the Grixis repo, Protocol §4 and its per-deck blueprints, e.g. `refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md`)**. Fill this in **before** you look at candidate cards. A blank or machine-seeded profile does not count as a blueprint.

| Field | What to write |
|---|---|
| Commander identity | What the commander's Oracle text does, quoted from its entry, and the strategy it naturally points to |
| Primary plan | How the commander advances it |
| Secondary plan | Only if it really supports the primary plan |
| Win routes | Each route and what enables it (link [EDH Win Conditions](EDH%20Win%20Conditions.md)) |
| Key interactions | Commander-specific rules lines; cite CR and rulings when a line depends on them |
| Essential functions | Mana, draw/selection, interaction/protection, recovery, closing power. Adapt to the deck; these are not fixed quotas |
| Core cards/packages | Cards central to the deck's identity, and what would justify cutting each one |
| Constraints and failure modes | Colored pips, speed, what beats the deck |
| Natural power ceiling | Target bracket and why. Check it against the Game Changer floor ([Power bracket assessment](EDH%20Standards.md#power-bracket-assessment)) |
| Deliberately rejected homogenization | Strong but off-plan additions to avoid, e.g. generic combo packages that work without this commander |
| Commander-necessity test | What is lost if the commander is removed. If the plan barely changes, the blueprint or list needs rework |

## 3. Role and package map (whole-list audit)
**(from the Grixis repo, Deck Quality Gates v3 "Mandatory whole-deck optimization audit")**. Every one of the 99 slots gets a role and a retention label. Start from the commander and work outward, as if building the deck today with no attachment to the existing list.

| Card | Package / role | Retention | Commander-specific reason |
|---|---|---|---|
| … | e.g. Ramp · Draw · Removal · Tutor · Protection · Engine · Payoff · Finisher · Land | CORE / STRONG RETAIN / ROLE-CONSTRAINED RETAIN / CUT CANDIDATE | one sentence |

Then record, with numbers where they mean something: land count, basics, average nonland MV, ramp, draw/selection, interaction, protection, engines, payoffs, recursion and finishers. Name the weakest retained cards and packages.

## 4. Swap ledger
**(from the Grixis repo, Protocol §7 and `refinement/Candidate_Decision_Ledger_TEMPLATE.csv`)**. The unit of optimization is a **named swap**: "For this named role or package, is Candidate A a meaningful improvement over Cut B for this commander, and what evidence would change our mind?"

| ID | Role / package | Candidate | Proposed cut | Expected benefit | Trade-off | Oracle, identity and legality checked | Evidence (EDHREC inclusion/Lift, sample size, date; Spellbook; tests) | Decision | Reason |
|---|---|---|---|---|---|---|---|---|---|
| DECK-001 | | | | | | ✅ entry link | | ACCEPT / REJECT / HOLD | |

Rules for the ledger. A high-impact HOLD blocks finalization. Popularity, rank or a single favorable goldfish is not acceptance evidence. Compare each candidate with the *best plausible cut anywhere in the deck* when roles are interchangeable.

## 5. Card-fit rubric
**(from the Grixis repo, Protocol §5 Stage C)**. Score each considered card 0–5, with a one-sentence evidence note per dimension. Scores organize the evidence; they are not measurements. A legality, identity or count failure is a **veto** that no score offsets.

| Dimension | 0–5 | Evidence note |
|---|---|---|
| Commander-plan contribution | | |
| Functional contribution at the slot/package | | |
| Synergy with the other 99 cards and the commander | | |
| Efficiency (mana, timing, pips, opportunity cost) | | |
| Resilience and versatility when the ideal line is disrupted | | |
| Evidence strength (Oracle text and rulings, commander-specific data, tests) | | |

Triage before scoring: **A** (high impact, evaluate fully), **B** (close alternative), **C** (low impact; log a reason and stop). Evaluate in depth only the strongest 3–8 candidates per package.

## 6. Finalization record
**(from the Grixis repo, `refinement/Deck_Finalization_Certificate_TEMPLATE.md`, adapted)**
```text
Deck / commander:        Snapshot date:          List hash (sha256 of the import block):
Scryfall bulk date:      B&R checkpoint date:    House exceptions (if any, listed separately from official legality):
Gates: [ ] evaluate_decklist.py PASS   [ ] blueprint complete   [ ] every slot mapped   [ ] ledger closed (no high-impact HOLD)
       [ ] rules lines verified (CR/rulings cited)   [ ] Spellbook combos reviewed   [ ] bracket floor ≤ stated bracket
       [ ] red-team pass with zero new material swaps   [ ] commander-necessity test passed
Strongest rejected alternatives and why:
Remaining uncertainty (label each VERIFIED / HIGH_CONFIDENCE / PROVISIONAL / TEST_REQUIRED / BLOCKED):
Reopen triggers: Oracle/rules/legality change · material new card · repeated failure in real games · discovered error · user request
```

## 7. Page layout for a finished deck
**(repo addition)**. Use the layout of the [decks/](decks/) skeletons and [grixis/decks/](grixis/decks/): YAML front-matter (`scripts/front_matter.py`) → Commander → Validation → Bracket assessment → Corrections or changes → Decklist (Archidekt import, see [List format](EDH%20Standards.md#list-format-archidekt)) → Card breakdown (role, type, MV, identity, GC) → Commentary (guidance, attributed) → Combos (Commander Spellbook block).

## 8. Lore-themed (story-first) extension
**(repo addition, Bot cycle 21, [#81](https://github.com/corymstover/GrokBotMTGCompanion/issues/81)).** Use with [EDH Lore-Themed Deckbuilding](EDH%20Lore-Themed%20Deckbuilding.md). Fill this **before** the role map when the goal is a lore deck.

| Field | What to write |
|---|---|
| Deck type | Arc-based or character-based |
| Story the deck tells | One cited paragraph; link Conflicts & Arcs / dossier / Timeline |
| Story packages | Beat or chapter names (not only Ramp/Draw) |
| Story keywords & sets | Regex/keywords and Scryfall set codes used as evidence |
| Lore score target | ≥ 85% of all non-basic cards (commander + every non-land + every non-basic land; basics excluded) story-linked by name, flavor text, story-set printing or official story page (Bot cycle 23). Mechanical/type echoes are guidance and don't count. Check land flavor text too |
| Deliberately rejected power | Game Changers / infinites / off-story staples you skipped and why (guidance) |
| Playability budget | Labeled unlinked playability slots — at most ~15% of non-basic cards |

Finished pages live under `decks/lore-*.md` and are rebuilt by `scripts/build_lore_decks.py`.
