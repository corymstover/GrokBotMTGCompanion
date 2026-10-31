# Phase 5/7 — Cited character and faction history lookup

**Status: PRELIMINARY RESEARCH / ENGINEERING TESTED, NOT OWNER APPROVED OR CERTIFIED.**

## v2.64 source-backed direct-claim gap closure (2026-10-31)

The five previously unconnected registered endpoints now each have a directly
incident official, historical claim, based on four Wizards primary pages:

| Previously uncovered node | Direct relationship | Original source and limitation |
| --- | --- | --- |
| Hazel Kenrith | King Kenrith and Queen Linden's child | [2019 Eldraine guide](https://magic.wizards.com/en/news/feature/planeswalkers-guide-eldraine-2019-10-31); does not supply a present-day biography. |
| Eric Kenrith | King Kenrith and Queen Linden's child | Same 2019 guide; **Eric** is the original spelling; later **Erec** usages are not silently identity-merged. |
| Lyra Dawnbringer | Commander of the angels of Serra | [2018 Return to Dominaria, Episode 5](https://magic.wizards.com/en/news/magic-story/return-dominaria-episode-5-2018-04-11); not a current leadership claim. |
| Valentin | Historic Witherbloom dean | [2021 Strixhaven legends guide](https://magic.wizards.com/en/news/feature/legends-strixhaven-2021-04-13); later status requires separate dated sources. |
| The Cabaretti | Led by Jetmir in the early New Capenna account | [Official New Capenna guide](https://magic.wizards.com/en/news/feature/planeswalkers-guide-to-streets-of-new-capenna); does not establish the present head. |

Five `CANON_CONFIRMED` source-grounded claims (`IEH001`–`IEH005`) bring the
new, **registered-only** count to **629/629** direct character/faction claim
incidences: 483 characters and 146 factions, including the newly named
Angels of Serra faction. The cited graph now holds **1,211 claims / 5,186
nodes / 8,279 edges**. These figures **do not** mean complete biographies,
coverage of all Magic characters or final owner approval. The original
v2.59 snapshot below remains preserved as historical evidence.

`scripts/audit_p5_isolated_entity_history.py --check` validates graph
identity, source links, quote digests and the lack of unsupported current
leadership. `--live` optionally verifies each short source excerpt against
the four Wizards pages. The 22-case foundation acceptance packet includes
the five new partial histories. No deck file, approval or lore-deck pilot
was changed.

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
