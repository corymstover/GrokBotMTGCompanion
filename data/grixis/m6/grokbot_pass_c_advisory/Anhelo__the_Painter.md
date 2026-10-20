```json
{"tracker_deck_id": "Anhelo__the_Painter", "tracker_index": 3, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "d19d94b8a96fb27a760c7b7d9181221f74bd61642d1d1dd7644fc1c59c09839e", "source_file_raw_sha256": "8d5f8a9bd4fcdcd164aab63150c14dc69a814a4d9fd764876de3214d3adf9972", "sha256_match": false, "verdict": "NEEDS VERIFICATION", "adds_cuts": [], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 02–21 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base 65423569; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20 + oracle bulk 2026-10-16; CR 2025-09-25 text"}
```
# Anhelo, the Painter: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Anhelo_the_Painter_Approval_Ready_2026-10-13.txt` (blob 0f5f55ea), 100 cards. Commander: Anhelo, the Painter. **Raw-file sha256 does NOT match the tracker (see weakness 1).** Every card is inside the commander's color identity, and Commander legality was checked against Scryfall (2026-10-16 bulk), with project exceptions noted below.

**Weaknesses / opportunities**
1. **Hash provenance.** The tracker/override hash (d19d94b8…) is not reproduced by the raw sha256 of the gate-named source (`Anhelo_the_Painter_Approval_Ready_2026-10-13.txt`, raw 8d5f8a9b…). The 100 reviewed here is that file.
2. Casualty 2 needs **power ≥2** fodder. The deck makes it with Startle, Cryptic Pursuit manifests, Army of the Damned, Jadar's decayed Zombies and Bloodghast. Gravecrawler is a possible extra recursive body, but it has no clean cut (judgment).
3. Time Warp, Jeska's Will, Big Score and Mana Geyser are the highest-value casualty copies (judgment).

**Candidate swaps (proposals for Cory; nothing applied)**
- None. No incumbent was clearly beaten in this pass.

**Rules notes.**
- A Little Chat has its own casualty 1. With Anhelo, two separate casualty instances should allow two sacrifices and two copies (unresolved hypothesis; verify against CR 702.153).

**Verdict:** NEEDS VERIFICATION.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- From the tracker, only the order, deck id and canonical hash were read. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #2–#21), not a card-by-card audit. The KEEP verdicts are low-cost judgments, not certificates.
- To locate the hashed source, the reviewer read only the `approved_source`/sha fields of `refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Machine_Gate_Summary_2026-10-14.json`, and saw `refinement/` file names in a listing. No author conclusions were read.
