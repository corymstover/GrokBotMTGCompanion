# Loki__the_Deceiver (Loki, the Deceiver) — M6 I local-best memo for the M7 research candidate (2026-10-23)

This memo is evidence only. The candidate is NOT owner approved, NOT M6 certified and NOT owner-presentable. It is RESEARCH_ONLY: two genuine swaps, below the five-swap floor. The canonical list is unchanged.

Scope: the eleven complete configurations in `data/grixis/m6/ij/tested_pools/Loki__the_Deceiver_M7_tested_configurations_20261023.json`, plus the named single-card contenders. Each configuration is 100 cards (1 commander and a 99-card library). This is not a global or statistical optimum.

Identity:
- Tracker index 27 (Deck 28), deck ID `Loki__the_Deceiver`, commander Loki, the Deceiver.
- The tracker, the overrides (APPROVED / LOCKED, 2026-10-14) and the registry agree.

Baseline:
- Canonical encyclopedia main 9b26aa28fc7e16f6652aaec292b4edf84e20db71, file `refinement/decklists/Loki_the_Deceiver_Approved_2026-10-14.txt`.
- Git blob 456d62d45e6e5ffb283a97b5603997a4d1d74c3e, introduced by canonical commit d97bc2b (2026-10-14); registry source_commit 1836b97 has the same bytes.
- Raw SHA-256 5079291c08c5af212b3d90d63ac5b01849d45c7700b1d64100ef57fb13458062. It equals the overrides `approved_list_sha256`, the registry recorded hash and the tracker `final_list_hash`, so no provenance exception is used.
- Logical hash lh1:1af6ee04….
- The registry Archidekt export `exports/grixis-archidekt/loki-the-deceiver.txt` (raw a46c0474…) is the same 100 in export format with the same logical hash, so it is current.
- Discrepancies: none material. The tracker notes still contain an older "current NOT STARTED state" sentence next to the APPROVED / LOCKED status. That is disclosed, not changed.

## Result
The research candidate (raw ce64e222…, lh1:d26a9eea…) is the canonical 100 with **+Ultimo, Civilization's End −Crimson Cowl, Master of Evil** and **+Elektra, Daughter of the Hand −Killmonger, Ruthless Usurper**. It is the local best of the tested pool.

**Two genuine improvements were found, so the deck is RESEARCH_ONLY.** Five is a floor, not a target. Twenty-one candidates were judged and fourteen incumbents were challenged. Apart from Ultimo and Elektra, every candidate failed for one of these reasons:
- **Pass C requested, tested, not better:** Strionic Resonator over Swiftfoot Boots (staged); Seize the Day over Black Market Connections or Urza's Incubator (rejected).
- **Dominated for the same slot:** Tri-Sentinel, Act of Vengeance (seven mana, targeted damage), against Ultimo.
- **Not clearly better than an incumbent:** Victor Timely, Wily Tycoon over Kang Prime (staged), Kingpin, Wilson Fisk over Madame Hydra, Archnemesis over Black Market Connections, Terminate / Bedevil (one-shot removal), Vampiric Tutor (generic tutor), Ancient Tomb (colourless, a sixth Game Changer).
- **Marginal:** Secluded Courtyard over Path of Ancestry (about one point on the goldfish, with restricted colours).
- **Does nothing on a Loki copy:** Lady Loki, Agent of Chaos (a cast trigger).
- **Owner-rejected class:** Kindred Charge, Twinflame, Helm of the Host (additional clone effects); Glorious Purpose (a Plan, like the removed Construct a Cosmic Cube).
- **Not a Villain:** Hostage Taker.
- **Invalid:** Hela, Mistress of Darkness // Dark Tutor and Mirror Universe Intrusion (unreleased, not_legal); Dockside Extortionist and Jeweled Lotus (banned).

Challenged incumbents: Crimson Cowl (cut), Killmonger (cut), Swiftfoot Boots, Black Market Connections, Kang Prime, Iron Monger, Madame Hydra, Path of Ancestry, Patchwork Banner, Stilt-Man, Oscorp Industries, plus the owner adds Red Ghost, Titan of Littjara and Hall of Echoes. All except the two cuts are kept.

## Why (commander-first)
Loki, the Deceiver ({1}{U}{B}{R} 4/4):
- "Whenever Loki attacks, create a tapped and attacking token that's a copy of another target Villain you control, except it isn't legendary and it's an Illusion in addition to its other types. Sacrifice that token at the beginning of the next end step."
- "Whenever one or more Villains you control deal combat damage to a player, draw a card."

The token is never declared as an attacker (CR 508.4), so the copied Villain's attack triggers never fire. Enters triggers (CR 603.6a), static abilities and combat-damage triggers do. The owner used the same rule on 2026-10-14 to reject attack-trigger-centric Villains.

