# Deck #54 — Tetsuo Umezawa — M7 Rev1 owner review (2026-10-27)

**Status:** Engineering review only, not owner-approved. Original October 15 canonical 100 remains APPROVED/LOCKED at raw SHA `14ca66ceae4d634630a85aa1787731cfe840fd9fc2093bc37ad5dc17d1539ff6`. Do not merge or modify canonical until Cory explicitly approves the exact new raw 100-card hash.

- Candidate: `data/grixis/m7/candidate_lists/Tetsuo_Umezawa_M7_Rev1.txt`
- **Proposed raw SHA-256:** `e00196135931bde6e380e47d5ffe9e4360d4756f00ad083ee5ed0757919fddd7`
- **100 physical; 93 distinct names; 35 land-faced cards plus Sink into Stupor MDFC; 19 honest swaps** (12 nonlands + 7 color/function lands). Island x3, Mountain x3, Swamp x4 are the only duplicates.
- Natural ceiling: **Power Bracket 4 — Optimized**. Tags: **Tap/Untap / Forced Combat / Activated Abilities**.

## Commander's actual mechanic

Tetsuo costs `{U}{B}{R}` and has `{U}{B}{B}{R}, {T}`: destroy target **tapped or blocking** creature. An untapped blocker is valid. A goaded creature does not immediately become tapped and vigilance can keep it untapped through attacking. Target legality is checked at activation and resolution, and friendly Aura SPELLS cannot target Tetsuo; Equipment can. Almost every useful repeated activation requires four real colored pips, an untapped Tetsuo who may use tap abilities, and a legal target. This is the original Tetsuo, not Imperial Champion.

## Nineteen decisions — the actual complete list, not a quota

| Cut | Add | Why it wins and what we lose |
|---|---|---|
| Rings of Brighthearth | **Battlemage's Bracers** | An equipped Tetsuo copies the UBBR destroy activation for one extra generic rather than Rings' two; haste on the equipped creature also handles a recast. Downside: Requires casting a three-mana red artifact and paying equip two, whereas Rings can copy activated abilities of other permanents without equipping. |
| Mountain | **City of Brass** | Any-color land supplies whichever activation pip is missing instead of a fifth single-red basic, especially the second black. Downside: Costs one life whenever tapped for mana and is vulnerable to nonbasic-land hate. |
| Propaganda | **Deflecting Swat** | With Tetsuo controlled, redirecting an opponent's targeted removal or stack interaction while retaining UBBR for activation is stronger than a three-mana passive attack tax. Downside: Does not stop board wipes, untargeted removal or an attack in a two-player endgame; Propaganda was a defensive floor. |
| Dark Ritual | **Dramatic Reversal** | At instant speed readies Tetsuo plus all nonland permanents, and with Isochron Scepter and productive colored rocks creates repeatable mana/untap access rather than one black burst. Downside: Alone it requires an established board and does not untap lands; one-shot Dark Ritual could accelerate a black-heavy early turn. |
| Counterspell | **Fierce Guardianship** | A free noncreature counter when Tetsuo is present preserves all four colored mana to destroy threats while answering interaction. Downside: Cannot counter creatures and costs 2U when the commander is absent, unlike Counterspell's unconditional UU. |
| Sulfur Falls | **Forbidden Orchard** | Turns conditional U/R dual into untapped U/B/R source for Tetsuo, and Spirits given to opponents can later be goaded or destroyed once tapped. Downside: Every activation gifts an opposing 1/1 flying token; those tokens may pressure us and enter untapped. |
| Geode Rager | **Icy Manipulator** | Four-mana artifact can pay one and tap an active utility creature during an opponent's upkeep, then make Tetsuo's destroy ability immediately relevant; Geode costs six plus a future landfall. Downside: Single target at once and one-mana extra activation; loses Rager's repeatable entire-player goad and first strike body. |
| Brainstorm | **Isochron Scepter** | Imprinting Reversal converts the existing colored-rock suite into repeated Tetsuo and rock untaps, potentially positive colored mana with three or more mana per iteration. Downside: Two-card setup needs an instant in hand and multiple productive rocks; Brainstorm gave immediate one-blue selection with fetch shuffles. |
| Fumiko the Lowblood | **Life of the Party** | Four-mana creature supplies each opponent a permanently goaded hasty first-striking trample token, and the tokens become tapped Tetsuo targets when they attack. Downside: Gives real threats to opponents, and tokens can attack Cory in endgame or when other opponents cannot be attacked; Fumiko forced every opposing creature to attack. |
| Mountain | **Mana Confluence** | Trades a second redundant single-red basic for immediately available blue or double-black pips, addressing the actual UBBR bottleneck. Downside: Requires paying life for every colored tap and increases exposure to nonbasic hate. |
| Island | **Morphic Pool** | In multiplayer the UB dual supplies either blue or an additional source for Tetsuo's double-black activation where an Island could only supply blue. Downside: Enters tapped in heads-up play or after opponents have been eliminated; fewer fetchable basics remain. |
| Island | **Otawara, Soaring City** | Retains blue land function and adds a Tetsuo-discounted channel bounce for untapped creatures, artifacts, enchantments or planeswalkers when removal must stay open. Downside: Channel needs available mana and losing a basic slightly weakens basic-search and nonbasic-hate resilience. |
| Sly Instigator | **Puppet Strings** | Artifact is usable the turn it enters to tap any creature for a Tetsuo target or untap Tetsuo for another payable activation, without a sick creature body. Downside: Two mana per activation and only one target; Sly's persistent goad and evasion manipulation could be superior in a slow political table. |
| Xantcha, Sleeper Agent | **Rhystic Study** | Opponents' spells now generate either cards or mana taxes; keeps removal/protection available without giving opponent cards as Xantcha's activated draw can. Downside: The trigger can be paid for and Study is a generic Grixis power card; Xantcha created a distinct shared political damage outlet. |
| Swamp | **Takenuma, Abandoned Mire** | Preserves B production and channels back a lost untap creature such as Aphetto Alchemist or Puppeteer, with a discount while Tetsuo is on board. Downside: Milling three may be undesirable in some draws, and it is a nonbasic rather than an easily searched basic Swamp. |
| Grenzo, Havoc Raiser | **Thornbite Staff** | Each creature killed by Tetsuo normally dies, untapping the equipped commander for another payable UBBR activation; extra death events also reset him. Downside: Equip four and no extra colored mana make setup costly; Grenzo's two-mana body could goad or generate card access through combat connections. |
| Blasphemous Act | **Toxic Deluge** | For three mana and X life, X=2 clears small utility creatures while Tetsuo stays a 1/1 until end of turn; Act's 13 damage kills our whole tap/untap setup. Downside: Paying life can be severe against large creatures and Deluge may leave high-toughness threats without a high X. |
| Urabrask the Hidden | **Uphill Battle** | Three-mana enchantment makes creatures played by opponents enter tapped two turns sooner than Urabrask's five-mana symmetrical haste/entry lock, so new utility creatures start as legal Tetsuo targets. Downside: Does not grant our team haste and does not cover every token entering; Urabrask's broader two-sided effect wins some high-mana games. |
| Swamp | **Urborg, Tomb of Yawgmoth** | Retains black land production and makes fetch/utility/color lands capable of producing B for repeated UBBR activations, substantially increasing second-black reliability. Downside: It is nonbasic, may strengthen opposing mana bases, and removes one basic Swamp from the deck. |

