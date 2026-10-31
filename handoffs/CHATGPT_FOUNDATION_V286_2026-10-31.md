# Foundation continuation handoff — v2.86 (2026-10-31)

## Prior verified baseline

GitHub main after v2.85 follow-up PR #955: `82b1e44bfbb31347f230c102447710cf90188c2a`.
PR #954's Commander Q&A fix passed 22/22 exact-head and 10/10 postmerge
checks; PR #955's documentation handoff passed 21/21 exact-head and 9/9
postmerge checks. **89/137 checked, 48 open, NOT_RELEASE_READY**.

## v2.86 engineering work

`mv_ask.py ask` gains a broad, bounded cross-entity connection route based
on the existing confirmed, cited graph. Four adversarial tests pass in a
local sparse clone, including a real Tezzeret–Kaladesh example. Complete
paths include grade, source URLs and edge direction, are only `QUALIFIED`,
and explicitly never prove a time sequence, causation, meeting or direct
relationship between endpoints. Missing or unprovable routes fail closed.
See `research/PHASE7_GRAPH_CONNECTION_QA_2026-10-31.md`.

## Remaining priority

1. Independently integrate official Amonkhet → War of the Spark and
   Thran/Weatherlight/Phyrexia histories into the source-local chronology and
   graph. Avoid combining episodes based only on publication years.
2. Improve hard rules/Oracle-currentness and mixed card/lore/rules Q&A.
3. Resolve Phase 1B source-specific product classes and Grixis/no-regression
   release evidence. Original pinned bulk hashes and owner decisions are gates.
4. Rebuild/check dependent evidence, exact-head CI and progress tracker.

Ten Phase 6 tasks are **deliberately deferred** until foundation release;
ongoing maintenance and seven release criteria are included in the raw 48
open boxes. Preserve all 62 approved Grixis lists and three unapproved pilots.
