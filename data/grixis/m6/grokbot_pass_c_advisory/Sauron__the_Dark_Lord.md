```json
{"tracker_deck_id": "Sauron__the_Dark_Lord", "tracker_index": 49, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "fab194f69a6e15b83679c1419f88ba6fdd56cd9527946cb94a6d8efe23a7dfc8", "source_file_raw_sha256": "fab194f69a6e15b83679c1419f88ba6fdd56cd9527946cb94a6d8efe23a7dfc8", "sha256_match": true, "verdict": "KEEP", "adds_cuts": [], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 43–62 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base ac22ea15; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20; CR 2025-09-25 text"}
```
# Sauron, the Dark Lord: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Sauron_the_Dark_Lord_Approved_2026-10-15.txt` (blob b7142453, canonical main ceffdcce), 100 cards. Commander: Sauron, the Dark Lord. The raw-file sha256 matches both the tracker and `state/current_deck_overrides.json`. Every card is inside the commander's color identity and officially Commander-legal per Scryfall live /cards/collection (2026-10-20), so no project exception is needed here. Some cards' newest printings carry future release dates (e.g. 2026-11-13 reprints), but each card's Oracle legality is "legal".

**Weaknesses / opportunities**
1. Opponent spells amass, Army hits tempt with the Ring, and each tempt lets you discard your hand and draw 4. Nazgûl x7 tempts on every ETB (fact).
2. **Weakest slots considered:** Bilbo, Retired Burglar and Claim the Precious (judgment).
3. **Best rejected alternative:** Notion Thief. It starves the opponents' spell volume that feeds Sauron's amass (judgment).

**Candidate swaps (proposals for Cory; nothing applied)**
- None. KEEP is a low-confidence judgment. See the weakest slots and rejected alternative above.

**Rules notes.**
- Roaming Throne naming **Wraith** doubles both Nazgûl triggers (ETB tempt and counters). Naming Avatar doubles Sauron's amass (Oracle fact).
- Sauron's ward needs a **legendary** artifact or creature sacrificed (fact).
- Nazgûl x7 is within its 9-copy rule (fact).

**Verdict:** KEEP.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- From the tracker, only the order, deck id and canonical hash were read (plus the entry's field names, not their values). The `approved_list_sha256` in state/current_deck_overrides.json was matched. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #43–#62, tracker indices 42–61), not a card-by-card audit. Each KEEP names the weakest slots considered and the best rejected alternative. KEEPs are not certificates.
