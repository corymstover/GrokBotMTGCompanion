# Davros, Dalek Creator — M6 I local-best memo for the M7 candidate (2026-10-23)

This memo is evidence only. The candidate is NOT owner approved and NOT M6 certified, and the canonical list is unchanged.

Scope: the eight complete configurations in
`data/grixis/m6/ij/tested_pools/Davros__Dalek_Creator_M7_tested_configurations_20261023.json`, plus named single-card contenders. Each configuration is 100 = 1 commander + 99 library. This is not a global or statistical optimum.

## Result
The preferred six (raw b5c3af5f…) is the local best of the tested pool:
- Adds: +Bloodletter of Aclazotz, +Unlicensed Disintegration, +Tergrid, God of Fright, +Purphoros, God of the Forge, +Fiery Confluence, +Tectonic Giant.
- Cuts: −Death in Heaven, −Weeping Angel, −The Cyber-Controller, −Blasphemous Act, −Vandalblast, −Swan Song.

## Why (commander-first)
Davros, Dalek Creator ({1}{U}{B}{R} 3/4 menace legendary artifact Alien Scientist, not a Dalek): at the beginning of our end step, if an opponent lost 3 or more life this turn, create a 3/3 menace Dalek; then each opponent who lost 3 or more faces a villainous choice (we draw a card, or that player discards a card). Only life lost on **our** turn counts.

Each add makes that condition easier to meet for more opponents, or punishes the answer opponents give:
- **Bloodletter of Aclazotz** doubles every opponent's life loss on our turn. 2 becomes 4, so Fiery's 2-damage mode, a Purphoros trigger and Missy's choice qualify on their own. **Death in Heaven** is a two-turn Saga with no life loss.
- **Unlicensed Disintegration** is instant removal that, with an artifact out (23 including Davros), deals 3 to the target's controller. **Weeping Angel** is a defensive flash body with no life-loss text (Pass C's own pairing).
- **Tergrid, God of Fright** steals the nontoken permanents opponents sacrifice or the permanent cards they discard to Davros, Court of Ambition, Torment of Hailfire, Perforating Artist, Sycorax Commander, The Dalek Emperor and Doomsday Confluence. That makes "pay with cards" the expensive answer. **The Cyber-Controller** is an X-cost Cyberman lord shared with Deck #11.
- **Purphoros, God of the Forge** deals 2 to each opponent whenever another creature enters under our control (Dalek tokens, myriad copies, creature spells). It is indestructible. **Blasphemous Act** kills our own Daleks and Davros.
- **Fiery Confluence** with 2-2-2 deals 6 to each opponent (12 with Bloodletter). Its artifact mode replaces **Vandalblast**.
- **Tectonic Giant** (post-floor sixth swap) deals 3 to each opponent whenever it attacks, before blockers. That is a repeatable table qualifier. **Swan Song** is a 1-mana counter that also gives an opponent a flying blocker.

## Pass C requested tests (bounded finite versions; not win rates)
Run in `tests/test_m6_davros_dalek_creator_m7_mechanics.py` (class `PassCBoundedMeasuredTests`):
1. **Unlicensed Disintegration variants** (Pass C item 1). A 16-case grid: target legal or removed/bounced × artifact controlled or not × our turn or another × target's controller already at 3+ or not.
   - It kills in all 8 legal-target cases.
   - With an illegal target nothing happens, including the 3 damage (608.2b).
   - It newly qualifies an opponent in exactly 1 of 16 cases (legal target, artifact, our turn, no prior loss), and only one opponent, never the table.
   - The deck has 23 artifacts counting Davros.
2. **Ingenious Artillerist variants** (Pass C item 2). Five entry patterns before our end step (none, one artifact, a batch of three, three separate entries, a 2-token myriad batch), plus a removal response and Davros's own post-threshold token.
   - Purphoros qualifies every opponent on 3 of 5 patterns; Artillerist does so on 2 of 5.
   - Artillerist deals 0 if removed in response and is a 3/1.
   - Davros's Dalek token is created after the condition check, so it cannot create the qualifying loss for that trigger. Its Purphoros/Artillerist triggers go on the stack after Davros's trigger finishes (603.3).
   - With two Davros triggers (Roaming Throne naming Alien or Scientist), the later trigger sees the token's damage: base A3/B1/C1 → Purphoros (2 qualify, 4 villainous choices), Artillerist (2, 2).
3. **Fiery Confluence vs current enablers** (Pass C item 3).
   - Boltwave (MV 1, 3 each) and Maestros Charm (MV 3, 3 each) qualify the table alone, as does Fiery 2-2-2 (6 each).
   - Fiery 2-2-artifact deals 4 each. If the artifact target becomes illegal, the whole spell does nothing (0). The 2-2-2 mode has no target, so it still deals 6.

Not done, stated plainly: Pass C asked for paired comparisons with the same opening hands, mana obligations, opponent hand density and removal windows. There was no shared opponent/mana sample, no removal-response rates and no matched multiplayer simulation. No simulator in this repository models Davros's end-step villainous choice, opponents' choices or multiplayer life totals, so no win rates are reported. The tests above are finite enumerations of the exact cases Pass C named.

## Self-challenge
- **Five-swap keeping Swan Song:** staged, RETAIN_ALTERNATIVE (MODERATE). It keeps a 1-mana counter for Davros and the engines but loses Tectonic Giant's repeatable table qualifier.
- **Six-swap keeping Blasphemous Act and cutting Ashad:** staged, rejected (MODERATE). Ashad's casualty copies (Roaming Throne, Auton Soldier, Dalek Squadron) multiply Davros triggers; the wipe kills our own Daleks.
- **Pass C's pairings (Fiery over Weeping Angel, Disintegration over This Is How It Ends, Vandalblast kept):** staged six-swap, rejected (MODERATE). This Is How It Ends is itself a villainous choice (lose 5, twice with The Valeyard).
- **Artillerist-over-Sycorax (Pass C's Artillerist pairing):** seven-swap, staged, rejected by the bounded entry test. Sycorax is itself a villainous-choice damage card.
- **Flame Rift over Ashad:** seven-swap, staged, rejected. It is self-damaging, one-shot and redundant.
- **Rejected singles:** Hellrider (vs Labyrinth Raptor), Impact Tremors (vs Enthusiastic Mechanaut), Archfiend of Despair (vs Cybermen Squadron), Exsanguinate (vs Auton Soldier), Kroxa (vs Dauthi Voidwalker), Painful Quandary (vs This Is How It Ends), Sheoldred, the Apocalypse (vs Toxic Deluge), Megrim (vs Feed the Swarm; the owner already cut Liliana's Caress), Pain Magnification (vs Counterspell), Torment of Scarabs (vs Snuff Out), Rhystic Study (vs Geth's Grimoire), Vampiric Tutor (vs Deadly Rollick). Excluded: Kaya's Guile (white).

## Limits
Only finite rules cases and bounded enumerations are tested. Main losses:
- Blasphemous Act. Toxic Deluge, Their Name Is Death (nonartifact only) and Cyclonic Rift remain.
- Vandalblast's one-sided artifact overload.
- Swan Song.
- Weeping Angel's flash body.
- Death in Heaven's delayed creature theft.
- The Cyber-Controller.

Other changes:
- Game Changers 5 → 6 (Tergrid).
- Creatures 23 → 25; instants/sorceries 24 → 23.
- Average nonland MV 3.185 → 3.231.
