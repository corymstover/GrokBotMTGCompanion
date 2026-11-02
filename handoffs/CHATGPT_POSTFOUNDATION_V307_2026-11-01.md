# MTG Companion v3.07 handoff — first-party set-context joins

**Latest source of truth:** `MTG_MULTIVERSE_MASTER_WORKFLOW.md` v3.07;
`Progress Tracker.md`; `data/release/full_checklist_triage_2026-11-01.json`;
`data/release/set_multiverse_context_acceptance_2026-11-01.json`;
`research/POSTFOUNDATION_SET_CONTEXT_V307_2026-11-01.md`.

## Verified work

- Previous v3.06 PR #976 merged into `main` at
  `4d64fe87a4d7a35f8493744557baa531ac5917cc`; **14/14** PR checks and
  **10/10** exact-main Actions checks passed. Its SHA-pinned v3.00 foundation
  certificate remains **7/7**.
- v3.07 adds first-party, source-local set-context navigation with **12**
  story series, **35** exact official story pages, **136** source/claim/entity
  rows (117 Character, 11 Faction, 8 Plane), three official mechanics
  features and one Wizards Commander release cross-checked against Scryfall
  parent metadata. Nine negative/positive acceptance tests pass locally.
- `--code` queries leave unsupported set context explicitly unknown. No
  inferred canon or individual printing attribution.
- K055's finite **supported** cross-domain capability is marked complete.
  This does **not** certify exhaustive set canon or close K050.
- Checklist now **116/137 checked**, **21** historical unchecked, **15**
  active repository-build items; six deferred pilot-review/upkeep tasks
  excluded from the finish line only.

## Still-open repository-build IDs

K022, K045, K046, K050, K074, K078, K079, K080, K088, K098, K099,
K100, K103, K108, K110. First-party historical set variants/products and
all-time premiere roster, disputed Elder Dragon genealogy, complete
history/chronology, power testing and updated Commander rules are not
truthfully certifiable from currently frozen evidence.

## Owner constraints

- Do not edit **62 owner-approved Grixis lists**.
- Keep the three existing pilot decks **UNAPPROVED**. Cory will rebuild and
  individually review them after the GitHub repository is finished.
- Do not treat pilot sign-off K112–K114 or perpetual monitoring K105,
  K125, K126 as repository construction work; preserve their unchecked
  archival status.
- Do not announce repository-complete until all **15** remaining build IDs
  have independently supported acceptance and green exact-main CI.

## Next actions

1. Publish v3.07 via PR; wait for its exact-head and exact-main CI, then
   record new merge SHA and checks here in the next handoff.
2. Continue the highest-priority unsourced Phase 1B gates K022/K045/K046/
   K050 with actual first-party evidence. Avoid promoting Scryfall taxonomy
   to a Wizards all-time premier-set count.
3. Independently synthesize and validate remaining global chronology,
   genealogy and Commander rules/strategy evidence before closing any item.
