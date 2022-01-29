FROM node:10.9 as build
WORKDIR /tmp
COPY global/static/modules/less/ /tmp/less/
RUN npm install -g less
RUN lessc /tmp/less/main.less /tmp/less/dist/main.css

FROM python:3.10-alpine
WORKDIR /usr/src/N5/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/N5
RUN pip install -r requirements.txt
COPY --from=build /tmp/build global/static/modules/less/dist/
