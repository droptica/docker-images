FROM droptica/drupal-dev

RUN curl -L -o /usr/bin/codecept http://codeception.com/codecept.phar \
 && chmod +x /usr/bin/codecept

RUN mkdir /root/composer_codecept

ADD ./composer.json /root/composer_codecept/composer.json

RUN composer global update -d /root/composer_codecept/

ENV PATH "/root/composer_codecept/vendor/bin:$PATH"