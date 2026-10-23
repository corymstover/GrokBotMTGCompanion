# Don Andres, the Renegade — M6 I local-best memo for the M7 candidate (2026-10-23)

This memo is evidence only. The candidate is NOT owner approved and NOT M6 certified, and the canonical list is unchanged.

Scope: the nine complete configurations in
`data/grixis/m6/ij/tested_pools/Don_Andres__the_Renegade_M7_tested_configurations_20261023.json`, plus named single-card contenders. Each configuration is 100 = 1 commander + 99 library. This is not a global or statistical optimum.

Baseline: canonical encyclopedia main 9b26aa28, `refinement/decklists/Don_Andres_the_Renegade_Approved_2026-10-14.txt`, blob 1d20d488, frozen by canonical commit 255c328; the registry source commit 1836b97 carries the same bytes. Raw SHA-256 a6022fdd… equals the registry recorded digest (no provenance exception); logical hash lh1:012d9c8c… equals registry baseline_hash.

## Result
The preferred five (raw 05e13311…) is the local best of the tested pool:
- Adds: +Gríma, Saruman's Footman, +Fallen Shinobi, +Treachery, +Gloomlake Verge, +Blazemire Verge.
- Cuts: −Professional Face-Breaker, −Seize the Spotlight, −Blasphemous Act, −Shipwreck Marsh, −Smoldering Marsh.

Five is the presentation floor, not a target: the four staged six-swaps were examined and rejected on their merits (below), and no card was added to reach a count.

## Why (commander-first)
Don Andres, the Renegade ({1}{U}{B}{R} Legendary Creature — Vampire Pirate 4/3): "Each creature you control but don't own gets +2/+2, has menace and deathtouch, and is a Pirate in addition to its other types." and "Whenever you cast a noncreature spell you don't own, create two tapped Treasure tokens." Ownership: 108.3, 110.2, 111.2; a copy is not cast (707.10).

- **Gríma, Saruman's Footman** ({2}{U}{B} 1/4, can't be blocked): on combat damage to a player, that player exiles until an instant or sorcery and we may cast it free. Every connection is a noncreature spell we don't own, i.e. one Don trigger (two tapped Treasures). **Professional Face-Breaker** makes Treasure from combat damage and can impulse-draw *our own* cards; it does not touch either half of Don's Oracle.
- **Fallen Shinobi** ({3}{U}{B} 5/4, ninjutsu {2}{U}{B}, 702.49): on combat damage, that player exiles the top two and we may play them free. Noncreature hits trigger Don (exact expectation 2 × 30/85 = 12/17 Don triggers per connection when 30 of an 85-card opposing library are noncreature spells); creature hits become opponent-owned creatures under our control, which Don buffs. **Seize the Spotlight** lets each opponent choose fame or fortune, so the opponent picks the worse outcome for us.
- **Treachery** ({3}{U}{U} Aura, untaps five lands on entry): permanent creature theft; the stolen creature gets Don's +2/+2, menace, deathtouch and Pirate type (613.1b, 613.4c; aura control 303.4e). **Blasphemous Act** destroys our own stolen army and Don; Toxic Deluge and Cyclonic Rift remain as resets.
- **Gloomlake Verge / Blazemire Verge** (unconditional U / B; second colour needs an Island/Swamp or Swamp/Mountain; 9 qualifying names each). They replace **Shipwreck Marsh** and **Smoldering Marsh**, whose two-basic condition rarely holds with four basics. Early conditional-or-tapped lands 5 → 3.

