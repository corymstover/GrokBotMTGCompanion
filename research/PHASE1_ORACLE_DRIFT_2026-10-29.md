# Phase 1: Oracle drift between committed card shards and Scryfall snapshot 2026-10-29

Status: read-only evidence, tests passing. No shard, enrichment, lore, deck, approval or Grixis file was changed.

Tool: `scripts/oracle_drift_report.py`. Report: `data/card_db/oracle_drift_2026-10-29.json`.

The input was the verified snapshot `oracle-cards-20261029090202.jsonl.gz` (snap-20261029; its manifest is kept on the box, not in the repo, because of size).

## Result
| Check (33,894 index rows / 33,894 shard sections parsed) | Changes |
|---|---|
| Oracle text, all faces, flavor excluded, whitespace/dash/apostrophe normalized | **0** |
| Name (ignoring the index's "(SET #)" disambiguation suffix) | 0 |
| Type line | 0 |
| Color identity | 0 |
| Commander legality | 0 |
| Game Changer | 0 |
| Index cards missing from the snapshot | 0 |

The snapshot has **5,270 oracle_ids not in the index**:
- 4,080 are non-gameplay layouts (art series, tokens, emblems, planes, schemes, vanguards, front cards).
- 885 are digital-only (Alchemy and similar).
- **305 are new paper gameplay cards:**
  - 190 from `trk` (expansion, releases 2026-11-13)
  - 112 from `trc` (Commander, releases 2026-11-13)
  - 2 from `slc` (2026-11-02)
  - 1 from `pf26`

## What this changes
- The 2026-10-15 shards match the 2026-10-29 Oracle data for every indexed card, so `mv_ask.py card` now reports these cards as VERIFIED with `ORACLE_RECONCILED_WITH_SNAPSHOT_2026-10-29`. It does that only when the committed report has the same snapshot date and does not list the card as changed. Otherwise the answer stays QUALIFIED with `STALE_ORACLE_VS_CURRENT_SNAPSHOT`.
- Next card-database step: a guarded addition of the 305 upcoming paper cards once they release. They are previews until 2026-11-13; their legality is `not_legal` in the snapshot.

## Limitations
- Formatting-only Oracle edits would count as changes, but none were found.
- Prices and EDHREC ranks are not compared.
- A listed change would be a refresh candidate, not proof of errata.
