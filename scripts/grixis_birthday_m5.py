#!/usr/bin/env python3
"""Fresh Birthday M5 regeneration and frozen-M5 delta (Cycle 74).

This runner intentionally keeps the accepted development corpus immutable:
  * B-F structural evidence remains bound to snap-20261016.
  * A (candidate saturation) is regenerated from the exact current authority snapshot.
  * EDHREC/Spellbook/Scryfall screening inputs are current and hash-bound.
  * cEDH card-level EDHTop16 evidence is refreshed in a convergence loop because
    tournament rows can themselves create a Step-A escalation signal.
  * all outputs live under data/grixis/birthday_m5; data/grixis/m5_regen and the
    frozen A-F directories are read-only inputs.

No function in this file can accept/reject a swap, register a challenger, approve a
deck, or lock a deck.  The finished corpus is evidence for Cory's explicit M5 gate.
"""
from __future__ import annotations

import argparse
import copy
import datetime as dt
import gzip
import hashlib
import json
import os
import re
import shutil
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

# SCRYFALL_CACHE is set by the workflow before Python starts so evaluate_decklist's
# Resolver sees the same current cache as grixis_candidates.
import grixis_authority as ga  # noqa: E402
import grixis_candidates as gc  # noqa: E402
import grixis_evidence as ge  # noqa: E402
import grixis_m5_af as gaf  # noqa: E402
import grixis_saturation as gs  # noqa: E402
import grixis_tournament as gt  # noqa: E402

VERSION = 1
CYCLE = 74
AUTH = ROOT / "data/grixis/birthday_authority"
MANIFEST = AUTH / "manifest.json"
IMPACT = ROOT / "data/grixis/birthday_m5/impact.json"
EDH_CURRENT = AUTH / "edhrec_current.json.gz"
SPELLBOOK_CURRENT = AUTH / "spellbook_almost.json"
OUTROOT = ROOT / "data/grixis/birthday_m5"
EVID = OUTROOT / "evidence"
SAT = OUTROOT / "saturation"
CANDS = OUTROOT / "candidates"
TOUR = CANDS / "tournament"
REGEN = OUTROOT / "regen"
SUMMARY = OUTROOT / "summary.json"
DELTA = OUTROOT / "delta_vs_frozen_m5.json"
PROVENANCE = OUTROOT / "provenance.json"
FROZEN_M5 = ROOT / "data/grixis/m5_regen/candidates"
FROZEN_SUMMARY = ROOT / "data/grixis/m5_regen/summary.json"
FROZEN_SAT = ROOT / "data/grixis/saturation"
CACHE = Path(os.environ.get("SCRYFALL_CACHE", ROOT / ".cache/birthday-m5"))
TODAY = dt.date(2026, 10, 17)
NEW_SINCE = (TODAY - dt.timedelta(days=183)).isoformat()
MAX_TOURNAMENT_PASSES = 4

SAT_ESC = (
    "tier_a_score", "dependency_graph_alternative", "spellbook_near_miss_completion", "package_gap", "new_card",
    "unusual_oracle_interaction", "anomaly_source_disagreement", "human_evidence", "tournament_evidence",
    "multi_source_corroboration",
)
ga.ESCALATION_REASONS = tuple(sorted(set(ga.ESCALATION_REASONS) | set(SAT_ESC)))


def sha_bytes(b: bytes) -> str:
    return "sha256:" + hashlib.sha256(b).hexdigest()


def sha_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return "sha256:" + h.hexdigest()


def rel(p: Path) -> str:
    return str(p.relative_to(ROOT))


def read_gz_json(p: Path):
    return json.loads(gzip.decompress(p.read_bytes()).decode("utf-8"))