## Full source and post-floor audit

The original 99 noncommander physical copies were each reconciled against the October 20 M6 comprehensive authored role table in `Tetsuo_Umezawa_M7_Rev1_99slot_ledger.csv`: **80 KEEP / 19 CUT**. Named retained roles include Aphetto Alchemist, Illusionist's Bracers, Flood, Puppet/Trapper tap, Minamo, Stone/Seal/Elixir/Sting, Karazikar/Firkraag/Kardur/Vengeful goad, Bloodthirsty Blade/Shiny Impetus, Verity Circle, Borrowing 100,000 Arrows, Bedevil, Chaos Warp, Mana Drain and colored fixing rocks.

The five-swap floor was not a stop. Our **complete 21-swap higher-count 100** `Tetsuo_Umezawa_M7_Rev1_alt21.txt` (SHA `f00107bb185625d66b5d2cdd140145a45830cf2c1d1f02ebfb73362d3f2e0941`) adds Vizier of Tumbling Sands and Nightscape Familiar by losing Rathi Trapper and Bedevil on top of the selected changes. That loses exact enemy-tap and artifact/planeswalker answers; Familiar's generic discount **cannot reduce UBR casting Tetsuo or UBBR activation**. The **complete 18-swap alternative 100** `Tetsuo_Umezawa_M7_Rev1_alt18.txt` (SHA `9f81a0269da93080400044daea725bf050f52abd36cff713e3b4536378f207a1`) keeps Geode Rager and Sly Instigator, uses Vizier over Rathi, and trades precise opponent-upkeep tap for slower political goad.

Additional material rejected or retained alternatives:

