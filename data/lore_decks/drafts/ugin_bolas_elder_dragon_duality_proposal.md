# Phase 6 Pilot 1 — Ugin & Nicol Bolas - Elder Dragon Duality (Phase 6 Pilot 1)

**Status: UNAPPROVED PROPOSAL - awaiting Cory's review; not approved, not locked, not certified**

Commander: **Nicol Bolas, the Ravager** (M19 #218). Ugin is colourless and appears in the 99 (three Ugin planeswalkers plus Ugin-named cards and sites).

## Verification (reproducible, offline after snapshot)

- Snapshot: `snap-20261029-40848334824-1`; default-cards `default-cards-20261029090546.jsonl.gz` sha256 `008434d5b89f1f2cb47411178d2ab181600faf9cb7ca1c5673422cdec5939595`.
- `story_deck_planner.py assemble … --validate --bulk-file oracle-cards-20261029090202.jsonl.gz` (multiverse mode, not the frozen Grixis lock): **passed**, 100 cards, identity UBR, 35 lands, 0 hard issues.
- `evaluate_decklist.py --combos` (multiverse cache, Scryfall bulk 2026-10-29): Hard checks PASS; Game Changers: Bolas's Citadel (1); mass land denial: none; extra turns: Ugin's Nexus (single, not chained); Commander Spellbook 0 combos / 0 two-card infinite (local Spellbook data as shipped; not an exhaustive combo proof); minimum bracket **3**.
- `scripts/audit_ugin_bolas_duality_pilot.py` + `tests/test_ugin_bolas_duality_pilot.py` replay counts, singleton, identity, recorded legality, tiers, provenance, Pack A grade preservation and the decklist SHA-256.
- Raw decklist SHA-256: `01d087aa2819b1ed3c7ac1f64843f76f36b551b72fda62d64218d19c40b0ab45`.

## Grading

| Tier | Count | Meaning |
|---|---|---|
| DIRECT_DEPICTION | 6 | Official Wizards story captions this exact art at the event, or Pack A4 exact-art scene match. |
| CANON_REFERENCE | 54 | Card is the character/object/event, or its printed text or an official article ties it to Ugin/Bolas canon. |
| LORE_INSPIRED | 8 | Named or thematic link only; no scene or event asserted. |
| MECHANICAL_SYMBOL | 15 | Included for function; no story claim. |

## Story acts

### Commander

- **Nicol Bolas, the Ravager // Nicol Bolas, the Arisen** (M19 #218, Svetlin Velinov) — `CANON_REFERENCE`. Grixis Elder Dragon commander; transforms into the Arisen. Ugin is colourless and lives in the 99. [source](https://magic.wizards.com/en/news/making-magic/more-odds-ends-core-set-2019-2018-08-06)

### I. Twin Elder Dragons of Dominaria and the Elder Dragon War

- **Nicol Bolas** (A25 #209, D. Alexander Gregory) — `CANON_REFERENCE`. The original Elder Dragon card; printed flavor 'Dominaria's most ancient evil.' Bolas and Ugin hatched as twins on Dominaria. [source](https://magic.wizards.com/en/news/magic-story/chronicle-bolas-twins-2018-06-13) — flavor: “Dominaria's most ancient evil.”
- **The Elder Dragon War** (DMU #121, Filip Burburan) — `CANON_REFERENCE`. Names the war Bolas instigated among the elder dragons. Not certified as a literal battlefield reconstruction. [source](https://magic.wizards.com/en/news/feature/dominaria-united-release-notes-2022-08-26)
- **Crosis, the Purger** (INV #242, Pete Venters) — `CANON_REFERENCE`. Grixis-coloured primeval descendant of the elder dragon lineage (Piru line, Pack A2). [source](https://magic.wizards.com/en/news/feature/returning-legends-modern-horizons-2-2021-06-10)
- **Ghostfire** (FUT #115, Cyril Van Der Haegen) — `CANON_REFERENCE`. Printed flavor: only those gifted with the eye of Ugin, the spirit dragon, can see his fiery breath. Colourless red spell. — flavor: “Only those gifted with the eye of Ugin, the spirit dragon, can see his fiery breath.”
- **Fraying Omnipotence** (M19 #97, Svetlin Velinov) — `CANON_REFERENCE`. Printed flavor: the Mending unravelled Nicol Bolas's power. Bridges the ancient god-like Bolas to the post-Mending schemer. — flavor: “The Great Mending that healed the Multiverse also unraveled the threads of Nicol Bolas's power.”

### II. Alara: the Conflux scheme

- **Nicol Bolas, Planeswalker** (CON #120, D. Alexander Gregory) — `CANON_REFERENCE`. Pack A4 exact-art match (NAMED_CHARACTER_ART_IN_STORY): the Bolas portrait used in the Ugin/Bolas duel coverage. [source](https://magic.wizards.com/en/news/feature/reforged-chain-2015-01-21)
- **Slave of Bolas** (ARB #136, Steve Argyle) — `CANON_REFERENCE`. Named after Bolas; flavor: Bolas does not distinguish servants and victims. — flavor: “Nicol Bolas doesn't distinguish between servants and victims.”
- **Soul Manipulation** (ARB #29, Carl Critchlow) — `CANON_REFERENCE`. Printed Nicol Bolas quote; Grixis counter/recursion of the Conflux era. — flavor: “"Birth and death are both reversible." —Nicol Bolas”
- **Countersquall** (DDH #59, Anthony Francisco) — `CANON_REFERENCE`. Duel Decks: Ajani vs. Nicol Bolas printing; flavor states Bolas's creed of power. — flavor: “"The essence of every world, every spell, and every thought is power. Nothing else matters, because nothing else exists." —Nicol Bolas”
- **Mana Drain** (J16 #2, Mike Bierek) — `CANON_REFERENCE`. Judge printing with a Nicol Bolas quote: 'Power is wasted on the weak.' Not a Game Changer. — flavor: “"Power is wasted on the weak. They never keep it for long." —Nicol Bolas”
- **Magmaquake** (M13 #140, Gabor Szikszai) — `CANON_REFERENCE`. Printed Nicol Bolas threat; the M13 Bolas planeswalker-deck era. — flavor: “"Where will you run when I punish you with the very ground you flee on?" —Nicol Bolas”
- **Augur of Bolas** (WAR #41, Alex Konstad) — `CANON_REFERENCE`. War of the Spark printing: 'There is no future save the one my master wills.' — flavor: “"There is no future save the one my master wills."”
- **Disciple of Bolas** (M13 #88, Slawomir Maniak) — `CANON_REFERENCE`. Printed 'Lord Bolas' quote; sacrifice-for-cards servant. — flavor: “"Lord Bolas has shown me how each miserable little life holds untold resources."”

### III. Zendikar: Ugin's hedrons and the Eldrazi prison

- **Hedron Archive** (BFZ #223, Craig J Spearing) — `CANON_REFERENCE`. Printed Ugin dialogue about the hedrons' true purpose. — flavor: “"You've begun to understand the hedrons' true purpose," said Ugin. "The Eldrazi can be imprisoned.""And how did that work out last time?" asked Jace.”
- **Perilous Vault** (M15 #224, Sam Burley) — `CANON_REFERENCE`. Printed flavor: Ugin arranged Zendikar's hedrons to direct leylines. — flavor: “The spirit dragon Ugin arranged the hedrons of Zendikar to direct leylines of energy. To disrupt one is to unleash devastation and chaos.”
- **Ugin's Insight** (BFZ #87, Tyler Jacobson) — `CANON_REFERENCE`. Printed Ugin quote on the three Eldrazi titans. — flavor: “"You speak to me of the threat of Ulamog. But do not forget: they came as three." —Ugin, to Jace Beleren”
- **Dispel** (BFZ #76, Chase Stone) — `CANON_REFERENCE`. BFZ printing contrasting Ugin's stasis plan with destruction of the Eldrazi. — flavor: “"I said we should destroy the Eldrazi. Ugin wanted to return them to stasis. Ugin's arguments were . . . unconvincing." —Jace Beleren”
- **Ugin's Binding** (MH3 #76, Drew Baker) — `LORE_INSPIRED`. Named Ugin binding magic (devoid, colourless spell for Ugin, Eye of the Storms). Card name only; no scene claimed.

### IV. Tarkir: the duel, the fall, and the reforged timeline

- **Crux of Fate** (FRF #65, Michael Komarck) — `DIRECT_DEPICTION`. Pack A4 exact-art match: official story art caption of the Ugin-Bolas battle. [source](https://magic.wizards.com/en/news/feature/reforged-chain-2015-01-21) — flavor: “Ugin's whispered summons led Sarkhan Vol to the moment that would echo down the centuries and seal Tarkir's fate: the primal battle between Ugin and Nicol Bolas.”
- **Ugin's Nexus** (KTK #227, Sam Burley) — `CANON_REFERENCE`. Pack A4: official story device (the nexus Sarkhan uses to reach the past). [source](https://magic.wizards.com/en/news/magic-story/chronicle-bolas-familiar-stranger-2018-08-01) — flavor: “All at once Sarkhan's mind fell silent.”
- **Ugin, the Spirit Dragon** (FRF #1, Raymond Swanland) — `CANON_REFERENCE`. Pack A4 exact Raymond Swanland art (not the ugin/1 promo art). Ugin survives in the reforged timeline. [source](https://magic.wizards.com/en/news/feature/reforged-chain-2015-01-21)
- **Bitter Revelation** (KTK #65, Viktor Titov) — `CANON_REFERENCE`. Printed Sorin quote at Ugin's tomb in the original Khans timeline. — flavor: “"Here you lie then, Ugin. The corpses of worlds will join you in the tomb." —Sorin Markov”
- **Witness of the Ages** (KTK #228, Izzy) — `CANON_REFERENCE`. Printed flavor: it strode through the clash of dragons and the fall of Ugin. — flavor: “It strode through the clash of dragons, the fall of Ugin, and the rise of the khans.”
- **Fearsome Awakening** (FRF #69, Véronique Meignaud) — `CANON_REFERENCE`. Fate Reforged printing tying the dragon tempests to Ugin; reanimates a dragon. — flavor: “On Tarkir, dragons emerge from enormous tempests, phenomena tied to Ugin's very presence on the plane.”
- **Sarkhan the Mad** (ROE #214, Chippy) — `CANON_REFERENCE`. Official profile: Sarkhan swore fealty to Bolas and went mad before returning to Tarkir. [source](https://magic.wizards.com/en/story/sarkhan-vol-planeswalker)
- **Sarkhan, the Dragonspeaker** (KTK #119, Daarken) — `CANON_REFERENCE`. Official profile: Sarkhan travelled back and saved Ugin from death at Bolas's hands. [source](https://magic.wizards.com/en/story/sarkhan-vol-planeswalker)
- **Dragonlord Silumgar** (DTK #220, Steven Belledin) — `CANON_REFERENCE`. Official Tarkir page: Ugin's survival produced the dragonlord timeline; Silumgar is the Grixis-adjacent UB dragonlord. [source](https://magic.wizards.com/en/story/tarkir-plane) — flavor: “Silumgar never passes up an opportunity to add to his opulence.”
- **Dragonlord Kolaghan** (DTK #218, Jaime Jones) — `CANON_REFERENCE`. Same consequence; Kolaghan is the BR dragonlord. [source](https://magic.wizards.com/en/story/tarkir-plane)

### V. Amonkhet: the God-Pharaoh and the Hour of Devastation

- **Nicol Bolas, God-Pharaoh** (HOU #140, Raymond Swanland) — `CANON_REFERENCE`. Official Amonkhet page: the God-Pharaoh is Nicol Bolas. [source](https://magic.wizards.com/en/story/amonkhet-plane)
- **The Scarab God** (HOU #145, Lius Lasahido) — `CANON_REFERENCE`. Bolas warped one of Amonkhet's gods to raise the Eternal army (official design article). [source](https://magic.wizards.com/en/news/making-magic/devastation-information-part-3-2017-07-17)
- **The Locust God** (HOU #139, Lius Lasahido) — `CANON_REFERENCE`. Bolas's god tasked with devouring the Hekma barrier. [source](https://magic.wizards.com/en/news/making-magic/devastation-information-part-3-2017-07-17)
- **The Scorpion God** (HOU #146, Lius Lasahido) — `CANON_REFERENCE`. Bolas's god tasked with killing the other five gods. [source](https://magic.wizards.com/en/news/making-magic/devastation-information-part-3-2017-07-17)
- **Hour of Devastation** (HOU #97, Simon Dominic) — `DIRECT_DEPICTION`. Art is captioned in the official 'Hour of Devastation' story at Bolas's arrival in the ruined plaza. [source](https://magic.wizards.com/en/news/magic-story/hour-devastation-2017-07-26) — flavor: “"Everything here exists or perishes at my whim. Including you, Gatewatch." —Nicol Bolas”
- **Jace's Defeat** (HOU #38, Kieran Yanner) — `DIRECT_DEPICTION`. Captioned in the official story as Bolas crushes Jace's mind. [source](https://magic.wizards.com/en/news/magic-story/hour-devastation-2017-07-26) — flavor: “"I had hoped for more from you, Jace. But I expected as much." —Nicol Bolas”
- **Liliana's Defeat** (HOU #68, Kieran Yanner) — `DIRECT_DEPICTION`. Captioned in the official story as Liliana leaves at Bolas's offer. [source](https://magic.wizards.com/en/news/magic-story/hour-devastation-2017-07-26) — flavor: “"All the power you have gathered for yourself, Liliana, I can take away." —Nicol Bolas”
- **Chandra's Defeat** (HOU #86, Kieran Yanner) — `DIRECT_DEPICTION`. Captioned in the official story as Chandra flees Bolas. [source](https://magic.wizards.com/en/news/magic-story/hour-devastation-2017-07-26) — flavor: “"Fire? Is that your only trick, Chandra?" —Nicol Bolas”
- **Doomfall** (HOU #62, Darek Zabrocki) — `CANON_REFERENCE`. Printed Nicol Bolas quote: 'This place has outlived its usefulness.' — flavor: “"This place has outlived its usefulness." —Nicol Bolas”
- **Neheb, the Eternal** (HOU #104, Chris Rahn) — `CANON_REFERENCE`. Printed Nicol Bolas quote: 'This is what glory looks like.' — flavor: “"This is what glory looks like." —Nicol Bolas”
- **Wasp of the Bitter End** (HOU #206, Tomasz Jedruszek) — `CANON_REFERENCE`. Printed flavor: a chorus of wings heralds the return of Nicol Bolas. — flavor: “As the Second Sun glided into its final position in the sky, a chorus of wings sounded to herald the return of Nicol Bolas.”
- **Visage of Bolas** (HOU #208, Titus Lunter) — `LORE_INSPIRED`. Named Bolas monument; Grixis mana. Card name only (no printed flavor).
- **Nicol Bolas, the Deceiver** (HOU #205, Svetlin Velinov) — `CANON_REFERENCE`. Bolas at the moment of the Hours. [source](https://magic.wizards.com/en/story/amonkhet-plane)
- **Tezzeret, Agent of Bolas** (MBS #97, Aleksi Briclot) — `CANON_REFERENCE`. Official HOU story ends with Tezzeret calling Bolas 'master' and running his errands. [source](https://magic.wizards.com/en/news/magic-story/hour-devastation-2017-07-26)

### VI. War of the Spark: the Elderspell, the fall, the prison

- **Nicol Bolas, Dragon-God** (WAR #207, Raymond Swanland) — `CANON_REFERENCE`. Bolas empowered by the Elderspell on Ravnica. [source](https://magic.wizards.com/en/news/magic-story/war-spark-ravnica-ashes-2019-06-12)
- **Bolas's Citadel** (WAR #79, Jonas De Ro) — `CANON_REFERENCE`. The Citadel atop which Bolas falls. Game Changer (counted; bracket 3). [source](https://magic.wizards.com/en/news/magic-story/war-spark-ravnica-ashes-2019-06-12)
- **Commence the Endgame** (WAR #45, Noah Bradley) — `CANON_REFERENCE`. Printed Nicol Bolas quote: 'Even gods shall kneel.' — flavor: “"Even gods shall kneel." —Nicol Bolas”
- **Command the Dreadhorde** (WAR #82, Daarken) — `CANON_REFERENCE`. Printed flavor: Liliana seized the reins of Bolas's army. — flavor: “Liliana seized the reins of Bolas's vast army, gritting her teeth behind the Chain Veil.”
- **Spark Harvest** (WAR #105, Kieran Yanner) — `CANON_REFERENCE`. Printed flavor: Domri's harvested spark fuels Bolas's ascension. — flavor: “With the harvest of Domri's spark, the Elderspell began to fuel Bolas's ascension to godhood.”
- **God-Eternal Kefnet** (WAR #53, Lius Lasahido) — `CANON_REFERENCE`. Official: Bolas remade the slain Amonkhet gods as God-Eternals. [source](https://magic.wizards.com/en/news/making-magic/more-war-games-2019-04-29)
- **God-Eternal Bontu** (WAR #92, Lius Lasahido) — `CANON_REFERENCE`. Official story: Bontu bites Bolas and harvests the sparks of the Elderspell. [source](https://magic.wizards.com/en/news/magic-story/war-spark-ravnica-ashes-2019-06-12)
- **Liliana, Dreadhorde General** (WAR #97, Chris Rallis) — `CANON_REFERENCE`. Liliana commands the Dreadhorde, then turns the God-Eternals on Bolas. [source](https://magic.wizards.com/en/news/magic-story/war-spark-ravnica-ashes-2019-06-12)
- **Liliana's Triumph** (WAR #98, Kieran Yanner) — `DIRECT_DEPICTION`. Art captioned in the official 'Ashes' story at the moment Bontu harvests Bolas's sparks. [source](https://magic.wizards.com/en/news/magic-story/war-spark-ravnica-ashes-2019-06-12) — flavor: “Her triumph came not from escaping her death, but in claiming her independence.”
- **Finale of Revelation** (WAR #51, Johann Bodin) — `CANON_REFERENCE`. Printed flavor: Ugin saw Bolas's gem as the key to his brother's imprisonment. — flavor: “Ugin saw the gem that connected Bolas to his Meditation Realm as the key to his brother's downfall.”
- **Ugin, the Ineffable** (WAR #2, Daarken) — `CANON_REFERENCE`. Ugin at the end of the war; he holds Bolas in the Meditation Realm. [source](https://magic.wizards.com/en/news/making-magic/even-more-war-games-2019-05-06)
- **Ugin's Conjurant** (WAR #3, Ryan Yee) — `LORE_INSPIRED`. Named Ugin construct; colourless spell. Card name only.
- **Sarkhan's Catharsis** (WAR #144, Zack Stella) — `CANON_REFERENCE`. Printed Sarkhan quote turning on Bolas. — flavor: “"You once brought havoc to my home and ruined my mind. I'm here to return the favor, Bolas."”
- **No Escape** (WAR #63, G-host Lee) — `CANON_REFERENCE`. Printed flavor: Jace surmised they were walking into Bolas's trap. — flavor: “Jace surmised that they were walking into Bolas's trap. He felt no joy in being right.”

### VII. Tarkir Dragonstorm: Ugin's later fate

- **Ugin, Eye of the Storms** (TDM #1, Joshua Raphael) — `CANON_REFERENCE`. Ugin in the Dragonstorm era. A011 (his status afterwards) remains OPEN_QUESTION. [source](https://magic.wizards.com/en/news/magic-story/tarkir-dragonstorm-episode-7-return)
- **Dracogenesis** (TDM #402, Kai Carpenter) — `CANON_REFERENCE`. Showcase printing chosen for its Ugin flavor: the dragonstorms weakened with his death and raged with his life. — flavor: “Ugin and the dragonstorms of Tarkir are intrinsically linked. With his death they weakened. With his life they raged. But even the Spirit Dragon does not hold them fully under his sway.”
- **Watcher of the Wayside** (TDM #249, Brian Valeza) — `CANON_REFERENCE`. Printed flavor: the golem survived dragonlords, khans and Ugin himself. — flavor: “Against dragonlords, khans, and Ugin himself, the golem survived. Original purpose forgotten, it awaits orders that will never come, from a world that has moved on without it.”

### Story lands

- **Tomb of the Spirit Dragon** (KTK #245, Sam Burley) — `CANON_REFERENCE`. Pack A4 STORY_LOCATION_ART_CAPTION: Ugin's tomb in the original timeline. [source](https://magic.wizards.com/en/news/feature/journey-nexus-2014-12-10) — flavor: “"The voice calls me here, yet I see only bones. Is this more dragon trickery?" —Sarkhan Vol”
- **Crucible of the Spirit Dragon** (FRF #167, Jung Park) — `CANON_REFERENCE`. Pack A4 STORY_LOCATION_ART_CAPTION. [source](https://magic.wizards.com/en/news/magic-story/chronicle-bolas-familiar-stranger-2018-08-01)
- **Haven of the Spirit Dragon** (DTK #249, Raymond Swanland) — `LORE_INSPIRED`. Named Ugin site in the reforged timeline; recurs Ugin and dragons.
- **Maelstrom of the Spirit Dragon** (TDM #260, Carlos Palma Cruchaga) — `LORE_INSPIRED`. Named Dragonstorm-era Ugin site.
- **Ugin's Labyrinth** (MH3 #233, Mark Poole) — `LORE_INSPIRED`. Named Ugin site; can imprint the seven-mana Ugins.
- **Cinder Barrens** (HOU #209, Titus Lunter) — `CANON_REFERENCE`. HOU printing with a Nicol Bolas quote: 'it is all mine.' — flavor: “"I do as I choose with what is mine. And it is all mine." —Nicol Bolas”
- **Crumbling Necropolis** (ALA #222, Dave Kendall) — `LORE_INSPIRED`. Grixis shard of Alara, the world Bolas fed on. — flavor: “"They say the ruins of Sedraxis were once a shining capital in Vithia. Now it is a blight, a place to be avoided by the living." —Olcot, Rider of Joffik”
- **Interplanar Beacon** (WAR #247, Adam Paquette) — `LORE_INSPIRED`. Bolas's planeswalker lure on Ravnica; theme, not a scene claim.

### Playability

- **Sol Ring** (LEA #269, Mark Tedin) — `MECHANICAL_SYMBOL`. Mana/fixing for a UUBBRR commander; no story claim.
- **Arcane Signet** (ELD #331, Dan Murayama Scott) — `MECHANICAL_SYMBOL`. Mana/fixing for a UUBBRR commander; no story claim.
- **Talisman of Dominance** (MRD #253, Mike Dringenberg) — `MECHANICAL_SYMBOL`. Mana/fixing for a UUBBRR commander; no story claim.
- **Talisman of Creativity** (C21 #269, Lindsey Look) — `MECHANICAL_SYMBOL`. Mana/fixing for a UUBBRR commander; no story claim.
- **Talisman of Indulgence** (MRD #255, Mike Dringenberg) — `MECHANICAL_SYMBOL`. Mana/fixing for a UUBBRR commander; no story claim.
- **Command Tower** (CMD #269, Ryan Yee) — `MECHANICAL_SYMBOL`. Mana/fixing for a UUBBRR commander; no story claim.
- **Watery Grave** (RAV #286, Rob Alexander) — `MECHANICAL_SYMBOL`. Mana/fixing for a UUBBRR commander; no story claim.
- **Blood Crypt** (DIS #171, Rob Alexander) — `MECHANICAL_SYMBOL`. Mana/fixing for a UUBBRR commander; no story claim.
- **Steam Vents** (GPT #164, Rob Alexander) — `MECHANICAL_SYMBOL`. Mana/fixing for a UUBBRR commander; no story claim.
- **Drowned Catacomb** (M10 #224, Dave Kendall) — `MECHANICAL_SYMBOL`. Mana/fixing for a UUBBRR commander; no story claim.
- **Dragonskull Summit** (M10 #223, Jon Foster) — `MECHANICAL_SYMBOL`. Mana/fixing for a UUBBRR commander; no story claim.
- **Sulfur Falls** (ISD #248, Cliff Childs) — `MECHANICAL_SYMBOL`. Mana/fixing for a UUBBRR commander; no story claim.
- **Underground River** (ICE #362, NéNé Thomas) — `MECHANICAL_SYMBOL`. Mana/fixing for a UUBBRR commander; no story claim.
- **Sulfurous Springs** (ICE #360, Phil Foglio) — `MECHANICAL_SYMBOL`. Mana/fixing for a UUBBRR commander; no story claim.
- **Shivan Reef** (APC #142, Rob Alexander) — `MECHANICAL_SYMBOL`. Mana/fixing for a UUBBRR commander; no story claim.

### Basics

6× Island, 6× Swamp, 5× Mountain

## Canon caveats

- A003/A004 (who struck first; Ugin's perspective) are CANON_DISPUTED and are not asserted by any card here.
- A011 (Ugin's status after Lorwyn Eclipsed episode 2) is an OPEN_QUESTION; Ugin, Eye of the Storms only marks the Dragonstorm era.
- A012 Reality Fracture material is ALTERNATE_CONTINUITY and is excluded.
- Printed flavor proves what Wizards printed on the card, not that the illustration depicts a specific story scene.
- DIRECT_DEPICTION is used only where an official story captions that art at that event (or Pack A4's exact-art match).

## Not representable in a Grixis identity

- Yasova Dragonclaw (G/U-R) and Sarkhan, Dragonstorm era green-identity cards cannot enter a Grixis identity deck.
- Sarkhan Unbroken (GUR) is outside UBR identity.
- Piru, the Volatile and The Ur-Dragon are outside UBR identity; the Piru lineage is represented only by Crosis.
- Arcades Sabboth, Chromium and Palladia-Mors (Pack A2 siblings) are outside UBR identity.

## Archidekt

Tags: `Story: Ugin & Bolas Duality` · `Grixis Elder Dragon` · `Unapproved Lore Pilot`

Commander-first import list: `data/lore_decks/drafts/ugin_bolas_elder_dragon_duality_archidekt_import.txt`.

## What this is not

Not approved, not locked, not certified. Only Cory can approve a lore deck. No Grixis deck, ledger, lock or approved lore deck was modified.
