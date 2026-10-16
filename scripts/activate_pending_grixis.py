#!/usr/bin/env python3
"""Activate Grixis decks published with `legality_status: pending` once their cards are Commander-legal (Bot cycle 38).

Registry: data/grixis_pending.json (deck id → status, legal_from, set, not-yet-legal cards). Steps:
  1. Live check: ask the Scryfall API (/cards/collection) for each pending card's Commander legality.
  2. Unless --check: refresh the cached Scryfall bulks the KB is built from
     (`ingest_scryfall.py --batch 0 --rulings-batch 0` = newest oracle-cards + rulings, card shards regenerated;
     newest default-cards for the printing-based checks).
  3. Re-check each pending deck's listed cards in the refreshed oracle bulk. A deck whose cards are all `legal`
     there is flipped to `status: active` (with the activation date and bulk date) in the registry.
  4. If any deck was flipped: rebuild `scripts/build_grixis.py` (the page loses its banner and joins the legal
     counts), `scripts/deck_calibration.py` and `scripts/rebuild_enrichment.sh` (which ends with validate_all).
Usage:
  python3 scripts/activate_pending_grixis.py --check   # read-only: live Scryfall legality + what would change
  python3 scripts/activate_pending_grixis.py           # refresh bulk, flip legal decks to active, rebuild, validate
Exit code: 0 = done or nothing to activate yet; 1 = a step failed; 2 = legal_from has passed but Scryfall still says
not legal (validate_all fails these decks until they are activated; re-run when Scryfall updates).
Then commit as a normal Bot cycle (branch, `gh pr create`, merge).
"""
import atomic_io  # noqa: F401  atomic Path.write_text (Bot cycle 34)
import datetime as dt
import json
import os
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = ROOT / "data" / "grixis_pending.json"
sys.path.insert(0, str(ROOT / "scripts"))
UA = {"User-Agent": "GrokBotMTGCompanion/1.0 (pending-legality check)", "Accept": "application/json", "Content-Type": "application/json"}


def live_legality(names):
    req = urllib.request.Request("https://api.scryfall.com/cards/collection", headers=UA, method="POST",
                                 data=json.dumps({"identifiers": [{"name": n} for n in names]}).encode())
    d = json.loads(urllib.request.urlopen(req, timeout=60).read())
    return {c["name"]: c.get("legalities", {}).get("commander") for c in d.get("data", [])}


def bulk_legality(names):
    import ingest_scryfall as ing
    os.environ["SCRYFALL_OFFLINE"] = "1"
    cards, bulk = ing.get_bulk(ing.DEFAULT_CACHE, None)
    by = {}
    for c in cards:
        by.setdefault(c["name"], c)
        for f in c.get("card_faces") or []:
            by.setdefault(f["name"], c)
    return {n: (by[n].get("legalities", {}).get("commander") if n in by else None) for n in names}, bulk


def run(cmd, env=None):
    print("$", " ".join(cmd), flush=True)
    return subprocess.run(cmd, cwd=ROOT, env=env).returncode == 0


def main():
    check = "--check" in sys.argv
    reg = json.loads(REG.read_text(encoding="utf-8"))
    pend = {k: v for k, v in reg["decks"].items() if v.get("status") == "pending"}
    if not pend:
        print("no pending decks"); return 0
    names = sorted({n for v in pend.values() for n in v["cards"]})
    try:
        live = live_legality(names)
        print("Scryfall API (live):", live)
    except Exception as ex:  # noqa: BLE001
        live = {}
        print("Scryfall API check failed:", ex)
    today = dt.date.today()
    if check:
        for did, v in pend.items():
            ok = all(live.get(n) == "legal" for n in v["cards"])
            print(f"{did}: legal_from {v['legal_from']} · live {'ALL LEGAL → would activate' if ok else 'not legal yet'}")
        return 0
    env = {k: v for k, v in os.environ.items() if k != "SCRYFALL_OFFLINE"}
    if not run([sys.executable, "scripts/ingest_scryfall.py", "--batch", "0", "--rulings-batch", "0"], env):
        return 1
    import ingest_scryfall as ing
    os.environ.pop("SCRYFALL_OFFLINE", None)
    ing.get_bulk(ing.DEFAULT_CACHE, None, "default-cards")  # newest printings bulk (old one replaced)
    leg, bulk = bulk_legality(names)
    print(f"cached oracle bulk {bulk}:", leg)
    flipped, late = [], []
    for did, v in pend.items():
        if all(leg.get(n) == "legal" for n in v["cards"]):
            v.update(status="active", activated=today.isoformat(), activated_bulk=bulk)
            flipped.append(did)
        elif dt.date.fromisoformat(v["legal_from"]) <= today:
            late.append(did)
    if flipped:
        REG.write_text(json.dumps(reg, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print("activated:", flipped)
        off = dict(os.environ, SCRYFALL_OFFLINE="1")
        for cmd in ([sys.executable, "scripts/build_grixis.py"], [sys.executable, "scripts/deck_calibration.py"], ["scripts/rebuild_enrichment.sh"]):
            if not run(cmd, off):
                return 1
    else:
        print("nothing to activate yet")
    if late:
        print(f"⚠️ legal_from has passed but Scryfall still lists these as not legal: {late}. validate_all fails them until activation; re-run later.")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
