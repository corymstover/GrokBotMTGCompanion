# Dr. Eggman — M6 I local-best memo for the M7 candidate (2026-10-23)

This memo is evidence only. The candidate is NOT owner approved and NOT M6 certified, and the canonical list is unchanged.

Scope: the nine complete configurations in
`data/grixis/m6/ij/tested_pools/Dr__Eggman_M7_tested_configurations_20261023.json`, plus named single-card contenders. Each configuration is 100 = 1 commander + 99 library. This is not a global or statistical optimum.

Baseline: canonical encyclopedia main 9b26aa28, `refinement/decklists/Dr_Eggman_Approved_2026-10-14.txt`, blob 86119caf, frozen by canonical commit 8883de3; the registry source commit 1836b97 carries the same bytes. Raw SHA-256 ef349862… equals the registry recorded digest (no provenance exception); logical hash lh1:04e4d973… equals registry baseline_hash.

## Result
The preferred five (raw 85bcd5a2…) is the local best of the tested pool:
- Adds: +Possession Engine, +Skysovereign, Consul Flagship, +Interceptor Mechan, +Su-Chi Cave Guard, +Behemoth of Vault 0.
- Cuts: −Blasphemous Act, −Cybermen Squadron, −Cryptothrall, −Unwinding Clock, −Foundry Inspector.

Five is the presentation floor, not a target: the three staged six-swaps were examined and rejected on their merits (below), and no card was added to reach a count.

## Why (commander-first)
Dr. Eggman ({2}{U}{B}{R} Legendary Creature — Human Scientist 3/6, flying): "At the beginning of your end step, draw a card. Then each opponent faces a villainous choice — That player discards a card, or you may put a Construct, Robot, or Vehicle card from your hand onto the battlefield." Villainous choice: 701.55a–d (each opponent chooses in turn order). A put permanent is not cast, so cast triggers do not fire (601.2, 603.2), but enters and dies triggers do (603.6a); a put Vehicle is not crewed.

- **Possession Engine** ({3}{U}{U} Vehicle 5/5, crew 3): when it enters, gain control of an opponent's creature while we control it (it can't attack or block). Works on a put. **Blasphemous Act** is a 9-MV sweeper that also kills Eggman and our artifact creatures; Toxic Deluge, Their Name Is Death (destroys only nonartifact creatures) and Cyclonic Rift remain.
- **Skysovereign, Consul Flagship** ({5} Vehicle 6/5 flying, crew 3): 3 damage to an opponent's creature or planeswalker on entering and on attacking; Eggman's 3 power crews it alone. **Cybermen Squadron** is a Cyberman (not a payload) whose myriad only matters when nonlegendary artifact creatures attack.
- **Interceptor Mechan** ({2}{B}{R} Robot 2/2 flying): on entering, return an artifact or creature card from our graveyard to hand. The returned card arrives after the current Eggman trigger, so it stocks the next one. **Cryptothrall** gives other artifact creatures hexproof; Padeem already gives all artifacts hexproof.
- **Su-Chi Cave Guard** ({8} Construct 8/8, vigilance, ward {4}): the largest cheap-to-put body; when it dies it adds eight {C} until end of turn. **Unwinding Clock** untaps artifacts on other turns and is not a payload.
- **Behemoth of Vault 0** ({6} Robot 6/6 trample): four energy on entering; when it dies, pay energy equal to a nonland permanent's MV to destroy it. **Foundry Inspector** is a 3/2 Construct whose discount applies only to artifacts we cast.
- Payloads (Construct/Robot/Vehicle in the 99) 28 → 31; P(no payload among 7 cards) 0.0893 → 0.0651, among 12 cards 0.0139 → 0.0079.

## Owner direction (flagged)
The owner's 2026-10-14 closeout named Blasphemous Act in the retained interaction suite and Foundry Inspector in the retained infrastructure. Both cuts contradict that and are flagged, not hidden. Each has a staged alternative: a four-swap that keeps Act (no Possession Engine) and a five-swap that keeps Inspector and cuts Weapons Manufacturing. Midnight Crusader Shuttle was demoted to a staged alternative because the owner rejected Damocles Base for permissive villainous-choice outcomes.

