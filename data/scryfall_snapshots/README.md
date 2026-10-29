# MTG Multiverse Scryfall snapshots

## Two independent authorities

- `data/grixis/dev_snapshot_lock.json` remains an immutable **historical Grixis
  development record** (`snap-20261016`). It names the three expected old bulk
  files and hashes. Nothing in this process replaces them or changes approved
  Grixis decks. Historical validation still requires the actual matching files.
- New **MTG Multiverse Companion** research opts into
  `MTG_SCRYFALL_MODE=multiverse`. This selects a separate `.cache/multiverse/`
  directory and does not impose the 2026-10-16 Grixis lock on lore/card research.

Do not use the old `SCRYFALL_BIRTHDAY_SNAPSHOT=1` escape hatch for modern
research. It is a legacy exception, not an archival or versioning strategy.

## Creating durable new inputs

Run `scripts/scryfall_snapshot.py capture --dir OUTPUT --snapshot-id snap-YYYYMMDD-UNIQUE`
to download three current compressed Scryfall JSONL bulk files (Oracle Cards,
Default Cards, Rulings), validate their JSONL contents, and generate a manifest
with sizes, record counts, version timestamps, exact URLs, and SHA-256 hashes.

The resulting directory is an **incomplete backup until it is independently
published and download-verified**. The GitHub Actions workflow
`multiverse-scryfall-snapshot.yml` performs these steps and publishes the three
`.jsonl.gz` files *plus* `manifest.json` as release attachments under a unique,
non-overwriting per-run tag. It then re-downloads the attachments and runs:

```
python3 scripts/scryfall_snapshot.py verify --dir DOWNLOADED_RELEASE_DIRECTORY
```

The repository commits the capture code and this policy, **not** large bulk
files, which would unnecessarily inflate Git history. Releases are historical
inputs, not authorities for deck revisions or automatic card-lore promotion.

## Using archived inputs without downloading newer ones

Download the release's four assets into an isolated directory, verify them,
then set `MTG_SCRYFALL_MODE=multiverse`, `MTG_MULTIVERSE_CACHE` to that directory,
and `SCRYFALL_OFFLINE=1` when running ingestion or card-enrichment research.

Without offline mode, the current-data path is allowed to fetch newer Scryfall
versions into its separate cache, **without removing earlier modern downloads**.
Record the specific snapshot ID in any reproducible study. Before accepting
new evidence, explicitly compare changed fields against the committed index and
enrichment data. Never mass-overwrite manually reviewed lore, historical Grixis
approvals, or canonical 62-deck lists as a side effect of refreshing the input.

`scripts/multiverse_snapshot_reconcile.py` compares the verified new input with
the existing index, enrichment inventory, printing-lore source manifest, and
ruling counts without modifying any of them. The companion Actions workflow
uploads a bounded JSON difference report for review; its findings do not grant
authority to change historical decks or automatically promote lore links.

## October 16 historical recovery

The old cache was gitignored. Bot cycle 66.3 documented temporary restoration
paths `/tmp/c64-cache-partial-backup` and `/tmp/c66-cache-refresh-backup`, but
neither path exists in the current development workspace. Historical release
assets inspected to date contain no Scryfall bulk files. Exact recovery remains
open unless a candidate matches all three recorded SHA-256 hashes; a newer
snapshot is **not** claimed to reproduce the original bytes.
