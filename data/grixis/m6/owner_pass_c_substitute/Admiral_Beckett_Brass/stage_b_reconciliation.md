# Josh-Lee-Kwai — Admiral Beckett Brass — Stage B controlled comparison

**Date:** 2026-10-20 America/Chicago, repository activity 2026-10-21 UTC. **Tracker #1.**  
**Canonical raw approved SHA-256:** `4ba5c483eb67b5f2647d375450adf9c2b7e79a036d0ba1866e58de8441bf3414`.  
**First Stage A commit:** `f88f7e76ebb13eef2ef41fe3469cf7c0106b2d82`; separate pre-unblinding seal `051ce82ddb5e5323bccca7d6b985fcc58bbf2086`; `stage_a.md` SHA-256 `cfb62e6a07afa2f52276bc85634b10d8cafdc610d120a43236001d9d57b6b8ba`; JSON `030606a80ecf9586e2cd1889c1466a1625ac8065bf5448d7b721e3f9b4685f06`.

**Explicit limitation:** Stage A had bounded ledger-level exposure to the exact `+City of Brass/-Crumbling Necropolis` proposal and an excerpt of a nonauthoritative older proposed list; this is not independent corroboration. Deep authored and advisory bodies were not opened before the separate seal. Historical shared GPT-6 context also limits blindness.

## Newly opened, exact unblinded source records

1. Comprehensive ChatGPT author review, `data/grixis/m6/deep_reviews/Admiral_Beckett_Brass.md`, Git blob `9260242347311f424a07bdaec24869c4c50263d8`. It audited 100 cards, 97 names, 35 lands, 34 creature cards (33 Pirate/changeling from printed types including commander), 31 noncreature/nonland cards, and proposes City/Necropolis as an off-ranking land tempo correction.
2. GrokBot advisory, `data/grixis/m6/grokbot_pass_c_advisory/Admiral_Beckett_Brass.md`, blob `3581b9f7079d30cd058c21f908bb518b687b011f`: `KEEP`, no concrete swap; true main bottleneck is three Pirate connections to one player; narrower batch first pass, no whole-list optimality proof.
3. Reconciliation, `data/grixis/m6/two_model_reconciliation/Admiral_Beckett_Brass.md`, blob `c93c4a7c25ca7457ef091c77baa16aa964c34f26`: author proposal `+City of Brass/-Crumbling Necropolis` upheld as `PROPOSE UPGRADE`, GrokBot KEEP treated as having missed an off-ranking tempo improvement. No card applied.
4. Prior factual research audit: canonical `refinement/verification/retrospective_1_to_8/Card_Verification_Admiral_Beckett_Brass_2026-10-14.csv` plus quality gate; historical 311+6 candidate triage acknowledged but not rerun. Official Ixalan Release Notes and Lost Caverns Roaming Throne notes were already used in Stage A.

## Findings by comparison

**Rules consensus:** Admiral costs {1}{U}{B}{R}, gives other Pirates +1/+1 and steals **one** nonland permanent at the beginning of its controller's end step from a player who received combat damage by **three different Pirate creatures that turn**. A single double striker hitting twice counts once; three Pirates hitting different players cannot combine. Roaming Throne choosing Pirate gains that type and causes Beckett's own triggered ability to occur twice; if qualified and two eligible permanents exist, each trigger can take a distinct target. These source-backed mechanics and the non-expiring theft are sound. All sources agree source current 100/97 and project APPROVED/LOCKED, no exception.

**Whole-deck identity:** Stage A preserves early flying/unblockable/menace Pirates, Daring Piracy start-of-combat hasty body, Black Market Connections changeling, Coercive Recruiter temporarily giving an opponent creature Pirate/haste, Roaming Throne, Double Down and combat-value draw/treasure. The original comprehensive review adds important specificity:
- **34 creature cards, 33 printed Pirates/changelings plus Throne choosing Pirate**. Extra goodstuff non-Pirates would directly dilute three-hit consistency.
- **Zephyr Singer convoke** can tap attack-ready Pirates before combat, so using it as a same-turn flying enabler requires sequence planning; cast after combat or tap otherwise unavailable bodies when possible.
- **Fathom Fleet Captain** creates a Pirate token from its attack trigger after attackers have already been declared; the token is not attacking and is a future-combat resource; do not count it as an immediate third connecting body.
- **The Indomitable** is a Vehicle rather than a Pirate creature and can reward combat/draw; do not mistakenly count it toward three Pirate sources.
- **Kari Zev's Monkey token** is not a Pirate; the printed legendary Ragavan card is.
These sharpen factual coverage without changing the provisional land recommendation.

