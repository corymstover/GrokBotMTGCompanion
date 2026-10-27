# Deck 50 — Sauron, the Dark Lord — M7 Rev1 owner-review research

**Status:** NOT owner-approved, NOT canonical. The October 15 approved/locked
100 remains authoritative pending Cory's explicit exact-SHA approval.

Canonical source: `corymstover/grixis-commander-encyclopediaGPT/main/refinement/decklists/Sauron_the_Dark_Lord_Approved_2026-10-15.txt`;
exact raw SHA-256 `fab194f69a6e15b83679c1419f88ba6fdd56cd9527946cb94a6d8efe23a7dfc8`.
Candidate exact raw SHA-256 `266660c6a3241c07a052da7624366be1f9617cb5db4c35c422b0e8f828977d9b`.
Live October 27, 2026 canonical registry still APPROVED/LOCKED on the old SHA.

## Distinct commander plan

Sauron is a six-mana **opponents-cast-spells** amass engine, not another generic
turbo-combo or the eight-mana cast-trigger reanimator Sauron from Deck 49.
An Army hitting a player causes the Ring to tempt, which can trigger Sauron's
optional discard-whole-hand/draw-four. Seven Nazgûl grow Wraiths on each
temptation. The revision makes the **existing Orc Army a Wraith**, turns its
counters into unblocked attacks, and converts the entire-hand discard into
mana, damage, future card access or selection rather than relying on
three separate symmetrical board sweeps.

Natural ceiling: **Bracket 4 — Optimized**, not a proven cEDH list.
Tags: **Amass Orcs / Ring Temptation / Wraiths**.

## Ten proposed changes and real losses

| Cut | Addition | Benefit and opportunity cost |
|---|---|---|
| Saruman, the White Hand | **Arcane Adaptation** | Choosing Wraith lets every Nazgûl's temptation trigger put +1/+1 counters on the Orc Army and all controlled creatures. Costs the useful four-mana independent amass-on-own-noncreature-spells engine. |
| Sauron, Lord of the Rings | **Lord of the Nazgûl** | Replaces an eight-mana alternate commander with a five-mana Wraith lord that creates 3/3 Wraiths from our instants/sorceries and makes nine Wraiths into 9/9s. Loses dramatic Sauron reanimation on cast and a premium graveyard target. |
| Moria Scavenger | **Bone Miser** | Each card discarded to Sauron's optional reset can yield mana, a token or replacement draw by card type. Costs a flavorful Orc combat/graveyard-value body and requires five mana for the new setup. |
| Sauron's Ransom | **Moonstone, Harsh Mistress** | Optional exile of each discarded card allows it to be played through next turn, letting Sauron's draw-four replace a hand without losing all castable resources. Loses a three-mana instant-speed political card selection spell, and exile conflicts with reanimation unless declined. |
| Summons of Saruman | **Glint-Horn Buccaneer** | Turns each card discarded on a Ring temptation into one damage to EACH opponent, and supplies a haste threat. Loses potentially explosive but X-hungry Army-making/self-mill/free-spell sorcery. |
| The Ozolith | **Herald of Secret Streams** | Makes an amass-built Army unblockable as soon as it has a +1/+1 counter; Arcane Adaptation also gives counter-bearing Wraiths unconditional access. Costs Ozolith's cheap counter conservation through board wipes and requires a four-mana vulnerable creature. |
| Widespread Brutality | **Lazotep Plating** | Two-mana instant protection makes you and permanents hexproof and amasses Zombies 1 on the same Army. Removes one Army-powered creature sweep (which also hits our own Wraiths). Does not protect against untargeted board wipes. |
| Windfall | **Birthday Escape** | One blue mana draws one and tempts the Ring; with Sauron it may also become an optional draw-four and Nazgûl-wide pump. Removes a potent wheel and its Sheoldred/Archfiend synergies; Wheel of Fortune remains. |
| Rogue's Passage | **Cavern of Souls** | Names Avatar to provide colored uncounterable Sauron casting, instead of a four-mana unblockable land activation competing with engine development. Does not make Wraiths uncounterable when Avatar was chosen, and reduces evasion redundancy if Herald is removed. |
| Blasphemous Act | **Soothing of Sméagol** | Two-mana instant bounce of any target nontoken creature plus a Ring temptation, including the ability to reuse our own Bilbo or Nazgûl ETB. Loses a cheap mass-clear against crowded boards, leaving Toxic Deluge and Cyclonic Rift as broader emergency outs. |

