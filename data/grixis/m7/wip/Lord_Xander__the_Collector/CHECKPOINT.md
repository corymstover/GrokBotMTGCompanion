# WIP CHECKPOINT — Deck 30 Lord_Xander__the_Collector (index 29) — RESEARCH_IN_PROGRESS, NOT owner approved

Checkpoint written: 2026-10-23 17:05 CDT (box clock).

- Baseline: canonical corymstover/grixis-commander-encyclopediaGPT main 9b26aa28fc7e16f6652aaec292b4edf84e20db71, refinement/decklists/Lord_Xander_the_Collector_Approved_2026-10-14.txt, blob 025aa284, introduced by 214fd50 (2026-10-14 21:45 CDT); raw SHA-256 92cdc2f9c1a3583ccf6a311679db66bef825dac2902761859e929f268b6b4787 == overrides approved_list_sha256 == registry recorded/raw (registry source commit 1836b97) == tracker row 29 final_list_hash; byte copy vendored.
- Shared infra copied byte-identically from PR 677 head e117a5ca (checker SHA-256 2962a640…3bf3b).
- KNOWN BLOCKER (investigated): data/grixis/m6/owner_pass_c_substitute/Lord_Xander__the_Collector/seal.json (commit bca97b98, 2026-10-21) records stage_a.md sha256 89a78d80…a879d1, but the committed stage_a.md bytes (only commit 6ebb511e; git blob e97d35fe, which the same seal records as git_blob_sha) hash to 826f0770…cd0322. The seal's git blob binding matches; its SHA-256 field does not match any committed version (no newline/CRLF variant reproduces it). stage_a.json matches its sealed SHA. Checker validate_pass_c raises "Stage A source diverged from separately sealed byte commitment". Not edited.
- Next: commander Oracle, live Scryfall, EDHREC, Spellbook, candidate judgments, bounded tests.
