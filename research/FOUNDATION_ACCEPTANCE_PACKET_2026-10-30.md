# Knowledge-foundation evidence for owner review — 2026-10-30

**Status: PRELIMINARY / NOT A CERTIFICATION / NOT OWNER ACCEPTED.**

This source-graded packet is reproducible from the repository, with exact input hashes. It is a bounded acceptance *review surface*, not a claim to know all Magic history. Phase 6 deckbuilding and its three pilots remain deferred.

## Inventory and supported lookups

- 576 official source pages cited and 50 reviewed without a claim within the inventoried 626-page scope. Citation does not mean exhaustive reading.
- 1211 source-graded graph claims across 5186 nodes; 33 registered planes, 16 still thin.
- 483 registered characters and 146 factions; 629 with direct cited claims, 0 without.
- 53 previously researched on-plane contextual claims in 4 dossiers, strictly distinct from new/direct graph claims.

## In-universe chronology (not a complete timeline)

- Legacy ledger: 56 events, 177/3074 ordered event pairs; 2897 unresolved, 13 components, 0 cycles.
- Source-local ledger: 31 events, 52/465 pairs. These counts are separate, not additive.
- L244 cross-source historical ordering remains open. UNKNOWN is the correct answer when no cited bridge exists.

## Representative end-to-end questions

| Question | Route | Confidence | Cited URLs |
| --- | --- | --- | ---: |
| What is the history of Alara? | `ask->plane_history` | `QUALIFIED` | 1 |
| What is the history of New Capenna? | `ask->plane_history` | `QUALIFIED` | 8 |
| What is the lore of Nicol Bolas? | `ask->entity_history` | `QUALIFIED` | 38 |
| What is the history of the Gatewatch? | `ask->entity_history` | `QUALIFIED` | 17 |
| What is the history of the Izzet? | `ask->entity_history` | `QUALIFIED` | 5 |
| Who is Ugin's twin? | `ask->lore:sibling_of|twin_sibling_of` | `VERIFIED` | 4 |
| Who killed Elesh Norn? | `ask->lore:killed` | `VERIFIED` | 1 |
| Explain the continuity of Ugin | `ask->continuity` | `QUALIFIED` | 27 |
| Who currently leads the Orzhov Syndicate? | `ask->lore:led|leader_of|leads` | `QUALIFIED` | 2 |
| Did Konda imprisons a part happen before Kyodai and Michiko defeat Konda? | `ask->chronology` | `QUALIFIED` | 1 |
| Did Konda imprisons a part happen before Marina lures her bullies? | `ask->chronology` | `QUALIFIED` | 0 |
| Can Sol Ring go in a Urza, Lord High Artificer deck? | `ask->rules:include` | `VERIFIED` | 1 |
| How many cards are in Alpha? | `ask->set_atlas:set` | `QUALIFIED` | 3 |
| Which sets was Black Lotus printed in? | `ask->set_atlas:card_printings` | `QUALIFIED` | 1 |
| How does Urza's Saga interact with Urza's Tower? | `ask->rules_evidence:interaction` | `QUALIFIED` | 3 |
| Did Karn introduces Phyrexian oil to Mirrodin happen before Mirran forces are overwhelmed in the early conquest? | `ask->chronology` | `QUALIFIED` | 1 |
| Did P:mirrans_overwhelmed happen before P:venser_restores_karn? | `ask->chronology` | `QUALIFIED` | 0 |
| What is the history of Eric Kenrith? | `ask->entity_history` | `QUALIFIED` | 1 |
| What is the history of Hazel Kenrith? | `ask->entity_history` | `QUALIFIED` | 1 |
| What is the history of Lyra Dawnbringer? | `ask->entity_history` | `QUALIFIED` | 1 |
| What is the history of Valentin? | `ask->entity_history` | `QUALIFIED` | 1 |
| What is the history of the Cabaretti? | `ask->entity_history` | `QUALIFIED` | 1 |

The underlying JSON retains response digests, exact source URLs and caveat flags. The two graph-navigation examples are **not** evidence of chronological or causal paths.

## Still open before foundation certification

- Quoted relative ordering does not yet establish a complete cross-source or cross-plane chronology.
- Plane histories and direct character/faction claims are incomplete, not a census of Magic canon.
- Pack A genealogy disputes GD2–GD7 require source-backed resolution or explicit owner decisions.
- No general game-state simulation or proof for uncited complex card interactions exists.
- Phase 1B qualified snapshot limits and release-time Oracle freshness require separate review.
- Actual owner foundation-scope acceptance and exact-release CI have not occurred.

## Reproduce

```bash
python3 scripts/build_foundation_acceptance_packet.py --check
python3 -m unittest discover -s tests -p 'test_foundation_acceptance_packet.py' -q
python3 -m unittest discover -s tests -p 'test_mv_ask*.py' -q
python3 scripts/certification_dry_run.py --check
python3 scripts/update_multiverse_progress_tracker.py --check
```

Packet SHA-256 (canonical JSON): `648a179ed061759e0be0ecc971b6e5c5c7b3b2fd1f7915c3493a642b51fb89e3`

**No decks were built, modified, reviewed or approved.**