## Pass C requested tests (bounded finite versions; not win rates)
Run in `tests/test_m6_don_andres_the_renegade_m7_mechanics.py` (class `PassCBoundedMeasuredTests`). Pass C #14's final disposition was **KEEP** (Stage A provisional +Mob Rule/−Insurrection). The Pass C receipt is a NON-INDEPENDENT owner-equivalent (genuinely independent model NO).
1. **Mob Rule vs Insurrection** at 6/7/8 available mana × five fixed mixed-power opponent tables × Don present/removed (60 cells).
   - Insurrection is uncastable at 6–7 mana; Mob Rule is castable in every cell.
   - At 8 mana Insurrection steals at least as many creatures and as much power as Mob Rule on all five tables, Don present or not. Mob Rule keeps 115/144 of Insurrection's stolen power and equals it on 2/5 tables.
   - Don's survival changes power (+2 per stolen creature), not the creatures taken, except that Mob Rule's best mode flips on the one-big-threat table (four small creatures with Don, the 8-power creature without).
   - Red availability (lands-only, 13 cards, turn 7 on the play): ≥2 red lands 0.8396 baseline / 0.8169 candidate; ≥3 red lands 0.5901 / 0.5529; identical to baseline when the Verge condition is met. Red land sources 22 → 21 (22 with Blazemire's conditional {R}). Rocks and Treasures also make red, so these are floors.
   - Mob Rule over Insurrection is staged as a complete six-swap 100 and rejected: a genuine trade, but Pass C's final KEEP and the owner's approved Insurrection stand.
2. **Bribery vs Thieving Amalgam / Jhoira** over five opponent creature densities (0/4/8/15/25), counting opponent-owned permanents gained and opponent turns until the first.
   - Bribery: at most one permanent ever, none on a creature-free library; pays off on resolution (0 opponent turns).
   - Thieving Amalgam: three opponent-owned manifests per round from the first opponent upkeep (1 opponent turn), six after two rounds, each a 4/4 menace deathtouch Pirate with Don.
   - Jhoira: one historic permanent on entering (0 turns) and one per surviving attack.
   - None of the three triggers Don (they are not cast). Both Bribery six-swaps are staged and rejected; Bribery was also an owner 2026-10-14 removal (flagged).

Not done, stated plainly: Pass C asked for "mixed tables" and "Don survival"; opponents' blocks, responses, hand contents and removal rates are not modelled, and there is no matched-opening playtest or multiplayer sample. No simulator in this repository models Don's ownership interactions, so no win rates are reported.

## Self-challenge
- **Four-swap keeping Blasphemous Act (no Treachery):** staged, RETAIN_ALTERNATIVE (MODERATE). For an owner who wants a second creature sweeper.
- **Dazzling Sphinx instead of Gríma:** staged five-swap, rejected. Same trigger on a 5-mana flyer; Gríma is cheaper and unblockable.
- **Nightveil Specter over Locke, Treasure Hunter:** staged six-swap, rejected (LOW, marginal).
- **Pass C Mob Rule over Insurrection; Bribery over Thieving Amalgam; Bribery over Jhoira:** staged six-swaps, rejected (items 1–2).
- **Rejected singles:** Control Magic (Treachery strictly better here), Sower of Temptation, Robber of the Rich, Intellect Devourer, Mass Mutiny, Call for Aid, Stolen Goods, Desertion, Port Razer, Thieving Skydiver, Knowledge Exploitation, Mnemonic Betrayal (its Treasure argument is false: Don's Treasures enter tapped, and returned permanents are not cast), Fevered Suspicion, Dream Harvest, Heartless Conscription, Riverpyre Verge, Swiftfoot Boots.
- **owner-removed class (flagged, not re-added):** the owner's 2026-10-14 approval removed Buried Alive, Living Death, Victimize, Cunning Rhetoric, Share the Spoils, The Ruinous Powers, Revel in Riches, Gonti, Lord of Luxury, Zara, Renegade Recruiter and four slow/tapped lands, and rejected Bribery, Agent of Treachery, Captivating Crew and Memory Plunder. Those evaluated here were rejected; none is re-added. Tinybones, Trinket Thief was not in the live batch and is not added.

## Limits
Only finite rules cases and bounded enumerations are tested. Main losses:
- Professional Face-Breaker's Treasure-on-combat and impulse draw.
- Seize the Spotlight's two-mana card/Treasure flexibility.
- Blasphemous Act's one-mana board reset.
- Shipwreck Marsh's and Smoldering Marsh's dual colours on the rare turns their condition holds.

Other changes:
- Game Changers 5 → 5 (Bracket 4 either way).
- Creatures 28 → 29; instants/sorceries 19 → 17.
- Average nonland MV 3.312 → 3.297.
