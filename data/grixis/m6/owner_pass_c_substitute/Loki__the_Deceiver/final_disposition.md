# Josh-Lee-Kwai formal Pass C #28 — Loki final disposition

**Final:** `NEEDS TESTING` on exact approved Loki 100; the canonical deck remains **APPROVED and LOCKED**. Evidence is a completed **FORMAL_PASS_C_OWNER_EQUIVALENT** review only after exact-head CI succeeds and merges; not a completed Phase B, I/J, M6, M7 or M8 acceptance.

## Source integrity, strict stage separation

- Canonical repository: `corymstover/grixis-commander-encyclopediaGPT@main`; owner lock `state/current_deck_overrides.json`.
- Approved source: `refinement/decklists/Loki_the_Deceiver_Approved_2026-10-14.txt`; blob `456d62d45e6e5ffb283a97b5603997a4d1d74c3e`; independently reproduced raw SHA-256 **`5079291c08c5af212b3d90d63ac5b01849d45c7700b1d64100ef57fb13458062`**.
- 100 cards = Loki commander + 99 library; 95 distinct names with only 3 Island, 3 Swamp and 2 Mountain repeated. 34 lands including eight basics. UBR identity. No special legal project exception for Loki.
- Neutral Stage A initial Git commit **`e1bfef564b035e0b7ae5c0428bd5894d9c3d3a4d`**; separate SHA-256 `seal.json` commit **`4fe0db7d5898c8fa3fa4d9bf330c59df054ba9b5`**. Stage A MD digest `2b9a529246254a9e39a5ee4c5ae155e2ddcaf0b78e3891c2708be6aad6bfff71`; JSON digest `66aa304fa81b201b92bae7e6cbc85a61146362ef0a5cbbaa37b22510869ead3d`. No previous Loki evaluations were opened before that seal; model lineage familiarity remains an unavoidable disclosure.
- [Stage B controlled comparison](stage_b_reconciliation.md) cites original full ChatGPT review, GrokBot advisory, 62/62 documentary reconciliation, current primary WotC release notes/bracket framework. The first-stage records remain immutable.

## Commander-first conclusion

Loki is a 4-mana UBR Villain that must be **declared attacking** and have another Villain target. On its attack it produces a tapped-and-attacking, nonlegendary Illusion token that copies the other target's copiable characteristics, with an obligatory **next-end-step sacrifice** unless protected by the relevant rule effect. Its combat draw is once per player struck by one or more Villains, not once per Villain. The deck's natural focus is **Villain typal attack pressure, ETB/copy value and token preservation**, with the capacity to draw and grind via Kindred Discovery, Titan, Tombstone, Prowler, Kangs, Mysterio, Stilt-Man, Red Ghost and tribal support. It is **Bracket 4 — Optimized** by natural power ceiling and the previously approved classification, without demonstrated cEDH-speed determinism. Preserve this identity, not a generic Grixis combo substitution.

## Verified material rules and adversarial windows

