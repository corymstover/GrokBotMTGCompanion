# Deck #55 — Tetsuo, Imperial Champion — M7 Rev1 owner packet and source-bound review

2026-10-27 · Cycle `global-restart-2026-10-13` · **REVIEW ONLY, not approved or canonically applied**.

## Pinned authority

- Canonical predecessor: `corymstover/grixis-commander-encyclopediaGPT/main`, `refinement/decklists/Tetsuo_Imperial_Champion_Approved_2026-10-15.txt`, blob `1049ea399013f9633c0aeae998139f8218ce75a2`, 100 physical, 91 names, SHA-256 `d6d7561f00cb56cfb86cd79024975130d718ddc7f3a1bddf0c62f61dc422822e`.
- Exact new candidate: `data/grixis/m7/candidate_lists/Tetsuo_Imperial_Champion_M7_Rev1.txt`, 100 physical, 93 names, SHA-256 `36890584524fb32d038ba27926af663dc98197f06f87d84a08282ce1f3fb29db`.
- 13 genuine physical substitutions; Island x4, Mountain x4, Swamp x2 only repeats; 35 lands. Preserves original approvals and exceptions. Commander has U/B/R identity; no project exception.
- Natural power ceiling **Bracket 4 — Optimized**, Archidekt tags **Equipment / Free-Cast Spells / Extra Combats**.

## Identity and decisive choice

Tetsuo must attack while equipped. His one attack trigger chooses either direct **noncombat** damage equal to the greatest attached Equipment's printed mana value or a free instant/sorcery from hand at/below that ceiling. The new package turns difficult-to-attach gear into a realistic attacking engine while multiplying Tetsuo's native burn into infect/damage lines and improving repeat combat. Original attack timing, color access and Free-Cast Spell suite remain central. This is not a generic Grixis turbo shell.

## All thirteen exact changes and downsides

1. **+Karlach, Fury of Avernus / −Akki Battle Squad:** Karlach costs five rather than six, grants first strike and works without checking modification; trades away a Samurai body.
2. **+Drach'Nyen / −Argentum Armor:** Both equipment are MV6, but Drach'Nyen exiles an enemy creature on entry and equips for two; lose repeatable any-permanent destruction.
3. **+Jeska's Will / −Brainstorm:** A normal main-phase Will accelerates equipment, and free-casting during attack grants end-turn access to three cards; attack-step red mana cannot be banked for the main.
4. **+Firion, Wild Rose Warrior / −Heiko Yamazaki, the General:** Firion supplies haste and duplicates nonlegendary equipment for a turn to reduce equip costs; loses persistent artifact recursion.
5. **+Otawara, Soaring City / −Island:** Untapped U land offers discounted legend-enabled bounce interaction; loses a fetchable basic.
6. **+Tainted Strike / −Kediss, Emberclaw Familiar:** Kediss only spreads combat damage, not Tetsuo's attack-trigger burn; Strike can give that burn infect in response for a lethal 10-poison line.
7. **+City of Brass / −Smoldering Marsh:** Any-color untapped mana improves three-color setup; costs life and loses a typed fetch target.
8. **+Shizo, Death's Storehouse / −Swamp:** Untapped B plus one-mana legendary fear helps commander land combat-damage Equipment triggers; loses basic Swamp fetch/resilience.
9. **+Mjölnir, Hammer of Thor / −Sword of Fire and Ice:** Mjölnir is attachable to red legendary Tetsuo for one and doubles his attack-trigger damage; lose on-hit draw and two damage.
10. **+Demonic Tutor / −Terminate:** Tutor can find exact Equipment, attach cheat, infect payoff or protection; lose efficient two-mana creature removal.
11. **+Grafted Exoskeleton / −The Reality Chip:** Infect makes Tetsuo's triggered noncombat damage a direct poison win route; loses top-deck spell access and gains unattach-sacrifice risk.
12. **+Magnetic Theft / −Vorpal Sword:** R instant can attach expensive Equipment to Tetsuo before attack even without equip activation; loses eight-mana hit-to-kill activation.
13. **+Brotherhood Regalia / −Winged Boots:** Equip legendary one gives unblockable and ward two; loses flying and the larger ward from Winged Boots.

## Whole-99 and post-floor challenge

`Tetsuo_Imperial_Champion_M7_Rev1_99slot_ledger.csv` reconciles all 99 old library physical copies with case-level role commentary: **86 KEEP / 13 CUT**. It reuses October20 91-line independent authored role annotations (expanded only basics) and explicitly adjudicates every replacement. Already protected high-MV gear includes Excalibur, Kaldra, Embercleave and Genji/Hexplate; protected support includes Brass Squire/Hammer/Blacksmith Talent, Mystic Remora/Rhystic Study/Jhoira, free-cast suspends, Tetsuo-specific Samurai protection, and the Assault/Sword repeat-combat package.

After thirteen selected upgrades, **Padeem vs Combat Celebrant**, **Basilisk Collar vs Shadowspear**, **Sword of the Animist vs Bitterthorn**, **Kaldra vs Tatsumasa**, and **Chandra Ignition vs Sword of Wealth and Power** were still challenged. No upper bound or quota was used. Staged whole-100 alternate `alt14` (SHA `b42e1247a3fc1359e82221979477289a4ef51c351aa400adbb260a7884f6601d`) adds Combat Celebrant for Padeem; `alt15` (SHA `9a18706f85e5cc778f8620c7613f23fe3ba86abe43325e5365fc54af93f5fd5e`) further adds Sword of Wealth and Power for Chandra's Ignition. Both lose more core protection/target availability than they add on imperfect combats. This is a quality-based stopping rule, not a thirteen-swap target.

