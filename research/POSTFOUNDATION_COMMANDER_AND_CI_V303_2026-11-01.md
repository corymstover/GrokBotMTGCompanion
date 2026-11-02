# v3.03 — Bounded Commander choice comparisons and CI-domain acceptance

The knowledge foundation remains **7/7 independently certified** for the original v3.00 release tree. The broader project advances from **111/137 to 113/137 engineering boxes**, with **24 still open**. This evidence is bounded: it does not approve a deck, establish current Commander legality, prove complete canon, or enable a future CI result to be assumed green.

## K107: commander options verified without story inflation

`scripts/audit_lore_commander_comparison.py` rebuilds `data/release/phase6_commander_comparison_2026-11-01.json` from existing **UNAPPROVED** pilot specs/printing evidence, the dated card index and `scripts/commander_rules.py`. It compares **two Commander-eligible candidates per pilot** without altering a card or a commander slot.

| Theme | Existing commander | Alternative | Source/identity distinction |
| --- | --- | --- | --- |
| Ugin & Bolas | Nicol Bolas, the Ravager (UBR) | Nicol Bolas (UBR) | Both are directly cited character-card contexts in the audited pilot. Neither art is asserted to prove a distinct scene. |
| Original Primeval Dragons | The Ur-Dragon (WUBRG) | Scion of the Ur-Dragon (WUBRG) | Both are **thematic** Dragon Avatar options. Neither is verified as a particular Primeval or Elder Dragon War participant. |
| Ugin's allies | Jace, Multiverse Architect (WUBR) | Jodah, the Unifier (WUBRG) | Jace has a cited official Jace/Ugin encounter; Jodah is a color-eligible alternate with **no verified Ugin ally link** in the curated pilot. |

Each is Commander-eligible according to the project's dated Oracle/rules model, and both choices can host the current 100-card draft's required color pool. This does not mean switching commanders leaves gameplay or story quality intact. The report retains provenance, source limits, the September 25 CR date, October 19 update-bulletin warning, and pilot `UNAPPROVED` status. Negative tests fail on invented names, duplicate commanders or inflated official-story grades.

## K124: targeted CI coverage (not branch-protection enforcement)

`scripts/audit_ci_domain_coverage.py` deterministically maps **nine** requested test domains to existing GitHub Actions workflows. It checks pull-request triggers, expected executable checks, real test/script paths, no `continue-on-error: true`, and workflow-content SHA-256. These domains include card counts/identity, source quote integrity, cited graph, rules, Q&A, set/printing data, frozen lore-pilot deck legality, original Grixis mechanics, and release/progress regressions. `tests/test_ci_domain_coverage.py` removes a required executable step in a temporary fixture and asserts that the audit fails closed.

**Administrative limitation:** Committed workflow YAML does not prove that GitHub branch protection *requires* every status check. The nine-domain report explicitly states that this protection setting is unverified and does not certify any future Actions run. The prior PR #972 did pass 13/13 candidate and 9/9 merged-main checks on their exact SHAs; v3.03 must earn its own green checks before merging. This is a finite CI coverage capability accepted under Cory's broad post-foundation engineering instruction, not a permanent upkeep guarantee.

## Remaining open work

- K108, K110: coherent realistic-power strategies, independent combo assessment and genuinely current Commander legality/brackets need additional verification.
- K112–K114: all three individual pilot decisions remain **UNAPPROVED**; no owner deck lock or canonical Grixis deck is touched.
- Set and source variant corroboration, ancient Elder Dragon genealogy, history coverage, fully connected temporal relations and future update/reconciliation tasks remain open. A checkmark cannot establish a missing first-party source or an unobserved rule change.

### Reproduce

```bash
python3 scripts/audit_lore_commander_comparison.py --check
python3 scripts/audit_ci_domain_coverage.py --check
python3 -m unittest discover -s tests -p 'test_lore_commander_comparison.py' -v
python3 -m unittest discover -s tests -p 'test_ci_domain_coverage.py' -v
python3 scripts/audit_lore_pilot.py
python3 scripts/audit_foundation_milestone_certificate.py
python3 scripts/audit_full_checklist.py --check
python3 scripts/update_multiverse_progress_tracker.py --check
python3 scripts/certification_dry_run.py --check
```
