# Deck #56 — The Madcap Jester — M7 Rev1 owner review

2026-10-27 · Cycle `global-restart-2026-10-13` · **REVIEW ONLY — not Cory-approved or canonically applied.**

## Source and exact 100

- Authoritative current approved/locked `corymstover/grixis-commander-encyclopediaGPT/main`: `refinement/decklists/The_Madcap_Jester_Approved_2026-10-15.txt`, blob `cd3a6ddb12cbac7034d0994b951137390eb804da`. Confirmed live main `89ef6f71eddf6e18b49b76d0bfb6f82e7f721bc5`; raw SHA-256 `caeffc07503581cd3ecba798ebc4e09d48f07310f1f117ce3b90a04b5ca6bfa7`.
- Engineering copy of exactly those bytes: `data/grixis/m7/madcap_jester_rev1/The_Madcap_Jester_Oct15_baseline.txt`.
- Proposed final: `data/grixis/m7/candidate_lists/The_Madcap_Jester_M7_Rev1.txt`; **100 cards, 100 distinct names, 34 lands, seven genuine swaps**; full LF-terminated UTF-8 raw SHA-256 **`643eb1cc4827c1dd95485e9922506b514746e6bbc5b4b8a4cfff0f44b1007e43`**.
- Historical canonical approved list, tracker, approval registry, exceptions, earlier locks, original research, M6 receipts, and Pass C seal have NOT been changed.
- Power Bracket **5 — cEDH-capable** (identity-driven exile theft plus compact Oracle/Pact/Breach backstop; **not** an empirical multiplayer win rate). Archidekt tags: **Exile Theft / Library Control / Grixis Combo**.

## Commander-first thesis

The Madcap Jester {1}{U}{B}{R} attacks to exile the top card from *each* opposing library. More importantly, an ability or spell we control that actually exiles an opposing library card grants normal-timing play permission for that card through **the end of our next turn**, with mana of any type spendable on spell color requirements. This is **not free casting**, does not grant additional land plays, and does not work retroactively after Jester arrives. Greaves and cheap access spells remain essential. Dragon's Smile can waive **one spell's mana cost on our turn**, but does not waive additional costs or make sorcery timing disappear. Compact Thassa's Oracle/Consultation/Tainted Pact and Underworld Breach/LED/Brain Freeze are secondary finishers that do not require Jester; they are not his unique identity.

