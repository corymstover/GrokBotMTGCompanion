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
official Wizards historical guides. v2.63 added six source-local proofs against
the already cited [Wizards New Phyrexia plane overview](https://magic.wizards.com/en/story/new-phyrexia-plane).
**v2.69 adds 15 bounded proofs from two more official Wizards pages**:
[the Muraganda section of the Aetherdrift guide](https://magic.wizards.com/en/news/feature/planeswalkers-guide-to-aetherdrift-part-2)
and [Ugin's narrated Meditation Realm memory in *The Unwritten Now*](https://magic.wizards.com/en/news/magic-story/chronicle-bolas-unwritten-now-2018-08-15).
**v2.70 adds 21 more source-local relations (20 strict, one non-ordering)
from the existing verified [*Known Multiverse* (2008) Wizards retrospective](https://magic.wizards.com/en/news/feature/known-mutliverse-2008-03-19),
connecting the Thran/Old Phyrexia/Rath history and Serra's Realm's historical
collapse. All **60 excerpts across seven pages passed live HTML quotation
verification** on 2026-10-31. Each relationship retains the official URL, quoted phrase,
SHA-256 quote digest, source ID, certainty and evidence limitation. The
archive remains a partial, non-owner-approved timeline.

**v2.71:** Seven deliberately curated `SAME_EVENT` links now identify
historical events shared with the separate legacy Packs A–C chronology
without merging their unverified eras or event counts. Each identity is
source-corroborated in both ledger entries against the same Wizards page.
The 60 before/overlap quotes plus seven identity quotes passed live audit
on 2026-10-31 (**67/67 total, seven official pages**).

| Bounded account | Nodes | Strict source-supported BEFORE edges | Qualified non-ordering relations | Interpretation |
| --- | ---: | ---: | ---: | --- |
| Kamigawa / Kami War | 7 | 5 | 0 | Official historical summary; Imperial founding is not assumed to be strictly after the barrier's rupture. |
| Valley / Bloomburrow | 9 | 6 | 1 | The *order in a narrated legend*, **not** proven objective ancient history. The Wildsear appearance is during the War of Cinders, **not** after its conclusion. |
| Mirrodin / early New Phyrexia | 7 | 6 | 0 | Oil's arrival and spread, the campaign and Mirran resistance, and Venser's sacrifice. The overview **does not order** Mirran defeat against the sacrifice or establish the post-March of the Machine political present. |
| Duskmourn / Marina and the House | 8 | 6 | 0 | Official historical account; neither the House's original plane name nor an AR year is supplied. |
| Muraganda / ancient collapse and Grand Prix arrangements | 10 | 5 | 1 | The ancient civilization discovered magic before its fall. **Moon-shattering versus collapse is unproven**; moon-strikes abating and survivor societies forming are overlapping processes, not a strict succession. The Grand Prix advance delegation is one year before the race, while the Autocracy's treaty maneuvering has only a partial local order. |
| Meditation Realm / Ugin's remembered early Bolas conflict | 10 | 9 | 0 | Within Ugin's memory, meditation precedes Bolas's assault, pursuit, return and cataclysm. The account later depicts Ugin reforming; **no permanent death or current Realm status** is asserted. Bolas's displacement versus Ugin's reconstitution is not strictly ordered by a cited bridge. |
| Thran decline / Old Phyrexia / Rath / first invasion | 16 | 14 | 1 | The official retrospective orders the creator's death, Yawgmoth's rise, Thran war, portal closure, long invasion preparations and the Rath incursion. **The soul-bomb devastation of Old Phyrexia is not ordered against Yawgmoth's defeat by the Weatherlight.** Rath's overlay and invasion onset are inseparable in the passage. |
| Serra's Realm / Urza and Radiant | 7 | 6 | 0 | Creation, Urza's refuge, attack, Serra's departure and the realm's eventual powerstone extraction. The source does not resolve **Radiant's reign versus Urza's final extraction**. |
| **Total** | **74** | **57** | **3** | **180 strict comparable pairs out of 2,701**, across eight separately bounded strands. |

The Valley row's war-start/appearance relation is deliberately
`DURING_OR_AFTER_START`, excluded from the BEFORE closure. Thus the tool does
**not** falsely infer an uninterrupted transitive path from the founding of
the Holly Leaf Order through the end of the legendary conflict to later
weaving restrictions. Similarly, there is no source-backed cross-plane edge.
The Muraganda moon-strike-abatement/survivor-formation relation uses the same
non-transitive qualifier: the source says *as*, not *after*. Its ancient
collapse and moon-shattering remain two separate events with UNKNOWN order.
The New Phyrexia strand can prove oil introduction before early Mirran defeat
through four direct source links. It **cannot** order that defeat against
Venser restoring Karn, or Karn's rise as Father of Machines against the onset
of the campaign: those comparisons remain `UNKNOWN`, not inferred from the
overview's paragraph order or its historical-present wording. The Meditation
Realm strand follows only Ugin's remembered early scene. It does not join
later events such as Bolas's release in *Tarkir: Dragonstorm* merely because
their stories were published later.

The new Thran-to-first-invasion strand supplies a connected historical route
from the unnamed creator's death to the closed Thran/Phyrexia portal and
Yawgmoth's later design for Rath. It also preserves an honest fork in the
first invasion's outcomes. The 2008 official retrospective cites the
planeswalkers' *soul-bomb* devastation of Old Phyrexia and the Weatherlight
crew's *Legacy* defeat of Yawgmoth, without saying which came first. Neither
the phrase order nor the set chronology is evidence for a strict BEFORE
relation between the two. The independent Serra's Realm sequence likewise
does not date Radiant's tenure relative to Urza's final extraction. Both
UNKNOWN cases are exercised by the normal Q&A route.

## Explicit cross-ledger identity proof (v2.71)

These are *equivalences*, not temporal edges. The merged proof search can
step across an equivalence, follow strict source-cited BEFORE edges, and
return BEFORE/AFTER only if an actual strict edge participates. Equivalence
alone yields `SAME_EVENT`; a path that requires an unsupported "during" or
across-era assumption still returns `UNKNOWN`. All seven source-quoted
bridges use the Wizards 2008 *Known Multiverse* account:

| Legacy event | Source-local same event |
| --- | --- |
| `B:phyrexia_creator_dies` | `T:phyrexian_creator_dies` |
| `B:yawgmoth_to_phyrexia` | `T:dyfed_brings_yawgmoth` |
| `B:phyrexia_portal_closed` | `T:portal_closed` |
| `B:thran_defeated` | `T:thran_defeated` |
| `C:weatherlight_to_rath` | `T:weatherlight_to_rath` |
| `C:weatherlight_mercadia` | `T:weatherlight_mercadia` |
| `C:rath_overlay` | `T:rath_overlay` |

The old and source-local event totals are **not additive**: seven events
are now explicitly recognized as the same historical occurrences. This
does not imply global chronological alignment or completeness. The
composite graph has **zero strict cycles**; a deliberate false-equivalence
regression must trigger cycle rejection. Example answers:

- `B:phyrexia_creator_dies` BEFORE `T:rath_constructed`: cited proof.
- `B:phyrexia_portal_closed` vs `T:portal_closed`: `SAME_EVENT`, not BEFORE.
- `B:phyrexia_creator_dies` vs `T:yawgmoth_destroyed`: `UNKNOWN`, because
  the connection would require treating Rath's overlay/invasion onset as a
  strictly ordered pair, which the source does not do.

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
python3 scripts/query_lore_chronology.py --compare M:ancient_magic_discovered M:ancient_collapse
python3 scripts/query_lore_chronology.py --compare M:ancient_collapse M:moons_shatter
python3 scripts/query_lore_chronology.py --compare M:moon_strikes_abate M:survivor_cultures
python3 scripts/query_lore_chronology.py --compare B:ugin_meditates B:ugin_reforms
python3 scripts/query_lore_chronology.py --compare B:bolas_displaced B:ugin_reforms
python3 scripts/query_lore_chronology.py --compare T:phyrexian_creator_dies T:thran_defeated
python3 scripts/query_lore_chronology.py --compare T:old_phyrexia_decimated T:yawgmoth_destroyed
python3 scripts/query_lore_chronology.py --compare S:urza_flees S:realm_powerstone_collapse
python3 scripts/query_lore_chronology.py --compare S:radiant_assumes_rule S:realm_powerstone_collapse
python3 scripts/query_lore_chronology.py --compare B:phyrexia_creator_dies T:rath_constructed
python3 scripts/query_lore_chronology.py --compare B:phyrexia_portal_closed T:portal_closed
python3 scripts/query_lore_chronology.py --compare B:phyrexia_creator_dies T:yawgmoth_destroyed
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
- Muraganda's collapse versus moon-shattering order, the emergence of modern
  factions, and the date/limits of the Saurid Autocracy's agreements.
- The Meditation Realm's subsequent transformations, including the later
  Bolas prison and events of *Tarkir: Dragonstorm*; Ugin's remembered death
  scene must not be misread as proof of a permanent death.
- The precise relative order of Old Phyrexia's soul-bomb devastation and the
  Legacy's defeat of Yawgmoth: both are described by Wizards in 2008, but
  not in a source-supported strict succession. Source-local ordering here
  cannot certify the broader cross-page L244 chronology gate.
- The ending of Radiant's administration relative to Urza's final extraction
  of Serra's Realm into a Weatherlight powerstone.
- Earlier Packs A–C original storyline cross-page gaps and the overall L244
  chronology closure criterion.
- Comprehensive character/faction histories, cross-plane retcon evidence,
  broad obscure Q&A and final foundation certification.

**Preservation:** No card lists, approved Grixis hashes or new deck pilots
were modified. The three existing lore-deck drafts remain unapproved and
parked until the owner-authorized foundation-first sequence is complete.
