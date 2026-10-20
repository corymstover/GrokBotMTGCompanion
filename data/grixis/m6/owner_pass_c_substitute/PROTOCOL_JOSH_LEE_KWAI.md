# Josh-Lee-Kwai — owner-authorized Pass C substitute protocol (NOT formally independent)

**Owner directive:** Cory Stover, 2026-10-20: after current 62-deck GrokBot/ChatGPT reconciliation, use a separate review role/alias **Josh-Lee-Kwai** to get as close to impartial third-pass scrutiny as possible with available ChatGPT resources. This accepts a **procedural substitute**, not a claim that the reviewer has a different model, author, memories or organization. **NO official Pass C certification by alias alone.** The formal-qualified-independent gate remains 0/62 until explicitly changed through a documented owner/governance decision that does not mislabel provenance.

**Purpose:** maximize usable disconfirming evidence while avoiding false equivalence: in a separate post-reconciliation second scrutiny, compare each exact locked canonical 100 to plausible alternatives and detect conflicts missed by both earlier models. Avoid restarting any completed M6 deep authored review, running the M5/Colab pipeline, or generating deck modifications. Reserve owner approval for actual candidate add/cut. Preserve existing 62/62 APPROVED/LOCKED state.

## 1. Reviewer provenance (mandatory, never anonymize)

- **Reviewer display alias:** Josh-Lee-Kwai.
- **Actual evaluator:** ChatGPT / OpenAI GPT-6, same model family/assistant that originally authored M6 deep reviews and executed the two-model reconciliation; subject to memory, prior context and other shared-model biases.
- **Conflict declaration:** Has *already* seen authored and advisory results for some decks. No guarantee a new chat/prompt can erase learned context or prevent latent recall. The alias does not change this.
- **Classification:** `OWNER_AUTHORIZED_PROCEDURAL_SUBSTITUTE`; do not call `QUALIFIED_INDEPENDENT_PASS_C` or `BLIND_INDEPENDENT_REVIEW`. A Stage-A *input* can be blinded to documents; a previously exposed model is not truly blind.
- **Owner acceptance:** Cory authorized undertaking this best-effort substitute; separate acceptance of eventual *completed results* is not automatic.
- **No new purchased GrokBot credit required.** Use GitHub, project compact sources and current public Scryfall/official rules as needed.

## 2. Strict deck-by-deck stage workflow

**Stage 0 — settle reconciliation first.** Complete 62 GrokBot/ChatGPT reconciliations or explicitly document per-deck open blockers. Read canonical live `state/current_deck_overrides.json` and tracker before starting any Josh-Lee-Kwai pass. **Do not begin a JLK Stage A for a deck while its reconciliation evidence is still only pending unresolved dispute**, unless labeled provisional and bounded. Canonical changes never automatic.

**Stage A — neutral input only.** A *fresh conversation* is preferred but cannot guarantee independence. Read only:
1. current owner-approved exact canonical 100-card TXT, approved SHA-256, deck ID, color identity and explicit project exceptions;
2. authoritative current Oracle/rulings/Commander official legality, current WotC rules, factual 100-name deck roles (NOT candidate verdicts);
3. raw unranked candidate card names only if useful; no grades, optimizer scores, proposed cuts, author decision captions, M6 deep review file paths or GrokBot assessments.
4. transparent provenance: neutral packet source blobs, observation date, affected exceptions, actual constraints.

**Explicitly excluded until Stage A is sealed:** `data/grixis/m6/deep_reviews/**`, `grokbot_pass_c_advisory/**`, `two_model_reconciliation/**`, historic author decisions/verdicts, ranked "best" cut labels and reports disclosing those judgments. File paths of excluded documents may appear in authority metadata; don't open their content. Existing prior-session exposure must still be disclosed, not washed away.

**Stage A — adversarial first verdict.** For one deck, in a fresh evidence file `data/grixis/m6/owner_pass_c_substitute/<deck_id>/stage_a.md`, determine commander-specific game plan, identity preservation, weak actual slots, strongest CHALLENGER hypothesis and competing removals, mana/curve, paid zone/timing/priority and rules trace, anti-synergy, opponent answers, table scenarios, official legality vs project exception, and a provisional `KEEP/PROPOSE UPGRADE/NEEDS TESTING/RULES LEGALITY BLOCKER`. Any known past exposure gets a dedicated disclosure; no invented simulation or sourced precision. Include a strong *counterargument to your own favorite*. Do not accept a "no improvements" verdict from ranked candidate scores.

**Hard seal before any author comparison:** put `stage_a.md` and machine-readable `stage_a.json` in a Git commit on a dedicated branch; record `SHA256(stage_a.md)`, `SHA256(stage_a.json)`, exact input packet canonical SHA256, Git commit SHA, reviewer alias and actual model, dates, and contamination disclosure in `seal.json`; commit `seal.json` in a separate, immutable follow-on commit before unblinding. Never rewrite earlier sealed contents. If a rerun is necessary, issue a NEW version/commit with prior version immutable, not overwrite. Git commit hashes are immutable fingerprints but do not prove independent human/model identity or absence of earlier context.

