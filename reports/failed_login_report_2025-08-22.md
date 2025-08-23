# Failed Login Incidents Report — 2025-08-22

- Total failed password attempts: **33**
- Invalid-user attempts: **15**

## Top IPs
- 127.0.0.1: 33

## Most targeted usernames
- kali: 18
- usernotexists: 15

## Peak hours (hour → count)
- 10:00 → 8
- 12:00 → 18
- 13:00 → 7

## Log samples
- `Aug 22 10:24:57 kali sshd-session[37139]: Failed password for invalid user usernotexists from 127.0.0.1 port 38194 ssh2`
- `Aug 22 10:24:59 kali sshd-session[37167]: Failed password for invalid user usernotexists from 127.0.0.1 port 40484 ssh2`
- `Aug 22 10:25:02 kali sshd-session[37187]: Failed password for invalid user usernotexists from 127.0.0.1 port 40488 ssh2`
- `Aug 22 10:25:05 kali sshd-session[37219]: Failed password for invalid user usernotexists from 127.0.0.1 port 40500 ssh2`
- `Aug 22 10:25:09 kali sshd-session[37247]: Failed password for invalid user usernotexists from 127.0.0.1 port 40502 ssh2`

## Quick recommendations
- Enable Fail2ban; prefer SSH keys over passwords; restrict access via UFW; disable unused accounts.
