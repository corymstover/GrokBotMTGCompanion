# ChatGPT foundation handoff — v2.96 official-source entity repairs

**Base:** GitHub `main` commit `22938154c776e4bb61ae3f208da1c610b5bf3ec8`
(v2.95 merged PR #965). Work on branch
`chatgpt-foundation-source-recovery-v296-20261101`.

## Completed evidence work

One source-repair batch adds four direct claims (`EL012`, `EL013`, `SE037`,
`EO031`) from three official Wizards of the Coast works. The 40 downloaded
source pages are **local ignored cache only**; committed pack audits cover
**113/113 verbatim quotations**. The source-specific `--arc` fetch option
makes this recovery reproducible without fetching all 626 registered pages.
All registered audit entities now have ≥1 direct cited claim, from **835/839
to 839/839**. The graph grew from **1,259/5,306/8,489** to
**1,263 claims / 5,310 nodes / 8,505 edges**; no date or global-order claim
was added. See `research/FOUR_ENTITY_SOURCE_REPAIR_2026-11-01.md`.
The card-anchor snapshot was absent; a new fail-closed same-source suffix
append reuses only previously qualified Gisa card tiers for `SE037`, adding
two named-participant links without inferring a printing or art depiction.

## Open issues and authority

**98/137 checked, 39 open; NOT_RELEASE_READY.** No new checklist closure:
the entity census task was already checked at v2.95. Specifically, the
precise `fbb`, `4bb`, `rin` product identities and the strict Weatherlight /
Old Phyrexia ordering lack first-party verification; GD2–GD7 remain
owner-dependent; exact release-head external CI and freshness remain required.
The 139 qualified-only entities and thin one-claim histories warrant further
source expansion. Neither preliminary research nor a dry run is certification.

**Never resume Phase 6 or alter the 62 approved Grixis decks / 3 parked
unapproved pilots under this directive.**
