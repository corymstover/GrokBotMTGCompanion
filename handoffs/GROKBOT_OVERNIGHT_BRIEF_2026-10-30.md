# MTG Multiverse Companion — overnight autonomous continuation (owner mandate t93u, 2026-10-30 01:13 CDT; restored 02:25 CDT after box replacement)

Owner: Cory Stover (GitHub corymstover). Repo: corymstover/GrokBotMTGCompanion (main). Local clone: /workspace/GrokBotMTGCompanion (fetch first; fresh worktrees under /workspace/mv-<slug>).
gh is logged in as corymstover. Push with: git -c credential.helper= -c credential.helper='!/usr/local/bin/gh auth git-credential' push. NEVER force-push. NEVER print tokens.

## Read first (every batch)
1. MTG_MULTIVERSE_MASTER_WORKFLOW.md on main — authoritative roadmap (Phases 1, 1B, 2–8, checklists, verification rules, Final Release Acceptance Checklist).
2. AGENTS.md, LORE_DECKBUILDING_READY.md, LORE_QUERY_QUICKSTART.md.
3. handoffs/GROKBOT_OVERNIGHT_2026-10-30.md (the in-repo record) and /workspace/out/multiverse/PROGRESS.md.
4. Latest commits on main, open PRs. ChatGPT also develops (chatgpt-* branches): never touch them; check overlap; re-check main before merging.

## Mission
Advance the whole Master Workflow across all 8 phases tonight, choosing the highest-value, highest-leverage achievable work. Real research, code, tests and GitHub publication — not plans. If blocked, document it and move on.

## Publication
- Branch per task grokbot-<topic>-20261030; push often and verify on remote.
- PR per cohesive milestone. You MAY merge (normal merge, --match-head-commit, no force, no admin bypass) safe, verified, non-approval-dependent research/engineering PRs when ALL checks on the exact head are green and there's no conflict with ChatGPT's work.
- After verified milestones, update MTG_MULTIVERSE_MASTER_WORKFLOW.md (bump version, checklists, counts, evidence).
- Evidence: Wizards official story/rules primary; Scryfall for card data. NEVER fabricate lore, citations, tests, CI or progress. Keep distinct: research vs tests passing vs merged vs owner approved vs certified. New lore decks are UNAPPROVED proposals; never check owner-approval boxes.

## Protected — never modify
- ALL Grixis work is FINISHED (owner t95u): don't touch Grixis decks, data/grixis/, grixis/, Grixis PRs/branches or the ledger. corymstover/grixis-commander-encyclopediaGPT is read-only.
- state/current_deck_overrides.json, data/lore_decks/approvals/, any approved/locked list, hash or documented exception.
- Historical Scryfall snapshot locks (dev_snapshot_lock.json, /workspace/grixis_cache); use separate modern data for the Companion.
- No spending, no secrets/cookies/tokens/personal files in commits.

## Efficiency (owner t96u/t97u)
Maximize progress. Prefer bulk, scripted, data-driven pipelines and throughput-multiplying tooling over one-by-one work. If slow or stalled, find a smart workaround or switch tasks. Fetch free public bulk data (e.g. Scryfall bulk, Commander Spellbook public API/bulk export, official Wizards pages) when a blocker is only a missing cache — but never spend money, and respect sites' normal public access.

## Everything in the repo (owner t98u)
Nothing may live only on the box (it can be wiped, as happened at ~02:15). Keep handoffs/GROKBOT_OVERNIGHT_2026-10-30.md current and pushed at the end of every batch; push partial work before stopping. Also commit a copy of this brief into the repo at handoffs/GROKBOT_OVERNIGHT_BRIEF_2026-10-30.md.

## Batch protocol
Roughly 60–120 minutes of work per batch, multiple milestones end-to-end, then stop and report: phases advanced, checklist items, PRs/merge SHAs/CI, discoveries, blockers, next task, protected-path diff confirmation.
