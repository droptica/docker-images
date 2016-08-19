FROM php:5.5-apache

RUN a2enmod rewrite && apt-get update && apt-get install -y \
  libfreetype6-dev \
  libjpeg62-turbo-dev \
  libmcrypt-dev \
  libpng12-dev \
  mcrypt \
  libmcrypt-dev \
  libjpeg-dev \
  && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
  && docker-php-ext-install -j$(nproc) gd pdo pdo_mysql mbstring iconv mcrypt zip\
  && docker-php-ext-enable opcache

RUN apt-get install -y \
  pkg-config libmagickwand-dev imagemagick \
  && curl -L -o /tmp/imagick.tgz http://pecl.php.net/get/imagick-3.4.2.tgz \
  && tar xfz /tmp/imagick.tgz \
  && rm -r /tmp/imagick.tgz \
  && mv imagick-3.4.2 /usr/src/php/ext/imagick \
  && docker-php-ext-install imagick
