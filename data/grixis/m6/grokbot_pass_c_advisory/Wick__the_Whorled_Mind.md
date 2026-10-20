```json
{"tracker_deck_id": "Wick__the_Whorled_Mind", "tracker_index": 60, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "f4556840dc8f7a8e1d532b73652d0035592b52b86adbbad6ed8fbe4270341e98", "source_file_raw_sha256": "f4556840dc8f7a8e1d532b73652d0035592b52b86adbbad6ed8fbe4270341e98", "sha256_match": true, "verdict": "KEEP", "adds_cuts": [], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 43–62 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base ac22ea15; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20; CR 2025-09-25 text"}
```
# Wick, the Whorled Mind: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Wick_the_Whorled_Mind_Approved_2026-10-15.txt` (blob 503378bb, canonical main ceffdcce), 100 cards. Commander: Wick, the Whorled Mind. The raw-file sha256 matches both the tracker and `state/current_deck_overrides.json`. Every card is inside the commander's color identity and officially Commander-legal per Scryfall live /cards/collection (2026-10-20), so no project exception is needed here. Some cards' newest printings carry future release dates (e.g. 2026-11-13 reprints), but each card's Oracle legality is "legal".

**Weaknesses / opportunities**
1. Rats make or grow Snails, and Wick turns each sacrificed Snail into burn and draws equal to its power. Bulk Up doubles power before the sacrifice (fact).
2. **Weakest slots considered:** Tainted Strike (infect is off-plan) and Blade of the Bloodchief (judgment).
3. **Best rejected alternative:** Village Rites. The deck already has plenty of sacrifice outlets (judgment).

**Candidate swaps (proposals for Cory; nothing applied)**
- None. KEEP is a low-confidence judgment. See the weakest slots and rejected alternative above.

**Rules notes.**
- **Type-changing (independently verified from Oracle):** Maskwood Nexus makes all your creatures Rats and Snails. Every creature ETB triggers Wick, you always control a Snail (so it puts a counter instead of making a token), and any creature can pay Wick's 'Sacrifice a Snail'. Its {3},{T} changeling token is also a Rat and a Snail. Arcane Adaptation and Leyline of Transformation pick one type: Rat for ETB triggers, or Snail for sacrifice fodder (fact).
- Damage uses the sacrificed creature's last-known power (fact).

**Verdict:** KEEP.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- The orchestrator saw the handoff caveat that the type-changing paid ability isn't modeled. I re-derived it here from Oracle text.
- From the tracker, only the order, deck id and canonical hash were read (plus the entry's field names, not their values). The `approved_list_sha256` in state/current_deck_overrides.json was matched. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #43–#62, tracker indices 42–61), not a card-by-card audit. Each KEEP names the weakest slots considered and the best rejected alternative. KEEPs are not certificates.
