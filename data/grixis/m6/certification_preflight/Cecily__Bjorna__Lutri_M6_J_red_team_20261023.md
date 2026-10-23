# Cecily, Haunted Mage + Bjorna, Nightfall Alchemist (companion Lutri) — M7 red-team memo (2026-10-23)

1. **Commander removed or taxed:** Cecily (MV 4) is the engine. Without her:
   - Twenty-Toed Toad still wins with twenty cards in hand (Peer into the Abyss, Sea Gate Restoration, Trade Secrets, Bargain).
   - Sea Gate is still a land or a seven-mana refill; Swat and Mana Drain are still interaction.
   - Resonator and Echo still copy Archmage Emeritus, Storm-Kiln Artist, Psychosis Crawler and Niv-Mizzet triggers, but they lose
     most value. Echo copies only abilities from a creature source.
   Protection rises: Deflecting Swat and Mana Drain join Fierce Guardianship, Counterspell and Lightning Greaves.
2. **Hand-size trap:** Cecily's maximum is eleven, Toad's is twenty. Hand size is checked only at cleanup (402.2/514.1), and
   the two effects apply in timestamp order (613.11), so the later one wins. Sea Gate Restoration's "no maximum hand size"
   lasts only the turn. Discarding at cleanup is the risk if Toad leaves first or arrived first.
3. **Copy model:** each copied Cecily trigger draws, loses 1 life and re-checks hand size on resolution (the check is inside the
   effect, not an intervening-if). Copies of the trigger are not spells; the spell cast from the copy IS cast, so magecraft and
   Lutri (which needs a cast spell) work with it. Lutri's ETB copies a spell; that copy is not cast (707.10).
4. **Mana screw:** lands 33 → 33 (+ Sea Gate MDFC), rocks 9 → 9. The two rituals are gone; see the mana memo.
5. **Wipes:** Resonator (artifact) survives creature wipes; Echo, Toad and the commanders do not. In Garruk's Wake, Cyclonic Rift
   and Toxic Deluge are unchanged.
6. **Graveyard hate:** blanks Underworld Breach lines; the adds do not depend on the graveyard. Emry/Engineer recursion is gone.
7. **Life loss:** each copied Cecily trigger costs 1 life, plus Peer into the Abyss (lose half our life, rounded up) and Yawgmoth's Bargain's
   pay-1-life draws. Toad + Peer: Peer costs half our life before Toad's attack trigger checks; the line needs Cecily's free cast or seven mana.
8. **Decking:** Peer draws half the library rounded up; drawing from an empty library loses only at the next state-based check
   (104.3c/121.4). The finite Toad model asserts the library stays nonnegative.
9. **Combo / bracket disclosure:**
   - Baseline Spellbook combos: 1368-1878-2706 (Breach + Wheel of Fortune + Jeska's Will, finite chain), 1561-2384 (Psychosis Crawler
     + Peer), 1561-5042 (Peer + Teferi's Ageless Insight; self-deck risk).
   - Candidate adds one: 1561-5850 (Twenty-Toed Toad + Peer into the Abyss, "Win the game"). It is a deterministic alternate win on
     attack, not an infinite loop.
   - No infinite combo is claimed. Game Changers are unchanged at 10 (Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Jeska's
     Will, Mystical Tutor, Notion Thief, Rhystic Study, The One Ring, Underworld Breach, Vampiric Tutor). **Bracket 4**, unchanged.
10. **Exceptions:** Lutri as companion (Commander companion ban), Trade Secrets and Yawgmoth's Bargain are documented project
    exceptions for this deck only. They are never described as officially legal and never applied elsewhere.
11. **Losses:** Emry, Goblin Engineer and Sai artifact value; Dark Deal; Mana Geyser and Seething Song bursts.
