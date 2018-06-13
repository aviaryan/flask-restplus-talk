from flask import Flask, request
from flask_restplus import Resource, Api, reqparse
from pagination import get_paginated_list

app = Flask(__name__)
api = Api(app)
todos = [{'id': 't1', 'task': 'some task'},
	{'id': 't2', 'task': 'another task'},
	{'id': 't3', 'task': 'yet another task'}]
parser = reqparse.RequestParser()
parser.add_argument('start', type=int, default=1)
parser.add_argument('limit', type=int, default=2)

@api.route('/todos')
class TodoList(Resource):
	def get(self):
		args = parser.parse_args()
		return get_paginated_list(todos, args=args)

app.run(debug=True)

"""
http GET http://localhost:5000/todos?start=1

https://aviaryan.in/blog/gsoc/paginated-apis-flask.html
"""
