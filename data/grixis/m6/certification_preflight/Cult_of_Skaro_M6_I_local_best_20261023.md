# Cult of Skaro — M6 I local-best memo for the M7 candidate (2026-10-23)

This memo is evidence only. The candidate is NOT owner approved and NOT M6 certified, and the canonical list is unchanged.

Scope: the eight complete configurations in
`data/grixis/m6/ij/tested_pools/Cult_of_Skaro_M7_tested_configurations_20261023.json`, plus named single-card contenders. Each configuration is 100 = 1 commander + 99 library. This is not a global or statistical optimum.

## Result
The preferred six (raw 8b765d85…) is the local best of the tested pool:
- Adds: +Karlach, Fury of Avernus, +Kindred Discovery, +Hammer of Purphoros, +Shaun, Father of Synths, +Quantum Misalignment, +Skorpekh Lord.
- Cuts: −Cybermen Squadron, −Canoptek Spyder, −Adaptive Omnitool, −The Master, Multiplied, −Anrakyr the Traveller, −Etherium Sculptor.

## Why (commander-first)
Cult of Skaro ({1}{U}{B}{R} 4/4 legendary artifact Dalek, no haste) is worth one random trigger per declared attack: Thay (+1/+1 counter on each artifact creature), Caan (draw two), Sec (3/3 menace Dalek) or Jast (each opponent loses 4). The approved list multiplies that trigger with copies (Strionic Resonator, Scientist Supreme), a second roll (Roaming Throne naming Dalek), clones, haste equipment and one-shot extra combats.

The six adds each produce more declared Cult attacks, or more value from them, than the slot they take:
- **Karlach, Fury of Avernus** gives an extra combat every turn in which we attack, so Cult and every untapped Cult copy trigger twice. **Cybermen Squadron**'s myriad copies enter tapped and attacking and never trigger Cult (CR 508.4).
- **Kindred Discovery** naming Dalek draws on every Dalek entry and declared attack, before blockers. The bounded measured test shows it beats **Canoptek Spyder** on 4 of 5 fixed boards; Spyder ignores all tokens.
- **Hammer of Purphoros** gives every creature haste: Cult from the command zone and every new clone attack at once. **Adaptive Omnitool** is an equip-{3} dig that needs an attack first.
- **Shaun, Father of Synths** makes a persistent non-legendary Synth copy of Cult whenever we attack. Ordered above Karlach's trigger, the Synth is untapped; with haste from Hammer or The Dalek Emperor (CR 302.6) it attacks in the extra combat (3 Cult triggers in one turn, otherwise 2). **The Master, Multiplied** mainly preserved myriad tokens, which do not trigger Cult.
- **Quantum Misalignment** is two non-legendary Cult copies over two turns (rebound). **Anrakyr the Traveller**'s free artifact cast costs life and rarely has a good target.
- **Skorpekh Lord** (post-floor sixth swap) gives other artifact creatures +1/+0 and menace for Research Thief, Thopter Spy Network, Sword and Jast finishes. **Etherium Sculptor** is the third of three artifact reducers (Mechanaut and Shuri stay).

## Pass C requested tests (bounded finite versions; not win rates)
Run in `tests/test_m6_cult_of_skaro_m7_mechanics.py` (class `PassCBoundedMeasuredTests`):
1. **Kindred vs Research Thief** — actual subtype mix of the 100 (4 Dalek creature cards: Cult, Dalek Drone, Dalek Squadron, The Dalek Emperor; 18 other artifact creatures in the baseline, 15 in the candidate; 5 Dalek-token makers; 8 Cult copy effects in the candidate). Five fixed boards, each at hit rates 0, 1/4, 1/2, 3/4, 1: pre-damage Kindred draws (5/4 Cult alone, 29/4 Genesis chapter III turn, 13/4 mixed board, 0 post-wipe non-Dalek rebuild, 13/4 Dalek Drone turn) vs post-damage Thief draws (artifact attackers × hit rate). Kindred is ≥ Thief at hit rates up to 1/2 on the 4 Dalek-containing boards; Thief wins on the post-wipe non-Dalek board and on fully connecting wide mixed boards. Result: keep Thief, cut Spyder instead (Kindred > Spyder on 4 of 5 boards).
2. **Kindred vs Thopter Spy Network** — the same boards give Spy Network's one draw per connecting combat (e.g. 15/16 on the Genesis board at hit rate 1/2). Spy Network also makes a Thopter each upkeep, which keeps artifact bodies coming after a rebuild. It was not cut.
3. **Karlach vs Biotransference / Spyder** — Karlach adds one full Cult trigger per turn (expected +1/2 card, +1/4 Dalek, +1 life per opponent), and with Shaun plus haste for the Synth 1 → 3 triggers. Biotransference's Necrons are 2/6/10 power across 1/3/5 artifact spells. Karlach takes Cybermen Squadron's slot instead; both Pass C pairings are staged as complete 100s and rejected.
4. **Hexplate Wallbreaker vs Biotransference or Spyder** — tempo trace: 5 mana to cast, then {3}{R} to move it to Cult = 9 mana before the first extra combat, against 5 for Karlach. Rejected.
5. **Fireweaver / Mechanized Production** (secondary) — judged as single-card contenders and rejected.

Not done, stated plainly: there was no shared opponent/mana sample, no removal-response rates and no matched multiplayer simulation. No existing simulator in this repository models Cult's random modes, attack-trigger copies or extra combats, so no win rates are reported. Kindred overdraw/deck-out risk (mandatory draws, CR 704.5b) is disclosed, not modeled.

## Self-challenge
- **Five-swap keeping Etherium Sculptor:** staged, RETAIN_ALTERNATIVE (MODERATE). It keeps a third reducer but loses team menace.
- **Four-swap keeping the myriad package (no Karlach or Shaun):** staged, rejected (MODERATE). Myriad copies never trigger Cult.
- **Pass C's Kindred-over-Research Thief pairing:** staged six-swap, rejected (MODERATE) by the bounded draw test.
- **Pass C's Karlach-over-Biotransference pairing:** staged six-swap, rejected (MODERATE). Biotransference makes Karlach, Shaun and the clones artifacts and makes Necrons.
- **Combat Celebrant over Thought Monitor:** seven-swap, staged, rejected. It is a redundant extra combat that exerts.
- **Rejected singles:** Hexplate Wallbreaker (vs Biotransference), Mechanized Production (vs Doomsday Confluence; the owner already cut it), Rising of the Day (vs Swiftfoot Boots), Reckless Fireweaver (vs Thopter Spy Network), Cryptothrall (vs Padeem), Mirror Box (vs Sakashima), World at War (vs Full Throttle), Foundry Inspector (vs Fellwar Stone), Weeping Angel (vs Baleful Strix). Excluded: Grand Abolisher (white).

## Limits
Only finite rules cases and bounded enumerations are tested. Main losses:
- The myriad package (Cybermen Squadron + The Master, Multiplied), including the Master's token protection.
- Spyder's nontoken-entry draws and Omnitool's artifact dig.
- Anrakyr's free artifact casting.
- One of three artifact reducers.
- Creatures 30 → 28. Average nonland MV 3.354 → 3.338.
