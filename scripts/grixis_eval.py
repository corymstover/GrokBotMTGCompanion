#!/usr/bin/env python3
"""Evaluate every decklist in the read-only Grixis source repo against this repo's card DB (Bot cycle 16).

Source: corymstover/grixis-commander-encyclopediaGPT (archived in grixis/source-archive/ since Bot cycle 45; a read-only clone path can be passed instead).
For each of its 62 decks picks the *current* list: the user-approved list named by
state/current_deck_overrides.json (matched by SHA-256, or by the deck's Card_Verification CSV),
else the frozen FINAL baseline from source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz.
Checks (facts from Scryfall oracle bulk in .cache/): name resolution, commander eligibility and
pairing, 100 cards (CR 903.5a), singleton with Oracle copy exceptions (903.5b), color identity
(903.5c), Commander legality/bans, companion legality, Game Changers, extra turns, mass land denial,
and Oracle text quoted in the source's verification CSVs vs current Oracle.
Writes data/grixis_eval.json.   Usage: python3 scripts/grixis_eval.py [SRC]
"""
import csv, glob, hashlib, json, sys, tarfile
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import ingest_scryfall as ing  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
# Bot cycle 45: default is the companion's own byte-identical source archive (single source of truth); a clone path still works.
SRC = Path(sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else Path(__file__).resolve().parent.parent / "grixis/source-archive/grixis-commander-encyclopediaGPT")


from evaluate_decklist import norm, parse, Resolver, check  # noqa: E402  (shared, any-identity evaluator)


def load_sources():
    tar = tarfile.open(SRC / "source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz")
    base = {}
    for m in tar.getmembers():
        if m.isfile() and m.name.endswith(".txt"):
            base[Path(m.name).stem] = tar.extractfile(m).read()
    st = json.load(open(SRC / "state/current_deck_overrides.json"))["decks"]
    files = {}
    for f in glob.glob(str(SRC / "refinement/decklists/*.txt")):
        files.setdefault(hashlib.sha256(open(f, "rb").read()).hexdigest(), []).append(f)
    decks = {}
    for did, raw in sorted(base.items()):
        rec = {"deck_id": did, "baseline_path": f"source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz → TXT/{did}.txt",
               "baseline_sha256": hashlib.sha256(raw).hexdigest()}
        key = next((k for k in st if norm(k) == norm(did)), None)
        s = st.get(key) if key else None
        text, path, how = raw.decode("utf-8-sig"), rec["baseline_path"], "baseline (deck not yet refined in the source repo)"
        if s and s.get("approval_status") == "APPROVED":
            rec["source_state"] = {k: s.get(k) for k in ("approval_status", "lock_status", "user_approval_date", "quality_gate_version", "approval_basis")}
            cand = [f for f in files.get(s["approved_list_sha256"], []) if "Approved" in f] or files.get(s["approved_list_sha256"], [])
            if s.get("approved_list_artifact") and (SRC / s["approved_list_artifact"]).exists():
                path, how = s["approved_list_artifact"], "approved list artifact (SHA-256 matches source state)"
            elif cand:
                path, how = str(Path(cand[0]).relative_to(SRC)), "approved list (matched by SHA-256 in source state)"
            else:
                ver = glob.glob(str(SRC / f"refinement/verification/**/Card_Verification_{key}_*.csv"), recursive=True)
                want = {}
                for r in csv.DictReader(open(ver[0])):
                    want[r["card_name_export"]] = want.get(r["card_name_export"], 0) + int(r["quantity"])
                for f in sorted(glob.glob(str(SRC / "refinement/decklists/*.txt"))):
                    got = {}
                    for e in parse(open(f).read()):
                        if not e.get("bad"):
                            got[e["name"]] = got.get(e["name"], 0) + e["qty"]
                    if got == want:
                        path, how = str(Path(f).relative_to(SRC)), f"approved list (card-for-card match with {Path(ver[0]).name}; hash differs only by file formatting)"
                        break
            if path != rec["baseline_path"]:
                text = (SRC / path).read_text(encoding="utf-8-sig")
        else:
            rec["source_state"] = {"approval_status": "UNREFINED (not in current-cycle approvals)"}
        rec.update(source_path=path, selection=how, text=text)
        decks[did] = rec
    return decks


def main():
    R = Resolver()
    bulk, uni, by_oid = R.bulk, list(R.by_oid.values()), R.by_oid
    decks = load_sources()
    out = {"bulk": bulk, "source_repo": "corymstover/grixis-commander-encyclopediaGPT", "decks": {}}
    for did, rec in decks.items():
        out["decks"][did] = {k: v for k, v in rec.items() if k != "text"} | check(rec["text"], R)
    # Oracle text recorded in the source repo's verification CSVs vs current Oracle
    stale, checked = {}, 0
    vfiles = sorted(glob.glob(str(SRC / "refinement/**/*Card_Verification*.csv"), recursive=True)) + \
        sorted(glob.glob(str(SRC / "refinement/tests/*Card_Audit*.csv")))
    vfiles += sorted(glob.glob(str(SRC / "refinement/metadata_audit/*Overlay*.csv")))
    jl = sorted(glob.glob(str(SRC / "refinement/metadata_audit/*Oracle_Cache*.jsonl")))
    def rows_of(f):
        if f.endswith(".jsonl"):
            return [json.loads(l) for l in open(f, encoding="utf-8") if l.strip()]
        return list(csv.DictReader(open(f, encoding="utf-8")))
    vfiles += jl
    for f in vfiles:
        for r in rows_of(f):
            ot, oid = r.get("oracle_text"), r.get("oracle_id")
            if not ot or not oid or oid not in by_oid:
                continue
            c = by_oid[oid]
            cur = c.get("oracle_text") or "\n".join(fc.get("oracle_text", "") for fc in c.get("card_faces") or [])
            checked += 1
            if norm(ot) != norm(cur) and norm(ot) not in norm(cur.replace("\n", " // ")):
                alt = " // ".join(fc.get("oracle_text", "") for fc in c.get("card_faces") or [])
                if norm(ot) == norm(alt):
                    continue
                stale.setdefault(c["name"], {"files": set(), "old": ot, "new": cur})["files"].add(str(Path(f).relative_to(SRC)))
    out["oracle_check"] = {"rows_checked": checked, "files": len(vfiles),
                           "stale": {k: {"files": sorted(v["files"]), "old": v["old"], "new": v["new"]} for k, v in sorted(stale.items())}}
    (ROOT / "data" / "grixis_eval.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
    for did, d in out["decks"].items():
        print(f"{did:38s} {d['source_state']['approval_status'][:10]:10s} total={d['total']} issues={[(i['type'], i['card']) for i in d['issues']]}")
    print("oracle rows checked", checked, "stale cards", len(stale), list(stale)[:20])


if __name__ == "__main__":
    main()
