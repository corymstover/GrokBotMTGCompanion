# Josh-Lee-Kwai Pass C #28 — Stage B controlled unblinding (Loki)

**Date:** 2026-10-21. **Canonical hash:** `5079291c08c5af212b3d90d63ac5b01849d45c7700b1d64100ef57fb13458062`, APPROVED/LOCKED unchanged. This document was created only **after** Stage A first Git commit `e1bfef564b035e0b7ae5c0428bd5894d9c3d3a4d` and separately committed neutral cryptographic seal `4fe0db7d5898c8fa3fa4d9bf330c59df054ba9b5`. Reviewer is still ChatGPT GPT-6 under owner's formal-equivalence waiver, not an independent technical model.

## Evidence unblinded

- [Prior complete ChatGPT M6 single-deck review](https://github.com/corymstover/GrokBotMTGCompanion/blob/chatgpt-cycle76-m6-refinement/data/grixis/m6/deep_reviews/Loki__the_Deceiver.md), October 19, entire 95-row/100-card audit, 16 manual play-state traces, 386 **screening** candidates (0 Pass B).
- [GrokBot advisory](https://github.com/corymstover/GrokBotMTGCompanion/blob/chatgpt-cycle76-m6-refinement/data/grixis/m6/grokbot_pass_c_advisory/Loki__the_Deceiver.md), October 20, 100-card Scryfall collection check, short **KEEP**, low-confidence, prior engineering involvement; not technically independent Pass C.
- [Two-model reconciliation ledger](https://github.com/corymstover/GrokBotMTGCompanion/blob/chatgpt-cycle76-m6-refinement/data/grixis/m6/two_model_reconciliation/progress.json), tracker index 27, source-exact `KEEP` **documentary agreement only**, and [agreement register](https://github.com/corymstover/GrokBotMTGCompanion/blob/chatgpt-cycle76-m6-refinement/data/grixis/m6/two_model_reconciliation/KEEP_AGREEMENT_REGISTER_2026-10-20.md).
- Canonical owner SHA records, neutral WotC Marvel/Doctor Who release notes, official Commander bans, [current official Commander Brackets page](https://magic.wizards.com/en/formats/commander). No new full current 100-name Scryfall API call or opponent simulation.

## Results against sealed Stage A

| Issue | Stage A independently documented | Historical evaluation | Post-seal disposition |
|---|---|---|---|
| Commander mechanics | Declared attack vs enters attacking, delayed sacrifice, draw once per damaged player | Author explicitly verified same with 16 manual states; Grok notes no fresh attack trigger | **RULE AGREEMENT**. Reuse author WotC-backed traces, no need rerun whole deck |
| Core engine | Loki+Villain ETB/combat, Master and end-step Sundial, tribal protections | Full author exactly agrees | **STRONG COMMANDER IDENTITY**; never force unrelated combo shell |
| Mana/count | 100 physical, 95 names, 34 land with 8 basics, UBR | Both source checks agree, Grok October 20 Scryfall collection supports legality | **AGREEMENT**; retain canonical approval, distinguish historic gate from present recrawl |
| Sundial timing | Must end turn while sacrifice trigger on stack | Full author documents same | **RESOLVED RULES**, with opponent response/removal caveats |
| Scepter and token typing | Temporary Villain type on stolen source not copied if not copiable | Full author explicitly catches | **RESOLVED RULES** |
| Token death / recursion | Thunderbolts does not revive token that ceases to exist | Full author and WotC token principles compatible | **RESOLVED RULES**, no fake revival loop |
| Strionic Resonator | **Add Strionic, cut Swiftfoot Boots**, provisional NEEDS TESTING | Full author considered Strionic but with **different cuts** Loki Lord of Misrule / Squadron Sinister; recommended KEEP because two mana per activation + board setup; Grok never assessed Resonator | **NARROW NOVEL COMPARISON**. The precise *Boots-cut* trade-off remained untested, but protection risk makes upgrade far from established |
| Other credible alternatives | Shared Animosity/Helm; no firm upgrade | Full author elevates **Seize the Day / Black Market Connections** extra-combat hypothesis, also Aggravated Assault/Kang Prime; no tested superiority. Grok rejects Hostage Taker/Stilt-Man (non-Villain) | **TARGETED TEST LIST** should prioritize source-paid extra combat vs independent value; retain KEEP control |
| Low-value slots | Sundial/Boots/Hall expensive or conditional but identity-relevant | Author singles generic Black Market Connections, slow Soul Stone and some high curve; Grok singles Stilt-Man and symmetric Blasphemous Act | **DIFFERENT WEAKNESS HYPOTHESES**. None independently proven inferior under protected Loki attack states |
| Final disposition | Stage A NEEDS TESTING | Author KEEP; Grok KEEP; reconciliation documentary KEEP | **SUBSTANTIVE JUDGMENT DIFFERENCE**, not a legality failure and not owner-approved swap |

## Bracket disagreement — correct the advisory label without pretending a new deck is weaker

GrokBot's short advisory calls Loki **Bracket 3** and simultaneously says it contains **five Game Changers**. Wizards' current [Commander format page](https://magic.wizards.com/en/formats/commander) explicitly caps Bracket 3 at **three** Game Changers; Brackets 4/5 allow unlimited. **If GrokBot's five-card count is correct, its B3 assignment cannot satisfy official B3 deckbuilding boundaries.** The original whole-deck author, October 14 approved state and sealed Stage A all place the optimized combat/Villain build in **Bracket 4**. Retain **B4 — Optimized** provisionally; do not reinterpret "B3" as a lawful category from the advisory. The exact current five Game Changer names must be checked by the eventual final M6 source sweep before claiming independently verified GC count; this corrects an internal inconsistency, not a canonical legality defect.

## New targeted comparison and strongest objection

**Strionic Resonator versus Swiftfoot Boots:** The full author did evaluate Resonator, but against different, intrinsic six-mana board/copy payoff cuts. Stage A's second protective equipment cut is the novel variable; tests must compare paired protected-Loki attack windows with and without Boots and actual {2} generic mana open after declaring Loki's attack. Resonator creates a second copied **trigger**, potentially choosing a new legal Villain, but does not retroactively trigger any entering-attacking creature's attack ability. The alternative setup has no hexproof/haste from Boots; if Greaves is absent and Loki is removed before a first attack, the bonus trigger never exists. This is a real risk, not a slam-dunk new card.

**Seize the Day versus Black Market Connections:** the earlier author identified a more direct commander-trigger multiplier. The two-combat line only works if Loki can attack both times: in postcombat main, Seize untaps its target and adds a combat, letting Loki be declared again after it survives first combat. It also gives up value/treasure/Changeling access of Connections. Full author supplied a manual paid line but no measured matchup result. This should be a **higher-priority Phase B test** than speculative Resonator if test capacity is scarce. The Stage A proposition is retained as recorded, not rewritten to claim independent discovery of Seize.

**Metagame and opposing responses:** instant removal before declared attack; removal of Loki target before copy trigger resolves; board wiping; enchantment removal of Cover; artifact removal of Resonator/Boots/Sundial; remove Master before delayed sacrifice; prevent combat damage. Both candidate lines require a functioning Loki+Villain target and are especially fragile into cheap targeted removal, while defensive Boots and Connections protect/rebuild a broken position.

## Post-seal observations and limitations

- The sealed Stage A properly identified Loki token **sacrifice**; it did not rely on incomplete card text on some secondary index snippets. The prior full authored manual rules cases independently agree.
- Existing `Roaming Throne` (name Villain) already doubles applicable Loki creature triggers, limiting marginal need for Resonator, while not doubling Kindred Discovery's enchantment trigger.
- Existing `Sundial` and six-mana Master cover different protection cost/time windows; proposals cutting both are not acceptable without durable replacement.
- The prior author explicitly observed the `Seize the Day` candidate, so any claim that this second-stage review *discovered* it would be false.
- Grok's Norman/Goben same-Oracle-ID caveat is retained as a source-specific alias record, not new illegality. The exact canonical name remains `Norman Osborn // Green Goblin`.
- A source-backed manual trace is **not** a sampled effect-aware Phase B run. No zero-improvement I certificate, J reproducibility bundle, fresh whole-list Oracle sweep, new owner swap or milestone acceptance has occurred.

**Controlled conclusion:** Formal review evidence can close as `NEEDS TESTING`: test exact add/cut lines **Strionic Resonator / Swiftfoot Boots** and **Seize the Day / Black Market Connections** against KEEP with source-paid combat/response and mana availability; test whether each actually preserves Loki's distinctive combat-copy plan. No card has been changed. Clean prior agreement is still useful supporting documentation but does not remove this targeted decision-grade test gap.

