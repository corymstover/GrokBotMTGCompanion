# Deck #36 — Mishra, Artificer Prodigy M7 Rev1
2026-10-26 · Engineering evidence only; candidate awaits Cory's explicit exact-hash approval. Canonical Oct 15 list remains locked and unchanged.

## Authority / source reconciliation
- Canonical: corymstover/grixis-commander-encyclopediaGPT/main, refinement/decklists/Mishra_Artificer_Prodigy_Approved_2026-10-15.txt.
- Baseline raw SHA-256: 9210aefa423dbe9cc69d18422c0d594cad6e5d0ee475d687b9f2278a2ca3b79d. Independently reconstructed from uploaded Oct15 archive and cross-checked against live canonical exact bytes.
- Exact proposed raw UTF-8 SHA-256: 45c0d559f0aa859b84e2fb52baf31fdbb683de3e7bc7f211821b50420dee9761. Candidate file is one card per line, commander first, trailing LF.
- Proposed list and both six-swap alternatives: 100 physical cards, 100 distinct names, 29 lands, one UBR commander, no exceptions. The two seven-swap alternatives also have 100 distinct physical cards.
- Current Scryfall cards/collection query 2026-10-26: all 100 named identities found, all Commander=legal, all color identities within U/B/R, current oracle_id present; retained as source-bound 100-card snapshot. Current Wizards Commander banned list checked separately. No project-specific exceptions.
- Owner status: NOT APPROVED for Rev1; old Oct15 list remains the sole canonical approved and locked one.

## Commander-first policy
Mishra's artifact CAST trigger searches eligible zones, not the stack. With counter/tuck effects under the same controller, place Mishra's trigger lower on stack; own counter or Possibility Storm moves the original to graveyard or library before Mishra's search. **Protected engines:** Blood Funnel, Nether Void, Chalice of the Void, Void Mirror, Vexing Bauble, Planar Chaos, Possibility Storm, Encroaching Mycosynth, cost-reduction/Top/Forge/Citadel/Aetherflux, KCI/Scrap Trawler/Myr Retriever/Junk Diver, Karn/Lattice. Reject generic Oracle/Consult/Breach replacement. Natural ceiling bracket 5, fringe commander-centric artifact prison-combo.

## Full 99 opportunity pass and actual role pressure
The existing October19 engineering deep review accounts for all 99 slots by name; reopened the seven counter/tuck axes, 29-land fixing, colored turn to Mishra, 0–2 mana artifacts, 4+ mana payoffs, draw/tutors, recursion, protection and Win B packages. Six elected cut slots are not the only challenged roles: also challenge Uthros Research Craft (stationed cast-draw vs Petal), Sculpting Steel (copy lock vs Grinding Station), Planar Chaos (random self-counter vs Defense Grid), Mox Amber (conditional colors vs The Enigma Jewel), Wishclaw Talisman (artifact universal tutor vs Reshape), and Blood Funnel (protected engine vs generic Scepter/Reversal).

