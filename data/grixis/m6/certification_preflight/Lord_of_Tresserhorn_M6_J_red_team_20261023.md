# Lord_of_Tresserhorn (Lord of Tresserhorn) — M7 red-team memo (2026-10-23)

1. **Commander text: attack this first.**
   - Lord's Oracle text, identical in the frozen cache and on live Scryfall, reads: "When Lord of Tresserhorn enters, you lose 2 life, you sacrifice two creatures, and target opponent draws two cards. {B}: Regenerate Lord of Tresserhorn."
   - There is no opponent-regeneration clause. The brief's paraphrase was wrong and is not used.
   - If you control fewer than two other creatures, Lord sacrifices himself (ruling 2004-10-04).
   - Regeneration replaces destruction only (CR 701.19a). It never saves him from his own trigger, from edicts or from -X/-X.
2. **Trigger handling.**
   - Torpor Orb and Karn stop the trigger. So does Dress Down, if it is already on the battlefield.
   - Stifle, Tale's End and Consign to Memory counter it on the stack. A countered trigger does nothing: no life loss, no sacrifice and no cards.
   - Removing a suppressor after Lord has entered does not create the trigger late.
3. **Fierce Guardianship (swap 1).**
   - It is free only while you control a commander on the battlefield (CR 903.3d). While Lord is a spell on the stack it costs {2}{U}, and Stubborn Denial's ferocious is off.
   - Both cards counter noncreature spells only, so neither protects Lord from a creature-spell race. Each can counter a counterspell aimed at Lord.
   - B4: FG answers 17/40 cells and Denial 9/40. Denial answers no cell that FG misses.
   - Costs:
     - Game Changers 2 → 3, still within the Bracket 3 cap; the deck stays Bracket 4 because of its combos.
     - It is the most homogenizing card: it is in 54/61 other project decks.
     - It replaces an owner-cycle add.
4. **Consign to Memory (swap 2).**
   - It counters triggered abilities and colourless spells, not noncreature spells in general.
   - Loss: Feed the Swarm was one of the deck's two hard enchantment answers. After the swaps, Chaos Warp is the only one, plus Otawara bounce. A resolved Rest in Peace, Torpor-style hate or an opposing Aura is harder to remove.
   - Feed the Swarm's life loss stacks with Lord's own 2.
5. **Black Market Connections (swap 3).**
   - Its life costs stack with Lord's 2, Mana Confluence and the fetches.
   - It does nothing the turn it lands.
   - Cover of Darkness gave fear, which is stopped by black and artifact blockers. Shizo still gives Lord fear.
6. **Ornithopter of Paradise (swap 4).**
   - Summoning sick, so it does not tap for mana on the turn it is cast. Fellwar Stone does.
   - It dies to sweepers and edicts. It is counted as fodder, not as a reliable ramp piece.
7. **Skullclamp (swap 5).**
   - Clamped to Lord he is 11/3, so he dies to 3 damage. Regeneration still saves him from lethal damage.
   - Loss: Sheoldred's Edict. Spot removal goes 5 → 3: Terminate, Deadly Rollick and Chaos Warp. B3: 2/14 threat cells lose their only spot answer, though Toxic Deluge and Blasphemous Act still cover them.
   - No infinite is claimed.
8. **Pass C items (bounded).**
   - Soul's Fire: retained alternative.
   - Distortion Strike over Rogue's Passage: retained alternative.
   - Dress Down layer-6 truth table: 24 cells, pinned in the mechanics test.
   - Temur Battle Rage: an owner cut, not reopened, so inadmissible.
9. **Combo / bracket.**
   - Commander Spellbook: 19 included combos in the baseline, the candidate and every alternative. Almost-included goes 283 → 289.
   - The two-card Gravecrawler + Phyrexian Altar loop needs another Zombie, such as Lord himself, a BMC changeling token or a Wilhelt token.
   - **Bracket 4 (Optimized)**, unchanged.
10. **Legality.**
    - All 100 cards are commander-legal on live Scryfall and inside U/B/R.
    - Lord of Tresserhorn is legal and not a Game Changer.
    - No unreleased or banned card is used, and no project exception is needed.
11. **Prior owner history.**
    - Not re-added: Temur Battle Rage and the other owner cuts.
    - Not added: the author-rejected cards that Pass C did not reopen (Embercleave, Psychotic Fury, Glistening Oil, among others).
    - All five cuts are flagged, because each was an owner add or an explicit audit KEEP.
12. **Open question.** Orcish Bowmasters is unmeasured and rejected with LOW confidence. It would be a fourth Game Changer, and the deck's suppression switches off its enters trigger.
13. **Verdict:** `READY_FOR_EXACT_OWNER_APPROVAL_NOT_YET_APPROVED`. This is not owner approval and the canonical list is unchanged.
