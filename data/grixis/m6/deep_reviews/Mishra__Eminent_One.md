# M6 single-deck deep review #37 — Mishra, Eminent One

**Source authority and lock:** `corymstover/grixis-commander-encyclopediaGPT/main/state/current_deck_overrides.json#decks.Mishra__Eminent_One`: **APPROVED / LOCKED**, 2026-10-15, exact approved SHA-256 `ca94785fa43094a0053aac5c87e517c9cfaafb34c3baf9b3eccb067a167dd1a0`; approved TXT `refinement/decklists/Mishra_Eminent_One_Approved_2026-10-15.txt`, blob `8126661064866bef95ca521a6aee34e1bd8ba5b2`. Engineering registry logical `lh1:6ac1d9c40c3c9286ba5c684cbd943af7ecfa15dabab1a024f02b22951531e89d`, no discrepancy. October 19, 2026 authored analysis. **No canonical changes.**

## Source and test receipts

Read live integration tracker, `AGENTS.md`, `grixis/M6 Commander-First Single-Deck Review Standard.md`, engineering registry and M6/M7 subtracker. At entry: **36/62 complete**, first PENDING index36 `Mishra__Eminent_One`; index35 `Mishra__Artificer_Prodigy` is already complete, and must NOT be re-reviewed. Consulted canonical approved TXT, exact override and Oct15 decision/verification, `grixis/blueprints/mishra-eminent-one.md`, `grixis/interactions/mishra-eminent-one.md` (nine Oracle/rules interactions), `data/grixis/m6/review_packets/mishra-eminent-one.json` (178 ranked candidate test hypotheses), `data/grixis/mana_base/mishra-eminent-one.json` and `data/grixis/birthday_m5/evidence/mishra-eminent-one.json` (274 EDHREC associations). Oracle checkpoint engineering Scryfall Oct16, rulings Oct15, CR Sep25; canonical official Commander legality checkpoint Oct15. These are **dated evidence**, not a fresh 100-card Scryfall lookup on Oct19.

**Independent TXT parse:** 100 lines with 1x each, **100 total**, **100 distinct**, commander exactly once, **34 lands**, **99 noncommander**, no companion, no project exceptions. U/B/R color identity approved at dated legality/identity gate. Power **Bracket 4 — Optimized**, not cEDH. October15 verification says approval-ready; later explicit approval/override supersedes that intermediate status.

## Commander identity and natural ceiling

Mishra costs {2}{U}{B}{R}, 5-mana Human Artificer; **at beginning of combat on YOUR turn**, target **noncreature artifact you control**, make a token copy named **Mishra's Warform** that is a **4/4 Construct artifact creature** in addition to other types, gains haste until end of turn and is sacrificed at beginning of next end step. You need Mishra to survive until your beginning-of-combat trigger, a legal noncreature artifact target, and for expensive activations the right available mana; opponent may remove target in response and make trigger fizzle. Copy preserves printed mana cost/MV, ETB and activated abilities, but not tapped status/counters. Name override can interact with legend rule if two copied legendary artifacts produce same named legendary Warforms; original and Warform have different names.

The deck is a **Warform ETB/death/value conversion and artifact-copy engine**, not generic Breach/Oracle cEDH: Ichor Wellspring and Prized Statue turn each combat into cards/Treasures; Lich's Relic, Mightstone/Weakstone, Spine and Portal create removal; Coveted Jewel draws and generates mana; Mindslaver turns Warform into repeatable turn control; Gonti's Aether Heart + copied trigger/populate provides extra-turn lines; Worldwalker Helm + Urza + Thousand-Year Elixir produces recursive artifact tokens/blue mana. Arcum, Welder, Engineer, Transmute Artifact, Repurposing Bay, KCI and Smelting Vat **convert** expendable Warforms into enduring material. Nine of 19 documented blueprint Spellbook combinations include Mishra, all reported infinite-turn lines are commander-native, unlike many persist-only decks. This high commander dependency and five-mana combat bottleneck support **high Bracket4** rather than manufacturing a Bracket5 rating through unrelated Thoracle/Breach.

## Full 100-card role audit

Every actual approved slot examined by name in exact TXT order. Roles and caveats are qualitative; unsupported exact new-card text is explicitly not presented as fresh Oracle verification.

