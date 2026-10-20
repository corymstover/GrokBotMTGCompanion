```json
{"tracker_deck_id": "Marchesa__the_Black_Rose", "tracker_index": 34, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "627b07f6466c0a48f16daea58ee9c01bba02c2b7fb4de76a37b14a7f75ad7f9b", "source_file_raw_sha256": "627b07f6466c0a48f16daea58ee9c01bba02c2b7fb4de76a37b14a7f75ad7f9b", "sha256_match": true, "verdict": "KEEP", "adds_cuts": [], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 22–42 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base 650d307a; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20; CR 2025-09-25 text"}
```
# Marchesa, the Black Rose: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Marchesa_the_Black_Rose_Approved_2026-10-15.txt` (blob e2103936, canonical main ceffdcce), 100 cards. Commander: Marchesa, the Black Rose. The raw-file sha256 matches both the tracker and `state/current_deck_overrides.json`. Every card is inside the commander's color identity and officially Commander-legal per Scryfall live /cards/collection (2026-10-20), so no project exception is needed here. Some cards' newest printings carry future release dates (e.g. 2026-11-13 reprints), but each card's Oracle legality is "legal".

**Weaknesses / opportunities**
1. The aristocrats/dethrone recursion (Altars, Grave Pact, Blood Artist, Gray Merchant, Mikaeus the Unhallowed, Ozolith) is coherent (judgment).
2. **Weakest slots considered:** Danny Pink (counter-draw on top of a counter theme) and Twilight Diviner (judgment).
3. **Best rejected alternative:** Blowfly Infestation for Twilight Diviner. It's another counter payoff, but the board is already counter-dense (judgment).

**Candidate swaps (proposals for Cory; nothing applied)**
- None. KEEP is a low-confidence judgment. See the weakest slots and rejected alternative above.

**Rules notes.**
- Yawgmoth's −1/−1 counters annihilate +1/+1 counters (CR 704.5q), which can switch off Marchesa's return. Order the activations with care (fact).
- A creature with undying and a +1/+1 counter that dies returns via Marchesa at end step, not via undying (fact).

**Verdict:** KEEP.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- From the tracker, only the order, deck id and canonical hash were read (plus the entry's field names, not their values). The `approved_list_sha256` in state/current_deck_overrides.json was matched. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #22–#42, tracker indices 21–41), not a card-by-card audit. Each KEEP names the weakest slots considered and the best rejected alternative. KEEPs are not certificates.
