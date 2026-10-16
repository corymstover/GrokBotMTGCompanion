#!/usr/bin/env python3
"""M4 99-slot audit (Bot cycle 59.2).

Every slot of every canonical project list (the 99, or 98 with partners; one entry per card name with its quantity) gets
a disposition evaluated against:
  * the M2 blueprint (packages and their minimums, identity core, tutor targets, wins, engines, anti-goals, and every
    blueprint field that names the card),
  * the role model (key roles from Oracle patterns, lands, mana sources) and the deck's role counts,
  * the M4 dependency graph (structural necessity, breaks-if-removed, redundancy, interchangeable combo pieces),
  * the best alternative in its role (M3 evidence layer candidate), EDHREC inclusion / synergy (derived_metric),
  * the M1 interaction rulings that name the card (flags are recorded, never auto-applied).

Authority (Cory constraints 2 and 6). M2 is not accepted, so no disposition here is authoritative: every slot is
`review_status: provisional`, `classifier: script`, and no cut or add is decided. `complete_eligible` says whether the
slot already carries blueprint, graph and alternative refs, redundancy, a role/package and a reason (what
grixis_authority.disposition_status() requires for `complete`); it becomes reviewable once M2 is accepted and a human
or review pass confirms it. Each slot's `decision_support` runs grixis_authority.decision_support_ok over its evidence
items: slots resting on heuristic / derived evidence alone are marked as unable to decide.

Disposition rules (first match; recorded in each file as `rules`), see DISPOSITION_RULES.

Lint: no reason text (with the card's own name removed) may repeat on more than LINT_MAX_DUP slots of a deck.
Baseline: every audit carries the deck's goldfish baseline (grixis_sim current model, BASE_SAMPLES games, seed BASE_SEED).

Usage:
  python3 scripts/grixis_audit.py --build [--deck SLUG]
  python3 scripts/grixis_audit.py --check
  python3 scripts/grixis_audit.py --summary
"""
import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_authority as ga  # noqa: E402

VERSION = "1"
CYCLE = 59
OUT = ROOT / "data" / "grixis" / "audit"
GRAPH = ROOT / "data" / "grixis" / "graph"
EVID = ROOT / "data" / "grixis" / "evidence"
BPS = ROOT / "data" / "grixis" / "blueprints"
INTER = ROOT / "data" / "grixis_interactions"
LINT_MAX_DUP = 2
BASE_SAMPLES, BASE_SEED = 1000, 59
KEY_ROLES = ("ramp", "draw", "removal", "wipe", "counter", "protection", "tutor")
FLEX_RED = 8          # role / colour mates at or above this make a plain role card or basic `flexible`
FLEX_MAX_INC = 0.40   # ... unless EDHREC inclusion is at least this (a widely played role card stays functional)
LOW_INCLUSION = 0.10  # EDHREC inclusion below this (or no row) counts as weak support
HATE_RX = re.compile(r"(exile (all cards from )?(target player's|all|each opponent's|an opponent's) graveyards?|"
                     r"cards in graveyards can't|creatures? your opponents control (enter|can't)|"
                     r"artifacts? (and creatures? )?your opponents control|players can't (search|cast|draw)|"
                     r"each opponent can't|your opponents can't)", re.I)
AUTHORITY = {"status": "provisional",
             "reason": "M2 (blueprints) is not accepted, so no audit disposition is authoritative and no cut/add is decided "
                       "(Cory constraints 2 and 6). Every slot is provisional until M2 is accepted and the slot is confirmed.",
             "m2_status": None}
DISPOSITION_RULES = [
    ["project_requirement", "the card is a registered project exception or authorized future-release card"],
    ["active_cut_candidate", "only a blueprint anti-goal names it; or it is structurally independent, has no Oracle hook, no "
                             "blueprint mention, weak EDHREC support and a named alternative (a review candidate, not a cut)"],
    ["core", "structurally necessary (graph) or identity core (blueprint)"],
    ["strong_retain", "structurally important: breaks a Spellbook combo, a blueprint tutor target, or a win piece / enabler"],
    ["package_dependent", "its job is a non-required blueprint package (keeps its value only while that package stays)"],
    ["meta_dependent", "narrow hate / taxing text whose value depends on what opponents play"],
    ["flexible", "a plain role card or basic land with many role / colour mates (FLEX_RED or more) and no structure"],
    ["functional_retain", "fills a key role, the mana base, or a required package, with fewer mates"],
    ["weak_retain", "none of the above, but an Oracle hook, blueprint mention or EDHREC support"],
]


