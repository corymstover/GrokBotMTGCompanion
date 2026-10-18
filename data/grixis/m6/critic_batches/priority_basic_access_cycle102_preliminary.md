# Cycle 102 — Preliminary engineering review: real access, basic mana and priority passes

**Scope:** M6 evidence-only. This is the author's technical review, **not an independent Pass C/I/J judgment or approval certificate**.

## Verified reproducible evidence

- Plan: `data/grixis/m6/phase_b_plans/priority_basic_access_62_01.json`.
- Main evidence: `data/grixis/m6/phase_b_bounded/priority_basic_access_62_01.json`.
- Small derived audit: `data/grixis/m6/phase_b_bounded/priority_basic_access_62_summary_01.json`.
- Fixed seed 102017; 62 authoritative deck baselines; 12 traces per deck; **744** shuffled 7-card openings plus one draw on each of four sampled own turns.
- All 100 unique physical cards are conserved per trace; no canonical list, M0–M5 acceptance, pending exception or approval is modified.
- Only available **basic lands** are played for mana in this access sampler; maximum one per turn. Arcane Signet is cast solely if actually held and two untapped basic-source physical cards are available to pay its printed mana. No injected mana appears in these access samples.
- Across 744 traces, Signet appears by turn 4 in **96**; the restricted policy casts it in **12**; it plays **440** basic lands total. These are counts under this model and selection policy, **not game win statistics**.

## Priority-window validation

- Cycle 101's bounded physical-stack adapter is wrapped by a four-seat, consecutive-pass state. The top frame resolves only after four passes; then the active player receives priority again.
- A scripted counter/removal outcome is prohibited before an opponent seat has priority. It remains a *recorded externally supplied outcome*, not a legally cast counterspell with targeting, payment or opponent AI.
- Source-backed basic-mana cost payment, controller priority and unsupported Abaddon-granted cascade are transactionally checked; failures cannot consume lands, mana, cards or change priority state.
- The Abaddon witness uses actual archived physical card IDs but **forces** the relevant cards into hand as a bounded stack/trigger test, not as a naturally drawn scenario.

## Red-team limitations and next work

1. **Nonbasic lands are not modeled.** Most of the actual 62 mana bases contain many nonbasics. The 12 source-paid casts out of 744 should never be interpreted as the real deck's ability to cast Arcane Signet; this is only a restrictive basic-land coverage check.
2. The sampler does not choose mulligans, play opponents' turns, draw for additional card effects, cast spells other than a sampled Signet, model alternate/additional costs, respond with real opponent spells, or execute actual Abaddon-granted cascade.
3. Four scripted priority passes are a useful invariant, **not full multiplayer priority/turn structure**; no comprehensive Magic rules correctness claim follows.
4. Twelve fixed trials per commander do not warrant statistical inference or an improvement recommendation. The intent is deterministic regression evidence.
5. Clerical plan text originally said "720" for 62 × 12; after the first green CI run this was transparently corrected to **744** with an explicit audit addendum. The original numeric sample and seed settings never changed; no measurements were selected after viewing outcomes.
6. The full evidence is too large to inspect via the repository's standard file-content connector; the compact summary is generated and independently compared by CI from the full dataset, not hand-authored.

**Next engineering recommendation:** explicitly model a small source-verified set of common nonbasic lands, with tapped/untapped entry, land-dependent life payments and color choices, and route that through the same actual-mana transactional stack. Keep invalid/complex land effects blocked. After that, extend actual 62-deck commander-specific action samples and independently review correctness. Do not promote M6, Phase B, Pass C/I/J or a deck change on this evidence.
