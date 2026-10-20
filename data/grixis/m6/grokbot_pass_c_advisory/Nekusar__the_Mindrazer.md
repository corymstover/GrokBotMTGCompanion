```json
{"tracker_deck_id": "Nekusar__the_Mindrazer", "tracker_index": 39, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "bc36908fb2f848dfd69407a317d7da5811532dba7e3b4e7be89a2905d901c6f1", "source_file_raw_sha256": "bc36908fb2f848dfd69407a317d7da5811532dba7e3b4e7be89a2905d901c6f1", "sha256_match": true, "verdict": "POSSIBLE UPGRADE", "adds_cuts": [{"in": "Forced Fruition", "out": "Kami of the Crescent Moon"}], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 22–42 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base 650d307a; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20; CR 2025-09-25 text"}
```
# Nekusar, the Mindrazer: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Nekusar_the_Mindrazer_Approved_2026-10-15.txt` (blob 8ee94e3e, canonical main ceffdcce), 100 cards. Commander: Nekusar, the Mindrazer. The raw-file sha256 matches both the tracker and `state/current_deck_overrides.json`. Every card is inside the commander's color identity and officially Commander-legal per Scryfall live /cards/collection (2026-10-20), so no project exception is needed here. Some cards' newest printings carry future release dates (e.g. 2026-11-13 reprints), but each card's Oracle legality is "legal".

**Weaknesses / opportunities**
1. Wizard's Staff on Nekusar (a Human Wizard) doubles both triggers, and Krang doubles draw-caused triggers. Together they're a strong damage engine (fact).
2. **Forced Fruition is missing.** Every spell an opponent casts draws them 7, which is 7+ Nekusar damage (fact: absent).
3. Notion Thief was considered and **rejected**: it replaces the opponents' extra draws, so it switches off Nekusar's damage (fact).

**Candidate swaps (proposals for Cory; nothing applied)**
- **+Forced Fruition / −Kami of the Crescent Moon.** Kami only duplicates Nekusar's draw-step clause, while Fruition scales with opponent spells. It's mono-U and Commander-legal (fact).

**Rules notes.**
- Teferi's Puzzle Box draws are real draws, so every one triggers Nekusar (fact).

**Verdict:** POSSIBLE UPGRADE.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- From the tracker, only the order, deck id and canonical hash were read (plus the entry's field names, not their values). The `approved_list_sha256` in state/current_deck_overrides.json was matched. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #22–#42, tracker indices 21–41), not a card-by-card audit. Each KEEP names the weakest slots considered and the best rejected alternative. KEEPs are not certificates.
