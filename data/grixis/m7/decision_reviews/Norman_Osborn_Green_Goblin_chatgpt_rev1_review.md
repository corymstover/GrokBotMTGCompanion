# M7 Deck #43 — Norman Osborn // Green Goblin — Rev1 owner candidate

2026-10-26/27 America/Chicago. **REVIEW-ONLY / NOT OWNER APPROVED / NOT CANONICALLY LOCKED AS REV1.**

## Authority and identity

- Canonical owner repo: `corymstover/grixis-commander-encyclopediaGPT/main`; tracker index 42 (human Deck #43) has the historical key `Goben__Gene_Splice_Savant`, which identifies the alternate printing of **Norman Osborn // Green Goblin**. The Oct 19 M6 review separately established print equivalence; do not rename the key or create a 63rd entry.
- Exact **current**, previously owner-approved source: `refinement/decklists/Norman_Osborn_Green_Goblin_Approved_2026-10-15.txt`; raw SHA-256 `23168e59b7d359ecf24ed95065a5a4b50c978a8f441208d593207e2feacbdea2`, 100 printed names, 23 lands, APPROVED/LOCKED since Oct 15. The 2026-10-12 FINAL and local derived Archidekt exports are *not* replacements for those approved bytes.
- This proposal touches only a separate engineering candidate: `data/grixis/m7/candidate_lists/Norman_Osborn_Green_Goblin_chatgpt_rev1.txt`, raw UTF-8 LF SHA-256 **`c002a49243bd54780bb0f4a36a3c239a00e042defa1d0c6c4b891c3c8060eef9`**. Neither the canonical state registry nor the Oct15 approved bytes are modified.
- Natural ceiling: **Bracket 5 — cEDH**, win with Oracle/Consultation/Pact or Breach/LED/Brain Freeze, but maintain a real Green Goblin discard→Mayhem→recast engine with relevant generic discounts and flash/timing infrastructure. You may cast either modal creature face from the command zone: front Norman for 1U and connive/transform, or back Green Goblin directly for 1UBR plus applicable commander tax; Cavern Human can protect either creature spell. No forced conversion to Rog/Si or generic Grixis goodstuff.

## Whole-100 reassessment: source and weakness inventory

Retains the full October 15 99-card audit as role-level membership evidence; independently re-challenged all roles and every physical land. Protected: Norman, Faithless Looting, Careful Study, Psychic Frog, Ghostly Pilferer, Attunement, Artist's Talent, Tolarian Winds, Dark Deal, Breakthrough, Frantic Search, Wheel, Windfall, Shadow of the Goblin, Unstable Experiment, Borne Upon a Wind, Valley Floodcaller, all three Oracle/Consultation/Pact pieces, Breach+LED+Brain Freeze+Grinding Station+Amber, low-cost protection and fast fixing. The engine must not disappear just because some of these have lower broad-cEDH percentages.

Named weakest/incumbent-challenge slots across the **99**:

1. **Yawgmoth's Will** — powerful generic replay but its replacement effect exiles *newly* discarded cards, switching off the same-turn Mayhem material it would otherwise help produce.
2. **Demonic Counsel** — B tutor only reaches its full any-card mode at delirium; without four distinct graveyard card types its early selection is restrictive. The build has artifact/land/instant/sorcery density, but many turbo hands lack one type on demand.
3. **City of Traitors** — excellent one-shot CC but no U/B/R at any time; sacrifices itself on follow-up land and is awkward for a two-mana U commander followed by exact `1UBR` transformation.
4. **Defense Grid** — can tax interaction around own Breach/Oracle, but affects all players' off-turn casts and does not selectively protect instant/sorcery battles on *opponents'* turns; increasingly competing with flexible protection.
5. **Will of the Jeskai** — commander-modal 3R wheel/flashback is real synergy, but four mana from hand, overlapping wheel/flashback packages and strong need for repeatable two-mana discard setup make this the selected flex cut.
6. **Big Score** — must spend a second card as an *additional* cost even at Green Goblin's reduced graveyard cost; retained because `1R` draw-two/Treasure-two on a Mayhem turn supplies immediate colored mana and cards.
7. **Reckless Handling** — the random discard can drop the just-tutored artifact, but this is unusually commander-compatible and finds LED/Station; retained.
8. **Grim Monolith** — one-time net colorless burst and expensive untap, but strong turbo speed and station-adjacent artifact density justify retaining.
9. **Final Fortune** — delayed loss liability; retained as RR decisive extra turn in protected combo windows, not an unbounded engine.
10. **Cavern of Souls** — names Human to protect *either face* when actually cast as a creature, including Green Goblin directly from command zone; does not shield a transform activation. Its exact-color role matters enough to retain.
11. **Ragavan** — combat-trigger Treasure/impulse with unreliable connection; retained for true one-mana acceleration rather than spending that slot on another two-drop.
12. **Mindbreak Trap** — zero mana only under opponent three-spell condition; retained for storm and uncounterable-spell stack exile in cEDH.

The 23-land skeleton remains nine fetches, three original duals, three shocks, Ancient Tomb, Cavern, Command Tower, City of Brass, Mana Confluence, Gemstone Caverns, Otawara, plus **Cephalid Coliseum** (in place of City of Traitors). Net land count 23, total named copies 100, all distinct. Tradeoff: lose City's two immediate generic mana and explosive ritual openings; gain an untapped blue land and threshold `U, tap, sacrifice: draw three then discard three` with *external* U required to activate. This is a deliberate UBR/Mayhem choice, not a free upgrade in all openers.

## Exactly five selected 1:1 swaps — not a padding target

| Add | Cut | Positive mechanism | Material accepted cost |
|---|---|---|---|
| **Fervent Mastery** | **Yawgmoth's Will** | When it itself has been discarded this turn, Goblin reduces its **3RR mayhem cost to 1RR**; searching up to three cards and then random-discarding three sets up immediate Mayhem for whichever nonlands are discarded. A commander-native bridge to Breach or Oracle components. | Five mana normally (or 2RR alternative from hand), random discard is not controlled when hand contains more than three cards; loses Will's high-ceiling replay of cards already in graveyard. Fervent mayhem and its 2RR alternate cost cannot be combined. |
| **Cephalid Coliseum** | **City of Traitors** | Color-producing land addresses Norman `{1}{U}` and transformation `{1}{U}{B}{R}`; threshold sacrifice draws/discards three cards during a Goblin turn, feeding Mayhem without using a spell slot. | Lose an immediate two-colorless turbo land; threshold needs seven existing graveyard cards, another blue source and sacrifice. Non-threshold Coliseum is merely painful U. |
| **Samut, Tyrant of Naktamun** | **Defense Grid** | New 1U legendary threat grants our instants and sorceries split second, protecting Mayhem spells, Consultation/Brain Freeze and our counterspells on **either** player's turn without opponents buying through a three-mana tax. Also makes front-face Mox Amber produce U if Norman removed. | Creature dies to normal removal; does **not** directly protect Thassa's Oracle as a creature or Underworld Breach as an enchantment, whereas Grid taxes replies to those on our turn. Split second also restricts our own responses while those spells are on the stack. |
| **Intuition** | **Demonic Counsel** | 2U instant finds three related options, supplies one to hand and two to graveyard, consistently accessible without delirium and excellent with an already established Breach. Compared with the Counsel's non-delirium restriction, presents a more reliable top-end tutor package. | Opponent chooses the card kept; the two put into the graveyard were **not discarded** and cannot Mayhem-cast merely because Goblin is present. Three mana instead of B. Keeps stronger Beseech the Mirror intact. |
| **Inti, Seneschal of the Sun** | **Will of the Jeskai** | 1R permanent turns Norman's unblockable attack into optional repeatable discard and a counter; each discrete discard event also exiles one top card playable through the next end step. Mayhem and impulse value interact without additional expensive spell setups; if Inti is discarded under Goblin its generic 1 is reduced and the Mayhem cast costs R. | Loses Will's one-spell wheel-to-five and temporary flashback access. Inti needs to survive and attack to discard by itself; impulse casting still pays normal costs/timing, and one batch discard triggers its impulse ability **once**, not once per card. |

This package keeps native discard density while exchanging three slow/awkward effects and two mana/protection/tutor inefficiencies. After the first five, specifically challenged 10+ additional candidates and did not see a sixth quality-positive replacement with a better incumbent. Five is an output of whole-deck judgment, not an optimization cap.

## EDHREC and off-ranking discovery, October 26–27, 2026

- [Norman cEDH Top Cards / High Lift](https://edhrec.com/commanders/norman-osborn/cedh) (Bracket-5 filter, 791 decks at crawl): Breach 98% inclusion, Attunement **40%, 11× lift**, Breakthrough **16%, 11× lift**, Reckless Handling **27%, 10× lift**, Psychic Frog **59%, 10× lift**. Existing deck already contains all five; retain. Fervent Mastery **13%, 11× lift** newly selected; Inti **6.1%, 11× lift** newly selected. Population metrics are *discovery only*, not tested win percentages.
- [Norman Mayhem subgroup](https://edhrec.com/commanders/norman-osborn/cedh/mayhem) has **only five** tagged cEDH decks; too small to override individually calculated spell and mana costs. [General Norman page](https://edhrec.com/commanders/norman-osborn) / [discard page](https://edhrec.com/commanders/norman-osborn/discard) favor larger, slower payoff creatures in casual builds; don't substitute sample popularity for natural Bracket-5 suitability.
- [2026 tournament evidence](https://cedhstats.org/decklists?commander_id=174&min_players=16&page=1&period=6m&sort=points&with=37108cd4-bbab-4ce3-9ed6-f60e8422e703) includes late-October Norman placements; reinforces that Bracket 5 is a legitimate target, without claiming a measured win rate from this exact untested list.

### Material alternatives and exact dispositions

| Candidate | Disposition | Named cut considered and falsifiable tradeoff |
|---|---|---|
| Fervent Mastery | SELECT | Replaces Will as anti-Mayhem graveyard replay, *not* a strictly faster raw hand cast. |
| Cephalid Coliseum | SELECT | Replaces City despite burst-loss because current Goblin engine has a real colored-mana and repeatable discard demand. |
| Samut, Tyrant of Naktamun | SELECT | Replaces Grid, stronger split-second access to spells on both turns, weaker vs noninstant/sorcery combo pieces. |
| Intuition | SELECT | Replaces conditional Counsel; rejected cutting Beseech due bargain direct-cast ceiling. |
| Inti, Seneschal of the Sun | SELECT | Replaces Will's pricey one-shot modal turn with two-mana commander-related outlet, retaining Big Score and permanent support. |
| Necropotence | REJECT | Would replace Big Score only by suppressing normal sorcery Mayhem: discard reaches GY, then exile trigger on stack prevents sorcery-speed Mayhem before exiling. |
| Force of Negation / Flare of Denial | RETAIN_ALTERNATIVE | Mindbreak Trap or one blast: more free counters but Force pitch not free on own turn; Flare asks for scarce nontoken blue creature/sacrificing Norman. |
| Opposition Agent | RETAIN_ALTERNATIVE | Hexing Squelcher or Mindbreak Trap: flash punishes tutoring, but 3MV narrower and does not protect an already assembled Goblin kill. |
| Skirge Familiar | REJECT | Big Score/Attunement: mass instant-speed discards, but five-mana body slower than existing one/two-mana outlets at turbo ceiling. |
| Change of Fortune | RETAIN_ALTERNATIVE | Tolarian Winds: potentially much larger refill after prior discards; initial 3R and need for previous discards lose to Winds' 1U predictable timing. |
| Secrets of the Dead / Monument to Endurance | REJECT | Big Score / Will: incremental engines can dominate slower pods, but are slower than immediate combo conversion, and Will is already removed for Inti. |
| Bazaar of Baghdad / Urza's Saga | REJECT | City/Coliseum: colorless or no mana in 23-land, UBR-specific color cost is severe. |
| Putrid Imp / Ledger Shredder | REJECT | Ghostly Pilferer or Inti: putrid cheap outlet without strong draw; Shredder's generic connive doesn't beat Goblin-specific repeated discard/impulse package. |
| Echo of Eons | RETAIN_ALTERNATIVE | Dark Deal: LED graveyard-flashback refill is real, but it gives opponents seven and does not provide Mayhem discount with generic 2U flashback unless chosen as alternate casting permission. |
| Entomb / Reanimate | REJECT | Intuition / another core slot: mill-to-graveyard does **not** meet Mayhem discard condition, and creature density remains low. |
| Malevolent Hermit | RETAIN_ALTERNATIVE | Squelcher: protective U counter and disturb effect are useful but two phases slower than Squelcher's immediate 2MV counter-tax ability on our turn. |
| Gilded Drake | RETAIN_ALTERNATIVE | Ragavan: steals opposing commander, but narrow to creature-rich pods and sacrifices first-turn red Treasure route. |
| Additional lands over Mox Diamond | REJECT | More than 23 lands without replacing a land would weaken burst/tutor or native outlet density; targeted Coliseum substitution is the less disruptive intervention. |

## Exact verification, actual limits and test mapping

- **Physical count/singleton**: 100 lines of `1x`, commander first, 100 unique, 99-card library, 23 lands, zero companion; no canonical project exception required. Exact candidate raw SHA above.
- **Oracle/legality**: historical 2026-10-15/16 independent 100-name Scryfall audit passed on the exact approved base; latest [official Commander banned list](https://magic.wizards.com/en/banned-restricted-list) rechecked 2026-10-26/27, October 12 general B&R concerned *Competitive Brawl* not tabletop Commander. New adds checked by card-specific Scryfall pages ([Samut](https://scryfall.com/card/fra/302/samut-tyrant-of-naktamun), [Fervent](https://scryfall.com/card/stx/101/fervent-mastery), [Inti](https://scryfall.com/card/lci/295/inti-seneschal-of-the-sun), [Intuition](https://scryfall.com/card/tpr/54/intuition)) and an October 23 local [Coliseum](https://scryfall.com/card/ody/319/cephalid-coliseum) snapshot, all UBR/colorless and Commander legal. We did **not** freshly query the entire 100-card list against external Scryfall; no 100/100 live API claim. `verify_norman_local.py` covered 66/100 through local historical cross-deck snapshots, with 34 without matching local snapshots; this is **not** a substitute for historical dedicated full baseline verification.
- **M6 original planned cases**: `data/grixis/m6/test_blueprints/Norman_Osborn_Green_Goblin.json` defines P0 C1, K1–K3, F1; relevant P1 K4–K7, E1/E2, W1–W3, F2/F3. That backlog is design-only. New finite check file `data/grixis/m7/norman_rev1/test_norman_rev1.py` executes **12 narrow bounded tests** with positive/negative fixtures: exact list, transform/pips, generic reduction and alternative-cost exclusion, discard-and-timing, Necropotence/Yawg/hate, both command-zone faces/tax/Cavern, corrected JSON/Markdown source regression, Intuition non-discard, Coliseum threshold and external U, LED casting-step restriction, Breach escape other-card cost, Samut/Inti scope. It is not a comprehensive game-state rules simulator or a claim that the old blueprint's P0 ledger changed automatically.
- **Corrected prior generated-source errors**: prior `grixis/interactions/norman-osborn.md` and `data/grixis_interactions/norman-osborn.json` wrongly said (1) back-face Goblin cannot be cast from command zone, and Cavern protects only front, and (2) LED can activate mid-spell cost payment. The present *versioned* M7 branch corrects both source JSON and readable Markdown, with bounded regression assertions for direct back-face cast, commander tax, either-face Cavern, LED priority and non-mid-cast. The locked original 2026-10-16 Oracle bulk snapshot is absent here, so the global generator `--check` remains unrun; do not transfer the old uncorrected "9 verified" claim into M7/M6 certification without that reproducibility step.
- **Combo/resource limitations**: Intuition graveyard placement never triggers Mayhem; Fervent three-card random discard only guarantees selected cards all discarded when they are the only hand cards; Coliseum consumes itself and needs external U; Breach escape needs three *other* graveyard cards per cast and payable colored mana; no free infinite claimed from empty resource zones. Goblin reduces only generic, not colored mana. Samut split second does not protect Breach/Oracle directly. A full multiplayer opponent-response/win-rate I/J experiment has not been executed on the exact revision; inherited I/J findings are not claimed transferable as an exact-final win-rate test.
- **Decision status**: five authored cards all SELECT after alternative tradeoffs; no simulation results invented. Pending exact-head CI/M7 gate/provenance and Cory's explicit named SHA approval. Older approval is preserved until a separate owner-authorized canonical approval PR and postmerge hash check.

## Owner packet

**M7 Rev1** — 100 unique cards, 23 lands; Bracket 5 — cEDH; **Mayhem / Graveyard Casting / Turbo Combo**.

Exact proposed raw SHA: `c002a49243bd54780bb0f4a36a3c239a00e042defa1d0c6c4b891c3c8060eef9`.

On approval: verify these exact bytes, do narrow canonical PR + final gate + guarded merge, verify approved list SHA/registry/tracker afterward. Do not transfer an approval to a revised SHA.
