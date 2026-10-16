---
title: "Grixis Authority Model"
category: meta
tags: [grixis, authority, governance, legality, approvals]
issues: []
generated_by: hand-written
sources: [grixis-repo]
related: ["Front-Matter Schema.md", "grixis/Grixis Authority Gap Analysis.md", "grixis/Grixis Refinement Cycle.md", "grixis/README.md", "Update Log.md", "grixis/Grixis Evaluation.md"]
schema: 2
---

# Grixis Authority Model

> **Bot cycle 47 (milestone M0, "authority foundation"), 2026-10-16.** This page defines who decides what a Grixis deck *is*, how a list moves from the imported source baseline to a list Cory has approved, what counts as evidence, and how official Commander legality is kept apart from project authorization. It implements Cory's decisions on the [gap analysis](Grixis%20Authority%20Gap%20Analysis.md) and his eight binding constraints (recorded below as [standing rules](#standing-rules-corys-binding-constraints)). The data lives in [`data/grixis/`](../data/grixis/registry.json); `validate_all` enforces it (steps `authority` and `unit-tests`).

## Contents
- [Authority hierarchy](#authority-hierarchy)
- [Standing rules (Cory's binding constraints)](#standing-rules-corys-binding-constraints)
- [Deck states](#deck-states)
- [Evidence classes](#evidence-classes)
- [Legality model](#legality-model)
- [Hashes](#hashes)
- [Ceilings](#ceilings)
- [Files and checks](#files-and-checks)
- [Migration steps](#migration-steps)
- [The GPT repository's role](#the-gpt-repositorys-role)
- [Milestone acceptance criteria](#milestone-acceptance-criteria)
- [Testing doctrine: stress scenarios and red team](#testing-doctrine-stress-scenarios-and-red-team)
- [Why this is stricter than both earlier systems](#why-this-is-stricter-than-both-earlier-systems)

## Authority hierarchy

From highest to lowest. A lower level never overrides a higher one; it can only produce evidence for it.

1. **Cory's explicit instructions and approval records.** Only a human approver (`human_approvers` in the registry: `corymstover`) can move a deck to `APPROVED` or `CANONICAL_LOCKED`, resolve a ceiling, authorize a project exception, or accept a milestone. Each sign-off is a record in [`data/grixis/approvals.json`](../data/grixis/approvals.json) naming the exact list hash. There are **no records yet**.
2. **Official rules and data.** The Comprehensive Rules, Oracle text, Wizards' banned & restricted list and Game Changers list, through the cached Scryfall bulk. These decide *official* legality and are never overruled by a project decision. A project decision can only *authorize an exception*, which stays labeled as not Commander-legal.
3. **The canonical project list of each deck.** Exactly one per commander (rule 1). Today it is the source baseline imported from the GPT repository (commit `1836b97`), plus, for Bjorna + Cecily, the authorized exceptions the import had removed.
4. **Evidence:** source approvals (62/62 APPROVED/LOCKED in the GPT repo), GrokBot's cycle 39–44 refinements, interaction reviews (M1), blueprints (M2), audits and tests (M3–M6). Evidence informs; it does not decide.
5. **Heuristics and derived metrics** (EDHREC numbers, commander dependence, the v1 gates). Diagnostics only. Alone they can never justify a decision (`decision_support_ok`).

**Derived compliance projections** sit outside the hierarchy: they are computed from a canonical list and never compete with it.

## Standing rules (Cory's binding constraints)

These apply to every later milestone. Each names where it is enforced today.

| # | Rule | Enforced by |
|---|---|---|
| 1 | **One canonical project list per commander.** Bjorna + Cecily has `canonical_project_list` (with the authorized exceptions), `official_commander_compliance`, and an *optional* `official_legal_projection` labeled **"derived compliance projection (not canonical)"** in data and exports. A projection can never be canonical or in an approval state, and can never be approved. | `registry.schema.json` (`label` and `canonical` are constants, `approval_state` must be null); `approval_problems()` (also rejects a projection whose hash equals the canonical one, or any approval record naming it); `grixis_refine.py --check` on `exports/grixis-archidekt/index.json`; tests in `tests/test_legality.py`. |
| 2 | **Automated dispositions need evidence refs** to the blueprint, the dependency graph and the alternatives considered (plus redundancy, role/package and a reason), or they are **provisional**. | `audit.schema.json` (`review_status: provisional / complete`, required ref arrays); `disposition_status()` / `audit_problems()` flag a slot marked complete without them. |
| 3 | **The 15–40 full-review range is a default workload, not a gate.** Any candidate can be escalated to full review for: dependency analysis, a new card, an unusual Oracle interaction, a package gap, reviewer evidence (or a suspected rank miss). | `candidate.schema.json` (`workload.is_gate` is the constant `false`; `escalation.reasons` enum); `candidate_problems()` requires reasons, evidence refs and full review for an escalated candidate. |
| 4 | **Ceilings:** store `source_ceiling`, `grok_estimated_ceiling`, the evidence for each, and `resolved_ceiling` (null until Cory reviews). Never overwrite source history. Disagreement is flagged, not overridden. | `registry.schema.json` `ceiling`; `approval_problems()` (resolved_ceiling needs a human `resolved_by`; `disagreement` must equal source ≠ estimate); `--build` preserves human-set fields and never rewrites `source_ceiling` from anything but the archived source. |
| 5 | **Cycle counts are estimates.** Each milestone has explicit [acceptance criteria](#milestone-acceptance-criteria); a milestone is accepted only by Cory. | `program.milestones` in the registry (`status`, `accepted_by`, `accepted_date`, `criteria_doc` linking here). |
| 6 | **M6 is gated on M2 + M4 acceptance.** Before then, v2 recommendations are labeled **exploratory**. `APPROVAL_READY` and above also need M2 + M4 accepted. | `grixis_authority.py --check` (v2 output must say `exploratory: true` until both are accepted); `refine_v2.schema.json` `m6_gate`; `approval_problems()` for the gated states. |
| 7 | **Two optimizers, two objective functions.** The commander-first optimizer and the performance optimizer produce **independent first passes** from different objective functions (not two weightings of one score), reconciled afterwards. | `optimizer_pass.schema.json` (`pass_a` / `pass_b`, `objective_function.family` blueprint_fidelity vs measured_performance, `formula_sha256`, `informed_by`, `blind_to`, `reconciliation`); `check_reconciliation()` rejects equal families, equal formulas, a pass informed by the other, or performance inputs in the commander-first objective (and vice versa). |
| 8 | **APPROVAL_READY, APPROVED and CANONICAL_LOCKED stay distinct.** Nothing becomes approved or locked without Cory's explicit sign-off. | State machine (`TRANSITIONS`: APPROVED only from APPROVAL_READY, CANONICAL_LOCKED only from APPROVED); `approval_problems()` needs a human approval record matching the exact hash, a separate `CANONICAL_LOCKED` decision for locking, and a certificate for APPROVAL_READY. |

Further standing rules from the same steering:
- **Adversarial testing means scripted stress scenarios plus red-team analysis.** No multiplayer win-rate simulation (see [testing doctrine](#testing-doctrine-stress-scenarios-and-red-team)).
- **No box-checking.** Every milestone is judged by its acceptance criteria and by whether the end state is demonstrably more rigorous than both the old GrokBot process and the GPT process ([comparison](#why-this-is-stricter-than-both-earlier-systems)).

## Deck states

| State | Meaning | Entered from | Who may set it |
|---|---|---|---|
| `SOURCE_BASELINE` | Imported source list is the canonical list; nothing reviewed under this model yet. **60 decks.** | start, `PENDING_RELEASE`, `UNDER_REVIEW` | bot |
| `PENDING_RELEASE` | Canonical list holds cards not Commander-legal until a known date (2026-11-13). **2 decks** (The Madcap Jester, Tresserhorn's Lord). | start, `SOURCE_BASELINE` | bot |
| `UNDER_REVIEW` | Blueprint/audit work in progress. | `SOURCE_BASELINE`, `PENDING_RELEASE`, `CHALLENGER`, `REVIEW_REQUIRED`, `APPROVAL_READY`, `REOPEN_REQUIRED` | bot |
| `CHALLENGER` | At least one challenger list competes with the canonical list. | `UNDER_REVIEW`, `TESTING` | bot |
| `TESTING` | Paired tests / stress scenarios running. | `UNDER_REVIEW`, `CHALLENGER`, `REVIEW_REQUIRED` | bot |
| `REVIEW_REQUIRED` | Evidence conflicts or a reconciliation disagreement needs deep review. | `UNDER_REVIEW`, `CHALLENGER`, `TESTING`, `APPROVAL_READY` | bot |
| `APPROVAL_READY` | Certificate complete; packet waits for Cory. Needs M2 + M4 accepted and a finalization certificate. | `TESTING`, `REVIEW_REQUIRED` | bot |
| `APPROVED` | Cory approved this exact list hash. | `APPROVAL_READY` only | **Cory only** (approval record) |
| `CANONICAL_LOCKED` | Cory locked this exact hash; only a reopen trigger moves it. | `APPROVED` only | **Cory only** (separate lock record) |
| `REOPEN_REQUIRED` | A trigger fired on an approved/locked or baseline deck. | `SOURCE_BASELINE`, `APPROVED`, `CANONICAL_LOCKED` | bot (trigger) |

Every deck keeps a `state_history` (date, cycle, reason); every transition is checked against `TRANSITIONS`. **Reopen triggers** (all ten armed on every deck): `new_card`, `oracle_change`, `rules_change`, `legality_change`, `new_exception`, `test_failure`, `new_interaction`, `meta_shift`, `audit_error`, `user_instruction`. Today the check turns snapshot drift into a warning (no deck is approved yet) and into a failure once any deck is in a gated state without an open `oracle_change` / `rules_change` trigger; a changed canonical hash on an approved deck fails until it is set to `REOPEN_REQUIRED`.

**Challengers.** GrokBot's cycle 39–44 refinements are now **"GrokBot challenger (unapproved)"** records (6 decks: Abaddon the Despoiler, Kefka, Nicol Bolas, Norman Osborn, Sol'kanar, The Rani), with their swaps, hashes and engine (`grixis_refine v1`). The other 56 decks' old "at/near ceiling" verdicts are relabeled **"heuristic: no candidate passed v1 gates (not a certificate)"**. A challenger that Cory approves becomes canonical through `supersedes_hash`; an approval of a challenger that was never promoted fails the check.

## Evidence classes

Every claim is an evidence item (`data/grixis/schemas/evidence.schema.json`): `id`, `class`, `confidence`, `claim`, `source {kind, ref}`, `author`, `created`, optional `supersedes`. Ideas reused from the source's `grixis_pipeline/epistemic.py`; its levels map onto ours (`VERIFIED→verified`, `HIGH_CONFIDENCE→high`, `PROVISIONAL→moderate`, `TEST_REQUIRED→test_required`, `BLOCKED→blocked`).

| Class | What it is | Example |
|---|---|---|
| `fact` | Directly checkable against an authoritative source | Oracle text, a B&R entry, a Spellbook combo id |
| `derived_metric` | Computed from facts by a declared formula | commander dependence, EDHREC lift with sample size |
| `heuristic` | A rule of thumb or gate outcome | v1 power guard, "generic in ≥ 16 lists" |
| `hypothesis` | A claim to be tested | "Wizard Class keeps Cecily's hand engine intact" |
| `test_result` | Output of a pre-registered test, with limitations | paired goldfish delta with CI |
| `strategic_judgment` | Reasoned human or reviewer judgment with stated grounds | blueprint identity core |
| `approved_decision` | A recorded decision by Cory | an approvals.json record |

Confidence: `verified`, `high`, `moderate`, `low`, `test_required`, `blocked`. **Decision rule** (`decision_support_ok`): a decision needs at least one `fact`, `test_result`, `strategic_judgment` or `approved_decision`; heuristics, derived metrics and hypotheses alone never decide; any `blocked` or `test_required` item blocks the decision until resolved.

## Legality model

Two separate fields, everywhere (registry, exception registry, deck page front matter, exports manifest):

- **`official_commander_legality`** (per card) / **`official_commander_compliance`** (per list): what the official rules say. Values per card: `legal`, `banned`, `banned_as_companion`, `not_legal`, `not_legal_until_release`. Per list: `compliant`, `not_compliant_project_exceptions`, `pending_release`.
- **`project_authorization_status`**: what Cory authorized for this project. Per card: `AUTHORIZED_EXCEPTION`, `AUTHORIZED_FUTURE_RELEASE`, `NOT_REQUIRED`, `UNAUTHORIZED`. Per deck: `none`, `authorized_exceptions`, `authorized_future_release`.

**Render rule:** labels come only from `legality_label()`. An exception renders as "🚩 project exception, NOT Commander-legal: …"; a future-release card as "⏳ authorized future release, NOT Commander-legal yet (legal from …)". Nothing that is not officially legal is ever labeled legal. **Validators** accept a registered `AUTHORIZED_EXCEPTION` only on the legality issue for that exact deck and card; color identity, singleton, size and pairing are never excused. The `decks` step also requires the page's 🚩 banner and `official_commander_compliance: not_compliant_project_exceptions` front matter and refuses "all checks pass" on such a page.

**The exception registry** ([`data/grixis/exceptions.json`](../data/grixis/exceptions.json)) imports the source's 8-row `Project_Exceptions_Current_2026-10-12.csv`, each row verified against Scryfall (bulk 2026-10-15) and Wizards. **4 rows were corrected:**

| Row | Source said | Verified | Correction |
|---|---|---|---|
| Lutri, the Spellchaser (Bjorna, companion) | intentional exception, present in exports | Scryfall shows `legal` (the companion ban is not a Scryfall legality); Wizards bans Lutri **as a companion** | recorded as `banned_as_companion`; the source's approved 100-card file has **no Lutri line**, so the companion line is restored from the approval record |
| Nazgûl (Sauron, Lord of the Rings) | project exception | Oracle "A deck can have up to nine cards named Nazgûl"; deck runs 4 | **not an exception**: official card rule (CR 903.5b), `NOT_REQUIRED` |
| Nazgûl (Sauron, the Dark Lord) | project exception | same; deck runs 7 | same |
| Tresserhorn's Lord, Returned | approval record: "official Commander legality PASS" | Scryfall `not_legal` | `not_legal_until_release` (2026-11-13), `AUTHORIZED_FUTURE_RELEASE` |

Trade Secrets and Yawgmoth's Bargain (banned) are verified `AUTHORIZED_EXCEPTION`s; Madcap Jester and Dragon's Smile are verified future releases.

**Bjorna + Cecily (Cory decision 1).** The canonical project list restores Trade Secrets, Yawgmoth's Bargain and Lutri (companion), all labeled not Commander-legal. The Bot cycle 16 replacements (Wizard Class, Flame of Anor, no companion) live on only as the [derived compliance projection](decks/bjorna-nightfall-alchemist-cecily.md#official-legal-projection-derived-not-canonical) ([`data/grixis/projections.json`](../data/grixis/projections.json)). Exports: `source-baseline/bjorna-nightfall-alchemist-cecily.txt` is the canonical list (with `1 Lutri, the Spellchaser [Companion]` outside the 100); `projections/…official-legal-projection.txt` is the projection. The legacy path `bjorna-nightfall-alchemist-cecily.txt` keeps its pre-cycle-47 bytes and is labeled as the projection, because the M1 interaction review hashed it; see [migration](#migration-steps).

## Hashes

- **Logical list hash `lh1:`** (authoritative): SHA-256 over sorted lines `<zone>|<oracle_id>|<qty>\n` (zones commander / companion / main; quantities summed per card). Independent of line order, printings, role tags and spelling; changes when any card, quantity or zone changes.
- **Raw hash `sha256:`**: SHA-256 of the file bytes. Recorded for provenance (`source.raw_sha256`, `index.json raw_sha256`), never used for identity.
- **Why both:** the source mixed them. Two decks' recorded `approved_list_sha256` values (Admiral Brass, Unsinkable; Anhelo, the Painter) match no file; they are list digests. The registry stores the recorded value, the raw hash and `recorded_matches_raw` side by side.
- Each deck stores `baseline_hash` (the source file), `current_canonical_hash`, `canonical_differs_from_source` (with reasons) and `supersedes_hash` (null until a challenger is promoted).

## Ceilings

`ceiling.source_ceiling` (the source's stated bracket, with evidence; 53 decks state one, 9 do not), `ceiling.bracket_floor` (Game Changers, mass land denial, two-card infinites; a floor, not a target), `ceiling.grok_estimated_ceiling` (null until M2 evidence exists), `ceiling.resolved_ceiling` (null until Cory resolves it), `ceiling.disagreement` (null while either side is unknown). Target = each commander's natural ceiling (Cory decision 3). An estimate that disagrees with the source is flagged for Cory, never applied.

## Files and checks

| File | Role |
|---|---|
| [`data/grixis/registry.json`](../data/grixis/registry.json) | One entry per deck (§19 fields): state + history, approval, hashes, source repo/commit/path, canonical list, compliance vs authorization, projection, challengers, v1 verdict, historical approvals (`counts_as: evidence`), ceilings, blueprint/test/certificate slots, snapshots id, reopen triggers. Program milestones. Built by `scripts/grixis_authority.py --build` (human fields preserved). |
| [`data/grixis/exceptions.json`](../data/grixis/exceptions.json) | Verified exception registry (8 rows, 4 corrected). `--build-exceptions`. |
| [`data/grixis/approvals.json`](../data/grixis/approvals.json) | Human approval records. Empty. |
| [`data/grixis/projections.json`](../data/grixis/projections.json) | Derived compliance projections (Bjorna). |
| `data/grixis/schemas/*.schema.json` | 14 JSON Schemas (draft 2020-12): common, evidence, exception, registry, approval, refine_v2, and v1 drafts for blueprint, graph, audit, candidate, optimizer_pass, swap, test, certificate. |
| `data/grixis_refine_v2.json` | v2 exploratory recommendations (never final). |
| `exports/grixis-archidekt/index.json` | Label, role, state, compliance and both hashes for every export file. |

`validate_all` step **`authority`** (`grixis_authority.py --check`): schema validation of registry, exceptions, approvals and v2 output; the v2 exploratory gate; approval enforcement and projection rules for all 62 decks; registry freshness (rebuilds it and compares hashes, challengers, projection, compliance, source); snapshot drift; every exception row re-verified against current Scryfall, the canonical lists and `data/grixis_pending.json`. Step **`unit-tests`** (`scripts/run_tests.py`): the `tests/` suite (pytest when installed, a stdlib runner otherwise; the schema tests cross-check the stdlib validator against the `jsonschema` package when it is installed).

**grixis_refine.py versions.** v1 (cycles 39–44) is frozen and stays reproducible (`--engine v1 --plan N`); its output is challengers and heuristic verdicts. v2 (`--engine v2`) changes the method: gates become diagnostics recorded on each recommendation; the at-ceiling shortcut and the "all candidates failed, so ceiling" fallback are gone (every nonland slot of every deck is analyzed); reviewer protections, Game Changers, combo pieces and cheap mana are priors; only explicit project/user constraints (registered exceptions, the commanders) are hard; "preserve every source combo" is reported per candidate instead of required; EDHREC lift, trend z-score, sample size (`num_decks` / `potential_decks`, small samples flagged) and retrieval date (cache mtime; the payload has no fetch time) are recorded. v2 never writes deck pages or exports.

## Migration steps

Per deck, in order. M0 completed steps 1–4 for all 62.

1. **Baseline:** import the source list (repo, commit `1836b97`, path, raw + logical hash) as `SOURCE_BASELINE` / `PENDING_RELEASE`. ✅
2. **Exceptions:** verify and import the exception registry; restore authorized exceptions to the canonical list; derive projections. ✅
3. **Recover evidence:** source approvals as `historical_approvals` (evidence), cycle 39–44 refinements as challengers, v1 verdicts relabeled. ✅
4. **Labels:** pages, exports and the Refinement Cycle page carry state and labels. ✅
5. **Interaction review** (M1), hashing the canonical list. M1 reviewed the legacy export files; for the 6 challenger decks and Bjorna those are not the canonical list, so M1 must re-point to `canonical_project_list.export` and review the canonical deltas (see [M1](#m1)).
6. **Blueprint** (M2) → `blueprint_version`; `grok_estimated_ceiling` with evidence.
7. **Graph + 99-slot audit** (M4), provisional until refs exist (rule 2).
8. **Candidates** (M5), escalation per rule 3.
9. **Two optimizer passes + reconciliation** (M6, rule 7); stress scenarios and red team; certificate → `APPROVAL_READY` or `REVIEW_REQUIRED`.
10. **Cory's decision** (M7) → `APPROVED`, then optionally `CANONICAL_LOCKED` (separate record).
11. **Birthday export** (M8) from registry states.

## The GPT repository's role

`corymstover/grixis-commander-encyclopediaGPT` (archived byte-identical in `grixis/source-archive/`, commit `1836b97`) **remains the provenance root and the origin of every canonical list**. Its approvals are kept as evidence, not as companion approvals. It is **not demoted** until all 62 decks are `APPROVED` or `CANONICAL_LOCKED` under this model (M9); only then do the docs name the companion as first authority and the GPT repository as the historical record. Its known defects (prose-only records, boilerplate whole-list reasons, the logical/raw hash mix, standing auto-approval in `DECK_QUALITY_GATES_V3.md`, an unqualified Forge harness) are recorded in the [gap analysis](Grixis%20Authority%20Gap%20Analysis.md) and are not ported.

## Milestone acceptance criteria

Status is in `data/grixis/registry.json → program.milestones`. Only Cory sets `accepted`. Cycle estimates in the gap analysis are estimates (rule 5).

### M0
**Authority foundation (Bot cycle 47).** Criteria, with the state at the end of cycle 47:
1. ✅ Evidence classes (7) and confidence levels (6) in a schema and a shared module, with the decision rule tested.
2. ✅ JSON Schemas for registry, exceptions, approvals (enforced in `validate_all`), v1 drafts for blueprint, graph, audit, candidate, optimizer pass, swap, test, certificate; all 14 carry `$schema` / `$id`; data files pass both the stdlib validator and `jsonschema`.
3. ✅ Registry with the §19 fields for all 62 decks; logical hash defined and recomputed from the pages; 60 `SOURCE_BASELINE`, 2 `PENDING_RELEASE`; reopen triggers armed; source repo and commit `1836b97`.
4. ✅ No deck in `APPROVAL_READY` / `APPROVED` / `CANONICAL_LOCKED`; approvals.json empty; enforcement tested with positive and negative cases.
5. ✅ Legality separate from authorization in registry, exceptions, front matter and exports; 8-row registry verified (4 corrected); validators accept exceptions but never report them legal (tested).
6. ✅ Bjorna canonical list restored with exceptions; projection labeled, never canonical or approvable (schema + check + tests).
7. ✅ grixis_refine v1 reproducible, v2 exploratory with diagnostics/priors and lift/trend/sample/date; no auto-published final.
8. ✅ Exports labeled per file with state; challengers vs source baseline; v1 "at ceiling" relabeled.
9. ✅ Test suite in `validate_all`; this page, the gap analysis, the index, README, Refinement Cycle notes and Update Log updated.
10. ✅ `validate_all` green.
11. ✅ Cory's acceptance (`program.milestones.M0.accepted_by`): **accepted by corymstover on 2026-10-16 at 10:52 UTC** ("I accept M0", an in-chat approval relayed by MTG Bot; recorded in Bot cycle 50). This accepts the milestone only and approves no decks.

### M1
**Interaction reviews, all 62.** Every deck has a current interaction review whose hash equals the deck's **canonical** list hash (`canonical_project_list.export`), every citation verbatim; Bjorna's review covers Trade Secrets, Yawgmoth's Bargain and the Lutri companion; reviews emit machine-readable edges for M4; the 518 source rulings are folded in or explicitly dispositioned.

### M2
**Commander blueprints v1.** 62 blueprints validate against `blueprint.schema.json`; each names identity core, anti-goals, packages with minimum counts, win conditions, failure modes, tutor targets and construction rules; each has a `grok_estimated_ceiling` with evidence and a `disagreement` flag where it differs from the source; Cory has reviewed the sample he chooses and marked them reviewed.

*Status (Bot cycles 50–53, in progress):* the schema is v2 (every field is a claim with `evidence_class`, `confidence` and resolvable evidence refs); tooling `scripts/grixis_blueprints.py` (`--scaffold`, `--check` = `validate_all` step `blueprints`, `--render`, `--m2-status`); **46/62 blueprints** (batch 1, cycle 50: Abaddon … Dr. Eggman; batch 2, cycle 52: Edea … Lord Xander; batch 3, cycle 53: Lynde … Parnesse) in `data/grixis/blueprints/`, rendered in [blueprints/](blueprints/README.md). The registry takes `blueprint_version` and `grok_estimated_ceiling` from the blueprint, computes `disagreement`, and records a source ceiling the original parse missed as `source_ceiling.recovered` (cited `path#Lline`; the parsed claim is never overwritten). Criteria, live: `python3 scripts/grixis_blueprints.py --m2-status`.
1. ⏳ 62 blueprints validate — 46/62.
2. ⏳ Every required section present (identity core ≥3, anti-goals, required packages with min counts, win conditions, failure modes ≥2, tutor targets, construction rules) — 46/46 written ones complete.
3. ⏳ GrokBot ceiling estimate with evidence and a disagreement flag — 46/62 (0 disagreements so far; 6 written decks have no source ceiling to compare).
4. ⏳ Cory's review of a sample he chooses (`status: cory_reviewed`, `provenance.reviewed_by`).
5. ⏳ Cory's acceptance (`program.milestones.M2`).

### M3
**Evidence layer and simulator.** Evidence vectors per candidate (lift, sample size, retrieval date, trend, Oracle hooks, graph facts) with classes and confidence; deterministic paired-seed goldfish simulator with a hypergeometric layer, London mulligan, mana/colors, commander turn and package assembly, unit-tested against exact math; stress scenarios scripted (below); every test record carries pre-registered metrics, CIs and limitations; snapshot-keyed caching.

### M4
**Dependency graph and 99-slot audit.** A graph per deck (Spellbook, interaction edges, hooks, roles, blueprint packages) with structural necessity, breaks-if-removed and redundancy; an audit per deck where every slot is `complete` with blueprint, graph and alternative refs or explicitly `provisional`; no duplicated boilerplate reason beyond a lint threshold; baseline simulator metrics per deck.

### M5
**Candidate deep dive.** Per deck a recorded candidate universe (definition, sources, size, snapshot), triage with the default 15–40 full reviews and escalations with reasons; tournament evidence only for decks whose estimated ceiling is cEDH, with sample size and date.

### M6
**Refinement cycle 1** (starts only after M2 and M4 are accepted). Per deck: independent commander-first and performance passes with different objective functions (rule 7), a reconciliation with a deep-review queue, paired tests of each material swap, stress scenarios and a red-team record, and a schema-valid certificate leading to `APPROVAL_READY` or `REVIEW_REQUIRED`.

### M7
**Cory review and refinement cycle 2.** Every packet has Cory's recorded decision; approved hashes match the registry; cycle 2 re-closes changed decks; reopen triggers processed (including the 2026-11-13 release).

### M8
**Birthday export.** A generated folder ("Birthday" is a folder name, not a date) with the newest list per deck, `index.json` with state, certificate link, hash and exception labels; `CANONICAL_LOCKED` only where Cory locked the exact hash; Bjorna's canonical list and projection both present and labeled; checked by `validate_all`.

## Testing doctrine: stress scenarios and red team

- **Exact math first:** hypergeometric probabilities where a question has a closed form.
- **Paired goldfish Monte Carlo:** the same seed gives both lists the same shuffle permutation; results are differences with confidence intervals against pre-registered thresholds; differences inside the noise are reported as "no detectable difference".
- **Scripted stress scenarios** (deterministic perturbations in the same engine): commander removed at turn T (once, twice); graveyard exiled; artifacts wiped; board wipe at T; first key spell countered; mana screw / color screw; key engine piece exiled. Each reports recovery turn and assembly-probability deltas.
- **Red-team analysis:** a structured written attack on each challenger and baseline (stax, fast combo, graveyard hate, aggro pressure, politics), with evidence classes and confidence.
- **Not done:** multiplayer win-rate simulation. Opponent-dependent claims never become simulated win rates.

## Why this is stricter than both earlier systems

| Concern | Old GrokBot (cycles 39–46) | GPT process | Now (M0) and the bar for later milestones |
|---|---|---|---|
| Who approves | Bot-written "manual review" promoted lists to "final" exports | 62/62 APPROVED/LOCKED; standing auto-approval clause | Only Cory, per exact hash, in a validated record; three top states distinct; tests enforce it |
| Heuristic vs decision | Gates decided; "at ceiling" when nothing passed | Prose verdicts, boilerplate reasons | Gates are diagnostics; decisions need fact / test / judgment / approval evidence |
| Legality vs authorization | Exceptions silently replaced at import | Exceptions accepted, one approval record claimed a not-yet-legal card PASS | Separate fields everywhere; exceptions verified and never called legal; projection derived and non-canonical |
| List identity | No list hash in the refinement engine | Raw and logical digests mixed | Logical `lh1` authoritative, raw recorded, recomputed by tests |
| Machine checks | `validate_all` without unit tests or schemas | 19 pytest files, prose records | Schemas + unit tests + registry freshness in `validate_all` |
| Two passes | Engine + hand review, not independent | Separate gates, one author | Independent objective functions, schema- and test-enforced, reconciled |
