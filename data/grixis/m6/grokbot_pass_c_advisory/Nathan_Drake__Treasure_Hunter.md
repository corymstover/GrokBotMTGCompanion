```json
{"tracker_deck_id": "Nathan_Drake__Treasure_Hunter", "tracker_index": 38, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "a5d59afc3a78d7ff6454b1d011c82c2f732e11f4d4dd03256df1195a3abe9ba0", "source_file_raw_sha256": "a5d59afc3a78d7ff6454b1d011c82c2f732e11f4d4dd03256df1195a3abe9ba0", "sha256_match": true, "verdict": "KEEP", "adds_cuts": [], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 22–42 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base 650d307a; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20; CR 2025-09-25 text"}
```
# Nathan Drake, Treasure Hunter: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Nathan_Drake_Treasure_Hunter_Approved_2026-10-15.txt` (blob 1cfc4be1, canonical main ceffdcce), 100 cards. Commander: Nathan Drake, Treasure Hunter. The raw-file sha256 matches both the tracker and `state/current_deck_overrides.json`. Every card is inside the commander's color identity and officially Commander-legal per Scryfall live /cards/collection (2026-10-20), so no project exception is needed here. Some cards' newest printings carry future release dates (e.g. 2026-11-13 reprints), but each card's Oracle legality is "legal".

**Weaknesses / opportunities**
1. The theft/impulse shell (Gonti, Thief of Sanity, Black Cat, Tinybones the Pickpocket, Robber of the Rich) fits Nathan's "spend mana as any color" clause (judgment).
2. **Weakest slots considered:** Plargg and Nassari (opponents choose the best card away) and Passionate Archaeologist (judgment).
3. **Best rejected alternative:** Hullbreacher-style effects are banned. Smothering Tithe is outside the colors (fact).

**Candidate swaps (proposals for Cory; nothing applied)**
- None. KEEP is a low-confidence judgment. See the weakest slots and rejected alternative above.

**Rules notes.**
- Nathan's any-color mana applies only to spells you don't own and to abilities of permanents you control but don't own (fact).

**Verdict:** KEEP.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- From the tracker, only the order, deck id and canonical hash were read (plus the entry's field names, not their values). The `approved_list_sha256` in state/current_deck_overrides.json was matched. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #22–#42, tracker indices 21–41), not a card-by-card audit. Each KEEP names the weakest slots considered and the best rejected alternative. KEEPs are not certificates.
