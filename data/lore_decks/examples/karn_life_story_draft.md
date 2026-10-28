# Karn — a life told through artifacts (100-card story deck, DRAFT)

**Status: research demonstration only; NOT user-approved or locked.** Do not replace any of Cory's approved 62 Grixis decks. Narrative over optimization. This list is a new colorless Karn exhibit.

## Verification

- **Commander:** Karn, Legacy Reforged; color identity C (colorless).
- **Deck size:** 100 (one commander, 80 distinct non-basic cards, 19 Wastes).
- **Lands:** 35, including 19 Wastes and 16 non-basic lands.
- **Hard rules:** PASS on actual repository `evaluate_decklist.check` (singleton, Commander eligibility, color identity, 100 cards, Scryfall legality); zero hard issues.
- **Provisional bracket floor:** 2 by existing `bracket_floor` checks; zero Scryfall Game Changers, zero detected mass-land-denial text. Commander Spellbook combination audit still pending; **do not guarantee Bracket 2**.
- **Printed evidence coverage:** 42/81 slots have a literal subject-term flavor mention in a selected printing; 35/81 have a story-era printing but no literal subject-term flavor; 4/81 are named objects or curated contextual connections. None of these counts independently proves depicted events.
- **Source snapshot:** Scryfall `default-cards-20261028090549.jsonl.gz`, SHA-256 `c7c6d738cae2a9419e2120afedba460c4afeaa026bf74ca60e6451d14486d1e2` (English/default-language paper printings).

## How this deck tells Karn's life

1. **Urza's Legacy: the Brothers' War, the silver golem, and the Thran** (27 cards). Curated lore pointers: Characters Index.md#karn · Characters Index.md#urza · Master Timeline.md#brothers-war--phyrexian-wars. Official background: [Wizards story](https://magic.wizards.com/en/story/urza-planeswalker) · [Wizards story](https://magic.wizards.com/en/story/karn-planeswalker).
2. **Karn creates Argentum and entrusts it to Memnarch** (21 cards). Curated lore pointers: Conflicts & Arcs.md#phyrexian-conquest-of-mirrodin · Planes Index.md#mirrodin-before-phyrexia. Official background: [Wizards story](https://magic.wizards.com/en/story/mirrodin-plane) · [Wizards story](https://magic.wizards.com/en/news/feature/vault-lore-2016-08-01).
3. **Mirrodin falls to Phyrexian oil and the multiverse invasion** (26 cards). Curated lore pointers: Conflicts & Arcs.md#phyrexian-invasion-of-the-multiverse · Master Timeline.md#phyrexian-invasion · Items & Artifacts Index.md#golgothian-sylex. Official background: [Wizards story](https://magic.wizards.com/en/story/new-phyrexia-plane) · [Wizards story](https://magic.wizards.com/en/story/mirrodin-plane).
4. **Karn's liberation, resistance, and renewed purpose** (6 cards). Curated lore pointers: Characters Index.md#karn · Conflicts & Arcs.md#march-of-the-machine-2023 · Conflicts & Arcs.md#march-of-the-machine-the-aftermath-2023. Official background: [Wizards story](https://magic.wizards.com/en/story/karn-planeswalker) · [Wizards story](https://magic.wizards.com/en/story/new-phyrexia-plane).

**Canon cautions:**
- Mirari became Memnarch; it was not the material used to create Argentum.
- The Golgothian Sylex's original creator/history has competing official accounts; do not assert one version as settled.
- Lore beat order is interpretive within chapters, not proof of precise dates for every card.
- English/default-language Scryfall printing archive, not all foreign-language editions.
- Mycosynth Lattice deliberately excluded from this low-bracket example: with Karn, the Great Creator it can lock opponents out of lands, and Karn, Silver Golem can animate their artifact lands into 0/0 creatures.

## Importable 100-card list

