# Josh-Lee-Kwai — Goro-Goro and Satoru — controlled Stage B unblinding

**Date:** 2026-10-21 America/Chicago | **Tracker:** #21/62 | **ID:** `Goro_Goro_and_Satoru`  
**Immutable Stage A first commit:** `23d35f6f5386f19175b73f35120b71aa45382ed5`  
**Separately committed and verified seal:** `9a1dd1a3afda35370d719e2cc59eb5a25cb7a94b`  
**Exact approved owner TXT SHA-256:** `2fd39e3b39afaeb1bf394a59b392d8a29f28645776fa0b13c5754df67ab85fdf`.

## Controlled sources, opened only after Stage A remote sealing

1. Sealed Stage A: `data/grixis/m6/owner_pass_c_substitute/Goro_Goro_and_Satoru/stage_a.md` and `stage_a.json`, hash receipts in `seal.json`.
2. Existing authored, full commander-first review: `data/grixis/m6/deep_reviews/Goro_Goro_and_Satoru.md` — actual last decision **KEEP**, original 100-copy audit 33 lands, 99 distinct names, 2 Island. It outlines 17 conditional A–Q source-paid interaction scenarios, not measured outcomes.
3. GrokBot `data/grixis/m6/grokbot_pass_c_advisory/Goro_Goro_and_Satoru.md` — advisory **KEEP**, zero proposed swaps, explicit previous pipeline involvement, lower-depth batch assessment, no new measured trial.
4. `data/grixis/m6/two_model_reconciliation/progress.json` row `tracker_index=20` and `KEEP_AGREEMENT_REGISTER_2026-10-20.md` row #21 — **documentary KEEP agreement only**, not a tested proof of local optimum. 62/62 reconciliation completion is unchanged.
5. Neutral current rules: [Wizards' March of the Machine release notes](https://magic.wizards.com/en/news/feature/march-of-the-machine-release-notes), [Wizards' Tarkir: Dragonstorm release notes (Frostcliff Siege)](https://magic.wizards.com/en/news/feature/tarkir-dragonstorm-release-notes), [Scryfall Bident of Thassa](https://scryfall.com/card/ths/42/bident-of-thassa), [Scryfall Bitterblossom](https://scryfall.com/card/mor/58/bitterblossom), [Breath of Fury Oracle/ruling](https://mtg.wtf/card?q=%21Breath+of+Fury). No fresh full 100-name legality sweep or empirical tests claimed.

## Agreements and genuine divergence

| Question | Original ChatGPT | GrokBot | Sealed JLK Stage A | Stage B judgment |
|---|---|---|---|---|
| Canon / identity | 100 copies; 33 lands; fresh evasive Ninjas and ephemeral hasty attackers make Dragons | Same approved list and ninjutsu principle | Same exact independently rehashed owner list | **AGREE**: no source conflict or identity concern |
| Goro grouping | Per player per damage-step; not per Ninja | Valid tapped-and-attacking Ninja | Explicit one-or-more, player/event and double-strike scenarios | **AGREE**; preserve distinction from multiple per-creature Bident draws |
| Haste timing | Goro activation snapshots; Samut/Tempest work on later tokens | Does not resolve this detail | Snapshot hazard plus Breath timing and opponent intervention | **AGREE**, with precision: Tempest provides haste as a new flying creature enters via its repeatable triggered ability, while Samut/Temur Siege continuously provide haste |
| Current deck optimization | **KEEP** after deep role audit; conditional token/haste alternatives considered | **KEEP** without individual cut contention | **NEEDS TESTING** `+Bitterblossom/-Bident of Thassa` | **REAL DISAGREEMENT**, not proof of upgrade: candidate adds recurrent flying fresh bodies but costs haste mana and removes very high-ceiling per-creature draws |
| Alternative cut | `-Frostcliff Siege` considered for token replacement, ultimately KEEP | None | `-Grazilaxx`, `-Waterbender Ascension` fallback, `-Bident` primary | **Retain protected role functions** until effect-aware comparison; Frostcliff is especially important on Temur mode |

**Newly sharpened correction to first-look risk identification:** The sealed first-look Stage A did not explicitly recognize the entire tactical value of *Frostcliff Siege's Temur mode*: for `{1}{U}{R}` it gives **all your creatures +1/+0, trample and haste continuously**, including Dragons created later during the turn. Its alternate **Jeskai mode** draws only **one card per damaged player per combat-damage event**, not a Bident card for every connecting creature. The 2025 Wizards Tarkir release notes confirm the Jeskai per-player grouping. Thus treating this modal enchantment as a disposable generic three-mana draw slot would undercount a native, critical extra-combat/Dragon haste redundancy. Its mode is locked on entry, however; it cannot function as both draw and team haste simultaneously. This strengthens the counterargument to replacing *any* utility engine with Bitterblossom. **Sealed Stage A remains unchanged.**

**Other retained details discovered in authored review:** Yuriko's commander ninjutsu from hand remains legal even though Goro commands this deck; Phoenix Chick may attack alone; three attackers are needed for its graveyard return; Raphael Sneak and Fire Navy Trebuchet create tapped-attacking entrants rather than declaration triggers. No new canonical illegality found. The prior author did not mention a Bitterblossom-versus-Bident measured trial; its absence is not negative experimental evidence.

## Narrow effect-aware opponent and resource traces — analytical only

**State A — one accessible flyer, Goro present, scarce mana.** Assume Bitterblossom is cast turn 2 and survives; a 1/1 Faerie appears on subsequent upkeep. To attack on its own creation turn, it needs `{1}{R}` *after* Goro is online or other actual haste. If tapped-out after paying UBR for Goro on turn 3, the fresh Faerie normally waits, and on turn 4 a blocker with flying or reach can still stop its Goro trigger. The extra creature can protect against a sweeper only if the enchantment survives. The paid two-mana haste requirement weakens the hypothesis that a two-mana enchantment gives a free immediate Dragon.

**State B — two or three evasive creatures hit one opponent.** Bident triggers independently for **each** creature's player combat damage (2–3 possible draws). Goro produces **one** Dragon for that player's current damage event even if several just-entered creatures hit. Frostcliff Siege/Jeskai yields **one** card for that opponent/event, and Grazilaxx similarly has a once-per-opponent-damaged ability. In a 33-land UBR deck drawing two to three cards can supply missing mana, countermagic and another combat piece; Bitterblossom does not replace that throughput. This is a deterministic rules/role comparison, not an observed hand statistic.

**State C — Breath of Fury attached to a fresh connector and Dragon enters.** Order the two player-damage triggers so Goro creates the Dragon before Breath resolves and sacrifices/reattaches. If Samut or Frostcliff Siege/Temur is active, a Dragon created later has haste for the extra combat; Dragon Tempest similarly grants haste to its new flying entrant; prior Goro `{1}{R}` activation alone does not. A removal spell killing the enchantment bearer before damage eliminates both trigger opportunities; kill haste source before the next attack and chain may stop. If there is no other legal Aura recipient after sacrifice, official 2005-10-01 Breath ruling says no untap/additional combat. These illustrate mechanic certainty, not a reliable infinite loop.

**State D — meaningful challenger comparison matrix (unmeasured).**

| Exact candidate list | Pros | Costs/negative cases | Gate |
|---|---|---|---|
| **Canonical KEEP** | Preserves Bident per-body draw, Grazilaxx shield, Waterbender evasion, Siege continuous-haste option; multiple existing fresh token sources | 33 lands; full engines are on-hit dependent; no Bitterblossom flyer each upkeep | Valid baseline |
| `+Bitterblossom / -Bident of Thassa` | Cheaper persistent flying fresh-entry generator; effective through some creature wipes | Loses per-body card engine, pays life and haste to attack, flyers can block | **UNPROVEN**; narrow paired trial only |
| `+Bitterblossom / -Grazilaxx, Illithid Scholar` | Preserves Bident card scaling | Sacrifices blocked-Ninja bounce/reentry and per-opponent card draws, relevant in clogged boards | Competing cut, also unproven |
| `+Bitterblossom / -Frostcliff Siege` | Three-to-two-mana recurring generator | **Costs modal continuous haste/trample** for post-hit Dragons, a critical Breath/Karlach chain enabler | Deprioritize unless conditional source-paid evidence reverses |

## Reconciliation and tests actually needed

- **No empirical game simulation, win-rate inference, Monte Carlo improvement estimate or new broad optimizer pass** was performed here. Existing deep review scenarios A–Q remain finite rules/board-state traces, not a measured local optimum.
- A targeted, seed-matched Phase B comparator may be warranted specifically for `-Bident/+Bitterblossom` and secondary `-Grazilaxx/+Bitterblossom`, not for all 62 generic slots: hold other 99 cards fixed, sample 33-land UBR access/turn-three commander, an open evasive opponent, flyer/reach creature walls, sweepers and removal, and measure turns 3–7 Dragons, net cards accessible, extra-combat initiations and failures, and life paid. A consistently negative result permits KEEP; statistically adequate upside plus preserved identity warrants owner-facing PROPOSE UPGRADE.
- Verify official current candidate legality and copy count before proposing a real locked-list change; candidate is hypothetical and legal conceptually, not approved or canonical. No unapproved swap, approval mark, M6 I/J certificate or Phase B completion is recorded.

**Controlled Stage B conclusion:** Existing reviewer agreement is real but of unequal depth (authored comprehensive versus GrokBot compact advisory). The sealed JLK has a specific **unresolved** challenger, while controlled comparison exposes a stronger KEEP reason from Bident's per-creature throughput and Frostcliff Siege's Temur haste. The correct record is **NEEDS TESTING — canonical KEEP pending evidence**, without forging a win-rate verdict. Reviewer provenance remains GPT-6, owner-equivalent formal Pass C only.
