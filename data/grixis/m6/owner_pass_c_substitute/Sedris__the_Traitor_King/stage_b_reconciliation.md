# Josh-Lee-Kwai — Sedris, the Traitor King — Stage B controlled comparison

**Date:** 2026-10-21 America/Chicago  
**Canonical SHA-256:** 65fbfe3eb64551ad6f5723243fcd62a286610c360e24bd700b584252e1da6365  
**Prerequisite first-stage commit:** cb4591485df61eec582b82820b89ae34650a0d1f  
**Separate cryptographic seal commit:** 07b6c01238980a78069895483c434359d7340ca2  
**Stage A hashes:** md 4f730ea771d246b9739dd6b9e025bb1615fd984a2a6a3f788fd2455c05017c59; JSON 0e0fb83faf6bbd34261b17f981693d3b3eb1c146d8f3450c8c00707bdaf2c49b.  
**Exposure:** prior administrative summary exposure was disclosed in the immutable Stage A and seal. Full author/GrokBot/reconciliation artifacts were opened only *after* the separate seal commit. No edit to sealed Stage A.

## Unblinded source documents and provenance

- Original complete authored report: data/grixis/m6/deep_reviews/Sedris__the_Traitor_King.md (Git blob fa1960358e6de2b6d3df7f340bba376a903cbcf1; ChatGPT; author KEEP). Its 100-row whole-list review, 111 historical candidate-pair judgments and 45 finite rules/timing probes are substantive evidence, **not measured multiplayer outcomes**.
- GrokBot advisory: data/grixis/m6/grokbot_pass_c_advisory/Sedris__the_Traitor_King.md (Git blob d78631c9c8ec67aa17691acb210db2157cf22314; advisory NEEDS VERIFICATION; exact +Ghostly Flicker/-Sundial).
- Two-model reconciliation: data/grixis/m6/two_model_reconciliation/Sedris__the_Traitor_King.md (Git blob a4978a0735e618d5855ee0b39fe8e8bda4e8e1bd; final KEEP rejected that exact swap after primary-source rule check).
- Machine source packet data/grixis/m6/review_packets/sedris-the-traitor-king.json (blob ad8d7f36b3a0d739b9302961d6249892237d6f8d, 111 M5 candidate pairs; neither Displacer Kitten nor Scholar of the Lost Trove appears); static mana record data/grixis/mana_base/sedris-the-traitor-king.json (blob cd0750143c25a7ff67d7229492a8ac11aa43caf8). The packet's win-turn proxy is not an effect-aware model of these new candidates.
- Earlier first-party interaction record grixis/interactions/sedris-the-traitor-king.md (blob 5399d57bf8f72d55ad2d0dc2ac841a18e3640cea) traces six Sedris rules interactions against an Oct16 Oracle/Oct15 rulings/Sept25 2026 CR snapshot.

## Independent Stage A findings vs historical evidence

| Issue | Sealed Stage A | Original author | GrokBot advisory | Reconciliation | Stage B judgment |
|---|---|---|---|---|---|
| Identity and ceiling | Six-MV UBR unearth ETB/attack toolbox; Bracket 4 | Same; commander-first KEEP | Same broad engine | Same | Substantive agreement, not empirical optimality |
| Card accounting and locks | 100 copies / 99 names / 31 lands, locked SHA | Same full 100-row audit | 100 / on-color | Same 100/99 | Revalidated from raw current GitHub TXT and independent SHA256 |
| End-step Sundial | Preserve after delayed triggers are on stack; replacement exile persists | Correct step/timing | **Incorrect claim** it never preserves bodies | Corrected GrokBot error, rejected -Sundial | KEEP Sundial; verified against Wizards' official Sundial and unearth explanations |
| Ghostly Flicker | Seen in administrative metadata; quarantined, not independent hypothesis | Considered among off-packet alternatives | +Ghostly / -Sundial | Reject that exact pair, while acknowledging flicker's distinct rescue niche | No basis to overturn protected Sundial on same incomplete evidence |
| New primary challenger | +Displacer Kitten / -Panharmonicon, **NEEDS TESTING** | Not examined by name | Not examined | Not examined | True unaddressed incremental hypothesis; remains undecided |
| New secondary challenger | +Scholar / -Etali, lower confidence | Not examined by name | Not examined | Not examined | Rules-valid mechanism with material preconditions; not enough to recommend |
| Mana / colored source bottleneck | 31 lands; 6MV UBR then 2B; removal tax | Same structural warning | No quantified rebuttal | No effect-aware test | Existing source proxy supports a concern, not a real-game failure rate |
| Win combo | Paid Drake+Navigator mana, Terror damage conditional | 45 finite probes; warns mana is not automatically Bombardment damage | Not decisive | Paid and interrupted sequences | Preserve precise conditional logic, no invented infinite kill from mana alone |

