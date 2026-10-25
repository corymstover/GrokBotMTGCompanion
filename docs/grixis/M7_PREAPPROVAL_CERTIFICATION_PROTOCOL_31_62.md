# Grixis Commander Encyclopedia — Decks #31–62: Certification Before Owner Approval

Effective 2026-10-25. Owner-directed standing workflow; applies to every remaining deck #31 through #62. Do not require the owner to restate it in subsequent chats.

## Mandatory order
1. Recover live canonical deck and approval state; preserve every previously locked deck.
2. Perform commander-first, decisive whole-list strategic optimization. Explore all meaningful changes, not an arbitrary minimum or maximum swap count. Research EDHREC high-lift and inclusion cards, relevant ranked candidates, Scryfall Oracle and legality, and meaningful alternatives. Preserve distinctive commander identity.
3. Prepare the final exact 100-card proposed list, singleton and Grixis identity checks, legality and project exception classification, relevant rules/combo tests, power bracket, Archidekt tags, candidate rationale, full evidence and exact raw SHA-256.
4. Commit engineering certification evidence and run the applicable M6/M7 case suites and GitHub CI on the **exact candidate SHA**. Resolve failures and any evidence/provenance discrepancies *before* requesting owner approval. Preserve historical evidence; never invent or waive checks without explicit owner authorization.
5. Only after certification succeeds, present the final proposed swaps, full copyable list, audit results, exact SHA and CI receipt for owner approval. If any gate is unavailable or unpassed, label it explicitly and do not represent the candidate as approval-ready.
6. On explicit approval of the exact SHA, do only the SHA-bound canonical decklist/approval/tracker update, final repository CI/integrity verification and merge. Do not repeat research, candidate generation, broad testing, or historical review unless the approved candidate changes or a genuinely new blocking discrepancy appears.
7. Confirm the canonical `main` record is APPROVED/LOCKED with matching SHA and archive preservation before advancing to the next deck.

## Operational objective
Minimize post-approval latency and redundant Actions runs. Prepare lock metadata and transfer receipts before approval where possible without falsely asserting approval. Do not bypass required integrity gates to save time. Avoid spawning unnecessary workflows; keep correction PRs separate when evidence-only scope policies require it.

## Handoff invariant
Every new conversation must recover and follow this file automatically for Decks #31–62. Owner approval is the final decision, not the beginning of certification. No automatic approvals or locks.
