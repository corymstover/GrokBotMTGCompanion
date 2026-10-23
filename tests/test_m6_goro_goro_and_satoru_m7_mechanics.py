"""Finite source-anchored rules/mana cases for the Goro-Goro and Satoru M7 research candidate.

No randomness. Goro-Goro and Satoru is modelled exactly as printed (current Oracle in the M7 snapshot): {U}{B}{R} 3/4
Legendary Creature - Goblin Human; "Whenever one or more creatures you control that entered this turn deal combat damage
to a player, create a 5/5 red Dragon Spirit creature token with flying. / {1}{R}: Creatures you control gain haste until
end of turn." Rules anchors: 603.2 (triggered abilities trigger on the event), 611.2c (a continuous effect from a
resolved ability affects only objects present at resolution, ruling 2023-04-14), 702.49 (ninjutsu: the creature enters
tapped and attacking after blockers, so it entered this turn), 302.6 (summoning sickness), 903.8 (commander tax).

This is a bounded, fully scripted rules model (turns 1-7, two board profiles x five opponent cases x five cards), NOT a
game engine, simulation or win-rate measurement; it supports no improvement claim by itself. PassCBoundedMeasuredTests
re-runs the bounded finite version of the M6 Pass C request (exact baseline vs +Bitterblossom -Bident of Thassa and vs
+Bitterblossom -Grazilaxx, Illithid Scholar; paid turn-3 UBR; turn 3-7 resources and draws; flying blockers; commander
removal; sweeper; one extra combat) and checks every recorded row, then recomputes exact hypergeometric paid-UBR turn-3
castability. Matched opening hands and games against opponents are NOT modelled (no validated Goro game model).
"""
from collections import Counter
from math import comb
from functools import lru_cache
import itertools
import json
import re
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
D = "Goro_Goro_and_Satoru"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
CAND = ROOT / f"data/grixis/m7/candidate_lists/{D}.txt"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
RC = ROOT / "data/grixis/m7/research_challengers"
SPELLBOOK = RC / f"{D}_CommanderSpellbook_20261023.json"
MEASURED = RC / f"{D}_bounded_measured_tests_20261023.json"
DRAGONSKULL = RC / f"{D}_two_DragonskullSummit_over_CrumblingNecropolis_20261023.txt"
GORO = "Goro-Goro and Satoru"
ADDS = ["Bitterblossom"]
CUTS = ["Mist-Syndicate Naga"]
GAME_CHANGERS = ["Ancient Tomb", "Cyclonic Rift", "Demonic Tutor", "Fierce Guardianship", "Jeska's Will", "Vampiric Tutor"]
OWNER_REMOVED = ["Reinforced Ronin", "Rising of the Day", "Feed the Swarm", "Combat Research", "Impact Tremors",
                 "Kaito, Dancing Shadow"]
OWNER_ADDED = ["Phoenix Chick", "Samut, Hazoret's Champion", "Withering Torment", "Waterbender Ascension",
               "Raphael, the Nightwatcher", "Fire Navy Trebuchet"]
COMBOS = ["1347-3259", "1674-3259", "2237-3259", "3259-3934", "33-3259"]
FETCH_ALL = {"Polluted Delta", "Bloodstained Mire", "Scalding Tarn", "Fabled Passage"}
RAINBOW = {"City of Brass", "Mana Confluence", "Command Tower", "Exotic Orchard"}


def names(path):
    out = Counter()
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.strip():
            q, raw = line.split(" ", 1)
            out[raw.removesuffix(" [Commander]")] += int(q.rstrip("x"))
    return out


def oracle():
    return {c["name"]: c for c in json.loads(SNAP.read_text())["cards"]}


