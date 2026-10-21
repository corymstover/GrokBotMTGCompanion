# Abaddon — Rakdos, Lord of Riots opportunity cost for Aggravated Assault challenger

**Date:** 2026-10-21 (America/Chicago)  
**Evidence class:** deterministic Oracle-cost arithmetic + frozen 100-card creature inventory. **Not** effect-aware full-deck gameplay or a comparative win rate.  
**Precommitted plan:** `data/grixis/m6/phase_b_plans/abaddon_rakdos_role_20261021.json`, originally committed at `3164204c8fec2c19d6d2a43c3ccae16ac00473e2`.  
**Candidate only:** +`Aggravated Assault` / -`Rakdos, Lord of Riots`. Neither card was changed in the approved baseline.  
**Canonical raw file SHA-256:** `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`, approval remains APPROVED/LOCKED.

## What the existing one-for-one proposal puts at risk

Rakdos's **creature spell** generic-mana reduction counts the same current-turn *aggregate opponent life loss* that Abaddon's hand-cast cascade threshold uses. The frozen source-baseline has **18 creature card names counting Abaddon and Rakdos**; therefore **17 creature identities can potentially benefit from Rakdos**, excluding Rakdos itself. This is a *conditional name inventory*, not a claim that all 17 are available at once, have a generic pip to reduce, or will be cast after Rakdos.

The authoritative [Wizards Ravnica Remastered release notes](https://magic.wizards.com/en/news/feature/ravnica-remastered-release-notes) clarify that reductions use life **lost**, not net change in opponents' life totals; reduction cannot pay colored requirements, cannot reduce Rakdos's own cast, and applies **after commander tax/additional costs**. Rakdos requires an opponent to have lost life before *casting Rakdos*; its cost is `{B}{B}{R}{R}`. It must have resolved and remain controlled before discounting subsequent creatures; this is not a retrospective discount.

| Subsequent spell/cost at nine aggregate opponent life lost, Rakdos already controlled | Generic after discount | Colored cost still due | Printed mana value |
|---|---:|---|---:|
| Abaddon first cast, as commander | 0 (was 2) | `{U}{B}{R}` | 5 |
| Abaddon third cast, with four generic commander-tax mana | 0 (was 6 total generic) | `{U}{B}{R}` | 5 |
| Neheb, the Eternal | 0 (was 3) | `{R}{R}` | 5 |
| Loyal Subordinate | 0 (was 2) | `{B}` | 3 |
| Prosper, Tome-Bound | 0 (was 2) | `{B}{R}` | 4 |
| Aggravated Assault enchantment spell | 2 (unchanged) | `{R}` | 3 |
| Aggravated Assault activation | 3 (unchanged) | `{R}{R}` | n/a |

Abaddon's own cascade-from-hand restriction remains unchanged: a commander cast from the **command zone** does not gain cascade from its own ability; the mana-value comparison of eligible other hand spells is printed mana value, **not discounted payment**. No physical mana-source colors or availability are inferred.

## Comparative judgment, explicitly bounded

The prior [Neheb/Assault/Loyal fixture](abaddon_neheb_assault_20261021.md) established a **conditional**, unopposed extra-combat drain finish when all key permanents are present, with legal postcombat Neheb mana and no interaction. This new fixture tests **the opportunity cost of removing Rakdos**, not the frequency of assembling either engine.

**Tradeoff:** Assault is cheaper to initially cast (three mana, one red pip), supports a compact four-piece repeat-combat route with Neheb and Loyal and Abaddon, and is a noncreature permanent. Rakdos is harder to cast (`{B}{B}{R}{R}`, prior opponent loss needed) and vulnerable to creature interaction, yet reinforces Abaddon's signature same-turn loss threshold and can accelerate multiple subsequent creatures, notably Neheb and commander recasts. These are distinct, non-interchangeable roles. Total discounted *potential* is not a quantitative win benefit.

**Disposition:** Challenger's net superiority is **not established**. Keep the **original approved baseline untouched** and carry both the Assault combo upside and Rakdos role loss into the full M7 whole-deck optimization. Do not apply the old Pass C recommendation automatically. Full source-paid access, removal exposure, hand-cast timing, mana-color feasibility, cascade throughput, and plausible replacements beyond the one-for-one slot remain for M7 judgment.

## Reproducibility and governance

- `scripts/grixis_m6_abaddon_rakdos_role.py` checks inventory using the frozen graph and approved source export, then runs explicit generic-mana cost cases.
- `tests/test_m6_abaddon_rakdos_role.py` tests eleven rule/inventory invariants. Test results are meaningful only after exact-head CI passes.
- The graph and source-export are support snapshots, not owner authority. Canonical approval remains exclusively in `corymstover/grixis-commander-encyclopediaGPT/main`.
- This does **not** complete M6.5's originally independent review, certify M6.6 Phase B for Abaddon, or approve M7. It is targeted Phase B evidence with `can_decide_swap=false`.
