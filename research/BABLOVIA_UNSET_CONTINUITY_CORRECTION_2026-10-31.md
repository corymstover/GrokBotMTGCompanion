# Foundation v2.76 — Bablovia / *Unstable* continuity-grade correction

**Disposition:** verified correction of a historical classification error; **not** new mainline canon, owner acceptance, full-history completion or permission to build decks.

The original 2017 Wizards [*World Class*](https://magic.wizards.com/en/news/magic-story/world-class-2017-11-29) story records a Bablovian student's statement about the **Carta Scientia**. The quotation and official page registration remain unchanged. Wizards' [*Get It? Unstable Edition*](https://magic.wizards.com/en/news/making-magic/get-it-unstable-edition-2022-03-21) separately distinguishes the silver-border Un-set world from ordinary black-border Magic.

| Evidence object | Before | After |
| --- | --- | --- |
| Legacy claim `SSX020` | `CANON_CONFIRMED` (overbroad continuity classification) | `ALTERNATE_CONTINUITY` with an explicit student-narrator and setting limitation |
| Bablovia dossier direct claims | 4 alternate, 1 ordinary-canon | **5 alternate, 0 ordinary-canon** |
| Full graph (1,259 graded claims) | 6 alternate, 989 confirmed | **7 alternate, 988 confirmed** |
| Original Wizards text and claim identity | Registered quote on original `wc` page | **Unchanged**; 25/25 source quotes pass verbatim verification |

Rebuilt the committed claim spec from its authoring source, the source-quoted pack, self-hashed provenance audit, graph and manifests, 33-plane dossiers/priorities and the foundation Q&A acceptance packet. The replay used the same frozen **October 29 Scryfall Oracle and Default Cards** bulk as the source indexes, independently re-downloaded and SHA-256 verified (`0358af62...f3088adb` Oracle and `008434d5...5939595` Default Cards), not a newer release substituted into historical outputs. The full 660-page source cache remained available; the author's original quote is verbatim in it.

New `tests/test_bablovia_unset_continuity.py` gates the grade simultaneously in source spec, derived pack, claim graph and Bablovia dossier. `scripts/audit_p5_last_four_thin_planes.py --check` now requires all five Bablovia claims to be alternate continuity. The 49 representative Q&A checks remain a bounded regression sample, not broad historical completeness.

**Release implications:** all 62 approved decks and Phase 6 hold are unchanged. No checklist item is closed merely by fixing a misgraded claim. The other unresolved genealogy, plane coverage, product sources, QA and exact-release engineering gates remain open; the foundation remains **NOT_RELEASE_READY**, and Cory's conditional automatic owner acceptance is not yet effective.
