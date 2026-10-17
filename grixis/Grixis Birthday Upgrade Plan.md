---
title: "Grixis Birthday Upgrade Plan"
category: meta
tags: [grixis, authority, plan]
issues: []
generated_by: hand-written
sources: [grixis-repo]
related: ["Front-Matter Schema.md", "grixis/Grixis Authority Model.md"]
schema: 2
---

# Grixis Birthday Upgrade Plan

> **Status:** plan approved by Cory (chat **t54u**, 2026-10-16) on the basis of the Bot cycle 64 gap audit. Recorded in Bot cycle 64.1. **This document accepts no milestone.** M2/M4 acceptance proceeds independently (PR #141); M5 stays **unaccepted** until saturation and layers A–F regenerate it. Only Cory accepts milestones, approves decks or locks hashes ([Authority Model](Grixis%20Authority%20Model.md#authority-hierarchy)).
>
> Machine-readable twin: [`data/grixis/upgrade_plan.json`](../data/grixis/upgrade_plan.json). Step G0 artifacts: [`data/grixis/benchmark/`](../data/grixis/benchmark/README.md).

## Contents
- [Cory's decisions (t54u)](#corys-decisions-t54u)
- [Ordered steps](#ordered-steps)
- [Acceptance standard for every step](#acceptance-standard-for-every-step)
- [Freeze rules](#freeze-rules)

## Cory's decisions (t54u)

Recorded as given (relayed by MTG Bot, 2026-10-16). Nothing here is paraphrased into a weaker form.

1. **Candidate saturation:** adaptive saturation with tiered testing, not exhaustive paired testing. No fixed numeric discovery cap. Cheap screening may prioritize workload but must never be an absolute exclusion gate; candidates may escalate through dependency evidence, unusual Oracle interaction, new-card status, package gaps, human evidence, anomaly detection, or other justified signals.
2. **Benchmark blinding:** frozen retrospective corpus with contamination flags plus a genuinely prospective holdout for future cards, corrections and human decisions. Never claim the historical corpus is perfectly blind where prior ingestion makes that impossible.
3. **Pass A/B:** shared factual inputs, commit-then-reveal output blinding; neither sees the other's conclusions before both outputs are committed and hashed. Pass C (incumbent-defense critic) may see both. Reconciliation only afterward.
4. **Opponent-facing mechanics:** bounded scripted proxies and deterministic perturbations approved, with explicit assumptions, sensitivity where appropriate, documented limitations. No unsupported multiplayer win-rate simulation.
5. **power_core backfill:** versioned post-M2 correction overlay plus a materiality gate. If a change does not alter commander role, dependency, ceiling, anti-goals, required packages or another material Blueprint conclusion, M2 is not reopened; if it does, targeted review/reopen for that deck. Regenerate downstream artifacts either way.
6. **Two-snapshot model:** snap-20261016 frozen as the development snapshot during A–F. Immediately before final M5 acceptance and the Birthday baseline freeze, create a fresh Birthday authority snapshot (current Oracle/Scryfall, rules, legality, EDHREC, Spellbook, tournament evidence, new cards), delta refresh, regenerate every affected artifact. The Birthday snapshot is M6's authoritative start.
7. **Human sampling:** build and freeze the H sampler/schema before M6 outputs exist. Strata: random, anomaly, exception, pending release, cEDH, low commander dependence, high optimizer disagreement, rules-sensitive, major-change.

**Order (Cory):** G0 benchmark freeze → A saturation → E mechanic modules → B combo quality + C mana base → D commander marginal value → F bracket stress suites → H sampling infra → regenerate M5 → fresh Birthday snapshot + full rebuild/validation → Cory's M5 review/acceptance → I/J certificate + reproducibility schemas → K three-sided M6 → M6 with H sampling → benchmark evaluation → M7/M8. M2/M4 acceptance proceeds independently. M5 stays unaccepted until saturation and A–F layers regenerate it.

## Ordered steps

Batch = one 20–35 minute bot batch. Estimates are estimates (standing rule 5), not commitments.

| # | Step | Batches | Depends on | Snapshot | Notes |
|---|---|---|---|---|---|
| 1 | **G0** benchmark corpus freeze | 3–4 (took 4: 64.1–64.4) | — | snap-20261016 | **Complete pending merge of PR #142.** 612 items, frozen in Bot cycle 64.4. Only the prospective holdout grows. |
| 2 | **A** adaptive candidate saturation (**next**) | 6–8 | G0 frozen | snap-20261016 (dev) | Removes `UNIVERSE_MAX = 500` (61/62 decks hit it). Multi-pass discovery, yield-based stop rule, per-deck saturation certificate, tiered testing (decision 1). |
| 3 | **E** mechanic test modules (sim v1.2) | 10–14 est. (15 engineering batches/sub-batches so far) | A | dev | **Code-complete through 66.13; local frozen-cache validation still required.** 21 bounded modules; residual death/sacrifice/token wording and commander-specific hooks remain explicit judgment/not-modelable rather than fake generic simulation. v1.0/v1.1 stay runnable. |
| 4 | **B** combo quality model + `power_core` backfill overlay | 4–6 (took 5: 67.1–67.5) | E | dev | **Complete as evidence infrastructure.** Quality vectors, D5 overlay, cached line semantics and near-variant family networks are integrated; all strategic priority remains unresolved for judgment. |
| 4 | **C** mana-base optimizer | 5–7 | E (parallel with B) | dev | Lands evaluated like spells; MDFC back faces. |
| 5 | **D** commander marginal value | 3–4 | E | dev | Adds a commander-unavailable simulator mode. |
| 6 | **F** bracket stress suites | 4–5 | E | dev | B5/B4 suites, weights pre-registered before any run. |
| 7 | **H** human-sampling infra | 2–3 | — (must precede M6 outputs) | dev | Sampler + schema frozen before M6 (decision 7). |
| 8 | Regenerate M5 on A–F | 2–3 | A–F | dev | — |
| 9 | Fresh **Birthday authority snapshot** + delta refresh + full rebuild / validate_all | 2–3 | 8 | Birthday | Decision 6. M6 starts from this snapshot. |
| 10 | Cory's **M5 review / acceptance** | — | 9 | Birthday | Cory only. |
| 11 | **I/J** Zero-Improvement Certificate + reproducibility bundle schemas | 4–5 | 10 | Birthday | — |
| 12 | **K** three-sided M6 (Pass A, Pass B, commit-then-reveal, Pass C critic, reconciliation) | 6–9 (infra) | 11 | Birthday | Decision 3. |
| 13 | **M6** with H sampling | per-deck cycles | 12, 7 | Birthday | — |
| 14 | **G** benchmark evaluation | 3–4 | 13 | Birthday | Retrospective corpus + prospective holdout scored separately. |
| 15 | M7 / M8 | — | 14 | — | — |

## Acceptance standard for every step

A step is done only when **all** of these hold. Cory still decides whether a milestone is accepted; a step being done accepts nothing.

1. **Schema:** every new record type has a JSON Schema in `data/grixis/schemas/` and every record validates.
2. **Determinism:** same inputs + seed give byte-identical outputs; a checker re-runs a sample.
3. **Tests:** unit tests in `tests/` cover the rules and at least one negative case per rule.
4. **validate_all integration:** a `--check` step is registered (or the reason it is deferred is recorded).
5. **Provenance:** every record cites its inputs (file + commit, snapshot ids, chat refs).
6. **Limitations:** every model output states what it cannot see.
7. **Evidence classes:** every claim carries `evidence_class` and confidence; test results never decide alone.
8. **Real-deck examples:** at least one worked example on a real Grixis deck in the docs.
9. **Demonstrated decision-quality gain:** measured against the frozen G0 corpus or a stated before/after on real decks. A step that only adds volume does not pass.

## Freeze rules

- **G0 corpus:** may grow in later G0 batches. It becomes **immutable once step A begins** (first A commit). After that only the prospective holdout grows; retrospective items are never edited, and a wrong item is retracted by a new record, not rewritten.
- **Development snapshot:** snap-20261016 stays frozen during A–F; newer cards and rule changes are logged as reopen triggers, not ingested.
- **Birthday snapshot:** created immediately before M5 acceptance; it is M6's authoritative start.

## G0 benchmark scoring rule (Bot cycle 64.3)

Most retrospective items cannot measure detection honestly. The source's approved changes are already in the canonical baselines the new system starts from, so the system "starts with the answer". Every G0 item therefore carries an `evaluation_role`:
- **`detection`:** the system must find or flag the item.
- **`regression_guard`:** the baseline already contains the outcome. The system passes if it does not propose reverting it without new evidence.
- **`judgment_calibration`:** v1 or other unvalidated labels. Scored as agreement, never as accuracy.

Any benchmark report (step 14) must stratify results by evaluation_role × origin × contamination level and must never give one pooled score (`data/grixis/benchmark/manifest.json` `reporting_rule`, checked by `scripts/grixis_benchmark.py --check`). Only the prospective holdout can measure uncontaminated detection.

## Development-snapshot policy (Cory D6, recorded in Bot cycle 65.1)

- **snap-20261016** stays the frozen development snapshot during A–F.
- **Deferred staleness, to be cleared at the Birthday snapshot refresh (not now):**
  - `Grixis Evaluation.md` is built from the 2026-10-15 bulk. Regenerating it rewrites deck pages and cascades.
  - A 2026-10-16 rulings bulk exists in `/tmp/c64-cache-partial-backup`, while validation uses the 2026-10-15 rulings.
- **Benchmark corpus:** immutable from this first step-A commit (Bot cycle 65.1). Only `prospective_holdout.json` may grow.

## Step A: adaptive candidate saturation (design, Bot cycle 65.1)

Implements decision D1. Code: `scripts/grixis_saturation.py`. Certificates: `data/grixis/saturation/<slug>.json`, with the full universe in `<slug>.universe.json.gz`. Schema: `data/grixis/schemas/saturation_certificate.schema.json`.

- **No fixed numeric cap.** The M5 bound `UNIVERSE_MIN, UNIVERSE_MAX = 200, 500` is not used. 61 of 62 decks sat exactly at 500. A unit test fails if a universe bound reappears in the saturation code.
- **Source passes, in fixed order:**
  1. EDHREC
  2. Commander Spellbook near-misses
  3. blueprint package candidates
  4. Oracle-text hooks
  5. package creature-type search
  6. rules interactions (cards and keywords named in the M1 interaction reviews)
  7. new cards (earliest printing on or after 2026-04-16)
  8. role gaps (the three thinnest key roles in the 99-slot audit)
  9. graph alternatives (audit alternative refs, plus same role-and-type signatures as weak incumbents at the same or lower MV)
  10. tutor targets (blueprint targets and their signatures)
  11. mana base (lands producing the deck's colours, mana rocks)
  12. archetype technology (in at least 3 other Grixis canonical lists and sharing the deck's hook or package type)
  13. tournament (EDHTop16 cards with entries, cEDH decks only)
- **Expansion rounds:** after the source passes, rounds seeded by the tier-A candidates found so far nominate Oracle-keyword and creature-type neighbours. They repeat until the stopping rule is met.
- **Materially new:** a pass is material if it adds at least **k = 3** new candidates with screening score **≥ X = 25.0** (tier B), or any new escalated candidate.
- **Stopping rule:** stop after **N = 2** consecutive non-material expansion rounds. k, X and N are recorded in every certificate.
- **Hard exclusions only:** not Commander-legal (project exceptions handled as in M5), outside the colour identity, already in the list, basic land, unresolved name.
- **Screening never excludes.** Every discovered card stays in the universe with a score and tier. Broad passes nominate by a recorded relevance predicate: EDHREC rank ≤ 8000, an Oracle hook, or a package type. A card no pass nominates is undiscovered, not excluded, and certificates list this as a blind spot.
- **Escalation signals:** dependency evidence (completes an infinite Spellbook variant), package gap (blueprint candidate), new card with a hook or package fit, unusual Oracle interaction (a hook outside EDHREC that also meets a package fit and a role, blueprint or combo need), tournament evidence. Human evidence and anomaly signals are open hooks for later batches.
- **Tiered testing:** `test_tier = paired_test` if tier A or escalated, otherwise `screen_only`. This orders work only.
- **Determinism:** fixed pass order and sorted inputs; the universe is gzipped with mtime 0. `--check` validates the schema and re-runs one deck byte-identically (validate_all step `saturation`).

**First measurements** (cycle 65.1, three decks, about 1–2 s per deck after a one-off pool load of about 5 s):

| Deck | Universe (old: 500) | paired_test / screen_only | Last material pass |
|---|---|---|---|
| wick-the-whorled-mind | 7,867 | 519 / 7,348 | 4 (oracle_text) |
| the-valeyard | 3,313 | 52 / 3,261 | 2 (spellbook near-miss) |
| kess-dissident-mage (B5) | 9,265 | 575 / 8,690 | 7 (new_card) |

**Open questions for later A batches:**
- The Oracle-hook pass is very broad (about 5–7k hits on hook-rich decks).
- Archetype-tech and type-search passes found nothing new on these decks; the list parsing and package types need checking.
- The paired-test budget at full scale is roughly 50–600 per deck.
- Human-evidence and anomaly escalation are not wired in yet.
- Integration into `grixis_candidates.py` (regenerating M5) is a later A batch.

### Step A revision (Bot cycle 65.2, rulings on 65.1 open questions)

- **No hidden discovery gate:**
  - The 65.1 relevance filter (EDHREC rank ≤ 8000, hook or package type) is removed as a gate.
  - A mandatory final **full-pool sweep** screens every eligible card and admits it to the universe. Eligible means Commander-legal or an authorized project exception, in colour identity, not in the list, and not a basic land.
  - Earlier passes are **signal sources**: they attach provenance signals and escalation.
  - Certificates record the pool size, sweep coverage (1.0) and per-signal counts.
  - A signal pass is material if it gives a *first* signal to ≥ 3 cards scoring ≥ 25.0, or newly escalates a card. Stop after 2 non-material expansion rounds.
- **Oracle hook specificity:**
  - `commander_specific`: the hook label matches ≤ 2% of the eligible pool.
  - `blueprint_package`: the card also fits a package.
  - `generic`: everything else.
  - Only the first two produce the oracle_text signal and the unusual-interaction escalation. Generic hooks still score.
- **Passes fixed:**
  - blueprint_package now uses package members not in the list, candidates and package-type matches.
  - archetype_tech no longer requires a hook (≥ 3 other canonical lists).
  - type_search is genuinely empty for 40 decks: package creature types are derived from members (≥ 40% sharing a subtype), and non-tribal packages have none.
  - Tournament is empty for 51 decks, which is genuine; it is recorded in the pass inputs.
- **Escalation reasons:**
  - tier-A score
  - dependency-graph alternative (audit alternative refs)
  - Spellbook near-miss completion (infinite)
  - package gap
  - new card (hook and score ≥ 25)
  - unusual Oracle interaction (commander-specific hook, no EDHREC row, package fit)
  - anomaly (EDHREC part vs structural part disagree by ≥ 30)
  - human evidence (card named in `blueprint_reviews.json`, `m1_corrections.json`, or the audit lint/M1 flags for the deck)
  - tournament evidence
- **Test tiers:** escalated cards are ranked by score + 5 × reasons. The first 250 (target, not cap) are `paired_test`; the overflow is `escalated_queued` and listed in `escalated_untested_queue` for later batches, never dropped.
- **Unreleased cards** (first printing after 2026-10-16, not yet legal) stay excluded but are listed per deck as a blind spot with `legal_from` (93–95 per deck).

**All 62 decks (65.2):**
- Universe 18,453–18,469 eligible per deck (old bound: 500); 5,449–14,597 of those enter only through the sweep.
- Tier A 11–97 (median 45); tier B 36–456 (median 112.5).
- Escalated 42–492 (median 135.5). paired_test 42–250 (median 135.5; 34 decks below 150). 1,248 queued across 16 decks.
- Every deck saturated, sweep coverage 1.0.
- Runtime about 0.7–8 s per deck; 33 s wall with 6 workers.

### Step A wiring (Bot cycle 65.3)

- **Escalation:** one justified signal added, `multi_source_corroboration`: a tier-B card signalled by at least 2 independent signal families. Passes that read the same source count once: blueprint_package + tutor_target; oracle_text + type_search; role_gap + graph_alternative(_ref). Low counts are not padded.
  - All 62 decks: escalated 60–569 (median 186). paired_test 60–250 (median 186; 20 decks below 150, 21 at the 250 target). 2,002 queued across 21 decks.
- **Compact storage:** universe files keep full rows for signalled or escalated cards; sweep-only cards are stored as `[card, score, tier]`.
- **`scripts/grixis_candidates.py` consumes the saturated universe:**
  - `build_universe` reads the certificate and universe, and refuses a certificate built for another list hash.
  - Full screening reviews are the certificate's `paired_test` cards; `escalated_queued` cards are listed in `triage.escalated_queued`.
  - `--build` requires `--out DIR` until M5 regeneration, so the stored files are never overwritten.
- **Caps removed:** `UNIVERSE_MIN/MAX` (200/500), `NICHE_RESERVE` (60), `DEFAULT_RANGE` [15, 40] (clamp of default full reviews), and the `rank_fill` top-up.
- **Truncations kept, each justified:** all are display or evidence-reference truncations that never change membership, score, tier or escalation:
  - `facts.spellbook[:8]` (the score uses all variants);
  - `esc_refs` / `evidence` `[:3]` and `[:4]` (cited refs);
  - `mates[:3]`, `breaks[:4]` and `reason[:160]` in swap text;
  - check output `p[:30]`.
  - The saturation `PAIRED_TARGET` (250) is a per-batch ordering target with an overflow queue, not a cap.
- **Stored M5 files:** `data/grixis/candidates/*.json.gz` are kept as-is and marked **capped legacy, superseded at M5 regeneration**. `--check` validates them against the bounds each file recorded. The byte-identical rebuild check is retired for legacy files, since the builder no longer produces capped universes.

## Step E: targeted mechanic modules (simulator v1.2 framework), batch 66.1

This step implements Cory directive item 3 and decision D4. It is **not** a multiplayer simulator: it adds declared, deterministic mechanic components on top of the paired v1.1 goldfish games.

- **Framework** (`scripts/grixis_mech/`): each module declares what it models and does not model, its assumptions, parameters, confidence, limitations, metrics, determinism and test file. Declarations are validated against `data/grixis/schemas/mechanic_module.schema.json`. Evidence class is `test_result`; win-rate metrics are forbidden by the schema and the check.
- **v1.1 stays byte-identical:**
  - `observe.py` runs the unchanged `grixis_sim.play_game` under a read-only line observer that snapshots battlefield, graveyard and hand at each end of turn. It uses no rng.
  - `grixis_sim.py` is not edited, so the model sha, stored tests, audits and M5 files are not invalidated.
  - `tests/test_mech.py` checks seeded v1.0/v1.1 outputs against golden hashes generated from main (996350d). The native hook and the v1.2 model bump come at M5 regeneration.
- **Opponents:** they appear only as bounded, deterministic perturbation grids (closed-form expectations) reported as a sensitivity range, never as win rates.
- **Router** (`router.py`): it maps the cut and add cards' Oracle features to step-E module families. A swap invokes only the modules it routes to; an unrouted swap stays `not_modelable` with a reason.
- **Module families:** graveyard recursion\*, graveyard tutoring, sacrifice costs, death triggers, attack/combat triggers\*, cast triggers, activated engines, repeatable draw, repeatable tutors, stax/tax, stack protection, counterspell density, opponent-dependent draw (bounded proxy), LED/Breach sequences, X spells, alternate costs, commander-specific engines, plus tokens, life loss and discard. \* = implemented in 66.1.
- **Modules in 66.1:**
  - `attack_trigger_proxy`: a creature with an attack trigger attacks every turn from the first turn it could (haste-aware). It reports expected trigger counts by turns 6/8/10 under block ∈ {0, .25, .5} × survive ∈ {1, .85, .7}.
  - `graveyard_recursion`: zone tracking. It reports P(a recursion card is available while the graveyard holds a legal target) by turns 4/6/8. This is a lower bound: v1.1 has no creature deaths.
- **Coverage over legacy M5 `not_modelable` swaps:** 9,040 swaps.
  - 2,158 (23.9%) now route to an implemented module.
  - 6,300 route only to planned modules.
  - 582 match no family (in total, 93.6% route to some family).
  - Per-family counts are in `data/grixis/mechanics/coverage_legacy_m5.json`; real-deck examples are in `examples.json`.
- **Known gap:** the recursion matcher counts self-recursion (e.g. Poxwalkers) as recursing other cards. It is to be split in 66.2.

### Step E batch 66.2: shared death layer, death triggers, sacrifice, self-recursion split

- **Shared death layer** (`scripts/grixis_mech/deaths.py`): v1.1 never kills a creature, so death and sacrifice need a removal model. The layer is a scripted, deterministic proxy (D4).
  - Opponent removal per turn cycle: each creature dies with probability `removal` ∈ {0, 0.1, 0.25}.
  - An opponent wipe at the end of turn `wipe` ∈ {none, 6, 8}.
  - Own sacrifice outlets actually used (`sac` on/off): one creature per turn while the outlet has fodder; never the outlet itself or the commander; tracked cards are sacrificed last.
  - Dead non-commander creatures go to the graveyard. Results are closed-form expectations (no rng).
  - The point (0, none, off) is v1.1's no-death lower bound and is always reported separately from the grid range. All assumptions are listed in each module's declaration.
- **New modules:**
  - `death_triggers`: self "when ~ dies" gives P(died by T); a watcher ("whenever a/another creature dies") gives expected deaths while it is on the battlefield.
  - `sacrifice_costs`: expected outlet uses with live fodder.
  - `self_recursion`: P(the card is in the graveyard by T).
- **Recursion split:** `graveyard_recursion` now excludes self-recursion (66.1 counted Poxwalkers as returning other cards) and gains `evaluate_grid` under the death layer.
- **Re-run recursion examples (by turn 8):**
  - Edward Kenway → Back in Town (`graveyard_recursion`): live 0.33% at the no-death lower bound; grid 0.33–4.9% (mid point 2.8%).
  - Birgi → Poxwalkers, now `self_recursion`: 0.67% lower bound; grid 0.67–11.3%. 66.1's 11.3% was a misroute.
- **Other examples (by turn 8):**
  - Syr Konrad (`death_triggers`, watcher): 0 at the lower bound, grid 0–0.45 triggers.
  - Gollum the Abandoned (`sacrifice_costs`): 0.06–0.30 uses.
- **Coverage over the 9,040 legacy not_modelable swaps:**
  - 2,412 (26.7%) route to an implemented module (66.1: 2,158 / 23.9%).
  - 6,048 route only to planned families; 580 match none.
  - Per family: attack 1,619; graveyard recursion 492; sacrifice outlets 236; death triggers 171; self-recursion 163.
  - Death/sacrifice text the new modules do not claim (`death_other` 649, `sacrifice_other` 1,228, e.g. sacrifice as a spell cost or "dies" in non-trigger text) stays planned.
- **Reconciliation of 9,044 vs 9,040:** 9,044 = 25,933 − 16,889 at cycle 61, and still 9,044 at 62.3. The cycle 63.2 regeneration (42157ff) moved 11 swaps out of the not_modelable set and 7 in (net −4) across 12 decks. The ids are listed in `not_modelable_reconciliation.json`.

### Step E batch 66.2a: death-trigger semantics correction (Cory t56u)

Cory caught an architecture error in the 66.2 `death_triggers` module (v1). v1 treated every watcher as "count every creature death while the watcher is listed in the trace":
- it counted the watcher's own death for "another creature";
- it counted creatures, not events, for "one or more creatures die";
- it gave full triggers on later turns because the unperturbed v1.1 trace still listed a watcher the death layer had killed.

**v2 (`death_triggers` version 2):**
- **Semantics are parsed from Oracle text:**
  - `self` ("when ~ dies");
  - `a` ("a creature dies", "~ or another creature dies"; includes its own death via CR 603.10a look-back);
  - `another` (excludes its own death);
  - `one_or_more` / `one_or_more_other` (one trigger per qualifying death **event**);
  - filters "you control" / any, and "nontoken".
- **Unknown wording is `not_modelable` with a reason, never a generic fallback:** "an opponent controls" / "your opponents control" / "you don't control" (the death layer has no opponent creatures), and creature-type filters such as "a Rat you control dies".
- **The death layer emits death events:** one per removed creature, one simultaneous event per wipe, one per sacrifice.
- **Survival weighting:** watcher expectations are weighted by the watcher's own survival probability before each event.
- **Look-back:** a watcher dying in the same wipe or sacrifice still sees the others die; its own death counts only where the wording includes it.
- **Tests:** edge cases cover the "another" self-exclusion, a multi-creature wipe as one "one or more" trigger, simultaneous watcher + other death, survival weighting (no triggers after the watcher died), nontoken, and the not_modelable wordings.
- **Old vs new, Syr Konrad, the Grim** (Abaddon; "another"; lower bound 0 in both):

  | Version | T6 grid range (mid) | T8 grid range (mid) | T10 grid range (mid) |
  |---|---|---|---|
  | v1 | 0–0.167 (0.026) | 0–0.45 (0.082) | 0–0.45 (0.166) |
  | v2 | 0–0.11 (0.013) | 0–0.337 (0.045) | 0–0.337 (0.091) |

- **Coverage (9,040 legacy not_modelable swaps):**
  - `death_triggers` routes 129 swaps (v1: 171).
  - Routed to an implemented module: 2,374 / 26.3% (66.2: 2,412 / 26.7%). Planned only: 6,086 (was 6,048). Matching none: 580 (unchanged).
  - not_modelable card occurrences with reasons: unrecognised wording 275, opponents' creatures 51.
- **Prospective holdout:** not added. Holdout rules require sealing before the evaluated system has seen the correction. The correction was received and implemented in this same batch, so a sealed item could not be uncontaminated (`contamination.level` must be "no"). The frozen corpus is untouched.
- **Shared cache:** the frozen dev-snapshot Oracle bulk was replaced in `.cache` by a newer Scryfall bulk twice this session (online `load_deck` runs). Both times it was restored from `/tmp/c64-cache-partial-backup`; the newer file is in `/tmp/c66-cache-refresh-backup/`. `grixis_mechanics.py` now forces `SCRYFALL_OFFLINE=1`.
### Step E batch 66.3: cast triggers, repeatable draw, activated engines, tokens, sacrifice as an additional cost

- **Derived events** (`scripts/grixis_mech/events.py`), deterministic:
  - Casts are inferred from the trace: a non-land card that newly reaches the battlefield or graveyard that turn.
  - Synthetic creature tokens come from recognised token makers (on arrival, per later turn, or per matching cast).
  - Tokens are death-layer fodder; they die like creatures but never reach the graveyard. The sacrifice outlet sacrifices tokens first.
- **Observer:** the snapshot now also records mana spent. It is still read-only, and v1.1 stays byte-identical (golden test).
- **New modules:**
  - `cast_triggers`: matching casts after arrival.
  - `repeatable_draw`: beginning-of-phase, cast, attack and death-triggered draws; death-triggered draws use the grid.
  - `activated_engines`: non-mana abilities, one per turn when the mana v1.1 left unspent covers the cost.
  - `token_makers`: creature tokens created.
  - `sacrifice_additional_cost`: P(the spell or ability cost is payable with live creature/token fodder), over the grid.
- **Coverage over the 9,040 legacy not_modelable swaps** (after merging the 66.2a correction):
  - 6,775 (74.9%) route to an implemented module (66.2a: 2,374 / 26.3%).
  - 1,732 route only to planned families; 533 match none.
  - Per family: attack_trigger_proxy 1,619, activated_engines 1,745, cast_triggers 1,270, repeatable_draw 2,825, token_makers 1,964, sacrifice_additional_cost 65, sacrifice_costs 236, death_triggers 171, graveyard_recursion 492, self_recursion 163, sacrifice_other 1,228, death_other 649, tokens_other 3,266.
- **Correction:** the 66.2 `sacrifice_other` figure (1,228) came from a broad planned regex (any ", sacrifice " text). Of those, the cards whose text is a creature/artifact/permanent sacrifice cost now route to `sacrifice_additional_cost`; the rest (land, self-sacrifice, opponent-sacrifice text) stay `sacrifice_other`.
- **Tokens in death events (66.3b):** synthetic creature tokens are death-event victims (removal, wipe, sacrifice), so watcher triggers count them unless the wording says nontoken. Tokens never reach the graveyard. Syr Konrad by turn 8 with the deck's token makers: grid 0–0.343, mid 0.046 (66.2a without tokens: 0–0.337, mid 0.045).
- **Cache incident (66.3):** an online `load_deck` replaced the frozen dev-snapshot Oracle bulk in the shared `.cache` (oracle-cards-20261016090200) with a newer Scryfall bulk (20261016210202). It was restored from `/tmp/c64-cache-partial-backup`, and the newer file was moved to `/tmp/c66-cache-refresh-backup/`. `grixis_mechanics.py` now forces `SCRYFALL_OFFLINE=1` (D6). Direct runs of other scripts outside `validate_all` (which is offline by default) can still refresh the cache.

### Dev snapshot lock (Bot cycle 66.3b)

The frozen development snapshot (D6) is now enforced for every script, not by convention.
- **Lock file:** `data/grixis/dev_snapshot_lock.json` names the oracle (20261016090200), rulings (20261015090033) and default-cards (20261015090541) bulk files, with sha256 hashes.
- **No fetches while locked:** `ingest_scryfall.get_bulk` (the only bulk fetcher, used by `evaluate_decklist.Resolver` and therefore by `grixis_sim.load_deck`) never fetches, replaces or adds a bulk while the lock exists. Every read resolves to the locked file, and a missing locked file is an error, never a download.
- **Override:** `SCRYFALL_BIRTHDAY_SNAPSHOT=1` or `ingest_scryfall.py --birthday-snapshot`, reserved for the Birthday snapshot step, which replaces the lock in the same commit.
- **validate_all step `dev-snapshot-lock`:** the newest cached bulk of each locked kind (what every glob-based script picks) must be the locked file with the locked hash.
- **Culprit:** online `load_deck` calls run outside `validate_all` (which is offline by default).
  - First refresh: 21:07 UTC, from the 66.3 `grixis_mechanics.py --build`.
  - Second refresh: 21:17:34 UTC (file mtime), during the 66.2a session. The likely trigger is a direct `pytest tests/test_mech.py` run, whose golden test calls `load_deck` online; pytest captured the "Downloading" message.
  - No cron jobs or background processes were found.

### Step E batch 66.4: semantic self-audit of the 66.3 modules (lesson: routing coverage is not correctness)

The audit followed the method of Cory's 66.2 death-trigger review. It used a seeded (664) sample of 12 UBR-identity cards per module, drawn from the match sets (cast 741, draw 530, activated 3,748, tokens 1,123, sacrifice cost 91), plus 42 probe cards. The probe cards were Rhystic Study, Mystic Remora, Howling Mine, Phyrexian Arena, Coveted Jewel, Psychosis Crawler, Plasma Jockey, Skeleton Key, Slith Strider, Lyra, Storm of Saruman, Devoted Duelist, Mysidian Elder, Quicksilver Servitor, Nightmare Sower, Coralhelm Chronicler, Battlefield Thaumaturge, Indris, Kaito Shizuki, Brood Keeper, Rooftop Bypass, Syphon Flesh, Firebender Ascension, Krenko, Bitterblossom, Encroaching Wastes, Deadly Dispute, Demand Answers, Trash for Treasure, Village Rites, and others.

Defects found, each now fixed:

- **Cast triggers:**
  - Unknown qualifiers mapped to "any". These were kicked, "from among cards put into your hand", "during an opponent's turn" and "that targets ~".
  - "Second spell each turn" was counted on every spell.
  - Quoted abilities granted to other objects (Mysidian Elder) and reminder text (prowess) were read as the card's own.
  - Opponent and any-player cast triggers had no not_modelable reason.
  - "Whenever you cast your commander" was unhandled.
  - "An instant or sorcery spell" was mis-parsed.
  - Copies are not casts.
- **Repeatable draw:**
  - The "other" rule matched but counted 0.
  - Blitz reminder text was counted as a death draw.
  - The subject was not checked: "that player/target player draws" was counted as yours.
  - Rhystic-style "unless ... pays" was counted as full draw. It is now not_modelable and left to the planned bounded D4 proxy.
  - "Whenever you draw" / "would draw" was counted as a draw.
  - Loots were counted as +1. They now count 0 net.
  - Intervening-if conditions were ignored.
  - "Each upkeep/end step" now counts x4.
  - Howling Mine-style "each player's ... that player draws" now counts only your own draw and is flagged symmetric. Its untapped condition is assumed true.
- **Activated engines:**
  - "Sacrifice this artifact/land" one-shots, hand costs (discard ~, channel) and loyalty abilities were counted.
  - A {T} cost on a mana source did not give up that source's mana. It now needs unspent mana of cost + 1.
  - Repeatable non-{T} abilities are still counted once per turn. This is a lower bound and is declared as a limitation.
- **Token makers:**
  - type_line was not used, so planeswalker loyalty abilities were counted.
  - Variable counts (for each / X) were counted as 1.
  - Intervening-if triggers and unmodelled trigger conditions (Brood Keeper, Rooftop Bypass) were classified as "spell".
  - Attack makers are now applied once per later turn.
- **Sacrifice as an additional cost:** artifact, artifact-or-creature and land fodder, and "or discard a card" alternatives, were all treated as creature fodder.

Fixes:

- `grixis_mech/semantics.py`: `clean` (name to ~; quoted granted abilities and reminder text removed), sentence split, and intervening-if detection.
- `engines.cast_parse`, `draw_parse`, `act_cost` and `sac_parse`.
- `events.token_parse` with type_line.
- Each module has a `why_not`, so wording that looks like the mechanic but is not recognised gets a not_modelable reason.
- Module versions are bumped to 2.
- Four negative/edge-case tests were added (`test_664_*`).

Old vs new figures, legacy M5 not_modelable swaps (9,040):

| | 66.3 | 66.4 |
|---|---|---|
| routed to an implemented module | 6,775 (74.9%) | 4,353 (48.2%) |
| planned module | 1,732 | 4,048 |
| none | 533 | 639 |
| cast_triggers | 1,270 | 792 |
| repeatable_draw | 2,825 | 283 |
| activated_engines | 1,745 | 1,483 |
| token_makers | 1,964 | 535 |
| sacrifice_additional_cost | 65 | 109 |

The 66.3 routed share overstated correctness. The draw drop is wording that matched before but was not modelled correctly. Across the UBR pool, most of it is combat-damage draw and other unmodelled trigger conditions (about 200 cards), then intervening-if draws, "whenever you draw" and replacement text, another player drawing, and opponent-dependent draw (Rhystic Study, Mystic Remora). Opponent-dependent draw is left to the planned `opponent_dependent_draw` proxy family.

Not yet done, carried to the next batch:

- Bucket classification of the 1,228 broad sacrifice_other matches.
- Per-module not_modelable reason tallies in the coverage file.
- graveyard_tutoring / repeatable_tutors / stack modules.

v1.1 outputs are unchanged (golden test), and the build ran offline under the dev snapshot lock.

## Step B completion — ChatGPT cycles 67.1–67.5

Step B is complete as **evidence infrastructure**, not as a deck decision. It records all frozen Commander Spellbook lines with quality vectors, D5 `power_core` review overlays, cached community line semantics, and deterministic near-variant redundancy networks. Variant families explicitly warn that transitive membership is not strategic equivalence. The D5 overlay changes no accepted M2 Blueprint field and requests no automatic M2 reopen.

The demonstrated-gain record shows materially finer decision resolution than binary combo presence while preserving **zero automatic primary/secondary/backup/incidental/value-loop priority decisions**. Exact/colored mana remains Step C; commander marginal value remains Step D; final priority remains judgment/M6.

Step E is code-closed through 66.13 but still waits on one local frozen-cache rebuild/full-validation gate before it is called fully validated.


### Step C batch 68.5: mana/color-screw and structural source resilience

- `scripts/grixis_mana_resilience.py` consumes the committed 68.1/68.2 mana artifacts only; it does not refresh Scryfall or simulate opponents.
- Records exact no-mulligan complements for land-drop and colored-source presence by turns 2–5. These are access failures, not game-loss or cast probabilities.
- Adds a one-source-unavailable sensitivity probe. The library stays at 99 and one source mask is blanked; absolute and baseline-relative deltas are both retained. Equivalent source masks are collapsed exactly for runtime, not sampled.
- Records fetch-target redundancy and single-color target points, plus demand/source context. No universal mana-quality score or automatic land cut is produced.
- All 62 deck records validate against `mana_resilience.schema.json`; focused regression tests pass. The development snapshot metadata is unchanged.
- 68.3 commander-casting/tax evidence remains code-ready but requires the frozen local Scryfall cache, so it is not counted complete yet.
