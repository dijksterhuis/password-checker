FROM python:alpine
#RUN apk update ; apk add wget
RUN pip install redis requests
WORKDIR /home
COPY redis_load.py /home
#RUN wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/10_million_password_list_top_1000000.txt
RUN chmod u+x /home/redis_load.py
EXPOSE 6379
