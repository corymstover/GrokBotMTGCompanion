# GrokBot ADVISORY Pass C — Stage B (post-seal reconciliation) — #1 Abaddon_the_Despoiler

**ADVISORY — not qualified Pass C.** Stage A was sealed in pushed commit `465e3371d1195549a865693dfce6a4607b7b970c` and has not been revised. Every change of mind is recorded here.

Read after the seal: `data/grixis/m6/deep_reviews/Abaddon_the_Despoiler.md` (blob bcda3955). Scryfall Oracle was checked for Aggravated Assault. The M5 packet was not opened: the deep review summarises it, and the cost limit applies.

## Material agreements
- **Mechanics.** Both reviews read Abaddon the same way: hand casts only, your turn only, X summed over all opponents, separate triggers for printed and granted cascade, and suspend MV-0 cards as premium hits. Both rate the deck Bracket 4 (Optimized), short of cEDH consistency.
- **Rakdos, Lord of Riots** is the most contestable slot (my Stage A #3 cut). Same reasons: BBRR cost, discounts creatures only.
- **Gap.** Both find no hard answer to resolved nonblue artifacts and enchantments. Both flag Rest in Peace, Drannith Magistrate and Rule of Law as the worst stax. Both keep Chaos Warp as a meta-dependent HOLD rather than cutting Pyroblast.
- **KEEP list matches:** the Breach/LED/Brain Freeze package, the free counters, Bloodletter/Solphim, the exile payoffs, and Mind's Desire over Aurora Phoenix.

## Material disagreements and corrections
1. **The author found a line I missed, and I accept it (my error).** Neheb, the Eternal + Aggravated Assault ({2}{R}; {3}{R}{R}: untap, extra combat, extra main, sorcery speed). Once opponents have lost ≥5 life, each extra postcombat main gives Neheb's cumulative red mana, which pays for the next activation. That means unbounded combats [F, traced from Oracle]. Loyal Subordinate drains 9 at each combat, so the kill is deterministic as long as Neheb, Loyal Subordinate and Abaddon stay on board. The deck already plays Neheb, Loyal Subordinate and the life-loss enablers, so this is a cheap, on-identity second compact win. **I agree: IN Aggravated Assault / OUT Rakdos, Lord of Riots** (moderate-high). This replaces my Stage A #3, Wheel of Fate for Rakdos.
2. **Factual error in the deep review.** It lists *Call Forth the Tempest* as **MV 11**, with the granted cascade needing X≥11. Current Oracle says {5}{R}{R}{R} = **MV 8** [M]. The triple cascade therefore turns on at X≥8: easier than the author thought, and it strengthens the card's identity KEEP.
3. **Blasphemous Act.** The author says KEEP; I still say **swap for Slaughter Pact** [J, moderate]. Blasphemous is symmetric and kills the deck's own engine creatures. It also kills Neheb and Loyal Subordinate, which makes it worse once Assault is in. The deck already has two one-sided sweepers. Slaughter Pact is instant and one-sided, kills Drannith Magistrate, and is an MV-0 cascade hit. Counterargument I accept: it loses the reset button against a huge or black creature board. That makes the swap test-gated, not certain.
4. **The MV-0 cascade pool is an opportunity the author did not consider.** The author has no entry for Lotus Bloom, Slaughter Pact, Wheel of Fate or Mox Tantalite. Every MV-1 hand cast with Abaddon out finds one of the 7 MV-0 cards, and only 3 of those are premium [M]. **Lotus Bloom / Nightscape Familiar** (moderate) stands. The author keeps Familiar mainly for a hypothetical Birgi + Grinning Ignus loop, but Ignus is not in the 99, so that defence does not apply to the current list.
5. **Breach kill timing: I was partly wrong.** The author points out that after the mill, an escaped Wheel of Fortune makes opponents draw from empty libraries, so they lose right away to state-based actions. My "not immediate" caveat applies only when Wheel is already exiled or unavailable.
6. **Kessig Flamebreather / Chaos Warp:** I withdraw this Stage A #4 swap. Kessig doubles as a Breach-loop pinger, and the author's engine protection is reasonable. Chaos Warp stays HOLD with no named cut.
7. **Mystic Remora / Stormfist Crusader:** no position. My Stage A was exposed to this pair, so any view I gave would not be independent.

## Final advisory recommendation (for Cory; nothing applied)
| Rank | IN | OUT | Confidence | One-line evidence |
|---|---|---|---|---|
| 1 | Aggravated Assault | Rakdos, Lord of Riots | moderate-high | A deterministic Neheb + Assault + Loyal Subordinate combat loop from cards already in the deck, replacing a narrow creature reducer. (This agrees with the author.) |
| 2 | Lotus Bloom | Nightscape Familiar | moderate | Turns MV-1 cascades into +3 mana. Familiar's only special defence relies on a card that isn't in the list. |
| 3 | Slaughter Pact | Blasphemous Act | moderate (test-gated) | One-sided instant removal and an MV-0 hit, replacing a symmetric wipe that kills Neheb, Loyal Subordinate and Abaddon. |
| 4 | Wheel of Fate | Keeper of Secrets | low | A free refill off MV-1 cascades, replacing a 6-MV payoff that duplicates Archaeologist. Speculative. |
Everything else: KEEP. Chaos Warp: HOLD (meta-dependent).

## Effect-aware testing required before any swap beyond #1
- (a) Exact enumeration of the MV-1 and MV-5 cascade hit distributions, baseline vs. #2–#4. Deterministic and cheap.
- (b) Multiplayer scenarios with an opposing Drannith Magistrate, Rest in Peace, or a wide/black creature board, Slaughter Pact vs. Blasphemous Act.
- (c) Turn-to-Abaddon/Neheb sequencing, Lotus Bloom vs. Nightscape Familiar.
- (d) For #1: confirm Neheb's trigger in each additional main phase and the Loyal Subordinate drain against removal and prevention responses. The rules trace is already source-backed. This step is a resilience check, not a legality check.

Goldfish passes don't qualify. **Evidence blocker for formal Pass C:** reviewer independence. GrokBot is disqualified, so this deck stays at formal Pass C 0.
