# Grixis Commander Encyclopedia — decisive optimization and test-economy contract

**Owner direction: 2026-10-22. Effective for all 62 commander-specific M6 mechanical investigations, M7 final optimization packets, and M8 exports.** This standard supplements (and where it differs, governs prospective work under) `AGENTS.md`, the M6 single-deck deep-review standard, M6 I/J contracts and existing quality gates. Historical completed reviews, original experiment records, immutable owner approvals and hashes are not retrospectively rewritten.

## Non-negotiable outcome

**Produce the strongest realistic, commander-first version of each deck; do not mistake "no statistically proven advantage in an incomplete simulator" for "the incumbent is best."** The owner expects substantive optimization of the *whole* 100-card deck after weeks of research, including off-ranking options and multiple coherent swaps where warranted. Preserve the distinct commander engine and natural power ceiling; never force generic Grixis staples or inflate brackets. A zero-swap or one-swap final recommendation is allowed **only after an explicit heightened opportunity audit**, not because a previous Pass C/M6 candidate received `HOLD`, a test excluded most card effects, or a model produced no winner. There is no arbitrary quota or artificially required swap.

A **test result** may legitimately be uncertain because effects, opponents or outcomes are not modeled. A **deckbuilding judgment** must still reach a reasoned **SELECT**, **REJECT**, **RETAIN_ALTERNATIVE**, or **EXCLUDE_INVALID** disposition, with its limitations disclosed. Unresolved genuine Oracle, legality, identity, source-integrity, payable combo or required M6 certification facts are **hard blockers**; never fill evidence gaps by invention or pretend CI/proxy coverage passed. When a major strategic decision remains sensitive to unknown information, make the strongest reasoned provisional recommendation, distinguish it from verification and identify precisely what fact could reverse it; do not submit an unverified final deck for owner approval.

## One finite decision process per deck

### A. Recover the whole deck and opportunity map — BEFORE new tests

- Confirm the live canonical approved/locked exact hash and 100 cards, legal commander identity, known project exceptions, blueprint, all 62-review research, Pass C, M5/M6, EDHREC and current Oracle/rulings as relevant. Historical M6 `KEEP` and `HOLD` are input evidence, **not M7 verdicts**.
- Complete the 99-card structural role and weakest-slot audit: commander enablers, accelerants, threshold sources, payoff density, interaction, protection, draws/tutors, mana base and color availability, curve, recursion, resilience, secondary wins, role congestion and redundant top end. Explicitly rank plausible *cuts*, not merely candidate adds.
- Assemble material candidates from **all** existing ranked and off-ranking research. Group substitutes by actual roles, identify interacting packages and likely multi-card portfolios; compare named alternative cuts and incumbent opportunity costs. Log each significant candidate as considered, selected, rejected, retained alternative or invalid with a concrete reason. Reject obviously inferior/illegal candidates quickly via sourced functional dominance.
- Define a **competitive baseline and at least one complete, legal 100-card challenger configuration** when evaluating a proposed swap; examine related simultaneous swaps as packages if interactions make one-for-one tests misleading. Do not benchmark isolated hypothetical extra cards added to 100.

### B. Choose the simplest *discriminating* verification technique

Use this ordered ladder; **stop at the cheapest sufficient step**:

1. Exact Oracle and Commander rules/legality proof; cost arithmetic, mana color proof, phase/stack sequencing, target/zone constraints, deterministic interaction/finite combo trace.
2. Structural role, synergy and dominance comparison: how each candidate materially improves the commander strategy and what every named cut sacrifices. Explicitly distinguish conditional ceiling from reliable floor.
3. Small matched **physical 100-card** fixtures or paired opening-hand/turn-access comparisons with identical seeds, actual costs, incumbent effects and named relevant opponent interference.
4. Only if steps 1–3 cannot discriminate a genuinely close/high-impact choice, a bounded effect-aware paired experiment implementing **both** candidate and incumbent relevant mechanics. Model meaningful opponent response/engine fragility rather than only uninterrupted goldfish.
5. Larger or repeated simulation **only if** a documented, concrete expected information gain can reverse the decision and the smaller method is inadequate. No default 2,000/20,000/100,000 samples, no test-count quota, no building a complete Magic engine for one swap.

**Reuse** frozen fixtures, rules tests, source snapshots and deck-specific blueprint cases. Combine shared ability mechanics across commanders into parameterized tests. Preserve applicable P0 verification from the 61-deck PR #535 backlog but translate its cases into economical, executable assertions rather than automatically launching 882 separate gameplay studies. P1 relevance is evaluated by decision impact and explicit existing M6 certification obligations; never silently mark unrun cases passed.

### C. A mandatory decision question BEFORE expensive simulation

Every materially expensive experiment must have a **precommitted decision brief** containing:

