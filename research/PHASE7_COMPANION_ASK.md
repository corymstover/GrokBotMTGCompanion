# Phase 7: companion question entry point with confidence flags (v1)

Status: engineering milestone, tests passing. This is not a complete Phase 7 QA companion.

`scripts/mv_ask.py` is one entry point for questions (`card`, `lore`, `ask`). Every answer is wrapped in an
envelope with `confidence` (VERIFIED / QUALIFIED / NOT_FOUND), named `flags`, `data_as_of` and `sources`:

- **Card lookups** read `data/card_index.csv` and the matching `cards/` shard section. They return Oracle text separately from flavor text, plus type, color identity, Commander legality, Game Changer status, ruling count and the Scryfall link. Index records built from the 2026-10-15 Oracle bulk are flagged `STALE_ORACLE_VS_CURRENT_SNAPSHOT` against the active snap-20261029, so the answer is QUALIFIED rather than VERIFIED.
- **Lore** answers come only from the cited Phase 3 claim graph. Relations are grouped by canon status, and each carries its claim summary, limitation, stage and Wizards source URLs. Any disputed, open-question or alternate-continuity claim makes the answer QUALIFIED and adds a flag. Ambiguous names (for example "Nicol Bolas" as both character and card) are flagged `AMBIGUOUS_NAME`, with the card pointer kept.
- **No evidence** returns `NOT_FOUND`, `NO_CITED_LORE` and exit code 3. The companion never guesses.

Example questions covered by tests: "Who is Urza's brother?", "Where did the Golgothian Sylex come from?" (DISPUTED; competing legends), "Who destroyed the Golgothian Sylex?" (inverse direction), "Nicol Bolas" (ambiguous, open question), "Who is Zorblax the Unreal?" (NOT_FOUND).

Not yet covered: set questions (use `scripts/set_atlas_lookup.py` / `historical_set_lookup.py` with the snapshot), rules-interaction explanations, Commander recommendations, and free-text parsing beyond a few patterns.
