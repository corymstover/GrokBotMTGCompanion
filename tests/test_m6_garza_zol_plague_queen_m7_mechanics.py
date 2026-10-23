"""Finite source-anchored rules/mana cases for the Garza Zol, Plague Queen M7 research candidate.

No randomness. Garza Zol, Plague Queen is modelled exactly as printed (current Oracle in the M7 snapshot): {4}{U}{B}{R}
5/5 Legendary Creature - Vampire Noble; "Flying, haste / Whenever a creature dealt damage by Garza Zol this turn dies,
put a +1/+1 counter on Garza Zol. / Whenever Garza Zol deals combat damage to a player, you may draw a card." Rules
anchors: 510.4 (first-strike combat damage step), 702.4b/c (double strike), 702.7 (first strike), 702.2b/c
(deathtouch), 702.12b (indestructible), 702.19 (trample), 702.90b (infect), 704.5c/g/h (state-based actions), 120.3
(damage results), 702.151a (reconfigure), 712 (modal double-faced cards), 903.10a (21 commander damage).

This is a bounded rules/qualification-count model over fixed, enumerated single-combat states, NOT a game engine,
simulation or win-rate measurement; it supports no improvement claim by itself. PassCBoundedMeasuredTests recomputes the
bounded finite version of the M6 Pass C request for this deck (+Fireshrieker / -Inquisitor's Flail; double strike vs
damage doubling; removal between strike steps; ordinary, first-strike, deathtouch and indestructible blockers; infect,
Kediss and Curiosity; 7-mana access) and checks every recorded row. Matched opening hands and games against opponents are
NOT modelled (no validated Garza game model). Castability approximation disclosed: colours assumed satisfied, Ancient
Tomb counts 2, rocks are Signets/Talismans/Fellwar Stone (1), Sol Ring (2), Mana Vault/Grim Monolith (3).
"""
from collections import Counter
from math import comb
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
D = "Garza_Zol__Plague_Queen"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
CAND = ROOT / f"data/grixis/m7/candidate_lists/{D}.txt"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
RC = ROOT / "data/grixis/m7/research_challengers"
SPELLBOOK = RC / f"{D}_CommanderSpellbook_20261023.json"
MEASURED = RC / f"{D}_bounded_measured_tests_20261023.json"
GARZA = "Garza Zol, Plague Queen"
SINK = "Sink into Stupor // Soporific Springs"
FELL = "Fell the Profane // Fell Mire"
ADDS = sorted(["Lizard Blades", "Giantfall", SINK, FELL])
CUTS = sorted(["Fellwar Stone", "Rapid Hybridization", "Exotic Orchard", "Takenuma, Abandoned Mire"])
GAME_CHANGERS = ["Ancient Tomb", "Cyclonic Rift", "Demonic Tutor", "Fierce Guardianship", "Grim Monolith",
                 "Jeska's Will", "Mana Vault", "Rhystic Study", "Vampiric Tutor"]
OWNER_REMOVED = ["Lightning Greaves", "Embercleave", "Bident of Thassa", "Ophidian Eye", "Frantic Search",
                 "Waltz of Rage", "Go for the Throat", "Soul Shatter", "Sword of Truth and Justice",
                 "Viridian Longbow", "Gorgon's Head", "Unscythe, Killer of Kings", "Vorpal Sword"]
SETUP = {"none": 0, "Inquisitor's Flail": 4, "Fireshrieker": 5, "Lizard Blades": 4,
         "Inquisitor's Flail + Fireshrieker": 9, "Inquisitor's Flail + Lizard Blades": 8}
BLOCKERS = {"unblocked": None, "5/5 vanilla": dict(p=5, t=5), "2/2 flyer": dict(p=2, t=2),
            "5/5 first strike": dict(p=5, t=5, fs=True), "3/3 deathtouch": dict(p=3, t=3, dt=True),
            "5/5 indestructible": dict(p=5, t=5, ind=True), "8/8 vanilla": dict(p=8, t=8),
            "4/4 double strike": dict(p=4, t=4, fs=True, ds=True)}
