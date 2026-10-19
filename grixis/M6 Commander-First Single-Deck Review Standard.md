# M6 — Commander-First Single-Deck Deep Review Standard

**Workflow decision:** One deck at a time, each given a full independent analytical treatment by the original author **before moving to the next**. Do not switch back to 5–29-deck authored batches just for cycle throughput. This is a depth/quality normalization of previous source-linked authored reviews, **not** a new accepted M6 milestone.

**Authorities:** `corymstover/grixis-commander-encyclopediaGPT/main/state/current_deck_overrides.json` for the exact 62 approved/locked canonical lists; `refinement/Deck_Refinement_Tracker_2026-10-12.csv` for the canonical 0–61 order; `corymstover/GrokBotMTGCompanion` engineering integration `chatgpt-cycle76-m6-refinement` for analysis, M5 candidates and receipts; project's exception registry for intentional deviations. GitHub state supersedes old copied context. Approved decks may NOT be modified by this process.

## Why this separate standard exists

Cycles 112–131 produced **62/62 original authored source-linked reviews**, but many only examined the first M5-ranked swap. In particular, Cycles 129–130 and 131 vary in depth. The M6.4 authored-coverage gate is already complete in its **narrow** contractual meaning. Do not imply that the original evidence was exhaustive or that it proved no upgrade remains.

Track **new deep-review completions separately**, starting at `0/62`, in `data/grixis/m6/single_deck_depth_tracker.json`. Preserve M6.4's original 62/62 count; M6.5 independent Pass C remains separate and uncompleted. An old approved list, old 62/62 authored record, favorable M5 rank or passing automation is never itself sufficient for deep-review credit.

## Mandatory single-deck lifecycle

Work on **exactly one deck at a time**. Complete all applicable stages below for that deck before beginning another. Do not ask Cory to type "Proceed" after each engineering-only review.

1. **Recover source and authority:** Live approved 100-card list and exact SHA, commander(s) and companion zones, current engineering logical hash, full per-card names/quantity reconciliation and known source raw-hash discrepancies. Note locked approval and never touch it. Check current Oracle, color identity and official Commander legality separately from explicit project exceptions.
2. **Reconstruct the commander's identity:** Accurate ability timing, mana, triggers, zones, legitimate core packages, power bracket/natural ceiling and differences from other Grixis builds. Read the commander-specific blueprint, previous review, candidate inventory and relevant source analyses. Record explicit *identity protection* and *anti-homogenization* criteria.
3. **Whole-deck structural audit:** Evaluate all 99 library cards (98 with two commanders) by meaningful strategic role. Examine lands and colored-source reliability, ramp and curve, card access, interaction, protection, recursion, commander-specific enablers/payoffs, win lines, redundancy, inefficient cards, overlap and role shortfalls. Identify the actual weakest/situation-dependent slots **with evidence**; do not reduce the review to one ranked swap. An accounting spreadsheet/table may aid analysis without adding one prose paragraph per card.
4. **Real candidate research:** Consider all **materially relevant** ranked candidates and credible additional alternatives (Oracle/EDHREC/other supported sources as appropriate); record examined pool/ranking limitations and the rationale for narrowing it. Compare multiple meaningful additions and **alternative cuts** where justified. Do not force an arbitrary number of swaps: a clean "keep 100 unchanged" is valid, but must follow genuine consideration of the substantive improvement opportunities rather than a superficial HOLD.
5. **Verify mechanics and access:** For major proposed interactions, trace current Oracle text, precise trigger/activation timing, copy/cast distinctions, targets, zone movement, payment/restricted mana, color identity and loopholes, relevant Commander legality, source-paid combo lines, protection and opponent interaction. Mark any unavailable current ruling/Oracle test *unverified*. No fabricated measured win rates.
6. **Run decision-relevant comparisons:** Realistic opening-hand/turn sequencing and opponent responses for material candidates, use representative table conditions, compare protected baseline vs proposed alternatives where test infrastructure models relevant effects. Explicitly label unsupported simulator mechanics and unmeasured claims. Conduct adversarial review of the strongest apparent improvement and biggest incumbent-cut downside.
7. **Conclude on this ONE deck:** Make precise `KEEP`, `PROPOSE_SWAP_FOR_CORY_APPROVAL`, or `BLOCKED_PENDING_EVIDENCE` recommendations for each genuinely material issue. List the strongest challenger(s), meaningful alternative cuts, why excluded candidates were weaker, outstanding experiments and the natural-ceiling effect. A proposed swap **never changes the canonical list**. Record each exception accurately.
8. **Verify and checkpoint:** Produce a complete deck-specific deep-review artifact linked to the exact canonical hash and source/Oracle versions, proof of 100-card baseline count/singleton/color identity as applicable, explicit coverage summary and limitations, and evidence for any claimed test. Run the existing pertinent tests and exact-head GitHub CI. Only then advance this deck's tracker entry to `DEEP_REVIEW_COMPLETE`. If evidence is insufficient, mark `BLOCKED`, explain what is missing and do not advance past it as though it were complete.