- Commander, authoritative 100-card source SHA, existing list, named challenger list and exact add/cut package; the identity/role being optimized.
- One answerable comparison question and one *falsifiable* decisive hypothesis, not "find out whether card X is good."
- Exact Oracle/rules preconditions; payable mana and timing; game-state initial conditions; modeled incumbent **and** challenger effects; one realistic adverse condition.
- A primary commander-relevant endpoint (e.g. reliable cascade opportunities, protected line completion, turn-to-payable-engine, answer effectiveness) and explicit tradeoff endpoints (incumbent engine loss, interaction, mana strain and setup fragility). State the smallest difference that would alter the **actual proposed M7 card choice**.
- The method's unsupported effects and bias direction; reproducible source fixtures, seeds, code and expected work ceiling.
- A **finite stop rule**: decision thresholds and what happens if close/equal; maximum experiment batch *in advance*; and a predeclared **judgment fallback** when the model cannot distinguish candidates. The fallback is a best-supported choice with stated confidence, **never fabricated empirical certainty**.
- An explicit written reason **why existing evidence/analytic proof cannot already decide**. If no plausible result could change the choice, **do not run the experiment**.

Default: **at most one substantive discriminating experiment per tightly defined candidate decision cluster**. A second requires a *documented model bug, invalid assumption, or newly discovered decision-changing interaction*, with a repaired question and revised stopping rule. More simulations solely to escape "inconclusive" are prohibited. High-volume randomized trials require special justification before execution. Ordinary small unit/regression tests for mandatory P0 rules verification are not counted as repeated expensive simulation campaigns.

### D. Finish the decision; no inconclusive candidate status in final M7

For every material candidate and named cut, write an authored conclusion:

- **SELECT_ADD** — strongest justified role/identity upgrade after weighing opportunity costs; name the exact cut(s).
- **REJECT** — not better than the strongest available package; specify decisive weakness.
- **RETAIN_ALTERNATIVE** — plausible, but loses to selected package on explicit factors; say where it would become preferable.
- **EXCLUDE_INVALID** — rules, legality, color identity, nonexistent Oracle identity, or hard source disqualification (must be independently verified).

`HOLD`, `UNRESOLVED`, `INCONCLUSIVE`, `NO_PROVEN_UPGRADE`, and `KEEP_BASELINE_BY_DEFAULT` are **not final M7 candidate decisions**. They may appear only in prior test evidence and must be converted to reasoned final judgments **without concealing uncertainty**. Do not equate weak model sensitivity with evidence for a KEEP decision. Explain strategic criteria and counterarguments; a professional qualitative conclusion is legitimate when a complete gameplay win-rate engine is not.

Every proposed final deck is a **coherent simultaneous 100-card configuration**, not the union of individually attractive swaps. Reconsider the final curve, color sources, counterplay, role redundancy, combo legality and commander identity after composing all changes. Re-run only the tests invalidated by those particular edits; reuse unaltered evidence.

### E. Heightened opportunity audit for zero/one swap

Before an M7 packet recommending **0 or 1 swaps**, independently re-evaluate:

1. The **five weakest plausible roles/slots** (or every plausible weak slot if fewer), with evidence and at least one alternative improvement considered for each.
2. The highest-upside **off-ranking** synergy and relevant overlooked packages, plus credible mana-base or answer-gap alternatives.
3. At least two coherent **multi-slot challenger packages** if supported by the candidate pool; otherwise document why no two-card package is strategically plausible rather than inventing swaps.
4. How each highest-impact previously tested `HOLD` would perform under an *alternative cut* or realistic play pattern that was omitted from the original test.
5. An explicit strong **adversarial case against unchanged/near-unchanged baseline**, followed by evidence-backed defense or extra changes.

This is heightened **analysis**, not a mandate for a large number of new simulations. A low-swap packet cannot pass without the written audit; the owner can still choose an unchanged list on convincing proof. Do not falsely label same-model adversarial review as independent.

### F. Completion and authority

- **M6:** All materially required, applicable P0 rules cases receive executed, reproducible receipts; other actual M6.6/M6.7/I/J obligations must be met on their own terms. Group/batch inexpensive fixtures when possible. Candidate judgments can be resolved without claiming complete probabilistic certainty; source/legality/final certification gaps may not.
- **M7:** Re-verify current Oracle, legality, project exceptions, physical 100-card quantity, singleton, color identity, coherent chosen swaps and interactions, Power Bracket and three tags. The complete final deck and recommendation go to the owner with the standard exact approval question. No request to choose individual card swaps. Existing locked decks remain unchanged until the owner approves the exact replacement SHA-256.
- **M8:** Verify all 62 owner-approved final lists and exports; no automatic certification from completed paperwork.
- Recover each deck's actual GitHub decision record after chat limits. **Never reset the analysis, rerun all test plans, or conflate unrun tests with passed ones.**

## Machine-enforced review contract

Use `data/grixis/m7/decision_reviews/<deck_id>.json` with `data/grixis/schemas/m7_decisive_optimization.schema.json` and `scripts/grixis_m7_decision_gate.py`. The gate checks candidate decisions, exact swaps, nonempty substantive evidence/tradeoffs, decision-question and stop-rule controls for expensive tests, complete final-list audit status and a special low-swap audit. **Passing structural validation cannot replace a real strategic review, current Oracle lookup or the owner's approval.** A broken/absent packet cannot claim M7 readiness. Preserve separate milestone and governance statuses.
