# Phase 6 Pilot 2 — Original & Primeval Dragons

**Status: UNAPPROVED PROPOSAL - awaiting Cory's review; not approved, not locked, not certified**

Commander: **The Ur-Dragon** (C17 #48), WUBRG — a *thematic* progenitor only (LORE_INSPIRED). The deck is a dragon procession: the five Legends Elder Dragons and their Core Set 2019 cards, Ugin, The Elder Dragon War, the post-war Piru/Dihada/Dakkon line, and the Invasion Primeval Dragons speaking through their printed flavor.

Built by the generic spec-driven builder (`scripts/build_lore_pilot.py`) from `data/lore_decks/specs/pilot2_original_primeval_dragons.json`. The same builder reproduces Pilot 1 byte-identically.

## Verification (reproducible, offline after snapshot)

- Snapshot `snap-20261029-40848334824-1`; default-cards `default-cards-20261029090546.jsonl.gz` sha256 `008434d5b89f1f2cb47411178d2ab181600faf9cb7ca1c5673422cdec5939595`.
- `scripts/audit_lore_pilot.py` (all specs): **PASS** — 100 cards, 85 named + 15 basics (3 of each), singleton, identity WUBRG, Commander-legal per snapshot, Game Changers 0 (ceiling 3), claims CANON_CONFIRMED in Pack A, official sources only.
- `evaluate_decklist.py --combos` (oracle bulk 2026-10-29): Hard checks PASS; Game Changers none; extra turns none; mass land denial none; Commander Spellbook 0 combos / 0 two-card infinite (local Spellbook data as shipped; not an exhaustive combo proof); minimum bracket **2** by the published barometers.
- Decklist SHA-256: `6ef1af37c371891b7d3e60a08c2d1bcee1d1205f2c01e5c3093a220fb4414888`.

## Structure

| Section | Cards | Grounding |
|---|---|---|
| I. Elder Dragons and the war Bolas started | 12 | Pack A claims A013–A017; Legends + M19 named character cards; The Elder Dragon War |
| II. After the war: Piru, Chromium, Dihada, Dakkon | 4 | A018–A022; MH2 printings (non-promo) |
| III. The Primeval Dragons | 13 | Crosis/Rith per Pack A2; Darigaaz/Dromar/Treva named-card only; 5 Attendants whose printed flavor says "ur-dragon" |
| IV. Invasion: the Primevals in their own words | 12 | Spells/charms chosen for printed quotes; earliest printing carrying that flavor |
| Story lands | 5 | The Primeval lairs (Planeshift) |
| Playability | 38 | MECHANICAL_SYMBOL: lands, ramp, removal, dragon support |
| Basics | 15 | 3 × each basic |

Tiers: DIRECT_DEPICTION 0 · CANON_REFERENCE 35 · LORE_INSPIRED 12 · MECHANICAL_SYMBOL 38 (named cards; basics excluded).

## Canon caveats

- A003/A004 (who struck first; Ugin's perspective) are CANON_DISPUTED; no card asserts either account.
- The Ur-Dragon is **not** asserted to be the "ur-dragon" of the Invasion Attendant flavor.
- Legends Elder Dragon art is not certified as any specific war scene, hence 0 DIRECT_DEPICTION.
- Darigaaz, Dromar and Treva are CANON_REFERENCE as named character cards only; Pack A2 sources name Crosis and Rith directly.
- Printed flavor proves what Wizards printed, not that an illustration depicts a specific story scene.
- Chromium Rhuell's banishment and Piru's death have no dedicated card; Piru/Dakkon cards stand in.

## Review asks for Cory

1. Is The Ur-Dragon acceptable as a thematic (not canonical) commander, or prefer a canonical Elder Dragon commander?
2. Playability slice is deliberately moderate (bracket 2 floor); raise or keep?
3. Any Primeval/Elder card swaps for preferred printings/art.
