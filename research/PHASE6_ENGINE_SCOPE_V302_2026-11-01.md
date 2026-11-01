# v3.02 — Post-foundation Phase 6 bounded engine acceptance

**Checkpoint:** 2026-11-01. **Foundation:** the v3.00 seven-gate milestone was externally certified for its exact baseline. **Project:** 111/137 checked, **26 still open**. This is **not final whole-project certification**.

After Cory's repeated post-foundation completion request, the active engineering prerequisite is met. The three lore-first Commander proposals are still **UNAPPROVED**; existing protected Grixis deck and approval files were not edited. The four general Phase 6 engineering boxes now have independently replayable acceptance evidence:

| Checklist item | Bounded pass evidence | Deliberate boundary |
| --- | --- | --- |
| K106 graded lore-card retrieval | `scripts/lore_deck_candidates.py` retrieves 255 existing curator-graded nonbasic cards by theme/pilot, grade and name, including chosen printing/Oracle IDs, source and story reason; all four tiers are represented. | Grading is source-reviewed curation in three known proposal pools, not proof that all possible cards are automatically classifiable. |
| K109 optional set, era, debut restrictions | `scripts/lore_deck_restrictions.py` checks chosen edition set, **real-world** publication date/year range and all tied first-recorded English paper printings of the *same Oracle identity*. Three 100-card pilot specs cross-check against the Phase 1B frozen historical shards; unknown records fail closed. | “Era” means publication era. A card printed in a set associated with a story does **not** establish when that fictional event occurred. The October 28/29 snapshot is not live. |
| K111 Archidekt interchange | `scripts/audit_lore_pilot.py` verifies every import row/name/count against all three explicit 100-card decks, including commander first, plus exactly three distinct tag strings per proposal. A unit test detects a changed middle row. | Export is structurally importable; owner has not approved these decks or externally exercised Archidekt's live website. |
| K115 original Grixis protection | `scripts/audit_phase6_engine_scope.py` rechecks all five protected approval/state digests against the externally verified v3.00 SHA-pinned foundation certificate, and audit/build code targets the separate unapproved proposal directory. | The 62-deck Grixis registry/approval process remains outside Phase 6 modifications. Latest PR must also pass exact-head CI and a protected-path diff. |

The recorded build is `data/release/phase6_engine_scope_review_2026-11-01.json`. Its three pilot source/evidence SHA-256 hashes, grades, tag strings, offline snapshot references, fail-closed filter totals and protected-file digests are checked by dedicated CI. The new filter never falls back from a missing stable Oracle ID to a name guess. The direct depiction tier continues to require the existing exact-art/story-source checks; vanilla flavor matches are not promoted.

## Independent replay

```bash
python3 scripts/audit_lore_pilot.py
python3 scripts/audit_phase6_engine_scope.py --check
python3 -m unittest discover -s tests -p test_lore_deck_restrictions.py -v
python3 -m unittest discover -s tests -p test_phase6_engine_scope.py -v
python3 scripts/lore_deck_candidates.py --stem ugin_bolas_elder_dragon_duality --grade DIRECT_DEPICTION
python3 scripts/lore_deck_restrictions.py --stem original_primeval_dragons --set-code c21
python3 scripts/lore_deck_restrictions.py --stem original_primeval_dragons --first-printed-in lea
python3 scripts/lore_deck_restrictions.py --stem original_primeval_dragons --release-from 2000 --release-through 2010
```

Filter output uses `ALLOWED`, `EXCLUDED` and `UNKNOWN` per exact recorded printing. `--require-all` causes nonzero exit if any card is excluded; unknown printing evidence is always a nonzero exit. No command rewrites a deck or changes its approval.

## Still open / no unsupported certification

- **K107:** multi-commander color-identity and cited story-context comparison is not accepted.
- **K108:** objective strategy/playability, matchup and realistic-power review is unfinished.
- **K110:** all three frozen 100-card pilot audits pass their October 29 legality snapshot, but a fully current Commander rules/combo/bracket decision after the October 19 bulletin is not proven.
- **K112–K114:** the individual decks remain unapproved; a blanket push instruction is not treated as a specific, reviewable Commander list sign-off.
- **Other 20 open tasks:** first-party source gaps, broader lore coverage, chronology and retcon synthesis, current rules/edge cases, and continuing release/monitoring items are not silently completed by this engineering milestone.

To finish the remaining project, the unresolved source/current-rules facts and owner review must be obtained and the actual main branch CI verified. Foundation certification remains separate and valid.