# ---- Pass C bounded ledger model (identical to the generator that wrote the measured JSON) ----
def sim(X,profile,opp):
    life=40; cards=0; dragons=0; dragons_on_board=0; log=[]
    board=[]  # dicts: name,p,t,fly,unbl,fresh,haste,sick,token
    def add(n,p,t,fly=False,unbl=False,haste=False,token=False):
        board.append(dict(name=n,p=p,t=t,fly=fly,unbl=unbl,fresh=True,haste=haste,token=token,ret=False))
    goro=False; goro_casts=0; bb=False; bident=False; graz=False; storm=False; slither_in_hand=False
    add('Slither Blade',1,2,unbl=True)
    for t in range(1,8):
        for c in board: c['fresh']=False; c['haste']=False
        mana=t
        if opp=='removal' and t==5 and goro: goro=False; log.append('T5 Goro destroyed')
        if opp=='sweeper' and t==6:
            board.clear(); goro=False; graz=False; storm=False; slither_in_hand=False; log.append('T6 sweeper: all creatures die')
        if bb: life-=1; add('Faerie Rogue',1,1,fly=True,token=True)
        if t==2 and X=='Bitterblossom': bb=True; mana-=2
        if slither_in_hand and mana>=1: slither_in_hand=False; mana-=1; add('Slither Blade',1,2,unbl=True)
        tax=2*goro_casts
        if not goro and t>=3 and mana>=3+tax and not (opp=='removal' and t==5) and not (opp=='sweeper' and t==6):
            goro=True; goro_casts+=1; mana-=3+tax; add('Goro-Goro and Satoru',3,4)
        if t==4 and X=='Bident of Thassa' and mana>=4: bident=True; mana-=4
        if t==4 and X=='Grazilaxx, Illithid Scholar' and mana>=3: graz=True; mana-=3; add('Grazilaxx, Illithid Scholar',3,2)
        if t==4 and X=='Redoubled Stormsinger' and mana>=3: storm=True; mana-=3; add('Redoubled Stormsinger',3,3)
        ninjutsu = (t==4 and X=='Mist-Syndicate Naga')
        if ninjutsu: mana-=3
        combats = 2 if (opp=='extra' and t==6) else 1
        if opp=='extra' and t==6: mana-=1
        for cn in range(combats):
            if profile=='engine' and t>=4: add('Pirate',1,1,haste=True,token=True)
            if goro and mana>=2 and any(c['fresh'] and not c['haste'] and c['name']!='Goro-Goro and Satoru' for c in board):
                mana-=2
                for c in board: c['haste']=True
            att=[c for c in board if c['name']!='Goro-Goro and Satoru' and not c.get('tapped') and (not c['fresh'] or c['haste']) and c['p']>0]
            if cn==1: att=[c for c in board if c['name']!='Goro-Goro and Satoru' and (not c['fresh'] or c['haste']) and (c.get('untapped_by_heist') or not c.get('tapped'))]
            # Stormsinger attack trigger: copy each creature token that entered this turn, tapped and attacking (sacrificed at end step)
            if storm and any(c['name']=='Redoubled Stormsinger' for c in att):
                for c in [c for c in board if c['token'] and c['fresh'] and c['name']!='Storm copy']:
                    cp=dict(c); cp['name']='Storm copy'; board.append(cp); att.append(cp)
            for c in att: c['tapped']=True
            blocked=None
            if opp=='flyer_wall':
                cand=[c for c in att if not c['unbl'] and c['fresh']] or [c for c in att if not c['unbl']]
                if cand: blocked=max(cand,key=lambda c:(c['fresh'],c['p']))
            conn=[c for c in att if c is not blocked]
            if ninjutsu and cn==0:
                sl=[c for c in conn if c['name']=='Slither Blade']
                if sl:
                    board.remove(sl[0]); conn.remove(sl[0]); slither_in_hand=True
                    add('Mist-Syndicate Naga',3,1); nm=board[-1]; nm['tapped']=True; conn.append(nm)
            if blocked is not None:
                if graz and blocked in board: board.remove(blocked); log.append(f'T{t} Grazilaxx returns blocked {blocked["name"]}')
                elif blocked['t']<=2 and blocked in board: board.remove(blocked)
            fresh_conn=[c for c in conn if c['fresh']]
            players_hit = min(3,len(fresh_conn)) + (1 if any(not c['fresh'] for c in conn) else 0)
            players_hit=min(players_hit,3)
            d = min(3,len(fresh_conn)) if goro else 0
            dragons+=d
            if bident: cards+=len(conn)
            if graz: cards+=players_hit
            if any(c['name']=='Mist-Syndicate Naga' for c in conn): add('Naga copy',3,1,token=True)
            for _ in range(d): add('Dragon Spirit',5,5,fly=True,token=True)
            if cn==0 and combats==2:
                for c in board:
                    if c in att: c['untapped_by_heist']=True
        for c in list(board):
            if c['name'] in ('Storm copy','Pirate'): board.remove(c)
        if t<7:
            for c in board: c['tapped']=False; c.pop('untapped_by_heist',None)
    db=sum(1 for c in board if c['name']=='Dragon Spirit'); fliers=sum(1 for c in board if c['fly'])
    return dict(dragons_made=dragons,dragons_on_board_end_T7=db,cards_drawn_T3_T7=cards,life_end=life,fliers_end=fliers,notes=log)


