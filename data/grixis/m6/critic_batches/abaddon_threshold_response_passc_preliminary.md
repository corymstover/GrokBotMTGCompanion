# Cycle 93 — Abaddon commander-first Pass C preliminary disposition: Heartless / Tree

**Reviewer:** ChatGPT, named agent, 2026-10-17. **Status:** substantive **preliminary** Pass C critique, not a final Pass C judgment or complete Phase-B; no swap, lock or acceptance authority.

**Canonical deck:** Abaddon the Despoiler, `lh1:5a1e5e5bb86ba35d7dbf712fbc3a7d29c3e05a17569c05e8a11976321699b793`. The full 100-card approved list and five required blueprint packages remain canonical.

**Grounding:** frozen accepted M5 review packet (Heartless IDs `d17609747acc`/`5ac285a18b7a`; Tree IDs `f2e3f08ecb7d`/`ba42cedcaa2f`); commander-first Abaddon blueprint; [Cycle 92 600-sample paired mana-only report](../phase_b_bounded/abaddon_threshold_access_01.json); [Cycle 93 29-case adversarial interaction grid](../phase_b_bounded/abaddon_interaction_grid_01.json); current Oracle/rules references below.

## Exact mechanical differences / immediate caution

**Heartless Hidetsugu** ({3}{R}{R}, {T}): floor(half) damage to *every player*. After it has legally activated, removing Heartless itself does **not** stop the ability; the damage source's last known information governs as needed (CR 113.7a). By contrast, destroying **Solphim** while the ability is on the stack removes its doubling replacement, and similarly removing Bloodletter removes its life-loss doubling. Damage prevention can nullify a target's loss without preventing Heartless's damage to its controller.

At opponents 40/39/31, pilot 40: ordinary Heartless activation deals 20/19/15 opponent damage and 20 to pilot; with Solphim still on battlefield, it deals 40/38/30 to opponents but still 20 to pilot. With both Solphim and Bloodletter active on the pilot's turn, the 40/39/31 opponents can all lose enough life to be eliminated (80/76/60), but this is a **multi-piece board state**, not a consistent one-card Abaddon cascade engine, and may win independent of Abaddon. If all opponents leave the game, a subsequent cascade spell is moot.

**Tree of Perdition** ({3}{B}, 0/13, {T}): conditional, **one-target** life exchange, not damage. On resolution with a legal 40-life opponent and unchanged toughness 13, opponent loses 27 life. Solphim **does not modify this loss**; Bloodletter can double the life loss on your turn. **Distinct from Heartless**, if Tree leaves before the exchange ability resolves, Wizards' explicit Eldritch Moon ruling says the exchange has no effect, even though the activated ability itself exists independently on the stack. Opponents at 13 life or less do not lose life to an unmodified Tree: an 8-life target gains five.

**Timing:** Without haste, neither creature can activate a tap ability on its controller's entry turn. In ordinary own-turn casting, Tree at four mana cannot activate until a subsequent turn; Heartless at five mana cannot activate until a subsequent turn. This substantially weakens immediate pre-cascade usefulness compared with **Kessig Flamebreather**, whose damage triggers during a noncreature spell chain, or **Birgi**, whose mana trigger occurs while casting spells. The approved list lacks a dedicated, general haste support package for these newcomers. Any new follow-up spell must be **cast from hand during your turn** with Abaddon already present and still have enough colored mana; producing a large life-loss X alone does not pay the follow-up spell's costs.

## Six tested swap hypotheses — provisional reviewer disposition

