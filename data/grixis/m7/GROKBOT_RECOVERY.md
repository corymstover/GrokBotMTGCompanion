# GrokBot M7 production — recovery procedure for a fresh session

1. `git fetch origin` and read `data/grixis/m7/grokbot_production_ledger.json` on branch `grokbot-m7-production-ledger`
   (mirror: /workspace/out/production/ledger.json; the remote branch wins if they differ).
2. Find the first entry whose status is not REVIEW_READY_AWAITING_CHATGPT / AWAITING_OWNER_APPROVAL / OWNER_APPROVED_LOCKED.
3. For that deck inspect: remote `working_branch` (`git ls-remote origin <branch>` must equal `last_pushed_commit`; if the
   remote is ahead, trust the remote), its open PR (`gh pr list --head <branch>`), and
   `data/grixis/m7/wip/<deck_id>/CHECKPOINT.md` on that branch.
4. Resume at the ledger's `next_step`. Do not redo stages listed in `completed_stages`; do not open a second PR for a
   branch that already has one (update the existing PR); never force-push; never create a new branch for an in-progress deck.
5. Commit and push after every meaningful phase (or ~10–15 min), verify with `git ls-remote`, then update and push this ledger.
6. Never touch canonical (corymstover/grixis-commander-encyclopediaGPT is read-only), PR #651, or decks #1–#3; never merge,
   approve, lock, or edit state/current_deck_overrides.json. CI success is not approval. WIP files must be removed or
   relabeled when a PR is marked ready for review.