| # | Approved card | Role | Commander-first contribution and material limitation |
|---:|---|---|---|
| 1 | Mishra, Eminent One | Commander | Five-mana UBR Warform 4/4 artifact-copy engine, beginning of combat target NONCREATURE artifact you control; haste, next-end-step sacrifice; copy can fuel ETB, taps, sacrifice, not copy creatures. |
| 2 | Academy Ruins | Land/recursion | Colorless land; {1}{U}, tap returns target artifact from GY to library top, protects Mindslaver/artifact loop but slow. |
| 3 | Aetherflux Reservoir | Artifact win/payoff | Warform copy gains 4 life on ETB (assuming source Oracle), can be sacrificed for end-step, 50 life activation to deal 50; verify copied Reservoir activation/life source. |
| 4 | An Offer You Can't Refuse | Stack defense | U counter noncreature spell, opponent gets two Treasures; protects artifact engines but does not counter creature threats. |
| 5 | Ancient Tomb | Land/fast mana | Two colorless for 2 damage; T2 artifact acceleration, no UBR fixing. |
| 6 | Arcane Signet | Mana rock | Two-mana UBR fixing; a Warform copy becomes 4/4 mana creature, poor target versus ETB engine. |
| 7 | Arcum Dagsson | Artifact tutor/creature | Tap sac artifact creature to put noncreature artifact from library directly on battlefield; Warform creature is ideal expendable target. |
| 8 | Badlands | Land BR | Untapped Swamp Mountain typed fetchable dual, helps Mishra BR and tutor spells. |
| 9 | Blood Crypt | Land BR | Fetchable shock, pay 2 life untapped, otherwise tap. |
| 10 | Bloodstained Mire | Land fetch | Sac life fetch Swamp/Mountain duals and Lounge. |
| 11 | Brudiclad, Telchor Engineer | Token copy multiplier | At combat create Myr and make all tokens copies of chosen token, potentially multiple Warforms/Hearts; trigger order matters. |
| 12 | Chaos Warp | Interaction | 2R shuffles problematic permanent into library; opponent may receive replacement permanent. |
| 13 | Chrome Mox | Fast colored mana | Imprint nonartifact nonland card to fix, card disadvantage; losing this for slower rock costs early commander. |
| 14 | City of Brass | Land rainbow | All colors, 1 damage each tap; reliable UBR. |
| 15 | Command Tower | Land rainbow | UBR without life. |
| 16 | Coveted Jewel | Warform ETB draw and mana | Warform enters draw 3, can tap for three mana of any one color due haste; source Jewel combat damage control drawback matters if original copied artifact. |
| 17 | Cryogen Relic | Warform ETB utility | Copyable noncreature artifact with commander-linked value; exact contemporary Oracle effect must be confirmed for any asserted detailed payoff. |
| 18 | Cyclonic Rift | Interaction | Single bounce or 6U overload opponents' nonland permanents; seven mana defensive tempo. |
| 19 | Darksteel Citadel | Artifact land | Indestructible colorless artifact land, metalcraft and artifact-sac target; not a legal Mishra target? It is NONCREATURE artifact so yes, Warform copy retains land type but 4/4 creature, haste. |
| 20 | Deflecting Swat | Protection | Free only while controlling commander, changes spell/ability targets, not blanket counter. |
| 21 | Demonic Tutor | Tutor | 2 mana any card to hand, finds Heart/Helm/protection. |
| 22 | Determined Iteration | Populate Warform | Own combat populate after Mishra trigger, makes second Warform, haste; copy gets its own end-step sac trigger. |
| 23 | Emry, Lurker of the Loch | GY artifact replay | Mills 4 on ETB, taps to cast artifact from GY, costs reduced by artifacts; vulnerable to summoning sickness. |
| 24 | Enthusiastic Mechanaut | Artifact cost reducer | Artifact spells cost 1 less, flying haste; Top/Forge cast loop support. |
| 25 | Esoteric Duplicator | Token artifact recursion | When nontoken artifact? Copy after sacrifice; specifically Mishra Warform token sacrifice triggers if an artifact token went GY from battlefield, pay2 next end-step copy; source verified. |
| 26 | Etherium Sculptor | Artifact cost reducer | Artifact spells cost 1 less, Top/Forge combo enabler; fragile 1/2. |
| 27 | Fierce Guardianship | Protection | Free counter noncreature spell with commander, otherwise 2U. |
| 28 | Flooded Strand | Land fetch | Find Island-typed U dual or Lounge, life 1. |
| 29 | Force of Will | Protection | Pitch blue card and pay 1 life or 3UU, counter any spell; strong vs turbo. |
| 30 | Gamble | Tutor with risk | R any card to hand then random discard; artifact can be recovered by Emry/Welder but no guarantee. |
| 31 | Goblin Engineer | Artifact tutor and reanimate | ETB bin artifact, 1R tap sac artifact return target MV≤3 artifact GY to battlefield; Warform sac fodder. |
| 32 | Goblin Welder | Artifact swap recursion | R tap exchange artifact you control and artifact in GY; Warform fodder, requires both legal targets, tap sickness. |
| 33 | Gonti's Aether Heart | Infinite-turn copy target | Original plus Warform triggers 2 energy each per artifact ETB; 8 energy and exile copy to take extra turn; needs multiplier/extra artifact entry. |
| 34 | Great Furnace | Artifact land R | Colored red, artifact count/sac, vulnerable to artifact hate. |
| 35 | Ichor Wellspring | Warform ETB/death draw | Copy ETB draws1, sacrifice at end step draws1 again; token GY death trigger still works. |
| 36 | Imperial Seal | Tutor | B sorcery topdeck any card and 2 life, tempo loss. |
| 37 | Inventors' Fair | Land artifact tutor | Colorless, life if 3 artifacts, 4 tap sac search artifact, finds Heart/Helm. |
| 38 | Island | Basic U | One copy, protects from nonbasic hate; UU pips relevant. |
| 39 | Krark-Clan Ironworks | Free artifact sac/mana | Sac artifact for CC, supports Warform value and Trawler/ Retriever recursion; do not cut for generic Mind Stone solely based on simulator. |
| 40 | Lich's Relic | Warform removal ETB | Copy ETB may pay2 to destroy up to one target creature/planeswalker each opponent; exact trigger and legality source checked Oct15. |
| 41 | Lithoform Engine | Trigger/ability copier | Copies Mishra beginning-combat trigger for 2 tap, or abilities/spells with more mana; costs/target restrictions matter. |
| 42 | Lotus Petal | Zero-mana fixing | Sac for one mana any color, accelerates Mishra and artifact count; one shot. |
| 43 | Luxury Suite | Land BR | Untapped with 2+ opponents, 1v1 conditional. |
| 44 | Machine God's Effigy | Noncreature artifact copy bridge | Can enter copying creature but remains noncreature artifact with tap U; Mishra copies Effigy into creature Warform inheriting copied abilities. |
| 45 | Mana Confluence | Land rainbow | Pay1 life per colored mana, reliable three pips. |
| 46 | Mana Drain | Stack counter and ramp | UU counters spell and adds colorless next main phase equal MV; strong protection but demanding U. |
| 47 | Mana Vault | Fast artifact mana | One mana to three colorless, untap expensive; accelerates Mishra generic. |
| 48 | Master Transmuter | Artifact cheat engine | U tap return artifact you control to hand as cost, put artifact from hand to battlefield; requires actual card in hand and untap. |
| 49 | Mindslaver | Warform turn control | Warform can pay4 tap sacrifice to control target player's next turn; original remains, but costs 4 each combat. |
| 50 | Mishra's Workshop | Land artifact acceleration | Three colorless only for artifact spells; does NOT cast Mishra creature or pay abilities/Warform Mindslaver activation. |
| 51 | Misty Rainforest | Land fetch | Find Island typed dual or Lounge. |
| 52 | Morphic Pool | Land UB | Untapped with 2+ opponents, conditional. |
| 53 | Mountain | Basic R | One, resilient to nonbasic hate. |
| 54 | Mox Diamond | Fast mana | Discard land as additional cost to enter; 0 mana rainbow rock, land/card tradeoff. |
| 55 | Mox Opal | Fast mana conditional | Metalcraft 3 artifacts needed for colored mana, strong in artifact shell. |
| 56 | Myr Retriever | GY artifact recursion | When dies returns another artifact card from GY to hand, Trawler/KCI combo loop. |
| 57 | Mystic Forge | Top-of-library artifact cast | Look top, cast artifacts/colorless from top, 1 life tap exile top; Top+reducer draw loop. |
| 58 | Mystic Remora | Early card access | U cumulative upkeep, draws when opponents cast noncreature unless pay4; huge early defense/card throughput. |
| 59 | Nihil Spellbomb | Warform graveyard hate | Warform can tap? Spellbomb sac no tap, exile target player's GY, pay B on death draw, copy reuses source. |
| 60 | Otawara, Soaring City | Land U/channel interaction | Channel bounce artifact/creature/enchantment/planeswalker, protects or clears hate. |
| 61 | Padeem, Consul of Innovation | Artifact protection/draw | Artifacts you control hexproof, draw at upkeep if highest-MV artifact; doesn't stop sweepers. |
| 62 | Polluted Delta | Land fetch | Find Island/Swamp duals or Lounge, one life. |
| 63 | Portal to Phyrexia | Warform ETB edict | Each opponent sacrifices three creatures on ETB, Warform sacrificed at end step; original Portal's upkeep reanimate only if survives. |
| 64 | Prized Statue | Warform ETB/death treasure | Copy ETB Treasure and when dies Treasure, repeated mana; token sacrifice source. |
| 65 | Repurposing Bay | Warform artifact upgrade | Tap/sac artifact as sorcery to tutor artifact MV exactly one higher; Warform copies mana cost/MV of source, NOT 4/4 MV. |
| 66 | Rhystic Study | Draw tax | Draw on opponent spell unless pay1, ongoing advantage. |
| 67 | Scalding Tarn | Land fetch | Find Island/Mountain typed duals or Lounge. |
| 68 | Scrap Trawler | Artifact recursion engine | When artifact you control goes GY, return another lower-MV artifact from GY to hand; KCI engine, Warform has source MV. |
| 69 | Seat of the Synod | Artifact land U | Colored U, metalcraft, artifact synergy, vulnerable to Vandalblast. |
| 70 | Sensei's Divining Top | Topdeck setup/combo | 1 look top3, tap draw and place on top; with Mystic Forge+reducer loops through deck, may need payoff. |
| 71 | Simulacrum Synthesizer | Artifact cast payoff | Creates Construct tokens from artifact casts MV≥3 and grows Constructs, can snowball but not itself copied ETB. |
| 72 | Smelting Vat | Artifact sacrifice to discover? | Artifact-sac value engine, detailed Oracle interaction must be verified before claiming deterministic loop. |
| 73 | Sol Ring | Fast mana | 1 to 2 colorless, artifact count and Mishra generic. |
| 74 | Spine of Ish Sah | Warform ETB permanent removal | Copy ETB destroy target permanent; source Spine returns to hand on GY, token triggers but ceases existing. |
| 75 | Spire of Industry | Land rainbow conditional | Pay1 life for colored if artifact controlled, otherwise colorless. |
| 76 | Steam Vents | Land UR | Typed shock for U/R. |
| 77 | Strionic Resonator | Mishra trigger copier | 2 tap copy beginning-combat triggered ability, may choose new target, original Warform target must still be legal. |
| 78 | Swamp | Basic B | One, black tutor/Deluge mana. |
| 79 | Takenuma, Abandoned Mire | Land B/channel recursion | Channel mills three, return creature/planeswalker from GY to hand; artifact spells not returned. |
| 80 | Talisman of Creativity | UR rock | 2-mana U/R fixing at 1 damage, supports blue-heavy costs. |
| 81 | Talisman of Dominance | UB rock | 2-mana U/B fixing at 1 damage, supports UU. |
| 82 | Talisman of Indulgence | BR rock | 2-mana B/R fixing at 1 damage, commander pips. |
| 83 | The Mightstone and Weakstone | Warform ETB and mana | Copy ETB draw2 or -5/-5 target creature, Warform tap CC due haste, mana restricted to nonartifact? Powerstone mana cannot cast nonartifact spells. |
| 84 | The One Ring | Protection/draw | Cast ETB protection applies only if cast, Warform copy does not grant protection; tap draw burden, powerful original. |
| 85 | Thousand-Year Elixir | Creature activated ability speed | New artifact creatures can tap as though haste, untap target creature for1 tap; essential Worldwalker Helm copies. |
| 86 | Toxic Deluge | Board wipe | 2B pay X life, -X/-X all creatures, kills Warforms and commander, retains noncreature artifacts. |
| 87 | Training Center | Land UR | Untapped multiplayer 2+ opponents. |
| 88 | Transmute Artifact | Artifact tutor by sac | UU sorcery, sacrifice artifact on resolution, search artifact into play, pay MV difference if positive; Warform cost/MV same as original. |
| 89 | Underground Sea | Land UB | Typed original dual, UU and B. |
| 90 | Urza's Saga | Saga land tutor | Construct tokens and find 0/1 MV artifact, sacrifices itself at chapter III; colorless mana. |
| 91 | Urza, Lord High Artificer | Artifact mana/token engine | Tap artifact you control to add U, Worldwalker Helm + Elixir loop; Urza's construct token payoff. |
| 92 | Uthros Research Craft | Station artifact draw | Mishra power5 can station five counters via tap in main; at 3 charge counters draw whenever cast artifact spell. |
| 93 | Vampiric Tutor | Topdeck tutor | B instant pay2 life, any card to top, powerful find engine. |
| 94 | Vault of Whispers | Artifact land B | Black source, metalcraft and artifact sacrifice. |
| 95 | Verdant Catacombs | Land fetch | Find Swamp dual or Lounge. |
| 96 | Volcanic Island | Land UR | Fetchable untapped dual. |
| 97 | Watery Grave | Land UB | Fetchable shock, pay2 life untapped. |
| 98 | Whir of Invention | Instant artifact tutor | XUUU improvise, tutor artifact MV≤X directly battlefield, demanding UUU and artifacts. |
| 99 | Worldwalker Helm | Artifact-token copy engine | Original creates Map replacement with artifact tokens; Warform copy has tap ability 1U to copy artifact token, combos with Urza+Elixir. |
| 100 | Xander's Lounge | Land UBR | Fetchable tri-land ETB tapped, cycle later; only unconditional tapped source. |

