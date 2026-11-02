# v3.05 — Cory's repository-completion finish line

The user has clarified that two kinds of unfinished historical checkboxes are **not unfinished repository construction**:

1. **Individual approval of the three pilot decks.** They will be **rebuilt using the completed repository's updated data and reviewed individually afterward**, not approved now or used to hold the repository hostage.
2. **Indefinite maintenance and monitoring.** Future stories, Oracle/rules changes, and future set/printing imports are recurring operations. Their perpetual nature does not prevent a completed initial repository build.

The 137-task Master Workflow remains a permanent auditable historical list. No original box has been checked, erased, or rewritten to manufacture progress. Instead `scripts/audit_full_checklist.py` assigns each task an independently auditable `completion_scope`, alongside its original triage status.

| Classification | Tasks | Counts toward repository-completion work? |
| --- | --- | --- |
| Already checked engineering tasks | 113 | Already done |
| **Active repository build** | **18** | **Yes** |
| Individual pilot reviews after full rebuild | 3 (`K112`, `K113`, `K114`) | No |
| Recurring maintenance after repository build | 3 (`K105`, `K125`, `K126`) | No |
| **Original historical checklist total** | **137** | Retained in full |

The 18 remaining build items are exactly:

- **Set/printing/source:** K022, K045, K046, K050, K055.
- **Card-to-lore and relationship graph:** K064, K069.
- **Original deep lore packs and chronology:** K074, K078, K079, K080, K088.
- **Broader historical and cross-plane knowledge:** K098, K099, K100, K103.
- **Reusable Commander strategy and rules-engine verification:** K108, K110. These remain engineering scope, **not final pilot acceptance**.

**Finish condition:** all 18 build items close only with reproducible, source-qualified evidence; relevant tests and exact-release GitHub CI pass; original protected Grixis decks remain unchanged. Existing bounded **7/7 certified foundation** is a prior milestone, not 18/18 repository completion. Never treat speculative genealogy, missing Wizards print proofs, untested deck interactions, future changes or an owner's future deck acceptance as already resolved.

The new triage JSON exposes `totals.remaining_repository_build`, `totals.excluded_from_repository_build`, and the two exclusion subcounts. Each item has `completion_scope` and `build_scope_reason`; the Markdown report lists only actionable items under the phase work sections and moves all six exclusions into an explicitly outside-build appendix. The generated Progress Tracker mirrors these counters. Tests fail if any of the six task IDs/wording change, a deferred review is marked completed, or the counts stop reconciling.

## Reproduce

```bash
python3 scripts/audit_full_checklist.py --check
python3 -m unittest discover -s tests -p 'test_full_checklist_triage.py' -v
python3 scripts/update_multiverse_progress_tracker.py --check
python3 -m unittest discover -s tests -p 'test_multiverse_progress_tracker.py' -v
python3 scripts/audit_foundation_milestone_certificate.py
```
