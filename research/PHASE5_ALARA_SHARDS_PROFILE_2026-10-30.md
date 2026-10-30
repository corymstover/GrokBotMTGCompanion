# Phase 5 — Alara's five shards, reunification, and first inter-shard conflicts

**PRELIMINARY_RESEARCH; not owner-approved, not a comprehensive history.**

The official [Wizards of the Coast Alara plane profile](https://magic.wizards.com/en/story/alara-plane)
was independently read on October 30, 2026. All ten short source excerpts
were also checked verbatim against the live page by
`python3 scripts/audit_lore_pack_alara.py --live`.

The ten new claims `ALA001`–`ALA010` preserve distinct, directly attested
facets of this single article:

1. Alara's long-separated regions were **Bant, Esper, Grixis, Jund and Naya**.
   The profile calls them *shards*, not five current independent planes.
2. During separation, each shard had only three mana colors; on reunion the
   single plane once again flowed with all five.
3. The dissolving borders produced cross-cultural war and hostile encounters.
4. Esper sought carmot to create dwindling etherium; its forces invaded shards.
5. Grixis undead attacked neighboring shards for life energy and enslavement.
6. Jund warriors expanded their life hunts into the reunited realm.
7. Naya's armies sought answers to the Anima's visions.
8. Bant's armies defended their homeland under the guardian angels' banner.

The existing `UP001` claim already captures Nicol Bolas's role in engineering
the reunion and feeding on Alara's mana; **it was preserved, not duplicated**.
These claims join only the primary-source profile's actual assertions. They do
not name commanders in the unreported battles, settle every shard's internal
history, infer dates from real-world card releases, or establish a strict
`BEFORE` edge between overlapping reunification and conflicts.

The generated `query_plane_history.py Alara` view now has **five distinct
Alara-direct cited claims** (up from one). The remaining six new records
connect specific regional groups, objects, motives and other shard references
to enable further relationship questions. One source alone cannot certify a
complete plane biography.

## Next research targets

- Trace the origin of the Sundering and the Conflux with separately verified
  official Wizards articles; do not invent exact in-world years.
- Research each shard's named civilizations and major characters, distinguishing
  the five shards' locations from planes.
- Investigate the aftermath of Bolas's plan and individual inter-shard battles;
  do not assume a general motive identifies a named combatant.
- Connect directly represented card printings only with independently verified
  printing/art evidence, never with title similarity alone.

**Files:** `data/lore_research/pack_p5_alara_plane_profile_2026-10-30.json`,
`scripts/audit_lore_pack_alara.py`, and the generated graph, coverage, plane
priority and partial-history reports.
