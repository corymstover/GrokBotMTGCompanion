# Pack C5 — Two separate first-invasion outcomes, not a proven order

Status: **PRELIMINARY_RESEARCH**, independently checked against Wizards' primary
published source on October 30, 2026. Not owner approved or a finished chronology.

Primary source: [*The Known Mutliverse* (Wizards, March 19, 2008)](https://magic.wizards.com/en/news/feature/known-mutliverse-2008-03-19).
The article summarizes the Thran, Old Phyrexia, the Rath overlay and the first
Phyrexian invasion. It is an editorial retrospective, not a replacement for
later canon, retcons or differing character/narrator perspectives.

## Source-backed facts

1. **C501 — Weatherlight's Legacy destroys Yawgmoth.** Wizards attributes
   the destruction of Yawgmoth on Dominaria to the Weatherlight crew's use of
   the Legacy artifacts. This is a confirmed attribution **in that article**,
   not proof of an exclusive individual killer. Pack C's C012 already compares
   different official attributions to Karn and allies, Gerrard and Urza;
   preserve them for Cory's disputed-lore review.
2. **C502 — Planeswalker soul bombs devastate Old Phyrexia.** The same
   article attributes Phyrexia's decimation to an unnamed group of planeswalkers
   using soul bombs. Their names are not supplied there; do not fabricate a
   named squad or formal faction.

The article presents the two outcomes together as parts of the invasion's
defeat but **does not say which occurred first**. Consequently the new records
do not create a `BEFORE` edge in the L244 chronology. Pack C's earlier C013
was graded IMPLIED on a different source and must not be silently promoted to
an explicit calendar ordering. This fills an official *outcome-source gap*
without pretending to close the remaining *ordering-source gap*.

## Reproduce

```bash
python3 scripts/audit_lore_pack_c5.py --check
python3 scripts/audit_lore_pack_c5.py --live
python3 -m unittest discover -s tests -p test_lore_pack_c5_invasion_outcome.py -q
python3 scripts/build_multiverse_graph.py --check
python3 scripts/build_story_coverage_inventory.py --check
```

`--live` verifies both short quoted passages directly on the official page.
Offline checks and CI cannot independently guarantee that Wizards' live page
is available in future; they verify the committed source registration and
schema. If the source changes, rerun the live check and preserve the conflict.

## Lore-first deck blueprint lead (not a finalized deck)

This is a useful *strict-canon core* for a **Weatherlight / Legacy / downfall
of Yawgmoth** theme. Possible commanders to evaluate using the current Oracle
and deck-building pipeline are *Sisay, Weatherlight Captain* (broad color
access, but the printed gameplay does not literally recreate the Legacy) and
more constrained historically connected commanders such as *Captain Sisay*
or *Gerrard, Weatherlight Hero*. Which best represents the complete narrative
requires a legal color-identity audit, source-grading of each character/artifact,
and a mechanical game-plan review. No commander has been chosen, no deck
approved or locked, and the 62 finalized Grixis decks remain untouched.

Open: an official quoted ordering between the two outcomes, reconciliation of
the differing Yawgmoth credit accounts with Cory, and additional official
Legacy component evidence before constructing a 100-card lore-first list.
