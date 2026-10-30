# MTG Multiverse Companion: Update Process

Batch 9, 2026-10-30. This covers how to refresh the Companion when Scryfall data, format legality, the official Comprehensive Rules, or the official Magic Story archive change. Each step uses a script that already exists in `scripts/`; nothing here approves, locks or certifies anything.

## Ground rules

- **Never modify these:**
  - Grixis work (`grixis/`, `data/grixis/`)
  - `state/current_deck_overrides.json`
  - `data/lore_decks/approvals/`
  - any approved or locked list, hash or documented exception
  - the historical snapshot locks (`data/grixis/dev_snapshot_lock.json` and the Grixis cache)
- **Keep Companion data separate.** It uses its own modern snapshot. Before running enrichment or anchor scripts, export `MTG_SCRYFALL_MODE=multiverse SCRYFALL_OFFLINE=1`.
- **Evidence sources.** Evidence comes only from official Wizards story and rules pages and from Scryfall.
- **Keep these statuses distinct:** research, tests passing, merged, owner approved, certified. New lore decks stay UNAPPROVED proposals.

## 1. Scryfall card data (Oracle text, printings, legality)

1. **Capture a new snapshot.** Run `python3 scripts/scryfall_snapshot.py --dir <dir> --snapshot-id <id>`.
   - The bytes are not committed.
   - The `multiverse-scryfall-snapshot.yml` workflow publishes them as release assets alongside the manifest.
   - The tool never reads or changes the Grixis dev snapshot lock.
2. **Reconcile, read-only.** Run `python3 scripts/multiverse_snapshot_reconcile.py --snapshot-dir <dir> --output <report.json>`.
3. **Check Oracle drift, read-only.** Run `python3 scripts/oracle_drift_report.py --oracle <oracle-cards.json> --out <report>`. This lists text and index-field drift against the committed shards.
4. **Rebuild derived card data from the verified snapshot.** Use `scripts/build_legality.py`, `scripts/build_printings.py` and `scripts/rebuild_enrichment.sh`, then the Phase 1B atlas and export scripts (`audit_set_printing_atlas.py`, `export_phase1b_set_cards.py`).
5. **Run the checks.** Run `python3 scripts/validate_all.py` and the test suites (see step 5).

## 2. Official Comprehensive Rules

1. **Download the official CR TXT.** Get it from Wizards and record its effective date and sha256.
2. **Rebuild the verbatim excerpts.**
   - Run `python3 scripts/build_cr_keyword_excerpt.py`.
   - Rebuild the Commander excerpt under `data/rules/` from the same file.
   - Update the effective date that `commander_rules.py` and `rules_interactions.py` cite.
3. **Run the tests.** Run `tests/test_commander_rules.py` and `tests/test_rules_interactions.py`.

## 3. Official Magic Story archive

1. **Find new pages.** Run `python3 scripts/crawl_story_index.py` (the enumerate and fetch steps).
2. **Refresh the cache.** Run `python3 scripts/fetch_story_pages.py`; add `--only` or `--refresh` as needed. The cache is the gitignored `.cache/story/`.
3. **Audit the cache.** Run `python3 scripts/story_cache_audit.py --strict`. Only URLs, hashes and counts are committed, never article text.
4. **Rebuild the source index.** Run `python3 scripts/build_primary_sources.py`, which writes `data/primary_sources.csv`.
5. **Extract claims.**
   - Add or extend a generator in `scripts/claim_spec_sources/` (`from mv import spec`).
   - Every quote must be a verbatim substring, at least 25 characters long, of the cached page.
   - Every non-CONFIRMED claim needs a limitation.
   - A claim set in a past era or an original or rewritten timeline must say so in its summary or limitation. `mv_ask` uses that to keep it as era context.
6. **Mark pages that have no story claim.** Add them to the reviewed-no-claim register with an honest reason code.
7. **Rebuild.** Run `bash scripts/claim_spec_sources/rebuild.sh`. Never run two rebuilds at once.
   - The rebuild covers packs, graph, card anchors and the coverage inventory, then their `--check` modes.
   - `story_claim_pipeline.py build` appends new packs to the manifest itself. Do not add them by hand.

## 4. Recount and representative queries (after every published batch)

Run `python3 scripts/batch_recount.py`, or add `--json --out data/release/batch_recount_<date>.json` for a recorded copy. It does two things:

- Recounts pages cited, pages reviewed, claims and arcs from the committed inventory and graph.
- Re-asks a fixed set of representative questions through `mv_ask`. These cover siblings, killers, creators, mentors, faction leaders (with era context) and an unknown entity that must stay NOT_FOUND.

It exits 1 if any question fails. CI runs it in `phase7-companion-ask.yml`. Add a question here whenever a batch adds a capability; every expected answer must already be a cited claim edge.

## 5. Tests and release status

1. **Run the test suites.** Run `python3 -m unittest discover tests` and `cd scripts && python3 -m unittest discover -p "test_*.py"`.
2. **Refresh readiness.** Run `python3 scripts/release_readiness.py --out data/release/readiness_<date>.json`, then `python3 scripts/phase8_status.py`.
3. **Record the batch.** Add it to the handoff and to `MTG_MULTIVERSE_MASTER_WORKFLOW.md`, and bump the version.

## 6. Publishing

- **Pull requests.** Open small PRs. Merge only with a normal merge and `--match-head-commit`, once every check on the exact head is green, with no force-push and no admin bypass.
- **ChatGPT's branches.** Never touch `chatgpt-*` branches. Re-check `main` before merging.
- **Protected paths.** Confirm the protected-path diff is empty: `git diff --stat <base> origin/main -- grixis/ data/grixis/ state/current_deck_overrides.json data/lore_decks/approvals/`.
