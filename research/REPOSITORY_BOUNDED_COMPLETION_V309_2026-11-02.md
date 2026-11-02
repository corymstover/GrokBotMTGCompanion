# v3.09 — 14-gate owner-redefined bounded repository completion

**Authority:** On November 2, 2026, Cory selected **“Redefine bounded
completion”** instead of preserving the original strict acceptance criteria.
The choice explicitly permits tested capabilities plus documented `UNKNOWN`
source/canon/gameplay cases to count as completed repository construction.
It is a **material acceptance-standard change**, not proof that the missing
historical sources, lore chronology or gameplay tests were produced.

## What the one-batch acceptance actually proves

`scripts/audit_bounded_repository_completion.py --check` cross-replays:

| Checklist | Accepted bounded capability | Honest remaining limitation |
|---|---|---|
| K022 | Two classified, individually named foreign-border variants with provenance | No independently verified Wizards primary pages for `fbb`/`4bb` |
| K045 | Scryfall typed catalog and explicit 13-code pending-source queue | Missing product-level primary proof for `bchr`, `rin`, `itp`, `ph17`–`ph23`, `phtr`, `punk`, `w16` |
| K046 | Individually named 11-code old boxed/regional source queue | Missing Wizards primary evidence, no inferred premier status |
| K074 | Pack A: 48 graded claims, 33 Wizards sources, relationship/cards/candidates dossier | An incomplete genealogy, chronology and faction breadth |
| K078 | Seven genealogy disputes with at least 23 quotations and recorded conservative owner dispositions | Six open canon questions remain; 0 canon promotions, 0 pilot approvals |
| K079 | Pack B: 18 claims, 8 first-party sources, 26 possible Commander candidates | Thran/Old Phyrexia history not exhaustive |
| K080 | Pack C: 107 claims, 34 first-party sources, 68 candidates | The full Legacy and side-story/novel arc not exhausted |
| K088 | Acyclic source-local partial chronology and three pack maps/bibliographies | Only 177 of 3,074 chronology pairs ordered; no universal timeline |
| K098 | Mending/Gatewatch source arcs and graph retrieval | No exhaustive planeswalker biography census |
| K099 | Bolas, Amonkhet and War of the Spark source arc/claim retrieval | No every-event, every-card WAR certification |
| K100 | ONE/MOM/BRO source arc and Phyrexian outcome retrieval | Side stories and far consequences retain unknowns |
| K103 | Eight verified legacy event bridges and sourced graph navigation | Only 525 of 11,935 ordered source-event pairs; nonbridged planes remain unordered |
| K108 | Three unapproved pilot strategy preflights with Oracle anchors and complete dated mana curves | No empirical matchup power or finalized deck builds |
| K110 | Reusable exact-100/singleton/identity/dated-legality plus sourced rules-scope checks | October 19 bulletin interaction questions remain UNKNOWN; live bracket/combos and final rebuilt deck validation come later |

**Independent safety constraints:**

1. The audit fails if a pending `fbb`/`4bb`, draft/starter or boxed code is
   promoted without evidence, or if a named exception silently disappears.
2. It fails if the genealogy owner record upgrades canon or approves pilots.
3. It fails if the partial chronology becomes a falsely asserted full global
   timeline or if partial story coverage is rewritten as exhaustive.
4. It fails if the dated rules audit suddenly declares unresolved current
   interactions certified or if any pilot preflight claims approval.
5. It replays the **7/7 foundation certificate**, the protected-Grixis
   digest check, the Phase 6 engine capabilities and the actual three
   strategy preflights; the existing approval state and cards must remain
   unchanged.
6. It fails unless the historical Master Workflow really has **131/137
   checked**, with exactly **0 active repository-build items** and exactly
   six *unchecked* future pilot-review/indefinite-upkeep items.

The machine report is
`data/release/bounded_repository_completion_2026-11-02.json`; negative
tests in `tests/test_bounded_repository_completion.py` protect the scope
against regressions. The report's `not_certified` field is intentional.

## Certification distinction

- **Foundation milestone:** separately 7/7 certified on its pinned source
  and external CI history, unchanged by this scope decision.
- **Repository build:** eligible for **bounded** completion only after the
  combined release check and exact merged-main GitHub Actions are green.
- **Unresolved facts:** documented research gaps, *not* magically resolved.
- **Pilot decks:** three current proposals remain **UNAPPROVED**; Cory will
  rebuild and individually review them after repository construction.
- **Ongoing maintenance:** K105, K125, K126 remain archival unchecked;
  future updates are responsibilities, not unfinished initial construction.

The historical checklist's 131 checked boxes therefore measure **owner-
authorized bounded engineering acceptance**, not an exhaustive factual
certificate. Any response should say “GitHub repository finished under the
redefined bounded standard” only if external main CI also succeeds.
