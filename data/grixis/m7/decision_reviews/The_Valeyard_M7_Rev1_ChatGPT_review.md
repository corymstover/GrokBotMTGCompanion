# Deck #58 — The Valeyard M7 Rev1: decisive owner-review packet

**Disposition before owner decision:** proposed and unapproved. Never modify the existing October 15 approval, canonical current-deck override, or lock based on this file. The historical repository-wide case-transfer gate remains a separate issue. This packet certifies **the proposed exact 100 within its own stated scope** and does not claim full Magic gameplay simulation or global transfer completion.

## Source and exact 100

- Authoritative baseline `corymstover/grixis-commander-encyclopediaGPT/main/refinement/decklists/The_Valeyard_Approved_2026-10-15.txt`, blob `01c81fffcf3c586f1de136cf055c395bab2209e8`, byte SHA-256 **`4bef619a33d85eafaf194997924fc8378dd490f62c59d76bafccc4fa07ef821c`**; immutable copy in `the_valeyard_rev1/The_Valeyard_Oct15_baseline.txt` matches byte-for-byte.
- Final staged candidate: `candidate_lists/The_Valeyard_M7_Rev1.txt`; LF raw SHA-256 **`1735629783fbea2c9b8782fe18835f6dc8b3b980715344249cdb0941fbd9887b`**.
- Exactly **100 cards**, commander first, **96 distinct names**, **36 lands**. The only repeated names are Island ×2, Mountain ×2 and Swamp ×3. Grixis U/B/R identity and official Commander legality pass on all **104 unique** names across baseline/candidate/alternatives, using preserved live Scryfall `/cards/collection` records retrieved 2026-10-27. **No project-specific legality exceptions** are used.
- The existing approved baseline has all **18** other Commander-legal Grixis cards explicitly referencing votes in Oracle text and **13** cards that can present an opponent with a villainous choice. The proposed six swaps preserve **all 31 of these protected source/payoff positions**; The Valeyard itself modifies but does not initiate a villainous choice.
- Current Scryfall Game Changers in final: Ancient Tomb, Chrome Mox, Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Force of Will, Rhystic Study, Vampiric Tutor. Natural ceiling and list bracket: **4 — Optimized**. Archidekt tags: `Villainous Choice`, `Voting`, `Valeyard Copies`.

## Commander-first reasoning

The Valeyard costs `{2}{U}{B}{R}`. A real villainous choice faced by an opponent produces one additional sequential choice; the opponent can choose the same or different modes. Each other legally surviving Valeyard adds one more *choice*, not an exponential doubling. A genuine vote event lets this controller cast one additional vote; merely selecting among modes is not voting. All thirteen cards generating choice outcomes and the entire color-legal voting inventory stay in. The existing Auton Soldier, Quantum Misalignment, Spark Double and Sakashima effects protect the clone plan; adding Irenicus strengthens it directly.

The actual strategy is politically asymmetric resource denial and alternative-mode pressure: Davros, Eggman, Daleks and Doctor Who villain cards force unfavorable choices; Council's Dilemma/Will/secret council offer real votes; Grudge Keeper/Model of Unity/Illusion of Choice influence or reward the results. The deck's credible natural power ceiling remains a strong but relatively slow Bracket 4. It does not inherit the consistency of generic Grixis deterministic combo.

## Six selected swaps

| Add | Cut | Specific improvement and price paid |
|---|---|---|
| **Irenicus's Vile Duplication** | Brainstorm | A second persistent nonlegendary Valeyard modifies every future opponent villainous choice and personal voting event. Lose cheap selection and excellent fetchland synergy. |
| **Double Vision** | Kess, Dissident Mage | A copied first instant/sorcery **cast** each turn creates another separate vote/choice resolution, rather than requiring a card in the graveyard. Lose cheaper four-mana recasting from grave on our turns; Double Vision costs five, and a copy is **not cast**. |
| **Swan Song** | Arcane Denial | Hold up one blue protecting the five-mana commander, copy engine and political payoffs without rewarding opponent with two draws. Lose the ability to counter creature, artifact and planeswalker spells; an opponent receives a 2/2 flyer. |
| **Toxic Deluge** | Blasphemous Act | Consistent three-mana scalable -X/-X can eliminate indestructible threats while leaving time to rebuild political engines. Lose Act's one-red mode in crowded boards; pay life. |
| **Chrome Mox** | Izzet Signet | Zero-mana colored acceleration makes a fast Valeyard/early copying line likelier; the same suite keeps other multicolor rocks. Must exile a nonartifact/nonland card and can be card-disadvantaged or poorly colored. |
| **Ancient Tomb** | Haunted Ridge | Two generic mana from one land materially advances a five-mana commander and high-MV voting sources. BR fixing becomes colorless and two life is paid per activation; no claim that this universally improves all openers. |

