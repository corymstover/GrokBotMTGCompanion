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

**Harvest (cycle 64.2, +318 → 366 items):**
- 76 rows from the 10 source candidate-decision CSV ledgers.
- 233 rows from the `| Cut | Add |` final-delta tables in the 28 Markdown candidate-decision files. A row is classed `mana_decision` when either card is a land (Scryfall type line).
- 9 legality, project-exception, colour-identity and mana items from cycles 16, 44 and 47 and the source verification files.
- Every item now carries a `deck_snapshot` (registry deck id, commanders, canonical and baseline `lh1`, source raw sha256 at commit 6ccc5b0).
- v1 prompts are self-contained.
- v1 labels are prefixed `unvalidated_v1_judgment`.
- Source labels say whether the list was user-approved (`source_process_decision (user-approved list)`) or not human-validated.

**Cycle 64.3 (+271 harvested, −48 de-duplicated → 589 items):**
- 236-row CUT pass over the 14 whole-list audit CSVs (rows with a named replacement only).
- `→` bullets from the 27 current-cycle decision files.
- 62 Game Changer / bracket-floor items and 2 hash-provenance items from the Bot cycle 37 corrections. The 62 `format` rows are not itemised because tag and format normalisation is not a decision-quality question.
- Quality pass: exact (deck, cut, add) duplicates dropped; mana items with the same (cut, add) pair across decks kept once (48 dropped); 64 no-cut rows (all rejections) reworded to "is there a defensible cut?".
- The checker now also requires every `deck_snapshot` id to exist in the registry.

## Evaluation roles and the reporting rule (cycle 64.3)

Every item has an `evaluation_role`:

| Role | Meaning | What a pass means |
|---|---|---|
| `detection` | The system must find or flag the error or upgrade (rules, factual, legality, bracket-floor and Cory-correction items). | It produces the sealed outcome. |
| `regression_guard` | The canonical baseline already contains the outcome: the source's approved change is in the list the new system starts from. **These items cannot measure detection.** | The system does NOT propose reverting the change without new evidence. |
| `judgment_calibration` | The label is an unvalidated GrokBot v1 judgment or a source-process decision no human validated. | Agreement or calibration against that judgment; never reported as accuracy. |

**Reporting rule** (in `manifest.json` `reporting_rule`, enforced by `--check`): every benchmark report gives results per stratum of `evaluation_role` × `originated_by` × `contamination.level`, with counts, and **never one pooled score**. The prospective holdout is reported separately.
