FROM node

RUN npm install -g maildev

# smtp port
EXPOSE 1025

# webserver port
EXPOSE 80

CMD ["maildev",  "-w", "80"]