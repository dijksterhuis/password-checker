from flask import Flask, jsonify, request, make_response
from flask_httpauth import HTTPBasicAuth
from flask_restful import reqparse, abort, Resource, Api
import json, os, datetime, time, redis

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

#### TODO - authorisation

#@auth.get_password
#def get_password(username):
#    if username == 'miguel':
#        return 'python'
#    return None
#
#@auth.error_handler
#def unauthorized():
#    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

class alive(Resource):
	def get(self):
		return make_response(jsonify({'status': 'OK'}),200)

class query(Resource):
	def post(self):
		redis_db = redis.Redis(host='pwchecker-redis',port='6379')
		query = request.get_json()
		if 'password' not in query.keys() or 'filesize' not in query.keys():
			return make_response('mising json keys for request - need *password* and *filesize*',301)
		redis_result = redis_db.sismember(str(query['filesize']),str(query['password']))
		return make_response(str(redis_result),200)

api.add_resource(alive ,'/alive')
api.add_resource(query, '/query')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=80,debug=False)
