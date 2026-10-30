import json,sys,os
def P(prefix): 
    return lambda k: k
def spec(pack_id, arc, stage, scope, pages, entities, claims, remaining):
    ents=[{"id":i,"type":t,"name":n} for i,t,n in entities]
    cl=[]
    for c in claims:
        cid,subj,pred,obj,grade,quotes,summary=c[:7]
        d={"id":cid,"subject":subj,"predicate":pred,"object":obj,"grade":grade,
           "quotes":[{"page":p,"quote":q} for p,q in quotes],"summary":summary}
        if len(c)>7 and c[7]: d["limitation"]=c[7]
        if len(c)>8 and c[8]: d["event_stage"]=c[8]
        cl.append(d)
    out={"pack_id":pack_id,"arc":arc,"event_stage":stage,"scope":scope,"pages":pages,"entities":ents,"claims":cl,"remaining":remaining}
    p=os.environ.get("MV_ROOT","/workspace/mv-b4")+f"/data/lore_research/claim_specs/{pack_id}.spec.json"
    json.dump(out,open(p,"w"),ensure_ascii=False,indent=1); open(p,"a").write("\n"); print("wrote",p,len(cl))
