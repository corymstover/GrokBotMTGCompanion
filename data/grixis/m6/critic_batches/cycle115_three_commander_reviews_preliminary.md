# Cycle 115 — Commander-first source reviews: Rograkh // Silas, original Nicol Bolas, Mai and Zuko

**Author strategic review, NOT independent Pass C.** The plan was preregistered before conclusions in `data/grixis/m6/phase_b_plans/cycle115_three_commander_reviews_01.json`, first commit `c8281cdcf1865fb42feeced53f8d21851d3b69f4`. Full structured decisions: `data/grixis/m6/author_reviews/cycle115_three_commander_reviews_01.json`. Separate direct read-only original-deck and recorded-SHA integrity receipt: `data/grixis/m6/phase_b_bounded/cycle115_direct_source_integrity_01.json`.

This batch advances the established Cycle111 human-review queue positions **11–13**, not a speculative reorder or cEDH strength ranking. It intentionally leaves earlier Cycle114 draft [PR #219](https://github.com/corymstover/GrokBotMTGCompanion/pull/219) unresolved and unmerged because its GitHub Actions workflow creation was tooling-blocked. That same restriction has **not** been worked around. No automated CI or formal independent reviewer is claimed for Cycle115.

## 1. Rograkh, Son of Rohgahh // Silas Renn, Seeker Adept — HOLD exact proposal

**Proposed:** The Enigma Jewel // Locus of Enlightenment **in**, Birgi, God of Storytelling // Harnfel, Horn of Bounty **out**. M5 ID `swap:rograkh-son-of-rohgahh-silas-renn:m5:c0b52a884319`. Approved raw SHA-256 `06c9e22b5afc46bd58bbbfdef5c42a796d2a986a2972456107c29aee1b5f905c`. **100 cards = 98 in the main library + two partner commanders**, both source/approval-verified.

Rograkh's free legendary body activates Mox Amber, Springleaf Drum, Paradise Mantle, Culling the Weak, Infernal Plunge and instant cast protection. The shell uses those efficiencies for turbo Ad Nauseam, Necropotence and compact Oracle/Breach lines; Silas is a combat artifact-graveyard recast tool but primarily adds color identity.

The Enigma Jewel costs {U}, **enters tapped**, then generates {C}{C} restricted to **activating abilities**, not casting spells. Crafting requires {8}{U} and exiling four or more *other* nonland permanents/cards with activated abilities at sorcery speed. Only the much later Locus copies activated **nonmana** abilities. This is not an inexpensive turbo-spell mana rock. Birgi gives a red mana trigger on casting every spell, directly sustaining ritual/cast chains; Harnfel discards a card to exile two library cards temporarily playable that turn. The candidate's M5 Spellbook match is not a legal accessible value/turn comparison.

**Hold Birgi/Harnfel.** Enigma Jewel might pay an occasional Wishclaw Talisman activation, but it fails to replace early spell-chain mana and card access without substantial source-backed proof.

## 2. Nicol Bolas (original Elder Dragon) — HOLD exact proposal

**Proposed:** Volcano Hellion **in**, Mystic Remora **out**. M5 ID `swap:nicol-bolas:m5:3adba7cabda7`. Approved raw SHA-256 `e47fdd5c31dce2d5b05e8fa8c217fe94caa16ef150057f98748254fc3c841617`. 100 cards = 99 main + original Bolas commander.

Original Nicol Bolas costs **{2}{U}{U}{B}{B}{R}{R}**, flies, imposes a recurring upkeep payment of {U}{B}{R}, and empties an opponent's hand when **Bolas himself deals damage to an opponent**, combat or otherwise. The approved deck specifically uses Dragon Tempest, Ingris Stingerquill, Chandra's Ignition, Pain for All, Quicksilver Dagger, Kediss and similar **Bolas-sourced damage**, then turns the discarded cards into Waste Not, Tergrid and Tinybones value. It is not the Ravager superfriends deck.

Volcano Hellion deals a chosen damage amount to its **controller and target creature** when its ETB resolves; that damage comes from **Volcano Hellion**, not from Bolas. It is neither player damage dealt by Bolas nor a source of Bolas hand-wipe triggers. The self-damage and upkeep **echo cost equal to controller life total** introduce major burdens even if the creature can function as conditional removal. Mystic Remora's cheap one-blue-mana noncreature-spell-triggered draw is a powerful way to access the enormous colored-mana deployment and upkeep needs. An uncrosschecked generic Spellbook synergy is not enough.

**Hold Mystic Remora.** Volcano Hellion is a poor replacement in this commander-specific damage/discard engine, regardless of its independent removal utility.

## 3. Mai and Zuko — Enigma Jewel identity-positive; HOLD proposed counterspell cut

**Proposed:** The Enigma Jewel // Locus of Enlightenment **in**, An Offer You Can't Refuse **out**. M5 ID `swap:mai-and-zuko:m5:efea4143158c`. Approved raw SHA-256 `aa2036f49f38e6503734d99c852acdfa704aa1b27e44bb26d6e9566a73a0d4a2`. 100 cards = 99 main + commander.

Mai and Zuko give artifact and Ally **spells** flash and have Firebending 3 for red combat mana. The deck's primary engines are Basalt Monolith + Rings of Brighthearth and Sensei's Divining Top / Mystic Forge / Bolas's Citadel cost-reduction loops, while Ally/Avatar value connects to the commander.

The Enigma Jewel does **not** generate mana for casting those flashed artifact spells. It can, however, use its restricted {C}{C} to pay *activated* ability costs such as Basalt Monolith's {3} untap or Rings of Brighthearth's {2} copy fee. This is **actual deck-specific mechanical synergy**, stronger than its connection to the Rograkh turbo spells deck. The Jewel is castable with flash permission, but enters tapped. Its expensive crafting is expressly **sorcery speed**, so the commander's flash-spell permission does not make the craft action instant speed. Reaching the Locus face also consumes multiple real activated-ability cards as crafting ingredients.

An Offer You Can't Refuse counters an opposing noncreature spell for {U} and gives that controller two Treasure tokens. Losing it weakens interaction/protection in an artifact-combo shell attempting to resolve expensive engine cards. No source-backed paired turn demonstrates that adding Jewel in that exact slot creates reliable additional combo wins.

**Do not remove An Offer.** Continue screening the Enigma Jewel for a different cut if a real legal fast-enough Basalt/Rings/Top activation ledger supports it. This is a positive candidate-investigation result, not an approved swap.

## Primary authority, limits and next gates

The primary project source is the current canonical approved 100-card TXT and locked SHA state, plus the companion registry/blueprint/M5 packet; older Spellbook or M5 simulation ratings are research cues, **not** approval. Read-only checks confirmed 62/62 canonical approvals locked, the three exact original full card counts (including two commanders for RogSi), singleton for nonbasics, matching **recorded** approved SHA values across repos, source-original swap IDs and add/cut presence. Source bytes' hashes were **not recomputed independently**; do not relabel recorded-hash equality as an independent cryptographic test.

Oracle ability claims were corroborated with public card text and original commander blueprint; the downloaded frozen Scryfall corpus and a full date-current 100-card legality check were **not run** during this session. The cycle remains CI-pending and should not be merged without permitted test execution. No full effect-aware Phase B, independent Pass C/I/J or candidate-pool-zero-improvement certificate exists here. No approval or card change was issued.

**Suggested next project step:** a permitted external CI run to unblock PRs #219 and the Cycle115 draft, a separate independent strategic reviewer, and then continue three new distinct commander reviews. Reuse the existing research evidence before commissioning expensive simulations.
