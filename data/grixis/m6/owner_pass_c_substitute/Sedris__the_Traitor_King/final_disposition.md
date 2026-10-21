# Josh-Lee-Kwai — Sedris, the Traitor King — final formal Pass C disposition

**Classification:** FORMAL_PASS_C_OWNER_EQUIVALENT — owner-authorized Pass C qualification; actual ChatGPT/OpenAI GPT-6 is **not** technically independent.  
**Date:** 2026-10-21 America/Chicago  
**Deck ID / order:** Sedris__the_Traitor_King / index 50, #51 of 62.  
**Exact canonical approved SHA-256:** 65fbfe3eb64551ad6f5723243fcd62a286610c360e24bd700b584252e1da6365  
**Approved TXT:** corymstover/grixis-commander-encyclopediaGPT / main / refinement/decklists/Sedris_the_Traitor_King_Approved_2026-10-15.txt (Git blob fc33a2493255d6033691b1195d1bc1091b420b3b).  
**Canonical state:** APPROVED/LOCKED, 100 cards, 99 distinct names, 31 lands, only two Swamps duplicated, Grixis U/B/R commander, no project exception. **NO canonical mutation.**  
**Stage A source and first commit:** stage_a.md + stage_a.json, commit cb4591485df61eec582b82820b89ae34650a0d1f.  
**Stage A separate seal commit:** 07b6c01238980a78069895483c434359d7340ca2 (seal.json).  
**Stage A SHA256:** md 4f730ea771d246b9739dd6b9e025bb1615fd984a2a6a3f788fd2455c05017c59; json 0e0fb83faf6bbd34261b17f981693d3b3eb1c146d8f3450c8c00707bdaf2c49b.  
**Controlled comparison:** stage_b_reconciliation.md, opened full author/GrokBot/reconciliation only after the seal.

## Decision and natural ceiling

**Final disposition: NEEDS TESTING — KEEP the present approved and locked 100 unchanged.**

Sedris remains a distinctive **Bracket 4 Optimized** six-mana UBR graveyard commander: fills the graveyard, grants every own graveyard creature unearth {2}{B}, exploits hasty ETB and attack value, and uses Convergence, Panharmonicon, Obeka, Sundial, Veil and Deadeye to improve its mana and one-turn exile economy. Preserve this identity; do not turn the deck into an unrelated Breach/Oracle goodstuff list to elevate nominal bracket. The strongest structural risk is 31 lands and repeated UBR / B access under commander removal, combined with hate-dependent graveyard engine activation; no empirical failure or win percentage is claimed.

### Rules actually verified and unresolved scope

- **Unearth is an activated ability from the graveyard, not a cast.** Opponents can exile that card before its activation resolves. The returned object has a one-shot delayed end-step exile **and** a separate leave-to-nonexile replacement; sacrificing it cannot send it back to the graveyard for another ordinary unearth. Verified against Wizards Warhammer 40,000 Commander official release notes.
- **Sundial of the Infinite is correctly retained.** Once own end-step exile triggers are on stack, paying {1}, tapping Sundial and ending the turn exiles all those pending one-shot triggers; the continuous replacement persists. Ending before end step instead postpones them to a later end step. Original GrokBot advisory erroneously generalized the before-end-step case. Official Wizards Sundial notes verify the distinction.
- **Blink to exile-and-return creates a new object** with no prior unearth obligation; Deadeye supports a paid route, while Kitten requires a noncreature spell **cast**, a surviving target and a surviving engine. Exiling a token with Kitten does not return that token.
- **Drake/Navigator repeatable paid land-untap may yield unlimited mana** when appropriate lands can pay each blink and net additional resources, but infinite mana does **not** by itself supply infinite Goblin Bombardment sacrifices. Terror of the Peaks or another actual repeatable payoff is necessary for a kill claim.
- **Convergence of Dominion** reduces a Sedris-granted {2}{B} graveyard-card ability to **{B}** while Sedris is controlled, never removes black.
- Current official legality source check is **bounded**, not a fresh per-card Oct21 Oracle sweep; previous Oct15/16 full 99-card approval/source gates PASS. Gifts Ungiven's 2025 Commander unban is confirmed; Scholar's 2026 ban is in **Historic**, not automatically Commander. Candidate-specific Commander legality must be confirmed before any owner-ready packet.

