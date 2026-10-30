# Phase 7 — Cited plane histories through the normal Q&A entry point

**Engineering feature, not an owner approval or certification.**

The earlier Phase 5 plane-history dossiers already compiled exact claim IDs,
Wizards URLs, confidence grades, limitations and directly attested relations.
This change exposes those existing facts to natural-language questions through
`scripts/mv_ask.py ask`, rather than requiring users to know the separate
history CLI command.

```bash
python3 scripts/mv_ask.py ask 'What is the history of Alara?'
python3 scripts/mv_ask.py ask 'Tell me about the history of Theros'
python3 scripts/mv_ask.py ask 'What happened on Phyrexia?'
```

Each response has the same envelope used by other Q&A queries: `route`,
`query`, `confidence`, `flags`, `data_as_of`, `sources` and `result`.

- `route=ask->plane_history` only for an **exact registered Plane**.
- `confidence=QUALIFIED` even if every selected claim is individually
  `CANON_CONFIRMED`, because the registered graph is incomplete.
- `PARTIAL_REGISTERED_PLANE_HISTORY` and `NO_VERIFIED_TOTAL_CHRONOLOGY`
  are mandatory, and disputed/implied/open/alternate claim grades remain visible.
- A claim naming several shards appears **once** with several relationship
  rows; it is not accidentally counted as five independent historical claims.
- Unknown plane names return to normal general lookup, with no statement that
  the named plane does not exist in the Magic multiverse.
- Oracle rules, commander-construction and existing lore queries keep their
  original routes; no card printing or approved deck was modified.

**Regression tests:** `tests/test_mv_ask_plane_history.py`. The integration
also participates in the existing `test_mv_ask*.py` CI matrix.

## Corrected historical count

This implementation independently checked the generated Theros dossier and
found **six** directly incident distinct claims: three from prior packs and
new claims `THP001`, `THP002`, `THP010`. The v2.51 narrative saying *five*
was a **prose-only counting error**. The generated dossier and graph were
already correct. The Master Workflow and Theros research report have been
corrected in v2.52 without changing facts, grades, or owner status.