These ten are qualitative commander-identity upgrades, not proof of a numerical
win-rate increase. They are not a swap quota. If new Oracle, interaction or
mana evidence falsifies a tradeoff, the candidate must be revised and rehashed.

## Whole-99 roles and challenged incumbents

All 99 baseline noncommander physical cards were reconsidered against the
commander's expected play patterns. The preserved core comprises:

- **Seven Nazgûl + Ring enablers:** Call of the Ring, Bilbo (both ETB and LTB tempt), In the Darkness Bind Them (three chapter temptations and Wraiths), Claim the Precious, Ringsight, Witch-king, and The One Ring. All are worth protecting; The Ring can tempt even when no Army hits.
- **Army production and conversion:** Sauron; Great Goblin, Foul-Hearted; Mauhúr; The Great Goblin; Orcish Siegemaster; March from the Black Gate; Barad-dûr; The Black Gate; Minas Morgul; Roaming Throne. The Nazgûl/Army bridge gains importance under Arcane Adaptation.
- **Mana and six-drop access:** 34 physical lands, typed duals/fetches, Ancient Tomb, Mana Vault, Sol Ring, Arcane Signet, all Talismans, Jeska's Will, Dark Ritual, Relic of Sauron, and Black Market Connections. Cavern is land-for-land, not an extra land. Relic's expensive fixing/looting remains thematic insurance.
- **Disruption/protection:** Force of Will, Mana Drain, Fierce Guardianship, Deflecting Swat, Swan Song, Saruman's Trickery, Deadly Rollick, Feed the Swarm, Cyclonic Rift, Toxic Deluge, Orcish Bowmasters. Replacing sweepers invites creature-swarm risk, but reduces self-destruction of the Wraith army.
- **Card advantage/recursion:** Rhystic, Remora, Sheoldred, Wheel of Fortune, Entomb, Anger, Wonder, Reanimate, Animate Dead, Victimize, Living Death. Retain the low-cost recursion with enough high-value midrange targets; lack of the eight-mana Sauron reduces top-end reanimation ceiling.

Additional **named, nonselected slot challenges** beyond the ten cuts:

1. **Relic of Sauron → Fellwar Stone:** would accelerate colored mana earlier, but loses repeatable discard to stock Anger/Wonder, a UBR source insulated from opponent land colors, and an iconic flavor asset. `RETAIN_ALTERNATIVE`.
2. **Orcish Siegemaster → Cover of Darkness:** with Wraith chosen, grants Wraith fear without waiting for Herald, but removes an independent Orc/Army combat engine and can be blocked by black creatures. `RETAIN_ALTERNATIVE`.
3. **Black Market Connections → Dimir Signet:** faster two-mana colored fixing, but loses Treasure plus repeatable cards and Changeling body to power the deck. `REJECT`.
4. **In the Darkness Bind Them → Gollum, Patient Plotter:** efficient two-mana repeatable death-based temptation, but the saga supplies THREE guaranteed Wraith tokens + Ring events and potential late creature theft. `RETAIN_ALTERNATIVE`.
5. **Toxic Deluge → Orcish Medicine:** one-mana thematic protection/amass, but removing the final reliable mass destroy/−X effect exposes the combat army to token stalls. `REJECT`.
6. **Call of the Ring → Phial of Galadriel:** the Phial offers draw/hand-size mana value, but the upkeep temptation is the only unconditional low-cost repeated Ring enabler. `REJECT`.

Other sourced candidates judged and not adopted: Sam's Desperate Rescue
(cheap creature recursion plus Ring tempt but narrower than Victimize's
two returns); One Ring to Rule Them All (chapter II kills nonlegendary
Nazgûl/support); Ringwraiths (six-mana body too slow); Sauron, the
Necromancer (five-mana attack/death setup competing with Lord); Shadow
of the Enemy (graveyard theft depends on opponent matchup); Shadowspear
(efficient trample/lifelink but duplicates Great Goblin while lacking
Herald's true unblocked army); Orcish Medicine (does not protect board
from targeted non-destroy control); Cover of Darkness (Arcane-dependent,
black blockers survive); Gollum, Patient Plotter (temptation needs death
or sacrifice, less autonomous than saga); All Will Be One (damage ceiling
but generic counter-burn approach over theme); and automatic Breach/
Oracle/Consultation (violates identity/no homogenization).