**Important disagreement resolved:** GrokBot's Sundial rule was factually overbroad. In your own end step, allow the one-shot unearth delayed exile triggers to go onto the stack, then use an untapped Sundial for {1},{T}. End turn exiles pending triggers; because already triggered they do not recur. The continuous replacement effect still exiles that creature when it would depart to a nonexile zone. Ending the turn during second main instead *skips* the end step and postpones the triggers, which is the limited case GrokBot described. Wizards Sundial release notes: https://magic.wizards.com/en/news/feature/avatar-the-last-airbender-release-notes ; Wizards unearth release notes: https://magic.wizards.com/en/news/feature/warhammer-40000-commander-release-notes-2022-09-19 . This confirms KEEP Sundial and does not require re-running the former 45 rules probes.

## New challenger: actual rules and judgment limits

### Displacer Kitten vs Panharmonicon

Wizards printed Displacer Kitten as {3}{U} 2/2 with a **cast-noncreature** triggered ability to exile and immediately return up to one target nonland permanent you control. The returned card is a **new object** (official CLB release notes https://magic.wizards.com/en/news/feature/commander-legends-battle-baldurs-gate-release-notes-2022-06-01). It legally resets an unearthed creature's future end-step exile and replacement effect when it can resolve while the creature is present. Its target may instead be a rock or ETB creature; if the object is a token, that token does not return after exile.

**Payable trace:** Sedris already on board, Archon in graveyard, Kitten on battlefield, at least {2}{B} available, and a cheap legal noncreature spell in hand. Activate unearth, let Archon enter (first normal ETB); cast the noncreature spell; Kitten triggers and targets Archon; if target remains legal, Archon is exiled and immediately returns as a new object, producing another ETB independent of the original unearth obligation. Kitten is vulnerable to interaction before its trigger and the legal target is vulnerable while trigger waits. This line requires **four conditions beyond having the standard unearth**: Kitten on field, noncreature spell available/castable, timing/mana, and permanent surviving until trigger resolves. No noncreature spell is automatically created by the unearth activation.

**Panharmonicon comparison:** Panharmonicon costs {4}, is harder to remove with creature kill, and doubles trigger events **whenever a creature/artifact entry causes a permanent you control to trigger**. An unearthed Archon already triggers twice under it with no extra spell; repeated unearths compound its value. It does **not** cancel the subsequent unearthed exile or double non-ETB attack triggers. Kitten offers a fresh object and flexible blink of another nonland target, but Panharmonicon gives a more reliable one-card multiplication payoff per unearth. They are not interchangeable effects and the earlier author's identity protection of Panharmonicon is a serious objection.

**Alternate exact cut screens:**
- **-Panharmonicon:** closest four-mana opportunity-cost comparison, but may materially reduce every ETB creature's baseline value; needs matched timing tests.
- **-Feldon of the Third Path:** gains Kitten but loses graveyard access when Sedris is absent and cheap repeatable token-copy ETB; makes the deck more commander-dependent.
- **-Etali, Primal Storm:** trades attack-trigger ceiling (immediately enabled by unearth haste) for four-mana blink utility; removes a powerful one-turn payoff and potentially underweights attack value.
- **-Jin-Gitaxias, Core Augur:** reduces bloated hardcast curve, but removes an impactful return target whose own end-step draw seven can resolve before its unearth exile with ordering; don't dismiss it from a mana-only score.
- **-Sundial:** reject as an improper identity loss and prior rules error.

**Effect coverage:** No fetched M5 screening result models Kitten's cast triggers, legally targeted blink, preservation windows, or Panharmonicon baseline doubled trigger counts in realistic opponent states. No measured win rate, new simulation, or Phase B completion is asserted. Targeted paired tests and hand-sequence scenarios must evaluate payoff *and* opportunities to cast the triggering noncreature spell. Do not count one trigger on paper as an achieved game advantage.

### Scholar of the Lost Trove vs Etali

First-party Wizards Oracle-source release notes (https://magic.wizards.com/en/news/feature/core-set-2021-and-jumpstart-release-notes-2020-06-20) establish Scholar costs {5}{U}{U} and can cast a targeted instant, sorcery **or artifact** card from your graveyard without paying its mana cost when it enters. Instant/sorcery spells cast this way are exiled rather than put into the graveyard this turn. Under Sedris, Scholar's high printed cost collapses to the same {2}{B} unearth activation as Etali, but its ETB may be empty if the yard contains only creature cards. Etali has an immediately available haste attack trigger but exiled opponent top-card quality and castable choices are volatile; neither is intrinsically better for all board states.

Search surfaced a Wizards February 9, 2026 **Historic-format** ban of Scholar, **not** a Commander ban (https://magic.wizards.com/en/news/announcements/banned-and-restricted-february-9-2026); do not mistake format scope for an official Commander blocker. A current commander-specific Scryfall legality response is still needed before declaring the candidate approval-ready. The secondary swap remains a lower-value test proposal, not an intended deck mutation.

### Mana and existing tests

The static mana file's 31 lands / 10 repeatable nonland mana sources and {3}{U}{B}{R} casting cost agree with Stage A. It estimates B/U/R land-source counts 19/17/15, or 24/22/20 after repeatable nonland sources, with caveats about tapped lands/fetch target access. Its no-mulligan source-presence proxies are **not** turn-five cast probabilities; therefore the Stage A concern is strategic, **not quantified by these proxy percentages**. The 111-case M5 review packet has prior proxy goldfish results that do not model Kitten/Scholar mechanics and cannot decide these new hypotheses. The author's 45 finite probes are useful for already tested Sedris rules, not a claim of Phase B effect-aware outcomes.

## Stage B disposition

1. **Confirmed agreement:** preserve Sedris's high-value ETB/attack unearth identity and existing owner lock.
2. **Resolved contradiction:** GrokBot's Sundial timing error does not justify +Ghostly Flicker/-Sundial. The replacement exile still applies after ending turn, and Ghostly Flicker has a distinct valid blink role.
3. **Independent new unresolved issue:** +Displacer Kitten/-Panharmonicon plausibly strengthens some preservation windows but may be weaker in normal ETB play; queue **targeted effect-aware testing** before any proposal for Cory.
4. **Lower-confidence unresolved issue:** +Scholar/-Etali merits current Commander legality confirmation and a narrow target-density/board-state comparison, not a general deck rewrite.
5. **Owner gate:** no swaps applied, no new approvals, no lock changes, no M6 or Phase B certification. All first-stage artifacts/seal remain immutable.

Stage C can finish as an evidence-grounded **NEEDS TESTING** Pass C disposition, while the two new exact candidate hypotheses remain *research*, not established improvements. Formal owner-equivalent Pass C completion is permissible after exact-head CI, but the outstanding targeted tests belong to the post-JLK risk-based Phase B queue.