EQ = ["none", "Inquisitor's Flail", "Fireshrieker", "Lizard Blades", "Inquisitor's Flail + Lizard Blades"]


def names(path):
    out = Counter()
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.strip():
            q, raw = line.split(" ", 1)
            out[raw.removesuffix(" [Commander]")] += int(q.rstrip("x"))
    return out


def oracle():
    return {c["name"]: c for c in json.loads(SNAP.read_text())["cards"]}


def combat(eq, blocker=None, collar=False, spike=False, exo=False, trample=False, removal_between=False,
           power_bonus=0, curiosity=False, kediss=False, opps=3):
    """One fully specified combat. Garza 5/5; damage doubled by Inquisitor's Flail (also damage dealt to her);
    double strike from Fireshrieker/Lizard Blades (702.4b); counter trigger resolves after the step's SBA check."""
    flail = "Flail" in eq
    ds = ("Fireshrieker" in eq) or ("Lizard Blades" in eq)
    P = 5 + power_bonus + (2 if exo else 0)
    T = 5 + (2 if exo else 0)
    counters = 0
    g = dict(dmg=0, poison=0, life=40, draws_garza=0, draws_curiosity=0, kediss_each_other=0, spike_loss=0,
             lifegain=0, garza_dies=False, blocker_dies=False)
    b = dict(blocker) if blocker else None
    gdmg = 0
    steps = ["fs", "reg"] if (ds or (b and b.get("fs"))) else ["reg"]
    for st in steps:
        if g["garza_dies"]:
            break
        if st == "reg" and removal_between and ds:
            break
        g_strikes = ds if st == "fs" else True
        b_strikes = b is not None and not b.get("dead") and (
            (st == "fs" and b.get("fs")) or (st == "reg" and (not b.get("fs") or b.get("ds"))))
        p = P + counters
        mult = 2 if flail else 1
        tough_now = T + counters
        to_player = to_blocker = 0
        if g_strikes:
            if b is None:
                to_player = p
            elif b.get("dead"):
                to_player = p if trample else 0
            else:
                lethal = 1 if (collar or spike) else max(b["t"] - b.get("dmg", 0), 0)
                if trample:
                    to_blocker = min(lethal, p)
                    to_player = p - to_blocker
                else:
                    to_blocker = p
        bd = b["p"] if b_strikes else 0
        if to_player:
            amt = to_player * mult
            if exo:
                g["poison"] += amt
            else:
                g["life"] -= amt
                g["dmg"] += amt
            g["draws_garza"] += 1
            if curiosity:
                g["draws_curiosity"] += 1 + (opps - 1 if kediss else 0)
            if kediss:
                g["kediss_each_other"] += amt
            if spike:
                half = -(-g["life"] // 2)
                g["spike_loss"] += half
                g["life"] -= half
            if collar:
                g["lifegain"] += amt
        if to_blocker:
            amt = to_blocker * mult
            if collar:
                g["lifegain"] += amt
            if exo:
                b["t_eff"] = b.get("t_eff", b["t"]) - amt
            b["dmg"] = b.get("dmg", 0) + amt
            hit = (collar or spike) or (exo and b.get("t_eff", b["t"]) <= 0) or b["dmg"] >= b["t"]
            if hit and not b.get("ind"):
                b["dead"] = True
                g["blocker_dies"] = True
                counters += 1
        if bd:
            gdmg += bd * (2 if flail else 1)
            if b.get("dt") or gdmg >= tough_now:
                g["garza_dies"] = True
    # A trigger that resolves after Garza has died puts no counter on her (she is no longer on the battlefield).
    g["garza_counters"] = 0 if g["garza_dies"] else counters
    g["commander_damage"] = g["dmg"]
    return g


def mana_categories(path, snap, mdfc_land):
    c = Counter()
    for n, q in names(path).items():
        if n == GARZA:
            continue
        faces = snap[n]["type_line"].split(" // ")
        if n == "Ancient Tomb":
            k = "T"
        elif "Land" in faces[0] or (mdfc_land and len(faces) > 1 and "Land" in faces[1]):
            k = "L"
        elif n == "Sol Ring":
            k = "R2"
        elif n in ("Mana Vault", "Grim Monolith"):
            k = "R3"
        elif "Signet" in n or "Talisman" in n or n == "Fellwar Stone":
            k = "R1"
        else:
            k = "X"
        c[k] += q
    assert sum(c.values()) == 99
    return c


def castable(c, T, need=7):
    """Exact hypergeometric P(at least `need` mana and two land drops by turn T on the play)."""
    keys = sorted(c)
    seen = 7 + T - 1
    total = 0

    def rec(i, left, acc, w):
        nonlocal total
        if i == len(keys):
            if left:
                return
            lands = min(acc.get("L", 0) + acc.get("T", 0), T)
            mana = lands + (1 if acc.get("T", 0) and lands >= 1 else 0)
            rocks = sorted([3] * acc.get("R3", 0) + [2] * acc.get("R2", 0) + [1] * acc.get("R1", 0),
                           reverse=True)[:max(T - 1, 0)]
            if mana + sum(rocks) >= need and lands >= 2:
                total += w
            return
        k = keys[i]
        for x in range(0, min(c[k], left) + 1):
            rec(i + 1, left - x, dict(acc, **{k: x}), w * comb(c[k], x))
    rec(0, seen, {}, 1)
    return round(total / comb(99, seen), 4)


class GarzaOracleAndDeltaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.o = oracle()
        cls.base = names(BASE)
        cls.cand = names(CAND)

    def test_commander_exact_oracle_legal_not_game_changer(self):
        g = self.o[GARZA]
        self.assertEqual(g["mana_cost"], "{4}{U}{B}{R}")
        self.assertEqual((g["power"], g["toughness"]), ("5", "5"))
        self.assertIn("Flying, haste", g["oracle_text"])
        self.assertIn("Whenever a creature dealt damage by Garza Zol this turn dies, put a +1/+1 counter",
                      g["oracle_text"])
        self.assertIn("Whenever Garza Zol deals combat damage to a player, you may draw a card.", g["oracle_text"])
        self.assertEqual(g["commander_legality"], "legal")
        self.assertIs(g["game_changer"], False)
        self.assertEqual((g["set"], g["released_at"]), ("csp", "2006-07-21"))

    def test_add_oracle_anchors(self):
        lb = self.o["Lizard Blades"]
        self.assertEqual((lb["mana_cost"], lb["power"], lb["toughness"]), ("{1}{R}", "1", "1"))
        self.assertIn("Equipped creature has double strike.", lb["oracle_text"])
        self.assertIn("Reconfigure {2}", lb["oracle_text"])
        gf = self.o["Giantfall"]
        self.assertIn("Target creature you control deals damage equal to its power to target creature an opponent "
                      "controls.", gf["oracle_text"])
        self.assertIn("Destroy target artifact.", gf["oracle_text"])
        self.assertIn("nonland permanent an opponent controls", self.o[SINK]["oracle_text"])
        self.assertIn("Destroy target creature or planeswalker.", self.o[FELL]["oracle_text"])
        for mdfc in (SINK, FELL):
            self.assertEqual(self.o[mdfc]["type_line"], "Instant // Land")
            self.assertIn("you may pay 3 life. If you don't, it enters tapped.", self.o[mdfc]["oracle_text"])
        self.assertIn("deals double that damage instead", self.o["Inquisitor's Flail"]["oracle_text"])
        self.assertIn("Equipped creature has double strike.", self.o["Fireshrieker"]["oracle_text"])

    def test_exact_four_swaps_singleton_identity_legality(self):
        self.assertEqual(sorted((self.cand - self.base).elements()), ADDS)
        self.assertEqual(sorted((self.base - self.cand).elements()), CUTS)
        self.assertEqual(sum(self.cand.values()), 100)
        self.assertTrue(all(q == 1 for q in self.cand.values()))
        for n in self.cand:
            self.assertEqual(self.o[n]["commander_legality"], "legal", n)
            self.assertTrue(set(self.o[n]["color_identity"]) <= set("UBR"), n)
        for n in OWNER_REMOVED:
            self.assertNotIn(n, self.cand, n)

    def test_game_changers_unchanged(self):
        for lst in (self.base, self.cand):
            self.assertEqual(sorted(n for n in lst if self.o[n]["game_changer"]), GAME_CHANGERS)

    def test_land_counts_and_mdfcs(self):
        def lands(lst):
            return sum(1 for n in lst if "Land" in self.o[n]["type_line"].split(" // ")[0])
        self.assertEqual(lands(self.base), 38)
        self.assertEqual(lands(self.cand), 36)
        mdfc = sorted(n for n in self.cand if " // " in self.o[n]["type_line"]
                      and "Land" in self.o[n]["type_line"].split(" // ")[1])
        self.assertEqual(mdfc, sorted([SINK, FELL]))

    def test_spellbook_same_three_combos(self):
        text = SPELLBOOK.read_text()
        for cid in ("3750-5039", "900-3750", "2822-3681"):
            self.assertIn(cid, text)


class PassCBoundedMeasuredTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = json.loads(MEASURED.read_text())
        cls.o = oracle()

    def test_every_combat_row_recomputes(self):
        rows = self.m["combat_rows"]
        self.assertEqual(len(rows), len(EQ) * len(BLOCKERS) * 3)
        for r in rows:
            cfg = r["config"]
            g = combat(r["equipment"], BLOCKERS[r["blocker"]], collar=cfg == "c_collar",
                       trample=cfg == "trample_shadowspear")
            for k in ("commander_damage", "garza_dies", "blocker_dies", "garza_counters", "draws_garza", "lifegain"):
                self.assertEqual(g[k], r[k], (r["equipment"], r["blocker"], cfg, k))
            self.assertEqual(r["setup_mana"], SETUP[r["equipment"]])

    def test_key_rows_double_strike_vs_flail(self):
        def row(eq, bl, cfg="a_bare"):
            return [r for r in self.m["combat_rows"]
                    if (r["equipment"], r["blocker"], r["config"]) == (eq, bl, cfg)][0]
        self.assertEqual([row(e, "unblocked")["commander_damage"] for e in EQ], [5, 10, 10, 10, 20])
        for bl in ("5/5 vanilla", "3/3 deathtouch", "4/4 double strike"):
            self.assertFalse(row("Lizard Blades", bl)["garza_dies"], bl)
            self.assertTrue(row("Lizard Blades", bl)["blocker_dies"], bl)
            self.assertTrue(row("none", bl)["garza_dies"], bl)
            self.assertTrue(row("Inquisitor's Flail", bl)["garza_dies"], bl)
        self.assertTrue(row("Lizard Blades", "5/5 first strike")["garza_dies"])
        self.assertTrue(row("Lizard Blades", "5/5 first strike")["blocker_dies"])
        self.assertTrue(row("Lizard Blades", "8/8 vanilla")["garza_dies"])
        self.assertTrue(row("Lizard Blades", "5/5 indestructible")["garza_dies"])
        self.assertFalse(row("Inquisitor's Flail + Lizard Blades", "8/8 vanilla")["garza_dies"])

    def test_special_rows_recompute(self):
        sp = {(s["equipment"], s["test"]): s for s in self.m["special_rows"]}
        self.assertEqual(len(sp), len(EQ) * 7)
        for eq in EQ:
            ck = combat(eq, None, curiosity=True, kediss=True)
            s = sp[(eq, "unblocked + Curiosity + Kediss (3 opponents)")]
            self.assertEqual((s["draws_garza"], s["draws_curiosity"], s["kediss_each_other"]),
                             (ck["draws_garza"], ck["draws_curiosity"], ck["kediss_each_other"]))
            spk = combat(eq, None, spike=True)
            s = sp[(eq, "unblocked + Quietus Spike (opp at 40)")]
            self.assertEqual((s["life"], s["spike_loss"]), (spk["life"], spk["spike_loss"]))
            ex = combat(eq, None, exo=True)
            self.assertEqual(sp[(eq, "unblocked + Grafted Exoskeleton infect (7 power)")]["poison"], ex["poison"])
            rm = combat(eq, None, removal_between=True)
            self.assertEqual(sp[(eq, "unblocked, instant removal on Garza after first-strike damage")]
                             ["commander_damage"], rm["commander_damage"])
            for pb in (0, 1, 5):
                cd = combat(eq, None, power_bonus=pb)["commander_damage"]
                s = sp[(eq, f"unblocked one-hit commander damage at power {5 + pb}")]
                self.assertEqual((s["commander_damage"], s["lethal_21"]), (cd, cd >= 21))
        # headline numbers quoted in the packet and PR body
        self.assertEqual(sp[("Lizard Blades", "unblocked + Curiosity + Kediss (3 opponents)")]["draws_curiosity"], 6)
        self.assertEqual(sp[("Inquisitor's Flail", "unblocked + Curiosity + Kediss (3 opponents)")]["draws_curiosity"], 3)
        self.assertEqual(sp[("Lizard Blades", "unblocked + Quietus Spike (opp at 40)")]["life"], 6)
        self.assertEqual(sp[("Inquisitor's Flail", "unblocked + Quietus Spike (opp at 40)")]["life"], 15)
        self.assertEqual(sp[("Lizard Blades", "unblocked, instant removal on Garza after first-strike damage")]
                         ["commander_damage"], 5)
        self.assertEqual(sp[("Inquisitor's Flail", "unblocked, instant removal on Garza after first-strike damage")]
                         ["commander_damage"], 10)
        self.assertTrue(sp[("Inquisitor's Flail + Lizard Blades", "unblocked one-hit commander damage at power 6")]
                        ["lethal_21"])

    def test_castability_recomputes_exactly(self):
        cast = self.m["castability"]
        files = {"base.txt": BASE, "cand.txt": CAND}
        for name in cast:
            if name not in files:
                files[name] = RC / name
        expect = {"base.txt": {"4": 0.1876, "5": 0.3093, "6": 0.4724}}
        for name, path in files.items():
            for mode, mdfc_land in (("mdfc_as_nonland", False), ("mdfc_as_land", True)):
                c = mana_categories(path, self.o, mdfc_land)
                got = {str(T): castable(c, T) for T in (4, 5, 6)}
                self.assertEqual(got, cast[name][mode], (name, mode))
        self.assertEqual(cast["base.txt"]["mdfc_as_land"], expect["base.txt"])
        self.assertEqual(cast["cand.txt"]["mdfc_as_land"], {"4": 0.1769, "5": 0.2882, "6": 0.4451})
        self.assertEqual(cast["cand.txt"]["mdfc_as_nonland"], {"4": 0.1649, "5": 0.2669, "6": 0.4073})

    def test_not_run_stated_plainly(self):
        self.assertIn("not run", self.m["not_run"]["matched_game_winrate"])
        self.assertIn("Robe of the Archmagi", self.m["pass_c_alternate_cuts"]["note"])
        self.assertIn("Quietus Spike", self.m["pass_c_alternate_cuts"]["note"])


if __name__ == "__main__":
    unittest.main()
