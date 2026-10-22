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

### A2. Mandatory EDHREC candidate-discovery expansion (owner directive, 2026-10-22)

Before declaring the M7 opportunity map exhausted, inspect the commander's **live EDHREC page**, the relevant commander-specific theme/tag views, and available **Top Cards / inclusion** and **High Lift** listings (historical snapshots may still label the latter **High Synergy**). Review high-lift as well as high-inclusion candidates: high inclusion exposes consensus staples, while high lift exposes underplayed, more commander-associated or niche cards that candidate ranking and the engineering database may have missed. Also examine on-theme newer/low-sample cards and viable interacting packages outside those lists. This is **mandatory active discovery for all 62 future M7 decks, even when existing M5/M6 candidate inventories are extensive**.

- Record source **URL, retrieval date, applied EDHREC filters, displayed metric name**, inclusion rate/count and lift (or historical synergy) **when actually observed**; do not silently equate lift with the deprecated synergy percentage. Metric definitions and availability can change; never invent values. EDHREC published its commander-page lift replacement on 2026-10-01.
- Compare source-derived candidates with the **exact canonical 100**, previously researched challenger pool, and fully specified live research packages. Identify previously absent cards by name and genuinely suitable commander-specific role; propose credible exact incumbents and alternative cuts. Evaluate evasion, tempo, costs, resilience and combo interaction with **current Scryfall Oracle/legality**, not crowd frequency.
- Give each material EDHREC-discovered candidate a **SELECT_ADD, REJECT, RETAIN_ALTERNATIVE or EXCLUDE_INVALID** supported disposition; not every popular/high-lift card needs inclusion. If an EDHREC item is present or already reviewed, link the existing finding; no duplicate analysis is required.
- **Do not stop at a Top 10, an arbitrary inclusion/lift threshold, the first five improvements, or a fixed candidate count.** Explore relevant further cards and packages until remaining credible alternatives no longer improve the fully compared 100-card configuration. Explicitly document inaccessible/stale EDHREC data, available alternatives, and remaining discovery uncertainty if a source cannot be inspected. A captured page or list by itself is research evidence, **not proof of superior play** or an approval-ready deck.
- This addition supplements the post-floor *unbounded optimization* and no-padding directives. Preserve official source and authority distinctions: EDHREC is discovery data, Scryfall/official rules control rules and legality, and only Cory controls canonical approval.

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

## Canonical source discipline across the full roster

The engineering mirror contains **seven** individual `exports/grixis-archidekt/source-baseline/*.txt` files, not 62. For remaining decks, use each `data/grixis/registry.json` `canonical_project_list.path` and only that Markdown file's `Decklist (Archidekt import)` source block. **Do not use the top-level `exports/grixis-archidekt/<slug>.txt` as canonical**: those exports may contain Bot-refined or derived officially legal projections (notably substitutions in the approved Bjorna/Cecily exception deck). For every final M7 packet, also independently recheck the live source repository's exact approved hash and current legality; an archived mirror alone does not establish latest canonical authority.

Exactly 100 cards include the commander(s); the authorized Bjorna/Cecily `Lutri, the Spellchaser` companion is **outside** that 100 and officially banned as a companion, while `Trade Secrets` and `Yawgmoth's Bargain` are preserved as project exceptions. Named card-text deckbuilding exceptions (e.g. up to nine `Nazgûl`, seven `Seven Dwarves`) differ from unrestricted permission to duplicate singleton nonbasic cards. Verify these Oracle exceptions rather than falsely failing compliant lists.

## Machine-enforced review contract

Use `data/grixis/m7/decision_reviews/<deck_id>.json` with `data/grixis/schemas/m7_decisive_optimization.schema.json` and `scripts/grixis_m7_decision_gate.py`. The gate checks candidate decisions, exact swaps, nonempty substantive evidence/tradeoffs, decision-question and stop-rule controls for expensive tests, complete final-list audit status and a special low-swap audit. **Passing structural validation cannot replace a real strategic review, current Oracle lookup or the owner's approval.** A broken/absent packet cannot claim M7 readiness. Preserve separate milestone and governance statuses.

## HARD owner directive — prevent shallow few-swap M7 presentations (2026-10-22)

