# WIP CHECKPOINT — Deck #14 Don_Andres__the_Renegade (RESEARCH_IN_PROGRESS, NOT owner-approved)

- Branch: grokbot-deck14-don-andres-the-renegade-m7-20261023 (base chatgpt-cycle76-m6-refinement b6b40ac8)
- Baseline: canonical corymstover/grixis-commander-encyclopediaGPT main 9b26aa28fc7e16f6652aaec292b4edf84e20db71, path
  refinement/decklists/Don_Andres_the_Renegade_Approved_2026-10-14.txt (git blob 1d20d488; frozen by canonical commit 255c328),
  raw SHA-256 a6022fddd295d7c671690fbce5e25dc6fed47ca7fa77bf1d8a86ebadb2d927bb == state/current_deck_overrides.json
  approved_list_sha256 == tracker final_list_hash (tracker index 13) == registry recorded_sha256 (registry import commit 1836b97; recorded_matches_raw true).
  100 physical cards / 99 rows (Island x2 the only repeat). Vendored byte-exact copy committed. Archidekt export
  exports/grixis-archidekt/don-andres-the-renegade.txt is logically identical (sorted order, "1 " vs "1x ").
- Owner direction (10-14 approval, 13-card delta): removed the self-recursion package (Buried Alive, Living Death, Victimize),
  symmetrical/slow value (Cunning Rhetoric, Share the Spoils, The Ruinous Powers, Revel in Riches), Gonti Lord of Luxury, Zara,
  and four tapped/slow/check lands (Crumbling Necropolis, Drowned Catacomb, Haunted Ridge, Stormcarved Coast). Do not re-add without flag.
- Pass C (#14, owner-equivalent, NOT independent): KEEP; requested measured tests: Mob Rule vs Insurrection (6/7/8 mana, mixed tables, Don survival); Bribery vs named theft cut (opponent density, turns-to-return).
- Shared infra copied byte-identically from PR #661 head 8bcc4c54 (bundle checker SHA 2962a640...).
- Completed: baseline_provenance. Next: research (Scryfall live, EDHREC, Spellbook), Pass C bounded tests, candidate judgments.

## Checkpoint 2 — research (2026-10-23 08:18 CDT)
- Live Scryfall /cards/collection: 99 baseline names + 155 evaluated names; frozen snap-20261016 oracle_id/text differences: zero (Mirror Universe Intrusion absent from frozen cache and not commander-legal; excluded). Baseline Game Changers (live): Ancient Tomb, Cyclonic Rift, Fierce Guardianship, Opposition Agent, Vampiric Tutor (5).
- Commander Spellbook: baseline 0 included combos / 23 almost; candidate 0 / 19.
- Staged candidate (5 swaps): +Gríma, Saruman's Footman / -Professional Face-Breaker; +Fallen Shinobi / -Seize the Spotlight; +Treachery / -Blasphemous Act; +Gloomlake Verge / -Shipwreck Marsh; +Blazemire Verge / -Smoldering Marsh. Candidate raw sha256 05e13311bac44898f2c299dca5a6b071133fb30a1c021d496e7de84e56049773.
- Six alternatives staged under research_challengers (Pass C Mob Rule / Bribery variants, keep-Blasphemous-Act, Dazzling Sphinx, Nightveil Specter).
- Next: bounded Pass C tests, decision review, snapshots, certificate/bundle, workflow.

## Checkpoint 3 — Pass C bounded tests + snapshots (2026-10-23 08:22 CDT)
- Oracle snapshot (249 legal U/B/R names) and rules snapshot committed. Baseline logical hash recomputed == registry baseline_hash lh1:012d9c8c…; candidate lh1:d387b103….
- Mechanics test (16 tests, passing): Pass C (a) Mob Rule vs Insurrection grid 2 spells x 5 tables x 6/7/8 mana x Don present/absent: Insurrection uncastable below 8; at 8 it steals >= Mob Rule everywhere; Mob Rule keeps 115/144 of Insurrection's stolen power (equal on 2/5 tables); Don flips Mob Rule's best mode on one table. (b) Bribery vs Amalgam/Jhoira over densities 0/4/8/15/25: Bribery <= 1 permanent ever (0 at density 0); Amalgam 3 per round from the first opponent upkeep; Jhoira 1 on ETB + 1 per surviving attack. Tapped-Treasure chain check; exact colour access (candidate -0.34 pt with Verges' second colour off, identical when on).
- Next: tested pool, decision review, I/J memos, adversarial packet, certificate/bundle, workflow, ij/candidate tests.

## Checkpoint 4 — pool + decision review (2026-10-23 08:30 CDT, commit cfad225d)
- Tested pool (9 configurations), decision review (30 material candidates, 18 weak slots; gate passes, READY_FOR_EXACT_OWNER_APPROVAL_NOT_YET_APPROVED), mechanics test now 17 methods (adds lands-only RR/RRR red availability by 13 cards).

## Checkpoint 5 — memos, packet, certificate/bundle, workflow, tests (2026-10-23 08:37 CDT)
- I local-best / J mana / J red-team memos; ChatGPT adversarial review packet; M7 certificate + revision bundle (data/grixis/m6/ij/...don-andres-the-renegade-m7.json); workflow m7-don-andres-the-renegade.yml (step names "Deck 14", no '#'); ij test (8) + candidate test (8).
- Focused: 137 passed (candidate, mechanics, ij, Pass C corpus); gate --check --check-sources passes; bundle checker --check unchanged vs base (2/62 valid).
- Next: remove WIP, full suite vs b6b40ac8, PR body, ready, exact-head CI.
