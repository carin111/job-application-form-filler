#!/usr/bin/env python3
"""Maintain a compact local progress record for multi-turn form filling."""
from __future__ import annotations
import argparse, json, os
from datetime import datetime, timezone
from pathlib import Path
DEFAULT=Path(os.environ.get("JOB_APPLICATION_DATA_DIR",Path.home()/".job-application-form-filler"))

def bool_arg(v):
    return {"true":True,"false":False}[v.lower()]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--data-dir",type=Path,default=DEFAULT); ap.add_argument("--key",required=True,help="Short non-secret application key"); ap.add_argument("--site"); ap.add_argument("--role"); ap.add_argument("--language"); ap.add_argument("--complete",action="append",default=[]); ap.add_argument("--pending",action="append",default=[]); ap.add_argument("--saved",type=bool_arg); ap.add_argument("--submitted",type=bool_arg); args=ap.parse_args()
    path=args.data_dir.expanduser().resolve()/"applications"/(args.key+".private.json"); path.parent.mkdir(parents=True,exist_ok=True)
    state=json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"key":args.key,"completed_sections":[],"pending_sections":[],"saved":False,"submitted":False}
    for k in ("site","role","language"):
        v=getattr(args,k)
        if v is not None: state[k]=v
    for x in args.complete:
        if x not in state["completed_sections"]: state["completed_sections"].append(x)
        if x in state["pending_sections"]: state["pending_sections"].remove(x)
    for x in args.pending:
        if x not in state["pending_sections"] and x not in state["completed_sections"]: state["pending_sections"].append(x)
    if args.saved is not None: state["saved"]=args.saved
    if args.submitted is not None: state["submitted"]=args.submitted
    state["updated_at"]=datetime.now(timezone.utc).isoformat()
    path.write_text(json.dumps(state,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(state,ensure_ascii=False,separators=(",",":")))
if __name__=="__main__": main()
