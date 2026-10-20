```json
{"tracker_deck_id": "Gwendlyn_Di_Corci", "tracker_index": 21, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "9a393cb7edf40f9bfb388d37dd657839cad851dc6a021440c7d1b239c1fd20a9", "source_file_raw_sha256": "9a393cb7edf40f9bfb388d37dd657839cad851dc6a021440c7d1b239c1fd20a9", "sha256_match": true, "verdict": "POSSIBLE UPGRADE", "adds_cuts": [{"in": "Megrim", "out": "Dream Salvage"}], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 22–42 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base 650d307a; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20; CR 2025-09-25 text"}
```
# Gwendlyn Di Corci: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Gwendlyn_Di_Corci_Approved_2026-10-14.txt` (blob 4ef2c267, canonical main ceffdcce), 100 cards. Commander: Gwendlyn Di Corci. The raw-file sha256 matches both the tracker and `state/current_deck_overrides.json`. Every card is inside the commander's color identity and officially Commander-legal per Scryfall live /cards/collection (2026-10-20), so no project exception is needed here. Some cards' newest printings carry future release dates (e.g. 2026-11-13 reprints), but each card's Oracle legality is "legal".

**Weaknesses / opportunities**
1. The deck is a random-discard punisher shell: Gwendlyn's tap, wheels, Liliana's Caress, Waste Not, three Tinybones and Bloodchief Ascension. It has **no Megrim**, the most direct per-discard damage payoff (fact: absent from the 100).
2. The untap and copy package (Illusionist's Bracers, Magewright's Stone, Patriar's Seal, Pemmin's Aura, Thousand-Year Elixir) multiplies Gwendlyn activations. That's on-plan, but five slots is dense (judgment).
3. Dream Salvage is the weakest slot. Off one Gwendlyn activation it draws 1 card, and it only spikes after a wheel that Liliana's Caress and Waste Not already reward (judgment).

**Candidate swaps (proposals for Cory; nothing applied)**
- **+Megrim / −Dream Salvage.** Megrim deals 2 damage for every discard from Gwendlyn, Dark Deal, wheels and Kefka-style effects, and it stacks with Liliana's Caress for 4 per card. It's mono-B and officially Commander-legal (fact, Scryfall 2026-10-20).

**Rules notes.**
- Gwendlyn activates only during your turn and needs haste or an untap to be used the turn she lands (fact). Lightning Greaves and Thousand-Year Elixir cover this.
- Wheel of Fortune and Windfall discard whole hands, so each card discarded counts separately for Megrim, Liliana's Caress and Waste Not (fact).

**Verdict:** POSSIBLE UPGRADE.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- From the tracker, only the order, deck id and canonical hash were read (plus the entry's field names, not their values). The `approved_list_sha256` in state/current_deck_overrides.json was matched. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #22–#42, tracker indices 21–41), not a card-by-card audit. Each KEEP names the weakest slots considered and the best rejected alternative. KEEPs are not certificates.
