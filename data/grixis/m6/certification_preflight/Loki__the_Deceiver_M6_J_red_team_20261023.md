# Loki__the_Deceiver (Loki, the Deceiver) — M7 red-team memo (2026-10-23)

1. **Commander removed or the trigger fizzled.**
   - Loki ({1}{U}{B}{R} 4/4) does nothing on the turn he is cast unless Lightning Greaves or Swiftfoot Boots gives haste.
   - His attack trigger targets another Villain. If that Villain is removed in response, the trigger fizzles (CR 608.2b).
   - Greaves' shroud also stops Loki's own trigger from targeting the equipped Villain (CR 702.18a); Boots' hexproof does not (CR 702.11b).
   - Protection: Fierce Guardianship, Deflecting Swat, An Offer You Can't Refuse, Mana Drain, Boots and Greaves (Cover of Darkness gives Villains fear, which is evasion, not protection). Recasting Loki costs commander tax (CR 903.8).
2. **Attack triggers on the copy (the selection rule).**
   - The token copy enters tapped and attacking. It was never declared as an attacker, so "whenever ~ attacks" abilities do not trigger (CR 508.4).
   - Enters triggers do fire (CR 603.6a), and so do combat-damage triggers.
   - The cuts fail this test. Crimson Cowl's trigger needs nontoken Villains attacking; the copy is a token, and the trigger fires on declaration only. Killmonger's pump is an attack trigger. Both adds' value is an enters trigger.
3. **Ultimo, Civilization's End (swap 1).**
   - On cast, and on every Loki copy, each opponent sacrifices a creature of their choice. That gets past hexproof, ward and indestructible.
   - With Roaming Throne naming Villain, the copied enters trigger fires an additional time.
   - "{2}{B}, Discard this card" is an instant-speed each-opponent edict when Ultimo is stuck in hand.
   - Costs:
     - Six mana where Crimson Cowl costs three.
     - Opponents choose the sacrifice, so they lose their worst creature, and tokens blank it.
     - P(MV ≤3 Villain by turn 3): 0.3005 → 0.2834 for this swap alone.
     - EDHREC adoption is against it: 131/2281 Loki decks, and it is absent from all four Loki commander pages, against Crimson Cowl's 862/2281 (optimized 5/25).
   - Staged alternative cut: Ultimo over Kang Prime, keeping Crimson Cowl.
4. **Elektra, Daughter of the Hand (swap 2).**
   - On cast, and on every Loki copy: destroy target creature an opponent controls with power 3 or less. That covers mana creatures, utility creatures and many commanders.
   - Sneak {1}{B}{B} (CR 702.190): during declare blockers, return an unblocked attacker you control (for example, Loki's doomed token copy) to hand and cast Elektra tapped and attacking. Her trigger still resolves. It is a cast Villain spell, so Madame Hydra makes a token and Baron Strucker / Tombstone reduce the cost.
   - Costs:
     - It is a targeted destroy, so hexproof, ward, indestructible and power 4+ stop it.
     - BB at four mana.
     - Killmonger's copy can still connect for an artifact sacrifice and a Treasure (its combat-damage half works on a copy). That artifact removal is a real loss.
     - EDHREC: Elektra 530/2355, optimized 4/26, against Killmonger's 796/2258 and 6/25.
   - Staged alternative cut: Elektra over Iron Monger, Sadistic Tycoon, keeping Killmonger.
5. **Pass C requested tests (bounded).** Seeded goldfish (seed 28, N=20000) plus an exhaustive rules grid.
   - **Strionic Resonator over Swiftfoot Boots: staged, not counted.**
     - Strionic copies Loki's trigger (CR 707.10c) for {2}. But the {2} is payable on an attack turn only 0.0164 by turn 5 and 0.0393 by turn 6.
     - Grid: Strionic gives more copies in 80/756 paired cells. Boots adds a whole Loki combat in 144/342 of its marginal cells, and more copies in 48.
   - **Seize the Day over Black Market Connections (and over Urza's Incubator): rejected.**
     - It needs a postcombat cast with Loki alive (CR 500.8). That is castable in only 0.0219 of games by turn 6.
     - Grid: more copies in 42/756 cells, but fewer total draws in 630/756 once Black Market Connections' draw is counted. Optimized 2/26.
6. **Combo / bracket.**
   - Commander Spellbook find-my-combos: 0 included combos in the baseline, the candidate and all eight alternatives. Almost-included: 28 baseline, 28 candidate, 31 for the Strionic variant and 29 for the Seize variant.
   - Game Changers 5 → 5 (Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Jeska's Will, Rhystic Study). **Bracket 4 (Optimized)**, unchanged.
   - The GrokBot advisory's "B3" label with 5 Game Changers was internally inconsistent; Pass C flagged it, and it is corrected to B4 here.
7. **Legality and exceptions:** none.
   - Loki, the Deceiver (Marvel Super Heroes Commander, `msc`, released 2026-06-26) is legal and released per live Scryfall, and is not a Game Changer. Both adds are released and legal. All 100 cards are legal and inside U/B/R.
   - Unreleased and excluded, never called legal: Hela, Mistress of Darkness // Dark Tutor (release 2027-04-09) and Mirror Universe Intrusion (release 2026-11-13).
   - Banned: Dockside Extortionist and Jeweled Lotus.
8. **Losses.**
   - The candidate loses Crimson Cowl (a cheap Villain and a token engine when nontoken Villains attack) and Killmonger (a cheap trampler with artifact removal on connection).
   - Both are three-drops, so the early curve thins.
9. **Prior owner history.**
   - Not re-added: the owner's 2026-10-14 removals (Construct a Cosmic Cube, The Masters of Evil, Reliquary Tower) and rejections (Kindred Dominance over Blasphemous Act, Raise the Palisade, Endless Ranks of HYDRA, attack-trigger-centric Villains such as Puppet Master, String Puller and Vulture, Scheming Scavenger, the Thassa's Oracle / Demonic Consultation / fast-combo class, and additional clone effects).
   - Kindred Charge, Twinflame and Helm of the Host are rejected as the clone class.
   - The owner's adds (Red Ghost, Intangible Genius; Titan of Littjara; Hall of Echoes) are kept.
10. **Distinctness.** Nonbasic names shared, candidate/baseline, from the registry Archidekt exports:
    - Doctor Doom, King of Latveria 53/53
    - Be'lakor, the Dark Master 42/42
    - Admiral Brass, Unsinkable 40/40
    - Nathan Drake, Treasure Hunter 40/40

    The swaps leave overlap unchanged. The 24 Loki-unique names are listed in the decision review.
11. **Verdict:** RESEARCH_ONLY. There are two genuine swaps, and the five-swap floor is not met without padding. The deck is not owner-presentable and NOT owner approved.
