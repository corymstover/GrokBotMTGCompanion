# Phase 8 restart and source-integrity plan

Status: **incomplete, paused after GrokBot cycle 36**. This file documents a safe recovery path; it does not retroactively claim the missing cards have been enriched.

## Recorded baseline (2026-10-15)

From `ROADMAP.md`, `Progress Tracker.md` and the generated `Card Enrichment.md`:

| Area | Historical baseline | Not yet resolved |
|---|---:|---:|
| Priority enrichment pool | 3,397 / 5,361 (63.4%) | 1,964 |
| Legendary creatures | 1,822 / 3,786 | 1,964 |
| Unverified character name matches | 341 | Requires source review |
| Synergy-batch cards showing “no lore entry yet” | 1,220 | Evidence research needed |

These totals are **not** automatically current as new Magic sets release. Run `python3 scripts/phase8_status.py` against the committed artifact for reproducible coverage. The pre-existing per-card data is the authoritative record, not a marketing dashboard. GitHub issues [#100](https://github.com/corymstover/GrokBotMTGCompanion/issues/100), [#101](https://github.com/corymstover/GrokBotMTGCompanion/issues/101), and [#103](https://github.com/corymstover/GrokBotMTGCompanion/issues/103) remain open.

## Safe operating procedure

1. **Never run the historical all-in-one rebuild against approved deck artifacts.** The old `scripts/rebuild_enrichment.sh` mixed card lore with Grixis refinement and broad cross-reference regeneration that can edit `grixis/decks/`. The revised script defaults to a read-only `--plan`, uses `--check` for consistency, and requires explicit `--apply` on a clean, non-default feature branch. It only regenerates card enrichment, card shards and EDH Packages.
2. **Recover source caches first.** The original repo's scratch recovery path `/workspace/salvage-c36/` was not part of the Git repository, and third-party caches may be absent in fresh environments. Regenerate Scryfall, EDHREC and Commander Spellbook snapshots through the approved scripts/normal credentials, preserving acquisition dates and licensing limits. Never substitute guessed values for an unavailable source.
3. **Keep approvals frozen.** No write to `grixis/`, `data/grixis/`, `exports/grixis-archidekt/`, the 62 canonical decklists, approval hashes or owner-lock records. A separate authorization and its existing certification gates are required for any deck change.
4. **Rebuild in bounded, versioned batches.** Recover the remaining 1,964 legendary creatures in incremental rank intervals/checkpoints, with a rollback-friendly PR per slice. Source code currently has `RANK36 = 9647` and `UNRANKED36 = False` as the historical stopping point; changing those numbers is a substantive new batch requiring caches and exact-head CI, not an automatic status flip.
5. **Prioritize story fidelity within the batch.** Before marking a card lore-enriched, use `lore_query.py deep`, `variants`, and `gaps` to consider alternate printing flavor, named associates and important historical events. Cite specific editions and direct official sources. A name match or broad Phyrexian label never upgrades itself to "depicts" without proof.
6. **Audit unresolved links separately.** Revisit the 341 uncertain matches and the cards lacking lore links with official articles, publication context, and actual card artwork. Keep direct depiction, explicit mention, and interpretive thematic connections in separate tiers.
7. **Review diffs and CI before merge.** Run `python3 -m unittest discover -s scripts -p 'test_lore_deep_research.py'`, `python3 -m unittest discover -s scripts -p 'test_phase8_safety.py'`, `scripts/rebuild_enrichment.sh --check`, and existing repository CI. Reject unexplained changes outside the enrichment outputs; never bypass protected GitHub checks.

## Read-only commands

```bash
python3 scripts/phase8_status.py --json
bash scripts/rebuild_enrichment.sh --plan
bash scripts/rebuild_enrichment.sh --check
python3 scripts/lore_query.py --human variants 'Corrupt'
python3 scripts/lore_query.py --human deep 'Yawgmoth' --limit 50
```

`--apply` deliberately refuses to run on `main`, a dirty worktree, or missing offline caches. That refusal is a safety feature—not permission to reconstruct missing evidence from memory.

## Publication status

This is a continuation of GrokBot's Phase 8, **not** a new completion claim. Historical Bot cycles, milestone links, and prior tags are retained for provenance. The README dashboard should clearly distinguish that legacy work from the current state and link here instead of describing the paused project as actively running hourly.
