#!/usr/bin/env python3
"""Phase 2/3 art-to-printing links from official story image labels (Batch 5, 2026-10-30).

Many recent official Magic Story pages label card art with an asset name such as
"0248_MTGFRA_MainPair: Koth, the Geomancer". This scans the cached official pages
(.cache/story/*/*.txt) for those labels and links each one to a Scryfall printing only
when the pinned default-cards snapshot has a paper English printing with
  set == the label's set code (lower-cased), collector_number == the label's number
  (leading zeros dropped), and a name (or face name) equal to the caption's card name.

Status per label (nothing is guessed):
  MATCHED              set, number and name all agree -> one exact printing. Commander-deck
                       labels (kind Cmdr*/Comm*) whose number and name agree in the set's Scryfall
                       commander companion set (set_type commander and set_name equal to the label
                       set's set_name + " Commander", e.g. Reality Fracture -> Reality Fracture
                       Commander) are MATCHED with set_resolution
                       "commander_companion_set"; all others use set_resolution "label_set"
  NAME_MISMATCH        that set/number exists but its name differs (recorded, not linked)
  NO_PRINTING          no paper English printing with that set/number in the snapshot
  NO_CAPTION_NAME      the label carries no ": Card Name" caption

Reality Fracture (FRA) is reported separately because that is where these labels are densest.
Only labels, card names, URLs, set codes, collector numbers, artists and Scryfall ids are stored.
Nothing here sets a lore grade or approves anything.

  python3 scripts/build_story_image_label_printings.py           # rebuild (needs .cache/story + snapshot)
  python3 scripts/build_story_image_label_printings.py --check   # self-hash + structure; full compare if caches exist
"""
import argparse
import glob
import gzip
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data/lore_research/story_image_label_printings_2026-10-30.json"
STORY = ROOT / ".cache/story"
SNAP = ROOT / ".cache/multiverse"
SCHEMA = "story-image-label-printings/v1"
STATUSES = ["MATCHED", "NAME_MISMATCH", "NO_PRINTING", "NO_CAPTION_NAME"]
LABEL = re.compile(r"^(?P<label>(?P<num>\d{3,4})_MTG(?P<set>[A-Z0-9]{2,5})_(?P<kind>[A-Za-z0-9_]+?))(?:: (?P<name>.+?))?\s*$")


def sha(body):
    return hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest()


def labels():
    pages = sorted(glob.glob(str(STORY / "*" / "*.txt")))
    if not pages:
        raise FileNotFoundError(".cache/story")
    seen, out = set(), []
    for p in pages:
        lines = Path(p).read_text(encoding="utf-8").split("\n")
        url = lines[0][5:] if lines[0].startswith("URL: ") else None
        if not url or not url.startswith("https://magic.wizards.com/"):
            continue
        for line in lines[1:]:
            m = LABEL.match(line.strip())
            if m and (url, m["label"], m["name"]) not in seen:
                seen.add((url, m["label"], m["name"]))
                out.append((url, line.strip(), m))
    return out


def snapshot_index(keys):
    """(set, number) -> printing for label sets, plus (parent set, number) -> printings in commander sets."""
    snaps = sorted(glob.glob(str(SNAP / "default-cards-*.jsonl.gz")))
    if not snaps:
        raise FileNotFoundError("default-cards snapshot")
    idx, by_set_name, commander_rows = {}, {}, []
    sets = {s for s, _ in keys}
    with gzip.open(snaps[-1], "rt", encoding="utf-8") as fh:
        for line in fh:
            c = json.loads(line)
            if c.get("lang") != "en" or "paper" not in c.get("games", []):
                continue
            if c["set"] in sets:
                by_set_name[c["set"]] = c["set_name"]
            k = (c["set"], c["collector_number"])
            if k in keys:
                idx[k] = c
            if c.get("set_type") == "commander" and c["set_name"].endswith(" Commander"):
                commander_rows.append(c)
    parent = {name + " Commander": code for code, name in by_set_name.items()}
    cmdr = {}
    for c in commander_rows:
        if c["set_name"] in parent:
            cmdr.setdefault((parent[c["set_name"]], c["collector_number"]), []).append(c)
    return Path(snaps[-1]).name, idx, cmdr


def names_of(c):
    return {c["name"]} | {f["name"] for f in c.get("card_faces", [])}


