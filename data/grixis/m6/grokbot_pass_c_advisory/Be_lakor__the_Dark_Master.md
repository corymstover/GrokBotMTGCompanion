```json
{"tracker_deck_id": "Be_lakor__the_Dark_Master", "tracker_index": 6, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "3abc951606a6db2b17ea2aceb471fc2ef4c55e2ef082d49d9140a83b2491155e", "source_file_raw_sha256": "3abc951606a6db2b17ea2aceb471fc2ef4c55e2ef082d49d9140a83b2491155e", "sha256_match": true, "verdict": "KEEP", "adds_cuts": [], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 02–21 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base 65423569; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20 + oracle bulk 2026-10-16; CR 2025-09-25 text"}
```
# Be lakor, the Dark Master: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Be_lakor_the_Dark_Master_Approved_2026-10-13.txt` (blob 89721509), 100 cards. Commander: Be'lakor, the Dark Master. Raw-file sha256 matches the tracker. Every card is inside the commander's color identity, and Commander legality was checked against Scryfall (2026-10-16 bulk), with project exceptions noted below.

**Weaknesses / opportunities**
1. The Demon density, cost cheats (Sneak Attack, Kardur, Rite of Replication, Reflections of Littjara) and Warstorm Surge redundancy match Lord of Torment well (judgment).
2. The ETB draw makes you lose X life. Bloodletter of Aclazotz doubles only opponents' loss, so a Be'lakor recast stays costly (fact).

**Candidate swaps (proposals for Cory; nothing applied)**
- None. No incumbent was clearly beaten in this pass.

**Rules notes.**
- A kicked Rite of Replication makes five Demon tokens enter at once, and each triggers Lord of Torment separately (fact).

**Verdict:** KEEP.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- From the tracker, only the order, deck id and canonical hash were read. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #2–#21), not a card-by-card audit. The KEEP verdicts are low-cost judgments, not certificates.
