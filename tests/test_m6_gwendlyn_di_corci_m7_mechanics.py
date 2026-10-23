"""Finite source-anchored rules/mana cases for the Gwendlyn Di Corci M7 research candidate.

No randomness. Gwendlyn Di Corci is modelled exactly as printed (current Oracle in the M7 snapshot): {U}{B}{B}{R} 3/5
Legendary Creature - Human Rogue; "{T}: Target player discards a card at random. Activate only during your turn."
Rules anchors: 602.5d (activation restriction), 605.1a (an ability with a target is not a mana ability, so Illusionist's
Bracers copies Gwendlyn's ability), 614.1a (Dauthi Voidwalker's "instead" is a replacement effect: an opponent's
discarded or sacrificed card never reaches the graveyard, so Tergrid, God of Fright ("from a graveyard"; ruling
2021-02-05), Tinybones, Bauble Burglar ("exile it from their graveyard") and Bloodchief Ascension ("put into an
opponent's graveyard") get nothing, while discard triggers still fire, ruling 2021-06-18), 701.9a/b (random discard).

This is a bounded, fully scripted rules model, NOT a game engine, simulation or win-rate measurement; it supports no
improvement claim by itself. PassCBoundedMeasuredTests re-runs the bounded finite version of the M6 Pass C request
(baseline Magewright's Stone vs +Aphetto Alchemist -Magewright's Stone across 9 fixed states), the exact no-tutor
assembly odds, the Hymn to Tourach vs Dauthi Voidwalker exact-expectation ledger (fractions), the Rings of
Brighthearth mana arithmetic, and exact hypergeometric paid-{U}{B}{B}{R} castability. Matched opening hands and games
against opponents are NOT modelled.
"""
from collections import Counter
from fractions import Fraction as F
from math import comb
import itertools
import json
import re
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
D = "Gwendlyn_Di_Corci"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
CAND = ROOT / f"data/grixis/m7/candidate_lists/{D}.txt"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
RC = ROOT / "data/grixis/m7/research_challengers"
SPELLBOOK = RC / f"{D}_CommanderSpellbook_20261023.json"
MEASURED = RC / f"{D}_bounded_measured_tests_20261023.json"
SPRINGS = RC / f"{D}_challenge_SulfurousSprings_over_CrumblingNecropolis_20261023.txt"
GW = "Gwendlyn Di Corci"
ADDS = ["Hymn to Tourach"]
CUTS = ["Dauthi Voidwalker"]
GAME_CHANGERS = ["Ancient Tomb", "Chrome Mox", "Cyclonic Rift", "Demonic Tutor", "Fierce Guardianship", "Force of Will",
                 "Gamble", "Imperial Seal", "Lion's Eye Diamond", "Mystical Tutor", "Notion Thief", "Opposition Agent",
                 "Orcish Bowmasters", "Rhystic Study", "Tergrid, God of Fright // Tergrid's Lantern", "Underworld Breach",
                 "Vampiric Tutor"]
OWNER_REMOVED = ["Bone Miser", "Fell Specter", "Hypnotic Specter", "Sangromancer", "Feed the Swarm", "Megrim",
                 "Counterspell", "Burning Inquiry", "Winds of Change", "The Locust God"]
OWNER_ADDED = ["Mind Twist", "Illusionist's Bracers", "Pemmin's Aura", "Tinybones, Pocket Nuisance", "Withering Torment",
               "Minamo, School at Water's Edge"]
OWNER_KEPT = ["Lightning Greaves", "Thousand-Year Elixir", "Magewright's Stone", "Patriar's Seal", "Bottomless Pit",
              "Oppression", "Chains of Mephistopheles", "Notion Thief", "Waste Not", "Geth's Grimoire", "Liliana's Caress",
              "Tinybones, Trinket Thief", "Tinybones, Bauble Burglar", "Tergrid, God of Fright // Tergrid's Lantern",
              "Underworld Breach", "Yawgmoth's Will", "Kess, Dissident Mage", "Bloodchief Ascension"]
