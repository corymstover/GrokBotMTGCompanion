# v3.04 — Three lore-first Commander strategy preflights (not power certification)

**Prior certified milestone:** the v3.00 knowledge foundation remains **7/7 independently certified** against its immutable exact tree. **Full 137-item project:** **113 checked / 24 open**. K108, K110 and each of K112–K114 stay open. This change supplies new mechanical evidence rather than prematurely checking an item.

## Exactly what was checked

`scripts/audit_phase6_strategy_preflight.py` loads all **three** unchanged `UNAPPROVED` pilot specifications and their existing printing evidence. It repeats the pilot's full 100-card/singleton/status/identity audit, then independently resolves *each* named card to its committed `data/card_index.csv` Oracle identity and `cards/` shard mana value. Basic lands are counted from the original spec. For every staged strategy, the engine requires at least two *present* cards from **each** of four distinct functions: mana acceleration, card/resource flow, interaction and game payoffs. The engine matches curated mechanical phrases against the *Oracle text lines*, not flavor, story notes or external synergy guesses.

| Preserved pilot | Lands / 100 | Mean MV, nonland incl. commander | Nonlands MV ≥5 | Nonlands MV ≥7 | Honest hypothesis |
| --- | ---: | ---: | ---: | ---: | --- |
| Ugin & Bolas | 35 | 4.185 | 32 | 7 | Slow casual, untested |
| Original Primeval Dragons | 37 | 4.302 | 26 | 10 | Mana-intensive casual, untested |
| Ugin's Allies and Heroes | 36 | 3.641 | 16 | 7 | Synergy-dependent casual, untested |

The figures are deterministic tallies of *dated Oracle data*, not turn-to-cast simulations; commander cost reduction, color accessibility, opening hands, land entry tapped, commander taxes, alternate costs and interaction timing are not modeled. The dated index is from **October 15**, while the pilot exact-printing snapshot is **October 29**. Format legality/bracket and post-October-19 CR changes remain independent K110 review items.

## Real strategies, including the weak points

1. **Bolas/Ugin Grixis control.** Early mana rocks (Sol Ring, Arcane Signet, Hedron Archive), reactive defense (Mana Drain, Crux of Fate), and later Nicol Bolas/Ugin planeswalkers; the commander transforms for card flow. The Bolas's Citadel plan is conditional. **Risk:** 32 of 65 nonland cards cost at least five mana, creating a slow, inconsistent opening without rock acceleration and correctly colored sources. The deck does not have a demonstrated competitive win loop.
2. **The Ur-Dragon's five-color Elder/Primeval combat.** Prioritize green for Cultivate, reduce Dragon costs with Dragonlord's Servant/Urza's Incubator, replenish with Kindred Discovery/Herald's Horn, interact with removal, and use The Ur-Dragon's attacks and Rith's token payoff. **Risk:** 10 cards at seven or more mana; five-color historic legends and tapped fixing raise the real casting burden beyond the aggregate MV. A sweeper may erase the entire Dragon combat engine.
3. **Jace/Gatewatch four-color loyalty control.** Use rocks, removal and sweepers to defend Jace, then increase planeswalker loyalty activations through Oath of Teferi, Flux Channeler, Deepglow Skate or The Chain Veil. **Risk:** the WUBR commander and high-end Eldrazi/Angel/Ugin lore inclusions strain a divided plan; The Chain Veil is costly and has a downside without loyalty activations.

All curated card-role excerpts and staged opening/middle/finish plans reside in `data/lore_decks/strategy_preflight_spec_2026-11-01.json`; the deterministic rendered results and source SHA-256s are in `data/release/phase6_strategy_preflight_2026-11-01.json`. The code **does not modify or propose silently replacing any card**, set approval flags, attach an owner signature, or rewrite the certified Grixis protected files.

## What would earn K108/K110 completion

- Reconcile each original list with genuinely current Commander rules/Oracle legality and specific gameplay interactions, including any discovered combos, before declaring a final list (K110).
- Use audited turn-by-turn goldfish/mana-color checks plus independent real multiplayer/matchup testing to determine whether a strategy's claimed casual-power ceiling is realistic, not just narratively appealing (K108).
- Resolve weaknesses with **separately reviewed proposals**, never by rewriting the preserved `UNAPPROVED` drafts or the 62 protected Grixis decks. Individual owner acceptance of each pilot remains its own K112–K114 decision.
- Retain uncertainty for Elder Dragon parentage and art claims: a functional card text is not a lore-source or scene-depiction citation.

## Replay

```bash
python3 scripts/audit_lore_pilot.py
python3 scripts/audit_phase6_strategy_preflight.py --check
python3 -m unittest discover -s tests -p 'test_phase6_strategy_preflight.py' -v
python3 scripts/audit_ci_domain_coverage.py --check
python3 scripts/audit_full_checklist.py --check
python3 scripts/update_multiverse_progress_tracker.py --check
python3 scripts/audit_foundation_milestone_certificate.py
```

Eight negative/positive unit tests include rejecting invented Oracle effects, a real card absent from the target pilot, removed roles, omitted pilots, fake definitive power claims and stale report bytes. The Phase 6 PR workflow runs the preflight and its tests. CI success of a different SHA, PR or merge never substitutes for this candidate's own checks.
