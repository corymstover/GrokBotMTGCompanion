# Phase 5 — curated on-plane story context (2026-10-30)

**Status:** PRELIMINARY_RESEARCH_NOT_OWNER_APPROVED. This release is a
**discovery and retrieval improvement**, not 53 new researched claims or
in-universe chronological edges. Phase 6 lore decks remain parked.

## What was recovered

Before this change, `scripts/query_plane_history.py` and
`scripts/mv_ask.py ask` displayed only source-backed claim relations with an
edge **directly incident on the plane node**. Significant already-audited
official story material was therefore hidden from queries for the plane.

The new `data/lore_research/plane_context_claims_spec_2026-10-30.json` is a
hand-curated, explicitly non-exhaustive list of source-grounded claims from
four official story packs. Regeneration retains the claim's *original*
grade, statement, exact quoted evidence, source URL, relations and limitations.
No graph edge is added, and on-plane context is never reported as a direct
claim about the plane itself.

| Plane | Existing distinct direct claims | Newly discoverable **existing** contextual claims | Official scope |
| --- | ---: | ---: | --- |
| Eldraine | 3 | 10 | The 2019 plane guide: Kenrith family, High Throne and court leaders. |
| Arcavios | 2 | 16 | Strixhaven's on-campus Oriq, founders and student story, with a separate official *Arcavios → Strixhaven* geographical bridge. |
| New Capenna | 2 | 15 | Streets of New Capenna: Halo, families, Crescendo and archived Phyrexian invasion accounts. |
| Lorwyn–Shadowmoor | 3 | 12 | Lorwyn Eclipsed's local residents and events, carefully excluding scenes on Arcavios. |
| **Total context** | **10** | **53** | **Four bounded packs; no new claims minted.** |

This is not an increase to the repository's **1,206 source-graded graph
claims**. Direct plane edges remain **183** across **33 registered planes**;
there are still **16** plane dossiers below five distinct direct claims.
The new *context* coverage number is deliberately separate: **53 contextual
claims across four planes**.

## Geographic and epistemic safeguards

- Eldraine, New Capenna and Lorwyn–Shadowmoor have their Plane entity
  explicitly declared in their original Wizards-sourced packs.
- Arcavios uses the official Wizards design article
  [*The Rabiah Scale, Part 3*](https://magic.wizards.com/en/news/making-magic/the-rabiah-scale-part-3),
  which explicitly identifies Strixhaven University as a location on
  Arcavios. Its precise location quote is hash-pinned and **live checked**.
- Exclusions are intentional: New Capenna's `SN015` takes place on
  Dominaria; Lorwyn's `EC006` and `EC008` describe Arcavios scenes; `EC014`
  is a later souvenir exchange elsewhere, and `EC013` is a local folktale;
  three Strixhaven claims lack enough on-plane historical context for this
  layer. The direct Eldraine `EL011` and Lorwyn `EC005`/`EC016` remain in the
  original direct section rather than being counted twice.
- Source grades such as CANON_CONFIRMED apply to the **underlying claim**,
  not to an invented exact GPS location for every character or incident.
  The contextual association is visibly labelled
  `CURATED_ON_PLANE_STORY_CONTEXT_NOT_DIRECT_GRAPH_EDGE`.
- Era labels, release dates and scene publication order are not converted
  into historical BEFORE/AFTER proof. All histories remain QUALIFIED and
  incomplete, with no universal chronology certification.

## Reproducibility and queries

```bash
python3 scripts/build_plane_history_dossiers.py
python3 scripts/build_plane_history_dossiers.py --check
python3 scripts/build_plane_history_dossiers.py --live
python3 -m unittest discover -s tests -p 'test_plane_context_claims.py' -q
python3 scripts/query_plane_history.py Eldraine
python3 scripts/query_plane_history.py 'New Capenna' --json
python3 scripts/mv_ask.py ask 'What is the history of Arcavios?'
```

The builder validates: each original claim's SHA-backed original Wizards
quote reference, graph grade/wording and official source URL; membership in
its already registered claim pack; and no duplicate direct/contextual
claims within a plane. Existing pack-level quotation audits passed against
their committed hashes here; the original story-page cache was absent, so
those 53 inherited excerpts were **not independently rechecked live** in
this change. The newly added Arcavios geographical bridge **was** checked
live against Wizards. Eight focused tests guard scope, exclusions, stability and
Q&A output. CI replays the builder and regression suite.

**Open:** Actual comprehensive histories for all 33 current graph Plane
nodes, the unregistered planes beyond them, historical chronology across
sources, major conflicts/retcons and final knowledge-foundation review.
Nothing here modifies the protected 62 Grixis decks or the three parked
lore-deck pilots.
