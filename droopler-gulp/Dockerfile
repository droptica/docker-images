FROM node:10.17.0-alpine
RUN mkdir -p /var/www/html/themes/custom/theme
RUN touch /var/www/html/themes/custom/theme/gulpfile.js
COPY droopler-gulp/config/package.json /var/www/html/themes/custom/theme/package.json
RUN npm install -g gulp@^3.9
RUN cd /var/www/html/themes/custom/theme && npm install && npm link gulp
EXPOSE 80
