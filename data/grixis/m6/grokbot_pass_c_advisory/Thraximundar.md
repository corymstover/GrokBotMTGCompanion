```json
{"tracker_deck_id": "Thraximundar", "tracker_index": 58, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "d4fa3421752a4d666528c5218aa18b240465c817dd160642c103b2de8c3f9442", "source_file_raw_sha256": "d4fa3421752a4d666528c5218aa18b240465c817dd160642c103b2de8c3f9442", "sha256_match": true, "verdict": "KEEP", "adds_cuts": [], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 43–62 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base ac22ea15; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20; CR 2025-09-25 text"}
```
# Thraximundar: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Thraximundar_Approved_2026-10-15.txt` (blob be5c2cad, canonical main ceffdcce), 100 cards. Commander: Thraximundar. The raw-file sha256 matches both the tracker and `state/current_deck_overrides.json`. Every card is inside the commander's color identity and officially Commander-legal per Scryfall live /cards/collection (2026-10-20), so no project exception is needed here. Some cards' newest printings carry future release dates (e.g. 2026-11-13 reprints), but each card's Oracle legality is "legal".

**Weaknesses / opportunities**
1. Attack edicts grow Thraximundar, with Grave Pact/Dictate and the aristocrat shell. Gravecrawler + Phyrexian Altar + a drain is a loop. Rooftop Storm makes Zombie spells, Thraximundar included, cost {0} plus tax (fact).
2. **Weakest slots considered:** Necrotic Hex (6 MV) and Mahadi, Emporium Master (judgment).
3. **Best rejected alternative:** Butcher of Malakir. At 7 MV it duplicates Grave Pact and Dictate (judgment).

**Candidate swaps (proposals for Cory; nothing applied)**
- None. KEEP is a low-confidence judgment. See the weakest slots and rejected alternative above.

**Rules notes.**
- Rooftop Storm waives only the mana cost. Commander tax is still paid (fact).

**Verdict:** KEEP.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- From the tracker, only the order, deck id and canonical hash were read (plus the entry's field names, not their values). The `approved_list_sha256` in state/current_deck_overrides.json was matched. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #43–#62, tracker indices 42–61), not a card-by-card audit. Each KEEP names the weakest slots considered and the best rejected alternative. KEEPs are not certificates.