## Material rejected candidates

- **Sword of Wealth and Power:** Strong EDHREC inclusion and treasure/spell-copy payoff, but its protection from instants **prevents Tainted Strike from targeting its equipped Tetsuo**, and prevents Chandra's Ignition from targeting that same Tetsuo. It only copies spells after combat damage to a player.
- **Combat Celebrant:** A real three-mana extra-combat creature, but loses Padeem's Equipment hexproof/draw and must attack with a 4/1 exert creature.
- **Shadowspear:** Useful trample and hexproof/indestructible stripping, but Basilisk Collar gives deathtouch to Tetsuo's noncombat trigger, making otherwise-large creature targets die.
- **Ultima Weapon / Tatsumasa:** Respectively seven-mana equip and six-mana slow setup; neither improves the present enter-the-battlefield removal / cheap attach packages.
- **Temporal Manipulation / Expropriate:** Efficient only at sufficient Equipment ceiling and pull away from the attack/equip/extra-combat identity; Expropriate usually requires Excalibur.
- **Helm of the Host / Bladegraft Aspirant / Renowned Weaponsmith / Bitterthorn:** Need extra setup or duplicate effects already served more efficiently by current Equipment, protection or mana.

## Rule-specific source and adverse-case audit

1. Equipped condition is an intervening-if test on attack declaration and resolution. Excalibur's **printed MV12** remains twelve even after casting cost reduction.
2. **Magnetic Theft** must attach gear *before* declaring the first equipped attack if it is to create the trigger; it cannot retroactively fix an unequipped attack.
3. **Mjölnir** can equip Tetsuo for {1}, because Tetsuo is a red legendary non-Villain, and doubles all damage **Tetsuo** would deal, including trigger damage. **Grafted Exoskeleton** grants infect to that source. Excalibur MV12 plus Mjölnir plus Exoskeleton yields 24 poison counters on an unprevented target-player Tetsuo damage trigger; this is not commander-combat damage.
4. **Tainted Strike** works if {B} is paid in response to Tetsuo's selected burn-mode trigger before resolution. Tetsuo chooses ONE trigger mode; he cannot both cast Strike for free and burn through the same attack trigger. Mjölnir with attached MV5+ can make the B response lethal through infect.
5. **Firion** makes temporary token Equipment copies of *nontoken* arrivals and gives equipped creatures haste. Copying a legendary Equipment causes the legend rule; copies are sacrificed next upkeep. Especially **never equip Tetsuo with a Firion-created Grafted Exoskeleton token expecting it to persist**, because becoming unattached can sacrifice the equipped Tetsuo.
6. **World at War** cast during combat schedules the later combat after the *second main phase*; it is not Relentless Assault. Its rebound may trigger because Tetsuo casts it from hand. **Savage Beating** works in combat but entwine remains a paid additional cost.
7. **Jeska's Will** cast free during declare attackers exiles three playable cards for that turn, but mana produced then empties at the end of the step; to use the red mana to deploy Equipment, cast Will normally in a main phase.
8. **Aggravated Assault / Sword of Feast and Famine** repeats only after player combat damage untaps enough lands that can pay {3}{R}{R} and the appropriate combat/attack condition occurs; blocked attacks and effects with replacement untap denial can break it. Reaver Cleaver Treasure is likewise damage/payable dependent.
9. **Drach'Nyen** exiles a target creature on entering and has an equipment MV6 ceiling with equip two. It does **not** replicate Argentum Armor's destroy-any-permanent trigger on every attack.

## Verification and scope

- **PASS:** Source raw SHA and staged candidate raw SHA, 100 physical, 93 distinct, land/basics, all 13 copy-accurate cuts/adds. Companion none.
- **PASS:** October 27 2026 public Scryfall Oracle Cards JSONL bulk (updated 21:02:43 UTC) downloaded once as a public GET and checked **locally** against all 93 exact names; all 93 have Oracle IDs, U/B/R or colorless identity, and official Commander `legal`. No deck inventory sent to the Scryfall API.
- **PASS, scoped:** 18 executed finite source/cost/phase C/K/E/W/F tests (command documented: `python3 data/grixis/m7/tetsuo_imperial_champion_rev1/verify.py`); these are not a full gameplay simulator or multiplayer win-rate trials.
- **PASS, structural:** `python3 scripts/grixis_m7_decision_gate.py --check --file data/grixis/m7/decision_reviews/Tetsuo__Imperial_Champion_rev1.json` — 13 swaps, 25 candidate decisions, whole-99 and post-floor alternative hashes; exact-head GitHub CI pending at authoring.
- **Unchanged historical limitation:** M6 P0/P1 blueprint originally design-only; its input-only I/J receipt explicitly records Phase B not replayed. This candidate's 18 bounded cases correspond to the main relevant trigger, free-cast, attack, infect, equipment and failure semantics, but do **not** retroactively certify M6 I/J or 62-deck milestones.

Only after an exact SHA approval may engineering merge and canonical approval/locking occur. The previous October15 source remains locked until that consent.
