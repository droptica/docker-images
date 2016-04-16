FROM droptica/drupal-php-fpm

RUN curl -L -o /tmp/xdebug.tgz http://xdebug.org/files/xdebug-2.4.0.tgz \
        && tar xfz /tmp/xdebug.tgz \
        && rm -r /tmp/xdebug.tgz \
        && mv xdebug-2.4.0 /usr/src/php/ext/xdebug \
        && docker-php-ext-install xdebug

