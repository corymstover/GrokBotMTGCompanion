# GitHub old-branch reconciliation — read-only checkpoint, November 2, 2026

Full SHA-resolved [head inventory](../../data/maintenance/github_branch_heads_2026-11-02.json)
was fetched directly from `git ls-remote --heads origin`: **888 branches**, **876
distinct tip SHAs** and **12 pairs** pointing to the exact same commit.
This gives every branch an exact recovery target before any cleanup. No refs
were deleted, forced or moved in this inventory step.

The 12 duplicate-head pairs are concentrated in October 22 Abaddon M6/M7
research, plus one M7 owner-gate pair. The manifest lists both names and
shared SHAs. One redundant **name** per pair *may* be a limited candidate for
deletion once references and branch protection are checked: deleting either
name does not by itself delete that identical commit while the other stays.
It **can** still break automation or documentation that hard-codes the name,
so it is not automatically authorized for deletion.

The other **864 branches with nonduplicate head SHAs** cannot safely be called
useless on head-count or age alone. They may contain unique owner receipts,
rules research, proposal snapshots, unresolved audit data or workflow code.
Determine ancestry, reachability from current main, exact PR/approval
relationships, and whether evidence has another immutable home *before*
pruning. An identical *tree* or a merged commit with a different SHA could
expand the safe pool, but that has **not** been established here.

**Explicit keep / do-not-prune targets:**

- `main` (production branch; never delete)
- `chatgpt-cycle76-m6-refinement` (historical M6/M7 source and PR base)
- `chatgpt-abaddon-rev3-owner-receipt-canonical-verified-20261023`
  (unmerged original PR #650 owner receipt and validation; head `6ca2e52ea2e9a8570691324af019486e37043859`)
- `chatgpt-m7-lord-approved-case-transfer-20261025`
  (unmerged original PR #707 14-case rules transfer and bulk sources;
  head `0d4c51d2c5756a0c6207fe4b5d47d4e8afdd0920`)
- Any other protected/default/release/current-CI branch or branch containing
  unique approvals, rules evidence or research not safely copied elsewhere.

PR-specific file provenance and owner distinctions are recorded in
[PR #650/#707 reconciliation](PR_650_707_RECONCILIATION_2026-11-02.md).
The GitHub connector available for this cleanup can close PRs and manage
branch refs but **cannot delete a ref**. We intentionally did not force-update
any ref as a substitute for deletion. Actual safe pruning remains gated on a
supported deletion interface and additional branch-by-branch proof.
