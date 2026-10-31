# Phase 4 — Bolas's imprisonment through Tarkir: Dragonstorm and later report

**Checkpoint:** 2026-10-31
**Status:** PRELIMINARY_RESEARCH_NOT_OWNER_APPROVED; NOT_RELEASE_READY.

## Three first-party accounts, one bounded sequence

1. In Wizards' [*Even More War Games* (2019)](https://magic.wizards.com/en/news/making-magic/even-more-war-games-2019-05-06), the editorial explanation of the *Prison Realm* card records that Nicol Bolas lost his spark at the end of *War of the Spark* and was jailed in the Meditation Realm with Ugin guarding him. This already underlies graded Pack A claim `A008`; it is not evidence of the prison's **current** integrity.
2. In the narrative of [*Tarkir: Dragonstorm*, Episode 7: *Return* (2025)](https://magic.wizards.com/en/news/magic-story/tarkir-dragonstorm-episode-7-return), Narset witnesses the Realm disintegrating and Bolas's restraints breaking. Ugin tries unsuccessfully to hold him. Both dragons then vanish from her view, after which she exits through an Omenpath. Narset explicitly wonders whether they are dead; **that is speculation, not a death confirmation**. The Realm's collapse and Bolas's escape overlap in the scene; neither is proved to begin strictly before the other.
3. In [*Lorwyn Eclipsed*, Episode 2: *Shake Off Slumber* (December 2025)](https://magic.wizards.com/en/news/magic-story/lorwyn-eclipsed-episode-2-shake-off-slumber), Ajani describes the earlier expedition to Liliana and reports Bolas's escape. He states that **Bolas's spark state is unknown**. His testimony does not establish Bolas's present plane, planeswalking capacity or whether the twins survived the void unchanged.

The `W` strand has **seven events and six strict, quoted BEFORE relations**, with six citations to the two 2025 episodes; the independently sourced 2019 imprisonment is linked as existing Pack A claim `A008` on the first event. The full source-local supplement grows from 11/107/87 to **12 strands / 114 events / 93 strict edges**, with **371 of 6,441 possible unordered event pairs** supported by strict paths. Eight cross-ledger `SAME_EVENT` bridges remain unchanged; the legacy 56-event ledger is untouched and remains distinct. All **104 directly quoted chronology excerpts across 11 official pages** must match live text.

## Questions the Companion can and cannot settle

| Query | Qualified result | Limitation |
| --- | --- | --- |
| `W:bolas_imprisoned` → `W:bolas_freed` | `BEFORE` | Prison break is proven; no proof of restored spark. |
| `W:bolas_freed` → `W:ugin_grapples` | `BEFORE` | The grapple fails; no certified later location. |
| `W:brothers_vanish` → `W:ajani_reports` | `BEFORE` | A disappearance and later report, not confirmed deaths. |
| `W:meditation_unravels` → `W:bolas_freed` | `UNKNOWN` | Described in an overlapping scene without an exact start order. |
| `B:ugin_reforms` → `W:bolas_imprisoned` | `UNKNOWN` | Ancient meditation account and modern imprisonment are not globally date-bridged in this source-local ledger. |

The five cases are added to the generated **64-question** Phase 8 foundation acceptance packet. `UNKNOWN` remains a valid, explicitly tested result rather than a failure to guess. These tests do not certify exhaustive lore, resolve the original/revised Tarkir-history retcon, infer an absolute AR year or validate any deck.

## Replay commands

```sh
python3 scripts/source_event_sequences.py --check
python3 scripts/source_event_sequences.py --live
python3 scripts/query_lore_chronology.py --check
python3 scripts/build_foundation_acceptance_packet.py --check
python3 -m unittest tests.test_phase4_bolas_post_war_chronology tests.test_source_event_sequences tests.test_foundation_acceptance_packet -q
python3 scripts/audit_full_checklist.py --check
python3 scripts/update_multiverse_progress_tracker.py --check
```

Foundation-first remains binding: **89/137** tasks checked, **48** open,
**NOT_RELEASE_READY**; three previous lore-deck pilots remain **UNAPPROVED**
and the 62 approved Grixis decks remain untouched.
