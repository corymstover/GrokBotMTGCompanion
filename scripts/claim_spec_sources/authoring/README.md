# Claim-spec authoring records

These files are **authoring records**, committed so nothing lives only on the worker box (overnight brief).
They are not part of the build: `rebuild.sh` and `tests/test_claim_spec_sources.py` only use the
generator scripts directly in `scripts/claim_spec_sources/`, which are the source of truth.

- `b8/b8_fill_1.py` … `b8_fill_9.py` — Batch 8 (2026-10-30) fills. Each was applied **once** to a
  generator script through `patch_spec.patch()` (PRs #875, #876, #877). Re-running one would try to insert
  claims that already exist; run from `scripts/claim_spec_sources/` with `PYTHONPATH=.` only on a scratch copy.
- `b6_superseded/` — Batch 6 first drafts of generator scripts as they existed on the box before
  later batches extended them in-repo. Superseded by the committed generators; kept only for provenance.
- `probe_paraphrases_b8.py` — the probe used to choose which free-text phrasings `mv_ask` answers
  (basis for `tests/test_mv_ask_rephrased_b8.py`). Read-only; prints one line per question.

Evidence rules are unchanged: quotes are verbatim from cached official magic.wizards.com story pages and
all packs are PRELIMINARY_RESEARCH, not owner approved.
