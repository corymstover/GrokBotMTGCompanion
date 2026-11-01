# Foundation certification sprint v2.98 — source refresh and honest owner-scope closure

**Date:** 2026-11-01 · **Decision:** NOT_RELEASE_READY. The engineering checklist advances **98 → 102 / 137**; 35 are still open, including all source-sensitive foundation/CI gates and the ten parked post-foundation deckbuilding tasks. No claim of total lore completeness or final foundation certification follows from this batch.

## Four owner decisions actually closed

Cory explicitly authorized owner-side decisions and approvals in the November 1 instruction. The bounded decisions and their supporting evidence are preserved verbatim in `data/release/owner_scope_decisions_2026-11-01.json`:

| ID | Accepted scope | What is *not* asserted |
| --- | --- | --- |
| K131 | All 5,362 priority enrichment entries are accounted for, including an explicit exception list. | The 2,626 no-story-lore entries (1,304 Universes Beyond) and 341 uncertain name matches are not resolved canon. |
| K134 | The previously CI-reviewed qualified, dated Phase 1B set atlas meets the defined functional catalog/export scope. | No guarantee of globally verified street dates, cross-snapshot metadata parity or in-world timing; the optional 555-source record queue remains. |
| K129 | The finite first milestone is the **knowledge foundation**, checked against its seven written criteria. | Not comprehensive all-time lore, a gameplay simulator or the post-foundation deck engine. |
| K130 | New stories, card printings, rules and Commander policy are ongoing maintenance. | Future maintenance is not already performed or certified. |

These policy and finite-scope approvals do not accept Pack A's unresolved genealogy, make a preliminary pack definitive, cure missing official sources, or satisfy exact-release-commit CI.

## November 1 Scryfall source replay

Using **all six original compressed Scryfall JSONL files** (the exact October 30 baseline plus the new November 1 Oracle Cards, Default Cards and Rulings), `scripts/audit_release_bulk_delta.py` independently verifies every file's SHA-256, compressed bytes and JSONL record count against its published manifest; compares existing source objects by stable Oracle UUID or printing UUID; compares the exact multiset of all published rulings; audits specified fields; and checks the current Oracle fields against every indexed Oracle UUID. The script is read-only, deterministic offline and test-covered. The raw compressed files are preserved outside git and may be recovered by their manifest URLs and hashes.

| Dataset | November 1 records | November 1 versus Oct. 30 |
| --- | ---: | --- |
| Oracle cards | 39,287 | 0 added/removed stable Oracle IDs; **7** existing records change tracked fields: 1 Oracle text, 1 color identity, 4 keyword lists, 1 layout. |
| Default/printing cards | 120,019 | 0 added/removed printing IDs; **49** records change tracked fields, including 45 release dates; the other material categories are enumerated in the report. |
| Rulings | 79,706 | **Identical record multiset**, no changed/added/deleted ruling. |
| Committed card index | 33,894 indexed Oracle UUIDs | No missing IDs and zero type-line, color-identity, Commander legality or game-changer differences. There are 66 special name-variant labels differing from current Scryfall names and 5,393 additional Scryfall Oracle objects not in the curated index; neither is represented as newly reconciled content. |

The full source-level report is `data/scryfall_snapshots/oct30_to_nov01_release_delta_2026-11-01.json`; the new pinned manifest is `data/scryfall_snapshots/snap-20261101-live-20261101.manifest.json`. The report separately checks **581 previously cited exact-art printing IDs** from Pack A and official-story image evidence; **none is missing or changed in source art-identity fields**. This does not repeat the visual inspection. **A newer live bulk after November 1 requires another exact-source replay before any later release.** This run does not silently refresh shard content, reinterpret source-grade story assertions, or change protected historical snapshot locks.

## Newer official Wizards rules bulletin

The official [October 19, 2026 Mystery Booster Commander Edition Update Bulletin](https://magic.wizards.com/en/news/announcements/mystery-booster-commander-edition-update-bulletin) announces a new pregame rulebreaker rule **903.5e**, meld-card rules moved to a new **713**, meld cards no longer counted as double-faced cards, and other rule reorganizations/Oracle wording changes. The official [rules hub](https://magic.wizards.com/en/rules) still linked to the **September 25** full TXT when directly checked November 1. Wizards explicitly says the bulletin describes *planned* changes and the published full rules take precedence in discrepancies. Consequently, no invented October comprehensive-rules hash or verbatim 903.5e excerpt is committed.

`data/rules/cr_20261019_bulletin_review.json` records this source discrepancy. Two code safeguards:

1. The Commander eligibility and inclusion route detects `Rulebreaker —` on a designated commander. Where a rulebreaker exception might supersede ordinary color-identity or basic-land restrictions, it now returns `allowed: null` and `determination: REQUIRES_RULEBREAKER_REVIEW`, **not** a false rejection or an unverified permission. Unrelated definitive failures (for example archived Commander `not_legal` status) still cause rejection. All answers cite the real September TXT and disclose the later bulletin.
2. Published-ruling and keyword Q&A now visibly flag `NEWER_OFFICIAL_RULES_BULLETIN_NOT_IN_CITED_EXCERPT`. The weekly official-source monitor also seeks *new Wizards update-bulletin links*, because only watching the rules-hub PDF can miss a newly announced rule change. A listing-page absence still cannot prove that no new update exists.

## Verification and remaining release blockers

- Focused rulebreaker, latest-bulk replay, source monitor, stale-data and release-readiness tests run locally. The regenerated November 1 coverage recount passes **15/15 representative questions** over **626 accounted-for inventoried source pages** (576 cited; 50 reviewed without new claims) and the preserved **1,263 claim graph**. Generate exact blocker reports with `scripts/certification_dry_run.py`; regenerate the entire 137-item triage with `scripts/audit_full_checklist.py` and the Progress Tracker checkpoint with `scripts/update_multiverse_progress_tracker.py`.
- The seven foundation criteria remain **2 MET, 3 PARTIAL, 2 EXTERNAL**. The partial gates are source-reviewed connected lore Packs A/B/C, current rules/lookup coverage, and bounded chronology/history/Q&A owner acceptance. The two EXTERNAL gates require protected Grixis verification and complete exact-release-commit CI.
- The 35 open checklist items include **ten deliberately parked Phase 6 tasks**; do not turn that deferral into a false foundation-certification requirement. The other source gaps and ongoing monitoring tasks are listed in the generated full triage.
- No approved Grixis deck, Grixis snapshot lock, canon claim pack, or parked pilot draft is edited by this sprint. A protected-path diff must be empty and GitHub workflows must pass on the proposed commit before merge.

**Next:** Obtain the actual updated Comprehensive Rules TXT from Wizards and independently hash/rebuild relevant excerpts; review disputed Pack A identities and partial chronology only against admissible primary sources; deepen broad histories; repeat Scryfall release-time verification; execute exact-head CI and approve foundation only when all seven finite gate checks genuinely pass. Do not mark unverified questions as solved.
