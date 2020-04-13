FROM python:3.7.6-alpine3.11

RUN apk add --update\
    alpine-sdk \
    python-dev \
    py-setuptools \
    && rm -rf /var/cache/apk/*

ENV HOME=/home/vector

# project dependencies
COPY requirements.txt $HOME/requirements.txt