COMBOS = ["1368-2706-3518"]
FETCH_ALL = {"Polluted Delta", "Bloodstained Mire", "Scalding Tarn"}
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


# ---- exact castability model (identical to the generator that wrote the measured JSON) ----
from math import comb
from functools import lru_cache
ANY={'Command Tower','City of Brass','Mana Confluence','Exotic Orchard','Crumbling Necropolis',"Xander's Lounge",'Polluted Delta','Bloodstained Mire','Scalding Tarn','Fabled Passage','Arid Mesa','Marsh Flats'}
PAIR={'UB':{'Underground Sea','Watery Grave','Drowned Catacomb','Morphic Pool','Shipwreck Marsh','Underground River'},
 'BR':{'Badlands','Blood Crypt','Dragonskull Summit','Luxury Suite','Sulfurous Springs','Smoldering Marsh'},
 'UR':{'Volcanic Island','Steam Vents','Sulfur Falls','Shivan Reef','Stormcarved Coast','Training Center','Spirebluff Canal','Fiery Islet'}}
MONO={'Island':'U','Otawara, Soaring City':'U',"Minamo, School at Water's Edge":'U','Swamp':'B','Takenuma, Abandoned Mire':'B','Bojuka Bog':'B','Urborg, Tomb of Yawgmoth':'B','Mountain':'R'}
COLORLESS_L={'Ancient Tomb',"Rogue's Passage"}
ROCK2={'Arcane Signet':'UBR','Fellwar Stone':'UBR','Talisman of Creativity':'UR','Talisman of Dominance':'UB','Talisman of Indulgence':'BR'}
def load(p):
    cats={}
    for l in open(p):
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
    if nl+nr<4: return False
    best=False
    for L in set(itertools.combinations(sorted(lands),nl)):
        for R in set(itertools.combinations(sorted(rocks),nr)):
            srcs=list(L)+list(R)
            for perm in itertools.permutations(range(len(srcs)),4):
                if all(col in srcs[i] for col,i in zip('UBBR',perm)): return True
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

# ---- Pass C bounded state model (identical to the generator that wrote the measured JSON) ----
def acts(state):
    """Return (gwendlyn_activations, copies_per_activation, mana_spent, notes) for one turn under fixed rules."""
    s=state; mana=s['spare_mana']; notes=[]
    if not s['gwendlyn_ready']: return 0,1,0,['Gwendlyn absent/summoning sick with no haste: zero activations']
    copies=2 if s['bracers']=='gwendlyn' else 1
    n=1; spent=0
    if s['bracers']=='alchemist' and s['untapper']=='alchemist' and s['untapper_ready']:
        # self-untap loop: Alchemist untaps Gwendlyn, copy untaps Alchemist; repeat with no mana; bounded by hands
        if s.get('removal_on_alchemist_after_loops') is not None:
            k=s['removal_on_alchemist_after_loops']; n+=k; notes.append(f'opponent kills Alchemist after {k} loop(s); stack untaps already resolving still resolve')
        else:
            n=10**6; notes.append('unbounded untaps; capped by cards in hands (finite)')
    elif s['untapper']=='stone' and s['untapper_ready'] and mana>=1:
        n+=1; spent+=1; mana-=1; notes.append('Stone: {1} for one extra Gwendlyn untap')
    elif s['untapper']=='alchemist' and s['untapper_ready']:
        n+=1; notes.append('Alchemist (no Bracers on it): one free extra untap')
    elif s['untapper']=='alchemist' and not s['untapper_ready']:
        notes.append('Alchemist summoning sick: no untap this turn')
    if s.get('pemmin') :
        k=mana; n+=k; spent+=k; mana=0; notes.append(f'Pemmin: {k} blue for {k} extra untaps')
    return n,copies,spent,notes
