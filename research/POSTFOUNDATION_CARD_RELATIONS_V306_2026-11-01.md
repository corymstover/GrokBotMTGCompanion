# v3.06 — Evidence-bounded card links and temporal graph acceptance

**Repository build:** 16 active items remain, down from 18. The historical 137-box ledger is **115 checked / 22 unchecked** (six intentionally outside build: three post-build pilot approvals and three continuing upkeep tasks). The separate v3.00 **7/7 finite foundation certificate** remains unchanged.

## K064: source-graded card/printed illustration links, not universal scene depiction

`scripts/audit_card_relationship_acceptance.py` independently joins the committed graph, source register, 2026-10-29 frozen Scryfall printing evidence, exact original story-art comparisons, label index and card/lore links. It refuses to call a named character card or an official art-file label a depicted event unless the explicit scene-caption grade supports that conclusion.

| Original evidence class | Verified count | Correct interpretation |
| --- | ---: | --- |
| Exact Wizards page art-file labels | 570 | A source page used that printing's art file; not a story scene |
| Distinct printing UUID representations | 560 | A dated exact printing identity, not every printing in Magic |
| Independently visually reviewed story-art matches | 6 | Precisely that image/printing comparison; 1 is a direct event-scene caption |
| Graph card-name navigation links | 701 | Printed name, not lore canon |
| Official-story art caption links | 1,025 | Artwork appeared on the cited Wizards page |
| Tiered `depicted_by` links | 15 | **1 direct event-scene caption**, 14 named/contextual links with limits |
| Source-graded curated card/lore links | 208 | Existing priority-pool claim/name/story/art evidence, not general coverage |
| Preserved frozen exact-printing flavor lines in pilot evidence | 133 | Printed flavor text, not an independently verified event |
| Priority-pool cards without a verified story link | 2,626 | Explicitly **unlinked**, not claimed to lack lore |
| Unresolved old image labels | 7 | Six name mismatches, one printing gap; no forced match |

This satisfies K064 as a **bounded evidence-supported linking capability**. It does **not** certify all card illustrations or imply an artist intended every event described on the source page.

## K069: time-qualified directional relations, with explicit absence

The graph contains **1,306** directional, source-ID-linked and canon-graded claim edges, including `allied_with`, `fought`, `created`, `member_of` and more. Precisely **36 edges from 35 claims** carry verbatim relative-time phrases in the claim's own official Wizards quotation; the remaining **1,270** retain no independently supported date.

`scripts/query_multiverse_graph.py` now surfaces these fields **when `--temporal` is explicitly requested** for neighbors, paths, cards or printings. Its default response remains byte-compatible with the v3.00 SHA-pinned foundation Q&A packet:

- the original forward/reverse graph direction;
- graded canon status and official source URLs;
- `in_universe_date`: original `value`, `quote` and `source_id`, or `null`;
- `time_qualification`: `QUOTED_SOURCE_LOCAL_SPAN`, `SOURCE_NOT_DATED` or `NOT_A_CANON_CHRONOLOGY_EDGE` for card/navigation links.

For example, an Amonkhet/Bolas relationship carries the explicit source-relative wording *Several decades ago*. No 4562 AR/global calendar year is inferred from that phrase. Undated relationships are not silently assigned the date of their source's publication. This satisfies K069's recording/query capability **where the cited text supports a time phrase**, not the still-open comprehensive chronology K088 or cross-plane synthesis K103.

## Tests and boundary

Seven fail-closed tests reject invented relative quotes, canon-grade upgrades, treating image labels as scenes, non-Wizards claim sources and stale generated evidence. Existing graph Q&A tests remain in CI, and the new acceptance replay is added to the temporal/graph integrity workflow. `data/release/card_relationship_acceptance_2026-11-01.json` records exact inputs SHA-256 and all evidence counts.

No protected 62 Grixis deck path, approved deck status, or one of the three UNAPPROVED pilot lists changed. The 16 still-active items include unresolved first-party 1990s printing documentation, full history packs, cross-plane chronology and current Commander engineering verification. This review is not all-canon certification.

```bash
python3 scripts/audit_card_relationship_acceptance.py --check
python3 -m unittest discover -s tests -p 'test_card_relationship_acceptance.py' -v
python3 -m unittest discover -s tests -p 'test_multiverse_graph.py' -v
python3 scripts/audit_full_checklist.py --check
python3 scripts/update_multiverse_progress_tracker.py --check
python3 scripts/audit_foundation_milestone_certificate.py
```
