from flask import Flask, request, abort
from flask_restplus import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
todos = {'t1': 'some secret task'}

parser = reqparse.RequestParser()
parser.add_argument('Authorization', type=str, location='headers')

@api.route('/todo/<string:todo_id>')
class TodoSimple(Resource):
	@api.header('Authorization', 'Basic {cred}')
	def get(self, todo_id):
		auth = parser.parse_args()['Authorization']
		if auth == 'Basic super secret':
			return {todo_id: todos[todo_id]}
		else:
			abort(403)

app.run(debug=True)

"""
http GET "http://localhost:5000/todos/t1"

http://flask-restplus.readthedocs.io/en/stable/parsing.html
"""
