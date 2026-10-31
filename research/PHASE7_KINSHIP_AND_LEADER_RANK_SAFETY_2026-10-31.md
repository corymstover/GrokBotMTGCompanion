# Phase 7 — kinship roles and leader-rank confidence audit (2026-10-31)

**Status:** engineering regression work; not canon-owner acceptance, release
certification, a full historical genealogy, or a change to the 62 Grixis decks.

## Reproduced issues on main v2.76

| Question | Previously returned as `VERIFIED` | Why that was unsafe |
| --- | --- | --- |
| Who is Nashi's father? | Tamiyo (claim `MOM010`, relation `mother_of`) | A cited **mother** is not evidence for a **father**. |
| Who is Killian Lu's mother? | Embrose Lu (`SX017`, generic `parent_of`) | A generic parent relationship does not establish a maternal role. |
| Who is Khrad's mother? | King Khal (`DF021`, generic `parent_of`) | A generic parent relationship does not establish a maternal role. |
| Who was the first leader of the Izzet? | `most_recent_cited` = Ral Zarek (`WR005`) | The latest article publication date does not establish the earliest in-universe officeholder. |

All four cases were reproduced against the pinned commit
`754d3631c60fbde6c17cb50d73635bbae6840508` using `scripts/mv_ask.py ask`.
The outputs expose claim IDs and primary Wizards URLs; they do **not** prove an
alternative answer or a complete family/leadership chronology.

## Evidence-safe behavior

- A `mother_of` or `father_of` edge can answer its own role. Older generic
  `parent_of` claims can answer only when their cited statement explicitly
  identifies that parent by name as the requested mother/father. For example,
  `WE009` directly identifies Oko as Kellan's father; `OT004` merely says
  Kellan is Oko's son and is not sufficient alone for that narrower inference.
- If no role-specific evidence is available, return `NOT_FOUND` with
  `NO_ROLE_SPECIFIC_PARENT_EVIDENCE` and a separate
  `known_parental_relations_not_answer` list. That list is *context*, never a
  response naming a father/mother. The original citation URLs remain visible.
- Generic parent lookups retain confirmed source-backed individual facts.
  A question requesting **parents** (plural) returns `QUALIFIED` and
  `PARENT_ROSTER_NOT_EXHAUSTIVELY_VERIFIED`, since one or two cited edges do
  not certify an exhaustive roster of biological/adoptive relationships.
- For questions requesting the **first**, **original**, or **new** leader,
  return `QUALIFIED` with `REQUESTED_LEADER_CHRONOLOGY_NOT_ESTABLISHED`,
  `verified_requested_leader: null`, and the rank term. The prior
  `most_recent_cited` field is retained only as an explicitly labeled
  publication-date citation, not a verified answer to the rank question.
- Non-ranked leader questions retain their old evidence and status; present-
  tense claims of current office remain limited by the existing currentness
  guard. Other relationship and card/rules lookups are unchanged.

## Verification and remaining limitations

Targeted command:

```shell
python3 -m unittest tests.test_mv_ask_rephrased_b8 \
  tests.test_mv_ask_rephrased tests.test_mv_ask_temporal_confidence \
  tests.test_mv_ask_kinship_and_leader_rank \
  tests.test_mv_ask_leader_phrasings_b14 tests.test_mv_ask_relations -q
```

Local result: **35 tests passed**. The new test file participates in the
existing Phase 7 `test_mv_ask*.py` CI discovery; exact-head CI still must run
and pass. This is a bounded improvement to the open Phase 7 difficult-query
item, not closure of its larger acceptance criteria. Publication-order
citations still cannot provide a complete, dated succession map. The claim
graph remains preliminary research and any role inferred from words in a
source-grade claim still depends on that claim's quality.

The release checklist remains **89/137 checked, 48 open**, with foundation
readiness **NOT_RELEASE_READY**. Phase 6 stays deferred and all owner gates,
Grixis approvals, locked snapshots, and three unapproved pilots are untouched.
