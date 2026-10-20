```json
{"tracker_deck_id": "Lynde__Cheerful_Tormentor", "tracker_index": 30, "review_class": "ADVISORY", "formal_independent_pass_c": false, "canonical_sha256": "05d1c4eea023d25e4308f78b109e80b78e0a3f4d655c3df36743ba3afbf04166", "source_file_raw_sha256": "05d1c4eea023d25e4308f78b109e80b78e0a3f4d655c3df36743ba3afbf04166", "sha256_match": true, "verdict": "NEEDS VERIFICATION", "adds_cuts": [], "sealed_before_author_review": true, "seal_commit": "see progress.json (batch 22–42 seal commit)", "reviewer_provenance": "GrokBot (MTG Bot) advisory critic; model/version unknown; 2026-10-20 CDT; engineering base 650d307a; canonical main ceffdcce; Scryfall live /cards/collection 2026-10-20; CR 2025-09-25 text"}
```
# Lynde, Cheerful Tormentor: ADVISORY first pass (not qualified Pass C)

**Canonical list.** `refinement/decklists/Lynde_Cheerful_Tormentor_Approved_2026-10-14.txt` (blob 5731e689, canonical main ceffdcce), 100 cards. Commander: Lynde, Cheerful Tormentor. The raw-file sha256 matches both the tracker and `state/current_deck_overrides.json`. Every card is inside the commander's color identity and officially Commander-legal per Scryfall live /cards/collection (2026-10-20), so no project exception is needed here. Some cards' newest printings carry future release dates (e.g. 2026-11-13 reprints), but each card's Oracle legality is "legal".

**Weaknesses / opportunities**
1. **Self-harm sequencing.** Lynde returns each dying Curse **attached to you**, and moves only **one** Curse per upkeep. Curse of Bloodletting doubles damage to you, Curse of Thirst damages its enchanted player (you), Cruel Reality makes you sacrifice or lose 5, Curse of Death's Hold shrinks your creatures, and Curse of Shaken Faith pings you. A multi-Curse return or a wipe can backfire (fact plus unresolved severity).
2. The curve is heavy: seven Curses at 5 MV or more (Bloodletting, Death's Hold, Echoes, Misfortunes, Obsession, Surveillance, Thirst) plus Fool's Wisdom (6) and Unbinding and Cruel Reality (7) (measured).
3. Paradox Haze (an extra upkeep) is the best fix, giving two moves per turn. The Claws of Gix and Despotic Scepter outlets are good (judgment).

**Candidate swaps (proposals for Cory; nothing applied)**
- None. No swap is proposed until the self-harm exposure is measured. Candidate cut to test: Curse of Thirst or Curse of Bloodletting.

**Rules notes.**
- On upkeep with both Thirst and Lynde triggers, Thirst's "that player" is fixed as you when it triggers. Moving Thirst first doesn't stop that damage (CR 603.2, judgment pending verification).
- Curse of Misfortunes and Bitterheart Witch put Curses onto players directly. Those count as "enchant player" attachments, not casts (fact).

**Verdict:** NEEDS VERIFICATION.

**Provenance and exposure (ADVISORY).**
- GrokBot's prior involvement is disqualifying: it wrote the M1 reviews, the blueprints (cycles 50–55), the M2–M5 tooling and the Cycle124 critiques.
- The orchestrator read the handoff caveats on Zevlor, Tresserhorn, The Rani and Wick, and the Goben/Norman alias note.
- From the tracker, only the order, deck id and canonical hash were read (plus the entry's field names, not their values). The `approved_list_sha256` in state/current_deck_overrides.json was matched. No deep review, deep_review_evidence_path target, M5 ranking/score, author decision file or author PR/commit text was opened. sealed_before_author_review: true.
- This is a batch first pass (decks #22–#42, tracker indices 21–41), not a card-by-card audit. Each KEEP names the weakest slots considered and the best rejected alternative. KEEPs are not certificates.