**Swap 1: +Ultimo, Civilization's End −Crimson Cowl, Master of Evil (MODERATE confidence).**
- Crimson Cowl's trigger ("whenever one or more nontoken Villains you control attack a player") does nothing on a Loki copy: the copy is a token and was not declared. Its copy is a blank 1/3.
- Ultimo's enters trigger makes each opponent sacrifice a creature on every Loki attack, twice with Roaming Throne. It gets around hexproof and ward, and the 6/5 menace body helps the draw trigger connect. The discard mode is an instant-speed edict.
- Cost: six mana where Cowl costs three; P(MV ≤3 Villain by turn 3) 0.3005 → 0.2834 for this swap alone.
- **Data caveat:** Ultimo is in 131/2281 Loki decks and is absent from the Loki commander pages, while Crimson Cowl has 862/2281 (optimized 5/25). The case rests on the rules and on the deck's thin repeatable removal, not on adoption.
- Staged alternative cut: Ultimo over Kang Prime, keeping Crimson Cowl.

**Swap 2: +Elektra, Daughter of the Hand −Killmonger, Ruthless Usurper (MODERATE confidence).**
- Killmonger's attack pump never fires on a copy. Only its combat-damage half works, and only when a 3/3 copy connects (that player sacrifices an artifact and we create a Treasure). That artifact removal is a disclosed loss.
- Elektra's enters trigger destroys an opponent's creature with power 3 or less on every Loki copy. Sneak {1}{B}{B} lets an unblocked doomed token be returned to cast her tapped and attacking (CR 702.190); she is a cast Villain spell for Madame Hydra.
- Cost: BB, four mana, and targeted removal (stopped by hexproof, ward and indestructible). P(Loki attacks with a valid target) on turn 4 is 0.1803 → 0.1763 for this swap alone.
- **Data caveat:** EDHREC has Elektra at 530/2355 (optimized 4/26) against Killmonger's 796/2258 (6/25).
- Staged alternative cut: Elektra over Iron Monger, Sadistic Tycoon, keeping Killmonger.

## Owner direction
- Neither cut is an owner addition or explicit keep.
- The owner's 2026-10-14 swaps (Construct a Cosmic Cube → Red Ghost, Intangible Genius; The Masters of Evil → Titan of Littjara; Reliquary Tower → Hall of Echoes) are kept, and the removed cards are not re-added.
- The owner's rejections are respected: Kindred Dominance, Raise the Palisade, Endless Ranks of HYDRA, attack-trigger Villains, the Thassa's Oracle / Demonic Consultation and fast-combo packages, and additional clone effects.
- The staged alternatives are complete 100s built on the candidate, so the owner can pick one directly.

## Pass C requested tests (bounded finite versions; not win rates)
These are in `data/grixis/m7/research_challengers/Loki__the_Deceiver_bounded_measured_tests_20261023.json`, and recomputed or consistency-checked in `tests/test_m6_loki_the_deceiver_m7_mechanics.py`.

Pass C's final disposition was **NEEDS TESTING**: retain the canonical deck, and compare +Strionic Resonator −Swiftfoot Boots and +Seize the Day −Black Market Connections across:
- Loki present or absent;
- a valid or invalid Villain target;
- haste and protection;
- combat-two payability;
- response windows;
- the delayed token sacrifice.

The Pass C receipt is a NON-INDEPENDENT owner-equivalent review (ChatGPT/OpenAI GPT-6, with a technical-independence waiver).

1. **Seeded goldfish** (seed 28, 20,000 games per configuration, on the play, no mulligans):

   | Configuration | P(Loki attacks, valid target) T4 | T5 | T6 | Strionic payable T6 | Seize castable postcombat T6 |
   |---|---|---|---|---|---|
   | Baseline | 0.1803 | 0.5849 | 0.7069 | – | – |
   | +Strionic Resonator −Swiftfoot Boots | 0.1801 | 0.5867 | 0.7082 | 0.0393 | – |
   | +Seize the Day −Black Market Connections | 0.1772 | 0.5764 | 0.7044 | – | 0.0219 |
   | Candidate (Ultimo, Elektra) | 0.1682 | 0.5696 | 0.7003 | – | – |

2. **Exhaustive rules grid.** The grid crosses:
   - Loki absent / summoning-sick / ready;
   - target none / valid / removed in response;
   - no protection / Lightning Greaves / Swiftfoot Boots;
   - opposing removal timing;
   - spare mana 0–6;
   - The Master, Multiplied absent / present.

   Results:
   - Strionic gives more copies in 80/756 paired cells.
   - Seize gives more copies in 42/756, but fewer total draws in 630/756 once Black Market Connections is counted.
   - Boots adds a Loki combat in 144/342 marginal cells, and more copies in 48.

   Conclusion: neither Pass C swap is a genuine improvement.

3. **Matched-hand games against opponents.** Not run: the repo has no validated game engine for this deck and no opponent model.

Commander Spellbook: 0 included combos in the baseline, the candidate and every alternative.

## Limits
Only finite scripted rules cases and seeded proxies are tested. The deployment model has no opponent, no blockers and no removal.

- Game Changers 5 → 5 (Bracket 4).
- Average nonland MV 3.394 → 3.455.
- Commander Spellbook 0 → 0.
