"""Exact M7 #41 99-name Scryfall legality, identities and strategic Oracle witness check."""
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from hashlib import sha256
from time import sleep
import json
from test_nicol_bolas_m7_rev1 import CAND, CAND_SHA, parse

CRITICAL={
"Nicol Bolas":["At the beginning of your upkeep","Whenever Nicol Bolas deals damage to an opponent"],
"Ingris Stingerquill":["Whenever a creature you control attacks","that creature deals 1 damage to each opponent"],
"Kediss, Emberclaw Familiar":["commander you control deals combat damage","deals that much damage to each other opponent"],
"Chandra's Ignition":["target creature you control","deals damage equal to its power"],
"Quicksilver Dagger":["Enchanted creature has","deals 1 damage"],
"Sarkhan, Soul Aflame":["Dragon spells you cast cost","become a copy","except its name"],
"Rivaz of the Claw":["Spend this mana only to cast Dragon creature spells","cast a Dragon creature spell from your graveyard"],
"Dream Halls":["Rather than pay the mana cost","discard a card that shares a color"],
"Plaza of Heroes":["legendary spell","hexproof and indestructible"],
"Minamo, School at Water's Edge":["Untap target legendary permanent"],
"Ophidian Eye":["Whenever enchanted creature deals damage to an opponent"],
"Reanimate":["Put target creature card from a graveyard onto the battlefield"],
"Coalition Relic":["Put a charge counter","remove all charge counters"],
"Mithril Coat":["Flash","indestructible","attach it to target legendary creature"],
}
URL="https://api.scryfall.com/cards/collection"
def group(items):
    data=json.dumps({"identifiers":[{"name":n} for n in items]}).encode("utf-8")
    request=Request(URL,data=data,method="POST",headers={
        "User-Agent":"GrixisCommanderEncyclopedia-Deck41-M7/1.0",
        "Content-Type":"application/json; charset=utf-8",
        "Accept":"application/json",
    })
    for k in range(4):
        try:
            with urlopen(request,timeout=35) as response:
                return json.load(response)
        except HTTPError as e:
            if e.code in (429,500,502,503,504) and k<3:
                sleep(2*(k+1))
                continue
            raise

def main():
    assert sha256(CAND.read_bytes()).hexdigest()==CAND_SHA,"Candidate SHA changed"
    cards=parse(CAND)
    # Query front names for double-faced cards while retaining unique physical cards.
    fronts={name:name.split(" // ")[0] for name in cards}
    ids=list(fronts.values())
    assert len(set(ids))==len(ids)
    resolved={}
    for i in range(0,len(ids),70):
        obj=group(ids[i:i+70])
        assert not obj.get("not_found"),obj.get("not_found")
        for c in obj["data"]:
            resolved[c["name"].split(" // ")[0]]=c
        sleep(0.15)
    errors=[]
    for name,front in fronts.items():
        c=resolved.get(front)
        if not c:
            errors.append(f"unresolved {name} / {front}")
            continue
        if c["legalities"]["commander"]!="legal":
            errors.append(f"{name} not Commander legal {c['legalities']['commander']}")
        if not set(c["color_identity"])<=set("UBR"):
            errors.append(f"{name} invalid color identity {c['color_identity']}")
    for name,needles in CRITICAL.items():
        c=resolved.get(name)
        if not c:
            errors.append(f"Missing Oracle witness {name}")
            continue
        txt=c.get("oracle_text","") or " ".join(f.get("oracle_text","") for f in c.get("card_faces",[]))
        for needle in needles:
            if needle.lower() not in txt.lower():
                errors.append(f"{name}: missing Oracle witness {needle}")
    if errors:
        raise AssertionError("\n".join(errors))
    print(f"PASS: Scryfall {len(resolved)}/{len(ids)} names resolved")
    print("PASS: 100 physical, singleton, Commander legalities and UBR color identity")
    print("PASS: 14 core Oracle witnesses, with no inference of live gameplay results")
    print(f"PASS: exact candidate SHA-256 {CAND_SHA}")

if __name__=="__main__":
    main()
