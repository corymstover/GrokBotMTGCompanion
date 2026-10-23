# Grixistax___October_2026 (Kraum, Ludevic's Opus + Tevesh Szat, Doom of Fools) — M7 red-team memo (2026-10-23)

1. **Commanders countered or removed.** Both commanders cost five mana, and recasting either costs commander tax for that commander only (CR 903.8; Partner, CR 702.124b/c). The stax pieces slow our own five-drops too, so the deck has to win or lock without them.
   - Protection: the free counters (Force of Will, Force of Negation, Fierce Guardianship, Pact of Negation, Mindbreak Trap, Mental Misstep), plus Mana Drain and Red Elemental Blast.
   - Bitterblossom (the new add) is a commander-independent token stream, so Thrull-dependent outlets (Contamination, Skullclamp, Phyrexian Tower, Culling the Weak, Tangle Wire, Diabolic Intent) still work if Tevesh is answered.
2. **Self-lock tensions (baseline, owner-accepted, disclosed).**
   - Our own Torpor Orb stops Overburden's trigger and Orcish Bowmasters' enter trigger (Torpor Orb ruling 2024-04-12).
   - Static Orb also caps our own untaps at two permanents, which is why the staged Opposition clashes with it.
   - Damping Sphere turns our Ancient Tomb into one colourless mana.
   - Chalice of the Void on 0 counters our own Moxen and Lotus Petal; on 1 it counters our own one-drops.
   - Trinisphere makes our free spells cost three mana.
   - Blood Moon / Magus of the Moon plus Back to Basics constrain our own nonbasic lands (CR 305.7).
   - Necropotence exiles discarded cards, which removes Breach fuel.
3. **Arcane Signet (swap 1).**
   - It adds one mana of any colour in the commanders' combined identity, U, B or R (ruling 2020-11-10). Contamination replaces only lands' mana, so Signet still makes U or R under our own Contamination. Blood Moon and Back to Basics do not affect it.
   - Costs: it costs {2} where Mox Amber costs {0}. Trinisphere taxes both to three. Opposing artifact hate stops both (measured equal: turn 4 mean 2.607 baseline, 2.602 candidate). It counts as an artifact for Mox Opal just as Amber does.
   - Mox Amber makes no mana off Karn, the Great Creator, which is colourless (Mox Amber ruling 2018-04-27). Our own Chalice on 0 counters Amber but not Signet.
   - Talisman of Indulgence (Pass C's challenger) has the same raw mana in the model, but makes {B}/{R} only, so it is dominated under Contamination (P(U) turn 4 0.2722 against Signet's 0.3299).
4. **Bitterblossom (swap 2).**
   - "At the beginning of your upkeep, you lose 1 life and create a 1/1 black Faerie Rogue creature token with flying." With Contamination, order Bitterblossom's trigger first (CR 603.3b) so the new Faerie pays Contamination's sacrifice.
   - Faerie tokens are tokens, so they do not trigger Overburden (nontoken creatures only), and Torpor Orb is irrelevant to them. Cursed Totem does not stop Skullclamp or Phyrexian Tower, because those are not creature abilities.
   - Opposition can tap a summoning-sick Faerie, because its tap is not a {T} cost (CR 302.6 applies only to {T}/{Q} costs).
   - Costs: 1 life every upkeep, stacking with Necropotence and our own Ancient Tomb / Mana Vault damage. It is a two-mana sorcery-speed permanent that dies to enchantment removal.
   - Bounded token-engine measurement (Tevesh castable, or Bitterblossom seen plus two mana including B, by turn 4; tutors ignored):

     | Lock state | Baseline (Tevesh only) | Candidate |
     |---|---|---|
     | No lock | 0.1532 | 0.2309 |
     | Contamination | 0.1187 | 0.2019 |
     | Blood Moon | 0.1111 | 0.1807 |
     | Artifact hate | 0.036 | 0.1071 |

5. **Windfall (the cut).**
   - Loss: a two-mana wheel, legal fuel for Underworld Breach, and refill after Necropotence or a Moon turn. It is in 53/81 Kraum + Tevesh cEDH lists.
   - Why it goes: in a stax deck it refills every opponent unless Narset, Parter of Veils or Notion Thief is out, and it is in none of the six Spellbook combos. Wheel of Fortune keeps the wheel lines (1368-1878-2706, 1368-2706-3518).
   - The blue Force pitch count drops 22 → 21 (exact hypergeometric, turn 1 0.7748 → 0.756).
6. **Staged Opposition, not counted.**
   - P(seen and castable by turn 4): Opposition 0.0329, and 0.0034 under Contamination.
   - Static Orb, which it would replace, is at 0.0599 and 0.0584.
   - Opposition needs {U}{U} under our own colour locks and clashes with Static Orb, so it stays an owner option only.
7. **Combo / bracket disclosure.**
   - Commander Spellbook find-my-combos: 6 → 6 complete combos, all unchanged:
     - Underworld Breach + Lotus Petal + Brain Freeze (1368-1414-4856);
     - Underworld Breach + Lion's Eye Diamond + Brain Freeze (1368-3518-4856);
     - Underworld Breach + Jeska's Will + Wheel of Fortune (1368-1878-2706);
     - Underworld Breach + Wheel of Fortune + Lion's Eye Diamond (1368-2706-3518);
     - the two Helm of Obedience lines (2581-5065, 2163-5065).
   - Neither swap card is a Game Changer: 22 → 22. **Bracket 5 (cEDH)**, unchanged.
8. **Exceptions:** none.
   - Kraum, Ludevic's Opus (Commander 2016, `c16`, released 2016-11-11) and Tevesh Szat, Doom of Fools (Commander Legends, `cmr`, released 2020-11-20) are both Commander-legal per live Scryfall, both have Partner, and neither is a Game Changer.
   - All 100 cards are legal and inside U/B/R. Archon of Emeria, Silence, Orim's Chant and Ethersworn Canonist are off-identity (W) and excluded.
9. **Losses.**
   - The candidate loses Mox Amber (the rare turn-1 Ragavan + Amber burst, and a zero-cost artifact) and Windfall (a cheap wheel).
   - What the alternatives would lose:
     - Bitterblossom over Cyclonic Rift: the main mass bounce (50/81).
     - Bitterblossom over Magus of the Moon: the third land-lock piece.
     - Arcane Signet over Overburden: an owner-kept lock piece.
     - Opposition over Static Orb or Magus of the Moon: a cheaper, more deployable lock.
10. **Prior owner history.** The owner-removed and owner-rejected cards and classes in the 2026-10-14 decisions are not re-added (see the I memo). Bitterblossom is not a symmetric tax and not part of the turbo package.
11. **Distinctness.** Nonbasic names shared, candidate/baseline, from the registry Archidekt exports:
    - Kefka, Court Mage 68/67
    - Rograkh, Son of Rohgahh + Silas Renn 65/66
    - Kess, Dissident Mage 65/65
    - Jeleva, Nephalia's Scourge 64/64

    The swaps lower overlap. Mox Amber is shared with Rograkh/Silas, and Windfall with Rograkh/Silas and Kess. Bitterblossom is in none of the four, while Arcane Signet is in three. The shared cards are the Grixis cEDH staple core; the 24 Grixistax-unique stax and win cards are listed in the decision review.
12. **Verdict:** RESEARCH_ONLY. Two genuine swaps; the five-swap floor is not met without padding. Not owner-presentable and NOT owner approved.
