name=redis-pw

docker stop $name ; docker rm $name
docker run -d -p 6379:6379 -v redis-pw:/data --restart=always --name $name --network redis-pw redis:alpine redisserver --appendonly yes