# ---- exact castability model (identical to the generator that wrote the measured JSON) ----
ANY={'Command Tower','City of Brass','Mana Confluence','Exotic Orchard','Crumbling Necropolis',"Xander's Lounge"}
PAIR={'UB':{'Underground Sea','Watery Grave','Drowned Catacomb','Morphic Pool','Shipwreck Marsh','Underground River','Polluted Delta'},
 'BR':{'Badlands','Blood Crypt','Dragonskull Summit','Luxury Suite','Sulfurous Springs','Bloodstained Mire'},
 'UR':{'Volcanic Island','Steam Vents','Sulfur Falls','Shivan Reef','Stormcarved Coast','Training Center','Scalding Tarn'}}
MONO={'Island':'U','Otawara, Soaring City':'U','Swamp':'B','Mountain':'R','Fabled Passage':'UBR'}
COLORLESS_L={'Ancient Tomb',"Rogue's Passage"}
ROCK2={'Arcane Signet':'UBR','Fellwar Stone':'UBR','Talisman of Creativity':'UR','Talisman of Dominance':'UB','Talisman of Indulgence':'BR'}
def load(p):
    cats={}
    for l in open(p, encoding='utf-8'):
        m=re.match(r'(\d+)x? (.+?)( \[Commander\])?$',l.strip())
        if not m or m.group(3): continue
        q,n=int(m.group(1)),m.group(2)
        if n in ANY: k=('L','UBR')
        elif any(n in v for v in PAIR.values()): k=('L',[a for a,v in PAIR.items() if n in v][0])
        elif n in MONO: k=('L',MONO[n])
        elif n in COLORLESS_L: k=('L','')
        elif n in ROCK2: k=('R',ROCK2[n])
        elif n=='Sol Ring': k=('S','')
        else: k=('X','')
        cats[k]=cats.get(k,0)+q
    return cats
def ok(hand,T):
    lands=[c for (t,c),x in hand for _ in range(x) if t=='L']; rocks=[c for (t,c),x in hand for _ in range(x) if t=='R']
    sol=any(t=='S' and x for (t,c),x in hand)
    nl=min(len(lands),T)
    if nl>=2: nr=min(len(rocks),(T-1)*(1)+(1 if sol else 0)) if T>=3 else 0
    elif nl==1 and sol: nr=min(len(rocks),1)
    else: nr=0
    if nl+nr<3: return False
    best=False
    for L in set(itertools.combinations(sorted(lands),nl)):
        for R in set(itertools.combinations(sorted(rocks),nr)):
            srcs=list(L)+list(R)
            for perm in itertools.permutations(range(len(srcs)),3):
                if all(col in srcs[i] for col,i in zip('UBR',perm)): return True
    return False
def P(cats,N,T):
    keys=list(cats); tot=sum(cats.values()); num=0
    def rec(i,left,acc,w):
        nonlocal num
        if i==len(keys):
            if left==0 and ok(acc,T): num+=w
            return
        k=keys[i]
        for x in range(0,min(cats[k],left)+1):
            rec(i+1,left-x,acc+[(k,x)],w*comb(cats[k],x))
    rec(0,N,[],1); return num/comb(tot,N)


def deck_stats(path, o):
    lib = [n for n, q in names(path).items() for _ in range(q) if n != GORO]
    lands = [n for n in lib if "Land" in o[n]["type_line"]]
    src = {c: 0 for c in "UBR"}
    basic = {"U": "Island", "B": "Swamp", "R": "Mountain"}
    for n in lands:
        if n in FETCH_ALL or n in RAINBOW:
            for c in src:
                src[c] += 1
            continue
        for c in "UBR":
            if "{" + c + "}" in (o[n]["oracle_text"] or "") or basic[c] in o[n]["type_line"]:
                src[c] += 1
    non = [n for n in lib if n not in lands]
    curve = Counter(int(o[n]["cmc"]) for n in non)
    pips = Counter()
    for n in non:
        for c in "UBR":
            pips[c] += o[n]["mana_cost"].split(" // ")[0].count("{" + c + "}")
    return dict(lands=len(lands), sources=src, curve=dict(sorted(curve.items())), pips=dict(pips),
                avg=round(sum(o[n]["cmc"] for n in non) / len(non), 3),
                creatures=sum("Creature" in o[n]["type_line"] for n in lib),
                gc=sorted({n for n in lib if o[n]["game_changer"]}))


