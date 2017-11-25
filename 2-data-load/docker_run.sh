docker run -i --rm --network pw-checker-redis --name pw-checker_redis-load pw-checker:redis-data-load /bin/ash -c 'python /home/redis_load.py'
