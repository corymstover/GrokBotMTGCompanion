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
| Cards with full entries | **33,894** |
| Target universe (paper cards, Scryfall Oracle) | 33,894 (100.0% complete) |
| EDHREC-rank coverage (all Commander-legal cards ranked ≤ N ingested) | N = 32,351 |
| Commander legality of ingested | banned: 83, legal: 32,116, not_legal: 1,695 |
| Game Changers ingested | 53 |
| Rulings ingested (Scryfall `rulings` bulk) | 2,604 rulings on 686 cards · 1,000/33,894 cards processed · 19,889 ingested cards have rulings on Scryfall |
| Shard files | 684 |
| Scryfall bulk data timestamp | 2026-10-15T09:02:01.217+00:00 |

### By color identity

| Identity | Cards |
|---|---|
| C | 3,129 |
| B | 4,996 |
| G | 4,878 |
| R | 5,014 |
| U | 4,934 |
| W | 5,061 |
| BG | 452 |
| BR | 519 |
| BU | 499 |
| BW | 445 |
| GR | 472 |
| GU | 457 |
| GW | 479 |
| RU | 460 |
| RW | 478 |
| UW | 506 |
| BGR | 95 |
| BGU | 78 |
| BGW | 62 |
| BRU | 122 |
| BRW | 76 |
| BUW | 104 |
| GRU | 74 |
| GRW | 115 |
| GUW | 101 |
| RUW | 97 |
| BGRU | 3 |
| BGRW | 2 |
| BGUW | 4 |
| BRUW | 4 |
| GRUW | 14 |
| BGRUW | 164 |

## Shards by letter

Cards are stored in `cards/<LETTER>/<prefix>.md` (accents stripped, punctuation ignored; 2-letter prefix, deepened to 3–5 letters where the full universe would exceed 350 cards in one file).

