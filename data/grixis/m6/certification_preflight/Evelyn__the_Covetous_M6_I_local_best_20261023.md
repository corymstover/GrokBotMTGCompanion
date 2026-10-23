# Evelyn, the Covetous — M6 I local-best memo for the M7 candidate (2026-10-23)

This memo is evidence only. The candidate is NOT owner approved and NOT M6 certified, and the canonical list is unchanged.

Scope: the eight complete configurations in
`data/grixis/m6/ij/tested_pools/Evelyn__the_Covetous_M7_tested_configurations_20261023.json`, plus named single-card contenders. Each configuration is 100 = 1 commander + 99 library. This is not a global or statistical optimum.

Baseline: canonical encyclopedia main 9b26aa28, `refinement/decklists/Evelyn_the_Covetous_Approved_2026-10-14.txt` (blob 03574140, frozen by canonical commit 43c0ceca); the registry source commit 1836b97 carries the same bytes. Raw SHA-256 1d602b5d… equals the registry recorded digest (no provenance exception); logical hash lh1:94c3b2c4… equals registry baseline_hash and current_canonical_hash.

## Result
The preferred five (raw c3f6862c…, lh1:7f36c397…) is the local best of the tested pool:
- Adds: +Marsh Flats, +Insolent Neonate, +Brainstorm, +Burnt Offering, +Verdant Catacombs.
- Cuts: −Thundering Falls, −Spellskite, −Redirect Lightning, −Wan Shi Tong, Librarian, −Blazemire Verge.

