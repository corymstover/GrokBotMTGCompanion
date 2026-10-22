# Admiral Beckett Brass — expanded evasion-horizon M7 reassessment (2026-10-22)

**Status: RESEARCH_ONLY / OWNER APPROVAL WITHHELD.** This is a supplemental, deliberately non-final research record following #604 and #605. Five swaps is a **minimum for owner presentation, not a search budget, optimization target, safe stopping point, or ceiling**. The previously presented five-swap deck remains withdrawn; the historical canonical source is still locked and unchanged. Neither the new six- nor seven-swap options below has completed changed-candidate Oracle/M6 I/J or received owner approval.

## New reason for further expansion

Admiral Beckett Brass is not a generic Pirate-damage deck: **three different Pirates must deal combat damage to the same opponent in a turn** to allow a targeted nonland-permanent theft at the beginning of your end step. Adding non-Pirate +1/+1 counters, land polish, or trigger-copy effects before enabling those three hits may be less important than obtaining an actual reliable three-source connection while keeping Admiral on the battlefield through the end-step trigger.

The earlier 6/6/7 source-complete research branch challenged March of the Drowned with Captain Storm, Cosmium Raider and Path of Ancestry with Shizo, Death's Storehouse. Neither directly assures the third unblocked attacker. This second horizon therefore adds an **independent axis**: repeatable single-Pirate evasion/protection, one-shot boardwide evasion, and whether the deck can afford to lose a card-draw engine or defensive Pirate-only wipe to gain those effects.

## Four additional *fully specified* 100-card physical research configurations

Each preserves all five replacements from the **WITHDRAWN** earlier D candidate and then makes the substitutions shown. Every file lists all 100 physical cards, commander included; the new exact-head regression test is responsible for auditing source deltas, card count, and retained approval freeze. These lists are **not proposals** until a comparative judgment and source-mechanical revalidation support one.

| Research configuration | Extra additions / cuts beyond D | Potential benefit | Material sacrifice / counterevidence |
|---|---|---|---|
| `six_Glaring_Spotlight` | **Glaring Spotlight** IN / **Bident of Thassa** OUT | {1} artifact plus {3}, sacrifice can make the whole current Pirate crew unblockable this turn and grant those creatures hexproof, a direct burst toward 3-on-one and possible protective combat swing | Permanently loses repeatable draw whenever a creature deals combat damage. Spotlight is a one-use effect and can be inert without enough Pirates or commander; it does not protect against mass non-targeted wipes |
| `six_Brotherhood_Regalia` | **Brotherhood Regalia** IN / **Bident of Thassa** OUT | {2} Equipment; equip a **legendary** Pirate for {1} to give ward {2} and unblockability, preserving Pirate type while adding Assassin. Repeatable source access / Admiral protection | Only one body connects automatically, unlike a mass evasion spell. It may just increase reliability of the first of three Pirate hits; loses draw engine and costs mana/tempo to equip |
| `six_Cosmotronic_Wave` | **Cosmotronic Wave** IN / **Fiery Cannonade** OUT | {3}{R} sorcery deals 1 to each opponent's creature and makes all of their creatures unable to block this turn: a full-team theft-enabling window regardless of blocker toughness | Fiery Cannonade is a cheaper **instant** dealing 2 to each **non-Pirate** creature, a superior reactive small-creature sweep. Wave is sorcery-speed and a single-use solution; opposition can respond before attackers connect |
| `seven_Regalia_Wave` | **Brotherhood Regalia** / Bident; **Cosmotronic Wave** / Fiery Cannonade | A coherent two-layer evasion package: durable single legendary-Pirate unblockability/ward alongside a burst turn for the entire team | Simultaneously weakens repeatable card advantage and an instant-speed blocker sweeper. Increasing the replacement total from five to seven is not independently positive |

Exact research paths:
- `data/grixis/m7/research_challengers/Admiral_Beckett_Brass_six_Glaring_Spotlight_20261022.txt`
- `data/grixis/m7/research_challengers/Admiral_Beckett_Brass_six_Brotherhood_Regalia_20261022.txt`
- `data/grixis/m7/research_challengers/Admiral_Beckett_Brass_six_Cosmotronic_Wave_20261022.txt`
- `data/grixis/m7/research_challengers/Admiral_Beckett_Brass_seven_Regalia_Wave_20261022.txt`

### Preliminary individual dispositions are non-final