**Land challenger:** Original author and reconciliation proposed City/Necropolis; GrokBot's advisory KEEP offered no meaningful counterfactual for an untapped all-color land. Stage A independently recounted **35 lands**, three standard fetches, six basics and two other always-tapped lands (Path of Ancestry and Xander's Lounge); exposed proposal provenance acknowledged. This is a *direct temporal exchange*: City produces any color untapped with one damage to the tapper, Necropolis produces U/B/R on later turns but cannot tap upon entering. Unlike creature swap hypotheses, Pirate count, evasion and interaction cards are identical between lists. If the fourth land is Necropolis, casting Beckett in that exact main phase is impossible using that land; City can provide the fourth mana with one damage provided the other lands cover requisite colors. This is source-paid deterministic conditional reasoning, not a measured win-rate delta or proof every game advances.

**One technical nuance:** City of Brass triggers one damage when tapped, whereas Mana Confluence pays one life as part of its activation cost. The distinction matters with damage prevention, life-loss triggers and timing, but no such special loop is being claimed here; both are untapped any-color lands in this deck. Official Commander legality is supported by the prior 2026-10-19 check; a fresh current Oracle snapshot for exact add/cut should still be attached to owner decisions.

**Strongest defense of KEEP:** The base already carries substantial Pirate density and 35 lands plus eight conventional rocks; three connections and surviving to end step, not a single land, dominate the commander's reliability. City self-damage becomes meaningful in attrition matchups and a tapped Necropolis can be naturally sequenced on an otherwise idle first turn. That is a legitimate strategic tradeoff; a challenger isn't automatically better because its card has higher generic usage. GrokBot's KEEP is reasonable about evasion but incomplete about the specific mana-base timing issue.

## Other alternatives and disagreements

- **Reflecting Pool** versus Necropolis avoids life pain but is source-dependent alongside Ancient Tomb and creature-restricted mana. Test as an honest alternative if life attrition matters; cannot universally supplant City.
- **Plaza of Heroes** might protect legendary Beckett and cast a legend, but produces unrestricted colored mana only conditionally; it is a different defensive hypothesis with nonlegend Pirate colored-mana costs. City more directly supports diverse Pirate one-drops and Counterspell.
- **Slippery Scoundrel** needs city's blessing/10 permanents for unblockable, slower than current evasive low-cost crew; replacing Zara or Daring Saboteur loses distinctive theft/selection. No valid immediate superiority.
- **Fell Flagship** is a non-Pirate Vehicle, so could improve damage but not the count of distinct Pirate hits by itself. Earlier hypothetical cuts Edward Kenway/Open into Wonder sacrifice meaningful current identity. Reject these exact prior proposed pairs.
- **Koh, the Face Stealer** is expensive and not itself a Pirate. Do not swap in under generic theft logic.
- **Crumbling alternatives:** Path of Ancestry provides tribal scry; Xander's Lounge has typed fetch/cycle value; Drowned Catacomb is conditionally untapped; Secluded Courtyard supports Piracy but only for creatures. Crumbling is the least distinctive always-tapped color-fixing slot if a City-type effect is available.

## Tests and current boundaries

Prior comprehensive review and reconciliation contain valid **static conditional mana sequencing**, not a qualified colored-source Monte Carlo or observed four-player game win rate. The probability that one named card appears among ten unordered cards from 99 is 10/99 under stated assumptions; it is not the chance City is decisive on T4. A proportional simulator not modeling tapped lands, Pirate combat access and damage-prevention effects would not justify a strategic claim.

**Targeted Phase B (post-JLK, if it changes M7 decision):** same-seed opening-hand/color-access comparison among baseline, City/Necropolis and Reflecting Pool/Necropolis; model turn-one cheap Pirates, turn-four Beckett with exact pips, turns land tapped/untapped, City life/damage across attrition games, and concrete three-Pirate board states under opponent removal. Preserve all 99 other cards and 35-land density. If no effect-aware engine is available, use enumerated hands/mana proof with disclosed bounds rather than fabricated win rates. No automated playtest performed in this Stage B.

**Controlled conclusion:** `PROPOSE UPGRADE` as the research recommendation `+1 City of Brass/-1 Crumbling Necropolis`, at moderate strategic confidence but **without owner approval**. This is an on-identity land tempo proposal; factual prior exposure means the Stage A alignment must not be counted as an independent third vote. Official whole-list legality/Oracle and Phase B/M6 certificate gates remain separate. Canonical unchanged.
