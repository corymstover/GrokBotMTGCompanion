```json
{"tracker_deck_id": "Marchesa__Dealer_of_Death", "tracker_index": 33, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "34a6a940c54aaebde612ae5d3a244e22931d3a977fa26e4c43f2a76aafc0f6b1", "source_file_raw_sha256": "34a6a940c54aaebde612ae5d3a244e22931d3a977fa26e4c43f2a76aafc0f6b1", "sha256_match": true, "verdict": "KEEP", "adds_cuts": [], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 22–42 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base 650d307a; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20; CR 2025-09-25 text"}
```
# Marchesa, Dealer of Death: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Marchesa_Dealer_of_Death_Approved_2026-10-15.txt` (blob 9e19b7a7, canonical main ceffdcce), 100 cards. Commander: Marchesa, Dealer of Death. The raw-file sha256 matches both the tracker and `state/current_deck_overrides.json`. Every card is inside the commander's color identity and officially Commander-legal per Scryfall live /cards/collection (2026-10-20), so no project exception is needed here. Some cards' newest printings carry future release dates (e.g. 2026-11-13 reprints), but each card's Oracle legality is "legal".

**Weaknesses / opportunities**
1. This is a cEDH crime shell. Targeted interaction and Hex Parasite / Spellskite-style crimes fuel Marchesa's {1} dig, alongside Oracle, Breach and Ad Nauseam (judgment).
2. **Weakest slots considered:** Hawkeye's Bow (an equipment ping that doesn't target, so it's no crime) and Rain of Filth (judgment).
3. **Best rejected alternative:** Intuition for Hawkeye's Bow. The deck already has dense instant tutors, and Bow is cheap repeatable damage (judgment).

**Candidate swaps (proposals for Cory; nothing applied)**
- None. KEEP is a low-confidence judgment. See the weakest slots and rejected alternative above.

**Rules notes.**
- A crime requires **targeting** an opponent, their permanents, spells or graveyard cards. Non-targeting effects don't trigger Marchesa (fact).
- Birgi is listed as `Birgi, God of Storytelling` (the front face of the MDFC Birgi // Harnfel). It's Oracle-resolved and legal (fact).

**Verdict:** KEEP.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- From the tracker, only the order, deck id and canonical hash were read (plus the entry's field names, not their values). The `approved_list_sha256` in state/current_deck_overrides.json was matched. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #22–#42, tracker indices 21–41), not a card-by-card audit. Each KEEP names the weakest slots considered and the best rejected alternative. KEEPs are not certificates.
