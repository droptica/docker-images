FROM composer/composer:php7

RUN apt-get update &&  apt-get -y install cron rsyslog

RUN composer global require drush/drush:dev-master

ENV PATH "/root/composer/vendor/bin:$PATH"

RUN ln -sf /dev/stdout /var/log/cron.log \
	&& ln -sf /dev/stderr /var/log/syslog


RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENTRYPOINT []

ADD ./run-cron.sh /run-cron.sh

RUN chmod +x /run-cron.sh

CMD ["/run-cron.sh"]
