FROM composer/composer:php7

RUN apt-get update &&  apt-get -y install cron rsyslog

RUN composer global require drush/drush:dev-master

ENV PATH "/root/composer/vendor/bin:$PATH"

RUN ln -sf /dev/stdout /var/log/cron.log

RUN docker-php-ext-install pdo_mysql \
      && docker-php-ext-enable opcache

RUN echo "cron.*                         /var/log/cron.log" >> /etc/rsyslog.d/cron.conf

RUN echo "* *     * * *   root  echo \"Current container's time:\"\$(date +\"%Y-%m-%d %H:%M\")" >> /etc/crontab
RUN echo "* *     * * *   root    crontab /etc/crontab" >> /etc/crontab



RUN crontab /etc/crontab

RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENTRYPOINT []

CMD ["/usr/sbin/cron" ,"-f" , "-L15"]
