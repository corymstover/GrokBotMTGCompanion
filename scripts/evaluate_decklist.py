#!/usr/bin/env python3
"""Evaluate any Commander decklist against this repo's card DB (Bot cycle 16; generalized from the Grixis import).

Works for every color identity. Input: a text list in Archidekt/Moxfield style, one card per line:
  1x Card Name (set) 123 [Tag]     2 Island     1x Commander Name [Commander{top}]    1x Lutri, the Spellchaser [Companion]
Lines tagged Commander are the commander(s); a [Companion] line is checked but not counted in the 100.
Hard checks (facts, Scryfall oracle bulk in .cache/): name resolution, commander eligibility (CR 903.3)
and pairing, exactly 100 cards (903.5a), singleton with Oracle copy exceptions such as "A deck can have
any number of cards named …" (903.5b), color identity (903.5c), Commander legality/bans, companion.
Bracket inputs: Game Changers, extra-turn cards, mass land denial, and (with --combos) Commander
Spellbook two-card infinites → minimum bracket. See "EDH Deck Evaluation Checklist.md" for the full method.
Usage: python3 scripts/evaluate_decklist.py LIST.txt [--combos] [--json]
"""
import csv, json, re, sys, unicodedata
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import ingest_scryfall as ing  # noqa: E402

MLD = re.compile(r"destroy all (nonbasic )?lands|each player sacrifices [^.]*lands|lands don't untap", re.I)
LINE = re.compile(r"^(\d+)x?\s+(.+?)(?:\s+\(([^)]+)\)\s+(\S+))?(?:\s+\*[A-Z]\*)?\s*(?:\[(.*)\])?\s*$")
HARD = ("banned", "not Commander-legal", "color identity", "deck size", "singleton", "unresolved name",
        "commander eligibility", "commander pairing", "unparseable line")
WORDS = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}


def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", s.lower())


def parse(text):
    out = []
    for raw in text.splitlines():
        l = raw.strip()
        if not l or l.startswith(("#", "//")) or l.lower() in ("deck", "commander", "sideboard", "companion"):
            continue
        m = LINE.match(l)
        if not m:
            out.append({"raw": l, "bad": True}); continue
        q, name, st, cn, tags = m.groups()
        out.append({"qty": int(q), "name": name.strip(), "set": st, "cn": cn, "tags": tags or "", "raw": l})
    return out


class Resolver:
    """Exact name → card, full names before face names, paper cards before digital-only Alchemy faces."""
    def __init__(self):
        cards, self.bulk = ing.get_bulk(ing.DEFAULT_CACHE, None)
        uni = sorted((c for c in cards if c.get("layout") not in ing.EXCLUDED_LAYOUTS), key=lambda c: 0 if ing.in_universe(c) else 1)
        self.exact, self.fuzzy = {}, {}
        for c in uni:
            self.exact.setdefault(c["name"], c); self.fuzzy.setdefault(norm(c["name"]), c)
        for c in uni:
            for f in c.get("card_faces") or []:
                self.exact.setdefault(f["name"], c); self.fuzzy.setdefault(norm(f["name"]), c)
        self.by_oid = {c["oracle_id"]: c for c in uni}
        self.index = {r["oracle_id"]: r for r in csv.DictReader(ing.INDEX_CSV.open(encoding="utf-8"))}

    def get(self, name):
        c = self.exact.get(name)
        if c:
            return c, False
        c = self.fuzzy.get(norm(name))
        return c, bool(c)


def oracle(c):
    return c.get("oracle_text") or "\n".join(f.get("oracle_text", "") for f in c.get("card_faces") or [])