def sha(b):
    return "sha256:" + hashlib.sha256(b).hexdigest()


def rel(p):
    return str(Path(p).relative_to(ROOT))


def blueprint_mentions(bp, name):
    """JSON paths of blueprint fields whose text names the card (exact name)."""
    out = []

    def walk(x, path):
        if isinstance(x, dict):
            for k, v in x.items():
                if k in ("evidence", "provenance", "oracle_text", "oracle_sha256", "oracle_id"):
                    continue
                walk(v, f"{path}/{k}")
        elif isinstance(x, list):
            for i, v in enumerate(x):
                key = v.get("id") or v.get("card") or v.get("target") or i if isinstance(v, dict) else i
                walk(v, f"{path}/{key}")
        elif isinstance(x, str) and (x == name or (len(name) > 4 and name in x)):
            out.append(path)
    walk({k: v for k, v in bp.items() if k not in ("commanders", "supporting_features")}, "")
    seen, res = set(), []
    for p in out:
        top = "/".join(p.split("/")[:3])
        if top not in seen:
            seen.add(top)
            res.append(top)
    return res


def baseline(slug, R):
    import grixis_sim as gs
    d = gs.load_deck(slug, R)
    recs = gs.run(d, BASE_SAMPLES, BASE_SEED)
    s = gs.summarize(d, recs)
    n = len(recs)
    keep = {k: v for k, v in s.items() if not isinstance(v, (list,)) and k != "samples"}
    keep["mana_spent_t1_t6_mean"] = round(sum(sum(r["spent"][:6]) for r in recs) / n, 4)
    keep["extra_cards_drawn_mean"] = round(sum(r.get("drawn_extra", 0) for r in recs) / n, 4)
    keep["tutored_mean"] = round(sum(len(r.get("tutored", [])) for r in recs) / n, 4)
    return {"simulator": {"name": gs.NAME, "version": gs.VERSION, "model_sha256": gs.model_sha256()}, "seed": BASE_SEED,
            "samples": BASE_SAMPLES, "keep_rule": gs.KEEP_RULE, "class": "test_result",
            "note": "Goldfish baseline of the canonical list (no opponents; never a win rate). Model limits: grixis_sim MODEL_NOTES.",
            "metrics": json.loads(json.dumps(keep, sort_keys=True))}


