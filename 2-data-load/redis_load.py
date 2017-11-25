#!/usr/bin/python
import requests, redis
from sys import stdout

r_p_checker = redis.Redis(host='redis-pw',port='6379')
added = 0
print(r_p_checker.ping())

filesizes = [100, 500, 1000, 10000, 100000, 1000000]
ghub_url = 'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/10_million_password_list_top_'

for size in filesizes:
	url = ghub_url + str(size) + '.txt'
	data = requests.get(url).text.split('\n')
	for idx, password in enumerate(data):
		added += r_p_checker.sadd(str(size),str(password.rstrip('\n')))
		if idx % (size / 10) == 0:
			stdout.write('\r + {} size - {} proc - {} add +'.format(size, idx, added) )
			stdout.flush()
print('\n +++ Load completed')
