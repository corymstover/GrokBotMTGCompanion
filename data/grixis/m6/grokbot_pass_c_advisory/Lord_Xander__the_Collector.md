```json
{"tracker_deck_id": "Lord_Xander__the_Collector", "tracker_index": 29, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "92cdc2f9c1a3583ccf6a311679db66bef825dac2902761859e929f268b6b4787", "source_file_raw_sha256": "92cdc2f9c1a3583ccf6a311679db66bef825dac2902761859e929f268b6b4787", "sha256_match": true, "verdict": "KEEP", "adds_cuts": [], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 22–42 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base 650d307a; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20; CR 2025-09-25 text"}
```
# Lord Xander, the Collector: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Lord_Xander_the_Collector_Approved_2026-10-14.txt` (blob 025aa284, canonical main ceffdcce), 100 cards. Commander: Lord Xander, the Collector. The raw-file sha256 matches both the tracker and `state/current_deck_overrides.json`. Every card is inside the commander's color identity and officially Commander-legal per Scryfall live /cards/collection (2026-10-20), so no project exception is needed here. Some cards' newest printings carry future release dates (e.g. 2026-11-13 reprints), but each card's Oracle legality is "legal".

**Weaknesses / opportunities**
1. The mill plan is coherent. Xander's attack (mill half) with Bruvac (double) mills an entire library. Duskmantle Guildmage + Mindcrank is an infinite loop. Auton Soldier (a nonlegendary myriad copy of Xander) and Blade of Selves multiply the attack trigger (fact plus judgment).
2. **Weakest slots considered:** Feign Death (a narrow Saw-in-Half-style trick) and Cruel Calculations (draw that's only good after a mill) (judgment).
3. **Best rejected alternative:** Phenax, God of Deception for Feign Death. It's sorcery-speed redundancy that doesn't interact with Xander's half-mill math (judgment).

**Candidate swaps (proposals for Cory; nothing applied)**
- None. KEEP is a low-confidence judgment. See the weakest slots and rejected alternative above.

**Rules notes.**
- Bruvac doubles the halved amount: half rounded down, ×2, so an odd library leaves 1 card (fact).
- Persist can't return Xander (he's legendary), but it can return Auton Soldier, which may still enter as a copy (fact).

**Verdict:** KEEP.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- From the tracker, only the order, deck id and canonical hash were read (plus the entry's field names, not their values). The `approved_list_sha256` in state/current_deck_overrides.json was matched. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #22–#42, tracker indices 21–41), not a card-by-card audit. Each KEEP names the weakest slots considered and the best rejected alternative. KEEPs are not certificates.