def build_deck(did, v, R, reg, exc):
    slug = v["slug"]
    rid = ga.registry_id(did)
    e = reg["decks"][rid]
    g = json.loads((GRAPH / f"{slug}.json").read_text(encoding="utf-8"))
    ev = json.loads((EVID / f"{slug}.json").read_text(encoding="utf-8"))
    bpf = BPS / f"{slug}.json"
    bp = json.loads(bpf.read_text(encoding="utf-8")) if bpf.exists() else {}
    bref, gref, eref = f"blueprint:{rel(bpf)}", f"graph:data/grixis/graph/{slug}.json", f"evidence:data/grixis/evidence/{slug}.json"
    review = INTER / f"{slug}.json"
    m1 = {x["id"]: x for x in json.loads(review.read_text(encoding="utf-8")).get("interactions", [])} if review.exists() else {}
    cols = ev["edhrec"]["columns"]
    edh = {x["card"]: dict(zip(cols, x["edhrec"])) for x in ev["vectors"] if x.get("edhrec") and x["status"] != "candidate"}
    hook = {x["card"]: (x.get("oracle_hook") or {}).get("label") for x in ev["vectors"] if x["status"] != "candidate"}
    nodes = {x["name"]: x for x in g["nodes"] if x["kind"] in ("card", "commander")}
    met = g["metrics"]
    import grixis_sim as gs
    ci = set(v["ci"])
    anti = " ".join((bp.get("anti_goals") or {}).get("value", []) or [])
    exc_cards = {x["card"] for x in exc if x["deck_id"] in (rid, did)}
    role_count = Counter()
    for n, x in nodes.items():
        if x["zone"] != "commander":
            for r in x["roles"]:
                role_count[r] += x["qty"]
    pk = {p["id"]: p for p in bp.get("packages", [])}
    m1_of = {}
    for x in g["edges"]:
        if x["layer"] in ("m1_edges", "m1_review") and x.get("interaction"):
            m1_of.setdefault(x["from"].split(":", 1)[1], set()).add(x["interaction"])
    slots = []
    for n in sorted(nodes):
        x = nodes[n]
        if x["zone"] == "commander":
            continue
        m = met[n]
        c, _ = R.get(n)
        text = (c.get("oracle_text") or " ".join(f.get("oracle_text", "") for f in c.get("card_faces", []))) if c else ""
        roles = x["roles"]
        krs = [r for r in roles if r in KEY_ROLES]
        cm = gs.card_model(c, ci) if c else {"source": None, "v11": {}}
        src_cols = set(cm["source"][0]) if cm.get("source") else set()
        pkgs = x["packages"]
        mention = blueprint_mentions(bp, n) if bp else []
        er = edh.get(n) or {}
        inc = er.get("inclusion")
        weak = inc is None or inc < LOW_INCLUSION
        req_pk = [p for p in pkgs if pk[p].get("required")]
        flags = []
        for i in sorted(m1_of.get(n, [])):
            r = m1.get(i, {})
            if r.get("status") in ("flag", "uncertain"):
                fl = r.get("flag") or {}
                flags.append({"interaction": i, "status": r.get("status"), "kind": fl.get("kind") if isinstance(fl, dict) else None,
                              "ref": f"review:{rel(review)}#{i}"})
        anti_hit = len(n) > 4 and n in anti
        # disposition
        if n in exc_cards:
            disp, why = "project_requirement", "registered project exception"
        elif anti_hit and not [q for q in mention if not q.startswith("/anti_goals")]:
            disp, why = "active_cut_candidate", "named only by a blueprint anti-goal"
        elif m["structural_necessity"] == "necessary" or x["identity_core"]:
            disp, why = "core", "; ".join(filter(None, ["identity core" if x["identity_core"] else "",
                                                       ("necessary: " + ", ".join(m["necessity_reasons"][:3])) if m["necessity_reasons"] else ""]))
        elif m["structural_necessity"] == "important":
            bits = []
            if m["combos"]:
                bits.append(f"piece of {len(m['combos'])} Spellbook combo(s)")
            if x["tutor_target"]:
                bits.append("blueprint tutor target")
            if not bits:
                bits.append("win piece / enabler")
            disp, why = "strong_retain", "; ".join(bits)
        elif m["structural_necessity"] == "independent" and not hook.get(n) and not mention and weak and m["best_alternative_in_role"]:
            disp, why = "active_cut_candidate", "independent in the graph, no Oracle hook, no blueprint mention, weak EDHREC support"
        elif pkgs and not req_pk and not krs:
            disp, why = "package_dependent", f"only job is optional package {', '.join(pkgs)}"
        elif HATE_RX.search(text) and not pkgs:
            disp, why = "meta_dependent", "hate / taxing text that depends on opponents"
        elif not pkgs and not m["combos"] and m["redundancy"] >= FLEX_RED and not mention and (
                ("land" in roles and len(src_cols & ci) < 2) or ("land" not in roles and krs and (inc is None or inc < FLEX_MAX_INC))):
            disp, why = "flexible", f"{m['redundancy']} {m['redundancy_basis']}"
        elif krs or "land" in roles or req_pk or "ramp" in roles:
            disp, why = "functional_retain", ("required package " + ", ".join(req_pk)) if req_pk else (
                f"fixing ({''.join(sorted(src_cols & ci))})" if "land" in roles and len(src_cols & ci) >= 2 else "role " + ", ".join(krs or roles))
        else:
            disp, why = "weak_retain", "no structure; " + ("Oracle hook " + hook[n] if hook.get(n) else "blueprint mention" if mention else "EDHREC support")
        # refs
        brefs = [f"{bref}#packages/{p}" for p in pkgs] + ([f"{bref}#identity_core/{n}"] if x["identity_core"] else []) + \
                ([f"{bref}#tutor_targets/{n}"] if x["tutor_target"] else []) + [f"{bref}#{p.lstrip('/')}" for p in mention]
        brefs = sorted(set(brefs))
        grefs = [f"{gref}#metrics/{n}"] + [f"{gref}#{b}" for b in m["breaks_if_removed"][:6]]
        alts = ([m["alternative"]["evidence"]] if m.get("alternative") else []) + [f"{gref}#card:{y}" for y in m["interchangeable_with"]]
        evid = sorted(set([f"oracle:{n}"] + [f"spellbook:{i}" for i in m["combos"]] + [f["ref"] for f in flags] +
                          ([f"{eref}#{n}"] if er else []) + brefs + grefs[:1]))
        # evidence items and classes
        items = [{"id": f"oracle:{n}", "class": "fact", "confidence": "verified"}]
        items += [{"id": f"role:{r}", "class": "heuristic", "confidence": "moderate"} for r in roles]
        items += [{"id": f"spellbook:{i}", "class": "fact", "confidence": "verified"} for i in m["combos"]]
        items += [{"id": r, "class": "strategic_judgment", "confidence": "moderate"} for r in brefs]
        if er:
            items.append({"id": f"{eref}#{n}", "class": "derived_metric", "confidence": er.get("confidence") or "moderate"})
        items += [{"id": f["ref"], "class": "fact", "confidence": "test_required" if f["status"] == "uncertain" else "high"} for f in flags]
        ok, why_not = ga.decision_support_ok([i for i in items if i["id"] != f"oracle:{n}"])
        cols = sorted(src_cols & (ci | {"C"}))
        fetch = re.search(r"[Ss]earch your library for (an? [^,.]+? card)", text) if "land" in roles else None
        feats = [k + (f" {v}" if isinstance(v, int) and not isinstance(v, bool) else "") for k, v in sorted(cm.get("v11", {}).items())
                 if v and k in ("draw", "upkeep_draw", "tutor", "ritual", "oneshot", "treasures", "condition", "wheel", "suspend")]
        if cm.get("v11", {}).get("condition"):
            feats = [f"condition {cm['v11']['condition']}" if f.startswith("condition") else f for f in feats]
        digest = re.sub(r"\([^)]*\)", "", text).strip().split("\n")[0].split(". ")[0].strip(" .")
        digest = (digest[:77] + "…") if len(digest) > 78 else digest
        cost = (c.get("mana_cost") or (c.get("card_faces") or [{}])[0].get("mana_cost") or "") if c else ""
        reason = compose_reason(n, disp, why, m, x, krs, role_count, inc, er, flags, mention, cols,
                                fetch.group(1) if fetch else None, feats, digest, cost)
        slot = {"card": n, "quantity": x["qty"], "zone": x["zone"], "disposition": disp, "review_status": "provisional", "classifier": "script",
                "roles": roles, "packages": pkgs, "blueprint_refs": brefs, "graph_refs": grefs, "alternatives": alts,
                "redundancy": m["redundancy"], "reason": reason, "evidence": evid,
                "structural_necessity": m["structural_necessity"],
                "evidence_classes": dict(sorted(Counter(i["class"] for i in items).items())),
                "decision_support": {"ok": ok, "why_not": why_not}, "m1_flags": flags}
        slot["complete_eligible"] = ga.disposition_status(slot) == "complete"
        slots.append(slot)
    total = sum(s["quantity"] for s in slots if s["zone"] == "main")  # the companion is outside the 100 (CR 702.139a)
    lint = lint_reasons(slots)
    sid = sha((json.dumps(g["snapshot"]["id"]) + json.dumps(ev["snapshot"]["id"]) + sha(Path(__file__).read_bytes()) +
               (sha(bpf.read_bytes()) if bpf.exists() else "") + (sha(review.read_bytes()) if review.exists() else "") +
               gs.model_sha256() + VERSION).encode())
    cands = sum(1 for x in ev["vectors"] if x["status"] == "candidate")
    doc = {"schema_version": 1, "deck_id": rid, "slug": slug, "generated_by": f"scripts/grixis_audit.py v{VERSION}", "cycle": CYCLE,
           "list_hash": e["canonical_project_list"]["hash"], "pass_id": f"audit:{slug}:c{CYCLE}:" + sid[7:19],
           "snapshot": {"id": sid, "graph": g["snapshot"]["id"], "evidence": ev["snapshot"]["id"], "m1": g["m1"]["status"]},
           "authority": dict(AUTHORITY, m2_status=reg["program"]["milestones"]["M2"]["status"]),
           "rules": DISPOSITION_RULES, "slot_total": total,
           "counts": {"slots": len(slots), "cards": total, "companion": [s["card"] for s in slots if s["zone"] == "companion"], "dispositions": dict(sorted(Counter(s["disposition"] for s in slots).items())),
                      "complete_eligible": sum(1 for s in slots if s["complete_eligible"]),
                      "decision_support_ok": sum(1 for s in slots if s["decision_support"]["ok"]),
                      "role_counts": dict(sorted(role_count.items()))},
           "lint": lint, "baseline_sim": baseline(slug, R), "slots": slots,
           "candidate_universe": {"definition": "M3 evidence-layer EDHREC candidates in colour identity on the deck's commander page(s), not basic lands, not in the list (screened only: full reviews and escalations are M5)",
                                  "screened": cands, "full_review": 0, "escalated": 0, "snapshot": ev["snapshot"]["id"]}}
    return doc


