### Create networks
docker network create redis-pw

### Stop and remove any running containers
docker stop redis-pw
docker rm redis-pw

### Bring containers up
docker run -d -p 6379:6379 -v redis-pw:/data --restart=always --name redis-pw --network redis-pw redis:alpine redisserver --appendonly yes
