#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.." || exit 1
mkdir -p logs reports

# 1) جمع الـ RAW لليوم (آخر 2000 سطر كافية)
if ! journalctl -t sshd -n 2000 | grep -E 'Failed password|Invalid user|authentication failure|PAM.*authentication failure' > "logs/auth_failed_$(date +%F).log"; then
  journalctl -u ssh  -n 2000 | grep -E 'Failed password|Invalid user|authentication failure|PAM.*authentication failure' > "logs/auth_failed_$(date +%F).log"
fi

# 2) تقرير Markdown
python3 scripts/report_auth_fail.py

# 3) تصدير CSV (لو عندك الملف من قبل)
[ -f scripts/export_csv.py ] && python3 scripts/export_csv.py

# 4) تنبيه إذا تعدّت المحاولات حد معيّن
th=20
cnt=$(grep -c 'Failed password' "logs/auth_failed_$(date +%F).log" || echo 0)
if [ "$cnt" -ge "$th" ]; then
  echo "[ALERT] $cnt failed logins today" | tee -a alerts.log
  command -v notify-send >/dev/null && notify-send "SSH Alert" "$cnt failed logins today"
fi

echo "Done: reports/failed_login_report_$(date +%F).md"
