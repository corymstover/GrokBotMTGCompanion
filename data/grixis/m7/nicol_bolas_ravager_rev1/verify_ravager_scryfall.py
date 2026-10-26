"""M7 #42 Ravager live Scryfall collection, Commander legality and Oracle witnesses."""
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from hashlib import sha256
from time import sleep
import json
from test_ravager_m7_rev1 import CAND, CAND_SHA, parse

CRITICAL = {
    "Nicol Bolas, the Ravager": ["each opponent discards a card", "return him transformed"],
    "Aetheric Amplifier": ["Add one mana of any color", "Double the number of each kind of counter on target permanent"],
    "Teferi's Talent": ["Enchant planeswalker", "Whenever you draw a card, put a loyalty counter", "You get an emblem"],
    "Experimental Augury": ["Look at the top three cards of your library", "Proliferate"],
    "Time Warp": ["Target player takes an extra turn"],
    "Chandra, Torch of Defiance": ["Add {R}{R}", "deals 4 damage to target creature"],
    "Vronos, Masked Inquisitor": ["Up to two other target planeswalkers you control phase out", "For each opponent, return up to one target nonland permanent"],
    "Training Grounds": ["Activated abilities of creatures you control cost {2} less"],
    "Deepglow Skate": ["Double the number of each kind of counter"],
    "Rowan's Talent": ["Whenever you activate a loyalty ability"],
    "The Chain Veil": ["you may activate loyalty abilities of planeswalkers"],
}
URL = "https://api.scryfall.com/cards/collection"

def group(names):
    data=json.dumps({"identifiers":[{"name":name} for name in names]}).encode("utf-8")
    request=Request(URL,data=data,method="POST",headers={
        "User-Agent":"GrixisCommanderEncyclopedia-RavagerM7-Rev1/1.0",
        "Content-Type":"application/json; charset=utf-8",
        "Accept":"application/json",
    })
    for attempt in range(4):
        try:
            with urlopen(request, timeout=35) as response:
                return json.load(response)
        except HTTPError as exc:
            if exc.code in (429,500,502,503,504) and attempt<3:
                sleep(2*(attempt+1))
                continue
            raise

def main():
    assert sha256(CAND.read_bytes()).hexdigest()==CAND_SHA, "Candidate SHA changed"
    cards=parse(CAND)
    fronts={name:name.split(" // ")[0] for name in cards}
    names=list(fronts.values())
    assert len(set(names))==len(names)
    resolved={}
    for start in range(0,len(names),70):
        payload=group(names[start:start+70])
        assert not payload.get("not_found"),payload.get("not_found")
        for card in payload["data"]:
            resolved[card["name"].split(" // ")[0]]=card
        sleep(0.2)
    errors=[]
    for physical,front in fronts.items():
        card=resolved.get(front)
        if not card:
            errors.append(f"UNRESOLVED {physical}")
            continue
        if card["legalities"]["commander"]!="legal":
            errors.append(f"Commander legality {physical}: {card['legalities']['commander']}")
        if not set(card["color_identity"])<=set("UBR"):
            errors.append(f"Out-of-identity {physical}: {card['color_identity']}")
    for name,needles in CRITICAL.items():
        card=resolved.get(name)
        if not card:
            errors.append(f"Missing Oracle source {name}")
            continue
        oracle=card.get("oracle_text","") or " ".join(face.get("oracle_text","") for face in card.get("card_faces",[]))
        for needle in needles:
            if needle.lower() not in oracle.lower():
                errors.append(f"Oracle witness missing: {name} / {needle}")
    if errors:
        raise AssertionError("\n".join(errors))
    print(f"PASS: {len(resolved)}/{len(names)} unique physical names Scryfall resolved")
    print("PASS: all names Commander legal, all within UBR and all critical Oracle witnesses")
    print(f"PASS: SHA-256 {CAND_SHA}; 100 copies and basic-only repeats separately verified")
    print("Limits: finite Oracle/source checks, no measured multiplayer game results")

if __name__=="__main__":
    main()
