#!/usr/bin/env bash


if [ "$WEB_USER" ] && [ "$WEB_PASS" ]; then
    printf "${WEB_USER}:`openssl passwd -apr1 $WEB_PASS`\n" >> /etc/apache2/.htpasswd
    a2enconf htpasswd.conf
fi

exec apache2-foreground