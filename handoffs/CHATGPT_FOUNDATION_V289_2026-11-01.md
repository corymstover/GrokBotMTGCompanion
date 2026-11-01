# ChatGPT foundation handoff — v2.89 (2026-11-01)

## Live baseline and policy

- Remote `main` before this batch: **`f16feb9ebe444c49169298a42db97a0b6fedd4df`**, merged [PR #958](https://github.com/corymstover/GrokBotMTGCompanion/pull/958). Its **23/23 exact-head** and **10/10 post-merge** checks passed.
- Master Workflow v2.89, original 137 task lines unchanged: **89 checked, 48 open, `NOT_RELEASE_READY`**. Conditional owner foundation-only acceptance is recorded but its prerequisite gates are not met.
- Foundation first. The 62 approved Grixis decks and frozen source snapshots are protected. All three pilot Commander lists and Phase 6 remain parked.

## v2.89 engineering work

- Added `mv_ask` → Phase 1B Set Atlas → exact Wizards story-series title navigation, built on the preexisting immutable `phase1b_release_scope_story_bridge_2026-10-29.json` (12 cited title matches / 1,062 set codes).
- Real-world Scryfall set `released_at` and official story-page publication dates appear as **different fields**; neither is interpreted as fictional event time or art-scene proof. Up to three sampled directly cited Wizards pages are shown with total recovered count, no fabricated claims beyond title links.
- Known unlinked sets return an honest bounded-index caveat (not no story exists). Unknown names fail closed. Fixed resolution of set titles starting with “The” (e.g. The Brothers' War).
- Five new adversarial Set Atlas tests and three new Q&A acceptance cases; **86 cases, NOT CERTIFIED**. See `research/PHASE7_SET_STORY_NAVIGATION_EVIDENCE_2026-11-01.md`.

## Verification / next steps

- Rebuild the acceptance packet and current tracker, run the full relevant local tests and deterministic evidence checks, and verify exact-head GitHub CI plus post-merge `main` runs. This handoff does not preempt that gate.
- Next: pursue official source gaps and source-graded cross-plane coverage; repeat current-release Oracle/rules freshness and seek the owner's bounded foundation review once all gates actually pass. Do not mark broad tasks complete based solely on a 12-title lookup, change the 62 approved decks, or start Phase 6.
