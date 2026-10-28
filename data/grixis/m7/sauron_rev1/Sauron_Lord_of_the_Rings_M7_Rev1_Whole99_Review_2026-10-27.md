# Deck #49 — Sauron, Lord of the Rings — M7 Rev1 owner-review candidate

**NOT OWNER-APPROVED. NOT CANONICAL. ORIGINAL OCTOBER 15 APPROVAL REMAINS LOCKED.**

- Global restart cycle: `global-restart-2026-10-13`; engineering: `corymstover/GrokBotMTGCompanion`; canonical authority: `corymstover/grixis-commander-encyclopediaGPT/main`.
- Oct. 15 approved full 100 source raw SHA-256: `72a814e6ae1153507c9c1469a7792043b2e5c055d9e5fcd9f6cfcf7781e287b0`.
- Oct. 27 proposed full 100 candidate raw SHA-256: `c427805f78f7aca7384db56022868a2e7cb7d01eeeabbb280a18e77e538a8159`.
- Proposed natural ceiling: **Bracket 4 — Optimized**. Tags: **Reanimator / Graveyard Setup / Amass Orcs**.
- Exactly **8** one-for-one physical changes after re-examining the complete 99 rather than treating eight as a quota.

## Commander-first judgment

Sauron is not a cheap Grixis combo engine. His eight-mana **cast** ability first amasses Orcs 5, then mills five, then returns a creature card from your graveyard. The bottleneck is putting high-quality creatures in that graveyard, assembling the mana to cast Sauron, and making the immediate reanimation matter. The revised deck improves these three functions and its land flexibility without breaking the Orc/Nazgûl/Ring identity.

| Cut | Add | Why, and what is lost |
|---|---|---|
| Ancient Brass Dragon | **Hoarding Broodlord** | Broodlord creates value on reanimation **immediately** by exiling a tutored card playable later, and spells cast from exile have convoke. Sauron's fresh Orc Army can help convoke one of them even on the turn it enters. Lost the hasty-with-Anger 7/6 flying damage-triggered Dragon reanimation lottery. |
| Feed the Swarm | **Chaos Warp** | Instant-speed answer to any target permanent, including artifacts and planeswalkers, useful for protecting the expensive Sauron turn. Lost an unconditional creature/enchantment kill in favor of Warp's possible replacement permanent. |
| Forbidden Alchemy | **Intuition** | Search three relevant distinct reanimation targets/recursion cards; an opponent chooses one to hand, **two go into the graveyard**, directly staging Sauron's triggered return. Lost flashback and a four-card dig from the library; an adversary chooses the card placed in hand. |
| Jin-Gitaxias, Core Augur | **Doom Whisperer** | Five-mana castable flying/trampling 6/6 with repeatedly activated 2-life surveil 2; stocks the graveyard at instant speed before Sauron or reanimation spells. Lost the devastating but slow/disruptable opposing maximum-hand-size lock and draw-seven upkeep trigger. |
| Relic of Sauron | **Basalt Monolith** | Three-mana rock taps for three colorless rather than a four-mana rock tapping for two colored; stronger leap into Sauron's five generic mana component. Lost a flavorful Ring artifact, colored fixing, and the late-game looting mode. **Basalt does not supply U, B, or R**, so the colored base must still function. |
| Summons of Saruman | **Sink into Stupor // Soporific Springs** | Retain interaction as a bounce spell for a stack spell or opposing nonland permanent, or play the back face as a blue-producing land, raising from 32 to **34 land-capable cards** without cutting physical lands. Lost a highly thematic X-cost mass amass/self-mill/free spell effect, which was expensive and timing constrained. |
| Thrill of Possibility | **Unmarked Grave** | Two mana explicitly places a nonlegendary creature/reanimation target into the graveyard; can stock Archon, Metamorphosis Fanatic, Hoarding Broodlord or Anger/Wonder. Lost instant-speed discard-two-card draw. Cannot fetch **legendary** Sauron/Jin/etc. |
| Windfall | **Valakut Awakening // Valakut Stoneforge** | Hand filtering without refilling opposing hands or graveyards, and a second spell/land MDFC to improve opening hands for an eight-mana commander. Lost the possibility of a huge seven-plus-card equalized wheel. |

## Whole-99 challenge — preserved roles and judged exclusions

Every one of the 99 noncommander physical cards in the October 15 approved list was evaluated by role and replacement opportunity. The 8 rows above are the only proposed cuts. The remaining 91 physical cards are preserved by category:

