# syntax=docker/dockerfile:1

FROM python:3.12-alpine

WORKDIR /app

COPY service/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY service/ /app/service/
COPY library/ /app/library/
COPY application/ /app/application/
COPY helpers/ /app/helpers/

ENV PYTHONPATH=/app

ENV FLASK_APP=service/app.py

CMD ["flask", "run", "--host=0.0.0.0"]