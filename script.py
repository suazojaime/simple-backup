#import sqlite3
import yaml
#import pandas as pd
import subprocess
from datetime import datetime

#import os
#print("📂 Current working directory:", os.getcwd())
#print("📄 Files in current dir:", os.listdir("."))

timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
datetime_hr = datetime.now()
print(f'''=== Starting script at  {datetime_hr} ===''')

with open("/app/assets.yml") as stream:
    try:
        #print(yaml.safe_load(stream))
        conf_yml = yaml.safe_load(stream)
        #df = pd.DataFrame.from_dict(conf_yml, orient='index').reset_index()
        #df = df.rename(columns={'index': 'asset'})
    except yaml.YAMLError as exc:
        print(exc)


# update cronjob
move_cronjob = 'cp /app/cronjob /etc/cron.d/monitor-cron && crontab /etc/cron.d/monitor-cron reload'
subprocess.run(move_cronjob, shell=True)
print('updated cronjob')

#conn = sqlite3.connect("simplebackup.db")
#df.to_sql(name='folder_config', con=conn, if_exists='replace', index=False)
#conn.close()

assets = conf_yml.keys()

for n in assets:
    print(n)
    conf_yml[n]
    source_path = conf_yml[n]['source_path']
    destination_path = conf_yml[n]['destination_path']
    lockfile = f'''/tmp/{n}_rsync_backup.lock'''
    command = f'''flock -n {lockfile} bash -c 'nohup rsync -avhc --delete  {source_path} {destination_path} > /app/logs/{n}_{timestamp}.log 2>&1 &' '''
    print(command)
    try:
        result = subprocess.run(command, shell=True)
        if result.returncode != 0:
            print("🔒 Lock is already held — another rsync is running.")
        else:
            print("✅ rsync started.")
    except subprocess.CalledProcessError as e:
        print(f"❌ rsync failed for: {e}")

# Delete log files older than 1 days
cmd = 'find /app/logs/ -name "*.log" -type f -mtime +1 -exec rm {} \;'
subprocess.run(cmd, shell=True)