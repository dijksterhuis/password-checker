docker rm -f pwchecker-flaskapi

docker run \
    -d \
    --restart=always \
    -v api-logs:/logs/ \
    --network pw-checker-api \
    --name pwchecker-flaskapi \
    -p 127.0.0.1:100:80 \
        pwchecker:flask-api /bin/ash -c 'python /home/api.py'