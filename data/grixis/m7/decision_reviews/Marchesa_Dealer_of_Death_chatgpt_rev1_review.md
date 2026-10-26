# Deck #34 — Marchesa, Dealer of Death — M7 Rev1 evidence and candidate

Date: 2026-10-25 America/Chicago. **Authority status: RESEARCH_ONLY, owner-unapproved.**
Do **not** change canonical `APPROVED/LOCKED` state or present this as an M6
certification or owner-ready packet until exact-head gates have passed.

## Cryptographic source and boundary

- Live canonical: `corymstover/grixis-commander-encyclopediaGPT/main`,
  `state/current_deck_overrides.json#decks.Marchesa__Dealer_of_Death`.
  October 15 approved 100, raw SHA-256
  `34a6a940c54aaebde612ae5d3a244e22931d3a977fa26e4c43f2a76aafc0f6b1`.
- M7 baseline bytes:
  `data/grixis/m7/baseline_sources/Marchesa_Dealer_of_Death_chatgpt_rev1_baseline.txt`.
- Proposed 100 bytes:
  `data/grixis/m7/candidate_lists/Marchesa_Dealer_of_Death_chatgpt_rev1.txt`;
  raw SHA-256 `f6f68d204925ef3528166722d874cd4122e50755b30f8b9a9ac19d7eff9afd3e`.
- Original prior October 15 approval and all other 61 decklocks remain intact.
- The M6 October 19 authored review was KEEP, while the sealed owner-equivalent
  Pass C October 21 said NEEDS TESTING rather than falsely accepting KEEP as
  proven. This M7 candidate is an independent current strategic choice, not a
  mechanical adoption of the 58 M5 hypotheses, and not an official lock.

## Identity, role accounting and ceiling

Marchesa's UBR {1} optional payment after each **targeted** crime converts
interaction into top-two hand/graveyard selection. She does not draw a card, has
no once-per-turn cap, and the {1} must actually be available per trigger.
Retain protected low-cost repeatable crimes: `Spatial Binding`,
`Hex Parasite`, `Spellskite`, `Lapis Lazuli Talisman`,
`Talon Gates of Madara`, `Urborg`, `Hammerheim`,
`Tezzeret, Cruel Captain`, `Bender's Waterskin` and Magda.
Retain all three compact wins:
`Thassa's Oracle` + `Tainted Pact`;
`Underworld Breach` + `Lion's Eye Diamond` + `Brain Freeze`;
and `Aphetto Alchemist` + `Hawkeye's Bow`. The Bow damage does **not**
target and is not itself a crime. Marchesa is the card/yard engine, not an
obligate piece of those kills. Natural Power Bracket **5 — cEDH**; the October
11 tournament first-place list supports viability, not a causal win-rate claim.

Whole-99 group disposition: retained efficient interaction and free protection
(`Fierce Guardianship`, `Force of Will`, `Mana Drain`, `Flusterstorm`,
`Pact of Negation`, `Mental Misstep`, `Stifle`), tutor/fast mana,
29 land faces, Marchesa-specific engines, anti-stax answers, and the three
independent combo routes. Challenged narrow/redundant reactive slots,
costly enchantment cloning, untargeted but unreliable topdeck tax,
four-mana token engine, risky sorcery extra-turn effect, and colored-mana traps.
These exact eight slots are the proposed full-100 portfolio; no fifth-swap quota
was used as a cut criterion.

## Eight exact candidate swaps, with burdens

| Add | Cut | Selected whole-deck advantage | Material downside |
|---|---|---|---|
| Demonic Consultation | Minor Misstep | Second one-mana route to Oracle; names absent card with Oracle's trigger on stack to empty library; also risky emergency tutor | Loses one-mana protection against zero/one-mana spells; Consultation can exile necessary cards, and timing/stack interruption remain real |
| Gilded Drake | Counterbalance | {1}{U} targeted ETB crime, answers an opposing commander/creature by control exchange without relying on top-card CMC | Loses passive free spell denial; Drake needs a valid opposing creature, the exchange is interactable |
| Opposition Agent | Last Chance | Instant-speed opponent-search interdiction and card-stealing; supports Marchesa's interactive cEDH table control | Agent itself does not target and thus is not a crime; loses the second, albeit dangerous, RR extra-turn race line (Final Fortune retained) |
| Mayhem Devil | Storm-Kiln Artist | Three-mana targeted crime trigger from **any player's** permanent sacrifices (fetchlands, Treasure, LED); makes opponents' and our sacrifices into real interaction and paid selection | Loses four-mana instant/sorcery Treasure acceleration; Devil requires targeting plus separate {1} Marchesa fees and can be removed |
| Scrabbling Claws | Copy Enchantment | {1} repeatable **target-player** crime, even with no GY cards; can cash in for exact enemy grave-card exile and a card; direct Breach mirror hate | Loses copies of Rhystic, Remora, Breach or an opponent's enchantment; tap-mode exile is chosen by affected player, exact exile requires sacrificing Claws |
| Snuff Out | Dispel | Free (Swamp + 4 life) **targeted** answer to a nonblack creature/hatebear, generating paid Marchesa selection if she survives | Loses one-mana instant-only counter for combo protection; black creatures cannot be destroyed, 4 life harms Ad Nauseam |
| Marsh Flats | Great Hall of the Citadel | Untapped fetch for Swamp-typed U/B/R dual choices instead of conditional legendary-spell/filter land, reducing colorless opening traps | Costs 1 life/search, susceptible to opposition searching hate; Great Hall could fix legendary Marchesa |
| Sink into Stupor // Soporific Springs | Tolaria | Blue land face with live opponent-targeted spell/permanent bounce mode = another crime; flexible anti-stax/protection | 3 life to enter untapped or tapped; loses Tolaria's historic targeted upkeep crime ability; instant side costs {1}{U}{U} |

