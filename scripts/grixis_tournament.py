#!/usr/bin/env python3
"""M5 tournament evidence (Bot cycle 60.3): only for decks whose blueprint estimated ceiling is bracket 5 (cEDH).

Source: EDHTop16 public GraphQL API (https://edhtop16.com/api/graphql), read-only queries.  Per deck: the
commander's tournament stats (entries = sample size, top cuts, conversion rate) for WINDOWS, and for every M5
full-review candidate and its hypothesised cut the entries / top cuts / conversion with and without the card
(ONE_YEAR).  Observed tournament results are a derived_metric about other people's lists: never a simulation, never
a decision on their own (constraint 2), and not applicable to decks whose ceiling is below cEDH (M5 rule).

  python3 scripts/grixis_tournament.py --online   # fetch (network) into data/grixis/candidates/tournament/<slug>.json
  python3 scripts/grixis_tournament.py --check
"""
import datetime as dt, json, sys, time, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_authority as ga  # noqa: E402

API = "https://edhtop16.com/api/graphql"
OUT = ROOT / "data" / "grixis" / "candidates" / "tournament"
CANDS = ROOT / "data" / "grixis" / "candidates"
BPS = ROOT / "data" / "grixis" / "blueprints"
WINDOWS = ("ONE_YEAR", "SIX_MONTHS")
CARD_WINDOW = "ONE_YEAR"
BATCH = 20
NOTE = ("EDHTop16 aggregates reported cEDH tournament results (entries with and without a card, top cuts, conversion "
        "= top cuts / entries). Entries without a submitted decklist count as 'without' the card, so 'without' "
        "figures are upper bounds on non-play. Observational, confounded by pilot skill and meta: derived_metric only.")


def cedh_slugs():
    out = []
    for f in sorted(BPS.glob("*.json")):
        b = json.loads(f.read_text(encoding="utf-8"))
        v = ((b.get("power") or {}).get("grok_estimated_ceiling") or {}).get("value", {})
        if str(v.get("value") if isinstance(v, dict) else v) == "5":
            out.append(b["slug"])
    return out


def gql(q):
    req = urllib.request.Request(API, data=json.dumps({"query": q}).encode(), headers={"Content-Type": "application/json",
                                                                                       "User-Agent": "GrokBotMTGCompanion/1.0"})
    for i in range(3):
        try:
            return json.load(urllib.request.urlopen(req, timeout=60))
        except Exception:
            if i == 2:
                raise
            time.sleep(3)


def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def fetch():
    summ = {v["slug"]: v for v in ga.summary().values()}
    today = dt.date.today().isoformat()
    for slug in cedh_slugs():
        v = summ[slug]
        name = " / ".join(sorted(v["commanders"]))
        win = " ".join(f'{w}: stats(filters:{{timePeriod:{w}}}) {{ count topCuts conversionRate metaShare }}' for w in WINDOWS)
        r = gql(f'{{ commander(name:"{esc(name)}") {{ name colorId {win} }} }}')
        cmd = (r.get("data") or {}).get("commander")
        doc = {"schema_version": 1, "slug": slug, "source": API, "commander_query": name, "retrieved": today, "class": "derived_metric",
               "note": NOTE, "card_window": CARD_WINDOW}
        if not cmd or not cmd.get("ONE_YEAR") or not cmd["ONE_YEAR"].get("count"):
            doc.update({"status": "no_data", "sample_size": 0, "window": CARD_WINDOW, "commander": None, "cards": {}})
        else:
            import grixis_candidates as gc
            cf = gc.load(slug)
            names = sorted({c["card"] for c in cf["candidates"] if c["full_review"]} | {c["review"]["cut"] for c in cf["candidates"]
                                                                                     if c["full_review"] and c["review"].get("cut")})
            cards = {}
            for i in range(0, len(names), BATCH):
                part = names[i:i + BATCH]
                body = " ".join(f'c{j}: cardWinrateStats(cardName:"{esc(n)}", timePeriod:{CARD_WINDOW}) '
                                f'{{ withCard {{ totalEntries topCuts conversionRate }} withoutCard {{ totalEntries topCuts conversionRate }} }}'
                                for j, n in enumerate(part))
                rr = gql(f'{{ commander(name:"{esc(name)}") {{ {body} }} }}')
                got = (rr.get("data") or {}).get("commander") or {}
                for j, n in enumerate(part):
                    x = got.get(f"c{j}")
                    if x:
                        cards[n] = {k: {"entries": x[k]["totalEntries"], "top_cuts": x[k]["topCuts"],
                                        "conversion": None if x[k]["conversionRate"] is None else round(x[k]["conversionRate"], 4)}
                                    for k in ("withCard", "withoutCard") if x.get(k)}
                time.sleep(1)
            doc.update({"status": "collected", "sample_size": cmd["ONE_YEAR"]["count"], "window": CARD_WINDOW,
                        "commander": {"name": cmd["name"], "color_id": cmd.get("colorId"),
                                      "windows": {w: {k: (round(x, 4) if isinstance(x, float) else x) for k, x in cmd[w].items()} for w in WINDOWS}},
                        "list_hash": cf["list_hash"], "cards": cards})
        (OUT / f"{slug}.json").write_text(json.dumps(doc, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
        print(f"  {slug}: {doc['status']}, sample {doc['sample_size']}, {len(doc['cards'])} card rows", flush=True)
        time.sleep(1)


def check(verbose=True):
    p = []
    want = set(cedh_slugs())
    have = {f.stem for f in OUT.glob("*.json")}
    for s in sorted(want - have):
        p.append(f"{s}: cEDH-ceiling deck without tournament evidence (run --online)")
    for s in sorted(have - want):
        p.append(f"{s}: tournament evidence for a deck whose ceiling is below cEDH (M5 rule: not applicable)")
    for s in sorted(have & want):
        d = json.loads((OUT / f"{s}.json").read_text(encoding="utf-8"))
        for k in ("retrieved", "sample_size", "window", "status", "class"):
            if d.get(k) is None:
                p.append(f"{s}: missing {k}")
        if d.get("class") != "derived_metric":
            p.append(f"{s}: tournament evidence must be class derived_metric")
    if verbose:
        print(f"tournament: {len(have & want)}/{len(want)} cEDH-ceiling deck(s) with evidence; {len(p)} problem(s)")
        for x in p:
            print("  -", x)
    return p


if __name__ == "__main__":
    if "--online" in sys.argv:
        fetch()
    sys.exit(1 if check() else 0)
