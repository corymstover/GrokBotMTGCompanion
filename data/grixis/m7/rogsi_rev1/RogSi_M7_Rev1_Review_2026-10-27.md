# Deck #47 — RogSi M7 Rev1 owner-review packet (2026-10-27)

**Status: REVIEW READY — NOT OWNER APPROVED — NOT CANONICAL — NOT LOCKED AS M7 REV1.** The October 15 canonical RogSi list remains approved/locked until Cory explicitly approves the exact 100-card Rev1 candidate.

- Commanders: Rograkh, Son of Rohgahh / Silas Renn, Seeker Adept
- Canonical October 15 source: `corymstover/grixis-commander-encyclopediaGPT:refinement/decklists/RogSi_Approved_2026-10-15.txt`
- Verified original raw SHA-256: `06c9e22b5afc46bd58bbbfdef5c42a796d2a986a2972456107c29aee1b5f905c`
- **Rev1 exact raw SHA-256: `97f3c0ca70303b44cd887938c320b75de01e991feec7d71d4c18811aeaa88225`**
- Candidate: `data/grixis/m7/rogsi_rev1/RogSi_M7_Rev1_Candidate_2026-10-27.txt`
- Physical cards: **100**, including **two Partner commanders**; 98 noncommander cards
- Distinct names: **100**, no repeats
- Physical lands: **24**
- Partner combined color identity: **U/B/R**
- Commander legality: **PASS**, 100/100 full live Scryfall collection verified 2026-10-27
- Authorized exceptions: **none**
- Power bracket: **5 — cEDH**
- Suggested tags: **Turbo Naus / Underworld Breach / Fast Mana**

## Open-ended strategic conclusion

Rograkh's zero-mana body remains a genuine resource engine (Mox Amber; Springleaf Drum; Paradise Mantle; Culling the Weak; Infernal Plunge; Diabolic Intent; commander-enabled Fierce Guardianship / Deflecting Swat / Deadly Rollick / Flare of Duplication). Silas supplies the U/B identity and actual artifact-recursion fallback. Preserve both deterministic wins: Thassa's Oracle plus Consultation/Pact; and Underworld Breach plus LED and Brain Freeze, with Grinding Station alternate material.

Compared with the October 15 candidate, this independent pass gives more weight to *winning on our own early turn through interaction* and *converting Necro/Ad Nauseam reloads*, with less reliance on a conditional delirium tutor, generic colorless burst, and symmetrical Windfall. The review does not require a fixed swap count.

## Six exact one-for-one swaps

| OUT | IN | Why the improvement is material | Real cost / tradeoff |
|---|---|---|---|
| Force of Negation | **Misdirection** | May pitch on **our own combo turn** to redirect a one-target answer/counter without keeping 1UU available; key turbo protection | Misdirection does not counter arbitrary spells or work against every multi-target/untargeted effect; Force better hard counters on opponents' turns |
| Into the Flood Maw | **Snapback** | Enables free creature bounce while tapped out, fighting Drannith Magistrate and other creature hatebears without passing a mana window | Exiles another blue card; narrower than one-mana bounce of any opposing nonland permanent |
| Windfall | **Chromatic Star** | Early 1-mana artifact density; Grinding Station can sacrifice it for both mill and a draw trigger; can turn mana into color and support Breach escape | Loses a wheel/reload and creates no inherent mana acceleration |
| Grim Monolith | **Last Chance** | Adds a third two-mana extra-turn way to convert end-step Necropotence/Necrodominance reloads or force a fresh win window | Loses 2-to-3 generic fast-mana burst; extra-turn delayed-loss trigger is real |
| Demonic Counsel | **Flashback** | `{R}` recasts a useful graveyard instant/sorcery by giving it flashback at its normal mana cost; functions on active storm/rebuild turns before delirium | Trades a late unrestricted tutor for narrower one-spell graveyard recursion; Flashback itself is not a zero-cost cast |
| Undercity Sewers | **Starting Town** | On turns 1–3 enters untapped, taps for U/B/R with 1 life, improving early colored access from a 24-land shell | After turn 3 enters tapped; unlike Sewers, not fetchable as Island/Swamp and no surveil |

## Serious rejected candidates

