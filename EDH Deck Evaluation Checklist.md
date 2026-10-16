---
title: "EDH Deck Evaluation Checklist"
category: edh
tags: [checklist, evaluation, brackets, methodology]
issues: [62, 81, 96]
generated_by: hand-written
sources: [grixis-repo, cr, scryfall, spellbook]
related: ["EDH Deck Template.md", "EDH Standards.md", "grixis/Grixis Corrections.md", "EDH Lore-Themed Deckbuilding.md", "EDH Mulligans.md", "grixis/Grixis Packages.md"]
schema: 2
---

# EDH Deck Evaluation Checklist

> **Bot cycle 16 ([#62](https://github.com/corymstover/GrokBotMTGCompanion/issues/62)).** A gate-by-gate checklist for judging **any** Commander list, whether a skeleton, an imported list or your own deck, in any color identity. Gate order and the epistemic gates come from the user's Grixis project, [grixis-commander-encyclopediaGPT](https://github.com/corymstover/grixis-commander-encyclopediaGPT) (`architecture/DECK_QUALITY_GATES_V3.md`, `refinement/Grixis_Refinement_Protocol_v1.md` §8–12, `architecture/OPTIMIZATION_STOPPING_RULES.md`), and are marked **(from the Grixis repo)**. The machine checks and the bracket and Game Changer gate are **repo additions**. The Grixis import showed that the source never tracked Game Changers ([Grixis Corrections](grixis/Grixis%20Corrections.md)). Build with the [EDH Deck Template](EDH%20Deck%20Template.md). Rules basis: [EDH Standards](EDH%20Standards.md).

## Contents
- [Gate A — hard correctness (machine-checked)](#gate-a--hard-correctness-machine-checked)
- [Gate B — bracket inputs](#gate-b--bracket-inputs)
- [Gate C — rules lines](#gate-c--rules-lines)
- [Gate D — strategy (guidance)](#gate-d--strategy-guidance)
- [Gate E — evidence labels and stopping](#gate-e--evidence-labels-and-stopping)
- [Gate F — approval-ready candidate and lock](#gate-f--approval-ready-candidate-and-lock)
- [Gate L — lore-themed (story-first)](#gate-l--lore-themed-story-first)
- [Official legality vs house exceptions](#official-legality-vs-house-exceptions)
- [Running the checks](#running-the-checks)

## Gate A — hard correctness (machine-checked)
A failure here is a **veto**. No synergy argument offsets it. **(Repo addition, implementing Grixis Protocol §8 Tier 1.)**
- [ ] Every line resolves to a real card name (Scryfall). Unreleased or custom cards fail.
- [ ] Commander eligibility (CR 903.3) and a valid pairing for two commanders (Partner, Friends forever, Choose a Background, Doctor's companion).
- [ ] Exactly **100** cards including commanders (CR 903.5a). A companion is outside the 100 and must itself be allowed as a companion.
- [ ] Singleton (CR 903.5b), except basics and cards whose Oracle text allows more copies (e.g. "A deck can have up to nine cards named Nazgûl").
- [ ] Every card's color identity is within the commander's (CR 903.5c).
- [ ] Commander-legal per Scryfall, so no banned or `not_legal` cards. Re-check after each B&R announcement.

## Gate B — bracket inputs
**(Repo addition. See [Power bracket assessment](EDH%20Standards.md#power-bracket-assessment).)**
- [ ] Count Game Changers. 0 → floor 2 or 1; 1–3 → floor 3; 4 or more → floor 4.
- [ ] Flag extra-turn cards and mass land denial (MLD → floor 4).
- [ ] Commander Spellbook combos. A two-card infinite raises the floor to at least 3. Whether a combo is "early-game" (Bracket 3 vs 4) is **opinion**.
- [ ] The stated target bracket must be ≥ the computed floor. Treat a gap as an error in the stated target.

## Gate C — rules lines
**(From the Grixis repo, Protocol §8 Tier 1: "Rules/interaction check for every combo, loop, copied ability, replacement effect, timing claim … actually relied upon.")**
- [ ] Quote the Oracle text from the card entry for every line the plan depends on, and cite CR rules or rulings for any timing, trigger, replacement or copy claim.
- [ ] Check trigger-multiplier arithmetic. Additional-trigger effects add up; they do not multiply. Check whether a multiplier applies to *this* trigger at all (example: [Grixis rules insights](grixis/Grixis%20Packages.md#grixis-rules-insights-from-the-source)).
- [ ] Look for replacement effects that break another card's condition, such as "exactly 1 damage".

## Gate D — strategy (guidance)
**(From the Grixis repo, Deck Quality Gates v3.)** Each item records a judgment, so label the result **guidance**.
- [ ] **Blueprint first.** A written commander-first blueprint exists ([template §2](EDH%20Deck%20Template.md#2-commander-first-blueprint)).
- [ ] **Whole-list audit.** All 99 slots have a role and a retention label. "Historically approved" is not evidence ([template §3](EDH%20Deck%20Template.md#3-role-and-package-map-whole-list-audit)).
- [ ] **Candidate exhaustion.** Every high-impact candidate is ACCEPT/REJECT/HOLD with a reason, and no high-impact HOLD remains ([template §4](EDH%20Deck%20Template.md#4-swap-ledger)).
- [ ] **Structure.** Lands vs curve, ramp, draw/selection, interaction, protection, engine and payoff density. Community ratios (~36 lands, ~10 ramp, ~10 draw, ~8–10 interaction) are convention, not rules.
- [ ] **Red team.** Challenge sacred cows; generic staples crowding out identity cards; tutor density; redundancy; win-more slots; low-frequency synergies; combo slot cost; resilience; metagame assumptions.
- [ ] **Commander necessity.** Explain what the commander contributes and what the deck loses without it. "Essentially unchanged" fails.
- [ ] **Homogenization check.** Note attractive generic packages you rejected (e.g. a commander-independent combo shell) and why.

## Gate E — evidence labels and stopping
**(From the Grixis repo, Deck Quality Gates v3 and Protocol §9–10.)**
- Label each material conclusion **VERIFIED**, **HIGH_CONFIDENCE**, **PROVISIONAL**, **TEST_REQUIRED** or **BLOCKED**. TEST_REQUIRED and BLOCKED prevent finalization.
- Testing must state its hypothesis before looking at results. Use exact hypergeometric odds for draw-probability questions ([EDH Mulligans](EDH%20Mulligans.md)) and seeded simulation for anything more complex. More simulations are not automatically better.
- **Stop rule.** A deck is final as of its snapshot date when every hard gate passes, every high-impact candidate is closed, and a complete pass finds **zero new material improvements**. This is a stopping rule, not a proof of optimality.
- **Reopen only on a trigger:** an Oracle, rules or legality change; a material new card; repeated failure in real games; a discovered error; or an explicit request.

## Gate F — approval-ready candidate and lock
**(Bot cycle 37, from the Grixis repo's 2026-10-15 approval records, e.g. [`Thraximundar_Approval_Ready_Verification_v2_2026-10-15.md`](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/1836b97/refinement/verification/Thraximundar_Approval_Ready_Verification_v2_2026-10-15.md) and [`Nekusar_the_Mindrazer_Whole_List_Audit_2026-10-15.md`](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/1836b97/refinement/verification/Nekusar_the_Mindrazer_Whole_List_Audit_2026-10-15.md).)** This is a process standard (guidance). It does not change Gate A.
- [ ] **Record the audit tally.** The whole-list audit states how many of the 99 non-commander slots were adjudicated and the KEEP/CUT split (the source records e.g. "99/99 … 86 KEEP / 13 CUT"). A partial audit cannot support approval.
- [ ] **Freeze an exact candidate.** The proposed list is saved as its own file and identified by the SHA-256 of that file. Verification runs on that file and marks it approval-ready but not yet approved or locked (the source's status line is `APPROVAL_READY`) until the user approves.
- [ ] **Approve the exact hash.** The approved list must be byte-identical to the verified candidate. Any change after a red-team pass makes a new candidate (`v2`) that is verified again from scratch.
- [ ] **Dated legality checkpoint.** At approval, re-check official Commander legality against a dated source (Scryfall bulk date or B&R date) and write it in the record. Cards from an unreleased set stay *not legal* until Scryfall says otherwise. **Repo addition:** we found one source approval that reported "current official Commander legality PASS" for a card Scryfall still lists as `not_legal` before its release date ([Grixis Corrections](grixis/Grixis%20Corrections.md#source-repo-structural-findings)).
- [ ] **Record the export provenance.** If the list is exported (e.g. an Archidekt import package), keep a manifest of deck id, file, card total and source hash. Check each export against the approved list card for card. The Grixis export's `manifest.csv` matched all 62 lists in Bot cycle 37.

## Official legality vs house exceptions
**(From the Grixis repo's exception registry, `source-package/research/Project_Exceptions_Current_2026-10-12.csv`, adapted.)** A playgroup may allow banned cards by Rule 0, but this repo **never presents such a list as Commander-legal**. Record official legality and house permission in separate fields. Published decks here must pass Gate A. The Grixis import replaced its two house-allowed banned cards and dropped a companion that Commander bans ([corrections](grixis/Grixis%20Corrections.md#corrections-table)).

## Running the checks
```bash
python3 scripts/evaluate_decklist.py my_deck.txt            # Gate A plus Game Changers, extra turns and MLD; exit 1 on any hard failure
python3 scripts/evaluate_decklist.py my_deck.txt --combos   # also query Commander Spellbook and compute the combo-adjusted floor
python3 scripts/evaluate_decklist.py my_deck.txt --json     # machine-readable result
```
The input is one card per line (`1x Name`, optional `(set) number`, optional `[Tag]`; tag commanders with `[Commander]`). The same evaluator runs the Grixis import (`scripts/grixis_eval.py`).

## Gate L — lore-themed (story-first)
**(Repo addition, Bot cycle 21, [#81](https://github.com/corymstover/GrokBotMTGCompanion/issues/81).)** Apply after Gates A–E when the deck is a lore list ([EDH Lore-Themed Deckbuilding](EDH%20Lore-Themed%20Deckbuilding.md)).
- [ ] **Story summary** is present, cites official sources, and matches the linked Conflicts & Arcs / dossier entry. No invented plot.
- [ ] **Lore score ≥ 85% of all non-basic cards (commander + every non-land + every non-basic land; basics excluded)** are story-linked by a counting test: name, flavor text (any paper printing — check lands too), story-set printing, or a note citing an official Wizards story page. Mechanical and type echoes are guidance and **do not count** (Bot cycle 23; enforced by `scripts/build_lore_decks.py --check` in `validate_all`).
- [ ] Every non-basic card has a **Why it belongs** row; playability slots are explicitly labeled **guidance**.
- [ ] **Cross-links** to the arc, character and plane pages exist on the deck page and (ideally) back-links from those lore pages.
- [ ] Secondary / unfetched novels and non-canonical sets are flagged ⚠️ / 🚫.
- [ ] Bracket floor is computed; lore decks should disclose any Game Changer or two-card infinite and prefer Bracket 2–3 (guidance).
