FROM php:7-fpm

RUN apt-get update && apt-get install -y \
        libjpeg62-turbo-dev \
        libpng12-dev \
  && docker-php-ext-install pdo pdo_mysql gd \
  && docker-php-ext-enable opcache

