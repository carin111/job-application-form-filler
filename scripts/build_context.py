#!/usr/bin/env python3
"""Build a small role-specific context packet without loading the full private bank."""
from __future__ import annotations
import argparse, json, os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = Path(os.environ.get("JOB_APPLICATION_DATA_DIR", Path.home()/".job-application-form-filler"))

def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def resolve_role(raw: str, cfg: dict) -> str:
    needle=raw.strip().lower()
    for role, spec in cfg["roles"].items():
        if needle==role or needle in [str(x).lower() for x in spec.get("aliases",[])]:
            return role
    return "general"

def compact(value):
    if value in (None,"",[],{},"UNKNOWN"):
        return None
    return value

def render_value(value):
    if isinstance(value,list):
        return "; ".join(render_value(x) for x in value if compact(x) is not None)
    if isinstance(value,dict):
        return "; ".join(f"{k}: {render_value(v)}" for k,v in value.items() if compact(v) is not None)
    return str(value)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--role",default="general")
    ap.add_argument("--language",choices=["zh","en"],default="zh")
    ap.add_argument("--data-dir",type=Path,default=DEFAULT_DATA)
    ap.add_argument("--sections",help="Comma-separated profile sections")
    ap.add_argument("--max-experiences",type=int)
    ap.add_argument("--kinds",help="Comma-separated kinds; defaults to the selected role configuration")
    ap.add_argument("--keywords",default="",help="Comma-separated tags to boost")
    ap.add_argument("--include-id",action="append",default=[])
    ap.add_argument("--list",action="store_true",help="List metadata only")
    ap.add_argument("--format",choices=["markdown","json"],default="markdown")
    args=ap.parse_args()

    cfg=load_json(ROOT/"config"/"targeting.json")
    role=resolve_role(args.role,cfg)
    data=args.data_dir.expanduser().resolve()
    profile_path=data/"profile.private.json"
    index_path=data/"experience-index.private.json"
    if not profile_path.exists() or not index_path.exists():
        raise SystemExit(f"Private data missing in {data}. Run init_private_data.py first.")
    profile=load_json(profile_path)
    index=load_json(index_path).get("experiences",[])

    if args.list:
        rows=[{k:x.get(k) for k in ("id","kind","tags","priority")} for x in index]
        print(json.dumps(rows,ensure_ascii=False,indent=2))
        return

    sections=[x.strip() for x in (args.sections or ",".join(cfg["default_profile_sections"])).split(",") if x.strip()]
    selected_profile={k:profile.get(k) for k in sections if compact(profile.get(k)) is not None}
    kinds_raw=args.kinds or ",".join(cfg["roles"][role].get("default_kinds",["internship","employment"]))
    allowed={x.strip() for x in kinds_raw.split(",") if x.strip()}
    role_tags=cfg["roles"][role].get("tags",[])
    extra=[x.strip().lower() for x in args.keywords.split(",") if x.strip()]
    weights={tag:(len(role_tags)-i)*10 for i,tag in enumerate(role_tags)}
    for tag in extra: weights[tag]=weights.get(tag,0)+100

    def score(item):
        tags=[str(x).lower() for x in item.get("tags",[])]
        return int(item.get("role_priority",{}).get(role,0))*1000 + sum(weights.get(t,0) for t in tags)+int(item.get("priority",0))

    candidates=[x for x in index if x.get("kind","internship") in allowed]
    candidates.sort(key=lambda x:(x.get("id") in args.include_id,score(x),x.get("priority",0)),reverse=True)
    limit=args.max_experiences or cfg["roles"][role].get("default_max",3)
    chosen=[]
    seen=set()
    for item in candidates:
        if item.get("id") in seen: continue
        if score(item)<=0 and item.get("id") not in args.include_id: continue
        chosen.append(item); seen.add(item.get("id"))
        if len(chosen)>=limit: break
    for wanted in args.include_id:
        if wanted not in seen:
            item=next((x for x in index if x.get("id")==wanted),None)
            if item: chosen.append(item); seen.add(wanted)

    experiences=[]
    for item in chosen:
        path=data/item["file"]
        if not path.exists(): raise SystemExit(f"Missing experience file: {path}")
        exp=load_json(path)
        experiences.append({k:v for k,v in exp.items() if compact(v) is not None})

    packet={"role":role,"target_language":args.language,"profile":selected_profile,"experiences":experiences,"permissions":profile.get("preferences",{})}
    if args.format=="json":
        print(json.dumps(packet,ensure_ascii=False,separators=(",",":")))
        return
    print(f"# Application context\nrole: {role}\ntarget_language: {args.language}")
    print("\n## Profile")
    for key,value in selected_profile.items(): print(f"- {key}: {render_value(value)}")
    print("\n## Selected experiences")
    for exp in experiences:
        print(f"\n### {exp.get('organization','')} | {exp.get('title','')} | {exp.get('start','')}–{exp.get('end','')}")
        print(exp.get("description",exp.get("description_zh","")))
        if exp.get("metrics"): print("Metrics: "+render_value(exp["metrics"]))
        if exp.get("do_not_claim"): print("Do not claim: "+render_value(exp["do_not_claim"]))
    print("\n## Permission defaults")
    for key,value in profile.get("preferences",{}).items(): print(f"- {key}: {value}")

if __name__=="__main__": main()