class GoroOracleAndList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.o = oracle()
        cls.base, cls.cand = names(BASE), names(CAND)

    def test_commander_oracle_anchor(self):
        g = self.o[GORO]
        self.assertEqual(g["mana_cost"], "{U}{B}{R}")
        self.assertEqual((g["power"], g["toughness"]), ("3", "4"))
        self.assertEqual(g["type_line"], "Legendary Creature \u2014 Goblin Human")
        self.assertIn("creatures you control that entered this turn deal combat damage to a player", g["oracle_text"])
        self.assertIn("5/5 red Dragon Spirit creature token with flying", g["oracle_text"])
        self.assertIn("{1}{R}: Creatures you control gain haste until end of turn.", g["oracle_text"])
        self.assertEqual((g["set"], g["released_at"], g["commander_legality"], g["game_changer"]),
                         ("moc", "2023-04-21", "legal", False))

    def test_add_and_cut_oracle_anchors(self):
        b = self.o["Bitterblossom"]
        self.assertEqual(b["mana_cost"], "{1}{B}")
        self.assertIn("At the beginning of your upkeep, you lose 1 life and create a 1/1 black Faerie Rogue creature token "
                      "with flying.", b["oracle_text"])
        self.assertIn("Enchantment", b["type_line"])
        n = self.o["Mist-Syndicate Naga"]
        self.assertIn("Ninjutsu {2}{U}", n["oracle_text"])
        # The Naga copy is created by a combat-damage trigger, i.e. after the damage event that would feed Goro (603.2).
        self.assertIn("Whenever this creature deals combat damage to a player, create a token that's a copy", n["oracle_text"])
        self.assertIn("Whenever a creature you control with flying enters, it gains haste", self.o["Dragon Tempest"]["oracle_text"])

    def test_exact_single_swap_singleton_100_and_identity(self):
        self.assertEqual(sorted((self.cand - self.base).elements()), ADDS)
        self.assertEqual(sorted((self.base - self.cand).elements()), CUTS)
        for lst in (self.base, self.cand):
            self.assertEqual(sum(lst.values()), 100)
            for n, q in lst.items():
                if q > 1:
                    self.assertEqual((n, q), ("Island", 2))
                self.assertEqual(self.o[n]["commander_legality"], "legal", n)
                self.assertTrue(set(self.o[n]["color_identity"]) <= set("UBR"), n)
        lines = CAND.read_text(encoding="utf-8").splitlines()
        self.assertEqual(lines[0], "1x Goro-Goro and Satoru [Commander]")
        self.assertEqual(lines[1:], sorted(lines[1:], key=lambda s: s.split(" ", 1)[1].lower()))

    def test_owner_direction_respected(self):
        for n in OWNER_ADDED:
            self.assertIn(n, self.cand, n)
        for n in OWNER_REMOVED:
            self.assertNotIn(n, self.cand, n)
        for keep in ("Bident of Thassa", "Grazilaxx, Illithid Scholar", "Frostcliff Siege", "Crumbling Necropolis",
                     "Fellwar Stone", "Dragon Tempest", "Terror of the Peaks", "Rogue's Passage", "Daring Piracy",
                     "Determined Iteration", "Loyal Apprentice", "Urabrask's Forge", "Enduring Curiosity"):
            self.assertIn(keep, self.cand, keep)

    def test_deck_stats_game_changers_lands_curve_pips(self):
        b, c = deck_stats(BASE, self.o), deck_stats(CAND, self.o)
        self.assertEqual(b["gc"], GAME_CHANGERS)
        self.assertEqual(c["gc"], GAME_CHANGERS)
        self.assertEqual((b["lands"], c["lands"]), (33, 33))
        self.assertEqual(b["sources"], {"U": 25, "B": 21, "R": 21})
        self.assertEqual(c["sources"], b["sources"])
        self.assertEqual(b["curve"], {1: 13, 2: 21, 3: 19, 4: 10, 5: 3})
        self.assertEqual(c["curve"], {1: 13, 2: 22, 3: 18, 4: 10, 5: 3})
        self.assertEqual((b["avg"], c["avg"]), (2.53, 2.515))
        self.assertEqual(b["pips"], {"U": 35, "B": 18, "R": 24})
        self.assertEqual(c["pips"], {"U": 34, "B": 19, "R": 24})
        self.assertEqual((b["creatures"], c["creatures"]), (31, 30))
        m = json.loads(MEASURED.read_text())["deck_stats"]
        self.assertEqual(m["baseline"]["sources_UBR"], b["sources"])
        self.assertEqual(m["candidate"]["sources_UBR"], c["sources"])
        self.assertEqual(m["candidate"]["game_changers"], GAME_CHANGERS)

    def test_opening_hand_hypergeometric(self):
        p24 = sum(comb(33, k) * comb(66, 7 - k) for k in range(2, 5)) / comb(99, 7)
        p14 = sum(comb(33, k) * comb(66, 7 - k) for k in range(1, 5)) / comb(99, 7)
        self.assertEqual((round(p24, 4), round(p14, 4)), (0.7069, 0.9083))

    def test_spellbook_same_five_combos(self):
        sb = json.loads(SPELLBOOK.read_text())
        for side in ("baseline", "candidate"):
            self.assertEqual(sorted(x["id"] for x in sb[side]["included"]), COMBOS, side)
            self.assertTrue(all("Breath of Fury" in x["uses"] for x in sb[side]["included"]), side)
        self.assertEqual((sb["baseline"]["almost_included_count"], sb["candidate"]["almost_included_count"]), (142, 138))


