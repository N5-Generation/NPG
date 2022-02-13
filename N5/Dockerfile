FROM node:10.9 as build
WORKDIR /tmp
COPY ./global/static/modules/less/ /tmp/less/
RUN npm install -g less
RUN lessc /tmp/less/main.less /tmp/less/dist/main.css

FROM python:3.10-alpine
WORKDIR /usr/src/N5/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/N5
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow \
    && apk del build-deps
RUN pip install -r requirements.txt
COPY --from=build /tmp/less/dist/main.css /usr/src/N5/global/static/modules/less/dist