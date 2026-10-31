# Phase 4 — Alara's unknown Sundering, Gideon's isolated Bant visit and the Conflux

**Checkpoint:** 2026-10-31

**Status:** PRELIMINARY_RESEARCH_NOT_OWNER_APPROVED; NOT_RELEASE_READY.

## Primary historical accounts

1. Wizards' [*The Worlds of Magic Origins* (2015)](https://magic.wizards.com/en/news/feature/worlds-magic-origins-2015-07-09) identifies the original shattering of Alara as an event caused by an **unknown cataclysm**. The five shards thereafter evolved independently, each with three mana colors. It explicitly locates Gideon's arrival on Bant while Bant was still isolated and contrasts that time with Alara's **later** reunion. This is a retrospective published in 2015; its publication date is **not** Gideon's in-world arrival year.
2. Wizards' [Alara plane profile](https://magic.wizards.com/en/story/alara-plane) describes the reunion of five shards and restoration of five-color mana. It says conflicts break out **as** the former shard boundaries dissolve, including Esper's search for carmot, Grixis undead incursions, Jund's hunts, Naya's march and Bant's defenses. The overview notes Bolas's later mana-seeking plan, but **does not say Bolas caused the original Sundering**.

The new source-local `G` strand adds **seven events / four strict BEFORE edges / two DURING_OR_AFTER_START relations**, with direct-source quote hashes. Its positive order is:

1. Unknown cataclysm sunders Alara.
2. Five shards spend centuries isolated.
3. Gideon arrives on Bant during isolation.
4. The shards converge into one plane.
5. The reunited Alara again flows with five mana colors.

The boundary dissolution and cross-shard wars are deliberately **not ordered strictly against the start or completion of the Conflux**. In particular, the narration does not establish that every border had fully dissolved before fighting began. Nor does the record anchor the Conflux to Dominaria's Mending or other remote plane histories.

## Verified boundaries

| Comparison | Result | Why |
| --- | --- | --- |
| `G:unknown_sundering` → `G:gideon_bant_arrival` | `BEFORE` | Official 2015 retrospective situates Gideon during already-existing isolation. |
| `G:gideon_bant_arrival` → `G:conflux_reunion` | `BEFORE` | Explicit *then vs since* contrast on the same official page. |
| `G:shards_isolated` → `G:five_colors_return` | `BEFORE` | Source-quoted path through Gideon's isolated visit and Alara's reunion. |
| `G:borders_dissolve` → `G:shard_wars` | `DURING_OR_AFTER_START` | Wars occur **as** borders dissolve, not strictly afterward. |
| `R:planeswalkers_mend_rifts` → `G:conflux_reunion` | `UNKNOWN` | No verified cross-strand chronological bridge. |

The source-local totals become **13 strands, 121 events, 97 strict edges,
5 non-ordering overlaps and 381 of 7,260 possible unordered event pairs**;
the previous 56-event ledger, 8 verified cross-ledger same-event bridges and
all existing canon grades are unchanged. The all-pairs independent chronology
oracle now checks all 7,260 comparisons; **110 quoted excerpts across 13 live
official pages passed**. Five new positive/negative questions raise the
representative Phase 8 packet to **72**, still **NOT CERTIFIED**.

## Reproduction

```sh
python3 scripts/source_event_sequences.py --check
python3 scripts/source_event_sequences.py --live
python3 scripts/query_lore_chronology.py --check
python3 -m unittest tests.test_phase4_alara_sundering_history tests.test_chronology_global_pair_matrix tests.test_source_event_sequences -q
python3 scripts/build_foundation_acceptance_packet.py --check
python3 scripts/audit_full_checklist.py --check
python3 scripts/update_multiverse_progress_tracker.py --check
```

Foundation-first remains binding. **89/137** tasks are checked and **48**
remain open. No Grixis list or owner record was changed; the three graph-built
lore pilots remain **UNAPPROVED** and parked until certification.