| Add → cut | Detailed reason | Preliminary verdict |
|---|---|---|
| **Heartless → Birgi // Harnfel** | Five-mana delayed tap threatens a spectacular board but replaces Birgi's mana-on-spell cast and Harnfel access. M3 v1.1 omitted **both** effect packages. Commander-first chain efficiency cost not measured. | **Disfavor; no approval** |
| **Heartless → Kessig Flamebreather** | Replaces two-mana repeatable tablewide damage that accumulates X as noncreature spells are cast with a delayed five-mana threat that also hits pilot. | **Preliminary reject this CUT**, independent of whether Heartless merits a different slot |
| **Heartless → Bituminous Blast** | Alternative cut retains cheap threshold and Birgi engine, preserving 8/9 threshold blueprint cards. But sacrifices a five-mana printed-cascade removal spell and drops the printed-cascade package from 5 to its minimum of 4. This is only one plausible lower-cost role tradeoff. | **Hold: top Heartless counterfactual for *true* Phase-B**, not recommendation |
| **Tree → Birgi // Harnfel** | Four-mana body survives to next turn and then targets one opponent. Birgi's chain mana access is lost for a threshold event that may arrive too late. | **Disfavor; no approval** |
| **Tree → Kessig Flamebreather** | Loses immediate recurring threshold to a removal-sensitive one-target activation. Tree can fail on resolution if removed, unlike Heartless. | **Preliminary reject this CUT** |
| **Tree → Bituminous Blast** | Preserves cheap threshold and Birgi, but drops printed-cascade to blueprint minimum and loses interaction. A 27-life threshold can be powerful yet often more X than needed, while lacking stack interaction or commander follow-through. | **Hold, lower priority than Heartless alternate cut** |

**Mana-only comparison:** In 600 preregistered paired v1.1 trials for each of the six, the modeled change in Abaddon-cast-by-turn-four lies between **−0.50 and +0.33 percentage points**; no paired estimate establishes an improvement. Crucially, the model omits the added active abilities **and** Birgi/Kessig/Bituminous Blast effects. Different pair-specific baseline fractions are not independent across-swap rankings.

## Exact sources / verified legality scope

- [Wizards: Eldritch Moon release notes](https://magic.wizards.com/en/news/feature/eldritch-moon-release-notes-2016-07-08) — Tree removal-before-exchange, life-loss/gain exchange semantics.
- [Comprehensive Rules 113.7a](https://mtg.wtf/help/rules#113.7a) — activated ability independent of removed source, including last known source information.
- [Wizards: Lost Caverns of Ixalan release notes](https://magic.wizards.com/en/news/feature/the-lost-caverns-of-ixalan-release-notes) — Bloodletter changes life loss, not damage amount.
- [Heartless Hidetsugu](https://mtg.wtf/card/cmm/539/Heartless-Hidetsugu), [Tree of Perdition](https://mtg.wtf/card/emn/109/Tree-of-Perdition), [Abaddon](https://mtg.wtf/card/40k/171/Abaddon-the-Despoiler) — current displayed Oracle and Commander-legal status as consulted Oct 17. These checks cover the *proposed added* cards and commander; every remaining card in a promoted 100 must still pass the project's final independent legality audit.

## Unclosed formal gates

1. **Deckwide effect-aware paired** multiplayer/interaction evidence is still absent. Bounded 29-case calculations verify conditional rules consequences only; they do not supply opponent-response frequencies, turn-based hand availability, color constraints or actual victory probability.
2. **Cost/tempo and alternative cut:** Heartless vs Bituminous Blast needs real effects for the removed printed-cascade removal, not just castability. The proposed six swaps are not eligible to enter approved-deck authority.
3. **Combo/rules review:** If Heartless+Solphim+Bloodletter is claimed to win, verify priority, prevention, life totals, state-based actions and opponents alive; do not conflate an assembled three-permanent elimination line with an Abaddon cascade threshold upgrade.
4. **Named Pass C completion and I/J** remain pending. This note records limited review, not certified `judgment_review`, tested-pool I certificate, or complete J reproducibility bundle.
5. **User authority:** no new swap, approval, lock, decklist promotion, or unauthorized exception permitted.

**Recommendation for the next experimental step (not a deck recommendation):** constrain further investigation to Heartless Hidetsugu versus the printed-cascade/interaction slot, with reliable turn-of-activation and surviving-board estimates, plus Tree versus the same slot as a lower-priority control. Retain Kessig and Birgi until an actual full-effect comparator demonstrates that removing either improves the commander-first deck.