**Mana:** 29 land faces in both configurations (the candidate is 28 land
front faces plus the Soporific Springs MDFC back face); seven of the
ordinary fetchlands now include Marsh Flats. Retains colorless `Ancient Tomb`,
`Urza's Saga`, `Talon Gates` and conditional `Mox Amber`. No quantified
first-three-turn castability claim is made; source-paid three-color stress
testing remains important with Ad Nauseam/life costs.

## Seriously considered but not selected

- **Hullbreaker Horror / Orcish Bowmasters (M6 P0): REJECT.** Seven-mana
  engine for cheap existing removal/rule of cEDH; M5 simulator does not model
  Bowmasters or Horror effects. Prevents cEDH early-window slowdown.
- **Bandit's Haul / Lotus Petal; Tezzeret, Master of the Bridge /
  Underworld Breach; Mnemonic Wall or Shipwreck Dowser / LED;
  Crackdown Construct or Wake Thrasher / Oracle: REJECT.**
  These substitute slow engines for fast protected finish/ramp components;
  old optimistic proxy "pass" was effect-blind.
- **Talisman of Indulgence / Copy Enchantment (sealed Pass C):**
  RETAIN_ALTERNATIVE. An untapped R/B rock may improve three-pip reliability.
  Here Marsh Flats plus Soporific Springs tackle color availability while the
  single copy slot goes to a Marchesa crime + exact graveyard-hate outlet.
  In pods where colored sources remain inadequate it is first re-open.
- **Ghost Vacuum / Copy Enchantment or Counterbalance:**
  RETAIN_ALTERNATIVE. More precise, repeatable grave hate once opposing grave
  cards exist, but can have no legal activation target when graveyards empty.
  Claws's target-player mode uniquely offers guaranteed Marchesa crime.
- **Glasses of Urza / Copy Enchantment:** REJECT after examining target-player
  activation; information alone is lower consequence than Claws grave hate.
- **Wheel of Fortune / Counterbalance, Wishclaw Talisman / Copy Enchantment,
  Ragavan / Magda:** REJECT at present. Wheel replenishes opponents and is not
  a crime; Wishclaw is a slower conditional shared tutor and **does not
  target** an opponent; Ragavan adds tempo but undermines the Magda crime
  resource slot and opponents can block.
- **Talisman vs Scrabbling/Mayhem package:** If exact first-three-turn source
  tests contradict current judgment, revisit *only the coherent full 100*
  instead of gratuitously adding a ninth card.

### Open-ended full-100 package audit after the eight selections

The eight selected cuts were **not** a search stop. Two other distinct plausible
incumbents challenged after the floor were `Magda, the Hoardmaster` (once-turn,
**tapped** Treasure payoff) and `Praetor's Grasp` (three-mana opponent-target
theft with double-black requirement). The following three **actual complete
100-card** alternatives were constructed from the selected candidate and
checked for exact singleton/physical count:

1. `alt8_counterbalance`: `+Counterbalance / -Magda` relative to selected
   100; SHA `728bcddce4c8f80c4c81c8f192f53958e515af035ea9cf8a08aedbd047cce98e`.
   Retains free top-of-library cEDH taxing and Gilded Drake, but deletes an
   actual commander-specific turn-cycle Treasure engine. **REJECT** in favor
   of the selected 100's Magda crime identity.
2. `alt8_talisman`: `+Talisman of Indulgence / -Scrabbling Claws`, SHA
   `1cfa6d9d4c6d6015c9a3676c84e12776407182bbf93159f8c4a071a08e260248`.
   Improves consistent two-mana B/R acceleration, but removes repeatable
   target-player crime plus exact emergency GY exile. **RETAIN_ALTERNATIVE**
   for demonstrated colored-pip bottlenecks.