**Review completion is based on substantive coverage, not document length or filling fields with boilerplate.** No automated checklist validates good strategy alone. A completed deep review is the original author's judgment; the later **qualified independent Pass C** must critically evaluate it and can disagree.

## Deep-review artifact minimum contents

Save one artifact under `data/grixis/m6/deep_reviews/<deck_id>.md` or a companion JSON with references and an accompanying readable narrative. It must contain the exact deck ID and canonical approved hash; commander/companion official-vs-project legitimacy; full card-role audit; protected identity; mana/curve/land-source and interaction/development findings; relevant candidate pool with substantive add/cut alternatives; source-backed Oracle/rules and actual finite/payable combo explanations; a baseline-versus-challenger evaluation with test receipts or a clear no-test reason; strongest counterargument; final per-candidate judgment; blocked uncertainties; and an explicit conclusion that **no canonical modifications were made**.

## Durable queue and stopping condition

`data/grixis/m6/single_deck_depth_tracker.json` is the **only progress authority for this new deep-review pass**. Queue is canonical deck-tracker index 0–61, starting `Abaddon_the_Despoiler`. Re-read it before each step.

- `PENDING`: no complete depth record. `IN_PROGRESS`: current deck, not yet eligible to advance. `BLOCKED`: evidence dependency; never claim finished. `DEEP_REVIEW_COMPLETE`: source-bound evidence meets the whole-deck standard and has passed appropriate CI.
- **At most one `IN_PROGRESS` or `BLOCKED` deck at once.** Never start a later deck while the current one is unfinished or blocked.
- Do not mark a complete deck merely because an earlier M6 authored file exists. Update its evidence path, exact canonical hash and review verification references atomically with a successful completion. A valid `KEEP` is just as valid as `PROPOSE_SWAP_FOR_CORY_APPROVAL`.
- On resuming after a chat/session limit, read the live tracker and start with the **first noncomplete** entry; if a prior reviewed deck later has a new external legality/source mismatch, raise the newly detected issue separately and do not silently revise locked records.
- Once **62/62 `DEEP_REVIEW_COMPLETE`** has been demonstrated, prepare the GrokBot Pass C handoff. Do not pronounce formal Pass C, complete Phase B, I/J, M6 acceptance or a deck approval on your own.

## Owner and reviewer boundaries

Cory approves or rejects actual decklist changes and accepts milestones. This engineering workflow **never** does either. No uniform staples shell. GrokBot's prospective Pass C is independent only if reviewer provenance, material prior exposure and genuinely independent/blinded first-stage analysis support it, followed by recorded comparison and reconciliation. Its opinion is not automatically certified just because it is a different agent. Preserve all designated project exceptions and avoid repeated false legality flags.

## Verified roster-identity discrepancy (do not silently rename)

When the new tracker was built, the exact 62-entry canonical refinement CSV and the 62 locked approval hashes were cross-referenced against the engineering registry. Three approved identical-hash entries differ by historical identifier normalization: `Anhelo__the_Painter` ↔ canonical `Anhelo_the_Painter`; `Ashad__the_Lone_Cyberman` ↔ canonical `Ashad_the_Lone_Cyberman`; `Be_lakor__the_Dark_Master` ↔ canonical `Be_lakor_the_Dark_Master`. Treat these as declared source aliases and confirm the actual commander when reviewed.

**More serious:** canonical `Goben__Gene_Splice_Savant` matches the source-list SHA used by engineering `Norman_Osborn_Green_Goblin`. **An identical 100-card SHA is not evidence that two differently named commanders have identical Oracle identities.** Resolve the Goben-vs-Norman named-commander conflict with actual canonical source and blueprint evidence, and obtain Cory's decision if necessary, before declaring that particular deep review completed. Do not silently delete a roster member, approve a new commander, or change the canonical deck.
