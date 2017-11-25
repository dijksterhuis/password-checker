docker run -i --rm --network pw-checker-redis --name pwchecker-redisload pw-checker:redis-data-load /bin/ash -c 'python /home/redis_load.py'
