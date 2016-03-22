#!/bin/sh

crontab /etc/crontab
/usr/sbin/cron -f -l -L 15