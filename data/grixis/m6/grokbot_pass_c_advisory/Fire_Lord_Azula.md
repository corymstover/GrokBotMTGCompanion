```json
{"tracker_deck_id": "Fire_Lord_Azula", "tracker_index": 18, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "b6ef396641f2b5cfac0eb81fb494f21f3745e2a3fd47fa75d2eaadbdc34ddee5", "source_file_raw_sha256": "b6ef396641f2b5cfac0eb81fb494f21f3745e2a3fd47fa75d2eaadbdc34ddee5", "sha256_match": true, "verdict": "KEEP", "adds_cuts": [], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 02–21 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base 65423569; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20 + oracle bulk 2026-10-16; CR 2025-09-25 text"}
```
# Fire Lord Azula: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Fire_Lord_Azula_Approved_2026-10-14.txt` (blob 0aa3e809), 100 cards. Commander: Fire Lord Azula. Raw-file sha256 matches the tracker. Every card is inside the commander's color identity, and Commander legality was checked against Scryfall (2026-10-16 bulk), with project exceptions noted below.

**Weaknesses / opportunities**
1. Copies happen only while Azula is attacking. Sorcery-speed cards (Wheel of Fortune, Demonic Tutor, Gamble) are never copied, and the deck accepts that as a cEDH shell (fact plus judgment).

**Candidate swaps (proposals for Cory; nothing applied)**
- None. No incumbent was clearly beaten in this pass.

**Rules notes.**
- The firebending {R}{R} empties at end of combat (fact). Quicken and Expedite are the deck's ways to cast sorcery-speed cards in combat.

**Verdict:** KEEP.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- From the tracker, only the order, deck id and canonical hash were read. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #2–#21), not a card-by-card audit. The KEEP verdicts are low-cost judgments, not certificates.
