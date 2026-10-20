```json
{"tracker_deck_id": "Mairsil__the_Pretender", "tracker_index": 32, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "51e8fd18c7ded6744a4fa2f871925a0679f85dada3e6e517334bd13c07889ee5", "source_file_raw_sha256": "51e8fd18c7ded6744a4fa2f871925a0679f85dada3e6e517334bd13c07889ee5", "sha256_match": true, "verdict": "KEEP", "adds_cuts": [], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 22–42 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base 650d307a; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20; CR 2025-09-25 text"}
```
# Mairsil, the Pretender: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Mairsil_the_Pretender_Approved_2026-10-14.txt` (blob 027eb7a0, canonical main ceffdcce), 100 cards. Commander: Mairsil, the Pretender. The raw-file sha256 matches both the tracker and `state/current_deck_overrides.json`. Every card is inside the commander's color identity and officially Commander-legal per Scryfall live /cards/collection (2026-10-20), so no project exception is needed here. Some cards' newest printings carry future release dates (e.g. 2026-11-13 reprints), but each card's Oracle legality is "legal".

**Weaknesses / opportunities**
1. The cage package (Aetherling, Arcanis, Torchling, Quicksilver Elemental, Morphling, Horseshoe Crab, Minion of Leshrac) supports a toolbox Mairsil. Rings and Training Grounds amplify it (judgment).
2. **Weakest slots considered:** Pack Rat (caged, it only lets Mairsil copy itself for {2}{B} plus a discard, once per turn) and Omen Hawker (judgment).
3. **Best rejected alternative:** Basalt Monolith as a cage-adjacent mana piece. It's an artifact, but caged it only grants a self-referential untap, so it does nothing on Mairsil (judgment).

**Candidate swaps (proposals for Cory; nothing applied)**
- None. KEEP is a low-confidence judgment. See the weakest slots and rejected alternative above.

**Rules notes.**
- Marvin, Murderous Mimic gains Mairsil's granted abilities. Whether Mairsil's "only once each turn" limit carries over to Marvin is an **unresolved hypothesis** that needs a ruling before any combo claim (unresolved).
- Caged abilities that refer to their own card name refer to Mairsil (CR 201.5; fact).

**Verdict:** KEEP.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- From the tracker, only the order, deck id and canonical hash were read (plus the entry's field names, not their values). The `approved_list_sha256` in state/current_deck_overrides.json was matched. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #22–#42, tracker indices 21–41), not a card-by-card audit. Each KEEP names the weakest slots considered and the best rejected alternative. KEEPs are not certificates.
