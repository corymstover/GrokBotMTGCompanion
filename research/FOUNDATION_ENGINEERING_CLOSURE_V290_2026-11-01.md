# Foundation v2.90 — independently accepted engineering checklist closures

**Date:** 2026-11-01  
**Scope:** Three previously unchecked *technical deliverables*, not the seven foundation-release criteria or an unconditional claim of lore completeness. The 62 approved Grixis decks and frozen Scryfall source snapshots were not changed.

## Closure decisions with machine rechecks

| Checklist | Technical completion evidence | Boundaries explicitly **not** closed |
| --- | --- | --- |
| **K053 — dated debut/reprint attribution** | An independent read-only pass across all 16 `historical_cards_?.json` Oracle-ID buckets reproduces **37,853** released English-paper identities, **33,766** one-set earliest dates and **4,087** multi-set ties. Agrees exactly with the G6 independent source audit; zero per-set debut mismatches. G6 also enumerates **364** promo-only debuts, **431** instances where all earliest printings have Scryfall `reprint=true`, **1,311** Oracle identities with no qualifying released English-paper printing, and token, double-face, split, adventure and other layout cohorts. | Source is the **2026-10-29 Scryfall snapshot's `released_at`**, not verified historical retail street dates. Count excludes other-language/digital-only printings from its English-paper debut calculation. A missing qualifying paper printing is not necessarily a digitally *first* printed card. Do not flatten ties or explain away the 431 reprint flags. |
| **K104 — set/story navigation** | `mv_ask` now resolves **all 12/12** existing primary-title link records from the immutable Phase 1B bridge, preserving each official Wizards citation; independently tests every source URL and source count. Scryfall set `released_at` and first-party story-page publication dates remain separate real-world fields. Known unlinked and unknown sets fail with bounded limitations. | Not 1,062 sourced story associations, not an in-universe chronology, not depicted-art attribution or an exhaustive story map. The remaining 1,050 catalog codes are not silently connected to lore. |
| **K122 — representative hard-query testing** | The deterministic foundation packet now runs **86** Q&A cases across cross-plane/source-local chronology, explicit `UNKNOWN` cases, cited lore/entity/plane history, card/Commander evidence, Set Atlas and first-party story navigation, a published rules-interaction explanation and deliberate missing-source negatives. `tests/test_foundation_v290_checklist_closure.py` checks the independent route matrix and release flags; the existing packet generator checks each actual route, confidence and citation evidence. | A representative *regression suite* is not an open-domain reasoning guarantee, complete plot encyclopedia, live rules/ban certificate or game-state simulation. Broad difficult-Q&A coverage remains tracked separately under K119/K121 and the foundation-release gate K135. |

## Why these three checks may close honestly

Each checkbox asks for a **bounded, testable engineering deliverable**: verify dated stable printing classifications, provide a source-safe way to navigate supported set/story associations, and test difficult representative questions. The machine evidence now directly implements and checks those specific requirements. The checks do **not** assert the stronger, separately tracked goals of first-party completeness, exhaustive chronology, full currentness, owner acceptance or broad natural-language coverage. No owner-decision cell or release gate is automatically approved.

**Raw-bulk caveat:** the local sparse checkout does *not* contain the pinned October 29 compressed Scryfall Default Cards file. Thus `scripts/audit_phase1b_snapshot_gates.py --check` currently stops with `MTG_PINNED_BULK_MISSING`; its earlier committed G6 findings are retained, and the **new** independent recensus is against the 16 published historical Oracle-ID buckets, not a fresh decompression of the original bulk. Do not claim that full raw-bulk check passed in this batch. The final foundation release still requires raw-source/freshness verification on the actual candidate.

Regenerate and check with:

```bash
python3 scripts/build_foundation_acceptance_packet.py --check
python3 -m unittest tests.test_foundation_v290_checklist_closure -v
python3 scripts/audit_full_checklist.py --check
python3 scripts/update_multiverse_progress_tracker.py --check
python3 scripts/certification_dry_run.py --check
```

When the exact SHA-256-matched October 29 Scryfall bulk is restored, additionally run `python3 scripts/audit_phase1b_snapshot_gates.py --check` to repeat the source-level comparison.

The refreshed 137-item triage is `data/release/full_checklist_triage_2026-11-01.json` and `research/FULL_CHECKLIST_TRIAGE_2026-11-01.md`. The **new working state is 92/137 checked, 45 open** (28 under review; 17 blocked, including ten intentionally deferred Phase 6 tasks). Foundation remains **`NOT_RELEASE_READY`**. Source-history ambiguities, unresolved genealogy, incomplete broad history, release-time currentness and owner gates stay visible.
