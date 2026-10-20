```json
{"tracker_deck_id": "Ashad__the_Lone_Cyberman", "tracker_index": 4, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "087e34c2127859111fc08f8d9ec7d66cd3495537cc571d88e829fd27d2823e25", "source_file_raw_sha256": "087e34c2127859111fc08f8d9ec7d66cd3495537cc571d88e829fd27d2823e25", "sha256_match": true, "verdict": "KEEP", "adds_cuts": [], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 02–21 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base 65423569; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20 + oracle bulk 2026-10-16; CR 2025-09-25 text"}
```
# Ashad, the Lone Cyberman: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Ashad_the_Lone_Cyberman_Approval_Ready_2026-10-13.txt` (blob df3e619f), 100 cards. Commander: Ashad, the Lone Cyberman. Raw-file sha256 matches the tracker. Every card is inside the commander's color identity, and Commander legality was checked against Scryfall (2026-10-16 bulk), with project exceptions noted below.

**Weaknesses / opportunities**
1. Biotransference turns creature spells into artifact spells, so Ashad's casualty also covers creature spells. It's a key enabler, not a weak card (fact plus judgment).
2. Fodder must have power ≥2. Wurmcoil, Kappa Cannoneer and the Cyberman tokens qualify. 1/1 Thopters don't (fact).

**Candidate swaps (proposals for Cory; nothing applied)**
- None. No incumbent was clearly beaten in this pass.

**Rules notes.**
- Ashad copies only the **first nonlegendary** artifact spell each turn. Legendary artifacts such as Iron Man, Brudiclad and Tezzeret's pieces get no casualty (fact).

**Verdict:** KEEP.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- From the tracker, only the order, deck id and canonical hash were read. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #2–#21), not a card-by-card audit. The KEEP verdicts are low-cost judgments, not certificates.
