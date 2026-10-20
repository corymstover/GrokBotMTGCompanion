```json
{"tracker_deck_id": "Lord_of_Tresserhorn", "tracker_index": 28, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "95863276f38beff6b0cf7609041006a6f1de94d5e62c73d76551d6793ffa5b8e", "source_file_raw_sha256": "95863276f38beff6b0cf7609041006a6f1de94d5e62c73d76551d6793ffa5b8e", "sha256_match": true, "verdict": "KEEP", "adds_cuts": [], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 22–42 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base 650d307a; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20; CR 2025-09-25 text"}
```
# Lord of Tresserhorn: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Lord_of_Tresserhorn_Approved_2026-10-14.txt` (blob d9ff96da, canonical main ceffdcce), 100 cards. Commander: Lord of Tresserhorn. The raw-file sha256 matches both the tracker and `state/current_deck_overrides.json`. Every card is inside the commander's color identity and officially Commander-legal per Scryfall live /cards/collection (2026-10-20), so no project exception is needed here. Some cards' newest printings carry future release dates (e.g. 2026-11-13 reprints), but each card's Oracle legality is "legal".

**Weaknesses / opportunities**
1. The plan is a 10/4 regenerating voltron with infect (Phyresis, Tainted Strike) plus Wonder, Uncaged Fury and Pain for All, on an aristocrats base whose recursive Zombies pay the ETB sacrifice. Rooftop Storm makes Tresserhorn (a Zombie) free to recast (fact plus judgment).
2. **Weakest slots considered:** Diregraf Captain and Wilhelt, the Rotcleaver. They're Zombie lords with little impact on a commander-damage/infect kill (judgment).
3. **Best rejected alternative:** Grafted Exoskeleton (infect redundancy) for Diregraf Captain. The deck already has two infect enablers plus Kediss and Pain for All, so the marginal gain is low (judgment).

**Candidate swaps (proposals for Cory; nothing applied)**
- None. KEEP is a low-confidence judgment. See the weakest slots and rejected alternative above.

**Rules notes.**
- Not of This World is free only when it targets a spell or ability that targets a creature you control with power 7 or greater. Tresserhorn qualifies (fact).
- Torpor Orb also suppresses Tresserhorn's own ETB drawback, which is a real synergy. It also turns off Undead Augur and Zulaport-style ETB value (fact).

**Verdict:** KEEP.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- **Deck-specific caveat disclosure:** a Tresserhorn caveat exists in the handoff and was seen by the orchestrator, not by this reviewer. This first pass was written without it.
- From the tracker, only the order, deck id and canonical hash were read (plus the entry's field names, not their values). The `approved_list_sha256` in state/current_deck_overrides.json was matched. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #22–#42, tracker indices 21–41), not a card-by-card audit. Each KEEP names the weakest slots considered and the best rejected alternative. KEEPs are not certificates.
