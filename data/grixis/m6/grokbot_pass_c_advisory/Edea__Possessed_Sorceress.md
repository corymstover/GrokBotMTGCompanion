```json
{"tracker_deck_id": "Edea__Possessed_Sorceress", "tracker_index": 15, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "fd560a9b0777088b3ad1684ded030566c894faa206ddf6763b74d95d82c532e4", "source_file_raw_sha256": "fd560a9b0777088b3ad1684ded030566c894faa206ddf6763b74d95d82c532e4", "sha256_match": true, "verdict": "KEEP", "adds_cuts": [], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 02–21 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base 65423569; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20 + oracle bulk 2026-10-16; CR 2025-09-25 text"}
```
# Edea, Possessed Sorceress: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Edea_Possessed_Sorceress_Approved_2026-10-14.txt` (blob e3651060), 100 cards. Commander: Edea, Possessed Sorceress. Raw-file sha256 matches the tracker. Every card is inside the commander's color identity, and Commander legality was checked against Scryfall (2026-10-16 bulk), with project exceptions noted below.

**Weaknesses / opportunities**
1. The steal–sacrifice–draw loop (Viscera Seer, the Altars, Grave Pact, Goblin Bombardment) is coherent (judgment).
2. A creature that dies under your control returns to its **owner's** battlefield, so their ETB creatures come back for them (fact).

**Candidate swaps (proposals for Cory; nothing applied)**
- None. No incumbent was clearly beaten in this pass.

**Rules notes.**
- Edea's return-and-draw applies to any creature you control but don't own, not only Edea's own target (fact).

**Verdict:** KEEP.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- From the tracker, only the order, deck id and canonical hash were read. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #2–#21), not a card-by-card audit. The KEEP verdicts are low-cost judgments, not certificates.
