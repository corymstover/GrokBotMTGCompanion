# Phase 7 v2.88 — cross-domain card, lore and Commander evidence

**Status:** bounded engineering capability; **NOT** a live Commander legality certificate, artwork-scene attribution, owner approval, deck recommendation, or full-card knowledge closure.

The ordinary `scripts/mv_ask.py ask` entry point now handles questions like:

- `What are the lore and Commander eligibility of Ugin, the Spirit Dragon?`
- `Show card, lore, and Commander rules for Nicol Bolas, the Ravager`
- `Tell me the lore and Commander eligibility of Blackblade Reforged`

## Strict provenance joins

1. Resolve a unique exact indexed card or unique front face; the card fact sheet comes from the committed Scryfall-derived card index/shard, with its own snapshot date.
2. Join to a graph **Card** node by *exact Oracle UUID*, never by card-title substring. A `names_entity` graph relation permits a named Character/Faction research lookup, but is explicitly **navigation**, not a source proving card art depicts a specific event or character pose.
3. Return at most eight direct, source-graded lore claims **per named subject**, with each cited source URL, the total distinct direct-claim count, omitted count, and all observed grades. Do not flatten `CANON_IMPLIED`, `CANON_DISPUTED`, `OPEN_QUESTION` or alternate continuity into unqualified truth.
4. Independently run the date-qualified official Comprehensive Rules Commander-eligibility check, including whether the named card is *eligible to be the commander*, not merely format-legal as a card. The combined result always remains `QUALIFIED`, carrying `DATED_SCRYFALL_LEGALITY_NOT_LIVE`, `NO_RULES_SIMULATION`, and the explicit rules/card snapshot dates.
5. Unknown cards fail closed as `NOT_FOUND`; no named graph link reports that absence, not a guessed story subject. Duplicate Oracle card anchors suppress the lore join with an ambiguity flag.

## Reproduced adversarial examples

| Card/query | What is supported | What is deliberately refused |
| --- | --- | --- |
| Ugin, the Spirit Dragon | Its Scryfall format field says `legal`, but CR 903.3 does **not** make the specific planeswalker card commander-eligible; direct claims about named entity Ugin are linked as graph navigation. | A false `allowed: true` conclusion or assertion that an Ugin story scene is depicted by this printing. |
| Nicol Bolas, the Ravager (front face) | The unique full dual-faced Oracle card is located; legal/eligible as a commander on the frozen evidence; named character Nicol Bolas has 52 registered direct claims with canon disputes disclosed. | A clean, total biography or permanent guarantee of current legality; no assertion that a card name alone proves a scene. |
| Blackblade Reforged | Card and CR lookup succeed; no `names_entity` graph link exists in the current graph. | Inventing the sword's character owner or a specific pictured lore event from an art-caption link. |
| Zorblax the Unreal | `NOT_FOUND` with no citations or facts. | Hallucinated card, lore, or rules conclusions. |

## Reproducibility

- `scripts/mv_ask.py`: exact Oracle identity join and provenance-qualified response envelope.
- `tests/test_mv_ask_cross_domain_card_lore_rules.py`: six test methods including an injected duplicate Oracle graph identity.
- `.github/workflows/phase7-companion-ask.yml`: new test path triggers both PR and push; full `test_mv_ask*.py` discovery and representative CLI cases.
- `scripts/build_foundation_acceptance_packet.py`: four representative cross-domain cases with explicit anti-overclaim assertions.
- Rebuilt `data/release/foundation_acceptance_packet_2026-10-30.json` and report: **83** representative Q&A cases; the packet remains **NOT CERTIFIED**.

This is a new bounded capability toward the still-open Phase 7 integrated difficult-research task. It does not finish general free-text QA, broader rules interactions, source completeness, current Oracle verification or release certification. The 137-task checklist is unchanged: **89 checked, 48 open, NOT_RELEASE_READY**. Phase 6 pilots and all 62 locked Grixis decks remain untouched.
