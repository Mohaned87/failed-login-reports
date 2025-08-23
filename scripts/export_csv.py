#!/usr/bin/env python3
import re, csv, os
from datetime import datetime
LOG=f"logs/auth_failed_{datetime.now():%F}.log"; OUT=f"reports/failed_login_{datetime.now():%F}.csv"
rx=re.compile(r'^(?P<mon>\w{3})\s+(?P<day>\d{1,2})\s+(?P<time>\d{2}:\d{2}:\d{2}).*sshd.*Failed password for (?P<kind>(invalid user )?)(?P<user>[\w.\-]+) from (?P<ip>[0-9a-fA-F\.:]+) port (?P<port>\d+)')
os.makedirs("reports", exist_ok=True)
with open(LOG, errors="ignore") as f, open(OUT,"w",newline="") as o:
    w=csv.writer(o); w.writerow(["timestamp","user","ip","port","kind"])
    for ln in f:
        m=rx.search(ln); 
        if m: w.writerow([f"{m['mon']} {m['day']} {m['time']}", m['user'], m['ip'], m['port'], "invalid" if m['kind'].startswith("invalid") else "valid"])
print("CSV:", OUT)
