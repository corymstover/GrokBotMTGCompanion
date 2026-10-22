# Abaddon — M6 technical I/J verified; exact M7 owner approval pending

**Current owner-decision status (2026-10-22):** The complete proposed Abaddon 100-card M7 replacement is technically ready to present. This is **not** owner approval or formal M6.10 milestone acceptance. The canonical approved and locked list remains untouched (raw SHA-256 `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`).

## Exact decision offered to Cory

- Adds: **Grinning Ignus**, **Chaos Warp**
- Cuts: **Rakdos, Lord of Riots**, **Inevitable Betrayal**
- Complete staged 100: `data/grixis/m7/candidate_lists/Abaddon_the_Despoiler.txt`
- Exact raw SHA-256: `1fabe1251a7868838365144bf0cb1ee903d394ed90ac146b2dd9cdd45683b7dd`
- 34 lands; Power Bracket **4 — Optimized**; Archidekt tags: **Cascade**, **Exile Cast**, **40K Chaos**
- Existing canonical list remains approved/locked with no mutations. Abaddon has no project-specific legality exception.

## Verified executable evidence

- M6.6 and M6.7: per-deck COMPLETE with scoped deterministic adjudication (PR #569). Global gates remain PARTIAL across 62 decks.
- Mandatory targeted mechanics: **104 executable named P0** and **14 P1** test cases, plus a source-bound classification of the 70 remaining names. PR #566 exact-head SUCCESS: [Actions #39819134570](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/39819134570). PR #567 exact-head SUCCESS: [Actions #39819765932](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/39819765932).
- Permanent source-bound **97-name current Scryfall Oracle snapshot**: `data/grixis/m6/oracle_snapshots/Abaddon_the_Despoiler_Scryfall_20261022.json` (PR #571); no invented rules proof or official legality exception.
- **M6 I**: `data/grixis/m6/ij/certificates/abaddon-the-despoiler.json`: strictly validated PASS *only* for the selected full 100 within the five explicitly evaluated full 100-card configurations, not a claim of global optimum, simulated win rate, or owner acceptance.
- **M6 J**: `data/grixis/m6/bundles/abaddon-the-despoiler.json`: finalized seven-input hash-bound reproducibility bundle with Pass A/B evidence, correctly labeled *non-independent* GPT-6 owner-waived Pass C, physical test results, Oracle snapshot, authoritative source hashes and chosen candidate.
- Strict I semantic and J bundle checks, adversarial tests: [PR #573 exact-head Actions #39824160094](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/39824160094) **SUCCESS**.
- Schema-valid candidate recommendation remains distinct from final owner authorization: `data/grixis/m7/decision_reviews/Abaddon_the_Despoiler.json`.

## Owner authority boundary

1. Cory alone may approve the **exact candidate** (and authorize canonical replacement after the SHA is reverified). No canonical approval is inferred from engineering CI.
2. M6.10 **formal certification / milestone acceptance remains owner-held**. M6.8 and M6.9 are per-deck adjudications, not 62/62 milestone completion. Never report formal M6 certification or global encyclopedia completion without the required separate acceptance and remaining-deck work.
3. If candidate is approved, preserve exact 100 and signed hashes in canonical workflow; move to the next commander in tracker order. If rejected, revise the staging list without touching canonical.

**Decision prompt for the complete owner deck presentation:** `This deck is complete. Do you approve it?`
