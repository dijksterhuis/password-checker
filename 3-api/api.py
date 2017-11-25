from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_restful import reqparse, abort, Resource, Api
import json, os, datetime, time

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

redis_db = redis.Redis(host='redis-pw',port='6379')
redis_db.ping()

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
		return {'status': 'OK'}

class query(Resource):
	@auth.login_required
	def post(self):
		query = request.get_json()
		if 'password' not in query.keys() or 'filesize' not in query.keys()
			return 'mising json keys for request - need *password* and *filesize*'
		redis_result = redis.sismember(str(query['filesize']),str(query['password']))
		return str(redis_result)

api.add_resource(am_i_alive ,'/alive')
api.add_resource(query, '/query')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=80,debug=True)