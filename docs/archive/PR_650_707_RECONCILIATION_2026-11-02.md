# Reconciliation of residual Grixis PRs #650 and #707 — 2026-11-02

Cory requested reconciliation and safe closure of old open PRs. **Neither
research branch was silently merged into current `main`**: both target the
older `chatgpt-cycle76-m6-refinement` development base, contain unmerged
material, and differ from the owner's current authoritative source records.
The exact head commits and branches below **must be retained** during any
GitHub branch cleanup unless every unique artifact is independently restored,
verified by checksum, and the owner authorizes its disposal. Closing a PR
only dismisses its review queue; it does **not** delete its branch or negate
its historical owner decisions.

## PR #650 — Abaddon Rev3 owner receipt and lock test

- PR: https://github.com/corymstover/GrokBotMTGCompanion/pull/650
- Head branch: `chatgpt-abaddon-rev3-owner-receipt-canonical-verified-20261023`
- **Exact head SHA:** `6ca2e52ea2e9a8570691324af019486e37043859`
- Original target: `chatgpt-cycle76-m6-refinement` (historical M6/M7 branch; **not main**)
- Owner-approved Rev3 raw 100-card SHA-256: `5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24`
- Separate **canonical Grixis repository** approval PR #48 was already merged;
  this companion PR is a downstream receipt/testing synchronization proposal.
- Compare: 5 commits ahead, 179 behind historical base; 5 changed files.
- **Unmerged unique content:** immutable-looking owner receipt
  `data/grixis/m7/owner_approvals/Abaddon_the_Despoiler_rev3_20261023.json`
  and `tests/test_m7_abaddon_rev3_owner_lock.py`, plus relevant CI and M7
  research state. The canonical approval is **not undone by closing this PR**.

| Diff status | Path | Added / removed lines |
|---|---|---:|
| modified | `.github/workflows/m7-decisive-optimization.yml` | +3/-0 |
| added | `data/grixis/m7/owner_approvals/Abaddon_the_Despoiler_rev3_20261023.json` | +106/-0 |
| modified | `data/grixis/m7/research_challengers/Abaddon_the_Despoiler_current_continuation_20261022.json` | +29/-25 |
| modified | `data/grixis/milestone_m6_m7_subtracker.json` | +5/-5 |
| added | `tests/test_m7_abaddon_rev3_owner_lock.py` | +80/-0 |

## PR #707 — Lord of Tresserhorn owner-approved candidate + M6 transfer evidence

- PR: https://github.com/corymstover/GrokBotMTGCompanion/pull/707
- Head branch: `chatgpt-m7-lord-approved-case-transfer-20261025`
- **Exact head SHA:** `0d4c51d2c5756a0c6207fe4b5d47d4e8afdd0920`
- Original target: `chatgpt-cycle76-m6-refinement` (historical M6/M7 branch; **not main**)
- Owner-approved **candidate** raw 100-card SHA-256:
  `fd09cb267660206b834257e5c455259985b0e53316743835f679760b11200f85`
- Original research includes distinct source-bound 14-case M6 P0/P1 transfer
  fixture, 2026-10-23 Oracle/rules and EDHREC/Spellbook snapshots, test
  harnesses, candidate/source lists and reviewed rejection history.
- Compare: 10 commits ahead, 174 behind historical base; 36 changed files;
  **31,014 added lines** per original GitHub PR inventory. Importing the
  snapshot bulk directly into `main` would expand the protected knowledge-base
  scope and would **not** establish canonical Grixis owner-lock authority.
- The PR's own description states a separate canonical encyclopedia approval
  PR would be needed; **do not infer that it happened** from this companion PR.
- **Retention required:** original head branch, complete original 14-case
  fixture and all exact source snapshots. Preserve before any future deletion.

