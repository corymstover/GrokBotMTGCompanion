```json
{"tracker_deck_id": "Doctor_Doom__King_of_Latveria", "tracker_index": 12, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "c97bd448aa4b18d2f7ed15e5d67006ab320ed67ad3ed267e44150de472e1dc58", "source_file_raw_sha256": "c97bd448aa4b18d2f7ed15e5d67006ab320ed67ad3ed267e44150de472e1dc58", "sha256_match": true, "verdict": "NEEDS VERIFICATION", "adds_cuts": [], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 02–21 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base 65423569; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20 + oracle bulk 2026-10-16; CR 2025-09-25 text"}
```
# Doctor Doom, King of Latveria: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Doctor_Doom_King_of_Latveria_Approved_2026-10-14.txt` (blob 324fdb30), 100 cards. Commander: Doctor Doom, King of Latveria. Raw-file sha256 matches the tracker. Every card is inside the commander's color identity, and Commander legality was checked against Scryfall (2026-10-16 bulk), with project exceptions noted below.

**Weaknesses / opportunities**
1. **Legality date.** The commander's Scryfall released_at is 2026-12-18 while its commander legality reads "legal" (fact, live 2026-10-20). That's later than the project's future-release date of 2026-11-13. Confirm it's covered, and keep official legality separate.
2. 35 lands plus Seismic Assault, Tectonic Reformation and Dakmor Salvage is coherent for "discard lands → 2 life each" (judgment).

**Candidate swaps (proposals for Cory; nothing applied)**
- None. No incumbent was clearly beaten in this pass.

**Rules notes.**
- Doom's combat trigger targets a Villain. Doom himself is a Villain, so it always has a target (fact). Norman Osborn // Green Goblin is listed under its canonical name. No alias was renamed.

**Verdict:** NEEDS VERIFICATION.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- From the tracker, only the order, deck id and canonical hash were read. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #2–#21), not a card-by-card audit. The KEEP verdicts are low-cost judgments, not certificates.
