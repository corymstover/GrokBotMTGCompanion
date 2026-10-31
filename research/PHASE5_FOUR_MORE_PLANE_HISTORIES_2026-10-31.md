# Phase 5 — Four additional cited plane histories (v2.67)

**Status: PRELIMINARY_RESEARCH_NOT_OWNER_APPROVED.** Partial historical evidence only: neither exhaustive plane history, current-state certification, owner signoff nor authority to begin Phase 6 deckbuilding.

Twelve new `CANON_CONFIRMED` direct plane relations, each with a source excerpt, official link, date/currentness boundary and limitation, are in `data/lore_research/pack_p5_four_more_plane_histories_2026-10-31.json`.

| Plane | Direct claims before → after | Primary evidence and qualification |
| --- | ---: | --- |
| Fiora | 4 → 7 | [Wizards' plane overview](https://magic.wizards.com/en/story/fiora-plane) documents Drakestown's massacre and Paliano's magically binding laws. [Marchesa's 2016 proclamation](https://magic.wizards.com/en/news/magic-story/proclamation-queen-marchesa-2016-08-15) proves her claim, not the legitimacy of her succession or the unknown perpetrators of the massacre. |
| Kaldheim | 4 → 7 | [Planeswalker's Guide (2021)](https://magic.wizards.com/en/news/feature/planeswalkers-guide-kaldheim-part-1-2021-01-08) describes the World Tree joining mini-plane realms, destructive Doomskar overlaps and the Skoti replacing the Einir. Its 'current' ruling family and 'few centuries' are relative to that guide. More realms are possible; no total realm census is claimed. |
| Lorwyn-Shadowmoor | 3 → 6 | [Planeswalker's Guide to Lorwyn Eclipsed](https://magic.wizards.com/en/news/magic-story/planeswalkers-guide-to-lorwyn-eclipsed) distinguishes the *historical* approximately 300-year, plane-wide Great Aurora shifts from the *newer* shifting boundaries between adjacent aspects, with transformative effects and rare exceptions. The old cycle is not projected onto the new one. |
| Thunder Junction | 2 → 5 | [Wizards' 2024 preview](https://magic.wizards.com/en/news/announcements/a-first-look-at-outlaws-of-thunder-junction), [Episode 2](https://magic.wizards.com/en/news/magic-story/episode-2-the-jailbreak) and [heist-crew feature](https://magic.wizards.com/en/news/feature/a-legendary-crew-for-an-unbelievable-heist-outlaws-of-thunder-junction) establish the ancient vault Maag Taranau, Oko's crew formation and Tarnation below the vault. They do not date or identify the vault builders, prove heist outcome or certify later control. |

All **seven** original Wizards pages passed a live short-excerpt match audit. The derived graph contains **1,246 claims**, **5,259 nodes**, **8,421 edges**, and **633/633** registered Character/Faction nodes with some direct cited evidence. All **33** registered plane dossiers have direct claims; **4** still have fewer than five. The five-claim threshold is a *triage heuristic*, never a completeness certificate. The packet now has **34 distinct qualified representative question IDs** and preserves `complete_history: false`, absent verified total chronology, explicit unknowns and the release/owner gates.

The engineering checklist remains **83/137 checked**. Release state stays **NOT_RELEASE_READY**; the three proposed Commander pilots are parked and none of the 62 approved Grixis decks, their hashes or owner decision gates were modified.

## Reproduction and limits

```sh
python3 scripts/build_multiverse_graph.py --check
python3 scripts/build_plane_history_dossiers.py --check
python3 scripts/build_plane_history_priorities.py --check
python3 scripts/build_story_coverage_inventory.py --check
python3 scripts/audit_p5_four_more_plane_histories.py --check
python3 scripts/build_foundation_acceptance_packet.py --check
python3 -m unittest discover -s tests -p 'test_p5_four_more_plane_histories.py' -q
```

For live independent corroboration, run `python3 scripts/audit_p5_four_more_plane_histories.py --live`. Offline CI audits provenance, graph incidence, direct counts, qualified query behavior, 34 unique Q&A IDs and unchanged release gates.

The pinned October 29 Scryfall `default-cards` bulk is absent from this workspace/repository. As in v2.66, the deliberately narrow `--append-unmapped-packs` pass safely accounts for **1,246/1,246** claims and registers **4,109** card-name anchors, preserving older art/printing tiers. Full source-level Scryfall replay remains an open gate. These seven official URLs are direct pack citations, not an assertion that the historical frozen story-page inventory has expanded.