## Pass C requested tests (bounded finite versions; not win rates)
Run in `tests/test_m6_dr_eggman_m7_mechanics.py` (class `PassCBoundedMeasuredTests`). Pass C #15's final disposition was **NEEDS TESTING, KEEP**. The Pass C receipt is a NON-INDEPENDENT owner-equivalent (genuinely independent model NO).
1. **+Goblin Welder / −Liliana's Caress** over a 192-cell grid (opponent hand size, our artifact cards in graveyard, artifacts on battlefield, The Valeyard present, opponent's choice). Caress is live in 72 cells and drains 12 per trigger at hand 3 with The Valeyard on the discard branch (6 without). Welder is live in 64 cells, needs an artifact card already in our graveyard, and puts onto the battlefield, never into hand, so it never feeds Eggman's put branch. Pass C KEEP stands; the six-swap is staged and rejected.
2. **31 vs 32/33 lands, {2}{U}{B}{R} timing.** Exact multivariate-hypergeometric DP over the 99. P(5 lands by card 11/12): 0.2289/0.3032 (31), 0.2539/0.3328 (32), 0.2798/0.3631 (33). P(Eggman castable on lands plus rocks with U, B and R by card 11/12): 0.3751/0.4696 → 0.404/0.5009 → 0.4333/0.532. The preferred five does not change the mana. The 32-land list (+Silverbluff Bridge −Thoughtcast) is staged and rejected because the owner deliberately kept 31 lands.
3. **Cast vs put and multipliers.** A 64-cell villainous-choice grid. In 40 of 64 cells at least one opponent has a no-cost answer (an empty hand or a dead payload branch). Trigger multipliers are finite: with Roaming Throne, Spark Double, Strionic Resonator and Y'shtola extra steps, at most 9 Eggman triggers per turn, and with The Valeyard 18 choices per opponent. Cityscape Leveler is the only cast-only payload.

Not done, stated plainly: Pass C asked for fixed legal hands and mulligans, rational opponents, artifact removal and graveyard hate. Those are not modelled; there is no matched-opening playtest or multiplayer sample, so no win rates are reported.

## Self-challenge
- **Four-swap keeping Blasphemous Act (no Possession Engine):** staged, RETAIN_ALTERNATIVE (below the floor).
- **Five-swap keeping Foundry Inspector, cutting Weapons Manufacturing:** staged, RETAIN_ALTERNATIVE (close call).
- **Midnight Crusader Shuttle instead of Su-Chi:** staged five-swap, rejected (owner's Damocles critique).
- **Goblin Welder over Caress; Tergrid over Caress; 32 lands:** staged six-swaps, rejected (items 1–2; Tergrid would be Game Changer #4 and is cast-only).
- **Rejected singles:** Drossforge Bridge, Relentless X-ATM092, Bygone Colossus, Thought Vessel, This Is How It Ends, Ensnared by the Mara, Starscream, Power Hungry, Krang, the All-Powerful (it doubles only draw-caused triggers; Eggman's is an end-step trigger), Craterclaw Colossus.
- **Owner-removed class (flagged, not re-added):** Imposter Mech, Torrential Gearhulk, Scrawling Crawler, Raiders' Wake, Chief of the Foundry and Steel Overseer were evaluated and rejected as OWNER-REMOVED/REJECTED in the 2026-10-14 closeout.

## Limits
Only finite rules cases and bounded enumerations are tested. Main losses:
- Blasphemous Act's cheap board reset (owner-retained).
- Foundry Inspector's cast discount (owner-retained).
- Cybermen Squadron's myriad, Cryptothrall's hexproof and Unwinding Clock's untaps.

Other changes:
- Game Changers 3 → 3 (Bracket 4 either way).
- Creatures 33 → 33; instants/sorceries 13 → 12.
- Average nonland MV 4.206 → 4.221.
