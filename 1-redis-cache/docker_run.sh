docker run -d -p 6379:6379 -v redis-pw:/data --restart=always --name redis-pw --network redis-pw redis:alpine redisserver --appendonly yes
