# Automated-Server-Log-Backup-Alert-System
Goal: Automatically back up server logs daily, store details in a MySQL database, and send an alert if something fails.

This project automates the backup of server logs, uploads them to AWS S3, and stores backup information in a MySQL database. 
It also allows sending alerts in case of failures. 

Built using: Linux, Bash, Python, MySQL, and AWS.

Features:
- Compress logs automatically with Bash
- Upload compressed logs to AWS S3 using Python
- Store backup details (filename, timestamp, status) in MySQL
- Optional: Send email alerts if backup fails
- Fully automated with cron (can simulate in WSL)

Workflow Diagram:
[Linux Logs] --> [Bash Compress] --> [Python Upload to S3] --> [MySQL Logging] --> [Email Alert]

Requirements:
- WSL (Ubuntu) or Linux system
- Python 3.x
- Bash
- MySQL Server
- AWS account with S3 access
- Python packages: boto3, mysql-connector-python

Setup & Installation:

1. Clone this repository.
2. Install Python packages.
3. Configure AWS and MySQL credentials in config.ini.
4. Create the MySQL table.
  
Usage:
1. Compress logs manually (for demo):
   ./backup_logs.sh

2. Upload to S3:
   python3 upload_s3.py /home/user/backups/logs_2025-10-07.tar.gz

3. Insert info into MySQL:
   python3 db_insert.py /home/user/backups/logs_2025-10-07.tar.gz SUCCESS

4. Optional: Automate daily with cron:
   0 2 * * * /home/user/server-log-backup-automation/backup_logs.sh | \
   while read line; do
       FILE=$(echo $line | cut -d':' -f2)
       STATUS=$(echo $line | cut -d':' -f1)
       python3 upload_s3.py $FILE
       python3 db_insert.py $FILE $STATUS
   done
