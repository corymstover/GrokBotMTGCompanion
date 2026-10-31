# Phase 4 v2.87 — bounded Amonkhet → Ravnica chronology

**Status:** PRELIMINARY_RESEARCH, NOT owner-reviewed or release-certified. Source-verifiable engineering milestone, not a complete War of the Spark chronology.

## New cited event strand `E`

The prior source-local chronology had separate Zendikar/Gatewatch and War of the Spark evidence but no bounded Amonkhet → Ravnica sequence. Official Wizards episodes now support three **strictly local** comparisons:

| In-universe comparison | Outcome | Verbatim anchor / official source |
| --- | --- | --- |
| Amonkhet has already been devastated → Samut warns Ravnica's council | `BEFORE` | Samut's first-person account that Bolas *left* her world devastated, in [*Rallying the Reluctant*](https://magic.wizards.com/en/news/magic-story/war-spark-ravnica-rallying-reluctant-2019-05-22). Linked to existing confirmed survivor claim `AKH029` only as its historical context. |
| Eternals begin entering Ravnica from Amonkhet → council plans to halt the flow | `BEFORE` | Jace states that the Planar Bridge *allows* the army to enter and that they must close it, in the same official episode. The arrival continues while the plan is discussed. |
| Eternal flow has begun → that flow is shut down | `BEFORE` | Rat reports that the bridge and flow from Amonkhet *had been shut down*, in [*Ashes*](https://magic.wizards.com/en/news/magic-story/war-spark-ravnica-ashes-2019-06-12). |

No stricter claim is made from the two publication dates: those are real-world dates, not AR years. Both episodes are narrated by Rat, and Samut's historical report is explicitly identified as hers.

## Deliberately unresolved

- Whether Samut's warning happened strictly before or after the bridge shutdown remains `UNKNOWN` in this ledger. It is not connected by an attested strict-order proof chain.
- The council's plan is not silently equated with the eventual shutdown. The interim mission and exact bridge-closure instant are not independently ordered by these three quotes.
- The original Zendikar founding-oath strand `Z` and later War-of-the-Spark-to-Dragonstorm strand `W` retain separate identities. Neither is joined to `E` merely because they mention the Gatewatch or Nicol Bolas.
- The Amonkhet Hours, Eternal manufacture, first bridge activation and all WAR missions have no invented total chronology or numeric AR date.
- The existing Pack A genealogy and Legacy/Old Phyrexia chronology blockers remain open.

## Reproducible implementation

- Spec: `data/lore_research/source_event_sequences_spec_2026-10-30.json` (two previously registered official source IDs `wr_rallying`, `wr_ashes`; five events, three strict edges).
- Rebuilt ledger: `data/lore_research/source_event_sequences_2026-10-30.json`: **15 strands, 139 events, 112 strict edges, five non-ordering overlaps, 462/9,591 ordered event pairs, eight unchanged same-event bridges**.
- Companion: `mv_ask` routes event-order questions before unrelated Set Atlas/rules imports; cited positive answers and unknowns remain `QUALIFIED`.
- Four focused regression methods: `tests/test_phase4_amonkhet_ravnica_chronology.py`, wired into the integrity workflow. They assert official URLs, grade `CANON_CONFIRMED` for `AKH029`, both supported orderings and multiple unproved `UNKNOWN` comparisons.
- Rebuilt knowledge-foundation review packet: **79 representative Q&A cases** (three added positive/negative Amonkhet/Ravnica cases), still `NOT_CERTIFIED`.

All 62 approved Grixis decks, protected paths, parked Phase 6 pilots and pending owner decisions are untouched. **Checklist: 89/137 checked, 48 open; NOT_RELEASE_READY.**
