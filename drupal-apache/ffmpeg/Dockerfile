FROM droptica/drupal-apache

RUN echo 'deb http://httpredir.debian.org/debian jessie main contrib non-free' > /etc/apt/sources.list
RUN echo 'deb-src http://httpredir.debian.org/debian jessie main contrib non-free' >> /etc/apt/sources.list

RUN echo 'deb http://httpredir.debian.org/debian jessie-updates main contrib non-free' >> /etc/apt/sources.list
RUN echo 'deb-src http://httpredir.debian.org/debian jessie-updates main contrib non-free' >> /etc/apt/sources.list

RUN echo 'deb http://security.debian.org/ jessie/updates main contrib non-free' >> /etc/apt/sources.list
RUN echo 'deb-src http://security.debian.org/ jessie/updates main contrib non-free' >> /etc/apt/sources.list

RUN echo 'deb http://ftp.debian.org/debian jessie-backports main' >> /etc/apt/sources.list

RUN a2enmod headers
RUN apt-get update && apt-get install -y libmemcached-dev
RUN echo "no" | pecl install memcached
RUN docker-php-ext-enable memcached

RUN apt-get -t jessie-backports install -y ffmpeg

RUN ln -s /usr/bin/ffmpeg /usr/local/bin/ffmpeg

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


ADD config/entrypoint.sh /bin/entrypoint.sh

RUN chmod 777 /bin/entrypoint.sh

ADD config/htpasswd.conf /etc/apache2/conf-available/htpasswd.conf

ADD config/000-default.conf /etc/apache2/sites-available/000-default.conf
ADD config/default-ssl.conf /etc/apache2/sites-available/default-ssl.conf

ENV DOCUMENT_ROOT /var/www/html

CMD entrypoint.sh