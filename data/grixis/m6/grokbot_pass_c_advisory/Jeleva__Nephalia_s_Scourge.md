```json
{"tracker_deck_id": "Jeleva__Nephalia_s_Scourge", "tracker_index": 23, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "00e3f52118f5944684ebc49a5398acf8184f7ca878e861221e4c99931191bc2f", "source_file_raw_sha256": "00e3f52118f5944684ebc49a5398acf8184f7ca878e861221e4c99931191bc2f", "sha256_match": true, "verdict": "POSSIBLE UPGRADE", "adds_cuts": [{"in": "Intuition", "out": "Long-Term Plans"}], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 22–42 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base 650d307a; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20; CR 2025-09-25 text"}
```
# Jeleva, Nephalia's Scourge: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Jeleva_Nephalia_s_Scourge_Approved_2026-10-14.txt` (blob 8cdc5b5a, canonical main ceffdcce), 100 cards. Commander: Jeleva, Nephalia's Scourge. The raw-file sha256 matches both the tracker and `state/current_deck_overrides.json`. Every card is inside the commander's color identity and officially Commander-legal per Scryfall live /cards/collection (2026-10-20), so no project exception is needed here. Some cards' newest printings carry future release dates (e.g. 2026-11-13 reprints), but each card's Oracle legality is "legal".

**Weaknesses / opportunities**
1. This is a cEDH turbo shell (Doomsday, Breach/LED/Brain Freeze, Ad Nauseam, Mind's Desire) at the natural ceiling. Jeleva's attack-cast is the value layer (judgment).
2. Long-Term Plans is the weakest tutor. It costs 3 and puts the card third from the top, so it needs Brainstorm, Top or Scroll Rack to arrive in time (fact plus judgment).
3. Torch Courier and Arena of Glory are haste slots for Jeleva. They're fine, but they're low-impact when Jeleva isn't the plan (judgment).

**Candidate swaps (proposals for Cory; nothing applied)**
- **+Intuition / −Long-Term Plans.** Same mana value, also an instant. Intuition puts the card in hand or sets up the graveyard (Breach/LED and Doomsday piles) instead of the third-from-top delay. It's mono-U and Commander-legal, and it's a Game Changer, but the deck is already Bracket 4/5 (fact).

**Rules notes.**
- Jeleva's free cast covers only **instants and sorceries** exiled by her own ETB, and only when she attacks (fact). A recast resets X, but the old exiled cards stay "exiled with" the old object and become inaccessible (fact, CR 607).

**Verdict:** POSSIBLE UPGRADE.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- From the tracker, only the order, deck id and canonical hash were read (plus the entry's field names, not their values). The `approved_list_sha256` in state/current_deck_overrides.json was matched. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #22–#42, tracker indices 21–41), not a card-by-card audit. Each KEEP names the weakest slots considered and the best rejected alternative. KEEPs are not certificates.
