# Phase 3 — Cited Multiverse claim graph (v1)

**Status:** an engineering layer, verified by CI. It covers the Pack A, A2, A3 and A4 research and the unapproved Pilot 1 proposal evidence. It is **not** a full graph of all Magic lore.

## What existed before
`data/lore_graph.json` (`lore-evidence-graph/v1`, built by `scripts/build_lore_graph.py`) holds 422 nodes and 1,062 edges, all wiki cross-references with the `contextual_pointer` tier. It is useful for navigation, but it records no directional, dated or cited relationship, and no canon status. The new layer **extends** that graph rather than replacing it. Graph entities whose names match a curated character, plane or dossier entry exactly get a `see_also_curated_entry` edge (navigation only).

## Model (`multiverse-claim-graph/v1`)
- **Stable typed IDs:**
  - `character:ugin`, `plane:tarkir`, `event:tarkir_duel`, `artifact:ugins_nexus`, `place:…`, `continuity:echoverse`
  - `claim:A001`, `source:chronicle_twins`
  - `card:crux_of_fate`, carrying its Oracle ID and exact story-art printing IDs
  - `deck:…` for proposals
- **Claims are reified.** Every claim node has a canon status, a stage, a limitation, `cited_by` edges from its sources and `asserts` edges to its subject and objects. A direct `subject —predicate→ object` edge repeats the claim ID, the status and the source IDs.
- **Canon statuses:** `CANON_CONFIRMED`, `CANON_IMPLIED`, `CANON_DISPUTED`, `OPEN_QUESTION`, `ALTERNATE_CONTINUITY` and `HYPOTHETICAL`. Any other grade fails the build.
- **Sources** are classed as `WIZARDS_OFFICIAL` (from the URL host) or `NON_WIZARDS_LABELLED`. In CI, every edge that carries a claim may cite only official Wizards sources.
- **Free text stays visible.** An object that names no entity becomes a `literal:` node instead of being merged into an entity.
- **Deck-proposal edges** (`proposed_in`) and curated bridges have no canon status. The query tool reports them as `NAVIGATION_ONLY`.

## Commands
```bash
python3 scripts/build_multiverse_graph.py          # rebuild data/multiverse_graph/multiverse_graph.json
python3 scripts/build_multiverse_graph.py --check  # CI: stale copy or validation problem fails
python3 scripts/query_multiverse_graph.py neighbors ugin --status CANON_CONFIRMED
python3 scripts/query_multiverse_graph.py path piru ugin      # shortest path through cited claims only
python3 scripts/query_multiverse_graph.py card "Crux of Fate"
python3 scripts/query_multiverse_graph.py status CANON_DISPUTED
```

## Adding a pack
Write the pack in the existing claim-pack schema (`source_register`, `entities`, `claims`, plus optional `card_anchors` or `card_art_context`). Add its path to `data/multiverse_graph/manifest.json`, then rebuild. All entities are registered before any claims, so a claim can name an entity that another pack defines.

## Validation (build-time plus `tests/test_multiverse_graph.py`)
The build fails on any of these:
- an unknown grade
- a claim with no source, or a source that is not registered
- an entity typed inconsistently across packs
- a conflicting attribute
- a broken edge endpoint
- a duplicate edge
- an uncited claim
- deck evidence whose status is not unapproved

Mutation tests confirm that each of these failures is detected.