```text
1x Karn, Legacy Reforged [Commander]
1x Karn, Silver Golem
1x Thran Golem
1x Power Matrix
1x Thran Dynamo
1x Thran Foundry
1x Thran Temporal Gateway
1x Gilded Lotus
1x Worn Powerstone
1x Powerstone Shard
1x Urza's Incubator
1x Urza's Armor
1x Urza's Avenger
1x Urza's Tome
1x Urza's Saga
1x Urza's Workshop
1x Urza's Mine
1x Urza's Power Plant
1x Urza's Tower
1x Tocasia's Dig Site
1x Mishra's Factory
1x Mishra's Foundry
1x Hall of Tagsin
1x Urza's Cave
1x Sculpting Steel
1x Bottle Gnomes
1x The Mightstone and Weakstone
1x The Stasis Coffin
1x Mirari
1x Darksteel Forge
1x Darksteel Citadel
1x Mirrodin's Core
1x Ur-Golem's Eye
1x Argentum Armor
1x Memnarch, the Warden
1x Memnite
1x Mycosynth Golem
1x Leveler
1x Coretapper
1x Genesis Chamber
1x Myr Retriever
1x Myr Battlesphere
1x Myr Turbine
1x Icy Manipulator
1x Tower of Fortunes
1x Darksteel Ingot
1x Darksteel Reactor
1x Darksteel Colossus
1x Glimmerpost
1x Mycosynth Wellspring
1x Phyrexian Atlas
1x Phyrexian Hulk
1x Phyrexian Revoker
1x Phyrexian Juggernaut
1x Phyrexian Triniform
1x Phyrexian Archivist
1x Soul of New Phyrexia
1x Wurmcoil Engine
1x Blightsteel Colossus
1x Portal to Phyrexia
1x The Filigree Sylex
1x Karn's Sylex
1x Golgothian Sylex
1x Darksteel Monolith
1x Darksteel Relic
1x Decimator Web
1x Contagion Clasp
1x Contagion Engine
1x Phyrexian Processor
1x Phyrexian Dreadnought
1x Phyrexia's Core
1x The Mycosynth Gardens
1x Weatherlight Compleated
1x Darksteel Plate
1x Ichor Wellspring
1x Karn's Bastion
1x Karn Liberated
1x Karn, Scion of Urza
1x Karn, Living Legacy
1x Karn, the Great Creator
1x Karn, Argent Defender
19x Wastes
```

## Card-by-card story rationale (source edition noted)

### Urza's Legacy: the Brothers' War, the silver golem, and the Thran

