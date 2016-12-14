FROM droptica/drupal-apache:7-xdebug

RUN apt-get -y install unzip

RUN curl -L -o xhprof.zip https://github.com/RustJason/xhprof/archive/php7.zip \
    && unzip xhprof.zip \
    && rm xhprof.zip \
    && mv xhprof-php7 /opt/ \
    && cd /opt/xhprof-php7/extension \
    && phpize \
    && ./configure --enable-xhprof \
    && make \
    && make install

ADD xhprof.ini /usr/local/etc/php/conf.d/xhprof.ini
