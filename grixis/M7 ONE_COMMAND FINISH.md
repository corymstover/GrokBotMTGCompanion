# Grixis Encyclopedia — ONE_COMMAND_FINISH_V1

**Owner directive 2026-10-24:** The ordinary user instruction is simply **“Finish Deck #N”**, **“Finish the next deck”**, or **“Finish Kefka.”** No repeated “Proceed” messages or re-explanation of repository architecture should be needed. The owner may also click **Actions → M7 One-Command Evidence Intake → Run workflow** to prepare a pinned, read-only intake artifact. The button is evidence preparation, **not an autonomous optimizer or owner approval**.

## Mandatory inherited process — reuse, never replace

For each deck, read the live canonical approval registry/tracker, the existing M6 single-deck review standard and depth tracker, full M6/M6.x/Phase B and Pass C record, commander-effect blueprint (C/K/E/W/F P0/P1), saved Grok M7 research/alternatives/tests and I/J receipts, the decisive optimization/test-economy contract, EDHREC commander-specific Top Cards and High Lift, and current Scryfall/Oracle/Commander-legality evidence. The original comprehensive engineering evidence is on `chatgpt-cycle76-m6-refinement`; do not presume it is in engineering `main`. Historical test passing cannot be transferred without *explicit scope correspondence* to the exact current final 100.

`python scripts/grixis_m7_one_command.py --deck next --output m7_intake.json` validates the live baseline 100, hashes raw canonical bytes and inventories pinned source evidence. Its result is always `RESEARCH_INTAKE_ONLY_NOT_OWNER_READY`. A success is **not** test completion, strategy certification, legality certification, or permission to alter canonical.

## One-command finalization sequence (normally without interruptions)

1. **Recover** pinned live canonical first and identify next unfinished *new* M7, honoring specific owner queue changes. Lock all other decks untouched. Show concise status only when useful, not a standalone stopping point.
2. **Reuse** existing in-repo research and original case-level M6/I/J evidence. Build one whole-100 baseline evaluation. Challenge Grok suggestions, lower-quality incumbent cards, EDHREC discoveries and meaningful off-ranking alternatives, strategic/tempo/mana opportunity costs, real Oracle/rules, land and ramp. New research is targeted and finite; no paid Grok/Colab/full pipeline. Investigate credible sixth/seventh/etc. swaps — **five is the ordinary minimum, not the target or cap; never pad**. Apply a deck-specific exception only if owner explicitly grants it.
3. **Decide** a coherent exact 100-card candidate; establish a meaningful stop reason. If additional research is unlikely to alter decision, stop searching and verify. No endless successive partial candidates or circular debate.
4. **Verify** source-pinned whole 100: physical count/singleton, first-line commander, companion exceptions, Commander color identity and legal cards, Oracle identities, relevant trigger/stack/combo interactions, color/mana sources and curve, role balance, M6 commander-effect P0 cases actually executed/passed, P1 passed or documented deferred, I/J outcome transferred to the **exact final source** via case-by-case mapping (including changed-card effects), and repository M7 decision/owner-ready gate. Do not count merely designed, prior-list, or speculative cases as executed. Exact-head engineering CI before owner proposal; state any remaining nonblocking verification limitations.
5. **Present one owner packet** below for an affirmative one-word **“Approve.”** Explicit consent attaches to that named exact raw SHA. Any revised candidate needs a *different* version/SHA and fresh approval. Canonical stays locked historical until then.
6. **After approval only:** independently recompute approved bytes, narrowly scoped canonical approval PR/receipt/tracker/registry, exact-head CI including M7 provenance gate and regression of prior locks, guarded merge and postmerge `main` hash/registry verification. Then automatically prepare the next deck when instructed to continue the sequence; never approve the next deck by inference.

## Owner packet: stable format, all required fields

### Deck #N — [Commander] M7 RevN — approval-ready

- **Decision:** recommended commander-first game plan and natural power bracket; why this is the best defensible 100 now.
- **Changes:** numbered `+Exact inclusion / −Exact removal` for *every* swap, each with reason and material downside. Include all quality-positive changes, not just five.
- **Rejected challenges:** a compact summary of the strongest tempting alternatives and why they lose whole-deck value. Highlight any overridden prior owner decision.
- **Verification:** 100; singleton; identity; Scryfall Oracle; official Commander legality and named project exceptions; land/ramp/fixing/castability; relevant mechanics/rules; actually executed P0 and P1 outcomes; exact-list I/J correspondence and M7 gate; GitHub PR and exact-head CI. Distinguish genuine passes from deferred or not evaluated, and never invent win rates.
- **Complete raw decklist:** `1x Commander Name [Commander]` first; one quantity-prefixed card per line; exactly 100 in commander deck; no set codes, group headings or role tags *inside the decklist*.
- **Power Bracket:** exact determination and rationale.
- **Three Archidekt tags**.
- **Raw SHA-256:** exact full digest computed from the immutable presented UTF-8 bytes, linked to the engineering candidate PR. Do not create a competing text rendering that silently changes line endings or hash.
- **Action:** “Cory, approve this exact M7 RevN 100-card SHA, or request specific changes.”

If honest upgrades fail the ordinary five-swap minimum or a material P0/Oracle/IJ issue cannot be resolved from bounded existing evidence, do **not** falsely present owner-ready. Record a precise `RESEARCH_ONLY` blocker plus strongest candidate; ask **one concrete decision** only if indispensable. This exception does **not** waive mandatory legality, count, source and mechanics verification.

## Permanence and boundaries

- Each new chat must read this contract and canonical `AGENTS.md` *before* writing owner-ready M7 packets; a handoff message cannot supersede live GitHub.
- Existing 24 new M7 locks remain immutable. The 20 pending retrospective evidence scope reconciliations are tracked in engineering issue #701; never rewrite prior receipts, weaken canonical gates, or reopen locks solely to reconcile evidence.
- The GitHub Action makes a reproducible **source intake** available in one click. It cannot perform independent strategic judgment, comprehensive rules testing, or authorization on Cory's behalf.