- **Commander speed/mana:** 32 front-face lands including Ancient Tomb, Command Beacon, Phyrexian Tower, typed duals and fetches; Sol Ring, Mana Vault, Grim Monolith, Arcane Signet, Fellwar Stone, three Talismans, Dark Ritual and Jeska's Will. The extra MDFCs mitigate draw inconsistency but are land-capable, **not extra printed lands**.
- **Graveyard setup/reanimation:** Entomb, Buried Alive, Faithless Looting, Frantic Search, Ripples of Undeath, Anger/Wonder, Reanimate, Animate Dead, Dance of the Dead, Necromancy, Persist, Victimize, Living Death, Grave Researcher // Reanimate and Sneak Attack. Sauron's own cast trigger is the flagship enabler, not an incidental effect.
- **Premium return targets:** Archon of Cruelty, Metamorphosis Fanatic, Sheoldred, Whispering One, Valgavoth, Terror Eater, Cavern-Hoard Dragon and the Middle-earth ETB threat Voracious Fell Beast. Moria Scavenger retains its Army/Orc-enabled recovery role; Sauron, the Dark Lord remains as a thematic independent threat.
- **Ring/Army/Middle-earth:** Four Nazgûl, Call of the Ring, The One Ring, Barad-dûr, Mount Doom, The Black Gate, The Balrog of Moria, The Mouth of Sauron, Moria Scavenger, Saruman, the White Hand, Too Greedily, Too Deep and Troll of Khazad-dûm remain. Nazgûl may legally appear up to nine copies by its own construction text; four are intentional.
- **Protection, draw and removal:** Force of Will, Mana Drain, Swan Song, Deflecting Swat, Deadly Rollick, Lightning Greaves, Cyclonic Rift, Toxic Deluge, Blasphemous Act, Orcish Bowmasters, Rhystic Study, Mystic Remora and The One Ring retained. No banned Mana Crypt, Jeweled Lotus, Dockside Extortionist or broad generic Oracle/Consultation/Breach conversion.

Further challenged but declined: Chrome Mox (card disadvantage at 32 lands; many creature targets cannot imprint if colorless), Mox Diamond (low land count), City of Traitors (land sacrifice and colored three-pip Sauron constraint), Exhume (hands opponents immediate free returns), Shallow Grave (top-creature restriction and exile), Razaketh (threatens unrelated tutor-combo conversion), Avacyn, Angel of Horror (no ETB), Rune-Scarred Demon (additional generic ETB tutor overlaps Hoarding Broodlord), Chainer, Nightmare Adept (slower recursion engine), Doom Blade-type removal (less flexible than Warp), and creature-heavy alterations that dilute Sauron's cast/reanimation structure. EDHREC inclusion and high lift used only for challenger discovery.

## Rules and failure-mode cases to verify

1. **Cast trigger sequencing:** Sauron's cast trigger exists independently of the spell even if Sauron is countered. It makes/expands the Orc Army, then mills five, *then* can target a creature card now in graveyard. Reanimated Metamorphosis Fanatic can add a second ETB return.
2. **Intuition:** exactly three cards must be selected, an opponent is targeted and decides one to hand; remaining two in graveyard. Against graveyard hate or replacement effects, the hoped-for graveyard setup can fail.
3. **Hoarding Broodlord:** the card is exiled **face down** on ETB and playable for as long as it remains exiled; its convoke-granting ability applies to spells cast from exile. A newly created Sauron Army can be tapped to convoke despite summoning sickness, but each tapped creature pays at most one mana and colors must be respected.
4. **Unmarked Grave:** one **nonlegendary card** into the graveyard; this includes nonlegendary creature targets and Anger/Wonder but not legendary Valgavoth or Sheoldred.
5. **Doom Whisperer:** pay 2 life per surveil 2 activation; the ability requires no tapping but cannot be used without paying the life. Does not itself reanimate a creature.
6. **Basalt Monolith:** `{T}: Add {C}{C}{C}`, `{3}: Untap` (no free infinite mana); Sauron's printed color demands `{U}{B}{R}`.
7. **MDFCs:** Sink into Stupor and Valakut Awakening may each be played as lands on their back faces. Their spell-fronts are not lands in library/graveyard. Sink land enters untapped only if life is paid; Valakut back face enters tapped.
8. **Anger/Wonder:** require a Mountain/Island land type controlled, not merely a red/blue-producing land. Core typed duals and basic land copies remain.
9. **Nazgûl:** four copies legal due to its explicit up-to-nine rule. Basic Swamp x2 is the other permitted repeat.

## Gate and approval boundary

- The exact-source checker verifies both full raw hashes, two sets of 100 physical, 96 distinct names, the only legal repeats, 32 actual lands + two MDFC land-capable slots, preserved critical core, and exactly eight one-for-one swaps.
- An independent CI step fetches **current** Scryfall collection data for all 96 named cards, checks Oracle resolution, official Commander legality and subset of U/B/R identity. Staging this file **does not by itself constitute CI success**.
- This is finite source-bound judgment, not randomized multiplayer or an aggregate M6/M7/M8 certification. The proposed list cannot change the October 15 canonical lock without Cory's explicit approval of the complete SHA-bound list.

Primary card/legality research: [Scryfall Sauron](https://scryfall.com/card/ltc/478/sauron-lord-of-the-rings), [Intuition](https://scryfall.com/card/tmp/70/intuition), [Unmarked Grave](https://scryfall.com/card/mh2/106/unmarked-grave), [Hoarding Broodlord](https://scryfall.com/card/mom/110/hoarding-broodlord), [Doom Whisperer](https://scryfall.com/card/grn/69/doom-whisperer), [Basalt Monolith](https://scryfall.com/search?q=%21%22Basalt+Monolith%22), [Sink into Stupor](https://scryfall.com/card/mh3/241/sink-into-stupor-soporific-springs), [Valakut Awakening](https://scryfall.com/card/znr/174/valakut-awakening-valakut-stoneforge), [official banned list](https://magic.wizards.com/en/banned-restricted-list). Candidate discovery: [Sauron EDHREC](https://edhrec.com/commanders/sauron-lord-of-the-rings).
