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
