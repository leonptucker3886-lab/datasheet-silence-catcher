# Silence Catcher — HOWTO

## Roster format (`roster.json`)
A JSON list; one entry per member with their last post time (ISO 8601, UTC):
```json
[{"name": "MAJ datasheet", "last_post": "2026-10-31T11:10:00Z"}]
```
Update `last_post` whenever a member posts (by hand for now; chat hookup is not built yet).

## Run
```
python3 silence_catcher.py roster.json              # default limit 60 min
python3 silence_catcher.py roster.json --minutes 30 # custom limit
```
- Exit 0: everyone active. Exit 1: someone SILENT, plus an `ESCALATE:` line.
- The hourly GitHub Action (`.github/workflows/silence-catcher.yml`) runs this on `roster.json` and fails on exit 1.

## First test run (2026-10-31 ~11:11 UTC)
Default 60 min:
```
ok      MAJ datasheet             last post 0 min ago
ok      Sgt MILES dAvis           last post 0 min ago
ok      Cpl Juan I Ezekiel        last post 9 min ago
All members active.      (exit 0)
```
With `--minutes 5` (proves the flag path):
```
ok      MAJ datasheet             last post 0 min ago
ok      Sgt MILES dAvis           last post 0 min ago
SILENT  Cpl Juan I Ezekiel        last post 9 min ago
ESCALATE: Cpl Juan I Ezekiel     (exit 1)
```
Note: the sample roster timestamps are static, so scheduled runs will flag everyone once they age past the limit until the roster is updated.
