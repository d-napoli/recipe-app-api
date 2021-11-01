FROM python:3.7-alpine
LABEL maintainer="Diego Napoli"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# POR SEGURANCA
# FAZER A APLICACAO RODAR COM O USUARIO 'USER'
RUN adduser -D user
USER user