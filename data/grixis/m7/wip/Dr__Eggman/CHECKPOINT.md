# WIP CHECKPOINT — Deck #15 Dr__Eggman (RESEARCH_IN_PROGRESS, NOT owner-approved)

- Branch: grokbot-deck15-dr-eggman-m7-20261023 (base chatgpt-cycle76-m6-refinement b6b40ac8)
- Baseline: canonical corymstover/grixis-commander-encyclopediaGPT main 9b26aa28fc7e16f6652aaec292b4edf84e20db71, path
  refinement/decklists/Dr_Eggman_Approved_2026-10-14.txt (git blob 86119caf; frozen by canonical commit 8883de3),
  raw SHA-256 ef34986253f71043e10c852b5f9f3ce79594fdfc1086b105f6744c3f639199c3 == state/current_deck_overrides.json
  approved_list_sha256 == tracker (index 14) == registry recorded_sha256 (registry import commit 1836b97; recorded_matches_raw true).
  100 physical cards / 97 rows (Island x2, Mountain x2, Swamp x2). Vendored byte-exact copy committed. Archidekt export
  exports/grixis-archidekt/dr-eggman.txt is logically identical (sorted order, "1 " vs "1x ").
- Pass C (#15, owner-equivalent, NOT independent): NEEDS TESTING, KEEP; requested bounded tests: +Goblin Welder/-Liliana's Caress;
  31 vs 32/33 lands payable {2}{U}{B}{R} timing.
- Shared infra copied byte-identically from PR #662 head bc4b9d53 (bundle checker SHA 2962a640...).
- Completed: baseline_provenance. Next: research (Scryfall live, EDHREC, Spellbook), Pass C bounded tests, candidate judgments.

## Checkpoint 2026-10-23 08:49 CDT — research snapshots
- Live Scryfall (discovery/legality only; frozen cache untouched): commander Dr. Eggman legal, released 2025-07-14 (sld Secret Lair), CI UBR, no exception.
  Baseline Game Changers (live): Ancient Tomb, Cyclonic Rift, Fierce Guardianship (3). Off-ranking type search Construct/Robot/Vehicle UBR: 458 hits.
- EDHREC general/upgraded/optimized frozen; Commander Spellbook: baseline 0 included / 36 almost; candidate 0 included / 30 almost.
- Provisional core five: +Possession Engine/-Blasphemous Act, +Skysovereign/-Cybermen Squadron, +Interceptor Mechan/-Cryptothrall,
  +Midnight Crusader Shuttle/-Unwinding Clock, +Behemoth of Vault 0/-Foundry Inspector. Five alternatives staged (Welder/Caress, Tergrid/Caress, 32 lands, keep Act, Su-Chi).
- Next: mechanics tests (exact land DP, villainous-choice grid, Welder vs Caress), decision review, I/J, bundle, workflow, tests.

## Checkpoint 2026-10-23 08:55 CDT — candidate revised, Oracle/rules snapshots, mechanics test
- Re-read the owner's 2026-10-14 closeout: Damocles Base (a Vehicle villainous choice) was rejected for combat dependency and permissive
  choice outcomes; Midnight Crusader Shuttle shares that critique, so it is demoted to a staged alternative and Su-Chi Cave Guard
  (8/8 vigilance ward 4 Construct) takes the slot over Unwinding Clock. Foundry Inspector and Blasphemous Act were named by the owner as
  retained infrastructure/interaction; both cuts are flagged and a keep-Inspector and a keep-Act alternative are staged.
- Preferred five: +Possession Engine/-Blasphemous Act, +Skysovereign, Consul Flagship/-Cybermen Squadron, +Interceptor Mechan/-Cryptothrall,
  +Su-Chi Cave Guard/-Unwinding Clock, +Behemoth of Vault 0/-Foundry Inspector. Candidate raw SHA-256 85bcd5a2...; payloads 28 -> 31.
- Six staged alternatives; Spellbook re-queried for the revised candidate (0 included in both lists).
- tests/test_m6_dr_eggman_m7_mechanics.py: 12 finite cases pass locally (exact land DP 31/32/33, 64-cell villainous grid, 192-cell Welder vs Caress grid, trigger multipliers max 9).
- Next: decision review, I/J memos, tested pool, certificate, bundle, workflow, candidate/IJ tests.