3. `alt9_intuition`: `+Intuition / -Praetor's Grasp` on top of all eight,
   SHA `eaac15030cbe0c153c01ce6b7e25efa623087142e5e2f4ccc9f4b12e6d054fed`.
   The instant targets an opponent (crime) and can bin Breach pieces, but
   opponents choose the hand card: an `Underworld Breach / LED / Brain Freeze`
   pile **cannot guarantee** placing Breach in hand. Praetor's Grasp can
   disrupt rival combo access and exploit known opposing lists, at the cost of
   sorcery timing and double black. **RETAIN_ALTERNATIVE**, but not enough
   reliable incremental win-line access to displace Grasp now.

The stop reason is that remaining credible extra changes either remove a
Marchesa-specific engine, worsen turn-cycle threat coverage, or add a
graveyard-dependent package in an already Breach-vulnerable 100. This is a
qualitative local choice, **not** a proof that no future meta-specific 9th
upgrade exists.

## Source and scope checks

- Source-date context: October 25, 2026. EDHREC Marchesa cEDH page
  `https://edhrec.com/commanders/marchesa-dealer-of-death/cedh` presents
  140 bracket-5 decks in the crawler view, using a **High Synergy** label.
  Key observed frequencies: Opposition Agent 56% (79/140), Gilded Drake 25%
  (35/140), Mayhem Devil 30% (42/140), Snuff Out 34% (48/140), Demonic
  Consultation 86% (121/140). Counts are community association, not efficacy.
  A separately distinct current **High Lift** value was not exposed by that
  page; do not mislabel old synergy percentages as lift.
- Scryfall named Oracle pages checked through public search for the eight
  additions. Official Wizards Commander banned list checked Oct 25, including
  its current October 12 announcement. None of these eight is banned or
  outside UBR; existing 92 retain October 15 whole-list checkpoint and October
  20 prior Scryfall `/cards/collection` advisory check. **No new fresh
  100/100 October 25 Scryfall collection transaction has run.**
- The 100 is exactly distinct and one commander; no project exceptions.
  Names with modal faces occupy a single Commander slot.
- Oracle caveats: A single spell/ability commits at most one crime at target
  choice. `Demonic Consultation`, `Opposition Agent` and fetchland
  activations themselves do **not** target and do not create crimes.
  `Mayhem Devil` must choose an opponent/opposing object as target to commit.
  `Scrabbling Claws` target-player ability is a crime even with empty GY.
  `Snuff Out` needs a Swamp for free mode and cannot target black creatures.
  `Sink into Stupor` targets an opposing spell/nonland permanent on its spell
  face; the land face has no target. `Gilded Drake`'s exchange is not mandatory
  if no target was chosen, and then it doesn't yield Marchesa's crime.
- Printed `Hawkeye's Bow` legality and exact Oracle remain tied to the
  earlier baseline legal-card audit, not falsely fresh-certified here.

## Actual test coverage versus open gates

- **Executed locally:** 19 named finite authored tests in
  `tests/test_m7_marchesa_dealer_rev1_exact.py`, including 100-card
  SHA/delta/count, C1, K1–K7, E1–E2, W1–W3, F1–F3 and the changed new-card
  target caveats. The little model asserts source-paid sequential examples,
  targeted definitions, Marchesa being absent, invalid self targets,
  opponent graveyard hate, and bounded Bow damage. It is **not** a general MTG
  engine or randomized four-player test; its fixture outputs do not prove
  cEDH win percentage, full stack semantics, or every unmodeled card effect.
- **M6 case provenance:** Exact commander-effect blueprint
  `data/grixis/m6/test_blueprints/Marchesa__Dealer_of_Death.json` has 16
  planned P0/P1 cases, all originally
  `DESIGN_ONLY_UNIMPLEMENTED_NOT_RUN`. New tests are case-labeled partial
  executions but have **not yet been accepted and scope-transferred** by the
  formal M6/I/J governance ledger.
- **I/J honest state:** Historic
  `data/grixis/m6/ij/input_receipts/marchesa-dealer-of-death.json` reports
  input bytes attested, `phase_b_replayed=false`, and downstream
  incomplete. The exact eight-card candidate creates new effects/targets and
  invalidates any blind transfer of historical full-100 outcome claims.
  An explicit case-by-case 16-ID plan is above; current finished I/J final
  bundle, test-pool local optimum certificate, exact-head CI receipt and final
  decision gate remain **unverified/pending**.

**Disposition:** coherent, source-pinned full-100 M7 candidate selected;
**not yet approval-ready** under ONE_COMMAND_FINISH_V1. Prepare research PR,
complete real remaining P0/I/J transfer, fresh complete Oracle transaction,
and exact-head CI before asking Cory for a SHA-bound "Approve".