## Mana, curve, interaction and identity protection

**Source model** (not empirical cast probability): 34 lands, six fetchlands, 13 fast-mana flags, 16 repeatable nonland mana sources, one one-shot mana source, 4 utility lands, 1 unconditional tapped land, 6 conditional tapped flags. Potential colored land sources **U18/B17/R15**; land+repeatable rocks **U27/B24/R22**, which are not independent guaranteed mana. Colored spell pip demand **U29 (69.05%) / R8 (19.05%) / B5 (11.90%)**; five double-U spells, none double B/R. Turn3 strict three land drop proxy **73.6993%**, all UBR potential land presence **68.961%**; turn4 strict four land drop proxy **56.2728%**, not turn4 Mishra cast probability. Actual commander requires FIVE mana including UBR; Chrome Mox/Mox Diamond/Opal, Vault, Tomb and Sol Ring can accelerate but cost cards/metalcraft/untap/life. `Mishra's Workshop` adds 3 **only for artifact spells**; cannot cast Mishra or pay Worldwalker/Mindslaver activations. `Urza's Saga` and artifact lands add critical artifact density but increase vulnerability to mass artifact destruction. Xander's Lounge tapped and fetchable; `Inventors' Fair`, `Academy Ruins`, `Urza's Saga`, `Mishra's Workshop` are valuable utility/colorless slots but can strand UU/UBR. The deck is blue-intensive **despite Grixis commander**; replacing Flooded Strand with Darkwater Catacombs or Shadowblood Ridge may hurt typed-dual selection.

**Interaction and defense:** Force of Will, Mana Drain, Fierce Guardianship, An Offer, Deflecting Swat, Chaos Warp, Cyclonic Rift, Toxic Deluge, Nihil Spellbomb, Otawara and Lich's Relic Warforms. `Padeem` protects artifacts with hexproof but doesn't protect Mishra creature from removal or prevent board wipes. `Mystic Remora` and `Rhystic Study` fuel interaction while waiting to untap with Mishra; `The One Ring` can refill hand but a Warform copy did NOT enter from being cast and gives no protection. `Arcum` and `Whir` access artifact threats, `Gamble` and `Imperial Seal` cost tempo/card quality. Artifact-hate `Vandalblast` overload, `Null Rod`, `Stony Silence`, `Collector Ouphe` and exile effects attack this deck on different axes; bounce/Chaos Warp/stack defense are necessary, and KCI/Urza mana abilities can bypass some activation restrictions only if their precise wording/rules allow.

**Role balance / cut pressure:** `Cryogen Relic`, `Lich's Relic`, `Coveted Jewel`, `Portal to Phyrexia`, `Spine of Ish Sah`, `Mindslaver` are high-value copy targets but multiple expensive artifacts can clog hand without Welder/Transmuter/Workshop. `Smelting Vat` and `Repurposing Bay` are activation/cost and mana-value gated; `Simulacrum Synthesizer` demands artifact spell casting (Warform **created**, not cast), so its synergy is with the artifact spell shell, not direct Warform triggers. `Aetherflux Reservoir` Warform is a 4/4 that copies spellcast/life-gain text, but Warform creation is NOT casting a spell and should not be credited as spell storm. `Brudiclad` costs 6 and needs tokens, but can convert multiple tokens to Warforms at combat. `Esoteric Duplicator` costs resources and deferred next-end-step trigger. `Thousand-Year Elixir` is poor alone but indispensable for specific Helm copies without haste. `Uthros Research Craft` can be stationed by Mishra in precombat main phase and still trigger Mishra's combat ability, but tapping Mishra can expose the commander to removal and consume potential artifact tap effects.

