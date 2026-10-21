# Josh-Lee-Kwai formal owner-equivalent Pass C — final disposition: Rograkh // Silas Renn (#47)

**Decision (2026-10-21 America/Chicago): NEEDS TESTING — retain exact currently APPROVED / LOCKED canonical list unchanged.** No proposed swap is accepted, auto-applied, or presented as proven stronger. The most consequential open card-role comparison is **+Brainstorm / -Demonic Counsel**, already conditional in the comprehensive author review, not the Stage A reversal of the owner's recent Vexing Bauble choice.

## Immutable source, formal proof and governance

| Item | Verified value |
|---|---|
| Deck/track position | `RogSi`, tracker index 46, deck 47/62 |
| Commanders | Rograkh, Son of Rohgahh **and** Silas Renn, Seeker Adept (partner; both command-zone cards) |
| Source authority | `corymstover/grixis-commander-encyclopediaGPT/main` |
| Approved list | `refinement/decklists/RogSi_Approved_2026-10-15.txt`, Git blob `6b7827592ff0f2eaca004b4b02a9867ed49a0879` |
| Independently recomputed RAW list SHA-256 | `06c9e22b5afc46bd58bbbfdef5c42a796d2a986a2972456107c29aee1b5f905c`, matching `state/current_deck_overrides.json` |
| Approval/status | Explicit owner approved October 15, 2026; **APPROVED / LOCKED**, unchanged |
| Structure | 100 physical cards; 2 legal partner commanders + 98 in library; 100 distinct; 24 lands; singleton OK |
| Commander color identity | U/B/R (Rograkh red color indicator despite {0}; Silas U/B) |
| Official Commander legality | No listed card in WotC current Commander banned list; no project-specific exception used; selected current Oracle/rules corroborated. Full fresh 100-card Oracle-by-Oracle refresh **not** performed at Pass C. |
| Stage A first-stage Git commitment | `466d805a8f500d6d7a8c5887d0e00f095c48b5a7` |
| Stage A immutable SHA-256 fingerprints | `stage_a.md: 589194ae8052f0cbf047c5bda2c0dd8f2e070ec93c8766e1dbd5ac0c3c90cf27`; `stage_a.json: 487f16a84f9f70923c8cadfb1bdc1d8e503488aaf046e35d5ba9c0e21eef27db` |
| Separate seal Git commit | `0d7b9f2d5beae8cc9b7026880c656d3eb90ffc8e`; seal committed **before** opening prior RogSi reviewer conclusions |
| Neutral Stage A disposition | NEEDS TESTING, provisional **+Orcish Bowmasters/-Vexing Bauble**, alternative cut Paradise Mantle |
| Prior author / GrokBot / reconciliation | KEEP / KEEP / documentary agreement, subject to unapproved conditional author challenge |
| Final Pass C classification | `FORMAL_PASS_C_OWNER_EQUIVALENT`; technical third-model independence **NOT PRESENT**, owner-waived |
| Stage B record | `data/grixis/m6/owner_pass_c_substitute/RogSi/stage_b_reconciliation.md` |

**Reviewer provenance:** Alias **Josh-Lee-Kwai** is actually **ChatGPT/OpenAI GPT-6**, same model lineage as the original comprehensive author/reconciler. Same-model latent prior-project memory cannot be erased. Before Stage A seal, no prior RogSi author/advisory/reconciliation/candidate-ranking or approval *decision* file was opened; general user-shared cEDH/ranking exposure and historical shared-model biases are disclosed. This satisfies Cory's explicitly authorized **formal owner-equivalent** governance qualification after technical evidence checks; it is **not** actual independent third-model execution, a measured tournament performance study, or owner acceptance of M6.

## Commander-first strategic finding and natural ceiling

**Natural ceiling: Bracket 5 — cEDH.** Rograkh's zero-mana red body is uniquely central: it makes Mox Amber live, can tap for Drum, pays native creature-sacrifice costs of Culling the Weak/Infernal Plunge/Diabolic Intent and alternative Flare of Duplication, and makes commander-controlled protection/Jeska's Will flexible. Recasting after a sacrifice incurs its *own* tax. Silas supplies U/B color identity plus situational combat-hit artifact recursion at paid mana and normal cast timing; he is not a turn-one guaranteed infinite artifact engine. Protect the compact low-curve turbo identity: Ad Nauseam/Necro resources, Thassa's Oracle + Consultation/Pact, and Breach + LED + Brain Freeze/Grinding Station, with substantial interactive stack defense. A generic high-CMC artifact Monolith package is not an identity-first improvement.

