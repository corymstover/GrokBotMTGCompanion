# Owner policy — formal Pass C equivalence and post-Josh-Lee-Kwai testing
**Decision date:** 2026-10-20
**Deciding authority:** project owner Cory (explicit in-chat instruction)
**Scope:** all 62 exact currently APPROVED/LOCKED Grixis Commander Encyclopedia decks, M6.5 Pass C qualification and downstream Phase B workload.

## Binding owner decision

Owner direction: “We are going to treat the Josh-Lee-Kwai as an independent third model, and a formal Pass C. Im aware and its fine.”

**Governance rule:** This is an intentional, owner-authorized *equivalence exception* to the original M6.5 demand for a technically separate, independent third evaluator. For **project approval and milestone-gating purposes**, a properly completed 62-deck **Josh-Lee-Kwai** staged critique may count as **formal Pass C**, as if a third-model review had been obtained. **No separate actual third-model review must be purchased or recruited** to discharge that owner-waived condition, subject to the evidence and conflict resolution gates below.

**Factual reviewer provenance remains unaltered:** Josh-Lee-Kwai is the review alias for **ChatGPT / OpenAI GPT-6** (same model family involved in the original authored reviews and reconciliation). The evaluator is **not actually a different model** and is **not technically or historically independent**. Earlier authorship/exposure may affect judgment. This record does not claim otherwise, and does not label the work genuinely blind, anonymous or externally independent. Operational acceptance **is not** a factual claim of model independence. Describe the result as **“FORMAL PASS C — OWNER-ACCEPTED EQUIVALENT, NOT TECHNICALLY INDEPENDENT”**. Retain machine-readable actual evaluator and waived independence criteria.

**Approved classification to use for qualifying reviewed decks:** `FORMAL_PASS_C_OWNER_EQUIVALENT`, accompanied by `reviewer_alias="Josh-Lee-Kwai"`, `actual_evaluator="ChatGPT/OpenAI GPT-6"`, `technically_independent=false`, `independence_requirement="OWNER_WAIVED_FOR_FORMAL_PASS_C"`, `review_stage="FINAL"`, and an immutable evidence/seal reference. An earlier `OWNER_AUTHORIZED_PROCEDURAL_SUBSTITUTE` is the reviewer provenance category, not a restriction on the owner's newly authorized acceptance route.

### Formal Pass C counting rules

1. **0 at this decision point.** Authorization of an alternative reviewer does **not** complete a review. Only actual stage-A critique, Git SHA-256 seal, stage-B controlled comparison and stage-C final judgment with explicit disagreements/testing limits count. Do not backfill 62 old ChatGPT/GrokBot reviews as new Pass C.
2. Review each deck's exact canonical hash; preserve previous official-vs-project legality exceptions and current locked owner status. Declare prior-exposure risks, conflicts, current Oracle/test limitations and unsupported performance claims.
3. A qualifying `FORMAL_PASS_C_OWNER_EQUIVALENT` record can satisfy the **Pass C qualification component** of M6.5 through **this explicit owner exception**, once the per-deck evidence passes integrity and decision/contradiction checks. M6.5 still needs meaningful disagreement resolution; the label alone is not an automatic M6 certificate.
4. Keep **two distinct counters**: (a) `formal_pass_c_owner_equivalent_completed` starts 0 and may reach 62; (b) `genuinely_independent_third_model_reviews` stays 0 unless independently sourced evidence actually arrives. Any old `formal_independent_pass_c_allowed=false` factual/technical provenance flag remains unchanged; use the approved equivalence path rather than falsifying it.
5. Do not silently change `data/grixis/milestone_m6_m7_subtracker.json`, M6 I/J evidence, formal M6 certification counts, canonical owner approval/lock status or prior sealed reviews. If milestone-level criteria or validators assume technical independence as a hard Boolean, adapt **only the acceptance logic through a separate auditable owner-waiver provision** after the actual evidence exists; do not spoof a third model or bypass other gates.
6. Final M6/M7 milestone acceptance and **every specific card swap** remain Cory's decisions. A review, passing CI or owner waiver does not authorize any decklist mutation.

## Post-JLK testing policy — owner directive

Owner direction: “After Josh-Lee-Kwai, concentrate testing on genuine disputed improvements, mechanically uncertain combos, and consequential weaknesses. Clean agreements should reuse the extensive evidence we've already produced wherever the certification criteria permit.”

After all 62 staged JLK final judgments are captured, use a **risk-based Phase B queue**:

**Priority 1 — material proposed additions/cuts and unresolved reviewer disputes.** Include the six prior PROPOSE_UPGRADE M6 reconciliation cases, four existing author-swap vs GrokBot KEEP disagreements (Lord Xander, Missy, Nicol Bolas the Ravager, Obeka Brute Chronologist), other NEEDS TESTING issues, and any *new* credible JLK proposals. Test actual named baseline/add/cut states with commander-specific functionality, alternative cuts, opponent responses, realistic mana/turn windows and counterarguments. Proposals are research until owner approval.

**Priority 2 — mechanically uncertain combos / factual legality or Oracle conflicts.** Verify exact current Oracle, cast-vs-copy, zone/control change, timing, costs/restrictions, trigger stacking, legitimate counterplay and recorded exceptions. An identified card/rules error may require correction without replacing any card.

**Priority 3 — consequential strategic weaknesses.** Test strong, plausible mana/protection/curve/answer shortfalls or commander failure states when the question could change a recommendation or safety/legality judgment. Escalate only where the expected information value is material.

**Clean KEEP/KEEP cases:** reuse previously sealed full ChatGPT commander-first reviews, GrokBot advisories, approved whole-list gates and source receipts, existing tests and JLK neutral/controlled evidence. Avoid another blanket review or automated candidate sweep. An agreement itself proves **only documentary agreement**; it does not become empirical multi-opponent data or a valid local-zero-improvement certificate merely by consensus. Where an I/J schema or M6 acceptance gate explicitly requires a specific complete test, supply it or record the remaining unmet requirement; **do not invent that it ran, waive other material gates, or claim 62 certified automatically.**

**Testing completion stop condition:** All genuine disputes and high-impact testable mechanics either have decision-grade evidence with applicable effect coverage or an explicitly disclosed owner-accepted unresolved limitation. Produce measured/derivable claims only from real test receipts. Move on to I local tested-pool zero-improvement (not global optimality), J reproducibility evidence, M6 owner acceptance, M7 owner packet decisions, and M8 source-exact final export in that order.

## Provenance, audit and exceptions

Project-approved exceptions (Lutri as designated companion; Trade Secrets and Yawgmoth's Bargain in designated Bjorna/Cecily; project-planned pre-release commanders) remain exception-labeled, **not officially legal merely because owner permits them**. All 62 canonical approved decks remain locked, no swap applied, formal M6 certification remains 0/62 at the moment this policy is recorded.

This signed-in-conversation **owner exception supersedes only the independence *qualification* requirement**, not the need for critical review, rules validation, evidence, testing, judgment or owner signoff. Keep attribution truthful even though owner elects to treat the formal substitute as sufficient.