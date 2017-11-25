FROM python:alpine
RUN pip install redis
COPY redis_load.py /home
RUN chmod u+x /home/redis_load.py
EXPOSE 6379
