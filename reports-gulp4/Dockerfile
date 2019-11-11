FROM node:alpine
RUN mkdir -p /var/www/html/theme
RUN touch /var/www/html/theme/gulpfile.js
COPY droopler-gulp/config/package.json /var/www/html/theme/package.json
RUN npm install -g gulp@^4.0.2
RUN cd /var/www/html/themes/custom/theme && npm install && npm link gulp
EXPOSE 80
