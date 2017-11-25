name=redis-pw

docker rm -f $name || true
docker run -d -p 6379:6379 -v redis-pw:/data --name $name --network redis-pw redis:alpine redisserver --appendonly yes
