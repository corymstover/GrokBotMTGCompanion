```json
{"tracker_deck_id": "Loki__the_Deceiver", "tracker_index": 27, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "5079291c08c5af212b3d90d63ac5b01849d45c7700b1d64100ef57fb13458062", "source_file_raw_sha256": "5079291c08c5af212b3d90d63ac5b01849d45c7700b1d64100ef57fb13458062", "sha256_match": true, "verdict": "KEEP", "adds_cuts": [], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 22–42 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base 650d307a; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20; CR 2025-09-25 text"}
```
# Loki, the Deceiver: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Loki_the_Deceiver_Approved_2026-10-14.txt` (blob 456d62d4, canonical main ceffdcce), 100 cards. Commander: Loki, the Deceiver. The raw-file sha256 matches both the tracker and `state/current_deck_overrides.json`. Every card is inside the commander's color identity and officially Commander-legal per Scryfall live /cards/collection (2026-10-20), so no project exception is needed here. Some cards' newest printings carry future release dates (e.g. 2026-11-13 reprints), but each card's Oracle legality is "legal".

**Weaknesses / opportunities**
1. Villain tribal (Bracket 3, 5 Game Changers). Loki's attack copy turns any Villain's ETB into a repeatable trigger, so ETB Villains are the core (judgment).
2. **Weakest slots considered:** Stilt-Man, Towering Terror (its steal needs connecting Villains) and Blasphemous Act (a symmetric wipe in a creature deck) (judgment).
3. **Best rejected alternative:** Hostage Taker for Stilt-Man. It's a stronger card, but it isn't a Villain, so Loki can neither copy it nor draw from it (judgment).

**Candidate swaps (proposals for Cory; nothing applied)**
- None. KEEP is a low-confidence judgment. See the weakest slots and rejected alternative above.

**Rules notes.**
- Loki copies "another target Villain you control". The token is tapped and attacking, so it doesn't trigger its own "whenever attacks" abilities (fact).
- **Goben/Norman alias:** the canonical ID `Norman Osborn // Green Goblin` is kept unchanged. Scryfall's om1 #30 printing shows the printed face names "Goben, Gene-Splice Savant" and "Fleem, Goben's Creation" with the same oracle_id `aa5b06a4-90c3-45e7-ab83-cb5c96ded21d` as the spm printings, so the prints are Oracle-equivalent (fact, Scryfall 2026-10-20).

**Verdict:** KEEP.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- **Alias disclosure:** the orchestrator saw the handoff's Goben/Norman alias note. The alias was verified here independently from Scryfall Oracle data (see Rules notes).
- From the tracker, only the order, deck id and canonical hash were read (plus the entry's field names, not their values). The `approved_list_sha256` in state/current_deck_overrides.json was matched. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #22–#42, tracker indices 21–41), not a card-by-card audit. Each KEEP names the weakest slots considered and the best rejected alternative. KEEPs are not certificates.
