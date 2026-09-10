#!/usr/bin/env python3
"""Fail on common personal-data and secret patterns before a public push."""
from __future__ import annotations
import argparse, re
from pathlib import Path
SKIP={".git","__pycache__"}; BINARY={".png",".jpg",".jpeg",".webp",".pdf",".docx",".zip"}
PATTERNS={
 "mainland_mobile":re.compile(r"(?<!\d)(?:\+?86[- ]?)?1[3-9]\d{9}(?!\d)"),
 "private_key":re.compile(r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY"),
 "github_token":re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
 "windows_user_path":re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+",re.I),
 "application_identifier":re.compile(r"(?:recommendCode|resumeId|shareId|userId)=[A-Za-z0-9_-]+",re.I),
}
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("path",nargs="?",type=Path,default=Path(__file__).resolve().parents[1]); ap.add_argument("--deny-file",type=Path); args=ap.parse_args(); root=args.path.resolve(); denied=[]
 if args.deny_file and args.deny_file.exists(): denied=[x.strip() for x in args.deny_file.read_text(encoding="utf-8").splitlines() if x.strip() and not x.startswith("#")]
 hits=[]
 for p in root.rglob("*"):
  if not p.is_file() or any(x in SKIP for x in p.parts) or p.suffix.lower() in BINARY: continue
  try:text=p.read_text(encoding="utf-8")
  except UnicodeDecodeError: continue
  for name,rx in PATTERNS.items():
   for m in rx.finditer(text): hits.append((str(p.relative_to(root)),name,m.group(0)))
  for value in denied:
   if value.lower() in text.lower(): hits.append((str(p.relative_to(root)),"deny-list",value))
 if hits:
  print("PUBLIC SCAN FAILED")
  for path,kind,value in hits: print(f"{path}: {kind}: {value}")
  raise SystemExit(1)
 print("PUBLIC SCAN PASSED")
if __name__=="__main__": main()

