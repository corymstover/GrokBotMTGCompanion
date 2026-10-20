```json
{"tracker_deck_id": "Obeka__Splitter_of_Seconds", "tracker_index": 44, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "c7e855e69d6538d05eec2e4b3da98b0a5bdb057b19e2c672294b9ba3a60a4f63", "source_file_raw_sha256": "c7e855e69d6538d05eec2e4b3da98b0a5bdb057b19e2c672294b9ba3a60a4f63", "sha256_match": true, "verdict": "POSSIBLE UPGRADE", "adds_cuts": [{"in": "Rogue's Passage", "out": "Swamp"}], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 43–62 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base ac22ea15; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20; CR 2025-09-25 text"}
```
# Obeka, Splitter of Seconds: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Obeka_Splitter_of_Seconds_Approved_2026-10-15.txt` (blob 3744ef1e, canonical main ceffdcce), 100 cards. Commander: Obeka, Splitter of Seconds. The raw-file sha256 matches both the tracker and `state/current_deck_overrides.json`. Every card is inside the commander's color identity and officially Commander-legal per Scryfall live /cards/collection (2026-10-20), so no project exception is needed here. Some cards' newest printings carry future release dates (e.g. 2026-11-13 reprints), but each card's Oracle legality is "legal".

**Weaknesses / opportunities**
1. Combat damage becomes extra upkeeps that multiply the Courts, the Ring cycle, Phyrexian Arena, Mechanized Production, Paradox Haze and Ancestral Vision's suspend. Hatred's +X becomes X more upkeeps (fact plus judgment).
2. Silent Arbiter (no more than one blocker) plus menace makes Obeka unblockable, and Aqueous Form/Brotherhood Regalia add evasion. Still, the whole deck depends on connecting (judgment).
3. **Opportunity:** a land-slot evasion source that costs no spell slot.

**Candidate swaps (proposals for Cory; nothing applied)**
- **+Rogue's Passage / −Swamp.** Repeatable unblockability for the one card the deck needs to connect. With 35 lands and 7 basics, the colorless land is affordable. Mono-colorless and Commander-legal (fact; low-confidence judgment).

**Rules notes.**
- Each extra upkeep is a full step, so 'at the beginning of your upkeep' triggers repeat. Monarch Court triggers need you to be monarch at the time (fact).

**Verdict:** POSSIBLE UPGRADE.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- From the tracker, only the order, deck id and canonical hash were read (plus the entry's field names, not their values). The `approved_list_sha256` in state/current_deck_overrides.json was matched. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #43–#62, tracker indices 42–61), not a card-by-card audit. Each KEEP names the weakest slots considered and the best rejected alternative. KEEPs are not certificates.
