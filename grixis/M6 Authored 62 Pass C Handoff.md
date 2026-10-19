# M6 authored-review completion — Pass C review handoff

> **Owner-directed quality normalization (2026-10-19):** The existing 62/62 source-specific authored records are real but vary in depth. They are NOT yet the completed comprehensive one-deck-at-a-time authored reviews the owner now requires before handing GrokBot the final Pass C package. Follow [M6 Commander-First Single-Deck Review Standard](M6%20Commander-First%20Single-Deck%20Review%20Standard.md) and the separate `data/grixis/m6/single_deck_depth_tracker.json` (initially 0/62). Preserve the historical M6.4 62/62 narrow count and formal Pass C 0/62. Never silently equate these counts.

**Scope:** All 62 commanders in the canonical Grixis Commander Encyclopedia. This file is the handoff of **original author opinions** for separate independent Pass C, **not Pass C completion, full Phase B, M6 acceptance or permission to alter canonical decks**.

## Authorship inventory and primary evidence

- Original authored cycle112–116: five files, 3 unique decks each (15).
- Cycle128: `data/grixis/m6/author_reviews/cycle128_six_commander_authored_judgments_01.json` (6).
- Cycle129: `data/grixis/m6/author_reviews/cycle129_six_detailed_01.json` (6).
- Cycle130: `data/grixis/m6/author_reviews/cycle130_six_detailed_01.json` (6).
- Cycle131: `data/grixis/m6/author_reviews/cycle131_batch_a_01.json` through `cycle131_batch_e_01.json` (6, 6, 6, 6, 5) — 29 original author reviews.
- The original five paths are enumerated in `scripts/grixis_m6_cycle117_independent_review_readiness.py` under `SOURCES`.
- Recalculate authoritative exact deck IDs from `data/grixis/m6/phase_b_bounded/commander_first_readiness_62_01.json`, and independently verify with `python scripts/grixis_m6_cycle131_all_62_authored.py --build --check`. A successful CI receipt for the authored stage is **evidence of source/readiness checks only**.

**Totals:** 15 + 6 + 6 + 6 + 29 = **62 distinct deck-specific author judgments**. No author-created swaps, list changes or final certifications. M6.4 may be COMPLETE after CI and source-aware acceptance of this narrow gate. M6.5 independent Pass C and M6.6 complete effect-aware Phase B remain unfulfilled. The project remains 62/62 canonically approved and locked, but **0/62 formally M6-certified**.

## Correct Pass C process (keep genuinely independent)

1. Independently read `grixis/Grixis Authority Model.md` and `grixis/Grixis M6 I-J Contract.md`. Recover current GitHub authority, not this snapshot.
2. **Initial blind/reduced-exposure stage:** for each deck, obtain its unmodified canonical approved 100, commander blueprint, source candidate, current/frozen Oracle/rulings and M5/Phase B artifacts without reading the matching ChatGPT author conclusion. Record a reviewer-signed, source-sha-bound initial evaluation of the proposed add/cut, commander-first mechanics, positive counterexample, explicit cut cost, necessary real tests and recommendation.
3. Record reviewer identity, model/version, tool access, timestamps, separation/exposure before/after review, a commit/seal for initial independent findings, and any earlier exposure. Previous GrokBot advisory findings for **Gwendlyn Di Corci; Nicol Bolas, the Ravager; Mai and Zuko** were not fully blinded; they remain advisory until independently qualified. A model's earlier participation in building the blueprint/optimizer must be disclosed, not hidden.
4. **Reconciliation stage:** only after independent first-pass findings are sealed, read the authored review file. Compare positive/adverse mechanisms, Oracle facts, disagreement/agreeing positions, sample and source-paid tests. Critique EACH author HOLD and EACH promising unresolved proposal; do not accept the original verdict solely because it was source-verified.
5. Distinguish evidence classes: a verified deck/Oracle hash is not a multiplayer win-rate, a top candidate is not an established upgrade, and technical A/B artifact projections are not independent human executors. Record specific unresolved disagreements, access gates, opponent responses and necessary Phase B checks.
6. Produce attributable individual Pass C dispositions for **62/62** ONLY if reviewer independence and sufficient source verification genuinely meet contract; otherwise leave the decks explicitly `PASS_C_BLOCKED` with exact blocker and evidence. Formal M6 certification also requires effect-aware Phase B, judgment review, I zero-improvement tested-pool certificates, J reproducibility bundle and **Cory's formal milestone acceptance**.
7. Existing canonical lists and exception registry are READ-ONLY. Do not apply a candidate swap, change deck hashes, unlock anything, claim official legality of project-banned cards or accept a milestone.

## Known exception and provenance issues to keep separate

- `Cecily__Bjorna__Lutri`: Bjorna and Cecily are two commanders within the regular 100; **Lutri is a companion outside 100** by project exception. Lutri, Trade Secrets and Yawgmoth's Bargain are **not officially legal**. The project has expressly authorized them.
- `Tresserhorn_s_Lord__Returned`: future-release commander authorized by project before 2026-11-13; snapshot official status pending. `The_Madcap_Jester` has authorized future-release exceptions including Dragon's Smile.
- `Admiral_Brass__Unsinkable` and `Anhelo__the_Painter`: historical recorded approved raw-source SHA discrepancy. Preserve exact logical deck hash and recorded mismatch; do not silently claim rehashed original raw bytes.
- Frozen Scryfall archive `oracle-cards-20261016090200.jsonl.gz`, SHA256 `ea7abac9906633415553b585b32c4071c79d42ba23d7e3163a0c4e9c265a7483`. **This is a frozen snapshot, not automatic proof of live October 19 Commander legality**. Refresh current Oracle/rulings/legality before binding Pass C statements.

## What to return to the owner

A short, accurate Pass C gate ledger: `qualified_independent_reviewed/62`, named qualified or blocked decks, technical/strategic disagreements, official vs project exceptions, Phase B tests required and evidence links to exact SHA commits. Contact Cory only if a real authority decision is needed; do not ask for routine approval every batch.
