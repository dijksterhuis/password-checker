import requests, redis
from sys import stdout

r_p_checker = redis.Redis(host='0.0.0.0',port='6379')
added = 0
with open('data/file.txt') as f:
	for idx, line in enumerate(f.readlines()):
		added += r_p_checker.lpush(index,str(line.rstrip('\n')))
		console.write('\r + {} proc - {} add +'.format(idx, added) )
		console.flush()
