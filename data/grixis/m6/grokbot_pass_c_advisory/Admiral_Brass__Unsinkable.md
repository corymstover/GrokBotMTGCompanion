```json
{"tracker_deck_id": "Admiral_Brass__Unsinkable", "tracker_index": 2, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "e66e3a59719401f41830e9938997a87a45a1b0dcaa0663b0ec7b44e10077dd39", "source_file_raw_sha256": "056f0369bc4b11967365eef65d15a806b2d0f673ecf8097b028ffcdfd472f5cc", "sha256_match": false, "verdict": "NEEDS VERIFICATION", "adds_cuts": [{"in": "Dire Fleet Ravager", "out": "Merchant Raiders"}], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 02–21 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base 65423569; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20 + oracle bulk 2026-10-16; CR 2025-09-25 text"}
```
# Admiral Brass, Unsinkable: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Admiral_Brass_Unsinkable_Whole_List_Approval_Candidate_2026-10-13.txt` (blob 5aabc4ba), 100 cards. Commander: Admiral Brass, Unsinkable. **Raw-file sha256 does NOT match the tracker (see weakness 1).** Every card is inside the commander's color identity, and Commander legality was checked against Scryfall (2026-10-16 bulk), with project exceptions noted below.

**Weaknesses / opportunities**
1. **Hash provenance.** The tracker/override hash (e66e3a59…) is not reproduced by the raw sha256 of the approved source named in the retrospective machine gate (`Admiral_Brass_Unsinkable_Whole_List_Approval_Candidate_2026-10-13.txt`, raw 056f0369…). It was also not reproduced by simple normalizations (fact). The 100 reviewed here is that file.
2. Merchant Raiders is a low-impact reanimation target. Brass returns each Pirate as a hasty 4/4, so the ETB text is what matters (judgment).
3. Skeleton Crew and Power Conduit (which removes finality counters) are good, niche synergies. Keep both (judgment).

**Candidate swaps (proposals for Cory; nothing applied)**
- **+Dire Fleet Ravager / −Merchant Raiders.** It's a mono-B Orc Pirate whose ETB makes every player lose a third of their life. As a free hasty 4/4 menace/deathtouch reanimation it's a strong pressure line, though the loss is symmetric, so watch your own life (judgment).

**Rules notes.**
- Finality means a returned creature that dies is exiled, so each Pirate in the yard is effectively a single-use resource. Power Conduit can remove that counter (fact, Oracle).

**Verdict:** NEEDS VERIFICATION.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- From the tracker, only the order, deck id and canonical hash were read. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #2–#21), not a card-by-card audit. The KEEP verdicts are low-cost judgments, not certificates.
- To locate the hashed source, the reviewer read only the `approved_source`/sha fields of `refinement/verification/retrospective_1_to_8/Retrospective_1_to_8_Machine_Gate_Summary_2026-10-14.json`, and saw `refinement/` file names in a listing. No author conclusions were read.
