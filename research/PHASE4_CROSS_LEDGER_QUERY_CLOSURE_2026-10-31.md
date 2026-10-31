# Phase 4 — source-bridged chronology query closure (2026-10-31)

**Status:** Bounded engineering retrieval improvement to PRELIMINARY_RESEARCH
chronology. No new historical claim, invented absolute date, owner canon
decision, deck proposal, or knowledge-foundation certification.

## Reproduced gap on main at workflow v2.77

The original `relative_chronology_2026-10-30.json` has 56 events and 177
ordered pairs. The separate `source_event_sequences_2026-10-30.json` has 74
events, 57 direct strict edges, 180 ordered pairs, and seven independently
verified SAME_EVENT links back to the original ledger. Each link requires
the same Wizards page and quoted event evidence on both sides.

The normal `compare_across_datasets` returned early for pairs in the same
ledger. That meant eight comparisons in the original B/C packs returned
UNKNOWN although the source-local sequence already supplied a fully cited
BEFORE path through one or more of those exact event-identity bridges.

The single primary source used for these comparisons is Wizards' historical
retrospective, [The Known Mutliverse](https://magic.wizards.com/en/news/feature/known-mutliverse-2008-03-19)
(March 19, 2008). Its Phyrexia section explicitly places the original
planeswalker's death before Dyfed brings Yawgmoth, then describes Yawgmoth's
rule, Thran conflict and portal closure, with the later Rath invasion plan.
These are **source-stated relations**, not publication-date inference.

## Eight newly answerable event pairs

| Left query event | Right query event | Relation returned |
| --- | --- | --- |
| B:phyrexia_creator_dies | B:phyrexia_portal_closed | BEFORE |
| B:phyrexia_creator_dies | B:thran_defeated | BEFORE |
| B:phyrexia_creator_dies | C:rath_overlay | BEFORE |
| B:phyrexia_portal_closed | B:yawgmoth_to_phyrexia | AFTER |
| B:phyrexia_portal_closed | C:rath_overlay | BEFORE |
| B:thran_defeated | B:yawgmoth_to_phyrexia | AFTER |
| B:thran_defeated | C:rath_overlay | BEFORE |
| B:yawgmoth_to_phyrexia | C:rath_overlay | BEFORE |

The labels above describe the **direction of each ordered query**, not a
claim that every row's left-hand event occurs before the right-hand one.
No quoted edge, event node or stored transitive-closure artifact was added.
The gains are eight *retrieval results* over previously saved evidence.

## Guardrails

- Already supported results from the original ledger or source-local strand
  are returned unchanged, including non-strict overlap and SAME_EVENT.
- An UNKNOWN pair can receive a new answer only if the composite proof
  traverses a cited SAME_EVENT bridge **and** a strict BEFORE chain. Proof
  steps remain individually inspectable, with Wizards URLs and limitations.
- Cross-ledger provenance is flagged even when both endpoints have legacy
  IDs; previously this flag depended only on endpoint membership.
- Unsupported orders involving Yawgmoth's destruction versus the decimation
  of Old Phyrexia, the Elder Dragon War versus Rath, or unrelated planes
  remain UNKNOWN. No cross-plane universal chronology is claimed.
- The original `query_lore_chronology.py --check` acyclicity and stored
  closure checks remain mandatory. No new claim packs or card data changed.

## Verification

```shell
python3 scripts/query_lore_chronology.py --check
python3 -m unittest tests.test_chronology_same_ledger_bridges \
  tests.test_mv_ask_chronology tests.test_relative_chronology -q
```

Locally, the chronology source check passed; the focused suite had 24 tests
pass, with one existing cache-dependent test skipped because its untracked
story cache is absent in the shallow checkout. The new five-test guard is
registered in the graph/temporal GitHub workflow. Full exact-head CI remains
the release gate for merging, and this does not close the full Phase 4 or
Phase 8 certification checklist.

The foundation remains **89/137 checklist items checked, 48 open,
NOT_RELEASE_READY**. All 62 approved Grixis decks and the three parked,
unapproved lore-deck pilots remain untouched.