1. **Attack/copy distinction:** Loki's token was not declared as an attacker. ETB, as-enters and later combat-damage triggers work; ordinary `whenever this attacks` on the copied token does not trigger immediately. Opponent may remove the target after Loki triggers but before resolution; if no legal target remains, the copy fails.
2. **Next-end-step sacrifice:** Wizards' full Loki text includes the sacrifice clause. `The Master, Multiplied` prohibits sacrifice/exile of your creature tokens caused by controlled triggered abilities while Master remains. `Sundial of the Infinite` must end the turn **with the sacrifice trigger on stack**; activating early merely risks deferring it. Remove Master before trigger resolution and the saved-copy assumption fails.
3. **Copying Villains:** `Loki's Scepter` can temporarily make an enemy creature a legal target, but this temporary type change normally isn't copied into the new token; the clone may be only an Illusion and its printed types. `Kindred Discovery` draws on arriving Villain copy **and** original declared attack, not on new token's non-declared attack; `Titan of Littjara` copied token can choose Villain on entry and trigger its ETB draw. `Roaming Throne` naming Villain doubles Loki creature triggers, not the enchantment's own triggers.
4. **Loss and recursion:** `Thunderbolts Conspiracy` can recur eligible nontoken Villains, not a token after it ceases to exist. `Venom, Eddie Brock` may care about a copy dying, whereas preserving it prevents death payoff; this is an actual branch decision, not simultaneously both values.
5. **Mana/opposition:** 34 land access includes conditional tapped fixing and specialty restricted Villainous Hideout. Four mana for Loki plus another Villain and protected access to combat remains a real dependency. Opponent can kill Loki before declaration, kill target after trigger, stop damage, wipe or remove preservation pieces.
6. **Official-vs-project legality:** Wizards Marvel MSC cards are Commander-legal on release, no list card was newly detected on WotC Commander bans; the existing October 14 whole-list approval gate and GrokBot October 20 Scryfall card collection check historically report legal/correct UBR. This Pass C did **not** execute a fresh all-100 Oracle/API query. No new exception or blocker is claimed.
7. **Bracket consistency:** Grok's advisory says Bracket 3 despite self-reporting five Game Changers. Wizards' [current Commander format page](https://magic.wizards.com/en/formats/commander) caps B3 at three, so that juxtaposition is internally inconsistent; the full author, approved source and this Pass C agree on **B4**. Exact current five GC identities still deserve a final source check before a new independently verified count claim.

## Prior consensus versus current unresolved challenger

Original detailed author **KEEP**, GrokBot low-confidence advisory **KEEP**, reconciliation **documentary KEEP/KEEP**. Sealed neutral Pass C **NEEDS TESTING**—first on **add Strionic Resonator / cut Swiftfoot Boots**, a different candidate cut than original author tested in text. Extra Loki-trigger copies are attractive, but casting/deploying Resonator and paying {2} in combat may be slower than protecting Loki through a haste/hexproof item; the remaining Greaves are not always available. `Roaming Throne` already supplies trigger amplification.

Controlled Stage B also identifies the author's previously disclosed potentially stronger commander-native challenger, **add Seize the Day / cut Black Market Connections**. A 3R postcombat extra-combat spell may enable a second declared Loki attack if it survives/untaps, but replaces Connections' cards/Treasures/Changeling and fails through removal/no available target. This is **not** claimed as a newly blind-discovered swap. Keep the original 100 as the baseline; do not automatically swap either line.

**Prioritize after Pass C:**
1. Run source-paid, effect-aware *paired* baseline/Strionic+Boots cut/Seize+Connections cut scenarios with Loki present/not present, another Villain valid/invalid, haste/protection, combat 1 and 2 payability, opponent response windows, and delayed token-sacrifice.
2. Compare the already documented manual state traces to actual source-bound test receipts, with opening/mulligan policy, cost/effect legality, relevant board/priority state, reproduction seeds and observed outcomes; avoid calling manually argued branches win-rate simulations.
3. Test alternatives only if they materially improve: attack/copy trigger doubles versus protected deployment, Stilt-Man damage-theft tempo, sweep recovery, source availability. Preserve a valid tested `KEEP` outcome.
4. If any exact swap clears decision gates, present it to **Cory** for explicit approval before canonical mutation and complete new 100-card/relevant Oracle/legality/hashing audit. No such approval exists.

## Provenance and accounting

- **Reviewer alias:** Josh-Lee-Kwai; **actual evaluator:** ChatGPT/OpenAI GPT-6.
- **Formal class:** `FORMAL_PASS_C_OWNER_EQUIVALENT`, technical model independence **false**, criterion `OWNER_WAIVED_FOR_FORMAL_PASS_C` by Cory October 20.
- **First-stage carryover:** prior memories possible but excluded previous Loki report file contents until separate neutral seal. Stage A not altered post-unblinding.
- **Formal status:** Stage A/B/C documented, subject to exact-head CI and merge; **NEEDS TESTING**. **No canonical edits**, **no owner-approved new swap**, **no certified effect-aware Phase B**, **no I/J/M6/M7/M8 acceptance**.
- **Ledger:** advance one deck only via a separate ledger PR after this full evidence passes exact-head CI and merges. Follow tracker order, next Lord_of_Tresserhorn (unless live tracker says otherwise).

**Final judgment:** Strong and identity-faithful optimized Loki build, with important timing rules already correctly represented in the full author record. No proposed card is yet evidenced superior; targeted additional-combat and trigger-doubling-versus-protection tests remain the consequential unresolved work.