EDHREC candidate discovery, read October 27, 2026, with no bracket
filter: <https://edhrec.com/commanders/sauron-the-dark-lord> Top Cards
had Call of the Ring at 78% inclusion/9.5 Lift, Nazgûl 59%/11 Lift,
and Ringsight 58%/8.1 Lift. High Lift featured Gollum, Patient Plotter
22%/11 Lift, Birthday Escape 26%/10 Lift, One Ring to Rule Them All
38%/10 Lift. Theme pages reviewed:
<https://edhrec.com/commanders/sauron-the-dark-lord/the-ring>,
<https://edhrec.com/commanders/sauron-the-dark-lord/orcs>,
<https://edhrec.com/commanders/sauron-the-dark-lord/core/wraiths>.
Metrics discover candidates, not establish strategic dominance.

## Two complete strategic package comparisons

**A — selected ten-swap 100:** retains the old saga/Bilbo/Call and
seven Nazgûl, replaces the slower value and sweep-heavy fringe with
Arcane/Herald/Lord Wraith growth, cheap Ring triggers, and three discard
payoffs. Worst case: creature-centric engines are removed repeatedly and
hand exile under Moonstone strands expensive spells.

**B — twelve-swap extended evasion/mana package:** the exact A 100 plus
`Cover of Darkness / Orcish Siegemaster` and `Fellwar Stone / Relic
of Sauron`. Trades independent Army combat identity and discard/colored
Relic for more evasion and faster rock. This is a *credible larger search
configuration*, not evidence that two additional swaps are better. Its
combat line is more vulnerable to losing Arcane's Wraith typing and it
gives up Relic's discard/Anger-Wonder enabler.
Full 100-card alternative: `sauron_dark_lord_alt12.txt`, raw SHA-256
`093ca97894cf29774505b7d97eccaf29f5b2fbb7ab6e39cda2bdf6876cebb9e7`.

**C — low-setup recurring temptation alternative:** the exact A 100,
except `Gollum, Patient Plotter / Moonstone, Harsh Mistress` and
`Sam's Desperate Rescue / Bone Miser`. More turn-two tempt/creature
recursion at the cost of real repeatable hand-discard economics once
the six-mana commander lands. Good against decks killing small bodies,
weaker when Sauron survives a full turn cycle.
Full 100-card alternative: `sauron_dark_lord_alt_early_ring.txt`, raw SHA-256
`ae88c6e4885a23100380b6691eadaefd9cb643d35c4e765231aeeba978927991`.

Post-floor search conclusion: the retained cards each beat their
named challenger on at least one valuable independence, mana-color,
tempo, repeated Ring, or Army-protection function. No extra swap was
included simply to reach a count. The strongest remaining challenge
is whether Fellwar's commander speed outweighs Relic's themed looting;
the list preserves Relic pending measured color-access evidence.

## Mechanical, legality and provenance boundary

Local structure PASS: old and candidate raw hashes; physical 100,
91 distinct names, 34 lands, repeats only 7 Nazgûl/3 Swamp/2 Mountain,
ten 1-for-1 changes and identity core. Nazgûl explicitly allows up to
nine copies under card Oracle; no project exceptions. UBR and official
Commander legality require CI's *live collection* check of all 91 names.

Bounded deterministic fixtures cover Sauron ward, spell-cast timing,
Mauhúr counter replacement, Great Goblin event counts, Roaming Throne
choice, 7-Nazgûl temptation, Minas Morgul, combat-only Ring,
quiet opponents, sweeper loss, and candidate Arcane/Herald/Moonstone/
Cavern interaction negatives. These are narrow source-bound state
probes; **not** a multiplayer win-rate sample, not a universal Magic
engine, and not blanket certification of all required external M6 P0/
I-J test plans. Prior M6 blueprint is design-only; the actual full
case-level receipt and final-source I/J correspondence remain a
separate hard-gate reconciliation.

The historical October 15 canonical lock remains untouched. Do not
represent this research PR as Cory's approval or automatic M8 acceptance.
