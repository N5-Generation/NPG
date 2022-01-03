FROM python:3-alpine

RUN apk update && apk add -u \
    postgresql-dev \
    gcc \
    python3-dev \
    musl-dev

RUN pip3 install psycopg2

ENV PGSYSCONFDIR=/usr/etc/postgresql
ADD pg_service.conf /usr/etc/postgresql/pg_service.conf

WORKDIR /app
ADD db_test.py /app

CMD ["python3", "db_test.py"]