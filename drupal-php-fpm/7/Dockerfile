FROM php:7-fpm

RUN apt-get update && apt-get install -y \
  libfreetype6-dev \
  libjpeg62-turbo-dev \
  libmcrypt-dev \
  libpng12-dev \
  && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
  && docker-php-ext-install -j$(nproc) gd
  && docker-php-ext-install pdo pdo_mysql mbstring \
  && docker-php-ext-enable opcache

RUN apt-get install -y \
  pkg-config libmagickwand-dev imagemagick \
  && curl -L -o /tmp/imagick.tgz http://pecl.php.net/get/imagick-3.4.1.tgz \
  && tar xfz /tmp/imagick.tgz \
  && rm -r /tmp/imagick.tgz \
  && mv imagick-3.4.1 /usr/src/php/ext/imagick \
  && docker-php-ext-install imagick