def write_gz_json(p: Path, doc) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    # Match candidate writer semantics: readable top-level JSON is not required for
    # deterministic comparison, only canonical content and gzip mtime=0.
    body = json.dumps(doc, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    p.write_bytes(gzip.compress(body, compresslevel=9, mtime=0))


def authority_manifest():
    if not MANIFEST.exists():
        raise SystemExit("fresh Birthday authority manifest missing")
    m = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if m.get("status") != "ready" or m.get("hard_blockers"):
        raise SystemExit(f"fresh Birthday authority not ready: {m.get('hard_blockers')}")
    if m.get("frozen_baseline", {}).get("snapshot_id") != "snap-20261016":
        raise SystemExit("fresh authority is not bound to snap-20261016")
    return m


def exact_current_bulk_files(m):
    src = m["sources"]["scryfall"]
    out = {}
    for kind in ("oracle-cards", "default-cards", "rulings"):
        rec = src[kind]
        p = CACHE / rec["file"]
        if not p.exists():
            raise SystemExit(f"missing exact fresh Scryfall artifact {p}")
        got = sha_file(p)
        if got != rec["sha256"]:
            raise SystemExit(f"fresh Scryfall hash mismatch {kind}: {got} != {rec['sha256']}")
        out[kind] = p
    return out


def freeze_digest(paths):
    rows = []
    for p in sorted(paths):
        rows.append((rel(p), sha_file(p)))
    return sha_bytes(json.dumps(rows, separators=(",", ":"), ensure_ascii=False).encode())


def frozen_digest():
    paths = [FROZEN_SUMMARY]
    paths += sorted(FROZEN_M5.glob("*.json.gz"))
    paths += sorted(FROZEN_SAT.glob("*.json")) + sorted(FROZEN_SAT.glob("*.json.gz"))
    # B-F evidence roots consumed by grixis_m5_af.
    for d in ("combo_quality", "power_core", "mana_base", "mana_timing", "mana_opportunity",
              "mana_resilience", "commander_mana", "commander_marginal", "bracket_stress",
              "bracket_stress_packets", "bracket_red_team"):
        paths += sorted((ROOT / "data/grixis" / d).glob("*.json"))
    return freeze_digest(paths)


def configure_paths():
    """Redirect mature engines to current-only outputs, leaving B-F untouched."""
    gc.CACHE = CACHE
    gc.EVID = EVID
    gc.ALMOST = SPELLBOOK_CURRENT
    gc.SATURATION = SAT
    gc.OUT = CANDS
    gc.WRITE_DIR = CANDS
    gc.TODAY = TODAY
    gc.NEW_SINCE = NEW_SINCE
    gc._CTX = None
    gc._ROLES.clear()

    gs.OUT = SAT
    gs.SNAPSHOT_DATE = TODAY.isoformat()
    gs._G.clear()

    gt.CANDS = CANDS
    gt.OUT = TOUR

    # Cycle-73 final triage rule: drain both Step-A work tiers.  This remains a
    # scripted screening review and does not become an M6 judgment review.
    def final_triage(D, keep, sat):
        esc = {n: sat[n]["escalation"] for n in keep if sat[n]["escalation"]}
        full = [n for n in keep if sat[n]["test_tier"] in ("paired_test", "escalated_queued")]
        return full, esc, []
    gc.triage = final_triage


def canonical_names(slug):
    names = set()
    for line in ga.deck_block_text(slug).splitlines():
        mm = re.match(r"^\s*(\d+)x?\s+(.+?)(?:\s+\[[^]]+\])?\s*$", line)
        if mm:
            names.add(mm.group(2).strip())
    return names


def prepare_evidence(m):
    """Materialize a minimal current M3-compatible EDHREC derivative layer."""
    current = read_gz_json(EDH_CURRENT)
    snap = m["snapshot_id"]
    EVID.mkdir(parents=True, exist_ok=True)
    counts = Counter()
    for slug, d in sorted(current["decks"].items()):
        pages = d.get("pages", [])
        method = d.get("method", "single_page")
        by = {}
        for page in pages:
            for n, row in page.get("rows", {}).items():
                if row.get("synergy") is None or not row.get("potential_decks"):
                    continue
                by.setdefault(n, []).append(row)
        vecs = []
        canon = canonical_names(slug)
        for n in sorted(by):
            row = ge.edh_row(by[n], method)
            if row is not None:
                vecs.append({"card": n, "status": "incumbent" if n in canon else "candidate", "edhrec": row})
        page_meta = [{"page": x.get("page"), "sha256": x.get("sha256"), "retrieved": current.get("retrieved")} for x in pages]
        payload = {
            "schema_version": 1, "deck_id": d.get("deck_id"), "slug": slug,
            "generated_by": f"scripts/grixis_birthday_m5.py v{VERSION}", "cycle": CYCLE, "date": TODAY.isoformat(),
            "edhrec": {"pages": page_meta, "method": method, "class": "derived_metric", "columns": ge.COLS,
                       "note": "Fresh Birthday EDHREC derivative. Community data informs screening and never decides."},
            "snapshot": {"id": sha_bytes(json.dumps({"birthday": snap, "pages": page_meta}, sort_keys=True).encode()),
                         "birthday_authority": snap, "source_artifact": rel(EDH_CURRENT), "source_sha256": sha_file(EDH_CURRENT)},
            "counts": {"vectors": len(vecs), "with_edhrec": len(vecs)}, "vectors": vecs,
        }
        (EVID / f"{slug}.json").write_text(json.dumps(payload, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
        counts["decks"] += 1; counts["vectors"] += len(vecs)
    if counts["decks"] != 62:
        raise SystemExit(f"fresh EDHREC evidence coverage {counts['decks']}/62")
    return dict(counts)


def rewrite_sat_snapshot(m):
    """Replace the legacy development-snapshot label in newly generated certificates only."""
    for p in SAT.glob("*.json"):
        d = json.loads(p.read_text(encoding="utf-8"))
        d["generated_by"] = f"scripts/grixis_saturation.py v{gs.VERSION} via grixis_birthday_m5.py v{VERSION}"
        d["cycle"] = "ChatGPT cycle 74 Birthday current A"
        d["snapshot"]["id"] = m["snapshot_id"]
        d["snapshot"]["frozen_structural_baseline"] = "snap-20261016"
        d["authority"]["note"] += " Current Birthday screening/discovery only; does not reopen frozen B-F or decide a swap."
        p.write_text(json.dumps(d, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def build_saturation_and_candidates(m, jobs=6):
    configure_paths()
    slugs = sorted(v["slug"] for v in ga.summary().values())
    # Force a fresh context each convergence pass because tournament rows may change.
    gc._CTX = None; gs._G.clear(); gc._ROLES.clear()
    gs.build(slugs, jobs=jobs)
    rewrite_sat_snapshot(m)
    # candidate builder reads the rewritten saturation files.
    gc._CTX = None
    gc.build(None, jobs=jobs)
    return review_targets()


def review_targets():
    out = {}
    for slug in gt.cedh_slugs():
        p = CANDS / f"{slug}.json.gz"
        if not p.exists():
            out[slug] = set(); continue
        d = json.loads(gzip.decompress(p.read_bytes()).decode("utf-8"))
        names = {c["card"] for c in d["candidates"] if c.get("full_review")}
        names |= {c["review"]["cut"] for c in d["candidates"] if c.get("full_review") and (c.get("review") or {}).get("cut")}
        out[slug] = names
    return out


def tournament_rows_present(targets):
    missing = {}
    for slug, names in targets.items():
        p = TOUR / f"{slug}.json"
        if not p.exists():
            missing[slug] = sorted(names); continue
        d = json.loads(p.read_text(encoding="utf-8"))
        if d.get("status") == "no_data":
            continue
        got = set((d.get("cards") or {}).keys())
        need = names - got
        if need:
            missing[slug] = sorted(need)
    return missing


def converge(m, jobs=6):
    """Candidate → tournament → candidate until every current review target has a current row."""
    configure_paths()
    history = []
    # Start with no current card rows; authority commander/meta files are not silently
    # copied because their cards maps are intentionally deferred/empty.
    if TOUR.exists():
        shutil.rmtree(TOUR)
    TOUR.mkdir(parents=True, exist_ok=True)
    targets = build_saturation_and_candidates(m, jobs)
    for i in range(1, MAX_TOURNAMENT_PASSES + 1):
        before = {s: sorted(v) for s, v in targets.items()}
        gt.fetch()
        probs = gt.check(verbose=False)
        if probs:
            raise SystemExit("fresh tournament evidence failed: " + "; ".join(probs))
        missing_before = tournament_rows_present(targets)
        # Missing rows after a successful fetch mean EDHTop16 returned no card object.
        # Keep the absence explicit but it is not an excuse to fabricate data.
        targets2 = build_saturation_and_candidates(m, jobs)
        missing = tournament_rows_present(targets2)
        changed = {s: sorted(targets2[s] ^ targets.get(s, set())) for s in targets2 if targets2[s] != targets.get(s, set())}
        history.append({"pass": i, "target_counts": {s: len(v) for s, v in targets2.items()},
                        "target_set_changes": changed,
                        "unreturned_rows_for_previous_targets": missing_before,
                        "missing_rows_for_current_targets": missing})
        # Stable target set and no missing rows for data-bearing commanders = convergence.
        if not changed and not missing:
            return history
        targets = targets2
    raise SystemExit(f"cEDH candidate/tournament loop did not converge in {MAX_TOURNAMENT_PASSES} passes")


def current_af(slug, rid, canonical_hash, pool):
    """Fresh A + frozen B-F evidence envelope."""
    af = gaf.DeckAFEvidence(slug, rid, canonical_hash, pool)
    ap = SAT / f"{slug}.json"
    ad = json.loads(ap.read_text(encoding="utf-8"))
    if ad.get("list_hash") != canonical_hash or ad.get("snapshot", {}).get("id") != authority_manifest()["snapshot_id"]:
        raise ValueError(f"{slug}: current A saturation binding mismatch")
    af.paths["A_saturation"] = ap
    af.docs["A_saturation"] = ad
    return af


def integrate_doc(doc, af, m):
    swap_by = {sw["id"]: sw for sw in doc["swaps"]}
    sat_ref = f"saturation:{rel(SAT / (doc['slug'] + '.json'))}"
    for rec in doc["candidates"]:
        if rec["escalation"]["escalated"]:
            rec["escalation"]["evidence_refs"] = sorted(set(rec["escalation"]["evidence_refs"] + [sat_ref + "#candidate=" + rec["card"]]))
            rec["escalation"]["by"] = f"script:grixis_saturation.py v{gs.VERSION}; drained by grixis_birthday_m5.py v{VERSION}"
            rec["escalation"]["note"] = "Fresh Birthday Step-A escalation; all paired_test/escalated_queued work is drained as screening review."
        rv = rec.get("review")
        if not rv:
            continue
        facts = rec.get("screening", {}).get("facts", {})
        ids = [x for x in (rv.get("swap"), (rv.get("elevated_alternative") or {}).get("swap")) if x]
        hypotheses = []
        for sid in ids:
            sw = swap_by[sid]
            tid = sw["tests"][0] if sw.get("tests") else None
            hypotheses.append(af.swap_envelope(sw["cuts"][0], sw["adds"][0], facts, tid))
        rv["a_f_evidence"] = af.review_envelope(rec["card"], facts, hypotheses)

    afc = af.deck_context()
    afc["authority"]["note"] += " Layer A is fresh Birthday saturation; B-F refs remain frozen snap-20261016 structural evidence."
    afc["fresh_authority_snapshot"] = m["snapshot_id"]
    afc["structural_baseline"] = "snap-20261016"
    afc["A"]["snapshot"] = m["snapshot_id"]
    doc["a_f_context"] = afc
    doc["triage"]["escalated_queued"] = []
    doc["triage"]["default_rule"] = (
        "Birthday current M5: fully review every fresh Step-A paired_test and escalated_queued candidate; screen_only remains in full legal-pool universe."
    )
    doc["universe"]["full_review_rule"] = doc["triage"]["default_rule"]
    doc["snapshot"]["birthday_authority"] = m["snapshot_id"]
    doc["snapshot"]["structural_baseline"] = "snap-20261016"
    doc["snapshot"]["a_f_digest"] = afc["digest"]
    sid = sha_bytes(json.dumps({"candidate_snapshot": doc["snapshot"]["id"], "birthday": m["snapshot_id"],
                                "a_f_digest": afc["digest"], "cycle": CYCLE}, sort_keys=True).encode())
    doc["snapshot"]["id"] = sid
    doc["generated_by"] = f"scripts/grixis_birthday_m5.py v{VERSION} + grixis_candidates.py v{gc.VERSION}"
    doc["cycle"] = CYCLE
    doc["pass_id"] = f"m5:{doc['slug']}:c{CYCLE}:" + sid[7:19]
    doc["authority"]["note"] += " Fresh Birthday M5 evidence only; Cory must explicitly accept M5. No deck is approved or locked."
    return doc


def integrate_all(m):
    configure_paths()
    R, reg, pool, first, almost = gc._ctx()
    REGEN.mkdir(parents=True, exist_ok=True)
    rows = []
    for did, v in sorted(ga.summary().items(), key=lambda kv: kv[1]["slug"]):
        slug = v["slug"]
        src = CANDS / f"{slug}.json.gz"
        doc = json.loads(gzip.decompress(src.read_bytes()).decode("utf-8"))
        rid = ga.registry_id(did)
        canonical_hash = reg["decks"][rid]["canonical_project_list"]["hash"]
        af = current_af(slug, rid, canonical_hash, pool)
        doc = integrate_doc(doc, af, m)
        # Keep mature dump format so downstream inspection remains familiar.
        (REGEN / f"{slug}.json.gz").write_bytes(gzip.compress(gc.dump(doc).encode("utf-8"), compresslevel=9, mtime=0))
        c = doc["counts"]
        rows.append({"slug": slug, "canonical_hash": canonical_hash, "universe": c["universe"],
                     "reviews": c["screening_reviews"], "swaps": c["swaps"], "tests": c["paired_tests"],
                     "af_digest": af.deck_context()["digest"]})
    return rows


def cand_map(doc):
    return {x["card"]: x for x in doc.get("candidates", [])}


def swap_sem(sw):
    return (tuple(sw.get("cuts", [])), tuple(sw.get("adds", [])))


def test_sem(t):
    # Test IDs can move with snapshot ids; semantic comparison is cut/add plus model verdict.
    return (t.get("cut"), t.get("add"))


def build_delta(m, convergence, before_frozen):
    rows = []
    totals = Counter()
    for slug in sorted(v["slug"] for v in ga.summary().values()):
        fp = FROZEN_M5 / f"{slug}.json.gz"; cp = REGEN / f"{slug}.json.gz"
        old = json.loads(gzip.decompress(fp.read_bytes()).decode("utf-8")); new = json.loads(gzip.decompress(cp.read_bytes()).decode("utf-8"))
        if old["list_hash"] != new["list_hash"]:
            raise SystemExit(f"{slug}: canonical list hash changed during Birthday M5")
        oc, nc = cand_map(old), cand_map(new)
        on, nn = set(oc), set(nc)
        score_changed = []
        for n in sorted(on & nn):
            a = (oc[n].get("screening") or {}).get("score")
            b = (nc[n].get("screening") or {}).get("score")
            if a != b:
                score_changed.append({"card": n, "from": a, "to": b, "delta": None if a is None or b is None else round(b-a, 4)})
        ofull = {n for n, x in oc.items() if x.get("full_review")}; nfull = {n for n, x in nc.items() if x.get("full_review")}
        osw = {swap_sem(x): x for x in old.get("swaps", [])}; nsw = {swap_sem(x): x for x in new.get("swaps", [])}
        ot = {test_sem(x): x for x in old.get("tests", [])}; nt = {test_sem(x): x for x in new.get("tests", [])}
        verdict_shifts = []
        for k in sorted(set(ot) & set(nt), key=str):
            if ot[k].get("verdict") != nt[k].get("verdict"):
                verdict_shifts.append({"cut": k[0], "add": k[1], "from": ot[k].get("verdict"), "to": nt[k].get("verdict")})
        sat_old = json.loads((FROZEN_SAT / f"{slug}.json").read_text(encoding="utf-8"))
        sat_new = json.loads((SAT / f"{slug}.json").read_text(encoding="utf-8"))
        row = {
            "slug": slug, "canonical_hash": new["list_hash"],
            "universe": {"old": len(on), "new": len(nn), "added": sorted(nn-on), "removed": sorted(on-nn),
                         "frozen_universe_sha256": sat_old["universe"]["sha256"], "fresh_universe_sha256": sat_new["universe"]["sha256"]},
            "screening": {"score_changed_count": len(score_changed), "score_changes": score_changed,
                          "full_review_added": sorted(nfull-ofull), "full_review_removed": sorted(ofull-nfull),
                          "full_review_old": len(ofull), "full_review_new": len(nfull)},
            "swaps": {"added": [{"cut": k[0], "add": k[1]} for k in sorted(set(nsw)-set(osw), key=str)],
                      "removed": [{"cut": k[0], "add": k[1]} for k in sorted(set(osw)-set(nsw), key=str)],
                      "old": len(osw), "new": len(nsw)},
            "tests": {"old": len(ot), "new": len(nt), "verdict_shifts": verdict_shifts},
            "counts": {"frozen": old["counts"], "fresh": new["counts"]},
        }
        rows.append(row)
        totals["score_changes"] += len(score_changed)
        totals["full_review_added"] += len(nfull-ofull); totals["full_review_removed"] += len(ofull-nfull)
        totals["swap_added"] += len(set(nsw)-set(osw)); totals["swap_removed"] += len(set(osw)-set(nsw))
        totals["verdict_shifts"] += len(verdict_shifts)
        totals["universe_added"] += len(nn-on); totals["universe_removed"] += len(on-nn)

    after_frozen = frozen_digest()
    if after_frozen != before_frozen:
        raise SystemExit(f"frozen M5/A-F digest changed during fresh run: {before_frozen} -> {after_frozen}")
    delta = {
        "schema_version": 1, "kind": "birthday_m5_delta", "generated_by": f"scripts/grixis_birthday_m5.py v{VERSION}",
        "birthday_authority_snapshot": m["snapshot_id"], "frozen_baseline": "snap-20261016",
        "frozen_m5_summary_sha256": sha_file(FROZEN_SUMMARY), "frozen_corpus_digest": before_frozen,
        "authority": {"can_decide": False, "can_approve_or_lock": False,
                      "note": "Current-vs-frozen M5 evidence delta only. Cory's explicit M5 acceptance is required before I/J/K."},
        "convergence": convergence, "totals": dict(totals), "decks": rows,
    }
    DELTA.write_text(json.dumps(delta, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    return delta


def build_summary(m, delta, convergence, evid_counts, before_frozen):
    rows = []
    total = Counter()
    for p in sorted(REGEN.glob("*.json.gz")):
        d = json.loads(gzip.decompress(p.read_bytes()).decode("utf-8")); c=d["counts"]
        row={"slug":d["slug"],"canonical_hash":d["list_hash"],"universe":c["universe"],"reviews":c["screening_reviews"],"swaps":c["swaps"],"tests":c["paired_tests"]}
        rows.append(row)
        for k in ("universe","reviews","swaps","tests"): total[k]+=row[k]
    summary = {
        "schema_version": 1, "generated_by": f"scripts/grixis_birthday_m5.py v{VERSION}", "cycle": CYCLE,
        "status": "complete_current_corpus_generated", "birthday_authority_snapshot": m["snapshot_id"],
        "structural_baseline": "snap-20261016", "frozen_corpus_digest": before_frozen,
        "fresh_edhrec": evid_counts, "tournament_convergence_passes": len(convergence),
        "authority": {"can_decide": False,"can_approve_or_lock":False,"accepted_by_cory":False,
                      "note":"Fresh M5 is ready for explicit Cory review/acceptance; it approves no deck."},
        "decks": rows, "totals": dict(total), "delta_totals": delta["totals"],
    }
    SUMMARY.write_text(json.dumps(summary, indent=1, ensure_ascii=False, sort_keys=True)+"\n",encoding="utf-8")
    prov={
        "schema_version":1,"birthday_authority_snapshot":m["snapshot_id"],"authority_manifest_sha256":sha_file(MANIFEST),
        "impact_sha256":sha_file(IMPACT),"edhrec_current_sha256":sha_file(EDH_CURRENT),"spellbook_current_sha256":sha_file(SPELLBOOK_CURRENT),
        "scryfall":{k:{"file":v["file"],"url":v["url"],"sha256":v["sha256"],"updated_at":v.get("updated_at")} for k,v in m["sources"]["scryfall"].items()},
        "frozen_corpus_digest":before_frozen,"outputs":{"summary":sha_file(SUMMARY),"delta":sha_file(DELTA)},
        "fresh_A_frozen_BF":True,"historical_raw_edhrec_required":False,
    }
    PROVENANCE.write_text(json.dumps(prov,indent=1,sort_keys=True)+"\n",encoding="utf-8")
    return summary


def semantic_problems(m):
    probs=[]
    expected={v["slug"] for v in ga.summary().values()}
    for label,d in (("saturation",SAT),("candidate",CANDS),("regen",REGEN)):
        got={p.name.removesuffix(".universe.json.gz").removesuffix(".json.gz").removesuffix(".json") for p in d.glob("*.json*") if "tournament" not in str(p)}
        # SAT has both cert+universe; set dedupes names after suffix stripping.
        if label=="saturation": got={p.stem for p in SAT.glob("*.json")}
        else: got={p.name[:-8] for p in d.glob("*.json.gz")}
        if got!=expected: probs.append(f"{label} coverage missing={sorted(expected-got)} extra={sorted(got-expected)}")
    if len(list(EVID.glob("*.json")))!=62: probs.append("fresh evidence coverage != 62")
    for slug in sorted(expected):
        cert=json.loads((SAT/f"{slug}.json").read_text(encoding="utf-8"))
        if cert.get("snapshot",{}).get("id")!=m["snapshot_id"]: probs.append(f"{slug}: wrong fresh-A snapshot")
        if not cert.get("saturated") or cert.get("pool",{}).get("sweep_coverage")!=1.0: probs.append(f"{slug}: fresh saturation incomplete")
        d=json.loads(gzip.decompress((REGEN/f"{slug}.json.gz").read_bytes()).decode("utf-8"))
        if d.get("list_hash")!=cert.get("list_hash"): probs.append(f"{slug}: list hash drift")
        if d.get("authority",{}).get("exploratory") is not True: probs.append(f"{slug}: lost exploratory authority")
        if d.get("triage",{}).get("escalated_queued"): probs.append(f"{slug}: escalated queue not drained")
        if d.get("snapshot",{}).get("birthday_authority")!=m["snapshot_id"]: probs.append(f"{slug}: missing Birthday snapshot binding")
        if d.get("snapshot",{}).get("structural_baseline")!="snap-20261016": probs.append(f"{slug}: wrong structural baseline")
        for c in d.get("candidates",[]):
            if c.get("full_review") and not c.get("review"): probs.append(f"{slug}/{c['card']}: full review missing")
            af=((c.get("review") or {}).get("a_f_evidence") or {})
            if af and (af.get("authority",{}).get("can_decide") is not False or af.get("authority",{}).get("aggregate_score") is not None):
                probs.append(f"{slug}/{c['card']}: A-F review became deciding")
        for sw in d.get("swaps",[]):
            if sw.get("decision",{}).get("verdict") is not None or sw.get("state")!="CHALLENGER" or not sw.get("exploratory"):
                probs.append(f"{slug}/{sw.get('id')}: swap became decided/non-exploratory")
    if not SUMMARY.exists() or not DELTA.exists() or not PROVENANCE.exists(): probs.append("summary/delta/provenance missing")
    else:
        s=json.loads(SUMMARY.read_text()); de=json.loads(DELTA.read_text())
        if len(s.get("decks",[]))!=62: probs.append("summary coverage != 62")
        if len(de.get("decks",[]))!=62: probs.append("delta coverage != 62")
        if s.get("authority",{}).get("accepted_by_cory") is not False: probs.append("M5 was auto-accepted")
        if de.get("authority",{}).get("can_decide") is not False: probs.append("delta became decision-capable")
    return probs


def build_all(jobs=6):
    m=authority_manifest(); exact_current_bulk_files(m); configure_paths()
    impact=json.loads(IMPACT.read_text(encoding="utf-8"))
    if impact.get("summary",{}).get("blocked") or impact.get("summary",{}).get("structural_refresh"):
        raise SystemExit(f"impact audit is not candidate-only safe: {impact.get('summary')}")
    if impact.get("summary",{}).get("candidate_refresh")!=62:
        raise SystemExit(f"expected 62 candidate refresh decks, got {impact.get('summary')}")
    before=frozen_digest()
    evid=prepare_evidence(m)
    convergence=converge(m,jobs)
    rows=integrate_all(m)
    delta=build_delta(m,convergence,before)
    summary=build_summary(m,delta,convergence,evid,before)
    probs=semantic_problems(m)
    if probs:
        for x in probs[:100]: print("FAIL",x)
        raise SystemExit(f"Birthday M5 validation failed: {len(probs)} problem(s)")
    print(json.dumps({"snapshot":m["snapshot_id"],"decks":len(rows),"totals":summary["totals"],"delta_totals":delta["totals"],
                      "tournament_convergence_passes":len(convergence),"problems":0},indent=2))


def check():
    m=authority_manifest(); exact_current_bulk_files(m)
    p=semantic_problems(m)
    print(f"birthday-m5: {len(list(REGEN.glob('*.json.gz')))}/62 decks; {len(p)} problem(s)")
    for x in p[:100]: print("FAIL",x)
    return 1 if p else 0


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--build",action="store_true"); ap.add_argument("--check",action="store_true"); ap.add_argument("--jobs",type=int,default=6)
    a=ap.parse_args()
    if not a.build and not a.check: ap.error("choose --build and/or --check")
    if a.build: build_all(a.jobs)
    return check() if a.check else 0

if __name__=="__main__":
    raise SystemExit(main())
