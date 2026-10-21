# Abaddon — targeted Phase B Neheb / Aggravated Assault / Loyal Subordinate evidence

**Date:** 2026-10-21 (America/Chicago)  
**Deck:** `Abaddon_the_Despoiler`; original canonical approved/locked raw SHA-256 `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`.  
**Candidate only, NOT APPLIED:** +1 **Aggravated Assault**, -1 **Rakdos, Lord of Riots**.  
**Prerecorded contract:** `data/grixis/m6/phase_b_plans/abaddon_neheb_assault_20261021.json`, committed before the fixture as `346bfa82e5b0b58e51dbb1f43b14284b193d9833`.  
**Executable evidence:** `scripts/grixis_m6_abaddon_neheb_assault.py`; ten adversarial unit tests in `tests/test_m6_abaddon_neheb_assault.py`. Initial exact-head run on `2dde3fbcd675686f305a3abb09c5796ce393df13`: [GitHub Actions 39692625675](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/39692625675), conclusion **success**. Merge requires this document's new exact PR-head CI too.

## Bounded outcomes

These are **effect-aware deterministic rules fixtures**, not paired full-deck games, goldfish win estimates, opponent-policy samples, or multiplayer win percentages.

1. **Legal postcombat repeat route:** with Abaddon, Loyal Subordinate, Neheb, and Assault already controlled, three opponents at 40 life, and no interaction, the first combat's Loyal trigger drains **3 per opponent (9 total)** even if nobody attacks. Neheb's first postcombat trigger makes **9 red**, enough to pay Assault's **{3}{R}{R}**; four leftover red expire on entering the extra combat. Its Loyal trigger contributes another 9 cumulative loss; the next postcombat Neheb trigger gives **18 red**. A continued unopposed deterministic route reaches 14 combat beginnings and 13 activations to make all three opponents lose the game. This is a **conditional line**, not a measurable outcome probability.
2. **Five-red floor and nonlethal loops:** if any scripted, legitimately sourced opponent loss totals at least **five that turn**, Neheb can generate at least five red after every extra combat's postcombat main, paying Assault repeatedly while both permanents remain; with no attacking damage or repeat drain, arbitrarily many combats **do not themselves win**. We test three additional combats under this finite no-damage assumption, without claiming the extra loss source's access frequency.
3. **Key interaction vulnerability:** if Abaddon is absent before Loyal triggers, or leaves in response before its intervening-if trigger resolves, there is **no Loyal drain**. Removal of Loyal *after* it triggers does not erase its trigger if Abaddon remains. Removing Neheb before a postcombat main prevents that main's Neheb trigger; removing Neheb after that trigger is on the stack still allows the already-created mana trigger to resolve, but not future postcombat triggers.
4. **Ability/timing:** Assault activation pays five actual red in a main-phase empty-stack window. Removal of Assault after activation does not erase an already-activated ability. One activation per postcombat main is a **test policy**, not a rules-imposed universal limit. Early/precombat activation and other timing variants are explicitly outside this fixture.
5. **Resource reset and prevention:** unspent red mana empties between phases; previous-turn opponent life loss does not carry into Neheb's next-turn calculation. A combat damage fog does not stop Loyal's **loss of life**, which is not damage.

**Source grounding:** [Wizards' Wilds of Eldraine release notes, Aggravated Assault](https://magic.wizards.com/en/news/feature/wilds-of-eldraine-release-notes); [Wizards' Commander Masters release notes, Neheb and lieutenant timing](https://magic.wizards.com/en/news/feature/commander-masters-release-notes); [Scryfall Oracle: Loyal Subordinate](https://scryfall.com/card/plst/SCD-90/loyal-subordinate).

## Adversarial assessment and what remains unresolved

The candidate has a **real, payable, commander-relevant payoff** already synergistic with Neheb and Loyal Subordinate. The prior Pass C `NEEDS TESTING` designation was justified; previous broad proxies did not model this engine.

This evidence **does not establish superiority over Rakdos**. Rakdos remains a {B}{B}{R}{R} 6/6 flying trampler and, after opponent life loss, discounts creature spells; removing it can slow natural Warhammer creature/exile engines. Assault can be a dead enchantment without Neheb, enough other red sources, or a way to profit from extra combats; commander and subordinate are removable. Even a legally infinite empty-combat loop need not win. The fixture hardcodes pieces already on battlefield, does not estimate 100-card access, colored mana, opponent responses, tutor tradeoffs, full cascade consequences, side effects, or baseline/challenger comparative outcome distributions. Do not use the 14-combat trace as a turn-to-win metric.

**Decision status:** `NEEDS_TARGETED_ACCESS_AND_ROLE_COMPARISON`; no swap approval or certification. Highest-value next bounded test is matched-baseline-versus-challenger **real approved 99-card opening hand and turn access**, legal U/B/R mana development for five-MV Neheb and Assault, and resilience under targeted removal/Rule of Law. If available infrastructure cannot model the actual challenger payoffs, label it a source-access proxy, not a Phase B win rate.

**Authority:** unchanged 62/62 APPROVED/LOCKED canonical baselines, no new M7 user approvals, no formal Phase B deck certificate, no I/J zero-improvement, no M6 or M7 acceptance. Original independent third-model gate still not completed.