def build():
    found = labels()
    keys = {(m["set"].lower(), str(int(m["num"]))) for _, _, m in found}
    snap, idx, cmdr = snapshot_index(keys)
    rows = []
    for url, line, m in found:
        k = (m["set"].lower(), str(int(m["num"])))
        c = idx.get(k)
        name = m["name"]
        res = "label_set"
        if name and m["kind"].startswith(("Cmdr", "Comm")) and (c is None or name not in names_of(c)):
            alt = [x for x in cmdr.get(k, []) if name in names_of(x)]
            if len(alt) == 1:
                c, res = alt[0], "commander_companion_set"
        if not name:
            st = "NO_CAPTION_NAME"
        elif c is None:
            st = "NO_PRINTING"
        elif name in names_of(c):
            st = "MATCHED"
        else:
            st = "NAME_MISMATCH"
        row = {"url": url, "quote": line, "label": m["label"], "caption_name": name,
               "set": k[0], "collector_number": k[1], "status": st}
        if c is not None and st in ("MATCHED", "NAME_MISMATCH"):
            row["set_resolution"] = res
            row["printing"] = {"name": c["name"], "set": c["set"], "collector_number": c["collector_number"],
                               "artist": c.get("artist"), "released_at": c["released_at"], "scryfall_id": c["id"]}
        rows.append(row)
    rows.sort(key=lambda r: (r["set"], int(r["collector_number"]), r["url"], r["label"]))
    by_set = {}
    for r in rows:
        s = by_set.setdefault(r["set"], {x: 0 for x in STATUSES})
        s[r["status"]] += 1
    body = {"schema": SCHEMA, "snapshot": snap, "source_text_embedded": "single-line image labels only",
            "counts": {x: sum(r["status"] == x for r in rows) for x in STATUSES},
            "by_set": dict(sorted(by_set.items())),
            "pages_with_labels": len({r["url"] for r in rows}),
            "matched_printings": len({r["printing"]["scryfall_id"] for r in rows if r["status"] == "MATCHED"}),
            "labels": rows,
            "limitations": [
                "Only art that the official page labels with an asset name is covered; unlabelled art and art credited only by artist is not.",
                "A label's set code is Wizards' internal asset code; it is linked only when it agrees with a Scryfall set code, number and name. Disagreements are kept as NAME_MISMATCH or NO_PRINTING, never forced.",
                "A label shows which printing's art file the page used; it does not say the art depicts any particular story event.",
                "Grades, approvals and deck lists are unchanged."]}
    body["sha256"] = sha(body)
    return body


def structural_problems(d):
    p = []
    if d.get("schema") != SCHEMA:
        p.append("schema")
    if d.get("sha256") != sha({k: v for k, v in d.items() if k != "sha256"}):
        p.append("self-hash")
    for r in d.get("labels", []):
        if r["status"] not in STATUSES:
            p.append(f"status {r['status']}")
        if not r["url"].startswith("https://magic.wizards.com/"):
            p.append(f"non-Wizards url {r['url']}")
        if not r["quote"].startswith(r["label"]):
            p.append(f"quote/label mismatch {r['label']}")
        if r["status"] == "MATCHED" and (not r.get("printing") or r["caption_name"] not in r["quote"]):
            p.append(f"matched without printing {r['label']}")
        if r.get("printing") and r["printing"]["collector_number"] != r["collector_number"]:
            p.append(f"collector number drift {r['label']}")
        if r.get("set_resolution") == "commander_companion_set" and r["status"] != "MATCHED":
            p.append(f"companion set without match {r['label']}")
        if r["status"] in ("NO_PRINTING", "NO_CAPTION_NAME") and r.get("printing"):
            p.append(f"printing on unlinked label {r['label']}")
    if d.get("counts") != {x: sum(r["status"] == x for r in d.get("labels", [])) for x in STATUSES}:
        p.append("counts")
    return p


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    if a.check:
        d = json.loads(OUT.read_text(encoding="utf-8"))
        probs = structural_problems(d)
        try:
            if build() != d:
                probs.append("stale: rebuild differs")
        except FileNotFoundError as e:
            print(f"caches absent ({e}); structural check only")
        print("PASS" if not probs else "FAIL " + "; ".join(probs))
        return 1 if probs else 0
    d = build()
    OUT.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"counts": d["counts"], "by_set": d["by_set"], "pages": d["pages_with_labels"],
                      "matched_printings": d["matched_printings"]}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
