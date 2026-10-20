```json
{"tracker_deck_id": "Crosis__the_Purger", "tracker_index": 9, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "a59150c323aa1e21cbda65291a3b172d08ecc3b83266b708768f4e14f0b07ec1", "source_file_raw_sha256": "a59150c323aa1e21cbda65291a3b172d08ecc3b83266b708768f4e14f0b07ec1", "sha256_match": true, "verdict": "POSSIBLE UPGRADE", "adds_cuts": [{"in": "Megrim", "out": "Sedraxis Specter"}], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 02–21 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base 65423569; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20 + oracle bulk 2026-10-16; CR 2025-09-25 text"}
```
# Crosis, the Purger: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Crosis_the_Purger_Approval_Candidate_2026-10-14.txt` (blob f0e0db5f), 100 cards. Commander: Crosis, the Purger. Raw-file sha256 matches the tracker. Every card is inside the commander's color identity, and Commander legality was checked against Scryfall (2026-10-16 bulk), with project exceptions noted below.

**Weaknesses / opportunities**
1. Painter's Servant + Crosis means "discard all cards of that color" empties the hand. That makes per-discard payoffs (Waste Not, Bottomless Pit, Tinybones, Dream Salvage, Geth's Grimoire) unusually strong (fact plus judgment).
2. Sedraxis Specter is the weakest of the hand-attack bodies (judgment).

**Candidate swaps (proposals for Cory; nothing applied)**
- **+Megrim / −Sedraxis Specter.** A Crosis hit on a 6-card hand is 12 damage, and every Hymn, Mind Twist and wheel discard also deals damage. It's mono-B and Commander-legal (fact).

**Rules notes.**
- Crosis's payment ({2}{B}) is made on the combat damage trigger, so leave mana up when attacking (fact).

**Verdict:** POSSIBLE UPGRADE.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- From the tracker, only the order, deck id and canonical hash were read. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #2–#21), not a card-by-card audit. The KEEP verdicts are low-cost judgments, not certificates.
