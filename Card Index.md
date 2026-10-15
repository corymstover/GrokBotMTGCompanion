# Card Index

> **Auto-generated** by `scripts/ingest_scryfall.py` — do not hand-edit. Tracks which cards have full entries. Machine-readable index: [`data/card_index.csv`](data/card_index.csv). State: [`data/ingest_state.json`](data/ingest_state.json).

## Contents
- [Totals](#totals)
- [Shards by letter](#shards-by-letter)
- [Category trackers](#category-trackers)
- [Game Changers ingested](#game-changers-ingested)
- [Top 100 by EDHREC rank](#top-100-by-edhrec-rank)
- [How to find a card](#how-to-find-a-card)

## Totals

| Metric | Value |
|---|---|
| Cards with full entries | **5,000** |
| Target universe (paper cards, Scryfall Oracle) | 34,185 (14.6% complete) |
| EDHREC-rank coverage (all Commander-legal cards ranked ≤ N ingested) | N = 4,980 |
| Commander legality of ingested | banned: 4, legal: 4,996 |
| Game Changers ingested | 48 |
| Shard files | 254 |
| Scryfall bulk data timestamp | 2026-10-15T09:02:01.217+00:00 |

### By color identity

| Identity | Cards |
|---|---|
| C | 756 |
| B | 626 |
| G | 724 |
| R | 599 |
| U | 650 |
| W | 620 |
| BG | 107 |
| BR | 77 |
| BU | 86 |
| BW | 98 |
| GR | 84 |
| GU | 89 |
| GW | 84 |
| RU | 73 |
| RW | 86 |
| UW | 80 |
| BGR | 10 |
| BGU | 12 |
| BGW | 10 |
| BRU | 15 |
| BRW | 19 |
| BUW | 13 |
| GRU | 14 |
| GRW | 17 |
| GUW | 15 |
| RUW | 12 |
| BGUW | 2 |
| GRUW | 2 |
| BGRUW | 20 |

## Shards by letter

Cards are stored in `cards/<LETTER>/<first-two-letters>.md` (accents stripped, punctuation ignored).

| Letter | Cards | Shard files |
|---|---|---|
| A | 312 | [aa](cards/A/aa.md), [ab](cards/A/ab.md), [ac](cards/A/ac.md), [ad](cards/A/ad.md), [ae](cards/A/ae.md), [af](cards/A/af.md), [ag](cards/A/ag.md), [ai](cards/A/ai.md), [aj](cards/A/aj.md), [ak](cards/A/ak.md), [al](cards/A/al.md), [am](cards/A/am.md), [an](cards/A/an.md), [ao](cards/A/ao.md), [ap](cards/A/ap.md), [aq](cards/A/aq.md), [ar](cards/A/ar.md), [as](cards/A/as.md), [at](cards/A/at.md), [au](cards/A/au.md), [av](cards/A/av.md), [aw](cards/A/aw.md), [ax](cards/A/ax.md), [ay](cards/A/ay.md), [az](cards/A/az.md) |
| B | 293 | [ba](cards/B/ba.md), [be](cards/B/be.md), [bi](cards/B/bi.md), [bl](cards/B/bl.md), [bo](cards/B/bo.md), [br](cards/B/br.md), [bu](cards/B/bu.md), [by](cards/B/by.md) |
| C | 347 | [ca](cards/C/ca.md), [ce](cards/C/ce.md), [ch](cards/C/ch.md), [ci](cards/C/ci.md), [cl](cards/C/cl.md), [co](cards/C/co.md), [cr](cards/C/cr.md), [cu](cards/C/cu.md), [cy](cards/C/cy.md) |
| D | 267 | [da](cards/D/da.md), [de](cards/D/de.md), [di](cards/D/di.md), [do](cards/D/do.md), [dr](cards/D/dr.md), [du](cards/D/du.md), [dw](cards/D/dw.md) |
| E | 202 | [ea](cards/E/ea.md), [ec](cards/E/ec.md), [ed](cards/E/ed.md), [ee](cards/E/ee.md), [ef](cards/E/ef.md), [ei](cards/E/ei.md), [el](cards/E/el.md), [em](cards/E/em.md), [en](cards/E/en.md), [eo](cards/E/eo.md), [ep](cards/E/ep.md), [er](cards/E/er.md), [es](cards/E/es.md), [et](cards/E/et.md), [eu](cards/E/eu.md), [ev](cards/E/ev.md), [ex](cards/E/ex.md), [ey](cards/E/ey.md), [ez](cards/E/ez.md) |
| F | 200 | [fa](cards/F/fa.md), [fe](cards/F/fe.md), [fi](cards/F/fi.md), [fl](cards/F/fl.md), [fo](cards/F/fo.md), [fr](cards/F/fr.md), [fu](cards/F/fu.md), [fy](cards/F/fy.md) |
| G | 246 | [ga](cards/G/ga.md), [ge](cards/G/ge.md), [gh](cards/G/gh.md), [gi](cards/G/gi.md), [gl](cards/G/gl.md), [go](cards/G/go.md), [gr](cards/G/gr.md), [gu](cards/G/gu.md), [gw](cards/G/gw.md), [gy](cards/G/gy.md) |
| H | 172 | [ha](cards/H/ha.md), [he](cards/H/he.md), [hi](cards/H/hi.md), [ho](cards/H/ho.md), [hu](cards/H/hu.md), [hy](cards/H/hy.md) |
| I | 125 | [ic](cards/I/ic.md), [id](cards/I/id.md), [if](cards/I/if.md), [ig](cards/I/ig.md), [ik](cards/I/ik.md), [il](cards/I/il.md), [im](cards/I/im.md), [in](cards/I/in.md), [io](cards/I/io.md), [ir](cards/I/ir.md), [is](cards/I/is.md), [it](cards/I/it.md), [iv](cards/I/iv.md), [iz](cards/I/iz.md) |
| J | 54 | [ja](cards/J/ja.md), [je](cards/J/je.md), [jh](cards/J/jh.md), [ji](cards/J/ji.md), [jo](cards/J/jo.md), [ju](cards/J/ju.md), [jw](cards/J/jw.md) |
| K | 128 | [k9](cards/K/k9.md), [ka](cards/K/ka.md), [ke](cards/K/ke.md), [kh](cards/K/kh.md), [ki](cards/K/ki.md), [kl](cards/K/kl.md), [kn](cards/K/kn.md), [ko](cards/K/ko.md), [kr](cards/K/kr.md), [ku](cards/K/ku.md), [kw](cards/K/kw.md), [ky](cards/K/ky.md) |
| L | 148 | [la](cards/L/la.md), [le](cards/L/le.md), [li](cards/L/li.md), [ll](cards/L/ll.md), [lo](cards/L/lo.md), [lu](cards/L/lu.md), [ly](cards/L/ly.md) |
| M | 310 | [ma](cards/M/ma.md), [me](cards/M/me.md), [mi](cards/M/mi.md), [mj](cards/M/mj.md), [mm](cards/M/mm.md), [mn](cards/M/mn.md), [mo](cards/M/mo.md), [ms](cards/M/ms.md), [mu](cards/M/mu.md), [my](cards/M/my.md) |
| N | 116 | [na](cards/N/na.md), [ne](cards/N/ne.md), [ni](cards/N/ni.md), [no](cards/N/no.md), [nu](cards/N/nu.md), [ny](cards/N/ny.md) |
| O | 117 | [oa](cards/O/oa.md), [ob](cards/O/ob.md), [oc](cards/O/oc.md), [od](cards/O/od.md), [of](cards/O/of.md), [og](cards/O/og.md), [oh](cards/O/oh.md), [oj](cards/O/oj.md), [ok](cards/O/ok.md), [ol](cards/O/ol.md), [om](cards/O/om.md), [on](cards/O/on.md), [op](cards/O/op.md), [or](cards/O/or.md), [os](cards/O/os.md), [ot](cards/O/ot.md), [ou](cards/O/ou.md), [ov](cards/O/ov.md), [oz](cards/O/oz.md) |
| P | 198 | [pa](cards/P/pa.md), [pe](cards/P/pe.md), [ph](cards/P/ph.md), [pi](cards/P/pi.md), [pl](cards/P/pl.md), [po](cards/P/po.md), [pr](cards/P/pr.md), [ps](cards/P/ps.md), [pu](cards/P/pu.md), [py](cards/P/py.md) |
| Q | 18 | [qa](cards/Q/qa.md), [qu](cards/Q/qu.md) |
| R | 260 | [ra](cards/R/ra.md), [re](cards/R/re.md), [rh](cards/R/rh.md), [ri](cards/R/ri.md), [rm](cards/R/rm.md), [ro](cards/R/ro.md), [ru](cards/R/ru.md), [ry](cards/R/ry.md) |
| S | 620 | [sa](cards/S/sa.md), [sc](cards/S/sc.md), [se](cards/S/se.md), [sh](cards/S/sh.md), [si](cards/S/si.md), [sk](cards/S/sk.md), [sl](cards/S/sl.md), [sm](cards/S/sm.md), [sn](cards/S/sn.md), [so](cards/S/so.md), [sp](cards/S/sp.md), [sq](cards/S/sq.md), [sr](cards/S/sr.md), [st](cards/S/st.md), [su](cards/S/su.md), [sv](cards/S/sv.md), [sw](cards/S/sw.md), [sy](cards/S/sy.md), [sz](cards/S/sz.md) |
| T | 422 | [ta](cards/T/ta.md), [te](cards/T/te.md), [th](cards/T/th.md), [ti](cards/T/ti.md), [to](cards/T/to.md), [tr](cards/T/tr.md), [tu](cards/T/tu.md), [tw](cards/T/tw.md), [ty](cards/T/ty.md) |
| U | 93 | [uc](cards/U/uc.md), [ug](cards/U/ug.md), [ul](cards/U/ul.md), [um](cards/U/um.md), [un](cards/U/un.md), [up](cards/U/up.md), [ur](cards/U/ur.md), [ut](cards/U/ut.md) |
| V | 121 | [va](cards/V/va.md), [ve](cards/V/ve.md), [vi](cards/V/vi.md), [vn](cards/V/vn.md), [vo](cards/V/vo.md), [vr](cards/V/vr.md) |
| W | 165 | [wa](cards/W/wa.md), [we](cards/W/we.md), [wh](cards/W/wh.md), [wi](cards/W/wi.md), [wo](cards/W/wo.md), [wr](cards/W/wr.md), [wu](cards/W/wu.md), [wy](cards/W/wy.md) |
| X | 6 | [xa](cards/X/xa.md), [xe](cards/X/xe.md), [xo](cards/X/xo.md), [xu](cards/X/xu.md), [xy](cards/X/xy.md) |
| Y | 25 | [ya](cards/Y/ya.md), [ye](cards/Y/ye.md), [yg](cards/Y/yg.md), [yo](cards/Y/yo.md), [ys](cards/Y/ys.md), [yu](cards/Y/yu.md) |
| Z | 35 | [za](cards/Z/za.md), [ze](cards/Z/ze.md), [zh](cards/Z/zh.md), [zi](cards/Z/zi.md), [zo](cards/Z/zo.md), [zu](cards/Z/zu.md) |

## Category trackers

Curated in [`data/categories.json`](data/categories.json) (mirrors the categories of the original Grok project). ✅ = full entry present; ⬜ = not yet ingested.

### Utility Lands (47/47)

✅ [Reliquary Tower](cards/R/re.md#reliquary-tower) · ✅ [Rogue's Passage](cards/R/ro.md#rogues-passage) · ✅ [Maze of Ith](cards/M/ma.md#maze-of-ith) · ✅ [Command Tower](cards/C/co.md#command-tower) · ✅ [Ancient Tomb](cards/A/an.md#ancient-tomb) · ✅ [Bojuka Bog](cards/B/bo.md#bojuka-bog) · ✅ [Homeward Path](cards/H/ho.md#homeward-path) · ✅ [Kor Haven](cards/K/ko.md#kor-haven) · ✅ [Gavony Township](cards/G/ga.md#gavony-township) · ✅ [Kessig Wolf Run](cards/K/ke.md#kessig-wolf-run) · ✅ [Field of the Dead](cards/F/fi.md#field-of-the-dead) · ✅ [Urza's Saga](cards/U/ur.md#urzas-saga) · ✅ [Academy Ruins](cards/A/ac.md#academy-ruins) · ✅ [Buried Ruin](cards/B/bu.md#buried-ruin) · ✅ [Inventors' Fair](cards/I/in.md#inventors-fair) · ✅ [Volrath's Stronghold](cards/V/vo.md#volraths-stronghold) · ✅ [Hall of Heliod's Generosity](cards/H/ha.md#hall-of-heliods-generosity) · ✅ [Myriad Landscape](cards/M/my.md#myriad-landscape) · ✅ [Thespian's Stage](cards/T/th.md#thespians-stage) · ✅ [Dark Depths](cards/D/da.md#dark-depths) · ✅ [Cabal Coffers](cards/C/ca.md#cabal-coffers) · ✅ [Urborg, Tomb of Yawgmoth](cards/U/ur.md#urborg-tomb-of-yawgmoth) · ✅ [Yavimaya, Cradle of Growth](cards/Y/ya.md#yavimaya-cradle-of-growth) · ✅ [Gaea's Cradle](cards/G/ga.md#gaeas-cradle) · ✅ [Nykthos, Shrine to Nyx](cards/N/ny.md#nykthos-shrine-to-nyx) · ✅ [Glacial Chasm](cards/G/gl.md#glacial-chasm) · ✅ [Mystifying Maze](cards/M/my.md#mystifying-maze) · ✅ [Karakas](cards/K/ka.md#karakas) · ✅ [Castle Ardenvale](cards/C/ca.md#castle-ardenvale) · ✅ [Castle Locthwain](cards/C/ca.md#castle-locthwain) · ✅ [Castle Embereth](cards/C/ca.md#castle-embereth) · ✅ [Castle Vantress](cards/C/ca.md#castle-vantress) · ✅ [Castle Garenbrig](cards/C/ca.md#castle-garenbrig) · ✅ [Otawara, Soaring City](cards/O/ot.md#otawara-soaring-city) · ✅ [Boseiju, Who Endures](cards/B/bo.md#boseiju-who-endures) · ✅ [Eiganjo, Seat of the Empire](cards/E/ei.md#eiganjo-seat-of-the-empire) · ✅ [Takenuma, Abandoned Mire](cards/T/ta.md#takenuma-abandoned-mire) · ✅ [Sokenzan, Crucible of Defiance](cards/S/so.md#sokenzan-crucible-of-defiance) · ✅ [War Room](cards/W/wa.md#war-room) · ✅ [Emeria, the Sky Ruin](cards/E/em.md#emeria-the-sky-ruin) · ✅ [Valakut, the Molten Pinnacle](cards/V/va.md#valakut-the-molten-pinnacle) · ✅ [Path of Ancestry](cards/P/pa.md#path-of-ancestry) · ✅ [Exotic Orchard](cards/E/ex.md#exotic-orchard) · ✅ [Scavenger Grounds](cards/S/sc.md#scavenger-grounds) · ✅ [High Market](cards/H/hi.md#high-market) · ✅ [Phyrexian Tower](cards/P/ph.md#phyrexian-tower) · ✅ [Temple of the False God](cards/T/te.md#temple-of-the-false-god)

### Land Destruction (28/28)

✅ [Strip Mine](cards/S/st.md#strip-mine) · ✅ [Wasteland](cards/W/wa.md#wasteland) · ✅ [Tectonic Edge](cards/T/te.md#tectonic-edge) · ✅ [Ghost Quarter](cards/G/gh.md#ghost-quarter) · ✅ [Field of Ruin](cards/F/fi.md#field-of-ruin) · ✅ [Demolition Field](cards/D/de.md#demolition-field) · ✅ [Dust Bowl](cards/D/du.md#dust-bowl) · ✅ [Encroaching Wastes](cards/E/en.md#encroaching-wastes) · ✅ [Armageddon](cards/A/ar.md#armageddon) · ✅ [Ravages of War](cards/R/ra.md#ravages-of-war) · ✅ [Ruination](cards/R/ru.md#ruination) · ✅ [Sinkhole](cards/S/si.md#sinkhole) · ✅ [Stone Rain](cards/S/st.md#stone-rain) · ✅ [Cataclysm](cards/C/ca.md#cataclysm) · ✅ [Jokulhaups](cards/J/jo.md#jokulhaups) · ✅ [Obliterate](cards/O/ob.md#obliterate) · ✅ [Decree of Annihilation](cards/D/de.md#decree-of-annihilation) · ✅ [Impending Disaster](cards/I/im.md#impending-disaster) · ✅ [Wildfire](cards/W/wi.md#wildfire) · ✅ [Destructive Flow](cards/D/de.md#destructive-flow) · ✅ [Boom // Bust](cards/B/bo.md#boom--bust) · ✅ [Mold Shambler](cards/M/mo.md#mold-shambler) · ✅ [Acidic Slime](cards/A/ac.md#acidic-slime) · ✅ [Sowing Salt](cards/S/so.md#sowing-salt) · ✅ [Avalanche Riders](cards/A/av.md#avalanche-riders) · ✅ [Fall of the Thran](cards/F/fa.md#fall-of-the-thran) · ✅ [Catastrophe](cards/C/ca.md#catastrophe) · ✅ [Winds of Abandon](cards/W/wi.md#winds-of-abandon)

### Counterspells (39/39)

✅ [Counterspell](cards/C/co.md#counterspell) · ✅ [Swan Song](cards/S/sw.md#swan-song) · ✅ [Force of Will](cards/F/fo.md#force-of-will) · ✅ [Mana Drain](cards/M/ma.md#mana-drain) · ✅ [Negate](cards/N/ne.md#negate) · ✅ [Dispel](cards/D/di.md#dispel) · ✅ [Spell Pierce](cards/S/sp.md#spell-pierce) · ✅ [Fierce Guardianship](cards/F/fi.md#fierce-guardianship) · ✅ [Pact of Negation](cards/P/pa.md#pact-of-negation) · ✅ [Flusterstorm](cards/F/fl.md#flusterstorm) · ✅ [An Offer You Can't Refuse](cards/A/an.md#an-offer-you-cant-refuse) · ✅ [Mental Misstep](cards/M/me.md#mental-misstep) · ✅ [Arcane Denial](cards/A/ar.md#arcane-denial) · ✅ [Dovin's Veto](cards/D/do.md#dovins-veto) · ✅ [Mana Leak](cards/M/ma.md#mana-leak) · ✅ [Cryptic Command](cards/C/cr.md#cryptic-command) · ✅ [Force of Negation](cards/F/fo.md#force-of-negation) · ✅ [Mindbreak Trap](cards/M/mi.md#mindbreak-trap) · ✅ [Stern Scolding](cards/S/st.md#stern-scolding) · ✅ [Stifle](cards/S/st.md#stifle) · ✅ [Miscalculation](cards/M/mi.md#miscalculation) · ✅ [Memory Lapse](cards/M/me.md#memory-lapse) · ✅ [Remand](cards/R/re.md#remand) · ✅ [Absorb](cards/A/ab.md#absorb) · ✅ [Lapse of Certainty](cards/L/la.md#lapse-of-certainty) · ✅ [Saw It Coming](cards/S/sa.md#saw-it-coming) · ✅ [Essence Scatter](cards/E/es.md#essence-scatter) · ✅ [Mystical Dispute](cards/M/my.md#mystical-dispute) · ✅ [Didn't Say Please](cards/D/di.md#didnt-say-please) · ✅ [Cancel](cards/C/ca.md#cancel) · ✅ [Delay](cards/D/de.md#delay) · ✅ [Disdainful Stroke](cards/D/di.md#disdainful-stroke) · ✅ [Rewind](cards/R/re.md#rewind) · ✅ [Supreme Will](cards/S/su.md#supreme-will) · ✅ [Muddle the Mixture](cards/M/mu.md#muddle-the-mixture) · ✅ [Tale's End](cards/T/ta.md#tales-end) · ✅ [Silumgar's Command](cards/S/si.md#silumgars-command) · ✅ [Hullbreacher](cards/H/hu.md#hullbreacher) · ✅ [Deflecting Swat](cards/D/de.md#deflecting-swat)

### Fast Mana & Rocks (20/20)

✅ [Sol Ring](cards/S/so.md#sol-ring) · ✅ [Arcane Signet](cards/A/ar.md#arcane-signet) · ✅ [Mana Crypt](cards/M/ma.md#mana-crypt) · ✅ [Mana Vault](cards/M/ma.md#mana-vault) · ✅ [Chrome Mox](cards/C/ch.md#chrome-mox) · ✅ [Mox Diamond](cards/M/mo.md#mox-diamond) · ✅ [Jeweled Lotus](cards/J/je.md#jeweled-lotus) · ✅ [Lotus Petal](cards/L/lo.md#lotus-petal) · ✅ [Fellwar Stone](cards/F/fe.md#fellwar-stone) · ✅ [Mind Stone](cards/M/mi.md#mind-stone) · ✅ [Thought Vessel](cards/T/th.md#thought-vessel) · ✅ [Talisman of Dominance](cards/T/ta.md#talisman-of-dominance) · ✅ [Dimir Signet](cards/D/di.md#dimir-signet) · ✅ [Commander's Sphere](cards/C/co.md#commanders-sphere) · ✅ [Grim Monolith](cards/G/gr.md#grim-monolith) · ✅ [Basalt Monolith](cards/B/ba.md#basalt-monolith) · ✅ [Dark Ritual](cards/D/da.md#dark-ritual) · ✅ [Simian Spirit Guide](cards/S/si.md#simian-spirit-guide) · ✅ [Mox Opal](cards/M/mo.md#mox-opal) · ✅ [Mox Amber](cards/M/mo.md#mox-amber)

### Removal & Board Wipes (28/28)

✅ [Swords to Plowshares](cards/S/sw.md#swords-to-plowshares) · ✅ [Path to Exile](cards/P/pa.md#path-to-exile) · ✅ [Chaos Warp](cards/C/ch.md#chaos-warp) · ✅ [Beast Within](cards/B/be.md#beast-within) · ✅ [Generous Gift](cards/G/ge.md#generous-gift) · ✅ [Anguished Unmaking](cards/A/an.md#anguished-unmaking) · ✅ [Assassin's Trophy](cards/A/as.md#assassins-trophy) · ✅ [Cyclonic Rift](cards/C/cy.md#cyclonic-rift) · ✅ [Wrath of God](cards/W/wr.md#wrath-of-god) · ✅ [Damnation](cards/D/da.md#damnation) · ✅ [Toxic Deluge](cards/T/to.md#toxic-deluge) · ✅ [Farewell](cards/F/fa.md#farewell) · ✅ [Blasphemous Act](cards/B/bl.md#blasphemous-act) · ✅ [Austere Command](cards/A/au.md#austere-command) · ✅ [Vandalblast](cards/V/va.md#vandalblast) · ✅ [Feed the Swarm](cards/F/fe.md#feed-the-swarm) · ✅ [Rapid Hybridization](cards/R/ra.md#rapid-hybridization) · ✅ [Pongify](cards/P/po.md#pongify) · ✅ [Nature's Claim](cards/N/na.md#natures-claim) · ✅ [Krosan Grip](cards/K/kr.md#krosan-grip) · ✅ [Deadly Rollick](cards/D/de.md#deadly-rollick) · ✅ [Infernal Grasp](cards/I/in.md#infernal-grasp) · ✅ [Vindicate](cards/V/vi.md#vindicate) · ✅ [Return to Dust](cards/R/re.md#return-to-dust) · ✅ [Evacuation](cards/E/ev.md#evacuation) · ✅ [Massacre Wurm](cards/M/ma.md#massacre-wurm) · ✅ [Supreme Verdict](cards/S/su.md#supreme-verdict) · ✅ [Sunfall](cards/S/su.md#sunfall)

### Tutors (22/22)

✅ [Demonic Tutor](cards/D/de.md#demonic-tutor) · ✅ [Vampiric Tutor](cards/V/va.md#vampiric-tutor) · ✅ [Enlightened Tutor](cards/E/en.md#enlightened-tutor) · ✅ [Mystical Tutor](cards/M/my.md#mystical-tutor) · ✅ [Worldly Tutor](cards/W/wo.md#worldly-tutor) · ✅ [Gamble](cards/G/ga.md#gamble) · ✅ [Diabolic Intent](cards/D/di.md#diabolic-intent) · ✅ [Imperial Seal](cards/I/im.md#imperial-seal) · ✅ [Grim Tutor](cards/G/gr.md#grim-tutor) · ✅ [Diabolic Tutor](cards/D/di.md#diabolic-tutor) · ✅ [Idyllic Tutor](cards/I/id.md#idyllic-tutor) · ✅ [Eladamri's Call](cards/E/el.md#eladamris-call) · ✅ [Finale of Devastation](cards/F/fi.md#finale-of-devastation) · ✅ [Green Sun's Zenith](cards/G/gr.md#green-suns-zenith) · ✅ [Chord of Calling](cards/C/ch.md#chord-of-calling) · ✅ [Natural Order](cards/N/na.md#natural-order) · ✅ [Survival of the Fittest](cards/S/su.md#survival-of-the-fittest) · ✅ [Fabricate](cards/F/fa.md#fabricate) · ✅ [Whir of Invention](cards/W/wh.md#whir-of-invention) · ✅ [Tainted Pact](cards/T/ta.md#tainted-pact) · ✅ [Personal Tutor](cards/P/pe.md#personal-tutor) · ✅ [Steelshaper's Gift](cards/S/st.md#steelshapers-gift)

### Card Advantage (23/23)

✅ [Rhystic Study](cards/R/rh.md#rhystic-study) · ✅ [Mystic Remora](cards/M/my.md#mystic-remora) · ✅ [Sylvan Library](cards/S/sy.md#sylvan-library) · ✅ [Phyrexian Arena](cards/P/ph.md#phyrexian-arena) · ✅ [Esper Sentinel](cards/E/es.md#esper-sentinel) · ✅ [Skullclamp](cards/S/sk.md#skullclamp) · ✅ [Necropotence](cards/N/ne.md#necropotence) · ✅ [The One Ring](cards/T/th.md#the-one-ring) · ✅ [Smothering Tithe](cards/S/sm.md#smothering-tithe) · ✅ [Harmonize](cards/H/ha.md#harmonize) · ✅ [Guardian Project](cards/G/gu.md#guardian-project) · ✅ [Beast Whisperer](cards/B/be.md#beast-whisperer) · ✅ [Night's Whisper](cards/N/ni.md#nights-whisper) · ✅ [Sign in Blood](cards/S/si.md#sign-in-blood) · ✅ [Brainstorm](cards/B/br.md#brainstorm) · ✅ [Ponder](cards/P/po.md#ponder) · ✅ [Preordain](cards/P/pr.md#preordain) · ✅ [Fact or Fiction](cards/F/fa.md#fact-or-fiction) · ✅ [Mulldrifter](cards/M/mu.md#mulldrifter) · ✅ [Jeska's Will](cards/J/je.md#jeskas-will) · ✅ [Wheel of Fortune](cards/W/wh.md#wheel-of-fortune) · ✅ [Windfall](cards/W/wi.md#windfall) · ✅ [Faithless Looting](cards/F/fa.md#faithless-looting)

### Protection (16/16)

✅ [Lightning Greaves](cards/L/li.md#lightning-greaves) · ✅ [Swiftfoot Boots](cards/S/sw.md#swiftfoot-boots) · ✅ [Heroic Intervention](cards/H/he.md#heroic-intervention) · ✅ [Teferi's Protection](cards/T/te.md#teferis-protection) · ✅ [Flawless Maneuver](cards/F/fl.md#flawless-maneuver) · ✅ [Boros Charm](cards/B/bo.md#boros-charm) · ✅ [Akroma's Will](cards/A/ak.md#akromas-will) · ✅ [Clever Concealment](cards/C/cl.md#clever-concealment) · ✅ [Mother of Runes](cards/M/mo.md#mother-of-runes) · ✅ [Giver of Runes](cards/G/gi.md#giver-of-runes) · ✅ [Darksteel Plate](cards/D/da.md#darksteel-plate) · ✅ [Whispersilk Cloak](cards/W/wh.md#whispersilk-cloak) · ✅ [Snakeskin Veil](cards/S/sn.md#snakeskin-veil) · ✅ [Tamiyo's Safekeeping](cards/T/ta.md#tamiyos-safekeeping) · ✅ [Blossoming Defense](cards/B/bl.md#blossoming-defense) · ✅ [Dauntless Bodyguard](cards/D/da.md#dauntless-bodyguard)

### Ramp (20/20)

✅ [Cultivate](cards/C/cu.md#cultivate) · ✅ [Kodama's Reach](cards/K/ko.md#kodamas-reach) · ✅ [Rampant Growth](cards/R/ra.md#rampant-growth) · ✅ [Farseek](cards/F/fa.md#farseek) · ✅ [Nature's Lore](cards/N/na.md#natures-lore) · ✅ [Three Visits](cards/T/th.md#three-visits) · ✅ [Skyshroud Claim](cards/S/sk.md#skyshroud-claim) · ✅ [Llanowar Elves](cards/L/ll.md#llanowar-elves) · ✅ [Elvish Mystic](cards/E/el.md#elvish-mystic) · ✅ [Birds of Paradise](cards/B/bi.md#birds-of-paradise) · ✅ [Sakura-Tribe Elder](cards/S/sa.md#sakura-tribe-elder) · ✅ [Wood Elves](cards/W/wo.md#wood-elves) · ✅ [Explore](cards/E/ex.md#explore) · ✅ [Exploration](cards/E/ex.md#exploration) · ✅ [Burgeoning](cards/B/bu.md#burgeoning) · ✅ [Dryad of the Ilysian Grove](cards/D/dr.md#dryad-of-the-ilysian-grove) · ✅ [Oracle of Mul Daya](cards/O/or.md#oracle-of-mul-daya) · ✅ [Azusa, Lost but Seeking](cards/A/az.md#azusa-lost-but-seeking) · ✅ [Lotus Cobra](cards/L/lo.md#lotus-cobra) · ✅ [Tireless Provisioner](cards/T/ti.md#tireless-provisioner)

## Game Changers ingested

Cards Scryfall flags as `game_changer` (used by the official Commander Brackets system). See [EDH Standards](EDH%20Standards.md).

[Ad Nauseam](cards/A/ad.md#ad-nauseam) · [Ancient Tomb](cards/A/an.md#ancient-tomb) · [Aura Shards](cards/A/au.md#aura-shards) · [Bolas's Citadel](cards/B/bo.md#bolass-citadel) · [Braids, Cabal Minion](cards/B/br.md#braids-cabal-minion) · [Chrome Mox](cards/C/ch.md#chrome-mox) · [Consecrated Sphinx](cards/C/co.md#consecrated-sphinx) · [Crop Rotation](cards/C/cr.md#crop-rotation) · [Cyclonic Rift](cards/C/cy.md#cyclonic-rift) · [Demonic Tutor](cards/D/de.md#demonic-tutor) · [Drannith Magistrate](cards/D/dr.md#drannith-magistrate) · [Enlightened Tutor](cards/E/en.md#enlightened-tutor) · [Farewell](cards/F/fa.md#farewell) · [Field of the Dead](cards/F/fi.md#field-of-the-dead) · [Fierce Guardianship](cards/F/fi.md#fierce-guardianship) · [Force of Will](cards/F/fo.md#force-of-will) · [Gaea's Cradle](cards/G/ga.md#gaeas-cradle) · [Gamble](cards/G/ga.md#gamble) · [Gifts Ungiven](cards/G/gi.md#gifts-ungiven) · [Glacial Chasm](cards/G/gl.md#glacial-chasm) · [Grand Arbiter Augustin IV](cards/G/gr.md#grand-arbiter-augustin-iv) · [Grim Monolith](cards/G/gr.md#grim-monolith) · [Imperial Seal](cards/I/im.md#imperial-seal) · [Intuition](cards/I/in.md#intuition) · [Jeska's Will](cards/J/je.md#jeskas-will) · [Lion's Eye Diamond](cards/L/li.md#lions-eye-diamond) · [Mana Vault](cards/M/ma.md#mana-vault) · [Mishra's Workshop](cards/M/mi.md#mishras-workshop) · [Mox Diamond](cards/M/mo.md#mox-diamond) · [Mystical Tutor](cards/M/my.md#mystical-tutor) · [Narset, Parter of Veils](cards/N/na.md#narset-parter-of-veils) · [Natural Order](cards/N/na.md#natural-order) · [Necropotence](cards/N/ne.md#necropotence) · [Notion Thief](cards/N/no.md#notion-thief) · [Opposition Agent](cards/O/op.md#opposition-agent) · [Orcish Bowmasters](cards/O/or.md#orcish-bowmasters) · [Rhystic Study](cards/R/rh.md#rhystic-study) · [Seedborn Muse](cards/S/se.md#seedborn-muse) · [Serra's Sanctum](cards/S/se.md#serras-sanctum) · [Smothering Tithe](cards/S/sm.md#smothering-tithe) · [Survival of the Fittest](cards/S/su.md#survival-of-the-fittest) · [Teferi's Protection](cards/T/te.md#teferis-protection) · [Tergrid, God of Fright // Tergrid's Lantern](cards/T/te.md#tergrid-god-of-fright--tergrids-lantern) · [Thassa's Oracle](cards/T/th.md#thassas-oracle) · [The One Ring](cards/T/th.md#the-one-ring) · [Underworld Breach](cards/U/un.md#underworld-breach) · [Vampiric Tutor](cards/V/va.md#vampiric-tutor) · [Worldly Tutor](cards/W/wo.md#worldly-tutor)

## Top 100 by EDHREC rank

| Rank | Card | Identity | Type |
|---|---|---|---|
| 1 | [Sol Ring](cards/S/so.md#sol-ring) | C | Artifact |
| 2 | [Command Tower](cards/C/co.md#command-tower) | C | Land |
| 3 | [Arcane Signet](cards/A/ar.md#arcane-signet) | C | Artifact |
| 9 | [Exotic Orchard](cards/E/ex.md#exotic-orchard) | C | Land |
| 10 | [Reliquary Tower](cards/R/re.md#reliquary-tower) | C | Land |
| 11 | [Swords to Plowshares](cards/S/sw.md#swords-to-plowshares) | W | Instant |
| 12 | [Swiftfoot Boots](cards/S/sw.md#swiftfoot-boots) | C | Artifact — Equipment |
| 13 | [Lightning Greaves](cards/L/li.md#lightning-greaves) | C | Artifact — Equipment |
| 14 | [Path of Ancestry](cards/P/pa.md#path-of-ancestry) | C | Land |
| 15 | [Path to Exile](cards/P/pa.md#path-to-exile) | W | Instant |
| 16 | [Counterspell](cards/C/co.md#counterspell) | U | Instant |
| 17 | [Fellwar Stone](cards/F/fe.md#fellwar-stone) | C | Artifact |
| 18 | [Rogue's Passage](cards/R/ro.md#rogues-passage) | C | Land |
| 19 | [Evolving Wilds](cards/E/ev.md#evolving-wilds) | C | Land |
| 20 | [Cultivate](cards/C/cu.md#cultivate) | G | Sorcery |
| 21 | [Thought Vessel](cards/T/th.md#thought-vessel) | C | Artifact |
| 22 | [Blasphemous Act](cards/B/bl.md#blasphemous-act) | R | Sorcery |
| 23 | [Farseek](cards/F/fa.md#farseek) | G | Sorcery |
| 24 | [Bojuka Bog](cards/B/bo.md#bojuka-bog) | B | Land |
| 25 | [Beast Within](cards/B/be.md#beast-within) | G | Instant |
| 26 | [Nature's Lore](cards/N/na.md#natures-lore) | G | Sorcery |
| 27 | [Rampant Growth](cards/R/ra.md#rampant-growth) | G | Sorcery |
| 28 | [Heroic Intervention](cards/H/he.md#heroic-intervention) | G | Instant |
| 29 | [Chaos Warp](cards/C/ch.md#chaos-warp) | R | Instant |
| 30 | [Terramorphic Expanse](cards/T/te.md#terramorphic-expanse) | C | Land |
| 31 | [Myriad Landscape](cards/M/my.md#myriad-landscape) | C | Land |
| 32 | [Mind Stone](cards/M/mi.md#mind-stone) | C | Artifact |
| 33 | [Dark Ritual](cards/D/da.md#dark-ritual) | B | Instant |
| 34 | [An Offer You Can't Refuse](cards/A/an.md#an-offer-you-cant-refuse) | U | Instant |
| 35 | [Birds of Paradise](cards/B/bi.md#birds-of-paradise) | G | Creature — Bird |
| 36 | [Polluted Delta](cards/P/po.md#polluted-delta) | C | Land |
| 37 | [Kodama's Reach](cards/K/ko.md#kodamas-reach) | G | Sorcery — Arcane |
| 38 | [Flooded Strand](cards/F/fl.md#flooded-strand) | C | Land |
| 39 | [Skullclamp](cards/S/sk.md#skullclamp) | C | Artifact — Equipment |
| 40 | [Three Visits](cards/T/th.md#three-visits) | G | Sorcery |
| 41 | [Solemn Simulacrum](cards/S/so.md#solemn-simulacrum) | C | Artifact Creature — Golem |
| 42 | [Misty Rainforest](cards/M/mi.md#misty-rainforest) | C | Land |
| 43 | [Bloodstained Mire](cards/B/bl.md#bloodstained-mire) | C | Land |
| 44 | [Fabled Passage](cards/F/fa.md#fabled-passage) | C | Land |
| 45 | [Windswept Heath](cards/W/wi.md#windswept-heath) | C | Land |
| 46 | [Rhystic Study](cards/R/rh.md#rhystic-study) | U | Enchantment |
| 47 | [Wooded Foothills](cards/W/wo.md#wooded-foothills) | C | Land |
| 48 | [Verdant Catacombs](cards/V/ve.md#verdant-catacombs) | C | Land |
| 49 | [Scalding Tarn](cards/S/sc.md#scalding-tarn) | C | Land |
| 50 | [Watery Grave](cards/W/wa.md#watery-grave) | BU | Land — Island Swamp |
| 51 | [Marsh Flats](cards/M/ma.md#marsh-flats) | C | Land |
| 52 | [Arcane Denial](cards/A/ar.md#arcane-denial) | U | Instant |
| 53 | [Reanimate](cards/R/re.md#reanimate) | B | Sorcery |
| 54 | [Commander's Sphere](cards/C/co.md#commanders-sphere) | C | Artifact |
| 55 | [Arid Mesa](cards/A/ar.md#arid-mesa) | C | Land |
| 56 | [Llanowar Elves](cards/L/ll.md#llanowar-elves) | G | Creature — Elf Druid |
| 57 | [Negate](cards/N/ne.md#negate) | U | Instant |
| 58 | [Cyclonic Rift](cards/C/cy.md#cyclonic-rift) | U | Instant |
| 59 | [Godless Shrine](cards/G/go.md#godless-shrine) | BW | Land — Plains Swamp |
| 60 | [Breeding Pool](cards/B/br.md#breeding-pool) | GU | Land — Forest Island |
| 61 | [Hallowed Fountain](cards/H/ha.md#hallowed-fountain) | UW | Land — Plains Island |
| 62 | [Steam Vents](cards/S/st.md#steam-vents) | RU | Land — Island Mountain |
| 63 | [Generous Gift](cards/G/ge.md#generous-gift) | W | Instant |
| 64 | [Demonic Tutor](cards/D/de.md#demonic-tutor) | B | Sorcery |
| 65 | [Toxic Deluge](cards/T/to.md#toxic-deluge) | B | Sorcery |
| 66 | [Swan Song](cards/S/sw.md#swan-song) | U | Instant |
| 67 | [Smothering Tithe](cards/S/sm.md#smothering-tithe) | W | Enchantment |
| 68 | [Blood Crypt](cards/B/bl.md#blood-crypt) | BR | Land — Swamp Mountain |
| 69 | [Ancient Tomb](cards/A/an.md#ancient-tomb) | C | Land |
| 70 | [Stomping Ground](cards/S/st.md#stomping-ground) | GR | Land — Mountain Forest |
| 71 | [Overgrown Tomb](cards/O/ov.md#overgrown-tomb) | BG | Land — Swamp Forest |
| 72 | [Brainstorm](cards/B/br.md#brainstorm) | U | Instant |
| 73 | [Sacred Foundry](cards/S/sa.md#sacred-foundry) | RW | Land — Mountain Plains |
| 74 | [Deflecting Swat](cards/D/de.md#deflecting-swat) | R | Instant |
| 75 | [Urborg, Tomb of Yawgmoth](cards/U/ur.md#urborg-tomb-of-yawgmoth) | C | Legendary Land |
| 76 | [Sulfur Falls](cards/S/su.md#sulfur-falls) | RU | Land |
| 77 | [Boseiju, Who Endures](cards/B/bo.md#boseiju-who-endures) | G | Legendary Land |
| 78 | [Clifftop Retreat](cards/C/cl.md#clifftop-retreat) | RW | Land |
| 79 | [Yavimaya, Cradle of Growth](cards/Y/ya.md#yavimaya-cradle-of-growth) | C | Legendary Land |
| 80 | [Esper Sentinel](cards/E/es.md#esper-sentinel) | W | Artifact Creature — Human Soldier |
| 81 | [Temple Garden](cards/T/te.md#temple-garden) | GW | Land — Forest Plains |
| 82 | [Fierce Guardianship](cards/F/fi.md#fierce-guardianship) | U | Instant |
| 83 | [Dragonskull Summit](cards/D/dr.md#dragonskull-summit) | BR | Land |
| 84 | [Temple of the False God](cards/T/te.md#temple-of-the-false-god) | C | Land |
| 85 | [Chromatic Lantern](cards/C/ch.md#chromatic-lantern) | C | Artifact |
| 86 | [Sunken Hollow](cards/S/su.md#sunken-hollow) | BU | Land — Island Swamp |
| 87 | [Cinder Glade](cards/C/ci.md#cinder-glade) | GR | Land — Mountain Forest |
| 88 | [Glacial Fortress](cards/G/gl.md#glacial-fortress) | UW | Land |
| 89 | [Otawara, Soaring City](cards/O/ot.md#otawara-soaring-city) | U | Legendary Land |
| 90 | [Isolated Chapel](cards/I/is.md#isolated-chapel) | BW | Land |
| 91 | [Garruk's Uprising](cards/G/ga.md#garruks-uprising) | G | Enchantment |
| 92 | [Talisman of Dominance](cards/T/ta.md#talisman-of-dominance) | BU | Artifact |
| 93 | [Feed the Swarm](cards/F/fe.md#feed-the-swarm) | B | Sorcery |
| 94 | [City of Brass](cards/C/ci.md#city-of-brass) | C | Land |
| 95 | [Smoldering Marsh](cards/S/sm.md#smoldering-marsh) | BR | Land — Swamp Mountain |
| 96 | [The One Ring](cards/T/th.md#the-one-ring) | C | Legendary Artifact |
| 97 | [Hinterland Harbor](cards/H/hi.md#hinterland-harbor) | GU | Land |
| 98 | [Frantic Search](cards/F/fr.md#frantic-search) | U | Instant |
| 99 | [Faithless Looting](cards/F/fa.md#faithless-looting) | R | Sorcery |
| 100 | [Vandalblast](cards/V/va.md#vandalblast) | R | Sorcery |
| 101 | [Mystic Remora](cards/M/my.md#mystic-remora) | U | Enchantment |
| 102 | [Elvish Mystic](cards/E/el.md#elvish-mystic) | G | Creature — Elf Druid |
| 103 | [Prairie Stream](cards/P/pr.md#prairie-stream) | UW | Land — Plains Island |
| 104 | [Phyrexian Arena](cards/P/ph.md#phyrexian-arena) | B | Enchantment |
| 105 | [Drowned Catacomb](cards/D/dr.md#drowned-catacomb) | BU | Land |

## How to find a card

1. Strip accents and punctuation from the name, take the first two letters → `cards/<FIRST>/<first two>.md` (names starting with a digit live in `cards/0-9/0-9.md`).
2. Or search [`data/card_index.csv`](data/card_index.csv) (columns: name, oracle_id, shard, anchor, edhrec_rank, color_identity, type_line, commander_legality, game_changer, batch).