| Letter | Cards | Shard files |
|---|---|---|
| 0-9 | 4 | [0-9](cards/0-9/0-9.md) |
| A | 1,944 | [aa](cards/A/aa.md), [ab](cards/A/ab.md), [ac](cards/A/ac.md), [ad](cards/A/ad.md), [ae](cards/A/ae.md), [af](cards/A/af.md), [ag](cards/A/ag.md), [ah](cards/A/ah.md), [ai](cards/A/ai.md), [aj](cards/A/aj.md), [ak](cards/A/ak.md), [al](cards/A/al.md), [am](cards/A/am.md), [an](cards/A/an.md), [ao](cards/A/ao.md), [ap](cards/A/ap.md), [aq](cards/A/aq.md), [ara](cards/A/ara.md), [arb](cards/A/arb.md), [arc](cards/A/arc.md), [ard](cards/A/ard.md), [are](cards/A/are.md), [arg](cards/A/arg.md), [ari](cards/A/ari.md), [arj](cards/A/arj.md), [ark](cards/A/ark.md), [arl](cards/A/arl.md), [arm](cards/A/arm.md), [arn](cards/A/arn.md), [aro](cards/A/aro.md), [arr](cards/A/arr.md), [ars](cards/A/ars.md), [art](cards/A/art.md), [arv](cards/A/arv.md), [arw](cards/A/arw.md), [ary](cards/A/ary.md), [arz](cards/A/arz.md), [as](cards/A/as.md), [at](cards/A/at.md), [au](cards/A/au.md), [av](cards/A/av.md), [aw](cards/A/aw.md), [ax](cards/A/ax.md), [ay](cards/A/ay.md), [az](cards/A/az.md) |
| B | 1,937 | [baa](cards/B/baa.md), [bab](cards/B/bab.md), [bac](cards/B/bac.md), [bad](cards/B/bad.md), [bae](cards/B/bae.md), [baf](cards/B/baf.md), [bag](cards/B/bag.md), [bai](cards/B/bai.md), [bak](cards/B/bak.md), [bal](cards/B/bal.md), [bam](cards/B/bam.md), [ban](cards/B/ban.md), [bar](cards/B/bar.md), [bas](cards/B/bas.md), [bat](cards/B/bat.md), [bax](cards/B/bax.md), [bay](cards/B/bay.md), [baz](cards/B/baz.md), [be](cards/B/be.md), [bf](cards/B/bf.md), [bh](cards/B/bh.md), [bi](cards/B/bi.md), [bj](cards/B/bj.md), [bla](cards/B/bla.md), [ble](cards/B/ble.md), [bli](cards/B/bli.md), [blo](cards/B/blo.md), [blu](cards/B/blu.md), [bo](cards/B/bo.md), [br](cards/B/br.md), [bu](cards/B/bu.md), [by](cards/B/by.md) |
| C | 2,355 | [cab](cards/C/cab.md), [cac](cards/C/cac.md), [cad](cards/C/cad.md), [cae](cards/C/cae.md), [cag](cards/C/cag.md), [cai](cards/C/cai.md), [cal](cards/C/cal.md), [cam](cards/C/cam.md), [can](cards/C/can.md), [cao](cards/C/cao.md), [cap](cards/C/cap.md), [car](cards/C/car.md), [cas](cards/C/cas.md), [cat](cards/C/cat.md), [cau](cards/C/cau.md), [cav](cards/C/cav.md), [cay](cards/C/cay.md), [caz](cards/C/caz.md), [ce](cards/C/ce.md), [cg](cards/C/cg.md), [cha](cards/C/cha.md), [che](cards/C/che.md), [chi](cards/C/chi.md), [chl](cards/C/chl.md), [cho](cards/C/cho.md), [chr](cards/C/chr.md), [cht](cards/C/cht.md), [chu](cards/C/chu.md), [ci](cards/C/ci.md), [cl](cards/C/cl.md), [coa](cards/C/coa.md), [cob](cards/C/cob.md), [coc](cards/C/coc.md), [cod](cards/C/cod.md), [coe](cards/C/coe.md), [cof](cards/C/cof.md), [cog](cards/C/cog.md), [coi](cards/C/coi.md), [col](cards/C/col.md), [com](cards/C/com.md), [con](cards/C/con.md), [coo](cards/C/coo.md), [cop](cards/C/cop.md), [cor](cards/C/cor.md), [cos](cards/C/cos.md), [cou](cards/C/cou.md), [cov](cards/C/cov.md), [cow](cards/C/cow.md), [cr](cards/C/cr.md), [cu](cards/C/cu.md), [cy](cards/C/cy.md) |
| D | 1,905 | [d0](cards/D/d0.md), [da](cards/D/da.md), [dea](cards/D/dea.md), [deb](cards/D/deb.md), [dec](cards/D/dec.md), [ded](cards/D/ded.md), [dee](cards/D/dee.md), [def](cards/D/def.md), [deg](cards/D/deg.md), [deh](cards/D/deh.md), [dei](cards/D/dei.md), [dej](cards/D/dej.md), [del](cards/D/del.md), [dem](cards/D/dem.md), [den](cards/D/den.md), [dep](cards/D/dep.md), [der](cards/D/der.md), [des](cards/D/des.md), [det](cards/D/det.md), [deu](cards/D/deu.md), [dev](cards/D/dev.md), [dew](cards/D/dew.md), [dh](cards/D/dh.md), [di](cards/D/di.md), [dj](cards/D/dj.md), [do](cards/D/do.md), [dra](cards/D/dra.md), [drb](cards/D/drb.md), [dre](cards/D/dre.md), [dri](cards/D/dri.md), [drj](cards/D/drj.md), [drm](cards/D/drm.md), [dro](cards/D/dro.md), [dru](cards/D/dru.md), [dry](cards/D/dry.md), [du](cards/D/du.md), [dw](cards/D/dw.md), [dy](cards/D/dy.md) |
| E | 1,206 | [ea](cards/E/ea.md), [eb](cards/E/eb.md), [ec](cards/E/ec.md), [ed](cards/E/ed.md), [ee](cards/E/ee.md), [ef](cards/E/ef.md), [eg](cards/E/eg.md), [ei](cards/E/ei.md), [ej](cards/E/ej.md), [ek](cards/E/ek.md), [el](cards/E/el.md), [em](cards/E/em.md), [en](cards/E/en.md), [eo](cards/E/eo.md), [ep](cards/E/ep.md), [eq](cards/E/eq.md), [er](cards/E/er.md), [es](cards/E/es.md), [et](cards/E/et.md), [eu](cards/E/eu.md), [ev](cards/E/ev.md), [ex](cards/E/ex.md), [ey](cards/E/ey.md), [ez](cards/E/ez.md) |
| F | 1,496 | [fa](cards/F/fa.md), [fb](cards/F/fb.md), [fe](cards/F/fe.md), [fi](cards/F/fi.md), [fl](cards/F/fl.md), [fo](cards/F/fo.md), [fr](cards/F/fr.md), [fu](cards/F/fu.md), [fy](cards/F/fy.md) |
| G | 1,780 | [ga](cards/G/ga.md), [ge](cards/G/ge.md), [gh](cards/G/gh.md), [gi](cards/G/gi.md), [gl](cards/G/gl.md), [gn](cards/G/gn.md), [goa](cards/G/goa.md), [gob](cards/G/gob.md), [god](cards/G/god.md), [gof](cards/G/gof.md), [gog](cards/G/gog.md), [goh](cards/G/goh.md), [gol](cards/G/gol.md), [gom](cards/G/gom.md), [gon](cards/G/gon.md), [goo](cards/G/goo.md), [gor](cards/G/gor.md), [gos](cards/G/gos.md), [got](cards/G/got.md), [gou](cards/G/gou.md), [gov](cards/G/gov.md), [gra](cards/G/gra.md), [gre](cards/G/gre.md), [gri](cards/G/gri.md), [gro](cards/G/gro.md), [gru](cards/G/gru.md), [gry](cards/G/gry.md), [gu](cards/G/gu.md), [gw](cards/G/gw.md), [gy](cards/G/gy.md) |
| H | 1,212 | [ha](cards/H/ha.md), [he](cards/H/he.md), [hi](cards/H/hi.md), [ho](cards/H/ho.md), [hr](cards/H/hr.md), [ht](cards/H/ht.md), [hu](cards/H/hu.md), [hy](cards/H/hy.md) |
| I | 904 | [ia](cards/I/ia.md), [ib](cards/I/ib.md), [ic](cards/I/ic.md), [id](cards/I/id.md), [if](cards/I/if.md), [ig](cards/I/ig.md), [ih](cards/I/ih.md), [ii](cards/I/ii.md), [ik](cards/I/ik.md), [il](cards/I/il.md), [im](cards/I/im.md), [ina](cards/I/ina.md), [inb](cards/I/inb.md), [inc](cards/I/inc.md), [ind](cards/I/ind.md), [ine](cards/I/ine.md), [inf](cards/I/inf.md), [ing](cards/I/ing.md), [inh](cards/I/inh.md), [ini](cards/I/ini.md), [inj](cards/I/inj.md), [ink](cards/I/ink.md), [inn](cards/I/inn.md), [ino](cards/I/ino.md), [inq](cards/I/inq.md), [inr](cards/I/inr.md), [ins](cards/I/ins.md), [int](cards/I/int.md), [inu](cards/I/inu.md), [inv](cards/I/inv.md), [inz](cards/I/inz.md), [io](cards/I/io.md), [ip](cards/I/ip.md), [ir](cards/I/ir.md), [is](cards/I/is.md), [it](cards/I/it.md), [iv](cards/I/iv.md), [iw](cards/I/iw.md), [ix](cards/I/ix.md), [iy](cards/I/iy.md), [iz](cards/I/iz.md) |
| J | 385 | [ja](cards/J/ja.md), [je](cards/J/je.md), [jh](cards/J/jh.md), [ji](cards/J/ji.md), [jj](cards/J/jj.md), [jo](cards/J/jo.md), [ju](cards/J/ju.md), [jw](cards/J/jw.md), [jy](cards/J/jy.md) |
| K | 901 | [k9](cards/K/k9.md), [ka](cards/K/ka.md), [ke](cards/K/ke.md), [kh](cards/K/kh.md), [ki](cards/K/ki.md), [kj](cards/K/kj.md), [kl](cards/K/kl.md), [kn](cards/K/kn.md), [ko](cards/K/ko.md), [kr](cards/K/kr.md), [ku](cards/K/ku.md), [kw](cards/K/kw.md), [ky](cards/K/ky.md) |
| L | 1,047 | [la](cards/L/la.md), [le](cards/L/le.md), [lh](cards/L/lh.md), [li](cards/L/li.md), [ll](cards/L/ll.md), [lo](cards/L/lo.md), [lu](cards/L/lu.md), [ly](cards/L/ly.md) |
| M | 1,983 | [maa](cards/M/maa.md), [mab](cards/M/mab.md), [mac](cards/M/mac.md), [mad](cards/M/mad.md), [mae](cards/M/mae.md), [mag](cards/M/mag.md), [mah](cards/M/mah.md), [mai](cards/M/mai.md), [maj](cards/M/maj.md), [mak](cards/M/mak.md), [mal](cards/M/mal.md), [mam](cards/M/mam.md), [man](cards/M/man.md), [map](cards/M/map.md), [mar](cards/M/mar.md), [mas](cards/M/mas.md), [mat](cards/M/mat.md), [mau](cards/M/mau.md), [mav](cards/M/mav.md), [maw](cards/M/maw.md), [max](cards/M/max.md), [may](cards/M/may.md), [maz](cards/M/maz.md), [mb](cards/M/mb.md), [me](cards/M/me.md), [mia](cards/M/mia.md), [mic](cards/M/mic.md), [mid](cards/M/mid.md), [mig](cards/M/mig.md), [mii](cards/M/mii.md), [mij](cards/M/mij.md), [mik](cards/M/mik.md), [mil](cards/M/mil.md), [mim](cards/M/mim.md), [min](cards/M/min.md), [mir](cards/M/mir.md), [mis](cards/M/mis.md), [mit](cards/M/mit.md), [miz](cards/M/miz.md), [mj](cards/M/mj.md), [mm](cards/M/mm.md), [mn](cards/M/mn.md), [moa](cards/M/moa.md), [mob](cards/M/mob.md), [moc](cards/M/moc.md), [mod](cards/M/mod.md), [mog](cards/M/mog.md), [moi](cards/M/moi.md), [mok](cards/M/mok.md), [mol](cards/M/mol.md), [mom](cards/M/mom.md), [mon](cards/M/mon.md), [moo](cards/M/moo.md), [mor](cards/M/mor.md), [mos](cards/M/mos.md), [mot](cards/M/mot.md), [mou](cards/M/mou.md), [mow](cards/M/mow.md), [mox](cards/M/mox.md), [mr](cards/M/mr.md), [ms](cards/M/ms.md), [mt](cards/M/mt.md), [mu](cards/M/mu.md), [mw](cards/M/mw.md), [my](cards/M/my.md), [mz](cards/M/mz.md) |
| N | 760 | [na](cards/N/na.md), [ne](cards/N/ne.md), [ni](cards/N/ni.md), [no](cards/N/no.md), [nu](cards/N/nu.md), [ny](cards/N/ny.md) |
| O | 696 | [oa](cards/O/oa.md), [ob](cards/O/ob.md), [oc](cards/O/oc.md), [od](cards/O/od.md), [of](cards/O/of.md), [og](cards/O/og.md), [oh](cards/O/oh.md), [oi](cards/O/oi.md), [oj](cards/O/oj.md), [ok](cards/O/ok.md), [ol](cards/O/ol.md), [om](cards/O/om.md), [on](cards/O/on.md), [oo](cards/O/oo.md), [op](cards/O/op.md), [or](cards/O/or.md), [os](cards/O/os.md), [ot](cards/O/ot.md), [ou](cards/O/ou.md), [ov](cards/O/ov.md), [ow](cards/O/ow.md), [ox](cards/O/ox.md), [oy](cards/O/oy.md), [oz](cards/O/oz.md) |
| P | 1,520 | [pa](cards/P/pa.md), [pe](cards/P/pe.md), [ph](cards/P/ph.md), [pi](cards/P/pi.md), [pl](cards/P/pl.md), [po](cards/P/po.md), [pr](cards/P/pr.md), [ps](cards/P/ps.md), [pt](cards/P/pt.md), [pu](cards/P/pu.md), [py](cards/P/py.md) |
| Q | 137 | [qa](cards/Q/qa.md), [qi](cards/Q/qi.md), [qu](cards/Q/qu.md) |
| R | 1,841 | [rab](cards/R/rab.md), [rac](cards/R/rac.md), [rad](cards/R/rad.md), [raf](cards/R/raf.md), [rag](cards/R/rag.md), [rai](cards/R/rai.md), [rak](cards/R/rak.md), [ral](cards/R/ral.md), [ram](cards/R/ram.md), [ran](cards/R/ran.md), [rap](cards/R/rap.md), [rar](cards/R/rar.md), [ras](cards/R/ras.md), [rat](cards/R/rat.md), [rau](cards/R/rau.md), [rav](cards/R/rav.md), [ray](cards/R/ray.md), [raz](cards/R/raz.md), [rd](cards/R/rd.md), [rea](cards/R/rea.md), [reb](cards/R/reb.md), [rec](cards/R/rec.md), [red](cards/R/red.md), [ree](cards/R/ree.md), [ref](cards/R/ref.md), [reg](cards/R/reg.md), [reh](cards/R/reh.md), [rei](cards/R/rei.md), [rej](cards/R/rej.md), [rek](cards/R/rek.md), [rel](cards/R/rel.md), [rem](cards/R/rem.md), [ren](cards/R/ren.md), [rep](cards/R/rep.md), [req](cards/R/req.md), [rer](cards/R/rer.md), [res](cards/R/res.md), [ret](cards/R/ret.md), [reu](cards/R/reu.md), [rev](cards/R/rev.md), [rew](cards/R/rew.md), [rex](cards/R/rex.md), [rey](cards/R/rey.md), [rh](cards/R/rh.md), [ri](cards/R/ri.md), [rm](cards/R/rm.md), [ro](cards/R/ro.md), [ru](cards/R/ru.md), [ry](cards/R/ry.md) |
| S | 4,488 | [saa](cards/S/saa.md), [sab](cards/S/sab.md), [sac](cards/S/sac.md), [sad](cards/S/sad.md), [saf](cards/S/saf.md), [sag](cards/S/sag.md), [sah](cards/S/sah.md), [sai](cards/S/sai.md), [sak](cards/S/sak.md), [sal](cards/S/sal.md), [sam](cards/S/sam.md), [san](cards/S/san.md), [sap](cards/S/sap.md), [sar](cards/S/sar.md), [sas](cards/S/sas.md), [sat](cards/S/sat.md), [sau](cards/S/sau.md), [sav](cards/S/sav.md), [saw](cards/S/saw.md), [say](cards/S/say.md), [saz](cards/S/saz.md), [sc](cards/S/sc.md), [sea](cards/S/sea.md), [sec](cards/S/sec.md), [sed](cards/S/sed.md), [see](cards/S/see.md), [sef](cards/S/sef.md), [seg](cards/S/seg.md), [seh](cards/S/seh.md), [sei](cards/S/sei.md), [sej](cards/S/sej.md), [sek](cards/S/sek.md), [sel](cards/S/sel.md), [sem](cards/S/sem.md), [sen](cards/S/sen.md), [sep](cards/S/sep.md), [seq](cards/S/seq.md), [ser](cards/S/ser.md), [ses](cards/S/ses.md), [set](cards/S/set.md), [sev](cards/S/sev.md), [sew](cards/S/sew.md), [sex](cards/S/sex.md), [sey](cards/S/sey.md), [sha](cards/S/sha.md), [she](cards/S/she.md), [shi](cards/S/shi.md), [sho](cards/S/sho.md), [shr](cards/S/shr.md), [shu](cards/S/shu.md), [shy](cards/S/shy.md), [si](cards/S/si.md), [sk](cards/S/sk.md), [sl](cards/S/sl.md), [sm](cards/S/sm.md), [sn](cards/S/sn.md), [so](cards/S/so.md), [spa](cards/S/spa.md), [spd](cards/S/spd.md), [spe](cards/S/spe.md), [sph](cards/S/sph.md), [spi](cards/S/spi.md), [spl](cards/S/spl.md), [spo](cards/S/spo.md), [spr](cards/S/spr.md), [spu](cards/S/spu.md), [spy](cards/S/spy.md), [sq](cards/S/sq.md), [sr](cards/S/sr.md), [sta](cards/S/sta.md), [ste](cards/S/ste.md), [sti](cards/S/sti.md), [sto](cards/S/sto.md), [str](cards/S/str.md), [stu](cards/S/stu.md), [sty](cards/S/sty.md), [sub](cards/S/sub.md), [suc](cards/S/suc.md), [sud](cards/S/sud.md), [sue](cards/S/sue.md), [suf](cards/S/suf.md), [sug](cards/S/sug.md), [sui](cards/S/sui.md), [suk](cards/S/suk.md), [sul](cards/S/sul.md), [sum](cards/S/sum.md), [sun](cards/S/sun.md), [sup](cards/S/sup.md), [suq](cards/S/suq.md), [sur](cards/S/sur.md), [sus](cards/S/sus.md), [sut](cards/S/sut.md), [sv](cards/S/sv.md), [sw](cards/S/sw.md), [sy](cards/S/sy.md), [sz](cards/S/sz.md) |
| T | 2,467 | [t4](cards/T/t4.md), [ta](cards/T/ta.md), [tc](cards/T/tc.md), [te](cards/T/te.md), [tha](cards/T/tha.md), [thea](cards/T/thea.md), [theb](cards/T/theb.md), [thec](cards/T/thec.md), [thed](cards/T/thed.md), [thee](cards/T/thee.md), [thef](cards/T/thef.md), [theg](cards/T/theg.md), [theh](cards/T/theh.md), [thei](cards/T/thei.md), [thej](cards/T/thej.md), [thek](cards/T/thek.md), [thel](cards/T/thel.md), [them](cards/T/them.md), [then](cards/T/then.md), [theo](cards/T/theo.md), [thep](cards/T/thep.md), [theq](cards/T/theq.md), [ther](cards/T/ther.md), [thes](cards/T/thes.md), [thet](cards/T/thet.md), [theu](cards/T/theu.md), [thev](cards/T/thev.md), [thew](cards/T/thew.md), [they](cards/T/they.md), [thez](cards/T/thez.md), [thi](cards/T/thi.md), [tho](cards/T/tho.md), [thr](cards/T/thr.md), [thu](cards/T/thu.md), [thw](cards/T/thw.md), [ti](cards/T/ti.md), [tl](cards/T/tl.md), [to](cards/T/to.md), [tp](cards/T/tp.md), [tra](cards/T/tra.md), [tre](cards/T/tre.md), [tri](cards/T/tri.md), [tro](cards/T/tro.md), [tru](cards/T/tru.md), [try](cards/T/try.md), [ts](cards/T/ts.md), [tu](cards/T/tu.md), [tv](cards/T/tv.md), [tw](cards/T/tw.md), [ty](cards/T/ty.md), [tz](cards/T/tz.md) |
| U | 476 | [ub](cards/U/ub.md), [uc](cards/U/uc.md), [ug](cards/U/ug.md), [uh](cards/U/uh.md), [uk](cards/U/uk.md), [ul](cards/U/ul.md), [um](cards/U/um.md), [un](cards/U/un.md), [up](cards/U/up.md), [ur](cards/U/ur.md), [us](cards/U/us.md), [ut](cards/U/ut.md), [uu](cards/U/uu.md), [uv](cards/U/uv.md), [uy](cards/U/uy.md) |
| V | 877 | [va](cards/V/va.md), [ve](cards/V/ve.md), [vg](cards/V/vg.md), [vh](cards/V/vh.md), [vi](cards/V/vi.md), [vn](cards/V/vn.md), [vo](cards/V/vo.md), [vr](cards/V/vr.md), [vu](cards/V/vu.md) |
| W | 1,190 | [wai](cards/W/wai.md), [wak](cards/W/wak.md), [wal](cards/W/wal.md), [wan](cards/W/wan.md), [war](cards/W/war.md), [was](cards/W/was.md), [wat](cards/W/wat.md), [wav](cards/W/wav.md), [wax](cards/W/wax.md), [way](cards/W/way.md), [we](cards/W/we.md), [wh](cards/W/wh.md), [wi](cards/W/wi.md), [wk](cards/W/wk.md), [wo](cards/W/wo.md), [wr](cards/W/wr.md), [wu](cards/W/wu.md), [wy](cards/W/wy.md) |
| X | 35 | [x2](cards/X/x2.md), [x_](cards/X/x_.md), [xa](cards/X/xa.md), [xe](cards/X/xe.md), [xi](cards/X/xi.md), [xm](cards/X/xm.md), [xo](cards/X/xo.md), [xu](cards/X/xu.md), [xy](cards/X/xy.md) |
| Y | 151 | [ya](cards/Y/ya.md), [yd](cards/Y/yd.md), [ye](cards/Y/ye.md), [yg](cards/Y/yg.md), [yi](cards/Y/yi.md), [yo](cards/Y/yo.md), [ys](cards/Y/ys.md), [yu](cards/Y/yu.md) |
| Z | 195 | [za](cards/Z/za.md), [ze](cards/Z/ze.md), [zh](cards/Z/zh.md), [zi](cards/Z/zi.md), [zn](cards/Z/zn.md), [zo](cards/Z/zo.md), [zu](cards/Z/zu.md), [zy](cards/Z/zy.md), [zz](cards/Z/zz.md) |
| _ | 2 | [__](cards/_/__.md) |