| Card | Why it belongs | Evidence level · selected printing |
|---|---|---|
| Karn, Silver Golem | The original silver golem's own legendary card anchors Karn's early life. | Story-era printing (contextual); [USG #298](https://scryfall.com/card/usg/298/karn-silver-golem?utm_source=api) |
| Thran Golem | Its printed flavor compares another golem's purpose to Karn's worth to Urza. | Literal printing-flavor mention; [UDS #141](https://scryfall.com/card/uds/141/thran-golem?utm_source=api) |
| Power Matrix | Its flavor text traces Karn repairing the Weatherlight's planeswalking engine. | Literal printing-flavor mention; [MB2 #229](https://scryfall.com/card/mb2/229/power-matrix?utm_source=api) |
| Thran Dynamo | A power source connected by flavor to Urza's mechanical ambitions. | Literal printing-flavor mention; [UDS #139](https://scryfall.com/card/uds/139/thran-dynamo?utm_source=api) |
| Thran Foundry | Urza's reclamation ethic appears in the printed quote. | Literal printing-flavor mention; [UDS #140](https://scryfall.com/card/uds/140/thran-foundry?utm_source=api) |
| Thran Temporal Gateway | The Thran artifact legacy bridges ancient technology and Karn's origins. | Story-era printing (contextual); [DOM #233](https://scryfall.com/card/dom/233/thran-temporal-gateway?utm_source=api) |
| Gilded Lotus | Karn's printed reflection on his hopes for Mirrodin and past failures. | Literal printing-flavor mention; [DOM #215](https://scryfall.com/card/dom/215/gilded-lotus?utm_source=api) |
| Worn Powerstone | A powerstone fragment evokes the engines of the Legacy. | Literal printing-flavor mention; [C18 #230](https://scryfall.com/card/c18/230/worn-powerstone?utm_source=api) |
| Powerstone Shard | Its flavor recounts the way powerstones refract planar energy through Urza's eyes. | Literal printing-flavor mention; [DOM #227](https://scryfall.com/card/dom/227/powerstone-shard?utm_source=api) |
| Urza's Incubator | Its flavor depicts Urza's conflicted role as a creator and father. | Literal printing-flavor mention; [UDS #142](https://scryfall.com/card/uds/142/urzas-incubator?utm_source=api) |
| Urza's Armor | Tawnos's blueprints and Urza's steel-bound body prefigure Karn's creation. | Literal printing-flavor mention; [USG #313](https://scryfall.com/card/usg/313/urzas-armor?utm_source=api) |
| Urza's Avenger | An early artificer's golem design from Urza's workshop. | Literal printing-flavor mention; [ATQ #74](https://scryfall.com/card/atq/74/urzas-avenger?utm_source=api) |
| Urza's Tome | The written memory of Urza's artifice and long research. | Story-era printing (contextual); [DOM #235](https://scryfall.com/card/dom/235/urzas-tome?utm_source=api) |
| Urza's Saga | A land-Saga that tells the Legacy's broader history through its chapters. | Named object/contextual; [PMH2 #259s](https://scryfall.com/card/pmh2/259s/urzas-saga?utm_source=api) |
| Urza's Workshop | Urza's machine workshop and Tocasia's influence, per its flavor. | Literal printing-flavor mention; [BRC #28](https://scryfall.com/card/brc/28/urzas-workshop?utm_source=api) |
| Urza's Mine | Powerstone mining from Dominaria's ancient past. | Literal printing-flavor mention; [2XM #329](https://scryfall.com/card/2xm/329/urzas-mine?utm_source=api) |
| Urza's Power Plant | Urza's escalating experiments and search for perfection. | Literal printing-flavor mention; [J22 #830](https://scryfall.com/card/j22/830/urzas-power-plant?utm_source=api) |
| Urza's Tower | Urza's study of Thran construction and desire to surpass it. | Literal printing-flavor mention; [ATQ #85c](https://scryfall.com/card/atq/85c/urzas-tower?utm_source=api) |
| Tocasia's Dig Site | The cave expedition that began Urza and Mishra's story. | Literal printing-flavor mention; [BRO #266](https://scryfall.com/card/bro/266/tocasias-dig-site?utm_source=api) |
| Mishra's Factory | The old war machine factory in the Brothers' War's aftermath. | Story-era printing (contextual); [ATQ #80b](https://scryfall.com/card/atq/80b/mishras-factory?utm_source=api) |
| Mishra's Foundry | The machinery of Mishra's side of the war in modern retellings. | Story-era printing (contextual); [BRO #265](https://scryfall.com/card/bro/265/mishras-foundry?utm_source=api) |
| Hall of Tagsin | The Thran powerstone site that begins the Brothers' War. | Literal printing-flavor mention; [BRO #263](https://scryfall.com/card/bro/263/hall-of-tagsin?utm_source=api) |
| Urza's Cave | Urza's deep research and regrets revisited by the land's flavor. | Literal printing-flavor mention; [MH3 #234](https://scryfall.com/card/mh3/234/urzas-cave?utm_source=api) |
| Sculpting Steel | Tawnos's self-assembling metals echo Karn's shaping of artifact life. | Literal printing-flavor mention; [BRR #113z](https://scryfall.com/card/brr/113z/sculpting-steel?utm_source=api) |
| Bottle Gnomes | A printing quotes Karn's fable of the silver egg and its humble center. | Literal printing-flavor mention; [WC99 #js278](https://scryfall.com/card/wc99/js278/bottle-gnomes?utm_source=api) |
| The Mightstone and Weakstone | The old powerstone halves recur in Karn's inherited Legacy. | Story-era printing (contextual); [BRO #238](https://scryfall.com/card/bro/238/the-mightstone-and-weakstone?utm_source=api) |
| The Stasis Coffin | Tawnos's sealed time-displacement artifact connects past and present. | Literal printing-flavor mention; [BRO #245](https://scryfall.com/card/bro/245/the-stasis-coffin?utm_source=api) |

### Karn creates Argentum and entrusts it to Memnarch

| Card | Why it belongs | Evidence level · selected printing |
|---|---|---|
| Mirari | Karn later transforms the dangerous Mirari into the sentient caretaker who becomes Memnarch—not the material used to make Argentum. | Named object/contextual; [V10 #9](https://scryfall.com/card/v10/9/mirari?utm_source=api) |
| Darksteel Forge | A named Mirrodin forge whose flavor questions its impossible origins. | Literal printing-flavor mention; [DST #110](https://scryfall.com/card/dst/110/darksteel-forge?utm_source=api) |
| Darksteel Citadel | The Panopticon and the seat of Mirrodin's keeper, per printed flavor. | Literal printing-flavor mention; [BRC #180](https://scryfall.com/card/brc/180/darksteel-citadel?utm_source=api) |
| Mirrodin's Core | The source-plane's own central land card. | Story-era printing (contextual); [DST #165](https://scryfall.com/card/dst/165/mirrodins-core?utm_source=api) |
| Ur-Golem's Eye | The remnant of Karn's protector-creation, whose flavor accuses Memnarch. | Literal printing-flavor mention; [DST #155](https://scryfall.com/card/dst/155/ur-golems-eye?utm_source=api) |
| Argentum Armor | Its flavor explicitly names Mirrodin's still-living creator. | Literal printing-flavor mention; [SOM #137](https://scryfall.com/card/som/137/argentum-armor?utm_source=api) |
| Memnarch, the Warden | The plane's increasingly tyrannical guardian, created from the Mirari. | Literal printing-flavor mention; [FRC #100](https://scryfall.com/card/frc/100/memnarch-the-warden?utm_source=api) |
| Memnite | Memnarch's legacy reflected in the plane's small artifact creatures. | Literal printing-flavor mention; [SOM #174](https://scryfall.com/card/som/174/memnite?utm_source=api) |
| Mycosynth Golem | Mirrodin's artificial organism before and during the spread of oil. | Story-era printing (contextual); [5DN #137](https://scryfall.com/card/5dn/137/mycosynth-golem?utm_source=api) |
| Leveler | Memnarch's century-spanning hunters ravage Mirrodin in printed flavor. | Literal printing-flavor mention; [MRD #195](https://scryfall.com/card/mrd/195/leveler?utm_source=api) |
| Coretapper | A Mirrodin core-worker feeding Memnarch's creations. | Literal printing-flavor mention; [DST #107](https://scryfall.com/card/dst/107/coretapper?utm_source=api) |
| Genesis Chamber | Memnarch's machine reproduction system in the original Mirrodin era. | Literal printing-flavor mention; [DST #122](https://scryfall.com/card/dst/122/genesis-chamber?utm_source=api) |
| Myr Retriever | A Myr laborer tied to the world's machine ecology. | Story-era printing (contextual); [MRD #215](https://scryfall.com/card/mrd/215/myr-retriever?utm_source=api) |
| Myr Battlesphere | Mirrodin's many-machine armies and Myr culture in one card. | Story-era printing (contextual); [SOM #180](https://scryfall.com/card/som/180/myr-battlesphere?utm_source=api) |
| Myr Turbine | A factory engine for the Myr that Memnarch deployed. | Story-era printing (contextual); [MBS #117](https://scryfall.com/card/mbs/117/myr-turbine?utm_source=api) |
| Icy Manipulator | Its Mirrodin printing calls it a model of the plane in shape and spirit. | Literal printing-flavor mention; [MRD #186](https://scryfall.com/card/mrd/186/icy-manipulator?utm_source=api) |
| Tower of Fortunes | Flavor chronicles Mirrodin's creator and Memnarch's later betrayal. | Literal printing-flavor mention; [MRD #267](https://scryfall.com/card/mrd/267/tower-of-fortunes?utm_source=api) |
| Darksteel Ingot | An artifact whose printed flavor recalls Mirrodin before Phyrexia. | Literal printing-flavor mention; [C13 #241](https://scryfall.com/card/c13/241/darksteel-ingot?utm_source=api) |
| Darksteel Reactor | An iconic example of the plane's indestructible darksteel technology. | Story-era printing (contextual); [DST #114](https://scryfall.com/card/dst/114/darksteel-reactor?utm_source=api) |
| Darksteel Colossus | The vast indestructible construct emblematic of darksteel's peak. | Story-era printing (contextual); [DST #109](https://scryfall.com/card/dst/109/darksteel-colossus?utm_source=api) |
| Glimmerpost | A Locus whose flavor remembers the Mirrodin watcher and its absence. | Literal printing-flavor mention; [SOM #227](https://scryfall.com/card/som/227/glimmerpost?utm_source=api) |

### Mirrodin falls to Phyrexian oil and the multiverse invasion

| Card | Why it belongs | Evidence level · selected printing |
|---|---|---|
| Mycosynth Wellspring | Its printed flavor explicitly joins the oil, mycosynth, and New Phyrexia. | Literal printing-flavor mention; [NPH #145](https://scryfall.com/card/nph/145/mycosynth-wellspring?utm_source=api) |
| Phyrexian Atlas | Its printed flavor details the conquest's redesign of Mirrodin's layers. | Literal printing-flavor mention; [ONE #237](https://scryfall.com/card/one/237/phyrexian-atlas?utm_source=api) |
| Phyrexian Hulk | The glistening oil's older war machines as preserved blueprints. | Literal printing-flavor mention; [NPH #150](https://scryfall.com/card/nph/150/phyrexian-hulk?utm_source=api) |
| Phyrexian Revoker | A Phyrexian machine made to punish dissent, in Venser's diary flavor. | Literal printing-flavor mention; [BRR #103](https://scryfall.com/card/brr/103/phyrexian-revoker?utm_source=api) |
| Phyrexian Juggernaut | A New Phyrexian siege-engine embodying machine supremacy. | Literal printing-flavor mention; [MBS #121](https://scryfall.com/card/mbs/121/phyrexian-juggernaut?utm_source=api) |
| Phyrexian Triniform | A massive construct of New Phyrexian military design. | Story-era printing (contextual); [MOC #370](https://scryfall.com/card/moc/370/phyrexian-triniform?utm_source=api) |
| Phyrexian Archivist | A machine enforcing the invasion's oppressive silence. | Story-era printing (contextual); [MOM #262](https://scryfall.com/card/mom/262/phyrexian-archivist?utm_source=api) |
| Soul of New Phyrexia | The metallic heart of the conquering plane. | Story-era printing (contextual); [MOC #382](https://scryfall.com/card/moc/382/soul-of-new-phyrexia?utm_source=api) |
| Wurmcoil Engine | One of Mirrodin's Phyrexian-engine horrors. | Story-era printing (contextual); [SOM #223](https://scryfall.com/card/som/223/wurmcoil-engine?utm_source=api) |
| Blightsteel Colossus | The corruption of darksteel into a Phyrexian weapon. | Story-era printing (contextual); [MBS #99](https://scryfall.com/card/mbs/99/blightsteel-colossus?utm_source=api) |
| Portal to Phyrexia | Its flavor announces the ancient nightmare returning after millennia. | Story-era printing (contextual); [BRO #240](https://scryfall.com/card/bro/240/portal-to-phyrexia?utm_source=api) |
| The Filigree Sylex | The invasion-era echo of the bowl at the center of Karn's plan. | Story-era printing (contextual); [ONE #394](https://scryfall.com/card/one/394/the-filigree-sylex?utm_source=api) |
| Karn's Sylex | Karn's attempted answer to the threat of New Phyrexia. | Story-era printing (contextual); [DMU #234](https://scryfall.com/card/dmu/234/karns-sylex?utm_source=api) |
| Golgothian Sylex | The original Brothers' War relic with an uncertain/conflicting origin. | Story-era printing (contextual); [ATQ #51](https://scryfall.com/card/atq/51/golgothian-sylex?utm_source=api) |
| Darksteel Monolith | Printed flavor locates Phyrexian oil in Mirrodin's heart. | Literal printing-flavor mention; [CMM #743](https://scryfall.com/card/cmm/743/darksteel-monolith?utm_source=api) |
| Darksteel Relic | Its flavor mourns what the Mirran resistance can still claim. | Story-era printing (contextual); [NPH #134](https://scryfall.com/card/nph/134/darksteel-relic?utm_source=api) |
| Decimator Web | Its flavor tracks mycosynth spreading beneath a black lacuna. | Literal printing-flavor mention; [MBS #105](https://scryfall.com/card/mbs/105/decimator-web?utm_source=api) |
| Contagion Clasp | A literal artifact of New Phyrexia's proliferating contamination. | Story-era printing (contextual); [ONC #129](https://scryfall.com/card/onc/129/contagion-clasp?utm_source=api) |
| Contagion Engine | The industrial machinery of infection and viral escalation. | Story-era printing (contextual); [SOM #145](https://scryfall.com/card/som/145/contagion-engine?utm_source=api) |
| Phyrexian Processor | An earlier Phyrexian engine linking old and new invasions. | Story-era printing (contextual); [USG #306](https://scryfall.com/card/usg/306/phyrexian-processor?utm_source=api) |
| Phyrexian Dreadnought | An Old Phyrexian war machine in the historical threat lineage. | Named object/contextual; [G10 #3](https://scryfall.com/card/g10/3/phyrexian-dreadnought?utm_source=api) |
| Phyrexia's Core | A land whose flavor mourns the corruption of Mirrodin's very center. | Story-era printing (contextual); [NPH #165](https://scryfall.com/card/nph/165/phyrexias-core?utm_source=api) |
| The Mycosynth Gardens | The transformed mycosynth landscape across Mirrodin/New Phyrexia. | Story-era printing (contextual); [ONE #256](https://scryfall.com/card/one/256/the-mycosynth-gardens?utm_source=api) |
| Weatherlight Compleated | The corruption of the ship Karn helped develop and the Legacy crew once used. | Story-era printing (contextual); [DMU #242](https://scryfall.com/card/dmu/242/weatherlight-compleated?utm_source=api) |
| Darksteel Plate | Koth's promise to fight on despite resistance's desperate odds. | Story-era printing (contextual); [MBS #104](https://scryfall.com/card/mbs/104/darksteel-plate?utm_source=api) |
| Ichor Wellspring | A Brothers' War retro-frame printing quotes Yawgmoth on self-multiplying glistening oil, directly illustrating the Phyrexian infection that spread through Mirrodin. | Literal printing-flavor mention; [BRR #84z](https://scryfall.com/card/brr/84z/ichor-wellspring?utm_source=api) |

### Karn's liberation, resistance, and renewed purpose

| Card | Why it belongs | Evidence level · selected printing |
|---|---|---|
| Karn's Bastion | A Mirrodin resistance land quoting Karn's vow to protect survivors. | Literal printing-flavor mention; [ONC #156](https://scryfall.com/card/onc/156/karns-bastion?utm_source=api) |
| Karn Liberated | Karn's emancipation from New Phyrexia and the pivot to resisting corruption. | Story-era printing (contextual); [NPH #1](https://scryfall.com/card/nph/1/karn-liberated?utm_source=api) |
| Karn, Scion of Urza | His bond to Urza and his inherited role as an artificer's creation. | Story-era printing (contextual); [DOM #1](https://scryfall.com/card/dom/1/karn-scion-of-urza?utm_source=api) |
| Karn, Living Legacy | His return to Dominaria to confront the Sylex problem. | Story-era printing (contextual); [DMU #372](https://scryfall.com/card/dmu/372/karn-living-legacy?utm_source=api) |
| Karn, the Great Creator | His role as maker and guardian of artifact worlds. | Named object/contextual; [SLD #501](https://scryfall.com/card/sld/501/karn-the-great-creator?utm_source=api) |
| Karn, Argent Defender | Karn's later vows to repair the harm his creations helped cause. | Story-era printing (contextual); [FRA #320](https://scryfall.com/card/fra/320/karn-argent-defender?utm_source=api) |

## How to use this draft

- Choose which moments matter most to Cory; replace any weak narrative fit only with a better documented card after color-identity and printing checks.
- A set appearance and a name coincidence are **not** direct proof a card depicts an event. Recheck disputed retcons and flavor variants before treating the narrative as canon.
- Re-run `python3 scripts/story_deck_planner.py assemble data/lore_decks/examples/karn_life_story_draft.json --validate --bulk-file /path/to/explicit-Scryfall-bulk.jsonl.gz` and independently inspect combos before any final approval.
- The example remains intentionally outside `decks/` and outside the 62-deck Grixis canonical collection.
