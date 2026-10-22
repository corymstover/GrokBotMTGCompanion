# M6 — Remaining 61 Commander-specific effect test design backlog

**Prepared 2026-10-22; DESIGN ONLY. NO effect-test implementation, execution, PASS result, measured win rate, M6 certificate, new owner approval or canonical deck change.**

This is a prospective test-plan inventory **for the 61 decks after Abaddon**. It intentionally keeps Abaddon locked/unchanged and leaves the existing M6.6 and M6.7 incomplete. The owner requested these cases be written *ahead of time*, without running them.

## Deliverables

- [`data/grixis/m6/test_blueprints/index.json`](../data/grixis/m6/test_blueprints/index.json): exact registry order for the remaining 61, priority counts, approved-source SHA reference, proposed reusable mechanics families and limited authority.
- `data/grixis/m6/test_blueprints/<Deck_ID>.json`: **61 individual files**, each source-anchored to the existing commander blueprint; contains direct commander Oracle snapshot, documented key interactions, named online engine prerequisites, finish conditions, and conditional failure/red-team fixtures. Each case is tagged **P0** or **P1**, with legal setup and expected assertion to independently verify.
- `scripts/grixis_m6_test_blueprint_catalog.py`: **read-only optional inspector/normalizer** for the draft documents, which were authored in several compatible formats. It never invokes any simulation, code from an effect adapter, or an existing unit test. The archive is accessible without using the inspector.

**Audited static inventory:** 61 plan files + one index; **882 case specifications**: 308 P0 and 574 P1. Planned tests actually run: **0**. Planned effect adapters implemented: **0**. Therefore the 882 count is not 882 ready-to-run Python unit tests or 882 guarantees of future necessary test executions. The final per-deck count should be reduced or expanded in response to material strategic uncertainties.

## Priority policy

**P0**: each commander's actual ability and valid zone/trigger/timing, first three documented unique interactions, and the most important documented failure/disruption case. For partner pairs, there are two direct commander cases. These generally need independent current Oracle verification and the targeted mechanism implementation before they can yield meaningful positive results.

**P1**: remaining source-listed interaction rulings, first documented engine loops, main win-condition traces (including false-infinite guardrails), and additional failure cases. **Do not run all P1s blindly**: implement only those needed to resolve real candidate comparisons, uncertain rules, or high-impact functional weaknesses. P1 does not mean low strategic importance: an unusual combo or contradictory official ruling can move to P0 when that deck is actively reviewed.

Each physical fixture should test positive *and* counterexample cases, correct real costs, cards/owners/physical zones, color identity and source count, timing and targets, and whether a loop actually produces bounded resources or a proven repeatable state. Avoid inferring a full-game win percentage from prearranged boards.

## Source authority and known registry historical differences

- Primary source per deck: existing `data/grixis/blueprints/<slug>.json`, including archived Oracle snapshot, `key_interactions`, `engines`, `win_conditions`, `failure_modes` and evidence pointers. The text from these blueprints is labeled a **source claim to test**, **not a newly verified 2026-10-22 Oracle truth**.
- Canonical approval repo remains `corymstover/grixis-commander-encyclopediaGPT@main`, `state/current_deck_overrides.json`; all 62 baseline decks were verified APPROVED/LOCKED at planning time. Each pending document includes a frozen SHA and source list Git blob, used for future invalidation.
- Historic registry aliases exist: `Anhelo__the_Painter` ↔ `Anhelo_the_Painter`, `Ashad__the_Lone_Cyberman` ↔ `Ashad_the_Lone_Cyberman`, `Be_lakor__the_Dark_Master` ↔ `Be_lakor_the_Dark_Master`, and `Norman_Osborn_Green_Goblin` ↔ canonical `Goben__Gene_Splice_Savant`; names were linked by **exact approved SHA**, not silently renamed. Those records must be checked against live canonical aliases before actual test execution.
- Some historic registry entries have `recorded_matches_raw=false` despite an approved canonical recorded hash; these are **provenance reconciliation flags**, not a license to replace the source or claim the deck is unapproved. Independently verify exact bytes when the deck's tests start.
- **A 94-line `1x` TXT is not necessarily 94 cards.** Repeated basics may be represented with `Nx` on a single line. The `source_card_lines`, `source_baseline_count_needs_reconciliation`, and similar legacy fields refer to **line entries**, NOT a verified physical-card count; `line_count != 100` is **not evidence of an invalid deck**. At execution, independently quantity-expand the latest canonical approval and verify actual commander + library + authorized companion handling.
- Project-authorized exceptions must be preserved and labeled correctly: Lutri is the officially banned companion in the designated Bjorna/Cecily list, and Trade Secrets/Yawgmoth's Bargain are allowed only as designated project exceptions; planned-release commanders are not automatically currently released/offically legal.
- No generic suite PASS, cache hit, authored review or precomputed blueprint passes M6.6 (real effect-aware evidence), M6.7 (actual commander-specific judgment), formal M6 certification, or new M7 owner approval.

