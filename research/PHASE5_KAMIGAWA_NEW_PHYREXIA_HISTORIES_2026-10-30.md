# Phase 4/5 — Kamigawa and early New Phyrexia historical dossiers

**Preliminary, source-graded knowledge work; NOT deckbuilding or owner certification.**

Twenty new claims (`KMH001`–`KMH012`, `NPHH001`–`NPHH008`) were
audited with `python3 scripts/audit_lore_plane_history_batch.py --live`
against three official Wizards of the Coast primary sources:

- [Kamigawa overview](https://magic.wizards.com/en/story/kamigawa-plane)
- [Planeswalker's Guide to Kamigawa: Neon Dynasty](https://magic.wizards.com/en/news/feature/planeswalkers-guide-kamigawa-neon-dynasty-2022-02-03)
- [New Phyrexia overview](https://magic.wizards.com/en/story/new-phyrexia-plane)

The historical Kamigawa pack connects the material/spirit realms, the
Reito massacre and the Kami War, Konda's imprisonment of O-Kagachi's
fragment, the emergence of Kyodai, and Kyodai and Michiko's victory.
It then traces the breakdown of the realm barrier, the unpredictable
merge sites, the founding of the Imperial organization, its later role
in government, the Kyodai bond for the emperor, and the tension with
the Saiba Futurists over technology. The source explicitly says **1,200
years ago** from its Neon Dynasty narrative standpoint; this is quoted
metadata and is not converted to AR. The older official profile explicitly
describes the **next twenty years** following the war's opening.

The New Phyrexia pack connects Memnarch's abducted populations,
Karn's introduction of the Phyrexian oil, underground transformation,
the campaign to compleat Mirrodin, Mirran military resistance,
Koth/Elspeth/Venser's early opposition, and the competing praetor factions
described in the *undated, historically situated* official profile.
It must **not** answer a question about the current ruler using that
profile's stale present tense. Newer stories have a separate evidence
timeline, so a one-page primer cannot supersede them.

## Regeneration and honest limits

- Existing official source-register IDs `up_kamigawa`, `neo_guide` and
  `up_nph` are reused without changing their metadata.
- All new claims are explicitly marked `CANON_CONFIRMED`, with a cited
  short excerpt, event-stage label and individual limitation; neither
  pack claims owner approval.
- Exact graph, date quote extraction, claim-to-card anchor sidecar,
  plane dossiers and priority ranking are regenerated together.
- `scripts/mv_ask.py ask 'What is the history of Kamigawa?'` and the
  corresponding New Phyrexia question retain `QUALIFIED` answers and
  `NO_VERIFIED_TOTAL_CHRONOLOGY`.
- The 33 currently registered planes remain a limited graph sample,
  **not an enumeration of every Magic plane**. A higher direct-claim count
  is progress, not proof of comprehensive history or complete chronology.
- Phase 6 lore decks and three existing pilot draft approvals remain
  deferred until the knowledge foundation passes its independent release.
  The 62 Grixis decks and owner approvals remain untouched.

**Next:** deeper conflict chronology, cross-plane causation, additional
thin plane dossiers and difficult evidence-backed questions. No deck edits.
