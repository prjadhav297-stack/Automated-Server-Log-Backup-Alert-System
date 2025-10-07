#!/bin/bash
LOG_DIR="$HOME/automation_project/sample_logs"
mkdir -p $LOG_DIR
echo "Sample log entry" >> $LOG_DIR/app.log

BACKUP_DIR="$HOME/automation_project/backups"
TIMESTAMP=$(date +%F_%H-%M-%S)
BACKUP_FILE="$BACKUP_DIR/logs_$TIMESTAMP.tar.gz"

tar -czf $BACKUP_FILE $LOG_DIR

if [ $? -eq 0 ]; then
    echo "SUCCESS:$BACKUP_FILE"
else
    echo "FAIL:$BACKUP_FILE"
fi
