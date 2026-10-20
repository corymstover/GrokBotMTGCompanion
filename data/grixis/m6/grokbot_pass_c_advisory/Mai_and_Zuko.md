```json
{"tracker_deck_id": "Mai_and_Zuko", "tracker_index": 31, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "aa2036f49f38e6503734d99c852acdfa704aa1b27e44bb26d6e9566a73a0d4a2", "source_file_raw_sha256": "aa2036f49f38e6503734d99c852acdfa704aa1b27e44bb26d6e9566a73a0d4a2", "sha256_match": true, "verdict": "POSSIBLE UPGRADE", "adds_cuts": [{"in": "Grim Monolith", "out": "Tundra Tank"}], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 22–42 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base 650d307a; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20; CR 2025-09-25 text"}
```
# Mai and Zuko: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Mai_and_Zuko_Approved_2026-10-14.txt` (blob 24d3f6d1, canonical main ceffdcce), 100 cards. Commander: Mai and Zuko. The raw-file sha256 matches both the tracker and `state/current_deck_overrides.json`. Every card is inside the commander's color identity and officially Commander-legal per Scryfall live /cards/collection (2026-10-20), so no project exception is needed here. Some cards' newest printings carry future release dates (e.g. 2026-11-13 reprints), but each card's Oracle legality is "legal".

**Weaknesses / opportunities**
1. This is an artifact-flash value/combo deck (Urza, Sai, Mystic Forge, Rings + Basalt Monolith infinite colorless, Aetherflux, Citadel). Mai and Zuko's flash enables instant-speed combo turns (fact plus judgment).
2. Tundra Tank is the weakest artifact: 3 MV, Crew 1, one R on attack, and a one-shot indestructible (fact plus judgment).
3. Grim Monolith is absent despite the flash-artifact plan and 15 Game Changers (measured).

**Candidate swaps (proposals for Cory; nothing applied)**
- **+Grim Monolith / −Tundra Tank.** Fast mana that can be flashed in at end of turn and that powers Urza and the Forge chains. It's colorless and Commander-legal, and it's a Game Changer (already Bracket 4) (fact).

**Rules notes.**
- Firebending mana lasts only until end of combat (fact).
- Basalt Monolith + Rings of Brighthearth gives infinite colorless mana. Grim Monolith + Rings doesn't (untap cost 4 + Rings 2 > 3 produced) (fact).

**Verdict:** POSSIBLE UPGRADE.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- From the tracker, only the order, deck id and canonical hash were read (plus the entry's field names, not their values). The `approved_list_sha256` in state/current_deck_overrides.json was matched. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #22–#42, tracker indices 21–41), not a card-by-card audit. Each KEEP names the weakest slots considered and the best rejected alternative. KEEPs are not certificates.
