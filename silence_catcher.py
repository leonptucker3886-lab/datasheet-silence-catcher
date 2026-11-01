#!/usr/bin/env python3
"""Silence Catcher v0.1 - flags members silent past a threshold.
Input: JSON list of {"name":..., "last_post":"ISO8601"}.
Usage: python3 silence_catcher.py roster.json [--minutes 60]
Exit code 1 if anyone is silent (usable in CI/cron)."""
import json, sys, argparse
from datetime import datetime, timezone
p=argparse.ArgumentParser(); p.add_argument("roster"); p.add_argument("--minutes",type=int,default=60)
a=p.parse_args(); now=datetime.now(timezone.utc); silent=[]
print("Last checked:", now.strftime("%Y-%m-%d %H:%M:%S UTC"))
for m in json.load(open(a.roster)):
    t=datetime.fromisoformat(m["last_post"].replace("Z","+00:00"))
    mins=int((now-t).total_seconds()//60)
    flag="SILENT" if mins>a.minutes else "ok"
    if flag=="SILENT": silent.append(m["name"])
    print(f"{flag:7} {m['name']:25} last post {mins} min ago")
if silent: print("ESCALATE:", ", ".join(silent)); sys.exit(1)
print("All members active.")
