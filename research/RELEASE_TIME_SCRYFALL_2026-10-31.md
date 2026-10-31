# Release-time Scryfall evidence — October 31, 2026

The official bulk API reported newer October 30 archives than the Companion's historical October 29 source. All three new **Oracle Cards, Default Cards and Rulings** JSONL gzip downloads were preserved outside Git. The independent capture verified each file's actual bytes, SHA-256, parsed record count and official Scryfall updated timestamp; the metadata is pinned in `data/scryfall_snapshots/snap-20261030-live-20261031.manifest.json`.

| Content | October 29 records | October 30 records | Differences from October 29 |
| --- | ---: | ---: | --- |
| Oracle identities | 39,164 | 39,287 | 123 added, zero removed; one existing type-line change |
| Individual printings | 119,701 | 120,019 | 318 added, zero removed; 100 release-date and four image-status changes |
| Published rulings | 79,706 | 79,706 | No added, removed or edited rulings |

The sole existing Oracle type-line change is to **Culber and Stamets, Star-Crossed**, which is outside the Companion's currently indexed identity set. Among prior printings, **zero** `illustration_id` or credited-artist changes were detected. A `released_at` update is a publisher metadata change and is **not independently a first-party product street-release date**; an `image_status` change is **not** a newly reviewed art depiction.

Separately, running the existing card-index reconciliation against the latest Oracle and Rulings bulk found **zero differences** in all indexed Oracle text, names, type lines, color identities, Commander legalities, game-changer flags or per-card rulings counts. No previously indexed Oracle identity is missing. The **5,393 Oracle identities not in the current card index** are a scope/inventory gap relative to its older build—not 5,393 additions since October 29, and not automatic deck-eligible cards. All 5,362 historically prioritized enrichments remain present.

Reproducible commands, using two immutable source directories containing the gzipped files named in their manifests:

```bash
python3 scripts/scryfall_snapshot.py verify --dir /path/to/current-snapshot
python3 scripts/audit_release_snapshot_delta.py --baseline-dir /path/to/oct29-files --current-dir /path/to/current-snapshot
python3 scripts/audit_release_snapshot_delta.py --check --baseline-dir /path/to/oct29-files --current-dir /path/to/current-snapshot
python3 scripts/oracle_drift_report.py --oracle /path/to/current-snapshot/oracle-cards-20261030210201.jsonl.gz
python3 scripts/multiverse_snapshot_reconcile.py --snapshot-dir /path/to/current-snapshot --output /tmp/current-reconcile.json
```

CI can run the portable delta `--check` against immutable manifests and stored evidence without redownloading 100+ MB. The full optional replay rechecks six source hashes and all content differences. Historical October 15–16 Grixis locks, October 28 printing shards and October 29 release assets are unchanged; no card shard, approved deck or pilot is modified.

**Limit:** this closes the October 31 *freshness evidence pass*, not the complete foundation's lookup/rules acceptance gate. Unmodelled interactions, qualified Atlas source gaps, owner decisions, and a possible **later** Scryfall update remain outside this check. Re-run on the actual final release candidate before automatic owner acceptance can become effective.
