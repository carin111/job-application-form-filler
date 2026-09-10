#!/usr/bin/env python3
"""Validate the private fact bank using only the Python standard library."""
from __future__ import annotations
import argparse, json, os
from pathlib import Path
DEFAULT=Path(os.environ.get("JOB_APPLICATION_DATA_DIR",Path.home()/".job-application-form-filler"))

def load(path):
    with path.open("r",encoding="utf-8") as f:return json.load(f)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--data-dir",type=Path,default=DEFAULT); args=ap.parse_args(); data=args.data_dir.expanduser().resolve(); errors=[]; warnings=[]
    pp=data/"profile.private.json"; ip=data/"experience-index.private.json"
    for p in (pp,ip):
        if not p.exists(): errors.append(f"missing {p}")
    if errors:
        print("INVALID"); [print("ERROR:",x) for x in errors]; raise SystemExit(1)
    try: profile=load(pp); index=load(ip)
    except Exception as e: print("INVALID\nERROR:",e); raise SystemExit(1)
    if not isinstance(profile,dict): errors.append("profile must be an object")
    items=index.get("experiences") if isinstance(index,dict) else None
    if not isinstance(items,list): errors.append("experience-index.experiences must be a list"); items=[]
    ids=set()
    for n,item in enumerate(items):
        for key in ("id","kind","file","tags"):
            if key not in item: errors.append(f"index item {n} missing {key}")
        eid=item.get("id")
        if eid in ids: errors.append(f"duplicate id {eid}")
        ids.add(eid)
        rel=item.get("file")
        if rel:
            p=data/rel
            if not p.exists(): errors.append(f"missing file for {eid}: {p}")
            else:
                try: exp=load(p)
                except Exception as e: errors.append(f"invalid JSON {p}: {e}"); continue
                for key in ("id","kind","organization","title","start","end","description"):
                    if not exp.get(key): errors.append(f"{eid} missing {key}")
                if exp.get("id")!=eid: errors.append(f"id mismatch for {eid}")
                if "<" in json.dumps(exp,ensure_ascii=False): warnings.append(f"possible placeholder in {eid}")
    print("VALID" if not errors else "INVALID")
    print(f"experiences={len(items)} warnings={len(warnings)} errors={len(errors)}")
    [print("WARNING:",x) for x in warnings]; [print("ERROR:",x) for x in errors]
    raise SystemExit(1 if errors else 0)
if __name__=="__main__": main()