def run(state):
    n,c,spent,notes=acts(state); cards=sum(state['opp_hands'])
    useful=min(n*c,cards)
    return dict(useful_discards=useful,activations_used=min(n,(cards+c-1)//c if c else 0) if cards else n,mana_spent_on_untaps=spent,notes=notes)

# ---- Hymn vs Dauthi exact-expectation ledger (identical to the generator) ----
def exp_perm(h, k, n):
    n = min(n, h)
    return F(n * k, h) if h else F(0)


def ledger_row(h, k, engine, dauthi):
    disc = min(h, 1) if dauthi else min(h, 3)
    perm = exp_perm(h, k, disc)
    v = {"discards": disc}
    if engine.startswith("Tergrid"):
        v["tergrid_reanimations_expected"] = str(0 if dauthi else perm)
    if engine.startswith("Tinybones"):
        v["stash_cards"] = 0 if dauthi else disc
    if engine.startswith("Bloodchief"):
        v["ascension_drain_life"] = 0 if dauthi else 2 * disc
    if engine.startswith("Liliana"):
        v["caress_life_loss"] = 2 * disc
    if engine == "Waste Not":
        v["waste_not_triggers"] = disc
    v["dauthi_void_cards_created"] = disc if dauthi else 0
    return v


def deck_stats(path, o):
    lib = [n for n, q in names(path).items() for _ in range(q) if n != GW]
    lands = [n for n in lib if "Land" in o[n]["type_line"].split(" // ")[0]]
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
    curve = Counter(min(int(o[n]["cmc"]), 7) for n in non)
    return dict(lands=len(lands), sources=src, curve={str(k): v for k, v in sorted(curve.items())},
                avg=round(sum(o[n]["cmc"] for n in non) / len(non), 3),
                creatures=sum("Creature" in o[n]["type_line"].split(" // ")[0] for n in lib),
                gc=sorted({n for n in lib if o[n]["game_changer"]}))


class GwendlynOracleAndList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.o = oracle()
        cls.base, cls.cand = names(BASE), names(CAND)

    def test_commander_oracle_anchor(self):
        g = self.o[GW]
        self.assertEqual(g["mana_cost"], "{U}{B}{B}{R}")
        self.assertEqual((g["power"], g["toughness"]), ("3", "5"))
        self.assertEqual(g["type_line"], "Legendary Creature \u2014 Human Rogue")
        self.assertEqual(g["oracle_text"], "{T}: Target player discards a card at random. Activate only during your turn.")
        self.assertEqual(sorted(g["color_identity"]), ["B", "R", "U"])
        self.assertEqual((g["commander_legality"], g["game_changer"]), ("legal", False))

    def test_add_and_cut_oracle_anchors_and_replacement_conflict(self):
        h = self.o["Hymn to Tourach"]
        self.assertEqual((h["mana_cost"], h["type_line"]), ("{B}{B}", "Sorcery"))
        self.assertEqual(h["oracle_text"], "Target player discards two cards at random.")
        d = self.o["Dauthi Voidwalker"]
        self.assertEqual(d["mana_cost"], "{B}{B}")
        self.assertIn("If a card would be put into an opponent's graveyard from anywhere, instead exile it with a void counter",
                      d["oracle_text"])
        # The owner-kept engines all read the graveyard, which Dauthi's replacement (614.1a) empties.
        self.assertIn("put that card from a graveyard onto the battlefield",
                      self.o["Tergrid, God of Fright // Tergrid's Lantern"]["oracle_text"])
        self.assertIn("exile it from their graveyard with a stash counter", self.o["Tinybones, Bauble Burglar"]["oracle_text"])
        self.assertIn("Whenever a card is put into an opponent's graveyard from anywhere",
                      self.o["Bloodchief Ascension"]["oracle_text"])
        # Bracers copies Gwendlyn's targeted (non-mana, 605.1a) ability; Aphetto untaps any artifact or creature.
        self.assertIn("if it isn't a mana ability, copy that ability", self.o["Illusionist's Bracers"]["oracle_text"])
        self.assertIn("{T}: Untap target artifact or creature.", self.o["Aphetto Alchemist"]["oracle_text"])
        self.assertIn("{1}, {T}: Untap target creature that has an activated ability with {T} in its cost.",
                      self.o["Magewright's Stone"]["oracle_text"])

    def test_exact_single_swap_singleton_100_and_identity(self):
        self.assertEqual(sorted((self.cand - self.base).elements()), ADDS)
        self.assertEqual(sorted((self.base - self.cand).elements()), CUTS)
        for lst in (self.base, self.cand):
            self.assertEqual(sum(lst.values()), 100)
            for n, q in lst.items():
                if q > 1:
                    self.assertIn((n, q), {("Island", 2), ("Mountain", 2), ("Swamp", 5)})
                self.assertEqual(self.o[n]["commander_legality"], "legal", n)
                self.assertTrue(set(self.o[n]["color_identity"]) <= set("UBR"), n)
        lines = CAND.read_text(encoding="utf-8").splitlines()
        self.assertEqual(lines[0], "1x Gwendlyn Di Corci [Commander]")
        self.assertEqual(lines[1:], sorted(lines[1:], key=lambda s: s.split(" ", 1)[1].lower()))

    def test_owner_direction_respected(self):
        for n in OWNER_ADDED + OWNER_KEPT:
            self.assertIn(n, self.cand, n)
        for n in OWNER_REMOVED + ["Aphetto Alchemist", "Battlemage's Bracers", "Mindcrank", "Mox Diamond"]:
            self.assertNotIn(n, self.cand, n)

    def test_deck_stats_game_changers_lands_curve(self):
        b, c = deck_stats(BASE, self.o), deck_stats(CAND, self.o)
        self.assertEqual(b["gc"], GAME_CHANGERS)
        self.assertEqual(c["gc"], GAME_CHANGERS)
        self.assertEqual((b["lands"], c["lands"]), (35, 35))
        self.assertEqual(b["sources"], {"U": 21, "B": 24, "R": 17})
        self.assertEqual(c["sources"], b["sources"])
        self.assertEqual(b["curve"], {"0": 3, "1": 12, "2": 20, "3": 22, "4": 4, "5": 3})
        self.assertEqual(c["curve"], b["curve"])
        self.assertEqual((b["avg"], c["avg"]), (2.328, 2.328))
        self.assertEqual((b["creatures"], c["creatures"]), (14, 13))
        m = json.loads(MEASURED.read_text())["deck_stats"]
        self.assertEqual(m["baseline"]["sources_UBR"], b["sources"])
        self.assertEqual(m["candidate"]["curve"], c["curve"])
        self.assertEqual(m["candidate"]["game_changers"], GAME_CHANGERS)

    def test_opening_hand_hypergeometric(self):
        p24 = sum(comb(35, k) * comb(64, 7 - k) for k in range(2, 5)) / comb(99, 7)
        p14 = sum(comb(35, k) * comb(64, 7 - k) for k in range(1, 5)) / comb(99, 7)
        self.assertEqual((round(p24, 4), round(p14, 4)), (0.7306, 0.9069))

    def test_spellbook_same_single_combo(self):
        sb = json.loads(SPELLBOOK.read_text())
        for side in ("baseline", "candidate"):
            self.assertEqual(sorted(x["id"] for x in sb[side]["included"]), COMBOS, side)
        self.assertEqual((sb["baseline"]["almost_included_count"], sb["candidate"]["almost_included_count"]), (52, 50))
        aph = sb["alternatives"][f"{D}_PassC_plus_AphettoAlchemist_minus_MagewrightsStone_20261023.txt"]
        self.assertIn("283-4091", [x["id"] for x in aph["included"]])


class PassCBoundedMeasuredTests(unittest.TestCase):
    def test_every_pass_c_state_recomputed(self):
        states = json.loads(MEASURED.read_text())["states"]
        self.assertEqual(len(states), 9)
        got = []
        for s in states:
            b, v = run(s["baseline_stone"]["setup"]), run(s["variant_alchemist"]["setup"])
            for side, r in (("baseline_stone", b), ("variant_alchemist", v)):
                for k in ("useful_discards", "activations_used", "mana_spent_on_untaps"):
                    self.assertEqual(r[k], s[side][k], (s["state"], side, k))
            got.append((b["useful_discards"], v["useful_discards"]))
        self.assertEqual(got, [(4, 4), (4, 9), (2, 1), (2, 2), (4, 3), (0, 0), (0, 0), (4, 21), (4, 5)])

    def test_exact_assembly_odds(self):
        p = json.loads(MEASURED.read_text())["exact_assembly_probabilities_no_tutors"]
        for n in (10, 11, 12, 14):
            self.assertEqual(round(comb(97, n - 2) / comb(99, n), 4), p[f"cards_seen_{n}"]["two_specific_cards"])
            self.assertEqual(round(1 - comb(98, n) / comb(99, n), 4), p[f"cards_seen_{n}"]["specific_card"])

    def test_hymn_vs_dauthi_ledger_recomputed(self):
        led = json.loads(MEASURED.read_text())["hymn_vs_dauthi_bounded_ledger"]
        self.assertEqual(len(led["rows"]), 36)
        for r in led["rows"]:
            h, k, e = r["opp_hand"], r["opp_permanent_cards_in_hand"], r["engine_on_board"]
            self.assertEqual(ledger_row(h, k, e, True), r["baseline_Dauthi_Voidwalker"], (h, k, e))
            self.assertEqual(ledger_row(h, k, e, False), r["candidate_Hymn_to_Tourach"], (h, k, e))
        t = ledger_row(7, 3, "Tergrid, God of Fright // Tergrid's Lantern", False)
        self.assertEqual((t["discards"], F(t["tergrid_reanimations_expected"])), (3, F(9, 7)))
        self.assertEqual(ledger_row(7, 3, "Tinybones, Bauble Burglar", True)["stash_cards"], 0)
        self.assertEqual(ledger_row(7, 3, "Bloodchief Ascension (3+ quest counters)", False)["ascension_drain_life"], 6)
        self.assertEqual(ledger_row(0, 0, "none", False)["discards"], 0)
        verdicts = [a["verdict"].split(" ")[0] for a in led["adversarial"]]
        self.assertEqual(sorted(verdicts), ["CANDIDATE_GAIN"] * 2 + ["CANDIDATE_LOSS"] * 3)

    def test_rings_mana_arithmetic(self):
        rows = json.loads(MEASURED.read_text())["hymn_vs_dauthi_bounded_ledger"]["rings_over_dauthi_comparison"]["rows"]
        for r in rows:
            m = r["spare_mana_after_gwendlyn_turn"]
            self.assertEqual(r["rings_extra_discards_per_turn_once_resolved"], m // 2)
            self.assertEqual(r["hymn_one_shot_extra_discards"], 2 if m >= 2 else 0)
        self.assertEqual(min(r["spare_mana_after_gwendlyn_turn"] for r in rows
                             if r["rings_extra_discards_per_turn_once_resolved"] > r["hymn_one_shot_extra_discards"]), 6)

    def test_exact_castability_recomputed(self):
        m = json.loads(MEASURED.read_text())["castability"]
        base, cand, spr = load(str(BASE)), load(str(CAND)), load(str(SPRINGS))
        self.assertEqual(base, cand)
        self.assertEqual((round(P(base, 10, 4), 4), round(P(base, 11, 4), 4)), (m["baseline"]["play_T4"], m["baseline"]["draw_T4"]))
        self.assertEqual((m["baseline"]["play_T4"], m["candidate"]["play_T4"]), (0.511, 0.511))
        self.assertEqual(round(P(spr, 10, 4), 4), m["challenge_SulfurousSprings_over_CrumblingNecropolis"]["play_T4"])
        self.assertEqual(m["challenge_SulfurousSprings_over_CrumblingNecropolis"]["play_T4"], 0.5094)


if __name__ == "__main__":
    unittest.main()
