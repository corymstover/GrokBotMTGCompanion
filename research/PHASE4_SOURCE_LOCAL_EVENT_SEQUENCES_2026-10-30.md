# Phase 4 — source-local event sequences (2026-10-30)

**Status:** PRELIMINARY_RESEARCH_NOT_OWNER_APPROVED. This is a bounded
chronology/query improvement, **not** closure of the L244 total-chronology gate,
not certified complete MTG history, and not permission to build or approve
the three lore-deck pilots. Phase 6 remains deferred at Cory's direction.

## Verified source-local result

`scripts/source_event_sequences.py` reads
`data/lore_research/source_event_sequences_spec_2026-10-30.json` and the
already registered v2.54–v2.55 lore packs, and regenerates
`data/lore_research/source_event_sequences_2026-10-30.json` deterministically.
The initial 18 source excerpts were checked in live HTML from three distinct
official Wizards historical guides. v2.63 adds six source-local proofs against
the already cited [Wizards New Phyrexia plane overview](https://magic.wizards.com/en/story/new-phyrexia-plane),
which was inspected again on 2026-10-31. Each relationship retains the official
URL, quoted phrase, SHA-256 quote digest, source ID, certainty and evidence
limitation. The archive remains a partial, non-owner-approved timeline.

| Bounded account | Nodes | Strict source-supported BEFORE edges | Qualified non-ordering relations | Interpretation |
| --- | ---: | ---: | ---: | --- |
| Kamigawa / Kami War | 7 | 5 | 0 | Official historical summary; Imperial founding is not assumed to be strictly after the barrier's rupture. |
| Valley / Bloomburrow | 9 | 6 | 1 | The *order in a narrated legend*, **not** proven objective ancient history. The Wildsear appearance is during the War of Cinders, **not** after its conclusion. |
| Mirrodin / early New Phyrexia | 7 | 6 | 0 | Oil's arrival and spread, the campaign and Mirran resistance, and Venser's sacrifice. The overview **does not order** Mirran defeat against the sacrifice or establish the post-March of the Machine political present. |
| Duskmourn / Marina and the House | 8 | 6 | 0 | Official historical account; neither the House's original plane name nor an AR year is supplied. |
| **Total** | **31** | **23** | **1** | **52 strict comparable pairs out of 465**, across four separate strands. |

The second row's war-start/appearance relation is deliberately
`DURING_OR_AFTER_START`, excluded from the BEFORE closure. Thus the tool does
**not** falsely infer an uninterrupted transitive path from the founding of
the Holly Leaf Order through the end of the legendary conflict to later
weaving restrictions. Similarly, there is no source-backed cross-plane edge.
The New Phyrexia strand can prove oil introduction before early Mirran defeat
through four direct source links. It **cannot** order that defeat against
Venser restoring Karn, or Karn's rise as Father of Machines against the onset
of the campaign: those comparisons remain `UNKNOWN`, not inferred from the
overview's paragraph order or its historical-present wording.

The legacy Packs A–C graph remains separately preserved: **56 event nodes,
63 stated edges, and 177 of 3,074 comparable pairs**. These two fractions
have **different universes of event pairs** and must never be summed into a
false global chronology completion percentage.

## Reproducible commands

```bash
python3 scripts/source_event_sequences.py --check
python3 scripts/source_event_sequences.py --live
python3 scripts/query_lore_chronology.py --check
python3 scripts/query_lore_chronology.py --list
python3 scripts/query_lore_chronology.py --compare K:konda_imprisons K:realm_barrier_breaks
python3 scripts/query_lore_chronology.py --compare V:war_of_cinders V:wildsear_appears
python3 scripts/query_lore_chronology.py --compare V:holly_pact D:ascension
python3 scripts/query_lore_chronology.py --compare P:karn_brings_oil P:mirrans_overwhelmed
python3 scripts/query_lore_chronology.py --compare P:mirrans_overwhelmed P:venser_restores_karn
python3 -m unittest discover -s tests -p 'test_source_event_sequences.py' -q
```

The shared query accepts an exact event ID or a **unique substring of an
event label**. It produces cited proof chains for BEFORE/AFTER, explicitly
qualified overlap, or UNKNOWN for missing/cross-ledger links. Ambiguous
human-readable phrases raise a helpful error rather than silently picking a
timeline. Since v2.57, the same proofs are also available in the
`mv_ask.py ask` natural-language chronology route, without inferring
unsupported timelines.

## Important open work

- Primary-source citations connecting historic *in-universe* sequences across
  currently unanchored guides; do not use real-world set publication dates as
  in-universe ordering.
- Missing Kamigawa war stages and exact ordering of Imperial founding relative
  to the realm boundary; missing valley history where the account gives only
  overlap or implies rather than proves a historical event.
- Duskmourn's unnamed original plane and unsupported AR synchronization.
- New Phyrexia's full early-conquest sequence, the exact relative positions of
  Mirran overwhelm and Venser's sacrifice, and the separate post-March of the
  Machine political state.
- Earlier Packs A–C original storyline cross-page gaps and the overall L244
  chronology closure criterion.
- Comprehensive character/faction histories, cross-plane retcon evidence,
  broad obscure Q&A and final foundation certification.

**Preservation:** No card lists, approved Grixis hashes or new deck pilots
were modified. The three existing lore-deck drafts remain unapproved and
parked until the owner-authorized foundation-first sequence is complete.
