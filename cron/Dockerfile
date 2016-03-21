FROM composer/composer:php7

RUN apt-get update &&  apt-get -y install cron

RUN composer global require drush/drush:dev-master

ENV PATH "/root/composer/vendor/bin:$PATH"

RUN touch /var/log/cron.log
RUN touch /var/log/syslog

RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENTRYPOINT cron && tail -F /var/log/syslog /var/log/cron.log
