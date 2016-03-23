FROM golang

RUN mkdir /jobs

RUN addgroup --gid 1000 jobber_client
RUN useradd -u 1000 -g jobber_client --home /jobs jobber_client


RUN go get github.com/dshearer/jobber \
 && cd src/github.com/dshearer/jobber \
 && git checkout v1.0.3 \
 && make

WORKDIR /jobs

#ADD reload.jobber /root/.jobber

CMD ["jobberd"]