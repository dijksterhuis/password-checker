name=redis-pw

docker rm -f $name || true
docker run -d --restart=always -p 6379:6379 -v redis-pw:/data --name $name redis:alpine redis-server --appendonly yes

docker network connect pw-checker-redis redis-pw
docker network connect api redis-pw