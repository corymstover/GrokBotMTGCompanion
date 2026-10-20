```json
{"tracker_deck_id": "Saruman__the_White_Hand", "tracker_index": 47, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "4981499230898c8b36c6f46b0f60a5277630d92abe477d48ed77091e2203ffe2", "source_file_raw_sha256": "4981499230898c8b36c6f46b0f60a5277630d92abe477d48ed77091e2203ffe2", "sha256_match": true, "verdict": "KEEP", "adds_cuts": [], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 43–62 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base ac22ea15; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20; CR 2025-09-25 text"}
```
# Saruman, the White Hand: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Saruman_the_White_Hand_Approved_2026-10-15.txt` (blob 64b58455, canonical main ceffdcce), 100 cards. Commander: Saruman, the White Hand. The raw-file sha256 matches both the tracker and `state/current_deck_overrides.json`. Every card is inside the commander's color identity and officially Commander-legal per Scryfall live /cards/collection (2026-10-20), so no project exception is needed here. Some cards' newest printings carry future release dates (e.g. 2026-11-13 reprints), but each card's Oracle legality is "legal".

**Weaknesses / opportunities**
1. Every noncreature spell amasses X equal to its MV. The Army carries ward {2}, and All Will Be One, The Ozolith and Commence the Endgame scale off the counters (fact).
2. **Weakest slots considered:** Orcish Medicine and Rage into the Valley, which are low-X amass (judgment).
3. **Best rejected alternative:** Lazotep Plating. Amass 1 plus hexproof overlaps with Saruman's ward {2} (judgment).

**Candidate swaps (proposals for Cory; nothing applied)**
- None. KEEP is a low-confidence judgment. See the weakest slots and rejected alternative above.

**Rules notes.**
- Saruman's trigger is on cast, so countered spells still amass (fact).
- X spells amass using the X paid on the stack (fact).

**Verdict:** KEEP.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- From the tracker, only the order, deck id and canonical hash were read (plus the entry's field names, not their values). The `approved_list_sha256` in state/current_deck_overrides.json was matched. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #43–#62, tracker indices 42–61), not a card-by-card audit. Each KEEP names the weakest slots considered and the best rejected alternative. KEEPs are not certificates.
