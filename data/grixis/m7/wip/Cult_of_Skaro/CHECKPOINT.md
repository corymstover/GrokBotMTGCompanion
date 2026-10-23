# WIP CHECKPOINT — Deck #11 Cult_of_Skaro (RESEARCH_IN_PROGRESS, NOT owner-approved)

- Branch: grokbot-deck11-cult-of-skaro-m7-20261023 (base chatgpt-cycle76-m6-refinement b6b40ac8)
- Baseline: canonical corymstover/grixis-commander-encyclopediaGPT main 9b26aa28fc7e16f6652aaec292b4edf84e20db71, path
  refinement/decklists/Cult_of_Skaro_Approval_Candidate_2026-10-14.txt (git blob bcb22f01), raw SHA-256
  4c221e5be0439338823ef621cd91706da8d405129cf6f5a41de36a83b875ef3b == state/current_deck_overrides.json approved_list_sha256
  == registry recorded_sha256 (registry import commit 1836b97). 100 physical cards / 94 rows (Island x3, Mountain x3, Swamp x3).
  Vendored byte-exact copy committed.
- Discrepancy (documented, not repaired): tracker CSV note cites "Revised clean-list SHA-256 cc2f7a54..." and says "Only change:
  Skorpekh Lord -> Ashad"; cc2f7a54 is the 2026-10-13 Current_Cycle_Baseline / Proposed_Final file. The approved 2026-10-14 list
  4c221e5b differs from it by 11 further swaps (e.g. Arcane Denial -> Mana Drain); the same CSV row's final_list_hash and the
  overrides record 4c221e5b. Archidekt 2026-10-15 export differs only by the missing [Commander] marker.
- Shared infra copied byte-identically from PR #658 head 7953eef5 (bundle checker SHA 2962a640...).
- Completed: baseline_provenance. Next: research (Scryfall live, EDHREC, Spellbook), Pass C bounded measured test, candidate judgments.
