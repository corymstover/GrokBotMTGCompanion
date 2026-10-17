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
