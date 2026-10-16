#!/usr/bin/env python3
"""Cache Commander Spellbook combo step text for every combo in the 62 Grixis lists (Bot cycle 48).

Reads the combo ids from data/grixis_combos.json (all decks, source and final lists) and fetches each
variant from the public API https://backend.commanderspellbook.com/variants/<id>/. Stores the step text
(`description`), prerequisites, mana needed, results and the retrieval date in
data/grixis_spellbook_steps.json. Commander Spellbook is community-maintained: its steps are a
documented line, not an official ruling. The interaction reviews (scripts/grixis_interactions.py)
quote these steps verbatim and check the quotes against this cache.

  python3 scripts/spellbook_steps.py            # fetch ids that are missing (existing entries kept)
  python3 scripts/spellbook_steps.py --refresh  # re-fetch everything
  python3 scripts/spellbook_steps.py --ids A B  # also fetch extra variant ids
  python3 scripts/spellbook_steps.py --check    # offline: every combo id in grixis_combos.json is cached
"""
import datetime, json, os, sys, time, urllib.error, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "grixis_spellbook_steps.json")
COMBOS = os.path.join(ROOT, "data", "grixis_combos.json")
API = "https://backend.commanderspellbook.com/variants/{}/"


def wanted():
    d = json.load(open(COMBOS))["decks"]
    return sorted({c["id"] for v in d.values() for c in v.get("combos", [])})


def load():
    if os.path.exists(OUT):
        return json.load(open(OUT))
    return {"_doc": "Commander Spellbook combo steps (community-maintained, not official rulings). "
                    "Written by scripts/spellbook_steps.py.", "source": API.format("<id>"), "variants": {}}


def fetch(vid):
    req = urllib.request.Request(API.format(vid), headers={"User-Agent": "GrokBotMTGCompanion/1.0"})
    for attempt in range(4):
        try:
            return json.load(urllib.request.urlopen(req, timeout=60))
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            time.sleep(3 * (attempt + 1))
        except Exception:
            time.sleep(3 * (attempt + 1))
    raise RuntimeError(f"could not fetch {vid}")


def compact(v, today):
    return {"cards": [u["card"]["name"] for u in v.get("uses", [])],
            "templates": [t["template"]["name"] for t in v.get("requires", [])],
            "produces": [p["feature"]["name"] for p in v.get("produces", [])],
            "mana_needed": v.get("manaNeeded", ""),
            "easy_prerequisites": v.get("easyPrerequisites", ""),
            "notable_prerequisites": v.get("notablePrerequisites", ""),
            "steps": v.get("description", ""),
            "notes": v.get("notes", ""),
            "status": v.get("status", ""),
            "url": f"https://commanderspellbook.com/combo/{v['id']}/",
            "retrieved": today}


def save(d):
    tmp = OUT + ".tmp"
    with open(tmp, "w") as f:
        json.dump(d, f, indent=1, ensure_ascii=False, sort_keys=True)
        f.write("\n")
    os.replace(tmp, OUT)


def main(a):
    d = load()
    ids = wanted()
    if "--check" in a:
        miss = [i for i in ids if i not in d["variants"]]
        print(f"spellbook steps: {len(d['variants'])} cached, {len(ids)} wanted, {len(miss)} missing")
        for i in miss[:20]:
            print("  - missing", i)
        return 1 if miss else 0
    if "--ids" in a:
        ids = sorted(set(ids) | set(a[a.index("--ids") + 1:]))
    today = datetime.date.today().isoformat()
    todo = ids if "--refresh" in a else [i for i in ids if i not in d["variants"]]
    gone = []
    for n, vid in enumerate(todo, 1):
        v = fetch(vid)
        if v is None:
            gone.append(vid)
            d["variants"][vid] = {"status": "not found", "retrieved": today, "url": f"https://commanderspellbook.com/combo/{vid}/"}
        else:
            d["variants"][vid] = compact(v, today)
        if n % 25 == 0:
            save(d)
            print(f"  {n}/{len(todo)}")
        time.sleep(0.3)
    d["retrieved"] = today
    save(d)
    print(f"spellbook steps: {len(d['variants'])} cached ({len(todo)} fetched, {len(gone)} not found)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