**Cory explicitly rejected the adequacy of Abaddon's two-swap final presentation after the project's extensive research/testing. This supersedes the earlier permissive zero/one-swap presentation policy for all 62 M7 decks.**

1. **Default owner-presentation floor: five genuinely strategic card swaps.** A proposed M7 physical list with **0–4** actual replacements is **RESEARCH_ONLY_NOT_OWNER_PRESENTABLE**. Do **not** tell Cory "This deck is complete" or ask for final approval, regardless of previously passed M6 mechanical tests, structural CI, purported local optimum, prior deep review, or the author’s confidence. An exceptional lower-swap presentation would require Cory to explicitly change this policy *before* a new candidate is called ready. Never assume authorization.
2. **Absolutely no artificial quota-padding.** Do not add weak or generic Grixis cards, manipulate mana lands cosmetically, or remove protected commander identity just to reach five. If only fewer than five true improvements withstand analysis, preserve an honest **research-only hold** and surface the exact tension to Cory as a governance question; never present a falsely optimized final 100.
3. **A ≥5-swap count is necessary, not sufficient.** A packet remains research-only until it compares **at least ten distinct material candidate judgments**, challenges **at least eight distinct genuinely plausible incumbent roles/slots**, documents **two or more complete multi-card 100-card alternative packages**, examines off-ranking and commander-specific missed synergies, and provides substantive rules/legality, source and applicable M6 findings with all hard blockers resolved. If fewer credible opportunities actually exist, the packet cannot be presented as owner-ready under this rule.
4. The machine gate `scripts/grixis_m7_decision_gate.py` and `data/grixis/schemas/m7_decisive_optimization.schema.json` must **fail closed** if a low-swap candidate claims owner-ready status or a historically withdrawn candidate is laundered back into final-ready status. The old Abaddon two-swap packet is retained as historically source-bound research, explicitly marked **withdrawn**—its 100-card research file and selected-pool M6 I/J hashes are historical, not a new final approval.
5. These criteria apply to **all 62 commanders** at M7. They do not rewrite canonical approved decks, historical M6 records, the GPT-6 non-independent owner-equivalent Pass C waiver, or owner-level approval authority. No new M7 deck approval is inferred by passing the new gate. Future changes to this owner directive require Cory's explicit authorization.


## OWNER CLARIFICATION — unbounded optimization, not five-swap anchoring (2026-10-22)

This prospective directive follows Cory's explicit concern that Admiral's previously owner-ready list and **all three** fully specified alternatives each made exactly five swaps. **Five is a minimum for presentation, not a recommendation target, preferred number, stopping rule, experiment budget, or maximum.** Do not infer "fully optimized" from five changes, ten judgments, eight challenges, two packages, successful CI or an exact candidate hash. These quantities are only eligibility checks.

- Complete a fresh, unconstrained full-99 opportunity pass after reaching the five-swap floor. Continue until all **credible** independent additional upgrades and interacting packages receive authored dispositions. Explicitly test the strongest argument that another 1–5+ substitutions would improve the already-selected configuration, including different cuts and overlooked commander-specific engines. Do not assume a deck should change only five cards.
- Challenge at least two additional named incumbent slots **outside the selected cuts**, against named alternative cards and their opportunity costs. Evaluate a **complete 100-card configuration with more substitutions** when one is credible and compare it with the selected list, including protection, mana/color reliability, curve, resilience and commander identity. The less-changed configuration may legitimately win; preserve the rejected larger package and explain why. If no credible larger package exists, document the factual reasons rather than inventing padding.
- Record the finite strategic *exhaustion criterion* and concrete best surviving counterargument as an `open_ended_optimization_audit`. The criterion must refer to relative card/package quality, not having reached a count. Rejected add/cut pairs and higher-count alternatives remain evidence, not obligatory changes. An owner-ready packet missing this post-floor proof is **RESEARCH_ONLY** regardless of its schema-valid five-swaps under the old gate.
- Apply this policy to every not-yet-owner-approved M7 replacement. Preserve the exact previously owner-approved Abaddon historical packet, its source-bound receipt and the earlier machine contract. Admiral's five-swap D packet is withdrawn, NOT approved; its already executed M6 evidence is retained, and any next candidate must be a newly verified numbered revision. No canonical deck or approval/lock is modified by this change.
