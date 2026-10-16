# Grixis source archive (grixis-commander-encyclopediaGPT)

> **Bot cycle 45 (2026-10-16).** The companion now holds the **complete** [grixis-commander-encyclopediaGPT](https://github.com/corymstover/grixis-commander-encyclopediaGPT) repository. From now on, **GrokBotMTGCompanion is the single source of truth** for the Grixis work. The original GitHub repo was not changed and stays as it is. It is now a historical upstream, not a dependency.

| | |
|---|---|
| Source repo | <https://github.com/corymstover/grixis-commander-encyclopediaGPT> |
| Commit | `1836b976ed2f5b6ff22a5d0a3c6f827e8f952110` (`1836b97`, 2026-10-16 03:58 UTC, "Add verified 62-deck Archidekt import package") |
| Imported | 2026-10-16, Bot cycle 45, by `scripts/grixis_archive.py --import` from a clean read-only clone |
| Tree | [grixis-commander-encyclopediaGPT/](grixis-commander-encyclopediaGPT/README.md): **1,017 files, 14,865,126 bytes**, byte-identical; only `.git` excluded |
| Manifest | [SHA256SUMS](SHA256SUMS): one SHA-256 per file (`sha256sum -c` format, paths relative to the tree) · [source.json](source.json): commit, counts, bundle hash and branch heads |
| History | `history/grixis-commander-encyclopediaGPT.bundle` (6.4 MB): git bundle with **all 49 branches** and **1,726 commits** |

## Contents
- [Verification](#verification)
- [Why a snapshot plus a bundle](#why-a-snapshot-plus-a-bundle)
- [Inert by design](#inert-by-design)
- [Map of the archive](#map-of-the-archive)
- [Where the content is already integrated](#where-the-content-is-already-integrated)
- [Refreshing](#refreshing)

## Verification
- **At import:**
  - The archived tree was compared with the source clone at `1836b97`: 1,017/1,017 tracked files, **0 hash differences**.
  - `diff -r` against the working tree came back clean.
  - `sha256sum -c SHA256SUMS` passes.
  - Restoring the history bundle with `git clone` gives the same HEAD and 1,017 files.
- **Every run since:** `scripts/validate_all.py` step `source-archive` (`scripts/grixis_archive.py --check`) re-hashes every file against `SHA256SUMS`. It fails if a file is missing, extra or changed, if the file count, byte total or bundle hash differs from `source.json`, or if a root `.github/workflows` appears.
- **Comparing with a clone:**
  ```bash
  python3 scripts/grixis_archive.py --check --against /path/to/clone
  (cd grixis/source-archive/grixis-commander-encyclopediaGPT && sha256sum -c --quiet ../SHA256SUMS)
  ```

## Why a snapshot plus a bundle
A plain snapshot (`git archive HEAD`, then `tar -x`) is one atomic step from a clean clone. If the box is interrupted, it can simply be re-run, with no half-finished merge state. `git subtree add --squash` would have added a merge commit but not kept the history. Instead, the full history (every branch, including `baseline/freeze-2026-10-12` and the per-deck refinement branches) is kept cheaply as a 6.4 MB git bundle. To restore it:
```bash
git clone grixis/source-archive/history/grixis-commander-encyclopediaGPT.bundle /tmp/grixis-src-restored   # all branches under origin/*
```

## Inert by design
Nothing in the archive runs in the companion:
- **Workflows:** the 62 workflows sit under the archive path, not the root `.github/`. GitHub only runs root workflows, and `--check` fails if a root `.github/workflows` exists.
- **Scripts and tests:** the 96 scripts, the `grixis_pipeline` package and the 19 test modules are never imported or run by the companion's generators or `validate_all`. Root `pytest.ini` has `norecursedirs = grixis/source-archive`, and the companion's own `python3 -m unittest discover` finds no tests.
- **Checkers and indexes:**
  - `check_links.py` and `check_citations.py` skip the tree, because it is archived content, not companion pages. The 788 Wizards URLs and 0 broken links are unchanged.
  - `front_matter.py` and `kb_find.py` only index registered pages and deck folders, so nothing is double-counted.
- **ripgrep:** `.rgignore` hides the tree and bundle from plain `rg`, so card searches are not double-counted. Search it on purpose with `rg --no-ignore-dot PATTERN grixis/source-archive/`. Note that an explicit `-g/--glob` include overrides `.rgignore`.
- **Generators:** `build_grixis.py`, `grixis_eval.py`, `grixis_refine.py` and `lore_quotes.py` now read this archive by default, not `/workspace/grixis-src`. The commit they cite comes from `source.json`. A clone path can still be passed, e.g. `build_grixis.py /path/to/clone`. Rebuilding from the archive gives the same pages.

## Map of the archive
Paths are relative to [grixis-commander-encyclopediaGPT/](grixis-commander-encyclopediaGPT/README.md). Counts are files.

| Area | Files | What it contains |
|---|---|---|
| `README.md`, `PROJECT_AUTOMATION_RUNBOOK.md`, `requirements-scryfall.txt` | 3 | Project operating rules, current checkpoint, automation runbook |
| `refinement/decklists/` | 151 | Every list version: frozen baselines, candidates, proposals, approved/locked lists (TXT/CSV) |
| `refinement/verification/` | 332 | Per-deck verification packets: approval-ready checks, whole-list audits, provenance passes, card verification CSVs, **38 `*_Rules_Attestation.json` files (518 interaction attestations, all PASS)** and official-legality attestations |
| `refinement/decisions/` | 92 | Candidate decision ledgers (CSV) and decision notes per deck |
| `refinement/approvals/` | 54 | User approval records per deck |
| `refinement/blueprints/` | 33 | Commander-first blueprints |
| `refinement/tests/` | 35 | Abaddon test programme: interaction coverage inventory and triage CSVs, Forge engine qualification, smoke-test results, finalization gates and runbooks, integrity payload scripts |
| `refinement/rules/` | 1 | [Abaddon the Despoiler Interaction Review](grixis-commander-encyclopediaGPT/refinement/rules/Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md) (63 KB): the model for phase 2 |
| `refinement/evidence/`, `metadata_audit/`, `audits/`, `policies/`, `variants/`, `tracker-sync/`, `tracker_reconciliation/` | 11 / 10 / 1 / 1 / 1 / 1 / 1 | Deck Quality v3 evidence dossiers, Scryfall metadata overlays and Oracle cache (JSONL), audit, policy, variant, tracker records |
| `refinement/*.md, *.csv` (top level) | 10 | Refinement Protocol v1, Workflow Optimization Playbook v1, Optimization Kit, legality checkpoint, tracker, templates (decision ledger, playtest benchmark, finalization certificate) |
| `architecture/` | 9 | Adaptive Pipeline v2 (contract, freeze checklist, release notes), Deck Quality Gates v3, Dependency Invalidation v1, Optimization Stopping Rules, Oracle Data Access v1, whole-list audit migration |
| `grixis_pipeline/` | 9 | Python package (437 lines): content-addressed cached stages, dependency invalidation, epistemic gates (red team, hypothesis tests, commander necessity, diversity audit), quality comparator, telemetry metrics, batch runner, state derivation |
| `scripts/` | 96 | Verifiers (`verify_*`, 23), one-shot finalizers (`finalize_*`, 34), oracle-cache augmenters (`augment_*`, 12), builders (`build_*`, 12: decision ledgers, oracle cache, Archidekt export), Forge tooling (`probe_forge_card_coverage`, `prepare_abaddon_forge_smoke_decks`, `run_abaddon_same_seed_pilot`, `analyze_abaddon_paired_pilot`), Scryfall refresh/validation, tracker/state/contract checks, Archidekt export builders |
| `tests/` | 19 | Unit tests (`unittest`) for the pipeline, Forge tooling, tracker, metadata refresh and retry logic |
| `.github/workflows/` | 62 | Archived (inactive) GitHub Actions: 35 verify, 17 finalize, 5 apply-approval, 2 Forge probes, the Abaddon same-seed pilot, adaptive pipeline v2, weekly Scryfall refresh |
| `config/`, `state/`, `templates/` | 1 / 2 / 1 | Pipeline policy (YAML), current cycle and per-deck override state (JSON), deck-quality evidence packet template |
| `source-package/` | 15 | Frozen `GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz` baseline, source manifest and hash manifest, status reports, consolidation register, review queue, historical guide v8.1.4, project-exceptions research |
| `exports/` | 66 | 62-deck Archidekt import package (2026-10-15): ZIP, MASTER.txt, per-deck files, README |

## Where the content is already integrated
Cory's coverage audit (cited in the Bot cycle 45 brief) puts **about 78% of the source's unique content** in companion pages already. This archive holds the rest verbatim, mainly the process machinery, per-deck verification packets and the full test programme.
- **Decks:** [grixis/decks/](../decks/): 62 deck pages, with each commander's blueprint, swap decisions, approval record and evidence dossiers quoted verbatim, the source's role tags and pinned printings, plus refined lists.
- **Grixis section:** [Grixis README](../README.md) · [Evaluation](../Grixis%20Evaluation.md) (all 62 source lists re-checked) · [Corrections](../Grixis%20Corrections.md) · [Packages](../Grixis%20Packages.md) · [Refinement Cycle](../Grixis%20Refinement%20Cycle.md) · [Mission](../Grixis%20Mission.md).
- **Integration record:** [Grixis Integration Summary](../Grixis%20Integration%20Summary.md): inventory, what was integrated, what was generalized into the any-identity [EDH Deck Template](../../EDH%20Deck%20Template.md), [Evaluation Checklist](../../EDH%20Deck%20Evaluation%20Checklist.md) and [EDH Standards](../../EDH%20Standards.md#deck-evaluation-method-from-the-grixis-repo), and what was not taken.
- **Exports:** [exports/grixis-archidekt/](../../exports/grixis-archidekt/README.md) (the companion's final lists; the source's own package is under `exports/` here).

## Refreshing
The original repo stays untouched. If it ever gets new commits, update the archive from a fresh read-only clone:
```bash
git clone https://github.com/corymstover/grixis-commander-encyclopediaGPT /tmp/grixis-src
python3 scripts/grixis_archive.py --import /tmp/grixis-src     # re-snapshot HEAD, rebuild bundle, SHA256SUMS and source.json
python3 scripts/build_grixis.py && python3 scripts/validate_all.py
```
