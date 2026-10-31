# October 31 independent Wizards story-cache recovery

This is a **reproducible source-integrity operation**, not a blanket canon certification. The primary-source inventories list exactly 660 official Wizards URLs: original story inventory in `data/primary_sources.csv`, cited non-story articles in `scripts/fetch_story_pages.py`, and supplemental source links in `data/story_extra_sources.csv`.

The previous environment's cache was lost, but its independently recorded **660-page metadata-only baseline** survives in `data/story_cache_provenance_2026-10-29.json`. That document records each URL's extraction SHA-256, title, word count and source kind. Do not rewrite the baseline from later content.

**Recovery results, October 31:** all **660/660 URLs strictly present**, **652** exact matches to the historical extract SHA-256, and **eight** extract drifts. Seven older articles gained ten extracted words each, with unchanged extracted titles. The eighth, the official Commander-format page, has unchanged word count but a different extract SHA-256. All eight remain explicitly marked `EXTRACT_DRIFT_REVIEW_ONLY`. Source integrity alone cannot tell whether an extra ten words are editorial changes, a site-template artifact or gameplay-relevant text; compare the actual pages before making content decisions.

With the pinned September 25, 2026 Wizards Comprehensive Rules text restored (`977,752` bytes; SHA-256 `8d860e451f20f38865b725b42d82feb714c725373dd8f3b32b8652b3eeb070ca`) and the original October Scryfall Default Cards/Rulings bulk available locally, `python3 scripts/lore_quotes.py --check` independently reverified **2,726 quotations across 27 documentation pages with zero problems**: 1,531 directly source-verified, 153 on another official page, 802 rules text, 209 card text, six preserved archival Grixis sources and 25 explicitly excepted labels/media references. This does **not** mean every claim in those documents is true or every canon conflict resolved.

`python3 scripts/check_citations.py --recheck` independently refreshed the citation registry. The subsequent offline audit found **920 distinct cited Wizards URLs** (862 in the official sitemap, ten live, 11 redirect, 37 archived), **776 distinct Comprehensive Rules citations**, and **zero problems**. The dated URL statuses are in `data/citations.json`; a live/archived URL alone does not guarantee the relevance or accuracy of a lore interpretation.

## Rebuild an independent source cache

```bash
python3 -m pip install -r requirements-story-cache.txt
python3 scripts/fetch_story_pages.py --delay 1.0
python3 scripts/fetch_story_pages.py --repair --delay 1.0
python3 scripts/story_cache_audit.py --strict
python3 scripts/replay_story_cache_provenance.py
python3 scripts/replay_story_cache_provenance.py --check
```

Use `--start-index` and `--end-index` (inclusive, one-based) for resumable, non-overlapping fetch batches. The integrity check reads the original URL inventory independently of the fetcher. It rejects missing, empty, suspiciously short, incorrectly attributed or corrupt pages and duplicate cache filenames. The SHA replay compares every recovered extraction to its earlier independently recorded hash. A changed HTML extract is placed in **`EXTRACT_DRIFT_REVIEW_ONLY`** and **must not automatically alter the lore graph, quotes, name matches, chronology or certification decisions**.

Source text lives under gitignored `.cache/story/`. **The source bodies are copyrighted and are not republished in Git.** The committed `data/story_cache_recovery_2026-10-31.json` contains hashes, URLs, word counts and drift diagnoses only. Portable CI checks that provenance and schema without needing to download the 660 original articles. When the full local cache is available, it additionally replays all 660 hashes.

The official text corpus is bounded by the inventoried URLs and the extraction method (`BeautifulSoup` + `lxml`). A complete cache is not complete *Magic* canon, a source URL is not proof of every implied event, and identical hashes do not resolve old conflicting interpretation. Foundation certification still depends on individually reviewed source-grade claims, release-gate tests and a current-source snapshot.
