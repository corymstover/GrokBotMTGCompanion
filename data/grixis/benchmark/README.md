# G0 benchmark corpus (Bot cycle 64.1)

Step G0 of the [Grixis Birthday Upgrade Plan](../../../grixis/Grixis%20Birthday%20Upgrade%20Plan.md) (Cory decision D2, t54u).

- `corpus.json`: **evaluation input**. Outcome-free prompts with category, originating and catching system, sources (file + quote + commit, PR + merge commit, or chat ref + the file that records it) and a **contamination flag** (`yes` / `partial` / `no` with a reason). Schema: `data/grixis/schemas/benchmark_item.schema.json`.
- `sealed/<id>.json`: the expected outcome, label authority and leak terms. Never given to the evaluated system. Its sha256 is in `manifest.json`.
- `manifest.json`: corpus, sealed and holdout hashes plus the freeze rule.
- `prospective_holdout.json`: empty for now, with the rules for adding future cards, corrections and human decisions before the system sees them.

**Checker:** `python3 scripts/grixis_benchmark.py --check` (validate_all step `benchmark`). It checks the schema, that the sealed hashes match the manifest, that no leak term or outcome appears in a prompt, and that every source exists (the quote is in the file, the commit is in git, the chat ref is in its record).

**Honesty limits:**
- Sealed files live in the same repository, so sealing gives tamper evidence and input separation, not secrecy.
- No retrospective item is flagged `no`: the new system has already ingested the source archive, the v1 refinement data and Cory's corrections.
- Labels from GrokBot v1 hand reviews and the power guard are v1 judgments, not ground truth (`label_authority` says so).

**Freeze rule:** the corpus may grow in G0 batches until step A begins. From the first A commit it is immutable; only the holdout grows.

**Harvest (cycle 64.1, 48 items):**
- 10 source-archive corrections (Ashnod Oracle, Abaddon cascade, Kess SHA).
- 4 v1 power-guard reverts (PR #111).
- 17 v1 hand-reviewed swaps.
- 4 v1 commander-identity scoring gaps and 2 v1 identity-vs-ceiling calls.
- 11 new-architecture errors caught by Cory (t49u/t50u) or the MV checker (PR #140).

The one-off harvest script is kept outside the repository because it holds answers next to prompts.
