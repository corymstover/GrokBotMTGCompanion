# MTG Companion v3.08 handoff — independently checked set totals

**Current sources:** `MTG_MULTIVERSE_MASTER_WORKFLOW.md` v3.08;
`Progress Tracker.md`; `data/release/full_checklist_triage_2026-11-01.json`;
`data/release/set_totals_acceptance_2026-11-01.json`;
`research/POSTFOUNDATION_SET_TOTALS_V308_2026-11-02.md`.

## Published baseline

- v3.06 PR #976, merged `4d64fe87a4d7a35f8493744557baa531ac5917cc`:
  14/14 PR and 10/10 exact-main Actions PASS.
- v3.07 PR #977, merged `3170c5c0c17015c9b1a544d9290d1312515bab67`:
  14/14 PR and 11/11 exact-main Actions PASS.
- Main tree before this batch:
  `5c7e0d8f2fa5e0d029a9c05292fb3cab8e65aaf1`.
- v3.00 SHA-pinned foundation certificate separately 7/7; exact legacy
  acceptance-packet replay must remain unchanged.

## v3.08 changes to publish

- K050 bounded qualified category-count **publication** check: 1,062
  set codes; 145 all-date Scryfall expansion/core types, 142 released
  nondigital candidates, 136 Wizards-primary-supported regular/mainline,
  four documented auxiliary, two provisional border, 848 other paper,
  62 digital and 10 future. The 140 Wizard-supported regular/auxiliary
  records retain exact per-code primary URLs. Explicitly **not** a universal
  all-time Wizards premier set roster.
- New independent `audit_set_totals_acceptance.py --check` and nine negative
  tests integrated into the Multiverse integrity workflow.
- Triage: **117/137 checked**, **20** historical open, **14** active
  repository-build tasks, **six** excluded only from the owner's build
  finish line. Never mark excluded tasks approved or permanently complete.
- PR creation and exact-main CI validation are pending this handoff.

## Remaining repository-build IDs (14)

K022, K045, K046, K074, K078, K079, K080, K088, K098, K099, K100,
K103, K108, K110. The first three lack named first-party product proofs;
the history and chronology tasks have source and uncertainty gaps; deck
strategies, current rules, realistic power and combos require further
independent engineering acceptance.

## Owner constraints

- Do not mutate the **62 approved Grixis decks**.
- The three existing pilot decks remain **UNAPPROVED** until rebuilt and
  individually reviewed by Cory **after** repository development finishes.
- K112–K114 pilot sign-offs and K105/K125/K126 ongoing monitoring are not
  repository-build tasks but remain archival unchecked.
- Do not announce repository completion until the **14** actual engineering
  requirements have valid evidence and exact-main CI succeeds.
