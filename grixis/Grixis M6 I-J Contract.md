# Post-M5 M6 I/J evidence and reproducibility contract

Status: **Input-evidence contract implemented; Phase-B and zero-improvement outcomes pending.**

The authoritative M5 acceptance is `data/grixis/registry.json → program.milestones.M5` (Cory's explicit 2026-10-17 acceptance). The generated Birthday corpus does not self-approve. The separate Encyclopedia repository remains the approval/lock authority for its 62 canonical decklists.

## I — Tested-pool zero-improvement certificate

`data/grixis/schemas/zero_improvement_certificate.schema.json` defines the *eventual* certificate. A PASS requires reconciliation, all required Phase-B tests, zero unresolved judgment obligations, a receipt bundle, no improving substitution remaining in the **explicitly tested** pool, and confirmation of local—not global—optimality. No certificate is emitted by this I/J input receipt process. A positive proxy simulator verdict cannot substitute for Phase-B tests or named strategic judgment.

## J — Reproducibility and receipts

`scripts/grixis_m6_ij.py --build --check` writes 62 schema-validated `data/grixis/m6/ij/input_receipts/*.json`, then recomputes SHA-256 for each of the five accepted-M5/triage inputs per deck. The receipt also binds the code generator, its schema, Birthday snapshot, corpus commit, and canonical list hash. This guarantees **byte-level traceability**, not a reproduced game result or a closed tested pool. The receipts explicitly mark Phase-B replay as false and each required future gate as pending.

`python -m unittest discover -s tests -p 'test_m6_ij_receipt.py'` includes adversarial changes to hashes, mandatory roles, code fingerprint, obligations, approval permissions, and simulator-result overclaims.

## J remaining prerequisites for final bundle

A final bundle must preserve machine-verifiable references to independent sealed Pass A/B commits and formula hashes, Pass C critic with resolved conflicts, Phase-B test receipts including model coverage and limitations, original and resulting complete decklist hashes, human/agent `judgment_review` evidence, exact snapshot/Oracle/rules versions, seed and test harness configuration, bracket stress records, and explicitly unresolved limitations. A checker must validate the referenced files against committed bytes, never just trust textual declarations.

No output from the I/J input receipt generator is eligible for `APPROVAL_READY`, `APPROVED`, or `CANONICAL_LOCKED`. The existing 62 approved decks and all project-specific exceptions must remain untouched.

## Implemented Cycle 77 commitments (2026-10-17)

- **Frozen corpus verification:** I/J now checks the accepted Birthday M5 summary's exact SHA-256 and checks each of the 62 decks' three source-input Git blobs directly against the accepted corpus commit `fcd28daff7d3f7b091de04299699645ba7e47aa2` (186 immutable M5 input comparisons). It also verifies all 62 commander/list-hash bindings, five per-deck input hashes, its generator hash and schema hash.
- **Independent first-pass commitment:** `scripts/grixis_m6_sealed.py` gives Pass A a blueprint/commander-structure projection and Pass B a separate test-verdict projection. The passes are serialized in distinct Git commits, rehashed against their original Git blobs and only then reconciled. `data/grixis/m6/sealed/reconciliation_manifest.json` binds the two commit IDs and counts. Technical field isolation is tested; the process is not evidence of a truly independent human critic. Pass C remains deliberately marked `awaiting_named_critic`.
- **Final J bundle gate:** `data/grixis/schemas/m6_reproducibility_bundle.schema.json` and `scripts/grixis_m6_bundle_check.py --check` define and verify eventual complete evidence bundles. `--require-complete` must fail until all 62 bundles exist and pass SHA, rules snapshot, named critique, effect coverage, Phase-B, mana and red-team checks. Current completed-bundle count remains zero.
- **Model limitation discipline:** A `pass` verdict from a goldfish proxy that does not model the swapped abilities is **not** supported proof of an improvement. `phase_b.tests[].supports_improvement_claim` is prohibited whenever `effect_coverage` is `bounded_partial` or `not_modelable`, irrespective of test score.
- **First strategic critique:** `data/grixis/m6/critic_batches/abaddon_01_to_05_preliminary.md` examines five Abaddon swap hypotheses. Its findings are provisional and authorize no swap.

### Unclosed gates

A/B Git-commit and input-projection separation improves reproducibility, but the workflow still runs both code paths in one CI job; it is **not** a physically isolated two-party commit/reveal blind protocol. Require separate independent execution envelopes if the strict blinding requirement cannot be shown to hold. Pass C must review all material disagreements and agreements critically; Phase-B test coverage, active-effect modeling, human/agent judgment receipts, exact Oracle/rules refresh, final complete J bundles and I zero-improvement certificates remain unproduced. M6 may not be accepted or used to auto-approve decks.

## 2026-10-21 owner waiver — substitute Pass C provenance (M6.5 only)

Cory explicitly and formally authorized substituting the completed 62/62 **ChatGPT/OpenAI GPT-6 owner-equivalent** Josh-Lee-Kwai critical reviews for the originally required **genuinely independent third-model** Pass C, **for the purpose of eventual M6 certification**. The owner response and limitation are preserved at `data/grixis/m6/governance/pass_c_owner_waiver_20261021.json` and `grixis/M6 Pass C Owner Waiver 2026-10-21.md`.

**M6.5 now qualifies as completed under the amended owner-authorized governance condition**. The original technical independence was never achieved and remains explicitly **0/62 independent reviewer executions**; 62 owner-equivalent final reviews were performed, not a third-model critique. Original sealed review evidence, actual disagreements, model provenance, and the 47 NEEDS TESTING dispositions remain intact. This supersedes only prior statements in this contract that a further *independent Pass C reviewer* must be obtained.

This waiver **does not** waive effect-aware Phase B, decision-grade judgments, M6 I local-optimum or J reproducibility evidence, final Oracle/legality/exception handling, individual exact deck approvals, or milestone acceptance. All M6 J evidence bundles that rely on owner-equivalent Pass C must trace the receipt and disclose lack of technical independence. **M6 is still in progress; no schema-valid final bundle is certified by this waiver.**