- **Brotherhood Regalia — RETAIN_ALTERNATIVE (strong):** Realistic card-for-card challenge to Bident of Thassa, primarily because Admiral has to survive to the end step. The equipped legendary Pirate remains a Pirate, and the equip-legendary discount materially lowers the protection cost. It cannot generate the other two qualifying damage sources, so test the loss of Bident's multi-hit cards over repeated turns.
- **Glaring Spotlight — RETAIN_ALTERNATIVE (strong):** Unlike a power pump, actually grants mass unblockability during the decisive combat. The sacrifice effect is not a repeatable engine, and its hexproof does not prevent an untargeted sweeper. Compare with `Open into Wonder`, which can already grant three qualifying attackers unblockability for X=3 at five total mana while producing cards on successful hits; Spotlight is cheaper to install, its sacrifice activation is cheaper in the attack turn, and protects current creatures.
- **Cosmotronic Wave — RETAIN_ALTERNATIVE (conditional):** Has commander-specific upside on high-toughness blocker boards where Cannonade's two damage does not clear any blockers. But a deck that needs emergency reactive instant-speed sweeps may be worse with Wave. Analyze that opposition model, not just a goldfish connection count.
- **Subira, Tulzidi Caravanner — REJECT for current primary packages:** Each paid {1} evasion activation covers **one other creature of power 2 or less**. Admiral's +1/+1 Pirate anthem turns ordinary base-2-power Pirates into power-3 creatures and makes them ineligible while Admiral is on the battlefield. A non-Pirate three-mana support creature that cannot force all three hit sources efficiently is not a clearly stronger fit than the actual mass-evasion options. Revisit only if a count of eligible power-1 Pirates and atypical board states changes the assessment.
- **Teleportal — RETAIN_ALTERNATIVE, not a selected test package:** Overload {3}{U}{R} makes all your creatures unblockable and gives +1/+0. At exactly three chosen Pirates, existing `Open into Wonder` already uses X=3 and {U}{U} (five mana total), gives three unblockability, and draws up to three cards. Teleportal improves boards of four or more eligible attacking creatures, but the relevant Admiral trigger threshold is three and the deck needs card access. It merits protection from automatic inclusion based on the word 'overload'.
- **War Cadence — UNRESOLVED RESEARCH LEAD:** Repeatable blocker tax may offer meaningful board-wide evasion but its actual Oracle, X cost and opponents' discretionary payment must be proven before strategic selection. It has not been included in a package.
- **Strionic Resonator, Molten Echoes, Amphin Mutineer — RETAIN_ALTERNATIVE pending prior documented stack, token and hit-source constraints:** They may improve theft conversion, token count or interaction, but do not erase the requirement to connect three separate Pirates to the *same* opponent. The stage-1 source docket remains authoritative for their precise risks.

### Source discovery; not full final Oracle certification

- Glaring Spotlight: https://scryfall.com/card/gtc/229/glaring-spotlight — its printed/current rules include an activated **{3}, sacrifice** effect to provide hexproof and unblockability until end of turn.
- Brotherhood Regalia: https://scryfall.com/card/acr/255/brotherhood-regalia — the equipment grants ward {2} and unblockability, adds Assassin without replacing Pirate, with **equip legendary creature {1} / equip {3}**.
- Cosmotronic Wave: https://scryfall.com/card/clu/129/cosmotronic-wave — {3}{R} sorcery, 1 damage each opposing creature, opposing creatures cannot block this turn.
- Teleportal: https://scryfall.com/card/mm3/193/teleportal — overload {3}{U}{R}.
- Subira, Tulzidi Caravanner: https://scryfall.com/search?q=%21%22Subira%2C+Tulzidi+Caravanner%22 .
- Baseline Open into Wonder official Amonkhet players' guide: https://media.wizards.com/2017/images/magic/amonkhet_players_guide-en.pdf .
- Merchant Raiders official card https://gatherer.wizards.com/CMR/en-us/81/merchant-raiders ; this is a **protected Pirate tap-lock enabler**, not a gratuitous extra cut to fabricate more swaps.

These references establish promising card text for research; new source-bound current legality, full Scryfall record, exact deck legality and candidate-specific source snapshots are **outstanding**.

## Mechanical and game-state evidence still owed

1. **Three Pirate sources:** Construct at least two legal boards with precisely three Pirates aimed at one opponent, including adversarial blockers, and compare D against each six/seven variant. Distinguish *damage by three Pirate sources to the player* from just declaring attacks, token attacking, or aggregate combat damage.
2. **Glaring Spotlight exact timing:** Show payment of the three generic activation cost, sacrifice, pre-blockers timing, and creature effects for a live board with Admiral. Compare one-shot payoff versus losing Bident draws over later turns; remember hexproof from Spotlight covers current creatures, not necessarily future arrivals.
3. **Regalia exact timing:** Show two-mana artifact cast, one-mana equip onto an actual legend (or generic equip {3} on nonlegend), ward payment/target restriction, and unchanged Pirate creature subtype. Judge whether keeping one key Pirate unblocked materially gets the third source online.
4. **Cosmotronic Wave versus Fiery Cannonade:** Compare against 2-toughness blockers at instant-speed, a five-toughness blocker, and opponent instant-speed interference. Treat two damage versus one damage and sorcery speed as real losses.
5. **Candidate-bound M6 I/J:** Existing receipts cover previously frozen D and other older variants. No rebranding those as proofs of these new exact 100-card lists. Complete changed Oracle/legality, source binding, P0/P1 and necessary I/J when a best-supported whole-deck package is selected.
6. **Real qualitative optimization:** Examine whether a larger package truly improves cross-turn theft conversion, mana/draw and resilience relative to both canonical and the withdrawn five-swap candidate. No fixed target at 5, 6, 7 or 8. Reject harmful substitutions even when they would satisfy a bigger count.

**Current honest conclusion:** Multiple additional *credible* strategically distinct cards and configurations exist; the former exactly-five-swap stopping point was premature. The improvement ranking remains **UNVERIFIED / RESEARCH_ONLY**, and Cory has explicitly withheld new Admiral owner approval.
