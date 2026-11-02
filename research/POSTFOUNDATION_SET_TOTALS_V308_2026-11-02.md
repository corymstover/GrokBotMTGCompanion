# v3.08 — qualified set-code and product-category counts

K050 asks for separately reproducible set-code and premier expansion/core
figures without an unqualified "total sets." This batch accepts the *finite
publication/counting requirement* and preserves the separate stronger
first-party exceptions and all-time premiere-roster limitation as open work.

## Independently checked denominators

| Snapshot measure | Count | Exact interpretation |
|---|---:|---|
| All Scryfall `/sets` codes | 1,062 | Set-code catalog objects, not separate sold products |
| Scryfall expansion/core types, all statuses | 145 | 120 expansion + 25 core codes, including future variants |
| Released nondigital expansion/core candidates | 142 | As of frozen 2026-10-29 date; **candidate**, not universal premier certification |
| Wizards-cited historical regular/mainline | 136 | Individually reviewed primary-supported subset of those 142 candidates |
| Documented auxiliary/discarded | 4 | `big`, `mat`, `sum`, `tsb`; not added to regular/mainline |
| Provisional foreign-border variants | 2 | `fbb`, `4bb`; primary classification remains unresolved (K022) |
| Other released paper-category codes | 848 | Includes supplements, Commander products, promos and tokens |
| Released digital-only codes | 62 | Separate from released paper candidates |
| Future announced codes | 10 | Not yet released at cutoff |

The six exclusive scope classes sum to 1,062:
`136 + 4 + 2 + 848 + 62 + 10 = 1062`. The official-supported
regular/auxiliary subset has 140 per-code `magic.wizards.com` citations;
individual source URLs and the exact per-code scope are preserved in
`data/set_atlas/phase1b_release_scope_story_bridge_2026-10-29.json`.
The 24-category Scryfall-type census independently agrees with the older
`phase1b_snapshot_gates_2026-10-30.json` audit.

## Acceptance and explicit non-claim

`scripts/audit_set_totals_acceptance.py --check` rebuilds the frozen report
`data/release/set_totals_acceptance_2026-11-01.json`, with input hashes,
the full per-type inventory and all 140 primary-cited codes. Nine tests
reject an invented all-time premier certificate, a missing set code,
category/date/digital drift, foreign-border upgrade without Wizards
evidence and substituted/nonofficial citations. The output **must** keep
`all_time_wizards_premier_census_certified: false`.

This closes the exact K050 *published, clearly defined category totals*
deliverable without claiming that Wizards has supplied a complete all-time
premier-set roster. It does not close K022 (two foreign-border variants),
K045 (13 curated/starter exceptions) or K046 (11 older boxed/regional
products). Those require separate first-party historical corroboration.
Nor does this refresh later releases; that is event-driven upkeep (excluded
from repository-build work by Cory).

## Protected scope and resulting finish line

Historical **117/137 checked**; **20** open. Only **14** are active
repository-build items after excluding three individual post-build pilot
approvals and three perpetual maintenance tasks. All three pilot proposals
remain UNAPPROVED and all 62 owner-approved Grixis lists remain unchanged.
The v3.00 foundation's separate 7/7 certificate is neither redefined nor
silently advanced by these counts.
