```json
{"tracker_deck_id": "Dr__Eggman", "tracker_index": 14, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "ef34986253f71043e10c852b5f9f3ce79594fdfc1086b105f6744c3f639199c3", "source_file_raw_sha256": "ef34986253f71043e10c852b5f9f3ce79594fdfc1086b105f6744c3f639199c3", "sha256_match": true, "verdict": "KEEP", "adds_cuts": [], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 02–21 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base 65423569; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20 + oracle bulk 2026-10-16; CR 2025-09-25 text"}
```
# Dr, Eggman: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Dr_Eggman_Approved_2026-10-14.txt` (blob 86119caf), 100 cards. Commander: Dr. Eggman. Raw-file sha256 matches the tracker. Every card is inside the commander's color identity, and Commander legality was checked against Scryfall (2026-10-16 bulk), with project exceptions noted below.

**Weaknesses / opportunities**
1. Opponents choose between discard and letting you cheat a Construct/Robot/Vehicle, so the payoffs need to be large. Myr Battlesphere, Metalwork Colossus and the Gearhulks do that (judgment).
2. No clear cut was found without a type-by-type audit.

**Candidate swaps (proposals for Cory; nothing applied)**
- None. No incumbent was clearly beaten in this pass.

**Rules notes.**
- Check the creature types: only Construct, Robot or Vehicle cards qualify for the cheat (fact). The Gearhulks are Constructs.

**Verdict:** KEEP.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- From the tracker, only the order, deck id and canonical hash were read. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #2–#21), not a card-by-card audit. The KEEP verdicts are low-cost judgments, not certificates.