| Diff status | Path | Added / removed lines |
|---|---|---:|
| added | `.github/workflows/m7-lord-of-tresserhorn.yml` | +51/-0 |
| added | `.github/workflows/m7-lord-owner-case-transfer.yml` | +34/-0 |
| added | `data/grixis/m6/certification_preflight/Lord_of_Tresserhorn_M6_I_local_best_20261023.md` | +126/-0 |
| added | `data/grixis/m6/certification_preflight/Lord_of_Tresserhorn_M6_J_mana_20261023.md` | +45/-0 |
| added | `data/grixis/m6/certification_preflight/Lord_of_Tresserhorn_M6_J_red_team_20261023.md` | +53/-0 |
| added | `data/grixis/m6/ij/certificates/lord-of-tresserhorn-m7.json` | +43/-0 |
| added | `data/grixis/m6/ij/revision_bundles/lord-of-tresserhorn-m7.json` | +233/-0 |
| added | `data/grixis/m6/ij/tested_pools/Lord_of_Tresserhorn_M7_tested_configurations_20261023.json` | +126/-0 |
| added | `data/grixis/m6/oracle_snapshots/Lord_of_Tresserhorn_M7_Scryfall_20261023.json` | +5429/-0 |
| added | `data/grixis/m6/rules_snapshots/Lord_of_Tresserhorn_M7_20261023.md` | +60/-0 |
| added | `data/grixis/m7/baseline_sources/Lord_of_Tresserhorn_approved_source_2026-10-14.txt` | +98/-0 |
| added | `data/grixis/m7/candidate_lists/Lord_of_Tresserhorn.txt` | +98/-0 |
| added | `data/grixis/m7/decision_reviews/Lord_of_Tresserhorn.json` | +819/-0 |
| added | `data/grixis/m7/decision_reviews/Lord_of_Tresserhorn_chatgpt_adversarial_review_packet.md` | +128/-0 |
| added | `data/grixis/m7/research_challengers/Lord_of_Tresserhorn_CommanderSpellbook_20261023.json` | +5165/-0 |
| added | `data/grixis/m7/research_challengers/Lord_of_Tresserhorn_EDHREC_discovery_20261023.json` | +7234/-0 |
| added | `data/grixis/m7/research_challengers/Lord_of_Tresserhorn_PassC_plus_DistortionStrike_minus_RoguesPassage_20261023.txt` | +98/-0 |
| added | `data/grixis/m7/research_challengers/Lord_of_Tresserhorn_PassC_plus_FierceGuardianship_minus_NightscapeFamiliar_20261023.txt` | +98/-0 |
| added | `data/grixis/m7/research_challengers/Lord_of_Tresserhorn_PassC_plus_SoulsFire_minus_SheoldredsEdict_over_candidate_Skullclamp_20261023.txt` | +98/-0 |
| added | `data/grixis/m7/research_challengers/Lord_of_Tresserhorn_Scryfall_live_20261023.json` | +6034/-0 |
| added | `data/grixis/m7/research_challengers/Lord_of_Tresserhorn_alt_A_four_swaps_keep_SheoldredsEdict_20261023.txt` | +98/-0 |
| added | `data/grixis/m7/research_challengers/Lord_of_Tresserhorn_alt_B_Skullclamp_minus_MuddleTheMixture_keep_SheoldredsEdict_20261023.txt` | +98/-0 |
| added | `data/grixis/m7/research_challengers/Lord_of_Tresserhorn_alt_C_Skullclamp_minus_NightscapeFamiliar_20261023.txt` | +98/-0 |
| added | `data/grixis/m7/research_challengers/Lord_of_Tresserhorn_bounded_measured_tests_20261023.json` | +2736/-0 |
| added | `data/grixis/m7/research_challengers/Lord_of_Tresserhorn_rejected_original_tentative_plan_20261023.txt` | +98/-0 |
| added | `data/grixis/m7/research_challengers/Lord_of_Tresserhorn_rejected_plus_AqueousForm_minus_MuddleTheMixture_20261023.txt` | +98/-0 |
| added | `data/grixis/m7/research_challengers/Lord_of_Tresserhorn_rejected_prior_draft_TemurBattleRage_minus_PainForAll_owner_cut_20261023.txt` | +98/-0 |
| modified | `data/grixis/schemas/m7_decisive_optimization.schema.json` | +44/-0 |
| modified | `scripts/grixis_m6_bundle_check.py` | +342/-4 |
| modified | `scripts/grixis_m7_decision_gate.py` | +47/-1 |
| added | `tests/test_m6_lord_of_tresserhorn_m7_approved_case_transfer.py` | +187/-0 |
| added | `tests/test_m6_lord_of_tresserhorn_m7_ij.py` | +257/-0 |
| added | `tests/test_m6_lord_of_tresserhorn_m7_mechanics.py` | +234/-0 |
| added | `tests/test_m6_pass_c_corpus_stabilization.py` | +247/-0 |
| modified | `tests/test_m7_decisive_optimization_gate.py` | +69/-0 |
| added | `tests/test_m7_lord_of_tresserhorn_candidate.py` | +193/-0 |

## Disposition and deletion rules

1. Record exact head SHAs and this complete per-file inventory on `main`.
2. Close the two superseded **review queues as unmerged archives**. Do not
   rewrite PR title/body as though code or decks were merged or discarded.
3. **Preserve both named branches** as recovery anchors: their unique files
   remain retrievable by exact SHA at the original PR pages and via GitHub's
   compare/file APIs. Neither branch is safe to prune solely because its PR
   is closed. The same holds for `chatgpt-cycle76-m6-refinement` (historical
   M6/M7 source and base) and current/protected heads.
4. For every other old branch, first inventory `name → exact head SHA →
   ancestors of main → distinct tree/content → open PR/owner decision links`.
   Delete only branches whose source commits are reachable from `main` or
   whose unique evidence has been independently preserved and documented.
   Never force-move refs, delete protected/current branches, or rely on branch
   age/count alone. Keep an exact pre-deletion manifest and recovery SHAs.
5. **GitHub branch deletion has not been executed by this document.** A
   separate authorized deletion interface and per-branch safety verification
   are required. No deck cards or canonical approvals were changed.

