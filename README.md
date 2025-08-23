# failed-login-reports# Failed Login Incidents (SSH) — Daily Report
Parses `journalctl` → outputs Markdown + CSV → simple threshold alert.
Includes scripts, sample report, and screenshots.
## Quick start
```bash
sudo journalctl -t sshd -n 2000 | \
  grep -E 'Failed password|Invalid user|authentication failure|PAM.*authentication failure' \
  > logs/auth_failed_$(date +%F).log

python3 scripts/report_auth_fail.py
python3 scripts/export_csv.py
```
