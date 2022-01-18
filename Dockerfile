FROM python:3.10-alpine
WORKDIR /usr/src/N5/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/N5
RUN pip install -r requirements.txt
COPY ./N5 /usr/src/N5

EXPOSE 0734
CMD ["python", "manage.py", "runserver", "0.0.0.0:0734"]