Five is the presentation floor, not a target. After the first five, eight further incumbents were challenged (Ripples of Undeath by Spell Pierce, Notion Thief by Wan Shi Tong, Mount Doom by Starting Town, Praetor's Grasp by Intuition, Dauthi Voidwalker by Grief, Gitaxian Probe by Lively Dirge, Hexing Squelcher by Dispel, Final Fortune by Gifts Ungiven); all were kept, and no card was added just to reach a count.

## Why (commander-first)
Evelyn, the Covetous ({2}{U/B}{B}{B/R} 2/5 Legendary Creature — Vampire Rogue, flash): "Whenever Evelyn or another Vampire you control enters, exile the top card of each player's library with a collection counter on it. Once each turn, you may play a card from exile with a collection counter on it if it was exiled by an ability you controlled, and you may spend mana as though it were mana of any color to cast it." The trigger is Vampire-only; in the baseline Evelyn is the only Vampire.

- **Insolent Neonate** ({R} 1/1 menace Vampire; discard a card, sacrifice: draw): the only add that triggers Evelyn's Vampire clause (four cards exiled in a four-player pod), and an instant-speed outlet that bins Worldgorger Dragon or a second creature card as the loop exit (104.4b). **Spellskite** (plain RETAIN) is a 2-mana redirect body absent from EDHREC Evelyn cEDH. This cut is flagged: the owner rejected the optimized-tribal Vampire package; Neonate is a single combo piece, not that package.
- **Burnt Offering** ({B} instant; sacrifice a creature: B/R mana equal to its MV): 46% stats.cedh.events Evelyn staple. Sacrificing Evelyn gives 5 and Worldgorger 6. **Wan Shi Tong, Librarian** (plain RETAIN; Pass C's optional cut target) is a slow X value creature.
- **Brainstorm** ({U} instant): the Pass C hypothesis card. It is added over **Redirect Lightning** (plain RETAIN, narrow) instead of over the owner-defended Ripples of Undeath.
- **Marsh Flats** and **Verdant Catacombs** (81% / 76% EDHREC cEDH): untapped fetches for **Thundering Falls** (the only always-tapped land, 9%) and **Blazemire Verge** (conditional R, 6%). Fetches 7 → 9 also turn Brainstorm's two returned cards into fresh draws.
- Creatures 14 → 13; Vampires 1 → 2; instants/sorceries 36 → 37; lands 26 → 26.

## Owner direction
Every cut is a plain RETAIN line in the owner's 2026-10-14 decisions. **No explicit owner keep is overridden.** Vexing Bauble ("intentional escape valve"), Ripples of Undeath, Saw in Half, Windfall/Notion Thief, Stifle and Mistrise Village stay. Pass C's exact swap (+Brainstorm / −Ripples of Undeath) is staged as a complete 100, not selected. Owner-removed classes are not re-added: Displacer Kitten, Otawara, Morphic Pool, Talisman of Creativity, Wheel of Fortune, The One Ring, Dragon's Rage Channeler, Cyclonic Rift, Deflecting Swat, Into the Flood Maw, Hoarding Broodlord, Beseech the Mirror and the optimized-tribal Vampire top-100 package. Insolent Neonate is flagged as the one add a reviewer could read as part of the rejected Vampire class.

## Pass C requested tests (bounded finite versions; not win rates)
These are in `data/grixis/m7/research_challengers/Evelyn__the_Covetous_bounded_measured_tests_20261023.json` and recomputed in `tests/test_m6_evelyn_the_covetous_m7_mechanics.py`. Pass C #18's final disposition was **NEEDS TESTING**. The Pass C receipt is a NON-INDEPENDENT owner-equivalent (actual technical third-model independence FALSE).
1. **Castability, Brainstorm {U} vs Ripples {1}{B}** (exact hypergeometric; lands plus rocks counted one each, moxen/rituals excluded): Brainstorm U source on turn 1, play/draw: baseline 0.8385/0.8771, candidate 0.8531/0.8899. Ripples castable on turn 2: 0.7852/0.8414 baseline.
2. **Ripples mills Worldgorger** (cast turn 2, first trigger turn 3, given Worldgorger not yet drawn), play: 0.0333/0.0671/0.1012 over 1/2/3 triggers (draw 0.0337/0.0678/0.1023), at 3 life plus {1} per take.
3. **Fetch support for Brainstorm** (≥1 fetch in the first 7 cards): 0.4115 → 0.4981 on the play.
4. **Evelyn castability** (min(lands,T)+rocks ≥ 5, a black source, ≥3 coloured sources): turn 4 on the play 0.1491 → 0.1491; turn 5 0.2767 → 0.2768.

Not done, stated plainly: Pass C asked for matched opening hands and games comparing the two cards. There is no validated Evelyn cEDH game or opponent model, so no matched-shuffle playtest, win rate or kill-turn distribution is reported.

## Self-challenge
- **Pass C exact swap (+Brainstorm / −Ripples):** staged, RETAIN_ALTERNATIVE (overrides the owner-defended Ripples).
- **Four-swap keeping Blazemire Verge:** staged, RETAIN_ALTERNATIVE (below the floor; the closest call).
- **Five-swap with Grim Monolith instead of Burnt Offering:** staged, RETAIN_ALTERNATIVE (Grim is a Game Changer: 19 → 20).
- **Five-swap keeping Wan Shi Tong, cutting Notion Thief:** staged, RETAIN_ALTERNATIVE (cuts the owner-defended Windfall pair).
- **Six-swap with Spell Pierce over Ripples:** staged, RETAIN_ALTERNATIVE.
- **Rejected singles:** Intuition, Forbidden Orchard, Fierce Guardianship, Dispel, Daze (our own Vexing Bauble counters it), Grief, Vampire Hexmage, Changeling Outcast, Brazen Borrower, Lively Dirge, Starting Town, Gifts Ungiven, Snow-Covered Swamp, Bloodtithe Harvester; Displacer Kitten and Otawara are owner-removed and stay out.
- **Owner-removed classes:** none re-added.

## Limits
Only finite rules cases and exact enumerations are tested. Main losses: Spellskite and Redirect Lightning (the redirect pair against targeted removal), Wan Shi Tong (search punishment), Thundering Falls' surveil, Blazemire Verge's non-fetch B/R (Stifle-proof). Game Changers 19 → 19 (Bracket 5). Average nonland MV 1.836 → 1.808. The castability model counts each fetch as a source of any one Grixis colour (true here: every fetch reaches a dual of each needed colour, but not simultaneously), counts Gemstone Caverns and Exotic Orchard as rainbow sources (Caverns needs the luck counter; Orchard depends on opponents' lands), and ignores fetch/shock life. Absolute figures are slightly optimistic for every list alike.