The 24-land configuration is intentional but has real source constraints: nine fetches, six shock/dual, a surveil tapped UB land, colorless fast lands, conditional Caverns/Moxen, and black/blue/red symbol competition. This deck can be fast and demanding. Counting nominal rocks as unconditional colored producers or assuming 100-card gross land rates represent competitive mulligans would be misleading. The extra-turn spells **Final Fortune** and **Warrior's Oath** demand a win before their losing triggers, not an automatic costless turn.

## Verified interactions, opponent responses and limitations

1. **Vexing Bauble is symmetric and timing-critical**, not a unilateral free counter lock. Rograkh's first {0} cast, free counterspells, 0-mana artifacts and Breach escape of LED with zero mana paid invite its triggered counter. Actual {2} commander tax is mana spent and can change the outcome. Spending {1}, tapping and sacrificing the Bauble opens the free-spell turn at a cost and a specific window. Hexing Squelcher makes our spells uncounterable while present; Samut's split second for our instants/sorceries does **not** prevent triggered Bauble abilities. A hostile free-spell table supports Bauble; a draw-rich table may reward Bowmasters but this is matchup-dependent. Source: WotC MH3, Lorwyn Eclipsed and Reality Fracture release notes.
2. **Demonic Counsel is blank as a tutor before delirium** in this specific 100, with zero Demon cards to find. Delirium requires four actual graveyard card types, not four spells cast or future expected cards. A fetchland, artifact, instant and sorcery can attain it, contingent on graveyard access. Necrodominance may strand the condition and exile the other Breach inputs. Brainstorm offers immediate {U} cantrip/selection, but post-delirium Counsel searches *any* needed singleton for {1}{B}. Source: WotC Duskmourn release notes.
3. **Necrodominance is a separate refill mode**, not a free graveyard enabler: skips draw, provides optional paid-life card draws on own end step, maximum hand five, and replaces transfers to own graveyard with exile. Active Necrodominance blocks new Breach escape fuel, Silas GY targets and delirium building; it is different from Necropotence. A main-phase Necrodominance that has not yet reached end step has not generated its draw. Source: WotC MH3 notes and 2026 Reality Fracture notes.
4. **Silas requires actual combat player damage**, a valid GY artifact target on its trigger, mana and later normal casting timing. Kill/block Silas or use gravehate to deny; the ability is not unconditional flash. Source: WotC Commander 2016 notes.
5. **Breach combo is interruptible**: LED can add a *single chosen color* and discards hand; every escape uses normal mana (where required) and exiles *three other* GY cards, Storm copies of Brain Freeze aren't cast, and hate/taxes or target availability constrain loops. Opponents can interrupt setup, remove Breach, exile graveyard or counter the Oracle win trigger; don't count deterministic lines as automatic games won.
6. **Other relevant stax:** Rule of Law constricts multi-spell turns; Collector Ouphe/Null Rod switch off artifact activation; Drannith Magistrate obstructs casting Rograkh from the command zone; removal of Hexing Squelcher/Samut before a protected cast reopens counter windows. Opponents can withhold extra draws to weaken Bowmasters. None is hypothetical proof of a win percentage.

**Source receipt family:** WotC `/en/banned-restricted-list`; `/en/news/feature/commander-2016-edition-release-notes-2016-10-28`; `/en/news/feature/modern-horizons-3-release-notes`; `/en/news/feature/lorwyn-eclipsed-release-notes`; `/en/news/feature/reality-fracture-release-notes`; `/en/news/feature/duskmourn-house-of-horror-release-notes`; `/en/news/feature/the-lord-of-the-rings-tales-of-middle-earth-release-notes`. These support selected mechanics. Current 100-card Oracle refresh and opponents' measured configurations remain beyond this Pass C record.