def compose_reason(n, disp, why, m, x, krs, role_count, inc, er, flags, mention, cols, fetch=None, feats=(), digest="", cost=""):
    tl = x["type_line"].split(" — ")[0].replace("Legendary ", "legendary ").lower()
    what = (f"{tl}" + (f", fetches {fetch}" if fetch else "") + (f", makes {''.join(cols)}" if cols else "")) if "land" in x["roles"] \
        else f"{cost or 'MV ' + str(x['mv'])} {tl}" + (f"; simulator models {', '.join(feats)}" if feats else "")
    parts = [f"{disp.replace('_', ' ')} ({what}): {why}."] + ([f"Oracle: “{digest}”."] if digest else [])
    if krs:
        parts.append("Role " + ", ".join(f"{r} ({role_count[r]} in list)" for r in krs) + ".")
    elif "land" in x["roles"]:
        parts.append(f"Land ({role_count['land']} in list).")
    if x["packages"]:
        parts.append("Packages " + ", ".join(x["packages"]) + ".")
    if m["breaks_if_removed"]:
        parts.append(f"Removing it breaks {len(m['breaks_if_removed'])}: " + ", ".join(m["breaks_if_removed"][:3]) + ("…" if len(m["breaks_if_removed"]) > 3 else "") + ".")
    parts.append(f"Redundancy {m['redundancy']} ({m['redundancy_basis']}).")
    if m["interchangeable_with"]:
        parts.append("Interchangeable with " + ", ".join(m["interchangeable_with"][:3]) + ".")
    if m["best_alternative_in_role"]:
        a = m["alternative"]
        parts.append(f"Best alternative: {m['best_alternative_in_role']} ({a['basis']}" + (f", EDHREC {a['inclusion']:.0%}" if a.get("inclusion") is not None else "") + ").")
    if inc is not None:
        parts.append(f"EDHREC inclusion {inc:.1%}, synergy {er.get('synergy'):+.2f}." if er.get("synergy") is not None else f"EDHREC inclusion {inc:.1%}.")
    else:
        parts.append("No EDHREC row.")
    if mention:
        parts.append("Blueprint names it in " + ", ".join(p.strip("/") for p in mention[:3]) + ".")
    if any(q.startswith("/anti_goals") for q in mention):
        parts.append("A blueprint anti-goal also names it (review the line it rules out).")
    if flags:
        parts.append("M1: " + ", ".join(f"{f['interaction']} ({f['kind'] or f['status']})" for f in flags) + " (recorded, not applied).")
    return " ".join(parts)


