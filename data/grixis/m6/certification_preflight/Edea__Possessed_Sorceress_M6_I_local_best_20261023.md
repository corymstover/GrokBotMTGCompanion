# Edea, Possessed Sorceress — M6 I local-best memo for the M7 candidate (2026-10-23)

This memo is evidence only. The candidate is NOT owner approved and NOT M6 certified, and the canonical list is unchanged.

Scope: the eight complete configurations in
`data/grixis/m6/ij/tested_pools/Edea__Possessed_Sorceress_M7_tested_configurations_20261023.json`, plus named single-card contenders. Each configuration is 100 = 1 commander + 99 library. This is not a global or statistical optimum.

Baseline: canonical encyclopedia main 9b26aa28, `refinement/decklists/Edea_Possessed_Sorceress_Approved_2026-10-14.txt`; the registry source commit 1836b97 carries the same bytes. Raw SHA-256 fd560a9b… equals the registry recorded digest (no provenance exception); logical hash lh1:d6ca0855… equals registry baseline_hash.

## Result
The preferred five (raw e8680caf…, lh1:60df4349…) is the local best of the tested pool:
- Adds: +Aggravated Assault, +Kaya's Ghostform, +Hall of Echoes, +Geyadrone Dihada, +Combat Celebrant.
- Cuts: −Evereth, Viceroy of Plunder, −Zara, Renegade Recruiter, −High Market, −Ayara, Widow of the Realm, −Seize the Spotlight.

Five is the presentation floor, not a target. After the first five, eight further incumbents were challenged (Irma, Impostor Syndrome, Industrial Advancement, Kethek, Lightning Greaves, Victimize, Mob Rule, Disciple of Bolas); all were kept, and no card was added just to reach a count.

## Why (commander-first)
Edea ({2}{U}{B}{R} Legendary Creature — Human Warlock 2/5, ward {2}): "At the beginning of combat on your turn, gain control of target creature an opponent controls until end of turn. Untap it. It gains haste until end of turn. Whenever a creature you control but don't own dies, return it to the battlefield under its owner's control and you draw a card." Every extra combat (500.8, 506.1) is another theft, and every copy of Edea is another trigger.

- **Aggravated Assault** ({2}{R} enchantment; {3}{R}{R}: untap all creatures you control, extra combat and main phase, sorcery speed): a repeatable extra combat, so a repeatable Edea theft. **Evereth** (FLAG: owner keep) is a 3-MV flier and sorcery-speed outlet whose death trigger drains each opponent for its power; it doesn't add thefts.
- **Kaya's Ghostform** ({B}): put on a stolen creature, order Ghostform's trigger first (603.3b). It returns the card under our control; Edea's return then finds a new object (400.7) and does as much as possible (609.3), so we still draw. This is not a delayed trigger, unlike the owner-rejected Marchesa route. **Zara** (5 MV) only borrows a creature card from the defending player's hand, and it goes back to hand at end step.
- **Hall of Echoes** (land; {T}: add {C}; {5}: it becomes a copy of target creature we control until end of turn, and the legend rule (704.5j) doesn't apply to our permanents this turn). Copying Edea in the first main phase (707.2) gives a second beginning-of-combat theft and a second death trigger (one return, two draws). **High Market** (owner-retained land outlet, FLAG) is the cut; repeatable outlets fall 10 → 7.
- **Geyadrone Dihada** ({1}{U}{B}{R}, loyalty 4): −3 steals a creature or planeswalker until end of turn (untap, haste) and corrupts it; −7 permanently gains control of every permanent with a corruption counter (the +1 also places counters). This is theft density, the owner's stated priority. **Ayara** is a 3-MV legendary outlet (tap, sacrifice another creature: damage and life equal to its MV) that doesn't steal.
- **Combat Celebrant** ({2}{R}, exert as it attacks for one more combat, 701.43a). OFF-RANKING. With exert it works on alternate turns unless Aggravated Assault or Full Throttle untaps it. **Seize the Spotlight** (54% EDHREC inclusion, notable loss) is a one-shot where each opponent chooses.
- Extra-combat sources 2 → 4; Edea copy and trigger effects 6 → 7.

## Owner direction (flagged)
The owner's 2026-10-14 decision challenged Evereth and kept it, and kept High Market as a "land-based sacrifice outlet". Both cuts override that and are flagged. A four-swap that keeps Evereth (Assault over Spotlight, no Celebrant) is staged. The owner wrote "Another four-mana clone had lower marginal value than theft density or extra combats", so Lithoform Engine was moved to a staged alternative and Dihada (theft) was selected. Conjurer's Closet stays rejected ("Thassa performs the same crucial end-step retention job one mana cheaper").

## Pass C requested tests (bounded finite versions; not win rates)
These are in `tests/test_m6_edea_possessed_sorceress_m7_mechanics.py` (class `PassCBoundedMeasuredTests`). Pass C #16's final disposition was **NEEDS TESTING, KEEP**. The Pass C receipt is a NON-INDEPENDENT owner-equivalent (genuinely independent model NO).
1. **+Closet / −Irma** (32-cell grid): Irma 216 vs Closet 120 steal triggers, with Irma ahead in 28 cells. Closet keeps 48 creatures vs 16, but Thassa already supplies the end-step keep in half the cells. KEEP Irma.
2. **+Closet / −Impostor Syndrome** (8 cells): Impostor ties or beats Closet in 6 and beats it in 4. KEEP.
3. **+Closet / −Industrial Advancement** (28 cells, exact hypergeometric): Advancement finds a creature 0.4936–0.8834 of the time (0.7308 at MV 5, 80 cards, 18 creatures), on top of Edea's draw. KEEP.
4. **Combat Celebrant vs Grim Haruspex** (32 cells): Celebrant gives 48 extra steals (exert model), and Haruspex draws 144 times. Both stay; Celebrant replaces Spotlight, not Haruspex (Pass C DEFER honoured).
5. **Untapped/coloured sources, turns 3–7** (exact DP on the play): P(Edea castable) by turns 3/4/5/6/7 is 0.0456/0.2304/0.4878/0.588/0.6772, the same in both lists.

Not done, stated plainly: Pass C asked for identical starting hands, shuffles and interaction sequences against legal opponent boards, blockers and hit rates. There is no opponent model, matched-shuffle playtest or multiplayer sample, so no win rates or success rates are reported.

## Self-challenge
- **Four-swap keeping Evereth:** staged, RETAIN_ALTERNATIVE (below the floor).
- **Five-swap with Lithoform Engine instead of Dihada:** staged, RETAIN_ALTERNATIVE.
- **Three Closet six-swaps:** staged and rejected (items 1–3).
- **Rejected singles:** Sephiroth, Bribery, Agent of Treachery, Treachery, Helm of the Host, Sakashima the Impostor, Nasty End, Rhystic Study, Cyclonic Rift, Dark Ritual, Jeska's Will, Nightscape Familiar, Relentless Assault, Hellkite Charger, Laughing Jasper Flint, Susur Secundi, Swiftfoot Boots. Jabs and Mistress of Mockery were EXCLUDE_INVALID.
- **Owner-removed classes:** none re-added. The delayed Marchesa-style return and Closet are not added.

## Limits
Only finite rules cases and bounded enumerations are tested. Main losses: Evereth's drain (owner keep), High Market's land outlet (owner keep), Ayara, Zara and Seize the Spotlight. Repeatable outlets 10 → 7 (P(at least one in 12 cards) 0.7432 → 0.6075). Game Changers 3 → 3 (Bracket 4). Creatures 24 → 22; instants/sorceries 24 → 23; average nonland MV 3.203 → 3.156.
