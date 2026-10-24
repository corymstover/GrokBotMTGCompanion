# Cecily / Bjorna with Lutri — ChatGPT independent M7 Rev2, ten swaps (2026-10-23)

**RESEARCH CANDIDATE — NOT OWNER APPROVED, NOT CANONICAL.** Historical canonical approved October 13 list remains locked. No legal exceptions are silently normalized.

## Provenance and physical convention
- Tracker deck #8 `Cecily__Bjorna__Lutri`. Baseline canonical `refinement/decklists/Cecily__Bjorna__Lutri_Approved_2026-10-13.txt`, raw 100-card SHA `553838da88fe00974e74664633be5051c4f1a0879baa71de81ca9f880e5a6d28` (no companion line).
- GrokBot first-pass PR #656, raw candidate `2cc7227f954e728e0b37949b74f9575128b2c82250f53e211289aa60e4fa1717`, six swaps.
- ChatGPT ten-swap candidate `data/grixis/m7/candidate_lists/Cecily__Bjorna__Lutri_ChatGPT_M7_Rev2_Ten_Approval_Candidate.txt`, raw SHA-256 **`e4028f06d2d928ad06fb8667ae4bba77c31b4f97c1d4fb5490f83b73eb6d6b5d`**. This file includes a physically separate companion line.
- **Exactly 100 Commander deck cards:** 2 commanders (Cecily, Bjorna) + 98 main library. `1x Lutri, the Spellchaser [Companion]` sits **outside** the 100. The text artifact therefore has 101 physical cards including companion and 100 unique names / 100 rows (Island ×2).
- **Project exceptions only for this designated deck:** Lutri is officially **banned as a companion** (Scryfall card-level legal response does not authorize the banned companion); Trade Secrets and Yawgmoth's Bargain are officially **Commander banned** and remain only by owner-authorized project exception. Every other selected name has archived current Oct23 Scryfall Oracle ID/text, legal Commander status, and UBR identity.
- Frozen baseline, registry and approved artifacts are not modified by this engineering research PR.

## Ten independent whole-deck swaps

| Add | Remove | Judgment |
| --- | --- | --- |
| Strionic Resonator | Emry, Lurker of the Loch | Copy Cecily's attack trigger and Lutri ETB, even on entry turn; costs {2} plus tap. Trade slow artifact recursion. |
| Echo, Perceptive Prodigy | Goblin Engineer | Cheap {1} copy of creature-source Cecily attack or Bjorna activated goad, plus vigilance means tap while attacking. Must have been under control since start of turn to activate. |
| Twenty-Toed Toad | Sai, Master Thopterist | Attack with a 20-card hand wins. Wizard/hand-size synergy; loses a Thopter-fodder engine for Bjorna. |
| Sea Gate Restoration // Sea Gate, Reborn | Dark Deal | MDFC offers a potentially untapped blue source and free-cast massive draw/no hand size. Cut wheel shrank its owner's hand by one. |
| Deflecting Swat | Mana Geyser | Commander-enabled free change of targets on threat to Cecily/Toad; loss of one ritual's big red burst. |
| Mana Drain | Seething Song | Adds premium stack control and delayed colorless mana; sacrifices direct {3}{R} → {R}{R}{R}{R}{R} burst. |
| **Fevered Suspicion** | **Cruel Ultimatum** | Commander-freecast multi-opponent spell chaining, cast from hand qualifies for rebound next upkeep; Lutri can copy it (copy does not rebound). Cruel hits only one opponent for heavy UUBBBRR. |
| **Aminatou's Augury** | **Wheel of Misfortune** | Commander-freecast can access a land plus spells across distinct card types from top eight, more ceiling than a sixth/seventh symmetric hand reset. Wheel's cheap reload lost, but Wheel of Fortune/Breach and other wheels remain. |
| **City of Brass** | **Crumbling Necropolis** | Unconditional untapped U/B/R improves attack setup; pay 1 damage when tapped. |
| **Mana Confluence** | **Fabled Passage** | Unconditional untapped U/B/R instead of frequent tapped basic fetch; pays life and loses Brainstorm-shuffle utility. |

## Commander-first reasoning and counterarguments
- Cecily attacks and **then** draws one/loses one, checking for 11 cards as the trigger resolves. The check is not intervening-if; 10 before draw suffices.
- Multiple free spells can be cast via Harmonic Prodigy, Strionic Resonator and Echo. Each copied Cecily trigger requires its own legal instant/sorcery in hand and enough cards after prior casts. Copying the trigger is not the same as copying a spell; spell copies do not get "cast" triggers.
- Toad, a Frog Wizard, has its win condition checked upon resolution. When Cecily and Toad both attack, stack Cecily's draw/free-cast trigger above Toad's win trigger. Free-casting Peer into the Abyss or Sea Gate Restoration can raise the hand to 20 before Toad resolves, but life total and empty-library risks remain real.
- Bjorna is still supported by Ichor Wellspring, Academy Manufactor, Oni-Cult Anvil, Third Path Iconoclast, Storm-Kiln Artist, Big Score and Brass's Bounty, though removal of Sai/Engineer/Emry lowers some artifact recursion/fodder density. Echo can copy Bjorna's activated ping/goad without paying a second sacrifice cost.
- Lutri's companion {3} special action and normal {1}{U/R}{U/R} cast remain payable, and copying a free-cast spell is not casting the copy. Never call Lutri officially companion-legal.
- Fevered and Augury add high-MV payoffs at the cost of normal hand castability. Nonland average mana value increases, but 33 normal lands + 1 Sea Gate modal land + 9 rocks and improved two early lands reduce mana stalls. No multiplayer win-rate claim.
- Alternate research candidates challenged and not chosen: Enter the Infinite duplicates Peer/Toad and is near-dead by hand; Time Stretch shifts toward generic extra-turns; Nerd Rage draws two and enhances an attack but risks losing the enchanted commander and is less secure than the existing Robe/Greaves package; Wizard Class/Body of Knowledge duplicate maximum-hand effects; Gogo and Peter Parker's Camera add redundant, mana-intensive trigger copies; Reliquary Tower damages colored mana; Galazeth Prismari is artifact-focused but competes with trigger/hand slots; Galvanic Iteration doubles a free spell but competes with more direct payoffs; Wisdom of Ages is recursion but requires a stocked graveyard and competes with Breach. None is mandatory by EDHREC prevalence.
- EDHREC pair sample is small and High-Lift values are discovery, not proof.

The two rituals removed (Mana Geyser and Seething Song) materially weaken burst ramp; the extra untapped lands and nine retained rocks do not fully replace their explosive ceiling. The three project exceptions are not officially legal for ordinary Commander and remain confined to this specific deck.

## Final check and limits
- 100 physical Commander-deck cards + separately project-authorized Lutri companion; 2 commanders, 98 library, Island ×2; correct singleton otherwise.
- 33 conventional lands plus 1 MDFC, 9 rocks, 10 unchanged Game Changers, Power Bracket 4. Archidekt tags **Spellslinger / Wheels / Hand Size Matters**.
- Existing Spellbook findings (Breach/Wheel/Jeska finite; Peer/Crawler; Peer/Teferi library exhaustion hazard) and first-pass Toad+Peer line are bounded references. No updated full-list Spellbook exhaustive search or new formal M6 I/J seal yet; do not claim all possible loops verified by index.
- The owner-equivalent Pass C waiver is expressly **non-independent**. This exact Rev2 requires owner approval of SHA `e4028f06d2d928ad06fb8667ae4bba77c31b4f97c1d4fb5490f83b73eb6d6b5d` before any canonical update.
