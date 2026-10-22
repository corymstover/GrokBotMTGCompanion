# Abaddon — post-PR545 M6 mechanical and decision gate ledger

**2026-10-22; active commander Abaddon the Despoiler; GPT-6 owner-equivalent review, not technically independent.** The 62 canonical decklists are historical approved/locked and never edited by this engineering work. Abaddon approved raw SHA-256 remains `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`. This supersedes the *next-action section* of `data/grixis/m6/phase_b_plans/abaddon_m6_coverage_disposition_20261022.md`, which was written before PRs #542–545; the older ledger remains evidence of what was actually known then.

## Source and test evidence already executed

| Obligation | Last reliable receipt | Disposition |
| --- | --- | --- |
| M6.4 entire deck depth | `data/grixis/m6/deep_reviews/Abaddon_the_Despoiler.md` and 62/62 depth tracker | Authored review complete; dated card-cost errata superseded by PR #543 |
| M6.5 critical Pass C | `data/grixis/m6/governance/pass_c_owner_waiver_20261021.json` and `owner_pass_c_substitute` | Owner formally accepted 62/62 GPT-6 equivalent; technically independent reviewer remains 0/62 |
| M6.6 hand-cast cascade, Ignus paid casts and adversarial priority | `tests/test_m6_abaddon_ignus_stack_windows.py`; `data/grixis/m6/phase_b_bounded/abaddon_ignus_stack_windows_20261022.md` | Eight controlled conditions, actual source-paid physical 99; correct Ignus mana ability, Rule of Law and Drannith |
| M6.6 Neheb/Assault/Loyal outlet | `tests/test_m6_abaddon_neheb_assault.py`; Actions `39727801845` | Twelve deterministic fixtures, removal breaks the line; not a claimed win percentage |
| M6.6 Chaos Warp/Otawara/hate | `data/grixis/m6/phase_b_bounded/abaddon_chaos_warp_stax_20261021.md` | Previous bounded paid access/answer cases; no guaranteed Warp replacement outcome |
| M6.6 nonhand payoff differentiation | `tests/test_m6_abaddon_lost_keeper_effect.py`, plan `abaddon_lost_keeper_effect_20261022.json`, Actions `39738731718` | Seven preregistered states in six test methods: Spawn created on actual nonhand spell cast and library-origin land; Keeper target opponent damage equal to MV. Zero-MV hit deals zero Keeper damage |
| Full exact-name current Oracle/official Commander legality | PR #545 head `2e987dd61ae09f9f0240ffeca6c441904fe80d76`, Actions `39740268083`, uploaded artifact `12407954955` | 97 distinct card identities across five exact 100-card physical source/candidate lists; passed live Scryfall collection name checks as of 2026-10-22; original canonical SHA-pinned, main independently rechecked via connector |
| M7 whole-deck physical contenders | PR #543 V2 4 exact alternatives + PR #544 effects + current `portfolio_v3_decisive.json` | Authored recommended *candidate* now `+Ignus/+Chaos Warp, -Rakdos/-Inevitable Betrayal` while retaining Keeper. More matchup data could reverse choice; owner has not approved |
| M6 I/J integrity | `scripts/grixis_m6_ij.py`, `scripts/grixis_m6_bundle_check.py`, I/J contract | Generic input receipts/checkers exist; **no complete Abaddon I local tested-pool certificate or final J bundle** |

## Truthful open mechanical/approval gate

**M6.6 = PARTIAL.** Missing an explicit exhaustive list of which applicable Abaddon P0 source/rules interactions remain unexecuted under the independent project certification standard; existing 99-card sparse effect modeling cannot prove all 99 abilities. The first next work is a finite, per-case *inventory* of decision-relevant P0 work, mapping actual implementation test names and required unsupported cases, **not** another mass simulation. Reuse the completed 8/12/7-case fixtures, but do not rename them as complete 99-card effect coverage.

**M6.7 = PARTIAL.** Current authorship ends the *material card choice* stage for Ignus/Warp/Assault/Ruinous and the Keeper/Betrayal cut choice, with counterarguments and actual 100-card alternatives. Formal M6.7 cannot be declared complete without reconciling explicit applicable M6.6 obligations and signable judgment receipts.

**M6.8 (I) = BLOCKED.** No schema-qualified certificate can assert a local zero-improvement conclusion in the defined tested pool while the materially selected Ignus/Warp package is a plausible upgrade and applicability of all test obligations remains open. Do not conflate local optimality with global proof.

**M6.9 (J) = BLOCKED.** A preliminary integrity scheme exists, but no final source/candidate replay bundle binds all required Phase B, sealed reviewers, official rules version, current Oracle snapshot (especially the private source snapshot mode), exact test head, case execution and limitations.

**M6.10/M7 new approvals = BLOCKED/0.** No owner acceptance. All historical 62/62 approval and locks remain intact.

## Next bounded step

1. Inspect the Abaddon-specific P0 list in `data/grixis/m6/phase_b_plans/abaddon_certification_gap_20261022.json`, inventoried executed test methods, and the current source Oracle/legality artifact; inventory remaining applicable P0 rules without inventing engine support.
2. Implement only missing, exact decision-changing P0 mechanical cases under a deterministic source-paid fixture, validate exact-head CI and record case-count reconciliation.
3. Recompute original and preferred final 100-byte hashes and prepare strict I/J bundle once it can genuinely pass; **do not issue I local optimum before there are no unresolved improving substitutes**. M7 requires schema-valid final packet and separate exact owner approval.

**No new gameplay simulation in this documentation action.** Nothing here changes canonical cards or certifies M6.
