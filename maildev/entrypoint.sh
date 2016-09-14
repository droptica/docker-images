#!/usr/bin/env bash

CMD="maildev -w 80"

if [ "$WEB_USER" ] && [ "$WEB_PASS" ]; then
  CMD="$CMD --web-user $WEB_USER --web-pass $WEB_PASS"
fi

exec $CMD