```json
{"tracker_deck_id": "Sol_kanar_the_Swamp_King", "tracker_index": 51, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "7d39fff42b91263e83415feef1e69d048c54f8b4e2226b8430fb584076d19106", "source_file_raw_sha256": "7d39fff42b91263e83415feef1e69d048c54f8b4e2226b8430fb584076d19106", "sha256_match": true, "verdict": "POSSIBLE UPGRADE", "adds_cuts": [{"in": "Sanguine Bond", "out": "Demon's Horn"}], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 43–62 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base ac22ea15; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20; CR 2025-09-25 text"}
```
# Sol'kanar the Swamp King: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Solkanar_the_Swamp_King_Approved_2026-10-15.txt` (blob 99ca0f3d, canonical main ceffdcce), 100 cards. Commander: Sol'kanar the Swamp King. The raw-file sha256 matches both the tracker and `state/current_deck_overrides.json`. Every card is inside the commander's color identity and officially Commander-legal per Scryfall live /cards/collection (2026-10-20), so no project exception is needed here. Some cards' newest printings carry future release dates (e.g. 2026-11-13 reprints), but each card's Oracle legality is "legal".

**Weaknesses / opportunities**
1. Black-spell lifegain feeds Exquisite Blood + Bloodthirsty Conqueror/Vito loops and Aetherflux. Painter's Servant naming black turns every player's spell into a Sol'kanar trigger and combos with Grindstone. Blanket of Night makes swampwalk universal (fact).
2. **Demon's Horn** is a second copy of Sol'kanar's own clause and doesn't win (judgment).
3. Exquisite Blood's only loop partners are Bloodthirsty Conqueror and Vito. There's no Sanguine Bond (fact: absent).

**Candidate swaps (proposals for Cory; nothing applied)**
- **+Sanguine Bond / −Demon's Horn.** A third Exquisite Blood partner that also turns every incidental Sol'kanar gain into a drain. Mono-B and Commander-legal (fact).

**Rules notes.**
- Painter's Servant changes colors of cards in every zone, including opponents' spells, so Sol'kanar triggers on them (fact).

**Verdict:** POSSIBLE UPGRADE.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- From the tracker, only the order, deck id and canonical hash were read (plus the entry's field names, not their values). The `approved_list_sha256` in state/current_deck_overrides.json was matched. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #43–#62, tracker indices 42–61), not a card-by-card audit. Each KEEP names the weakest slots considered and the best rejected alternative. KEEPs are not certificates.
