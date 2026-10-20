```json
{"tracker_deck_id": "Cecily__Bjorna__Lutri", "tracker_index": 7, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "553838da88fe00974e74664633be5051c4f1a0879baa71de81ca9f880e5a6d28", "source_file_raw_sha256": "553838da88fe00974e74664633be5051c4f1a0879baa71de81ca9f880e5a6d28", "sha256_match": true, "verdict": "KEEP", "adds_cuts": [], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 02–21 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base 65423569; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20 + oracle bulk 2026-10-16; CR 2025-09-25 text"}
```
# Cecily, Bjorna, Lutri: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Cecily__Bjorna__Lutri_Approved_2026-10-13.txt` (blob 543f7afa), 100 cards. Commander: Bjorna, Nightfall Alchemist + Cecily, Haunted Mage. Raw-file sha256 matches the tracker. Every card is inside the commander's color identity, and Commander legality was checked against Scryfall (2026-10-16 bulk), with project exceptions noted below.

**Weaknesses / opportunities**
1. The hand-size plan (Cecily's 11, Peer into the Abyss, wheels, Trade Secrets) reliably reaches the free-cast threshold (judgment).
2. Bjorna needs artifact fodder. Treasures from Big Score and Brass's Bounty plus the Signets cover it (judgment).

**Candidate swaps (proposals for Cory; nothing applied)**
- None. No incumbent was clearly beaten in this pass.

**Rules notes.**
- Lutri is the companion and sits outside the 100, which is correct. Its singleton condition is trivially met (fact). Trade Secrets and Yawgmoth's Bargain are officially BANNED and kept as **project exceptions**. They aren't official legality.

**Verdict:** KEEP.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- From the tracker, only the order, deck id and canonical hash were read. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #2–#21), not a card-by-card audit. The KEEP verdicts are low-cost judgments, not certificates.
