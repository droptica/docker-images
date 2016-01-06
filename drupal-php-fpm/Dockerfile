FROM php:5-fpm


RUN apt-get update && apt-get install -y \
        libjpeg62-turbo-dev \
        libpng12-dev \
  && docker-php-ext-install pdo pdo_mysql gd mbstring\
  && docker-php-ext-enable opcache

