# GrokBot ADVISORY Pass C trail (NOT qualified Pass C)

**Purpose:** GrokBot's first-pass critiques of the 62 canonical decks, done one deck at a time in tracker order.

**Advisory label:** GrokBot wrote the blueprints, the M1 reviews, the M2–M5 tooling and the Cycle124 critiques, so it is not independent. Nothing here counts as formal Pass C, changes `formal_independent_pass_c_allowed`, edits a canonical deck or approval, or counts toward an M6 gate. This trail is kept separate from `deep_reviews/`.

**Future qualified independent reviewers must seal their own first pass before reading these files**, and must disclose any exposure to them.

**Format:**
- One file per deck: `<tracker_deck_id>.md`.
- Each file opens with a JSON front block containing `tracker_deck_id`, `canonical_sha256`, `verdict` (KEEP / POSSIBLE UPGRADE / NEEDS VERIFICATION), `adds_cuts`, `reviewer_provenance`, `sealed_before_author_review`, and `review_class: "ADVISORY"`.
- The front block is followed by a concise review of under one page.
- `progress.json` is the checkpoint for this trail.
