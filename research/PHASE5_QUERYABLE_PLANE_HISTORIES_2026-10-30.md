# Phase 5 — Queryable official-source plane-history dossiers

**Status: PRELIMINARY / PARTIAL RESEARCH. Not owner-approved or certified.**

The repository had a numerical plane-history priority list but no source-backed,
human-readable lookup for each registered plane. This milestone builds a
reproducible dossier from *existing, individually graded claim-to-plane edges*.

## What a reader gets

- 33 graph-registered planes, each with cited facts, the exact claim ID and grade,
  claim summary/limitation, subject–relation–object, optional era label, any
  explicitly quoted in-world date and a direct Wizards source URL.
- A direct-claim incidence count, **not a full census of every plane in Magic**.
  Some claims mention planes in their summary but have no direct Plane edge and
  are deliberately not fabricated into new relationships by this query.
- No claims are upgraded. A `CANON_DISPUTED` claim stays disputed; an `OPEN_QUESTION`
  remains open. Era labels are displayed as *descriptive labels*, never AR dates
  or proven temporal orderings. Official publication date is not in-world time.
- A query for an unregistered plane returns **NOT_FOUND IN THIS GRAPH**, never a
  claim that the plane doesn't exist in Magic.

## Run / verify

```bash
python3 scripts/query_plane_history.py Dominaria
python3 scripts/query_plane_history.py Phyrexia --json
python3 scripts/query_plane_history.py 'New Phyrexia'
python3 scripts/build_plane_history_dossiers.py --check
python3 -m unittest discover -s tests -p 'test_plane_history_dossiers.py' -q
```

**Source-of-truth inputs:** `data/multiverse_graph/multiverse_graph.json`,
itself generated from the source-graded claim-pack manifest. **Generated result:**
`data/lore_research/plane_history_dossiers_2026-10-30.json` (content checksum,
source graph checksum and exact `--check` replay).

## Next genuinely open Phase 5 research

1. Expand thin plane dossiers with more directly evidenced events, factions,
   inhabitants, outcomes and chronological relationships using official Wizards
   stories and dated quotes.
2. Review whether a plane mentioned only in a claim's *summary* genuinely
   needs another **separately justified** Plane edge; do not infer by substring.
3. Reconcile Old Phyrexia's fate and Yawgmoth's defeat only when official sources
   establish any missing order or owner's disputed canon decisions are made.
4. Build a true cross-plane chronology independently of these unordered lists.

The old Grixis deck collection and approval registry were not touched.
