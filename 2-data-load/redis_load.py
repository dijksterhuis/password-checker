#!/usr/bin/python
import requests, redis
from sys import stdout

r_p_checker = redis.Redis(host='redis-pw',port='6379')
added = 0
with open('10_million_password_list_top_1000000.txt') as f:
	for idx, line in enumerate(f.readlines()):
		added += r_p_checker.sadd(index,str(line.rstrip('\n')))
		console.write('\r + {} proc - {} add +'.format(idx, added) )
		console.flush()
print('\n +++ Load completed')
