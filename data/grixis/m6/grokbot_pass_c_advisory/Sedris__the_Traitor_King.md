```json
{"tracker_deck_id": "Sedris__the_Traitor_King", "tracker_index": 50, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "65fbfe3eb64551ad6f5723243fcd62a286610c360e24bd700b584252e1da6365", "source_file_raw_sha256": "65fbfe3eb64551ad6f5723243fcd62a286610c360e24bd700b584252e1da6365", "sha256_match": true, "verdict": "NEEDS VERIFICATION", "adds_cuts": [{"in": "Ghostly Flicker", "out": "Sundial of the Infinite"}], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 43–62 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base ac22ea15; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20; CR 2025-09-25 text"}
```
# Sedris, the Traitor King: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Sedris_the_Traitor_King_Approved_2026-10-15.txt` (blob fc33a249, canonical main ceffdcce), 100 cards. Commander: Sedris, the Traitor King. The raw-file sha256 matches both the tracker and `state/current_deck_overrides.json`. Every card is inside the commander's color identity and officially Commander-legal per Scryfall live /cards/collection (2026-10-20), so no project exception is needed here. Some cards' newest printings carry future release dates (e.g. 2026-11-13 reprints), but each card's Oracle legality is "legal".

**Weaknesses / opportunities**
1. Sedris gives every graveyard creature unearth {2}{B}. The Entomb/Buried Alive/Vile Entomber and reanimation suite is strong (fact).
2. **Sundial of the Infinite doesn't keep unearthed creatures.** Unearth exiles them at "the **next** end step", so ending your turn just moves that to the next opponent's end step. Sundial works only on your turn. The same goes for Obeka and Sneak Attack (CR 702.84, 724; fact).
3. What actually keeps unearthed creatures is a blink, which returns a new object: Deadeye Navigator. Teferi's Veil also works because the delayed trigger resolves while the creature is phased out (fact plus judgment).

**Candidate swaps (proposals for Cory; nothing applied)**
- **+Ghostly Flicker / −Sundial of the Infinite.** It blinks two unearthed creatures (new objects with no unearth exile) at instant speed and re-triggers ETBs. Mono-U and Commander-legal. If Sundial is there for a different line, verify that line first (fact plus judgment).

**Rules notes.**
- Unearth's "if it would leave the battlefield, exile it instead" also applies to blink. The card is exiled anyway and comes back as a new object (CR 702.84a; fact).

**Verdict:** NEEDS VERIFICATION.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- From the tracker, only the order, deck id and canonical hash were read (plus the entry's field names, not their values). The `approved_list_sha256` in state/current_deck_overrides.json was matched. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #43–#62, tracker indices 42–61), not a card-by-card audit. Each KEEP names the weakest slots considered and the best rejected alternative. KEEPs are not certificates.
