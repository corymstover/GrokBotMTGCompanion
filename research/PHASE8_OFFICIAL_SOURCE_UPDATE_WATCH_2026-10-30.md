# Phase 8 — Read-only official MTG source-change watch

Status: **engineering tested, preliminary maintenance facility**. This is not
full certification and never updates a card/deck/approval record automatically.

## What now runs

- Weekly, Monday **15:23 UTC**, or manually via GitHub Actions:
  `.github/workflows/multiverse-update-watch.yml`.
- The script checks the live Wizards *Magic Story* listing for URLs absent
  from the committed story index/extra-source list. This checks **one listing
  page, not all fiction ever published**, and reports candidates only.
- It compares Scryfall's currently advertised `default_cards`, `oracle_cards`
  and `rulings` bulk-data timestamps with the **exact pinned** active October 29
  snapshot. It does not download bulk or change historical snapshot locks.
- It checks the Wizards rules hub for new official `MagicCompRules` PDF links.
  It also records the Wizards Commander format page as source metadata, but
  **does not infer a ban/rules change from a changing HTTP ETag** (the ETag was
  unstable over repeated observations on October 30).
- It uploads `mtg-source-change-review-signals` as a 30-day GitHub Actions
  artifact, with no automatic pushes, issues, PRs, lore changes or approvals.
- Network failures are explicitly `SOURCE_UNAVAILABLE`, not falsely marked
  "no updates." Offline unit tests cover parsing, false-alarm behavior and
  snapshot timestamp logic.

## First read-only probe, October 30, 2026

- The currently visible official listing had **five story links**, all already
  present in the existing indexed inventory. That says nothing about omitted
  articles on other pages or future releases.
- All three Scryfall bulk families advertised an October 30 refresh, newer
  than the pinned October 29 manifest. This is **expected new data available**,
  not a signal to overwrite October 29 or the older Grixis snapshot.
- The Wizards rules hub still linked the observed
  `MagicCompRules 20260925.pdf` document, with no new PDF candidate.
- The Commander format page ETag changed between two reads without any
  independent evidence that the Commander format changed. Therefore ETags
  are informational only, never an actionable ban-change alert.

## Run and interpret

```bash
python3 scripts/monitor_multiverse_updates.py --validate
python3 -m unittest discover -s tests -p test_multiverse_update_monitor.py -q
python3 scripts/monitor_multiverse_updates.py --live --output /tmp/mtg-update-signals.json
```

`--live` requires network access; tests and `--validate` do not. Reports are
ephemeral unless explicitly reviewed and committed as a separately qualified
source milestone. Never auto-approve lore packs, update Grixis decks, rewrite
historical Scryfall hashes, or treat a new story URL as established canon facts.

## Open work

Expand coverage to Wizards announcement/release-notes archives, verified
Commander ban and bracket announcements, and a broader official story
discovery index. Verify changed rules PDFs and Oracle/rulings records before
changing the companion's accepted live rules. No owner approval/certification
is implied by this maintenance tool.
