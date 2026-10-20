```json
{"tracker_deck_id": "Cormela__Glamour_Thief", "tracker_index": 8, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "80f4bdef2b8b140aeae23775cfdf87fda81e7215038b8db9b1746c806f366e0b", "source_file_raw_sha256": "80f4bdef2b8b140aeae23775cfdf87fda81e7215038b8db9b1746c806f366e0b", "sha256_match": true, "verdict": "KEEP", "adds_cuts": [], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 02–21 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base 65423569; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20 + oracle bulk 2026-10-16; CR 2025-09-25 text"}
```
# Cormela, Glamour Thief: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Cormela_Glamour_Thief_Approved_2026-10-14.txt` (blob ee008725), 100 cards. Commander: Cormela, Glamour Thief. Raw-file sha256 matches the tracker. Every card is inside the commander's color identity, and Commander legality was checked against Scryfall (2026-10-16 bulk), with project exceptions noted below.

**Weaknesses / opportunities**
1. This is a cEDH Breach/LED/Brain Freeze and Thassa's Oracle shell, at the commander's natural ceiling (judgment).
2. Doomsday is the main unused Oracle line, but there's no clean cut. Molten Duplication is **not** a cut, because Dualcaster Mage + Molten Duplication makes infinite hasty tokens (fact).

**Candidate swaps (proposals for Cory; nothing applied)**
- None. No incumbent was clearly beaten in this pass.

**Rules notes.**
- Cormela's mana is restricted to instants and sorceries, so it can't pay for LED's activation or for artifacts (fact).

**Verdict:** KEEP.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- From the tracker, only the order, deck id and canonical hash were read. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #2–#21), not a card-by-card audit. The KEEP verdicts are low-cost judgments, not certificates.
