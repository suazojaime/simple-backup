# Simple Backup

A simple backup solution using rsync for efficiently backing up directories. This script is designed to be run on a schedule (via cron or other schedulers) to automate backups from a source to a destination folder. It supports running in a Docker container.

## Features

- Automated backups using rsync

- Periodic sync with a configurable frequency (in minutes)

- Error handling and logging

- Dockerized for easy deployment and setup

## Requirements

- Docker

- Python 3

- rsync (installed inside the Docker container)

- Access to networked file systems (via cifs or other mounts)

## Setup

1. Clone the repository

```bash
git clone https://github.com/suazojaime/simple-backup.git
cd simple-backup
```
2. Modify configuration

Update the assets.yml file with the source and destination directories, and specify the backup frequency.

Example of assets.yml:

```yml
foldertest:
  source_path: /mnt/nas_mount/cv/
  destination_path: /mnt/backup/test/
  frequency_minutes: 30

foldertest2:
  source_path: /mnt/nas_mount/landingpage/
  destination_path: /mnt/backup/landingpage/
  frequency_minutes: 30
```

3. Build and run with Docker

Build the Docker container:

```bash
docker compose build
```

Start the container:

```bash
docker compose up -d
```

4. Check logs

The script will log output to /app/logs/ inside the container. You can check the logs to monitor backup progress:

```bash
docker exec -it backup-service tail -f /app/logs/cron.log
```
Usage

This script can be run manually or scheduled using cron (inside or outside the container).

To run manually, use:

```bash
python3 /app/script.py
```

Alternatively, you can configure a cron job in the Docker container to run periodically.

License

This project is licensed under the MIT License - see the LICENSE
 file for details.