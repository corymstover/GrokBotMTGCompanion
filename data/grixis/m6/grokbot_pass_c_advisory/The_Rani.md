```json
{"tracker_deck_id": "The_Rani", "tracker_index": 56, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "7220937ed5817b4ef9cacd2463a3434b98ae58690ffa1d7ef440881ba97d729c", "source_file_raw_sha256": "7220937ed5817b4ef9cacd2463a3434b98ae58690ffa1d7ef440881ba97d729c", "sha256_match": true, "verdict": "KEEP", "adds_cuts": [], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 43–62 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base ac22ea15; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20; CR 2025-09-25 text"}
```
# The Rani: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/The_Rani_Approved_2026-10-15.txt` (blob f65ef47b, canonical main ceffdcce), 100 cards. Commander: The Rani. The raw-file sha256 matches both the tracker and `state/current_deck_overrides.json`. Every card is inside the commander's color identity and officially Commander-legal per Scryfall live /cards/collection (2026-10-20), so no project exception is needed here. Some cards' newest printings carry future release dates (e.g. 2026-11-13 reprints), but each card's Oracle legality is "legal".

**Weaknesses / opportunities**
1. Goad Auras on ETB and attack, plus investigate. Forced combat comes from the Impetus cycle, Disrupt Decorum, Grenzo, Karazikar and Kardur, and Urza and Academy Manufactor turn Clues into value (fact).
2. **Weakest slots considered:** Five Hundred Year Diary and Curse of Opulence (judgment).
3. **Best rejected alternative:** Cunning Rhetoric-style taxes. They don't goad, so they miss The Rani's investigate payoff (judgment).

**Candidate swaps (proposals for Cory; nothing applied)**
- None. KEEP is a low-confidence judgment. See the weakest slots and rejected alternative above.

**Rules notes.**
- **Force of Will pitch count (independently verified):** the 99 has 24 blue nonland cards. Dimir Signet, Izzet Signet and the Creativity and Dominance Talismans have blue **identity** but are colorless, so they can't be pitched (Oracle/CR 105.2c fact).
- Mark of the Rani must target **another** creature, and each enchanted creature gets +2/+2 and is goaded (fact).

**Verdict:** KEEP.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- The orchestrator saw the handoff caveat that the FoW count excludes colorless blue-identity rocks. I verified it here from Oracle data.
- From the tracker, only the order, deck id and canonical hash were read (plus the entry's field names, not their values). The `approved_list_sha256` in state/current_deck_overrides.json was matched. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #43–#62, tracker indices 42–61), not a card-by-card audit. Each KEEP names the weakest slots considered and the best rejected alternative. KEEPs are not certificates.
