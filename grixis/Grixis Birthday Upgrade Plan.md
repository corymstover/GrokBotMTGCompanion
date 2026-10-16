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
| 3 | **E** mechanic test modules (sim v1.2) | 10–14 | A | dev | Priority by `not_modelable` counts (9,044 / 25,940 swaps). Opponent-facing parts as bounded proxies (decision 4). v1.0/v1.1 stay runnable. |
| 4 | **B** combo quality model + `power_core` backfill overlay | 4–6 | E | dev | Backfill follows decision 5 (overlay + materiality gate). |
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
