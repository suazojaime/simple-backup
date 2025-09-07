# SimpleBackup – Automated Rsync Backup with Docker & Cron

## SimpleBackup is a lightweight, Dockerized Python-based backup utility that automates directory syncing using rsync. It reads backup jobs from a YAML config file and executes them on a schedule using cron, supporting options like:

🔁 Periodic syncing of NAS or mounted folders

✅ Optional integrity checks with rsync --checksum

🔒 Locking to prevent concurrent runs (flock)

📁 Automatic folder creation

📝 Log rotation and per-job logging

🔧 Technologies

Python 3

Docker / Docker Compose

Cron

rsync

YAML config