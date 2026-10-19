"""Cycle129 frozen-Oracle and canonical-source validation, NOT Pass C."""
import json,sys,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import evaluate_decklist as ev
import grixis_authority as ga
import grixis_sim as sim
from collections import Counter
def load(p):return json.loads((ROOT/p).read_text())
def validate():
 rows=load("data/grixis/m6/author_reviews/cycle129_six_detailed_01.json")
 plan=load("data/grixis/m6/phase_b_plans/cycle129_six_commander_reviews_preregistered_01.json")
 reg=load("data/grixis/registry.json");track=load("data/grixis/milestone_m6_m7_subtracker.json")
 queues={x["deck_id"]:x for x in load("data/grixis/m6/phase_b_bounded/commander_first_readiness_62_01.json")["ordered_decks"]}
 prior=load("data/grixis/m6/author_reviews/cycle128_six_commander_authored_judgments_01.json")
 ids=[x["deck_id"] for x in rows["rows"]]
 assert plan["cycle"]==129 and rows["review_count"]==len(ids)==6 and len(set(ids))==6
 assert set(ids).isdisjoint(x["deck_id"] for x in prior["rows"])
 assert (rows["prior_authored"],rows["authored_if_verified"])==(21,27)
 assert track["m6"]["gates"][3]["completed"]==21
 assert track["m6"]["formal_m6_certified_decks"]==0
 assert reg["program"]["milestones"]["M6"]["status"]=="in_progress"
 R=ev.Resolver();out=[]
 for item in rows["rows"]:
  did=item["deck_id"];m=reg["decks"][did];q=queues[did];c=q["first_three_TO_REVIEW_NOT_TO_APPLY"][0]
  assert (item["add"],item["cut"])==(c["add"],c["cut"])
  assert c["swap_id"].startswith("swap:"+m["slug"]+":m5:")
  assert m["current_canonical_hash"]==q["source_canonical_logical_hash"]
  assert m["source"]["recorded_matches_raw"]
  assert ga.text_hash(ga.deck_block_text(m["slug"]),R)==m["current_canonical_hash"]
  deck=sim.load_deck(m["slug"],R);names=[v["name"] for v in deck.library]
  assert len(names)==99 and len(deck.commanders)==1
  assert names.count(item["cut"])==1 and item["add"] not in names
  assert not {n:k for n,k in Counter(names).items() if k>1 and n not in ("Island","Swamp","Mountain","Forest","Plains","Wastes")}
  assert item["positive"] and item["cut_cost"] and item["reason"] and item["next"] and len(item["rules"])>=5
  assert item["approved_swaps"]==0 and not item["independent_pass_c"] and not item["complete_phase_b"]
  cardhash={}
  for name in [m["commanders"][0],item["add"],item["cut"]]:
   obj,fuzzy=R.get(name);assert obj is not None and not fuzzy and obj["name"]==name,name
   txt=obj.get("oracle_text") or "\n".join(f.get("oracle_text") or "" for f in obj.get("card_faces",[]))
   assert txt;cardhash[name]=hashlib.sha256(txt.encode()).hexdigest()
  out.append({"deck_id":did,"M5_swap":c["swap_id"],"logical_hash":m["current_canonical_hash"],"oracle_text_hashes":cardhash,
   "official_snapshot_status":m["official_commander_compliance"]["status"],"exceptions":m["project_exceptions"],"independent_pass_c":False})
 j=next(x for x in out if x["deck_id"]=="The_Madcap_Jester")
 assert j["official_snapshot_status"]=="pending_release" and len(j["exceptions"])==2
 return {"cycle":129,"authored_total":27,"checks":out,"independent_pass_c":0,"phase_b_full":0,"canonical_edits":0}
if __name__=="__main__":
 print(json.dumps(validate(),sort_keys=True,indent=2))