class PassCBoundedMeasuredTests(unittest.TestCase):
    def test_every_ledger_row_recomputed(self):
        rows = json.loads(MEASURED.read_text())["per_card_rows"]
        self.assertEqual(len(rows), 50)
        for r in rows:
            got = sim(r["card"], r["profile"], r["opponents"])
            for k in ("dragons_made", "dragons_on_board_end_T7", "cards_drawn_T3_T7", "life_end", "fliers_end"):
                self.assertEqual(got[k], r[k], (r["profile"], r["opponents"], r["card"], k))

    def test_bitterblossom_vs_naga_key_rows(self):
        d = lambda x, p, o: sim(x, p, o)["dragons_made"]
        lean = [(d("Bitterblossom", "lean", o), d("Mist-Syndicate Naga", "lean", o))
                for o in ("open", "flyer_wall", "removal", "sweeper", "extra")]
        eng = [(d("Bitterblossom", "engine", o), d("Mist-Syndicate Naga", "engine", o))
               for o in ("open", "flyer_wall", "removal", "sweeper", "extra")]
        self.assertEqual(lean, [(4, 2), (0, 2), (2, 1), (3, 2), (6, 3)])
        self.assertEqual(eng, [(8, 6), (4, 2), (5, 4), (6, 5), (11, 9)])
        self.assertEqual(sum(a > b for a, b in lean + eng), 9)
        self.assertEqual(sim("Bitterblossom", "lean", "open")["life_end"], 35)
        for o in ("open", "flyer_wall", "removal", "sweeper", "extra"):
            self.assertEqual(sim("Redoubled Stormsinger", "lean", o)["dragons_made"], 0, o)
        draws = [sim("Bident of Thassa", p, o)["cards_drawn_T3_T7"] for p in ("lean", "engine")
                 for o in ("open", "flyer_wall", "removal", "sweeper", "extra")]
        self.assertEqual((min(draws), max(draws)), (2, 23))

    def test_exact_castability_recomputed(self):
        m = json.loads(MEASURED.read_text())["castability"]
        base, cand = load(str(BASE)), load(str(CAND))
        self.assertEqual(base, cand)
        for key, cats in (("baseline", base), ("candidate", cand), ("alt_two_DragonskullSummit_over_CrumblingNecropolis",
                                                                       load(str(DRAGONSKULL)))):
            self.assertEqual((round(P(cats, 9, 3), 4), round(P(cats, 10, 3), 4)),
                             (m[key]["play_T3"], m[key]["draw_T3"]), key)
        nofell = dict(base)
        nofell[("R", "UBR")] -= 1
        nofell[("X", "")] += 1
        self.assertEqual((round(P(nofell, 9, 3), 4), round(P(nofell, 10, 3), 4)), (0.6452, 0.7254))
        self.assertEqual((m["baseline"]["play_T3"], m["baseline"]["draw_T3"]), (0.6668, 0.7456))
        self.assertEqual(m["alt_two_DragonskullSummit_over_CrumblingNecropolis"]["play_T3"], 0.6654)


if __name__ == "__main__":
    unittest.main()
