# Phase 3 — Exact printing identities and official story-page artwork

**Status:** deterministic engineering verification, not canon/owner certification.
**As of:** 2026-10-30. **Source freeze:** committed Oct 29 Scryfall image-label
crosswalk, independently joined by UUID to the committed older Phase 1B card index.

## What this improves

Before this checkpoint, an art credit could attach to a `card:<name>` node,
which is not enough to establish a specific set and collector number. Now the
graph has a stable `CardRepresentation` node type keyed by exact printing ID:

- **560** unique `printing:<Scryfall UUID>` nodes, each with an Oracle UUID,
  printed name, set code, collector number, artist and recorded release date.
- **560** `has_printing` navigation edges from a card name to that exact print.
- **570** `art_file_used_on_official_page` edges from cited official Wizards
  image-page URLs to exact prints (some prints appear on multiple pages).
- **Five** additional official source-page nodes where the existing claim packs
  had not already registered that Wizards page.
- **Seven** `NO_PRINTING`/`NAME_MISMATCH` image labels left unresolved.
- **Zero** invented story-event depictions or new canon-status claims.

All 560 printing UUIDs agree with a separate committed historical card index
on exact printing UUID, Oracle ID, printed name, set and collector number. That
is a verified **bounded subset**, not a statement of whole-catalog parity
between historical Scryfall snapshots. Future/new cards remain outside this
index until independently verified. The graph retains its earlier 1,139 claims.

## How to use

```bash
python3 scripts/query_multiverse_graph.py printing blc 1
python3 scripts/query_multiverse_graph.py node printing:31e4b7a1-b377-49d2-a92e-4bcb0db35f16
python3 scripts/query_multiverse_graph.py card "Bello, Bard of the Brambles"
python3 scripts/build_multiverse_graph.py --check
python3 scripts/audit_entity_structures.py --check
python3 -m unittest discover -s tests -p test_printing_card_representations.py -q
```

The `printing blc 1` example identifies *Bello, Bard of the Brambles* (Commander
Bloomburrow BLC #1), then shows the official Wizards art-page citation.
The source's image label confirms which print's art file was used there. It
**does not** establish that the card depicts the event described in the page.

## Still open

1. Full lore mapping for the other historical printings; creating 119,000
   content-free graph nodes would not improve source-graded knowledge.
2. The seven unresolved label/printing joins, where a forced name match would
   risk identifying the wrong art.
3. Rich claim-level exact-printing connections only where direct Wizards text
   says a scene/event is depicted in a particular artwork.
4. Full October 28/29 source-bulk replay and global cross-snapshot printing-ID
   certification; the original older bulk bytes remain missing.
5. The remaining 16 orphan entity/source nodes and six *different-ID* alias
   candidates in the graph audit; neither is silently removed or merged.

No approved Grixis deck, approval registry, card hash or historical snapshot lock
was touched by this work.
