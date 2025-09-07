FROM python:3.11-slim

# Install rsync and cron
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    rsync cron && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy Python script and requirements
COPY *.py requirements.txt fstab /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create log file
RUN touch /var/log/cron.log

# Copy cronjob file and install it
COPY cronjob /etc/cron.d/monitor-cron
RUN chmod 0644 /etc/cron.d/monitor-cron && \
    crontab /etc/cron.d/monitor-cron

# Start cron and keep container running
CMD cron && tail -f /var/log/cron.log