### Six selected trades and downside
1. **+Lotus Petal / −Nullstone Gargoyle.** Turn-one zero-mana artifact that converts colorless-heavy land hands to the missing U/B/R pip, counts for cast/metalcraft and can be retrieved by Mishra under a zero-spend Bauble/Mirror trigger. Sacrifice is one-shot; loses a true first-noncreature-spell lock and Welder/Engineer Gargoyle target. This is the strongest historical Pass C unresolved tempo trade, decided qualitatively for real colored access rather than simulated win rate.
2. **+Deflecting Swat / −Praetor's Grasp.** Commander-dependent free target redirection protects Mishra/critical artifact from targeted interaction and turns opponent spell into a tactical asset; Grasp's flexible library theft is lost. Under our own Vexing Bauble or Void Mirror, free Swat gets countered as a nonartifact spell, so it must be used before that lock or cast by paying mana where legal.
3. **+Imperial Seal / −Fabricate.** One-black generic tutor to top instead of three-mana artifact-only tutor to hand improves early colored-commander/lock selection; Forge, Top and draw can immediately access the top card in prepared boards. Downside: card is not in hand immediately, two life lost, sorcery under Blood Funnel must be sequenced before prison.
4. **+Otawara, Soaring City / −Academy Ruins.** Turns a colorless-only land into an immediate blue source and channel interaction, which is an activated ability rather than a spell subject to own Nether Void/Bauble/Funnel. Costs Academy's reusable artifact top-deck rescue, mitigated by Engineer, Welder, Emry, Retriever, Diver and Scrap Trawler; channel cost still substantial.
5. **+Flusterstorm / −Mana Drain.** Single-U stack-war defense at early cEDH windows, storm scaling versus chains, improving odds of holding interaction while deploying 1UBR Mishra. Loses UU unconditional counter of artifact/creature/planeswalker and delayed colorless burst; under own nonartifact-counter prison Flusterstorm may still fail.
6. **+Grinding Station / −Thought Monitor.** Two-mana searchable artifact makes KCI/Trawler recycling both a self-mill selection route for Welder/Emry and a secondary mill payoff for repeated artifact ETB/sac loops. Loses frequently affinity-discounted 2-card ETB refill and a flying body; mill wins only with an actually repeatable source-paid artifact loop, never from merely having Station+KCI.

### Material rejected and retained candidates
- **Reshape** for Wishclaw or Fabricate: a real battlefield-put tutor and artifact-sac enabler, but its UUX plus additional sacrifice narrows openings and its nonartifact sorcery self-counters under Blood Funnel. Retained in explicit seven-swap challenger.
- **Defense Grid** for Planar Chaos: two-mana artifact protection when comboing on own turn but taxes *our* counterspells on opponent turns and deletes the Planar Chaos cast-counter rescue. Seven-swap challenger only.
- **Uthros Research Craft cut for Petal:** preserves Gargoyle prison but loses repeatable draw through countered artifact casts; complete six-swap alternative 50b95dc782087e5565fb66fe21c1f4d0c21bdd8df97ac37a8aebc9a9f59a7468.
- **Sculpting Steel cut for Grinding Station:** keeps Thought Monitor draw but loses a lock-piece copy and extra artifact recursion flexibility; complete six-swap alternative cceed4d31b1dece7f26ef1fb03b33626463e7670898c840cb6fe974e52527e5e.
- **The Enigma Jewel for Mox Amber:** restricted activated-ability mana and enters tapped; it does not solve colored 1UBR commander casting. Mox Amber is live once Mishra/another qualifying legend arrives.
- **Isochron Scepter + Dramatic Reversal for Blood Funnel + Planar Chaos:** rejected prior M6 advisory. Scepter's 2 activation mana is not mana spent to cast the free-copy Reversal; our own Vexing Bauble/Void Mirror stop that nonartifact free copy and removing Blood Funnel destroys a key asymmetric Mishra mechanic.
- **Ice Cave:** other players may pay to counter a spell; the caster cannot pay for their own spell with Ice Cave to retrieve it, and mirrored mana payments don't provide consistent Mishra break.
- **Winter Orb / Static Orb / Cursed Totem:** slow or cripple our own critical color, Welder, Engineer and Metalworker resources; none recovers artifact spells for Mishra.
- **Power Artifact + Grim Monolith:** unlimited colorless mana is real with Grim but doesn't natively supply UBR or a standalone outlet; the Aura is a nonartifact vulnerable to our own denial. Unselected over the existing Top/Citadel/KCI and actual commander's locks.
- **Beseech the Mirror / Jeska's Will / Underworld Breach:** Beseech's BBB requirement is harder than our urgent pip constraints, Will depends on opponent hand/our nonartifact lock and Breach package shifts toward generic Grixis game plan.
- **Kuldotha Forgemaster:** strong artifact tutor but 5 mana, summoning sickness and three artifact sacrifices crowd a list already dense with Engineer/Welder/Whir/Transmute.