## Category trackers

Curated in [`data/categories.json`](data/categories.json) (mirrors the categories of the original Grok project). ✅ = full entry present; ⬜ = not yet ingested.

### Utility Lands (47/47)

✅ [Reliquary Tower](cards/R/rel.md#reliquary-tower) · ✅ [Rogue's Passage](cards/R/ro.md#rogues-passage) · ✅ [Maze of Ith](cards/M/maz.md#maze-of-ith) · ✅ [Command Tower](cards/C/com.md#command-tower) · ✅ [Ancient Tomb](cards/A/an.md#ancient-tomb) · ✅ [Bojuka Bog](cards/B/bo.md#bojuka-bog) · ✅ [Homeward Path](cards/H/ho.md#homeward-path) · ✅ [Kor Haven](cards/K/ko.md#kor-haven) · ✅ [Gavony Township](cards/G/ga.md#gavony-township) · ✅ [Kessig Wolf Run](cards/K/ke.md#kessig-wolf-run) · ✅ [Field of the Dead](cards/F/fi.md#field-of-the-dead) · ✅ [Urza's Saga](cards/U/ur.md#urzas-saga) · ✅ [Academy Ruins](cards/A/ac.md#academy-ruins) · ✅ [Buried Ruin](cards/B/bu.md#buried-ruin) · ✅ [Inventors' Fair](cards/I/inv.md#inventors-fair) · ✅ [Volrath's Stronghold](cards/V/vo.md#volraths-stronghold) · ✅ [Hall of Heliod's Generosity](cards/H/ha.md#hall-of-heliods-generosity) · ✅ [Myriad Landscape](cards/M/my.md#myriad-landscape) · ✅ [Thespian's Stage](cards/T/thes.md#thespians-stage) · ✅ [Dark Depths](cards/D/da.md#dark-depths) · ✅ [Cabal Coffers](cards/C/cab.md#cabal-coffers) · ✅ [Urborg, Tomb of Yawgmoth](cards/U/ur.md#urborg-tomb-of-yawgmoth) · ✅ [Yavimaya, Cradle of Growth](cards/Y/ya.md#yavimaya-cradle-of-growth) · ✅ [Gaea's Cradle](cards/G/ga.md#gaeas-cradle) · ✅ [Nykthos, Shrine to Nyx](cards/N/ny.md#nykthos-shrine-to-nyx) · ✅ [Glacial Chasm](cards/G/gl.md#glacial-chasm) · ✅ [Mystifying Maze](cards/M/my.md#mystifying-maze) · ✅ [Karakas](cards/K/ka.md#karakas) · ✅ [Castle Ardenvale](cards/C/cas.md#castle-ardenvale) · ✅ [Castle Locthwain](cards/C/cas.md#castle-locthwain) · ✅ [Castle Embereth](cards/C/cas.md#castle-embereth) · ✅ [Castle Vantress](cards/C/cas.md#castle-vantress) · ✅ [Castle Garenbrig](cards/C/cas.md#castle-garenbrig) · ✅ [Otawara, Soaring City](cards/O/ot.md#otawara-soaring-city) · ✅ [Boseiju, Who Endures](cards/B/bo.md#boseiju-who-endures) · ✅ [Eiganjo, Seat of the Empire](cards/E/ei.md#eiganjo-seat-of-the-empire) · ✅ [Takenuma, Abandoned Mire](cards/T/ta.md#takenuma-abandoned-mire) · ✅ [Sokenzan, Crucible of Defiance](cards/S/so.md#sokenzan-crucible-of-defiance) · ✅ [War Room](cards/W/war.md#war-room) · ✅ [Emeria, the Sky Ruin](cards/E/em.md#emeria-the-sky-ruin) · ✅ [Valakut, the Molten Pinnacle](cards/V/va.md#valakut-the-molten-pinnacle) · ✅ [Path of Ancestry](cards/P/pa.md#path-of-ancestry) · ✅ [Exotic Orchard](cards/E/ex.md#exotic-orchard) · ✅ [Scavenger Grounds](cards/S/sc.md#scavenger-grounds) · ✅ [High Market](cards/H/hi.md#high-market) · ✅ [Phyrexian Tower](cards/P/ph.md#phyrexian-tower) · ✅ [Temple of the False God](cards/T/te.md#temple-of-the-false-god)

### Land Destruction (28/28)

✅ [Strip Mine](cards/S/str.md#strip-mine) · ✅ [Wasteland](cards/W/was.md#wasteland) · ✅ [Tectonic Edge](cards/T/te.md#tectonic-edge) · ✅ [Ghost Quarter](cards/G/gh.md#ghost-quarter) · ✅ [Field of Ruin](cards/F/fi.md#field-of-ruin) · ✅ [Demolition Field](cards/D/dem.md#demolition-field) · ✅ [Dust Bowl](cards/D/du.md#dust-bowl) · ✅ [Encroaching Wastes](cards/E/en.md#encroaching-wastes) · ✅ [Armageddon](cards/A/arm.md#armageddon) · ✅ [Ravages of War](cards/R/rav.md#ravages-of-war) · ✅ [Ruination](cards/R/ru.md#ruination) · ✅ [Sinkhole](cards/S/si.md#sinkhole) · ✅ [Stone Rain](cards/S/sto.md#stone-rain) · ✅ [Cataclysm](cards/C/cat.md#cataclysm) · ✅ [Jokulhaups](cards/J/jo.md#jokulhaups) · ✅ [Obliterate](cards/O/ob.md#obliterate) · ✅ [Decree of Annihilation](cards/D/dec.md#decree-of-annihilation) · ✅ [Impending Disaster](cards/I/im.md#impending-disaster) · ✅ [Wildfire](cards/W/wi.md#wildfire) · ✅ [Destructive Flow](cards/D/des.md#destructive-flow) · ✅ [Boom // Bust](cards/B/bo.md#boom--bust) · ✅ [Mold Shambler](cards/M/mol.md#mold-shambler) · ✅ [Acidic Slime](cards/A/ac.md#acidic-slime) · ✅ [Sowing Salt](cards/S/so.md#sowing-salt) · ✅ [Avalanche Riders](cards/A/av.md#avalanche-riders) · ✅ [Fall of the Thran](cards/F/fa.md#fall-of-the-thran) · ✅ [Catastrophe](cards/C/cat.md#catastrophe) · ✅ [Winds of Abandon](cards/W/wi.md#winds-of-abandon)

### Counterspells (39/39)

✅ [Counterspell](cards/C/cou.md#counterspell) · ✅ [Swan Song](cards/S/sw.md#swan-song) · ✅ [Force of Will](cards/F/fo.md#force-of-will) · ✅ [Mana Drain](cards/M/man.md#mana-drain) · ✅ [Negate](cards/N/ne.md#negate) · ✅ [Dispel](cards/D/di.md#dispel) · ✅ [Spell Pierce](cards/S/spe.md#spell-pierce) · ✅ [Fierce Guardianship](cards/F/fi.md#fierce-guardianship) · ✅ [Pact of Negation](cards/P/pa.md#pact-of-negation) · ✅ [Flusterstorm](cards/F/fl.md#flusterstorm) · ✅ [An Offer You Can't Refuse](cards/A/an.md#an-offer-you-cant-refuse) · ✅ [Mental Misstep](cards/M/me.md#mental-misstep) · ✅ [Arcane Denial](cards/A/arc.md#arcane-denial) · ✅ [Dovin's Veto](cards/D/do.md#dovins-veto) · ✅ [Mana Leak](cards/M/man.md#mana-leak) · ✅ [Cryptic Command](cards/C/cr.md#cryptic-command) · ✅ [Force of Negation](cards/F/fo.md#force-of-negation) · ✅ [Mindbreak Trap](cards/M/min.md#mindbreak-trap) · ✅ [Stern Scolding](cards/S/ste.md#stern-scolding) · ✅ [Stifle](cards/S/sti.md#stifle) · ✅ [Miscalculation](cards/M/mis.md#miscalculation) · ✅ [Memory Lapse](cards/M/me.md#memory-lapse) · ✅ [Remand](cards/R/rem.md#remand) · ✅ [Absorb](cards/A/ab.md#absorb) · ✅ [Lapse of Certainty](cards/L/la.md#lapse-of-certainty) · ✅ [Saw It Coming](cards/S/saw.md#saw-it-coming) · ✅ [Essence Scatter](cards/E/es.md#essence-scatter) · ✅ [Mystical Dispute](cards/M/my.md#mystical-dispute) · ✅ [Didn't Say Please](cards/D/di.md#didnt-say-please) · ✅ [Cancel](cards/C/can.md#cancel) · ✅ [Delay](cards/D/del.md#delay) · ✅ [Disdainful Stroke](cards/D/di.md#disdainful-stroke) · ✅ [Rewind](cards/R/rew.md#rewind) · ✅ [Supreme Will](cards/S/sup.md#supreme-will) · ✅ [Muddle the Mixture](cards/M/mu.md#muddle-the-mixture) · ✅ [Tale's End](cards/T/ta.md#tales-end) · ✅ [Silumgar's Command](cards/S/si.md#silumgars-command) · ✅ [Hullbreacher](cards/H/hu.md#hullbreacher) · ✅ [Deflecting Swat](cards/D/def.md#deflecting-swat)

### Fast Mana & Rocks (20/20)

✅ [Sol Ring](cards/S/so.md#sol-ring) · ✅ [Arcane Signet](cards/A/arc.md#arcane-signet) · ✅ [Mana Crypt](cards/M/man.md#mana-crypt) · ✅ [Mana Vault](cards/M/man.md#mana-vault) · ✅ [Chrome Mox](cards/C/chr.md#chrome-mox) · ✅ [Mox Diamond](cards/M/mox.md#mox-diamond) · ✅ [Jeweled Lotus](cards/J/je.md#jeweled-lotus) · ✅ [Lotus Petal](cards/L/lo.md#lotus-petal) · ✅ [Fellwar Stone](cards/F/fe.md#fellwar-stone) · ✅ [Mind Stone](cards/M/min.md#mind-stone) · ✅ [Thought Vessel](cards/T/tho.md#thought-vessel) · ✅ [Talisman of Dominance](cards/T/ta.md#talisman-of-dominance) · ✅ [Dimir Signet](cards/D/di.md#dimir-signet) · ✅ [Commander's Sphere](cards/C/com.md#commanders-sphere) · ✅ [Grim Monolith](cards/G/gri.md#grim-monolith) · ✅ [Basalt Monolith](cards/B/bas.md#basalt-monolith) · ✅ [Dark Ritual](cards/D/da.md#dark-ritual) · ✅ [Simian Spirit Guide](cards/S/si.md#simian-spirit-guide) · ✅ [Mox Opal](cards/M/mox.md#mox-opal) · ✅ [Mox Amber](cards/M/mox.md#mox-amber)

### Removal & Board Wipes (28/28)

✅ [Swords to Plowshares](cards/S/sw.md#swords-to-plowshares) · ✅ [Path to Exile](cards/P/pa.md#path-to-exile) · ✅ [Chaos Warp](cards/C/cha.md#chaos-warp) · ✅ [Beast Within](cards/B/be.md#beast-within) · ✅ [Generous Gift](cards/G/ge.md#generous-gift) · ✅ [Anguished Unmaking](cards/A/an.md#anguished-unmaking) · ✅ [Assassin's Trophy](cards/A/as.md#assassins-trophy) · ✅ [Cyclonic Rift](cards/C/cy.md#cyclonic-rift) · ✅ [Wrath of God](cards/W/wr.md#wrath-of-god) · ✅ [Damnation](cards/D/da.md#damnation) · ✅ [Toxic Deluge](cards/T/to.md#toxic-deluge) · ✅ [Farewell](cards/F/fa.md#farewell) · ✅ [Blasphemous Act](cards/B/bla.md#blasphemous-act) · ✅ [Austere Command](cards/A/au.md#austere-command) · ✅ [Vandalblast](cards/V/va.md#vandalblast) · ✅ [Feed the Swarm](cards/F/fe.md#feed-the-swarm) · ✅ [Rapid Hybridization](cards/R/rap.md#rapid-hybridization) · ✅ [Pongify](cards/P/po.md#pongify) · ✅ [Nature's Claim](cards/N/na.md#natures-claim) · ✅ [Krosan Grip](cards/K/kr.md#krosan-grip) · ✅ [Deadly Rollick](cards/D/dea.md#deadly-rollick) · ✅ [Infernal Grasp](cards/I/inf.md#infernal-grasp) · ✅ [Vindicate](cards/V/vi.md#vindicate) · ✅ [Return to Dust](cards/R/ret.md#return-to-dust) · ✅ [Evacuation](cards/E/ev.md#evacuation) · ✅ [Massacre Wurm](cards/M/mas.md#massacre-wurm) · ✅ [Supreme Verdict](cards/S/sup.md#supreme-verdict) · ✅ [Sunfall](cards/S/sun.md#sunfall)

### Tutors (22/22)

✅ [Demonic Tutor](cards/D/dem.md#demonic-tutor) · ✅ [Vampiric Tutor](cards/V/va.md#vampiric-tutor) · ✅ [Enlightened Tutor](cards/E/en.md#enlightened-tutor) · ✅ [Mystical Tutor](cards/M/my.md#mystical-tutor) · ✅ [Worldly Tutor](cards/W/wo.md#worldly-tutor) · ✅ [Gamble](cards/G/ga.md#gamble) · ✅ [Diabolic Intent](cards/D/di.md#diabolic-intent) · ✅ [Imperial Seal](cards/I/im.md#imperial-seal) · ✅ [Grim Tutor](cards/G/gri.md#grim-tutor) · ✅ [Diabolic Tutor](cards/D/di.md#diabolic-tutor) · ✅ [Idyllic Tutor](cards/I/id.md#idyllic-tutor) · ✅ [Eladamri's Call](cards/E/el.md#eladamris-call) · ✅ [Finale of Devastation](cards/F/fi.md#finale-of-devastation) · ✅ [Green Sun's Zenith](cards/G/gre.md#green-suns-zenith) · ✅ [Chord of Calling](cards/C/cho.md#chord-of-calling) · ✅ [Natural Order](cards/N/na.md#natural-order) · ✅ [Survival of the Fittest](cards/S/sur.md#survival-of-the-fittest) · ✅ [Fabricate](cards/F/fa.md#fabricate) · ✅ [Whir of Invention](cards/W/wh.md#whir-of-invention) · ✅ [Tainted Pact](cards/T/ta.md#tainted-pact) · ✅ [Personal Tutor](cards/P/pe.md#personal-tutor) · ✅ [Steelshaper's Gift](cards/S/ste.md#steelshapers-gift)

### Card Advantage (23/23)

✅ [Rhystic Study](cards/R/rh.md#rhystic-study) · ✅ [Mystic Remora](cards/M/my.md#mystic-remora) · ✅ [Sylvan Library](cards/S/sy.md#sylvan-library) · ✅ [Phyrexian Arena](cards/P/ph.md#phyrexian-arena) · ✅ [Esper Sentinel](cards/E/es.md#esper-sentinel) · ✅ [Skullclamp](cards/S/sk.md#skullclamp) · ✅ [Necropotence](cards/N/ne.md#necropotence) · ✅ [The One Ring](cards/T/theo.md#the-one-ring) · ✅ [Smothering Tithe](cards/S/sm.md#smothering-tithe) · ✅ [Harmonize](cards/H/ha.md#harmonize) · ✅ [Guardian Project](cards/G/gu.md#guardian-project) · ✅ [Beast Whisperer](cards/B/be.md#beast-whisperer) · ✅ [Night's Whisper](cards/N/ni.md#nights-whisper) · ✅ [Sign in Blood](cards/S/si.md#sign-in-blood) · ✅ [Brainstorm](cards/B/br.md#brainstorm) · ✅ [Ponder](cards/P/po.md#ponder) · ✅ [Preordain](cards/P/pr.md#preordain) · ✅ [Fact or Fiction](cards/F/fa.md#fact-or-fiction) · ✅ [Mulldrifter](cards/M/mu.md#mulldrifter) · ✅ [Jeska's Will](cards/J/je.md#jeskas-will) · ✅ [Wheel of Fortune](cards/W/wh.md#wheel-of-fortune) · ✅ [Windfall](cards/W/wi.md#windfall) · ✅ [Faithless Looting](cards/F/fa.md#faithless-looting)

### Protection (16/16)

✅ [Lightning Greaves](cards/L/li.md#lightning-greaves) · ✅ [Swiftfoot Boots](cards/S/sw.md#swiftfoot-boots) · ✅ [Heroic Intervention](cards/H/he.md#heroic-intervention) · ✅ [Teferi's Protection](cards/T/te.md#teferis-protection) · ✅ [Flawless Maneuver](cards/F/fl.md#flawless-maneuver) · ✅ [Boros Charm](cards/B/bo.md#boros-charm) · ✅ [Akroma's Will](cards/A/ak.md#akromas-will) · ✅ [Clever Concealment](cards/C/cl.md#clever-concealment) · ✅ [Mother of Runes](cards/M/mot.md#mother-of-runes) · ✅ [Giver of Runes](cards/G/gi.md#giver-of-runes) · ✅ [Darksteel Plate](cards/D/da.md#darksteel-plate) · ✅ [Whispersilk Cloak](cards/W/wh.md#whispersilk-cloak) · ✅ [Snakeskin Veil](cards/S/sn.md#snakeskin-veil) · ✅ [Tamiyo's Safekeeping](cards/T/ta.md#tamiyos-safekeeping) · ✅ [Blossoming Defense](cards/B/blo.md#blossoming-defense) · ✅ [Dauntless Bodyguard](cards/D/da.md#dauntless-bodyguard)

### Ramp (20/20)

✅ [Cultivate](cards/C/cu.md#cultivate) · ✅ [Kodama's Reach](cards/K/ko.md#kodamas-reach) · ✅ [Rampant Growth](cards/R/ram.md#rampant-growth) · ✅ [Farseek](cards/F/fa.md#farseek) · ✅ [Nature's Lore](cards/N/na.md#natures-lore) · ✅ [Three Visits](cards/T/thr.md#three-visits) · ✅ [Skyshroud Claim](cards/S/sk.md#skyshroud-claim) · ✅ [Llanowar Elves](cards/L/ll.md#llanowar-elves) · ✅ [Elvish Mystic](cards/E/el.md#elvish-mystic) · ✅ [Birds of Paradise](cards/B/bi.md#birds-of-paradise) · ✅ [Sakura-Tribe Elder](cards/S/sak.md#sakura-tribe-elder) · ✅ [Wood Elves](cards/W/wo.md#wood-elves) · ✅ [Explore](cards/E/ex.md#explore) · ✅ [Exploration](cards/E/ex.md#exploration) · ✅ [Burgeoning](cards/B/bu.md#burgeoning) · ✅ [Dryad of the Ilysian Grove](cards/D/dry.md#dryad-of-the-ilysian-grove) · ✅ [Oracle of Mul Daya](cards/O/or.md#oracle-of-mul-daya) · ✅ [Azusa, Lost but Seeking](cards/A/az.md#azusa-lost-but-seeking) · ✅ [Lotus Cobra](cards/L/lo.md#lotus-cobra) · ✅ [Tireless Provisioner](cards/T/ti.md#tireless-provisioner)

## Game Changers ingested

Cards Scryfall flags as `game_changer` (used by the official Commander Brackets system). See [EDH Standards](EDH%20Standards.md).

[Ad Nauseam](cards/A/ad.md#ad-nauseam) · [Ancient Tomb](cards/A/an.md#ancient-tomb) · [Aura Shards](cards/A/au.md#aura-shards) · [Biorhythm](cards/B/bi.md#biorhythm) · [Bolas's Citadel](cards/B/bo.md#bolass-citadel) · [Braids, Cabal Minion](cards/B/br.md#braids-cabal-minion) · [Chrome Mox](cards/C/chr.md#chrome-mox) · [Coalition Victory](cards/C/coa.md#coalition-victory) · [Consecrated Sphinx](cards/C/con.md#consecrated-sphinx) · [Crop Rotation](cards/C/cr.md#crop-rotation) · [Cyclonic Rift](cards/C/cy.md#cyclonic-rift) · [Demonic Tutor](cards/D/dem.md#demonic-tutor) · [Drannith Magistrate](cards/D/dra.md#drannith-magistrate) · [Enlightened Tutor](cards/E/en.md#enlightened-tutor) · [Farewell](cards/F/fa.md#farewell) · [Field of the Dead](cards/F/fi.md#field-of-the-dead) · [Fierce Guardianship](cards/F/fi.md#fierce-guardianship) · [Force of Will](cards/F/fo.md#force-of-will) · [Gaea's Cradle](cards/G/ga.md#gaeas-cradle) · [Gamble](cards/G/ga.md#gamble) · [Gifts Ungiven](cards/G/gi.md#gifts-ungiven) · [Glacial Chasm](cards/G/gl.md#glacial-chasm) · [Grand Arbiter Augustin IV](cards/G/gra.md#grand-arbiter-augustin-iv) · [Grim Monolith](cards/G/gri.md#grim-monolith) · [Humility](cards/H/hu.md#humility) · [Imperial Seal](cards/I/im.md#imperial-seal) · [Intuition](cards/I/int.md#intuition) · [Jeska's Will](cards/J/je.md#jeskas-will) · [Lion's Eye Diamond](cards/L/li.md#lions-eye-diamond) · [Mana Vault](cards/M/man.md#mana-vault) · [Mishra's Workshop](cards/M/mis.md#mishras-workshop) · [Mox Diamond](cards/M/mox.md#mox-diamond) · [Mystical Tutor](cards/M/my.md#mystical-tutor) · [Narset, Parter of Veils](cards/N/na.md#narset-parter-of-veils) · [Natural Order](cards/N/na.md#natural-order) · [Necropotence](cards/N/ne.md#necropotence) · [Notion Thief](cards/N/no.md#notion-thief) · [Opposition Agent](cards/O/op.md#opposition-agent) · [Orcish Bowmasters](cards/O/or.md#orcish-bowmasters) · [Panoptic Mirror](cards/P/pa.md#panoptic-mirror) · [Rhystic Study](cards/R/rh.md#rhystic-study) · [Seedborn Muse](cards/S/see.md#seedborn-muse) · [Serra's Sanctum](cards/S/ser.md#serras-sanctum) · [Smothering Tithe](cards/S/sm.md#smothering-tithe) · [Survival of the Fittest](cards/S/sur.md#survival-of-the-fittest) · [Teferi's Protection](cards/T/te.md#teferis-protection) · [Tergrid, God of Fright // Tergrid's Lantern](cards/T/te.md#tergrid-god-of-fright--tergrids-lantern) · [Thassa's Oracle](cards/T/tha.md#thassas-oracle) · [The One Ring](cards/T/theo.md#the-one-ring) · [The Tabernacle at Pendrell Vale](cards/T/thet.md#the-tabernacle-at-pendrell-vale) · [Underworld Breach](cards/U/un.md#underworld-breach) · [Vampiric Tutor](cards/V/va.md#vampiric-tutor) · [Worldly Tutor](cards/W/wo.md#worldly-tutor)

## Top 100 by EDHREC rank

| Rank | Card | Identity | Type |
|---|---|---|---|
| 1 | [Sol Ring](cards/S/so.md#sol-ring) | C | Artifact |
| 2 | [Command Tower](cards/C/com.md#command-tower) | C | Land |
| 3 | [Arcane Signet](cards/A/arc.md#arcane-signet) | C | Artifact |
| 9 | [Exotic Orchard](cards/E/ex.md#exotic-orchard) | C | Land |
| 10 | [Reliquary Tower](cards/R/rel.md#reliquary-tower) | C | Land |
| 11 | [Swords to Plowshares](cards/S/sw.md#swords-to-plowshares) | W | Instant |
| 12 | [Swiftfoot Boots](cards/S/sw.md#swiftfoot-boots) | C | Artifact — Equipment |
| 13 | [Lightning Greaves](cards/L/li.md#lightning-greaves) | C | Artifact — Equipment |
| 14 | [Path of Ancestry](cards/P/pa.md#path-of-ancestry) | C | Land |
| 15 | [Path to Exile](cards/P/pa.md#path-to-exile) | W | Instant |
| 16 | [Counterspell](cards/C/cou.md#counterspell) | U | Instant |
| 17 | [Fellwar Stone](cards/F/fe.md#fellwar-stone) | C | Artifact |
| 18 | [Rogue's Passage](cards/R/ro.md#rogues-passage) | C | Land |
| 19 | [Evolving Wilds](cards/E/ev.md#evolving-wilds) | C | Land |
| 20 | [Cultivate](cards/C/cu.md#cultivate) | G | Sorcery |
| 21 | [Thought Vessel](cards/T/tho.md#thought-vessel) | C | Artifact |
| 22 | [Blasphemous Act](cards/B/bla.md#blasphemous-act) | R | Sorcery |
| 23 | [Farseek](cards/F/fa.md#farseek) | G | Sorcery |
| 24 | [Bojuka Bog](cards/B/bo.md#bojuka-bog) | B | Land |
| 25 | [Beast Within](cards/B/be.md#beast-within) | G | Instant |
| 26 | [Nature's Lore](cards/N/na.md#natures-lore) | G | Sorcery |
| 27 | [Rampant Growth](cards/R/ram.md#rampant-growth) | G | Sorcery |
| 28 | [Heroic Intervention](cards/H/he.md#heroic-intervention) | G | Instant |
| 29 | [Chaos Warp](cards/C/cha.md#chaos-warp) | R | Instant |
| 30 | [Terramorphic Expanse](cards/T/te.md#terramorphic-expanse) | C | Land |
| 31 | [Myriad Landscape](cards/M/my.md#myriad-landscape) | C | Land |
| 32 | [Mind Stone](cards/M/min.md#mind-stone) | C | Artifact |
| 33 | [Dark Ritual](cards/D/da.md#dark-ritual) | B | Instant |
| 34 | [An Offer You Can't Refuse](cards/A/an.md#an-offer-you-cant-refuse) | U | Instant |
| 35 | [Birds of Paradise](cards/B/bi.md#birds-of-paradise) | G | Creature — Bird |
| 36 | [Polluted Delta](cards/P/po.md#polluted-delta) | C | Land |
| 37 | [Kodama's Reach](cards/K/ko.md#kodamas-reach) | G | Sorcery — Arcane |
| 38 | [Flooded Strand](cards/F/fl.md#flooded-strand) | C | Land |
| 39 | [Skullclamp](cards/S/sk.md#skullclamp) | C | Artifact — Equipment |
| 40 | [Three Visits](cards/T/thr.md#three-visits) | G | Sorcery |
| 41 | [Solemn Simulacrum](cards/S/so.md#solemn-simulacrum) | C | Artifact Creature — Golem |
| 42 | [Misty Rainforest](cards/M/mis.md#misty-rainforest) | C | Land |
| 43 | [Bloodstained Mire](cards/B/blo.md#bloodstained-mire) | C | Land |
| 44 | [Fabled Passage](cards/F/fa.md#fabled-passage) | C | Land |
| 45 | [Windswept Heath](cards/W/wi.md#windswept-heath) | C | Land |
| 46 | [Rhystic Study](cards/R/rh.md#rhystic-study) | U | Enchantment |
| 47 | [Wooded Foothills](cards/W/wo.md#wooded-foothills) | C | Land |
| 48 | [Verdant Catacombs](cards/V/ve.md#verdant-catacombs) | C | Land |
| 49 | [Scalding Tarn](cards/S/sc.md#scalding-tarn) | C | Land |
| 50 | [Watery Grave](cards/W/wat.md#watery-grave) | BU | Land — Island Swamp |
| 51 | [Marsh Flats](cards/M/mar.md#marsh-flats) | C | Land |
| 52 | [Arcane Denial](cards/A/arc.md#arcane-denial) | U | Instant |
| 53 | [Reanimate](cards/R/rea.md#reanimate) | B | Sorcery |
| 54 | [Commander's Sphere](cards/C/com.md#commanders-sphere) | C | Artifact |
| 55 | [Arid Mesa](cards/A/ari.md#arid-mesa) | C | Land |
| 56 | [Llanowar Elves](cards/L/ll.md#llanowar-elves) | G | Creature — Elf Druid |
| 57 | [Negate](cards/N/ne.md#negate) | U | Instant |
| 58 | [Cyclonic Rift](cards/C/cy.md#cyclonic-rift) | U | Instant |
| 59 | [Godless Shrine](cards/G/god.md#godless-shrine) | BW | Land — Plains Swamp |
| 60 | [Breeding Pool](cards/B/br.md#breeding-pool) | GU | Land — Forest Island |
| 61 | [Hallowed Fountain](cards/H/ha.md#hallowed-fountain) | UW | Land — Plains Island |
| 62 | [Steam Vents](cards/S/ste.md#steam-vents) | RU | Land — Island Mountain |
| 63 | [Generous Gift](cards/G/ge.md#generous-gift) | W | Instant |
| 64 | [Demonic Tutor](cards/D/dem.md#demonic-tutor) | B | Sorcery |
| 65 | [Toxic Deluge](cards/T/to.md#toxic-deluge) | B | Sorcery |
| 66 | [Swan Song](cards/S/sw.md#swan-song) | U | Instant |
| 67 | [Smothering Tithe](cards/S/sm.md#smothering-tithe) | W | Enchantment |
| 68 | [Blood Crypt](cards/B/blo.md#blood-crypt) | BR | Land — Swamp Mountain |
| 69 | [Ancient Tomb](cards/A/an.md#ancient-tomb) | C | Land |
| 70 | [Stomping Ground](cards/S/sto.md#stomping-ground) | GR | Land — Mountain Forest |
| 71 | [Overgrown Tomb](cards/O/ov.md#overgrown-tomb) | BG | Land — Swamp Forest |
| 72 | [Brainstorm](cards/B/br.md#brainstorm) | U | Instant |
| 73 | [Sacred Foundry](cards/S/sac.md#sacred-foundry) | RW | Land — Mountain Plains |
| 74 | [Deflecting Swat](cards/D/def.md#deflecting-swat) | R | Instant |
| 75 | [Urborg, Tomb of Yawgmoth](cards/U/ur.md#urborg-tomb-of-yawgmoth) | C | Legendary Land |
| 76 | [Sulfur Falls](cards/S/sul.md#sulfur-falls) | RU | Land |
| 77 | [Boseiju, Who Endures](cards/B/bo.md#boseiju-who-endures) | G | Legendary Land |
| 78 | [Clifftop Retreat](cards/C/cl.md#clifftop-retreat) | RW | Land |
| 79 | [Yavimaya, Cradle of Growth](cards/Y/ya.md#yavimaya-cradle-of-growth) | C | Legendary Land |
| 80 | [Esper Sentinel](cards/E/es.md#esper-sentinel) | W | Artifact Creature — Human Soldier |
| 81 | [Temple Garden](cards/T/te.md#temple-garden) | GW | Land — Forest Plains |
| 82 | [Fierce Guardianship](cards/F/fi.md#fierce-guardianship) | U | Instant |
| 83 | [Dragonskull Summit](cards/D/dra.md#dragonskull-summit) | BR | Land |
| 84 | [Temple of the False God](cards/T/te.md#temple-of-the-false-god) | C | Land |
| 85 | [Chromatic Lantern](cards/C/chr.md#chromatic-lantern) | C | Artifact |
| 86 | [Sunken Hollow](cards/S/sun.md#sunken-hollow) | BU | Land — Island Swamp |
| 87 | [Cinder Glade](cards/C/ci.md#cinder-glade) | GR | Land — Mountain Forest |
| 88 | [Glacial Fortress](cards/G/gl.md#glacial-fortress) | UW | Land |
| 89 | [Otawara, Soaring City](cards/O/ot.md#otawara-soaring-city) | U | Legendary Land |
| 90 | [Isolated Chapel](cards/I/is.md#isolated-chapel) | BW | Land |
| 91 | [Garruk's Uprising](cards/G/ga.md#garruks-uprising) | G | Enchantment |
| 92 | [Talisman of Dominance](cards/T/ta.md#talisman-of-dominance) | BU | Artifact |
| 93 | [Feed the Swarm](cards/F/fe.md#feed-the-swarm) | B | Sorcery |
| 94 | [City of Brass](cards/C/ci.md#city-of-brass) | C | Land |
| 95 | [Smoldering Marsh](cards/S/sm.md#smoldering-marsh) | BR | Land — Swamp Mountain |
| 96 | [The One Ring](cards/T/theo.md#the-one-ring) | C | Legendary Artifact |
| 97 | [Hinterland Harbor](cards/H/hi.md#hinterland-harbor) | GU | Land |
| 98 | [Frantic Search](cards/F/fr.md#frantic-search) | U | Instant |
| 99 | [Faithless Looting](cards/F/fa.md#faithless-looting) | R | Sorcery |
| 100 | [Vandalblast](cards/V/va.md#vandalblast) | R | Sorcery |
| 101 | [Mystic Remora](cards/M/my.md#mystic-remora) | U | Enchantment |
| 102 | [Elvish Mystic](cards/E/el.md#elvish-mystic) | G | Creature — Elf Druid |
| 103 | [Prairie Stream](cards/P/pr.md#prairie-stream) | UW | Land — Plains Island |
| 104 | [Phyrexian Arena](cards/P/ph.md#phyrexian-arena) | B | Enchantment |
| 105 | [Drowned Catacomb](cards/D/dro.md#drowned-catacomb) | BU | Land |

## How to find a card

1. Strip accents and punctuation from the name and lower-case it → take the first two letters → `cards/<FIRST>/<first two>.md`; very common prefixes are split one letter deeper (e.g. `cards/T/the.md`, `cards/M/mag.md`) — see the shard table above. Names starting with a digit live in `cards/0-9/0-9.md`.
2. Or search [`data/card_index.csv`](data/card_index.csv) (columns: name, oracle_id, shard, anchor, edhrec_rank, color_identity, type_line, commander_legality, game_changer, batch, rulings).
