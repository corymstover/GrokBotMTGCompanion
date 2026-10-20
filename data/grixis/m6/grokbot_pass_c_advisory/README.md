# GrokBot ADVISORY Pass C evidence trail (separate; NOT qualified Pass C)

GrokBot wrote the blueprints, M1 reviews, M2–M5 tooling and the Cycle124 critiques, so it is **not independent**. Every file here is ADVISORY. Nothing here sets `formal_independent_pass_c_allowed`, changes a canonical deck or approval, or counts toward formal Pass C or the M6 gates. This trail is kept apart from ChatGPT's `deep_reviews/`.

**Future qualified independent reviewers should NOT read these files before sealing their own first pass.** Exposure to them must be disclosed.

Each deck has its own folder, `<tracker_deck_id>/`, built in this order:
1. `stage_a.md` + `stage_a.json` (+ an optional `stage_a_oracle_snapshot.json`). Written before any exposure to author conclusions.
2. `seal.json`: sha256 of the Stage A files plus the input fingerprints. It is committed and pushed **before** Stage B. Stage A is never edited afterwards.
3. `stage_b.md` + `stage_b.json`: the comparison with the deep review and M5. `stage_b.json.seal_commit` must be an ancestor of HEAD, and the seal commit's tree must already contain identical Stage A bytes and no Stage B.

`progress.json` is the checkpoint for this advisory pass. Validator: `python scripts/grixis_m6_grokbot_advisory_check.py --check`.