def lint_reasons(slots):
    c = Counter(s["reason"].replace(s["card"], "<card>") for s in slots)
    dup = {k: v for k, v in c.items() if v > LINT_MAX_DUP}
    return {"max_duplicate": max(c.values()) if c else 0, "threshold": LINT_MAX_DUP, "over_threshold": len(dup),
            "distinct_reasons": len(c), "ok": not dup}


def dump(doc):
    head = {k: v for k, v in doc.items() if k != "slots"}
    rows = [f"  {json.dumps(s, ensure_ascii=False, separators=(',', ':'))}" for s in doc["slots"]]
    return json.dumps(head, indent=1, ensure_ascii=False)[:-2] + ',\n "slots": [\n' + ",\n".join(rows) + "\n ]\n}\n"


def build(only=None, verbose=True):
    import evaluate_decklist as ev
    R = ev.Resolver()
    reg = ga.load_json(ga.REGISTRY)
    exc = ga.load_json(ga.EXCEPTIONS)["exceptions"]
    OUT.mkdir(parents=True, exist_ok=True)
    for did, v in sorted(ga.summary().items(), key=lambda x: x[1]["slug"]):
        if only and v["slug"] != only:
            continue
        doc = build_deck(did, v, R, reg, exc)
        (OUT / f"{v['slug']}.json").write_text(dump(doc), encoding="utf-8")
        if verbose:
            c = doc["counts"]
            print(f"{v['slug']}: {c['cards']} cards / {c['slots']} slots; {c['dispositions']}; lint max dup {doc['lint']['max_duplicate']}")


