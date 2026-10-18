# Cycle 108 — Actual Abaddon/Bituminous Blast cascade offers: preliminary engineering critique

**Authority:** this is author-side source/evidence analysis only. **Not** independent Pass C, full Phase B, zero-improvement, deck upgrade, or M6 acceptance. All 62 canonical lists remain approved and locked.

## Source, scope and reproducibility

- [Preregistered seven-offer audit](../phase_b_plans/abaddon_cascade_offer_triage_01.json) was committed first at `513a1612cc0ef5ce1f52d47187ead34b0fc7689b`, before deriving the card names from Cycle 107 evidence.
- [Post-result exploratory card-specific mechanics addendum](../phase_b_plans/abaddon_cascade_role_followup_01.json) was committed **after** those seven names were observed; the added printed-text checks are explicitly **not** falsely labeled preregistered hypotheses.
- [Deterministic Oracle-gated receipt](../phase_b_bounded/abaddon_cascade_offer_triage_01.json) reconciles the **seven identical physical printed-cascade offers** under Cycle 107's scripted opponent 3/3 target-survival and target-removal policies. Fourteen policy rows represent the same seven offered cards; **not fourteen independent games**.
- Every hit is a printed-mana-value-less-than-five nonland card in the exact approved Abaddon main library. Name, printed Oracle type/cost/text and card-specific mechanisms are verified against the hash-pinned October 2026 Scryfall source. Source approved raw SHA remains `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`.

## Actual revealed offer identities and conditional role

| One offered card | Opportunity if legitimately chosen and resolved | Decisive remaining requirement |
|---|---|---|
| **Mana Vault** | Fast colorless mana, can tap for three colorless | Actual casting/resolution, spell-follow-up availability; later untap/upkeep burden |
| **Windfall** | Discard-and-redraw all players' hands | Actual four player hands, discard triggers, resulting card values |
| **Deflecting Swat** | Retarget stack interaction | Legal target spell/ability and relevant new targets. Blast itself is still on the stack beneath cascade; benefit not established |
| **Demonic Tutor** | Search library for a chosen card to hand | Actual library choice policy, cast/follow-up, shuffle |
| **Chrome Mox** | Conditional imprint-based colored acceleration | Requires suitable card from hand to exile and determines mana colors; free entry does not imply free colored mana |
| **Vampiric Tutor** | Search library and put chosen card on top, losing two life | Actual selection, draw access and controller life cost |
| **Sol Ring** | Colorless acceleration | Legal casting, artifact resolution and actual next payable spell |

These offers are not interchangeable. **Three** were mana artifacts, **two** tutors, **one** discard/draw wheel and **one** target-redirection spell.

## Known versus unknown

- **Known:** Bituminous Blast had 7 physically cast, source-paid opportunities among 240 scripted Cycle 107 baseline histories with an externally supplied opposing 3/3 target. With that target surviving, the seven spells removed it; when the target disappeared after casting, Blast failed to resolve but the seven printed cascade triggers still found their identical lower-MV offers.
- **Known:** the seven offered cards are printed real cards in the approved 99, with potentially strategically relevant effects.
- **NOT known:** whether a player could or would choose each offer and legally cast/resolve it in the recorded priority/board state; the downstream effects, mana-use opportunities, tutor selections, four opposing hands or actual comparative value. Cycle 107's controller chose to **decline every optional cascade cast** as a conservative implementation decision; that is not evidence a competent player would decline them.
- **NOT known:** expected frequency of these opportunities in real Commander multiplayer games, actual card-win impact, and whether Heartless Hidetsugu or Tree of Perdition replacing Blast would improve Abaddon's strategy. This seven-card sample cannot justify a superiority claim, even though card identities are qualitatively promising.
- **No equal opponent-board comparator exists yet:** Heartless's tap affects players, Tree targets a single opponent's life, and Blast answers a 3/3 creature. The difference is real role differentiation, not automatically a value ranking.

## Open model gates / next experiment

Do **not** continue adding generic mana or Oracle keyword counts and calling that deck optimization. The next useful M6 test is a preregistered *actual cascade cast-from-exile/resolution replay* of these seven named cards with original physical IDs, and the exact bounded game states where they appeared. Carry the opponent 3/3 and remaining Blast on the stack, prioritize **Demonic Tutor, Vampiric Tutor, Mana Vault and Sol Ring** for effectful resolution using the existing Cycle 99 tutor engine and ledger; model Chrome Mox's legal imprint separately. Add appropriately complete four-player hands before attempting Windfall; explicitly decline or mark the uncertain redirection outcome of Deflecting Swat. Include actual post-hit land mana, commander state and follow-up. Independently verify correct ordering (cascade trigger resolves, offered spell may be cast from exile on top of unresolved original Blast, then effect resolves); a spell cast from cascade exile does **not** receive Abaddon's hand-only cascade.

If any required effect or opponent choice is not modeled, retain `CANNOT_EVALUATE`. Mandatory independent critic and real deck-specific Phase B for all 62 remain outstanding.

**Decision position:** preserve the currently approved Bituminous Blast baseline. Do not approve Heartless/Tree, infer numeric card strength, accept M6, or issue a tested-pool certificate from this evidence. This is a **useful source-derived target list for real follow-through tests**, not a completed superiority test.