## Exact proposed alternatives (testing only; no owner swap requested yet)

| Prioritization | Exact challenger | Why still plausible | Why not applied |
|---|---|---|---|
| **Targeted priority** | **ADD Brainstorm / CUT Demonic Counsel** | Always functions for {U}; nine fetches smooth putbacks; removes a potentially completely blank pre-delirium draw | Council becomes a true any-card tutor with four GY types, particularly valuable later; no documented pre-delirium dead-draw frequency or exact effect-aware tempo gain |
| Conditional/meta only | ADD Orcish Bowmasters / CUT Vexing Bauble | Punishes opponents' extra draws and own wheels, covers some small creatures, removes own free-spell Bauble conflict | **Exact inverse of Oct15 owner-approved Bowmasters→Bauble**, already carefully researched; 1,767-list original cohort descriptive inclusion Bauble 84.2% vs Bowmasters 19.5%, not updated causal data; removing cheap free-stack disruption may weaken turbo protecting its win |
| Weaker alternative cut | ADD Orcish Bowmasters / CUT Paradise Mantle | Retains Vexing protection and reduces a slower equip-dependent accelerator | Costs commander-colored mana and loses zero artifact/metalcraft and later colored mana functionality; hasn't shown net benefit in 24-land shell |
| Pod-dependent | ADD Dauthi Voidwalker / CUT Vexing Bauble | Effective against enemy graveyard wins, preserves use of our own graveyard while exiling theirs | {B}{B} hard in some burst hands; loses cheap universal anti-free-spell stack shield, and no matchup test |
| Alternative fix | ADD Fellwar Stone / CUT Demonic Counsel | Colored ramp versus live tutor role, useful under longer games | Two mana, opponent land colors conditional; doesn't replace late tutor precision |

**Strongest counterargument to our remaining test target:** no generic one-mana cantrip is a strict substitute for a two-mana tutor that can become unrestricted by turn two/three in a sacrifice-/fetch-/ritual-heavy deck. Fast RogSi likely enables delirium earlier than ordinary black decks. The test must measure *actual* graveyard type availability without incorrectly assuming either never- or always-on delirium.

## Final judgment and next evidence gate

**Final disposition = NEEDS TESTING; current owner-approved deck = KEEP unchanged.** Stage A's Bowmasters idea was independently generated within the source-isolated packet, but controlled Stage B identified it as a **previously rejected/owner-approved inverse**, so an attempted rollback on novelty alone fails the strongest adversarial counterargument. The prior author/GrokBot KEEP agreement remains relevant and is not incorrectly relabeled as measured no-improvement proof. Demonic Counsel versus Brainstorm is the most credible contingent difference from that agreement, already documented by the author and not resolved by raw candidate ranks. If actual Phase B effects/mulligan tests favor the incumbent or show insufficient coverage, document local limits and KEEP rather than manufacturing swaps.

**Future tests**: exact baseline and exact named challenger lists; record deck hashes, affected opening hands, mulligan rule, colors and mana timing, four graveyard types, opponent free-spell/draw/hate fixtures, Breach-exile treatment, legal stack windows, RNG seeds and simulator effect coverage. Distinguish deterministic rules traces, proxy/partial model checks, and full effect-aware performance. Reuse prior validated source/whole-list/Oracle coverage where still valid; do not rerun Colab or a universal candidate sweep.

**Approval boundary:** zero card changes applied or approved; exact canonical owner SHA and all 62 owner locks preserved. The user must explicitly authorize **any** eventual named add/cut after targeted evidence and a new complete structural/Oracle/legality verification. Neither CI nor this Pass C disposition completes effect-aware Phase B, tested-pool I zero-improvement, reproducibility J, M6 certification, M7 final owner decisions, or M8 Birthday export.

**Reviewer/governance:** Josh-Lee-Kwai = ChatGPT/OpenAI GPT-6, not technically independent. Qualification is owner-authorized `FORMAL_PASS_C_OWNER_EQUIVALENT`, technical independence false, waiver `OWNER_WAIVED_FOR_FORMAL_PASS_C`. Formal per-deck evidence counts only after exact-head PR CI, merge and separate progress-ledger integrity checks.