def check(verbose=True, rebuild=True):
    import evaluate_decklist as ev
    p = []
    summ = ga.summary()
    reg = ga.load_json(ga.REGISTRY)
    want = {v["slug"]: (did, v) for did, v in summ.items()}
    files = {f.stem: f for f in OUT.glob("*.json")}
    for s in sorted(set(want) - set(files)):
        p.append(f"{s}: no audit (run --build)")
    R = ev.Resolver() if rebuild and (ROOT / ".cache").exists() else None
    exc = ga.load_json(ga.EXCEPTIONS)["exceptions"]
    tot = Counter()
    for s, f in sorted(files.items()):
        if s not in want:
            p.append(f"{s}: audit for an unknown deck")
            continue
        did, v = want[s]
        doc = json.loads(f.read_text(encoding="utf-8"))
        for e in ga.validate_file(doc, "audit.schema.json"):
            p.append(f"{s}: {e}")
        p += [f"{s}: {x}" for x in ga.audit_problems(doc)]
        if doc["list_hash"] != reg["decks"][ga.registry_id(did)]["canonical_project_list"]["hash"]:
            p.append(f"{s}: list_hash is not the canonical list hash (stale)")
        g = json.loads((GRAPH / f"{s}.json").read_text(encoding="utf-8"))
        if doc["snapshot"]["graph"] != g["snapshot"]["id"]:
            p.append(f"{s}: built from an older dependency graph (run --build)")
        expect = 100 - sum(1 for x in g["nodes"] if x["kind"] == "commander")
        if doc["slot_total"] != sum(x["quantity"] for x in doc["slots"] if x["zone"] == "main"):
            p.append(f"{s}: slot_total doesn't add up")
        if doc["slot_total"] != expect:
            p.append(f"{s}: {doc['slot_total']} slots, expected {expect}")
        for x in doc["slots"]:
            if x["review_status"] != "provisional":
                p.append(f"{s}: {x['card']} is not provisional while M2 is not accepted (constraint 6)")
            if x["complete_eligible"] != (ga.disposition_status(x) == "complete"):
                p.append(f"{s}: {x['card']} complete_eligible inconsistent")
            tot[x["disposition"]] += x["quantity"]
        if not doc["lint"]["ok"] or lint_reasons(doc["slots"]) != doc["lint"]:
            p.append(f"{s}: boilerplate lint fails ({doc['lint']})")
        if R is not None and s in ("wick-the-whorled-mind", "bjorna-nightfall-alchemist-cecily"):
            if dump(build_deck(did, v, R, reg, exc)) != f.read_text(encoding="utf-8"):
                p.append(f"{s}: rebuild does not reproduce the stored audit")
    if verbose:
        print(f"audit: {len(files)} deck(s), {sum(tot.values())} cards; {dict(sorted(tot.items()))}; {len(p)} problem(s)")
        for x in p[:30]:
            print("  -", x)
    return p


def summary():
    tot, el, ok, n = Counter(), 0, 0, 0
    for f in sorted(OUT.glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        for s in d["slots"]:
            tot[s["disposition"]] += s["quantity"]
            n += 1
            el += s["complete_eligible"]
            ok += s["decision_support"]["ok"]
    print(f"{n} slots; complete-eligible {el}; decision-support ok {ok}; {dict(tot.most_common())}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--summary", action="store_true")
    ap.add_argument("--deck")
    a = ap.parse_args()
    if a.build:
        build(a.deck)
        return 0
    if a.summary:
        summary()
        return 0
    return 1 if check() else 0


if __name__ == "__main__":
    sys.exit(main())
