# Phase 7 — Commander Q&A eligibility and currentness guard (2026-10-31)

## Issue reproduced and correction

`scripts/commander_rules.py include CARD --commander LEADER` previously checked
the candidate's color identity and archived Scryfall legality, but never checked
whether `LEADER` was eligible or legal as a commander. For two names it applied
their combined colors without checking a shared partner ability. Thus a valid
colorless card such as Sol Ring could be reported `allowed: true` in a
Griselbrand-led deck, a nonlegendary-creature-led deck, or a pair with no valid
partner mechanic. The same Commander routes returned `VERIFIED` even though
they used dated card-shard legality and a 2026-09-25 CR excerpt, not a live ban
list or refreshed Oracle ruling.

The inclusion route now calls the same deterministic commander eligibility and
pairing check used by the stand-alone Commander question, rejects an invalid
configuration, and exposes `commander_configuration.allowed` alongside the
candidate-specific reasons. It also refuses empty and more-than-two leader
lists with `NOT_FOUND` and `INVALID_COMMANDER_COUNT`. The answer is **always
QUALIFIED** when a known card is evaluated from the archived data: flag
`DATED_SCRYFALL_LEGALITY_NOT_LIVE`, `card_data_as_of: 2026-10-15`, and the
existing official `rules_source.effective: 2026-09-25`. A current live
legality check is still required for deck finalization.

## Independent adversarial checks

`tests/test_commander_deck_config_safety.py` uses explicitly synthetic records,
not the protected Grixis deck collection or any owner-approval artifact. It
tests the expected `False` for a banned commander, an ordinary nonlegendary
creature, an invalid pair with a banned commander, and a pair with no common
partner ability. It preserves `True` for an eligible single leader and a
valid partner pair while retaining qualified confidence. The ordinary
`mv_ask ask` route is exercised in both a positive and negative case. Missing
and excessive leader counts are kept out of the supported route. This file
is included in the Phase 7 Action's PR and push triggers.

Local verification at this checkpoint:

```
python3 -m unittest tests.test_commander_deck_config_safety -q
# Ran 4 tests — OK
```

The older `test_commander_rules.py` contract is updated to expect qualified
historical answers. It requires the full card shards for its end-to-end run;
full-checkout GitHub CI must validate that suite and the rest of Phase 7.
No broader historical or rules data was changed, no official current bans are
asserted, and no foundation-release gate is being signed off.

## Remaining work

- Independently test more complex real-card interactions and Commander-specific
  exceptions against current, authoritative Oracle/rules/ban evidence.
- Continue cross-era source-backed history and graph research; do not promote
  historical citation publication dates into in-universe chronology.
- Preserve the original hash-locked snapshots, all 62 approved Grixis lists,
  and the three explicitly unapproved parked lore-deck pilots.
- Run exact-head GitHub CI and maintain **89/137 / 48 open / NOT_RELEASE_READY**
  until evidence justifies a real checklist change.
