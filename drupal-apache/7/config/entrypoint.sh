#!/usr/bin/env bash


if [ "$WEB_USER" ] && [ "$WEB_PASS" ]; then
    printf "${WEB_USER}:`openssl passwd -apr1 $WEB_PASS`\n" >> /etc/apache2/.htpasswd
    a2enconf htpasswd.conf
fi

sed -i "s#{DOCUMENT_ROOT}#`echo $DOCUMENT_ROOT`#g" /etc/apache2/sites-available/000-default.conf
sed -i "s#{DOCUMENT_ROOT}#`echo $DOCUMENT_ROOT`#g" /etc/apache2/sites-available/default-ssl.conf

exec apache2-foreground