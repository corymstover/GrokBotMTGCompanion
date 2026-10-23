# WIP CHECKPOINT — Deck #13 Doctor_Doom__King_of_Latveria (RESEARCH_IN_PROGRESS, NOT owner-approved)

- Branch: grokbot-deck13-doctor-doom-king-of-latveria-m7-20261023 (base chatgpt-cycle76-m6-refinement b6b40ac8)
- Baseline: canonical corymstover/grixis-commander-encyclopediaGPT main 9b26aa28fc7e16f6652aaec292b4edf84e20db71, path
  refinement/decklists/Doctor_Doom_King_of_Latveria_Approved_2026-10-14.txt (git blob 324fdb30; frozen by canonical commit 6207ad5),
  raw SHA-256 c97bd448aa4b18d2f7ed15e5d67006ab320ed67ad3ed267e44150de472e1dc58 == state/current_deck_overrides.json
  approved_list_sha256 == tracker final_list_hash == registry recorded_sha256 (registry import commit 1836b97; recorded_matches_raw true).
  100 physical cards / 100 rows (all 1x; 38 lands). Vendored byte-exact copy committed. Archidekt export
  exports/grixis-archidekt/doctor-doom-king-of-latveria.txt is logically identical (sorted order, "1 " vs "1x ").
- Legality status: Doctor Doom, King of Latveria is an officially released commander (Marvel Super Heroes Commander, June 26 2026);
  NO future-release project exception applies (two-model reconciliation + formal Pass C #13 both say so; the Nov 13 2026
  activation plan covers only MBC cards such as The Madcap Jester / Tresserhorn's Lord). Live Scryfall check pending.
- Owner direction (10-14 approval): removed opponent-discard punishers (Liliana's Caress, Geth's Grimoire, Waste Not) and Dark Deal; do not re-add without flag.
- Shared infra copied byte-identically from PR #660 head bb3be7d3 (bundle checker SHA 2962a640...).
- Completed: baseline_provenance. Next: research (Scryfall live, EDHREC, Spellbook), Pass C bounded measured tests, candidate judgments.

## Checkpoint 2 (2026-10-23 07:47 CDT) — research + provisional candidate
- Live Scryfall (/cards/collection): 100 baseline + 135 evaluated names, all commander-legal; every list card within U/B/R.
- EDHREC general/upgraded/optimized discovery snapshot and Commander Spellbook lookup committed (1 included combo in baseline and candidate: Surly Badgersaur + Tectonic Reformation + Dakmor Salvage, library-bounded, not infinite).
- Provisional candidate (six swaps): +Lightning Axe -Feed the Swarm; +Magmakin Artillerist -Change of Fortune; +Red Ghost, Intangible Genius -Loki, the Deceiver; +Coastal Peak -Shipwreck Marsh; +Swiftfoot Boots -Fellwar Stone; +Mox Diamond -Talisman of Creativity.
- Staged alternatives: five keeping Talisman of Creativity; Withering Torment instead of Lightning Axe; Pass C Glint-Horn over Revenant; Glint-Horn instead of Artillerist; Ledger Shredder over Iron Monger; Putrid Imp over Demand Answers.
- Next: mechanics tests incl. bounded Pass C tests, oracle/rules snapshots, pool, decision review, memos, certificate, bundle, workflow.

## Checkpoint 3 (2026-10-23 07:51 CDT) — Pass C bounded tests; candidate revised by measured grid
- Bounded Pass C grid (5 fixed turn patterns x attack possible/not x removal before attacks): Glint-Horn Buccaneer >= Magmakin Artillerist in every cell (79 vs 64 total damage units; the extra is the hasty attack loot); Buccaneer > Green Goblin, Revenant on damage in 20/20 cells, Revenant > Buccaneer on cards in 4/20 (needs an attack, no haste; refill ceiling 8 cards on a wheel turn).
- Candidate revised: +Glint-Horn Buccaneer replaces +Magmakin Artillerist (cut still Change of Fortune). Revenant kept (Villain, the deck's remaining one-sided refill after cutting Change of Fortune). New candidate raw 21d5ebd66352c34e9f7b786e71d121e9e0101f2426049741c2ddb1d95d1ab3fb.
- Staged: six with Artillerist instead of Buccaneer; Pass C exact pairing +Buccaneer -Revenant keeping Change of Fortune; Pass C exact single swap on the baseline; five keeping Talisman; Withering Torment; Ledger Shredder; Putrid Imp.
- Dakmor loop: finite, library-bounded (40 life: 20 iterations / 38 library cards; with Buccaneer 14 / 26). Exact lands-only colour access: turn-4 Doom 0.5550 -> 0.5570 (on the play), RRR by turn 5 0.3895 -> 0.4248. Oscorp Industries counted UBR per Oracle.
- Commander Spellbook re-run on the revised candidate (1 included combo; 22 almost-included).
- Oracle + rules snapshots committed. Next: candidate/IJ tests, pool, decision review, memos, certificate, bundle, workflow.

## Checkpoint 4 (2026-10-23 08:05 CDT) — pool, decision review, tests, memos, certificate, bundle, workflow
- Tested pool (10 configurations), decision review (21 material candidates, 12 post-floor challenges, Power Bracket 4, tags Land Discard / Villains / Connive), candidate and IJ tests, I/J memos (local best, mana, red team), adversarial packet, zero-improvement certificate, M6 J revision bundle and focused workflow (step names without '#').
- Local: focused tests 195 passed; gate --check --check-sources PASS (Doom M7_STRUCTURALLY_DECISION_READY_NOT_OWNER_APPROVED); bundle checker --check PASS.
- Next: remove this WIP file (final content commit), full suite vs base b6b40ac8, PR body, ready for review, exact-head CI.
