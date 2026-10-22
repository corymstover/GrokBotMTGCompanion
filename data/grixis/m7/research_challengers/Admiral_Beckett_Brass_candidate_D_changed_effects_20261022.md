# Admiral Beckett Brass M7 Pirate-density D — changed-effect timing proof

**RESEARCH_ONLY, 2026-10-22; no final approval/certification.** Target exact D 100-card research SHA-256 `201a1d5fc90e30d6aff9a565603fcf8caef69604dad2c07b4951be2b41cc92ee`, canonical approved baseline `4ba5c483eb67b5f2647d375450adf9c2b7e79a036d0ba1866e58de8441bf3414`. Current full Oct22 Scryfall snapshot includes all involved names and 121/121 Commander-legal UBR identities. This is a targeted changed-effects addendum, not a repeated Pass C review or large simulated gameplay study.

## Commander-specific synergy established by exact Oracle reasoning

**Skyship Plunderer plus Malcolm, Alluring Scoundrel:** Both are Pirate flyers in D; when both deal combat damage to the same player, Skyship triggers a targeted counter-increase effect and Malcolm triggers a chorus-counter/card filter effect. The same controller chooses their ordering on the stack. Assume Malcolm entered combat with **two chorus counters** and Skyship targets Malcolm:

1. Resolve Skyship **first**: Malcolm increases from 2 to 3 existing chorus counters.
2. Resolve Malcolm **second**: it puts its own chorus counter (3 → 4), draws and discards; because four chorus counters exist at the relevant resolution, it may cast the **actual discarded card** without paying its mana cost, provided it can legally be cast.
3. Reverse the order: Malcolm goes 2 → 3, draws/discards and **does not** qualify for the free cast; Skyship then increases 3 → 4 **too late** to retroactively cast that discarded card. The permanent still has four counters for later hits.

If Malcolm started with zero chorus counters, Skyship resolving first adds **none** (it cannot invent a new counter type); Malcolm then adds one. Resolving Malcolm first adds one chorus and Skyship then adds the second. This is a real threshold/timing interaction, not an assumed additional card-draw or free spell every attack. Zephyr Singer's printed flying counters and possible Francisco +1/+1 explore counters are other target situations, but no automatic extra payoff is inferred without existing counters and legal targets.

## Broadside Bombardiers paid combat windows

- It has haste/menace and may boast **after it has attacked**, even before blockers are declared, but only **once each turn**. The mana value of the creature/artifact sacrificed **as cost** determines 2 + MV damage. The sacrificed permanent must be **another** artifact or creature; not Broadside itself.
- A preexisting Treasure is MV **0**, so it pays a boast cost for precisely **two damage**. That will not kill a normal 3/3 blocker. An Arcane Signet is MV **2**, enabling four damage but sacrificing actual ramp and colored fixing; that trade can be defensible but is not free.
- A Treasure created later from combat damage cannot retroactively clear an already-declared blocker in that same combat. The same Treasure cannot be both spent for mana and sacrificed to pay the boast cost.
- This line supports Beckett's Pirate connection and a secondary combat finisher only when actual resources, legal timing and the defender's interaction allow it.

## Defensive cost of passive Pirate evasion

- Departed Deckhand is a Spirit **Pirate** that normally evades non-Spirit blockers. However, the act of becoming the target of **any spell** triggers its sacrifice, including our own targeting spells. An equipment *equip ability* is not a spell and does not trigger this sacrifice by itself; subsequent shroud/protection may still change legality.
- Cloud Pirates supplies a one-blue flying Pirate but its printed restriction allows it to block **only** creatures with flying. It is not a normal blocker for the ground-combat retaliation it invites. Neither card can be counted as universally unblockable/defensive.

## Evidence receipt and honest limits

Test source: `tests/test_m6_admiral_beckett_candidate_d_changed_effects.py` (7 finite bounded methods: source hash, chorus order and zero-counter negative, conditional free-cast source, boast damage/sacrifice/attack timing, Deckhand-target distinction). Existing D four-turn source-paid fixture and 13/13 original blueprint IDs remain separate receipts. These new checks do **not** simulate an opponent holding Counterspell, Fog, creature removal, or a deckwide competitive win rate; they cannot themselves establish M6.6–M6.9 completion, M6.10 acceptance, or final M7 optimality.

**Next actual gate:** bind the exact-head CI result to a candidate D continuation ledger; then reconcile the remaining Phase-B strategic judgment and M6 I/J reproducibility prerequisites. Never recycle Abaddon's certificate or label a research-only candidate owner-ready.
