FROM php:5-apache

RUN a2enmod rewrite && apt-get update && apt-get install -y \
  libjpeg62-turbo-dev \
  libpng12-dev \
  && docker-php-ext-install pdo pdo_mysql gd mbstring \
  && docker-php-ext-enable opcache

RUN apt-get install -y \
  pkg-config libmagickwand-dev imagemagick \
  && curl -L -o /tmp/imagick.tgz http://pecl.php.net/get/imagick-3.4.1.tgz \
  && tar xfz /tmp/imagick.tgz \
  && rm -r /tmp/imagick.tgz \
  && mv imagick-3.4.1 /usr/src/php/ext/imagick \
  && docker-php-ext-install imagick