**Stage B — controlled unblinding.** Only now open: existing ChatGPT deep review, GrokBot Stage-A advisory and summary, **finished two-model reconciliation** and candidate tests. Save `stage_b_reconciliation.md` with exact citations to each; classify each agreement/disagreement, correct own Stage A mistakes, identify unexplained divergence; run narrowly selected effect-aware tests where it genuinely changes an add/cut. Preserve rule-vs-heuristic distinctions, challenge all KEEP claims, and require plausible alternative cuts. Never rewrite or replace sealed Stage-A verdict merely to match author.

**Stage C — evidence-aware conclusion.** `final_disposition.md` includes approved canonical raw hash, source baseline, first-pass commit/seal, verified current card/rules and official-vs-exception scope, multiple opponent response windows, final decision, blocker/tests, recommended EXACT add/cut if warranted, power bracket, owner-approval flag, provenance and any contradictions. Distinguish source-backed fact from strategic judgment and measured performance. Do not treat a correct rules interaction alone as a proven win-rate upgrade.

## 3. Progress ledger kept out of formal Pass C

Use `data/grixis/m6/owner_pass_c_substitute/progress.json` only when first review starts, with `schema_version`, `reviewer_alias`, `actual_model`, `provenance_disclosure`, `review_class`, `canonical_branch`, `decks` entries (index, id, canonical approved hash, stage status, seal commit SHA, final evidence path, owner approval flag), and separate `stage_a_complete`, `stage_b_complete`, `final_complete` counts. All counts start **0** when created. No fake seed completions from the 62 old authored reviews, GrokBot advisory or reconciliation work.

**Never modify** `data/grixis/m6/single_deck_depth_tracker.json`, `data/grixis/milestone_m6_m7_subtracker.json`, `state/current_deck_overrides.json`, any sealed GrokBot/author records, `formal_independent_pass_c_allowed`, `formal_m6_certified_decks` or formal J/I certificates to make a separate count appear qualified.

Canonical approved decks stay locked. All recommended additions/cuts require Cory's explicit card-by-card approval followed by independently recounted new 100, Oracle/color/legality/singleton and actual combo checks and a new SHA/approval transaction *only when authorized*.

## 4. Guardrails and success definition

- **Hard limitations:** same assistant/model lineage and learned prior work, so this process is **not formally independent**. A "fresh" conversation plus neutral packet hides *visible review text*, not the latent memory of having written it. Do not conceal that limitation under an alias or cryptographic seal.
- **What can be legitimately completed:** owner-authorized secondary critique count, 62 evidence-separated per-deck judgments, explicit fixes and approved proposals, adversarial testing/verification where possible, complete transparent provenance, owner acceptance of alternative process.
- **What cannot be asserted merely from this protocol:** formally independent Pass C complete; Phase B complete; zero-improvement I; final reproducibility J; 62/62 M6 certification or any new canonical lock.
- **Acceptance gate:** On completion deliver an exact, checkable ledger of all 62 JLK substitute final dispositions, outstanding tests and material disagreements; Cory may accept the substitute results as fit-for-purpose, while formal unmet independence is documented as waived/alternative—not literally independently passed. Any amended definition requires a separate owner-signed authority exception, not silent tracker replacement.
- **CI:** One deck and one small PR per evidence group, validate source hash/seal/disposition and existing source guards on the exact PR head. Do not merge unvalidated PRs or automatically adjust milestones.
- **Stop/go:** Post-reconciliation JLK passes should run consecutively without unnecessary manual 'Proceed' requests; stop before any canonical mutation, explicit owner approval, source conflict or failed evidence gate.

**Scope:** light process addition, not a new optimization/ranking pipeline, no Colab rerun, no credit expenditure, no architectural replacement. The technical independence requirement remains explicitly unresolved.

## Exact-head evidence CI provenance
The M6 evidence-only integrity workflow was established by engineering PR #354, merge `76c8236b8e35657824df65d258e0a5f7a5c51aa6`. It verifies branch-changed path scope, SHA/source and independence disclosures, approved 62/source-ledger integrity and unmodified formal certification fields. **This reconciliation/review protocol is NOT formally independent Pass C, and a CI PASS is NOT an MTG strategy or current Oracle-complete certification.** Canonical deck approvals remain untouched.

## Exact-head evidence CI provenance
The M6 evidence-only integrity workflow was established by engineering PR #354, merge `76c8236b8e35657824df65d258e0a5f7a5c51aa6`. It checks changed-file scope, approved-source SHA receipts, disclosure of reviewer overlap, and preserved formal certification state. **This reconciliation/review protocol is NOT formally independent Pass C; a CI PASS is NOT a strategy or full Oracle certification.** Canonical deck approvals remain untouched.
