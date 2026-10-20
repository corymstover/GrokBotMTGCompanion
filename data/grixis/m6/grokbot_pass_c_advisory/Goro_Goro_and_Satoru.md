```json
{"tracker_deck_id": "Goro_Goro_and_Satoru", "tracker_index": 20, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "2fd39e3b39afaeb1bf394a59b392d8a29f28645776fa0b13c5754df67ab85fdf", "source_file_raw_sha256": "2fd39e3b39afaeb1bf394a59b392d8a29f28645776fa0b13c5754df67ab85fdf", "sha256_match": true, "verdict": "KEEP", "adds_cuts": [], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 02–21 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base 65423569; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20 + oracle bulk 2026-10-16; CR 2025-09-25 text"}
```
# Goro Goro and Satoru: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Goro_Goro_and_Satoru_Approved_2026-10-14.txt` (blob 9d9e1b7b), 100 cards. Commander: Goro-Goro and Satoru. Raw-file sha256 matches the tracker. Every card is inside the commander's color identity, and Commander legality was checked against Scryfall (2026-10-16 bulk), with project exceptions noted below.

**Weaknesses / opportunities**
1. The ninjutsu suite turns returned or ninjutsu'd creatures into "entered this turn" damage dealers, which reliably triggers the Dragon (judgment).

**Candidate swaps (proposals for Cory; nothing applied)**
- None. No incumbent was clearly beaten in this pass.

**Rules notes.**
- Ninjutsu puts the Ninja onto the battlefield tapped and attacking, so it has entered this turn. Its damage triggers Goro-Goro (fact).

**Verdict:** KEEP.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- From the tracker, only the order, deck id and canonical hash were read. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #2–#21), not a card-by-card audit. The KEEP verdicts are low-cost judgments, not certificates.