Relevant first-party sources: https://magic.wizards.com/en/news/feature/warhammer-40000-commander-release-notes-2022-09-19 ; https://magic.wizards.com/en/news/feature/avatar-the-last-airbender-release-notes ; https://magic.wizards.com/en/news/feature/core-set-2021-and-jumpstart-release-notes-2020-06-20 . For the Kitten official CLB URL, the canonical verified URL is https://magic.wizards.com/en/news/feature/commander-legends-battle-baldurs-gate-release-notes-2022-06-01 .

## Prior opinion comparison and exact candidate decisions

| Question | Final judgment |
|---|---|
| GrokBot +Ghostly Flicker / -Sundial | **REJECT exact cut**, supported by independent primary rules. Flicker can rescue two legal targets but cannot replace repeatable multi-creature Sundial end-step preservation as a strict improvement. |
| Original ChatGPT KEEP | **Agree for currently locked baseline**, not evidence of global optimality. Prior author reviewed all 100 and 111 historical candidates but did not assess two newer Stage A hypotheses. |
| **+Displacer Kitten / -Panharmonicon** | **NEEDS TARGETED TESTING**. Legitimate new cast-triggered blink/rescue mechanism, but replaces automatic ETB trigger doubling with vulnerable 2/2 conditional engine. Test before recommending; strongest counterargument is lost reliability from existing ETB toolbox. |
| +Displacer Kitten / -Feldon | **NOT YET RECOMMENDED**. Gives up commander-independent grave-to-ETB token copies; consider only if comparison clearly favors resilience of blink package. |
| +Scholar of the Lost Trove / -Etali, Primal Storm | **LOWER-PRIORITY NEEDS SCREEN**. Three-mana Sedris unearth yields a free graveyard artifact/instant/sorcery cast if legal target exists, but fails empty-target states; Etali's immediate haste attack has its own strong role. |
| Mana-base / commander recast weakness | **TRACK**, source proxies show 31 lands/10 nonland rocks and colored pips but cannot establish cast probabilities under multiplayer removal. No exact land swap proposed. |

**Phase B risk queue:** (P1) effect-aware matched-hand timing comparisons of +Kitten/-Panharmonicon with a creature ETB vs attack target and spot removal counterplay, including whether the requisite noncreature spell is available; (P2) Scholar/Etali current Commander legality + grave-target density/stack payment check; (P3) six-mana UBR access and 2B/1B follow-up under commander tax, graveyard hate and tapped source conditions. Reuse previous 45 paid traces and the 2026-10-15 approved full-list legality evidence where justified. No unmeasured win-rate or 62-deck simulation assertions.

**Owner decision:** No new swap approved or applied. Before any later change, Cory must approve the **exact** addition and cut; the resulting 100 must be independently recounted, re-hashed and verified for singleton, UBR identity, official legality, project exceptions and rules functionality. Existing Sedris approval remains controlling.

## Provenance and certification limits

Reviewer alias Josh-Lee-Kwai, actual evaluator ChatGPT/OpenAI GPT-6, technically_independent=false, independence_requirement=OWNER_WAIVED_FOR_FORMAL_PASS_C. The process includes known earlier author/model exposure; an administrative search exposed prior Sedris KEEP / Ghostly Flicker/Sundial summary snippets before Stage A, explicitly disclosed in the sealed source. The full prior review texts were not read until AFTER the Stage A Git SHA256 seal. This is **FORMAL PASS C — OWNER-ACCEPTED EQUIVALENT, NOT TECHNICALLY INDEPENDENT**.

**Qualification:** On evidence-specific SHA verification and exact-head CI/merge, this deck may count as 1 completed formal owner-equivalent Pass C, with unresolved tests transparently queued. It does **not** constitute an independently executed third model, Phase B completed test, I tested-pool zero-improvement certificate, J complete reproduction, final M6 certification, M7 acceptance or M8 export certificate. Progress ledger is separate and must not advance before evidence PR CI passes and merges.
