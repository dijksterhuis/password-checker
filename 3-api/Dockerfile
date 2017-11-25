FROM python:alpine
RUN apk update
RUN mkdir /logs/

WORKDIR /home/
RUN pip install --upgrade flask flask-restful flask-httpauth redis
COPY *.py /home/
RUN chmod u+x /home/*.py