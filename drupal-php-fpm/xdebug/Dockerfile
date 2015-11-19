FROM php:fpm

RUN apt-get update && apt-get install -y \
        libjpeg62-turbo-dev \
        libpng12-dev \
  && pecl install xdebug \
  && docker-php-ext-install pdo pdo_mysql gd \
  && docker-php-ext-enable opcache xdebug

