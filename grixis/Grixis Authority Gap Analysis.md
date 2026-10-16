---
title: "Grixis Authority Gap Analysis"
category: meta
tags: [grixis, authority, governance, plan]
issues: []
generated_by: hand-written
sources: [grixis-repo]
related: ["grixis/Grixis Authority Model.md", "Front-Matter Schema.md", "Update Log.md", "grixis/README.md"]
schema: 2
---

# Grixis Authority Gap Analysis

> **Approved by Cory on 2026-10-16** and committed in Bot cycle 47 as the plan of record for the authority program. It is kept as written (a read-only analysis of `origin/main` @ `bd6f845`). What changed since, decided by Cory or found while implementing M0, is recorded here and in the [Grixis Authority Model](Grixis%20Authority%20Model.md):
> - **Cory's decisions (§2.1):** Bjorna + Cecily keeps ONE canonical project list with Trade Secrets, Yawgmoth's Bargain and Lutri (companion) as labeled project exceptions; the officially legal variant is a *derived compliance projection (not canonical)*, not a second canonical list. All 62 decks start at `SOURCE_BASELINE` (2 at `PENDING_RELEASE`). Target each commander's natural ceiling; record the source claim and an independent estimate, flag disagreement. "Birthday" is a folder name, not a date.
> - **Cory's eight binding constraints** are the [standing rules](Grixis%20Authority%20Model.md#standing-rules-corys-binding-constraints); milestone acceptance criteria replace cycle counts as the measure of progress ([criteria](Grixis%20Authority%20Model.md#milestone-acceptance-criteria)).
> - **Implementation differences:** the registry lives at `data/grixis/registry.json` (not `data/authority/`); the GrokBot challengers are 6 decks (the "7 existing swaps" below count swaps loosely); the exception registry verification corrected 4 of 8 rows (Lutri's companion ban is not a Scryfall legality, the source's approved Bjorna file has no Lutri line, the two Nazgûl rows are official card rules, and Tresserhorn's Lord was wrongly recorded as legal).

**Date:** 2026-10-16. **Scope:** read-only analysis. Nothing in `/workspace/GrokBotMTGCompanion` was edited, committed or branched.
**Read from:** `origin/main` @ `bd6f845` (worktree `/tmp/gap-wt`, since removed) and branch `origin/bot-cycle46-interactions` @ `ae54606`, the in-progress interaction phase.
**Source archive:** `grixis/source-archive/grixis-commander-encyclopediaGPT/` (commit `1836b97`), called **SA/** below.
**Brief:** Cory's 24-section design brief. "Companion" means GrokBotMTGCompanion.

---

## 0. Executive summary

1. **Most of the brief's ideas were already written down in the source repo, often in stronger wording than the brief.** The relevant SA files are:
   - `refinement/Grixis_Refinement_Protocol_v1.md`, §§2–12;
   - `architecture/DECK_QUALITY_GATES_V3.md`;
   - `grixis_pipeline/epistemic.py`;
   - `DEPENDENCY_INVALIDATION_V1.md`;
   - `Candidate_Decision_Ledger_TEMPLATE.csv`, `Playtest_Benchmark_TEMPLATE.csv` and `Deck_Finalization_Certificate_TEMPLATE.md`;
   - `source-package/research/Project_Exceptions_Current_2026-10-12.csv`.

   The source's weakness was execution. Most records are prose Markdown, not machine-readable data. The whole-list audits use boilerplate reasons; for example, Thraximundar's 99 rows have only 11 distinct reasons, and every KEEP reads "Retained in approval candidate after commander-first whole-list audit." The Forge testing never produced a valid comparison: 0 runs, engine "NOT QUALIFIED". The approval semantics also contradict each other (see §2.3).
2. **The companion's refinement engine works almost exactly against brief §§2 and 14.** In `scripts/grixis_refine.py::plan()`, heuristics are the decision authority:
   - a hard "at/near ceiling" shortcut (line 317), plus the fallback decision strings at lines 434–435;
   - absolute protections: Game Changers, Spellbook pieces, MV ≤ 2 ramp, and the `protect` list (line 328), plus the kept-combo superset check (line 423);
   - power-guard vetoes in `guard()` (line 100);
   - cuts drawn only from "generic" cards. Only cards with no hook, synergy < 5% and ≥ 16 lists are ever examined, so it is not a 99-slot pass.

   The result: 56 of 62 decks are labeled "at/near ceiling" because no candidate passed a gate. The brief (§2) explicitly rejects that inference.
3. **The companion's real strengths:**
   - verification: Oracle, legality, singleton, color identity, bracket floor, Spellbook, `validate_all` (15 steps; 16 on the cycle-46 branch);
   - provenance: a byte-identical archive with SHA256SUMS and a history bundle; frozen plans in `data/grixis_refine_batches.json`;
   - verbatim-quote discipline;
   - the new interaction review (`scripts/grixis_interactions.py`), which hashes each deck and machine-checks every CR, Oracle and ruling citation.

   These are the right foundation for the authority layer.
4. **Mandatory §13 flag, checked exactly.** The Bjorna + Cecily corrections were **not made in the last refinement cycle**:
   - They were made at **import, Bot cycle 16**, and kept through Bot cycles 37 and 45 (see `grixis/Grixis Corrections.md` lines 39–41 and 182; `grixis/Grixis Integration Summary.md` lines 69, 77 and 109–110; and the `bjorna-nightfall-alchemist-cecily.md` deck page lines 98–100 and 335).
   - The corrections replaced **Trade Secrets → Wizard Class** and **Yawgmoth's Bargain → Flame of Anor**, and **dropped Lutri as companion**.
   - The source's registry (`Project_Exceptions_Current_2026-10-12.csv`) records all three as `INTENTIONAL — ACCEPTED`, with the rule "User explicitly permits … Preserve unless the user requests a change."
   - So the companion **overrode a user-authorized project exception**. Under brief §13 that is a conflict, and **Cory must decide** (§2.1).
   - The two replacement cards are officially legal and came from the source dossier's own list of alternatives, so this was not an error under official rules. It only conflicts with project authorization.
   - A further oddity: SA's approved 100-card file (`Cecily__Bjorna__Lutri_Approved_2026-10-13.txt`) does not list Lutri. The source itself is internally inconsistent here.
5. **EDHREC Lift is ignored.** The cached EDHREC JSON (`.cache/edhrec/*.json`, 3,943 files, fetched 2026-10-15) already contains `lift` and `trend_zscore`. `edhrec()` reads only `synergy`. The source protocol (§5, "Critical ranking-method caution") notes that EDHREC replaced Synergy with Lift on commander pages on 2026-10-01 and says legacy synergy must not be treated as a current power statistic. The engine also never records sample size or retrieval date per value. It stores `num_decks` but does not use it in decisions.
6. **Self-approval risk.** The refined list is auto-promoted to `exports/grixis-archidekt/` as the deck's "final" list (`grixis_refine.py::exports()`, docstring line ~710). The "manual review" in `data/grixis_refine_review.json` is written by the bot, so it is not human approval in the brief's sense (§§8 and 18).

---

## (a) Status of all 24 brief sections

Legend:
- **Implemented:** present and adequate.
- **Partial:** some of it exists, or it exists only in the source archive.
- **Missing:** nothing usable exists.
- **Omit:** drop or modify; see (b).

"C:" marks companion evidence and "SA:" marks source-archive evidence.

| # | Section | Status | Evidence (file / function) | Notes |
|---|---|---|---|---|
| 1 | Preserve history; version, don't erase | **Partial** (strong base) | C: `scripts/grixis_archive.py --check` (SHA256SUMS, git bundle, `source.json`); deck pages keep the source list + `## Corrections applied` + `<!-- REFINED -->` block; frozen plans and `log` in `data/grixis_refine_batches.json`; git history. SA: protocol §2 (immutable baseline, normalized list hash for every revision). | No per-deck **version chain**. `grixis_refine.py` computes no list hash (grep finds no sha256 there). Exports are overwritten in place. No `supersedes` link. Only the interaction branch hashes lists (`deck_sha256`). |
| 2 | Heuristics as diagnostics, not authority; no "at ceiling" by default | **Missing** (inverted) | C: `plan()` line 317 (dependence ≥ 60% and generic ≤ 15% → "at/near ceiling", unchanged); lines 432–435 ("all N … failed the power guard … unchanged"); `guard()` hard veto. SA: protocol §12 ("rejection must rest on a substantive reason, not … 'already optimized'"). | The core change the brief asks for. Keep every gate as a computed **evidence field** on candidates. Replace "at ceiling" with "no guard-passing candidate (heuristic)", a diagnostic that triggers deeper review. |
| 3 | Machine-readable Commander Blueprint | **Partial** (source prose only) | SA: `refinement/blueprints/` has 33 `.md` files for 32 commanders (Be'lakor appears twice); the protocol §4 field list. C: `Ctx.hooks` (Oracle regex hooks); deck pages quote the blueprints; cycle-46 interaction JSON has a `dependency` category. Coverage audit: 32 of 33 blueprints carried; Norman Osborn missing. | About 30 decks have no blueprint at all, and none are machine-readable. The source field list is close to the brief's. Add the brief's extra fields: anti-goals, identity-core cards, tutor targets, dependency level, construction rules. |
| 4 | Per-deck dependency graph | **Missing** | C: building blocks only. `data/grixis_combos.json` + the Spellbook cache in the batches file give combo edges; `roles()` / `EXTRA_RX` give role tags; `Ctx.hook()` gives commander edges; interaction reviews (`CATS`: combo, engine, pair, dependency) cover 1 deck. SA: `DEPENDENCY_INVALIDATION_V1.md` and `grixis_pipeline/dependencies.py` cover *analysis* invalidation, not a card graph. | Feasible as a **generated** graph: nodes = cards and packages; edges from Spellbook, the interaction reviews, hooks, roles and the blueprint. Use it to answer "what breaks if X is removed" and redundancy counts. Indirect contribution needs interaction-review edges and should be partly hand-authored. |
| 5 | Full 99-slot pass with dispositions | **Missing in C, Partial in SA** | C: `plan()` only considers cuts from `cuts` (generic, unhooked, synergy < 5%, ≥ 16 lists; GCs, combo pieces and cheap ramp excluded). SA: `DECK_QUALITY_GATES_V3.md` "Mandatory whole-deck optimization audit"; about 56 `*Whole_List_*` files, with dispositions KEEP/CUT (CSV) or CORE/STRONG/ROLE-CONSTRAINED/CUT CANDIDATE (policy). Thraximundar CSV: 99 rows, 89 KEEP / 10 CUT, 11 distinct reasons (KEEP reasons are boilerplate). Missy's audit has real per-card reasons. | Import SA dispositions as **priors**, labeled hypothesis/strategic judgment, then regenerate. Adopt the brief's 9-value disposition enum. "Zero change only after 99 survive" is SA policy, and the companion should enforce it in its certificate. |
| 6 | Evidence aggregation instead of rigid EDHREC gates | **Partial** | C: EDHREC inclusion %, synergy, overall rank, Oracle hooks, Spellbook, role/MV, Jaccard. Lift and `trend_zscore` are in the cache but unused; `num_decks`/`potential_decks` are read but not used as a sample-size weight; no per-value retrieval date. SA: ledger CSV columns `edhrec_inclusion, edhrec_lift, edhrec_sample_size, edhrec_retrieved_date` + six 0–5 rubric scores (`Candidate_Decision_Ledger_TEMPLATE.csv`); 35 CSV ledgers / 2,531 decision rows; 57 decision `.md` notes. | Build an evidence vector per candidate; see (e). Tournament data is realistic only for the cEDH-ceiling subset; see (b). |
| 7 | Evidence-backed swap record | **Partial** | C: each swap in `grixis_refine_batches.json` has cut, add, cycle, guard reasons, review, roles/add_roles, hook (verbatim Oracle quotes), add/cut EDHREC, cut_freq, mv. SA: ledger template (hypothesis, benefit, trade-off, tests, decision, rejection reason). | Missing: deck hash before/after, expected cost, official legality vs project authorization, impact dimensions, test link, confidence, and a decision state separate from "applied". |
| 8 | Champion/challenger; no auto-promotion | **Partial / currently harmful** | C: the source list is the de facto champion and `<!-- REFINED -->` the challenger, but `exports()` promotes the refined list as **final** with no human step. SA: `variants/Abaddon_Aurora_Phoenix_Test_Variant_v1.txt` (one single-swap variant). | Keep the source/refined split, but exports must carry the state (CHALLENGER / APPROVAL_READY / APPROVED). Add challenger classes. Treat the 7 existing swaps as challengers. |
| 9 | Reproducible testing (exact math + paired MC) | **Partial** (exact math only) | C: `deck_calibration.py::hyper_at_least/hyper_between`, `build_mulligans.py::p_atleast` (hypergeometric, 99-card library); no Monte Carlo, no goldfish. SA: `Playtest_Benchmark_TEMPLATE.csv` (all of the brief's record fields); `Abaddon_Forge_Engine_Qualification_2026-10-13.md`: Forge **NOT QUALIFIED**, 0 valid comparative runs; unordered `ItemPool` iteration breaks matched starts; `analyze_abaddon_paired_pilot.py` says "pilot outcomes cannot decide card choice". | Agree that Forge should not be the engine. Build a small in-repo goldfish simulator, deterministic and with paired seeds (same seed means the same shuffle permutation for both lists), plus a hypergeometric layer. Scope it honestly; see (b). |
| 10 | Adversarial testing | **Missing** (as tests); **Partial** (as review) | SA: red-team gate (`epistemic.py::red_team_gate`, categories in `DECK_QUALITY_GATES_V3.md`); commander necessity gate. C: interaction-review flag kinds (`non-bo`, `dependency-risk`, `anti-synergy`, …). | A full adversarial simulator is impractical. Use scripted scenario stress tests in the goldfish simulator plus a structured red-team checklist; see (b). |
| 11 | Separate dimensions, not one score | **Partial** | C: dependence %, homogenization (mean/max Jaccard), generic share, Thoracle/control-core counts, bracket floor, GC count, combos (`grixis_refinement.json`, Refinement Cycle "All decks: metrics"). SA: `grixis_pipeline/quality.py` collapses 8 dimensions into a weighted score with `min_gain=0.25`, which the brief rejects; `epistemic.py` per-dimension confidence. | Adopt the brief's 11 dimensions as a vector. Use `quality.py`'s hard-fail logic but not its weighted sum. |
| 12 | Independent power-ceiling estimate | **Partial** | C: `target_of()` parses the source claim (`src_claim`); `ev.bracket_floor()`; `deck_calibration.py`; hand reviews (Evelyn, Fire Lord Azula flagged "cEDH ceiling"). SA: each blueprint's "Natural power ceiling — provisional". | No independent estimate field and no disagreement flag. The companion uses the source claim as its target, which is circular. |
| 13 | **Official legality vs project authorization** | **Partial, with a conflict** | C: `data/grixis_pending.json` + `activate_pending_grixis.py` + `validate_all::decks_step` correctly separate *pending official legality* (Madcap Jester, Dragon's Smile, Tresserhorn's Lord; `legal_from` 2026-11-13, sourced to Wizards). `evaluate_decklist.py` applies Oracle copy exceptions (Nazgûl). **No `project_authorization` field anywhere.** Bjorna/Cecily: 3 authorized exceptions removed at Bot cycle 16 import, still removed. SA: `Project_Exceptions_Current_2026-10-12.csv` (8 rows: Lutri companion, Trade Secrets, Yawgmoth's Bargain, Nazgûl ×2, Madcap Jester, Dragon's Smile, Tresserhorn's Lord); `Official_Commander_Legality_Checkpoint_2026-10-12.md`; protocol §11.4 PASS / PROJECT_EXCEPTION / FAIL / UNVERIFIED. | See §2.1. Import the registry verbatim. Add a per-card `official_status` and `project_status`. Never print "legal" for a PROJECT_EXCEPTION. The brief's wording ("last cycle's Corrections") is inaccurate on timing: Bot cycle 16, not cycle 44. |
| 14 | No absolute protection rules | **Missing** (inverted) | C: `plan()` line 328 (never cut GC, combo piece, unhooked high-synergy); line 332 (never cut ramp MV ≤ 2); line 323 `protect`; line 423 requires `src_combo_ids ⊆ new combos`; line 343 blocks GC adds unless `gcn > 3 and tgt >= 4`. | Convert each into a prior with a weight and an explicit override reason. Keep only real constraints: legality, color identity, singleton, registered exceptions, and Cory's explicit instructions such as bracket targets. |
| 15 | Evidence confidence classes | **Partial** | SA: `epistemic.py::Confidence` (VERIFIED, HIGH_CONFIDENCE, PROVISIONAL, TEST_REQUIRED, BLOCKED) and `evidence_confidence_report`. C: prose labels on pages ("Facts … guidance", "community data, not a quality judgment"). | Adopt the brief's 7 classes × confidence level as one schema for every claim; see (e). Map SA's levels onto confidence. |
| 16 | Two independent passes + reconciliation | **Missing** | C: the automatic engine plus hand reviews (10 decks) is informally two passes, but not independent or reconciled. SA: red team and commander necessity are separate gates, not separate passes. | Feasible if Pass B (performance) is mostly computed (simulator + evidence vector) and Pass A (commander-first) is blueprint-driven review. Disagreement goes to a deep-review queue. Real independence is limited when one agent writes both; see (b). |
| 17 | Zero-Improvement Certificate | **Partial** (SA template) | SA: `Deck_Finalization_Certificate_TEMPLATE.md`, `Abaddon_Finalization_Certificate_TEMPLATE.md`, `whole_list_audit_passed` fields in the quality-gate policy, `candidate_exhaustion()`. C: none. | Make it a JSON artifact generated from audit, test and candidate records, validated by schema and by `validate_all`. |
| 18 | State machine; human approval for APPROVED/LOCKED | **Partial, contradictory** | SA: `grixis_pipeline/state.py::VALID_STAGES` (UNREFINED…LOCKED, BLOCKED); `state/current_deck_overrides.json` has 62/62 APPROVED/LOCKED (user approval dates 2026-10-13…15). **But** `DECK_QUALITY_GATES_V3.md § Approval boundary` grants "standing project-level authorization" to auto-mark APPROVED/LOCKED, while protocol §10 says "Do not auto-approve, lock". C: only `legality_status: pending/active` and "refined / unchanged (ceiling)". | Adopt the brief's 10 states. Historical source approvals count as **evidence** (`approval_origin: source`), not companion approval. |
| 19 | Canonical authority registry | **Missing** (C); **Partial** (SA) | C: `data/grixis_summary.json` (slug, commanders, floor, src_claim, source_path; no hash, no state). SA: `current_deck_overrides.json` (approved_list_sha256, user_approval_date, gate artifacts); 2 decks' digests match no file because they are "logical/list digests" (`build_grixis.py` line 411). | New `data/authority/registry.json`. Record both a raw-file sha256 and a canonical normalized-list hash to avoid SA's logical/raw mismatch. |
| 20 | Reopen triggers | **Partial** | C: `validate_all` re-checks every list against the current Oracle bulk; `freshness_step`; `activate_pending_grixis.py` (legality date); interaction `--check` fails when the deck hash changes. SA: protocol §10 trigger list; `dependencies.py::invalidated()` (DECKLIST / ORACLE_SNAPSHOT / LEGALITY_SNAPSHOT / COMMANDER_STRATEGY / PROJECT_EXCEPTION). | Add a trigger evaluator that compares registry snapshot ids with current caches and sets REOPEN_REQUIRED. Port `invalidated()`; it is small and tested. |
| 21 | 17-step migration per deck | **Missing** (as pipeline) | SA ran a version for all 62 (all APPROVED/LOCKED 2026-10-13…15), with uneven depth: 37 legality attestations, 25 rules attestations (518 interaction rulings in total), 8 Card_Verification CSVs, 3 Deck_Quality_v3 JSON packets. | The milestone plan (c) is the migration. Steps 1–3 (baseline, exceptions, recover evidence) can be automated across all 62 in M0. |
| 22 | Authority hierarchy | **Partial** | C: deck pages say "Corrections we made … take precedence"; the archive is "single source of truth" *for the source*; the Mission says the source list stays credited. | The current de facto order (corrected source list > companion refinements) is fine until M7. Write the hierarchy down as policy now and switch only after approvals. |
| 23 | Engineering standards | **Partial** | C: `validate_all.py` (15 steps); `atomic_io`; deterministic tie-breaks (cycle 45); frozen plans; verbatim-quote checks. **No unit test suite** (no `tests/`; `pytest.ini` only excludes the archive); no JSON Schemas for `data/grixis_*`; "at ceiling" presents a heuristic as a conclusion. SA: 19 pytest files in `tests/`. | Add `jsonschema` validation and a `tests/` suite (the simulator especially), plus one `validate_all` step ("authority"). Minimal churn: one new module family, and refactor `grixis_refine.py` rather than rewrite it. |
| 24 | Process (inspect, classify, plan, implement, test, document, report) | **In progress** | This document covers inspect, classify and plan. | Implementation follows (c). |

---

## (b) Items to omit or modify, with reasons

### 2.1 Decisions only Cory can make (blockers for M0)
- **Bjorna / Cecily exceptions.** There are three options:
  - (i) Restore Trade Secrets, Yawgmoth's Bargain and Lutri (companion) as `PROJECT_EXCEPTION` in the canonical project list.
  - (ii) Keep both a canonical *project* list and an *official-legal* variant (the current Wizard Class / Flame of Anor list).
  - (iii) Formally retire the exceptions.

  **Recommendation: (ii).** The registry records the exceptions; the Birthday export carries both files, clearly labeled. Note also that Lutri is missing from SA's approved 100-card file, so the source never had a consistent version.
- **Future-release decks** (Madcap Jester with Dragon's Smile, Tresserhorn's Lord, Returned): state `PENDING_RELEASE` until 2026-11-13, with `project_status: AUTHORIZED_FUTURE_RELEASE`. This matches the existing `grixis_pending.json`. The only change is the explicit authorization field.
- **Source approvals (62/62 APPROVED/LOCKED in SA).** The brief says historical approval doesn't carry over. Confirm that Cory wants all 62 to start at `SOURCE_BASELINE` in the companion and not at `APPROVED`.
- **Bracket intent per deck.** When the independent ceiling estimate (§12) disagrees with the source claim (for example Evelyn and Fire Lord Azula, which are cEDH shells with weak identity), the brief's "identity-max vs raw efficiency" tension can only be settled by Cory. The engine should flag it, not decide.

### 2.2 Impractical as written, with realistic versions

| Brief item | Problem | Realistic version |
|---|---|---|
| §9/§10 full adversarial multiplayer simulator | A rules-faithful 4-player engine is a Forge-sized project. SA already showed Forge is unqualified (no matched starts, AI limits). Win-rate claims from a home-made engine would be false precision. | **Goldfish simulator (solitaire)**: draw, mulligan (London, with a declared keep policy), land drops, color requirements, mana from tagged sources, castability by turn, commander turn, engine-online turn from blueprint "engine" cards, a combo-assembly check from Spellbook pieces + tutor model. **Scenario stress tests** inside the same engine: "commander removed on turn T (×1, ×2)", "graveyard exiled at T", "artifacts wiped", "board wipe at T", "first spell countered". Each is a deterministic perturbation reporting recovery turn / assembly-probability deltas. Opponent-dependent claims (stax, aggro, fast combo) stay in a **structured red-team checklist** with confidence labels, never as simulated win rates. |
| §9 metrics like "interaction availability", "protection", "win assembly" for every deck | Needs per-card behavior models for 3,000+ distinct cards. | Model cards through **role tags + mana cost + blueprint-declared packages** (abstract: "removal available by T4", "≥ 1 protection piece with commander", "all pieces of combo X in hand/library-accessible by T"). Store each card's abstraction in the blueprint or graph so humans can correct it. Accept that rules nuance belongs to interaction reviews, not the simulator. |
| §5 full 99-slot disposition every cycle, written by hand | 62 × 99 = 6,138 dispositions per cycle. Hand-written reasons at that scale become boilerplate, as already happened in SA. | Machine-assign a **provisional disposition** from graph + evidence (role redundancy, hook, centrality, evidence vector). Write prose only for: the weakest 10–15 slots, every disposition that changed, every cut candidate, and every core card. Later cycles carry dispositions forward when inputs are unchanged (`invalidated()` logic). |
| §6 tournament / cEDH data | Only about 8–12 decks sit at a cEDH ceiling. Usable sources (EDHTop16, TopDeck.gg) cover commanders actually played in cEDH events. Most of these commanders have no tournament presence, and API terms and keys must be respected. | Pull tournament data **only for decks whose ceiling estimate is cEDH**, as an evidence field with sample size and date; `null` = "no data" (not negative). Never generalize it to casual decks (as SA protocol §3.4 says). |
| §6 "human judgment" and §16 "two independent passes" | One agent writing both passes is not independent. Cory can't review 6,000 slots. | Pass B = computed (simulator + evidence vector + graph). Pass A = blueprint-driven review. Independence comes from **different inputs**: Pass A doesn't see the EDHREC numbers, and Pass B doesn't see prose. Human judgment is spent where it matters: Cory reviews blueprints (once), APPROVAL_READY packets, and disagreement queues. |
| §6 public lists | Scraping Moxfield/Archidekt at scale is fragile and of low value. | Targeted only, as SA protocol §3.5 says: when a specific question is open, cite ≤ 3 lists with URL and date. |
| §17 "no material candidate unresolved" | The candidate universe is unbounded. | Define it as SA does: "bounded discovery closes with zero new material candidates". Record the universe definition (sources, filters, size) in the certificate. |
| Queued program: "200–500 candidates per deck" deep dive | 62 × 500 = 31,000 written evaluations is impossible. | 200–500 **machine-screened** per deck (Scryfall Oracle search from blueprint hooks + EDHREC lift list + Spellbook "almost included" + new sets), then automated A/B/C triage. Write up only A-tier (about 15–40 per deck) and B-tier close calls. |

### 2.3 Harmful or redundant (modify)
- **SA standing auto-approval** (`DECK_QUALITY_GATES_V3.md § Approval boundary`) contradicts brief §18 and SA's own protocol §10. **Do not port it.**
- **SA `quality.py` weighted score** (`quality_score`, `min_gain=0.25`) is the "one score" pattern the brief rejects (§11). Port only the hard-fail checks.
- **The companion's "at/near ceiling" label** should be removed as a decision. Keep it as a diagnostic: `no_guard_passing_candidate: true`.
- **Combo-superset rule** (`plan()` line 423): "never lose a source combo" conflicts with §14. Make it a prior: losing a combo requires an explicit reason in the swap record.
- **Brief §12 vs mission principle 2**: an "independent" ceiling estimate that disagrees with the source should **flag**, never auto-lower or auto-raise a deck's bracket target.
- **Brief §19 field bloat**: snapshot fields should reference one `snapshots/index.json` entry by id, not repeat dates per deck.
- **Redundant with existing work:** brief §20 reopen triggers for Oracle and legality changes are already enforced by `validate_all` (`decks` step + `freshness`). Wire them into states rather than building a second checker.

---

## (c) Milestone plan (brief merged with the queued program)

"Cycle" means a Bot cycle (one PR-sized unit, as in cycles 39–46). Estimates are rough.

```
M0 ─┬─> M1 (interactions, running) ──────────────┐
    ├─> M2 (blueprints) ──> M4 (graph + 99-slot) ─┼─> M5 (candidate deep dive) ─> M6 (Refinement cycle 1) ─> M7 (Cory review + Refinement cycle 2) ─> M8 (Birthday) ─> M9 (steady state)
    └─> M3 (evidence layer, simulator, knowledge) ┘
```

| M | Name | Contents | Depends on | Cycles |
|---|---|---|---|---|
| **M0** | Authority foundation | Schemas (e) + `data/authority/registry.json` for all 62. Baseline = the source's approved list → `SOURCE_BASELINE`, with raw + canonical hash. Companion refined lists → `CHALLENGER` records; the 7 existing swaps become swap records. Exception registry imported (8 rows) with `official_status` / `project_status`. Snapshot index (Oracle bulk 2026-10-15, CR 2026-09-25, EDHREC cache 2026-10-15, Spellbook cache). State machine + `validate_all` "authority" step. **Relabel exports and pages** ("at ceiling" → diagnostic; exports state CHALLENGER, not "final"). Cory decisions from §2.1. Start a `tests/` suite. | none | 1–2 |
| **M1** | Interaction review, all 62 (in progress) | Continue `grixis_interactions.py` batches A–F (Abaddon done; about 61 left). **Add** machine-readable `edges` output to each review (card → card/commander, kind, rule cite) to feed the M4 graph. Fold in the 518 SA rulings (coverage gap #1) and the Bjorna Rule 0 variant (gap #6). | M0 (deck hash = registry canonical) | 5–6 (can run alongside M2/M3) |
| **M2** | Commander Blueprints v1 (62) | Seed from SA's 33 blueprint files (32 commanders, including the uncarried Norman Osborn), `Ctx.hooks`, deck-page source commentary and interaction reviews. Write the remaining ~30. **Cory reviews a sample (or all, as he prefers): this is the highest-leverage human input.** | M0 | 3–4 |
| **M3** | Evidence layer + tooling + knowledge | (a) Refactor `grixis_refine.py` into an **evidence producer**: guards become fields; read Lift, sample size and retrieval date. (b) **Goldfish simulator** v1: hypergeometric layer + deterministic paired-seed Monte Carlo, London mulligan, mana and colors, commander turn, engine/combo assembly from blueprint packages, scenario perturbations for §10. Unit-tested; pre-registered thresholds; reports CIs (Wilson / paired bootstrap). (c) **Knowledge expansion** pages on Lift vs synergy vs inclusion, commander-first construction, and package theory, cited, in the general EDH docs. (d) Efficiency: caching keyed on snapshot ids (port `invalidated()`). | M0; simulator v1 needs M2 packages for engine metrics (can start on mana/curve metrics first) | 3–4 |
| **M4** | Dependency graph + 99-slot audit (Pass A baseline) | Generate per-deck graphs (Spellbook + interaction edges + hooks + roles + blueprint packages). Provisional dispositions for all 99 slots; SA whole-list audits imported as prior evidence. Prose for the weakest 10–15 slots, cores and changes. Baseline simulator metrics per deck. | M1 (partial OK), M2, M3 | 3–4 |
| **M5** | Candidate deep dive | Per deck: 200–500 machine-screened candidates (Oracle search by blueprint hooks, EDHREC lift list, Spellbook near-misses, sets since the last snapshot, the SA ledgers' 2,531 decisions as priors). Automated A/B/C triage; written evaluation for A and close B. Tournament evidence only for cEDH-ceiling decks. | M3, M4 | 4–6 |
| **M6** | **Refinement cycle 1** | Per deck: challengers by class (identity-max, raw efficiency, resilience, meta, new card, alt-win). Pass B computed; reconciliation with Pass A; paired simulator tests of each material swap/package; red-team checklist; certificate draft. Output: `APPROVAL_READY` packets or `REVIEW_REQUIRED`. Batches of about 10–12 decks. | M5 | 5–6 |
| **M7** | Cory review + **Refinement cycle 2** | Cory approves or rejects packets (→ `APPROVED`). Cycle 2 reruns the whole-list closure on every changed deck (package imbalance), handles rejections and `REVIEW_REQUIRED`, and processes reopen triggers (e.g. 2026-11-13 MBC legality → the pending decks leave `PENDING_RELEASE`). | M6; Cory's availability | 4–5 |
| **M8** | **Birthday folder** | `exports/birthday-<date>/`: newest list per deck (Archidekt `.txt`), plus `INDEX.md` and `index.json` with state (**APPROVAL_READY or APPROVED**; **CANONICAL_LOCKED only where Cory explicitly approved the exact hash**), certificate link, hash, and project-exception labels. Bjorna gets both variants if option (ii) is chosen. Generated by a script and checked by `validate_all`. | End of M7 (or a fixed date with whatever states exist then) | 1 |
| **M9** | Steady state + hierarchy switch | The trigger evaluator runs every cycle. After all 62 are APPROVED/LOCKED, documents promote the companion to first authority (§22); the GPT repo is labeled historical record. | M7 complete | ongoing |

**Total:** about 30–38 cycles to Birthday at full scope. A "Birthday-lite" path can fit an earlier date: M0 → M2 → M3 (mana-only simulator) → M6 on the decks most likely to improve (low dependence, high generic share, hand-review flags), with the rest shipping as `SOURCE_BASELINE` / `CHALLENGER`. That takes about 14–18 cycles. The Birthday date is not in the repo; confirm it with Cory.

---

## (d) Key risks

1. **Self-approval drift.** The bot writes the evidence, the review and the "manual" verdicts. Without a hard state gate, APPROVAL_READY quietly becomes canonical, as happens today with `exports()`. Mitigation: schema-enforced `approved_by` (a human id plus a source reference such as an issue or comment URL) for APPROVED/LOCKED; `validate_all` fails otherwise.
2. **False precision from the simulator.** Goldfish metrics tempt "win-rate" claims. Mitigation: pre-registered thresholds, CIs, a mandatory `limitations` field, no opponent-dependent conclusions, and differences inside the noise reported as "no detectable difference".
3. **Churn and homogenization from raw-efficiency challengers.** Once absolute protections become priors, generic staples may win more slots (mission principle 3). Mitigation: identity and distinctiveness dimensions are always shown next to power; the cross-deck diversity audit (SA `diversity_audit()`) runs every cycle; the minimal-churn prior is explicit.
4. **Boilerplate at scale.** This is SA's demonstrated failure. Mitigation: machine-provisional dispositions plus targeted prose; a lint rejecting duplicate reason strings above N per deck.
5. **Data drift.** EDHREC Synergy→Lift (2026-10-01) already broke the engine's main input. Others: Oracle updates, the 2026-11-13 MBC legality date, Spellbook IDs. Mitigation: a snapshot index, per-value retrieval dates, reopen triggers.
6. **The exception dispute** (Bjorna) and any future Rule-0 items. Risk: a page or export calls a project exception "legal". Mitigation: separate fields and a render rule ("project exception, not Commander-legal") enforced by `validate_all`.
7. **Hash ambiguity.** SA mixed raw-file and logical digests (2 decks). Mitigation: always store both; the canonical normalized hash is authoritative.
8. **Concurrency.** Another process commits to the repo, and multi-cycle milestones touch the same files (deck pages, exports). Mitigation: data in per-deck JSON files; generated blocks inside markers; small PRs per batch.
9. **Scope and attention.** About 30+ cycles and Cory's review bandwidth. Mitigation: the Birthday-lite path; ask Cory for blueprints and approval packets only.
10. **Tournament / public-list sourcing.** API terms, rate limits and sparse coverage. Mitigation: targeted pulls, cached with provenance; `null` ≠ negative.

---

## (e) Recommended data model

### File layout
```
data/authority/
  registry.json                  # one entry per deck (§19)
  exceptions.json                # project exceptions (§13), imported from SA CSV
  snapshots.json                 # snapshot ids → dates/versions/hashes of Oracle bulk, CR, EDHREC, Spellbook, legality
  states.md                      # human doc of the state machine (rendered)
  schemas/                       # JSON Schema (draft 2020-12) for every file below
    evidence.schema.json  blueprint.schema.json  graph.schema.json  audit.schema.json
    swap.schema.json  test.schema.json  certificate.schema.json  registry.schema.json  exception.schema.json
data/blueprints/<slug>.json      # hand-authored + seeded (§3)
data/graphs/<slug>.json          # generated (§4)
data/audits/<slug>/<cycle>.json  # 99-slot dispositions + candidate universe summary (§5, §16)
data/swaps/<slug>.jsonl          # append-only swap/challenger records (§7, §8)
data/tests/<slug>/<test_id>.json # test records (§9, §10)
data/certificates/<slug>/<canonical_hash>.json   # §17
data/lists/<slug>/<canonical_hash>.txt           # immutable list versions (§1); exports point here
data/grixis_interactions/<slug>.json             # existing (cycle 46), plus "edges"
scripts/authority/{registry,hashing,evidence,graph,audit,simulate,certify,triggers}.py
tests/test_{hashing,simulate,graph,schemas,states,triggers}.py
exports/birthday-<date>/{<slug>.txt, INDEX.md, index.json}
```

### Canonical list hash
`sha256` over UTF-8 lines `"<zone>|<qty>|<oracle_id>"` (zone ∈ commander/companion/main), sorted, joined by `\n`. Store `raw_sha256` of the file alongside it.

### Evidence item (shared by all records; §15)
```json
{
  "id": "ev:abaddon:edhrec:aurora-phoenix:2026-10-15",
  "class": "fact | derived_metric | heuristic | hypothesis | test_result | strategic_judgment | approved_decision",
  "confidence": "verified | high | moderate | low | blocked | test_required",
  "claim": "Aurora Phoenix appears in 31.2% of Abaddon decks (n=6744)",
  "value": {"inclusion": 0.312, "lift": 2.1, "num_decks": 2104, "potential_decks": 6744},
  "source": {"kind": "edhrec|scryfall|cr|spellbook|tournament|public_list|simulator|review|cory", "ref": "commanders__abaddon-the-despoiler.json", "snapshot": "edhrec-2026-10-15", "retrieved": "2026-10-15T20:20:08Z"},
  "author": "bot|cory", "created": "2026-10-16", "supersedes": null
}
```
Rule: `heuristic` and `derived_metric` can never on their own justify a decision (enforced: every `decision` needs at least one `fact`, `test_result` or `strategic_judgment`).

### Blueprint (§3)
```json
{
  "schema": 1, "deck_id": "Abaddon_the_Despoiler", "version": 1, "status": "draft|cory_reviewed",
  "commanders": [{"name": "Abaddon the Despoiler", "oracle_id": "…", "oracle_text_sha": "…"}],
  "plan": {"primary": "…", "secondary": "…", "commander_advances_plan": "…"},
  "win_conditions": [{"id": "wc:breach-led-brainfreeze", "kind": "natural|alternate|combo", "cards": ["…"], "enablers": ["pkg:tutors"]}],
  "engines": [{"id": "eng:cascade-threshold", "cards": ["…"], "online_condition": "commander on battlefield AND life_lost_this_turn >= k"}],
  "packages": [{"id": "pkg:threshold-enablers", "required": true, "min_count": 8, "cards": ["…"], "role": "enabler"}],
  "key_interactions": ["int:abaddon-the-despoiler#3"],
  "tutor_targets": [{"target": "…", "via": ["Vampiric Tutor"]}],
  "recursion": ["…"],
  "requirements": {"interaction_min": 8, "protection_min": 4, "ramp_min": 10, "lands_range": [32, 35], "colored_sources": {"U": 18, "B": 18, "R": 18}},
  "failure_modes": [{"id": "fm:no-life-loss", "description": "…", "mitigations": ["pkg:threshold-enablers"]}],
  "dependency_level": "low|medium|high|total",
  "power": {"natural_ceiling": "B4|B5|cEDH", "expected_bracket": 4, "source_claim": "4 — Optimized", "disagreement": null, "rationale_evidence": ["ev:…"]},
  "project_exceptions": ["exc:…"],
  "identity_core": [{"card": "…", "why": "…"}],
  "anti_goals": ["generic Thoracle shell", "…"],
  "thematic_constraints": ["…"],
  "construction_rules": [{"rule": "CR 903.5c", "note": "…"}],
  "provenance": {"seeded_from": ["SA:refinement/blueprints/Abaddon_the_Despoiler_v1.md"], "reviewed_by": null}
}
```

### Dependency graph (§4; generated)
```json
{
  "schema": 1, "deck_id": "…", "list_hash": "…", "blueprint_version": 1, "generated_from": ["spellbook:…", "interactions:…", "hooks", "roles"],
  "nodes": [{"id": "card:Underworld Breach", "kind": "card|commander|package|engine|win|combo|role", "roles": ["combo", "recursion"], "mv": 2}],
  "edges": [{"from": "card:Lion's Eye Diamond", "to": "combo:breach-led-bf", "kind": "piece_of|enables|tutors_for|protects|recurs|fuels|payoff_of|fixes|redundant_with", "weight": 1.0, "evidence": ["ev:…"]}],
  "metrics": {"card:Underworld Breach": {"structural_necessity": "necessary|important|redundant|independent", "breaks_if_removed": ["combo:breach-led-bf"], "redundancy": 2, "centrality": 0.41, "best_alternative_in_role": "card:…"}}
}
```

### 99-slot audit (§5, §16)
```json
{
  "deck_id": "…", "cycle": 47, "list_hash": "…", "pass": "A|B|reconciled",
  "slots": [{"card": "…", "disposition": "core|strong_retain|functional_retain|flexible|weak_retain|active_cut_candidate|package_dependent|meta_dependent|project_requirement",
             "roles": ["…"], "packages": ["pkg:…"], "provisional": true, "reason": "…", "evidence": ["ev:…"], "pass_a": "core", "pass_b": "flexible", "agreement": false}],
  "reviews": {"lands": {...}, "colored_sources": {...}, "curve": {...}, "ramp": {...}, "interaction": {...}, "protection": {...}, "combos": {...}},
  "candidate_universe": {"definition": "oracle hooks + edhrec lift top 150 + spellbook near-miss + sets since snapshot", "screened": 412, "tier_a": 23, "tier_b": 41, "snapshot": "…"},
  "deep_review_queue": ["…"]
}
```

### Swap / challenger record (§7, §8)
```json
{
  "id": "swap:abaddon:2026-10-16:001", "deck_id": "…", "commander": "…", "challenger_class": "identity_max|raw_efficiency|resilience|meta|new_card|alt_win",
  "base_hash": "…", "result_hash": "…", "adds": ["…"], "cuts": ["…"], "role_package": "pkg:…",
  "hypothesis": "…", "expected_benefit": "…", "expected_cost": "…", "rules_interaction": ["int:…"],
  "legality": {"official": "legal|banned|not_legal_until:2026-11-13", "project_authorization": "n/a|authorized:exc:…|unauthorized"},
  "impacts": {"identity": "+", "power": "0", "consistency": "+", "resilience": "-", "speed": "0", "distinctiveness": "+"},
  "observational_evidence": ["ev:…"], "priors_overridden": [{"prior": "game_changer_retain", "reason": "…"}],
  "tests": ["test:…"], "state": "CHALLENGER|TESTING|REVIEW_REQUIRED|APPROVAL_READY|APPROVED|REJECTED",
  "decision": {"verdict": "accept|reject|hold", "confidence": "high", "reason": "…", "by": "bot|cory", "date": "…"}
}
```

### Test record (§9, §10)
```json
{
  "id": "test:abaddon:goldfish:7f3a", "deck_id": "…", "kind": "exact|goldfish_mc|scenario",
  "baseline_hash": "…", "challenger_hash": "…", "simulator": {"name": "grixis-goldfish", "version": "0.1.0", "model_hash": "…"},
  "seed": 20261016, "paired": true, "samples": 20000, "mulligan": "london; keep>=3 lands & >=1 ramp|draw…", "seat": "on_play",
  "scenario": null, "preregistered": {"metric": "commander_cast_by_T4", "threshold_abs": 0.02, "registered": "2026-10-16T09:00Z"},
  "results": [{"metric": "commander_cast_by_T4", "baseline": 0.612, "challenger": 0.641, "diff": 0.029, "ci95": [0.021, 0.037], "method": "paired bootstrap"}],
  "verdict": "pass|fail|inconclusive", "limitations": ["no opponents", "role-abstracted cards"]
}
```

### Certificate (§17)
```json
{
  "deck_id": "…", "final_hash": "…", "baseline_hash": "…", "cycle": 52, "blueprint_version": 2,
  "dispositions_ref": "data/audits/<slug>/52.json", "all_99_reviewed": true,
  "weakest_slots": [{"card": "…", "why_retained": "…"}],
  "best_challengers": [{"swap": "swap:…", "why_failed": "…"}],
  "reviews": {"package": "…", "mana": "…", "curve": "…", "interaction": "…", "win": "…", "combo": "…", "resilience": "…"},
  "tests": ["test:…"], "uncertainties": ["…"], "snapshots": "snap:2026-10-15",
  "unresolved_material_candidates": 0, "zero_improvement": true,
  "state_requested": "APPROVAL_READY", "generated": "…"
}
```

### Registry entry (§19)
```json
{
  "deck_id": "Abaddon_the_Despoiler", "slug": "abaddon-the-despoiler", "commanders": ["…"],
  "current_canonical_hash": "…", "current_raw_sha256": "…", "list_path": "data/lists/abaddon-the-despoiler/<hash>.txt",
  "state": "SOURCE_BASELINE", "approval": {"cycle": null, "date": null, "by": null, "ref": null},
  "historical_approvals": [{"origin": "source", "state": "APPROVED/LOCKED", "date": "2026-10-13", "hash": "2d6203d2…", "counts_as": "evidence"}],
  "baseline_hash": "…", "supersedes_hash": null, "blueprint_version": 1,
  "snapshots": "snap:2026-10-15", "project_exceptions": [], "test_suite_version": "0.1.0", "test_result_hash": null,
  "finalization_certificate": null, "reopen_triggers": ["new_card", "oracle_change", "rules_change", "legality_change", "new_exception", "test_failure", "new_interaction", "meta_shift", "audit_error", "user_instruction"],
  "open_triggers": [], "source_repository": "corymstover/grixis-commander-encyclopediaGPT", "source_commit": "1836b97"
}
```
State transitions are checked in code. `APPROVED` and `CANONICAL_LOCKED` require `approval.by` to be a human id and `approval.ref` to point to a recorded instruction. Any change to the list hash or to a snapshot listed in the dependency map sets the state to `REOPEN_REQUIRED`.

### Exception (§13)
```json
{"id": "exc:bjorna:trade-secrets", "deck_id": "Cecily__Bjorna__Lutri", "card": "Trade Secrets", "type": "banned_card|companion|future_release|copy_rule",
 "official_status": "banned", "official_checked": {"date": "2026-10-12", "source": "https://magic.wizards.com/en/banned-restricted-list"},
 "project_status": "authorized|retired|pending_cory", "authorized_by": "Cory (source registry v8.1.4)", "source_ref": "SA:source-package/research/Project_Exceptions_Current_2026-10-12.csv#row3",
 "companion_handling": "Bot cycle 16 replaced with Wizard Class (official-legal variant)", "render_label": "Project exception: NOT Commander-legal"}
```
