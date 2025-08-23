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

## Structure
failed-login-reports/
├─ scripts/
├─ reports/
└─ screenshots/

- Fail2ban (sshd jail), UFW allow-list, cron schedule.

## Artifacts (2025-08-22)
- [Markdown report](reports/failed_login_report_2025-08-22.md)
- [CSV export](reports/failed_login_2025-08-22.csv)
- [PDF](reports/Failed_Login_Incidents_2025-08-22.pdf)

## Screenshots
<details><summary><b>01 — SSHD config (INFO, keys-only)</b></summary>
<p><img src="screenshots/01-sshd-config.png" alt="sshd_config shows LogLevel INFO and PasswordAuthentication no" /></p>
</details>

<details><summary><b>02 — Generate failed attempts</b></summary>
<p><img src="screenshots/02-generate-fails.png" alt="sshpass loop sending wrong passwords to localhost" /></p>
</details>

<details><summary><b>03 — Raw sample (journalctl)</b></summary>
<p><img src="screenshots/03-raw-sample.png" alt="terminal sample of raw journalctl lines" /></p>
</details>

<details><summary><b>04 — Raw count & head</b></summary>
<p><img src="screenshots/04-raw-count.png" alt="wc/head output for today’s RAW file" /></p>
</details>

<details><summary><b>05 — Run report script</b></summary>
<p><img src="screenshots/05-run-report-script.png" alt="running report_auth_fail.py successfully" /></p>
</details>

<details><summary><b>06 — Markdown report preview</b></summary>
<p><img src="screenshots/06-md-report.png" alt="markdown report KPIs and samples" /></p>
</details>

<details><summary><b>07 — CSV export</b></summary>
<p><img src="screenshots/07-csv-export.png" alt="CSV export created under reports/" /></p>
</details>

<details><summary><b>08 — Threshold alert</b></summary>
<p><img src="screenshots/08-threshold-alert.png" alt="terminal alert showing count ≥ threshold" /></p>
</details>

<details><summary><b>09 — Project structure</b></summary>
<p><img src="screenshots/09-project-structure.png" alt="project tree showing logs/reports/scripts" /></p>
</details>

<details><summary><b>10 — Harden back (keys-only)</b></summary>
<p><img src="screenshots/10-harden-back.png" alt="restored SSH hardening (keys-only, LogLevel INFO)" /></p>
</details>

## Release
- **v0.1.0** — first public release: [download (PDF/MD/CSV)](https://github.com/Mohaned87/failed-login-reports/releases/tag/v0.1.0)
