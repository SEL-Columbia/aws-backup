#!/bin/bash

LOGFILE=/home/ubuntu/backup/backup.log
PROJECT_ENV=/home/ubuntu/srv/formhub-ec2/project_env/bin/activate
BACKUP_SCRIPT=/home/ubuntu/backup/backup_volume.py

touch $LOGFILE
echo "Running $BACKUP_SCRIPT" >> $LOGFILE
date >> $LOGFILE
source $PROJECT_ENV
python $BACKUP_SCRIPT >> $LOGFILE 2>&1
date >> $LOGFILE
echo "Finished $BACKUP_SCRIPT" >> $LOGFILE
