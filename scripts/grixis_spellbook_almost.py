#!/usr/bin/env python3
"""Spellbook near-miss snapshot for M5 candidate universes (Bot cycle 60).

Posts each canonical list (commanders + main) to Commander Spellbook find-my-combos and keeps
the `almostIncluded` variants (every piece but one already in the list) whose missing piece is
in the deck's colour identity.  Read-only query; the result is stored in
data/grixis/candidates/spellbook_almost.json so offline rebuilds are deterministic.

  python3 scripts/grixis_spellbook_almost.py --online   # refresh (network)
  python3 scripts/grixis_spellbook_almost.py --check    # schema-ish sanity of the snapshot
"""
import datetime, hashlib, json, pathlib, sys, time
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
OUT = ROOT / "data" / "grixis" / "candidates" / "spellbook_almost.json"


def deck_names(slug, R):
    import grixis_authority as ga
    cmd, main = [], []
    for zone, oid, qty, name in ga.list_entries(ga.deck_block_text(slug), R):
        (cmd if zone == "commander" else main if zone == "main" else []).append(name)
    return cmd, main


def fetch():
    import grixis_authority as ga, evaluate_decklist as ev, detect_combos as dc
    R = ev.Resolver()
    out = {"source": "https://backend.commanderspellbook.com/find-my-combos", "field": "almostIncluded",
           "retrieved": datetime.date.today().isoformat(), "decks": {}}
    for did, v in sorted(ga.summary().items()):
        slug = v["slug"]
        cmd, main = deck_names(slug, R)
        res = dc.query(cmd, main)
        have = set(cmd) | set(main)
        rows = []
        for var in sorted(res.get("almostIncluded", []), key=lambda x: (len(x["uses"]), x["id"])):
            names = [u["card"]["name"] for u in var["uses"]]
            missing = [n for n in names if n not in have and n.split(" // ")[0] not in have]
            if len(missing) != 1:
                continue
            rows.append({"id": var["id"], "cards": names, "missing": missing[0],
                         "identity": var.get("identity"), "infinite": dc.infinite(var),
                         "produces": [p["feature"]["name"] for p in var["produces"]][:4],
                         "popularity": var.get("popularity"), "bracket_tag": var.get("bracketTag")})
        sig = hashlib.sha256("\n".join(sorted(cmd + main)).encode()).hexdigest()[:16]
        out["decks"][slug] = {"sig": sig, "n_almost_raw": len(res.get("almostIncluded", [])), "variants": rows}
        print(f"  {slug}: {len(rows)} near-miss variants", flush=True)
        time.sleep(1)
    OUT.write_text(json.dumps(out, separators=(",", ":"), sort_keys=True) + "\n")


def check():
    d = json.loads(OUT.read_text())
    bad = [s for s, v in d["decks"].items() if not isinstance(v.get("variants"), list) or any(len([r["missing"]]) != 1 for r in v["variants"])]
    if bad or not d.get("retrieved"):
        print("spellbook_almost: malformed", bad); return 1
    print(f"spellbook_almost OK: {len(d['decks'])} decks, {sum(len(v['variants']) for v in d['decks'].values())} near-miss variants (retrieved {d['retrieved']})")
    return 0


if __name__ == "__main__":
    if "--online" in sys.argv:
        fetch()
    sys.exit(check())