This is **six because of quality**, not a minimum quota. The supplementary 99-physical-slot CSV documents six actual cuts and 93 protected retained cards; the whole-card M6 comprehensive review and fresh Scryfall Oracle were adjudicated rather than substituted with a popular-card ranking.

## More aggressive complete alternatives, explicitly rejected

1. **Seven-swap alternative:** +Mana Vault / −Fellwar Stone on top of the six. Full 100 SHA-256 `c05cd0dbefe9b79178bfb448a89275f4122e145005cb7c7a8dda89eaa8b12ac0`. Faster colorless burst, but weakens repeatable U/B/R when a vote/control spell needs specific pips. Retain Fellwar Stone.
2. **Eight-swap alternative:** additionally +Helm of the Host / −Midnight Crusader Shuttle. Full 100 SHA-256 `e39ec2c076650057ae1b55d5c5de4d2149168e2e2cbc5e5a0d4763d5a300c497`. Helm can repeatedly make nonlegendary Valeyards, but costs four plus **five equip** and loses one of thirteen independent actual Villainous Choice sources. Retain Shuttle.

Other examined off-ranking opportunities: Chandra, Hope's Beacon, Displacer Kitten, Narset's Reversal, Mystical Tutor, Spellseeker, Cavern of Souls, Gemstone Caverns, Mirror Box, Strionic Resonator and invalid/unverified Ballot Broker. The exact cut-by-cut authored verdicts appear in `The_Valeyard_rev1.json`. The Master, Gallifrey's End remains deliberately: Missy's controlled face-down Cybermen are actual nontoken creature cards that can die to cause its villainous-choice trigger. We did not erase a commander-native interaction to make room for a tutor.

## Rules and testing boundaries

- Two Valeyards mean each opponent makes **three** individual choices per actual villainous-choice event (base + two replacement effects), never four recursively. The player choosing may vary the answer.
- A true vote requires vote wording. `Prisoner's Dilemma`, `The Toymaker's Trap` and `Seize the Spotlight` are not vote substitutes. The three `Path of ...` cards do contain true Will of the Planeswalkers votes; do not assume an ordinary Commander game has meaningful plane events without Planechase setup.
- The controller's extra vote does **not** guarantee a majority against three opposing voters. Grudge Keeper also requires that an opponent voted for a choice **the controller did not vote for**, so splitting personal votes may negate punishment.
- Irenicus explicitly creates a **nonlegendary** creature-token copy. Double Vision copies a spell without casting its copy, thus real voting instructions repeat on resolution but separate cast triggers do not.
- The M6 P0 `C1/K1/K2/K3` cases and two bounded extra `K4/F1` scenarios were executed against the fixed raw candidate and current Oracle snapshot with both positive and adversarial preconditions. These are **finite event-accounting fixtures, not a complete rules-engine simulation**; no inferred win percentages.
- `verify.py` checks four exact raw hashes, deck counts, singleton, color identity, legalities, 36 lands, protected vote/choice inventory and key Oracle text/interaction assertions. `scripts/grixis_m7_decision_gate.py` checks all 18 material judgments, 16 weak-slot challenges, two exact larger full-100 alternatives and the change reconciliation.

## Required engineering gate and owner authority

The dedicated Deck #58 exact-head GitHub Actions workflow must pass **on the proposed PR head**, as must any applicable global M6/M7 certification prerequisites; never infer global success from this local packet. The unrelated missing historical Nekusar transfer record observed in the prior Deck #57 canonical workflow is **not** repaired or waived here, and no false global certification is asserted. The canonical Oct15 approval and full history remain untouched until Cory explicitly approves **the exact new raw SHA** and required lock gates are truly green.

**Owner approval question, only after exact-head checks:** This deck is complete. Do you approve it?
