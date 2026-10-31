# Phase 5 — Four further cited plane histories (v2.66)

**Status: PRELIMINARY_RESEARCH_NOT_OWNER_APPROVED.** This is not complete history, a current-world-state guarantee, an accepted foundation release, or permission for Phase 6 deckbuilding.

Twelve new `CANON_CONFIRMED` plane-incident claims are recorded in
`data/lore_research/pack_p5_four_plane_histories_2026-10-31.json`,
each with a verbatim, short Wizards excerpt, source URL and limitation:

| Plane | Direct claims before → after | Evidence and boundary |
| --- | ---: | --- |
| Arcavios | 2 → 5 | [Strixhaven guide (2021)](https://magic.wizards.com/en/news/feature/planeswalkers-guide-strixhaven-2021-04-01): overlapping mana at the plane's birth, five dragons emerging from mana vortices, and the university's roughly 700-year-old foundation. Neither parent-plane identities nor an AR founding year are established. |
| Vryn | 2 → 5 | [Worlds of Magic Origins (2015)](https://magic.wizards.com/en/news/feature/worlds-magic-origins-2015-07-09): mage-ring mana extraction to the Core States, the Ampryn League and Trovian Separatists. The guide explicitly says the rings' ages and builders are unknown; the ultimate political outcome is not asserted. |
| Serra's Realm | 2 → 5 | [Known Multiverse (2008)](https://magic.wizards.com/en/news/feature/known-mutliverse-2008-03-19): Phyrexian contamination, Radiant's historical regency and Urza's final powerstone collapse. Not modern rulership or proof the plane survives. |
| Regatha | 2 → 5 | [Original Spin (2015)](https://magic.wizards.com/en/news/making-magic/original-spin-2015-08-17) and [Offers to the Fire (2015)](https://magic.wizards.com/en/news/magic-story/offers-fire-2015-08-05): Jaya's founding of Chandra's monastery, Keral Keep's volcanic training setting and Jaya-derived fire exercises. Neither foundation date nor current condition is settled. |

The current source-graded graph contains **1,234 claims**, **5,232 nodes** and **8,372 edges**, with **633/633** registered Character/Faction nodes incident on at least one cited claim. This is a coverage-of-registered-entities measure, not an exhaustive census of the Multiverse. All **33** registered planes have some direct evidence; **8** remain below the five-direct-claim threshold, versus 12 in v2.65. The threshold is a research triage tool, never a declaration of completeness.

The foundation review packet has **30 distinct ID-stable representative Q&A cases**. The earlier New Capenna background and history questions no longer share one ID. The packet retains separate chronology ledgers, source links, qualified confidence, explicit unknowns and `complete_history: false`. The tracker and dry-run stay **NOT_RELEASE_READY** with **83/137** workflow items checked. No canon genealogy disputes, snapshot source absences, owner gates, Grixis deck authority or three parked pilots were altered.

## Reproduction and limits

```sh
python3 scripts/build_multiverse_graph.py --check
python3 scripts/build_plane_history_dossiers.py --check
python3 scripts/build_plane_history_priorities.py --check
python3 scripts/build_story_coverage_inventory.py --check
python3 scripts/audit_p5_four_plane_histories.py --check
python3 scripts/build_foundation_acceptance_packet.py --check
python3 -m unittest discover -s tests -p 'test_p5_four_plane_histories.py' -q
```

`scripts/audit_p5_four_plane_histories.py --live` optionally fetches all five Wizards pages to compare excerpts against live HTML. Offline CI gates recorded quotations, grades, direct plane incidence, source URLs, history counts and Q&A behavior. Neither audit proves a full lore chronology.

**Known reproducibility blocker:** `scripts/build_claim_card_anchors.py` requires the pinned `default-cards` bulk at `.cache/multiverse`, which is deliberately not in the repository. Without those exact archived bytes the existing card-anchor overlay cannot be safely rebuilt; historical card-anchor records stay unchanged and the pre-existing source-level replay gate stays open. The five additional official history URLs are cited within the packs even when outside the frozen 626-page story inventory.

The supported `--append-unmapped-packs` path **did** append the new non-set
history pack to the claim-card anchor registry: **1,234/1,234** claims are
accounted for and **4,104** card-name anchors are registered. No historical
printing or art tier was recalculated without the pinned Scryfall source bytes;
the entire bulk-dependent rebuilding limitation remains open.