- **Vizier of Tumbling Sands** over Rathi Trapper: **RETAIN_ALTERNATIVE** — Rathi's cheap repeatable B tap directly manufactures legal targets; Vizier cannot tap opposing creatures and its cycling needs two mana plus discarded card.
- **Nightscape Familiar** over Bedevil: **RETAIN_ALTERNATIVE** — Tetsuo's cast cost UBR and destroy cost UBBR contain no generic symbols, so a spell discount cannot cure the central activation bottleneck; Bedevil answers artifacts/planeswalkers.
- **Stalking Assassin** over Royal Assassin: **REJECT** — Its tap costs 3U or kill 3B plus tap and summoning sickness, much slower than Royal Assassin's free kill and current Crown/Strings tap.
- **Ensnare** over Blustersquall: **REJECT** — It taps own Tetsuo too, the deck drops to three Islands, and bouncing lands worsens UBBR supply; Blustersquall overload spares Tetsuo.
- **Angler Turtle** over Firkraag, Cunning Instigator: **REJECT** — No goad-away rule and late seven-mana exposure, unlike Firkraag's attack-directed goad and card advantage.
- **Pemmin's Aura** over Aphetto Alchemist: **EXCLUDE_INVALID** — Tetsuo cannot be targeted by Aura spells; normal casting on him is prohibited, so the supposed direct commander untap package does not function.

EDHREC was used as discovery, never rules authority. On October 27 the [Tetsuo commander page](https://edhrec.com/commanders/tetsuo-umezawa) showed 162 total decks and High Lift for direct tap tools (e.g. Icy and Uphill Battle); [forced combat](https://edhrec.com/commanders/tetsuo-umezawa/forced-combat) and [tap/untap](https://edhrec.com/commanders/tetsuo-umezawa/tap-untap) tagged samples are small (10 and 3). The latter historic page labels a distinct old *synergy* metric, not October 2026 lift. Additional off-ranking Scryfall checks caught Reversal/Scepter, Staff/Bracers, Channel utility lands, and both alternative-cut packages.

## Payable mechanics and exact verification

- A ready Icy requires four to deploy, then `{1}, {T}` to create a tapped target; Tetsuo still pays `{U}{B}{B}{R}, {T}`. Unlike six-mana Geode, no later landfall/attack step is needed.
- Puppet Strings `{2}, {T}` can tap an enemy or untap Tetsuo, but cannot target friendly Tetsuo while Lightning Greaves gives shroud.
- Thornbite Staff requires equip `{4}`; a Tetsuo kill that actually **dies** can untap him, without refunding any colored mana or creating targets.
- Dramatic Reversal untaps **nonland** permanents. Imprinted under Isochron Scepter, paying 2 each cycle and untapping three or more mana from productive nonland rocks can generate a positive resource loop; colors still matter, and opposing removal/stax stops it. It is not guaranteed to win without a useful outlet.
- Aphetto Alchemist with Illusionist's Bracers and Arcane Signet can repeat copy-self-untap plus original-rock-untap to generate colored mana, but mana alone does not supply a legal Tetsuo target or untap Tetsuo.
- Uphill Battle makes *opposing played creatures* enter tapped; it is not a blanket effect on token creatures.
- Toxic Deluge at X=2 can remove enemy utility 2-toughness creatures while a 3/3 Tetsuo survives, at two life and reduced commander toughness for the rest of turn.
- Mana base retains 35 land-faced + 1 MDFC; every card remains commander-legal within U/B/R. Seven land changes directly improve U/B/B/R pip availability, with life/nonbasic-hate costs rather than aesthetic upgrades.

**Executed:** `python3 data/grixis/m7/tetsuo_umezawa_rev1/verify.py` gives 22 bounded finite, source/cost/scenario checks (corresponding to 14 C/K/E/W/F blueprint cases plus changed-card fixtures), and `--live` resolved all 93 distinct selected names through current Scryfall Oracle IDs, official Commander legalities and UBR color identity on October 27. These are scope-limited checks, not full Magic gameplay or win-rate simulations. **Historical M6 I/J receipt** `data/grixis/m6/ij/input_receipts/tetsuo-umezawa.json` remains `inputs_attested_downstream_incomplete` with `phase_b_replayed=false`; this is not a retrospective M6/I/J milestone certificate.

**M7 machine gate:** `python3 scripts/grixis_m7_decision_gate.py --check --file data/grixis/m7/decision_reviews/Tetsuo_Umezawa_rev1.json` passes locally. The duplicate basic-land cuts exposed an M7 schema shape bug: cuts must allow physical repeated basic copies while the original gate's `Counter` reconciliation still rejects cuts unsupported by the authoritative 100. CI must pass on the actual PR head before this review is presented as final owner-ready.

## Authority

Review PR only until exact owner approval. Existing canonical lock untouched. After Cory approves this specific raw SHA, merge verified engineering evidence and follow the canonical PR/exact-head regression/postmerge lock procedure. No aggregate M6.10/M8 or independent Grok certification is inferred.
