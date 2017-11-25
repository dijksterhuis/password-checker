#!/usr/bin/python
import requests, redis
from sys import stdout

r_p_checker = redis.Redis(host='redis-pw',port='6379')
added = 0
with open('10_million_password_list_top_1000000.txt') as f:
	for idx, line in enumerate(f.readlines()):
		added += r_p_checker.sadd('1000000',str(line.rstrip('\n')))
		stdout.write('\r + {} proc - {} add +'.format(idx, added) )
		stdout.flush()
print('\n +++ Load completed')
