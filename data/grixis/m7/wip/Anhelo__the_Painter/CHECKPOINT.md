# WIP CHECKPOINT — Deck #4 Anhelo, the Painter (tracker index 3) — INCOMPLETE, NOT CERTIFICATION

Status: RESEARCH_IN_PROGRESS. Not owner approved. Not reviewed by ChatGPT. Nothing here changes canonical.

## Completed stages
1. Baseline/provenance: canonical corymstover/grixis-commander-encyclopediaGPT@90e00446
   `refinement/decklists/Anhelo_the_Painter_Approval_Ready_2026-10-13.txt`, raw SHA-256
   8d5f8a9bd4fcdcd164aab63150c14dc69a814a4d9fd764876de3214d3adf9972 (vendored at
   data/grixis/m7/baseline_sources/Anhelo_the_Painter_approved_source_2026-10-13.txt).
   Historical registry/override digest d19d94b8a96fb27a760c7b7d9181221f74bd61642d1d1dd7644fc1c59c09839e is NOT reproducible
   from those bytes (registry recorded_matches_raw:false). Closeout note "31 lands" is a row count; physical lands = 34.
2. Shared gate infra copied byte-identical from PR #651 head 447d9d69 (schema, gate, bundle_check, gate tests) so the
   provenance exception can be validated; PR #651 itself untouched.
3. 99-slot audit (in progress notes): 34 lands + 9 rocks = 43 static mana sources for avg nonland MV 2.83 / 3-MV commander -> excess;
   recursive power-2+ creature fodder is under-supplied (instant/sorcery-made fodder consumes the turn's one casualty slot).
4. Discovery: EDHREC (6318 decks) + one live Scryfall /cards/collection batch (115 names, all legal, Grixis, zero diffs vs frozen 2026-10-16 cache).

## Tentative package (WIP, subject to change)
+Skyclave Shade -Fellwar Stone; +Sinister Concierge -Talisman of Indulgence; +Dogged Detective -Exotic Orchard;
+Tenacious Underdog -Talisman of Dominance; +Bedevil -Feed the Swarm.

## Staged (WIP)
Candidate + 4 alternative full-100 lists and oracle snapshot staged; baseline logical hash equals registry lh1:627cae66.

## Next step
Stage candidate + alternative 100s, write decision packet, tests, I/J, memos, focused CI workflow.