- **Brainstorm:** 10 fetchlands make this more attractive, but cutting Ragavan weakens a first-turn Treasure generator without sufficient positive proof; keep the actual mana engine.
- **Commandeer:** strong interaction, but two blue cards exiled in addition to itself is a higher cost than Misdirection for this turbo exchange.
- **Snap:** mana-positive on dual lands in some spots, but Snapback's pitch mode is more often live with all mana committed to the win.
- **Copy Artifact / keys / Bolas's Citadel / Mishra's Workshop artifact conversion:** a valid RogSi branch with observed top results, but would change the established classic Ad Nauseam/Breach turbo posture and impose expensive new slots.
- **Storm-Kiln Artist:** Treasure payoff and spell-chain ceiling are appealing; four mana and Ad Nauseam life cost are poor in the current 24-land classic turbo shell.
- **Peer into the Abyss:** enormous payoff but 7 mana, heavy black demand, and a painful Ad Nauseam reveal.
- **Exotic Orchard, Gemstone Mine, extra two-mana rocks:** mana alternatives reviewed; Starting Town versus tapped Sewers is the clearest early-turn improvement while retaining 24 lands.
- **Orcish Bowmasters / Opposition Agent:** generic interaction does not displace the commander-enabled fast/proactive core.
- **Last Chance for Warrior's Oath as a name-only swap:** rejected; both may be worthwhile together but a straight swap is no gain.

## Critical focused rules checks

- **Partner legality:** Rograkh and Silas each have Partner, and their combined color identity is U/B/R. Their two commander slots count toward the 100.
- **Rograkh / Vexing Bauble:** a first zero-mana Rograkh cast is vulnerable to our own Bauble if no mana was spent. Bauble may be sacrificed for a card; a later command-tax recast spends mana. Free counters/pitch spells are also affected unless protected by Hexing Squelcher.
- **Misdirection:** targets a *spell with a single target* and changes that target to something legal. It is not a universal counterspell.
- **Snapback:** pitches one other blue card to bounce a creature; no generic permanent bounce. The alternative cost is not a generic free counter to Bauble.
- **Chromatic Star / Grinding Station:** sacrifice to Station sends the Star from battlefield to graveyard, triggering Star's draw in addition to Station mill; Breach escape still requires exiling three *other* graveyard cards plus paying mana.
- **Last Chance:** the lose-the-game trigger occurs at the beginning of the *extra turn's* end step; winning before that trigger resolves is essential.
- **Flashback:** the selected graveyard instant/sorcery gains flashback equal to its mana cost until end of turn; it follows original timing permissions and cannot bypass additional costs or cast from exile. It is not Underworld Breach and does not itself confer repeated escape.
- **Starting Town:** enters untapped only on the owner's first, second or third turn; costs 1 life to produce any color. It is not fetchable with Polluted Delta or other fetchlands.
- **Samut:** split second does not prevent triggered Vexing Bauble abilities. The regular Breach/LED/Brain Freeze and Thassa's Oracle plus Pact/Consultation lines remain retained.

## Verification and evidentiary bounds

- Re-fetched October 15 canonical text. Raw bytes SHA match its current registered approval digest.
- Independent diff computation: exactly **six removed / six added** physical cards, no unauthorized change in commanders.
- Exact-file digest generated from newline-terminated raw UTF-8.
- All **100 current candidate names** queried live from Scryfall card collection on 2026-10-27 (split-faced Birgi resolved via front-face name). All resolved, each Commander `legal`, each color identity within U/B/R. 24 land cards; 100 unique names.
- Current official Commander ban list was cross-checked, and no project exception applies.
- Current EDHREC RogSi cEDH top/high-lift data reviewed as candidate evidence; recent actual event placements and their decklists compared for the October 4 winner and September 26 winner and October 17 runner-up. Frequency is not assumed to prove win rate.
- No fresh randomized multiplayer win-rate simulation, independent third-model certification, or aggregate M6/M7/M8 acceptance claimed.
- This packet is **approval-ready research evidence**, not a canonical approval record. Preserve all October 15 files and previous 46 M7 locks.

## Research sources

- [Official Commander banned/restricted list](https://magic.wizards.com/en/banned-restricted-list)
- [Official Secrets of Strixhaven release notes — Flashback card and keyword](https://magic.wizards.com/en/news/feature/secrets-of-strixhaven-release-notes)
- [EDHREC RogSi cEDH Top and High Lift](https://edhrec.com/commanders/rograkh-son-of-rohgahh-silas-renn-seeker-adept/cedh)
- [Top16 RogSi tournament records](https://edhtop16.com/commander/Rograkh,%20Son%20of%20Rohgahh%20/%20Silas%20Renn,%20Seeker%20Adept)
- [September 26 first-place list](https://edhtop16.com/tournament/css-20000-cedh-invitational-qualifier-5/decklist/RlX8UKFqR1euXnRbyzMymHKqsef1)
- [October 4 first-place list](https://edhtop16.com/tournament/mortal-kraumbat-3/decklist/crjjFgcVC0hi4otJ6ls9Wf9EdGl1)

**Next decision:** Cory may reply once with **Approve** to authorize only this exact hash and candidate, followed by canonical versioned locking and post-merge verification. No second approval should be requested.
