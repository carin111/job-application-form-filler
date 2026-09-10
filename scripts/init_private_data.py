#!/usr/bin/env python3
"""Create a private data directory from fictional examples without overwriting files."""
from __future__ import annotations
import argparse, os, shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DEFAULT=Path(os.environ.get("JOB_APPLICATION_DATA_DIR",Path.home()/".job-application-form-filler"))

def copy_new(src:Path,dst:Path):
    if dst.exists(): return False
    dst.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(src,dst); return True

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--data-dir",type=Path,default=DEFAULT); args=ap.parse_args()
    data=args.data_dir.expanduser().resolve(); created=[]
    pairs=[(ROOT/"examples/profile.example.json",data/"profile.private.json"),(ROOT/"examples/experience-index.example.json",data/"experience-index.private.json"),(ROOT/"examples/experiences/example-ecommerce-internship.json",data/"experiences/example-ecommerce-internship.json")]
    for src,dst in pairs:
        if copy_new(src,dst): created.append(str(dst))
    (data/"applications").mkdir(parents=True,exist_ok=True)
    print("Private data directory:",data)
    print("Created:" if created else "No files created; existing private files were preserved.")
    for p in created: print("-",p)
    print("Replace fictional values locally and never commit this directory.")
if __name__=="__main__": main()
