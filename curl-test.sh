echo "------"
echo "+++++++++++++++ Testing for a TRUE value"
echo "------"

curl -i -H "Content-Type: application/json" -X POST -d '{"filesize":1000000,"password":"qwerty"}' -v http://127.0.0.1:100/query

echo "------"
echo "+++++++++++++++ Testing for a FALSE value"
echo "------"

curl -i -H "Content-Type: application/json" -X POST -d '{"filesize":1000000,"password":"lkasfgy92bhvlis83gf"}' -v http://127.0.0.1:100/query

echo "------"
echo "+++++++++++++++ Testing for wrong POST data"
echo "------"

curl -i -H "Content-Type: application/json" -X POST -d '{"filesize":1000000,"pw":"lkasfgy92bhvlis83gf"}' -v http://127.0.0.1:100/query
