FROM droptica/drupal-apache

RUN curl -L -o /tmp/xdebug.tgz http://xdebug.org/files/xdebug-2.4.0rc3.tgz \
        && tar xfz /tmp/xdebug.tgz \
        && rm -r /tmp/xdebug.tgz \
        && mv xdebug-2.4.0RC3 /usr/src/php/ext/xdebug \
        && docker-php-ext-install xdebug

