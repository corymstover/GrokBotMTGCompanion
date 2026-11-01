# War of the Spark: Ravnica operations — bounded source-local chronology

**Date:** 2026-11-01  
**Status:** PRELIMINARY_RESEARCH_NOT_OWNER_APPROVED; **not** a complete history or foundation release.

## Scope and primary evidence

This adds a distinct **Y** chronology strand for the Rat-narrated Ravnica operation scenes, separate from the existing **X** Azorius succession and **E** Amonkhet-to-Ravnica accounts. It uses these four official Wizards of the Coast 2019 Magic Story chapters:

1. [Old Friends and New](https://magic.wizards.com/en/news/magic-story/war-spark-ravnica-old-friends-and-new-2019-05-08) — portal breach and the arriving Eternal army.
2. [Rallying the Reluctant](https://magic.wizards.com/en/news/magic-story/war-spark-ravnica-rallying-reluctant-2019-05-22) — Jace's retreat command and a council identifying the Beacon, Immortal Sun, Planar Bridge, Liliana and Bolas as problems to address.
3. [Operation Desperation](https://magic.wizards.com/en/news/magic-story/war-spark-ravnica-operation-desperation-2019-06-05) — the already-disabled Bridge and preparation of Niv-Mizzet's Firemind's Vessel.
4. [Ashes](https://magic.wizards.com/en/news/magic-story/war-spark-ravnica-ashes-2019-06-12) — Niv-Mizzet incapacitated, a renewed assault, Dack Fayden killed after a failed escape attempt, and Blackblade shattering on Bolas's brow.

All **ten distinct new ordering quotations** were checked against freshly fetched official page text by normalized verbatim substring (10/10, zero misses), then retained in the generated ledger with source URL and quotation SHA-256. The source page cache is deliberately uncommitted. This is not based on article publication order.

## Finite result

| Metric | v2.96 | v2.97 |
| --- | ---: | ---: |
| Source-local strands | 16 | **17** |
| Events | 144 | **155** |
| Strict cited edges | 116 | **126** |
| Proven within-strand ordered pairs | 472 | **525** |
| Total pair universe across registered events | 10,296 | **11,935** |
| Separate legacy same-event bridges | 8 | **8** |
| Representative foundation acceptance questions | 115 | **119** |

The main supported sequence runs from a portal breach and Eternal invasion through an emergency council, reported Bridge shutdown, Firemind preparation and incapacitation, the later general assault, and Dack Fayden's death. The Blackblade strike descends from the general assault as a separate branch, with **no citation-backed strict order** between Dack's death and the blade shattering.

## Disputed, inferred and still unknown

- Rat observes Dack fail to planeswalk and be killed by an Eternal; **Rat infers** that the Immortal Sun was reactivated in time. No independently timed activation is asserted.
- The web chapter ends with Blackblade broken and Gideon falling. It does **not**, on its own, settle either Gideon's later fate or Bolas's ultimate defeat, imprisonment, spark status or whereabouts.
- The two War-of-the-Spark source-local strands **X** (Azorius succession) and **Y** (combat operations) share a setting, but no exact sourced SAME_EVENT bridge was added. The separate **E** Amonkhet/Bridge strand also remains unmerged.
- A generic “Show chronology of the War of the Spark” now returns an ambiguity with two candidates; users can ask for `Show chronology strand X` or `Show chronology strand Y`. This is a deliberate correctness safeguard, not a search failure.
- No absolute AR year, all-war timeline, date for each mission, or source-independent cross-plane order is inferred.

## Reproduction and tests

The `source_event_sequences_spec_2026-10-30.json` contains the 11 Y event nodes, 10 edges and citation keys. `scripts/source_event_sequences.py` rebuilds the deterministic graph and content hash. New tests cover the nine-edge portal-to-Dack proof, the independent Blackblade branch, four-strand official citations, and Q&A handling of supported and unknown orderings. The Phase 8 acceptance packet now contains **119** representative cases and retains the **NOT CERTIFIED** flag. CI includes the new tests in the chronology workflow.

Checklist status remains **98/137 checked, 39 open**. This advances K099/K103/K088 evidence but does not close those broader history tasks. Phase 6 and the protected 62 Grixis lists were not touched.
