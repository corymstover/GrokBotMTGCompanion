# Phase 4 — Mercadia, Argentum/Mirrodin and Serra's Realm: bounded history sequences

**Date:** 2026-10-31
**Status:** PRELIMINARY_RESEARCH_NOT_OWNER_APPROVED; foundation NOT_RELEASE_READY.
**Authoritative source:** Wizards of the Coast, *The Known Mutliverse* (2008-03-19),
<https://magic.wizards.com/en/news/feature/known-mutliverse-2008-03-19>.
The page spells its own title “Mutliverse”; the original URL and citation are preserved.

## Source-verified additions

- **Mercadia (T strand):** six detailed nodes and six successive source-quoted strict
  edges tracing the Weatherlight's escape from Rath through its crash, seizure,
  recovery arrangements, discovery of the Phyrexian warship fleet, preemptive
  strike and departure. A seventh strict edge places the existing constructed
  invasion plane of Rath before the Weatherlight's visit to that same plane.
  This joins the previously disconnected Thran/Rath chain with the Mercadian
  episode without imposing a date on either.
- **Argentum/Mirrodin (new H strand):** seven events and six strict edges:
  creation by Karn, creation of the warden, Karn and Jeska's introduction of
  an *unnamed mysterious contagion*, infection/transformation into Memnarch,
  his interplanar capture plan, defeat by Glissa and allies, and Karn's return
  to restore order. This is explicitly the 2008 account, not an automatic
  same-event alias to later descriptions of Phyrexian oil in the P strand.
- **Serra's Realm (S strand):** Radiant's harsh/paranoid administration is
  recorded after her assumption of control, without claiming it ended before
  Urza's final extraction of the realm's power.

The new **14 nodes / 14 strict edges** yield source-local counts of **9 strands,
88 events, 71 strict BEFORE edges, 3 nonordering relations, and 314 of 3,828
ordered event pairs**. The legacy ledger remains separately **56 events / 177
ordered pairs**, and the seven verified SAME_EVENT bridges remain unchanged.
All generated chronology artifacts carry quoted source URLs and SHA-256 digests.

## Safety boundaries

1. The source does not strictly order the Weatherlight's departure from
   Mercadia versus Rath's later overlay; this pair remains `UNKNOWN`.
2. The soul-bomb devastation of Old Phyrexia and the Legacy's destruction
   of Yawgmoth remain unordered relative to each other.
3. Original-Mirrodin H-strand accounts are not silently collapsed with the
   later New Phyrexia P-strand: even the apparently matching creation event
   has no independently corroborated SAME_EVENT bridge here.
4. Radiant's increasing paranoia and the realm's final powerstone collapse
   remain unordered in strict chronology. No AR year or total Multiverse
   timeline is inferred from publication order.
5. These histories extend, but **do not complete**, Pack A/B/C synthesis,
   comprehensive plane/character/faction biographies or release gate L244.

## Verification

From repository root:

```sh
python3 scripts/source_event_sequences.py --check
python3 scripts/source_event_sequences.py --live
python3 scripts/query_lore_chronology.py --check
python3 -m unittest tests.test_phase4_mercadia_mirrodin_sequences tests.test_source_event_sequences tests.test_chronology_same_ledger_bridges -q
```

Live quote replay checked **81 excerpts across seven official Wizards pages**;
the new test suite asserts direct and transitive proofs, citations, normal
Companion Q&A behavior, and negative UNKNOWN controls. No approval file,
decklist, snapshot lock, protected Grixis path or previously graded claim
was changed. Checklist stays **89/137 checked, 48 open**.

The deterministic Phase 8 knowledge-only acceptance packet was also regenerated
with **53 representative Q&A cases**, including four new positive/negative
Mercadia and historical-Mirrodin questions. The packet remains explicitly
**NOT CERTIFIED** and owner acceptance remains conditional and inoperative.
