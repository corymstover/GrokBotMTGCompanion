# Phase 5/7 — Cited character and faction history lookup

**Status: PRELIMINARY RESEARCH / ENGINEERING TESTED, NOT OWNER APPROVED OR CERTIFIED.**

The Phase 3 graph already records hundreds of characters and factions, but
natural-language questions such as "What is the lore of Nicol Bolas?" were
not routed to the stored claims. The `mv_ask.py ask` entry point now exposes
an explicitly **partial history** for exact or unambiguously resolved
`Character` and `Faction` nodes. This is a read-only retrieval improvement:
**no claims, graph edges, dates, sources, grades or Grixis decks changed.**

## Reproducible usage

```bash
python3 scripts/mv_ask.py ask 'What is the history of Nicol Bolas?'
python3 scripts/mv_ask.py ask 'What is the lore of the Izzet?'
python3 scripts/mv_ask.py ask 'Tell me about the history of the Gatewatch'
python3 -m unittest discover -s tests -p 'test_mv_ask_entity_history.py' -q
```

At the 2026-10-30 graph checkpoint: **483 Character nodes, 145 Faction nodes**;
**623 of the 628** have at least one directly incident source-graded graph
claim, while five registered nodes have none. For orientation, direct distinct
claim counts include Nicol Bolas **51**, the Gatewatch **22**, and the Izzet
League **5**. Counts describe *only direct graph incidence*, **not** the
depth of a complete biography or the entirety of canon.

## Evidence boundaries

- Every response carries claim ID, original status/grade, summary, caveat,
  optional quoted in-world date, optional undated era label, named direct
  relationships and the original source URLs. Multiple relations from one
  claim are grouped and counted as **one** claim.
- All nonempty histories are `QUALIFIED` with
  `PARTIAL_CITED_ENTITY_HISTORY`, `DIRECT_GRAPH_CLAIMS_ONLY` and
  `NO_VERIFIED_TOTAL_CHRONOLOGY`. Original non-confirmed statuses remain
  visible. A cited historical leader is **not** asserted to be the current
  leader; a source publication date is not an in-world historical date.
- The route does not walk through neighboring people, locations, cards,
  printings or entire factions to invent additional biography entries.
  It does not conflate all members of a group with the group's direct acts.
- A registered node with no direct claims returns `NOT_FOUND` with an
  explicit absence-of-evidence flag; a missing name follows ordinary Q&A
  fallback. Neither proves the subject absent from Magic's canon.
- Plane-history, specific relationship, card, rules and cited chronology
  routes retain their existing precedence. The phase-6 Commander pilots
  remain parked and unapproved.

## Verification

The focused test suite cross-checks **every registered Character and Faction**
against the original graph's directly incident claim-bearing edges. It checks
deduplication, claim grades, Wizards source references, the no-chronology
assertions, alias consistency and the preservation of other Q&A routes.
The existing Phase 7 `test_mv_ask*.py` CI matrix includes these tests.

## Remaining work (not newly checked off)

Research comprehensive, chronologically grounded biographies and faction
histories from original Wizards stories; compare variant identities, retcons,
leadership transitions and cross-plane events; connect them to exact source
evidence while preserving uncertainty. The present graph-based retrieval
cannot substitute for these tasks or for foundation certification.
