# Phase 2–8: history, chronology and lore-first pilots — source-safe navigation

Date: 2026-10-30. Status: **PRELIMINARY_RESEARCH / engineering tested**, **not owner approved**.

## What is reproducible now

- In-universe chronology: `python3 scripts/query_lore_chronology.py --check` checks the
  entire published transitive closure, node references, exact quote digests, Wizards
  URLs, printed AR-label arithmetic and cycle status without uncommitted page caches.
- Ask whether one named event predates another:
  `python3 scripts/query_lore_chronology.py --compare A:elder_dragon_war A:primeval_rule`.
  The proof cites the Wizards source supporting the Elder Dragon War → Primeval rule.
- Printed dates: `--compare B:kroog_siege B:trench_war` uses **28 AR → 44 AR**
  from the official *Brothers' War* story headers. Both primary-source scene citations
  travel with the arithmetic result.
- Crucial negative example: `--compare C:josu_undead A:eldrazi_imprisoned`
  returns `UNKNOWN`, because the story presents have no sourced cross-page anchor.
  UNKNOWN does not mean these events were simultaneous or never happened.
- Enumerate valid names with `--list`. Results never silently equate the original
  Tarkir timeline with its rewritten replacement; see the proof note on the
  Bolas/Ugin duel → original-timeline dragon extinction edge.

The chronology remains **56 event nodes, 16 independent story presents,
seven printed AR labels, 63 quoted source edges, six derived AR edges,
177 of 3,074 comparable pairs, 13 components, zero cycles**. The **2,897
unorderable pairs** require more official in-universe chronology evidence. These
are not a list of 2,897 independent facts to research; one well-sourced bridge can
resolve many pairs. L222/L244 stay open.

## Plane-by-plane research prioritization

Rebuild/check the machine-readable report:
`python3 scripts/build_plane_history_priorities.py --check`.
It uses only direct claim-bearing edges to the **33 Plane nodes already registered**
in `data/multiverse_graph/multiverse_graph.json`. All 33 have at least one such
claim, but **22 have fewer than five**. The report includes every registered plane,
its distinct claim IDs, source IDs, claim grades, and cautious research priority.
It does **not** claim to enumerate every plane in Magic or to measure the depth of
storytelling about a plane through only this one direct-edge metric.

High-priority examples with just one registered direct claim include Alara,
Argentum, Bablovia and Muraganda. These need *primary-source-backed*
biographies, conflicts, transformations and timelines, not synthetic graph links.
Conversely, heavily cited planes such as Amonkhet (16 direct claims), Ravnica (11)
and Tarkir (10) still need deeper full-history dossiers; node/claim count does not
certify completeness.

## Three independent lore-first Commander pilots

The report reads their **existing spec and proposal artifacts** without altering
any card, source, approval or hash. All remain **UNAPPROVED** and need Cory's
specific judgement. Counts below exclude basic lands and use each card's recorded
research tier, not independent plot-certification:

| Pilot | Direct depiction | Canon reference | Lore-inspired | Mechanical symbol |
| --- | ---: | ---: | ---: | ---: |
| Ugin & Bolas duality | 6 | 54 | 8 | 15 |
| Original Primeval Dragons | 0 | 35 | 12 | 38 |
| Ugin's allies and heroes | 0 | 15 | 32 | 40 |

The main lore compromises are worth reviewing *before* asking for approvals:

1. Ugin and Bolas share the narrative, but Nicol Bolas leads a Grixis deck;
   Ugin's playable cards are necessarily in the 99. Some exact artwork is
   associated with stories but is not necessarily an event depiction.
2. The Ur-Dragon is a mechanics/lineage-inspired five-color commander for the
   Primeval Dragons. This **does not establish** that the Ur-Dragon is their
   canonical parent. Pack A genealogy disputes GD2–GD7 remain owner-gated.
3. Ugin's allies uses Jace as its legal four-color commander. Caption-based
   story connections and mechanics-inspired stand-ins are **not** all directly
   attested allies of Ugin; re-evaluate the theme's fidelity before approval.

Offline auditors (`scripts/audit_lore_pilot.py` and focused CI) check counts,
singleton/identity, recorded snapshot legality, tier provenance and decklist
hashes, but cannot replace a fresh rules/bans/brackets check at release.

## Still to research, with explicit evidence boundaries

- **Phases 2–3:** Complete individual print-specific CardRepresentation IDs,
  16 orphan nodes and 22 display-name-variant triages without inventing identity.
- **Phase 4/L244:** Find a first-party bridge between Thran/Yawgmoth,
  Brothers' War, Weatherlight and Phyrexian Invasion eras. In particular, an
  official recap for Yawgmoth's end/Old Phyrexia would resolve a documented
  novel-era ordering blocker without copying copyrighted prose. Do not subtract
  open-ended span statements or assume two pages have the same story present.
- **Phase 5:** Use the plane priority JSON as a *queue*, not a finished atlas;
  research wars, legends, civilizations, source conflicts and in-world eras
  across first-party canonical planes. Tag alternate or Universes Beyond
  material separately.
- **Phase 6:** Reassess the lore grade of all three pilots against official
  biographies, art/printing provenance and current Oracle; seek Cory's exact
  approval before locking or publishing any final deck.
- **Phase 7:** Broaden hard-question tests for retcons, leaders, deaths,
  chronology and known-unknown questions. `UNKNOWN` is a necessary answer.
- **Phase 8:** Re-run all source, snapshot and exact-head CI checks, monitor new
  stories/rules/cards, and leave release certification blocked until technical,
  source and owner decisions actually pass.

No Grixis approved decks, snapshot locks, or owner approval flags were modified.