def check(text, R):
    """Return dict(commanders, ci, total, cards, issues) for one list."""
    issues, cmdrs, main_, comp = [], [], [], []
    for e in parse(text):
        if e.get("bad"):
            issues.append({"type": "unparseable line", "card": e["raw"], "detail": "line not in `Nx Name` form"}); continue
        c, fuzzy = R.get(e["name"])
        if fuzzy:
            issues.append({"type": "name normalized", "card": e["name"], "detail": f"resolved to Scryfall name “{c['name']}”"})
        if not c:
            issues.append({"type": "unresolved name", "card": e["name"], "detail": "no Scryfall card with this name (unreleased/custom?)"})
        e["card"] = c
        t = e["tags"].lower()
        (cmdrs if "commander" in t else comp if "companion" in t else main_).append(e)
    ci = set()
    for e in cmdrs:
        if e["card"]:
            ci |= set(e["card"].get("color_identity", []))
    total = sum(e["qty"] for e in cmdrs + main_)
    if total != 100:
        issues.append({"type": "deck size", "card": "—", "detail": f"{total} cards in commander + main deck (CR 903.5a needs 100)"})
    seen = {}
    for e in cmdrs + main_:
        if e["card"]:
            seen[e["card"]["name"]] = seen.get(e["card"]["name"], 0) + e["qty"]
    for n, q in seen.items():
        c = R.exact[n]
        allow = 10**6 if "Basic" in c.get("type_line", "") else 1
        m = re.search(r"A deck can have (any number of|up to (\w+)) cards named", oracle(c))
        if m:
            allow = 10**6 if m.group(1).startswith("any") else WORDS.get(m.group(2), 1)
        if q > allow:
            issues.append({"type": "singleton", "card": n, "detail": f"{q} copies (CR 903.5b)"})
    for e in cmdrs:
        if e["card"] and ing.commander_eligibility(e["card"]).startswith("No"):
            issues.append({"type": "commander eligibility", "card": e["card"]["name"], "detail": "not a legal commander (CR 903.3)"})
    if len(cmdrs) > 2:
        issues.append({"type": "commander pairing", "card": "—", "detail": f"{len(cmdrs)} commanders"})
    if len(cmdrs) == 2 and all(e["card"] for e in cmdrs):
        k = [set(e["card"].get("keywords") or []) for e in cmdrs]
        o = [oracle(e["card"]) for e in cmdrs]
        ok = (("Partner" in k[0] and "Partner" in k[1]) or ("Friends forever" in k[0] and "Friends forever" in k[1])
              or any("Partner with" in x for x in k) or any("Choose a Background" in x for x in k)
              or any("Doctor's companion" in x for x in k) or any("Background" in e["card"].get("type_line", "") for e in cmdrs)
              or all("Partner" in x for x in o))
        if not ok:
            issues.append({"type": "commander pairing", "card": " + ".join(e["card"]["name"] for e in cmdrs), "detail": "no shared pairing ability (CR 702.124)"})
    rows = []
    for e in cmdrs + main_ + comp:
        c = e["card"]
        if not c:
            continue
        leg = c.get("legalities", {}).get("commander")
        zone = "commander" if e in cmdrs else "companion" if e in comp else "main"
        if zone == "companion":
            issues.append({"type": "companion", "card": c["name"], "detail": f"companion outside the 100; Scryfall commander legality {leg}" +
                           ("; Lutri is banned as a companion in Commander (B&R 2026-02-09)" if c["name"].startswith("Lutri") else "")})
        elif leg != "legal":
            issues.append({"type": "banned" if leg == "banned" else "not Commander-legal", "card": c["name"], "detail": f"Scryfall commander legality: {leg}"})
        if not set(c.get("color_identity", [])) <= ci:
            issues.append({"type": "color identity", "card": c["name"], "detail": f"identity {''.join(c.get('color_identity', [])) or 'C'} not within commander {''.join(sorted(ci))} (CR 903.5c)"})
        r = R.index.get(c["oracle_id"])
        if not r:
            issues.append({"type": "not in card DB", "card": c["name"], "detail": "no entry in data/card_index.csv"})
        rows.append({"name": c["name"], "src_name": e["name"], "qty": e["qty"], "zone": zone, "tags": e["tags"],
                     "set": e.get("set"), "cn": e.get("cn"), "oracle_id": c["oracle_id"],
                     "ci": "".join(x for x in "WUBRG" if x in c.get("color_identity", [])) or "C",
                     "type": c.get("type_line", ""), "mv": c.get("cmc", 0), "gc": bool(c.get("game_changer")),
                     "legal": leg, "shard": r["shard"] if r else None, "anchor": r["anchor"] if r else None,
                     "xturn": "extra turn" in oracle(c).lower(), "mld": bool(MLD.search(oracle(c)))})
    return {"commanders": [e["card"]["name"] if e["card"] else e["name"] for e in cmdrs],
            "ci": "".join(x for x in "WUBRG" if x in ci), "total": total, "cards": rows, "issues": issues}


def bracket_floor(rows, two_card_infinites=0):
    gcs = [r["name"] for r in rows if r["gc"] and r["zone"] != "companion"]
    mld = [r["name"] for r in rows if r["mld"]]
    floor = 4 if (mld or len(gcs) > 3) else 3 if gcs else 2
    return (max(floor, 3) if two_card_infinites else floor), gcs, mld


def main():
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    if not a:
        sys.exit(__doc__)
    R = Resolver()
    res = check(Path(a[0]).read_text(encoding="utf-8-sig"), R)
    two = 0
    if "--combos" in sys.argv:
        import detect_combos as dc
        cs = dc.query([r["name"] for r in res["cards"] if r["zone"] == "commander"], [r["name"] for r in res["cards"] if r["zone"] == "main"])["included"]
        res["combos"] = [{"id": v["id"], "cards": [u["card"]["name"] for u in v["uses"]], "infinite": dc.infinite(v)} for v in cs]
        two = sum(1 for x in res["combos"] if len(x["cards"]) == 2 and x["infinite"])
    floor, gcs, mld = bracket_floor(res["cards"], two)
    res.update(bracket_floor=floor, game_changers=gcs, mass_land_denial=mld, extra_turns=[r["name"] for r in res["cards"] if r["xturn"]], bulk=R.bulk[:10])
    if "--json" in sys.argv:
        print(json.dumps(res, indent=1, ensure_ascii=False)); return 0
    hard = [i for i in res["issues"] if i["type"] in HARD]
    print(f"Commander(s): {' + '.join(res['commanders'])} · identity {res['ci'] or 'C'} · {res['total']} cards · Scryfall bulk {res['bulk']}")
    print("Hard checks: " + ("PASS" if not hard else f"FAIL ({len(hard)})"))
    for i in res["issues"]:
        print(f"  - [{i['type']}] {i['card']}: {i['detail']}")
    print(f"Game Changers ({len(gcs)}): {', '.join(gcs) or 'none'}")
    print(f"Extra turns: {', '.join(res['extra_turns']) or 'none'} · Mass land denial: {', '.join(mld) or 'none'}")
    if "combos" in res:
        print(f"Commander Spellbook: {len(res['combos'])} complete combos, {two} two-card infinite")
    print(f"Minimum bracket by the published barometers: {floor}" + ("" if "combos" in res else " (two-card combos not checked; add --combos)"))
    return 1 if hard else 0


if __name__ == "__main__":
    sys.exit(main())
