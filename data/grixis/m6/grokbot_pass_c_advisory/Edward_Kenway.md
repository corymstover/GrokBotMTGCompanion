```json
{"tracker_deck_id": "Edward_Kenway", "tracker_index": 16, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "a08d3bc9c283415f1579c493eccb3febd7d10dea3777bf3dc50cfbc0dbed4019", "source_file_raw_sha256": "a08d3bc9c283415f1579c493eccb3febd7d10dea3777bf3dc50cfbc0dbed4019", "sha256_match": true, "verdict": "KEEP", "adds_cuts": [], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 02–21 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base 65423569; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20 + oracle bulk 2026-10-16; CR 2025-09-25 text"}
```
# Edward Kenway: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Edward_Kenway_Approved_2026-10-14.txt` (blob 46df00ee), 100 cards. Commander: Edward Kenway. Raw-file sha256 matches the tracker. Every card is inside the commander's color identity, and Commander legality was checked against Scryfall (2026-10-16 bulk), with project exceptions noted below.

**Weaknesses / opportunities**
1. Treasure scales with tapped Assassins, Pirates and Vehicles at end step. Crew costs and attacks both count (judgment).
2. The deck is already Bracket-4-dense, with 10 Game Changers by the local count (fact).

**Candidate swaps (proposals for Cory; nothing applied)**
- None. No incumbent was clearly beaten in this pass.

**Rules notes.**
- The Vehicle exile is face-down and playable "as long as it remains exiled". It doesn't let you spend mana as any color (fact).

**Verdict:** KEEP.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- From the tracker, only the order, deck id and canonical hash were read. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #2–#21), not a card-by-card audit. The KEEP verdicts are low-cost judgments, not certificates.
