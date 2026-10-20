```json
{"tracker_deck_id": "Tresserhorn_s_Lord__Returned", "tracker_index": 59, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "8c802586a4742156fb96246f4f23331eb51d1a77d6717da63ceed2446e98adf8", "source_file_raw_sha256": "8c802586a4742156fb96246f4f23331eb51d1a77d6717da63ceed2446e98adf8", "sha256_match": true, "verdict": "NEEDS VERIFICATION", "adds_cuts": [], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 43–62 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base ac22ea15; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20; CR 2025-09-25 text"}
```
# Tresserhorn's Lord, Returned: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Tresserhorn_s_Lord_Returned_Approved_2026-10-15.txt` (blob 767089b6, canonical main ceffdcce), 100 cards. Commander: Tresserhorn's Lord, Returned. The raw-file sha256 matches both the tracker and `state/current_deck_overrides.json`. All cards are within color identity. Official legality per Scryfall live (2026-10-20): **the commander is not_legal** (MBC). Every other card is legal.

**Weaknesses / opportunities**
1. A sacrifice shell where every creature sacrifice draws. The deck has token makers (Bitterblossom, Mogg War Marshal, Endrek Sahr, The Locust God) and loop pieces (Gravecrawler, Bloodghast, Phyrexian Altar) (fact).
2. **Legality pending:** Scryfall lists **Tresserhorn's Lord, Returned** (the commander) as Commander **not_legal** (MBC 2026-10-19). It's not a 2026-11-13 future release (fact).
3. **Weakest slots considered:** Infantry Shield and Chasm Skulker (judgment).

**Candidate swaps (proposals for Cory; nothing applied)**
- None until legality is settled.

**Rules notes.**
- Indestructible doesn't stop the ETB sacrifice. If it's sacrificed, its own 'whenever you sacrifice a creature' trigger still draws, as a leaves-the-battlefield look-back (CR 603.10a; judgment, fact-based).
- Paying the ETB means sacrificing three creatures, which draws you 3. The opponent's 3 draws are symmetrical value (fact).

**Verdict:** NEEDS VERIFICATION.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- From the tracker, only the order, deck id and canonical hash were read (plus the entry's field names, not their values). The `approved_list_sha256` in state/current_deck_overrides.json was matched. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #43–#62, tracker indices 42–61), not a card-by-card audit. Each KEEP names the weakest slots considered and the best rejected alternative. KEEPs are not certificates.
