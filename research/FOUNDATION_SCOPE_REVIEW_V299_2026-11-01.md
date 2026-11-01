# v2.99 — bounded knowledge-foundation owner acceptance and rules-lookup review

**Status:** **CANDIDATE ONLY — NOT RELEASE CERTIFIED UNTIL EXACT-HEAD CI AND PROTECTED DECK CHECKS.**

Cory gave explicit owner authorization for finishing the finite foundation milestone on November 1. This review applies that authorization only to source-graded existing claims and guarded supported Q&A. It does not invent missing lore or call any post-bulletin card interaction definitively legal.

## Graph and disputed genealogy — K132

`scripts/audit_foundation_graph_scope.py --check` validates the exact five historical Pack A/B/C claim files against their source registers and the rebuilt graph. The audit covers **78 existing linked claims** (A 32, B 18, C 28), checks their grade and claim-edge identity, confirms that every cited source in their joined register belongs to `magic.wizards.com`, and independently rechecks all input SHA-256 values in `data/release/foundation_graph_scope_review_2026-11-01.json`.

The direct Pack A/Pack B/Pack C structures remain preliminary. The separate owner disposition record, `data/release/pack_a_genealogy_owner_dispositions_2026-11-01.json`, deliberately refuses unsupported genealogical promotions:

| Dispute | Conservative disposition |
| --- | --- |
| GD1 | The twins remain directly sourced; Bolas's ambiguous in-story dissent remains acknowledged. |
| GD2 | Ugin/Bolas parentage is **UNKNOWN**; no Ur-Dragon parentage inference. |
| GD3 | Conflicting Elder Dragon survivor rosters remain **DISPUTED**. |
| GD4 | Raider-descendant claim stays limited to its narration frame. |
| GD5 | Piru/Crosis ancestry retains its direct evidence; precise generation and Piru–twins relation stay unknown. |
| GD6 | Darigaaz/Rith sibling material stays a research note, no invented shared parents. |
| GD7 | Chromium's banishment and murder are not assigned a fabricated temporal order. |

This fulfills **searchable, source-graded connections across three packs**, not the separate broad-history, complete-genealogy or all-source chronology research tasks. The Yawgmoth/Old Phyrexia order and unrelated source-local histories stay open.

## Reviewed history, chronology, and hard Q&A — K135

`data/release/knowledge_foundation_acceptance.json` accepts exactly the documented knowledge-only scope using the independently rebuildable **119 distinct difficult questions**, 626 accounted-for inventoried Wizards source pages (576 cited + 50 reviewed with no new claim), and 17 independent source-local historical strands (155 events, 126 strict relations, 525 evidenced comparable pairs). Both chronology ledgers remain separately labeled; publication dates cannot supply fictional event order. Assertions with disputed voices, unsupported family relations, current-leader gaps or unanchored transitions remain `QUALIFIED`/`NOT_FOUND`/UNKNOWN.

The final seven-gate release still requires the rules lookup and two exact-commit CI gates. No existing lore-deck draft, pilot, or one of the 62 approved Grixis decks is reviewed or changed by this acceptance.

## Current-source supported card/rules lookup — K133

`scripts/audit_lookup_rules_scope.py --check` validates currentness **within the supported, explicitly dated routes**, anchored to the latest independently downloaded **November 1 22:00 UTC** SHA-verified Scryfall bulks (39,287 Oracle cards, 120,019 default printings, 79,706 ruling records) and the archived October 30 indexed Oracle-text parity. The exact October 30 → November 1 22:00 audit found **7 semantically tracked Oracle changes, 49 printing changes, 0 ruling changes, and 0 new IDs**; mere keyword-array ordering is normalized. All **33,894 indexed Oracle UUIDs** are still present; the only newly changed indexed Oracle tracked field is a layout-only token. Both newly changed Oracle texts and the new color-identity change occurred on *unindexed* cards. No new ruling record was added, removed, or changed. The historical set/printing atlas retains its separate dated limitations.

The acceptance audit runs ordinary legal and illegal Commander inclusion, a rulebreaker caution, a directly documented published-ruling interaction, a no-ruling case, and a newly affected meld question. The official [October 19 update bulletin](https://magic.wizards.com/en/news/announcements/mystery-booster-commander-edition-update-bulletin) announces pregame Rulebreaker and a meld/DFC recategorization, while the [downloadable official Comprehensive Rules](https://magic.wizards.com/en/rules) still linked the September 25 TXT at the date of review. These are **two separately labeled sources**; the new bulletin is not substituted for verbatim rules text. The affected meld, transform, convert, double-faced and rulebreaker Q&A routes explicitly return **`QUALIFIED` plus a `current_gameplay_application: UNRESOLVED_PENDING_CURRENT_CR_TEXT_RECONCILIATION` marker**, not an asserted post-update gameplay ruling.

Thus the accepted capability is *reliable, source-qualified lookup within the tested scope*. A complete gameplay simulator, an automatic live ban-list decision, and new/unindexed Oracle cards remain out of scope. Missing official full rules text is openly tracked for future refresh; it is not misrepresented as a newly hashed document.

## Gate status and exact-release checks

Machine readiness before GitHub candidate CI: **5 MET / 0 PARTIAL / 2 EXTERNAL**, verdict `READY_FOR_OWNER_REVIEW` (never a certification claim). K132, K133 and K135 are closed for their explicitly qualified capabilities; **K136 and K137 remain open** until the exact candidate's focused Grixis validation, protected-path zero diff, all GitHub workflow results and current coverage recount have been checked. No owner deck approval is a prerequisite for the foundation.

After the candidate passes, record the exact main SHA, source/report hashes, no-regression diff and full Actions results in a separate final certificate. Keep open research and ongoing maintenance tasks visible in the 137-item triage; a *knowledge-foundation milestone certificate* does not mean every future Magic story, unknown genealogy or Phase 6 deckbuilding task is finished.
