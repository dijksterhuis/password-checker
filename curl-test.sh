echo "\n+++++++++++++++ Testing for a TRUE value"
curl -i -H "Content-Type: application/json" -X POST -d '{"filesize":1000000,"password":"qwerty"}' -v http://127.0.0.1:100/query
echo "\n+++++++++++++++ Testing for a FALSE value"
curl -i -H "Content-Type: application/json" -X POST -d '{"filesize":1000000,"password":"lkasfgy92bhvlis83gf"}' -v http://127.0.0.1:100/query
echo "\n+++++++++++++++ Testing for WRONG data"
curl -i -H "Content-Type: application/json" -X POST -d '{"filesize":1000000,"pw":"lkasfgy92bhvlis83gf"}' -v http://127.0.0.1:100/query
