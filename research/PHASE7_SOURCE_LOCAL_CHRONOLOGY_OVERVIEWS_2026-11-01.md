# Foundation v2.94 — source-local chronology overviews without invented timeline order

**2026-11-01 · PRELIMINARY_RESEARCH_NOT_OWNER_APPROVED · NOT_RELEASE_READY**

## Engineering change

The Phase 7 natural-language entry point now recognizes `Timeline of X`,
`Show chronology of X`, and `Show chronology strand X`. Its dedicated
`ask->chronology_overview` route reads the checked, separately source-graded
`source_event_sequences_2026-10-30.json` ledger. It returns the selected
strand's original title, certainty and limitation; all event IDs, labels and
graded claim references; quoted official Wizards `BEFORE` edges; separate
non-strict temporal relations; the strict transitive reachability table;
exact reachable and unresolved strict-pair counts; and all exact page URLs.

The events array is sorted by **identifier**, not manufactured chronological
position. A locally complete strict order is explicitly labeled
`source_local_total_order`; the separate `verified_total_chronology` flag is
**always false** because no global chronology is certified. Overlaps never
become strict predecessors. Distinct account IDs are never merged by title
keyword: for example, an unqualified Mirrodin request returns `NOT_FOUND`
plus the `H` (2008 Argentum/Mirrodin) and `P` (early New Phyrexia) candidate
IDs without an invented joined sequence.

| Representative question | Bounded behavior |
| --- | --- |
| `Show timeline of Azorius` | `X`: five attested events, four cited strict edges, 10/10 locally ordered pairs from three official pages; no current-office claim. |
| `Show chronology of the Gatewatch` | `Z`: 13 source-graded events in the bounded Zendikar founding account; not a complete Gatewatch biography. |
| `Show timeline of Mirrodin` | `NOT_FOUND`, `AMBIGUOUS_SOURCE_STRAND`, choices `H`/`P`; no invented cross-account proof. |
| `Show timeline of Bloomburrow Valley` | `V`: explicit narrated-tradition flag, one non-strict temporal relation and unresolved strict-pair count; not independently verified history. |
| `Show chronology strand E` | Five-event Amonkhet/Ravnica account; three direct strict edges, unresolved pairs preserved. |
| `Show timeline of Zorblax` | `NOT_FOUND`, no sources or fictional events. |
| `Show chronology strand X` | Direct ID choice agrees with natural Azorius selection. |

All seven are executed and regression-asserted within the deterministic
foundation acceptance packet, now **99** representative end-to-end Q&A cases.
Focused unit tests also guard the separated two-event chronology route,
official-source quotations, identity ambiguity, certainty, explicit ID routing
and partial-order bounds. The actual source-local historical corpus is
unchanged: 16 strands, 144 events, 116 strict edges, five non-ordering
relations, 472/10,296 within-corpus ordered pairs, eight legacy bridges.

## Evidence boundaries and unfinished gates

This is a **query usability and correctness** improvement, not seven new
historical citations, resolution of the original Mirrodin source disagreement,
a cross-plane timestamp conversion, source-by-source exhaustive research, or
owner acceptance. The historical `fbb`, `4bb` and `rin` first-party printing
identity questions are still unverified: a 1995 retrospective reference to
Renaissance does not establish the exact localized Scryfall product identity.
Do not check off the corresponding Phase 1B research tasks without a direct
primary-source match.

K099/K103 historical breadth and K119/K121 difficult Q&A remain under
review; Phase 8 certification remains blocked. Keep all 62 approved Grixis
lists and three parked pilots unchanged. Do not restart Phase 6 deckbuilding.
