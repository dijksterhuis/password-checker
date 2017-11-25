FROM python:alpine
WORKDIR /home
RUN apk update
RUN pip install --upgrade flask flask-api flask-httpauth
COPY *.py /home/
RUN chmod u+x /home/*.py
