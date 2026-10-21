# Josh-Lee-Kwai — Abaddon the Despoiler — formal owner-equivalent Pass C final disposition

**Tracker:** 0 / `Abaddon_the_Despoiler`  
**Date:** 2026-10-20 America/Chicago  
**Reviewer alias:** Josh-Lee-Kwai  
**Actual evaluator:** ChatGPT/OpenAI GPT-6  
**Review classification:** `FORMAL_PASS_C_OWNER_EQUIVALENT` (per Cory's 2026-10-20 owner waiver)  
**Technically independent third model:** `false`; `independence_requirement=OWNER_WAIVED_FOR_FORMAL_PASS_C`; same-model familiarity and bounded Stage A ledger leak disclosed.  
**Per-deck stage:** `FINAL` documentary A/seal/B/C, subject to exact-head integrity CI. **Disposition:** `NEEDS TESTING` for superiority of a plausible swap, **not** new owner approval or a blocker to evidence filing.

## Immutable authority and seal

- **Canonical repository/branch:** `corymstover/grixis-commander-encyclopediaGPT/main`, observed HEAD `ceffdcceec19e51fa01e3cbe01cca99da0558b07`.
- **Exact file:** `refinement/decklists/Abaddon_the_Despoiler_Approved_2026-10-13.txt`, Git blob `1bbead6e8a7973bd7eb1982147e917d39e217492`.
- **Canonical approved raw SHA-256:** `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`, rehashed from the live GitHub file and matched `state/current_deck_overrides.json`. Exactly **100 cards**, **94 unique names**, only Island/Mountain/Swamp repeated x3, **34 lands**, one Abaddon commander; UBR identity, **no project exception**.
- **Approval:** existing `APPROVED` / `LOCKED`, untouched.
- **First-stage Git commit:** `524d7dec1252cb9d78d6afe9b9f7ebde37775807` holding `stage_a.md` and `stage_a.json`; independent follow-on **seal commit** `3aa089798ad7949b0ee9eaca21c85e4f79650fec`. `stage_a.md` SHA-256 `99d529944d91f061d67eb10acbfe004bef65f992010c8f8d5ee820296510b665`; JSON SHA-256 `e4533ba69bb59192f89556c15ed2c8ed756aaa9eaaea2bfabbd1a2f42c83b060`. Git blob SHAs and canonical SHA are bound in separate `seal.json`.
- **Controlled comparison:** `stage_b_reconciliation.md` compares exact authored, GrokBot advisory, and two-model reconciliation source blobs after sealing, records both material agreement and dissent. Stage A is not rewritten.

## Commander-first final judgment

Abaddon is a five-mana on-turn, hand-cast cascade engine fueled by *total same-turn opponents' life lost*, not generic UBR goodstuff. Natural ceiling remains **optimized Bracket 4** as the existing corpus classified it (GrokBot advisory cites 14 Game Changers), with some fast-combo spikes but no demonstrated cEDH reliability. Preserve life-loss openers, printed cascade, zero-MV suspend hits, distinctive 40K cast-from-exile payoffs, protection and compact Breach/LED/Brain Freeze fallback. No forced bracket escalation.

The current 34-land, 19-source-tagged-ramp list has rich fixing and early bursts but five-mana commander exposure; optimistic land-source options (~22 U/23 B/21 R with seven flexibly counted fetches and conditional Orchard) are **not** measured turn-five access. High-impact weakness: resolved Rule of Law/Rest in Peace or analogous nonblue stax can be hard to answer once on the battlefield. Power and mana findings are source/strategic judgments, not empirical win rates.

## Key interaction: exact hypothetical swap

**Conditional research recommendation: +1 Aggravated Assault / -1 Rakdos, Lord of Riots.** No actual card change.

- **Rules-positive:** Assault ({2}{R}) gives an extra combat and main phase after paying {3}{R}{R} in a sorcery window. Existing **Neheb, the Eternal** generates red at each postcombat main from cumulative opponents' life loss that turn; with ≥5 actual aggregate loss it can repeatedly pay an Assault activation while Neheb survives. Existing **Loyal Subordinate**, with Abaddon controlled, drains 3 from each opponent at every beginning of combat—including Assault's extra combats without needing to attack. In a three-opponent example, regular combat causes nine aggregate loss, Neheb produces 9R, paying Assault's 3 and 5 leaves 1R, extra combat drains nine more, then next postcombat Neheb trigger yields 18R. Each event still uses appropriate priority/response windows. At exactly five opponent loss per iteration this is zero-net-red extra phases, not automatically infinite mana or lethal. No unmodeled free resource is assumed. Official relevant source: Wizards' Commander Masters release notes for Neheb and official cascade rules.
- **Identity-positive:** turns existing damage/drain and postcombat red into a concrete extra-combat/endgame line, and Assault can gain Abaddon's hand-cast cascade once threshold ≥3. It does not replace the Warhammer engine with unrelated Grixis staples.
- **Burden/weakness:** Neheb (5 MV), Assault (3 MV), Loyal Subordinate and Abaddon must be available through removal, counterspells, timing and mana restrictions. With no Neheb or combat payoff, Assault is low-tempo. Rakdos is a real flying/trampling threat and discounts creature casts after opponent loss, despite demanding {B}{B}{R}{R} and often discounting the wrong spell types. Valid combo ≠ proven net deck improvement.

**Reason for Stage C `NEEDS TESTING` rather than automatic `PROPOSE UPGRADE`:** the original ChatGPT deep review and reconciliation already favor the exact pair; Stage A's agreement is partially contaminated by prior progress-ledger exposure, so it is not a third independent confirmation. The added payoff is real, but no matched effect-aware comparison has quantified setup frequency, losses in ordinary hands or recovery when key pieces are removed. Earlier author certainty can justify owner *consideration*, not an unqualified local zero-improvement or superiority certificate. Targeted Phase B is warranted under Cory's testing directive.

### Other disputes and disposition

1. `+Slaughter Pact/-Blasphemous Act`: **reject exact swap**; removes board wipe, adds conditional target and potentially dangerous upkeep payment; MV0 cascade hit can be uncastable.
2. `+Wheel of Fate/-Rakdos`: **not preferred**; another MV0 wheel benefits opponents and overlaps Wheel of Fortune/Windfall; Assault offers more unique function.
3. `+Lotus Bloom/-Nightscape Familiar`: **needs bounded timing/cascade testing**, especially three-upkeep suspend liability versus Familiar's repeatable cost reduction and commander casting.
4. `+Chaos Warp/-Kessig Flamebreather`: **reject this cut**; protect fast all-opponent pinger. Resolved nonblue permanent-answer gap is valid; examine Warp versus a slower peripheral payoff such as Ruinous Powers only under stax-heavy evidence.
5. `+Guttersnipe/-Rakdos`: **hold as comparator**, on-identity threshold engine but partly redundant with cheaper Flamebreather/Thermo, vulnerable to removal and depends on spells first.
6. `Orcish Bowmasters`, `Grinning Ignus` etc.: no verified exact superior cut; documented research, not new recommendations.

## Current verified scope and limitations

- Prior canonical 94-name Scryfall/Commander official legality gate (October 13/16) and GrokBot's October 20 spot refresh are documentary evidence. On October 20 current Wizards Commander banned list and original WotC cascade/Neheb notes were consulted. **This reviewer did not independently refetch every 2026-10-20 Oracle entry or run a new live Scryfall full-deck test**; card pages returned 403, and proposed candidates need current per-card receipts before approval. No Abaddon exception implicated.
- Cascade grants only hand-cast on-turn spells under current loss threshold. Exile casts feed Passionate Archaeologist, Nalfeshnee, Keeper and Wild-Magic Sorcerer conditionally, but are not re-cascaded by Abaddon merely for being cast. Storm copies are not cast. Drannith/Rule of Law impede cascade; Grafdigger's Cage does not prevent cascade from exile, though it stops graveyard casting. Neheb's postcombat trigger uses the stack and opponents may answer.
- **No new empirical gameplay tests**, matched hands, turn-to-win distribution, realistic opponent AI model or measured win-rate delta were generated. Existing inconclusive Aurora Phoenix vs Mind's Desire Forge experiment did not cast either challenger; generic M5 proxy `PASS` cannot stand in for Assault effect awareness. No fabricated performance claims.

## Risk-based testing queue, prerequisites and owner gates

**Highest priority:** test exact baseline vs `Aggravated Assault/Rakdos` (and `Guttersnipe/Rakdos` as second comparator), with whole-list hashes; track Neheb phases/mana, Loyal Subordinate drain and lieutenant resolution, Abaddon granted cascade, commander removal, Rule of Law, fogs, stax and interruption. Record precise effect coverage: if simulator cannot model these, use bounded scripted rules traces and report unresolved advantage instead of counterfeit metrics.

**Secondary:** Lotus Bloom/Familiar timing and same-seed opening-hand/cascade distribution; Chaos Warp against a meaningful slow cut and explicit resolved-stax scenarios, if that matchup is decision-changing.

Before any owner-facing M7 swap packet: live current Oracle and legality for all changed names, specific opponent interaction review, legal 100-card recount, color/singleton verification, variant SHA-256 and concrete test limitations. **Cory's explicit approval remains mandatory.** Existing locked deck remains exactly unchanged until then. No Phase B complete label, I zero-improvement, J final reproducibility bundle, M6/M7 acceptance or M8 export certificate is granted by this document.

**Formal Pass C evidence claim:** this deck is eligible to count as **one owner-authorized formal Pass C equivalent only after the exact-head evidence checks and merge**. `technically_independent=false`, actual third-model execution count remains zero. Only a documented owner governance waiver supports the formal classification; evidence scrutiny and downstream milestones remain separate.
