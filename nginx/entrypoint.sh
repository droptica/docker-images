#!/usr/bin/env bash

if [ "$WEB_USER" ] && [ "$WEB_PASS" ]; then
    printf "${WEB_USER}:`openssl passwd -apr1 $WEB_PASS`\n" >> /etc/nginx/.htpasswd
    cp /etc/nginx/passwd.conf /etc/nginx/conf.d/passwd.conf
fi

exec nginx -g "daemon off;"