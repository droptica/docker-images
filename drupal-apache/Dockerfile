FROM php:5-apache

RUN a2enmod rewrite && apt-get update && apt-get install --no-install-recommends -y \
  libfreetype6-dev \
  libjpeg62-turbo-dev \
  libmcrypt-dev \
  libpng12-dev \
  mcrypt \
  libmcrypt-dev \
  libjpeg-dev \
  pkg-config libmagickwand-dev imagemagick \
  zlib1g-dev libicu-dev g++ \
  && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
  && docker-php-ext-install -j$(nproc) gd pdo pdo_mysql mbstring iconv mcrypt zip bcmath intl exif fileinfo\
  && docker-php-ext-enable opcache

RUN curl -L -o /tmp/imagick.tgz http://pecl.php.net/get/imagick-3.4.2.tgz \
  && tar xfz /tmp/imagick.tgz -C /tmp \
  && docker-php-source extract \
  && rm -r /tmp/imagick.tgz \
  && mv /tmp/imagick-3.4.2 /usr/src/php/ext/imagick \
  && docker-php-ext-install imagick

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD config/entrypoint.sh /bin/entrypoint.sh

RUN chmod 777 /bin/entrypoint.sh

ADD config/htpasswd.conf /etc/apache2/conf-available/htpasswd.conf

ADD config/000-default.conf /etc/apache2/sites-available/000-default.conf
ADD config/default-ssl.conf /etc/apache2/sites-available/default-ssl.conf

ENV DOCUMENT_ROOT /var/www/html

CMD entrypoint.sh