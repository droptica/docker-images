#!/bin/bash
docker build -t wodzik/drupal-dev .
docker push wodzik/drupal-dev
docker pull wodzik/drupal-dev