The Oct15 list invested six/five/four mana in several effects that must survive an upkeep or opponent landfall before exiling cards. The new physical 100 moves slots toward earlier controlled library-exile, legal access windows, and protection. It deliberately retains one iconic slow high ceiling (Dragon's Smile), the ability to **search and take exact cards** (Jester's Cap, Extract, Sadistic Sacrament, Praetor's Grasp), and Jester's Scepter face-down five-card burst. No cheap generic card wins a slot by popularity alone.

## Seven selected swaps and losses

| Add | Cut | Commander benefit and concrete downside |
|---|---|---|
| **Opposition Agent** | Sire of Stagnation | Flash intercepts opposing searches at 3 mana instead of waiting for 6-mana Sire and opposing landfall. Agent can steal searched cards even while Jester is absent. **Loss:** Sire exiles two top library cards and draws two on each opposing land ETB. Agent search exile is *not* counted as a proven Jester trigger. |
| **Black Widow, Super Spy** | Nalfeshnee | {1}{B} menace on-hit exile until a nonland card; with Jester live the intervening lands also receive access. **Loss:** damage-dependent 2-mana attacker and setup; Nalfeshnee at six can copy every spell cast from exile, including temporary permanent tokens. |
| **Grimoire Thief** | Plargg and Nassari | {U}{U} taps to exile top three of an opponent on attack, even if blocked, before damage; Jester can access face-down cards while controller may look. **Loss:** requires Jester present *when* tapping exile occurs, needs two blue early, and can die before follow-up attacks; Plargg independently casts up to two spells free after a five-mana upkeep. |
| **Borne Upon a Wind** | Gonti, Night Minister | {1}{U} draws one and grants this-turn flash to otherwise stranded stolen sorceries and combo spells. **Loss:** one turn only; Gonti at four produces Treasure on stolen casts and combat-theft, though can also grant other attackers access. |
| **Hexing Squelcher** | Wild-Magic Sorcerer | Uncounterable {1}{R} creature makes **all our spells** uncounterable, including cast Jester and stolen spells; other creatures gain pay-two-life ward. **Loss:** removal still works and triggered abilities can still be countered; Wild-Magic Sorcerer at four grants cascade to the first exile-cast spell each turn. |
| **Gloomlake Verge** | Drowned Catacomb | Always supplies untapped {U}; supplies {B} with Island/Swamp, unlike Catacomb which may **enter tapped** without one. **Loss:** Verge cannot supply early black with no Island/Swamp, whereas untapped Catacomb always supplies U/B. No red is gained. |
| **Flusterstorm** | Bitter Ordeal | {U} instant/sorcery stack protection and storm copies work sooner and more frequently in cEDH, while Cap/Sacrament/Extract/Praetor's Grasp retain exact opposing-library theft. **Loss:** loses {2}{B} chosen-card library exile and powerful gravestorm copies after sacrificed/destroyed permanents. |

**Owner-direction flag:** every cut was part of the Oct15 approved/locked list. The earlier authored 99-slot decisions intentionally retained all seven. This Rev1 **proposes** to override those historical KEEPs prospectively, not silently rewrite their rationale. Only a separate explicit approval of this exact SHA can authorize that supersession.

## Open-ended alternatives (not swap-count anchoring)

After composing seven selected upgrades, the 99-slot ledger was revisited. **Six additional retained slots** were challenged with real alternatives, beyond the selected seven cuts. Two *complete* larger 100-card packages were staged:

1. **Eight swaps** (`The_Madcap_Jester_M7_Rev1_alt8.txt`, SHA `65c548d31e38e11ff05d66404720bb322275d751b953f3a6eee357a254a93c34`): add The Stone Brain over Jester's Cap. It reduces upfront cast+activation cost **six → four mana** but names only one target card, searches broader zones, must activate as a sorcery, and cannot provide Cap's **three independently selected opponent library cards** at instant speed. **Retain Cap** for commander-first precise multi-card theft.
2. **Nine swaps** (`The_Madcap_Jester_M7_Rev1_alt9.txt`, SHA `fd4ea044323ce9cffd7952ca6e97fc052a7ea7c92f3438fd331957e366d7b83d`): the above Stone Brain plus Arena of Glory over Sulfurous Springs. Arena may confer haste via spent exerted RR but requires an initial R activation payment, is tapped without Mountain, produces only R rather than BR and misses its next untap; loss of guaranteed early black makes BBB cards and the UBR commander less reliable. **Retain Springs**.

Further direct incumbent challenges: Roaming Throne vs Circu doubles Jester attack bursts but pays four mana and needs another attack; Siphon Insight vs Inside Information swaps scalable X exile/life-casting for one target top-two selection; Cavern of Souls vs Shivan Reef makes only chosen-type creatures uncounterable but compromises noncreature U/R color; Final Fortune vs Rite of Flame risks losing the game and abandons early ritual speed. Samut's split second, Valley Floodcaller's persistent flash, Mindbreak Trap, Gríma, Raven Guild Master, Memory Vessel and prior M5 Grinding Station/Hullbreaker Horror packages were adjudicated. The gated JSON carries **23 distinct material judgments**. The stopping rule is opportunity cost and retained identity, **never that seven is enough by number**.

## EDHREC discovery and baseline context

- [General Jester EDHREC](https://edhrec.com/commanders/the-madcap-jester) checked Oct27, any bracket, 1,659 decks: Top Tasha's Hideous Laughter 91%, Extract 79%, Jester's Cap 76%; High Lift Grimoire Thief **12% inclusion / 62 lift**, Raven Guild Master **32% / 61 lift**; Black Widow 37% inclusion / 38 lift in creature listings.
- [Jester cEDH subpage](https://edhrec.com/commanders/the-madcap-jester/cedh) checked Oct27, **only 21 user-designated decks**, so fragile sampling: Flusterstorm 95%, Hexing Squelcher 95%, Borne Upon a Wind 86%, Opposition Agent 71%, Black Widow 24% inclusion. Metrics are *discovery only*, not a win-rate proof. [Theft](https://edhrec.com/commanders/the-madcap-jester/theft) and [Exile](https://edhrec.com/commanders/the-madcap-jester/exile) themed pages also inspected.
- 2026-10-20 comprehensive original authored M6 deep review: exactly **99/99 library physical positions audited**, 34 lands, 38 M5 candidate pairs and 64 previously authored finite rules examples. This revision exports an independent per-slot KEEP/CUT ledger: **92 keep, 7 cut**.
- Oct21 owner-equivalent Pass C: `NEEDS TESTING` (+Opposition Agent/−Sire proposed) and uncertainty about Dauthi-modified Brain Freeze. It did not furnish a measured game sample or technically independent reviewer. The Oct17 M6 I/J receipt is **inputs attested; downstream Phase B incomplete** and remains so.

## Live Oracle and rules/evidence scope

- Public Scryfall Oracle Cards **2026-10-27 21:02 UTC** compressed JSONL loaded by public GET, then checked **locally** for the complete candidate plus two extra alternative-only names: **102/102 resolved, all have Oracle IDs and U/B/R-compatible color identities; all 98 ordinary selected deck cards officially Commander `legal`.** Exactly two selected project-authorized cards are `not_legal`: **The Madcap Jester** and **Dragon's Smile**. Wizards says new-to-Magic MBC cards become Commander-legal **November 13, 2026**, so project exception is not official legality. No unauthorized Jabs card added. See [Wizards product announcement](https://magic.wizards.com/en/news/feature/whats-inside-mystery-booster-commander-edition) and [release notes](https://magic.wizards.com/en/news/feature/mystery-booster-commander-edition-release-notes).
- Source-bound `verify.py`: **24 executed bounded C/K/E/W/F unit assertions**, exact baseline and proposed SHA/count/delta, actual Oracle text snippets, 34 lands, legal/project exception separation. Cases cover Jester attack vs damage/removal, two-turn permission and ordinary mana/timing, Grimoire tap/face-down access, Black Widow exile until nonland, Borne flash, Squelcher's scope, Flusterstorm cast count, opposition search, stone-brain timing and Arena exert, Tainted Pact unique names, Oracle/Consult/Breach payable assumptions and defensive counterplay.
- **Dauthi causation caveat:** Dauthi's replacement sends opponent-milled cards to exile with void counters (Comprehensive Rules **614.6**: modified event may trigger effects), but Wizards has **no Madcap-specific ruling** saying whether the modified event is attributed to the controller of Brain Freeze for the wording “causes ... exiled.” This packet does *not* assume or claim that Jester gains cards from Dauthi-replaced milling and does not rely on such a combo for its seven swaps. A conservative test checks actual zone replacement, not an asserted Jester access trigger. That caveat remains an M6 interaction certification limitation, not a fabricated synergy.
- **Scope limits:** These 24 small case assertions do not constitute a complete Magic game engine, paid multiplayer testing, a win-rate model, official legal status for the two exceptions, the unrun M6 I/J Phase B, a qualified independent third-model review, or M6.10/M7/M8 project milestone certification.

## Local/CI verification commands

```bash
python3 data/grixis/m7/madcap_jester_rev1/verify.py
python3 data/grixis/m7/madcap_jester_rev1/verify.py --oracle-file /path/to/oracle-cards-20261027210243.jsonl.gz
python3 scripts/grixis_m7_decision_gate.py --check --file data/grixis/m7/decision_reviews/The_Madcap_Jester_rev1.json
python3 scripts/grixis_m7_decision_gate.py --check
```

The GitHub Actions workflow downloads the above **public bulk file** by GET, runs the complete 102-card current Oracle lookup **locally**, the 24 finite cases, the M7 structural gate and repository-wide structural regression. Exact-head GitHub Actions results are required before any approval-ready owner presentation.

## Authority

**Not approved, not locked, do not merge canonical or change its approved hash.** This engineering PR prepares an exact review source only. Cory can approve the exact full raw SHA later with a single **Approve**, at which point engineering merge and a separately guarded canonical PR/postmerge rehash are authorized under the one-command workflow. Earlier owner approval of the Oct15 baseline remains intact meanwhile.