## Mechanic-family reuse backlog

The index preassigns representative decks to common mechanics. Implement one *correct* **source-paid and Oracle-verified** reusable primitive before commander-specific per-deck scenarios consume it.

| Reusable adapter candidates | Representative decks | High-value shared semantics |
| --- | --- | --- |
| Combat damage and theft | Beckett Brass, Edward Kenway, Thraximundar | distinct damage sources and opponents, attack timing, combat-damage triggers |
| Copies versus casts | Anhelo, Fire Lord Azula, Parnesse, Zevlor | targets/modes, extra costs, cast triggers vs copies, stack windows |
| Activated objects / cages | Mairsil | acquired abilities, per-object use limits, copying restrictions, blink |
| Artifact copies/sacrifices | Ashnod, both Mishras, Dr. Eggman | artifacts/constructs, token object identity, sacrifice payments |
| Death and recursion | Marchesa the Black Rose, Missy, Sedris | death/replacement/finality/unearth and correctly timed return |
| Opponent-owned cards in exile | Jeleva, Evelyn, Madcap Jester, Don Andres | ownership, permission, hand/exile casts and usable mana |
| Extra end steps / delayed triggers | both Obekas, Lynde, Sol'Kanar the Tainted | trigger multiplicity, delayed effects, reset by new object |
| Draw/discard/mill | Nekusar, Lord Xander, Gwendlyn | per-player attribution, replacement and empty libraries |
| Transform / modal effects | Kefka, Nicol Bolas the Ravager, Norman/Goben | face/state changes, object IDs, command-zone/tax rules |
| Multi-commander and exceptions | Bjorna/Cecily/Lutri, Kraum/Tevesh, Rograkh/Silas | separate commanders, partner eligibility, companion legality flag |
| Graveyard casts and storm | Kess, Cormela, Inalla | cast permissions, taxes, source cards after spell resolves |
| Choices / villainous effects | Davros, The Valeyard, The Rani, Cult of Skaro | opponent choices and random/modal outcomes |

These are **candidate adapters only**, not falsely labeled implemented code. If two commanders both need the same primitive, implement its factual rules once, extend the source-aware test matrix, and execute those cases during each actual deck review. The new reusable PASS-only foundation cache from PR #534 can skip identical shared tests, while newly introduced or changed mechanics must be independently tested.

## How to use this later (but DO NOT run tests now)

For an upcoming deck, open its `test_blueprints/<Deck_ID>.json`. Read P0 first, confirm the exact current canonical deck and refreshed Oracle, map the named cards to physical sources, and implement only the missing rules primitives/negative fixtures. Then run the actual effects, inspect outcomes, decide whether additional P1 fixtures are decision-material, and record verified receipts. Do not reopen the source data pipeline merely to rerun generic candidate rankings.

An optional read-only inventory inspection command is `python scripts/grixis_m6_test_blueprint_catalog.py --deck-id Admiral_Beckett_Brass --priority P0`. This parses case **descriptions**; it cannot run or certify those effects. `--summary-only` shows case counts, while `--json-out PATH` emits a source-labeled queue.

## Design quality / readiness caveat

This was a **bulk source-backed test-design pass**, not 61 independent fresh Oracle/legal audits and not 61 sets of complete executable rules fixtures. Some older blueprints carry previously corrected disputed assertions or conditional interactions that may depend on cards absent from the current list; these must be corrected/confirmed before executing, rather than encoding a false source claim as an unquestionable expected value. Each plan marks absent/unproven named cards so a hypothetical candidate isn't mistakenly treated as part of an approved deck.

**Next engineering work when resumed**: complete Abaddon on its own evidence; then consume the P0 plans one commander at a time. Prioritize adapting common mechanics, not repeating a long four-arm Abaddon simulation 61 more times. Keep every existing canonical approval locked until owner explicitly approves changes.
