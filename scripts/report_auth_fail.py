#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, os
from datetime import datetime
from collections import Counter

LOG_RAW = f"logs/auth_failed_{datetime.now():%F}.log"
REPORT = f"reports/failed_login_report_{datetime.now():%F}.md"

if not os.path.exists(LOG_RAW) or os.path.getsize(LOG_RAW) == 0:
    print("No RAW log for today. Populate logs/auth_failed_YYYY-MM-DD.log first."); exit(1)

# Example line:
# Aug 22 10:24:57 kali sshd-session[37139]: Failed password for invalid user usernotexists from 127.0.0.1 port 38194 ssh2
line_re = re.compile(
    r'^(?P<mon>\w{3})\s+(?P<day>\d{1,2})\s+(?P<time>\d{2}:\d{2}:\d{2}).*sshd.*Failed password for (?P<kind>(invalid user )?)(?P<user>[\w.\-]+) from (?P<ip>[0-9a-fA-F\.:]+)'
)

ips = Counter()
users = Counter()
per_hour = Counter()
invalid_user_count = 0
samples = []

with open(LOG_RAW, 'r', errors='ignore') as f:
    for ln in f:
        m = line_re.search(ln)
        if not m:
            continue
        ip = m.group('ip'); user = m.group('user')
        hour = m.group('time').split(':')[0]
        ips[ip] += 1; users[user] += 1; per_hour[hour] += 1
        if m.group('kind').startswith('invalid'):
            invalid_user_count += 1
        if len(samples) < 5:
            samples.append(ln.strip())

total = sum(ips.values())

os.makedirs("reports", exist_ok=True)
with open(REPORT, 'w', encoding='utf-8') as out:
    out.write(f"# Failed Login Incidents Report — {datetime.now():%F}\n\n")
    out.write(f"- Total failed password attempts: **{total}**\n")
    out.write(f"- Invalid-user attempts: **{invalid_user_count}**\n\n")

    out.write("## Top IPs\n")
    for ip, c in ips.most_common(10):
        out.write(f"- {ip}: {c}\n")

    out.write("\n## Most targeted usernames\n")
    for u, c in users.most_common(10):
        out.write(f"- {u}: {c}\n")

    out.write("\n## Peak hours (hour → count)\n")
    for h, c in sorted(per_hour.items()):
        out.write(f"- {h}:00 → {c}\n")

    out.write("\n## Log samples\n")
    for s in samples:
        out.write(f"- `{s}`\n")

    out.write("\n## Quick recommendations\n")
    out.write("- Enable Fail2ban; prefer SSH keys over passwords; restrict access via UFW; disable unused accounts.\n")

print(f"Done: {REPORT}")
