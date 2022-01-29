FROM python:3.10-alpine
WORKDIR /usr/src/N5/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/N5
RUN pip install -r requirements.txt

FROM node:10.9
WORKDIR /usr/src/N5/
RUN npm install -g less
RUN lessc global/static/modules/less/main.less global/static/modules/less/dist/main.css 
