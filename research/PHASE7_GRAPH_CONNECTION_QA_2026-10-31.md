# Phase 7 — source-safe cross-entity connection questions (2026-10-31)

## Engineering gap

The Phase 3 graph had a strict, depth-bounded and citation-bearing path
retriever, but the normal `mv_ask.py ask` interface could not answer a general
"How is X connected to Y?" question. Its fallthrough usually queried the
entire question as though it were one entity name. This prevented useful
cross-reference navigation even where the project already stored confirmed
claims and full official-source citations.

`graph_connection_question()` now resolves both endpoints uniquely, restricts
graph traversals to `CANON_CONFIRMED` cited edges, and returns at most four
complete hops with original edge direction, traversal direction, claim IDs,
grades and official-source URLs. It always says `GRAPH_NAVIGATION_ONLY` and
`NOT_TEMPORAL_OR_CAUSAL_PROOF`; the answer is `QUALIFIED` even when every hop
is independently confirmed. No path within the search limit means `NOT_FOUND`
with an explicit limitation, never a claim that the two subjects are unrelated.
The route executes before importing large card/set/rule lookup modules.

## Specific, independently inspected example

"How is Tezzeret connected to Kaladesh?" returns three individually cited
edges: Tezzeret's order to arrest Pia Nalaar (`KLD006`), Pia's parent relation
with Chandra Nalaar (`DF005`), and Chandra's return to Kaladesh (`KLD002`).
The sources are Wizards story pages. This **does not** prove that Tezzeret
personally visited Kaladesh, that he traveled with Chandra, or that those
separately cited episodes occurred in immediate succession. The interface
explicitly forbids those inferred answers.

The regression suite `tests/test_mv_ask_graph_connection.py` uses a synthetic
graph with a disputed shortcut and reverse traversal, plus the actual cited
Tezzeret/Kaladesh path. Four methods passed locally:

```
python3 -m unittest tests.test_mv_ask_graph_connection -v
# Ran 4 tests — OK
```

Phase 7 CI's trigger and discovery include the new test. This expands practical
source-backed graph navigation, not the total chronology or comprehensive
game-rule answer engine. It does not check an additional foundation task,
alter canon-status grades, modify archived decks or accept owner gates.