## Whole-package alternatives — exact complete 100s
- Prison-first six-swap 50b95dc782087e5565fb66fe21c1f4d0c21bdd8df97ac37a8aebc9a9f59a7468: keep Nullstone, make Petal replace Uthros. Preserves seven-axis prison but loses stationed draw through counters, and still has nine-mana dead hands. Rejected relative to primary.
- Artifact-refill-first six-swap cceed4d31b1dece7f26ef1fb03b33626463e7670898c840cb6fe974e52527e5e: keep Thought Monitor, cut Sculpting Steel for Grinding Station. Preserves cards now, loses ability to copy key lock/Forge/Lattice artifacts and Metalworker utility. Rejected relative to primary.
- Seven swaps add Reshape / cut Wishclaw, 708d03593c2864df18d6bbcaecec12bc2fd07a46d011a5ce2849cd6c9e2129d4: greater artifact-board tutor access but less universal immediacy and another spell susceptible to self-stax; rejected.
- Seven swaps add Defense Grid / cut Planar Chaos, 82c2a25895910c947e20d7eb4ff2d49c31e76457e4be87857e789d688b98f7e5: better own-turn protection before lock, weakens opponents'-turn counterspell defense and removes real Mishra rescue; rejected.
These were compared as full legal physical 100s, not separate 101st-card claims. The two higher-swap challenges are meaningful; extra changes are not selected just to increase swap count.

## Paid rules and adversarial finite cases (not win-rate sims)
- Baseline three land drops Badlands + Island + Ancient Tomb can offer one B/R pip, U and CC but not B and R simultaneously; Lotus Petal supplies missing pip for payable 1UBR Mishra. Before/after comparison is exact resource accounting, not probability.
- Mishra's Workshop makes CCC *only for casting artifact spells*, never for commander casting, activated Channel or paying Nether Void's triggered {3} tax.
- Under Vexing Bauble, free-cast Swat is countered because no mana was spent; paying normal 2R can avoid Bauble and also Void Mirror if R spent, assuming other lock/tax conditions permit.
- Under own zero-spend trigger on a Petal cast, the card enters grave first then Mishra's pending trigger may recover it; if Mishra is absent when Petal is cast or card leaves grave first, no recovery. Once a Mishra trigger is on stack, removing Mishra later does not itself counter that trigger.
- Possibility Storm tucks original from hand; it is available in library when earlier-ordered Mishra trigger searches. A replacement free spell may be countered by Bauble or Mirror; this is not unconditional for spells from other zones or uncounterable spells.
- New Grinding Station untaps upon artifact ETB. It must tap and sacrifice an actual controlled artifact per milling activation; infinite mill requires a repeatable, payable recursion loop with sufficient artifacts, not an assumed unbounded KCI.
- The presence of Planar Chaos or Blood Funnel can counter own nonartifact Imperial Seal/Flusterstorm and free protection; deploy and protect before locking. An adversary can exile artifacts between self-counter and Mishra recovery and can stop the engine by preventing initial Mishra cast.
- No empirical multiplayer games, win-rate uplift, exhaustive mulligan Monte Carlo or generic Magic simulator claimed. Existing P0 case blueprint comprises C1 K1 K2 K3 F1; altered K6/E1/F3 P1 scope tracked in attached exact-list test receipts, not passed by provenance alone.

## Stop rule
The protected six-axis counter/tuck core, Top/Forge/Citadel, KCI/GY and Lattice locks remain. Compared six selected slots, four full alternative configurations and more than ten material challengers. Additional credible changes lose color certainty, artifact payoff, stack defense, or native parity-breaker density more than they gain. Best counterargument: the 9-mana Gargoyle is a unique cheatable lock and Petal fades late. We select early castability at fringe cEDH tables with that loss explicit, not as proven win-rate gain. Repo CI and case-transfer obligations must pass before presenting as approval-ready; until then this is evidence-only.

**Owner authority:** no canonical write, no approval inferred.
