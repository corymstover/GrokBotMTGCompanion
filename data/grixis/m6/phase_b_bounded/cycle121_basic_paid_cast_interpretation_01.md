# Cycle 121 — Source-locked, basic-land-only paid-cast evidence

**Source:** The engineering authority's exact approved 99-card project deck blocks and archived Scryfall Oracle, matched to all three Cycle120 source-approved logical SHA hashes and recorded raw TXT approval hashes. The local historical ZIP is **not** a CI input. No authorized canonical list changes.

**Verified by:** [GitHub Actions #39193379838](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/39193379838), head `d466e3d1654b87663964a7477344f452c6222c0f`, 15 positive/adversarial tests, frozen Scryfall checksum, 3072 deterministic source-library pairs (6144 arm views), identical repeated JSON receipt. Full gate output is the run's `cycle121-source-locked-basic-land-cast-receipt` artifact.

## Source-paid casts under a deliberately restricted mana model

Per 1,024 seeded paired source-library samples (7 opening + one draw at the start of each own turn through turn 8, no mulligans/tutors/extra draws):

| Deck | Named exact approved slot | Drawn | Supported paid cast or conditional entry | Named candidate | Drawn | Supported paid cast |
|---|---|---:|---:|---|---:|---:|
| Gwendlyn Di Corci | Opposition Agent | 144 | 16 | Aphetto Alchemist | 144 | 37 |
| Nicol Bolas, the Ravager | Mox Diamond | 144 | 51 | Aetheric Amplifier | 144 | 3 |
| Mai and Zuko | An Offer You Can't Refuse | 144 | 0 | The Enigma Jewel // Locus of Enlightenment | 144 | 0 |

The counts **are not win rates, optimal plays, or improvement evidence**. Samples use an identical same-seed physical slot and shared unchanged 98 cards; cross-deck singleton draw counts are correlated. Only printed *basic lands* supply colored mana, with one basic land drop per turn. Nonbasics, ramp, tutor effects, opponents, free/alternative costs, triggered abilities, command-zone casting and full stack priorities are unsupported. Source physical main cards conserve unique UIDs across hand, battlefield, library and graveyard.

- **Gwendlyn:** `Opposition Agent` is supported only as an own-main-phase permanent cast for {2}{B}; flash/opponent tutor replacement value is unmeasured. `Aphetto Alchemist` is supported only as a cast for {1}{U}; its tap/untap, summoning sickness and extra Gwendlyn activation effects do not follow from resolving it.
- **Bolas:** `Mox Diamond` enters only with the source pilot discarding an actual physical *basic* land from hand. This models only the replacement-cost branch; nonbasic discards, the Mox's mana ability and commander acceleration were not simulated. Amplifier {3} may resolve using basic lands; neither its loyalty doubling nor Ravager transformation was simulated.
- **Mai/Zuko:** The approved deck has no basic lands. Both zeroes are expected in a basic-only system and **cannot support any card choice**. The model refuses to counter a nonexistent opponent noncreature spell with An Offer. The Jewel is correctly printed **{U}**, enters tapped, and has restricted {C}{C} only usable for activated abilities; that restricted mana is not executed.

## Material defect found and repaired before accepting the receipt

The earlier **local-only October 15 ZIP model incorrectly used {1} as the cost of The Enigma Jewel**. It was not accepted in the GitHub engineering repository. The first GitHub CI attempt correctly FAILED its frozen Oracle cost assertion at [run #39193272560](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/39193272560). The GitHub runner and adversarial test were corrected to {U}; the 15-test run passed. The obsolete local README/receipt should not be treated as authoritative current card mechanics.

The engineering repository's exact deck source logical-hash verification and pinned frozen Oracle are stronger guards than the noncryptographic FNV inventory comparison in the local preliminary work. The raw approved TXT SHA remains a recorded authority field, not a fresh independently downloaded/rehash check in this CI run.

## Explicit unfinished gates

- **No** realistic nonbasic-land mana, stacks/counterspell responses, commander-specific actions or opponent decisions.
- **No** independently completed Pass C/I/J, Phase B evaluation, game-winning outcomes, tested-pool zero improvement or M6 acceptance.
- **No** card swaps, canonical deck unlocks/approvals, milestone changes or 62-deck source replacements.
- **Next cycle:** isolate true nonbasic-land mana and conditional entry abilities with archived Oracle and source-physical land provenance, then retest Mai and Zuko's ability to legally pay {U}; preserve paired-seed and opponent-response limits.

**Conclusion:** Source-conserved payability is a narrower diagnostic than strategic performance. These counts do not rank the candidates or authorize a deck upgrade.
