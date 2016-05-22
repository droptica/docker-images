FROM droptica/symfony-dev

RUN apt-get update && apt-get install -y --no-install-recommends python python-yaml python-setuptools pkg-config

RUN easy_install python-dotenv

RUN php -r "readfile('http://files.drush.org/drush.phar');" > /usr/bin/drush \
    && chmod +x /usr/bin/drush \
    && drush init -y

RUN curl http://drupalconsole.com/installer -L -o /usr/local/bin/drupal-console \
  && chmod +x /usr/local/bin/drupal-console

RUN curl -L -o /usr/bin/codecept http://codeception.com/codecept.phar \
 && chmod +x /usr/bin/codecept

RUN cd /root && git clone git@github.com:droptica/docker-drupal.git \
    && cd docker-drupal && python setup.py install && cd .. && rm -Rf docker-drupal

#RUN drush -y dl registry_rebuild-7.x

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENTRYPOINT []

CMD ["bash"]
