#!/usr/bin/env python3
"""M4 per-deck dependency graph (Bot cycle 59.1).

One graph per deck, built from the deck's canonical project list (M0 registry), its M2 blueprint, the Commander
Spellbook combos still complete in the list, the M3 evidence layer, the heuristic role model of grixis_refine, and the
M1 interaction reviews. Output: data/grixis/graph/<slug>.json, valid against graph.schema.json.

M1 ingest. The interaction executor (Bot cycle 58) writes data/grixis_interactions/edges/<slug>.json (rule edges-v1,
interaction_edges.schema.json). This script only *reads* those files:
  * present, valid, and matching the canonical list (deck_sha256 = sha256 of the export bytes) and the review
    (review_sha256): membership edges (graph_kind piece_of / member_of) and authored edges with a graph kind become
    graph edges; pair edges (graph_kind null) are kept as `annotations` (review-layer relations, derived_metric);
  * absent: the stub fallback reads the M1 review's own `interactions[].cards` (membership only, layer `m1_review`);
  * invalid or stale: ignored with a warning (the review must be rebuilt by its owner), fallback as above.
The M1 status per deck is recorded in `m1`.

Edge layers and classes (every edge carries evidence refs and an evidence_class):
  spellbook   card → combo:<id> piece_of (fact); interchangeable pieces → redundant_with (derived_metric)
  blueprint   card → package / engine member_of, card → win piece_of, enabler → win enables, tutor → target
              tutors_for (the blueprint field's own class, normally strategic_judgment)
  role        card → role:<r> member_of (heuristic: Oracle patterns, grixis_refine.roles); protection → commander
              protects (heuristic); multi-colour mana source → commander fixes (derived_metric)
  m1_edges / m1_review   card → combo/interaction hub (the ruling's class)

Metrics per card (graph.schema.json): breaks_if_removed (combos, wins, sole-member engines, required packages that
would drop below min_count), redundancy (interchangeable combo pieces, else other members of its packages, else other
cards sharing a key role, else lands sharing a colour), structural_necessity (rules in NECESSITY), and
best_alternative_in_role (the best in-identity EDHREC candidate from the evidence layer that shares a role; blueprint
package candidates first). These are structural diagnostics: nothing here is a cut or add decision.

Usage:
  python3 scripts/grixis_graph.py --build [--deck SLUG]
  python3 scripts/grixis_graph.py --check      # schema, snapshot (stale inputs), exact rebuild, M1 ingest status
  python3 scripts/grixis_graph.py --show SLUG CARD
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_authority as ga  # noqa: E402

VERSION = "1"
RULE = "graph-v1"
CYCLE = 59
OUT = ROOT / "data" / "grixis" / "graph"
BPS = ROOT / "data" / "grixis" / "blueprints"
EVID = ROOT / "data" / "grixis" / "evidence"
INTER = ROOT / "data" / "grixis_interactions"
EDGES = INTER / "edges"
COMBOS = ROOT / "data" / "grixis_combos.json"
ROLE_REF = "companion:scripts/grixis_refine.py#roles"
NECESSITY = {
    "necessary": "the commander; or removing it breaks a win condition, the deck's only engine member, a required "
                 "package's minimum, or every Spellbook combo in the list",
    "important": "removing it breaks at least one Spellbook combo, or it is identity core, a blueprint tutor target, "
                 "or a win piece / enabler",
    "redundant": "it belongs to a package or key role and at least one other card does the same job",
    "independent": "none of the above (no package, combo, win or key-role membership; or the only card in its role "
                   "outside any structure)",
}


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha_file(p):
    return "sha256:" + sha_bytes(Path(p).read_bytes()) if Path(p).exists() else None


def pkg_node(pid):
    return "package:" + (pid[4:] if pid.startswith("pkg:") else pid)


def rel(p):
    return str(Path(p).relative_to(ROOT))


# ---------------------------------------------------------------- M1 ingest
M1_CORR = ROOT / "data" / "grixis" / "m1_corrections.json"


def m1_corrections(slug):
    """Bot cycle 62: {interaction id: correction} for this deck from the M1 post-acceptance overlay (M1 files are not edited)."""
    if not M1_CORR.exists():
        return {}
    return {c["id"]: c for c in json.loads(M1_CORR.read_text(encoding="utf-8"))["corrections"] if c["slug"] == slug}


def apply_m1_correction(x, corr, iid):
    c = corr.get(iid)
    if c:
        x["status"] = c["corrected_status"]
        x["m1_correction"] = f"registry:data/grixis/m1_corrections.json#{iid}"
        for k in ("class", "evidence_class"):
            if k in x:
                x[k] = c["evidence_class"]
        if isinstance(x.get("evidence"), list) and x["m1_correction"] not in x["evidence"]:
            x["evidence"] = x["evidence"] + [x["m1_correction"]] + [f"cr:{r}" for r in c["cr"] if f"cr:{r}" not in x["evidence"]]
    return x


def m1_status(slug, export, review):
    """(edges doc or None, status, note). Never writes anything under data/grixis_interactions/."""
    f = EDGES / f"{slug}.json"
    if not f.exists():
        return None, "absent", "no edges file yet (Bot cycle 58 not on main): fallback to the review's interactions[].cards"
    try:
        d = json.loads(f.read_text(encoding="utf-8"))
    except ValueError as e:
        return None, "invalid", f"unreadable edges file: {e}"
    errs = ga.validate_file(d, "interaction_edges.schema.json") if (ga.SCHEMAS / "interaction_edges.schema.json").exists() else []
    if errs:
        return None, "invalid", f"edges file fails interaction_edges.schema.json: {errs[0]}"
    if d.get("deck_sha256") != sha_bytes(Path(export).read_bytes()):
        return None, "stale_list", "edges deck_sha256 differs from the canonical export (owner must rebuild)"
    if review.exists() and d.get("review_sha256") != sha_bytes(review.read_bytes()):
        return None, "stale_review", "edges review_sha256 differs from the review file (owner must rebuild)"
    return d, "ingested", f"{rel(f)} ({d.get('rule_version')})"


# ---------------------------------------------------------------- build
def deck_inputs(slug, export, did):
    files = [export, BPS / f"{slug}.json", COMBOS, INTER / f"{slug}.json", EDGES / f"{slug}.json", EVID / f"{slug}.json",
             Path(__file__), ROOT / "scripts" / "grixis_refine.py"]
    inp = {rel(f): sha_file(f) for f in files}
    if m1_corrections(slug):  # Bot cycle 62: only decks with an M1 post-acceptance correction depend on the overlay
        inp[rel(M1_CORR)] = sha_file(M1_CORR)
    bulk = sorted((ROOT / ".cache").glob("oracle-cards-*.jsonl.gz"))
    inp["oracle_bulk"] = bulk[-1].name if bulk else None
    return inp, "sha256:" + sha_bytes((json.dumps(inp, sort_keys=True) + VERSION).encode())


def colours_of_source(c, ci):
    pm = c.get("produced_mana") or []
    return sorted({x for x in pm if x in ci})


def build_deck(did, v, R, combos_all, reg):
    import grixis_refine as gr
    import grixis_sim as gs
    slug = v["slug"]
    rid = ga.registry_id(did)
    e = reg["decks"][rid]
    export = ROOT / e["canonical_project_list"]["export"]
    text = export.read_text(encoding="utf-8")
    ents = ga.list_entries(text, R)
    zone = {n: z for z, o, q, n in ents}
    qty = {}
    for z, o, q, n in ents:
        qty[n] = qty.get(n, 0) + q
    cards = {n: R.get(n)[0] for n in zone}
    cmdn = sorted(n for n, z in zone.items() if z == "commander")
    ci = set().union(*(set(cards[n].get("color_identity", [])) for n in cmdn))
    bpf = BPS / f"{slug}.json"
    bp = json.loads(bpf.read_text(encoding="utf-8")) if bpf.exists() else {}
    bref = f"blueprint:{rel(bpf)}"
    review = INTER / f"{slug}.json"
    inp, sid = deck_inputs(slug, export, did)
    nodes, edges, ann = {}, [], []
    warnings = []

    def nid(n):
        return ("commander:" if zone.get(n) == "commander" else "card:") + n

    def add_edge(a, b, kind, ev_refs, cls, layer, **kw):
        edges.append(dict({"from": a, "to": b, "kind": kind, "evidence": sorted(set(ev_refs)), "evidence_class": cls, "layer": layer}, **kw))

    # card nodes and roles
    role_of = {}
    for n in sorted(zone):
        c = cards[n]
        tl = c.get("type_line") or " // ".join(f.get("type_line", "") for f in c.get("card_faces", []))
        cm = gs.card_model(c, ci)
        rs = set(gr.roles(c)) if not ("Land" in tl and "//" not in n) else set()
        if "Land" in tl:
            rs.add("land")
        elif cm["source"]:
            rs.add("ramp")
        role_of[n] = sorted(rs)
        nodes[nid(n)] = {"id": nid(n), "kind": "commander" if zone[n] == "commander" else "card", "name": n, "qty": qty[n],
                         "zone": zone[n], "mv": int(c.get("cmc") or 0), "type_line": tl, "roles": role_of[n],
                         "packages": [], "identity_core": False, "tutor_target": False, "recursion": False}
    for r in sorted({r for rs in role_of.values() for r in rs}):
        nodes[f"role:{r}"] = {"id": f"role:{r}", "kind": "role", "name": r, "class": "heuristic"}
    for n in sorted(zone):
        for r in role_of[n]:
            add_edge(nid(n), f"role:{r}", "member_of", [ROLE_REF, f"oracle:{n}"], "heuristic", "role")
    # blueprint
    pk_count = {}
    for p in bp.get("packages", []):
        pid = pkg_node(p["id"])
        inl = [n for n in p.get("cards", []) if n in zone]
        cnt = sum(qty[n] for n in inl)
        pk_count[pid] = cnt
        nodes[pid] = {"id": pid, "kind": "package", "name": p["id"], "required": bool(p.get("required")),
                      "min_count": p.get("min_count"), "count_in_list": cnt, "role": p.get("role"),
                      "candidates": sorted(p.get("candidates") or []), "class": p.get("evidence_class")}
        for n in inl:
            nodes[nid(n)]["packages"].append(p["id"])
            add_edge(nid(n), pid, "member_of", [f"{bref}#packages/{p['id']}"], p.get("evidence_class") or "strategic_judgment", "blueprint")
    for g in bp.get("engines", []):
        gid = f"engine:{g['id']}"
        inl = [n for n in g.get("cards", []) if n in zone]
        nodes[gid] = {"id": gid, "kind": "engine", "name": g["id"], "online_condition": g.get("online_condition"),
                      "members_in_list": len(inl), "class": g.get("evidence_class")}
        for n in inl:
            add_edge(nid(n), gid, "member_of", [f"{bref}#engines/{g['id']}"] + list(g.get("evidence", [])[:2]), g.get("evidence_class") or "strategic_judgment", "blueprint")
    for w in bp.get("win_conditions", []):
        wid = f"win:{w['id']}"
        inl = [n for n in w.get("cards", []) if n in zone]
        nodes[wid] = {"id": wid, "kind": "win", "name": w["id"], "win_kind": w.get("kind"), "pieces_in_list": len(inl),
                      "class": w.get("evidence_class")}
        for n in inl:
            add_edge(nid(n), wid, "piece_of", [f"{bref}#win_conditions/{w['id']}"], w.get("evidence_class") or "strategic_judgment", "blueprint")
        for n in w.get("enablers", []) or []:
            if n in zone:
                add_edge(nid(n), wid, "enables", [f"{bref}#win_conditions/{w['id']}/enablers"], w.get("evidence_class") or "strategic_judgment", "blueprint")
    for t in bp.get("tutor_targets", []):
        tg = t.get("target")
        if tg in zone:
            nodes[nid(tg)]["tutor_target"] = True
            for via in t.get("via", []) or []:
                if via in zone:
                    add_edge(nid(via), nid(tg), "tutors_for", [f"{bref}#tutor_targets/{tg}"] + list(t.get("evidence", [])[:2]),
                             t.get("evidence_class") or "strategic_judgment", "blueprint")
    for x in bp.get("identity_core", []):
        if x.get("card") in zone:
            nodes[nid(x["card"])]["identity_core"] = True
    for n in (bp.get("recursion") or {}).get("value", []) or []:
        if n in zone:
            nodes[nid(n)]["recursion"] = True
    # Spellbook
    deck_combos = [co for co in combos_all.get(did, {}).get("combos", []) if set(co["cards"]) <= set(zone)]
    for co in sorted(deck_combos, key=lambda c: c["id"]):
        cid = f"combo:{co['id']}"
        nodes[cid] = {"id": cid, "kind": "combo", "name": co["id"], "n": co.get("n"), "infinite": co.get("infinite"),
                      "produces": co.get("produces", [])[:4], "requires": co.get("requires", []), "class": "fact"}
        for n in co["cards"]:
            add_edge(nid(n), cid, "piece_of", [f"spellbook:{co['id']}"], "fact", "spellbook")
    subs = {}
    sets = {frozenset(co["cards"]): co["id"] for co in deck_combos}
    for s, cid in sets.items():
        for x in s:
            rest = s - {x}
            for s2, cid2 in sets.items():
                if len(s2) == len(s) and rest <= s2 and s2 != s:
                    (y,) = tuple(s2 - rest)
                    if x < y:
                        subs.setdefault((x, y), set()).update({cid, cid2})
    for (x, y), ids in sorted(subs.items()):
        add_edge(nid(x), nid(y), "redundant_with", [f"spellbook:{i}" for i in sorted(ids)], "derived_metric", "spellbook", symmetric=True)
    # role-derived structure
    cm0 = cmdn[0] if cmdn else None
    for n in sorted(zone):
        if zone[n] == "commander" or cm0 is None:
            continue
        if "protection" in role_of[n]:
            add_edge(nid(n), nid(cm0), "protects", [ROLE_REF, f"oracle:{n}"], "heuristic", "role")
        cols = colours_of_source(cards[n], ci)
        if len(cols) >= 2 and ("land" in role_of[n] or "ramp" in role_of[n]):
            add_edge(nid(n), nid(cm0), "fixes", [f"oracle:{n}"], "derived_metric", "role", colours=cols)
    # M1
    ed, st, note = m1_status(slug, export, review)
    m1 = {"status": st, "note": note, "rule_version": ed.get("rule_version") if ed else None,
          "review": rel(review) if review.exists() else None, "review_sha256": sha_file(review)}
    if st in ("invalid", "stale_list", "stale_review"):
        warnings.append(f"M1 edges {st}: {note}")
    corr = m1_corrections(slug)
    if ed:
        ed = json.loads(json.dumps(ed))
        for x in ed["nodes"]:
            apply_m1_correction(x, corr, x.get("interaction") or x["id"].rpartition("/")[2])
        for x in ed["edges"]:
            apply_m1_correction(x, corr, x.get("interaction"))
        for x in ed["nodes"]:
            if x["kind"] in ("combo", "interaction") and x["id"] not in nodes:
                nodes[x["id"]] = {"id": x["id"], "kind": x["kind"], "name": x.get("interaction") or x["id"],
                                  "topic": x.get("topic"), "status": x.get("status"), "flag_kind": x.get("flag_kind"),
                                  "class": x.get("evidence_class"), "spellbook": x.get("spellbook", []), "layer": "m1"}
            elif x["kind"] in ("card", "commander") and x["id"] not in nodes and x.get("in_list") is False:
                pass  # a card the review names that is not in the list: not a graph node
        for x in ed["edges"]:
            if x["from"] not in nodes or x["to"] not in nodes:
                continue
            extra = {"m1_edge": x["id"], "interaction": x["interaction"], "status": x["status"], "flag_kind": x.get("flag_kind")}
            if x.get("graph_kind"):
                add_edge(x["from"], x["to"], x["graph_kind"], x["evidence"], x["evidence_class"], "m1_edges", **extra)
            else:
                ann.append(dict({"from": x["from"], "to": x["to"], "kind": x["kind"], "symmetric": x.get("symmetric", True),
                                 "evidence": x["evidence"], "evidence_class": x["evidence_class"]}, **extra))
    elif review.exists():
        rv = json.loads(review.read_text(encoding="utf-8"))
        for x in rv.get("interactions", []):
            x = apply_m1_correction(dict(x), corr, x["id"])
            hub = f"interaction:{slug}/{x['id']}"
            nodes[hub] = {"id": hub, "kind": "interaction", "name": x["id"], "topic": x.get("topic"), "status": x.get("status"),
                          "flag_kind": x.get("flag_kind") or x.get("flag"), "class": x.get("evidence_class") or "fact", "layer": "m1_review"}
            for n in x.get("cards", []):
                if n in zone:
                    add_edge(nid(n), hub, "member_of", [f"review:{rel(review)}#{x['id']}"], x.get("evidence_class") or "fact", "m1_review",
                             interaction=x["id"], status=x.get("status"))
    # metrics
    metrics = card_metrics(zone, qty, nodes, edges, deck_combos, bp, role_of, cards, ci, slug, cmdn)
    edges.sort(key=lambda x: (x["layer"], x["kind"], x["from"], x["to"]))
    ann.sort(key=lambda x: (x["kind"], x["from"], x["to"], x["m1_edge"]))
    doc = {"schema_version": 1, "deck_id": rid, "slug": slug, "generated_by": f"scripts/grixis_graph.py v{VERSION}", "rule_version": RULE,
           "cycle": CYCLE, "list_hash": e["canonical_project_list"]["hash"], "blueprint_version": bp.get("version") or 0,
           "generated_from": sorted(k for k, s in inp.items() if s), "snapshot": {"id": sid, "inputs": inp}, "m1": m1,
           "necessity_rules": NECESSITY, "warnings": warnings,
           "counts": {"cards": sum(1 for x in nodes.values() if x["kind"] in ("card", "commander")), "nodes": len(nodes),
                      "edges": len(edges), "annotations": len(ann), "combos": len(deck_combos),
                      "by_layer": dict(sorted({l: sum(1 for x in edges if x["layer"] == l) for l in {x["layer"] for x in edges}}.items()))},
           "nodes": [nodes[k] for k in sorted(nodes)], "edges": edges, "annotations": ann, "metrics": metrics}
    return doc


def best_alternative(n, roles, pkgs, bp, slug, R, ci, zone):
    """Best in-identity EDHREC candidate (evidence layer) sharing a key role; blueprint package candidates first."""
    import grixis_refine as gr
    ev = EVID / f"{slug}.json"
    if not ev.exists():
        return None, None
    key = getattr(best_alternative, "_cache", {})
    if slug not in key:
        d = json.loads(ev.read_text(encoding="utf-8"))
        cols = d["edhrec"]["columns"]
        cands = []
        for x in d["vectors"]:
            if x["status"] != "candidate" or x["card"] in zone:
                continue
            c, _ = R.get(x["card"])
            if not c:
                continue
            tl = c.get("type_line") or " // ".join(f.get("type_line", "") for f in c.get("card_faces", []))
            rs = set(gr.roles(c)) | ({"land"} if "Land" in tl else set())
            row = dict(zip(cols, x["edhrec"])) if x.get("edhrec") else {}
            cands.append((x["card"], rs, row, (x.get("oracle_hook") or {}).get("label")))
        hooks = {x["card"]: (x.get("oracle_hook") or {}).get("label") for x in d["vectors"] if x["status"] != "candidate"}
        key[slug] = (cands, hooks)
        best_alternative._cache = key
    cands, hooks = key[slug]
    pkg_c = {m for p in bp.get("packages", []) if p["id"] in pkgs for m in (p.get("candidates") or [])}
    rs = set(roles) - {"ramp"} if set(roles) - {"ramp"} else set(roles)
    hook = hooks.get(n)
    basis = "shared key role"
    pool = [c for c in cands if c[0] in pkg_c or c[1] & rs]
    if not pool and hook:
        pool, basis = [c for c in cands if c[3] == hook], f"same Oracle hook ({hook})"
    if not pool:
        return None, None
    pool.sort(key=lambda c: (c[0] not in pkg_c, -(c[2].get("synergy") if c[2].get("synergy") is not None else -9),
                             -(c[2].get("inclusion") or 0), c[0]))
    b = pool[0]
    return b[0], {"basis": "blueprint package candidate" if b[0] in pkg_c else basis, "shared_roles": sorted(b[1] & rs),
                  "synergy": b[2].get("synergy"), "inclusion": b[2].get("inclusion"),
                  "evidence": f"evidence:data/grixis/evidence/{slug}.json#{b[0]}"}


def card_metrics(zone, qty, nodes, edges, deck_combos, bp, role_of, cards, ci, slug, cmdn):
    import evaluate_decklist as ev
    R = getattr(card_metrics, "_R", None) or ev.Resolver()
    card_metrics._R = R
    combos_of = {}
    for co in deck_combos:
        for n in co["cards"]:
            combos_of.setdefault(n, []).append(co["id"])
    subs = {}
    for x in edges:
        if x["kind"] == "redundant_with":
            a, b = x["from"].split(":", 1)[1], x["to"].split(":", 1)[1]
            subs.setdefault(a, set()).add(b)
            subs.setdefault(b, set()).add(a)
    wins = {x["to"]: [] for x in edges if x["to"].startswith("win:")}
    for x in edges:
        if x["to"].startswith("win:") and x["kind"] == "piece_of":
            wins[x["to"]].append(x["from"].split(":", 1)[1])
    engines = {}
    for x in edges:
        if x["to"].startswith("engine:"):
            engines.setdefault(x["to"], []).append(x["from"].split(":", 1)[1])
    enablers = {x["from"].split(":", 1)[1] for x in edges if x["kind"] == "enables"}
    pkg = {p["id"]: p for p in bp.get("packages", [])}
    out = {}
    for n in sorted(zone):
        nd = nodes[("commander:" if zone[n] == "commander" else "card:") + n]
        brk = [f"combo:{i}" for i in sorted(combos_of.get(n, []))]
        nec_reasons = []
        for w, pcs in sorted(wins.items()):
            if n in pcs:
                others = [p for p in pcs if p != n and p not in cmdn]
                wc = [co for co in deck_combos if set(co["cards"]) & set(pcs)]
                if (not others) or (wc and all(n in co["cards"] for co in wc)):
                    brk.append(w)
                    nec_reasons.append(w)
        for g, mem in sorted(engines.items()):
            if mem == [n]:
                brk.append(g)
                nec_reasons.append(g)
        for pid in nd["packages"]:
            p = pkg[pid]
            pn = pkg_node(pid)
            if p.get("required") and p.get("min_count") and nodes[pn]["count_in_list"] - qty[n] < p["min_count"]:
                brk.append(pn)
                nec_reasons.append(pn)
        if deck_combos and all(n in co["cards"] for co in deck_combos):
            nec_reasons.append("all-combos")
        key_roles = [r for r in role_of[n] if r != "land"]
        if n in subs:
            red, basis = len(subs[n]), "interchangeable Spellbook pieces"
        elif nd["packages"]:
            red = max(nodes[pkg_node(p)]["count_in_list"] for p in nd["packages"]) - qty[n]
            basis = "other cards in its package(s)"
        elif key_roles:
            red = sum(qty[m] for m in zone if m != n and zone[m] != "commander" and set(role_of[m]) & set(key_roles))
            basis = "other cards sharing a key role"
        elif "land" in role_of[n]:
            cols = set(colours_of_source(cards[n], ci))
            red = sum(qty[m] for m in zone if "land" in role_of[m] and (m != n) and (not cols or cols & set(colours_of_source(cards[m], ci)))) + (qty[n] - 1)
            basis = "other lands sharing a colour"
        else:
            red, basis = 0, "no shared job"
        red = max(red, 0)
        if zone[n] == "commander" or nec_reasons:
            nec = "necessary"
        elif brk or nd["identity_core"] or nd["tutor_target"] or n in enablers or any(n in p for p in wins.values()):
            nec = "important"
        elif (nd["packages"] or key_roles or "land" in role_of[n]) and red >= 1:
            nec = "redundant"
        else:
            nec = "independent"
        alt, alt_info = (None, None) if zone[n] == "commander" else best_alternative(n, role_of[n], nd["packages"], bp, slug, R, ci, zone)
        out[n] = {"structural_necessity": nec, "breaks_if_removed": brk, "redundancy": red, "redundancy_basis": basis,
                  "best_alternative_in_role": alt, "alternative": alt_info, "necessity_reasons": nec_reasons,
                  "combos": sorted(combos_of.get(n, [])), "interchangeable_with": sorted(subs.get(n, []))}
    return out


def dump(doc):
    """Readable header; one node / edge / annotation / metric per line (diff-friendly, about a third of indent=1)."""
    big = ("nodes", "edges", "annotations", "metrics")
    head = {k: v for k, v in doc.items() if k not in big}
    out = json.dumps(head, indent=1, ensure_ascii=False)[:-2] + ",\n"
    parts = []
    for k in big:
        if isinstance(doc[k], dict):
            rows = [f"  {json.dumps(n, ensure_ascii=False)}: {json.dumps(v, ensure_ascii=False, separators=(',', ':'))}" for n, v in doc[k].items()]
            parts.append(f' "{k}": {{' + ("\n" + ",\n".join(rows) + "\n " if rows else "") + "}")
        else:
            rows = [f"  {json.dumps(x, ensure_ascii=False, separators=(',', ':'))}" for x in doc[k]]
            parts.append(f' "{k}": [' + ("\n" + ",\n".join(rows) + "\n " if rows else "") + "]")
    return out + ",\n".join(parts) + "\n}\n"


def build(only=None, verbose=True):
    import evaluate_decklist as ev
    R = ev.Resolver()
    reg = ga.load_json(ga.REGISTRY)
    combos = json.loads(COMBOS.read_text(encoding="utf-8"))["decks"]
    OUT.mkdir(parents=True, exist_ok=True)
    n = 0
    for did, v in sorted(ga.summary().items(), key=lambda x: x[1]["slug"]):
        if only and v["slug"] != only:
            continue
        doc = build_deck(did, v, R, combos, reg)
        (OUT / f"{v['slug']}.json").write_text(dump(doc), encoding="utf-8")
        n += 1
        if verbose:
            c = doc["counts"]
            print(f"{v['slug']}: {c['nodes']} nodes, {c['edges']} edges ({c['annotations']} annotations), M1 {doc['m1']['status']}")
    return n


def check(verbose=True, rebuild=True):
    import evaluate_decklist as ev
    p, warn = [], []
    summ = ga.summary()
    want = {v["slug"]: (did, v) for did, v in summ.items()}
    files = {f.stem: f for f in OUT.glob("*.json")}
    for s in sorted(set(want) - set(files)):
        p.append(f"{s}: no dependency graph (run --build)")
    for s in sorted(set(files) - set(want)):
        p.append(f"{s}: graph for an unknown deck")
    have_cache = (ROOT / ".cache").exists()
    R = ev.Resolver() if have_cache and rebuild else None
    reg = ga.load_json(ga.REGISTRY)
    combos = json.loads(COMBOS.read_text(encoding="utf-8"))["decks"]
    st = {}
    for s, f in sorted(files.items()):
        if s not in want:
            continue
        doc = json.loads(f.read_text(encoding="utf-8"))
        for e in ga.validate_file(doc, "graph.schema.json"):
            p.append(f"{s}: {e}")
        did, v = want[s]
        if doc["list_hash"] != reg["decks"][ga.registry_id(did)]["canonical_project_list"]["hash"]:
            p.append(f"{s}: list_hash is not the canonical list hash (stale; run --build)")
        export = ROOT / reg["decks"][ga.registry_id(did)]["canonical_project_list"]["export"]
        inp, sid = deck_inputs(s, export, did)
        if sid != doc["snapshot"]["id"]:
            changed = sorted(k for k in inp if inp[k] != doc["snapshot"]["inputs"].get(k))
            if changed and all(k.startswith("data/grixis_interactions/") for k in changed):
                warn.append(f"{s}: M1 review/edges changed ({', '.join(changed)}): regenerate with --build to ingest")
            else:
                p.append(f"{s}: stale snapshot ({', '.join(changed)}); run --build")
        ids = {x["id"] for x in doc["nodes"]}
        for x in doc["edges"]:
            if x["from"] not in ids or x["to"] not in ids:
                p.append(f"{s}: edge {x['from']} -> {x['to']} names an unknown node")
                break
        cardn = {x["name"] for x in doc["nodes"] if x["kind"] in ("card", "commander")}
        if set(doc["metrics"]) != cardn:
            p.append(f"{s}: metrics don't cover exactly the list's cards")
        st[doc["m1"]["status"]] = st.get(doc["m1"]["status"], 0) + 1
        if R is not None and sid == doc["snapshot"]["id"] and s in ("wick-the-whorled-mind", "abaddon-the-despoiler"):
            if dump(build_deck(did, v, R, combos, reg)) != f.read_text(encoding="utf-8"):
                p.append(f"{s}: rebuild does not reproduce the stored graph")
    if verbose:
        print(f"graph: {len(files)} deck graph(s); M1 ingest {dict(sorted(st.items()))}; {len(p)} problem(s), {len(warn)} warning(s)")
        for x in (p + warn)[:30]:
            print("  -", x)
    return p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--deck")
    ap.add_argument("--show", nargs=2, metavar=("SLUG", "CARD"))
    a = ap.parse_args()
    if a.build:
        build(a.deck)
        return 0
    if a.show:
        d = json.loads((OUT / f"{a.show[0]}.json").read_text(encoding="utf-8"))
        n = a.show[1]
        print(json.dumps({"metrics": d["metrics"].get(n), "edges": [x for x in d["edges"] if n in (x["from"].split(":", 1)[1], x["to"].split(":", 1)[1])]},
                         indent=1, ensure_ascii=False))
        return 0
    return 1 if check() else 0


if __name__ == "__main__":
    sys.exit(main())
